import json
from collections import Counter

with open("incomplete_mods_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total in has_translatable: {len(data['has_translatable'])}")
for item in data['has_translatable'][:40]:
    print(f"\n=== {item['mod']} | {item['file']} ({item['total_incomplete']} strings) ===")
    for s in item['real_samples'][:5]:
        print(f"   {s}")
