import json

with open('targeted_perk_fixes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for mod_name, items in data.items():
    print(f"\n==================== {mod_name} ({len(items)}) ====================")
    for i, x in enumerate(items, 1):
        print(f"[{i}] ({x['type']}) ID: {x['form_id']}")
        print(f"  EN: {x['original']}")
        print(f"  FR: {x['translation']}")
        print()
