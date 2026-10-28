"""Scan for stores, taverns, farms, mines, and inner-city locations."""
import json
import os
import re

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

LOCATION_CHECKS = [
    # Solitude
    ("Castle Dour", re.compile(r"\bCastle Dour\b", re.IGNORECASE), "Mornefort"),
    ("Bards College", re.compile(r"\bBards College\b", re.IGNORECASE), "l'Académie des bardes"),
    ("The Winking Skeever", re.compile(r"\b(?:The )?Winking Skeever\b", re.IGNORECASE), "le Ragnard pervers"),
    ("Dainty Sload", re.compile(r"\b(?:The )?Dainty Sload\b", re.IGNORECASE), "le Fol Sload"),
    ("Katla's Farm", re.compile(r"\bKatla's Farm\b", re.IGNORECASE), "la ferme de Katla"),

    # Whiterun
    ("Skyforge", re.compile(r"\bSkyforge\b", re.IGNORECASE), "la Forgeciel"),
    ("Underforge", re.compile(r"\bUnderforge\b", re.IGNORECASE), "la Basse-Forge"),
    ("Gildergreen", re.compile(r"\bGildergreen\b", re.IGNORECASE), "le Vermidor"),
    ("Honningbrew Meadery", re.compile(r"\bHonningbrew(?: Meadery)?\b", re.IGNORECASE), "l'Hydromellerie d'Hydromel de miel"),
    ("The Bannered Mare", re.compile(r"\b(?:The )?Bannered Mare\b", re.IGNORECASE), "la Jument pavoisée"),
    ("Drunken Huntsman", re.compile(r"\b(?:The )?Drunken Huntsman\b", re.IGNORECASE), "le Chasseur ivre"),
    ("Belethor's General Goods", re.compile(r"\bBelethor's(?: General Goods)?\b", re.IGNORECASE), "le Bazar de Belethor"),
    ("Arcadia's Cauldron", re.compile(r"\bArcadia's Cauldron\b", re.IGNORECASE), "le Chaudron d'Arcadia"),
    ("Warmaiden's", re.compile(r"\bWarmaiden's\b", re.IGNORECASE), "la Guerrière"),
    ("Pelagia Farm", re.compile(r"\bPelagia Farm\b", re.IGNORECASE), "la ferme Pelagia"),
    ("Battle-Born Farm", re.compile(r"\bBattle-Born Farm\b", re.IGNORECASE), "la ferme Guerrier-Né"),
    ("Chillfurrow Farm", re.compile(r"\bChillfurrow Farm\b", re.IGNORECASE), "la ferme de Sillonfrais"),

    # Riften
    ("The Bee and Barb", re.compile(r"\b(?:The )?Bee and Barb\b", re.IGNORECASE), "le Dard de l'abeille"),
    ("The Ragged Flagon", re.compile(r"\b(?:The )?Ragged Flagon\b", re.IGNORECASE), "la Cruche percée"),
    ("The Ratway", re.compile(r"\b(?:The )?Ratway\b", re.IGNORECASE), "la Ratière"),
    ("Black-Briar Meadery", re.compile(r"\bBlack-Briar Meadery\b", re.IGNORECASE), "l'Hydromellerie Roncenoir"),
    ("Black-Briar Lodge", re.compile(r"\bBlack-Briar Lodge\b", re.IGNORECASE), "le Manoir Roncenoir"),
    ("Pawned Prawn", re.compile(r"\b(?:The )?Pawned Prawn\b", re.IGNORECASE), "la Crevette gagée"),
    ("Elgrim's Elixirs", re.compile(r"\bElgrim's Elixirs\b", re.IGNORECASE), "les Élixirs d'Elgrim"),
    ("Snow-Shod Farm", re.compile(r"\bSnow-Shod Farm\b", re.IGNORECASE), "la ferme des Chausses-neige"),
    ("Merryfair Farm", re.compile(r"\bMerryfair Farm\b", re.IGNORECASE), "la ferme de Bonheur-champêtre"),

    # Windhelm
    ("Candlehearth Hall", re.compile(r"\bCandlehearth Hall\b", re.IGNORECASE), "le Cœur de chandelle"),
    ("New Gnisis Cornerclub", re.compile(r"\bNew Gnisis(?: Cornerclub)?\b", re.IGNORECASE), "le Club de la Nouvelle Gnisis"),
    ("Sadri's Used Wares", re.compile(r"\bSadri's Used Wares\b", re.IGNORECASE), "les Marchandises d'occasion de Sadri"),
    ("White Phial", re.compile(r"\b(?:The )?White Phial\b", re.IGNORECASE), "la Fiole blanche"),
    ("Aretino Residence", re.compile(r"\bAretino Residence\b", re.IGNORECASE), "la Maison Aretino"),
    ("Brandy-Mug Farm", re.compile(r"\bBrandy-Mug Farm\b", re.IGNORECASE), "la ferme Cruche-à-eau"),
    ("Hlaalu Farm", re.compile(r"\bHlaalu Farm\b", re.IGNORECASE), "la ferme Hlaalu"),
    ("Hollyfrost Farm", re.compile(r"\bHollyfrost Farm\b", re.IGNORECASE), "la ferme de Givre-houx"),

    # Markarth
    ("Silver-Blood Inn", re.compile(r"\bSilver-Blood Inn\b", re.IGNORECASE), "l'Auberge Sang-d'Argent"),
    ("Cidhna Mine", re.compile(r"\bCidhna Mine\b", re.IGNORECASE), "la mine de Cidhna"),
    ("Hag's Cure", re.compile(r"\b(?:The )?Hag's Cure\b", re.IGNORECASE), "les Remèdes de la vieille"),
    ("Arnleif and Sons", re.compile(r"\bArnleif and Sons\b", re.IGNORECASE), "Arnleif et fils"),
    ("Left Hand Mine", re.compile(r"\bLeft Hand Mine\b", re.IGNORECASE), "la mine de Main gauche"),
    ("Kolskeggr Mine", re.compile(r"\bKolskeggr Mine\b", re.IGNORECASE), "la mine de Kolskeggr"),
    ("Salvius Farm", re.compile(r"\bSalvius Farm\b", re.IGNORECASE), "la ferme Salvius"),

    # Dawnstar
    ("Windpeak Inn", re.compile(r"\bWindpeak Inn\b", re.IGNORECASE), "l'Auberge du Pic venteux"),
    ("Iron-Breaker Mine", re.compile(r"\bIron-Breaker Mine\b", re.IGNORECASE), "la mine de Brise-fer"),
    ("Quicksilver Mine", re.compile(r"\bQuicksilver Mine\b", re.IGNORECASE), "la mine de Vif-argent"),

    # Winterhold
    ("The Frozen Hearth", re.compile(r"\b(?:The )?Frozen Hearth\b", re.IGNORECASE), "le Foyer gelé"),
    ("Birna's Oddments", re.compile(r"\bBirna's Oddments\b", re.IGNORECASE), "le Bric-à-brac de Birna"),

    # Falkreath
    ("Dead Man's Drink", re.compile(r"\bDead Man's Drink\b", re.IGNORECASE), "À la boisson du mort"),
    ("Corpselight Farm", re.compile(r"\bCorpselight Farm\b", re.IGNORECASE), "la ferme de Sombre-Lueur"),
    ("Gray Pine Goods", re.compile(r"\bGray Pine Goods\b", re.IGNORECASE), "les Marchandises du Pin gris"),

    # Morthal
    ("Moorside Inn", re.compile(r"\bMoorside Inn\b", re.IGNORECASE), "l'Auberge du Bât-flanc"),
    ("Thaumaturgist's Hut", re.compile(r"\bThaumaturgist's Hut\b", re.IGNORECASE), "la Maison du thaumaturge"),
]

