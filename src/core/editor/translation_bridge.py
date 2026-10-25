"""
Copyright (c) Cutleast
"""

import logging
import tempfile
from pathlib import Path
from typing import Any, Optional

from cutleast_core_lib.core.archive_legacy.archive import Archive

from core.file_types.plugin.file import PluginFile
from core.file_types.plugin.string import PluginString
from core.string.string_status import StringStatus
from core.string.types import StringList


class TranslationBridge:
    """
    Builds a translation bridge between an original mod file (English vOld)
    and a translated mod file (e.g. French vOld) of the same version,
    and applies it to a target mod file (e.g. English vNew / ESL-compacted).
    """

    log: logging.Logger = logging.getLogger("TranslationBridge")

    @classmethod
    def find_plugins_in_source(
        cls, source_path: Path, temp_dir: Path
    ) -> dict[str, Path]:
        """
        Extracts or identifies all plugin files (*.esp, *.esm, *.esl) from a source
        which can be a single plugin file, an archive, or a folder.

        Args:
            source_path (Path): Path to the source file or folder.
            temp_dir (Path): Destination for any extracted files.

        Returns:
            dict[str, Path]: Map of lowered plugin file name to extracted/actual Path.
        """
        plugins: dict[str, Path] = {}

        if source_path.is_file():
            suffix = source_path.suffix.lower()
            if suffix in (".esp", ".esm", ".esl"):
                plugins[source_path.name.lower()] = source_path
            elif suffix in (".7z", ".zip", ".rar"):
                try:
                    archive = Archive.load_archive(source_path)
                    all_files = archive.get_files()
                    plugin_files = [
                        f
                        for f in all_files
                        if Path(f).suffix.lower() in (".esp", ".esm", ".esl")
                    ]
                    if plugin_files:
                        dest = temp_dir / source_path.stem
                        dest.mkdir(parents=True, exist_ok=True)
                        archive.extract_files(plugin_files, dest)
                        for pf in plugin_files:
                            extracted_path = dest / pf
                            if extracted_path.exists():
                                plugins[extracted_path.name.lower()] = extracted_path
                except Exception as ex:
                    cls.log.error(
                        f"Failed to extract plugins from archive '{source_path}': {ex}",
                        exc_info=ex,
                    )
        elif source_path.is_dir():
            for p in source_path.rglob("*"):
                if p.is_file() and p.suffix.lower() in (".esp", ".esm", ".esl"):
                    plugins[p.name.lower()] = p

        return plugins

    @classmethod
    def build_bridge(
        cls,
        translated_source: Path,
        original_source: Path,
        target_plugin_names: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """
        Builds translation mappings between an old translated source (French)
        and an old original source (English) of the exact same version.

        Args:
            translated_source (Path): Path to old translated archive or file.
            original_source (Path): Path to old original archive or file.
            target_plugin_names (Optional[list[str]], optional):
                Limit extraction to specific plugin names if specified. Defaults to None.

        Returns:
            dict[str, Any]: Bridge dictionary containing lookup maps.
        """
        temp_dir = Path(tempfile.mkdtemp(prefix="sse_bridge_"))

        trans_plugins = cls.find_plugins_in_source(translated_source, temp_dir / "trans")
        orig_plugins = cls.find_plugins_in_source(original_source, temp_dir / "orig")

        cls.log.info(
            f"Building bridge: found {len(trans_plugins)} translated plugin(s) "
            f"and {len(orig_plugins)} original plugin(s)."
        )

        text_map: dict[str, str] = {}
        edid_map: dict[tuple[str, str], str] = {}
        edid_indexed_map: dict[tuple[str, str, Optional[int]], tuple[str, str]] = {}
        formid_map: dict[tuple[str, str, Optional[int]], tuple[str, str]] = {}

        common_names = set(trans_plugins.keys()) & set(orig_plugins.keys())
        if target_plugin_names:
            target_lowers = {n.lower() for n in target_plugin_names}
            common_names = {n for n in common_names if n in target_lowers}

        pair_count = 0
        for name in common_names:
            t_path = trans_plugins[name]
            o_path = orig_plugins[name]

            try:
                trans_strings = PluginFile(name=t_path.name, full_path=t_path).get_strings()
                orig_strings = PluginFile(name=o_path.name, full_path=o_path).get_strings()
            except Exception as ex:
                cls.log.error(f"Failed to read strings for '{name}': {ex}", exc_info=ex)
                continue

            trans_by_key = {
                (s.form_id, s.type, s.index): s
                for s in trans_strings
            }

            for orig_str in orig_strings:
                key = (orig_str.form_id, orig_str.type, orig_str.index)
                trans_str = trans_by_key.get(key)
                if trans_str is None:
                    continue

                en_text = (orig_str.original or orig_str.string or "").strip()
                fr_text = (trans_str.original or trans_str.string or "").strip()

                if not en_text or not fr_text or en_text == fr_text:
                    continue

                # Normalize spaces
                fr_clean = (
                    fr_text.replace("\xa0", " ")
                    .replace("\u202f", " ")
                    .replace("\u200b", "")
                )

                pair_count += 1

                # 1. Exact English text -> French translation
                if en_text not in text_map:
                    text_map[en_text] = fr_clean

                # 2. EDID + Type (when index is None)
                if orig_str.editor_id and orig_str.index is None:
                    edid_map[(orig_str.editor_id, orig_str.type)] = fr_clean

                # 3. EDID + Type + Index
                if orig_str.editor_id:
                    edid_indexed_map[
                        (orig_str.editor_id, orig_str.type, orig_str.index)
                    ] = (en_text, fr_clean)

                # 4. FormID map
                formid_map[(orig_str.form_id, orig_str.type, orig_str.index)] = (
                    en_text,
                    fr_clean,
                )

        cls.log.info(
            f"Bridge constructed successfully: {pair_count} translation pairs, "
            f"{len(text_map)} unique English phrases mapped."
        )

        return {
            "text_map": text_map,
            "edid_map": edid_map,
            "edid_indexed_map": edid_indexed_map,
            "formid_map": formid_map,
            "pair_count": pair_count,
        }

    @classmethod
    def apply_bridge(
        cls,
        bridge: dict[str, Any],
        target_strings: StringList,
        missing_only: bool = True,
    ) -> int:
        """
        Applies translation bridge mappings to a list of target strings.

        Args:
            bridge (dict[str, Any]): Bridge mappings generated by `build_bridge`.
            target_strings (StringList): Target strings to translate.
            missing_only (bool, optional): Only translate missing strings. Defaults to True.

        Returns:
            int: Number of strings translated.
        """
        text_map = bridge.get("text_map", {})
        edid_map = bridge.get("edid_map", {})
        edid_indexed_map = bridge.get("edid_indexed_map", {})
        formid_map = bridge.get("formid_map", {})

        modified_count = 0

        for target in target_strings:
            if (
                missing_only
                and target.status == StringStatus.TranslationComplete
                and target.string
            ):
                continue

            fr_match: Optional[str] = None

            # 1. Direct FormID match if FormID didn't change and English matches
            fkey = (target.form_id, target.type, target.index)
            if fkey in formid_map:
                en_text, fr_text = formid_map[fkey]
                if target.original and target.original.strip() == en_text:
                    fr_match = fr_text

            # 2. Exact English text match (safe across ESL compaction for dialogues, quests, etc.)
            if not fr_match and target.original:
                orig_clean = target.original.strip()
                if orig_clean in text_map:
                    fr_match = text_map[orig_clean]

            # 3. EDID + Type match (only if index is None)
            if (
                not fr_match
                and isinstance(target, PluginString)
                and target.editor_id
                and target.index is None
            ):
                ekey = (target.editor_id, target.type)
                if ekey in edid_map:
                    fr_match = edid_map[ekey]

            # 4. EDID + Type + Index match (verifying English text matches)
            if (
                not fr_match
                and isinstance(target, PluginString)
                and target.editor_id
                and target.index is not None
            ):
                eikey = (target.editor_id, target.type, target.index)
                if eikey in edid_indexed_map:
                    en_text, fr_text = edid_indexed_map[eikey]
                    if target.original and target.original.strip() == en_text:
                        fr_match = fr_text

            if (
                fr_match
                and fr_match.strip() != (target.original.strip() if target.original else "")
            ):
                target.string = fr_match
                target.status = StringStatus.TranslationComplete
                modified_count += 1

        cls.log.info(f"Applied bridge: translated {modified_count} string(s).")
        return modified_count
