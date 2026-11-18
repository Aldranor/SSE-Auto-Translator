"""
Copyright (c) Cutleast
"""

import logging
from pathlib import Path
from typing import Optional

from cutleast_core_lib.core.filesystem.utils import add_suffix, rem_last_suffix

from core.string.string_loader import StringLoader
from core.string.types import StringList, StringListModel


class TranslationService:
    """
    Class for loading and saving translations.
    """

    TRANSLATION_FILE_SUFFIXES: set[str] = {
        ".esl",
        ".esm",
        ".esp",
        ".json",
        ".txt",
    }
    """Supported mod file suffixes wrapped by translation JSON files."""

    log: logging.Logger = logging.getLogger("TranslationService")

    @staticmethod
    def is_translation_json_file(json_file: Path) -> bool:
        """
        Checks whether a JSON file path corresponds to a valid mod file translation
        (i.e. `<modfile>.<ext>.json`).

        Args:
            json_file (Path): Path to the JSON file to check.

        Returns:
            bool: `True` if the JSON file wraps a supported mod file extension.
        """

        if json_file.suffix.lower() != ".json":
            return False

        modfile_path: Path = rem_last_suffix(json_file)
        return (
            modfile_path.suffix.lower() in TranslationService.TRANSLATION_FILE_SUFFIXES
        )

    @classmethod
    def load_translation_strings(
        cls, translation_folder: Path, raise_errors: bool = False
    ) -> dict[Path, StringList]:
        """
        Loads the strings for a translation from the specified folder.

        Args:
            translation_folder (Path): Path to the folder with the translation's files.
            raise_errors (bool, optional):
                Whether to raise errors when a file fails to load instead of logging and
                skipping it. Defaults to False.

        Raises:
            OSError: If `raise_errors` is True and a file could not be read.
            ValidationError: If `raise_errors` is True and a file contains invalid data.

        Returns:
            dict[Path, StringList]: Map of mod file names to their list of strings.
        """

        json_files: list[Path] = [
            json_file
            for json_file in translation_folder.rglob("*.json")
            if TranslationService.is_translation_json_file(json_file)
        ]
        strings: dict[Path, StringList] = {}
        for json_file in json_files:
            modfile_path: Path = rem_last_suffix(json_file).relative_to(
                translation_folder
            )
            try:
                strings[modfile_path] = StringLoader.load_strings_from_json_file(
                    json_file
                )
            except Exception as ex:
                if raise_errors:
                    raise

                cls.log.error(
                    f"Failed to load strings from file '{json_file}': {ex}", exc_info=ex
                )

        return strings

    @classmethod
    def save_translation_strings(
        cls, translation_folder: Path, strings: dict[Path, StringList]
    ) -> None:
        """
        Saves the strings for a translation to the specified folder.

        Args:
            translation_folder (Path): Path to the folder to save the strings to.
            strings (dict[Path, StringList]): Map of mod file names to their list of strings.
        """

        for modfile_name, modfile_strings in strings.items():
            json_file_path: Path = translation_folder / add_suffix(modfile_name, ".json")
            json_file_path.parent.mkdir(parents=True, exist_ok=True)
            cls.save_strings_to_json_file(json_file_path, modfile_strings)

    @classmethod
    def save_strings_to_json_file(
        cls, json_file_path: Path, strings: StringList, indent: Optional[int] = None
    ) -> None:
        """
        Saves strings to a JSON file.

        Args:
            json_file_path (Path): Path to the JSON file.
            strings (StringList): List of strings.
            indent (Optional[int], optional): Indentation level. Defaults to None.
        """

        json_file_path.write_bytes(StringListModel.dump_json(strings, indent=indent))
