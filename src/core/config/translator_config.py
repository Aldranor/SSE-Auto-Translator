"""
Copyright (c) Cutleast
"""

from typing import Annotated, Optional, override

from cutleast_core_lib.core.config.base_config import BaseConfig

from core.translator.apis import TranslatorApi


class TranslatorConfig(BaseConfig):
    """
    Class for translator settings.
    """

    translator: TranslatorApi = TranslatorApi.Google
    """The translator API to use for machine translations."""

    api_key: Annotated[Optional[str], BaseConfig.PropertyMarker.ExcludeFromLogging] = (
        None
    )
    """The API key for the translator API."""

    gemini_api_key: Annotated[
        Optional[str], BaseConfig.PropertyMarker.ExcludeFromLogging
    ] = None
    """The API key for the Gemini API."""

    gemini_model: str = "gemini-3.5-flash"
    """The Gemini model used for translation and editor chat."""

    gemini_custom_instructions: str = ""
    """Optional user instructions prepended to Gemini translation prompts."""

    show_confirmation_dialogs: bool = True
    """Whether to ask for confirmation before starting a machine translation."""

    @override
    @staticmethod
    def get_config_name() -> str:
        return "translator/config.json"
