import json
from collections import Counter

with open('numeric_discrepancies.json', 'r', encoding='utf-8') as f:
    discrepancies = json.load(f)

print(f"Total: {len(discrepancies)}")

# Filter to gameplay relevant: PERK, SPEL, MGEF, ENCH, ALCH
gameplay_discrepancies = [
    d for d in discrepancies 
    if any(t in (d.get('type') or '') for t in ['PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH'])
    or any(w in d.get('original', '').lower() for w in ['damage', 'points', '%', 'increase', 'decrease', 'cost', 'health', 'magicka', 'stamina', 'seconds'])
]

print(f"Gameplay rebalances / discrepancies: {len(gameplay_discrepancies)}")

# Look at top mods affected
mod_counts = Counter(d['mod'] for d in gameplay_discrepancies)
print("\nTop 15 mods with gameplay numeric discrepancies:")
for m, c in mod_counts.most_common(15):
    print(f"  {m}: {c}")

print("\nSample 15 critical gameplay discrepancies:")
for d in gameplay_discrepancies[:15]:
    print(f"Mod: {d['mod']} | File: {d['file']} | Type: {d['type']}")
    print(f"  Orig: {d['original']}")
    print(f"  Trad: {d['translation']}")
    print(f"  Orig Nums: {d['orig_nums']} vs Trad Nums: {d['trans_nums']}")
    print("-" * 50)
