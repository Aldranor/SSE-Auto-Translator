import json
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Target files for 2D
target_dirs = [
    'data/user/database/french/Modpocalypse NPCs - Patch Collection - French',
    'data/user/database/french/True Sons of Skyrim Refined - Nolvus Patch - French',
    'data/user/database/french/Fanatical Enemies - Patches - French',
    'data/user/database/french/DIbella\'s Blessing - RSV Exclusion Patches - French',
    'data/user/database/french/AI Overhaul - Nithi NPC Enhancements Patch Hub - French',
    # Also check TSOS AI Overhaul patch
    'data/user/database/french/True Sons of Skyrim Refined - French'
]

files = []
for d in target_dirs:
    if os.path.isdir(d):
        for f in glob.glob(os.path.join(d, '*.json')):
            # In True Sons of Skyrim Refined - French, only take the patch if desired, or all patches
            if 'True Sons of Skyrim Refined - French' in d and 'tsosrefined.esp.json' in f:
                continue # tsosrefined is the base mod, not a patch
            files.append(f)

print(f"Total target files in Phase 2D: {len(files)}")

total_records = 0
status_counts = {}
duplicate_fids_by_file = {}
english_anomalies = []
mismatches = []

# Known vanilla French NPC terms to look out for
# e.g., Guard -> Garde, Bandit, Farmer -> Fermier, Miner -> Mineur, Soldier -> Soldat, Citizen -> Citoyen, etc.
job_keywords = {
    'guard': 'garde',
    'miner': 'mineur',
    'farmer': 'fermier',
    'soldier': 'soldat',
    'citizen': 'citoyen',
    'beggar': 'mendiant',
    'blacksmith': 'forgeron',
    'apprentice': 'apprenti',
    'assassin': 'assassin',
    'hunter': 'chasseur',
    'fisherman': 'pêcheur',
    'woodcutter': 'bûcheron',
    'jailer': 'geôlier',
    'cook': 'cuisinier',
    'stable master': 'maître des écuries',
    'stableman': 'palefrenier',
    'innkeeper': 'aubergiste',
    'servant': 'domestique'
}

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as jf:
        data = json.load(jf)
    
    total_records += len(data)
    fid_counts = {}
    
    for item in data:
        st = item.get('status')
        status_counts[st] = status_counts.get(st, 0) + 1
        fid = item.get('form_id')
        fid_counts[fid] = fid_counts.get(fid, 0) + 1
        
        orig = item.get('original', '')
        curr = item.get('string', '')
        typ = item.get('type')
        idx = item.get('index')
        
        if not curr or curr.strip() == '':
            english_anomalies.append({
                'file': fname, 'form_id': fid, 'type': typ, 'index': idx,
                'issue': 'EMPTY_STRING', 'orig': orig, 'curr': curr
            })
        elif st == 'TranslationRequired':
            english_anomalies.append({
                'file': fname, 'form_id': fid, 'type': typ, 'index': idx,
                'issue': 'STATUS_REQUIRED', 'orig': orig, 'curr': curr
            })
        
        # Check if original had an occupation that wasn't translated
        orig_lower = orig.lower()
        curr_lower = curr.lower()
        
        # If original is identical to current, check if it looks like English occupation
        if orig == curr and len(orig) > 3:
            for en_word, fr_word in job_keywords.items():
                if en_word in orig_lower.split():
                    english_anomalies.append({
                        'file': fname, 'form_id': fid, 'type': typ, 'index': idx,
                        'issue': f'JOB_UNTANSLATED ({en_word} -> {fr_word})',
                        'orig': orig, 'curr': curr
                    })
                    break

    multis = {k: v for k, v in fid_counts.items() if v > 1}
    if multis:
        duplicate_fids_by_file[fname] = multis

print(f"\nTotal records analyzed: {total_records}")
print(f"Status distribution: {status_counts}")
print(f"Files with multi-entry FormIDs: {len(duplicate_fids_by_file)}")
for fn, m in duplicate_fids_by_file.items():
    print(f"   {fn}: {len(m)} multi-entry FormIDs (e.g. {list(m.items())[:3]})")

print(f"\nPotential anomalies detected: {len(english_anomalies)}")
for an in english_anomalies[:25]:
    print(f"[{an['file']}] {an['form_id']} ({an['type']}) : {an['issue']}")
    print(f"    orig: {an['orig']}")
    print(f"    curr: {an['curr']}")
