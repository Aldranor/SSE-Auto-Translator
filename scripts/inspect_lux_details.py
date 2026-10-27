import json
import os
import sys

sys.path.append('.')
sys.stdout.reconfigure(encoding='utf-8')

# Run inspect directly
lux_dir = 'data/user/database/french/Lux - Patch Hub - French'
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

# Also load from master mods (Carved Brink, Beyond Reach, etc.)
for m in ['Carved Brink', 'Beyond Reach', 'L\'Héritage de l\'Enfant de dragon']:
    p = os.path.join('data/user/database/french', m)
    if os.path.exists(p):
        for fn in os.listdir(p):
            if fn.endswith('.json'):
                d = json.load(open(os.path.join(p, fn), encoding='utf-8'))
                for item in d:
                    fid = item.get('form_id')
                    typ = item.get('type')
                    s = item.get('string')
                    if fid and typ and s and s.strip():
                        ref_map[(fid, typ)] = s

diffs = []
for fn in os.listdir(lux_dir):
    if not fn.endswith('.json'):
        continue
    data = json.load(open(os.path.join(lux_dir, fn), encoding='utf-8'))
    for item in data:
        fid = item.get('form_id')
        typ = item.get('type')
        orig = item.get('original')
        curr = item.get('string')
        ref = ref_map.get((fid, typ))
        if ref and ref.strip().lower() != curr.strip().lower():
            diffs.append((fn, fid, typ, orig, curr, ref))

print(f"Total meaningful diffs in Lux against master mods/USSEP: {len(diffs)}")
for fn, fid, typ, orig, curr, ref in diffs[:35]:
    print(f"[{fn}] {fid} ({typ})")
    print(f"  orig: {orig}")
    print(f"  curr: {curr}")
    print(f"  ref:  {ref}")
