"""
Copyright (c) Cutleast
"""

from pathlib import Path
from typing import Any, Optional, Self
from unittest.mock import MagicMock

import pytest
from bethkit import StringFileKind
from pytest_mock import MockerFixture

from core.editor.translation_bridge import TranslationBridge
from core.file_types.plugin.string import PluginString
from core.string.string_status import StringStatus
from tests.base_test import BaseTest


class TestTranslationBridge(BaseTest):
    """
    Tests `core.editor.translation_bridge.TranslationBridge`.
    """

    @staticmethod
    def __make_plugin_string(
        form_id: str,
        record_type: str,
        text: str,
        index: Optional[int] = None,
        editor_id: Optional[str] = None,
    ) -> PluginString:
        return PluginString(
            form_id=form_id,
            type=record_type,
            index=index,
            editor_id=editor_id,
            original=text,
            status=StringStatus.TranslationRequired,
        )

    def test_build_and_apply_bridge_matches_formid_text_edid_and_identical(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """
        Tests that `build_bridge` and `apply_bridge` match records by local FormID,
        exact text fallback, EDID fallback, and mark identical lines as incomplete.

        Args:
            tmp_path (Path): Temporary folder.
            mocker (MockerFixture): Pytest mocker fixture.
        """

        original_dir: Path = tmp_path / "original"
        translated_dir: Path = tmp_path / "translated"
        original_dir.mkdir()
        translated_dir.mkdir()
        (original_dir / "Example.esp").write_bytes(b"")
        (translated_dir / "Example.esp").write_bytes(b"")

        original_strings: list[PluginString] = [
            self.__make_plugin_string(
                "01000100", "NPC_:FULL", "Iron\xa0Sword", editor_id="IronSword"
            ),
            self.__make_plugin_string(
                "01000101", "NPC_:FULL", "Yes", editor_id="YesA"
            ),
            self.__make_plugin_string(
                "01000102", "NPC_:FULL", "Yes", editor_id="YesB"
            ),
            self.__make_plugin_string(
                "01000103", "NPC_:FULL", "Alduin", editor_id="DragonAlduin"
            ),
        ]
        translated_strings: list[PluginString] = [
            self.__make_plugin_string(
                "02000100", "NPC_:FULL", "Épée\u202fen fer", editor_id="IronSword"
            ),
            self.__make_plugin_string(
                "02000101", "NPC_:FULL", "Oui", editor_id="YesA"
            ),
            self.__make_plugin_string(
                "02000102", "NPC_:FULL", "Ouais", editor_id="YesB"
            ),
            self.__make_plugin_string(
                "02000103", "NPC_:FULL", "Alduin", editor_id="DragonAlduin"
            ),
        ]

        def fake_plugin_file(name: str, full_path: Path) -> MagicMock:
            plugin = MagicMock()
            plugin.extract_external_string_ids.return_value = {}
            if full_path.parent == original_dir:
                plugin.get_strings.return_value = original_strings
            else:
                plugin.get_strings.return_value = translated_strings
            return plugin

        mocker.patch(
            "core.editor.translation_bridge.PluginFile",
            side_effect=fake_plugin_file,
        )

        bridge: dict[str, Any] = TranslationBridge.build_bridge(
            translated_dir, original_dir, "french"
        )

        targets: list[PluginString] = [
            self.__make_plugin_string("05000100", "NPC_:FULL", "Iron Sword"),
            self.__make_plugin_string("05000999", "NPC_:FULL", "Yes"),
            self.__make_plugin_string(
                "05000103", "NPC_:FULL", "Alduin", editor_id="DragonAlduin"
            ),
        ]
        modified = TranslationBridge.apply_bridge(
            bridge, targets, missing_only=True
        )

        assert len(modified) == 3
        assert targets[0].string == "Épée en fer"
        assert targets[0].status == StringStatus.TranslationComplete
        assert targets[1].string == "Oui"
        assert targets[1].status == StringStatus.TranslationComplete
        assert targets[2].string == "Alduin"
        assert targets[2].status == StringStatus.TranslationIncomplete
        assert bridge["stats"]["formid"] == 1
        assert bridge["stats"]["text"] == 1
        assert bridge["stats"]["identical"] == 1

    def test_build_bridge_reads_localized_string_tables(
        self, tmp_path: Path, mocker: MockerFixture
    ) -> None:
        """
        Tests that `build_bridge` pairs external string table entries across
        `.strings`, `.dlstrings`, and `.ilstrings` tables.

        Args:
            tmp_path (Path): Temporary folder.
            mocker (MockerFixture): Pytest mocker fixture.
        """

        original_dir: Path = tmp_path / "original"
        translated_dir: Path = tmp_path / "translated"
        original_dir.mkdir()
        translated_dir.mkdir()
        (original_dir / "Mod.esp").write_bytes(b"")
        (translated_dir / "Mod.esp").write_bytes(b"")
        (original_dir / "Mod_english.strings").write_bytes(b"")
        (translated_dir / "Mod_french.strings").write_bytes(b"")

        original_ref = self.__make_plugin_string("01000200", "BOOK:FULL", "")
        translated_ref = self.__make_plugin_string("02000200", "BOOK:FULL", "")

        def fake_plugin_file(name: str, full_path: Path) -> MagicMock:
            plugin = MagicMock()
            plugin.get_strings.return_value = []
            if full_path.parent == original_dir:
                plugin.extract_external_string_ids.return_value = {
                    (StringFileKind.STRINGS, 42): [original_ref],
                }
            else:
                plugin.extract_external_string_ids.return_value = {
                    (StringFileKind.STRINGS, 99): [translated_ref],
                }
            return plugin

        mocker.patch(
            "core.editor.translation_bridge.PluginFile",
            side_effect=fake_plugin_file,
        )

        class FakeTable:
            def __init__(self, entries: dict[int, bytes]) -> None:
                self.__entries = entries

            def __enter__(self) -> Self:
                return self

            def __exit__(self, *args: object) -> None:
                return None

            def get(self, string_id: int) -> Optional[bytes]:
                return self.__entries.get(string_id)

        def fake_from_stream(stream: object, kind: StringFileKind) -> FakeTable:
            stream_name: str = str(getattr(stream, "name", ""))
            if "english" in stream_name:
                return FakeTable({42: b"Original Book\0"})
            return FakeTable({99: b"Livre Original\0"})

        mocker.patch(
            "core.editor.translation_bridge.StringTable.from_stream",
            side_effect=fake_from_stream,
        )

        bridge: dict[str, Any] = TranslationBridge.build_bridge(
            translated_dir, original_dir, "french"
        )

        assert bridge["text_map"] == {"Original Book": "Livre Original"}
        assert ("000200", "BOOK:FULL", None) in bridge["formid_map"]

    def test_build_bridge_reads_dsd_json_without_original_archive(
        self, tmp_path: Path
    ) -> None:
        """
        Tests that `build_bridge` can read Dynamic String Distributor JSON files
        even when no original archive is provided.

        Args:
            tmp_path (Path): Temporary folder.
        """

        dsd_dir: Path = (
            tmp_path / "SKSE" / "Plugins" / "DynamicStringDistributor" / "Example.esp"
        )
        dsd_dir.mkdir(parents=True)
        (dsd_dir / "0.json").write_text(
            '[{"form_id": "000100|Example.esp", "type": "NPC_:FULL", '
            '"original": "Iron Sword", "string": "Épée en fer"}]',
            encoding="utf-8",
        )

        bridge: dict[str, Any] = TranslationBridge.build_bridge(
            translated_source=tmp_path,
            original_source=None,
            target_plugin_names=["Example.esp"],
        )

        assert bridge["text_map"] == {"Iron Sword": "Épée en fer"}
        assert bridge["pair_count"] == 1


@pytest.mark.parametrize("missing_only", [True, False])
def test_editor_apply_bridge(tmp_path: Path, missing_only: bool) -> None:
    """
    Tests `Editor.apply_bridge` respecting `missing_only`.

    Args:
        tmp_path (Path): Temporary folder.
        missing_only (bool): Whether complete translations should be preserved.
    """

    from core.config.translator_config import TranslatorConfig
    from core.database.translation import Translation
    from core.editor.editor import Editor
    from core.mod_file.translation_status import TranslationStatus
    from core.mod_instance.mod import Mod
    from core.translator.service import TranslatorService
    from core.utilities.game_language import GameLanguage
    from tests.setup.data_factory import DataFactory
    from tests.setup.paths import DICTIONARY_PATH

    translation: Translation = DataFactory.stored_translation(
        "Wet and Cold SE - German", tmp_path
    )
    original_mod: Mod = DataFactory.instance_mod("Wet and Cold SE")
    for modfile in original_mod.modfiles:
        modfile.status = TranslationStatus.TranslationInstalled

    editor = Editor(
        translation,
        GameLanguage.German,
        DataFactory.database(tmp_path, [translation]),
        DataFactory.mod_instance([original_mod]),
        TranslatorConfig(),
        MagicMock(spec=TranslatorService),
        tmp_path / "user",
        DICTIONARY_PATH,
    )

    untranslated = editor.all_strings[0]
    untranslated.string.string = None
    untranslated.string.status = StringStatus.TranslationRequired
    complete = next(
        s
        for s in editor.all_strings[1:]
        if s.string.status == StringStatus.TranslationComplete
    )

    bridge: dict[str, Any] = {
        "text_map": {
            untranslated.string.original.strip(): "Bridge Untranslated",
            complete.string.original.strip(): "Bridge Overwrite",
        },
        "edid_map": {},
        "edid_indexed_map": {},
        "formid_map": {},
        "identical_edid_map": {},
        "identical_edid_indexed_map": {},
        "stats": {"formid": 0, "text": 0, "edid": 0, "identical": 0, "total": 0},
    }

    applied: int = editor.apply_bridge(bridge, missing_only=missing_only)

    assert untranslated.string.string == "Bridge Untranslated"
    assert applied >= 1
    if missing_only:
        assert complete.string.string != "Bridge Overwrite"
    else:
        assert complete.string.string == "Bridge Overwrite"
