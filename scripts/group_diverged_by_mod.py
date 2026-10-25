import json
import re

with open('true_balance_discrepancies.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by mod
by_mod = {}
for x in items:
    # Filter out pure metric conversions
    if re.search(r'\b(?:feet|foot)\b', x['original'], re.IGNORECASE) and re.search(r'\b(?:mètres|mètre|m)\b', x['translation'], re.IGNORECASE):
        continue
    # Filter out trivial cases
    if x['original'] == x['translation']:
        continue
    m = x['mod']
    if m not in by_mod:
        by_mod[m] = []
    by_mod[m].append(x)

print(f"Total mods with diverged perks/spells descriptions: {len(by_mod)}")
for mod_name, mod_items in sorted(by_mod.items(), key=lambda kv: len(kv[1]), reverse=True):
    print(f"- {mod_name}: {len(mod_items)} entrées")
