"""Independent verification script for Phase 5."""
import json
import os

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

# Check the modified files
checks = [
    # Book pagebreaks
    ("LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", 3549, 4, "Frostmere Crypt"),
    ("LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", 3918, 8, "Japhet LOTD"),
    ("USSEP - Traduction Francaise/unofficial skyrim special edition patch.esp.json", 2630, 8, "Japhet USSEP"),

    # Set agreements
    ("Armure daedrique légère/mihailxivkynarmor.esp.json", 7, "Gantelets daedriques légers", "Xivkyn Gauntlets"),
    ("Dragon Infused Daedric Armor fr/DragonInfusedDaedricArmor.esp.json", 2, "Bottes daedriques infusées du dragon (lourdes)", "Dragon Infused Boots"),
    ("Apocalypse - Magie de Bordeciel/Apocalypse - Magic of Skyrim.esp.json", 1730, "Armure de Khash-Ti Dhrur", "Khash-Ti Armor"),

    # Calques
    ("Ordonnateur - Atouts de Bordeciel/Ordinator - Perks of Skyrim.esp.json", 909, "Permet de marchander", "Ordinator trade"),
    ("Amulettes de Bordeciel/SL01AmuletsSkyrim.esp.json", 51, "inflige <15> points de dégâts", "Amulets damage"),
    ("Les Outils de Kagrénac/Tools of Kagrenac.esp.json", 26, "inflige <mag> points de dégâts", "Kagrenac damage"),
]

passed = 0
failed = 0

for rel, idx, expected, desc in checks:
    p = os.path.join(DB_DIR, rel.replace("/", "\\"))
    try:
        with open(p, "r", encoding="utf-8") as fp:
            d = json.load(fp)
        s = d[idx]["string"]
        if isinstance(expected, int):
            count = s.count("[pagebreak]")
            if count == expected:
                passed += 1
                print(f"[OK] {desc}: pagebreaks = {count}")
            else:
                failed += 1
                print(f"[FAIL] {desc}: pagebreaks = {count} (expected {expected})")
        else:
            if expected in s:
                passed += 1
                print(f"[OK] {desc}: contains '{expected}'")
            else:
                failed += 1
                print(f"[FAIL] {desc}: missing '{expected}' in '{s}'")
    except Exception as e:
        failed += 1
        print(f"[ERROR] {desc} in {rel}: {e}")

print("=" * 60)
print(f"PHASE 5 VERIFICATION: {passed} PASSED, {failed} FAILED")
print("=" * 60)
