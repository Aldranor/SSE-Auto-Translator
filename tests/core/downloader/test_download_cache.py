"""
Copyright (c) Cutleast
"""

import time
from pathlib import Path

from core.downloader.cached_downloads import CachedModDownloads
from core.downloader.file_download import FileDownload
from core.downloader.mod_info import ModInfo
from core.downloader.translation_download import TranslationDownload
from core.translation_provider.mod_details import ModDetails
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.source import Source


def test_cached_mod_downloads_serialization(tmp_path: Path) -> None:
    """Tests that CachedModDownloads serializes to JSON and deserializes cleanly."""
    mod_details = ModDetails(
        mod_id=NxmModId(mod_id=123, file_id=456, nm_game_id="skyrimspecialedition"),
        file_name="TestTranslation.7z",
        version="1.0",
        author="Traducteur",
        display_name="Test Translation FR",
        timestamp=1700000000,
        uploader="TradUploader",
        modpage_url="https://nexusmods.com/skyrimspecialedition/mods/123",
    )
    file_download = FileDownload(mod_details=mod_details, source=Source.NexusMods)
    translation_download = TranslationDownload(
        mod_info=ModInfo(
            display_name="Test Translation FR",
            mod_id=NxmModId(mod_id=123, nm_game_id="skyrimspecialedition"),
            source=Source.NexusMods,
        ),
        available_downloads=[file_download],
    )

    cached = CachedModDownloads(
        timestamp=time.time(),
        files={"test_mod.esp": [translation_download]},
    )

    cache_file = tmp_path / "cache_entry.json"
    cache_file.write_text(cached.model_dump_json(), encoding="utf-8")

    loaded = CachedModDownloads.model_validate_json(
        cache_file.read_text(encoding="utf-8")
    )
    assert "test_mod.esp" in loaded.files
    assert len(loaded.files["test_mod.esp"]) == 1
    loaded_td = loaded.files["test_mod.esp"][0]
    assert loaded_td.mod_info.display_name == "Test Translation FR"
    assert loaded_td.available_downloads[0].mod_details.file_name == "TestTranslation.7z"
