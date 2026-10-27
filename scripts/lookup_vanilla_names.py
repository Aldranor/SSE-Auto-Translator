import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

targets = {
    '00013264|Skyrim.esm': 'Bolgeir Bearclaw',
    '0001326F|Skyrim.esm': 'Endarie',
    '00013272|Skyrim.esm': 'Erikur',
    '00013296|Skyrim.esm': 'Wayfinder',
    '000132AB|Skyrim.esm': 'Taarie',
    '000133B8|Skyrim.esm': 'Skaggi Scar-Face',
    '0001365F|Skyrim.esm': 'Dravynea the Stoneweaver',
    '00014122|Skyrim.esm': 'Suvaris Atheron',
    '00014123|Skyrim.esm': 'Niranye',
    '00019A2E|Skyrim.esm': 'Michel',
    '00019BFE|Skyrim.esm': 'Avrusa Sarethi',
    '00019BFF|Skyrim.esm': 'Aduri Sarethi',
    '0001C196|Skyrim.esm': 'Brelyna Maryon',
    '000350A7|Skyrim.esm': 'Erik the Slayer',
    '000877AF|Skyrim.esm': 'Edith',
    '00065657|Skyrim.esm': 'Erik',
    '000274A0|Skyrim.esm': 'Laelette the Vampire'
}

found = {}
for p in glob.glob('data/user/database/french/*/*.json'):
    # skip the phase 2d files themselves so we see other sources
    fn = os.path.basename(p)
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for x in d:
            fid = x.get('form_id')
            if fid in targets:
                found.setdefault(fid, []).append((fn, x.get('type'), x.get('original'), x.get('string')))
    except:
        pass

for fid, occurrences in found.items():
    print(f"\n{fid} ({targets[fid]}):")
    for fn, typ, orig, curr in occurrences:
        print(f"   [{fn}] {typ} | {repr(orig)} -> {repr(curr)}")
