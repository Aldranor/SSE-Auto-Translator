import json
import os
import sys
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

sys.stdout.reconfigure(encoding='utf-8')

# We collect all NPC_ FULL and NPC_ SHRT entries in Phase 2D
npc_entries = {}
for f in files_2d:
    fname = os.path.basename(f)
    d = json.load(open(f, encoding='utf-8'))
    for item in d:
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = item.get('original')
        curr = item.get('string')
        k = (fid, typ)
        if k not in npc_entries:
            npc_entries[k] = []
        npc_entries[k].append((fname, orig, curr, idx))

print(f"Total unique (form_id, type) pairs in Phase 2D: {len(npc_entries)}")

# Check for conflicts where the same (form_id, type) is translated differently across Phase 2D patches
conflicts = []
for k, occurrences in npc_entries.items():
    strings = set(x[2] for x in occurrences)
    if len(strings) > 1:
        conflicts.append((k, occurrences))

print(f"Conflicts found across Phase 2D patches: {len(conflicts)}")
for k, occs in conflicts:
    print(f"\nConflict on {k[0]} ({k[1]}):")
    for fname, orig, curr, idx in occs:
        print(f"   [{fname}] orig={repr(orig)} -> curr={repr(curr)}")
