"""
Copyright (c) Cutleast
"""

import logging
import re
from copy import copy, deepcopy
from pathlib import Path
from typing import Any, Optional

from cutleast_core_lib.core.multithreading.progress import ProgressUpdate
from cutleast_core_lib.ui.progress.display import ProgressDisplay
from PySide6.QtCore import QObject, Signal

from core.database.database import TranslationDatabase
from core.database.translation import Translation
from core.string.string_status import StringStatus
from core.string.types import String, StringList
from core.translator.service import TranslatorService
from core.translator.translator import Translator
from core.utilities.game_language import GameLanguage


class Editor(QObject):
    """
    Class for editing a translation.
    """

    strings_changed = Signal(object)
    """
    Signal emitted when any of the strings in the translation change.

    Args:
        StringList: The list of strings that changed.
    """

    __language: GameLanguage
    __database: TranslationDatabase
    __translator_service: TranslatorService

    __translation: Translation
    __strings_cache: dict[Path, StringList]
    """
    Stores a deep copy of the strings in the translation.
    """

    __changes_pending: bool

    log: logging.Logger = logging.getLogger("Editor")

    def __init__(
        self,
        translation: Translation,
        language: GameLanguage,
        database: TranslationDatabase,
        translator_service: TranslatorService,
    ) -> None:
        """
        Args:
            translation (Translation): The translation to edit.
            language (GameLanguage): The language of the translation.
            database (TranslationDatabase): The translation database.
            translator_service (TranslatorService): The translator service.
        """

        super().__init__()

        self.__translation = translation

        self.__language = language
        self.__database = database
        self.__translator_service = translator_service

        # Make a deep copy to prevent immediately modifying the translation
        self.__strings_cache = deepcopy(self.__translation.strings)

        self.__changes_pending = False

        self.strings_changed.connect(lambda _: self.__on_change())

    def save(self) -> None:
        """
        Saves changes to the translation.
        """

        self.__translation.strings = self.__strings_cache
        self.__translation.save()

        self.log.info(f"Saved translation '{self.__translation.name}'.")
        self.__changes_pending = False

    def __on_change(self, changes_pending: bool = True) -> None:
        self.__changes_pending = changes_pending

    @property
    def changes_pending(self) -> bool:
        """
        Whether there are unsaved changes.
        """

        return self.__changes_pending

    @property
    def strings(self) -> dict[Path, StringList]:
        """
        Map of plugin names to their list of strings.
        Returns their current editing state.
        """

        return copy(self.__strings_cache)

    @property
    def all_strings(self) -> StringList:
        """
        List of all strings.
        """

        return [
            string for strings in self.__strings_cache.values() for string in strings
        ]

    def get_string_states_summary(
        self, strings: Optional[StringList] = None
    ) -> dict[StringStatus, int]:
        """
        Get a summary of string states.

        Args:
            strings (Optional[StringList], optional):
                List of strings to summarize. If None, summarizes all strings. Defaults
                to None.

        Returns:
            dict[StringStatus, int]:
                Dictionary of string states and number of strings in each state
        """

        if strings is None:
            strings = self.all_strings

        return {
            state: len([string for string in strings if string.status == state])
            for state in StringStatus
        }

    def set_status(self, strings: StringList, status: StringStatus) -> None:
        """
        Sets the status of a list of strings.

        Args:
            strings (StringList): List of strings
            status (Status): The status to set
        """

        for string in strings:
            string.status = status

        self.strings_changed.emit(strings)
        self.log.info(f"Updated status for {len(strings)} string(s).")

    def translate_with_api(
        self, strings: StringList, pdisplay: Optional[ProgressDisplay]
    ) -> None:
        """
        Translates a list of strings with a translator API.

        Args:
            strings (StringList): List of strings
            pdisplay (Optional[ProgressDisplay]):
                Optional progress display, defaults to None.
        """

        if pdisplay is not None:
            pdisplay.updateMainProgress(
                ProgressUpdate(status_text=self.tr("Translating with API..."))
            )

        self.log.info(f"Translating {len(strings)} string(s) with API...")

        translator: Translator = self.__translator_service.get_translator()

        self.log.info(f"Used translator API: {translator.__class__.__name__}")

        texts: list[str] = [selected_string.original for selected_string in strings]
        result: dict[str, str] = translator.mass_translate(texts, self.__language)

        for string in strings:
            string.string = result[string.original]
            string.status = StringStatus.TranslationIncomplete

        self.strings_changed.emit(strings)
        self.log.info("API translation complete.")

    def apply_regex(
        self, strings: StringList, replace_text: str, pattern: re.Pattern
    ) -> int:
        """
        Applies a regex to a list of strings.

        Args:
            strings (StringList): List of strings
            replace_text (str): Replacer text
            pattern (re.Pattern): Regex pattern

        Returns:
            int: Number of strings modified
        """

        self.log.info(f"Applying regex to {len(strings)} string(s)...")

        modified_strings: StringList = []
        for string in strings:
            src: str = string.string if string.string is not None else string.original
            res: str = pattern.sub(replace_text, src)
            string.string = res

            if src != string.string:
                string.status = StringStatus.TranslationIncomplete
                modified_strings.append(string)

        self.strings_changed.emit(modified_strings)
        self.log.info("Regex applied.")

        return len(modified_strings)

    def apply_database(self, strings: StringList) -> int:
        """
        Applies database to a list of strings.

        Args:
            strings (StringList): List of strings

        Returns:
            int: Number of strings modified
        """

        self.log.info(f"Applying database to {len(strings)} string(s)...")

        database_originals: dict[str, String] = {
            string.original: string for string in self.__database.strings
        }
        database_strings: dict[str, String] = {
            string.id: string for string in self.__database.strings
        }

        modified_strings: StringList = []
        for string in strings:
            if string.id in database_strings:
                string.string = database_strings[string.id].string
                string.status = StringStatus.TranslationComplete
                modified_strings.append(string)

            elif string.original in database_originals:
                string.string = database_originals[string.original].string
                string.status = StringStatus.TranslationComplete
                modified_strings.append(string)

        self.strings_changed.emit(modified_strings)
        self.log.info("Database applied.")

        return len(modified_strings)

    def apply_to_matching_strings(self, original: str, translation: str) -> int:
        """
        Applies translation to strings that are matching.

        Args:
            original (str): The original string
            translation (str): The translation

        Returns:
            int: Number of strings modified
        """

        modified_strings: StringList = []
        for string in self.all_strings:
            if (
                string.original == original
                and string.status != StringStatus.TranslationComplete
            ):
                string.string = translation
                string.status = StringStatus.TranslationIncomplete
                modified_strings.append(string)

        self.strings_changed.emit(modified_strings)
        self.log.info(f"Applied translation to {len(modified_strings)} string(s).")

        return len(modified_strings)

    def reset_strings(self, strings: StringList) -> None:
        """
        Resets the translation and the status of a list of strings.

        Args:
            strings (StringList): List of strings
        """

        self.log.info(f"Resetting {len(strings)} string(s)...")

        for string in strings:
            string.string = None
            string.status = StringStatus.TranslationRequired

        self.strings_changed.emit(strings)
        self.log.info("Strings reset.")

    def apply_translation_strings(
    
            self,
    
            new_strings: dict[Path, StringList] | StringList,
    
            missing_only: bool = True,
    
        ) -> int:
            """
    
            Applies translated strings from an external source (download or re-translation)
    
            to the current translation strings.
    
    
    
            Matching rules:
    
            1. Direct match: Exact string ID (FormID + editor_id + type + index)
    
            2. Exact original text match: target.original == source.original
    
            3. EDID match: target.editor_id == source.editor_id (ONLY IF target.index is None and source.index is None)
    
    
    
            If missing_only is True, only modifies strings that are not TranslationComplete or missing translation.
    
    
    
            Returns:
                int: Number of strings modified.
    
            """
    
    
    
            from core.file_types.plugin.string import PluginString
    
    
    
            modified_strings: StringList = []
    
    
    
            if isinstance(new_strings, dict):
    
                all_source_strings: StringList = [
    
                    s for s_list in new_strings.values() for s in s_list
    
                ]
    
            else:
    
                all_source_strings = new_strings
    
    
    
            for modfile_path, target_strings in self.__strings_cache.items():
    
                source_candidates: StringList = all_source_strings
    
                if isinstance(new_strings, dict):
    
                    matched_key = next(
    
                        (
    
                            k
    
                            for k in new_strings
    
                            if k.name.lower() == modfile_path.name.lower()
    
                        ),
    
                        None,
    
                    )
    
                    if matched_key is None:
    
                        matched_key = next(
    
                            (
    
                                k
    
                                for k in new_strings
    
                                if k.stem.lower() == modfile_path.stem.lower()
    
                            ),
    
                            None,
    
                        )
    
                    if matched_key is not None:
    
                        source_candidates = new_strings[matched_key]
    
    
    
                by_id: dict[str, String] = {s.id: s for s in source_candidates}
    
                by_original: dict[str, String] = {
    
                    s.original.strip(): s
    
                    for s in source_candidates
    
                    if s.original and s.original.strip()
    
                }
    
                by_edid: dict[str, String] = {
    
                    f"{s.editor_id}###{s.type}": s
    
                    for s in source_candidates
    
                    if isinstance(s, PluginString) and s.editor_id and s.index is None
    
                }
    
    
    
                for target in target_strings:
    
                    if (
    
                        missing_only
    
                        and target.status == StringStatus.TranslationComplete
    
                        and target.string
    
                    ):
    
                        continue
    
    
    
                    matched: Optional[String] = None
    
    
    
                    # 1. Direct ID match
    
                    if target.id in by_id:
    
                        matched = by_id[target.id]
    
                    # 2. Exact original match
    
                    elif target.original and target.original.strip() in by_original:
    
                        matched = by_original[target.original.strip()]
    
                    # 3. EDID match ONLY if index is None
    
                    elif (
    
                        isinstance(target, PluginString)
    
                        and target.editor_id
    
                        and target.index is None
    
                    ):
    
                        edid_key = f"{target.editor_id}###{target.type}"
    
                        if edid_key in by_edid:
    
                            matched = by_edid[edid_key]
    
    
    
                    if matched is not None:
    
                        trans_text = (
    
                            matched.string
    
                            if (matched.string and matched.string != matched.original)
    
                            else matched.original
    
                        )
                        if trans_text:
                            trans_text = trans_text.replace("\xa0", " ").replace("\u202f", " ").replace("\u200b", "")
    
                        if trans_text and trans_text.strip() != target.original.strip():
                            target.string = trans_text
                            target.status = StringStatus.TranslationComplete
                            modified_strings.append(target)
                        elif trans_text and trans_text.strip() == target.original.strip():
                            if target.status == StringStatus.TranslationRequired:
                                target.string = trans_text
                                if matched.status in (
                                    StringStatus.NoTranslationRequired,
                                    StringStatus.TranslationIncomplete,
                                ):
                                    target.status = matched.status
                                else:
                                    target.status = StringStatus.TranslationIncomplete
                                modified_strings.append(target)

            if modified_strings:
    
                self.strings_changed.emit(modified_strings)
    
                self.log.info(
    
                    f"Applied {len(modified_strings)} strings from source translation."
    
                )
    
    
    
            return len(modified_strings)

    def apply_bridge(
        self,
        bridge: dict[str, Any],
        missing_only: bool = True,
    ) -> int:
        """
        Applies a translation bridge to the current translation strings.

        Args:
            bridge (dict[str, Any]): Bridge mappings generated by TranslationBridge.
            missing_only (bool, optional): Only translate missing strings. Defaults to True.

        Returns:
            int: Number of strings modified.
        """
        from core.editor.translation_bridge import TranslationBridge

        modified_strings: StringList = []
        for target_strings in self.__strings_cache.values():
            changed = TranslationBridge.apply_bridge(
                bridge=bridge,
                target_strings=target_strings,
                missing_only=missing_only,
            )
            modified_strings.extend(changed)

        if modified_strings:
            self.strings_changed.emit(modified_strings)
            self.log.info(f"Bridge applied {len(modified_strings)} strings.")

        return len(modified_strings)
    
    
    
