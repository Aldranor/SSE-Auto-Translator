import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ussep_path = 'data/user/database/french/USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json'
with open(ussep_path, 'r', encoding='utf-8') as f:
    ussep_data = json.load(f)

ussep_map = {}
for x in ussep_data:
    fid = x.get('form_id')
    typ = x.get('type')
    orig = x.get('original')
    s = x.get('string')
    if fid and typ:
        ussep_map[(fid, typ)] = (orig, s)

import glob
files_2d = [
    *glob.glob('data/user/database/french/Modpocalypse NPCs - Patch Collection - French/*.json'),
    'data/user/database/french/True Sons of Skyrim Refined - Nolvus Patch - French/nolvus awakening tsos patch.esp.json',
    *glob.glob('data/user/database/french/Fanatical Enemies - Patches - French/*.json'),
    'data/user/database/french/DIbella\'s Blessing - RSV Exclusion Patches - French/DIbella\'s Blessing - RSV Exclusion Patch.esp.json',
    *glob.glob('data/user/database/french/AI Overhaul - Nithi NPC Enhancements Patch Hub - French/*.json'),
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_AI_Overall_Patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDawnguard.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDragonborn.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedHearthfire.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/tsos_apachii_store_patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_TsunDal_Patch.esp.json'
]

discrepancies = []

for fpath in files_2d:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = item.get('original')
        curr = item.get('string')
        
        k = (fid, typ)
        if k in ussep_map:
            u_orig, u_str = ussep_map[k]
            # If original texts match, compare strings
            if orig.strip().lower() == u_orig.strip().lower():
                if curr.strip() != u_str.strip():
                    discrepancies.append({
                        'file': fname,
                        'fpath': fpath,
                        'form_id': fid,
                        'type': typ,
                        'index': idx,
                        'original': orig,
                        'current': curr,
                        'ussep': u_str
                    })

print(f"Total discrepancies with USSEP in Phase 2D: {len(discrepancies)}")
for d in discrepancies:
    print(f"\n[{d['file']}] {d['form_id']} ({d['type']})")
    print(f"   Orig:  {repr(d['original'])}")
    print(f"   Curr:  {repr(d['current'])}")
    print(f"   USSEP: {repr(d['ussep'])}")

with open('phase2d_ussep_discrepancies.json', 'w', encoding='utf-8') as f:
    json.dump(discrepancies, f, ensure_ascii=False, indent=2)
