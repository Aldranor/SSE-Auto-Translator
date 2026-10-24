"""
Copyright (c) Cutleast
"""

from pydantic import BaseModel

from .translation_download import TranslationDownload


class CachedModDownloads(BaseModel):
    """
    Cache model for available translation downloads of a mod.
    """

    timestamp: float
    files: dict[str, list[TranslationDownload]]
