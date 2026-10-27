import json
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read listing to get all filenames of Category 10
with open('listing_traductions_locales_non_verifiees.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Category 10 starts at "## 📁 Autres Patchs de Compatibilité & Corrections"
cat10_part = text.split("## 📁 Autres Patchs de Compatibilité & Corrections")[1]
# Split by lines and extract all `.esp.json`, `.esm.json`, `.esl.json`
import re
cat10_json_names = set(re.findall(r'`([^`]+\.es[pml]\.json)`', cat10_part))

print(f"Total Category 10 json filenames found in listing: {len(cat10_json_names)}")

# Search for these files on disk
base = 'data/user/database/french'
found_files = {}

for root, dirs, files in os.walk(base):
    for f in files:
        f_lower = f.lower()
        for target in cat10_json_names:
            if f_lower == target.lower():
                found_files[target] = os.path.join(root, f)

print(f"Found on disk: {len(found_files)} / {len(cat10_json_names)}")

missing = cat10_json_names - set(found_files.keys())
if missing:
    print(f"Files not found on disk ({len(missing)}): {missing}")

# Now scan every found file
total_records = 0
status_dist = {}
anomalies = []
multi_fids_files = {}

for target_name, fpath in found_files.items():
    with open(fpath, 'r', encoding='utf-8') as jf:
        data = json.load(jf)
    total_records += len(data)
    
    fid_counts = {}
    for item in data:
        st = item.get('status')
        status_dist[st] = status_dist.get(st, 0) + 1
        
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = item.get('original', '')
        curr = item.get('string', '')
        
        fid_counts[fid] = fid_counts.get(fid, 0) + 1
        
        # Check empty or None
        if curr is None or not str(curr).strip():
            anomalies.append((target_name, fid, typ, idx, orig, curr, "EMPTY_OR_NONE"))
            continue
        elif st == 'TranslationRequired':
            anomalies.append((target_name, fid, typ, idx, orig, curr, "STATUS_REQUIRED"))
            
        curr_str = str(curr)
        orig_str = str(orig)
        # Check illegal brackets like <10> or <5> not part of valid variables
        # Valid variables: <mag>, <dur>, <Global=...>, etc.
        illegal_tags = re.findall(r'<(\d+)>', curr_str)
        if illegal_tags:
            # Check if original also has them
            orig_tags = re.findall(r'<(\d+)>', orig_str)
            if not orig_tags:
                anomalies.append((target_name, fid, typ, idx, orig, curr, f"ILLEGAL_NUMERIC_TAG: {illegal_tags}"))
        
        # Check mojibake
        if any(c in curr_str for c in ['Ã©', 'Ã¨', 'Ã ', 'Ã¢', 'Ã¹', 'Ã®', 'Ã«', 'Ã¯']):
            anomalies.append((target_name, fid, typ, idx, orig, curr, "MOJIBAKE"))

    multis = {k: v for k, v in fid_counts.items() if v > 1}
    if multis:
        multi_fids_files[target_name] = len(multis)

print(f"\nTotal records scanned across Category 10: {total_records}")
print(f"Status distribution: {status_dist}")
print(f"Files with multi-entry FormIDs: {len(multi_fids_files)}")
print(f"Total anomalies flagged: {len(anomalies)}")
for an in anomalies[:30]:
    print(f"[{an[0]}] {an[1]} | {an[2]} | {an[3]} -> {an[6]}")
    print(f"   Orig: {repr(an[4])}")
    print(f"   Curr: {repr(an[5])}")
