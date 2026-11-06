"""
Copyright (c) Cutleast
"""

import logging
from collections.abc import Iterable
from copy import copy
from typing import Optional

from cutleast_core_lib.core.utilities.unique import unique

from core.file_types.plugin.string import PluginString

from .string_status import StringStatus
from .types import String, StringList, StringType


class StringUtils:
    """
    Class with various utility methods for strings.
    """

    log: logging.Logger = logging.getLogger("StringUtils")

    @staticmethod
    def unique(strings: Iterable[String]) -> StringList:
        """
        Removes duplicates from an iterable of strings. Unique strings are identified by
        `String.id`.

        Convenience method for
            `unique(strings, key=lambda s: s.id)`.

        Args:
            strings (Iterable[String]): Iterable with duplicate strings.

        Returns:
            List of strings without duplicates.
        """

        return unique(strings, key=lambda s: s.id)

    @classmethod
    def _build_lookup_maps(
        cls, translation_strings: list[StringType]
    ) -> tuple[
        dict[str, StringType],
        dict[str, StringType],
        dict[str, StringType],
        dict[str, StringType],
    ]:
        """Builds reusable indexes for exact and fallback string matching.

        Args:
            translation_strings (list[StringType]): Strings to index.

        Returns:
            tuple[dict[str, StringType], ...]: Indexes by ID, EDID, original text,
                and lowercase original text.
        """

        strings_by_id: dict[str, StringType] = {}
        strings_by_edid: dict[str, StringType] = {}
        strings_by_original: dict[str, StringType] = {}
        strings_by_original_lower: dict[str, StringType] = {}

        for string in translation_strings:
            strings_by_id.setdefault(string.id, string)

            if (
                isinstance(string, PluginString)
                and string.editor_id
                and string.index is None
            ):
                edid_key = f"{string.editor_id}###{string.type}"
                strings_by_edid.setdefault(edid_key, string)

            original_text = string.original.strip() if string.original else ""
            if original_text:
                strings_by_original.setdefault(original_text, string)
                strings_by_original_lower.setdefault(original_text.lower(), string)

        return (
            strings_by_id,
            strings_by_edid,
            strings_by_original,
            strings_by_original_lower,
        )

    @classmethod
    def _find_matching_string(
        cls,
        original_string: StringType,
        strings_by_id: dict[str, StringType],
        strings_by_edid: dict[str, StringType],
        strings_by_original: dict[str, StringType],
        strings_by_original_lower: dict[str, StringType],
    ) -> tuple[Optional[StringType], bool]:
        """Finds an exact or fallback match for a source string.

        Args:
            original_string (StringType): Source string to match.
            strings_by_id (dict[str, StringType]): Exact string ID index.
            strings_by_edid (dict[str, StringType]): Plugin EDID and type index.
            strings_by_original (dict[str, StringType]): Exact trimmed text index.
            strings_by_original_lower (dict[str, StringType]): Casefolded text index.

        Returns:
            tuple[Optional[StringType], bool]: Matched translation and whether its ID
                matched exactly.
        """

        if original_string.id in strings_by_id:
            return strings_by_id[original_string.id], True

        if isinstance(original_string, PluginString) and original_string.index in (
            None,
            1,
        ):
            alt_index = 1 if original_string.index is None else None
            alt_id = (
                f"{original_string.record_id}###{original_string.editor_id}###"
                f"{original_string.type}###{alt_index}"
            )
            if alt_id in strings_by_id:
                return strings_by_id[alt_id], False

        if (
            isinstance(original_string, PluginString)
            and original_string.editor_id
            and original_string.index is None
        ):
            edid_key = f"{original_string.editor_id}###{original_string.type}"
            if edid_key in strings_by_edid:
                return strings_by_edid[edid_key], False

        original_text = original_string.original.strip()
        if original_text in strings_by_original:
            return strings_by_original[original_text], False

        if original_text.lower() in strings_by_original_lower:
            return strings_by_original_lower[original_text.lower()], False

        return None, False

    @classmethod
    def map_strings(
        cls, original_strings: list[StringType], translation_strings: list[StringType]
    ) -> list[StringType]:
        """
        Maps translated strings to the original strings.

        Args:
            original_strings (list[StringType]): List of original strings.
            translation_strings (list[StringType]): List of translated strings.

        Returns:
            list[StringType]: List of mapped strings.
        """

        cls.log.debug(
            f"Mapping {len(translation_strings)} translated string(s) to "
            f"{len(original_strings)} original string(s)..."
        )

        (
            strings_by_id,
            strings_by_edid,
            strings_by_original,
            strings_by_original_lower,
        ) = cls._build_lookup_maps(translation_strings)

        merged_strings: list[StringType] = []
        for original_string in original_strings:
            merged_string: StringType = copy(original_string)

            if merged_string.status == StringStatus.NoTranslationRequired:
                merged_string.string = merged_string.original
                merged_strings.append(merged_string)
                continue

            # Translate string if available
            translated_string, is_exact = cls._find_matching_string(
                original_string,
                strings_by_id,
                strings_by_edid,
                strings_by_original,
                strings_by_original_lower,
            )

            if translated_string is not None:
                translated_text = (
                    translated_string.string
                    if translated_string.string
                    and translated_string.string != translated_string.original
                    else translated_string.original
                )
                merged_string.string = translated_text

                if translated_text == original_string.original:
                    merged_string.status = StringStatus.NoTranslationRequired
                elif is_exact:
                    merged_string.status = (
                        translated_string.status
                        if translated_string.status
                        in (
                            StringStatus.TranslationComplete,
                            StringStatus.TranslationIncomplete,
                        )
                        else StringStatus.TranslationComplete
                    )
                else:
                    merged_string.status = StringStatus.TranslationIncomplete

            # Set status to translation required if no translation available
            else:
                merged_string.status = StringStatus.TranslationRequired

            merged_strings.append(merged_string)

        if merged_strings:
            cls.log.debug(f"Mapped {len(merged_strings)} string(s).")
        else:
            cls.log.error("Mapping failed!")

        return merged_strings

    @classmethod
    def match_strings(
        cls, strings_to_update: StringList, database_strings: StringList
    ) -> None:
        """
        Updates a list of strings and attempts to translate them via similarities to
        existing strings.

        Args:
            strings_to_update (StringList): Strings to update.
            database_strings (StringList): Existing strings to use for translation.
        """

        cls.log.debug(
            f"Attempting to translate {len(strings_to_update)} string(s) from "
            f"{len(database_strings)} existing string(s)..."
        )

        (
            db_strings_by_id,
            db_strings_by_edid,
            db_strings_by_original,
            db_strings_by_original_lower,
        ) = cls._build_lookup_maps(database_strings)

        matched: int = 0
        for string in strings_to_update:
            matched += cls.match_string(
                string_to_update=string,
                database_strings_by_id=db_strings_by_id,
                database_strings_by_original=db_strings_by_original,
                database_strings_by_edid=db_strings_by_edid,
                database_strings_by_original_lower=db_strings_by_original_lower,
            )

        cls.log.debug(f"Successfully translated {matched} string(s).")

    @classmethod
    def match_string(
        cls,
        string_to_update: String,
        database_strings_by_id: dict[str, String],
        database_strings_by_original: dict[str, String],
        database_strings_by_edid: Optional[dict[str, String]] = None,
        database_strings_by_original_lower: Optional[dict[str, String]] = None,
    ) -> bool:
        """
        Updates a string and attempts to translate it via similarities to existing strings.

        Args:
            string_to_update (String): String to update.
            database_strings_by_id (dict[str, String]):
                Dictionary mapping string IDs to existing strings.
            database_strings_by_original (dict[str, String]):
                Dictionary mapping original strings to existing strings.
            database_strings_by_edid (Optional[dict[str, String]], optional):
                Plugin strings indexed by editor ID and type.
            database_strings_by_original_lower (Optional[dict[str, String]], optional):
                Strings indexed by lowercased original text.

        Returns:
            bool: `True` if the string was updated, `False` otherwise.
        """

        if string_to_update.id in database_strings_by_id:
            database_string = database_strings_by_id[string_to_update.id]
            if database_string.string:
                string_to_update.string = database_string.string
                string_to_update.status = StringStatus.TranslationComplete
                return True

        if (
            isinstance(string_to_update, PluginString)
            and string_to_update.index in (None, 1)
        ):
            alt_index = 1 if string_to_update.index is None else None
            alt_id = (
                f"{string_to_update.record_id}###{string_to_update.editor_id}###"
                f"{string_to_update.type}###{alt_index}"
            )
            if alt_id in database_strings_by_id:
                database_string = database_strings_by_id[alt_id]
                if database_string.string:
                    string_to_update.string = database_string.string
                    string_to_update.status = StringStatus.TranslationIncomplete
                    return True

        if (
            database_strings_by_edid is not None
            and isinstance(string_to_update, PluginString)
            and string_to_update.editor_id
            and string_to_update.index is None
        ):
            edid_key = f"{string_to_update.editor_id}###{string_to_update.type}"
            if edid_key in database_strings_by_edid:
                database_string = database_strings_by_edid[edid_key]
                if database_string.string:
                    string_to_update.string = database_string.string
                    string_to_update.status = StringStatus.TranslationIncomplete
                    return True

        original_text = string_to_update.original.strip()
        if original_text in database_strings_by_original:
            database_string = database_strings_by_original[original_text]
            if database_string.string:
                string_to_update.string = database_string.string
                string_to_update.status = StringStatus.TranslationIncomplete
                return True

        lower_text = original_text.lower()
        if (
            database_strings_by_original_lower is not None
            and lower_text in database_strings_by_original_lower
        ):
            database_string = database_strings_by_original_lower[lower_text]
            if database_string.string:
                string_to_update.string = database_string.string
                string_to_update.status = StringStatus.TranslationIncomplete
                return True

        return False

    @classmethod
    def update_string_list(
        cls,
        translation_strings: StringList,
        original_strings: StringList,
        keep_deleted: bool = False,
    ) -> bool:
        """
        Updates a list of strings based on a list of original strings. This method fills
        in missing strings and resets translations where the original text has changed.
        If `keep_deleted` is set to `False`, strings that are no longer present in the
        original list will be removed from the translation list.

        Args:
            translation_strings (StringList): List of translated strings.
            original_strings (StringList): List of original strings.
            keep_deleted (bool):
                Whether to keep strings that are no longer present in the original list.
                Defaults to `False`.

        Returns:
            bool:
                `True` if any strings were updated, added or removed, `False` otherwise.
        """

        (
            strings_by_id,
            strings_by_edid,
            strings_by_original,
            strings_by_original_lower,
        ) = cls._build_lookup_maps(translation_strings)

        changed: bool = False
        for original_string in original_strings:
            translated_string: Optional[String] = strings_by_id.get(original_string.id)

            if translated_string is None:
                fallback_string, _ = cls._find_matching_string(
                    original_string,
                    strings_by_id,
                    strings_by_edid,
                    strings_by_original,
                    strings_by_original_lower,
                )
                if (
                    fallback_string is not None
                    and fallback_string.string
                    and fallback_string.string != fallback_string.original
                ):
                    new_string = copy(original_string)
                    new_string.string = fallback_string.string
                    new_string.status = StringStatus.TranslationIncomplete
                else:
                    new_string = copy(original_string)
                    new_string.status = StringStatus.TranslationRequired
                    new_string.string = new_string.original

                strings_by_id[new_string.id] = new_string
                translation_strings.append(new_string)
                changed = True

            elif translated_string.original != original_string.original:
                # original string has changed -> reset translation to original and mark
                # string as "translation required"
                translated_string.original = original_string.original
                translated_string.status = StringStatus.TranslationRequired
                translated_string.string = translated_string.original
                changed = True

        if not keep_deleted:
            # remove strings that are no longer present in the original list
            original_ids: set[str] = {string.id for string in original_strings}

            for translated_string in translation_strings.copy():
                if translated_string.id not in original_ids:
                    translation_strings.remove(translated_string)
                    changed = True

        return changed
