import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

mod_dir = 'data/user/database/french/Eating Animations and Sounds - Patch Collection - French'
for fn in os.listdir(mod_dir):
    if not fn.endswith('.json'):
        continue
    p = os.path.join(mod_dir, fn)
    data = json.load(open(p, encoding='utf-8'))
    print(f"\n--- {fn} ({len(data)} entries) ---")
    for item in data:
        orig = item.get('original') or ''
        curr = item.get('string') or ''
        fid = item.get('form_id') or ''
        typ = item.get('type') or ''
        # Look for English, typos, or inconsistencies
        if 'Faillaise' in curr and 'Falkreath' in orig:
            print(f"  [MISMATCH FALKREATH] {fid}: orig='{orig}' | curr='{curr}'")
        if 'Beure' in curr:
            print(f"  [TYPO] {fid}: {curr}")
        if 'Faisant' in curr:
            print(f"  [TYPO] {fid}: {curr}")
        if 'Cake' in curr:
            print(f"  [ANGLICISM] {fid}: {curr}")
