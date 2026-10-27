# -*- coding: utf-8 -*-
"""
Script d'audit, révision et traduction pour :
1. Stances - Dynamic Weapon Movesets SE.esp.json (Mod de base)
2. Stances - Add-On.esp.json (Add-On)
"""

import json

BASE_JSON_PATH = r"data/user/database/french/Stances - Dynamic Animation Sets/stances - dynamic weapon movesets se.esp.json"
ADDON_JSON_PATH = r"data/user/database/french/Stances - Add-On.esp - French/stances - add-on.esp.json"

# --- 1. MOD DE BASE ---
BASE_TRANSLATIONS = {
    # Noms de base harmonisés sur "Posture"
    ("04005901|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "Stances - Dynamic Weapon Movesets"):
        "Postures - Mouvements d'armes dynamiques",
    ("04005902|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "Stances - Dynamic Weapon Movesets"):
        "Postures - Mouvements d'armes dynamiques",
    ("04005903|Stances - Dynamic Weapon Movesets SE.esp", "QUST FULL", "Stances - Dynamic Weapon Movesets"):
        "Postures - Mouvements d'armes dynamiques",

    ("04005908|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "High Stance"):
        "Posture haute",
    ("04042518|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "High Stance"):
        "Posture haute",
    ("04005905|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "High Stance"):
        "Posture haute",

    ("04005909|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "Mid Stance"):
        "Posture médiane",
    ("04042519|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "Mid Stance"):
        "Posture médiane",
    ("04005906|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "Mid Stance"):
        "Posture médiane",

    ("0400590C|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "Low Stance"):
        "Posture basse",
    ("0404251A|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "Low Stance"):
        "Posture basse",
    ("04005907|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "Low Stance"):
        "Posture basse",

    # Descriptions MGEF DNAM avec terminologie officielle (Vigueur et non endurance) et style fluide
    ("04005906|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "Attacks from this stance are balanced between defensive and offensive properties. It excels at blocking. Mid Stance is good for defense, and is easy to use, but attack power falls somewhere between High Stance and Low Stance."):
        "Les attaques adoptées depuis cette posture offrent un équilibre idéal entre attaque et défense. Elle excelle au blocage. La posture médiane est solide sur le plan défensif et facile à manier, mais sa puissance d'attaque se situe entre celle de la posture haute et de la posture basse.",

    ("04005905|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "Attacks from this stance feature increased damage at the cost of reduces Stamina regeneration. High Stance emphasizes attack power and aggression. It provides more Attack and Break power than any other stance, but defense and maneuverability are relatively limited."):
        "Les attaques adoptées depuis cette posture infligent des dégâts accrus au détriment d'une régénération de vigueur ralentie. La posture haute privilégie la puissance d'attaque et l'agressivité, offrant une force d'impact et une capacité de rupture supérieures à toute autre posture, mais la défense et la maniabilité y sont plus restreintes.",

    ("04005907|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "Attacks from this stance are fast and low damage as well as low Stamina consuming. Focuses on quick movement and is effective against groups or escaping a situation. Low Stance is best for dodging. Its primary focus is evasive movement, allowing you to escape quickly, get behind your opponent and attack."):
        "Les attaques de cette posture sont rapides, infligent des dégâts modérés et consomment peu de vigueur. Axée sur la vivacité des déplacements, elle est idéale contre les groupes ou pour se dégager d'une situation difficile. La posture basse excelle dans l'esquive et le mouvement évasif, vous permettant de vous replier rapidement, de contourner votre adversaire et de riposter.",
}

# --- 2. ADD-ON ---
ADDON_TRANSLATIONS = {
    # Vitesse de déplacement
    ("06000803|Stances - Add-On.esp", "MGEF FULL", "Movement Speed Buff"):
        "Bonus de vitesse de déplacement",
    ("06000808|Stances - Add-On.esp", "MGEF FULL", "Movement Speed Debuff"):
        "Pénalité de vitesse de déplacement",

    # Vitesse d'attaque
    ("06000802|Stances - Add-On.esp", "MGEF FULL", "Attack Speed Buff: Main Hand"):
        "Bonus de vitesse d'attaque : main principale",
    ("06000807|Stances - Add-On.esp", "MGEF FULL", "Attack Speed Buff: Off-Hand"):
        "Bonus de vitesse d'attaque : main secondaire",
    ("06000805|Stances - Add-On.esp", "MGEF FULL", "Attack Speed Debuff: Main Hand"):
        "Pénalité de vitesse d'attaque : main principale",
    ("06000806|Stances - Add-On.esp", "MGEF FULL", "Attack Speed Debuff: Off-Hand"):
        "Pénalité de vitesse d'attaque : main secondaire",

    # Correctifs techniques de vitesse
    ("06000812|Stances - Add-On.esp", "SPEL FULL", "Base WeaponSpeedMult Fix"):
        "Correctif de vitesse d'attaque de base",
    ("06000810|Stances - Add-On.esp", "MGEF FULL", "Weapon Speed Fix: Main Hand"):
        "Ajustement de vitesse d'arme : main principale",
    ("06000811|Stances - Add-On.esp", "MGEF FULL", "Weapon Speed Fix: Off-Hand"):
        "Ajustement de vitesse d'arme : main secondaire",

    # Résistances et Vigueur
    ("0600080B|Stances - Add-On.esp", "MGEF FULL", "Resist Damage"):
        "Résistance aux dégâts",
    ("0600080A|Stances - Add-On.esp", "MGEF FULL", "Regenerate Stamina"):
        "Récupération de vigueur",
    ("06000809|Stances - Add-On.esp", "MGEF FULL", "Damage Stamina Regeneration"):
        "Pénalité de récupération de vigueur",

    # Atouts et Quête MCM
    ("0600080C|Stances - Add-On.esp", "PERK FULL", "Stances Personalized Perk"):
        "Postures personnalisées",
    ("06000804|Stances - Add-On.esp", "MGEF FULL", "Stances Personalized Perk"):
        "Postures personnalisées",
    ("06000815|Stances - Add-On.esp", "QUST FULL", "Personalized Stances MCM"):
        "Menu MCM de postures personnalisées",

    # Overrides des noms de postures
    ("05005908|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "High Stance"):
        "Posture haute",
    ("05005905|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "High Stance"):
        "Posture haute",
    ("05042518|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "High Stance"):
        "Posture haute",

    ("05005909|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "Mid Stance"):
        "Posture médiane",
    ("05005906|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "Mid Stance"):
        "Posture médiane",
    ("05042519|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "Mid Stance"):
        "Posture médiane",

    ("0500590C|Stances - Dynamic Weapon Movesets SE.esp", "SPEL FULL", "Low Stance"):
        "Posture basse",
    ("05005907|Stances - Dynamic Weapon Movesets SE.esp", "MGEF FULL", "Low Stance"):
        "Posture basse",
    ("0504251A|Stances - Dynamic Weapon Movesets SE.esp", "PERK FULL", "Low Stance"):
        "Posture basse",

    # Descriptions MGEF DNAM spécifiques à l'Add-On
    ("05005905|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "High Stance emphasizes aggression providing more attack and break power than any other stance at the expense of limiting your defence, overall maneuverability, and stamina regeneration."):
        "La posture haute privilégie l'agressivité, conférant une puissance d'attaque et de rupture inégalée, au détriment de la défense, de la maniabilité générale et de la régénération de vigueur.",

    ("05005906|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "Mid Stance is the most defensive of the stances. Excelling at blocking and damage reduction you are harder to stagger. Comes with a modest loss of attack power."):
        "La posture médiane est la plus défensive. Excellant dans le blocage et la réduction des dégâts subis, vous êtes plus difficile à déséquilibrer, au prix d'une légère diminution de la puissance d'attaque.",

    ("05005907|Stances - Dynamic Weapon Movesets SE.esp", "MGEF DNAM",
     "Low Stance focuses on evasive movement . Attacks from this stance are faster but don't strike as hard, tiring you less and allowing for greater stamina regeneration."):
        "La posture basse met l'accent sur les mouvements d'esquive. Les attaques adoptées dans cette posture sont plus vives mais moins percutantes, réduisant la fatigue et favorisant une meilleure régénération de vigueur.",
}

def update_base():
    print(f"Loading base mod: {BASE_JSON_PATH}...")
    with open(BASE_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for entry in data:
        key = (entry.get("form_id"), entry.get("type"), entry.get("original"))
        if key in BASE_TRANSLATIONS:
            entry["string"] = BASE_TRANSLATIONS[key]
            entry["status"] = "TranslationComplete"
            updated += 1

    print(f"Base mod: updated {updated} entries.")

    with open(BASE_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    print("Base mod saved successfully.")

def update_addon():
    print(f"\nLoading addon mod: {ADDON_JSON_PATH}...")
    with open(ADDON_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for entry in data:
        key = (entry.get("form_id"), entry.get("type"), entry.get("original"))
        if key in ADDON_TRANSLATIONS:
            entry["string"] = ADDON_TRANSLATIONS[key]
            entry["status"] = "TranslationComplete"
            updated += 1
        else:
            print("Unmapped entry in addon:", key)

    print(f"Addon mod: updated {updated}/{len(data)} entries.")

    with open(ADDON_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    print("Addon mod saved successfully.")

if __name__ == "__main__":
    update_base()
    update_addon()
