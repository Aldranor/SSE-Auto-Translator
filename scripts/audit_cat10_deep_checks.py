import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('listing_traductions_locales_non_verifiees.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cat10_part = text.split("## 📁 Autres Patchs de Compatibilité & Corrections")[1]
cat10_json_names = set(re.findall(r'`([^`]+\.es[pml]\.json)`', cat10_part))

base = 'data/user/database/french'
found_files = {}

for root, dirs, files in os.walk(base):
    for f in files:
        f_lower = f.lower()
        for target in cat10_json_names:
            if f_lower == target.lower():
                found_files[target] = os.path.join(root, f)

print(f"Auditing specific Category 10 key files...")

# 1. Check JK's College of Winterhold
p_jkw = found_files.get("jk's college of winterhold.esp.json")
if p_jkw:
    d = json.load(open(p_jkw, encoding='utf-8'))
    print(f"\n--- {os.path.basename(p_jkw)} ({len(d)} entries) ---")
    for x in d:
        orig = x.get('original')
        curr = x.get('string')
        fid = x.get('form_id')
        typ = x.get('type')
        if 'Midden' in orig or 'Arcanaeum' in orig or 'Hall' in orig:
            print(f"  {fid} | {typ} | {repr(orig)} -> {repr(curr)}")

# 2. Check YOT patches
yot_files = [f for f in found_files.keys() if f.startswith('yot -')]
print(f"\n--- YOT files ({len(yot_files)}) ---")
for yf in yot_files:
    d = json.load(open(found_files[yf], encoding='utf-8'))
    print(f"  {yf}: {len(d)} entries")
    # Sample 2 entries
    for x in d[:2]:
        print(f"     {repr(x.get('original')[:50])} -> {repr(x.get('string')[:50])}")

# 3. Check HOHQE - Wintersun patch
p_hoh = found_files.get("hohqe - wintersun patch.esp.json")
if p_hoh:
    d = json.load(open(p_hoh, encoding='utf-8'))
    print(f"\n--- {os.path.basename(p_hoh)} ({len(d)} entries) ---")
    for x in d[:5]:
        print(f"  {x.get('type')} | {repr(x.get('original')[:50])} -> {repr(x.get('string')[:50])}")
