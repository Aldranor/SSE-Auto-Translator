"""
Copyright (c) Cutleast
"""

from pydantic import BaseModel


class DatabaseImportResult(BaseModel, frozen=True):
    """
    Summarizes the outcome of importing translations from database folders.
    """

    imported: int
    """The number of new translations that were imported into the database."""

    skipped: int
    """
    The number of folders that were already present or contained no valid translation
    files and were skipped.
    """

    failed: int
    """The number of translation folders that failed to import."""
