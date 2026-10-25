"""
Copyright (c) Cutleast
"""

import re
from pathlib import Path
from typing import BinaryIO, Optional, override

from core.file_source.file_source_factory import FileSourceFactory
from core.mod_file.mod_file import ModFile
from core.string.string_status import StringStatus
from core.string.types import StringList

from .string import InterfaceString


class InterfaceFile(ModFile):
    """
    Class for interface translation files (data/interface/translations/*_<language>.txt).
    """

    @override
    @classmethod
    def get_glob_patterns(cls, language: str) -> list[str]:
        patterns = [f"interface/translations/*_{language.lower()}.txt"]
        if language and language.lower() != "english":
            patterns.append("interface/translations/*_english.txt")
        return patterns

    @override
    @classmethod
    def can_be_in_bsas(cls) -> bool:
        return True

    @override
    def _extract_strings(self) -> StringList:
        result: StringList = []

        stream: Optional[BinaryIO] = None
        try:
            stream = FileSourceFactory.for_file_path(self.full_path).get_file_stream()
            raw_bytes: bytes = stream.read()

            text: str = ""
            for enc in ("utf-16", "utf-8-sig", "utf-8", "cp1252"):
                try:
                    text = raw_bytes.decode(enc)
                    break
                except UnicodeDecodeError:
                    continue

            for line in text.splitlines():
                if not line.strip():
                    continue

                try:
                    parts = line.split("\t", 1)
                    if len(parts) == 2:
                        string_id, string = parts
                        if string_id and string:
                            result.append(
                                InterfaceString(
                                    mcm_id=string_id.strip(),
                                    original=string.strip(),
                                    status=StringStatus.TranslationRequired,
                                )
                            )
                except ValueError:
                    continue

        finally:
            if stream is not None:
                stream.close()

        return result

    @override
    def dump_strings(
        self,
        strings: StringList,
        output_folder: Path,
        use_dsd_format: bool,
        output_mod: bool = False,
    ) -> None:
        target_lang = "FRENCH"
        try:
            from app import App

            app = App.get()
            if hasattr(app, "_App__user_data") and app._App__user_data:
                target_lang = app._App__user_data.user_config.language.id.upper()
        except Exception:  # noqa: BLE001
            try:
                import json

                cfg_path = Path("data/user/config.json")
                if cfg_path.is_file():
                    cfg_data = json.loads(cfg_path.read_text(encoding="utf-8"))
                    if "language" in cfg_data:
                        target_lang = str(cfg_data["language"]).upper()
            except Exception:  # noqa: BLE001, S110
                pass

        target_path: Path = self.path
        match = re.search(r"^(.*?)_([a-zA-Z]+)\.txt$", self.path.name, re.IGNORECASE)
        if match:
            base_name = match.group(1)
            new_filename = f"{base_name}_{target_lang}.txt"
            target_path = self.path.with_name(new_filename)

        output_file: Path = output_folder / target_path
        output_file.parent.mkdir(parents=True, exist_ok=True)

        lines: list[str] = []
        for string in strings:
            if isinstance(string, InterfaceString):
                val = (
                    string.string
                    if string.string is not None
                    else string.original
                )
                lines.append(f"{string.mcm_id}\t{val}")

        content: str = "\r\n".join(lines) + ("\r\n" if lines else "")
        output_file.write_bytes(content.encode("utf-16"))
