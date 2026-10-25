import os
import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

# 1. Check for Mojibake (UTF-8 decoded as Windows-1252 or double-encoded UTF-8)
# Common patterns: Ã©, Ã¨, Ã , Ã§, Ã´, Ã¢, Ã¹, Â, â€™, â€œ, etc.
mojibake_pattern = re.compile(r'(?:Ã[©¨§àôâù«»]|â€™|â€“|â€œ|â€\x9d|Â)')

# 2. Check for broken Alias tags (e.g., <Alias=Joueur> instead of <Alias=Player>)
broken_alias_pattern = re.compile(r'<Alias=(?:Joueur|Personnage|Héros)', re.IGNORECASE)

# 3. Check for unclosed HTML tags in books (like <font ... without </font> or unclosed <p>)
unclosed_tags_pattern = re.compile(r'<font[^>]*>(?!.*</font>)', re.IGNORECASE | re.DOTALL)

mojibake_findings = []
broken_aliases = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            trans = s.get('string') or s.get('translation') or ''
            orig = s.get('original') or ''
            
            if mojibake_pattern.search(trans):
                mojibake_findings.append({
                    'file': p.name,
                    'orig': orig[:50],
                    'trans': trans[:50]
                })
                
            if broken_alias_pattern.search(trans):
                broken_aliases.append({
                    'file': p.name,
                    'orig': orig,
                    'trans': trans
                })
    except Exception:
        pass

print(f"Mojibake findings: {len(mojibake_findings)}")
print(f"Broken Alias findings: {len(broken_aliases)}")

# 4. Check Nolvus Interface/Translations folder for missing French txt files
nolvus_mods = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods")
missing_mcm_french = []

if nolvus_mods.exists():
    for mod_folder in nolvus_mods.iterdir():
        if not mod_folder.is_dir():
            continue
        trans_dir = mod_folder / "Interface" / "Translations"
        if trans_dir.exists():
            english_files = list(trans_dir.glob("*ENGLISH.txt")) + list(trans_dir.glob("*english.txt"))
            for ef in english_files:
                base_name = re.sub(r'english\.txt$', '', ef.name, flags=re.IGNORECASE)
                french_file = trans_dir / f"{base_name}FRENCH.txt"
                french_file_lower = trans_dir / f"{base_name}french.txt"
                if not french_file.exists() and not french_file_lower.exists():
                    missing_mcm_french.append({
                        'mod': mod_folder.name,
                        'english_file': ef.name
                    })

print(f"Missing MCM French translation files in Nolvus: {len(missing_mcm_french)}")
if missing_mcm_french:
    print("\nSample missing MCM French files:")
    for m in missing_mcm_french[:15]:
        print(f"  Mod: {m['mod']} -> {m['english_file']}")

if broken_aliases:
    print("\nBroken Aliases found:")
    for b in broken_aliases[:5]:
        print(f"  {b['file']}: {b['trans']}")
