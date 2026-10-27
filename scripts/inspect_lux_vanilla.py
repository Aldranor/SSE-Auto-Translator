import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Check Lux - Patch Hub for Skyrim.esm, Dawnguard.esm, Dragonborn.esm cells
lux_dir = 'data/user/database/french/Lux - Patch Hub - French'
vanilla_issues = []

for fn in os.listdir(lux_dir):
    if not fn.endswith('.json'):
        continue
    data = json.load(open(os.path.join(lux_dir, fn), encoding='utf-8'))
    for item in data:
        fid = item.get('form_id', '')
        typ = item.get('type', '')
        orig = item.get('original', '')
        curr = item.get('string', '')
        if any(esm in fid for esm in ['Skyrim.esm', 'Dawnguard.esm', 'Dragonborn.esm', 'HearthFires.esm']):
            # check identical or strange
            if orig == curr and len(orig) > 3:
                vanilla_issues.append((fn, fid, typ, orig, curr, "Identical in vanilla"))

print(f"Vanilla cells with identical strings in Lux: {len(vanilla_issues)}")
for v in vanilla_issues[:30]:
    print(v)
