"""
Copyright (c) Cutleast
"""

from typing import override

from pydantic import BaseModel

from core.translation_provider.mod_details import ModDetails
from core.translation_provider.source import Source


class FileDownload(BaseModel):
    """
    Class for single file downloads.
    """

    mod_details: ModDetails
    """Metadata of the downloaded mod file."""

    source: Source
    """Source the download is from."""

    stale: bool = False
    """
    Whether the download is stale and should be removed as soon as a thread picks it up.
    """

    unverified: bool = False
    """
    Whether this download was included without content preview verification and requires
    manual confirmation/selection in the download list.
    """

    @override
    def __hash__(self) -> int:
        return hash(
            (self.source.name, self.mod_details.mod_id, self.mod_details.file_name)
        )
