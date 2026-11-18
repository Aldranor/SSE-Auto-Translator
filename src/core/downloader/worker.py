"""
Copyright (c) Cutleast
"""

import logging
import time
from pathlib import Path
from queue import Empty, Queue
from tempfile import gettempdir
from typing import Any, Optional, override

from bethkit import BethkitError
from cutleast_core_lib.core.archive_legacy.archive import Archive
from cutleast_core_lib.core.downloader import Downloader
from cutleast_core_lib.core.multithreading.progress import ProgressUpdate
from PySide6.QtCore import QThread, Signal

from core.config.app_config import AppConfig
from core.config.user_config import UserConfig
from core.database.database import TranslationDatabase
from core.database.database_service import DatabaseService
from core.database.translation import Translation
from core.editor.translation_bridge import TranslationBridge
from core.file_types.plugin.file import PluginFile
from core.mod_file.mod_file import ModFile
from core.mod_instance.mod import Mod
from core.mod_instance.mod_instance import ModInstance
from core.string.string_extractor import StringExtractor
from core.string.types import StringList
from core.translation_provider.cdt_api.cdt_id import CdtModId
from core.translation_provider.nm_api.nm_api import NexusModsApi
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.provider import TranslationProvider
from core.translation_provider.source import Source
from core.utilities.exceptions import (
    DownloadFailedError,
    InstallationFailedError,
    NoStringsExtractedError,
)
from core.utilities.temp_folder_provider import TempFolderProvider

from .file_download import FileDownload


