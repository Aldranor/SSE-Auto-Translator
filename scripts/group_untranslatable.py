import json
from collections import defaultdict

with open("classification_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

no_trans = data["NO_TRANSLATION_NEEDED"]
print(f"Total files in NO_TRANSLATION_NEEDED: {len(no_trans)}")

# Group by the dominant type of strings
grouped_by_reason = {
    "only_npc_proper_names": [],    # NPC proper names (e.g. Remiel, Kaidan, Auri, Bijin, Pandorable, etc.)
    "only_tech_variables": [],      # Technical tokens, <Alias>, <mag>, numbers, brackets
    "only_internal_dev_engine": [], # Dummy, visual effects, hidden perks, sound markers, test cells
    "only_proper_item_names": [],   # Proper names of unique items/weapons (e.g. named weapons)
    "mixed_untranslatable": []      # Mix of the above
}

for item in no_trans:
    counts = item["counts"]
    total = item["total_incomplete"]
    
    npc = counts.get("npc_proper_name", 0)
    tech = counts.get("tech_var", 0)
    dev = counts.get("internal_dev", 0)
    item_name = counts.get("proper_item_name", 0)
    ident = counts.get("identical_valid", 0)
    
    if npc == total:
        grouped_by_reason["only_npc_proper_names"].append(item)
    elif tech == total:
        grouped_by_reason["only_tech_variables"].append(item)
    elif dev == total:
        grouped_by_reason["only_internal_dev_engine"].append(item)
    elif item_name == total:
        grouped_by_reason["only_proper_item_names"].append(item)
    else:
        grouped_by_reason["mixed_untranslatable"].append(item)

for k, v in grouped_by_reason.items():
    print(f"{k}: {len(v)}")

with open("grouped_untranslatable_mods.json", "w", encoding="utf-8") as out:
    json.dump(grouped_by_reason, out, indent=2, ensure_ascii=False)
