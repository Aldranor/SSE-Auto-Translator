"""
Copyright (c) Cutleast
"""

from typing import Optional

from mod_manager_lib.core.game_service import GameService
from mod_manager_lib.core.mod_manager.modorganizer.instance_info import MO2InstanceInfo
from mod_manager_lib.core.mod_manager.vortex.profile_info import ProfileInfo
from mod_manager_lib.ui.instance_selector.instance_selector_widget import (
    InstanceSelectorWidget,
)
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from core.config.user_config import UserConfig
from core.utilities.constants import GAME_ID


class NewProfileDialog(QDialog):
    """Collects the name and modlist instance for a new profile."""

    __name_input: QLineEdit
    __instance_selector: InstanceSelectorWidget

    def __init__(
        self,
        user_config: UserConfig,
        parent: Optional[QWidget] = None,
    ) -> None:
        """
        Args:
            user_config (UserConfig): Current settings used to seed the new profile.
            parent (Optional[QWidget], optional): Parent widget. Defaults to None.
        """

        super().__init__(parent)
        self.setWindowTitle(self.tr("Create profile"))
        self.setMinimumWidth(560)

        layout = QVBoxLayout(self)
        layout.addWidget(
            QLabel(
                self.tr(
                    "Each profile keeps its own modlist settings and cache. "
                    "The translation database is shared between profiles."
                )
            )
        )

        form_layout = QFormLayout()
        self.__name_input = QLineEdit()
        self.__name_input.setPlaceholderText(self.tr("For example, Gate to Sovngard"))
        form_layout.addRow(self.tr("Profile name:"), self.__name_input)

        self.__instance_selector = InstanceSelectorWidget()
        self.__instance_selector.set_cur_game(GameService.get_game_by_id(GAME_ID))
        self.__instance_selector.set_cur_instance_data(user_config.mod_instance)
        form_layout.addRow(self.tr("Modlist instance:"), self.__instance_selector)
        layout.addLayout(form_layout)

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        create_button = button_box.button(QDialogButtonBox.StandardButton.Ok)
        create_button.setText(self.tr("Create"))
        create_button.clicked.connect(self.__validate_and_accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    @property
    def profile_name(self) -> str:
        """Returns the trimmed profile name."""

        return self.__name_input.text().strip()

    @property
    def mod_instance(self) -> Optional[MO2InstanceInfo | ProfileInfo]:
        """Returns the selected modlist instance."""

        return self.__instance_selector.get_cur_instance_data()

    def __validate_and_accept(self) -> None:
        """Accepts the dialog only when the name and instance are valid."""

        if not self.profile_name:
            self.__name_input.setFocus()
            return

        if self.__instance_selector.validate():
            self.accept()
