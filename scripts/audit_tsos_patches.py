import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ussep_ref = {}
p_ussep = 'data/user/database/french/USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json'
with open(p_ussep, 'r', encoding='utf-8') as f:
    for x in json.load(f):
        ussep_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

tsos_files = [
    'data/user/database/french/True Sons of Skyrim Refined - Nolvus Patch - French/nolvus awakening tsos patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_AI_Overall_Patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDawnguard.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDragonborn.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedHearthfire.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/tsos_apachii_store_patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_TsunDal_Patch.esp.json'
]

for f in tsos_files:
    fname = os.path.basename(f)
    d = json.load(open(f, encoding='utf-8'))
    print(f"\n=== {fname} ({len(d)} entries) ===")
    for x in d:
        fid = x.get('form_id')
        typ = x.get('type')
        orig = x.get('original')
        curr = x.get('string')
        u_val = ussep_ref.get((fid, typ))
        if u_val and curr != u_val:
            print(f"  DISC: {fid} | {typ} | {repr(orig)} -> curr={repr(curr)} vs USSEP={repr(u_val)}")
