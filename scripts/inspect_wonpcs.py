import json

path = r"data/user/database/french/Whiterun Outskirts Market - Miggyluv's NPCs - French/WONpcs.esp.json"
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

items = d if isinstance(d, list) else d.get('strings', [])
for s in items:
    print(f"{s.get('original')}  ===>  {s.get('translation')}")
