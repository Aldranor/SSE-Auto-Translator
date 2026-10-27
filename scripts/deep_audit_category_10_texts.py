import json
import os
import re
import sys
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

sys.stdout.reconfigure(encoding='utf-8')

# Exclude proper names, technical identifiers, single-word names that are identical in FR/EN (e.g. Katana, Dagger if name, etc.)
# Look for translatable English words in names and descriptions

translatable_flags = []

en_words = [
    'the', 'of', 'and', 'in', 'with', 'for', 'to', 'from', 'at', 'by',
    'sword', 'shield', 'helmet', 'boots', 'gauntlets', 'cuirass', 'armor', 'bow', 'arrow',
    'ring', 'necklace', 'amulet', 'cloak', 'robe', 'staff', 'dagger', 'axe', 'mace',
    'potion', 'poison', 'scroll', 'book', 'key', 'spell', 'tome',
    'damage', 'health', 'magicka', 'stamina', 'increases', 'decreases', 'points', 'seconds',
    'percent', 'chance', 'target', 'caster', 'absorb', 'resist', 'fire', 'frost', 'shock'
]

pattern = re.compile(r'\b(' + '|'.join(en_words) + r')\b', re.IGNORECASE)

for target_name, fpath in found_files.items():
    if 'vigilant subtitle fix' in target_name:
        # 1,121 subtitle lines, already checked or checked separately
        continue
    with open(fpath, 'r', encoding='utf-8') as jf:
        data = json.load(jf)
    
    for item in data:
        orig = str(item.get('original') or '')
        curr = str(item.get('string') or '')
        typ = item.get('type')
        fid = item.get('form_id')
        idx = item.get('index')
        st = item.get('status')
        
        if st == 'NoTranslationRequired':
            continue
            
        # If original and current are identical, check if it's English
        if orig == curr and len(orig) > 3:
            # Check if original contains English words
            matches = pattern.findall(orig)
            # Exclude false positives like "in", "de", etc. if it's French
            # But here orig == curr, so if it contains English words, it might be untranslated English!
            if len(matches) >= 2 or (len(matches) == 1 and matches[0].lower() in ['sword', 'shield', 'helmet', 'boots', 'gauntlets', 'cuirass', 'armor', 'bow', 'ring', 'necklace', 'amulet', 'cloak', 'staff', 'dagger']):
                translatable_flags.append({
                    'file': target_name,
                    'form_id': fid,
                    'type': typ,
                    'index': idx,
                    'original': orig,
                    'current': curr,
                    'matches': matches
                })

print(f"Total potential untranslated items flagged: {len(translatable_flags)}")
for f in translatable_flags:
    print(f"\n[{f['file']}] {f['form_id']} ({f['type']}) : matches={f['matches']}")
    print(f"   Orig: {repr(f['original'])}")
    print(f"   Curr: {repr(f['current'])}")
