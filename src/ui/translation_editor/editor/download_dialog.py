"""
Copyright (c) Cutleast
"""

from typing import Optional

from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

from core.database.translation import Translation
from core.translation_provider.cdt_api.cdt_id import CdtModId
from core.translation_provider.nm_api.nxm_id import NxmModId
from core.translation_provider.source import Source


class DownloadTranslationDialog(QDialog):
    """Collects a translation source and mod identifier for an editor download."""

    __confrerie_button: QRadioButton
    __nexus_button: QRadioButton
    __mod_id_input: QLineEdit
    __missing_only_checkbox: QCheckBox

    def __init__(
        self,
        translation: Translation,
        source_available: dict[Source, bool],
        parent: Optional[QWidget] = None,
    ) -> None:
        """
        Args:
            translation (Translation): Translation currently open in the editor.
            source_available (dict[Source, bool]): Provider availability by source.
            parent (Optional[QWidget], optional): Parent widget. Defaults to None.
        """

        super().__init__(parent)
        self.setWindowTitle(self.tr("Download translation"))
        self.setMinimumWidth(480)

        layout = QVBoxLayout(self)
        layout.addWidget(
            QLabel(
                self.tr("Download and apply a translation for <b>{0}</b>.").format(
                    translation.name
                )
            )
        )

        source_layout = QHBoxLayout()
        button_group = QButtonGroup(self)
        self.__confrerie_button = QRadioButton(
            Source.Confrerie.get_localized_name()
        )
        self.__nexus_button = QRadioButton(Source.NexusMods.get_localized_name())
        button_group.addButton(self.__confrerie_button)
        button_group.addButton(self.__nexus_button)
        source_layout.addWidget(self.__confrerie_button)
        source_layout.addWidget(self.__nexus_button)
        layout.addLayout(source_layout)

        self.__confrerie_button.setEnabled(
            source_available.get(Source.Confrerie, False)
        )
        self.__nexus_button.setEnabled(source_available.get(Source.NexusMods, False))

        default_source: Optional[Source] = None
        initial_id: str = ""
        if isinstance(translation.mod_id, CdtModId):
            default_source = Source.Confrerie
            initial_id = str(translation.mod_id.nm_mod_id)
        elif isinstance(translation.mod_id, NxmModId):
            default_source = Source.NexusMods
            initial_id = str(translation.mod_id.mod_id)
            if translation.mod_id.file_id is not None:
                initial_id += f":{translation.mod_id.file_id}"
        elif translation.source in (Source.Confrerie, Source.NexusMods):
            default_source = translation.source

        if default_source is Source.NexusMods and self.__nexus_button.isEnabled():
            self.__nexus_button.setChecked(True)
        elif self.__confrerie_button.isEnabled():
            self.__confrerie_button.setChecked(True)
        elif self.__nexus_button.isEnabled():
            self.__nexus_button.setChecked(True)

        form_layout = QFormLayout()
        self.__mod_id_input = QLineEdit(initial_id)
        self.__mod_id_input.setPlaceholderText(
            self.tr("Mod ID, or Nexus mod ID:file ID")
        )
        form_layout.addRow(self.tr("Mod ID:"), self.__mod_id_input)

        self.__missing_only_checkbox = QCheckBox(
            self.tr("Apply to untranslated strings only")
        )
        self.__missing_only_checkbox.setChecked(True)
        form_layout.addRow("", self.__missing_only_checkbox)
        layout.addLayout(form_layout)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        download_button = QPushButton(self.tr("Download and apply"))
        download_button.setEnabled(
            self.__confrerie_button.isEnabled() or self.__nexus_button.isEnabled()
        )
        download_button.setDefault(True)
        download_button.clicked.connect(self.accept)
        button_layout.addWidget(download_button)
        cancel_button = QPushButton(self.tr("Cancel"))
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    @property
    def selected_source(self) -> Source:
        """Returns the selected remote translation source."""

        if self.__nexus_button.isChecked():
            return Source.NexusMods
        return Source.Confrerie

    @property
    def mod_id_text(self) -> str:
        """Returns the entered mod identifier."""

        return self.__mod_id_input.text().strip()

    @property
    def missing_only(self) -> bool:
        """Returns whether existing translations should be preserved."""

        return self.__missing_only_checkbox.isChecked()
