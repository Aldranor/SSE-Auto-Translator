"""
Copyright (c) Cutleast
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from cutleast_core_lib.core.utilities.truncate import raw_string
from cutleast_core_lib.ui.widgets.search_bar import SearchBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QMenu,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from core.string.string_status import StringStatus
from core.string.types import String, StringList

if TYPE_CHECKING:
    from .editor_tab import EditorTab


class ReviewItem(QTreeWidgetItem):
    """A combined-review row that keeps its owning editor and string."""

    def __init__(
        self, translation_name: str, editor_tab: EditorTab, string: String
    ) -> None:
        """Creates a row for a string and its owning editor."""

        super().__init__(
            [
                translation_name,
                string.display_id,
                raw_string(string.original, max_length=140),
                raw_string(
                    string.string if string.string is not None else string.original,
                    max_length=140,
                ),
                StringStatus.get_localized_name(string.status),
            ]
        )
        self.editor_tab = editor_tab
        self.string = string
        self.setToolTip(1, string.display_id)
        self.setToolTip(2, string.original)
        self.setToolTip(
            3, string.string if string.string is not None else string.original
        )
        self.setToolTip(4, StringStatus.get_localized_description(string.status))
        for column in range(5):
            self.setForeground(column, string.status.get_fg_color())
            self.setBackground(column, string.status.get_bg_color())


class ReviewWidget(QWidget):
    """Unified review view over all currently open translation editors."""

    __tabs: list[EditorTab]
    __rows: list[ReviewItem]
    __search_text: Optional[tuple[str, bool]] = None
    __show_all: bool = False

    def __init__(self) -> None:
        """Initializes the unified review view."""

        super().__init__()
        self.__tabs = []
        self.__rows = []
        self.__init_ui()

    def __init_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        toolbar = QHBoxLayout()
        layout.addLayout(toolbar)

        self.__search = SearchBar()
        self.__search.searchChanged.connect(self.__on_search_changed)
        toolbar.addWidget(self.__search, 1)

        self.__scope = QComboBox()
        self.__scope.addItem(self.tr("Needs review"), False)
        self.__scope.addItem(self.tr("All strings"), True)
        self.__scope.currentIndexChanged.connect(self.__on_scope_changed)
        toolbar.addWidget(self.__scope)

        self.__count = QLabel()
        self.__count.setProperty("subtitle", True)
        toolbar.addWidget(self.__count)

        self.__save_all_button = QPushButton(self.tr("Save all"))
        self.__save_all_button.clicked.connect(self.__save_all)
        toolbar.addWidget(self.__save_all_button)

        actions = QHBoxLayout()
        layout.addLayout(actions)

        self.__edit_button = QPushButton(self.tr("Edit selected"))
        self.__edit_button.clicked.connect(self.__edit_current)
        actions.addWidget(self.__edit_button)

        self.__complete_button = QPushButton(
            StringStatus.TranslationComplete.get_localized_name()
        )
        self.__complete_button.clicked.connect(
            lambda: self.__set_selected_status(StringStatus.TranslationComplete)
        )
        actions.addWidget(self.__complete_button)

        self.__incomplete_button = QPushButton(
            StringStatus.TranslationIncomplete.get_localized_name()
        )
        self.__incomplete_button.clicked.connect(
            lambda: self.__set_selected_status(StringStatus.TranslationIncomplete)
        )
        actions.addWidget(self.__incomplete_button)

        self.__not_required_button = QPushButton(
            StringStatus.NoTranslationRequired.get_localized_name()
        )
        self.__not_required_button.clicked.connect(
            lambda: self.__set_selected_status(StringStatus.NoTranslationRequired)
        )
        actions.addWidget(self.__not_required_button)
        actions.addStretch()

        self.__tree = QTreeWidget()
        self.__tree.setColumnCount(5)
        self.__tree.setHeaderLabels(
            [
                self.tr("Translation"),
                self.tr("ID"),
                self.tr("Original"),
                self.tr("String"),
                self.tr("Status"),
            ]
        )
        self.__tree.setSelectionMode(QTreeWidget.SelectionMode.ExtendedSelection)
        self.__tree.setUniformRowHeights(True)
        self.__tree.setSortingEnabled(True)
        self.__tree.itemDoubleClicked.connect(lambda *_: self.__edit_current())
        self.__tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.__tree.customContextMenuRequested.connect(self.__open_context_menu)
        layout.addWidget(self.__tree, 1)

        self.__edit_button.setEnabled(False)
        self.__complete_button.setEnabled(False)
        self.__incomplete_button.setEnabled(False)
        self.__not_required_button.setEnabled(False)
        self.__tree.itemSelectionChanged.connect(self.__on_selection_changed)

        self.__bind_shortcut("F1", StringStatus.TranslationComplete)
        self.__bind_shortcut("F2", StringStatus.TranslationIncomplete)
        self.__bind_shortcut("F3", StringStatus.NoTranslationRequired)

    def __bind_shortcut(self, sequence: str, status: StringStatus) -> None:
        shortcut = QShortcut(QKeySequence(sequence), self)
        shortcut.setContext(Qt.ShortcutContext.WidgetWithChildrenShortcut)
        shortcut.activated.connect(lambda: self.__set_selected_status(status))

    def set_tabs(self, tabs: list[EditorTab]) -> None:
        """Refreshes the combined view after translations are opened or closed."""

        for tab in self.__tabs:
            try:
                tab.changed_signal.disconnect(self.__refresh)
            except RuntimeError:
                pass

        self.__tabs = tabs.copy()
        for tab in self.__tabs:
            tab.changed_signal.connect(self.__refresh)

        self.__refresh()

    def __on_search_changed(self, text: str, case_sensitive: bool) -> None:
        self.__search_text = (text, case_sensitive) if text.strip() else None
        self.__refresh()

    def __on_scope_changed(self, _: int) -> None:
        self.__show_all = bool(self.__scope.currentData())
        self.__refresh()

    def __refresh(self) -> None:
        selected_ids = {id(item.string) for item in self.__tree.selectedItems()}
        self.__tree.setSortingEnabled(False)
        self.__tree.clear()
        self.__rows = []

        search_text: Optional[str] = None
        case_sensitive = False
        if self.__search_text is not None:
            search_text, case_sensitive = self.__search_text
            search_text = search_text.strip()
            if not case_sensitive:
                search_text = search_text.lower()

        available_count = 0
        for tab in self.__tabs:
            for string in tab.review_strings:
                if not self.__show_all and string.status not in (
                    StringStatus.TranslationRequired,
                    StringStatus.TranslationIncomplete,
                ):
                    continue

                available_count += 1
                if search_text is not None:
                    row_search_text = (
                        tab.translation_name
                        + string.display_id
                        + string.original
                        + (string.string or "")
                    )
                    if not case_sensitive:
                        row_search_text = row_search_text.lower()
                    if search_text not in row_search_text:
                        continue

                item = ReviewItem(tab.translation_name, tab, string)
                self.__tree.addTopLevelItem(item)
                self.__rows.append(item)
                if id(string) in selected_ids:
                    item.setSelected(True)

        self.__tree.setSortingEnabled(True)
        self.__count.setText(
            self.tr("Showing {0} of {1} strings").format(
                len(self.__rows), available_count
            )
        )
        self.__on_selection_changed()

    def __on_selection_changed(self) -> None:
        has_selection = bool(self.__tree.selectedItems())
        self.__edit_button.setEnabled(has_selection)
        self.__complete_button.setEnabled(has_selection)
        self.__incomplete_button.setEnabled(has_selection)
        self.__not_required_button.setEnabled(has_selection)

    def __selected_items(self) -> list[ReviewItem]:
        return [
            item for item in self.__tree.selectedItems() if isinstance(item, ReviewItem)
        ]

    def __edit_current(self) -> None:
        selected = self.__selected_items()
        if selected:
            selected[0].editor_tab.edit_string_from_review(selected[0].string)

    def __set_selected_status(self, status: StringStatus) -> None:
        grouped: dict[EditorTab, StringList] = {}
        for item in self.__selected_items():
            grouped.setdefault(item.editor_tab, []).append(item.string)

        for tab, strings in grouped.items():
            tab.set_status_from_review(strings, status)

    def __save_all(self) -> None:
        for tab in self.__tabs:
            tab.save_from_review()

    def __open_context_menu(self, position) -> None:
        if not self.__selected_items():
            return

        menu = QMenu(self)
        edit_action = menu.addAction(self.tr("Edit selected"))
        menu.addSeparator()
        complete_action = menu.addAction(
            StringStatus.TranslationComplete.get_localized_name()
        )
        incomplete_action = menu.addAction(
            StringStatus.TranslationIncomplete.get_localized_name()
        )
        no_required_action = menu.addAction(
            StringStatus.NoTranslationRequired.get_localized_name()
        )
        action = menu.exec(self.__tree.viewport().mapToGlobal(position))

        if action == edit_action:
            self.__edit_current()
        elif action == complete_action:
            self.__set_selected_status(StringStatus.TranslationComplete)
        elif action == incomplete_action:
            self.__set_selected_status(StringStatus.TranslationIncomplete)
        elif action == no_required_action:
            self.__set_selected_status(StringStatus.NoTranslationRequired)
