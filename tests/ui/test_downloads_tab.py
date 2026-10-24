"""
Copyright (c) Cutleast
"""

from cutleast_core_lib.test.utils import Utils
from PySide6.QtGui import QAction
from pytest_mock import MockerFixture
from pytestqt.qtbot import QtBot

from core.config.app_config import AppConfig
from core.downloader.download_manager import DownloadManager
from core.translation_provider.provider import TranslationProvider
from core.translation_provider.provider_preference import ProviderPreference
from core.user_data.user_data import UserData
from tests.base_test import BaseTest
from ui.main_page.database.downloads.downloads_tab import DownloadsTab
from ui.main_page.database.downloads.downloads_toolbar import DownloadsToolbar
from core.downloader.file_download import FileDownload
from core.translation_provider.mod_details import ModDetails
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.source import Source
from core.utilities.exceptions import DownloadFailedError


class TestDownloadsTab(BaseTest):
    """
    Tests `ui.main_page.database.downloads.downloads_tab.DownloadsTab`.
    """

    HANDLE_NXM_ACTION: tuple[str, type[QAction]] = "handle_nxm_action", QAction
    """Identifier for accessing the Nexus Mods action."""

    TOOLBAR: tuple[str, type[DownloadsToolbar]] = "toolbar", DownloadsToolbar
    """Identifier for accessing the downloads toolbar."""

    def test_initializes_without_provider(
        self,
        app_config: AppConfig,
        user_data: UserData,
        qtbot: QtBot,
        mocker: MockerFixture,
    ) -> None:
        """
        Tests initialization when no Nexus Mods API is available.

        Args:
            app_config (AppConfig): Application configuration.
            user_data (UserData): User data containing the configuration.
            qtbot (QtBot): Fixture for Qt widgets.
            mocker (MockerFixture): Fixture for mocking dependencies.
        """

        # given
        user_data.user_config.provider_preference = ProviderPreference.OnlyNexusMods
        mocker.patch(
            "core.translation_provider.provider_manager.NexusModsApi",
            side_effect=RuntimeError,
        )
        provider = TranslationProvider(user_data.user_config)
        download_manager = DownloadManager(
            database=user_data.database,
            mod_instance=user_data.mod_instance,
            provider=provider,
            app_config=app_config,
            user_config=user_data.user_config,
            masterlist=user_data.masterlist,
        )

        # when
        widget = DownloadsTab(download_manager, provider)
        qtbot.addWidget(widget)

        # then
        toolbar: DownloadsToolbar = Utils.get_private_field(
            widget, *TestDownloadsTab.TOOLBAR
        )
        handle_nxm_action: QAction = Utils.get_private_field(
            toolbar, *TestDownloadsTab.HANDLE_NXM_ACTION
        )
        assert not handle_nxm_action.isEnabled()

    def test_retry_failed_download(
        self,
        app_config: AppConfig,
        user_data: UserData,
        qtbot: QtBot,
        mocker: MockerFixture,
    ) -> None:
        """
        Tests retrying a failed download from the UI.
        """
        user_data.user_config.provider_preference = ProviderPreference.OnlyNexusMods
        mocker.patch(
            "core.translation_provider.provider_manager.NexusModsApi",
            side_effect=RuntimeError,
        )
        provider = TranslationProvider(user_data.user_config)
        download_manager = DownloadManager(
            database=user_data.database,
            mod_instance=user_data.mod_instance,
            provider=provider,
            app_config=app_config,
            user_config=user_data.user_config,
            masterlist=user_data.masterlist,
        )
        widget = DownloadsTab(download_manager, provider)
        qtbot.addWidget(widget)

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
        download = FileDownload(mod_details=mod_details, source=Source.NexusMods)

        # 1. Add download
        download_manager.request_download(download)
        items = Utils.get_private_field(widget, "download_items", dict)
        assert download in items
        item = items[download]
        assert not item.is_failed

        # 2. Simulate failure
        download_manager.download_failed.emit(download, DownloadFailedError("Failed"))
        assert item.is_failed
        item_widget = Utils.get_private_field(item, "widget", object)
        retry_button = Utils.get_private_field(item_widget, "retry_button", object)
        assert not retry_button.isHidden()

        # 3. Trigger retry via button click
        retry_button.click()

        # 4. Verify item state is reset to pending and not failed
        assert not item.is_failed
        assert retry_button.isHidden()
        assert not download.stale
