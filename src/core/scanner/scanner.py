"""
Copyright (c) Cutleast
"""

import logging
from concurrent.futures import Future, as_completed
from pathlib import Path
from threading import Lock
from typing import Optional

from cutleast_core_lib.core.multithreading.progress import (
    ProgressUpdate,
    UpdateCallback,
    update,
)
from cutleast_core_lib.core.multithreading.progress_executor import ProgressExecutor
from cutleast_core_lib.core.utilities.unique import unique
from cutleast_core_lib.ui.progress.display import ProgressDisplay
from PySide6.QtCore import QObject

from core.config.app_config import AppConfig
from core.config.user_config import UserConfig
from core.database.database import TranslationDatabase
from core.database.database_service import DatabaseService
from core.database.translation import Translation
from core.file_types.bestiary.file import BestiaryFile
from core.masterlist.masterlist import Masterlist
from core.masterlist.masterlist_entry import MasterlistEntry
from core.mod_file.mod_file import ModFile
from core.mod_file.translation_status import TranslationStatus
from core.mod_instance.mod import Mod
from core.mod_instance.mod_instance import ModInstance
from core.string.search_filter import SearchFilter, matches_filter
from core.string.string_extractor import StringExtractor
from core.string.string_status import StringStatus
from core.string.string_utils import StringUtils
from core.string.types import StringList, StringType
from core.translation_provider.mod_id import ModId
from core.translation_provider.provider import TranslationProvider
from core.translation_provider.source import Source

from .detector import LangDetector, Language


