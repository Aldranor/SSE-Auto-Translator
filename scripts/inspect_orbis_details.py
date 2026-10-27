import json
import os
import sys

sys.path.append('.')
sys.stdout.reconfigure(encoding='utf-8')

orbis_dir = 'data/user/database/french/Lux Orbis - Patch Hub - French'
ref_map = {}
ussep_path = 'data/user/database/french/USSEP - Traduction Francaise'
for fn in os.listdir(ussep_path):
    if fn.endswith('.json'):
        d = json.load(open(os.path.join(ussep_path, fn), encoding='utf-8'))
        for item in d:
            fid = item.get('form_id')
            typ = item.get('type')
            s = item.get('string')
            if fid and typ and s and s.strip():
                ref_map[(fid, typ)] = s

diffs = []
if os.path.exists(orbis_dir):
    for fn in os.listdir(orbis_dir):
        if not fn.endswith('.json'):
            continue
        data = json.load(open(os.path.join(orbis_dir, fn), encoding='utf-8'))
        for item in data:
            fid = item.get('form_id')
            typ = item.get('type')
            orig = item.get('original')
            curr = item.get('string')
            ref = ref_map.get((fid, typ))
            if ref and ref.strip().lower() != curr.strip().lower():
                diffs.append((fn, fid, typ, orig, curr, ref))

print(f"Total meaningful diffs in Lux Orbis against USSEP: {len(diffs)}")
for fn, fid, typ, orig, curr, ref in diffs:
    print(f"[{fn}] {fid} ({typ}): orig='{orig}' | curr='{curr}' | ref='{ref}'")
