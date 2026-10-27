import json
from pathlib import Path

p = Path("data/user/database/french/Nolvus Awakening Armors Balance Patch.esp - French/nolvus awakening armors balance patch.esp.json")
data = json.load(open(p, encoding="utf-8"))

corrections = {
    ("870008BF|Black Mage Armor SE.esp", "ARMO FULL"): "Armure d'ébène d'archimage noir (lourde)",
    ("870008BF|Black Mage Armor SE.esp", "ARMO DESC"): "Réduit de 15 % le coût de tous les sorts et augmente de 100 % la régénération de magie.",
    
    ("870008C1|Black Mage Armor SE.esp", "ARMO FULL"): "Armure d'ébène d'archimage noir (légère)",
    ("870008C1|Black Mage Armor SE.esp", "ARMO DESC"): "Réduit de 15 % le coût de tous les sorts et augmente de 100 % la régénération de magie.",
    
    ("870008C7|Black Mage Armor SE.esp", "ARMO FULL"): "Robe d'archimage noir",
    ("870008C7|Black Mage Armor SE.esp", "ARMO DESC"): "Réduit de 15 % le coût de tous les sorts et augmente de 100 % la régénération de magie.",
    
    ("870008C9|Black Mage Armor SE.esp", "ARMO FULL"): "Armure de plates d'archimage noir (lourde)",
    ("870008C9|Black Mage Armor SE.esp", "ARMO DESC"): "Réduit de 15 % le coût de tous les sorts et augmente de 100 % la régénération de magie.",
    
    ("870008CB|Black Mage Armor SE.esp", "ARMO FULL"): "Armure d'écailles d'archimage noir (légère)",
    ("870008CB|Black Mage Armor SE.esp", "ARMO DESC"): "Réduit de 15 % le coût de tous les sorts et augmente de 100 % la régénération de magie.",
    
    ("6B000861|Soul Hunter Armor.esp", "ARMO FULL"): "Cuirasse de chasseur d'âmes (armure légère)",
    ("6B000861|Soul Hunter Armor.esp", "ARMO DESC"): "Tous les sorts coûtent 25 % de moins et la magie se régénère 250 % plus vite. La réserve de magie augmente de 85 points.",
}

updated = 0
for item in data:
    key = (item.get("form_id"), item.get("type"))
    if key in corrections:
        item["string"] = corrections[key]
        item["status"] = "TranslationComplete"
        updated += 1

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Corrected {updated} records in Nolvus Armors Balance Patch.")
