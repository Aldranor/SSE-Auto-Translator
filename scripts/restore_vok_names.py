import json
from pathlib import Path

p = Path("data/user/database/french/Nolvus Awakening Vokriinator Black Integration.esp - French/nolvus awakening vokriinator black integration.esp.json")
data = json.load(open(p, encoding="utf-8"))

# Perk names mapping
perk_names = {
    "Furious Strength": "Force furieuse",
    "Ravage": "Ravage",
    "Flurry": "Rafale",
    "Maul": "Mutilation",
    "Crushing Blows": "Coups écrasants",
    "Fencer": "Fine lame",
    "Bone Breaker": "Brise-os",
    "Smite": "Châtiment",
    "Disciplined Fighter": "Combattant discipliné",
    "Clash of Champions": "Choc des champions",
    "Execute": "Exécution",
    "Fall of Kings": "Chute des rois",
    "Overrun": "Déferlement",
    "Ram's Head": "Tête de bélier",
    "Raging Torrent": "Torrent déchaîné",
    "Savage": "Sauvagerie",
    "Subdual": "Soumission",
    "Death's Door": "Porte de la mort",
    "Toll the Bell": "Le glas sonne",
    "Rise Above": "S'élever au-dessus",
    "Massacre": "Massacre",
    "Disciplined Striker": "Frappeur discipliné",
    "Skullcrusher": "Brise-crâne",
    "Limbsplitter": "Fendeur de membres",
    "Hack and Slash": "Fendre et tailler",
    "Bladesman": "Fine lame",
    "Dual Flurry": "Double rafale",
    "Dual Savagery": "Double sauvagerie",
    "Greatsword": "Espadon",
    "Warhammer": "Marteau de guerre",
    "Battleaxe": "Hache d'armes",
    "War Axe": "Hache de guerre",
    "Mace": "Masse",
    "Sword": "Épée",
    "Dagger": "Dague",
    "Rogue's Parry": "Parade du gredin",
    "Swaying Cobra": "Cobra ondulant",
    "Jinada": "Jinada",
    "Coiling Python": "Python constricteur",
    "Falling Sword": "Épée tombante",
    "Decimate": "Décimation",
    "Ferocious Strength": "Force féroce",
    "Shieldbiter": "Brise-bouclier",
    "Denting Blows": "Coups déformants",
    "Clash of Heroes": "Choc des héros",
    "Batter": "Pilonnage",
    "Overthrow": "Renversement",
    "Unleash the Beast": "Déchaîner la bête",
    "One-Handed Mastery": "Maîtrise d'arme à une main",
    "Two-Handed Mastery": "Maîtrise d'arme à deux mains",
    "Warmaster": "Maître de guerre",
    "Crater Maker": "Créateur de cratère",
}


restored_names = 0
for item in data:
    orig = item.get("original", "").strip()
    rec_type = item.get("type", "")
    current_trans = item.get("string", "")
    
    if "FULL" in rec_type:
        if orig in perk_names:
            item["string"] = perk_names[orig]
            item["status"] = "TranslationComplete"
            restored_names += 1
        elif current_trans != orig and len(current_trans) > 50 and len(orig) < 30:
            # The description was put in the name!
            print(f"Suspicious long name for {orig}: {current_trans}")

with open(p, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Restored {restored_names} perk names in Vokriinator Black Nolvus Integration.")
