import json
import re

with open('perks_spells_number_fixes.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Conversion ratios: feet -> mètres (approx 3.28 feet per meter)
def is_metric_conversion(orig, trans):
    # Check if 'feet' or 'foot' in orig and 'mètre' or 'metres' or 'm' in trans
    if re.search(r'\b(?:feet|foot)\b', orig, re.IGNORECASE) and re.search(r'\b(?:mètres|mètre|m)\b', trans, re.IGNORECASE):
        return True
    return False

true_balance_discrepancies = []

for item in items:
    orig = item['original']
    trans = item['translation']
    
    # If the ONLY difference is a feet->meters conversion, ignore it
    # Check percentage differences
    orig_pcts = re.findall(r'(\d+(?:[.,]\d+)?)\s*%', orig)
    trans_pcts = re.findall(r'(\d+(?:[.,]\d+)?)\s*%', trans)
    
    pct_mismatch = False
    if orig_pcts != trans_pcts:
        # Check if values actually differ
        o_set = set(p.replace(',', '.') for p in orig_pcts)
        t_set = set(p.replace(',', '.') for p in trans_pcts)
        if o_set != t_set:
            pct_mismatch = True
            
    # Check multiplier differences (e.g. "4 times", "twice", "10 times")
    has_multiplier_en = bool(re.search(r'\b(?:twice|\d+\s*times)\b', orig, re.IGNORECASE))
    
    # Check if it's not just a metric conversion
    if pct_mismatch or (not is_metric_conversion(orig, trans) and item['orig_nums'] != item['trans_nums']):
        true_balance_discrepancies.append({
            **item,
            'pct_mismatch': pct_mismatch
        })

print(f"Total true balance / outdated perk discrepancies: {len(true_balance_discrepancies)}")
with open('true_balance_discrepancies.json', 'w', encoding='utf-8') as f:
    json.dump(true_balance_discrepancies, f, indent=2, ensure_ascii=False)

# Let's inspect some top percentage mismatches
pct_mismatches = [x for x in true_balance_discrepancies if x.get('pct_mismatch')]
print(f"Total percentage mismatches (% differs between EN and FR): {len(pct_mismatches)}")
print("\nSample 15 percentage mismatches:")
for x in pct_mismatches[:15]:
    print(f"[{x['mod']}] ({x['type']})")
    print(f"  EN: {x['original']}")
    print(f"  FR: {x['translation']}")
    print("-" * 50)
