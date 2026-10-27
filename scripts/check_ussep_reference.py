import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Find USSEP file
ussep_path = None
for root, dirs, files in os.walk('data/user/database/french'):
    for f in files:
        if 'unofficial skyrim special edition patch' in f.lower() and f.endswith('.json'):
            ussep_path = os.path.join(root, f)
            break

print(f"USSEP path: {ussep_path}")
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

print(f"Loaded {len(ussep_map)} USSEP reference records.")

# Check the 19 conflicts against USSEP
targets = [
    '00013264|Skyrim.esm', # Bolgeir
    '0001326F|Skyrim.esm', # Endarie
    '00013272|Skyrim.esm', # Erikur
    '00013296|Skyrim.esm', # Wayfinder
    '000132AB|Skyrim.esm', # Taarie
    '000133B8|Skyrim.esm', # Skaggi Scar-Face
    '0001365F|Skyrim.esm', # Dravynea the Stoneweaver
    '00014122|Skyrim.esm', # Suvaris Atheron
    '00014123|Skyrim.esm', # Niranye
    '00019A2E|Skyrim.esm', # Michel
    '00019BFE|Skyrim.esm', # Avrusa Sarethi
    '00019BFF|Skyrim.esm', # Aduri Sarethi
    '0001C196|Skyrim.esm', # Brelyna Maryon
    '000350A7|Skyrim.esm', # Erik
    '000877AF|Skyrim.esm', # Edith
    '00065657|Skyrim.esm', # Erik the Slayer
    '0008BB91|Skyrim.esm', # Movarth
    '000274A0|Skyrim.esm', # Laelette
]

print("\n--- USSEP REFERENCE VALUES ---")
for fid in targets:
    for typ in ['NPC_ FULL', 'NPC_ SHRT']:
        if (fid, typ) in ussep_map:
            orig, s = ussep_map[(fid, typ)]
            print(f"{fid} | {typ} | {repr(orig)} -> {repr(s)}")
