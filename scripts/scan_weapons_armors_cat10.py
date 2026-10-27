import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('listing_traductions_locales_non_verifiees.md', 'r', encoding='utf-8') as f:
    text = f.read()

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

item_types = {'ARMO FULL', 'WEAP FULL', 'ALCH FULL', 'AMMO FULL', 'BOOK FULL', 'MISC FULL'}

untranslated = []
for target_name, fpath in found_files.items():
    if 'vigilant subtitle fix' in target_name:
        continue
    data = json.load(open(fpath, encoding='utf-8'))
    for item in data:
        typ = item.get('type')
        if typ in item_types:
            orig = str(item.get('original') or '')
            curr = str(item.get('string') or '')
            st = item.get('status')
            if st == 'NoTranslationRequired':
                continue
            if orig == curr and len(orig) > 3:
                # check if original contains english words
                en_match = re.search(r'\b(the|of|and|sword|dagger|bow|axe|armor|cuirass|boots|gauntlets|helmet|ring|necklace|dress|robes?|shield|staff|mace|cloak|vestments?|gown|knuckles|cross|pack|potion|poison|book|note|key)\b', orig, re.IGNORECASE)
                if en_match:
                    untranslated.append((target_name, item.get('form_id'), typ, orig, curr, en_match.group(0)))

print(f"Untranslated equipment/items found in Cat 10: {len(untranslated)}")
for u in untranslated:
    print(f"[{u[0]}] {u[1]} ({u[2]}) -> {repr(u[3])} matches {u[5]}")
