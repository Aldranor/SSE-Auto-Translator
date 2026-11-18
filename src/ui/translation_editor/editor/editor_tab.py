"""
Copyright (c) Cutleast
"""

import logging
import os
import re
import webbrowser
from pathlib import Path
from tempfile import gettempdir
from typing import Any, Optional, override

from cutleast_core_lib.core.multithreading.progress import ProgressUpdate
from cutleast_core_lib.core.utilities.thread import Thread
from cutleast_core_lib.core.utilities.typing_utils import coalesce, not_none
from cutleast_core_lib.ui.progress.dialog import ProgressDialog
from cutleast_core_lib.ui.progress.display import ProgressDisplay
from cutleast_core_lib.ui.progress.spinner_display import SpinnerDisplayWidget
from cutleast_core_lib.ui.theme.manager import ThemeManager
from cutleast_core_lib.ui.utilities.state_manager import WidgetStateManager
from cutleast_core_lib.ui.utilities.window_manager import WindowManager
from cutleast_core_lib.ui.widgets.elided_label import ElidedLabel
from cutleast_core_lib.ui.widgets.help_label import HelpLabel
from cutleast_core_lib.ui.widgets.search_bar import SearchBar
from PySide6.QtCore import QByteArray, Qt, Signal
from PySide6.QtGui import QAction, QKeySequence, QShortcut, QShowEvent
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.database.exporter import Exporter
from core.database.translation import Translation
from core.editor.editor import Editor
from core.editor.models import EditorString
from core.editor.translation_bridge import TranslationBridge
from core.string.string_extractor import StringExtractor
from core.string.string_status import StringStatus
from core.string.types import StringList
from core.translation_context.related import RelatedString
from core.translation_provider.cdt_api.cdt_id import CdtModId
from core.translation_provider.mod_details import ModDetails
from core.translation_provider.mod_id import ModId
from core.translation_provider.nm_api.nm_api import NexusModsApi
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.provider import TranslationProvider
from core.translation_provider.provider_preference import ProviderPreference
from core.translation_provider.source import Source
from core.translator.models.excerpt import TranslationExcerpt
from core.translator.service import TranslatorService
from core.user_data.user_data import UserData
from ui.string_list.columns import StringsColumns
from ui.widgets.stacked_bar import StackedBar

