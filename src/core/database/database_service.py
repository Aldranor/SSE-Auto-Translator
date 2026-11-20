"""
Copyright (c) Cutleast
"""

import logging
import os
import shutil
from pathlib import Path
from typing import Any, Optional

import jstyleson as json
from cutleast_core_lib.core.alerts.alert import Alert
from cutleast_core_lib.core.alerts.manager import AlertManager
from cutleast_core_lib.core.filesystem.utils import rem_last_suffix
from cutleast_core_lib.core.multithreading.progress import ProgressUpdate
from cutleast_core_lib.core.utilities.exceptions import format_exception
from cutleast_core_lib.core.utilities.unique import unique
from cutleast_core_lib.ui.progress.display import ProgressDisplay
from pydantic import ValidationError
from PySide6.QtWidgets import QApplication

from core.database.translation import Translation
from core.mod_file.mod_file import ModFile
from core.mod_file.translation_status import TranslationStatus
from core.mod_instance.mod import Mod
from core.mod_instance.mod_instance import ModInstance
from core.string.string_loader import StringLoader
from core.string.string_utils import StringUtils
from core.string.types import StringList
from core.translation_provider.mod_id import ModId
from core.translation_provider.source import Source
from core.utilities.constants import OUTPUT_MOD_MARKER_FILENAME
from core.utilities.game_language import GameLanguage

from .database import TranslationDatabase
from .database_import_result import DatabaseImportResult
from .database_reload_result import DatabaseReloadResult
from .translation_service import TranslationService


