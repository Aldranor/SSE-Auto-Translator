import json
from collections import defaultdict

with open("detailed_analysis.json", "r", encoding="utf-8") as f:
    data = json.load(f)

false_pos = data["pure_false_positives"]

groups = {
    "PNJ_NAMES": [],      # Mods containing only NPC proper names (replacers, children, orcs, followers)
    "TECH_ANIM": [],      # Technical animation effects, script events, internal dummy variables
    "PROPER_WEAPONS": [], # Weapon/Armor unique proper names (fantasy/author names)
    "DEV_INTERNAL": []    # Internal quest IDs (Dialogue...), test cells, controller spells
}

for item in false_pos:
    cats = item["categories"]
    mod = item["mod"]
    file = item["file"]
    total = item["total_incomplete"]
    
    samples = []
    for c, itms in item["cat_details"].items():
        for t, orig in itms:
            samples.append(f"{orig} [{t}]")
            
    sample_str = ", ".join(samples[:3])
    entry = {"mod": mod, "file": file, "total": total, "samples": sample_str}
    
    if cats.get("npc_name", 0) == total:
        groups["PNJ_NAMES"].append(entry)
    elif cats.get("tech_var", 0) == total:
        groups["TECH_ANIM"].append(entry)
    elif cats.get("proper_noun", 0) == total:
        groups["PROPER_WEAPONS"].append(entry)
    else:
        # Check predominant
        if cats.get("npc_name", 0) > 0 and cats.get("npc_name", 0) + cats.get("dev_internal", 0) >= total * 0.7:
            groups["PNJ_NAMES"].append(entry)
        elif cats.get("tech_var", 0) + cats.get("internal_dev", 0) >= total * 0.7:
            groups["TECH_ANIM"].append(entry)
        else:
            groups["DEV_INTERNAL"].append(entry)

with open("categorized_false_positives.json", "w", encoding="utf-8") as out:
    json.dump(groups, out, indent=2, ensure_ascii=False)

print("SUMMARY OF FALSE POSITIVES:")
for g, items in groups.items():
    print(f"\n=== {g} ({len(items)} mods/files) ===")
    for it in sorted(items, key=lambda x: x['mod']):
        line = f"  * {it['mod']} ({it['file']}) - {it['total']} str : {it['samples']}"
        print(line.encode("ascii", "replace").decode("ascii"))
