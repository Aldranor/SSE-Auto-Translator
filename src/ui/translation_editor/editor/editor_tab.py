"""
Copyright (c) Cutleast
"""

import logging
import os
import re
from pathlib import Path
from typing import Optional, cast

from cutleast_core_lib.core.multithreading.progress import ProgressUpdate
from cutleast_core_lib.ui.progress.dialog import ProgressDialog
from cutleast_core_lib.ui.progress.display import ProgressDisplay
from cutleast_core_lib.ui.theme.manager import ThemeManager
from cutleast_core_lib.ui.utilities.state_manager import WidgetStateManager
from cutleast_core_lib.ui.utilities.window_manager import WindowManager
from cutleast_core_lib.ui.widgets.elided_label import ElidedLabel
from cutleast_core_lib.ui.widgets.search_bar import SearchBar
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.config.app_config import AppConfig
from core.database.exporter import Exporter
from core.database.translation import Translation
from core.editor.editor import Editor
from core.editor.translation_report import TranslationReport
from core.string.string_extractor import StringExtractor
from core.string.string_status import StringStatus
from core.string.types import String, StringList
from core.translation_provider.cdt_api.cdt_id import CdtModId
from core.translation_provider.nm_api.nm_api import NexusModsApi
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.provider import TranslationProvider
from core.translation_provider.source import Source
from core.translator.service import TranslatorService
from core.user_data.user_data import UserData
from ui.string_list.columns import StringsColumns
from ui.widgets.stacked_bar import StackedBar

from .download_dialog import DownloadTranslationDialog
from .editor_menu import EditorMenu
from .editor_toolbar import EditorToolbar
from .strings_widget import StringsWidget
from .translation_report_dialog import TranslationReportDialog
from .translator_dialog import TranslatorDialog


