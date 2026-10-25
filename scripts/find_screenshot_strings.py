import json
from pathlib import Path

db_dir = Path('data/user/database/french')
results = []
keywords = ['Sinnen', 'Trueaz', "Owl's Perch", 'Thieves Guild Fence']

for p in db_dir.rglob('*.json'):
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for s in data.get('strings', []):
            orig = s.get('original', '')
            trans = s.get('translation', '')
            if any(k.lower() in orig.lower() for k in keywords):
                results.append({
                    'file': str(p.relative_to(db_dir)),
                    'orig': orig,
                    'trans': trans,
                    'form_id': s.get('form_id'),
                    'editor_id': s.get('editor_id'),
                    'status': s.get('status')
                })
    except Exception as e:
        pass

print(f'Found {len(results)} matches:')
for r in results:
    print(r)
