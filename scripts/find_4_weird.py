import json

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    trans = s.get('string') or ''
    orig = s.get('original') or ''
    for weird in ['<pagebreak]', '< ?>', '<intraduisible>', '$Bordecielbooks']:
        if weird in trans:
            print(f"[{s.get('type')}] FormID: {s.get('form_id')} | EDID: {s.get('editor_id')}")
            print(f"Orig: {orig[:150]}")
            print(f"Trans: {trans[:150]}")
            print()
