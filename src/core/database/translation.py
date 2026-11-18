"""
Copyright (c) Cutleast
"""

from __future__ import annotations

import time
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any, Optional, Self, override

from cutleast_core_lib.core.filesystem.scanner import DirectoryScanner
from pydantic import BaseModel, Field, ValidationError

from core.string.string_status import StringStatus
from core.string.string_utils import StringUtils
from core.string.types import StringList
from core.translation_provider.cdt_api.cdt_id import CdtModId
from core.translation_provider.mod_id import ModId
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.source import Source

from .translation_service import TranslationService


class Translation(BaseModel):
    """
    Class for mod translations.
    """

    name: str
    """The name of the translation."""

    path: Path = Field(exclude=True)
    """The path to the translation."""

    mod_id: Optional[ModId] = None
    """The mod identifier of the translation at its source."""

    version: Optional[str] = None
    """The version of the translation at its source."""

    strings_: Optional[dict[Path, StringList]] = Field(default=None, exclude=True)
    """Map of mod file names to list of strings."""

    source: Source = Source.Local
    """The source of the translation."""

    timestamp: int = Field(default_factory=lambda: int(time.time()))
    """The creation timestamp of the translation."""

    def to_index_data(self) -> dict[str, Any]:
        """
        Generates index data for the index.json file in the database.

        Returns:
            dict[str, Any]: Index data.
        """

        return self.model_dump(mode="json", exclude_defaults=True)

    @classmethod
    def from_index_data(cls, index_data: dict[str, Any], database_path: Path) -> Self:
        """
        Gets a Translation object from the specified index data.

        Args:
            index_data (dict[str, Any]): Entry from the database's index.json file.
            database_path (Path): The path to the database.

        Returns:
            Self: Translation object.
        """

        translation: Self
        try:
            data: dict[str, Any] = index_data.copy()
            relative_path: str = str(data.get("path", data["name"]))
            data["path"] = database_path / relative_path

            translation = cls.model_validate(data)
        except ValidationError:
            translation = cls.__load_legacy_index_data(index_data, database_path)

        if not translation.path.is_dir():
            legacy_path: Optional[Path] = Translation.__get_legacy_storage_path(
                translation, database_path
            )
            if legacy_path is not None:
                translation.path = legacy_path

        return translation

    @classmethod
    def __load_legacy_index_data(
        cls, index_data: dict[str, Any], database_path: Path
    ) -> Self:
        """
        Loads a translation from legacy index data using flat mod identifier fields.

        Args:
            index_data (dict[str, Any]): Legacy entry from the index.json file.
            database_path (Path): The path to the database.

        Returns:
            Self: Translation object.
        """

        legacy_data: dict[str, Any] = index_data.copy()
        name: str = legacy_data["name"]
        raw_mod_id: Optional[int] = legacy_data.pop("mod_id", None)
        raw_file_id: Optional[int] = legacy_data.pop("file_id", None)
        raw_orig_mod_id: Optional[int] = legacy_data.pop("original_mod_id", None)
        relative_path: str = str(legacy_data.pop("path", name))

        translation_path: Path = database_path / relative_path
        source_name: str = legacy_data.pop("source", "")
        source: Optional[Source] = Source.get(source_name)

        if source is None:
            if raw_mod_id and raw_file_id:
                source = Source.NexusMods
            elif raw_mod_id:
                source = Source.Confrerie
            else:
                source = Source.Local

        mod_id: Optional[ModId] = None
        if raw_mod_id and raw_file_id and source == Source.NexusMods:
            mod_id = NxmModId(mod_id=raw_mod_id, file_id=raw_file_id)
        elif raw_mod_id and source == Source.Confrerie and raw_orig_mod_id is not None:
            mod_id = CdtModId(mod_id=raw_mod_id, nm_mod_id=raw_orig_mod_id)

        return cls(path=translation_path, mod_id=mod_id, **legacy_data, source=source)

    @staticmethod
    def __get_legacy_storage_path(
        translation: Translation, database_path: Path
    ) -> Optional[Path]:
        """
        Resolves a translation path stored in hashed folders by legacy database formats.

        Args:
            translation (Translation): The translation to resolve the folder for.
            database_path (Path): The path to the database directory.

        Returns:
            Optional[Path]: The existing legacy folder path or None.
        """

        if translation.version is None:
            return None

        local_source_id: str = sha256(
            f"{translation.mod_id}:{translation.version}:Local".encode()
        ).hexdigest()[:16]
        local_path: Path = database_path / "local_mod_translations" / local_source_id
        if local_path.is_dir():
            return local_path

        remote_source_id: str = sha256(
            f"{translation.mod_id}:{translation.version}:"
            f"{translation.source.value}".encode()
        ).hexdigest()[:16]
        source_path: Path = database_path / "source_mod_translations" / remote_source_id
        if source_path.is_dir():
            return source_path

        return None

    @classmethod
    def create(
        cls, name: str, path: Path, strings: Optional[dict[Path, StringList]] = None
    ) -> Self:
        """
        Creates a new translation.

        Args:
            name (str): The name of the translation.
            path (Path): The path to the translation's folder.
            strings (Optional[dict[Path, StringList]], optional):
                The initial strings of the translation. Defaults to None.

        Returns:
            Self: Created translation.
        """

        translation = cls(name=name, path=path)
        if strings is not None:
            translation.strings = strings
        return translation

    @property
    def id(self) -> str:
        """
        Generates a unique id for the translation.

        Included attributes:
        - `name`
        - `path`
        """

        return f"{self.name}###{self.path}".lower()

    @override
    def __hash__(self) -> int:
        return hash(self.id)

    @property
    def strings(self) -> dict[Path, StringList]:
        """
        List of strings for each mod file name.
        """

        if self.strings_ is None:
            self.strings_ = TranslationService.load_translation_strings(self.path)

        return self.strings_

    @strings.setter
    def strings(self, strings: dict[Path, StringList]) -> None:
        self.strings_ = strings

    def reload_strings(self) -> None:
        """
        Reloads the strings of the translation from the translation's folder and
        discards its cached size. The cached strings are only replaced if all files of
        the translation could be loaded successfully.

        Raises:
            OSError: If a file of the translation could not be read.
            ValidationError: If a file of the translation contains invalid data.
        """

        self.strings_ = TranslationService.load_translation_strings(
            self.path, raise_errors=True
        )
        Translation.get_size.cache_clear()

    @lru_cache  # noqa: B019
    def get_size(self) -> int:
        """
        Returns the size of the translation in bytes.

        Returns:
            int: Size of the translation in bytes.
        """

        return DirectoryScanner.get_folder_size(self.path)

    @property
    def size(self) -> int:
        """
        Returns the size of the translation in bytes.

        Returns:
            int: Size of the translation in bytes.
        """

        return self.get_size()

    @property
    def status(self) -> dict[Path, StringStatus]:
        """
        Returns the status of the translation.

        Returns:
            dict[Path, StringStatus]: Status of the translation.
        """

        return {
            modfile_name: max(
                (string.status for string in modfile_strings),
                default=StringStatus.NoneStatus,
            )
            for modfile_name, modfile_strings in self.strings.items()
        }

    @property
    def is_complete(self) -> bool:
        """If no mod file of this translation has untranslated strings."""

        return not any(
            status > StringStatus.TranslationComplete for status in self.status.values()
        )

    def remove_duplicates(self, save: bool = True) -> None:
        """
        Removes duplicate strings from the translation.

        Args:
            save (bool, optional): Whether to save the translation. Defaults to True.
        """

        for modfile_name, modfile_strings in self.strings.items():
            self.strings[modfile_name] = StringUtils.unique(modfile_strings)

        if save:
            self.save()

    def save(self) -> None:
        """
        Saves the translation.
        """

        TranslationService.save_translation_strings(self.path, self.strings)
