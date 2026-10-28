"""
Copyright (c) Cutleast
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TranslationReport:
    """
    Data structure capturing the results and details of a translation download/bridge operation.
    """

    total_modified: int = 0
    remaining_missing: int = 0
    translation_source_name: Optional[str] = None
    translation_version: Optional[str] = None

    bridge_enabled: bool = False
    vo_archive_name: Optional[str] = None
    vo_archive_version: Optional[str] = None
    bridge_pairs_count: int = 0
    bridge_unique_phrases_count: int = 0
    bridge_formid_applied: int = 0
    bridge_text_applied: int = 0
    bridge_edid_applied: int = 0
    bridge_identical_applied: int = 0
    bridge_total_applied: int = 0
    bridge_warning: Optional[str] = None

    standard_applied: int = 0
    extracted_files_count: int = 0
    extracted_file_names: list[str] = field(default_factory=list)

    log_messages: list[str] = field(default_factory=list)
