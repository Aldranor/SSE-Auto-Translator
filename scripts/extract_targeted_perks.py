import json

with open('true_balance_discrepancies.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Inspect top mods
target_mods = [
    'La Voie du Sorcier', 'Adamant - Refonte des atouts', 'Vokrii - Atouts minimalistes',
    'Vokriinateur - Morceaux choisis', 'Artéfacts de Zim', 'Commerce & Troc'
]

categorized_fixes = {}

for m in target_mods:
    mod_items = [x for x in items if m in x['mod']]
    categorized_fixes[m] = mod_items

print("Summary of targeted mods:")
for m, l in categorized_fixes.items():
    print(f"- {m}: {len(l)} items")

with open('targeted_perk_fixes.json', 'w', encoding='utf-8') as f:
    json.dump(categorized_fixes, f, indent=2, ensure_ascii=False)
