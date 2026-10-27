import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for mod in ['Complete Crafting Overhaul Remastered - Immersive Sounds Patch - French', 'Creation Club Crossbow Integration - French']:
    mod_dir = os.path.join('data/user/database/french', mod)
    if not os.path.exists(mod_dir):
        continue
    for fn in os.listdir(mod_dir):
        if not fn.endswith('.json'):
            continue
        p = os.path.join(mod_dir, fn)
        data = json.load(open(p, encoding='utf-8'))
        print(f"\n--- {mod} / {fn} ({len(data)} entries) ---")
        for item in data:
            orig = item.get('original') or ''
            curr = item.get('string') or ''
            fid = item.get('form_id') or ''
            typ = item.get('type') or ''
            if orig == curr and len(orig) > 3 and not typ.startswith('NPC_'):
                print(f"  [IDENTICAL] {fid} ({typ}): {orig}")
            orig_tags = re.findall(r'<[^>]+>', orig)
            curr_tags = re.findall(r'<[^>]+>', curr)
            missing = [t for t in orig_tags if t not in curr]
            if missing:
                print(f"  [TAGS] {fid} ({typ}): missing {missing}")
