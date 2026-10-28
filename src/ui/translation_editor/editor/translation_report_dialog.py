"""
Copyright (c) Cutleast
"""

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.editor.translation_report import TranslationReport


class TranslationReportDialog(QDialog):
    """
    Dialog displaying a detailed report of the translation import/bridge results.
    """

    def __init__(
        self,
        parent: Optional[QWidget],
        report: TranslationReport,
    ) -> None:
        """
        Initializes the TranslationReportDialog.

        Args:
            parent (Optional[QWidget]): Parent widget.
            report (TranslationReport): Report data to display.
        """
        super().__init__(parent)

        self.setWindowTitle(self.tr("Translation Report"))
        self.setMinimumWidth(620)
        self.setMinimumHeight(480)

        main_layout = QVBoxLayout(self)

        # Header summary
        header_widget = QWidget()
        header_layout = QVBoxLayout(header_widget)
        header_layout.setContentsMargins(4, 4, 4, 8)

        status_color = "#2e7d32" if report.total_modified > 0 else "#c62828"
        status_text = (
            self.tr("Translation Applied Successfully")
            if report.total_modified > 0
            else self.tr("No Strings Translated")
        )

        title_label = QLabel(
            f"<h3 style='margin:0; color:{status_color};'>{status_text}</h3>"
        )
        subtitle_label = QLabel(
            self.tr(
                "Applied translation to <b>{0}</b> string(s). "
                "<b>{1}</b> string(s) remaining untranslated."
            ).format(report.total_modified, report.remaining_missing)
        )
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        main_layout.addWidget(header_widget)

        # 1. Translation Bridge Section
        bridge_group = QGroupBox(self.tr("Translation Bridge"))
        bridge_form = QFormLayout(bridge_group)

        if not report.bridge_enabled:
            status_lbl = QLabel(self.tr("Disabled"))
            status_lbl.setStyleSheet("color: gray;")
            bridge_form.addRow(self.tr("Status:"), status_lbl)
        elif report.bridge_warning:
            status_lbl = QLabel(self.tr("Warning / Not matched"))
            status_lbl.setStyleSheet("color: #e65100; font-weight: bold;")
            bridge_form.addRow(self.tr("Status:"), status_lbl)

            warn_lbl = QLabel(report.bridge_warning)
            warn_lbl.setWordWrap(True)
            warn_lbl.setStyleSheet("color: #bf360c;")
            bridge_form.addRow(self.tr("Details:"), warn_lbl)
        else:
            status_lbl = QLabel(self.tr("Active"))
            status_lbl.setStyleSheet("color: #2e7d32; font-weight: bold;")
            bridge_form.addRow(self.tr("Status:"), status_lbl)

            vo_text = report.vo_archive_name or self.tr("Unknown")
            if report.vo_archive_version:
                vo_text += f" (v{report.vo_archive_version})"
            bridge_form.addRow(self.tr("English VO archive:"), QLabel(vo_text))

            trans_text = report.translation_source_name or self.tr("Downloaded archive")
            if report.translation_version:
                trans_text += f" (v{report.translation_version})"
            bridge_form.addRow(self.tr("Translation source:"), QLabel(trans_text))

            bridge_form.addRow(
                self.tr("Bridge mappings:"),
                QLabel(
                    self.tr(
                        "{0} pair(s) constructed ({1} unique English phrase(s))"
                    ).format(
                        report.bridge_pairs_count,
                        report.bridge_unique_phrases_count,
                    )
                ),
            )

            parts = [
                f"{self.tr('FormID')}: {report.bridge_formid_applied}",
                f"{self.tr('Exact Text')}: {report.bridge_text_applied}",
                f"{self.tr('EDID')}: {report.bridge_edid_applied}",
            ]
            if report.bridge_identical_applied > 0:
                parts.append(f"{self.tr('Identical/To verify')}: {report.bridge_identical_applied}")
            breakdown = f"<b>{report.bridge_total_applied}</b> (" + ", ".join(parts) + ")"
            breakdown_lbl = QLabel(breakdown)
            bridge_form.addRow(self.tr("Strings applied:"), breakdown_lbl)

        main_layout.addWidget(bridge_group)

        # 2. Direct / Standard Matching Section
        direct_group = QGroupBox(self.tr("Direct / Standard Extraction"))
        direct_form = QFormLayout(direct_group)

        direct_form.addRow(
            self.tr("Extracted files:"),
            QLabel(
                self.tr("{0} file(s) found in archive").format(
                    report.extracted_files_count
                )
            ),
        )
        direct_form.addRow(
            self.tr("Strings applied:"),
            QLabel(f"<b>{report.standard_applied}</b> {self.tr('string(s)')}"),
        )
        main_layout.addWidget(direct_group)

        # 3. Log Details
        log_group = QGroupBox(self.tr("Execution Details & Logs"))
        log_layout = QVBoxLayout(log_group)

        self.__log_edit = QPlainTextEdit()
        self.__log_edit.setReadOnly(True)
        mono_font = QFont("Consolas", 9)
        mono_font.setStyleHint(QFont.StyleHint.Monospace)
        self.__log_edit.setFont(mono_font)
        self.__log_edit.setPlainText("\n".join(report.log_messages))
        self.__log_edit.setMaximumHeight(140)
        log_layout.addWidget(self.__log_edit)

        copy_btn = QPushButton(self.tr("Copy Log to Clipboard"))
        copy_btn.clicked.connect(self.__on_copy_log)
        log_layout.addWidget(copy_btn, 0, Qt.AlignmentFlag.AlignRight)

        main_layout.addWidget(log_group)

        # Dialog Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        close_btn = QPushButton(self.tr("Close"))
        close_btn.setDefault(True)
        close_btn.clicked.connect(self.accept)
        btn_layout.addWidget(close_btn)

        main_layout.addLayout(btn_layout)

    def __on_copy_log(self) -> None:
        """Copies log output to clipboard."""
        QApplication.clipboard().setText(self.__log_edit.toPlainText())