class Worker(QThread):
    """
    Class for worker thread of downloader.
    """

    log: logging.Logger

    processing: bool = False
    running: bool = False
    paused: bool = False
    waiting: bool = False

    task_done = Signal()
    """
    This signal gets emitted everytime the worker finishes a task.
    """

    download_started = Signal(FileDownload)
    """
    This signal gets emitted everytime the worker starts a download.

    Args:
        FileDownload: The download that was started.
    """

    download_finished = Signal(FileDownload)
    """
    This signal gets emitted everytime the worker finishes a download.

    Args:
        FileDownload: The download that was finished.
    """

    user_action_required = Signal(FileDownload, str)
    """
    This signal gets emitted everytime the worker requires user action to continue a
    download.

    Args:
        FileDownload: The download that requires user action.
        str: The download URL to open.
    """

    download_failed = Signal(FileDownload, Exception)
    """
    This signal gets emitted everytime the worker fails a download.

    Args:
        FileDownload: The download that failed.
        Exception: The exception that caused the failure.
    """

    progress_updated = Signal(FileDownload, ProgressUpdate)
    """
    Signal emitted when the progress of a download changed.

    Args:
        FileDownload: The download whose progress changed.
        ProgressUpdate: The new progress data.
    """

    __download_queue: Queue[FileDownload]
    __downloader: Downloader
    __app_config: AppConfig
    __user_config: UserConfig
    __provider: TranslationProvider
    __database: TranslationDatabase
    __mod_instance: ModInstance

    def __init__(
        self,
        installer_queue: Queue[FileDownload],
        thread_id: int,
        app_config: AppConfig,
        user_config: UserConfig,
        provider: TranslationProvider,
        database: TranslationDatabase,
        mod_instance: ModInstance,
    ) -> None:
        """
        Args:
            installer_queue (Queue[FileDownload]): Queue of downloads to process.
            thread_id (int): ID of the thread.
            app_config (AppConfig): The application configuration.
            user_config (UserConfig): The user configuration.
            provider (TranslationProvider): The translation provider.
            database (TranslationDatabase): The translation database.
            mod_instance (ModInstance): The loaded mod instance.
        """

        super().__init__()

        self.log = logging.getLogger(f"DownloaderThread-{thread_id}")

        self.__download_queue = installer_queue

        self.__downloader = Downloader(provider.user_agent)
        self.__app_config = app_config
        self.__user_config = user_config
        self.__provider = provider
        self.__database = database
        self.__mod_instance = mod_instance

    def __process_download(self, download: FileDownload) -> None:
        """
        Processes a file download.

        Args:
            download (FileDownload): File to download.
        """

        file_name: str = download.mod_details.file_name

        self.log.info(f"Processing download '{file_name}'...")

        downloads_folder: Path = (
            self.__app_config.downloads_path
            or TempFolderProvider.get().get_temp_folder()
        )
        downloads_folder.mkdir(parents=True, exist_ok=True)
        mod_file: Path = downloads_folder / file_name

        if not mod_file.is_file():
            if not self.__provider.direct_downloads_possible(download.source):
                if download.source == Source.NexusMods:
                    self.log.info("Waiting for free download to be started...")
                    assert isinstance(download.mod_details.mod_id, NxmModId)

                    nxm_url: str = NexusModsApi.create_nexus_mods_url(
                        game_id=download.mod_details.mod_id.nm_game_id,
                        mod_id=download.mod_details.mod_id.mod_id,
                        file_id=download.mod_details.mod_id.file_id,
                        mod_manager=True,
                    )
                    self.user_action_required.emit(download, nxm_url)

                else:
                    raise DownloadFailedError

            self.waiting = True
            url: str = self.__provider.request_download(
                download.mod_details.mod_id, download.source
            )
            self.waiting = False

            self.log.info("Downloading translation...")
            self.progress_updated.emit(
                download,
                ProgressUpdate(
                    status_text=self.tr("Downloading translation..."), value=0, maximum=0
                ),
            )
            self.download_started.emit(download)

            self.__downloader.download(
                url,
                downloads_folder,
                file_name,
                lambda update: self.progress_updated.emit(download, update),
            )
            self.log.info(f"Downloaded translation to '{mod_file}'.")
        else:
            self.log.info("Translation already downloaded.")

        if mod_file.is_file():
            self.__install_translation(download, mod_file)
        else:
            raise DownloadFailedError

        self.log.info("Processing complete.")
        self.download_finished.emit(download)

    def __install_translation(
        self,
        download: FileDownload,
        downloaded_file: Path,
    ) -> None:
        self.log.info("Installing translation...")
        self.progress_updated.emit(
            download,
            ProgressUpdate(
                status_text=self.tr("Installing translation..."), value=0, maximum=0
            ),
        )

        strings: dict[Path, StringList] = {}
        try:
            strings = self.__try_bridge_install(download, downloaded_file)
        except (BethkitError, OSError, ValueError, RuntimeError, LookupError) as ex:
            self.log.warning(
                f"Bridge install failed for '{downloaded_file.name}', "
                f"falling back to standard extraction: {ex}"
            )

        if not strings:
            try:
                strings = StringExtractor().extract_strings(
                    input=downloaded_file,
                    mod_instance=self.__mod_instance,
                    language=self.__database.language,
                    max_workers=self.__app_config.worker_thread_num,
                )
            except Exception as ex:
                raise InstallationFailedError from ex

        if not strings:
            raise NoStringsExtractedError

        translation = Translation(
            name=download.mod_details.display_name,
            path=(
                self.__database.userdb_path
                / self.__database.language.id
                / download.mod_details.display_name
            ),
            mod_id=download.mod_details.mod_id,
            version=download.mod_details.version,
            source=download.source,
            timestamp=download.mod_details.timestamp,
        )
        translation.strings = strings
        translation.save()
        DatabaseService.add_translation(translation, self.__database)

    def __try_bridge_install(
        self,
        download: FileDownload,
        downloaded_file: Path,
    ) -> dict[Path, StringList]:
        """
        Attempt to install a downloaded translation via `TranslationBridge` first,
        including localized plugin string tables. Returns an empty dict when bridge
        data cannot be built so the caller falls back to standard extraction.
        """

        archive = Archive.load_archive(downloaded_file)
        archive_files: list[str] = archive.get_files()
        plugin_suffixes: set[str] = {".esp", ".esm", ".esl"}
        table_suffixes: set[str] = {".strings", ".dlstrings", ".ilstrings"}

        plugin_names: set[str] = {
            Path(name).name.lower()
            for name in archive_files
            if Path(name).suffix.lower() in plugin_suffixes
        }
        plugin_names.update(
            Path(name).parent.name.lower()
            for name in archive_files
            if (
                Path(name).suffix.lower() == ".json"
                and "dynamicstringdistributor" in name.replace("\\", "/").lower()
                and Path(name).parent.suffix.lower() in plugin_suffixes
            )
        )
        table_stems: set[str] = {
            Path(name).stem.rsplit("_", 1)[0].lower()
            for name in archive_files
            if Path(name).suffix.lower() in table_suffixes and "_" in Path(name).stem
        }

        if not plugin_names and not table_stems:
            return {}

        exact_modfiles: list[tuple[Mod, ModFile]] = [
            (mod, modfile)
            for mod in self.__mod_instance.mods
            for modfile in mod.modfiles
            if modfile.name.lower() in plugin_names
            or (
                isinstance(modfile, PluginFile)
                and modfile.path.stem.lower() in table_stems
            )
        ]
        matched_names: set[str] = {mf.name.lower() for _, mf in exact_modfiles}
        unmatched_stems: set[str] = {
            Path(name).stem.lower()
            for name in plugin_names
            if name not in matched_names
        }
        stem_modfiles: list[tuple[Mod, ModFile]] = (
            [
                (mod, modfile)
                for mod in self.__mod_instance.mods
                for modfile in mod.modfiles
                if isinstance(modfile, PluginFile)
                and modfile.path.stem.lower() in unmatched_stems
                and (mod, modfile) not in exact_modfiles
            ]
            if unmatched_stems
            else []
        )
        target_modfiles: list[tuple[Mod, ModFile]] = exact_modfiles + stem_modfiles
        if not target_modfiles:
            return {}

        installed_mod: Optional[Mod] = target_modfiles[0][0]
        source_mod_id = 0
        if isinstance(download.mod_details.mod_id, CdtModId):
            source_mod_id = download.mod_details.mod_id.nm_mod_id
        elif installed_mod.mod_id is not None:
            source_mod_id = installed_mod.mod_id.mod_id

        original_archive: Optional[Path] = None
        if source_mod_id and self.__provider.direct_downloads_possible(Source.NexusMods):
            self.__provider.get_provider_by_source(Source.NexusMods)
            nexus = self.__provider.get_provider(NexusModsApi)
            files = nexus.get_mod_files("skyrimspecialedition", source_mod_id)
            if files.files:
                original_file = TranslationBridge.select_nexus_original_file(
                    files=list(files.files),
                    version=download.mod_details.version,
                    modfile_paths=[mf.path for _, mf in target_modfiles],
                    installed_mod=installed_mod,
                )
                original_id = NxmModId(
                    mod_id=source_mod_id, file_id=original_file.file_id
                )
                original_url = self.__provider.request_download(
                    original_id, Source.NexusMods
                )
                original_archive = (
                    Path(gettempdir())
                    / "sse-at"
                    / Path(original_file.file_name).name
                )
                TranslationBridge.download_archive(original_url, original_archive)

        bridge_data: dict[str, Any] = TranslationBridge.build_bridge(
            translated_source=downloaded_file,
            original_source=original_archive,
            language=self.__database.language.id,
            target_plugin_names=[mf.name for _, mf in target_modfiles],
        )
        if (
            bridge_data.get("pair_count", 0) == 0
            and bridge_data.get("identical_count", 0) == 0
        ):
            return {}

        result: dict[Path, StringList] = {}
        for _, modfile in target_modfiles:
            try:
                target_strings = modfile.get_strings()
                if not target_strings and isinstance(modfile, PluginFile):
                    target_strings = (
                        TranslationBridge.extract_localized_plugin_strings(
                            modfile.full_path, "english"
                        )
                    )
            except (BethkitError, OSError, ValueError, RuntimeError, LookupError) as ex:
                self.log.warning(
                    f"Skipping bridge target '{modfile.name}' due to read error: {ex}"
                )
                continue
            if not target_strings:
                continue
            changed = TranslationBridge.apply_bridge(
                bridge=bridge_data,
                target_strings=target_strings,
                missing_only=False,
            )
            if changed:
                result[modfile.path] = target_strings

        return result

    @override
    def run(self) -> None:
        self.log.info("Thread started.")
        self.running = True

        while self.running:
            if self.paused:
                self.log.info("Thread paused.")
                self.running = False

                while self.paused:
                    time.sleep(0.01)

                self.running = True
                self.log.info("Thread continued.")

            try:
                # Wait at max 1 second for a download or just repeat the loop
                # while the thread is set to running
                download = self.__download_queue.get(timeout=1)
            except Empty:
                continue

            if not download.stale:
                self.processing = True
                try:
                    self.__process_download(download)
                except Exception as ex:
                    self.log.error(
                        f"Failed to process translation '{download.mod_details.file_name}':"
                        f" {ex}",
                        exc_info=ex,
                    )
                    self.download_failed.emit(download, ex)

                self.processing = False
            else:
                self.download_finished.emit(download)

            self.__download_queue.task_done()
            self.task_done.emit()

        self.running = False
        self.log.info("Thread stopped.")