class Scanner(QObject):
    """
    Class for various scanning actions on the loaded modlist.
    """

    log: logging.Logger = logging.getLogger("Scanner")

    __mod_instance: ModInstance
    __database: TranslationDatabase
    __app_config: AppConfig
    __user_config: UserConfig
    __provider: TranslationProvider
    __masterlist: Masterlist
    __detector: LangDetector

    def __init__(
        self,
        mod_instance: ModInstance,
        database: TranslationDatabase,
        app_config: AppConfig,
        user_config: UserConfig,
        provider: TranslationProvider,
        masterlist: Masterlist,
    ) -> None:
        """
        Args:
            mod_instance (ModInstance): The loaded mod instance.
            database (TranslationDatabase): The translation database.
            app_config (AppConfig): The application configuration.
            user_config (UserConfig): The user configuration.
            provider (TranslationProvider): The translation provider.
            masterlist (Masterlist): The loaded masterlist.
        """

        super().__init__()

        self.__mod_instance = mod_instance
        self.__database = database
        self.__app_config = app_config
        self.__user_config = user_config
        self.__provider = provider
        self.__masterlist = masterlist
        self.__detector = LangDetector(
            self.__app_config.detector_confidence,
            getattr(Language, self.__user_config.language.id.upper()),
        )
        self.__translation_lock = Lock()

    def run_basic_scan(
        self,
        items: dict[Mod, list[ModFile]],
        pdisplay: Optional[ProgressDisplay] = None,
        apply_db: Optional[bool] = None,
    ) -> dict[Mod, dict[ModFile, TranslationStatus]]:
        """
        Scans mods for required and installed translations.
        Automatically imports installed translations if enabled by the user.

        Args:
            items (dict[Mod, list[ModFile]]): The items to scan.
            pdisplay (Optional[ProgressDisplay], optional):
                Optional progress display. Defaults to None.
            apply_db (Optional[bool], optional):
                Whether to apply database translations. Defaults to None (uses app config).

        Returns:
            dict[Mod, dict[ModFile, TranslationStatus]]:
                A dictionary of mods, their mod files and their status.
        """

        total_modfiles: int = sum(len(modfiles) for modfiles in items.values())
        self.log.info(
            f"Scanning {len(items)} mod(s) with {total_modfiles} mod file(s)..."
        )

        if pdisplay is not None:
            pdisplay.updateMainProgress(
                ProgressUpdate(
                    status_text=self.tr("Scanning modlist..."), value=0, maximum=0
                )
            )

        database_originals: set[str] = {
            string.original
            for string in self.__database.strings
            if string.status != StringStatus.TranslationRequired
        }

        database_translations: dict[str, tuple[Translation, StringList]] = {}
        for translation in self.__database.user_translations:
            for modfile_key, strings in translation.strings.items():
                norm_key: str = str(modfile_key).lower().replace("\\", "/")
                database_translations[norm_key] = (translation, strings)

        if apply_db is None:
            apply_db = self.__app_config.auto_create_database_translations

        db_lookup_maps = None
        if apply_db:
            db_lookup_maps = StringUtils._build_lookup_maps(self.__database.strings)

        scan_result: dict[Mod, dict[ModFile, TranslationStatus]] = {
            mod: {} for mod in items
        }
        scan_targets: dict[
            str, tuple[Mod, ModFile, list[tuple[Mod, ModFile]]]
        ] = {}
        for mod, modfiles in items.items():
            for modfile in modfiles:
                winning_modfile = self.__mod_instance.get_modfile(modfile.path)
                if winning_modfile is None:
                    winning_modfile = modfile

                winning_mod = (
                    self.__mod_instance.get_mod_with_modfile(winning_modfile.path)
                    or mod
                )
                key = str(winning_modfile.path).lower().replace("\\", "/")
                target = scan_targets.setdefault(
                    key, (winning_mod, winning_modfile, [])
                )
                target[2].append((mod, modfile))

        failed_modfiles: int = 0
        with ProgressExecutor(
            pdisplay, max_workers=self.__app_config.worker_thread_num
        ) as executor:
            executor.set_main_progress_text(self.tr("Scanning modlist..."))

            tasks: dict[
                Future[TranslationStatus], tuple[Mod, ModFile, list[tuple[Mod, ModFile]]]
            ] = {}
            for mod, modfile, references in scan_targets.values():
                future: Future[TranslationStatus] = executor.submit(
                    lambda ucb, m=mod, mf=modfile: self.__basic_scan_modfile(
                        mod=m,
                        modfile=mf,
                        database_originals=database_originals,
                        database_translations=database_translations,
                        db_lookup_maps=db_lookup_maps,
                        apply_db=apply_db,
                        update_callback=ucb,
                    )
                )
                tasks[future] = (mod, modfile, references)

            for future in as_completed(tasks):
                mod, modfile, references = tasks[future]
                try:
                    status = future.result()
                    for reference_mod, reference_modfile in references:
                        scan_result[reference_mod][reference_modfile] = status
                except Exception as ex:
                    failed_modfiles += 1
                    self.log.error(
                        f"Failed to scan '{mod.name}' > '{modfile.name}': {ex}",
                        exc_info=ex,
                    )

        self.log.info("Modlist scan complete.")
        self.log.info(f"Status summary: {self.__create_status_summary(scan_result)}")

        return scan_result

    def __basic_scan_modfile(
        self,
        mod: Mod,
        modfile: ModFile,
        database_originals: set[str],
        database_translations: dict[str, tuple[Translation, StringList]],
        db_lookup_maps: Optional[
            tuple[
                dict[str, StringType],
                dict[str, StringType],
                dict[str, StringType],
                dict[str, StringType],
            ]
        ] = None,
        apply_db: bool = False,
        update_callback: Optional[UpdateCallback] = None,
    ) -> TranslationStatus:
        modfile_path_text: str = f"{mod.name} > {modfile.name}"
        self.log.debug(f"Scanning {modfile_path_text}...")

        update(
            update_callback,
            ProgressUpdate(
                status_text=self.tr("{item_name}: Extracting strings...").format(
                    item_name=modfile_path_text
                ),
                value=0,
                maximum=0,
            ),
        )

        self.log.debug("Extracting strings...")
        modfile_strings: StringList = list(
            filter(
                lambda s: s.status != StringStatus.NoTranslationRequired,
                modfile.get_strings(),
            )
        )
        if not len(modfile_strings):
            return TranslationStatus.NoStrings

        update(
            update_callback,
            ProgressUpdate(
                status_text=self.tr("{item_name}: Detecting language...").format(
                    item_name=modfile_path_text
                ),
            ),
        )

        self.log.debug("Detecting language...")

        status: TranslationStatus
        norm_path: str = str(modfile.path).lower().replace("\\", "/")
        if self.__detector.requires_translation(modfile_strings):
            if norm_path in database_translations:
                translation, trans_strings = database_translations[norm_path]

                if (
                    isinstance(modfile, BestiaryFile)
                    and self.__detector.detect_lang(
                        "\n".join(
                            list(
                                dict.fromkeys(
                                    string.original for string in modfile_strings
                                )
                            )[:39]
                        )
                    )
                    is None
                    and self.__bestiary_strings_match_translation(
                        modfile_strings, trans_strings
                    )
                ):
                    self.log.debug(
                        f"Bestiary file '{modfile_path_text}' matches its installed "
                        "database translation; language detection was inconclusive."
                    )
                    return TranslationStatus.IsTranslated

                required_string_ids: set[str] = {
                    string.id for string in modfile_strings
                }
                has_incomplete: bool = any(
                    string.id in required_string_ids
                    and string.status > StringStatus.TranslationComplete
                    for string in trans_strings
                )
                translated_string_ids: set[str] = {
                    string.id for string in trans_strings
                }
                is_partially_covered: bool = not required_string_ids.issubset(
                    translated_string_ids
                )

                if (has_incomplete or is_partially_covered) and apply_db:
                    changed = False
                    if is_partially_covered:
                        extracted = [
                            string
                            for string in modfile.get_strings()
                            if string.status != StringStatus.NoTranslationRequired
                        ]
                        translated_string_ids = {
                            string.id for string in trans_strings
                        }
                        if any(
                            string.id not in translated_string_ids
                            for string in extracted
                        ) and StringUtils.update_string_list(trans_strings, extracted):
                            changed = True

                    untranslated = [
                        s for s in trans_strings
                        if s.status in (StringStatus.TranslationRequired, StringStatus.TranslationIncomplete)
                        or not s.string
                        or s.string == s.original
                    ]
                    if untranslated:
                        matched_count = StringUtils.match_strings(
                            strings_to_update=untranslated,
                            database_strings=self.__database.strings,
                            lookup_maps=db_lookup_maps,
                        )
                        if matched_count > 0:
                            changed = True

                    if changed:
                        with self.__translation_lock:
                            translation.save()

                    has_incomplete = any(
                        string.id in required_string_ids
                        and string.status > StringStatus.TranslationComplete
                        for string in trans_strings
                    )
                    translated_string_ids = {
                        string.id for string in trans_strings
                    }
                    is_partially_covered = not required_string_ids.issubset(
                        translated_string_ids
                    )

                if has_incomplete or is_partially_covered:
                    status = TranslationStatus.TranslationIncomplete
                else:
                    status = TranslationStatus.TranslationInstalled

            elif any(
                string.original not in database_originals
                for string in modfile_strings
            ):
                status = TranslationStatus.RequiresTranslation
            else:
                status = TranslationStatus.TranslationAvailableInDatabase

        else:
            status = TranslationStatus.IsTranslated
            self.log.debug("Mod file is already translated.")

        return status

    @staticmethod
    def __bestiary_strings_match_translation(
        modfile_strings: StringList, translation_strings: StringList
    ) -> bool:
        """Checks whether the extracted Bestiary file exactly matches its translation."""

        if not modfile_strings:
            return False

        translated_by_id = {
            string.id: string.string
            for string in translation_strings
            if string.string is not None
        }
        return all(
            translated_by_id.get(string.id) == string.original
            for string in modfile_strings
        )

    def run_online_scan(
        self,
        items: dict[Mod, list[ModFile]],
        pdisplay: Optional[ProgressDisplay] = None,
    ) -> dict[Mod, dict[ModFile, TranslationStatus]]:
        """
        Scans online for available translations.

        Args:
            items (dict[Mod, list[ModFile]]): The items to scan.
            pdisplay (Optional[ProgressDisplay], optional):
                Optional progress display. Defaults to None.

        Returns:
            dict[Mod, dict[ModFile, TranslationStatus]]:
                A dictionary of mods, their mod files and their status.
        """

        if not self.__provider.is_available:
            self.log.warning("Skipping online scan because no provider is available.")
            return {}

        if pdisplay is not None:
            pdisplay.updateMainProgress(
                ProgressUpdate(
                    status_text=self.tr("Scanning online for available translations..."),
                    value=0,
                    maximum=0,
                )
            )

        scan_result: dict[Mod, dict[ModFile, TranslationStatus]] = {}

        relevant_items: dict[Mod, list[ModFile]] = {}
        for mod, modfiles in items.items():
            relevant_modfiles: list[ModFile] = [
                modfile
                for modfile in modfiles
                if modfile.status == TranslationStatus.RequiresTranslation
            ]
            if not relevant_modfiles:
                continue

            if mod.mod_id is not None and self.__provider.is_mod_id_valid(
                mod.mod_id, check_online=False
            ):
                relevant_items[mod] = relevant_modfiles

            # mod's source is unknown => no translation available
            else:
                scan_result[mod] = {
                    modfile: TranslationStatus.NoTranslationAvailable
                    for modfile in modfiles
                }

        self.log.info(
            "Scanning online for available translations "
            f"for {len(relevant_items)} mod(s)..."
        )

        with ProgressExecutor(
            pdisplay, max_workers=self.__app_config.worker_thread_num
        ) as executor:
            executor.set_main_progress_text(
                self.tr("Scanning online for available translations...")
            )

            tasks: dict[Future[dict[ModFile, TranslationStatus]], Mod] = {}
            for mod, modfiles in relevant_items.items():
                future: Future[dict[ModFile, TranslationStatus]] = executor.submit(
                    # this lambda is necessary as it gets an update callable as first
                    # positional argument
                    lambda ucb, m=mod, mfs=modfiles: self.__online_scan_mod(m, mfs, ucb)
                )
                tasks[future] = mod

            for future in as_completed(tasks):
                mod: Mod = tasks[future]
                try:
                    mod_scan_result: dict[ModFile, TranslationStatus] = future.result()
                    scan_result[mod] = mod_scan_result
                except Exception as ex:
                    self.log.error(f"Failed to scan for '{mod.name}': {ex}", exc_info=ex)

        self.log.info("Online scan complete.")
        self.log.info(f"Status summary: {self.__create_status_summary(scan_result)}")

        return scan_result

    def __online_scan_mod(
        self,
        mod: Mod,
        modfiles: list[ModFile],
        update_callback: Optional[UpdateCallback] = None,
    ) -> dict[ModFile, TranslationStatus]:
        if mod.mod_id is None:
            return {}

        result: dict[ModFile, TranslationStatus] = {}
        for m, modfile in enumerate(modfiles):
            update(
                update_callback,
                ProgressUpdate(
                    status_text=f"{mod.name} > {modfile.name} ({m}/{len(modfiles)})",
                    value=m,
                    maximum=len(modfiles),
                ),
            )

            self.log.debug(f"Scanning for '{mod.name}' > '{modfile.name}'...")
            try:
                result[modfile] = self.__online_scan_modfile(mod.mod_id, modfile)
            except Exception as ex:
                self.log.error(
                    f"Failed to scan for '{mod.name}' > '{modfile.name}': {ex}",
                    exc_info=ex,
                )
                result[modfile] = TranslationStatus.NoTranslationAvailable

        return result

    def __online_scan_modfile(
        self, mod_id: ModId, modfile: ModFile
    ) -> TranslationStatus:
        available_translations: dict[Source, list[ModId]] = (
            self.__provider.get_translations(
                mod_id=mod_id,
                file_name=modfile.name,
                language=self.__user_config.language.id,
                masterlist=self.__masterlist,
                author_blacklist=self.__user_config.author_blacklist,
            )
        )

        masterlist_entry: Optional[MasterlistEntry] = self.__masterlist.entries.get(
            modfile.name.lower()
        )

        if (
            masterlist_entry is not None
            and masterlist_entry.type == MasterlistEntry.Type.Route
            and masterlist_entry.targets
        ):
            self.log.debug(
                f"Found route entry for mod file '{modfile.name}' in masterlist."
            )
            return TranslationStatus.TranslationAvailableOnline

        if len(available_translations):
            return TranslationStatus.TranslationAvailableOnline
        else:
            return TranslationStatus.NoTranslationAvailable

    def run_string_search(
        self,
        items_to_search: dict[Mod, list[ModFile]],
        filter: SearchFilter,
        pdisplay: Optional[ProgressDisplay] = None,
    ) -> dict[Path, StringList]:
        """
        Searches the modlist for strings.

        Args:
            items_to_search (dict[Mod, list[ModFile]]): The items to search.
            filter (SearchFilter): The search filter.
            pdisplay (Optional[ProgressDisplay], optional):
                Optional progress display. Defaults to None.

        Returns:
            dict[Path, StringList]:
                A dictionary of mod file names and their matching strings.
        """

        relevant_items: dict[Mod, list[ModFile]] = {
            mod: [
                modfile
                for modfile in modfiles
                if modfile.status != TranslationStatus.NoStrings
            ]
            for mod, modfiles in items_to_search.items()
            if any(modfile.status != TranslationStatus.NoStrings for modfile in modfiles)
        }

        self.log.info(f"Searching {len(relevant_items)} mod(s) for strings...")

        results: dict[Path, StringList] = {}
        for m, (mod, modfiles) in enumerate(relevant_items.items()):
            if pdisplay is not None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Searching modlist for strings...")
                        + f" ({m}/{len(relevant_items.items())})",
                        value=m,
                        maximum=len(relevant_items.items()),
                    )
                )

            self.log.debug(f"Searching for strings in '{mod.name}'...")
            mod_result: dict[Path, StringList] = self.__search_mod(
                mod, modfiles, filter, pdisplay
            )
            if mod_result:
                results.update(mod_result)

        self.log.info(
            f"Search modlist for strings complete. Found results in {len(results)} mod "
            "file(s)."
        )

        return results

    def __search_mod(
        self,
        mod: Mod,
        modfiles: list[ModFile],
        filter: SearchFilter,
        pdisplay: Optional[ProgressDisplay] = None,
    ) -> dict[Path, StringList]:
        result: dict[Path, StringList] = {}

        for m, modfile in enumerate(modfiles):
            if pdisplay is not None:
                pdisplay.updateProgress(
                    progress_id=1,
                    payload=ProgressUpdate(
                        status_text=f"{mod.name} > {modfile.name} ({m}/{len(modfiles)})",
                        value=m,
                        maximum=len(modfiles),
                    ),
                )

            self.log.debug(
                f"Searching for strings in '{mod.name}' > '{modfile.name}'..."
            )
            modfile_result: StringList = self.__search_modfile(modfile, filter)
            if modfile_result:
                result[Path(f"{mod.name} > {modfile.name}")] = modfile_result

        return result

    def __search_modfile(self, modfile: ModFile, filter: SearchFilter) -> StringList:
        result: StringList = []

        strings: StringList = modfile.get_strings()
        for string in strings:
            if matches_filter(filter, string):
                result.append(string)

        return result

    def import_installed_translations(
        self, mods: list[Mod], pdisplay: Optional[ProgressDisplay] = None
    ) -> None:
        """
        Scans for and imports installed translations. Creates database translations for
        mod files that are entirely covered by installed translations if enabled.

        Args:
            mods (list[Mod]): The mods to scan.
            pdisplay (Optional[ProgressDisplay], optional):
                Optional progress display. Defaults to None.
        """

        installed_translations: dict[Mod, Mod] = self.run_translation_scan(
            mods, pdisplay
        )

        self.log.info(
            f"Importing {len(installed_translations)} installed translation(s)..."
        )

        new_translations: list[Translation] = []
        for m, (installed_translation, original_mod) in enumerate(
            installed_translations.items()
        ):
            if pdisplay is not None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Importing translations...")
                        + f" ({m}/{len(installed_translations)})",
                        value=m,
                        maximum=len(installed_translations),
                    ),
                )
                pdisplay.updateProgress(
                    progress_id=1,
                    payload=ProgressUpdate(
                        status_text=installed_translation.name, value=0, maximum=0
                    ),
                )

            self.log.debug(
                f"Importing translation '{installed_translation.name}' for original "
                f"mod '{original_mod.name}'..."
            )

            translation_strings: dict[Path, StringList] = (
                StringExtractor.map_strings_from_mods(
                    installed_translation, original_mod
                )
            )

            if not translation_strings:
                self.log.warning(
                    f"No additional strings from '{installed_translation.name}'."
                )
                continue

            new_translations.append(
                DatabaseService.create_translation_from_mod(
                    mod=installed_translation,
                    original_mod=original_mod,
                    strings=translation_strings,
                    database=self.__database,
                    add_and_save=False,
                )
            )

        self.log.info(f"Imported {len(new_translations)} installed translation(s).")

        if self.__app_config.auto_create_database_translations:
            self.log.info("Creating database translations...")
            items: dict[Mod, list[ModFile]] = {
                mod: [
                    modfile
                    for modfile in mod.modfiles
                    if modfile.status == TranslationStatus.TranslationAvailableInDatabase
                ]
                for mod in mods
                if any(
                    modfile.status == TranslationStatus.TranslationAvailableInDatabase
                    for modfile in mod.modfiles
                )
            }

            for m, mod in enumerate(items):
                if pdisplay is not None:
                    pdisplay.updateMainProgress(
                        ProgressUpdate(
                            status_text=self.tr("Creating database translations...")
                            + f" ({m}/{len(items)})",
                            value=m,
                            maximum=len(items),
                        )
                    )
                    pdisplay.updateProgress(
                        progress_id=1,
                        payload=ProgressUpdate(status_text=mod.name, value=0, maximum=0),
                    )

                self.log.debug(f"Creating database translation for '{mod.name}'...")
                new_translations.append(
                    DatabaseService.create_translation_for_mod(
                        mod=mod,
                        database=self.__database,
                        only_complete_coverage=True,
                        add_and_save=False,
                    )
                )

            self.log.info(
                f"Created {len(new_translations)} new database translation(s)."
            )

        for new_translation in new_translations:
            # remove duplicate strings and save the translation
            new_translation.remove_duplicates()

        if new_translations:
            DatabaseService.add_translations(new_translations, self.__database)

    def run_translation_scan(
        self, mods: list[Mod], pdisplay: Optional[ProgressDisplay] = None
    ) -> dict[Mod, Mod]:
        """
        Scans for installed translations.

        Args:
            mods (list[Mod]): The mods to scan.
            pdisplay (Optional[ProgressDisplay], optional):
                Optional progress display. Defaults to None.

        Returns:
            dict[Mod, Mod]: Map of translations to their (approximate) original mod.
        """

        result: dict[Mod, Mod] = {}

        self.log.info(f"Scanning {len(mods)} mod(s) for installed translations...")

        for m, mod in enumerate(mods):
            if pdisplay is not None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Scanning for installed translations...")
                        + f" ({m}/{len(mods)})",
                        value=m,
                        maximum=len(mods),
                    ),
                )
                pdisplay.updateProgress(
                    progress_id=1,
                    payload=ProgressUpdate(status_text=mod.name, value=0, maximum=0),
                )

            original_mod: Optional[Mod] = self.__translation_scan_mod(mod, pdisplay)

            if original_mod is not None:
                result[mod] = original_mod

        self.log.info(
            f"Found {len(result)} installed translation(s) that can be imported."
        )

        return result

    def __translation_scan_mod(
        self, mod: Mod, pdisplay: Optional[ProgressDisplay] = None
    ) -> Optional[Mod]:
        self.log.debug(f"Scanning for installed translations in '{mod.name}'...")

        original_mod: Optional[Mod] = None

        modfile_paths: list[Path] = list(
            filter(
                lambda m: self.__database.get_translation_by_modfile_path(m) is None,
                unique(
                    [
                        modfile.path
                        for modfile in mod.modfiles
                        if modfile.status == TranslationStatus.IsTranslated
                    ]
                    + [Path(Path(dsd_file).parent.name) for dsd_file in mod.dsd_files],
                ),
            )
        )
        for m, modfile_path in enumerate(modfile_paths):
            if pdisplay is not None:
                pdisplay.updateProgress(
                    progress_id=1,
                    payload=ProgressUpdate(
                        status_text=f"{mod.name} > {modfile_path} ({m}/{len(modfile_paths)})",
                        value=m,
                        maximum=len(modfile_paths),
                    ),
                )

            original_mod = self.__mod_instance.get_mod_with_modfile(
                modfile=modfile_path,
                ignore_mods=[mod],
                ignore_states=[
                    TranslationStatus.IsTranslated,
                    TranslationStatus.TranslationInstalled,
                ],
            )

            if original_mod is not None:
                break

        else:
            if modfile_paths:
                self.log.warning(
                    f"No original mod found for installed translation '{mod.name}'!"
                )

        return original_mod

    def __create_status_summary(
        self, scan_result: dict[Mod, dict[ModFile, TranslationStatus]]
    ) -> str:
        status_counts: dict[TranslationStatus, int] = {}
        for mod_results in scan_result.values():
            for status in mod_results.values():
                status_counts[status] = status_counts.get(status, 0) + 1

        status_summary: str = " | ".join(
            f"{status.name}: {count}"
            for status, count in sorted(
                status_counts.items(), key=lambda item: item[0].value
            )
        )

        return status_summary
