"""
Copyright (c) Cutleast
"""

from typing import override

from cutleast_core_lib.core.utilities.typing_utils import not_none
from cutleast_core_lib.ui.widgets.tree_menu import TreeMenu
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction

from core.translation_provider.source import Source
from ui.utilities.icon_provider import IconProvider, ResourceIcon


class DownloadsMenu(TreeMenu):
    """
    Context menu for the downloads widget.
    """

    open_modpage_requested = Signal()
    """Signal emitted when the user clicks on the open modpage action."""

    retry_requested = Signal()
    """Signal emitted when the user clicks on the retry action."""

    __retry_action: QAction
    __open_modpage_action: QAction

    @override
    def __init__(self) -> None:
        super().__init__()

        self.__init_actions()

        self.__retry_action.triggered.connect(self.retry_requested.emit)
        self.__open_modpage_action.triggered.connect(self.open_modpage_requested.emit)

    def __init_actions(self) -> None:
        self.__retry_action = self.addAction(
            IconProvider.get_qta_icon("mdi6.refresh"),
            self.tr("Retry download"),
        )
        self.__open_modpage_action = self.addAction(
            IconProvider.get_res_icon(ResourceIcon.NexusMods),
            self.tr("Open mod page..."),
        )

    @override
    def open(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, current_item_source: Source, is_failed: bool = False
    ) -> None:
        """
        Opens the context menu at the current cursor position.

        Args:
            current_item_source (Source): The source of the current item.
            is_failed (bool, optional): Whether the item is in a failed state.
        """

        self.__retry_action.setVisible(is_failed)
        self.__open_modpage_action.setIcon(not_none(current_item_source.get_icon()))

        super().open(False)
