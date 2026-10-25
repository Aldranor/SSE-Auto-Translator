"""
Copyright (c) Cutleast
"""

import pytest

from core.file_types.plugin.string import PluginString
from core.string.string_status import StringStatus
from core.string.string_utils import StringUtils
from core.string.types import String, StringList

from ..core_test import CoreTest


class TestStringUtils(CoreTest):
    """
    Tests `core.string.string_utils.StringUtils`.
    """

    def test_map_strings(self) -> None:
        """
        Tests `StringUtils.map_strings()`.
        """

        # given
        original_strings: list[PluginString] = [
            PluginString(
                original="Options: Obsidian Weathers",
                form_id="04000D65|Obsidian Weathers.esp",
                type="SPEL FULL",
                editor_id="ObsidianSpell",
            ),
            PluginString(
                original="Default",
                form_id="04000D62|Obsidian Weathers.esp",
                type="MESG ITXT",
                index=0,
                editor_id="ObsidianMessage",
            ),
            PluginString(
                original="Torch",
                form_id="0001D4EC|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch01",
            ),
            PluginString(
                original="AnInternalName",
                form_id="00012345|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch01",
                status=StringStatus.NoTranslationRequired,
            ),
            PluginString(
                original="An Unchanged String",
                form_id="00098765|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch02",
            ),
        ]
        translation_strings: list[PluginString] = [
            PluginString(
                original="Optionen: Obsidian-Wetter",
                form_id="04000D65|Obsidian Weathers.esp",
                type="SPEL FULL",
                editor_id="ObsidianSpell",
            ),
            PluginString(
                original="Standard",
                form_id="04000D62|Obsidian Weathers.esp",
                type="MESG ITXT",
                index=0,
                editor_id="ObsidianMessage",
            ),
            PluginString(
                original="An Unchanged String",
                form_id="00098765|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch02",
            ),
        ]

        # when
        merged_strings: list[PluginString] = StringUtils.map_strings(
            original_strings, translation_strings
        )

        # then
        assert merged_strings == [
            PluginString(
                form_id="04000D65|Obsidian Weathers.esp",
                type="SPEL FULL",
                original="Options: Obsidian Weathers",
                string="Optionen: Obsidian-Wetter",
                editor_id="ObsidianSpell",
                status=StringStatus.TranslationComplete,
            ),
            PluginString(
                form_id="04000D62|Obsidian Weathers.esp",
                type="MESG ITXT",
                original="Default",
                string="Standard",
                index=0,
                editor_id="ObsidianMessage",
                status=StringStatus.TranslationComplete,
            ),
            PluginString(
                original="Torch",
                form_id="0001D4EC|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch01",
                status=StringStatus.TranslationRequired,
            ),
            PluginString(
                original="AnInternalName",
                string="AnInternalName",
                form_id="00012345|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch01",
                status=StringStatus.NoTranslationRequired,
            ),
            PluginString(
                original="An Unchanged String",
                string="An Unchanged String",
                form_id="00098765|Skyrim.esm",
                type="LIGH FULL",
                editor_id="Torch02",
                status=StringStatus.TranslationRequired,
            ),
        ]

    @staticmethod
    def provide_update_string_data() -> list[
        tuple[PluginString, StringList, PluginString]
    ]:
        """
        Provides test data for `test_update_string`.

        Returns:
            list[tuple[String, StringList, String]]: Test data.
        """

        test_data: list[tuple[PluginString, StringList, PluginString]] = []

        # test translation by form id
        string1a = PluginString(
            form_id="1",
            type="SPEL FULL",
            original="Original",
        )
        string1b = PluginString(
            form_id="1",
            type="SPEL FULL",
            original="Original",
            string="Translated",
        )
        string1c = PluginString(
            form_id="1",
            type="SPEL FULL",
            original="Original",
            string="Translated",
            status=StringStatus.TranslationComplete,
        )

        # test translation by original string
        string2a = PluginString(
            form_id="2",
            type="SPEL FULL",
            original="Original",
        )
        string2b = PluginString(
            form_id="a different form id",
            type="SPEL FULL",
            original="Original",
            string="Translated",
        )
        string2c = PluginString(
            form_id="2",
            type="SPEL FULL",
            original="Original",
            string="Translated",
            status=StringStatus.TranslationIncomplete,
        )

        # test that unmatched strings aren't altered
        string3a = PluginString(
            form_id="3",
            type="SPEL FULL",
            original="Original",
        )
        string3b = PluginString(
            form_id="a different form id",
            type="SPEL FULL",
            original="and a different original",
            string="Translated",
        )

        test_data.append((string1a, [string1b], string1c))
        test_data.append((string2a, [string2b], string2c))
        test_data.append((string3a, [string3b], string3a))

        return test_data

    @pytest.mark.parametrize(
        "string_to_update, existing_strings, expected_string",
        provide_update_string_data(),
    )
    def test_match_string(
        self,
        string_to_update: String,
        existing_strings: StringList,
        expected_string: String,
    ) -> None:
        """
        Tests `StringUtils.match_string()`.

        Args:
            string_to_update (String): String to update.
            existing_strings (StringList): Existing strings to use for translation.
            expected_string (String): Expected updated string.
        """

        # given
        input_hash: int = CoreTest.calc_unique_string_hash(string_to_update)
        expected_hash: int = CoreTest.calc_unique_string_hash(expected_string)
        existing_strings_by_id: dict[str, String] = {
            string.id: string for string in existing_strings
        }
        existing_strings_by_original: dict[str, String] = {
            string.original: string for string in existing_strings
        }

        # when
        updated: bool = StringUtils.match_string(
            string_to_update, existing_strings_by_id, existing_strings_by_original
        )
        actual_hash: int = CoreTest.calc_unique_string_hash(string_to_update)

        # then
        assert updated == (input_hash != expected_hash)
        assert actual_hash == expected_hash, (
            f"<{string_to_update}> and <{expected_string}> differ!"
        )

    def test_map_strings_fallbacks(self) -> None:
        """
        Tests fallback matching by EDID and original text when FormIDs differ.
        """
        # given
        original_strings: list[PluginString] = [
            # Case 1: FormID shifted between mod versions, but EDID is identical (no index)
            PluginString(
                original="Steel Claymore",
                form_id="02001500|Mod.esp",
                type="WEAP FULL",
                editor_id="ModSteelClaymore",
            ),
            # Case 2: FormID and EDID changed, but original text matches (DSD fallback)
            PluginString(
                original="Flame Ring of Protection",
                form_id="02002000|Mod.esp",
                type="ARMO FULL",
                editor_id="NewRingEDID",
            ),
            # Case 3: Dialogue record (index not None) with different FormID - should NOT match by EDID
            PluginString(
                original="Need something?",
                form_id="02003000|Mod.esp",
                type="INFO NAM1",
                editor_id="SharedDialogueTopic",
                index=0,
            ),
        ]

        translation_strings: list[PluginString] = [
            # Translation from old version with old FormID 02001000
            PluginString(
                original="Steel Claymore",
                string="Claymore d'acier",
                form_id="02001000|Mod.esp",
                type="WEAP FULL",
                editor_id="ModSteelClaymore",
                status=StringStatus.TranslationComplete,
            ),
            # DSD translation with arbitrary old FormID
            PluginString(
                original="Flame Ring of Protection",
                string="Anneau de flammes protecteur",
                form_id="02000ABC|Mod.esp",
                type="ARMO FULL",
                editor_id="OldRingEDID",
                status=StringStatus.TranslationComplete,
            ),
            # Different dialogue line sharing the same topic EDID
            PluginString(
                original="Good morning.",
                string="Bonjour.",
                form_id="02003999|Mod.esp",
                type="INFO NAM1",
                editor_id="SharedDialogueTopic",
                index=1,
                status=StringStatus.TranslationComplete,
            ),
        ]

        # when
        mapped = StringUtils.map_strings(original_strings, translation_strings)

        # then
        # Case 1: Matched by EDID -> translated to French, bound to new FormID
        assert mapped[0].form_id == "02001500|Mod.esp"
        assert mapped[0].string == "Claymore d'acier"
        assert mapped[0].status == StringStatus.TranslationIncomplete

        # Case 2: Matched by original text -> translated to French, bound to new FormID
        assert mapped[1].form_id == "02002000|Mod.esp"
        assert mapped[1].string == "Anneau de flammes protecteur"
        assert mapped[1].status == StringStatus.TranslationIncomplete

        # Case 3: Dialogues with index should NOT match by EDID -> remains untranslated
        assert mapped[2].form_id == "02003000|Mod.esp"
        assert mapped[2].status == StringStatus.TranslationRequired
