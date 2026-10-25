import json
import re
from pathlib import Path
from collections import Counter

db_dir = Path('data/user/database/french')

def extract_all_numbers(text):
    if not text:
        return []
    # Replace <mag>, <dur>, etc. with empty so only real numbers remain
    cleaned = re.sub(r'<[a-zA-Z_]+>', '', text)
    # Extract numbers (integer, float, percentages)
    matches = re.findall(r'\b\d+(?:[.,]\d+)?%?\b', cleaned)
    norm = []
    for m in matches:
        # strip trailing % or punctuation, normalize 1,5 -> 1.5
        val = m.replace('%', '').replace(',', '.')
        norm.append(val)
    return sorted(norm)

real_discrepancies = []

ignored_mods = [
    'legacy of the dragonborn', "l'héritage de l'enfant de dragon", 'lotd',
    'falskaar', 'wyrmstooth', 'inigo', 'lucien',
    'vigilant', 'unslaad', 'glenmoril', 'bruma', 'bsheartland', 'bsassets',
    'interesting npcs', '3dnpc', 'unofficial skyrim special edition patch'
]

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    mod_name = p.parent.name
    mod_name_lower = mod_name.lower()
    
    if any(ig in mod_name_lower for ig in ignored_mods):
        continue
        
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            rec_type = s.get('type', '')
            
            if not trans or not orig or trans == orig:
                continue
            
            # Check only gameplay perks, spells, magic effects, enchantments, actor values, potions
            is_gameplay = any(t in rec_type for t in ['PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH']) or any(
                k in orig.lower() for k in ['increase', 'decrease', 'damage', 'points', 'health', 'magicka', 'stamina', 'seconds', '%']
            )
            if not is_gameplay:
                continue
            
            orig_nums = extract_all_numbers(orig)
            trans_nums = extract_all_numbers(trans)
            
            # If both have numbers but sets of values are different
            if orig_nums != trans_nums:
                # Exclude trivial cases like empty in one when it's not a stat
                real_discrepancies.append({
                    'mod': mod_name,
                    'file': p.name,
                    'form_id': form_id,
                    'type': rec_type,
                    'original': orig,
                    'translation': trans,
                    'orig_nums': orig_nums,
                    'trans_nums': trans_nums
                })
    except Exception:
        pass

print(f"Total REAL numeric discrepancies: {len(real_discrepancies)}")
with open('real_numeric_discrepancies.json', 'w', encoding='utf-8') as f:
    json.dump(real_discrepancies, f, indent=2, ensure_ascii=False)
