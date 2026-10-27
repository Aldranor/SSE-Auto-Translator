"""
Copyright (c) Cutleast
"""

from typing import override

from cutleast_core_lib.core.config.exceptions import ConfigValidationError
from cutleast_core_lib.ui.settings.settings_page import SettingsPage
from cutleast_core_lib.ui.widgets.enum_radiobutton_widget import EnumRadiobuttonsWidget
from cutleast_core_lib.ui.widgets.key_edit import KeyLineEdit
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QWidget,
)

from core.config.translator_config import TranslatorConfig
from core.translator.apis import TranslatorApi


class TranslatorSettings(SettingsPage[TranslatorConfig]):
    """
    Widget for translator API settings.
    """

    __flayout: QFormLayout

    __api_selector: EnumRadiobuttonsWidget[TranslatorApi]
    __deepl_api_key_entry: KeyLineEdit
    __gemini_api_key_entry: KeyLineEdit
    __gemini_model_entry: QLineEdit
    __gemini_instructions_entry: QPlainTextEdit

    __show_confirmations_box: QCheckBox

    @override
    def _init_ui(self) -> None:
        scroll_widget = QWidget()
        self.setWidget(scroll_widget)

        self.__flayout = QFormLayout()
        self.__flayout.setContentsMargins(4, 0, 4, 0)
        scroll_widget.setLayout(self.__flayout)

        self.__init_api_settings()
        self.__init_confirmation_box()

    def __init_api_settings(self) -> None:
        self.__api_selector = EnumRadiobuttonsWidget(
            TranslatorApi,
            self._initial_config.translator,
            orientation=Qt.Orientation.Horizontal,
        )
        self.__api_selector.currentValueChanged.connect(
            lambda _: self.changed_signal.emit()
        )
        self.__flayout.addRow(self.tr("Translator API"), self.__api_selector)

        deepl_api_key_label = QLabel(self.tr("DeepL API key"))
        self.__deepl_api_key_entry = KeyLineEdit()
        if self._initial_config.api_key:
            self.__deepl_api_key_entry.setText(self._initial_config.api_key)
        self.__deepl_api_key_entry.textChanged.connect(
            lambda _: self.changed_signal.emit()
        )
        self.__flayout.addRow(deepl_api_key_label, self.__deepl_api_key_entry)

        gemini_api_key_label = QLabel(self.tr("Gemini API key"))
        self.__gemini_api_key_entry = KeyLineEdit()
        self.__gemini_api_key_entry.setText(self._initial_config.gemini_api_key or "")
        self.__gemini_api_key_entry.textChanged.connect(
            lambda _: self.changed_signal.emit()
        )
        self.__flayout.addRow(gemini_api_key_label, self.__gemini_api_key_entry)

        self.__gemini_model_entry = QLineEdit(self._initial_config.gemini_model)
        self.__gemini_model_entry.textChanged.connect(
            lambda _: self.changed_signal.emit()
        )
        self.__flayout.addRow(self.tr("Gemini model"), self.__gemini_model_entry)

        self.__gemini_instructions_entry = QPlainTextEdit()
        self.__gemini_instructions_entry.setPlainText(
            self._initial_config.gemini_custom_instructions
        )
        self.__gemini_instructions_entry.setMaximumHeight(100)
        self.__gemini_instructions_entry.textChanged.connect(
            lambda: self.changed_signal.emit()
        )
        self.__flayout.addRow(
            self.tr("Custom translation instructions"),
            self.__gemini_instructions_entry,
        )

        def update_api_fields(translator_api: TranslatorApi) -> None:
            is_deepl = translator_api == TranslatorApi.DeepL
            deepl_api_key_label.setEnabled(is_deepl)
            self.__deepl_api_key_entry.setEnabled(is_deepl)

        self.__api_selector.currentValueChanged.connect(update_api_fields)
        update_api_fields(self._initial_config.translator)

    def __init_confirmation_box(self) -> None:
        self.__show_confirmations_box = QCheckBox(
            self.tr("Ask for confirmation before starting a batch machine translation")
        )
        self.__show_confirmations_box.setChecked(
            self._initial_config.show_confirmation_dialogs
        )
        self.__show_confirmations_box.stateChanged.connect(
            lambda _: self.changed_signal.emit()
        )
        self.__flayout.addRow(self.__show_confirmations_box)

    @override
    def validate(self) -> None:
        if (
            self.__api_selector.getCurrentValue() == TranslatorApi.DeepL
            and not self.__deepl_api_key_entry.text().strip()
        ):
            raise ConfigValidationError(
                self.tr("An API key is required for DeepL translator!")
            )
        if (
            self.__api_selector.getCurrentValue() == TranslatorApi.Gemini
            and not self.__gemini_api_key_entry.text().strip()
        ):
            raise ConfigValidationError(
                self.tr("A Gemini API key is required for Gemini translator!")
            )

    @override
    def apply(self, config: TranslatorConfig) -> None:
        config.translator = self.__api_selector.getCurrentValue()
        config.api_key = self.__deepl_api_key_entry.text().strip() or None
        config.gemini_api_key = self.__gemini_api_key_entry.text().strip() or None
        config.gemini_model = (
            self.__gemini_model_entry.text().strip() or "gemini-3.8-flash"
        )
        config.gemini_custom_instructions = (
            self.__gemini_instructions_entry.toPlainText().strip()
        )
        config.show_confirmation_dialogs = self.__show_confirmations_box.isChecked()