class DatabaseService:
    """
    Service class for managing the translation database.
    """

    LEGACY_STORAGE_DIR_NAMES: set[str] = {
        "local_mod_translations",
        "source_mod_translations",
    }
    """Folder names used by legacy databases to store hashed translation folders."""

    log: logging.Logger = logging.getLogger("DatabaseService")

    @classmethod
    def load_database(
        cls,
        appdb_path: Path,
        userdb_path: Path,
        language: GameLanguage,
        profiledb_path: Optional[Path] = None,
    ) -> TranslationDatabase:
        """
        Loads the translation database for the specified language from the specified
        paths. Creates a new user database if there is none for the specified language.

        Args:
            appdb_path (Path): Path to the application database directory.
            userdb_path (Path): Path to the shared user database directory.
            language (GameLanguage): Language to load the database for.
            profiledb_path (Optional[Path], optional): Active profile catalog directory.
                Defaults to `userdb_path`.

        Returns:
            TranslationDatabase: The loaded translation database.
        """

        cls.log.info(f"Loading translation database for '{language}'...")
        cls.log.debug(f"App database path: {appdb_path}")
        cls.log.debug(f"User database path: {userdb_path}")

        if not (userdb_path / language.id).is_dir():
            (userdb_path / language.id).mkdir(parents=True, exist_ok=True)

            index_path = userdb_path / language.id / "index.json"
            with open(index_path, "w", encoding="utf8") as index_file:
                json.dump([], index_file, indent=4)

            cls.log.info(f"Created new database for '{language}'.")

        active_profile_db_path: Path = profiledb_path or userdb_path
        if not (active_profile_db_path / language.id).is_dir():
            (active_profile_db_path / language.id).mkdir(parents=True, exist_ok=True)

        shared_translations: list[Translation] = cls.__load_user_database(
            userdb_path, userdb_path, language
        )
        if active_profile_db_path == userdb_path:
            user_translations: list[Translation] = shared_translations
        else:
            profile_translations: list[Translation] = cls.__load_user_database(
                active_profile_db_path, userdb_path, language
            )
            shared_by_id: dict[str, Translation] = {
                translation.id: translation for translation in shared_translations
            }
            user_translations = [
                shared_by_id[translation.id]
                for translation in profile_translations
                if translation.id in shared_by_id
            ]

        database = TranslationDatabase(
            userdb_path=userdb_path,
            profiledb_path=active_profile_db_path,
            appdb_path=appdb_path,
            language=language,
            vanilla_translation=cls.__load_vanilla_translation(appdb_path, language),
            user_translations=user_translations,
            shared_translations=shared_translations,
        )

        cls.log.info(
            f"Loaded database with {len(database.strings)} strings(s) from "
            f"{len(database.shared_translations) + 1} shared translation(s), "
            f"{len(database.user_translations)} active profile translation(s)."
        )

        return database

    @classmethod
    def __load_vanilla_translation(
        cls, appdb_path: Path, language: GameLanguage
    ) -> Translation:
        """
        Loads vanilla translation.

        Args:
            appdb_path (Path): Path to the application database directory.
            language (GameLanguage): Language to load the database for.
        """

        cls.log.info("Loading vanilla database...")

        translation = Translation(name="Base Game", path=appdb_path / language.id)
        translation.strings  # build cache of strings by "calling" the strings property  # noqa: B018

        cls.log.info(
            f"Loaded vanilla database for {len(translation.strings)} base game "
            "plugin(s)."
        )

        return translation

    @classmethod
    def __load_user_database(
        cls, index_path_root: Path, storage_path_root: Path, language: GameLanguage
    ) -> list[Translation]:
        """
        Loads user installed translation database.

        Args:
            index_path_root (Path): Root containing the profile index file.
            storage_path_root (Path): Root containing translation folders.
            language (GameLanguage): Language to load the database for.

        Returns:
            list[Translation]: List of loaded user translations.
        """

        cls.log.info("Loading user database...")

        db_path: Path = index_path_root / language.id
        storage_path: Path = storage_path_root / language.id
        translations: list[Translation] = []
        for translation_data in cls.__load_index_data(db_path):
            name: str = translation_data["name"]
            try:
                translation = Translation.from_index_data(translation_data, storage_path)
                translation.strings  # build cache of strings by "calling" the strings property  # noqa: B018
                translations.append(translation)
            except Exception as ex:
                cls.log.error(f"Failed to load translation '{name}': {ex}", exc_info=ex)

        cls.log.info(f"Loaded {len(translations)} user translation(s).")

        return translations

    @classmethod
    def __load_index_data(cls, db_path: Path) -> list[dict[str, Any]]:
        """
        Loads the raw index data of the user database at the specified path. Creates an
        empty index file if there is none.

        Args:
            db_path (Path): Path to the user database directory of a language.

        Returns:
            list[dict[str, Any]]: List of raw translation entries from the index file.
        """

        index_path: Path = db_path / "index.json"

        if not index_path.is_file():
            with index_path.open("w", encoding="utf8") as index_file:
                json.dump([], index_file)

        with index_path.open(encoding="utf8") as index_file:
            translation_list: list[dict[str, Any]] = json.load(index_file)

        return translation_list

    @classmethod
    def reload_database(
        cls, database: TranslationDatabase, pdisplay: Optional[ProgressDisplay] = None
    ) -> DatabaseReloadResult:
        """
        Reloads the user translations of the specified database from disk to apply
        changes that were made outside of the application. Existing translation objects
        are updated in-place, translations that were added to the index file are added
        and translations that were removed from the index file are removed from the
        database (without deleting their files). Translations that fail to load are
        left unchanged and reported as alerts to the `AlertManager`.

        Args:
            database (TranslationDatabase): The database to reload.
            pdisplay (Optional[ProgressDisplay], optional):
                Progress display to report the progress to. Defaults to None.

        Returns:
            DatabaseReloadResult: Summary of the reload.

        ## Emitted Signals:
            `TranslationDatabase.add_signal(translations)`:
                With the translations that were added to the index file.
            `TranslationDatabase.remove_signal(translations)`:
                With the translations that were removed from the index file.
            `TranslationDatabase.changed_signal(translation)`:
                For every successfully reloaded translation that was already in the
                database.
            `TranslationDatabase.reload_signal(translations, removed_modfiles)`:
                With the successfully reloaded translations that were already in the
                database.
            `TranslationDatabase.update_signal()`: Always.
        """

        cls.log.info(f"Reloading translation database for '{database.language}'...")

        db_path: Path = database.profiledb_path / database.language.id
        index_data: list[dict[str, Any]] = cls.__load_index_data(db_path)
        existing_translations: dict[str, Translation] = {
            translation.id: translation for translation in database.user_translations
        }
        shared_translations: dict[str, Translation] = {
            translation.id: translation for translation in database.shared_translations
        }

        # The path of a user translation is derived from its name, so the name is
        # sufficient to identify it. This also keeps translations whose index entry
        # is present but fails to load.
        indexed_names: set[str] = {
            str(entry["name"]).lower() for entry in index_data if "name" in entry
        }

        added_translations: list[Translation] = []
        reloaded_translations: list[Translation] = []
        removed_modfiles: list[Path] = []
        failed_count: int = 0
        for i, translation_data in enumerate(index_data):
            name: str = str(translation_data.get("name", ""))

            if pdisplay is not None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=f"{name} ({i + 1}/{len(index_data)})",
                        value=i,
                        maximum=len(index_data),
                    )
                )

            try:
                loaded_translation = Translation.from_index_data(
                    translation_data, database.userdb_path / database.language.id
                )
                existing_translation: Optional[Translation] = existing_translations.get(
                    loaded_translation.id
                )
                if existing_translation is None:
                    shared_translation: Optional[Translation] = shared_translations.get(
                        loaded_translation.id
                    )
                    if shared_translation is not None:
                        removed_modfiles.extend(
                            cls.__reload_translation(
                                shared_translation, loaded_translation
                            )
                        )
                        added_translations.append(shared_translation)
                    else:
                        loaded_translation.reload_strings()
                        added_translations.append(loaded_translation)
                else:
                    removed_modfiles.extend(
                        cls.__reload_translation(
                            existing_translation, loaded_translation
                        )
                    )
                    reloaded_translations.append(existing_translation)
            except (KeyError, OSError, ValidationError) as ex:
                failed_count += 1
                cls.__report_reload_failure(name, db_path / name, ex)

        removed_translations: list[Translation] = [
            translation
            for translation in existing_translations.values()
            if translation.name.lower() not in indexed_names
        ]

        cls.__apply_reload(
            database,
            added_translations,
            reloaded_translations,
            removed_translations,
            removed_modfiles,
        )

        result = DatabaseReloadResult(
            reloaded=len(reloaded_translations),
            added=len(added_translations),
            removed=len(removed_translations),
            failed=failed_count,
        )
        cls.log.info(f"Reloaded database: {result}")

        return result

    @classmethod
    def __reload_translation(
        cls, existing_translation: Translation, loaded_translation: Translation
    ) -> list[Path]:
        """
        Reloads the strings of an existing translation from disk and updates it
        in-place with the metadata of a freshly loaded translation. The translation is
        left unchanged if its strings fail to load.

        Args:
            existing_translation (Translation): Translation that is in the database.
            loaded_translation (Translation):
                Translation with the same ID that was freshly loaded from the index file.

        Raises:
            OSError: If a file of the translation could not be read.
            ValidationError: If a file of the translation contains invalid data.

        Returns:
            list[Path]: Paths of mod files that are no longer covered by the translation.
        """

        old_modfiles: set[Path] = set(existing_translation.strings)
        existing_translation.reload_strings()

        existing_translation.mod_id = loaded_translation.mod_id
        existing_translation.version = loaded_translation.version
        existing_translation.source = loaded_translation.source
        existing_translation.timestamp = loaded_translation.timestamp

        return list(old_modfiles - set(existing_translation.strings))

    @classmethod
    def __report_reload_failure(
        cls, name: str, path: Path, ex: KeyError | OSError | ValidationError
    ) -> None:
        """
        Logs a translation that failed to reload and reports it as an alert.

        Args:
            name (str): The name of the translation.
            path (Path): The path to the translation's folder.
            ex (KeyError | OSError | ValidationError):
                The exception that caused the failure.
        """

        cls.log.error(f"Failed to reload translation '{name}': {ex}", exc_info=ex)

        AlertManager.get().add_alert(
            Alert(
                severity=Alert.Severity.Error,
                title=QApplication.translate(
                    "DatabaseService", "Failed to reload translation '{name}'"
                ).format(name=name),
                summary=QApplication.translate(
                    "DatabaseService",
                    "The translation '{name}' could not be reloaded from disk and was "
                    "left unchanged.",
                ).format(name=name),
                details=format_exception(ex),
                context={
                    QApplication.translate("DatabaseService", "Translation"): name,
                    QApplication.translate("DatabaseService", "Path"): str(path),
                },
            )
        )

    @classmethod
    def __apply_reload(
        cls,
        database: TranslationDatabase,
        added_translations: list[Translation],
        reloaded_translations: list[Translation],
        removed_translations: list[Translation],
        removed_modfiles: list[Path],
    ) -> None:
        """
        Applies the result of a database reload to the specified database and emits the
        respective signals.

        Args:
            database (TranslationDatabase): The reloaded database.
            added_translations (list[Translation]): Translations to add.
            reloaded_translations (list[Translation]):
                Translations that were already in the database and got reloaded.
            removed_translations (list[Translation]): Translations to remove.
            removed_modfiles (list[Path]):
                Paths of mod files that are no longer covered by the reloaded
                translations.
        """

        for translation in removed_translations:
            database.user_translations.remove(translation)
            cls.log.info(f"Removed translation '{translation.name}' from database.")

        for translation in added_translations:
            database.user_translations.append(translation)
            if (
                database.user_translations is not database.shared_translations
                and not database.is_translation_in_shared_database(translation)
            ):
                database.shared_translations.append(translation)
            cls.log.info(f"Added translation '{translation.name}' to database.")

        if removed_translations:
            database.remove_signal.emit(removed_translations)

        if added_translations:
            database.add_signal.emit(added_translations)

        for translation in reloaded_translations:
            database.changed_signal.emit(translation)

        if reloaded_translations:
            database.reload_signal.emit(reloaded_translations, removed_modfiles)

        database.update_signal.emit()

    @classmethod
    def save_database(cls, database: TranslationDatabase) -> None:
        """
        Saves the translation database index (not the translations themselves).

        Args:
            database (TranslationDatabase): The database to save.
        """

        cls.log.info(f"Saving database index for '{database.language}'...")

        shared_index_path: Path = (
            database.userdb_path / database.language.id / "index.json"
        )
        shared_index_path.parent.mkdir(parents=True, exist_ok=True)
        shared_index_data: list[dict[str, Any]] = [
            translation.to_index_data()
            for translation in unique(database.shared_translations, key=lambda t: t.id)
        ]

        with shared_index_path.open("w", encoding="utf8") as index_file:
            json.dump(shared_index_data, index_file, indent=4, ensure_ascii=False)

        if database.profiledb_path != database.userdb_path:
            profile_index_path: Path = (
                database.profiledb_path / database.language.id / "index.json"
            )
            profile_index_path.parent.mkdir(parents=True, exist_ok=True)
            profile_index_data: list[dict[str, Any]] = [
                translation.to_index_data()
                for translation in unique(
                    database.user_translations, key=lambda t: t.id
                )
            ]
            with profile_index_path.open("w", encoding="utf8") as index_file:
                json.dump(profile_index_data, index_file, indent=4, ensure_ascii=False)

        cls.log.info("Database index saved.")

    @classmethod
    def synchronize_profile_with_modlist(
        cls, database: TranslationDatabase, mod_instance: ModInstance
    ) -> None:
        """
        Removes profile catalog entries that do not belong to the loaded modlist.

        Shared translation files are deliberately kept so another profile can still
        reference them.

        Args:
            database (TranslationDatabase): Database of the active profile.
            mod_instance (ModInstance): Loaded modlist.
        """

        if database.profiledb_path == database.userdb_path:
            return

        mod_ids: set[ModId] = {
            mod.mod_id for mod in mod_instance.mods if mod.mod_id is not None
        }
        modfile_paths: set[Path] = {
            modfile.path for mod in mod_instance.mods for modfile in mod.modfiles
        }
        removed_translations: list[Translation] = [
            translation
            for translation in database.user_translations
            if (
                translation.mod_id not in mod_ids
                and not any(
                    modfile_path in modfile_paths
                    for modfile_path in translation.strings
                )
            )
        ]

        if not removed_translations:
            return

        for translation in removed_translations:
            database.user_translations.remove(translation)

        database.remove_signal.emit(removed_translations)
        database.update_signal.emit()
        cls.save_database(database)
        cls.log.info(
            f"Removed {len(removed_translations)} stale profile translation(s)."
        )

    @classmethod
    def add_translation(
        cls, translation: Translation, database: TranslationDatabase, save: bool = True
    ) -> None:
        """
        Adds the specified translation to the specified translation database.
        Optionally saves the database.

        If a translation with the same ID (same name and path) is already in the database,
        the existing translation will be updated and their strings are merged.

        Args:
            translation (Translation): Translation to add.
            database (TranslationDatabase): Database to add the translation to.
            save (bool, optional): Whether to save the database. Defaults to True.

        ## Emitted Signals:
            `TranslationDatabase.add_signal([translation])`:
                If the translation wasn't in the database before.
            `TranslationDatabase.update_signal()`: Always.
        """

        cls.add_translations(translations=[translation], database=database, save=save)

    @classmethod
    def add_translations(
        cls,
        translations: list[Translation],
        database: TranslationDatabase,
        save: bool = True,
    ) -> None:
        """
        Adds the specified translations to the specified translation database.
        Optionally saves the database.

        If a translation with the same ID (same name and path) is already in the database,
        the existing translation will be updated and their strings are merged.

        Args:
            translations (list[Translation]): Translations to add.
            database (TranslationDatabase): Database to add the translations to.
            save (bool, optional): Whether to save the database. Defaults to True.

        ## Emitted Signals:
            `TranslationDatabase.add_signal(translations)`:
                With the translation that weren't in the database before.
            `TranslationDatabase.update_signal()`: Always.
        """

        added_translations: list[Translation] = []
        for translation in translations:
            was_visible: bool = database.is_translation_in_database(translation)
            shared_translation: Optional[Translation] = next(
                (
                    existing
                    for existing in database.shared_translations
                    if existing.id == translation.id
                ),
                None,
            )
            if shared_translation is None:
                database.shared_translations.append(translation)
                shared_translation = translation
                cls.log.info(f"Added translation '{translation.name}' to database.")
            elif shared_translation is not translation:
                cls.merge_translations(shared_translation, translation)
                cls.log.info(f"Updated translation '{translation.name}' in database.")

            if not was_visible:
                if database.user_translations is not database.shared_translations:
                    database.user_translations.append(shared_translation)
                added_translations.append(shared_translation)

        if added_translations:
            database.add_signal.emit(added_translations)

        database.update_signal.emit()

        if save:
            cls.save_database(database)

    @classmethod
    def merge_translations(
        cls, existing_translation: Translation, new_translation: Translation
    ) -> Translation:
        """
        Merges the new translation into the existing translation by updating the metadata
        and merging the strings.

        Args:
            existing_translation (Translation):
                Translation that already exists in the database.
            new_translation (Translation):
                Translation to merge into the existing translation.

        Returns:
            Translation: The merged translation.
        """

        cls.merge_translation_strings(
            existing_translation.strings, new_translation.strings
        )

        # Merge metadata
        existing_translation.mod_id = new_translation.mod_id
        existing_translation.version = new_translation.version

        return existing_translation

    @classmethod
    def merge_translation_strings(
        cls,
        existing_strings: dict[Path, StringList],
        new_strings: dict[Path, StringList],
    ) -> dict[Path, StringList]:
        """
        Merges the strings of two translations and removes duplicate strings.

        Args:
            existing_strings (dict[Path, StringList]): Strings that are merged into.
            new_strings (dict[Path, StringList]): New strings to merge.

        Returns:
            dict[Path, StringList]: The merged strings.
        """

        for modfile_name, modfile_strings in new_strings.items():
            existing_strings.setdefault(modfile_name, []).extend(modfile_strings)

            # Remove duplicates
            existing_strings[modfile_name] = StringUtils.unique(
                existing_strings[modfile_name]
            )

        return existing_strings

    @classmethod
    def delete_translation(
        cls, translation: Translation, database: TranslationDatabase, save: bool = True
    ) -> None:
        """
        Deletes the specified translation from the translation database.

        Args:
            translation (Translation): Translation to delete.
            database (TranslationDatabase): Database to delete from.
            save (bool, optional): Whether to save the database. Defaults to True.

        ## Emitted Signals:
            `TranslationDatabase.remove_signal([translation])`:
                If the translation was in the database.
            `TranslationDatabase.update_signal()`: Always.
        """

        cls.delete_translations(translations=[translation], database=database, save=save)

    @classmethod
    def delete_translations(
        cls,
        translations: list[Translation],
        database: TranslationDatabase,
        save: bool = True,
    ) -> None:
        """
        Deletes the specified translations from the translation database.

        Args:
            translations (list[Translation]): Translations to delete.
            database (TranslationDatabase): Database to delete from.
            save (bool, optional): Whether to save the database. Defaults to True.

        ## Emitted Signals:
            `TranslationDatabase.remove_signal(translations)`:
                With every translation that was in the database.
            `TranslationDatabase.update_signal()`: Always.
        """

        deleted_translations: list[Translation] = []
        for translation in translations:
            if database.is_translation_in_database(translation):
                database.user_translations.remove(translation)
                deleted_translations.append(translation)
                cls.log.info(f"Deleted translation '{translation.name}' from database.")

            if database.profiledb_path == database.userdb_path:
                shutil.rmtree(translation.path, ignore_errors=True)
                if database.is_translation_in_shared_database(translation):
                    database.shared_translations.remove(translation)

        if deleted_translations:
            database.remove_signal.emit(deleted_translations)

        database.update_signal.emit()

        if save:
            cls.save_database(database)

    @classmethod
    def rename_translation(
        cls,
        translation: Translation,
        new_name: str,
        database: TranslationDatabase,
        save: bool = True,
    ) -> None:
        """
        Renames a translation and its folder.

        Args:
            translation (Translation): Translation to rename.
            new_name (str): New name for the translation.
            database (TranslationDatabase): Database to rename in.
            save (bool, optional):
                Whether to save the database if the translation is in the database.
                Defaults to True.

        ## Emitted Signals:
            `TranslationDatabase.rename_signal(translation)`: If the translation is in the database.
            `TranslationDatabase.update_signal()`: If the translation is in the database.
        """

        old_name: str = translation.name
        new_path: Path = database.userdb_path / database.language.id / new_name
        os.rename(translation.path, new_path)
        translation.name = new_name
        translation.path = new_path

        cls.log.info(f"Renamed translation '{old_name}' to '{new_name}'.")

        if (
            database.is_translation_in_database(translation)
            or database.is_translation_in_shared_database(translation)
        ) and save:
            cls.save_database(database)
            cls.__rename_in_other_profile_indexes(
                old_name=old_name, new_name=new_name, database=database
            )

        if database.is_translation_in_database(translation):
            database.rename_signal.emit(translation)
            database.update_signal.emit()

    @classmethod
    def __rename_in_other_profile_indexes(
        cls,
        old_name: str,
        new_name: str,
        database: TranslationDatabase,
    ) -> None:
        """
        Updates the renamed translation entry in all other profile catalogs.

        Args:
            old_name (str): Previous translation name.
            new_name (str): New translation name.
            database (TranslationDatabase): Database whose shared directory is used.
        """

        profiles_root: Path = database.userdb_path.parent.parent / "profiles"
        if not profiles_root.is_dir():
            return

        active_index_path: Path = (
            database.profiledb_path / database.language.id / "index.json"
        )
        for profile_dir in profiles_root.iterdir():
            if not profile_dir.is_dir():
                continue

            profile_index_path: Path = (
                profile_dir / "user" / "database" / database.language.id / "index.json"
            )
            if (
                profile_index_path == active_index_path
                or not profile_index_path.is_file()
            ):
                continue

            index_data: list[dict[str, Any]] = cls.__load_index_data(
                profile_index_path.parent
            )
            updated: bool = False
            for entry in index_data:
                if str(entry.get("name", "")).lower() == old_name.lower():
                    entry["name"] = new_name
                    updated = True

            if updated:
                with profile_index_path.open("w", encoding="utf8") as index_file:
                    json.dump(index_data, index_file, indent=4, ensure_ascii=False)

    @classmethod
    def create_blank_translation(
        cls,
        name: str,
        strings: dict[Path, StringList],
        database: TranslationDatabase,
    ) -> Translation:
        """
        Creates a blank translation with the specified name and strings.

        Args:
            name (str): The name of the translation.
            strings (dict[Path, StringList]): Strings to add to the translation.
            database (TranslationDatabase):
                Database to determine the translation's path but the translation doesn't
                get added to it by this method.

        Returns:
            Translation: The created translation.
        """

        path: Path = database.userdb_path / database.language.id / name
        return Translation.create(name=name, path=path, strings=strings)

    @classmethod
    def create_translation_for_mod(
        cls,
        mod: Mod,
        database: TranslationDatabase,
        only_complete_coverage: bool = False,
        apply_db: bool = True,
        add_and_save: bool = True,
    ) -> Translation:
        """
        Creates a translation for the specified mod.

        Args:
            mod (Mod): Mod to create translation for.
            database (TranslationDatabase): Database to add the translation to.
            only_complete_coverage (bool, optional):
                Whether to only create translations for mod files that are completely
                covered by the database. Defaults to False.
            apply_db (bool, optional): Whether to apply database. Defaults to True.
            add_and_save (bool, optional):
                Whether to add the translation to the database and save them. Defaults to
                True.

        Returns:
            Translation: The created translation.
        """

        cls.log.info(f"Creating translation for mod '{mod.name}'...")

        # Match by the installed mod identity or its plugin paths. The version is not
        # part of either lookup, so a newer mod build can reuse the shared translation.
        translation: Optional[Translation] = database.get_translation_by_mod(mod)
        if translation is None:
            translation = database.get_shared_translation_by_mod(mod)
        if translation is None:
            translation = cls.create_blank_translation(
                name=mod.name + " - " + database.language.name,
                strings={},
                database=database,
            )

        relevant_modfiles: list[ModFile] = list(
            filter(
                lambda modfile: (
                    modfile.status
                    not in [
                        TranslationStatus.NoStrings,
                        TranslationStatus.TranslationInstalled,
                        TranslationStatus.IsTranslated,
                    ]
                    and (modfile.path not in translation.strings)
                    and (
                        not only_complete_coverage
                        or modfile.status
                        == TranslationStatus.TranslationAvailableInDatabase
                    )
                ),
                mod.modfiles,
            )
        )

        if not relevant_modfiles:
            if (
                add_and_save
                and database.is_translation_in_shared_database(translation)
                and not database.is_translation_in_database(translation)
            ):
                cls.add_translation(translation, database)
            return translation

        translation_strings: dict[Path, StringList] = translation.strings
        for modfile in relevant_modfiles:
            modfile_strings: StringList = modfile.get_strings()

            for string in modfile_strings:
                string.string = string.original

            if apply_db:
                StringUtils.match_strings(
                    strings_to_update=modfile_strings, database_strings=database.strings
                )

            translation_strings.setdefault(modfile.path, []).extend(modfile_strings)

        translation.strings = translation_strings
        translation.remove_duplicates(save=False)

        if add_and_save:
            translation.save()
            cls.add_translation(translation, database)

        cls.log.info(
            f"Created translation with strings for {len(translation.strings)} "
            "modfile(s)."
        )

        return translation

    @classmethod
    def create_translation_for_modfile(
        cls,
        modfile: ModFile,
        database: TranslationDatabase,
        apply_db: bool = True,
        add_and_save: bool = True,
    ) -> Translation:
        """
        Creates a translation for the specified mod file.

        Args:
            modfile (ModFile): Mod file to create translation for.
            database (TranslationDatabase): Database to add the translation to.
            apply_db (bool, optional): Whether to apply database. Defaults to True.
            add_and_save (bool, optional):
                Whether to add the translation to the database and save them. Defaults to
                True.

        Returns:
            Translation: The created translation.
        """

        cls.log.info(f"Creating translation for mod file '{modfile.full_path}'...")

        translation: Optional[Translation] = database.get_translation_by_modfile_path(
            modfile.path
        )
        if translation is None:
            translation = database.get_shared_translation_by_modfile_path(modfile.path)
        if translation is None:
            translation = cls.create_blank_translation(
                name=modfile.name + " - " + database.language.name,
                strings={},
                database=database,
            )

        modfile_strings: StringList = modfile.get_strings()
        for string in modfile_strings:
            string.string = string.original

        if apply_db:
            StringUtils.match_strings(
                strings_to_update=modfile_strings, database_strings=database.strings
            )

        translation.strings.setdefault(modfile.path, []).extend(modfile_strings)
        translation.remove_duplicates(save=False)

        if add_and_save:
            translation.save()
            cls.add_translation(translation, database)

        cls.log.info(f"Created translation with {len(modfile_strings)} string(s).")

        return translation

    @classmethod
    def create_translation_from_mod(
        cls,
        mod: Mod,
        original_mod: Optional[Mod],
        strings: dict[Path, StringList],
        database: TranslationDatabase,
        add_and_save: bool = True,
    ) -> Translation:
        """
        Creates a translation from the metadata of the specified mod and the specified
        merged (!) strings.

        Args:
            mod (Mod): Mod to create translation from.
            original_mod (Optional[Mod]): Original mod that is translated.
            strings (dict[Path, StringList]): **Merged** strings to add to the translation.
            database (TranslationDatabase): Database to add the translation to.
            add_and_save (bool, optional):
                Whether to add the translation to the database and save them. Defaults
                to True.

        Returns:
            Translation: The created translation.
        """

        translation: Optional[Translation] = database.get_translation_by_mod(mod)
        if translation is None:
            translation = Translation(
                name=mod.name,
                path=database.userdb_path / database.language.id / mod.name,
                mod_id=mod.mod_id,
                version=mod.version,
                strings_={},
                source=mod.mod_id.source if mod.mod_id is not None else Source.Local,
            )

        translation.strings = cls.merge_translation_strings(translation.strings, strings)

        if add_and_save:
            translation.save()
            cls.add_translation(translation, database)

        return translation

    @classmethod
    def import_database_folder(
        cls,
        folder_path: Path,
        database: TranslationDatabase,
        pdisplay: Optional[ProgressDisplay] = None,
    ) -> DatabaseImportResult:
        """
        Imports translations from a legacy database directory or a single translation
        folder into the specified translation database.

        Args:
            folder_path (Path):
                Path to the database folder (or single translation folder) to import.
            database (TranslationDatabase): The target translation database.
            pdisplay (Optional[ProgressDisplay], optional):
                Progress display to report the import progress to. Defaults to None.

        Returns:
            DatabaseImportResult: Summary of the import operation.
        """

        return cls.import_database_folders(
            folder_paths=[folder_path], database=database, pdisplay=pdisplay
        )

    @classmethod
    def import_database_folders(
        cls,
        folder_paths: list[Path],
        database: TranslationDatabase,
        pdisplay: Optional[ProgressDisplay] = None,
    ) -> DatabaseImportResult:
        """
        Imports translations from one or more legacy database folders or individual
        translation folders into the specified translation database. Both indexed entries
        and unindexed existing folders on disk are recovered. Existing translations and
        already-covered mod files in the target database are skipped without modification.

        Args:
            folder_paths (list[Path]): Paths to database or translation folders.
            database (TranslationDatabase): The target translation database.
            pdisplay (Optional[ProgressDisplay], optional):
                Progress display to report the import progress to. Defaults to None.

        Returns:
            DatabaseImportResult: Summary of the import operation.
        """

        cls.log.info(
            f"Importing translation folder(s) into '{database.language}' database..."
        )

        candidates: list[tuple[Translation, Path]]
        failed_count: int
        candidates, failed_count = cls.__collect_import_candidates(
            folder_paths, database.language
        )

        target_db_dir: Path = database.userdb_path / database.language.id
        target_db_dir.mkdir(parents=True, exist_ok=True)

        existing_names: set[str] = {
            translation.name.lower() for translation in database.shared_translations
        }
        existing_mod_ids: set[ModId] = {
            translation.mod_id
            for translation in database.shared_translations
            if translation.mod_id is not None
        }
        covered_modfiles: set[str] = {
            DatabaseService.__normalize_modfile_key(modfile_path)
            for translation in database.shared_translations
            for modfile_path in translation.strings
        }

        added_translations: list[Translation] = []
        skipped_count: int = 0

        for i, (candidate, source_path) in enumerate(candidates):
            if pdisplay is not None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=f"{candidate.name} ({i + 1}/{len(candidates)})",
                        value=i,
                        maximum=len(candidates),
                    )
                )

            if (source_path / OUTPUT_MOD_MARKER_FILENAME).is_file():
                skipped_count += 1
                continue

            json_files: list[Path] = [
                json_file
                for json_file in source_path.rglob("*.json")
                if TranslationService.is_translation_json_file(json_file)
            ]
            if not json_files:
                skipped_count += 1
                cls.log.debug(
                    f"Skipping folder '{source_path}' without valid translation files."
                )
                continue

            if (
                source_path.parent.name.lower()
                in DatabaseService.LEGACY_STORAGE_DIR_NAMES
                and candidate.name == source_path.name
            ):
                first_modfile: Path = rem_last_suffix(json_files[0]).relative_to(
                    source_path
                )
                candidate.name = f"{first_modfile.name} - {database.language.name}"

            normalized_name: str = DatabaseService.__normalize_translation_name(
                candidate.name
            )
            uncovered_json_files: list[tuple[Path, Path]] = [
                (
                    rem_last_suffix(json_file).relative_to(source_path),
                    json_file,
                )
                for json_file in json_files
                if (
                    DatabaseService.__normalize_modfile_key(
                        rem_last_suffix(json_file).relative_to(source_path)
                    )
                    not in covered_modfiles
                )
            ]

            if (
                normalized_name.lower() in existing_names
                or (
                    candidate.mod_id is not None and candidate.mod_id in existing_mod_ids
                )
                or not uncovered_json_files
            ):
                skipped_count += 1
                continue

            try:
                strings: dict[Path, StringList] = cls.__load_uncovered_strings(
                    uncovered_json_files
                )
            except (OSError, ValidationError) as ex:
                failed_count += 1
                cls.__report_import_failure(normalized_name, source_path, ex)
                continue

            if not strings:
                skipped_count += 1
                continue

            candidate.name = normalized_name
            candidate.path = target_db_dir / normalized_name
            candidate.strings = strings
            candidate.remove_duplicates(save=False)
            candidate.save()
            candidate.size  # build size cache on worker thread  # noqa: B018

            existing_names.add(normalized_name.lower())
            if candidate.mod_id is not None:
                existing_mod_ids.add(candidate.mod_id)
            for modfile_path in candidate.strings:
                covered_modfiles.add(
                    DatabaseService.__normalize_modfile_key(modfile_path)
                )

            added_translations.append(candidate)
            cls.log.debug(f"Imported new translation '{candidate.name}'.")

        cls.__finalize_import(
            database=database,
            added_translations=added_translations,
        )

        result = DatabaseImportResult(
            imported=len(added_translations),
            skipped=skipped_count,
            failed=failed_count,
        )
        cls.log.info(f"Finished importing database folder(s): {result}")

        return result

    @staticmethod
    def __load_uncovered_strings(
        uncovered_json_files: list[tuple[Path, Path]],
    ) -> dict[Path, StringList]:
        """
        Loads translation string lists for the specified uncovered JSON files.

        Args:
            uncovered_json_files (list[tuple[Path, Path]]):
                Pairs of `(modfile_path, json_file_path)` to load.

        Raises:
            OSError: If a JSON file cannot be read.
            ValidationError: If a JSON file contains malformed string data.

        Returns:
            dict[Path, StringList]: Non-empty string lists keyed by mod file path.
        """

        strings: dict[Path, StringList] = {}
        for modfile_path, json_file in uncovered_json_files:
            loaded_strings: StringList = StringLoader.load_strings_from_json_file(
                json_file
            )
            if loaded_strings:
                strings[modfile_path] = loaded_strings

        return strings

    @classmethod
    def __finalize_import(
        cls,
        database: TranslationDatabase,
        added_translations: list[Translation],
    ) -> None:
        """
        Applies newly imported translations to the database, emits signals and persists
        the index file.

        Args:
            database (TranslationDatabase): Target translation database.
            added_translations (list[Translation]): Newly imported translations.
        """

        if not added_translations:
            return

        cls.add_translations(
            translations=added_translations, database=database, save=True
        )

    @classmethod
    def __collect_import_candidates(
        cls, folder_paths: list[Path], language: GameLanguage
    ) -> tuple[list[tuple[Translation, Path]], int]:
        """
        Collects all candidate translations and their source directories from the
        specified folder paths.

        Args:
            folder_paths (list[Path]): Input folder paths to scan.
            language (GameLanguage): Target game language.

        Returns:
            tuple[list[tuple[Translation, Path]], int]:
                List of `(Translation, source_path)` pairs and the number of failed index
                entries.
        """

        candidates: list[tuple[Translation, Path]] = []
        failed_count: int = 0
        for folder_path in folder_paths:
            folder_candidates: list[tuple[Translation, Path]]
            folder_failed: int
            folder_candidates, folder_failed = (
                cls.__collect_import_candidates_from_folder(folder_path, language)
            )
            candidates.extend(folder_candidates)
            failed_count += folder_failed

        return candidates, failed_count

    @classmethod
    def __collect_import_candidates_from_folder(
        cls, folder_path: Path, language: GameLanguage
    ) -> tuple[list[tuple[Translation, Path]], int]:
        """
        Collects candidate translations from a single folder path (either a single
        translation folder or a database directory).

        Args:
            folder_path (Path): Folder path to inspect.
            language (GameLanguage): Target game language.

        Returns:
            tuple[list[tuple[Translation, Path]], int]:
                List of `(Translation, source_path)` pairs and the number of failed index
                entries.
        """

        resolved_folder: Path = DatabaseService.__resolve_database_folder(
            folder_path, language
        )
        if not resolved_folder.is_dir():
            return [], 0

        if DatabaseService.__is_single_translation_folder(resolved_folder):
            name: str = DatabaseService.__normalize_translation_name(
                resolved_folder.name
            )
            return [(Translation(name=name, path=resolved_folder), resolved_folder)], 0

        candidates: list[tuple[Translation, Path]] = []
        covered_paths: set[str] = set()
        covered_root_names: set[str] = set()
        failed_count: int = 0

        index_path: Path = resolved_folder / "index.json"
        if index_path.is_file():
            failed_count += cls.__collect_indexed_candidates(
                resolved_folder=resolved_folder,
                index_path=index_path,
                candidates=candidates,
                covered_paths=covered_paths,
                covered_root_names=covered_root_names,
            )

        cls.__collect_unindexed_disk_candidates(
            resolved_folder=resolved_folder,
            candidates=candidates,
            covered_paths=covered_paths,
            covered_root_names=covered_root_names,
        )

        return candidates, failed_count

    @classmethod
    def __collect_indexed_candidates(
        cls,
        resolved_folder: Path,
        index_path: Path,
        candidates: list[tuple[Translation, Path]],
        covered_paths: set[str],
        covered_root_names: set[str],
    ) -> int:
        """
        Populates import candidates from an existing `index.json` file.

        Args:
            resolved_folder (Path): Database folder containing the index file.
            index_path (Path): Path to the `index.json` file.
            candidates (list[tuple[Translation, Path]]): List to append candidates to.
            covered_paths (set[str]): Set of normalized folder paths already covered.
            covered_root_names (set[str]): Set of lowercase root folder names covered.

        Returns:
            int: Number of index entries that failed to parse.
        """

        failed_count: int = 0
        try:
            with index_path.open(encoding="utf8") as index_file:
                raw_index: Any = json.load(index_file)
        except (OSError, ValueError) as ex:
            cls.__report_import_failure("index.json", index_path, ex)
            return 1

        if not isinstance(raw_index, list):
            return 0

        for entry in raw_index:
            if not isinstance(entry, dict):
                continue

            raw_name: str = str(entry.get("name", ""))
            try:
                loaded_translation = Translation.from_index_data(entry, resolved_folder)
                normalized_name: str = DatabaseService.__normalize_translation_name(
                    loaded_translation.name
                )
                loaded_translation.name = normalized_name
                source_path: Path = loaded_translation.path
                if not source_path.is_dir():
                    fallback_path: Path = resolved_folder / normalized_name
                    if fallback_path.is_dir():
                        source_path = fallback_path

                if not source_path.is_dir():
                    continue

                covered_paths.add(DatabaseService.__normalize_folder_key(source_path))
                if source_path.parent == resolved_folder:
                    covered_root_names.add(normalized_name.lower())

                candidates.append((loaded_translation, source_path))
            except (KeyError, OSError, ValidationError) as ex:
                failed_count += 1
                cls.__report_import_failure(raw_name, resolved_folder / raw_name, ex)

        return failed_count

    @classmethod
    def __collect_unindexed_disk_candidates(
        cls,
        resolved_folder: Path,
        candidates: list[tuple[Translation, Path]],
        covered_paths: set[str],
        covered_root_names: set[str],
    ) -> None:
        """
        Scans the database directory on disk and appends any existing translation
        folders that were not already listed in `index.json`.

        Args:
            resolved_folder (Path): Database directory to scan.
            candidates (list[tuple[Translation, Path]]): List to append candidates to.
            covered_paths (set[str]): Set of normalized folder paths already covered.
            covered_root_names (set[str]): Set of lowercase root folder names covered.
        """

        subdirs: list[Path] = sorted(
            (path for path in resolved_folder.iterdir() if path.is_dir()),
            key=lambda path: path.name.lower(),
        )
        for subdir in subdirs:
            if subdir.name.lower() in DatabaseService.LEGACY_STORAGE_DIR_NAMES:
                hashed_dirs: list[Path] = sorted(
                    (path for path in subdir.iterdir() if path.is_dir()),
                    key=lambda path: path.name.lower(),
                )
                for hashed_dir in hashed_dirs:
                    hashed_key: str = DatabaseService.__normalize_folder_key(hashed_dir)
                    if hashed_key not in covered_paths:
                        covered_paths.add(hashed_key)
                        candidates.append(
                            (
                                Translation(name=hashed_dir.name, path=hashed_dir),
                                hashed_dir,
                            )
                        )
                continue

            normalized_name: str = DatabaseService.__normalize_translation_name(
                subdir.name
            )
            folder_key: str = DatabaseService.__normalize_folder_key(subdir)
            if (
                folder_key in covered_paths
                or normalized_name.lower() in covered_root_names
            ):
                continue

            covered_paths.add(folder_key)
            covered_root_names.add(normalized_name.lower())
            candidates.append((Translation(name=normalized_name, path=subdir), subdir))

    @staticmethod
    def __resolve_database_folder(folder_path: Path, language: GameLanguage) -> Path:
        """
        Resolves a user-selected directory to the language-specific database folder when
        a parent `database` or `data` folder was selected.

        Args:
            folder_path (Path): Selected folder path.
            language (GameLanguage): Target language of the active database.

        Returns:
            Path: Resolved folder path.
        """

        if not (folder_path / "index.json").is_file():
            language_dir: Path = folder_path / language.id
            if language_dir.is_dir():
                return language_dir

            nested_language_dir: Path = folder_path / "user" / "database" / language.id
            if nested_language_dir.is_dir():
                return nested_language_dir

        return folder_path

    @staticmethod
    def __is_single_translation_folder(folder_path: Path) -> bool:
        """
        Determines whether a folder is an individual translation folder rather than a
        parent database directory containing multiple translation folders.

        Args:
            folder_path (Path): Folder path to inspect.

        Returns:
            bool: `True` if `folder_path` directly represents a single translation.
        """

        if (folder_path / "index.json").is_file() or (
            folder_path / OUTPUT_MOD_MARKER_FILENAME
        ).is_file():
            return False

        if any(
            TranslationService.is_translation_json_file(file)
            for file in folder_path.glob("*.json")
        ):
            return True

        interface_dir: Path = folder_path / "interface"
        return interface_dir.is_dir() and any(
            TranslationService.is_translation_json_file(file)
            for file in interface_dir.rglob("*.json")
        )

    @staticmethod
    def __normalize_translation_name(name: str) -> str:
        """
        Normalizes a translation name by stripping trailing dots and spaces that Windows
        filesystems remove from directory names.

        Args:
            name (str): Raw translation name.

        Returns:
            str: Normalized translation name.
        """

        stripped: str = name.rstrip(". ")
        return stripped if stripped else name

    @staticmethod
    def __normalize_folder_key(folder_path: Path) -> str:
        """
        Produces a case-insensitive normalized key for a directory path.

        Args:
            folder_path (Path): Directory path to normalize.

        Returns:
            str: Normalized path key.
        """

        return os.path.normcase(str(folder_path.resolve()))

    @staticmethod
    def __normalize_modfile_key(modfile_path: Path) -> str:
        """
        Produces a case-insensitive normalized key for a relative mod file path.

        Args:
            modfile_path (Path): Relative mod file path to normalize.

        Returns:
            str: Normalized mod file key.
        """

        return modfile_path.as_posix().lower()

    @classmethod
    def __report_import_failure(cls, name: str, path: Path, ex: Exception) -> None:
        """
        Logs a translation that failed to import and reports it as an alert.

        Args:
            name (str): The name of the translation.
            path (Path): The path to the translation's folder.
            ex (Exception): The exception that caused the failure.
        """

        cls.log.error(f"Failed to import translation '{name}': {ex}", exc_info=ex)

        AlertManager.get().add_alert(
            Alert(
                severity=Alert.Severity.Error,
                title=QApplication.translate(
                    "DatabaseService", "Failed to import translation '{name}'"
                ).format(name=name),
                summary=QApplication.translate(
                    "DatabaseService",
                    "The translation '{name}' could not be imported from disk.",
                ).format(name=name),
                details=format_exception(ex),
                context={
                    QApplication.translate("DatabaseService", "Translation"): name,
                    QApplication.translate("DatabaseService", "Path"): str(path),
                },
            )
        )
