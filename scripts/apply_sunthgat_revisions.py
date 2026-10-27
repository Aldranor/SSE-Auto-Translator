import json
import shutil
from pathlib import Path

target_file = Path("data/user/database/french/Sunthgat/Sunthgat.esp.json")
backup_file = Path("data/user/database/french/Sunthgat/Sunthgat.esp.json.bak")

# Create backup
shutil.copy2(target_file, backup_file)
print(f"Created backup: {backup_file}")

with open(target_file, "r", encoding="utf-8") as f:
    entries = json.load(f)

# Complete dictionary of revisions keyed by (form_id, type, original)
revisions = {
    # MISC
    ("050293E3|Sunthgat.esp", "MISC FULL", "Suspicious Crate"): "Caisse suspecte",
    
    # WEAP
    ("05029401|Sunthgat.esp", "WEAP FULL", "Greatsword of Sister Hawk"): "Espadon de Sœur Faucon",
    
    # KEYM
    ("0500AD45|Sunthgat.esp", "KEYM FULL", "Clever Man's Cauldron Key"): "Clé du Chaudron de l'érudit",
    
    # CELL
    ("05005B40|Sunthgat.esp", "CELL FULL", "Clever Man's Cauldron"): "Le Chaudron de l'érudit",
    
    # LCTN
    ("05005B3E|Sunthgat.esp", "LCTN FULL", "Clever Man's Cauldron"): "Le Chaudron de l'érudit",
    
    # DIALOGUE & INFO - QUEST 01
    ("05014FDB|Sunthgat.esp", "INFO NAM1", "My partners will be pleased."): "Mes associés seront ravis.",
    ("050293E1|Sunthgat.esp", "INFO NAM1", "My partners will be pleased."): "Mes associés seront ravis.",
    
    # DIALOGUE & INFO - QUEST 02 (Gamrik & crate)
    ("050293E5|Sunthgat.esp", "DIAL FULL", "How's business up here?"): "Comment vont les affaires par ici ?",
    ("050293EE|Sunthgat.esp", "INFO NAM1", "Not many patrons, but there are other sources of income."): "Peu de clients, mais j'ai d'autres sources de revenus.",
    ("050293EE|Sunthgat.esp", "INFO NAM1", "Interested in recovering some stolen goods?"): "Récupérer des marchandises volées, ça vous intéresserait ?",
    ("050293E6|Sunthgat.esp", "DIAL FULL", "What do you need?"): "De quoi avez-vous besoin ?",
    ("050293EF|Sunthgat.esp", "INFO NAM1", "A former associate of mine thought it would be a good idea to disappear with a crate that belongs to me."): "L'un de mes anciens associés s'est mis en tête de disparaître avec une caisse qui m'appartient.",
    ("050293EF|Sunthgat.esp", "INFO NAM1", "I want that crate back. I'll show you where to find it."): "Je veux récupérer cette caisse. Je vais vous indiquer où la trouver.",
    ("050293E7|Sunthgat.esp", "DIAL FULL", "Not my line of work."): "Ce n'est pas dans mes cordes.",
    ("050293E9|Sunthgat.esp", "DIAL FULL", "About that retrieval job."): "À propos de cette caisse à récupérer...",
    ("050293F1|Sunthgat.esp", "INFO NAM1", "Ready to get going?"): "Vous êtes prêt à partir ?",
    ("050293F3|Sunthgat.esp", "INFO NAM1", "You better forget about this."): "Vous feriez mieux d'oublier tout ça.",
    ("050293F3|Sunthgat.esp", "INFO NAM1", "Take this coin and I will take care of the rest."): "Prenez cet or et je m'occupe du reste.",
    
    # DIALOGUE & INFO - QUEST 03 (Wendela & Larunon / Band of Kyne)
    ("050293F7|Sunthgat.esp", "DIAL FULL", "A war axe, huh? Have you always been a priest? "): "Une hache de guerre, hein ? Vous avez toujours été prêtresse ?",
    ("050293FE|Sunthgat.esp", "INFO NAM1", "I used to be part of a mercenary group. Not your average bandit rabble. We fought with honor. The Band of Kyne they called us."): "Jadis, je faisais partie d'une compagnie de mercenaires. Rien à voir avec de vulgaires bandits : nous nous battions avec honneur. On nous appelait la Bande de Kyne.",
    ("050293FE|Sunthgat.esp", "INFO NAM1", "But it has been almost three decades since then. We were betrayed by one of our own. Larunon, an elven mage. Not surprising."): "Mais cela remonte à près de trente ans. Nous avons été trahis par l'un des nôtres : Larunon, un mage elfe. Rien de surprenant...",
    ("050293FE|Sunthgat.esp", "INFO NAM1", "Everyone was dead. Except for that bastard and me. Continued to work as a mercenary for a while. But someday I couldn't do it anymore."): "Tous mes compagnons ont péri. Tous, sauf ce bâtard et moi. J'ai continué à louer mon épée comme mercenaire pendant un temps, mais un jour, je n'ai plus pu supporter tout ça.",
    ("050293FE|Sunthgat.esp", "INFO NAM1", "Met an old priest up here and chose to assist him. He passed away of old age and I carried on his work."): "J'ai rencontré un vieux prêtre ici même et j'ai choisi de l'aider. Il s'est éteint de vieillesse, et j'ai perpétué son œuvre.",
    ("050293F8|Sunthgat.esp", "DIAL FULL", "What is with Larunon. You don't want to avenge your dead friends?"): "Et qu'en est-il de Larunon ? Vous ne voulez pas venger vos compagnons ?",
    ("050293FF|Sunthgat.esp", "INFO NAM1", "I tried to track him down every now and then, before I settled down here. But he was always gone when i thought I got him."): "J'ai bien essayé de le traquer de temps à autre, avant de m'établir ici. Mais chaque fois que je croyais le tenir, il m'échappait.",
    ("050293FF|Sunthgat.esp", "INFO NAM1", "Last I heard he joined some coven. But I just don't want to fuel this hatred anymore..."): "Aux dernières nouvelles, il aurait rejoint un convent de sorciers. Mais je ne veux plus entretenir cette rancœur...",
    ("05029400|Sunthgat.esp", "INFO NAM1", "I don't know how to feel about this. He was the only other one who could remember our golden days."): "Je ne sais pas trop quoi en penser. C'était le seul autre témoin de nos jours de gloire.",
    ("05029400|Sunthgat.esp", "INFO NAM1", "But I guess all things have to come to an end. Take this sword. It belonged to our leader. Please remember me and also the Band of Kyne."): "Mais toute chose a une fin, je suppose. Prenez cette épée : elle appartenait à notre meneuse. Ne m'oubliez pas, et n'oubliez pas la Bande de Kyne.",
    
    # DIALOGUE & INFO - QUEST 04 (Aberlin & The Rune)
    ("05029404|Sunthgat.esp", "DIAL FULL", "Do you need any help?"): "Avez-vous besoin d'aide ?",
    ("05029407|Sunthgat.esp", "INFO NAM1", "How nice of you to ask. You look like you could indeed help me."): "C'est aimable à vous de demander. Vous avez l'air de quelqu'un qui pourrait effectivement m'être utile.",
    ("05029407|Sunthgat.esp", "INFO NAM1", "I'm looking for a rare spell tome. It contains the knowledge of a rune that triggers an unbridled rage."): "Je cherche un livre de sorts très rare. Il renferme les secrets d'une rune capable de déclencher une fureur incontrôlable.",
    ("05029407|Sunthgat.esp", "INFO NAM1", "There is a rumor that one copy is hidden in Shriekwind Bastion to the south."): "La rumeur veut qu'un exemplaire soit dissimulé au Bastion de Hurlevent, vers le sud.",
    ("05029407|Sunthgat.esp", "INFO NAM1", "But beware, if you intend to recover it. The place is overrun by vampires."): "Mais prenez garde si vous comptez le récupérer : les vampires ont envahi les lieux.",
    ("05029406|Sunthgat.esp", "DIAL FULL", "I got your spell tome."): "J'ai votre livre de sorts.",
    ("05029408|Sunthgat.esp", "INFO NAM1", "So it really existed? That's good to know. Please keep the book and also take this potion as your reward."): "Il existait donc réellement ? C'est bon à savoir. Gardez l'ouvrage, et acceptez cette potion en guise de récompense.",
    
    # QUEST TITLES & OBJECTIVES
    ("0500FED6|Sunthgat.esp", "QUST FULL", "Expected Betrayal"): "Trahison prévisible",
    ("0500FED6|Sunthgat.esp", "QUST NNAM", "Get the crate from <Alias=BanditCamp>"): "Récupérez la caisse à <Alias=BanditCamp>",
    ("0500FED3|Sunthgat.esp", "QUST FULL", "Mammoth Tusk and Skooma"): "Défenses de mammouth et skooma",
    ("0500FED5|Sunthgat.esp", "QUST FULL", "The Clever Craft"): "L'art des mages",
    ("0500FED5|Sunthgat.esp", "QUST NNAM", "Get the spell tome from Shriekwind Bastion"): "Récupérez le livre de sorts au Bastion de Hurlevent",
    ("0500FED5|Sunthgat.esp", "QUST NNAM", "Deliver the spell tome to Aberlin"): "Rapportez le livre de sorts à Aberlin",
    ("0500FED4|Sunthgat.esp", "QUST FULL", "Golden Days"): "Jours de gloire",
    ("0500FED4|Sunthgat.esp", "QUST NNAM", "Try to find Larunon at <Alias=WarlockLair>"): "Retrouvez Larunon à <Alias=WarlockLair>",
}

