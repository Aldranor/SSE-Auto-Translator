"""
Copyright (c) Cutleast
"""

from __future__ import annotations

from typing import Any, Optional, override

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from core.translator.gemini import GeminiTranslator
from core.utilities.game_language import GameLanguage


class GeminiChatWorker(QThread):
    """Runs a Gemini chat request away from the UI thread."""

    response_ready = Signal(str)
    request_failed = Signal(str)
    retry_status = Signal(str)

    def __init__(
        self,
        translator: GeminiTranslator,
        original: str,
        current_translation: str,
        context: str,
        language: GameLanguage,
        history: list[dict[str, Any]],
    ) -> None:
        """Initializes the worker with a copy of the conversation context."""

        super().__init__()
        self.__translator = translator
        self.__original = original
        self.__current_translation = current_translation
        self.__context = context
        self.__language = language
        self.__history = history

    def run(self) -> None:
        """Runs one Gemini chat turn and emits its response or error."""

        try:
            response = self.__translator.chat(
                original=self.__original,
                current_translation=self.__current_translation,
                string_context=self.__context,
                dst=self.__language,
                history=self.__history,
                on_retry=self.retry_status.emit,
            )
        except Exception as ex:  # noqa: BLE001
            self.request_failed.emit(str(ex))
        else:
            self.response_ready.emit(response)


class GeminiChatDialog(QDialog):
    """Contextual Gemini chat for discussing one translation string."""

    translation_proposed = Signal(str)

    __translator: GeminiTranslator
    __original: str
    __current_translation: str
    __context: str
    __language: GameLanguage
    __history: list[dict[str, Any]]
    __worker: Optional[GeminiChatWorker]
    __latest_response: Optional[str]
    __close_button: QPushButton

    def __init__(
        self,
        parent: QWidget,
        translator: GeminiTranslator,
        original: str,
        current_translation: str,
        context: str,
        language: GameLanguage,
    ) -> None:
        """Creates a chat scoped to the string currently open in the editor."""

        super().__init__(parent)
        self.__translator = translator
        self.__original = original
        self.__current_translation = current_translation
        self.__context = context
        self.__language = language
        self.__history = []
        self.__worker = None
        self.__latest_response = None

        self.setWindowTitle(self.tr("Gemini translation chat"))
        self.resize(760, 620)

        layout = QVBoxLayout(self)
        self.__transcript = QTextBrowser()
        self.__transcript.setOpenExternalLinks(False)
        layout.addWidget(self.__transcript, stretch=1)

        self.__status = QLabel(
            self.tr(
                "Discuss this string with Gemini. Your custom instructions are included."
            )
        )
        self.__status.setWordWrap(True)
        layout.addWidget(self.__status)

        self.__prompt = QPlainTextEdit()
        self.__prompt.setPlaceholderText(self.tr("Ask about the translation…"))
        self.__prompt.setMaximumHeight(100)
        layout.addWidget(self.__prompt)

        buttons = QHBoxLayout()
        layout.addLayout(buttons)
        self.__send_button = QPushButton(self.tr("Send"))
        self.__send_button.clicked.connect(self.__send)
        buttons.addWidget(self.__send_button)
        buttons.addStretch()
        self.__use_button = QPushButton(self.tr("Use latest response"))
        self.__use_button.setEnabled(False)
        self.__use_button.clicked.connect(self.__use_latest_response)
        buttons.addWidget(self.__use_button)
        self.__close_button = QPushButton(self.tr("Close"))
        self.__close_button.clicked.connect(self.accept)
        buttons.addWidget(self.__close_button)

        self.__append_message(
            self.tr("Source"), f"{self.__context}\n\n{self.__original}"
        )

    def __send(self) -> None:
        if self.__worker is not None and self.__worker.isRunning():
            return
        prompt = self.__prompt.toPlainText().strip()
        if not prompt:
            return

        self.__prompt.clear()
        self.__history.append({"role": "user", "parts": [{"text": prompt}]})
        self.__append_message(self.tr("You"), prompt)
        self.__send_button.setEnabled(False)
        self.__close_button.setEnabled(False)
        self.__use_button.setEnabled(False)
        self.__status.setText(self.tr("Gemini is thinking…"))

        worker = GeminiChatWorker(
            translator=self.__translator,
            original=self.__original,
            current_translation=self.__current_translation,
            context=self.__context,
            language=self.__language,
            history=list(self.__history),
        )
        self.__worker = worker
        worker.response_ready.connect(self.__on_response)
        worker.request_failed.connect(self.__on_error)
        worker.retry_status.connect(self.__status.setText)
        worker.finished.connect(self.__on_finished)
        worker.start()

    def __on_response(self, response: str) -> None:
        self.__history.append({"role": "model", "parts": [{"text": response}]})
        self.__latest_response = response
        self.__append_message("Gemini", response)
        self.__status.setText(self.tr("Response received. Review it before applying."))

    def __on_error(self, message: str) -> None:
        if self.__history and self.__history[-1].get("role") == "user":
            self.__history.pop()
        self.__status.setText(self.tr("Gemini request failed."))
        QMessageBox.warning(self, self.tr("Gemini error"), message)

    def __on_finished(self) -> None:
        self.__send_button.setEnabled(True)
        self.__close_button.setEnabled(True)
        self.__use_button.setEnabled(bool(self.__latest_response))
        if self.__worker is not None:
            self.__worker.deleteLater()
            self.__worker = None

    def __append_message(self, speaker: str, message: str) -> None:
        safe_speaker = (
            speaker.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        safe_message = (
            message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        safe_message = safe_message.replace("\n", "<br>")
        self.__transcript.append(f"<b>{safe_speaker}</b><br>{safe_message}<br>")

    def __use_latest_response(self) -> None:
        if self.__latest_response and (
            self.__worker is None or not self.__worker.isRunning()
        ):
            self.translation_proposed.emit(self.__latest_response)
            self.accept()

    @override
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.__worker is not None and self.__worker.isRunning():
            self.__status.setText(
                self.tr("Wait for the current Gemini response before closing this chat.")
            )
            event.ignore()
            return
        event.accept()

    @override
    def reject(self) -> None:
        if self.__worker is not None and self.__worker.isRunning():
            self.__status.setText(
                self.tr("Wait for the current Gemini response before closing this chat.")
            )
            return
        super().reject()
