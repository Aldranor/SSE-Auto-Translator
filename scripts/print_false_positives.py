import json

with open("detailed_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

false_pos = data["pure_false_positives"]
print(f"Total false positives: {len(false_pos)}")

for item in false_pos[:40]:
    cats = ", ".join(f"{k}: {v}" for k, v in item['categories'].items())
    sample_items = []
    for cat, items in item['cat_details'].items():
        for t, orig in items[:2]:
            sample_items.append(f"{orig} ({t})")
    sample_str = "; ".join(sample_items[:4])
    print(f"- **{item['mod']}** (`{item['file']}`) [{item['total_incomplete']} strings] -> {cats}")
    print(f"    Ex: {sample_str}")
