import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

# Track: category -> original -> set of (cleaned_translation, mod_name, file_name, form_id)
# Categories:
# 1. Locations: CELL, WRLD, LCTN
# 2. Perks / Skills: PERK, AVIF
# 3. Spells / Powers / Shouts / Words of Power: SPEL, MGEF, SHOU, WOOP

categories = {
    'Locations': {'CELL', 'WRLD', 'LCTN'},
    'Perks_Skills': {'PERK', 'AVIF'},
    'Spells_Magic': {'SPEL', 'MGEF', 'SHOU', 'WOOP'}
}

data_by_cat = {
    'Locations': defaultdict(lambda: defaultdict(list)),
    'Perks_Skills': defaultdict(lambda: defaultdict(list)),
    'Spells_Magic': defaultdict(lambda: defaultdict(list))
}

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    mod_name = p.parent.name
    file_name = p.name
    
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            rec_type = s.get('type') or ''
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            
            if not orig or not trans or orig == trans:
                continue
            
            # Match only NAME fields (FULL, or short strings < 60 chars)
            if 'DESC' in rec_type or 'DNAM' in rec_type or 'CNAM' in rec_type:
                # ignore descriptions for name consistency
                continue
            if len(orig) > 60:
                continue
                
            for cat_name, type_set in categories.items():
                if any(t in rec_type for t in type_set):
                    data_by_cat[cat_name][orig][trans].append({
                        'mod': mod_name,
                        'file': file_name,
                        'form_id': form_id
                    })
    except Exception:
        pass

# Now analyze conflicts
conflicts = {
    'Locations': [],
    'Perks_Skills': [],
    'Spells_Magic': []
}

for cat_name, orig_dict in data_by_cat.items():
    for orig, trans_map in orig_dict.items():
        # Clean variants to ignore simple case or whitespace differences
        cleaned_variants = {}
        for trans, occurrences in trans_map.items():
            norm = trans.strip().lower()
            if norm not in cleaned_variants:
                cleaned_variants[norm] = (trans, occurrences)
            else:
                cleaned_variants[norm][1].extend(occurrences)
                
        if len(cleaned_variants) > 1:
            # Significant conflict found!
            conflicts[cat_name].append({
                'original': orig,
                'variants': [
                    {
                        'translation': v_trans,
                        'count': len(v_occ),
                        'mods': list(set(x['mod'] for x in v_occ))[:5]
                    }
                    for v_trans, v_occ in cleaned_variants.values()
                ]
            })

print("=== CONFLICT SUMMARY ===")
print("Location conflicts:", len(conflicts['Locations']))
print("Perk/Skill conflicts:", len(conflicts['Perks_Skills']))
print("Spell/Magic conflicts:", len(conflicts['Spells_Magic']))

with open('name_consistency_conflicts.json', 'w', encoding='utf-8') as f:
    json.dump(conflicts, f, indent=2, ensure_ascii=False)
