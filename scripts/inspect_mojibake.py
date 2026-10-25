import json
import re
from pathlib import Path
from collections import Counter

db_dir = Path('data/user/database/french')
mojibake_pattern = re.compile(r'(?:Ã[©¨§àôâù«»]|â€™|â€“|â€œ|â€\x9d|Â)')

mojibake_files = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        has_mojibake = False
        sample = None
        for s in items:
            trans = s.get('string') or s.get('translation') or ''
            if mojibake_pattern.search(trans):
                has_mojibake = True
                sample = trans[:80]
                break
        if has_mojibake:
            mojibake_files.append((p.parent.name, p.name, sample))
    except Exception:
        pass

print(f"Total files with Mojibake: {len(mojibake_files)}")
for mod, fn, s in mojibake_files[:15]:
    print(f"Mod: {mod} | File: {fn}")
    print(f"  Sample: {s}\n")
