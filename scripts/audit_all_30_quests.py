import json
import re

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

# Load CC database if possible
cc_path = "data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json"
cc_data = json.load(open(cc_path, encoding="utf-8"))
cc_lookup = {}
for e in cc_data:
    orig = e.get("original")
    trad = e.get("string")
    if orig and trad:
        cc_lookup[orig] = trad

print(f"CC lookup loaded: {len(cc_lookup)} strings")

issues = []

# Known official French CC Quest Titles:
official_titles = {
    "A Dying Wish": "Dernières volontés",
    "Ghosts of the Tribunal": "Fantômes du Tribunal",
    "Vile Whispers": "Vils murmures",
    "Let Sleeping Wolves Lie": "Le sommeil des loups",
    "The Heart of Dibella": "Le Cœur de Dibella",
    "Blood in the Water": "Du sang dans l'eau",
    "Unholy Vigil": "Veillée impie",
    "Beyond the Grave": "Par-delà la tombe",
    "Crypt of the Heart": "La crypte du Cœur",
    "Legends Lost": "Légendes perdues",
    "Battle of the Champions": "Le combat des champions",
    "The Rising Dead": "Morts d'outre-tombe",
    "Myrwatch": "Myrwatch",
    "Necromantic Arts": "Arts nécromantiques",
    "Put A Fork In It": "Un bon coup de fourchette",
    "Caught in a Web": "Pris dans la toile",
    "Horse Whisperer": "L'homme qui murmurait à l'oreille des chevaux",
    "Guests for Dinner": "Des convives au dîner",
    "The Cause": "La Cause",
    "The Edge of Ruin": "Au bord de la ruine",
    "Gift of Kynareth": "Le don de Kynareth",
    "Balance of Power": "L'équilibre des forces", # ou Équilibre du pouvoir
    "Hendraheim": "Hendraheim",
    "If I had a Hammer": "Si j'avais un marteau",
    "Pets of Skyrim": "Animaux sauvages de Bordeciel", # ou Familiers de Bordeciel
    "Beneath Bronze Waters": "Sous les flots de bronze",
    "Relics of the Crusader": "Reliques du Divin Croisé",
    "A Soul Divided": "Âme divisée",
    "Siege on the Dragon Cult": "Le siège du culte des dragons",
    "In the Shadows": "Dans l'ombre"
}

for idx, e in enumerate(data):
    orig = e.get("original") or ""
    trad = e.get("string") or ""
    qtype = e.get("type")
    fid = e.get("form_id")
    edid = e.get("editor_id")
    stage = e.get("index")

    # Quest titles
    if qtype == "QUST FULL":
        if orig in official_titles and trad != official_titles[orig]:
            issues.append({
                "idx": idx,
                "type": "QUEST_TITLE",
                "orig": orig,
                "curr": trad,
                "target": official_titles[orig],
                "reason": "Titre officiel Bethesda non respecté"
            })
        continue

    # Objectives (QUST NNAM)
    if qtype == "QUST NNAM":
        # Check if CC lookup has an exact match
        if orig in cc_lookup:
            cc_t = cc_lookup[orig]
            # normalize punctuation at end
            if trad != cc_t:
                # check if difference is substantial
                if trad.rstrip('. ') != cc_t.rstrip('. '):
                    issues.append({
                        "idx": idx,
                        "type": "OBJECTIVE_DIFF_CC",
                        "orig": orig,
                        "curr": trad,
                        "target": cc_t,
                        "reason": "Différence substantielle avec la version officielle CC"
                    })
        # Check for trailing periods in NNAM if inconsistent (Skyrim vanilla NNAM usually has no final period, but CC often has one)
        # Let's check common typos
        if "coeur" in trad.lower() and "cœur" not in trad.lower():
            # Typo ligature œ
            pass

    # Stage descriptions (QUST CNAM)
    if qtype == "QUST CNAM":
        if not trad or e.get("status") == "TranslationRequired":
            issues.append({
                "idx": idx,
                "type": "MISSING_CNAM",
                "orig": orig,
                "curr": trad,
                "target": "",
                "reason": "Description de quête manquante"
            })
        elif orig in cc_lookup:
            cc_t = cc_lookup[orig]
            if trad != cc_t:
                issues.append({
                    "idx": idx,
                    "type": "CNAM_DIFF_CC",
                    "orig": orig,
                    "curr": trad,
                    "target": cc_t,
                    "reason": "Texte différent du CC officiel"
                })

print(f"Total issues flagged: {len(issues)}")
for i in issues:
    print(f"[{i['type']}] #{i['idx']} | Orig: {i['orig'][:40]} | Curr: {repr(i['curr'])} -> Target: {repr(i['target'])}")
