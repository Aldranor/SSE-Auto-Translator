import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

# Real UTF-8 decoded as CP1252 mojibake patterns:
# Ã© (é), Ã¨ (è), Ã  (à), Ã§ (ç), Ã´ (ô), Ã¢ (â), Ã® (î), Ã¯ (ï), Ã» (û), Ã¹ (ù), Ã« (ë)
# â€™ (’), â€” (—), â€“ (–), â€œ (“), â€\x9d (”), Å“ (œ)
mojibake_strict = re.compile(r'(?:Ã[©¨§ àôâîï»«ûùë]|â€[™—“”]|Å“|Ã\x89|Ã\x88|Ã\x80)')

true_mojibake = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            trans = s.get('string') or s.get('translation') or ''
            if mojibake_strict.search(trans):
                true_mojibake.append({
                    'file': p.name,
                    'mod': p.parent.name,
                    'form_id': s.get('form_id'),
                    'trans': trans[:100]
                })
    except Exception:
        pass

print(f"Total TRUE mojibake occurrences: {len(true_mojibake)}")
for x in true_mojibake[:20]:
    print(f"[{x['mod']}] {x['file']}: {x['trans']}")
