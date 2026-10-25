import json
from collections import Counter

with open('real_numeric_discrepancies.json', 'r', encoding='utf-8') as f:
    discrepancies = json.load(f)

# Sort by those where both original and translation have numbers, but they differ
changed_values = []
for d in discrepancies:
    o_nums = d['orig_nums']
    t_nums = d['trans_nums']
    if o_nums and t_nums and o_nums != t_nums:
        changed_values.append(d)

print(f"Total where both have numbers but values differ: {len(changed_values)}")

mod_counts = Counter(d['mod'] for d in changed_values)
print("\nTop mods:")
for m, c in mod_counts.most_common(12):
    print(f"  {m}: {c}")

print("\nSample 20 concrete discrepancies:")
for d in changed_values[:20]:
    print(f"[{d['mod']}] ({d['type']})")
    print(f"  EN ({d['orig_nums']}): {d['original']}")
    print(f"  FR ({d['trans_nums']}): {d['translation']}\n")
