"""
Copyright (c) Cutleast
"""

import logging
import shutil
import tempfile
from pathlib import Path
from typing import Any, Optional

from bethkit import StringFileKind, StringTable
from curl_cffi import requests as curl_requests
from cutleast_core_lib.core.archive_legacy.archive import Archive
from sse_bsa import BSAArchive

from core.file_source.file_source_factory import FileSourceFactory
from core.file_types.plugin.file import PluginFile
from core.file_types.plugin.string import PluginString
from core.string.string_loader import StringLoader
from core.string.string_status import StringStatus
from core.string.types import StringList

_TABLE_KINDS: dict[str, StringFileKind] = {
    ".strings": StringFileKind.STRINGS,
    ".dlstrings": StringFileKind.DL_STRINGS,
    ".ilstrings": StringFileKind.IL_STRINGS,
}
_PLUGIN_SUFFIXES: set[str] = {".esp", ".esm", ".esl"}
_BRIDGE_ERRORS: tuple[type[Exception], ...] = (
    OSError,
    ValueError,
    RuntimeError,
    LookupError,
)


class TranslationBridge:
    """
    Build and apply a cross-version translation bridge from matching plugin archives.
    """

    log: logging.Logger = logging.getLogger("TranslationBridge")
    __temp_dirs: list[tempfile.TemporaryDirectory[str]] = []

    @staticmethod
    def download_archive(url: str, destination: Path) -> None:
        """
        Download an archive using a browser-impersonating HTTP client, reusing an
        existing file when its byte size matches `Content-Length`.

        Args:
            url (str): Direct download URL.
            destination (Path): Target file path on disk.
        """

        destination.parent.mkdir(parents=True, exist_ok=True)
        response = curl_requests.get(
            url, impersonate="chrome", stream=True, timeout=60
        )
        try:
            response.raise_for_status()
            total_size = int(response.headers.get("Content-Length", "0") or "0")
            if (
                destination.is_file()
                and total_size > 0
                and destination.stat().st_size == total_size
            ):
                return
            with destination.open("wb") as output:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        output.write(chunk)
        finally:
            response.close()

    @staticmethod
    def select_nexus_original_file(
        files: list[Any],
        version: str,
        modfile_paths: list[Path],
        installed_mod: Any = None,
    ) -> Any:
        """
        Select the best matching Nexus original file for a translation version and
        plugin set.

        Args:
            files (list[Any]): Nexus `NmFile` candidates.
            version (str): Translation version string (may be empty).
            modfile_paths (list[Path]): Target plugin paths being translated.
            installed_mod (Any): Optional installed `Mod` metadata.

        Returns:
            Any: Best matching `NmFile`.
        """

        target_version = version.lower().removeprefix("v").strip()
        matching_files = (
            [
                file
                for file in files
                if file.version.lower().removeprefix("v").strip() == target_version
                or file.mod_version.lower().removeprefix("v").strip()
                == target_version
            ]
            if target_version
            else []
        )
        if not matching_files:
            matching_files = list(files)

        installed_file_id = (
            installed_mod.mod_id.file_id
            if installed_mod is not None and installed_mod.mod_id is not None
            else None
        )
        if installed_file_id is not None:
            exact = next(
                (f for f in matching_files if f.file_id == installed_file_id),
                None,
            )
            if exact is not None:
                return exact

        patch_words = ("patch", "fix", "hotfix", "update", "addon", "compat")
        has_main_plugin = any(
            path.suffix.lower() in (".esm", ".esp")
            and not any(w in path.stem.lower() for w in patch_words)
            for path in modfile_paths
        )

        def score_candidate(file: Any) -> tuple[int, int]:
            combined = f"{file.name} {file.file_name}".lower()
            score = 0
            for path in modfile_paths:
                stem = path.stem.lower()
                if stem in combined:
                    score += 20
                if "heartland" in stem and "bruma" in combined:
                    score += 18
                if "assets" in stem and "assets" in combined:
                    score += 15
            if installed_mod is not None:
                words = [
                    w
                    for w in installed_mod.name.lower()
                    .replace("-", " ")
                    .replace("_", " ")
                    .split()
                    if len(w) > 3
                ]
                for word in words:
                    if word in combined:
                        score += 5
            is_patch = any(w in combined for w in patch_words)
            if is_patch and has_main_plugin:
                score -= 30
            elif is_patch and not has_main_plugin:
                score += 15
            if file.is_primary or (file.category_name or "").upper() == "MAIN":
                score += 10
            return (score, file.size or 0)

        return max(matching_files, key=score_candidate)

    @staticmethod
    def extract_localized_plugin_strings(
        plugin_path: Path,
        language: str = "english",
    ) -> StringList:
        """
        Extract strings from a localized plugin using its external string tables
        (loose or inside BSA archives in the same mod folder).

        Args:
            plugin_path (Path): Path to the localized plugin file.
            language (str): Language suffix to load from string tables.

        Returns:
            StringList: Populated `PluginString` entries.
        """

        plugin = PluginFile(name=plugin_path.name, full_path=plugin_path)
        ext_ids = plugin.extract_external_string_ids()
        if not ext_ids:
            return []
        tables = TranslationBridge.__load_string_tables(
            plugin_path.parent, language, plugin_path.stem, set(ext_ids)
        )
        result: StringList = []
        for table_id, refs in ext_ids.items():
            text = tables.get(table_id)
            if not text:
                continue
            cleaned = TranslationBridge.__normalize(text)
            for ref in refs:
                ref.original = cleaned
                result.append(ref)
        return result

    @classmethod
    def clean_temp_dirs(cls) -> None:
        """Remove temporary folders created while building translation bridges."""

        while cls.__temp_dirs:
            temp_dir = cls.__temp_dirs.pop()
            try:
                temp_dir.cleanup()
            except OSError as ex:
                cls.log.warning(
                    "Failed to clean translation bridge temp folder '%s': %s",
                    temp_dir.name,
                    ex,
                )

        for temp_dir in Path(tempfile.gettempdir()).glob("sse_bridge_*"):
            if not temp_dir.is_dir():
                continue
            try:
                shutil.rmtree(temp_dir)
            except OSError as ex:
                cls.log.warning(
                    "Failed to clean translation bridge temp folder '%s': %s",
                    temp_dir,
                    ex,
                )

    @classmethod
    def find_plugins_in_source(
        cls, source_path: Path, temp_dir: Path
    ) -> dict[str, Path]:
        """
        Extract or locate all plugin files in a plugin, folder, or archive.

        Args:
            source_path (Path): Path to the source plugin, folder, or archive.
            temp_dir (Path): Destination folder for extracted files.

        Returns:
            dict[str, Path]: Mapping of lowered plugin filenames to paths.
        """

        plugins: dict[str, Path] = {}
        if source_path.is_file():
            suffix = source_path.suffix.lower()
            if suffix in _PLUGIN_SUFFIXES:
                plugins[source_path.name.lower()] = source_path
            elif suffix in {".7z", ".zip", ".rar"}:
                try:
                    archive = Archive.load_archive(source_path)
                    wanted = [
                        file_name
                        for file_name in archive.get_files()
                        if (
                            Path(file_name).suffix.lower() in _PLUGIN_SUFFIXES
                            or Path(file_name).suffix.lower() in _TABLE_KINDS
                            or (
                                Path(file_name).suffix.lower() == ".json"
                                and "dynamicstringdistributor"
                                in file_name.replace("\\", "/").lower()
                            )
                            or (
                                Path(file_name).suffix.lower() == ".bsa"
                                and "texture" not in Path(file_name).stem.lower()
                            )
                        )
                    ]
                    if wanted:
                        dest = temp_dir / source_path.stem
                        dest.mkdir(parents=True, exist_ok=True)
                        archive.extract_files(wanted, dest)
                        for path in dest.rglob("*"):
                            if path.is_file() and path.suffix.lower() in _PLUGIN_SUFFIXES:
                                plugins[path.name.lower()] = path
                except _BRIDGE_ERRORS as ex:
                    cls.log.warning(
                        "Failed to extract plugins from archive '%s': %s",
                        source_path,
                        ex,
                    )
        elif source_path.is_dir():
            for path in source_path.rglob("*"):
                if path.is_file() and path.suffix.lower() in _PLUGIN_SUFFIXES:
                    plugins[path.name.lower()] = path

        return plugins

    @classmethod
    def build_bridge(
        cls,
        translated_source: Path,
        original_source: Optional[Path] = None,
        language: str = "french",
        target_plugin_names: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """
        Build multi-level translation mappings between matching original and translated
        sources of the same mod version (or directly from DSD JSON files).

        Args:
            translated_source (Path): Path to translated archive, folder, plugin, or DSD.
            original_source (Optional[Path]):
                Path to matching original archive, folder, or plugin.
            language (str): Language suffix for external string tables.
            target_plugin_names (Optional[list[str]]):
                Optional plugin filenames to restrict extraction to.

        Returns:
            dict[str, Any]: Bridge dictionary containing lookup maps and statistics.
        """

        with tempfile.TemporaryDirectory(prefix="sse_bridge_") as temp_name:
            temp_dir = Path(temp_name)
            trans_root = temp_dir / "trans"
            orig_root = temp_dir / "orig"
            trans_plugins = cls.find_plugins_in_source(translated_source, trans_root)
            orig_plugins = (
                cls.find_plugins_in_source(original_source, orig_root)
                if original_source is not None
                else {}
            )
            trans_table_root = (
                translated_source if translated_source.is_dir() else trans_root
            )
            orig_table_root = (
                original_source
                if original_source is not None and original_source.is_dir()
                else orig_root
            )

            cls.log.info(
                "Building bridge: found %s translated plugin(s) and %s original plugin(s).",
                len(trans_plugins),
                len(orig_plugins),
            )

            text_map: dict[str, str] = {}
            edid_map: dict[tuple[str, str], str] = {}
            edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]] = {}
            formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]] = {}
            identical_edid_map: dict[tuple[str, str], tuple[str, str]] = {}
            identical_edid_indexed_map: dict[
                tuple[str, str, Optional[int]], tuple[str, str]
            ] = {}

            common_names = set(trans_plugins.keys()) & set(orig_plugins.keys())
            table_only_names = set(orig_plugins.keys()) - set(trans_plugins.keys())
            if target_plugin_names:
                target_lowers = {name.lower() for name in target_plugin_names}
                filtered_common = {
                    name for name in common_names if name in target_lowers
                }
                filtered_table_only = {
                    name for name in table_only_names if name in target_lowers
                }
                if filtered_common or filtered_table_only:
                    common_names = filtered_common
                    table_only_names = filtered_table_only

            pair_count = 0
            identical_count = 0
            for name in common_names:
                t_path = trans_plugins[name]
                o_path = orig_plugins[name]
                try:
                    t_plugin = PluginFile(name=t_path.name, full_path=t_path)
                    o_plugin = PluginFile(name=o_path.name, full_path=o_path)
                    trans_strings = t_plugin.get_strings()
                    orig_strings = o_plugin.get_strings()
                except _BRIDGE_ERRORS as ex:
                    cls.log.warning("Failed to read strings for '%s': %s", name, ex)
                    continue

                counts = cls.__collect_plugin_pairs(
                    orig_strings=orig_strings,
                    trans_strings=trans_strings,
                    text_map=text_map,
                    edid_map=edid_map,
                    edid_indexed_map=edid_indexed_map,
                    formid_map=formid_map,
                    identical_edid_map=identical_edid_map,
                    identical_edid_indexed_map=identical_edid_indexed_map,
                )
                pair_count += counts[0]
                identical_count += counts[1]

                ext_counts = cls.__collect_external_table_pairs(
                    o_plugin=o_plugin,
                    t_plugin=t_plugin,
                    orig_table_root=orig_table_root,
                    trans_table_root=trans_table_root,
                    plugin_stem=Path(name).stem,
                    language=language,
                    text_map=text_map,
                    edid_map=edid_map,
                    edid_indexed_map=edid_indexed_map,
                    formid_map=formid_map,
                    identical_edid_map=identical_edid_map,
                    identical_edid_indexed_map=identical_edid_indexed_map,
                )
                pair_count += ext_counts[0]
                identical_count += ext_counts[1]

            for name in table_only_names:
                o_path = orig_plugins[name]
                try:
                    o_plugin = PluginFile(name=o_path.name, full_path=o_path)
                except _BRIDGE_ERRORS as ex:
                    cls.log.warning("Failed to read plugin '%s': %s", name, ex)
                    continue

                ext_counts = cls.__collect_external_table_pairs(
                    o_plugin=o_plugin,
                    t_plugin=o_plugin,
                    orig_table_root=orig_table_root,
                    trans_table_root=trans_table_root,
                    plugin_stem=Path(name).stem,
                    language=language,
                    text_map=text_map,
                    edid_map=edid_map,
                    edid_indexed_map=edid_indexed_map,
                    formid_map=formid_map,
                    identical_edid_map=identical_edid_map,
                    identical_edid_indexed_map=identical_edid_indexed_map,
                )
                pair_count += ext_counts[0]
                identical_count += ext_counts[1]

            dsd_counts = cls.__collect_dsd_pairs(
                translated_source=translated_source,
                trans_table_root=trans_table_root,
                target_plugin_names=target_plugin_names,
                text_map=text_map,
                edid_map=edid_map,
                edid_indexed_map=edid_indexed_map,
                formid_map=formid_map,
                identical_edid_map=identical_edid_map,
                identical_edid_indexed_map=identical_edid_indexed_map,
            )
            pair_count += dsd_counts[0]
            identical_count += dsd_counts[1]

            cls.log.info(
                "Bridge built: %s translation pair(s), %s identical pair(s), "
                "%s unique phrase(s) mapped.",
                pair_count,
                identical_count,
                len(text_map),
            )

            return {
                "text_map": text_map,
                "edid_map": edid_map,
                "edid_indexed_map": edid_indexed_map,
                "formid_map": formid_map,
                "identical_edid_map": identical_edid_map,
                "identical_edid_indexed_map": identical_edid_indexed_map,
                "pair_count": pair_count,
                "identical_count": identical_count,
                "orig_plugins": list(orig_plugins.keys()),
                "trans_plugins": list(trans_plugins.keys()),
                "common_plugins": list(common_names),
                "stats": {
                    "formid": 0,
                    "text": 0,
                    "edid": 0,
                    "identical": 0,
                    "total": 0,
                },
            }

    @classmethod
    def apply_bridge(
        cls,
        bridge: dict[str, Any],
        target_strings: StringList,
        missing_only: bool = True,
    ) -> StringList:
        """
        Apply translation bridge mappings to target strings in priority order:
        1. Local FormID + Type + Index (with English source verification)
        2. Exact English text match
        3. EDID + Type / EDID + Type + Index

        Args:
            bridge (dict[str, Any]): Bridge mappings generated by `build_bridge`.
            target_strings (StringList): Target strings to translate.
            missing_only (bool): Whether already-completed strings should be preserved.

        Returns:
            StringList: List of modified strings.
        """

        text_map: dict[str, str] = bridge.get("text_map", {})
        edid_map: dict[tuple[str, str], str] = bridge.get("edid_map", {})
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]] = (
            bridge.get("edid_indexed_map", {})
        )
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]] = (
            bridge.get("formid_map", {})
        )
        identical_edid_map: dict[tuple[str, str], tuple[str, str]] = bridge.get(
            "identical_edid_map", {}
        )
        identical_edid_indexed_map: dict[
            tuple[str, str, Optional[int]], tuple[str, str]
        ] = bridge.get("identical_edid_indexed_map", {})

        modified_strings: StringList = []
        formid_applied = 0
        text_applied = 0
        edid_applied = 0
        identical_applied = 0

        for target in target_strings:
            if (
                missing_only
                and target.status == StringStatus.TranslationComplete
                and target.string
            ):
                continue

            fr_match: Optional[str] = None
            match_type: Optional[str] = None
            is_identical_match = False
            is_exact_match = False
            target_orig = cls.__normalize(target.original)

            if isinstance(target, PluginString):
                fkey = (target.form_id[2:].lower(), target.type, target.index)
                if fkey in formid_map:
                    en_text, fr_text, is_id = formid_map[fkey]
                    if target_orig and target_orig == en_text:
                        fr_match = fr_text
                        match_type = "formid"
                        is_identical_match = is_id
                        is_exact_match = True

            if not fr_match and target_orig and target_orig in text_map:
                fr_match = text_map[target_orig]
                match_type = "text"
                is_identical_match = False
                is_exact_match = True

            if (
                not fr_match
                and isinstance(target, PluginString)
                and target.editor_id
                and target.index is None
            ):
                ekey = (target.editor_id, target.type)
                if ekey in edid_map:
                    fr_match = edid_map[ekey]
                    match_type = "edid"
                    is_identical_match = False
                elif ekey in identical_edid_map:
                    en_text, fr_text = identical_edid_map[ekey]
                    if target_orig and target_orig == en_text:
                        fr_match = fr_text
                        match_type = "edid"
                        is_identical_match = True

            if (
                not fr_match
                and isinstance(target, PluginString)
                and target.editor_id
                and target.index is not None
            ):
                eikey = (target.editor_id, target.type, target.index)
                if eikey in edid_indexed_map:
                    en_text, fr_text = edid_indexed_map[eikey]
                    if target_orig and target_orig == en_text:
                        fr_match = fr_text
                        match_type = "edid"
                        is_identical_match = False
                        is_exact_match = True
                elif eikey in identical_edid_indexed_map:
                    en_text, fr_text = identical_edid_indexed_map[eikey]
                    if target_orig and target_orig == en_text:
                        fr_match = fr_text
                        match_type = "edid"
                        is_identical_match = True

            if fr_match is None:
                continue

            if not is_identical_match and cls.__normalize(fr_match) != target_orig:
                target.string = fr_match
                target.status = (
                    StringStatus.TranslationComplete
                    if is_exact_match
                    else StringStatus.TranslationIncomplete
                )
                modified_strings.append(target)
                if match_type == "formid":
                    formid_applied += 1
                elif match_type == "text":
                    text_applied += 1
                elif match_type == "edid":
                    edid_applied += 1
            elif (
                is_identical_match
                and target.status == StringStatus.TranslationRequired
            ):
                target.string = fr_match
                target.status = StringStatus.TranslationIncomplete
                modified_strings.append(target)
                identical_applied += 1

        stats: dict[str, int] = bridge.setdefault(
            "stats",
            {"formid": 0, "text": 0, "edid": 0, "identical": 0, "total": 0},
        )
        stats["formid"] += formid_applied
        stats["text"] += text_applied
        stats["edid"] += edid_applied
        stats["identical"] += identical_applied
        stats["total"] += len(modified_strings)
        return modified_strings

    @classmethod
    def __collect_plugin_pairs(
        cls,
        orig_strings: StringList,
        trans_strings: StringList,
        text_map: dict[str, str],
        edid_map: dict[tuple[str, str], str],
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]],
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]],
        identical_edid_map: dict[tuple[str, str], tuple[str, str]],
        identical_edid_indexed_map: dict[
            tuple[str, str, Optional[int]], tuple[str, str]
        ],
    ) -> tuple[int, int]:
        """Pair embedded plugin strings by local FormID, type, and index."""

        trans_by_key: dict[tuple[str, str, Optional[int]], PluginString] = {
            (item.form_id[2:].lower(), item.type, item.index): item
            for item in trans_strings
            if isinstance(item, PluginString)
        }
        pair_count = 0
        identical_count = 0

        for orig_str in orig_strings:
            if not isinstance(orig_str, PluginString):
                continue
            key = (orig_str.form_id[2:].lower(), orig_str.type, orig_str.index)
            trans_str = trans_by_key.get(key)
            if trans_str is None:
                continue

            en_text = cls.__normalize(orig_str.original or orig_str.string or "")
            fr_clean = cls.__normalize(trans_str.original or trans_str.string or "")
            if not en_text or not fr_clean:
                continue

            added_pair, added_identical = cls.__record_pair(
                key=key,
                editor_id=orig_str.editor_id,
                record_type=orig_str.type,
                index=orig_str.index,
                en_text=en_text,
                fr_clean=fr_clean,
                text_map=text_map,
                edid_map=edid_map,
                edid_indexed_map=edid_indexed_map,
                formid_map=formid_map,
                identical_edid_map=identical_edid_map,
                identical_edid_indexed_map=identical_edid_indexed_map,
            )
            pair_count += added_pair
            identical_count += added_identical

        return pair_count, identical_count

    @classmethod
    def __collect_external_table_pairs(
        cls,
        o_plugin: PluginFile,
        t_plugin: PluginFile,
        orig_table_root: Path,
        trans_table_root: Path,
        plugin_stem: str,
        language: str,
        text_map: dict[str, str],
        edid_map: dict[tuple[str, str], str],
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]],
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]],
        identical_edid_map: dict[tuple[str, str], tuple[str, str]],
        identical_edid_indexed_map: dict[
            tuple[str, str, Optional[int]], tuple[str, str]
        ],
    ) -> tuple[int, int]:
        """Pair localized plugin records backed by external string tables."""

        try:
            orig_ids = o_plugin.extract_external_string_ids()
            trans_ids = t_plugin.extract_external_string_ids()
            if not orig_ids or not trans_ids:
                return 0, 0
            orig_tables = cls.__load_string_tables(
                orig_table_root, "english", plugin_stem, set(orig_ids)
            )
            trans_tables = cls.__load_string_tables(
                trans_table_root, language, plugin_stem, set(trans_ids)
            )
        except _BRIDGE_ERRORS as ex:
            cls.log.warning(
                "Could not read localized bridge strings in '%s': %s",
                plugin_stem,
                ex,
            )
            return 0, 0

        orig_by_key: dict[tuple[str, str, Optional[int]], tuple[PluginString, str]] = {}
        for table_id, strings in orig_ids.items():
            text = orig_tables.get(table_id)
            if not text:
                continue
            for item in strings:
                key = (item.form_id[2:].lower(), item.type, item.index)
                orig_by_key[key] = (item, cls.__normalize(text))

        trans_by_key: dict[tuple[str, str, Optional[int]], str] = {}
        for table_id, strings in trans_ids.items():
            text = trans_tables.get(table_id)
            if not text:
                continue
            for item in strings:
                key = (item.form_id[2:].lower(), item.type, item.index)
                trans_by_key[key] = cls.__normalize(text)

        pair_count = 0
        identical_count = 0
        for key, (orig_str, en_text) in orig_by_key.items():
            fr_clean = trans_by_key.get(key)
            if not en_text or not fr_clean:
                continue
            added_pair, added_identical = cls.__record_pair(
                key=key,
                editor_id=orig_str.editor_id,
                record_type=orig_str.type,
                index=orig_str.index,
                en_text=en_text,
                fr_clean=fr_clean,
                text_map=text_map,
                edid_map=edid_map,
                edid_indexed_map=edid_indexed_map,
                formid_map=formid_map,
                identical_edid_map=identical_edid_map,
                identical_edid_indexed_map=identical_edid_indexed_map,
            )
            pair_count += added_pair
            identical_count += added_identical

        return pair_count, identical_count

    @classmethod
    def __collect_dsd_pairs(
        cls,
        translated_source: Path,
        trans_table_root: Path,
        target_plugin_names: Optional[list[str]],
        text_map: dict[str, str],
        edid_map: dict[tuple[str, str], str],
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]],
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]],
        identical_edid_map: dict[tuple[str, str], tuple[str, str]],
        identical_edid_indexed_map: dict[
            tuple[str, str, Optional[int]], tuple[str, str]
        ],
    ) -> tuple[int, int]:
        """Collect translation pairs from Dynamic String Distributor JSON files."""

        dsd_paths: list[Path] = []
        if (
            translated_source.is_file()
            and translated_source.suffix.lower() == ".json"
        ):
            dsd_paths.append(translated_source)
        elif trans_table_root.exists():
            dsd_paths = [
                path
                for path in trans_table_root.rglob("*.json")
                if path.is_file()
                and "dynamicstringdistributor"
                in str(path).replace("\\", "/").lower()
            ]

        if target_plugin_names and len(dsd_paths) > 1:
            target_lowers = {name.lower() for name in target_plugin_names}
            filtered = [
                path for path in dsd_paths if path.parent.name.lower() in target_lowers
            ]
            if filtered:
                dsd_paths = filtered

        pair_count = 0
        identical_count = 0
        for dsd_path in dsd_paths:
            try:
                strings = StringLoader.load_strings_from_json_file(dsd_path)
            except _BRIDGE_ERRORS as ex:
                cls.log.warning(
                    "Could not read DSD file '%s': %s", dsd_path, ex
                )
                continue

            for item in strings:
                if not isinstance(item, PluginString):
                    continue
                en_text = cls.__normalize(item.original)
                fr_clean = cls.__normalize(item.string or "")
                if not en_text or not fr_clean:
                    continue
                key = (item.form_id[2:].lower(), item.type, item.index)
                added_pair, added_identical = cls.__record_pair(
                    key=key,
                    editor_id=item.editor_id,
                    record_type=item.type,
                    index=item.index,
                    en_text=en_text,
                    fr_clean=fr_clean,
                    text_map=text_map,
                    edid_map=edid_map,
                    edid_indexed_map=edid_indexed_map,
                    formid_map=formid_map,
                    identical_edid_map=identical_edid_map,
                    identical_edid_indexed_map=identical_edid_indexed_map,
                )
                pair_count += added_pair
                identical_count += added_identical

        return pair_count, identical_count

    @staticmethod
    def __record_pair(
        key: tuple[str, str, Optional[int]],
        editor_id: Optional[str],
        record_type: str,
        index: Optional[int],
        en_text: str,
        fr_clean: str,
        text_map: dict[str, str],
        edid_map: dict[tuple[str, str], str],
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]],
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str, bool]],
        identical_edid_map: dict[tuple[str, str], tuple[str, str]],
        identical_edid_indexed_map: dict[
            tuple[str, str, Optional[int]], tuple[str, str]
        ],
    ) -> tuple[int, int]:
        """Store a paired original/translated entry into all lookup maps."""

        if en_text != fr_clean:
            text_map.setdefault(en_text, fr_clean)
            if editor_id and index is None:
                edid_map[(editor_id, record_type)] = fr_clean
            if editor_id:
                edid_indexed_map[(editor_id, record_type, index)] = (
                    en_text,
                    fr_clean,
                )
            formid_map[key] = (en_text, fr_clean, False)
            return 1, 0

        formid_map[key] = (en_text, fr_clean, True)
        if (
            editor_id
            and index is None
            and (editor_id, record_type) not in edid_map
        ):
            identical_edid_map[(editor_id, record_type)] = (en_text, fr_clean)
        if editor_id:
            identical_edid_indexed_map[(editor_id, record_type, index)] = (
                en_text,
                fr_clean,
            )
        return 0, 1

    @staticmethod
    def __load_string_tables(
        root: Path,
        language: str,
        plugin_stem: str,
        string_ids: set[tuple[StringFileKind, int]],
    ) -> dict[tuple[StringFileKind, int], str]:
        """
        Load string-table entries, preferring the requested language suffix.

        Args:
            root (Path): Extracted archive or source folder.
            language (str): Preferred language suffix.
            plugin_stem (str): Plugin stem used to select related string tables.
            string_ids (set[tuple[StringFileKind, int]]): Referenced table IDs.

        Returns:
            dict[tuple[StringFileKind, int], str]: Decoded table strings.
        """

        tables: dict[tuple[StringFileKind, int], str] = {}
        if not root.exists():
            return tables

        table_paths: list[Path] = [
            path
            for path in root.rglob("*")
            if path.is_file()
            and path.suffix.lower() in _TABLE_KINDS
            and path.stem.lower().startswith(f"{plugin_stem.lower()}_")
        ]
        for bsa_path in root.rglob("*.bsa"):
            if not bsa_path.is_file():
                continue
            try:
                bsa = BSAArchive(bsa_path)
                for inner in bsa.glob(f"strings/{plugin_stem.lower()}_*.*strings"):
                    if Path(inner).suffix.lower() in _TABLE_KINDS:
                        table_paths.append(bsa_path / inner)
            except _BRIDGE_ERRORS as ex:
                TranslationBridge.log.warning(
                    "Could not scan BSA '%s' for string tables: %s",
                    bsa_path.name,
                    ex,
                )

        table_paths.sort(
            key=lambda path: not path.stem.lower().endswith(f"_{language.lower()}")
        )
        for path in table_paths:
            kind = _TABLE_KINDS[path.suffix.lower()]
            try:
                with (
                    FileSourceFactory.for_file_path(path).get_file_stream() as stream,
                    StringTable.from_stream(stream, kind) as table,
                ):
                    for kind_, string_id in string_ids:
                        if kind_ != kind:
                            continue
                        raw = table.get(string_id)
                        if raw is not None:
                            tables.setdefault(
                                (kind, string_id),
                                TranslationBridge.__decode_string(
                                    raw.removesuffix(b"\0")
                                ),
                            )
            except _BRIDGE_ERRORS as ex:
                TranslationBridge.log.warning(
                    "Could not read string table '%s': %s", path.name, ex
                )
        return tables

    @staticmethod
    def __decode_string(data: bytes) -> str:
        """Decode string-table bytes using common Skyrim localization encodings."""

        for encoding in ("utf-8", "cp1250", "cp1252", "cp1251"):
            try:
                return data.decode(encoding)
            except UnicodeDecodeError:
                continue
        return data.decode("utf-8", errors="ignore")

    @staticmethod
    def __normalize(text: str) -> str:
        """Normalize whitespace variants commonly introduced by archives."""

        return (
            text.strip()
            .replace("\xa0", " ")
            .replace("\u202f", " ")
            .replace("\u200b", "")
        )
