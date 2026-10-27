import json
from collections import defaultdict

data = json.load(open("local_unverified_analysis.json", encoding="utf-8"))
unverif = data["unverified"]
total_strings = sum(u["total_strings"] for u in unverif)
total_files = sum(u["total_files"] for u in unverif)
empty_strings = sum(u["empty_strings"] for u in unverif)

print(f"Total unverified local mods: {len(unverif)}")
print(f"Total files in these mods: {total_files}")
print(f"Total strings: {total_strings}")
print(f"Empty strings: {empty_strings}")

# Sort by date, then name
by_date = sorted(unverif, key=lambda x: (x["date"], x["name"]))

# Categories based on naming patterns
categories = {
    "Nolvus & Overhaul Patches": [],
    "Legacy of the Dragonborn (LOTD) & Addons": [],
    "Quêtes, Donjons & Nouveaux Lieux": [],
    "Gameplay, Combats, Atouts & Mécaniques": [],
    "Équipements, Armes & Armures": [],
    "PNJs, Compagnons & Enfants (Modpocalypse, RS Children, etc.)": [],
    "Immersion, Audio, Visuel & Environnement": [],
    "Interfaces, MCM & Menus": [],
    "Autres Patchs & Fixes": []
}

for u in unverif:
    name_l = u["name"].lower()
    files_l = " ".join(u["unverified_files"]).lower()
    combined = name_l + " " + files_l
    
    if "lotd" in combined or "dragonborn" in combined or "museum" in combined:
        categories["Legacy of the Dragonborn (LOTD) & Addons"].append(u)
    elif "nolvus" in combined:
        categories["Nolvus & Overhaul Patches"].append(u)
    elif any(k in combined for k in ["modpocalypse", "rs children", "npc", "follower", "companion", "inigo", "vilkas", "serana", "aedan", "citizens"]):
        categories["PNJs, Compagnons & Enfants (Modpocalypse, RS Children, etc.)"].append(u)
    elif any(k in combined for k in ["quest", "dungeon", "city", "town", "wyrm", "falskaar", "bruma", "reach", "sanctum", "shack", "temple", "gate", "ruin"]):
        categories["Quêtes, Donjons & Nouveaux Lieux"].append(u)
    elif any(k in combined for k in ["perk", "spell", "magic", "combat", "animation", "stance", "vokrii", "adamant", "stealth", "arrow", "enchant", "alchemy", "death", "dodge", "poise", "parry"]):
        categories["Gameplay, Combats, Atouts & Mécaniques"].append(u)
    elif any(k in combined for k in ["armor", "weapon", "sword", "bow", "shield", "blade", "axe", "helm", "robe", "clothes", "outfit", "ring", "amulet", "craft", "smithing"]):
        categories["Équipements, Armes & Armures"].append(u)
    elif any(k in combined for k in ["mcm", "menu", "ui", "hud", "key", "display", "font", "interface", "map"]):
        categories["Interfaces, MCM & Menus"].append(u)
    elif any(k in combined for k in ["audio", "sound", "music", "weather", "lighting", "water", "tree", "grass", "texture", "mesh", "fx", "immersion", "campfire", "hunter"]):
        categories["Immersion, Audio, Visuel & Environnement"].append(u)
    else:
        categories["Autres Patchs & Fixes"].append(u)

print("\n--- CATEGORY BREAKDOWN ---")
for cat, items in categories.items():
    cat_strings = sum(it["total_strings"] for it in items)
    print(f"{cat}: {len(items)} mods, {cat_strings} strings")

# Top 20 largest mods among unverified
print("\n--- TOP 20 LARGEST MODS (BY STRING COUNT) ---")
largest = sorted(unverif, key=lambda x: x["total_strings"], reverse=True)[:20]
for it in largest:
    print(f"[{it['date']}] {it['name']} : {it['total_strings']} chaînes ({it['total_files']} fichiers)")
