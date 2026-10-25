import json
import re

with open('true_balance_discrepancies.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total: {len(items)}\n")

for i, x in enumerate(items[:30], 1):
    print(f"[{i}] {x['mod']} > {x['file']} ({x['type']})")
    print(f"  EN: {x['original']}")
    print(f"  FR: {x['translation']}")
    print()
