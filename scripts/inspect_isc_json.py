import json

p = r'data/user/database/french/ISC - Bruitages immersifs/Immersive Sounds - Compendium.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
for i, x in enumerate(data[:30]):
    print(f"{i:2d}: orig={x.get('original')} --> str={x.get('string')} (status={x.get('status')}, form_id={x.get('form_id')})")
