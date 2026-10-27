import json
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# List of all Phase 2D files
files_2d = [
    # 1. Modpocalypse NPCs - Patch Collection
    *glob.glob('data/user/database/french/Modpocalypse NPCs - Patch Collection - French/*.json'),
    # 2. True Sons of Skyrim Refined - Nolvus Patch
    'data/user/database/french/True Sons of Skyrim Refined - Nolvus Patch - French/nolvus awakening tsos patch.esp.json',
    # 3. Fanatical Enemies - Patches
    *glob.glob('data/user/database/french/Fanatical Enemies - Patches - French/*.json'),
    # 4. DIbella's Blessing - RSV Exclusion Patches
    'data/user/database/french/DIbella\'s Blessing - RSV Exclusion Patches - French/DIbella\'s Blessing - RSV Exclusion Patch.esp.json',
    # 5. AI Overhaul - Nithi NPC Enhancements Patch Hub
    *glob.glob('data/user/database/french/AI Overhaul - Nithi NPC Enhancements Patch Hub - French/*.json'),
    # 6. TSOS AI Overhaul patch & other TSOS patches
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_AI_Overall_Patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDawnguard.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedDragonborn.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOSRefinedHearthfire.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/tsos_apachii_store_patch.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_TsunDal_Patch.esp.json'
]

print(f"Total files in Phase 2D: {len(files_2d)}")

# Let's check all entries
all_anomalies = []
total_entries = 0

for fpath in files_2d:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    total_entries += len(data)
    
    for item in data:
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = item.get('original', '')
        curr = item.get('string', '')
        
        # Check 1: Empty or whitespace
        if not curr or not curr.strip():
            all_anomalies.append((fname, fid, typ, idx, orig, curr, "EMPTY_STRING"))
            continue
            
        # Check 2: Obvious English leftover words in NPC names or descriptions
        # e.g., Guard, Bandit, Warrior, Mage, Hunter, Citizen, Prisoner, Soldier, Ghost, Skeleton, Vampire, Cultist
        en_words = ['guard', 'bandit', 'warrior', 'hunter', 'prisoner', 'soldier', 'ghost', 'cultist', 'assassin',
                    'courier', 'beggar', 'miner', 'farmer', 'cook', 'apprentice', 'child', 'boy', 'girl', 'priest',
                    'priestess', 'elder', 'captain', 'commander', 'general', 'sergeant', 'corpse', 'sailor', 'fisherman']
        
        orig_words = set(orig.lower().split())
        curr_words = set(curr.lower().split())
        
        for w in en_words:
            if w in orig_words and w in curr_words:
                # If the word is still in English in French translation, check if it's not a common proper noun
                # e.g., "Garde" in FR vs "Guard" in EN. If "guard" is in curr, that's English!
                all_anomalies.append((fname, fid, typ, idx, orig, curr, f"ENGLISH_KEYWORD_REMAINING: {w}"))
                break

print(f"Total entries inspected: {total_entries}")
print(f"Total anomalies flagged: {len(all_anomalies)}")
for an in all_anomalies:
    print(f"[{an[0]}] {an[1]} | {an[2]} | {an[3]}")
    print(f"   Orig: {repr(an[4])}")
    print(f"   Curr: {repr(an[5])}")
    print(f"   Type: {an[6]}")
