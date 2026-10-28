"""
Copyright (c) Cutleast
"""

from pathlib import Path
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QGroupBox,
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
    """
    Dialog to re-download translation from Confrérie des Traducteurs or Nexus Mods.
    """

    def __init__(
        self,
        parent: Optional[QWidget],
        translation: Translation,
        default_source: Optional[Source] = None,
        detected_id: Optional[str] = None,
    ) -> None:
        """
        Initializes the download translation dialog.

        Args:
            parent (Optional[QWidget]): Parent widget.
            translation (Translation): Translation being edited.
            default_source (Source, optional): Default source to select. Defaults to Confrerie.
            detected_id (Optional[str], optional): Detected mod ID if any. Defaults to None.
        """
        super().__init__(parent)

        self.setWindowTitle(self.tr("Download translation"))
        self.setMinimumWidth(550)

        self.__selected_file: Optional[Path] = None
        self.__selected_vo_file: Optional[Path] = None

        layout = QVBoxLayout(self)

        # Info header
        info_label = QLabel(
            self.tr("Download translation for: <b>{0}</b>").format(translation.name)
        )
        info_label.setTextFormat(Qt.TextFormat.RichText)
        layout.addWidget(info_label)

        # Source Selection Group
        source_group = QGroupBox(self.tr("Source"))
        source_layout = QHBoxLayout(source_group)
        self.__button_group = QButtonGroup(self)

        self.__radio_confrerie = QRadioButton(self.tr("Confrérie des Traducteurs"))
        self.__radio_nexus = QRadioButton(self.tr("Nexus Mods"))

        self.__button_group.addButton(self.__radio_confrerie, 1)
        self.__button_group.addButton(self.__radio_nexus, 2)

        source_layout.addWidget(self.__radio_confrerie)
        source_layout.addWidget(self.__radio_nexus)
        layout.addWidget(source_group)

        # Determine initial source
        if default_source is None or default_source == Source.Local:
            if translation.source in (Source.NexusMods, Source.Confrerie):
                default_source = translation.source
            elif isinstance(translation.mod_id, NxmModId):
                default_source = Source.NexusMods
            elif isinstance(translation.mod_id, CdtModId):
                default_source = Source.Confrerie
            else:
                default_source = Source.Confrerie

        if default_source == Source.NexusMods:
            self.__radio_nexus.setChecked(True)
        else:
            self.__radio_confrerie.setChecked(True)

        # Determine prefill ID
        initial_id = ""
        if detected_id:
            initial_id = str(detected_id)
        elif translation.mod_id is not None:
            if isinstance(translation.mod_id, CdtModId):
                initial_id = str(
                    translation.mod_id.nm_mod_id or translation.mod_id.mod_id
                )
            elif isinstance(translation.mod_id, NxmModId):
                initial_id = str(translation.mod_id.mod_id)

        # Input form
        form_layout = QFormLayout()

        self.__id_input = QLineEdit()
        self.__id_input.setPlaceholderText(
            self.tr("Nexus Mod ID or Confrérie URL / ID (e.g. 70917)")
        )
        self.__id_input.setText(initial_id)
        form_layout.addRow(self.tr("Mod ID / URL:"), self.__id_input)

        # Local archive option
        archive_layout = QHBoxLayout()
        self.__archive_label = QLabel(self.tr("None"))
        self.__archive_label.setStyleSheet("color: gray;")
        browse_button = QPushButton(self.tr("Browse archive..."))
        browse_button.clicked.connect(self.__on_browse_archive)
        archive_layout.addWidget(self.__archive_label, 1)
        archive_layout.addWidget(browse_button)
        form_layout.addRow(self.tr("Or local archive:"), archive_layout)

        # Matching English VO archive (Bridge mode)
        vo_layout = QHBoxLayout()
        self.__vo_label = QLabel(self.tr("Auto-detect / None"))
        self.__vo_label.setStyleSheet("color: gray;")
        browse_vo_button = QPushButton(self.tr("Browse VO archive..."))
        browse_vo_button.clicked.connect(self.__on_browse_vo)
        vo_layout.addWidget(self.__vo_label, 1)
        vo_layout.addWidget(browse_vo_button)
        form_layout.addRow(self.tr("Original VO (Bridge):"), vo_layout)

        # Missing strings only checkbox
        self.__missing_only_checkbox = QCheckBox(
            self.tr("Apply to missing strings only")
        )
        self.__missing_only_checkbox.setChecked(True)
        form_layout.addRow("", self.__missing_only_checkbox)

        # Bridge mode checkbox
        self.__bridge_mode_checkbox = QCheckBox(
            self.tr("Bridge mode (auto-match via original VO for ESL/version differences)")
        )
        self.__bridge_mode_checkbox.setChecked(True)
        form_layout.addRow("", self.__bridge_mode_checkbox)

        layout.addLayout(form_layout)

        # Dialog buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        self.__download_button = QPushButton(self.tr("Download & Apply"))
        self.__download_button.setDefault(True)
        self.__download_button.clicked.connect(self.accept)
        button_layout.addWidget(self.__download_button)

        cancel_button = QPushButton(self.tr("Cancel"))
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)

        layout.addLayout(button_layout)

    def __on_browse_vo(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Select matching original VO archive or plugin"),
            "",
            self.tr("Supported Files (*.7z *.zip *.rar *.esp *.esm *.esl);;All Files (*.*)"),
        )
        if file_path:
            self.__selected_vo_file = Path(file_path)
            self.__vo_label.setText(self.__selected_vo_file.name)
            self.__vo_label.setStyleSheet("color: normal;")

    def __on_browse_archive(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Select translation archive"),
            "",
            self.tr("Archives (*.7z *.zip *.rar);;All Files (*.*)"),
        )
        if file_path:
            self.__selected_file = Path(file_path)
            self.__archive_label.setText(self.__selected_file.name)
            self.__archive_label.setStyleSheet("color: normal;")
            self.__download_button.setText(self.tr("Apply from archive"))

    @property
    def selected_source(self) -> Source:
        """Returns the chosen translation source."""
        if self.__radio_nexus.isChecked():
            return Source.NexusMods
        return Source.Confrerie

    @property
    def mod_id_text(self) -> str:
        """Returns the user entered mod id or URL."""
        return self.__id_input.text().strip()

    @property
    def local_archive(self) -> Optional[Path]:
        """Returns the selected local archive if any."""
        return self.__selected_file

    @property
    def missing_only(self) -> bool:
        """Returns whether to apply to missing strings only."""
        return self.__missing_only_checkbox.isChecked()

    @property
    def local_vo_archive(self) -> Optional[Path]:
        """Returns the selected original English VO archive if any."""
        return self.__selected_vo_file

    @property
    def bridge_mode(self) -> bool:
        """Returns whether bridge mode is enabled."""
        return self.__bridge_mode_checkbox.isChecked()
