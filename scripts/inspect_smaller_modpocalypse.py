import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ussep = json.load(open('data/user/database/french/USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json', encoding='utf-8'))
ussep_map = {(x.get('form_id'), x.get('type')): (x.get('original'), x.get('string')) for x in ussep if x.get('form_id') and x.get('type')}

modp_files = glob.glob('data/user/database/french/Modpocalypse NPCs - Patch Collection - French/*.json')

for f in sorted(modp_files):
    fname = os.path.basename(f)
    if fname == "[xPatch] Modpocalypse NPCs (v3) SSE - AI Overhaul.esp.json":
        continue # we'll inspect separately
    d = json.load(open(f, encoding='utf-8'))
    print(f"\n=== {fname} ({len(d)} entries) ===")
    for x in d:
        fid = x.get('form_id')
        typ = x.get('type')
        orig = x.get('original')
        curr = x.get('string')
        u_info = ""
        if (fid, typ) in ussep_map:
            u_orig, u_str = ussep_map[(fid, typ)]
            if curr != u_str:
                u_info = f" [DIFF WITH USSEP: {repr(u_str)}]"
        print(f"  {fid} | {typ} | {repr(orig)} -> {repr(curr)}{u_info}")
