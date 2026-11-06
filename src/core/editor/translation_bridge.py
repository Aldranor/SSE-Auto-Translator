"""
Copyright (c) Cutleast
"""

import logging
import tempfile
from pathlib import Path
from typing import Optional

from cutleast_core_lib.core.archive_legacy.archive import Archive

from core.file_types.plugin.file import PluginFile
from core.file_types.plugin.string import PluginString
from core.string.string_status import StringStatus
from core.string.types import StringList


class TranslationBridge:
    """Transfers translations between plugin versions using shared record data."""

    log: logging.Logger = logging.getLogger("TranslationBridge")
    __plugin_suffixes: tuple[str, ...] = (".esp", ".esm", ".esl")
    __archive_suffixes: tuple[str, ...] = (".7z", ".rar", ".zip")

    @classmethod
    def apply(
        cls,
        translated_source: Path,
        original_source: Path,
        target_strings: StringList,
        missing_only: bool = True,
    ) -> StringList:
        """Builds a bridge from source files and applies it to the target strings.

        Args:
            translated_source (Path): Older translated archive or plugin.
            original_source (Path): Matching original-language archive or plugin.
            target_strings (StringList): Strings in the currently open translation.
            missing_only (bool, optional): Preserve existing completed strings.
                Defaults to True.

        Returns:
            StringList: Strings modified by the bridge.
        """

        with tempfile.TemporaryDirectory(prefix="sse-translation-bridge-") as temp:
            temp_dir: Path = Path(temp)
            translated_plugins: dict[str, Path] = cls.__find_plugins(
                translated_source, temp_dir / "translated"
            )
            original_plugins: dict[str, Path] = cls.__find_plugins(
                original_source, temp_dir / "original"
            )
            common_names: set[str] = set(translated_plugins) & set(original_plugins)

            if not common_names:
                raise ValueError("The selected sources contain no matching plugins.")

            by_form_id: dict[
                tuple[str, str, Optional[int]], tuple[str, str, bool]
            ] = {}
            by_editor_id: dict[tuple[str, str], str] = {}
            by_editor_id_and_index: dict[
                tuple[str, str, Optional[int]], tuple[str, str]
            ] = {}
            by_text: dict[str, str] = {}
            identical_editor_ids: dict[tuple[str, str], str] = {}
            identical_editor_ids_and_indexes: dict[
                tuple[str, str, Optional[int]], tuple[str, str]
            ] = {}

            for plugin_name in common_names:
                translated_file: PluginFile = PluginFile(
                    name=translated_plugins[plugin_name].name,
                    full_path=translated_plugins[plugin_name],
                )
                original_file: PluginFile = PluginFile(
                    name=original_plugins[plugin_name].name,
                    full_path=original_plugins[plugin_name],
                )
                translated_strings: list[PluginString] = [
                    string
                    for string in translated_file.get_strings()
                    if isinstance(string, PluginString)
                ]
                original_strings: list[PluginString] = [
                    string
                    for string in original_file.get_strings()
                    if isinstance(string, PluginString)
                ]
                translated_by_key: dict[
                    tuple[str, str, Optional[int]], PluginString
                ] = {
                    cls.__plugin_key(string): string for string in translated_strings
                }

                for original_string in original_strings:
                    key: tuple[str, str, Optional[int]] = cls.__plugin_key(
                        original_string
                    )
                    translated_string: Optional[PluginString] = translated_by_key.get(
                        key
                    )
                    if translated_string is None:
                        continue

                    original_text: str = (original_string.original or "").strip()
                    translated_text: str = (
                        translated_string.string or translated_string.original or ""
                    ).strip()
                    translated_text = cls.__normalize_text(translated_text)
                    if not original_text or not translated_text:
                        continue

                    by_form_id[key] = (
                        original_text,
                        translated_text,
                        original_text == translated_text,
                    )
                    if original_text == translated_text:
                        if original_string.editor_id:
                            edid: tuple[str, str] = (
                                original_string.editor_id,
                                original_string.type,
                            )
                            if original_string.index is None:
                                identical_editor_ids.setdefault(edid, translated_text)
                            identical_editor_ids_and_indexes[
                                (
                                    original_string.editor_id,
                                    original_string.type,
                                    original_string.index,
                                )
                            ] = (original_text, translated_text)
                        continue

                    by_text.setdefault(original_text, translated_text)
                    if original_string.editor_id:
                        editor_id_key: tuple[str, str] = (
                            original_string.editor_id,
                            original_string.type,
                        )
                        if original_string.index is None:
                            by_editor_id.setdefault(editor_id_key, translated_text)
                        by_editor_id_and_index[
                            (
                                original_string.editor_id,
                                original_string.type,
                                original_string.index,
                            )
                        ] = (original_text, translated_text)

        modified_strings: StringList = []
        for target in target_strings:
            if target.status in (StringStatus.NoTranslationRequired,):
                continue
            if missing_only and target.status == StringStatus.TranslationComplete:
                continue

            match: Optional[str] = None
            exact_match: bool = False
            identical_match: bool = False

            if isinstance(target, PluginString):
                form_id_key: tuple[str, str, Optional[int]] = cls.__plugin_key(target)
                form_id_match: Optional[tuple[str, str, bool]] = by_form_id.get(
                    form_id_key
                )
                if form_id_match is not None:
                    original_text, translated_text, is_identical = form_id_match
                    if target.original.strip() == original_text:
                        match = translated_text
                        exact_match = True
                        identical_match = is_identical

            target_text: str = (target.original or "").strip()
            if match is None and target_text:
                match = by_text.get(target_text)
                exact_match = match is not None

            if isinstance(target, PluginString) and target.editor_id:
                edid: tuple[str, str] = (target.editor_id, target.type)
                if match is None and target.index is None:
                    match = by_editor_id.get(edid)
                    if match is None:
                        identical_text = identical_editor_ids.get(edid)
                        if identical_text is not None and target_text == identical_text:
                            match = identical_text
                            identical_match = True

                if match is None and target.index is not None:
                    indexed_key: tuple[str, str, Optional[int]] = (
                        target.editor_id,
                        target.type,
                        target.index,
                    )
                    indexed_match: Optional[tuple[str, str]] = (
                        by_editor_id_and_index.get(indexed_key)
                    )
                    if indexed_match is not None and target_text == indexed_match[0]:
                        match = indexed_match[1]
                        exact_match = True
                    else:
                        identical_indexed: Optional[tuple[str, str]] = (
                            identical_editor_ids_and_indexes.get(indexed_key)
                        )
                        if (
                            identical_indexed is not None
                            and target_text == identical_indexed[0]
                        ):
                            match = identical_indexed[1]
                            identical_match = True

            if match is None:
                continue

            if identical_match:
                if target.status == StringStatus.TranslationRequired:
                    target.string = match
                    target.status = StringStatus.TranslationIncomplete
                    modified_strings.append(target)
                continue

            if match == target_text:
                continue

            target.string = match
            target.status = (
                StringStatus.TranslationComplete
                if exact_match
                else StringStatus.TranslationIncomplete
            )
            modified_strings.append(target)

        cls.log.info("Translation bridge updated %d string(s).", len(modified_strings))
        return modified_strings

    @classmethod
    def __find_plugins(cls, source: Path, output_dir: Path) -> dict[str, Path]:
        """Finds plugins in a file, archive, or directory.

        Args:
            source (Path): Plugin, archive, or directory to inspect.
            output_dir (Path): Destination for plugins extracted from archives.

        Returns:
            dict[str, Path]: Plugin paths keyed by lowercase filename.
        """

        if source.is_file() and source.suffix.lower() in cls.__plugin_suffixes:
            return {source.name.lower(): source}

        if source.is_dir():
            return {
                plugin.name.lower(): plugin
                for plugin in source.rglob("*")
                if plugin.is_file() and plugin.suffix.lower() in cls.__plugin_suffixes
            }

        if not source.is_file() or source.suffix.lower() not in cls.__archive_suffixes:
            raise ValueError(f"Unsupported bridge source: '{source}'.")

        archive: Archive = Archive.load_archive(source)
        archive_files: list[str] = archive.get_files()
        plugin_paths: list[str] = [
            file_path
            for file_path in archive_files
            if Path(file_path).suffix.lower() in cls.__plugin_suffixes
        ]
        output_dir.mkdir(parents=True, exist_ok=True)
        archive.extract_files(plugin_paths, output_dir)

        return {
            Path(plugin_path).name.lower(): output_dir / plugin_path
            for plugin_path in plugin_paths
            if (output_dir / plugin_path).is_file()
        }

    @staticmethod
    def __plugin_key(
        string: PluginString,
    ) -> tuple[str, str, Optional[int]]:
        """Builds a record key without the plugin load-order byte.

        Args:
            string (PluginString): Plugin string to key.

        Returns:
            tuple[str, str, Optional[int]]: Record ID, string type, and index.
        """

        return string.record_id.lower(), string.type, string.index

    @staticmethod
    def __normalize_text(text: str) -> str:
        """Normalizes whitespace characters commonly found in translated text.

        Args:
            text (str): Text to normalize.

        Returns:
            str: Text with special whitespace characters replaced or removed.
        """

        return text.replace("\xa0", " ").replace("\u202f", " ").replace("\u200b", "")
