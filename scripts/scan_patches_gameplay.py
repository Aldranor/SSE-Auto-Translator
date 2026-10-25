import os
import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

patch_keywords = [
    'patch', 'compat', 'integration', 'rebalance', 'reworked', 
    'fix', 'tweak', 'hub', 'override', 'nolvus'
]

def is_patch(path: Path) -> bool:
    name_low = path.name.lower()
    folder_low = path.parent.name.lower()
    return any(k in name_low or k in folder_low for k in patch_keywords)

print("Scanning for patch database files...")
patch_files = [p for p in db_dir.rglob('*.json') if p.name != 'index.json' and is_patch(p)]
print(f"Found {len(patch_files)} patch database files.")

# Analyze discrepancies in patches
gameplay_types = {'PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH', 'AVIF'}

patch_issues = []

for p in patch_files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            rec_type = s.get('type') or ''
            # Check gameplay types, or if original contains gameplay text
            is_gameplay = any(t in rec_type for t in gameplay_types) or any(
                w in (s.get('original') or '').lower() for w in ['<mag>', '<dur>', '%', 'damage', 'health', 'magicka', 'stamina', 'points', 'resist', 'chance']
            )
            if not is_gameplay:
                continue
                
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            
            if not orig:
                continue
                
            # Issue 1: Untranslated English in a patch gameplay record
            if not trans or orig == trans:
                # If more than 1 word and not a code/number
                if len(orig.split()) > 1 and not orig.startswith('<') and not orig.startswith('['):
                    patch_issues.append({
                        'mod': p.parent.name,
                        'file': p.name,
                        'form_id': form_id,
                        'type': rec_type,
                        'issue': 'Gameplay string left in English in patch',
                        'original': orig,
                        'translation': trans
                    })
                continue
            
            # Issue 2: Numeric difference (% or numbers differ between EN and FR)
            # Extract numbers excluding tags like <mag>
            en_clean = re.sub(r'<[a-zA-Z_]+>', '', orig)
            fr_clean = re.sub(r'<[a-zA-Z_]+>', '', trans)
            en_nums = [n.replace('%', '').replace(',', '.') for n in re.findall(r'\b\d+(?:[.,]\d+)?%?\b', en_clean)]
            fr_nums = [n.replace('%', '').replace(',', '.') for n in re.findall(r'\b\d+(?:[.,]\d+)?%?\b', fr_clean)]
            
            # Exclude standard feet -> mètres conversions
            is_metric = bool(re.search(r'\b(?:feet|foot)\b', orig, re.IGNORECASE) and re.search(r'\b(?:mètres|mètre|m)\b', trans, re.IGNORECASE))
            
            if not is_metric and set(en_nums) != set(fr_nums):
                # Filter out pure thousand separators like "5 000" -> "5" and "000"
                if not ('000' in fr_nums and any(n.endswith('000') for n in en_nums)):
                    patch_issues.append({
                        'mod': p.parent.name,
                        'file': p.name,
                        'form_id': form_id,
                        'type': rec_type,
                        'issue': 'Numeric discrepancy in patch gameplay text',
                        'original': orig,
                        'translation': trans,
                        'en_nums': en_nums,
                        'fr_nums': fr_nums
                    })
    except Exception as e:
        pass

print(f"Total gameplay issues found in patches: {len(patch_issues)}")
with open('patch_gameplay_issues.json', 'w', encoding='utf-8') as f:
    json.dump(patch_issues, f, indent=2, ensure_ascii=False)
