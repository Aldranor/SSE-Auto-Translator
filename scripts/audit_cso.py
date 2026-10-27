import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

cso_dir = 'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French'
ref_map = {}
ussep_path = 'data/user/database/french/USSEP - Traduction Francaise'
for fn in os.listdir(ussep_path):
    if fn.endswith('.json'):
        d = json.load(open(os.path.join(ussep_path, fn), encoding='utf-8'))
        for item in d:
            fid = item.get('form_id')
            typ = item.get('type')
            if fid and typ and item.get('string'):
                ref_map[(fid, typ)] = item.get('string')

for fn in os.listdir(cso_dir):
    if not fn.endswith('.json'):
        continue
    data = json.load(open(os.path.join(cso_dir, fn), encoding='utf-8'))
    diffs = []
    for item in data:
        fid = item.get('form_id')
        typ = item.get('type')
        orig = item.get('original')
        curr = item.get('string')
        if not orig or not curr:
            continue
        ref = ref_map.get((fid, typ))
        if ref and ref != curr:
            # Check if meaningful difference
            if ref.lower().strip() != curr.lower().strip():
                diffs.append((fid, typ, orig, curr, ref))
    print(f"\n--- {fn} ({len(data)} total entries) ---")
    print(f"Meaningful diffs against vanilla official French: {len(diffs)}")
    for fid, typ, orig, curr, ref in diffs[:25]:
        print(f"  {fid} ({typ}): orig=\"{orig}\" | curr=\"{curr}\" --> ref=\"{ref}\"")
