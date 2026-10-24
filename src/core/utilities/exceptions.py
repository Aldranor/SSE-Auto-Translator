"""
Copyright (c) Cutleast
"""

from typing import override

from cutleast_core_lib.core.utilities.exceptions import LocalizedException
from PySide6.QtWidgets import QApplication


class DownloadFailedError(LocalizedException):
    """
    Exception when download failed.
    """

    @override
    def getLocalizedMessage(self) -> str:
        return QApplication.translate("exceptions", "Download failed!")


class InstallationFailedError(LocalizedException):
    """
    Exception when installation failed.
    """

    @override
    def getLocalizedMessage(self) -> str:
        return QApplication.translate("exceptions", "Installation failed!")


class NoStringsExtractedError(InstallationFailedError):
    """
    Exception when the translation could not be mapped to the original mod.
    """

    def __init__(self, details: str = "") -> None:
        """
        Args:
            details (str, optional): Diagnostic explanation. Defaults to "".
        """
        if not details:
            details = QApplication.translate(
                "exceptions",
                "Translation is either incompatible or there are no original mod files in need of a translation.",
            )
        super().__init__(details)

    @override
    def getLocalizedMessage(self) -> str:
        return QApplication.translate(
            "exceptions",
            "No strings extracted! {0}",
        )


class NoOriginalModFound(InstallationFailedError):
    """
    Exception when no original mod could be found for the translation.
    """

    @override
    def getLocalizedMessage(self) -> str:
        return QApplication.translate(
            "exceptions", "No original mod found for the translation!"
        )
