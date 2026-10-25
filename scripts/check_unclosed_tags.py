import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

unclosed_tags = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            orig = s.get('original') or ''
            trans = s.get('string') or s.get('translation') or ''
            if not trans:
                continue
                
            # Count opening and closing font tags
            open_font = len(re.findall(r'<font\b', trans, re.IGNORECASE))
            close_font = len(re.findall(r'</font>', trans, re.IGNORECASE))
            
            orig_open_font = len(re.findall(r'<font\b', orig, re.IGNORECASE))
            orig_close_font = len(re.findall(r'</font>', orig, re.IGNORECASE))
            
            # If original had balanced tags but translation has unbalanced tags
            if (orig_open_font == orig_close_font) and (open_font != close_font):
                unclosed_tags.append({
                    'file': p.name,
                    'mod': p.parent.name,
                    'form_id': s.get('form_id'),
                    'diff': open_font - close_font,
                    'trans': trans[:100]
                })
    except Exception:
        pass

print(f"Total unclosed font tags: {len(unclosed_tags)}")
for x in unclosed_tags[:10]:
    print(f"[{x['mod']}] {x['file']} (diff: {x['diff']}): {x['trans']}")
