import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

extra_dirs = [
    'Dawn of Skyrim Director\'s Cut - Modpocalypse NPCs',
    'Dawn of Skyrim Director\'s Cut - Modpocalypse NPCs - Fix - French',
    'Modpocalypse NPCs - Citizens of Tamriel',
    'Modpocalypse NPCs - Cutting Room Floor',
    'Modpocalypse NPCs - Falskaar',
    'Modpocalypse NPCs - Legacy of the Dragonborn',
    'Modpocalypse NPCs - Moon and Star - French',
    'Modpocalypse NPCs - Moonpath to Elsweyr',
    'Modpocalypse NPCs - Project AHO - French',
    'Modpocalypse NPCs - The Forgotten City',
    'Modpocalypse NPCs - The Gray Cowl of Nocturnal - French',
    'Modpocalypse NPCs - Wyrmstooth',
    'Amber Guard - Modpocalypse NPCs - French',
    'Dunpar Wall - Modpocalypse NPCs - French',
    'Granite Hill Village - Modpocalypse NPCs',
    'Lainalten - Modpocalypse NPCs',
    'Oakwood - Modpocalypse NPCs',
    'Reich Corigate - Modpocalypse NPCs',
    'Sunthgat - Modpocalypse NPCs - French',
    'The Great Town of Karthwasten - Modpocalypse NPCs - French',
    'The Great Town of Shor\'s Stone - Modpocalypse NPCs - French',
    'The Great Village of Kynesgrove - Modpocalypse NPCs - French',
    'The Great Village of Mixwater Mill - Modpocalypse NPCs - French',
    'The Great Village of Old Hroldan - Modpocalypse NPCs - French',
]

total_files = 0
total_records = 0
empty_or_english = []

for d in extra_dirs:
    full_d = os.path.join('data/user/database/french', d)
    if os.path.exists(full_d):
        for f in glob.glob(os.path.join(full_d, '*.json')):
            total_files += 1
            data = json.load(open(f, encoding='utf-8'))
            total_records += len(data)
            for x in data:
                orig = x.get('original', '')
                curr = x.get('string', '')
                st = x.get('status')
                if not curr or not curr.strip():
                    empty_or_english.append((os.path.basename(f), x.get('form_id'), orig, curr, "EMPTY"))
                elif st == 'TranslationRequired':
                    empty_or_english.append((os.path.basename(f), x.get('form_id'), orig, curr, "REQUIRED"))

print(f"Extra Modpocalypse files: {total_files} files, {total_records} records.")
print(f"Anomalies: {len(empty_or_english)}")
for a in empty_or_english:
    print(a)