class EditorTab(QWidget):
    """
    Class for editor tabs.
    """

    changed_signal = Signal()
    """
    This signal gets emitted when the tab has unsaved changes.
    """

    close_signal = Signal(Translation)
    """
    This signal gets emitted when tab is to be closed.
    """

    __editor: Editor

    __translation: Translation
    __app_config: AppConfig
    __user_data: UserData
    __translator_service: TranslatorService
    __provider: Optional[TranslationProvider]

    __vlayout: QVBoxLayout
    __title_label: QLabel
    __strings_num_label: QLabel
    __tool_bar: EditorToolbar
    __search_bar: SearchBar
    __bar_chart: StackedBar
    __menu: EditorMenu
    __strings_widget: StringsWidget
    log: logging.Logger = logging.getLogger("EditorTab")
    __last_translation_report: Optional[TranslationReport] = None

    def __init__(
        self,
        translation: Translation,
        app_config: AppConfig,
        user_data: UserData,
        translator_service: TranslatorService,
        provider: Optional[TranslationProvider] = None,
    ) -> None:
        """
        Args:
            translation (Translation): The translation to edit.
            app_config (AppConfig): The application configuration.
            user_data (UserData): The user data.
            translator_service (TranslatorService): The translator service.
            provider (Optional[TranslationProvider], optional):
                The translation provider. Defaults to None.
        """

        super().__init__()

        self.__translation = translation
        self.__app_config = app_config
        self.__user_data = user_data
        self.__translator_service = translator_service
        self.__provider = provider

        self.__editor = Editor(
            translation=translation,
            language=user_data.user_config.language,
            database=user_data.database,
            translator_service=translator_service,
        )
        self.__editor.strings_changed.connect(self.__on_strings_changed)

        self.__init_ui()
        self.__init_shortcuts()

        self.__strings_widget.itemSelectionChanged.connect(
            lambda: self.__tool_bar.set_edit_actions_enabled(
                len(self.__strings_widget.get_selected_strings()) > 0
            ),
        )
        self.__strings_widget.itemActivated.connect(
            lambda item, col: self.__edit_string()
        )
        self.__strings_widget.customContextMenuRequested.connect(
            lambda *_: self.__menu.open(
                bool(self.__strings_widget.get_selected_strings())
            )
        )

        self.__tool_bar.filter_changed.connect(self.set_state_filter)
        self.__tool_bar.apply_database_requested.connect(self.__apply_database)
        self.__tool_bar.download_translation_requested.connect(
            self.__download_translation
        )
        self.__tool_bar.search_and_replace_requested.connect(self.__search_and_replace)
        self.__tool_bar.api_translation_requested.connect(self.__translate_with_api)
        self.__tool_bar.save_requested.connect(self.__save)
        self.__tool_bar.export_requested.connect(self.__export)
        self.__tool_bar.show_report_requested.connect(self.__show_last_report)

        self.__menu.expand_all_clicked.connect(self.__expand_all)
        self.__menu.collapse_all_clicked.connect(self.__collapse_all)
        self.__menu.edit_string_requested.connect(self.__edit_string)
        self.__menu.copy_string_requested.connect(self.__copy_selected)
        self.__menu.reset_translation_requested.connect(self.__reset_selected)
        self.__menu.mark_as_requested.connect(self.__set_status)

        ThemeManager.get().theme_changed.connect(lambda _: self.__update_metadata())

    def __init_ui(self) -> None:
        self.__vlayout = QVBoxLayout()
        self.__vlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__vlayout)

        self.__init_header()
        self.__init_strings_widget()
        self.__init_context_menu()
        self.__update_metadata()

    def __init_header(self) -> None:
        self.__tool_bar = EditorToolbar()
        self.__vlayout.addWidget(self.__tool_bar)

        first_action: QAction = self.__tool_bar.actions()[0]

        title_label = QLabel(self.tr("Translation Editor"))
        title_label.setProperty("title", True)
        self.__tool_bar.insertWidget(first_action, title_label)

        self.__title_label = ElidedLabel(self.__translation.name)
        self.__title_label.setMaximumWidth(300)
        self.__title_label.setProperty("subtitle", True)
        self.__tool_bar.insertWidget(first_action, self.__title_label)

        self.__tool_bar.insertSeparator(first_action)

        self.__search_bar = SearchBar()
        self.__search_bar.searchChanged.connect(self.set_name_filter)
        self.__tool_bar.addWidget(self.__search_bar)

        num_label = QLabel(self.tr("Strings") + ":")
        num_label.setProperty("subtitle", True)
        self.__tool_bar.addWidget(num_label)

        self.__strings_num_label = QLabel()
        self.__strings_num_label.setProperty("subtitle", True)
        self.__tool_bar.addWidget(self.__strings_num_label)

        hlayout = QHBoxLayout()
        self.__vlayout.addLayout(hlayout)

        self.__bar_chart = StackedBar(
            values=[0 for _ in StringStatus],
            colors=[s.get_base_color() for s in StringStatus],
        )
        self.__bar_chart.setFixedHeight(3)
        self.__vlayout.addWidget(self.__bar_chart)

    def __init_strings_widget(self) -> None:
        self.__strings_widget = StringsWidget(self.__editor.strings)
        self.__vlayout.addWidget(self.__strings_widget)

        WidgetStateManager.get().register_state(
            "editor_tab_strings_widget_header", self.__strings_widget.header()
        )

    def __init_shortcuts(self) -> None:
        save_shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        save_shortcut.activated.connect(self.__save)

        close_shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        close_shortcut.activated.connect(
            lambda: self.close_signal.emit(self.__translation)
        )

        complete_shortcut = QShortcut(QKeySequence("F1"), self)
        incomplete_shortcut = QShortcut(QKeySequence("F2"), self)
        no_required_shortcut = QShortcut(QKeySequence("F3"), self)
        reset_shortcut = QShortcut(QKeySequence("F4"), self)

        complete_shortcut.activated.connect(
            lambda: self.__set_status(StringStatus.TranslationComplete)
        )

        incomplete_shortcut.activated.connect(
            lambda: self.__set_status(StringStatus.TranslationIncomplete)
        )

        no_required_shortcut.activated.connect(
            lambda: self.__set_status(StringStatus.NoTranslationRequired)
        )

        reset_shortcut.activated.connect(self.__reset_selected)

    def __init_context_menu(self) -> None:
        self.__menu = EditorMenu()

        self.__strings_widget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

    @property
    def changes_pending(self) -> bool:
        """
        Whether there are unsaved changes.
        """

        return self.__editor.changes_pending

    @property
    def translation_name(self) -> str:
        """Name of the translation displayed in the combined review view."""

        return self.__translation.name

    @property
    def review_strings(self) -> StringList:
        """Strings currently held by this editor, for the combined review view."""

        return self.__editor.all_strings

    def edit_string_from_review(self, string: String) -> None:
        """Opens a string in the regular translator dialog from the review view."""

        self.__edit_string(string)

    def set_status_from_review(self, strings: StringList, status: StringStatus) -> None:
        """Sets statuses for selected strings in the combined review view."""

        self.__editor.set_status(strings, status)

    def save_from_review(self) -> None:
        """Saves this translation when requested by the combined review view."""

        if self.__editor.changes_pending:
            self.__save()

    def __edit_string(self, string: Optional[String] = None) -> None:
        """
        Opens a string in a translator dialog.

        Args:
            string (Optional[String]): String to open. Defaults to the current string.
        """

        if string is None:
            string = self.__strings_widget.get_current_string()

        if string is not None:
            assert string.id in [s.id for s in self.__editor.all_strings]

            dialog = TranslatorDialog(
                parent=self,
                initial_string=string,
                app_config=self.__app_config,
                user_config=self.__user_data.user_config,
                translator=self.__translator_service,
            )
            dialog.update_signal.connect(
                lambda: self.__on_strings_changed([dialog.current_string])
            )
            WidgetStateManager.get().register_geometry("translator_dialog", dialog)
            WindowManager.get().show(dialog)

    def update_matching_strings(self, original: str, translation: str) -> None:
        """
        Update strings that are matching
        """

        self.__editor.apply_to_matching_strings(original, translation)

    def get_visible_string_count(self) -> int:
        """
        Gets the number of visible strings.

        Returns:
            int: Number of visible strings
        """

        count: int = self.__strings_widget.get_visible_string_count()
        return count

    def get_index(self, string: String) -> int:
        """
        Gets the index of a string in the list.

        Args:
            string (String): The string to get the index of.

        Returns:
            int: The index
        """

        index: int = self.__strings_widget.get_index_of_string(string, only_visible=True)
        return index

    def get_string(self, index: int) -> Optional[String]:
        """
        Gets a string from an index.

        Args:
            index (int): The index.

        Returns:
            Optional[String]: The string or None if not found.
        """

        string: Optional[String] = self.__strings_widget.get_string_from_index(
            index, only_visible=True
        )
        return string

    def __on_strings_changed(self, changed_strings: StringList) -> None:
        for changed_string in changed_strings:
            self.__strings_widget.update_string(changed_string)

        self.__update_metadata()
        self.changed_signal.emit()

    def reload_from_translation(self) -> None:
        """Reloads this editor tab from the translation's current in-memory data."""
        self.__editor.reload_from_translation()
        self.__strings_widget.reload_strings(self.__editor.strings)
        self.__update_metadata()
        self.changed_signal.emit()

    def __update_metadata(self) -> None:
        if self.__editor.changes_pending:
            self.__title_label.setText(self.__translation.name + "*")
        else:
            self.__title_label.setText(self.__translation.name)

        visible_strings: StringList = self.__strings_widget.get_visible_strings()
        summary: dict[StringStatus, int] = self.__editor.get_string_states_summary(
            visible_strings
        )

        self.__strings_num_label.setText(str(len(visible_strings)))
        self.__bar_chart.setValues(list(summary.values()))
        self.__bar_chart.setColors([s.get_base_color() for s in StringStatus])

        num_tooltip = ""

        for status, count in summary.items():
            color: str = status.get_fg_color().name()

            num_tooltip += (
                f"<tr><td><font color='{color}'>{status.get_localized_name()}:"
                f"</font></td><td align=right><font color='{color}'>{count}"
                "</font></td></tr>"
            )

        self.__strings_num_label.setToolTip(num_tooltip)
        self.__bar_chart.setToolTip(num_tooltip)


    def __download_translation(self) -> None:
        """
        Opens dialog to download translation from Confrérie or Nexus and apply to missing strings.
        """

        detected_id: Optional[str] = None
        detected_source: Optional[Source] = None

        # 1. Check translation object
        if self.__translation.source in (Source.Confrerie, Source.NexusMods):
            detected_source = self.__translation.source

        if self.__translation.mod_id is not None:
            if isinstance(self.__translation.mod_id, CdtModId):
                detected_id = str(
                    self.__translation.mod_id.nm_mod_id
                    or self.__translation.mod_id.mod_id
                )
                detected_source = Source.Confrerie
            elif isinstance(self.__translation.mod_id, NxmModId):
                detected_id = str(self.__translation.mod_id.mod_id)
                detected_source = Source.NexusMods

        # 2. Check mod instance / meta.ini
        if self.__user_data.mod_instance is not None:
            for modfile_path in self.__translation.strings:
                mf = self.__user_data.mod_instance.get_modfile(modfile_path)
                if mf is not None:
                    for mod in self.__user_data.mod_instance.mods:
                        if mf in mod.modfiles:
                            if not detected_id and mod.mod_id is not None:
                                detected_id = str(mod.mod_id.mod_id)

                            if detected_source is None:
                                meta_path = mod.path / "meta.ini"
                                if meta_path.exists():
                                    try:
                                        import configparser

                                        cp = configparser.ConfigParser()
                                        cp.read(meta_path, encoding="utf-8")
                                        url = cp.get("General", "url", fallback="")
                                        inst_file = cp.get("General", "installationFile", fallback="")
                                        source_str = cp.get("General", "source", fallback="")

                                        if any("confrerie" in s.lower() for s in (url, inst_file, source_str)):
                                            detected_source = Source.Confrerie
                                        elif (
                                            any(
                                                "nexusmods" in s.lower() or "nexus" in s.lower()
                                                for s in (url, inst_file, source_str)
                                            )
                                            or (cp.has_option("General", "modid") and cp.getint("General", "modid", fallback=0) > 0)
                                        ):
                                            detected_source = Source.NexusMods
                                    except Exception as ex:  # noqa: BLE001
                                        self.log.debug(f"Could not read meta.ini for source: {ex}")

                                if detected_source is None and mod.mod_id is not None:
                                    detected_source = Source.NexusMods
                if detected_id and detected_source:
                    break

        if detected_source is None:
            pref = self.__user_data.user_config.provider_preference
            from core.translation_provider.provider_preference import ProviderPreference
            if pref in (ProviderPreference.OnlyNexusMods, ProviderPreference.PreferNexusMods):
                detected_source = Source.NexusMods
            else:
                detected_source = Source.Confrerie

        dialog = DownloadTranslationDialog(
            parent=self,
            translation=self.__translation,
            default_source=detected_source,
            detected_id=detected_id,
        )
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        source = dialog.selected_source
        id_text = dialog.mod_id_text
        local_archive = dialog.local_archive
        local_vo_archive = dialog.local_vo_archive
        missing_only = dialog.missing_only
        bridge_mode = dialog.bridge_mode

        def run_task(pdisplay: ProgressDisplay) -> TranslationReport:
            report = TranslationReport()
            report.bridge_enabled = bridge_mode

            def log_msg(msg: str) -> None:
                self.log.info(msg)
                report.log_messages.append(msg)

            archive_path: Path
            target_version: Optional[str] = None
            original_nm_id: Optional[int] = None

            modfile_paths = list(self.__editor.strings.keys())
            target_plugin_names = [mf_p.name for mf_p in modfile_paths]
            mod_stems = [mf_p.stem.lower() for mf_p in modfile_paths]

            installed_modfile = (
                self.__user_data.mod_instance.get_modfile(modfile_paths[0])
                if modfile_paths
                else None
            )

            if local_archive is not None:
                archive_path = local_archive
                log_msg(f"Using local translation archive: {archive_path.name}")
            else:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Downloading translation archive..."),
                        value=0,
                        maximum=0,
                    )
                )
                import requests

                from core.utilities.temp_folder_provider import TempFolderProvider

                temp_dir = TempFolderProvider.get().get_temp_folder()
                temp_dir.mkdir(parents=True, exist_ok=True)

                download_url: Optional[str] = None
                file_name = "downloaded_translation.7z"

                if source == Source.Confrerie:
                    from core.translation_provider.cdt_api.ctd_api import CDTApi

                    cdt_id: Optional[int] = None
                    try:
                        cdt_id = CDTApi.get_cdt_id_from_url(id_text)
                    except ValueError:
                        m = re.search(r"\d+", id_text)
                        if m:
                            cdt_id = int(m.group(0))

                    if not cdt_id:
                        raise ValueError(
                            self.tr("Invalid Confrérie ID or URL: '{0}'").format(id_text)
                        )

                    url = f"https://www.confrerie-des-traducteurs.fr/api/skyrim/sse-at/{cdt_id}"
                    headers = {"User-Agent": "SSE-AT"}
                    resp = requests.get(url, headers=headers, timeout=30)
                    if resp.status_code == 200:
                        try:
                            data = resp.json()
                            download_url = data.get("DownloadLink")
                            if data.get("Filename"):
                                file_name = data["Filename"]
                            if data.get("Version"):
                                target_version = str(data["Version"]).strip()
                            if data.get("NexusModId"):
                                try:
                                    original_nm_id = int(data["NexusModId"])
                                except (ValueError, TypeError):
                                    pass
                        except Exception as ex:  # noqa: BLE001
                            self.log.debug(f"Could not parse Confrerie API response: {ex}")

                    if not download_url:
                        download_url = f"https://www.confrerie-des-traducteurs.fr/skyrim/telechargement-se/{cdt_id}?fromSseAtAPI=1"

                elif source == Source.NexusMods:
                    if self.__provider is None:
                        raise ValueError(
                            self.tr("Translation provider for Nexus Mods not available.")
                        )

                    pattern = re.compile(
                        r"^(?:https?://(?:www\.)?nexusmods\.com/(?P<game>[a-zA-Z0-9_]+)/mods/)?(?P<mod_id>\d+)(?:.*[?&]file_id=(?P<file_id>\d+))?",
                        re.IGNORECASE,
                    )
                    m = pattern.search(id_text.strip())
                    if not m or not m.group("mod_id"):
                        raise ValueError(
                            self.tr("Invalid Nexus Mod ID or URL: '{0}'").format(id_text)
                        )

                    game_id = m.group("game") or "skyrimspecialedition"
                    nm_id = int(m.group("mod_id"))
                    file_id: Optional[int] = (
                        int(m.group("file_id")) if m.group("file_id") else None
                    )

                    nm_api = cast(
                        NexusModsApi,
                        self.__provider.get_provider_by_source(Source.NexusMods),
                    )

                    target_lang_str = self.__user_data.user_config.language.name

                    if file_id is None:
                        # 1. Check if nm_id is an original mod that has translations on Nexus
                        pdisplay.updateMainProgress(
                            ProgressUpdate(
                                status_text=self.tr(
                                    "Checking Nexus for {0} translations..."
                                ).format(target_lang_str),
                                maximum=0,
                            )
                        )
                        trans_mod_ids: list[int] = []
                        try:
                            trans_mod_ids = nm_api._NexusModsApi__scrape_mod_translations(
                                game_id=game_id,
                                mod_id=nm_id,
                                language=target_lang_str,
                            )
                        except Exception as ex:  # noqa: BLE001
                            self.log.debug(f"Could not scrape translations for mod {nm_id}: {ex}")

                        if trans_mod_ids:
                            original_nm_id = nm_id
                            log_msg(
                                f"Detected original mod {original_nm_id}. Found {len(trans_mod_ids)} "
                                f"{target_lang_str} translation mod(s) on Nexus: {trans_mod_ids}"
                            )

                            # Try get_translations for target plugins to find exact matching files
                            found_trans: list[NxmModId] = []
                            for pname in target_plugin_names:
                                try:
                                    res = nm_api.get_translations(
                                        mod_id=NxmModId(mod_id=original_nm_id, nm_game_id=game_id),
                                        file_name=pname,
                                        language=target_lang_str,
                                    )
                                    if res:
                                        found_trans.extend(res)
                                except Exception as ex:  # noqa: BLE001
                                    self.log.debug(f"get_translations failed for {pname}: {ex}")

                            if found_trans:
                                nm_id = found_trans[0].mod_id
                                file_id = found_trans[0].file_id
                                log_msg(f"Resolved to translation mod {nm_id}, file ID {file_id}.")
                            else:
                                nm_id = trans_mod_ids[0]
                                log_msg(f"Targeting translation mod {nm_id} on Nexus Mods.")

                    if file_id is None:
                        pdisplay.updateMainProgress(
                            ProgressUpdate(
                                status_text=self.tr(
                                    "Querying files for Nexus mod {0}..."
                                ).format(nm_id),
                                maximum=0,
                            )
                        )
                        files_obj = nm_api.get_mod_files(game_id, nm_id)
                        files_list = files_obj.files if files_obj else []
                        if not files_list:
                            raise ValueError(
                                self.tr("No files found on Nexus for mod {0}.").format(
                                    nm_id
                                )
                            )

                        lang_name = target_lang_str.lower()
                        lang_keywords = (
                            lang_name,
                            "trad",
                            "french",
                            "français",
                            "francais",
                            " vf",
                            "[vf]",
                            "(vf)",
                            "_vf",
                            "-vf",
                            "vostfr",
                        )
                        lang_files = [
                            f
                            for f in files_list
                            if any(
                                k in f.name.lower() or k in f.file_name.lower()
                                for k in lang_keywords
                            )
                        ]

                        is_known_translation = (original_nm_id is not None)
                        if not is_known_translation:
                            try:
                                mod_info = nm_api.get_mod_details(
                                    NxmModId(mod_id=nm_id, nm_game_id=game_id)
                                )
                                if getattr(mod_info, "category_id", None) == 42 or any(
                                    k in (mod_info.display_name or "").lower()
                                    for k in lang_keywords
                                ):
                                    is_known_translation = True
                            except Exception as ex:  # noqa: BLE001
                                self.log.debug(f"Could not get mod details: {ex}")

                        if lang_files:
                            candidates = lang_files
                        elif is_known_translation:
                            candidates = files_list
                        else:
                            raise ValueError(
                                self.tr(
                                    "Nexus mod {0} appears to be the original English mod and has no {1} "
                                    "translations listed on Nexus Mods.\n"
                                    "Please enter the Nexus translation mod ID/URL directly, or select a local archive."
                                ).format(nm_id, target_lang_str)
                            )

                        main_file = next(
                            (f for f in candidates if f.is_primary),
                            next(
                                (
                                    f
                                    for f in sorted(
                                        candidates,
                                        key=lambda f: f.uploaded_timestamp,
                                        reverse=True,
                                    )
                                    if getattr(f, "category_id", None) == 1
                                    or (
                                        f.category_name
                                        and f.category_name.upper() == "MAIN"
                                    )
                                ),
                                max(
                                    candidates,
                                    key=lambda f: f.uploaded_timestamp,
                                ),
                            ),
                        )
                        file_id = main_file.file_id
                        file_name = main_file.file_name
                        target_version = main_file.version or main_file.mod_version
                        if original_nm_id is None and not is_known_translation:
                            original_nm_id = nm_id

                    if original_nm_id is None and installed_modfile is not None and self.__user_data.mod_instance is not None:
                        for mod in self.__user_data.mod_instance.mods:
                            if installed_modfile in mod.modfiles and mod.mod_id is not None:
                                try:
                                    original_nm_id = int(mod.mod_id.mod_id)
                                    break
                                except (ValueError, TypeError):
                                    pass

                    nxm_mod_id = NxmModId(
                        mod_id=nm_id,
                        file_id=file_id,
                        nm_game_id=game_id,
                        file_name=file_name,
                    )

                    if not self.__provider.direct_downloads_possible(Source.NexusMods):
                        import webbrowser

                        nxm_url = NexusModsApi.create_nexus_mods_url(
                            game_id=game_id,
                            mod_id=nm_id,
                            file_id=file_id,
                            mod_manager=True,
                        )
                        pdisplay.updateMainProgress(
                            ProgressUpdate(
                                status_text=self.tr(
                                    "Waiting for Nexus download authorization in browser..."
                                ),
                                maximum=0,
                            )
                        )
                        webbrowser.open(nxm_url)

                    try:
                        download_url = self.__provider.request_download(
                            nxm_mod_id, Source.NexusMods
                        )
                    except TimeoutError:
                        raise TimeoutError(
                            self.tr(
                                "Nexus download timed out. For non-premium accounts, "
                                "click 'Mod Manager Download' in the opened browser window, "
                                "or select the archive file manually via 'Browse local archive'."
                            )
                        )

                if not download_url:
                    raise ValueError(
                        self.tr("Could not obtain download URL for translation.")
                    )

                archive_path = temp_dir / file_name
                r = requests.get(
                    download_url,
                    headers={"User-Agent": "SSE-AT"},
                    stream=True,
                    timeout=60,
                )
                r.raise_for_status()
                with open(archive_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1048576):
                        if chunk:
                            f.write(chunk)

            report.translation_source_name = archive_path.name
            report.translation_version = target_version
            log_msg(f"Translation archive obtained: {archive_path.name} (v{target_version or 'unknown'})")

            total_modified = 0
            vo_archive_path: Optional[Path] = local_vo_archive
            vo_version: Optional[str] = None

            # If bridge mode is enabled and no manual VO archive was selected, try smart auto-detection
            if bridge_mode:
                if vo_archive_path is not None:
                    log_msg(f"Using manually selected English VO archive: {vo_archive_path.name}")
                else:
                    pdisplay.updateMainProgress(
                        ProgressUpdate(
                            status_text=self.tr("Searching for matching original English VO..."),
                            maximum=0,
                        )
                    )
                    log_msg(f"Searching for English VO archive (Target translation version: {target_version or 'unknown'})...")

                    candidate_dirs: list[Path] = []
                    if self.__app_config.downloads_path and self.__app_config.downloads_path.exists():
                        candidate_dirs.append(self.__app_config.downloads_path)

                    mo2_inst = self.__user_data.user_config.mod_instance
                    if hasattr(mo2_inst, "base_folder") and mo2_inst.base_folder:
                        mo2_dl = Path(mo2_inst.base_folder) / "downloads"
                        if mo2_dl.exists():
                            candidate_dirs.append(mo2_dl)
                        nolvus_arc = Path(mo2_inst.base_folder).parent / "ARCHIVE"
                        if nolvus_arc.exists():
                            candidate_dirs.append(nolvus_arc)

                    clean_target_v = target_version.lower().lstrip("v").strip() if target_version else None

                    # 1. Search candidate archive folders for an archive matching BOTH mod stem AND target_version
                    if clean_target_v:
                        for cdir in candidate_dirs:
                            for arc in cdir.rglob("*"):
                                if (
                                    arc.is_file()
                                    and arc.suffix.lower() in (".zip", ".7z", ".rar")
                                    and any(st in arc.name.lower() for st in mod_stems)
                                    and clean_target_v in arc.name.lower()
                                ):
                                    vo_archive_path = arc
                                    vo_version = target_version
                                    log_msg(f"Found version-matched VO archive in local library: {arc.name}")
                                    break
                            if vo_archive_path:
                                break

                    # 2. Check meta.ini of the installed mod (only if version matches or target_version is unknown)
                    if vo_archive_path is None and installed_modfile is not None:
                        try:
                            mod_dir = installed_modfile.full_path.parent
                            meta_ini = mod_dir / "meta.ini"
                            if meta_ini.exists():
                                import configparser

                                cp = configparser.ConfigParser()
                                cp.read(meta_ini, encoding="utf-8")
                                meta_v = cp.get("General", "version", fallback=None)
                                install_file = cp.get("General", "installationFile", fallback=None)
                                if install_file and Path(install_file).exists():
                                    clean_meta_v = meta_v.lower().lstrip("v").strip() if meta_v else None
                                    if clean_target_v is None or (clean_meta_v and clean_target_v == clean_meta_v):
                                        vo_archive_path = Path(install_file)
                                        vo_version = meta_v
                                        log_msg(f"Found version-matched VO archive from meta.ini: {vo_archive_path.name} (v{meta_v})")
                        except Exception as ex:  # noqa: BLE001
                            self.log.debug(f"Could not check meta.ini: {ex}")

                    # 3. If still not found and we have original_nm_id and target_version on Nexus:
                    if vo_archive_path is None and self.__provider is not None and original_nm_id and clean_target_v:
                        try:
                            log_msg(f"Checking Nexus for original VO files (Nexus ID: {original_nm_id}, Version: {target_version})...")
                            nm_api = cast(NexusModsApi, self.__provider.get_provider_by_source(Source.NexusMods))
                            files_obj = nm_api.get_mod_files("skyrimspecialedition", original_nm_id)
                            # Filter files matching target version
                            version_candidates = [
                                f
                                for f in files_obj.files
                                if (f.version and f.version.lower().lstrip("v").strip() == clean_target_v)
                                or (f.mod_version and f.mod_version.lower().lstrip("v").strip() == clean_target_v)
                                or (f"-{clean_target_v}-" in f.file_name.lower())
                            ]
                            if not version_candidates:
                                version_candidates = [
                                    f
                                    for f in files_obj.files
                                    if getattr(f, "category_id", None) == 1
                                    or (f.category_name and f.category_name.upper() == "MAIN")
                                ]

                            def score_candidate(f) -> tuple[int, int]:
                                fname = (f.name or "").lower()
                                ffile = (f.file_name or "").lower()
                                combined = f"{fname} {ffile}"
                                score = 0

                                # 1. Stem and keyword matching
                                for p in modfile_paths:
                                    stem = p.stem.lower()
                                    if stem in combined:
                                        score += 20
                                    # Handle BSHeartland -> Bruma
                                    if "heartland" in stem and "bruma" in combined:
                                        score += 18
                                    # Handle BSAssets -> Assets
                                    if "assets" in stem and "assets" in combined:
                                        score += 15

                                # 2. Match installed mod folder name if available
                                if installed_modfile:
                                    inst_mod_name = installed_modfile.full_path.parent.name.lower()
                                    words = [w for w in inst_mod_name.replace("-", " ").replace("_", " ").split() if len(w) > 3]
                                    for w in words:
                                        if w in combined:
                                            score += 5

                                # 3. Penalize patch / fix / update if the plugin being translated is a main ESM
                                is_patch_file = any(w in combined for w in ("patch", "fix", "hotfix", "update", "addon", "compat"))
                                has_main_plugin = any(
                                    p.suffix.lower() in (".esm", ".esp")
                                    and not any(w in p.stem.lower() for w in ("patch", "fix", "compat"))
                                    for p in modfile_paths
                                )
                                if is_patch_file and has_main_plugin:
                                    score -= 30

                                # 4. Prefer MAIN category over OPTIONAL/UPDATE
                                is_main_cat = (getattr(f, "category_id", None) == 1) or (f.category_name and f.category_name.upper() == "MAIN")
                                if is_main_cat:
                                    score += 10

                                # 5. Tie breaker: file size (larger files contain the main ESM records)
                                size = getattr(f, "size_in_bytes", 0) or getattr(f, "size_kb", 0) or 0
                                return (score, size)

                            matching_vo_file = max(version_candidates, key=score_candidate) if version_candidates else None
                            if matching_vo_file:
                                if not self.__provider.direct_downloads_possible(Source.NexusMods):
                                    import webbrowser

                                    nxm_url = NexusModsApi.create_nexus_mods_url(
                                        game_id="skyrimspecialedition",
                                        mod_id=original_nm_id,
                                        file_id=matching_vo_file.file_id,
                                        mod_manager=True,
                                    )
                                    pdisplay.updateMainProgress(
                                        ProgressUpdate(
                                            status_text=self.tr(
                                                "Waiting for Nexus VO download authorization in browser..."
                                            ),
                                            maximum=0,
                                        )
                                    )
                                    webbrowser.open(nxm_url)

                                pdisplay.updateMainProgress(
                                    ProgressUpdate(
                                        status_text=self.tr("Downloading matching English VO archive ({0})...").format(
                                            matching_vo_file.file_name
                                        ),
                                        maximum=0,
                                    )
                                )
                                log_msg(f"Downloading version-matched English VO from Nexus: {matching_vo_file.file_name}")
                                vo_nxm_id = NxmModId(
                                    mod_id=original_nm_id,
                                    file_id=matching_vo_file.file_id,
                                    nm_game_id="skyrimspecialedition",
                                    file_name=matching_vo_file.file_name,
                                    version=matching_vo_file.version,
                                )
                                vo_dl_url = self.__provider.request_download(vo_nxm_id, Source.NexusMods)
                                vo_archive_path = temp_dir / matching_vo_file.file_name
                                vo_version = matching_vo_file.version
                                r_vo = requests.get(
                                    vo_dl_url,
                                    headers={"User-Agent": "SSE-AT"},
                                    stream=True,
                                    timeout=60,
                                )
                                r_vo.raise_for_status()
                                with open(vo_archive_path, "wb") as f_vo:
                                    for chunk in r_vo.iter_content(chunk_size=1048576):
                                        if chunk:
                                            f_vo.write(chunk)
                                log_msg(f"Downloaded English VO archive: {vo_archive_path.name}")
                        except Exception as ex:  # noqa: BLE001
                            log_msg(f"Could not auto-download VO archive from Nexus: {ex}")

                    # 4. Fallback: if no version-matched VO archive was found, use installed mod's installationFile
                    if vo_archive_path is None and installed_modfile is not None:
                        try:
                            mod_dir = installed_modfile.full_path.parent
                            meta_ini = mod_dir / "meta.ini"
                            if meta_ini.exists():
                                import configparser

                                cp = configparser.ConfigParser()
                                cp.read(meta_ini, encoding="utf-8")
                                install_file = cp.get("General", "installationFile", fallback=None)
                                meta_v = cp.get("General", "version", fallback=None)
                                if install_file and Path(install_file).exists():
                                    vo_archive_path = Path(install_file)
                                    vo_version = meta_v
                                    log_msg(
                                        f"Fallback to installed mod VO archive: {vo_archive_path.name} "
                                        f"(v{meta_v or 'unknown'}, translation is v{target_version or 'unknown'})."
                                    )
                        except Exception as ex:  # noqa: BLE001
                            self.log.debug(f"Fallback meta.ini check failed: {ex}")

                    if vo_archive_path is None:
                        for cdir in candidate_dirs:
                            for arc in cdir.rglob("*"):
                                if (
                                    arc.is_file()
                                    and arc.suffix.lower() in (".zip", ".7z", ".rar")
                                    and any(st in arc.name.lower() for st in mod_stems)
                                ):
                                    vo_archive_path = arc
                                    log_msg(f"Fallback to locally found VO archive: {arc.name}")
                                    break
                            if vo_archive_path:
                                break

            report.vo_archive_name = vo_archive_path.name if vo_archive_path else None
            report.vo_archive_version = vo_version

            # 4. If vo_archive_path found, build and apply Translation Bridge!
            if vo_archive_path and vo_archive_path.exists():
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Building bridge with original VO ({0})...").format(vo_archive_path.name),
                        maximum=0,
                    )
                )
                from core.editor.translation_bridge import TranslationBridge

                try:
                    log_msg(f"Building bridge between translation ({archive_path.name}) and VO ({vo_archive_path.name})...")
                    bridge_data = TranslationBridge.build_bridge(
                        translated_source=archive_path,
                        original_source=vo_archive_path,
                        target_plugin_names=target_plugin_names,
                    )
                    report.bridge_pairs_count = bridge_data.get("pair_count", 0)
                    report.bridge_unique_phrases_count = len(bridge_data.get("text_map", {}))
                    log_msg(
                        f"Bridge constructed: {report.bridge_pairs_count} pair(s), "
                        f"{report.bridge_unique_phrases_count} unique phrase(s) mapped."
                    )

                    bridge_count = self.__editor.apply_bridge(
                        bridge=bridge_data,
                        missing_only=missing_only,
                    )
                    stats = bridge_data.get("stats", {})
                    report.bridge_formid_applied = stats.get("formid", 0)
                    report.bridge_text_applied = stats.get("text", 0)
                    report.bridge_edid_applied = stats.get("edid", 0)
                    report.bridge_identical_applied = stats.get("identical", 0)
                    report.bridge_total_applied = bridge_count
                    total_modified += bridge_count
                    log_msg(
                        f"Bridge applied {bridge_count} string(s) "
                        f"(FormID: {report.bridge_formid_applied}, "
                        f"Exact Text: {report.bridge_text_applied}, "
                        f"EDID: {report.bridge_edid_applied}, "
                        f"Identical/To verify: {report.bridge_identical_applied})."
                    )
                    if bridge_count == 0 and report.bridge_pairs_count > 0:
                        log_msg("Note: Bridge found pairs, but target strings either already had translations or did not match.")
                    elif report.bridge_pairs_count == 0:
                        report.bridge_warning = self.tr(
                            "Bridge found 0 matching translation pairs between VO and translation archive. "
                            "Ensure the VO archive contains the same plugin files as the translation."
                        )
                except Exception as ex:
                    log_msg(f"Bridge building failed: {ex}")
                    report.bridge_warning = str(ex)
                    self.log.warning(f"Bridge building failed: {ex}", exc_info=ex)
            elif bridge_mode:
                report.bridge_warning = self.tr(
                    "Original English VO archive could not be auto-detected. "
                    "You can select it manually in 'Download translation' using 'Browse VO archive'."
                )
                log_msg("Bridge skipped: no English VO archive found.")

            # 5. Extract and apply standard/direct matches (MCM txt, DSD, direct FormIDs)
            pdisplay.updateMainProgress(
                ProgressUpdate(
                    status_text=self.tr("Extracting and matching strings..."),
                    value=0,
                    maximum=0,
                )
            )

            extractor = StringExtractor()
            extracted_strings = extractor.extract_strings(
                input=archive_path,
                mod_instance=self.__user_data.mod_instance,
                language=self.__user_data.user_config.language,
                ignore_states=[],
                pdisplay=pdisplay,
            )

            report.extracted_files_count = len(extracted_strings)
            report.extracted_file_names = [p.name for p in extracted_strings]
            log_msg(f"Direct extraction found {len(extracted_strings)} file(s) in translation archive.")

            standard_modified = self.__editor.apply_translation_strings(
                extracted_strings, missing_only=missing_only
            )
            report.standard_applied = standard_modified
            total_modified += standard_modified
            log_msg(f"Direct matching applied {standard_modified} string(s).")

            report.total_modified = total_modified
            report.remaining_missing = sum(
                1 for s in self.__editor.all_strings if s.status == StringStatus.TranslationRequired
            )
            log_msg(f"Translation completed: {total_modified} string(s) modified, {report.remaining_missing} untranslated.")
            return report

        try:
            report: TranslationReport = ProgressDialog(run_task).run()
            self.__last_translation_report = report
            self.__tool_bar.set_report_available(True)
            TranslationReportDialog(self, report).exec()
        except Exception as ex:
            self.__editor.log.error(
                f"Download/apply translation failed: {ex}", exc_info=ex
            )
            QMessageBox.critical(
                self,
                self.tr("Error"),
                self.tr("Failed to download or apply translation:\n{0}").format(
                    str(ex)
                ),
            )

    def __show_last_report(self) -> None:
        """
        Shows the last translation report dialog.
        """
        if self.__last_translation_report is not None:
            TranslationReportDialog(self, self.__last_translation_report).exec()

    def __save(self) -> None:
        """
        Saves translation.
        """

        self.__editor.save()
        self.__update_metadata()
        self.changed_signal.emit()

    def __apply_database(self) -> None:
        """
        Applies database to untranslated strings.
        """

        modified_strings: int = self.__editor.apply_database(
            self.__strings_widget.get_selected_strings()
        )

        messagebox = QMessageBox(QApplication.activeModalWidget())
        messagebox.setWindowTitle(self.tr("Success!"))
        messagebox.setText(
            self.tr(
                "Translated %n string from database.",
                "Translated %n strings from database.",
                modified_strings,
            )
        )
        messagebox.exec()

    def __search_and_replace(self) -> None:
        """
        Opens dialog for advanced search and replace operations.
        """

        dialog = QDialog(QApplication.activeModalWidget())
        dialog.setMinimumWidth(700)
        dialog.setWindowTitle(self.tr("Search and Replace"))

        vlayout = QVBoxLayout()
        dialog.setLayout(vlayout)

        flayout = QFormLayout()
        vlayout.addLayout(flayout)

        search_entry = QLineEdit()
        flayout.addRow(self.tr("Search"), search_entry)

        replace_entry = QLineEdit()
        flayout.addRow(self.tr("Replace"), replace_entry)

        case_sensitivity_checkbox = QCheckBox(self.tr("Case sensitive"))
        flayout.addRow(case_sensitivity_checkbox)

        vlayout.addStretch()

        hlayout = QHBoxLayout()
        vlayout.addLayout(hlayout)

        hlayout.addStretch()

        apply_button = QPushButton(self.tr("Apply"))
        apply_button.setDefault(True)
        apply_button.clicked.connect(dialog.accept)
        hlayout.addWidget(apply_button)

        cancel_button = QPushButton(self.tr("Cancel"))
        cancel_button.clicked.connect(dialog.reject)
        hlayout.addWidget(cancel_button)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            pattern: re.Pattern
            if case_sensitivity_checkbox.isChecked():
                pattern = re.compile(re.escape(search_entry.text()))
            else:
                pattern = re.compile(re.escape(search_entry.text()), re.IGNORECASE)

            self.__editor.apply_regex(
                self.__strings_widget.get_selected_strings(),
                replace_entry.text(),
                pattern,
            )

    def __translate_with_api(self) -> None:
        """
        Opens dialog to configure batch translation via user configured API.
        """

        if self.__user_data.translator_config.show_confirmation_dialogs:
            dialog = QDialog(QApplication.activeModalWidget())
            dialog.setWindowTitle(self.tr("Translate with API"))

            vlayout = QVBoxLayout()
            dialog.setLayout(vlayout)

            label = QLabel(
                self.tr(
                    "Are you sure you want to translate %n string via translator API?\n"
                    "Depending on the translator API this can raise unexpected costs.",
                    "Are you sure you want to translate %n strings via translator API?\n"
                    "Depending on the translator API this can raise unexpected costs.",
                    len(self.__strings_widget.get_selected_strings()),
                )
            )
            vlayout.addWidget(label)

            vlayout.addStretch()

            hlayout = QHBoxLayout()
            vlayout.addLayout(hlayout)

            hlayout.addStretch()

            do_not_show_again_checkbox = QCheckBox(self.tr("Don't show again"))
            hlayout.addWidget(do_not_show_again_checkbox)

            confirm_button = QPushButton(self.tr("Continue"))
            confirm_button.clicked.connect(dialog.accept)
            confirm_button.setDefault(True)
            hlayout.addWidget(confirm_button)

            cancel_button = QPushButton(self.tr("Cancel"))
            cancel_button.clicked.connect(dialog.reject)
            hlayout.addWidget(cancel_button)

            if dialog.exec() == QDialog.DialogCode.Accepted:
                if do_not_show_again_checkbox.isChecked():
                    self.__user_data.translator_config.show_confirmation_dialogs = False
                    self.__user_data.translator_config.save()
            else:
                return

        ProgressDialog(
            lambda pdisplay: self.__editor.translate_with_api(
                self.__strings_widget.get_selected_strings(), pdisplay
            ),
            QApplication.activeModalWidget(),
        ).run()

    def __export(self) -> None:
        """
        Exports translation in DSD format to a user selected path.
        """

        if self.__editor.changes_pending:
            message_box = QMessageBox(self)
            message_box.setWindowTitle(self.tr("Save before export?"))
            message_box.setText(
                self.tr(
                    "Do you want to save the translation before exporting? Unsaved "
                    "changes are not exported."
                )
            )
            message_box.setStandardButtons(
                QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes
            )
            message_box.setDefaultButton(QMessageBox.StandardButton.Yes)
            message_box.button(QMessageBox.StandardButton.No).setText(
                self.tr("Export only")
            )
            message_box.button(QMessageBox.StandardButton.Yes).setText(
                self.tr("Save and export")
            )
            ThemeManager.update_widget_styles(message_box)

            if message_box.exec() == QMessageBox.StandardButton.Yes:
                self.__save()

        file_dialog = QFileDialog(QApplication.activeModalWidget())
        file_dialog.setWindowTitle(self.tr("Export Translation (DSD Format only)"))
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)

        if file_dialog.exec():
            folder = file_dialog.selectedFiles()[0]
            folder = os.path.normpath(folder)
            folder_path = Path(folder)

            Exporter.export_translation(
                self.__translation, self.__user_data.mod_instance, folder_path
            )

            messagebox = QMessageBox(QApplication.activeModalWidget())
            messagebox.setWindowTitle(self.tr("Success!"))
            messagebox.setText(self.tr("Translation successfully exported."))
            messagebox.exec()

    def __set_status(self, status: StringStatus) -> None:
        selected_items: StringList = self.__strings_widget.get_selected_strings()
        self.__editor.set_status(selected_items, status)

    def __reset_selected(self) -> None:
        selected_items: StringList = self.__strings_widget.get_selected_strings()

        if not selected_items:
            return

        message_box = QMessageBox(QApplication.activeModalWidget())
        message_box.setWindowTitle(self.tr("Reset selected String(s)"))
        message_box.setText(
            self.tr("Are you sure you want to reset the selected string(s)?")
        )
        message_box.setStandardButtons(
            QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes
        )
        message_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        message_box.button(QMessageBox.StandardButton.No).setText(self.tr("No"))
        message_box.button(QMessageBox.StandardButton.Yes).setText(self.tr("Yes"))
        ThemeManager.update_widget_styles(message_box)

        if message_box.exec() == QMessageBox.StandardButton.Yes:
            self.__editor.reset_strings(selected_items)

    def __copy_selected(self) -> None:
        """
        Copies current selected strings to clipboard.
        """

        selected_strings: StringList = self.__strings_widget.get_selected_strings()

        clipboard_text = ""
        for string in selected_strings:
            for col in StringsColumns.get_columns(type(string)):
                clipboard_text += col.get_copy_text(string) + "\t"

            clipboard_text = clipboard_text.rstrip("\t")
            clipboard_text += "\n"

        QApplication.clipboard().setText(clipboard_text.rstrip("\n"))

    def set_name_filter(self, name_filter: str, case_sensitive: bool) -> None:
        """
        Sets the name filter.

        Args:
            name_filter (str): The name to filter by.
            case_sensitive (bool): Case sensitivity.
        """

        self.__strings_widget.set_name_filter(name_filter, case_sensitive)
        self.__update_metadata()

    def set_state_filter(self, state_filter: list[StringStatus]) -> None:
        """
        Sets the state filter.

        Args:
            state_filter (list[StringStatus]): The states to filter by.
        """

        self.__strings_widget.set_state_filter(state_filter)
        self.__update_metadata()

    def go_to_modfile(self, modfile: Path) -> None:
        """
        Selects and scrolls to a specified mod file item.

        Args:
            modfile (Path):
                The path of the mod file, relative to the game's "Data" folder.
        """

        self.__strings_widget.go_to_modfile(modfile)

    def __collapse_all(self) -> None:
        self.__strings_widget.collapseAll()

    def __expand_all(self) -> None:
        self.__strings_widget.expandAll()
