import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

jk_dirs = [
    "data/user/database/french/JK's Interiors Patch Collection - French",
    "data/user/database/french/JKs Guild HQ Interiors Patch Collection - French",
    "data/user/database/french/JKs Guild HQ Interiors Patch Collection"
]

for d in jk_dirs:
    if not os.path.exists(d):
        continue
    print(f"\n=== {os.path.basename(d)} ===")
    for fn in os.listdir(d):
        if not fn.endswith('.json'):
            continue
        p = os.path.join(d, fn)
        data = json.load(open(p, encoding='utf-8'))
        for item in data:
            orig = item.get('original') or ''
            curr = item.get('string') or ''
            fid = item.get('form_id') or ''
            typ = item.get('type') or ''
            if orig == curr and len(orig) > 3 and not typ.startswith('NPC_'):
                print(f"  [IDENTICAL] [{fn}] {fid} ({typ}): {orig}")
            if any(k in curr.lower() for k in ['endurance', 'mana', 'montagne rouge']):
                print(f"  [LORE] [{fn}] {fid} ({typ}): {curr}")
