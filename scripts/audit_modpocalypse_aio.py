import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load references
aio_ref = {}
p_aio = 'data/user/database/french/AI Overhaul - French/AI Overhaul.esp.json'
if os.path.exists(p_aio):
    with open(p_aio, 'r', encoding='utf-8') as f:
        for x in json.load(f):
            aio_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

modp_ref = {}
p_modp = 'data/user/database/french/Modpocalypse NPCs - All Vanilla NPCs - French/Modpocalypse NPCs (v3) SSE.esp.json'
if os.path.exists(p_modp):
    with open(p_modp, 'r', encoding='utf-8') as f:
        for x in json.load(f):
            modp_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

ussep_ref = {}
p_ussep = 'data/user/database/french/USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json'
if os.path.exists(p_ussep):
    with open(p_ussep, 'r', encoding='utf-8') as f:
        for x in json.load(f):
            ussep_ref[(x.get('form_id'), x.get('type'))] = x.get('string')

target_p = 'data/user/database/french/Modpocalypse NPCs - Patch Collection - French/[xPatch] Modpocalypse NPCs (v3) SSE - AI Overhaul.esp.json'
with open(target_p, 'r', encoding='utf-8') as f:
    target_data = json.load(f)

print(f"Target file: {os.path.basename(target_p)} ({len(target_data)} entries)")

discrepancies = []
for item in target_data:
    k = (item.get('form_id'), item.get('type'))
    curr = item.get('string')
    orig = item.get('original')
    
    # Priority of truth: AIO ref (since this is an AIO patch) > USSEP > Modp ref
    ref_val = None
    ref_source = ""
    if k in aio_ref:
        ref_val = aio_ref[k]
        ref_source = "AI Overhaul"
    elif k in ussep_ref:
        ref_val = ussep_ref[k]
        ref_source = "USSEP"
    elif k in modp_ref:
        ref_val = modp_ref[k]
        ref_source = "Modpocalypse Vanilla"
        
    if ref_val and curr != ref_val:
        discrepancies.append({
            'form_id': k[0],
            'type': k[1],
            'index': item.get('index'),
            'original': orig,
            'current': curr,
            'reference': ref_val,
            'source': ref_source
        })

print(f"Total discrepancies found in Modpocalypse AIO patch: {len(discrepancies)}")
for d in discrepancies:
    print(f"\n{d['form_id']} | {d['type']}")
    print(f"   Orig: {repr(d['original'])}")
    print(f"   Curr: {repr(d['current'])}")
    print(f"   Ref:  {repr(d['reference'])} (from {d['source']})")
