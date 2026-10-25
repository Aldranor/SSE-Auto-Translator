import os
import re
from pathlib import Path

nolvus_mods = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods")

missing_mcm = []

for mod_folder in nolvus_mods.iterdir():
    if not mod_folder.is_dir():
        continue
    trans_dir = mod_folder / "Interface" / "Translations"
    if trans_dir.exists():
        en_files = list(trans_dir.glob("*_ENGLISH.txt")) + list(trans_dir.glob("*_english.txt"))
        for ef in en_files:
            base_prefix = re.sub(r'_(?:english|ENGLISH)\.txt$', '', ef.name)
            fr_file1 = trans_dir / f"{base_prefix}_FRENCH.txt"
            fr_file2 = trans_dir / f"{base_prefix}_french.txt"
            if not fr_file1.exists() and not fr_file2.exists():
                # Count strings
                count = 0
                try:
                    for line in ef.read_text(encoding='utf-16').splitlines():
                        if '\t' in line:
                            count += 1
                except Exception:
                    try:
                        for line in ef.read_text(encoding='utf-8', errors='ignore').splitlines():
                            if '\t' in line:
                                count += 1
                    except Exception:
                        pass
                missing_mcm.append({
                    'mod': mod_folder.name,
                    'file': ef.name,
                    'path': str(ef),
                    'target_fr': f"{base_prefix}_FRENCH.txt",
                    'strings_count': count
                })

print(f"Total untranslated MCM files found: {len(missing_mcm)}")
total_strings = sum(x['strings_count'] for x in missing_mcm)
print(f"Total strings across all MCM files: {total_strings}\n")

for x in missing_mcm[:20]:
    print(f"- {x['mod']} :: {x['file']} ({x['strings_count']} strings) -> {x['target_fr']}")
