"""
Copyright (c) Cutleast
"""

from pathlib import Path
from typing import Optional

from cutleast_core_lib.ui.theme.manager import ThemeManager
from cutleast_core_lib.ui.widgets.icon_button import IconButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QKeySequence
from PySide6.QtWidgets import (
    QHeaderView,
    QMessageBox,
    QSplitter,
    QStackedWidget,
    QTreeWidget,
    QTreeWidgetItem,
)

from core.config.app_config import AppConfig
from core.database.translation import Translation
from core.translation_provider.provider import TranslationProvider
from core.translator.service import TranslatorService
from core.user_data.user_data import UserData
from ui.utilities.icon_provider import IconProvider

from .editor.editor_tab import EditorTab
from .editor.review_widget import ReviewWidget


class EditorPage(QSplitter):
    """
    Page for translation editor.
    """

    tab_count_updated = Signal(int)
    """
    Signal emitted everytime one or more tabs are opened or closed.

    Args:
        int: New number of open tabs.
    """

    refresh_translation_requested = Signal(Translation)
    """Signal emitted when an editor tab requests a translation reload from disk."""

    __app_config: AppConfig
    __user_data: UserData
    __translator_service: TranslatorService
    __provider: Optional[TranslationProvider] = None

    __tabs: dict[Translation, tuple[EditorTab, QTreeWidgetItem]] = {}
    """
    Mapping of translations to their tabs and the respective item in the list.
    """

    __tab_list_widget: QTreeWidget
    __page_widget: QStackedWidget
    __review_widget: ReviewWidget
    __review_item: QTreeWidgetItem

    def __init__(
        self,
        app_config: AppConfig,
        user_data: UserData,
        translator_service: TranslatorService,
        provider: Optional[TranslationProvider] = None,
    ) -> None:
        """
        Args:
            app_config (AppConfig): The application configuration.
            user_data (UserData): The user data.
            translator_service (TranslatorService): The translator service.
            provider (Optional[TranslationProvider], optional): Translation provider. Defaults to None.
        """

        super().__init__()

        self.__app_config = app_config
        self.__user_data = user_data
        self.__translator_service = translator_service
        self.__provider = provider

        self.__init_ui()

        w: int = self.contentsRect().width()
        self.setSizes([int(0.25 * w), int(0.75 * w)])

    def __init_ui(self) -> None:
        self.setOrientation(Qt.Orientation.Horizontal)

        self.__tab_list_widget = QTreeWidget()
        self.__tab_list_widget.setProperty("no_header", True)
        self.__tab_list_widget.header().hide()
        self.__tab_list_widget.setColumnCount(2)
        self.__tab_list_widget.header().setStretchLastSection(False)
        self.__tab_list_widget.header().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch
        )
        self.__tab_list_widget.header().setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )
        self.addWidget(self.__tab_list_widget)

        self.__review_item = QTreeWidgetItem([self.tr("Review all open translations")])
        self.__review_item.setFont(
            0, ThemeManager.get().theme.texts.emphasized.as_qfont()
        )
        self.__review_item.setHidden(True)
        self.__tab_list_widget.addTopLevelItem(self.__review_item)

        self.__page_widget = QStackedWidget()
        self.addWidget(self.__page_widget)

        self.__review_widget = ReviewWidget()
        self.__page_widget.addWidget(self.__review_widget)

        self.__tab_list_widget.currentItemChanged.connect(
            lambda cur, _: self.__set_tab_from_item(cur)
        )

    def __set_tab_from_item(self, item: Optional[QTreeWidgetItem]) -> None:
        """
        Sets the page widget to the tab corresponding to a specified item.

        Args:
            item (Optional[QTreeWidgetItem]): The item to set the tab for.
        """

        if item is None:
            return

        if item is self.__review_item:
            self.__page_widget.setCurrentWidget(self.__review_widget)
            return

        tabs: dict[QTreeWidgetItem, EditorTab] = {
            item: tab for tab, item in self.__tabs.values()
        }

        # Check if item is a top level item
        tab: EditorTab
        parent_item: Optional[QTreeWidgetItem] = item.parent()
        if parent_item is None:
            tab = tabs[item]
        else:
            tab = tabs[parent_item]
            tab.go_to_modfile(Path(item.text(0)))

        self.__page_widget.setCurrentWidget(tab)

    def __set_tab(self, tab: EditorTab, modfile: Optional[Path] = None) -> None:
        """
        Switches to a specified tab and goes to a specified mod file, if any.

        Args:
            tab (EditorTab): The tab to switch to.
            modfile (Optional[Path], optional):
                The path of the mod file to go to, relative to the game's "Data" folder.
                Defaults to None.
        """

        item: QTreeWidgetItem = next(
            item for t, item in self.__tabs.values() if t is tab
        )
        self.__tab_list_widget.setCurrentItem(item)

        if modfile is not None:
            tab.go_to_modfile(modfile)

    @property
    def tabs(self) -> list[EditorTab]:
        """
        List of all open editor tabs.
        """

        return [tab for tab, _ in self.__tabs.values()]

    def __update_tab_labels(self) -> None:
        for tab, item in self.__tabs.values():
            if tab.changes_pending and not item.text(0).endswith("*"):
                item.setText(0, item.text(0) + "*")
            else:
                item.setText(0, item.text(0).removesuffix("*"))

            font: QFont = item.font(0)
            font.setItalic(tab.changes_pending)
            item.setFont(0, font)

    def close_translation(self, translation: Translation, silent: bool = False) -> None:
        """
        Closes all tabs belonging to a translation.

        Args:
            translation (Translation): The translation to close.
            silent (bool, optional):
                Whether to skip the confirmation dialog if there are unsaved changes.
                Defaults to False.
        """

        tab: EditorTab
        item: QTreeWidgetItem
        tab, item = self.__tabs[translation]

        if tab.changes_pending and not silent:
            message_box = QMessageBox(self)
            message_box.setWindowTitle(self.tr("Close"))
            message_box.setText(
                self.tr("Are you sure you want to close? All changes will be lost!")
            )
            message_box.setStandardButtons(
                QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes
            )
            message_box.setDefaultButton(QMessageBox.StandardButton.Yes)
            message_box.button(QMessageBox.StandardButton.No).setText(self.tr("No"))
            message_box.button(QMessageBox.StandardButton.Yes).setText(self.tr("Yes"))
            ThemeManager.update_widget_styles(message_box)

            if message_box.exec() != QMessageBox.StandardButton.Yes:
                return

        self.__tabs.pop(translation)

        self.__tab_list_widget.takeTopLevelItem(
            self.__tab_list_widget.invisibleRootItem().indexOfChild(item)
        )

        if self.tabs:
            self.__set_tab(self.tabs[-1])
        else:
            self.__page_widget.setCurrentWidget(self.__review_widget)

        self.__review_widget.set_tabs(self.tabs)
        self.__review_item.setHidden(not self.tabs)

        self.tab_count_updated.emit(len(self.tabs))
        self.__update_tab_labels()

    def confirm_translation_reload(self, translation: Translation) -> bool:
        """Confirms discarding unsaved editor changes before reloading a translation."""
        tab_entry = self.__tabs.get(translation)
        if tab_entry is None or not tab_entry[0].changes_pending:
            return True

        message_box = QMessageBox(self)
        message_box.setWindowTitle(self.tr("Refresh translation"))
        message_box.setText(
            self.tr(
                "'{0}' has unsaved changes. Discard them and reload the translation "
                "from disk?"
            ).format(translation.name)
        )
        message_box.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )
        message_box.setDefaultButton(QMessageBox.StandardButton.Cancel)
        message_box.button(QMessageBox.StandardButton.Yes).setText(
            self.tr("Discard and refresh")
        )
        ThemeManager.update_widget_styles(message_box)

        return message_box.exec() == QMessageBox.StandardButton.Yes

    def reload_translation(self, translation: Translation) -> None:
        """Refreshes an open editor tab after its translation was reloaded."""
        tab_entry = self.__tabs.get(translation)
        if tab_entry is None:
            return

        tab_entry[0].reload_from_translation()
        self.__update_tab_labels()

    def open_translation(self, translation: Translation) -> None:
        """
        Opens a translation in a new tab.

        Args:
            translation (Translation): The translation to open.
        """

        # Create new tab if translation is not already open
        if translation not in self.__tabs:
            translation_item = QTreeWidgetItem([translation.name])
            translation_item.setFont(
                0, ThemeManager.get().theme.texts.emphasized.as_qfont()
            )

            translation_tab = EditorTab(
                translation=translation,
                app_config=self.__app_config,
                user_data=self.__user_data,
                translator_service=self.__translator_service,
                provider=self.__provider,
            )
            translation_tab.changed_signal.connect(self.__update_tab_labels)
            translation_tab.close_signal.connect(self.close_translation)
            translation_tab.refresh_translation_requested.connect(
                self.refresh_translation_requested.emit
            )
            self.__tabs[translation] = translation_tab, translation_item
            self.__page_widget.addWidget(translation_tab)

            close_button = IconButton()
            close_button.setObjectName("list_close_button")
            IconProvider.bind_qta_icon(close_button, close_button.setIcon, "mdi6.close")
            close_button.setToolTip(
                self.tr("Close translation")
                + "\t"
                + QKeySequence("Ctrl+W").toString(QKeySequence.SequenceFormat.NativeText)
            )
            close_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)

            for modfile in sorted(translation.strings, key=lambda m: m.name.lower()):
                modfile_item = QTreeWidgetItem([str(modfile)])
                modfile_item.setFirstColumnSpanned(True)
                translation_item.addChild(modfile_item)

            self.__tab_list_widget.addTopLevelItem(translation_item)

            self.__tab_list_widget.setItemWidget(translation_item, 1, close_button)
            close_button.clicked.connect(lambda: self.close_translation(translation))

            translation_item.setExpanded(True)

        self.__review_item.setHidden(False)
        self.__review_widget.set_tabs(self.tabs)

        self.__tab_list_widget.resizeColumnToContents(1)

        # Switch to Tab
        self.__set_tab(self.tabs[-1])

        self.tab_count_updated.emit(len(self.tabs))
        self.__update_tab_labels()