diffs = []
modified_count = 0

for entry in entries:
    key = (entry.get("form_id"), entry.get("type"), entry.get("original"))
    if key in revisions:
        old_val = entry.get("string")
        new_val = revisions[key]
        if old_val != new_val:
            diffs.append({
                "type": entry.get("type"),
                "form_id": entry.get("form_id"),
                "original": entry.get("original"),
                "old": old_val,
                "new": new_val
            })
            entry["string"] = new_val
            modified_count += 1

print(f"Total entries: {len(entries)}")
print(f"Modified entries: {modified_count}")

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Saved {target_file}")

# Also synchronize Lux - Patch Hub - French if present
lux_patch = Path("data/user/database/french/Lux - Patch Hub - French/Lux - Sunthgat.esp.json")
if lux_patch.exists():
    with open(lux_patch, "r", encoding="utf-8") as f:
        lux_entries = json.load(f)
    lux_mod = False
    for le in lux_entries:
        if le.get("original") == "Clever Man's Cauldron" and le.get("string") != "Le Chaudron de l'érudit":
            le["string"] = "Le Chaudron de l'érudit"
            lux_mod = True
    if lux_mod:
        with open(lux_patch, "w", encoding="utf-8") as f:
            json.dump(lux_entries, f, indent=2, ensure_ascii=False)
        print("Synchronized Lux - Patch Hub - French/Lux - Sunthgat.esp.json")

# Write report
with open("sunthgat_changes_report.json", "w", encoding="utf-8") as f:
    json.dump(diffs, f, indent=2, ensure_ascii=False)
