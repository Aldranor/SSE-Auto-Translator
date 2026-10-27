import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ussep_ref = {}
p_ussep = 'data/user/database/french/USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json'
with open(p_ussep, 'r', encoding='utf-8') as f:
    for x in json.load(f):
        ussep_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

modp_ref = {}
p_modp = 'data/user/database/french/Modpocalypse NPCs - All Vanilla NPCs - French/Modpocalypse NPCs (v3) SSE.esp.json'
with open(p_modp, 'r', encoding='utf-8') as f:
    for x in json.load(f):
        modp_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

target_p = 'data/user/database/french/DIbella\'s Blessing - RSV Exclusion Patches - French/DIbella\'s Blessing - RSV Exclusion Patch.esp.json'
with open(target_p, 'r', encoding='utf-8') as f:
    target_data = json.load(f)

print(f"Target: {os.path.basename(target_p)} ({len(target_data)} entries)")

discs = []
for item in target_data:
    k = (item.get('form_id'), item.get('type'))
    curr = item.get('string')
    orig = item.get('original')
    
    ref_val = ussep_ref.get(k) or modp_ref.get(k)
    source = "USSEP" if k in ussep_ref else "Modpocalypse"
    
    if ref_val and curr != ref_val:
        discs.append({
            'form_id': k[0],
            'type': k[1],
            'index': item.get('index'),
            'original': orig,
            'current': curr,
            'reference': ref_val,
            'source': source
        })

print(f"Total discrepancies in Dibella's Blessing RSV patch: {len(discs)}")
for d in discs:
    print(f"\n{d['form_id']} | {d['type']}")
    print(f"   Orig: {repr(d['original'])}")
    print(f"   Curr: {repr(d['current'])}")
    print(f"   Ref:  {repr(d['reference'])} (from {d['source']})")
