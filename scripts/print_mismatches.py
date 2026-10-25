import json

with open('concept_mismatches.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total: {len(items)}\n")
for i, item in enumerate(items, 1):
    print(f"[{i}] Mod: {item['mod']} | File: {item['file']} ({item['type']})")
    print(f"  EN: {item['original']}")
    print(f"  FR: {item['translation']}")
    print(f"  Diff concepts: EN={item['en_concepts']} vs FR={item['fr_concepts']} (ratio {item['len_ratio']})")
    print("-" * 60)