found = []

for root, _, files in os.walk(DB_DIR):
    for f in sorted(files):
        if not f.endswith(".json") or f == "index.json":
            continue
        p = os.path.join(root, f)
        rel = os.path.relpath(p, DB_DIR)
        try:
            with open(p, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except Exception:
            continue
        for idx, row in enumerate(data):
            s = row.get("string", "")
            orig = row.get("original", "")
            t = row.get("type", "")
            status = row.get("status", "")
            if not s or status == "NoTranslationRequired":
                continue

            for name, pat, target in LOCATION_CHECKS:
                if pat.search(s):
                    # Check if text is french
                    if any(w in s.lower() for w in [" le ", " la ", " les ", " de ", " du ", " des ", " un ", " une ", " à ", " a ", " en ", " dans ", " pour "]):
                        if not any(ign in s for ign in [".esp", ".esm", ".dds", ".nif", ".png", "http"]):
                            found.append({
                                "file": rel,
                                "index": idx,
                                "form_id": row.get("form_id", ""),
                                "type": t,
                                "name": name,
                                "target": target,
                                "original": orig[:80],
                                "string": s[:120]
                            })

with open("locations_inner_audit.json", "w", encoding="utf-8") as out:
    json.dump(found, out, indent=2, ensure_ascii=False)

print(f"Inner location findings: {len(found)}")
for item in found:
    print(f"[{item['name']}] -> {item['target']} | {item['file']} idx={item['index']}")
    print(f"   ORIG: {item['original']}")
    print(f"   STR : {item['string']}")
    print("-" * 50)
