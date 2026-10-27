import json
from pathlib import Path

p = Path("data/user/database/french/Nolvus Awakening Weapons Balance Patch.esp - French/nolvus awakening weapons balance patch.esp.json")
data = json.load(open(p, encoding="utf-8"))

corrections = {
    ("28000800|[TDarce] Black Silence Durandal.esp", "WEAP FULL"): "Silence noir - Durandal",
    ("28000800|[TDarce] Black Silence Durandal.esp", "WEAP DESC"): "Inflige 10 points de dégâts de saignement pendant 5 secondes.",
    
    ("17000D64|FGCAegeanSentinelHalberd.esp", "WEAP FULL"): "Hallebarde de sentinelle égéenne +1",
    ("17000D64|FGCAegeanSentinelHalberd.esp", "WEAP DESC"): "Hallebarde maniée par les chevaliers égéens, des guerriers ayant voué leur vie à la protection du peuple de Tamriel.",
    
    ("17000D65|FGCAegeanSentinelHalberd.esp", "WEAP FULL"): "Hallebarde de sentinelle égéenne +2",
    ("17000D65|FGCAegeanSentinelHalberd.esp", "WEAP DESC"): "Hallebarde maniée par les chevaliers égéens, des guerriers ayant voué leur vie à la protection du peuple de Tamriel.",
    
    ("17000D66|FGCAegeanSentinelHalberd.esp", "WEAP FULL"): "Hallebarde de sentinelle égéenne +3",
    ("17000D66|FGCAegeanSentinelHalberd.esp", "WEAP DESC"): "Hallebarde maniée par les chevaliers égéens, des guerriers ayant voué leur vie à la protection du peuple de Tamriel.",
    
    ("17000D67|FGCAegeanSentinelHalberd.esp", "WEAP FULL"): "Hallebarde de sentinelle égéenne +4",
    ("17000D67|FGCAegeanSentinelHalberd.esp", "WEAP DESC"): "Hallebarde maniée par les chevaliers égéens, des guerriers ayant voué leur vie à la protection du peuple de Tamriel.",
    
    ("17000D68|FGCAegeanSentinelHalberd.esp", "WEAP FULL"): "Hallebarde de sentinelle égéenne +5",
    ("17000D68|FGCAegeanSentinelHalberd.esp", "WEAP DESC"): "Hallebarde maniée par les chevaliers égéens, des guerriers ayant voué leur vie à la protection du peuple de Tamriel.",
    
    ("24000D67|Elexorien.esp", "WEAP FULL"): "Elexorien (deux mains)",
    ("2C000805|Luciendar.esp", "WEAP FULL"): "Luciendar (Espadon)",
    
    ("38000D69|Swords 2-5.esp", "WEAP FULL"): "Traqueur",
    ("38000D66|Swords 2-5.esp", "WEAP FULL"): "Justice",
    ("38000D68|Swords 2-5.esp", "WEAP FULL"): "Traître",
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

print(f"Corrected {updated} records in Weapons Balance Patch.")
