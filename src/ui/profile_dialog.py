"""
Copyright (c) Cutleast
"""

from typing import Optional

from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.user_data.profile_service import ProfileService
from core.user_data.user_data import UserData

from .new_profile_dialog import NewProfileDialog


class ProfileDialog(QDialog):
    """Selects an existing profile or creates a new one."""

    __profile_service: ProfileService
    __user_data: UserData
    __profile_box: QComboBox

    def __init__(
        self,
        profile_service: ProfileService,
        user_data: UserData,
        parent: Optional[QWidget] = None,
    ) -> None:
        """
        Args:
            profile_service (ProfileService): Profile registry and storage service.
            user_data (UserData): Currently loaded profile settings.
            parent (Optional[QWidget], optional): Parent widget. Defaults to None.
        """

        super().__init__(parent)
        self.__profile_service = profile_service
        self.__user_data = user_data

        self.setWindowTitle(self.tr("Translation profiles"))
        self.setMinimumWidth(460)

        layout = QVBoxLayout(self)
        layout.addWidget(
            QLabel(
                self.tr(
                    "Profiles keep modlist settings and caches separate. "
                    "Their translation database is shared, so matching strings "
                    "can be reused between modlists."
                )
            )
        )

        form_layout = QFormLayout()
        self.__profile_box = QComboBox()
        self.__populate_profiles()
        form_layout.addRow(self.tr("Profile:"), self.__profile_box)
        layout.addLayout(form_layout)

        profile_actions = QHBoxLayout()
        create_button = QPushButton(self.tr("Create profile..."))
        create_button.clicked.connect(self.__create_profile)
        profile_actions.addWidget(create_button)
        rename_button = QPushButton(self.tr("Rename..."))
        rename_button.clicked.connect(self.__rename_profile)
        profile_actions.addWidget(rename_button)
        layout.addLayout(profile_actions)

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Close
            | QDialogButtonBox.StandardButton.Apply
        )
        button_box.button(QDialogButtonBox.StandardButton.Apply).setText(
            self.tr("Switch profile")
        )
        button_box.button(QDialogButtonBox.StandardButton.Apply).clicked.connect(
            self.accept
        )
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    @property
    def selected_profile_id(self) -> str:
        """Returns the selected profile identifier."""

        return str(self.__profile_box.currentData())

    def __populate_profiles(self, selected_profile_id: Optional[str] = None) -> None:
        """Populates the selector from the saved profile registry.

        Args:
            selected_profile_id (Optional[str], optional): Profile to select.
                Defaults to the active profile.
        """

        profile_id: str = (
            selected_profile_id or self.__profile_service.active_profile.id
        )
        self.__profile_box.clear()
        for profile in self.__profile_service.profiles:
            self.__profile_box.addItem(profile.name, profile.id)
        index: int = self.__profile_box.findData(profile_id)
        if index >= 0:
            self.__profile_box.setCurrentIndex(index)

    def __create_profile(self) -> None:
        """Creates a profile and selects it for the subsequent switch."""

        dialog = NewProfileDialog(self.__user_data.user_config, self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        try:
            profile = self.__profile_service.create_profile(
                name=dialog.profile_name,
                mod_instance=dialog.mod_instance,
                user_config=self.__user_data.user_config,
                translator_config=self.__user_data.translator_config,
            )
        except (OSError, ValueError) as ex:
            QMessageBox.critical(
                self,
                self.tr("Profile creation failed"),
                str(ex),
            )
            return

        self.__populate_profiles(profile.id)
        self.accept()

    def __rename_profile(self) -> None:
        """Renames the selected profile."""

        profile_id: str = self.selected_profile_id
        current_name: str = self.__profile_box.currentText()
        new_name, accepted = QInputDialog.getText(
            self,
            self.tr("Rename profile"),
            self.tr("Profile name:"),
            text=current_name,
        )
        if not accepted:
            return

        try:
            self.__profile_service.rename_profile(profile_id, new_name)
        except ValueError as ex:
            QMessageBox.warning(self, self.tr("Rename profile"), str(ex))
            return

        self.__populate_profiles(profile_id)