from .dialog import TranslatorDialog
from .download_translation_dialog import DownloadTranslationDialog
from .editor_menu import EditorMenu
from .editor_toolbar import EditorToolbar
from .strings_widget import StringsWidget


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

    __translation: Translation
    __user_data: UserData
    __translator_service: TranslatorService
    __provider: TranslationProvider

    __editor: Editor

    __init_thread: Optional[Thread]

    __vlayout: QVBoxLayout
    __tool_bar: EditorToolbar
    __title_label: QLabel
    __search_bar: SearchBar
    __strings_num_label: QLabel
    __bar_chart: StackedBar
    __menu: EditorMenu
    __strings_widget: StringsWidget

    __context_help_label: HelpLabel
    __init_spinner: SpinnerDisplayWidget

    __dialog: TranslatorDialog

    def __init__(
        self,
        translation: Translation,
        user_data: UserData,
        translator_service: TranslatorService,
        provider: TranslationProvider,
        user_data_path: Path,
        dictionary_path: Path,
    ) -> None:
        """
        Args:
            translation (Translation): The translation to edit.
            app_config (AppConfig): The application configuration.
            user_data (UserData): The user data.
            translator_service (TranslatorService): The translator service.
            provider (TranslationProvider): The translation provider.
            user_data_path (Path): The path to the user data directory.
            dictionary_path (Path): The folder with the Hunspell dictionaries.
        """

        super().__init__()

        self.__translation = translation
        self.__user_data = user_data
        self.__translator_service = translator_service
        self.__provider = provider

        self.__editor = Editor(
            translation=translation,
            language=user_data.user_config.language,
            database=user_data.database,
            mod_instance=user_data.mod_instance,
            translator_config=user_data.translator_config,
            translator_service=translator_service,
            user_data_path=user_data_path,
            dictionary_path=dictionary_path,
        )
        self.__editor.strings_changed.connect(self.__on_strings_changed)
        self.__editor.strings_modified.connect(self.__on_strings_modified)

        self.__init_thread = None

        self.__init_ui()
        self.__init_shortcuts()
        self.__init_dialog()

        self.__tool_bar.filter_changed.connect(self.__on_state_filter_changed)
        self.__tool_bar.download_translation_requested.connect(
            self.__download_translation
        )
        self.__tool_bar.search_and_replace_requested.connect(self.__search_and_replace)
        self.__tool_bar.api_translation_requested.connect(
            lambda: self.__translate_with_api()
        )
        self.__tool_bar.save_requested.connect(self.__save)
        self.__tool_bar.export_requested.connect(self.__export)
        self.__search_bar.searchChanged.connect(self.__on_text_filter_changed)

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
        self.__strings_widget.visible_string_count_changed.connect(
            self.__on_visible_string_count_changed
        )
        self.__strings_widget.order_changed.connect(self.__on_index_changed)

        self.__menu.expand_all_clicked.connect(self.__expand_all)
        self.__menu.collapse_all_clicked.connect(self.__collapse_all)
        self.__menu.edit_string_requested.connect(self.__edit_string)
        self.__menu.copy_string_requested.connect(self.__copy_selected)
        self.__menu.reset_translation_requested.connect(self.__reset_selected)
        self.__menu.mark_as_requested.connect(self.__set_status)

        self.__dialog.text_changed.connect(self.__on_dialog_text_changed)
        self.__dialog.status_change_requested.connect(self.__on_dialog_status_changed)
        self.__dialog.reset_requested.connect(self.__on_dialog_reset_requested)
        self.__dialog.prev_requested.connect(self.__on_prev_requested)
        self.__dialog.next_requested.connect(self.__on_next_requested)
        self.__dialog.api_translate_requested.connect(self.__on_api_translate_requested)
        self.__dialog.api_translate_selection_requested.connect(
            self.__on_api_translate_selection_requested
        )
        self.__dialog.related_string_requested.connect(
            self.__on_related_string_requested
        )
        self.__dialog.add_word_to_dict_requested.connect(self.__editor.add_word_to_dict)

        self.__update_metadata()
        ThemeManager.get().theme_changed.connect(lambda _: self.__update_metadata())

    def __init_ui(self) -> None:
        self.__vlayout = QVBoxLayout()
        self.__vlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__vlayout)

        self.__init_header()
        self.__init_strings_widget()
        self.__init_context_menu()
        self.__init_footer()

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
        self.__strings_widget = StringsWidget(self.__editor.all_strings)
        self.__vlayout.addWidget(self.__strings_widget)

        WidgetStateManager.get().register_state(
            "editor_tab_strings_widget_header", self.__strings_widget.header()
        )

    def __init_context_menu(self) -> None:
        self.__menu = EditorMenu()

        self.__strings_widget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )

    def __init_footer(self) -> None:
        hlayout = QHBoxLayout()
        hlayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hlayout.setContentsMargins(0, 0, 0, 0)
        self.__vlayout.addLayout(hlayout)

        self.__context_help_label = HelpLabel(
            self.tr(
                "The translation context includes similar strings and contextual "
                "information from the respective mod file where available and is "
                "currently being built for all strings of the translation.<br/>"
                "Depending on the translation size, this may take a bit of time.<p>"
                "You can cancel this any time you want, but note that without the full "
                "context, operations like editing strings and machine translations may "
                "initially take a bit longer."
            )
        )
        hlayout.addWidget(self.__context_help_label)

        self.__init_spinner = SpinnerDisplayWidget()
        hlayout.addWidget(self.__init_spinner)

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

    def __init_dialog(self) -> None:
        self.__dialog = TranslatorDialog()
        self.__dialog.set_strings_count(self.__strings_widget.get_visible_string_count())
        WidgetStateManager.get().register_geometry("translator_dialog", self.__dialog)

    @property
    def changes_pending(self) -> bool:
        """
        Whether there are unsaved changes.
        """

        return self.__editor.changes_pending

    def __edit_string(self, string: Optional[EditorString] = None) -> None:
        """
        Opens a string in the translator dialog.

        Args:
            string (Optional[EditorString]): String to open. Defaults to the current string.
        """

        if string is None:
            string = self.__strings_widget.get_current_string()

        if string is not None:
            assert string.string.id in [s.string.id for s in self.__editor.all_strings]

            self.__goto_index(
                self.__strings_widget.get_index_of_string(string, only_visible=True)
            )

            WindowManager.get().show(self.__dialog, delete_on_close=False)
            self.__dialog.raise_()
            self.__dialog.activateWindow()

    def __on_visible_string_count_changed(self, count: int) -> None:
        self.__dialog.set_strings_count(count)
        self.__on_index_changed()

    def __on_index_changed(self) -> None:
        current_string: Optional[EditorString] = self.__dialog.current_string
        if current_string is not None:
            try:
                index: int = self.__strings_widget.get_index_of_string(
                    current_string, only_visible=True
                )
            except ValueError:
                # The string no longer matches the filters, but stays open until the
                # user navigates to another string.
                pass
            else:
                self.__dialog.set_index(index)

    def __on_next_requested(self) -> None:
        self.__goto_adjacent_string(forward=True)

    def __on_prev_requested(self) -> None:
        self.__goto_adjacent_string(forward=False)

    def __goto_adjacent_string(self, forward: bool) -> None:
        """
        Applies the filters again, so that edited strings that no longer match them
        are hidden, and opens the visible string following or preceding the current
        string in the dialog.

        Args:
            forward (bool): Whether to open the following instead of the preceding one.
        """

        current_string: Optional[EditorString] = self.__dialog.current_string
        self.__strings_widget.reapply_filters()

        if current_string is None:
            self.__goto_index(0)
            return

        adjacent_string: Optional[EditorString] = (
            self.__strings_widget.get_adjacent_visible_string(current_string, forward)
        )
        if adjacent_string is not None:
            self.__goto_index(
                self.__strings_widget.get_index_of_string(
                    adjacent_string, only_visible=True
                )
            )
        elif self.__strings_widget.get_visible_string_count() < 1:
            self.__dialog.close()

    def __on_related_string_requested(self, related_string: RelatedString) -> None:
        try:
            index: int = self.__strings_widget.get_index_of_string(
                self.__editor.get_editor_string(related_string.string), only_visible=True
            )
        except KeyError, ValueError:
            # The string is part of another translation or hidden by the current
            # filter, so its translation is offered for reuse instead.
            QApplication.clipboard().setText(
                related_string.string.string or related_string.string.original
            )
            return

        self.__goto_index(index)

    def __goto_index(self, index: int) -> None:
        string: Optional[EditorString] = self.__strings_widget.get_string_from_index(
            index, only_visible=True
        )
        if string is None:
            self.__dialog.close()
            return

        self.__strings_widget.select_string(string)
        self.__dialog.set_string(string, len(self.__editor.get_sync_candidates(string)))
        self.__dialog.set_index(index)
        self.__dialog.set_context(self.__editor.get_string_context(string))

    def __on_strings_changed(self, changed_strings: list[EditorString]) -> None:
        for changed_string in changed_strings:
            self.__strings_widget.update_string(changed_string)

        current_string: Optional[EditorString] = self.__dialog.current_string
        if any(string is current_string for string in changed_strings):
            self.__dialog.refresh_from_string()

        self.__update_metadata()

    def __on_strings_modified(self) -> None:
        self.__update_metadata()
        self.changed_signal.emit()

    def __update_metadata(self) -> None:
        if self.__editor.changes_pending:
            self.__title_label.setText(self.__translation.name + "*")
        else:
            self.__title_label.setText(self.__translation.name)

        visible_strings: list[EditorString] = self.__strings_widget.get_visible_strings()
        summary: dict[StringStatus, int] = self.__editor.get_string_states_summary(
            visible_strings
        )

        self.__strings_num_label.setText(str(len(visible_strings)))
        self.__bar_chart.setValues(list(summary.values()))
        self.__bar_chart.setColors([s.get_base_color() for s in StringStatus])
        self.__dialog.set_states_summary(summary)

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

    def __save(self) -> None:
        """
        Saves translation.
        """

        self.__editor.save()
        self.__update_metadata()
        self.changed_signal.emit()

    def __download_translation(self) -> None:
        """Download or load a translation archive and apply it to this editor."""

        detected_id = ""
        detected_source = self.__translation.source
        installed_mod = None
        if self.__translation.mod_id is not None:
            detected_id = str(
                self.__translation.mod_id.nm_mod_id
                if isinstance(self.__translation.mod_id, CdtModId)
                else self.__translation.mod_id.mod_id
            )
            detected_source = self.__translation.mod_id.source
        for mod in self.__user_data.mod_instance.mods:
            if any(
                modfile.path in self.__translation.strings
                for modfile in mod.modfiles
            ):
                installed_mod = mod
                if mod.mod_id is not None and (
                    not detected_id
                    or isinstance(self.__translation.mod_id, NxmModId)
                ):
                    detected_id = str(mod.mod_id.mod_id)
                    if detected_source == Source.Local:
                        detected_source = Source.NexusMods
                break
        preference = self.__user_data.user_config.provider_preference
        show_source_selector = preference != ProviderPreference.OnlyNexusMods
        if not show_source_selector:
            detected_source = Source.NexusMods
        elif detected_source not in (Source.Confrerie, Source.NexusMods):
            detected_source = (
                Source.NexusMods
                if preference == ProviderPreference.PreferNexusMods
                else Source.Confrerie
            )

        dialog = DownloadTranslationDialog(
            translation=self.__translation,
            default_source=detected_source,
            mod_id=detected_id,
            show_source_selector=show_source_selector,
            parent=self,
        )
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        def process(
            pdisplay: ProgressDisplay,
        ) -> tuple[Path, dict[Path, StringList], dict[str, Any]]:
            archive_path = dialog.translation_archive
            details: Optional[ModDetails] = None
            source_mod_id = 0
            if archive_path is None:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Searching for translation..."),
                        maximum=0,
                    )
                )
                selected_provider = self.__provider.get_provider_by_source(
                    dialog.source
                )
                match = re.search(r"\d+", dialog.mod_id)
                if match is None:
                    raise ValueError(self.tr("Enter a valid mod ID or URL."))
                original_mod_id = NxmModId(mod_id=int(match.group()))
                candidates: list[ModId] = []
                for modfile_path in self.__editor.strings:
                    available = selected_provider.get_translations(
                        original_mod_id,
                        modfile_path.name,
                        self.__user_data.user_config.language.name,
                    )
                    candidates.extend(available)
                    if candidates:
                        break
                if not candidates:
                    raise ValueError(self.tr("No translation was found for this mod."))

                details = selected_provider.get_mod_details(candidates[0])
                source_mod_id = (
                    candidates[0].nm_mod_id
                    if isinstance(candidates[0], CdtModId)
                    else int(match.group())
                )
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Downloading translation archive ({0})...").format(
                            Path(details.file_name).name
                        ),
                        maximum=0,
                    )
                )
                self.__open_nexus_download_if_needed(candidates[0], dialog.source)
                download_url = selected_provider.request_download(candidates[0])
                archive_path = (
                    Path(gettempdir()) / "sse-at" / Path(details.file_name).name
                )
                TranslationBridge.download_archive(download_url, archive_path)

            original_archive = dialog.original_archive
            if dialog.bridge and original_archive is None:
                version = (
                    details.version
                    if details is not None
                    else (
                        self.__translation.version
                        or (installed_mod.version if installed_mod is not None else "")
                    )
                )
                if not source_mod_id:
                    entered_id = re.search(r"\d+", dialog.mod_id)
                    source_mod_id = int(entered_id.group()) if entered_id else 0
                if source_mod_id:
                    pdisplay.updateMainProgress(
                        ProgressUpdate(
                            status_text=self.tr(
                                "Searching for matching original archive on Nexus..."
                            ),
                            maximum=0,
                        )
                    )
                    self.__provider.get_provider_by_source(Source.NexusMods)
                    nexus = self.__provider.get_provider(NexusModsApi)
                    files = nexus.get_mod_files("skyrimspecialedition", source_mod_id)
                    if not files.files:
                        raise ValueError(
                            self.tr(
                                "No Nexus original archive was found for mod {0}."
                            ).format(source_mod_id)
                        )
                    original_file = TranslationBridge.select_nexus_original_file(
                        files=list(files.files),
                        version=version,
                        modfile_paths=list(self.__editor.strings.keys()),
                        installed_mod=installed_mod,
                    )
                    original_id = NxmModId(
                        mod_id=source_mod_id, file_id=original_file.file_id
                    )
                    pdisplay.updateMainProgress(
                        ProgressUpdate(
                            status_text=self.tr(
                                "Downloading original archive ({0})..."
                            ).format(Path(original_file.file_name).name),
                            maximum=0,
                        )
                    )
                    self.__open_nexus_download_if_needed(
                        original_id, Source.NexusMods
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

            imported: dict[Path, StringList] = {}
            bridge_data: dict[str, Any] = {}
            if dialog.bridge:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr(
                            "Building translation bridge ({0})..."
                        ).format(
                            original_archive.name
                            if original_archive is not None
                            else archive_path.name
                        ),
                        maximum=0,
                    )
                )
                bridge_data = TranslationBridge.build_bridge(
                    translated_source=archive_path,
                    original_source=original_archive,
                    language=self.__user_data.user_config.language.name,
                    target_plugin_names=[path.name for path in self.__editor.strings],
                )
                if (
                    original_archive is None
                    and bridge_data.get("pair_count", 0) == 0
                    and bridge_data.get("identical_count", 0) == 0
                ):
                    raise ValueError(
                        self.tr(
                            "Enter a Nexus mod ID or select an original source for bridge mode."
                        )
                    )
            else:
                pdisplay.updateMainProgress(
                    ProgressUpdate(
                        status_text=self.tr("Extracting strings from archive ({0})...").format(
                            archive_path.name
                        ),
                        maximum=0,
                    )
                )
                imported = StringExtractor().extract_strings(
                    input=archive_path,
                    mod_instance=self.__user_data.mod_instance,
                    language=self.__user_data.user_config.language,
                    max_workers=4,
                )
            return archive_path, imported, bridge_data

        try:
            archive_path, imported, bridge_data = ProgressDialog(process, self).run()
            if dialog.bridge:
                applied = self.__editor.apply_bridge(bridge_data, dialog.missing_only)
                stats: dict[str, int] = bridge_data.get("stats", {})
                detail = self.tr(
                    "Bridge pairs: {0} (FormID: {1}, Text: {2}, EDID: {3}, Identical: {4})"
                ).format(
                    bridge_data.get("pair_count", 0),
                    stats.get("formid", 0),
                    stats.get("text", 0),
                    stats.get("edid", 0),
                    stats.get("identical", 0),
                )
            else:
                applied = self.__editor.apply_imported_strings(
                    imported, dialog.missing_only
                )
                detail = self.tr("Extracted files: {0}").format(len(imported))

            QMessageBox.information(
                self,
                self.tr("Download complete"),
                self.tr("Archive: {0}\n{1}\nStrings applied: {2}").format(
                    archive_path.name, detail, applied
                ),
            )
        except Exception as ex:
            logging.getLogger("EditorTab").exception(
                "Failed to download and apply translation."
            )
            QMessageBox.critical(
                self,
                self.tr("Download failed"),
                self.tr("Could not apply the translation: {0}").format(ex),
            )

    def __open_nexus_download_if_needed(self, mod_id: ModId, source: Source) -> None:
        """Open the Nexus mod-manager link before waiting for a free download."""

        if source == Source.NexusMods and not self.__provider.direct_downloads_possible(
            source
        ):
            assert isinstance(mod_id, NxmModId) and mod_id.file_id is not None
            webbrowser.open(
                NexusModsApi.create_nexus_mods_url(
                    game_id=mod_id.nm_game_id,
                    mod_id=mod_id.mod_id,
                    file_id=mod_id.file_id,
                    mod_manager=True,
                )
            )

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

        selected_strings: list[EditorString] = (
            self.__strings_widget.get_selected_strings()
        )

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
                    len(selected_strings),
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
                    self.__user_data.translator_config_manager.save()
            else:
                return

        additional_instructions: Optional[str]
        continue_: bool
        additional_instructions, continue_ = self.__prompt_additional_instructions()

        if not continue_:
            return

        ProgressDialog(
            lambda pdisplay: self.__editor.translate_with_api(
                selected_strings, additional_instructions, pdisplay
            ),
            QApplication.activeModalWidget(),
        ).run()

    def __prompt_additional_instructions(self) -> tuple[Optional[str], bool]:
        """
        Prompts the user for additional instructions, if supported by the currently
        configured translator API.

        Returns:
            tuple[Optional[str], bool]:
                The additional instructions and if the user chose to continue.
        """

        if self.__translator_service.get_translator().supports_instructions():
            dialog = QInputDialog()
            dialog.setLabelText(self.tr("Additional instructions for the translator:"))
            dialog.setInputMode(QInputDialog.InputMode.TextInput)
            dialog.setOkButtonText(self.tr("Continue"))
            dialog.setCancelButtonText(self.tr("Cancel"))

            WidgetStateManager.get().register_custom(
                "editor_tab/additional_instructions_text",
                lambda: QByteArray(dialog.textValue().encode()),
                lambda state: dialog.setTextValue(bytes(state.data()).decode()),
                dialog,
            )

            if dialog.exec() == QDialog.DialogCode.Accepted:
                return dialog.textValue().strip() or None, True
            else:
                return None, False

        return None, True

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
        selected_items: list[EditorString] = self.__strings_widget.get_selected_strings()
        self.__editor.set_status(selected_items, status)

    def __reset_selected(self) -> None:
        selected_items: list[EditorString] = self.__strings_widget.get_selected_strings()

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
        selected_strings: list[EditorString] = (
            self.__strings_widget.get_selected_strings()
        )

        clipboard_text = ""
        for string in selected_strings:
            for col in StringsColumns.get_columns(type(string.string)):
                clipboard_text += col.get_copy_text(string.string) + "\t"

            clipboard_text = clipboard_text.rstrip("\t")
            clipboard_text += "\n"

        QApplication.clipboard().setText(clipboard_text.rstrip("\n"))

    def __on_text_filter_changed(self, name_filter: str, case_sensitive: bool) -> None:
        self.__strings_widget.set_name_filter(name_filter, case_sensitive)
        self.__update_metadata()

    def __on_state_filter_changed(self, state_filter: list[StringStatus]) -> None:
        self.__strings_widget.set_state_filter(state_filter)
        self.__update_metadata()

    def __on_dialog_text_changed(
        self, string: EditorString, translated_text: str, sync_identical: bool
    ) -> None:
        # Edits that were reverted before they were written back don't count as edits.
        current_text: str = coalesce(string.string.string, string.string.original)
        if translated_text == current_text:
            return

        self.__editor.set_translated_text(string, translated_text, sync_identical)
        self.__editor.set_string_status(
            string, StringStatus.TranslationIncomplete, sync_identical
        )

    def __on_dialog_status_changed(
        self, status: StringStatus, sync_identical: bool
    ) -> None:
        current_string: EditorString = not_none(self.__dialog.current_string)
        self.__editor.set_string_status(current_string, status, sync_identical)

    def __on_dialog_reset_requested(self, sync_identical: bool) -> None:
        current_string: EditorString = not_none(self.__dialog.current_string)
        self.__editor.reset_string(current_string, sync_identical)

    def __on_api_translate_requested(self, sync_identical: bool) -> None:
        current_string: Optional[EditorString] = self.__dialog.current_string
        if current_string is None:
            return

        translated_text: Optional[str] = self.__request_api_translation(current_string)
        if translated_text is None:
            return

        # The dialog applies the translation as an undoable change and writes it back,
        # which also marks the string as incomplete.
        self.__dialog.apply_translated_text(translated_text)

    def __on_api_translate_selection_requested(
        self, excerpt: TranslationExcerpt, sync_identical: bool
    ) -> None:
        current_string: Optional[EditorString] = self.__dialog.current_string
        if current_string is None:
            return

        translated_text: Optional[str] = self.__request_api_translation(
            current_string, excerpt
        )
        if translated_text is None:
            return

        # The dialog writes the complete text back, which also marks the string as
        # incomplete.
        self.__dialog.replace_selected_part(translated_text)

    def __request_api_translation(
        self, string: EditorString, excerpt: Optional[TranslationExcerpt] = None
    ) -> Optional[str]:
        """
        Prompts the user for additional instructions, if supported, and requests an
        API translation for a string or a part of its translation while displaying the
        progress.

        Args:
            string (EditorString): The string to translate.
            excerpt (Optional[TranslationExcerpt], optional):
                Selected part of the string's translation that should be translated
                instead of the entire string. Defaults to None.

        Returns:
            Optional[str]: The translated text or None if the user cancelled.
        """

        additional_instructions: Optional[str]
        continue_: bool
        additional_instructions, continue_ = self.__prompt_additional_instructions()

        if not continue_:
            return None

        translated_text: str = ProgressDialog(
            lambda pdisplay: self.__editor.get_api_translation(
                string, additional_instructions, excerpt, pdisplay
            ),
            self.__dialog,
        ).run()

        return translated_text

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

    @override
    def showEvent(self, event: QShowEvent, /) -> None:
        super().showEvent(event)

        if self.__init_thread is None:
            self.__init_thread = Thread(
                lambda: self.__editor.initialize(self.__init_spinner)
            )
            self.__init_thread.finished.connect(self.__init_spinner.hide)
            self.__init_thread.finished.connect(self.__context_help_label.hide)
            self.__init_thread.start()

    def close_tab(self) -> bool:
        """
        Call this when the tab is closed.

        Returns:
            bool: False if the user cancelled to close the tab.
        """

        # The context is only discarded once the tab is actually closed, as it is never
        # built again for a tab that stays open.
        if not self.__dialog.close():
            return False

        if self.__init_thread is not None and self.__init_thread.isRunning():
            self.__init_spinner.cancel()

        return True
