import os
import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

def extract_numbers(text):
    if not text:
        return []
    # Remove HTML tags / color tags / variable tags first
    cleaned = re.sub(r'<[^>]+>', '', text)
    # Extract floating point and integer numbers
    # Also ignore years like 4E 201 or dates if needed, or keep all numbers
    numbers = re.findall(r'\b\d+(?:[.,]\d+)?%?\b', cleaned)
    # normalize comma decimals: 1,5 -> 1.5
    norm_nums = []
    for n in numbers:
        n_clean = n.replace(',', '.')
        norm_nums.append(n_clean)
    return norm_nums

# Mod types to check
target_record_types = {'PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH', 'BOOK', 'QUST'}

ignored_mods = [
    'legacy of the dragonborn', "l'héritage de l'enfant de dragon", 'lotd',
    'falskaar', 'wyrmstooth', 'inigo', 'lucien',
    'vigilant', 'unslaad', 'glenmoril', 'bruma', 'bsheartland', 'bsassets',
    'interesting npcs', '3dnpc', 'unofficial skyrim special edition patch'
]

discrepancies = []

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
            
            # Check if this is a perk, spell, magic effect or has description
            orig_nums = extract_numbers(orig)
            trans_nums = extract_numbers(trans)
            
            # If both have numbers but they differ
            if orig_nums != trans_nums:
                # Ignore if just order difference or empty
                if set(orig_nums) != set(trans_nums):
                    # Check if original or translation has numbers
                    discrepancies.append({
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

print(f"Total numeric discrepancies found: {len(discrepancies)}")
with open('numeric_discrepancies.json', 'w', encoding='utf-8') as f:
    json.dump(discrepancies, f, indent=2, ensure_ascii=False)
