"""
Copyright (c) Cutleast
"""

from pathlib import Path
from typing import Optional

from PySide6.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QDialog,
    QFileDialog,
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
from core.translation_provider.source import Source


class DownloadTranslationDialog(QDialog):
    """Options for downloading and applying a translation to the open editor."""

    __mod_id_input: QLineEdit
    __translation_path: Optional[Path]
    __original_path: Optional[Path]
    __translation_label: QLabel
    __original_label: QLabel
    __nexus_radio: QRadioButton
    __missing_only: QCheckBox
    __bridge: QCheckBox

    def __init__(
        self,
        translation: Translation,
        default_source: Source,
        mod_id: str,
        show_source_selector: bool = True,
        parent: Optional[QWidget] = None,
    ) -> None:
        """Initialize the dialog with source and mod information when available.

        Args:
            translation (Translation): Translation currently open in the editor.
            default_source (Source): Initially selected download provider.
            mod_id (str): Mod ID used to prefill the editable field.
            show_source_selector (bool): Whether to display the provider selector.
            parent (Optional[QWidget]): Parent widget.
        """

        super().__init__(parent)
        self.setWindowTitle(self.tr("Download translation"))
        self.setMinimumWidth(560)
        self.__translation_path = None
        self.__original_path = None

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self.tr("Translation: {0}").format(translation.name)))

        source_group = QButtonGroup(self)
        confrerie_radio = QRadioButton(self.tr("Confrérie des Traducteurs"))
        self.__nexus_radio = QRadioButton(self.tr("Nexus Mods"))
        source_group.addButton(confrerie_radio)
        source_group.addButton(self.__nexus_radio)
        selected_radio = (
            self.__nexus_radio
            if default_source == Source.NexusMods
            else confrerie_radio
        )
        selected_radio.setChecked(True)
        if show_source_selector:
            source_layout = QHBoxLayout()
            source_layout.addWidget(confrerie_radio)
            source_layout.addWidget(self.__nexus_radio)
            source_layout.addStretch()
            layout.addLayout(source_layout)
        else:
            confrerie_radio.hide()
            self.__nexus_radio.hide()

        form = QFormLayout()
        self.__mod_id_input = QLineEdit(mod_id)
        self.__mod_id_input.setPlaceholderText(self.tr("Mod ID or URL"))
        form.addRow(self.tr("Mod ID / URL:"), self.__mod_id_input)

        self.__translation_label = QLabel(self.tr("None selected"))
        trans_button = QPushButton(self.tr("File…"))
        trans_button.clicked.connect(self.__choose_translation)
        trans_dir_button = QPushButton(self.tr("Folder…"))
        trans_dir_button.clicked.connect(self.__choose_translation_folder)
        trans_row = QHBoxLayout()
        trans_row.addWidget(self.__translation_label, 1)
        trans_row.addWidget(trans_button)
        trans_row.addWidget(trans_dir_button)
        form.addRow(self.tr("Translation source:"), trans_row)

        self.__original_label = QLabel(self.tr("None selected"))
        original_button = QPushButton(self.tr("File…"))
        original_button.clicked.connect(self.__choose_original)
        original_dir_button = QPushButton(self.tr("Folder…"))
        original_dir_button.clicked.connect(self.__choose_original_folder)
        original_row = QHBoxLayout()
        original_row.addWidget(self.__original_label, 1)
        original_row.addWidget(original_button)
        original_row.addWidget(original_dir_button)
        form.addRow(self.tr("Original source (bridge):"), original_row)

        self.__missing_only = QCheckBox(self.tr("Apply on missing strings only"))
        self.__missing_only.setChecked(True)
        form.addRow("", self.__missing_only)
        self.__bridge = QCheckBox(self.tr("Bridge translations across versions"))
        self.__bridge.setChecked(True)
        form.addRow("", self.__bridge)
        layout.addLayout(form)

        buttons = QHBoxLayout()
        buttons.addStretch()
        download_button = QPushButton(self.tr("Download"))
        download_button.setDefault(True)
        download_button.clicked.connect(self.accept)
        buttons.addWidget(download_button)
        cancel_button = QPushButton(self.tr("Cancel"))
        cancel_button.clicked.connect(self.reject)
        buttons.addWidget(cancel_button)
        layout.addLayout(buttons)

    def __choose_translation(self) -> None:
        """Select a local translated archive, plugin, or DSD JSON file."""

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Select translation file"),
            "",
            self.tr(
                "Archives, plugins, DSD (*.7z *.zip *.rar *.esp *.esm *.esl *.json);;"
                "All files (*.*)"
            ),
        )
        if file_name:
            self.__translation_path = Path(file_name)
            self.__translation_label.setText(self.__translation_path.name)

    def __choose_translation_folder(self) -> None:
        """Select a local folder containing translated plugins or DSD files."""

        folder = QFileDialog.getExistingDirectory(
            self, self.tr("Select translation folder")
        )
        if folder:
            self.__translation_path = Path(folder)
            self.__translation_label.setText(self.__translation_path.name)

    def __choose_original(self) -> None:
        """Select a local original archive or plugin."""

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Select original file"),
            "",
            self.tr(
                "Archives and plugins (*.7z *.zip *.rar *.esp *.esm *.esl);;"
                "All files (*.*)"
            ),
        )
        if file_name:
            self.__original_path = Path(file_name)
            self.__original_label.setText(self.__original_path.name)

    def __choose_original_folder(self) -> None:
        """Select a local folder containing original plugins."""

        folder = QFileDialog.getExistingDirectory(
            self, self.tr("Select original folder")
        )
        if folder:
            self.__original_path = Path(folder)
            self.__original_label.setText(self.__original_path.name)

    @property
    def source(self) -> Source:
        """Return the selected download source."""

        return Source.NexusMods if self.__nexus_radio.isChecked() else Source.Confrerie

    @property
    def mod_id(self) -> str:
        """Return the entered mod identifier or URL."""

        return self.__mod_id_input.text().strip()

    @property
    def translation_archive(self) -> Optional[Path]:
        """Return the selected local translation archive, if any."""

        return self.__translation_path

    @property
    def original_archive(self) -> Optional[Path]:
        """Return the selected local original archive, if any."""

        return self.__original_path

    @property
    def missing_only(self) -> bool:
        """Whether existing translations should be preserved."""

        return self.__missing_only.isChecked()

    @property
    def bridge(self) -> bool:
        """Whether cross-version bridge matching is enabled."""

        return self.__bridge.isChecked()
