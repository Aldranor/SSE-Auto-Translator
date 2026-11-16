"""
Copyright (c) Cutleast
"""

from pathlib import Path

from core.database.database import TranslationDatabase
from core.database.database_service import DatabaseService
from core.database.translation import Translation
from core.file_types.plugin.file import PluginFile
from core.mod_instance.mod_instance import ModInstance
from core.translation_provider.source import Source
from core.utilities.game_language import GameLanguage
from tests.setup.data_factory import DataFactory

from ..core_test import CoreTest


class TestProfileDatabase(CoreTest):
    """Tests profile-specific translation catalogs."""

    def test_profile_catalog_is_separate_from_shared_corpus(self, tmp_path: Path) -> None:
        """Loads shared strings without exposing them in an empty profile catalog."""

        language: GameLanguage = GameLanguage.German
        shared_root: Path = tmp_path / "shared"
        profile_root: Path = tmp_path / "profile"
        shared_language_path: Path = shared_root / language.id
        shared_language_path.mkdir(parents=True)
        (profile_root / language.id).mkdir(parents=True)

        translation: Translation = DataFactory.translation(
            "GTS translation",
            shared_language_path,
            {Path("GTS.esp"): []},
        )
        translation.source = Source.Confrerie
        translation.save()

        database = TranslationDatabase(
            userdb_path=shared_root,
            profiledb_path=profile_root,
            appdb_path=tmp_path / "app",
            language=language,
            vanilla_translation=DataFactory.translation("Base", tmp_path / "app"),
            user_translations=[],
            shared_translations=[translation],
        )
        DatabaseService.save_database(database)

        loaded: TranslationDatabase = DatabaseService.load_database(
            tmp_path / "app", shared_root, language, profile_root
        )

        assert loaded.user_translations == []
        assert [item.name for item in loaded.shared_translations] == [
            "GTS translation"
        ]

        DatabaseService.add_translation(loaded.shared_translations[0], loaded)

        assert loaded.user_translations[0].source == Source.Confrerie
        assert loaded.profiledb_path == profile_root

    def test_profile_sync_removes_entries_for_missing_plugins(self, tmp_path: Path) -> None:
        """Keeps only catalog entries whose plugins exist in the active modlist."""

        language: GameLanguage = GameLanguage.German
        shared_root: Path = tmp_path / "shared"
        profile_root: Path = tmp_path / "profile"
        language_path: Path = shared_root / language.id
        language_path.mkdir(parents=True)

        nolvus_translation: Translation = DataFactory.translation(
            "Nolvus translation",
            language_path,
            {Path("Nolvus.esp"): []},
        )
        gts_translation: Translation = DataFactory.translation(
            "GTS translation",
            language_path,
            {Path("GTS.esp"): []},
        )
        nolvus_translation.save()
        gts_translation.save()

        database = TranslationDatabase(
            userdb_path=shared_root,
            profiledb_path=profile_root,
            appdb_path=tmp_path / "app",
            language=language,
            vanilla_translation=DataFactory.translation("Base", tmp_path / "app"),
            user_translations=[nolvus_translation, gts_translation],
            shared_translations=[nolvus_translation, gts_translation],
        )
        modfile = PluginFile(
            name="Nolvus.esp",
            full_path=tmp_path / "Nolvus.esp",
        )
        mod_instance: ModInstance = DataFactory.mod_instance(
            [DataFactory.mod("Nolvus", [modfile])]
        )

        DatabaseService.synchronize_profile_with_modlist(database, mod_instance)

        assert [item.name for item in database.user_translations] == [
            "Nolvus translation"
        ]
        assert gts_translation.path.exists()
