import json
from pathlib import Path

# 1. Weapons patch
p_weap = Path("data/user/database/french/Nolvus Awakening Weapons Patch - French/nolvus awakening weapons patch.esp.json")
data_w = json.load(open(p_weap, encoding="utf-8"))
for it in data_w:
    if it.get("type") == "WEAP FULL" and "Dragonbane" in it.get("original", ""):
        it["string"] = "Fléau des dragons"
        it["status"] = "TranslationComplete"
with open(p_weap, "w", encoding="utf-8") as f:
    json.dump(data_w, f, indent=2, ensure_ascii=False)

# 2. Crafting patch
p_craft = Path("data/user/database/french/Nolvus Awakening Crafting Patch - French/nolvus awakening crafting patch.esp.json")
data_c = json.load(open(p_craft, encoding="utf-8"))
for it in data_c:
    if it.get("type") == "SPEL FULL" and "Sinderion" in it.get("original", ""):
        it["string"] = "Héritage de Sinderion"
        it["status"] = "TranslationComplete"
with open(p_craft, "w", encoding="utf-8") as f:
    json.dump(data_c, f, indent=2, ensure_ascii=False)

print("Corrected Dragonbane names to 'Fléau des dragons' and Sinderion to 'Héritage de Sinderion'.")
