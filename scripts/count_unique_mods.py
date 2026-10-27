import json
from collections import defaultdict

with open("categorized_false_positives.json", "r", encoding="utf-8") as f:
    data = json.load(f)

unique_mods = set()
for g, items in data.items():
    for it in items:
        unique_mods.add(it["mod"])

print(f"Total unique mod folders in false positives: {len(unique_mods)}")
