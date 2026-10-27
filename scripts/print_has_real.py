import json

with open("classification_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"=== 23 MODS WITH REAL STRINGS TO TRANSLATE ===")
for item in data["HAS_REAL_STRINGS"]:
    print(f"\n[Mod: {item['mod']}] - {item['file']} ({item['total_incomplete']} incomplete)")
    for s in item["must_translate_samples"]:
        print(f"   -> {s}")
