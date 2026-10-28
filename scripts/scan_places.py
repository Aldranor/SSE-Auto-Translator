"""Exhaustive scan for Skyrim / Solstheim / Cyrodiil place names."""
import json
import os
import re

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

PLACE_NAMES = [
    # Iconic Dungeons & Ruins
    ("Blackreach", re.compile(r"\bBlackreach\b", re.IGNORECASE), "Griffenoire"),
    ("Bleak Falls Barrow", re.compile(r"\bBleak Falls(?: Barrow)?\b", re.IGNORECASE), "Tertre des Chutes tourmentées"),
    ("Labyrinthian", re.compile(r"\bLabyrinthian\b", re.IGNORECASE), "le Labyrinthe"),
    ("High Gate Ruins", re.compile(r"\bHigh Gate Ruins\b", re.IGNORECASE), "Ruines de la Porte haute"),
    ("Silent Moons Camp", re.compile(r"\bSilent Moons(?: Camp)?\b", re.IGNORECASE), "Camp des Lunes silencieuses"),
    ("Halted Stream Camp", re.compile(r"\bHalted Stream(?: Camp)?\b", re.IGNORECASE), "Camp du Ruisseau blanc"),
    ("Redoran's Retreat", re.compile(r"\bRedoran's Retreat\b", re.IGNORECASE), "Retraite de Rédoran"),
    ("Brittleshin Pass", re.compile(r"\bBrittleshin Pass\b", re.IGNORECASE), "Passe de Brise-tibia"),
    ("Fellglow Keep", re.compile(r"\bFellglow Keep\b", re.IGNORECASE), "Donjon de Ronflot"),
    ("Fort Sungard", re.compile(r"\bFort Sungard\b", re.IGNORECASE), "Fort Gardesoleil"),
    ("Fort Snowhawk", re.compile(r"\bFort Snowhawk\b", re.IGNORECASE), "Fort Busard"),
    ("Broken Tower Redoubt", re.compile(r"\bBroken Tower(?: Redoubt)?\b", re.IGNORECASE), "Redoute de la Tour brisée"),
    ("Red Eagle Redoubt", re.compile(r"\bRed Eagle Redoubt\b", re.IGNORECASE), "Redoute de l'Aigle carmin"),
    ("Sundered Towers", re.compile(r"\bSundered Towers\b", re.IGNORECASE), "Tours scindées"),
    ("Cradlecrush Rock", re.compile(r"\bCradlecrush Rock\b", re.IGNORECASE), "Roc du Berceau brisé"),
    ("Serpent's Bluff", re.compile(r"\bSerpent's Bluff\b", re.IGNORECASE), "Redoute du Serpent"),
    ("Deepwood Redoubt", re.compile(r"\bDeepwood Redoubt\b", re.IGNORECASE), "Redoute de Profondebois"),
    ("Hag's End", re.compile(r"\bHag's End\b", re.IGNORECASE), "Fin d'Harfreuse"),
    ("Karthspire", re.compile(r"\bKarthspire\b", re.IGNORECASE), "la Flèche de Karth"),
    ("Reachwater Rock", re.compile(r"\bReachwater Rock\b", re.IGNORECASE), "Roc de l'Eau-de-Crevasse"),
    ("Geirmund's Hall", re.compile(r"\bGeirmund's Hall\b", re.IGNORECASE), "Manoir de Geirmund"),
    ("Shroud Hearth Barrow", re.compile(r"\bShroud Hearth(?: Barrow)?\b", re.IGNORECASE), "Tertre du Voile funéraire"),
    ("Hillgrund's Tomb", re.compile(r"\bHillgrund's Tomb\b", re.IGNORECASE), "Tombeau d'Hillgrund"),
    ("Tower of Mzark", re.compile(r"\bTower of Mzark\b", re.IGNORECASE), "Tour de Mzark"),
    ("Chillwind Depths", re.compile(r"\bChillwind Depths\b", re.IGNORECASE), "Profondeurs de Vent-froid"),
    ("Haemar's Shame", re.compile(r"\bHaemar's Shame\b", re.IGNORECASE), "Honte de Haemar"),
    ("Halldir's Cairn", re.compile(r"\bHalldir's Cairn\b", re.IGNORECASE), "Cairn d'Halldir"),
    ("Hob's Fall Cave", re.compile(r"\bHob's Fall(?: Cave)?\b", re.IGNORECASE), "Grotte de Hob"),
    ("Liar's Retreat", re.compile(r"\bLiar's Retreat\b", re.IGNORECASE), "Repaire des menteurs"),
    ("Lost Knife Hideout", re.compile(r"\bLost Knife(?: Hideout)?\b", re.IGNORECASE), "Repaire de Couteauperdu"),
    ("Movarth's Lair", re.compile(r"\bMovarth's Lair\b", re.IGNORECASE), "Repaire de Movarth"),
    ("Rebel's Cairn", re.compile(r"\bRebel's Cairn\b", re.IGNORECASE), "Cairn du Rebelle"),
    ("Shimmermist Cave", re.compile(r"\bShimmermist(?: Cave)?\b", re.IGNORECASE), "Grotte du Voile scintillant"),
    ("Sightless Pit", re.compile(r"\bSightless Pit\b", re.IGNORECASE), "la Fosse aveugle"),
    ("Snapleg Cave", re.compile(r"\bSnapleg(?: Cave)?\b", re.IGNORECASE), "Grotte de Brise-jambe"),
    ("Swindler's Den", re.compile(r"\bSwindler's Den\b", re.IGNORECASE), "Repaire d'escrocs"),
    ("Treva's Watch", re.compile(r"\bTreva's Watch\b", re.IGNORECASE), "Guet de Treva"),
    ("White River Watch", re.compile(r"\bWhite River Watch\b", re.IGNORECASE), "Guet de la Rivière blanche"),
    ("Wolfskull Cave", re.compile(r"\bWolfskull(?: Cave)?\b", re.IGNORECASE), "Grotte du Crâne de loup"),
    ("Yngol Barrow", re.compile(r"\bYngol Barrow\b", re.IGNORECASE), "Tertre d'Yngol"),

    # Taverns & Shops
    ("The Bannered Mare", re.compile(r"\b(?:The )?Bannered Mare\b", re.IGNORECASE), "la Jument pavoisée"),
    ("Sleeping Giant Inn", re.compile(r"\bSleeping Giant(?: Inn)?\b", re.IGNORECASE), "l'Auberge du Géant endormi"),
    ("Winking Skeever", re.compile(r"\b(?:The )?Winking Skeever\b", re.IGNORECASE), "le Ragnard pervers"),
    ("Candlehearth Hall", re.compile(r"\bCandlehearth Hall\b", re.IGNORECASE), "le Cœur de chandelle"),
    ("Bee and Barb", re.compile(r"\b(?:The )?Bee and Barb\b", re.IGNORECASE), "le Dard de l'abeille"),
    ("Silver-Blood Inn", re.compile(r"\bSilver-Blood Inn\b", re.IGNORECASE), "l'Auberge Sang-d'Argent"),
    ("Frozen Hearth", re.compile(r"\b(?:The )?Frozen Hearth\b", re.IGNORECASE), "le Foyer gelé"),
    ("Windpeak Inn", re.compile(r"\bWindpeak Inn\b", re.IGNORECASE), "l'Auberge du Pic venteux"),
    ("Moorside Inn", re.compile(r"\bMoorside Inn\b", re.IGNORECASE), "l'Auberge du Bât-flanc"),
    ("Vilemyr Inn", re.compile(r"\bVilemyr Inn\b", re.IGNORECASE), "l'Auberge de Vilemyr"),
    ("Nightgate Inn", re.compile(r"\bNightgate Inn\b", re.IGNORECASE), "l'Auberge de la Porte de la nuit"),
    ("Dead Man's Drink", re.compile(r"\bDead Man's Drink\b", re.IGNORECASE), "À la boisson du mort"),
    ("Four Shields Tavern", re.compile(r"\bFour Shields(?: Tavern)?\b", re.IGNORECASE), "l'Auberge des Quatre boucliers"),
    ("Frostfruit Inn", re.compile(r"\bFrostfruit Inn\b", re.IGNORECASE), "l'Auberge du Fruit givré"),
    ("Ragged Flagon", re.compile(r"\b(?:The )?Ragged Flagon\b", re.IGNORECASE), "la Cruche percée"),
    ("The Ratway", re.compile(r"\b(?:The )?Ratway\b", re.IGNORECASE), "la Ratière"),
    ("Warmaiden's", re.compile(r"\bWarmaiden's\b", re.IGNORECASE), "la Guerrière"),
    ("Belethor's General Goods", re.compile(r"\bBelethor's(?: General Goods)?\b", re.IGNORECASE), "le Bazar de Belethor"),
    ("Arcadia's Cauldron", re.compile(r"\bArcadia's Cauldron\b", re.IGNORECASE), "le Chaudron d'Arcadia"),
    ("Drunken Huntsman", re.compile(r"\b(?:The )?Drunken Huntsman\b", re.IGNORECASE), "le Chasseur ivre"),
    ("White Phial", re.compile(r"\b(?:The )?White Phial\b", re.IGNORECASE), "la Fiole blanche"),
    ("Pawned Prawn", re.compile(r"\b(?:The )?Pawned Prawn\b", re.IGNORECASE), "la Crevette gagée"),
    ("Elgrim's Elixirs", re.compile(r"\bElgrim's Elixirs\b", re.IGNORECASE), "les Élixirs d'Elgrim"),
    ("Hag's Cure", re.compile(r"\b(?:The )?Hag's Cure\b", re.IGNORECASE), "les Remèdes de la vieille"),
    ("Breezehome", re.compile(r"\bBreezehome\b", re.IGNORECASE), "Douce Brise"),
    ("Proudspire Manor", re.compile(r"\bProudspire Manor\b", re.IGNORECASE), "le Manoir de Hauteflèche"),
    ("Honeyside", re.compile(r"\bHoneyside\b", re.IGNORECASE), "Rucheline"),
    ("Vlindrel Hall", re.compile(r"\bVlindrel Hall\b", re.IGNORECASE), "le Manoir de Vlindrel"),
    ("Severin Manor", re.compile(r"\bSeverin Manor\b", re.IGNORECASE), "le Manoir Severin"),
    ("Lakeview Manor", re.compile(r"\bLakeview Manor\b", re.IGNORECASE), "le Manoir du Lac"),
    ("Windstad Manor", re.compile(r"\bWindstad Manor\b", re.IGNORECASE), "le Manoir Bourduvent"),
    ("Heljarchen Hall", re.compile(r"\bHeljarchen Hall\b", re.IGNORECASE), "le Manoir d'Heljarchen"),

    # Geographic Features & Solstheim
    ("Raven Rock", re.compile(r"\bRaven Rock\b", re.IGNORECASE), "Corberoc"),
    ("Fort Frostmoth", re.compile(r"\bFort Frostmoth\b", re.IGNORECASE), "Fort Molène"),
    ("Castle Karstaag", re.compile(r"\bCastle Karstaag\b", re.IGNORECASE), "Château Karstaag"),
    ("Temple of Miraak", re.compile(r"\bTemple of Miraak\b", re.IGNORECASE), "Temple de Miraak"),
    ("Thirsk Mead Hall", re.compile(r"\bThirsk(?: Mead Hall)?\b", re.IGNORECASE), "Hydromellerie de Thirsk"),
    ("Sea of Ghosts", re.compile(r"\bSea of Ghosts\b", re.IGNORECASE), "la Mer des Fantômes"),
    ("Jerall Mountains", re.compile(r"\bJerall Mountains\b", re.IGNORECASE), "les Montagnes de Jerall"),
    ("Velothi Mountains", re.compile(r"\bVelothi Mountains\b", re.IGNORECASE), "les Monts Vélothi"),
    ("Dragontail Mountains", re.compile(r"\bDragontail Mountains\b", re.IGNORECASE), "les Montagnes de la Queue du dragon"),
    ("Pale Pass", re.compile(r"\bPale Pass\b", re.IGNORECASE), "le Col pâle"),
    ("Imperial City", re.compile(r"\bImperial City\b", re.IGNORECASE), "la Cité impériale"),
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

            for name, pat, target in PLACE_NAMES:
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

with open("places_audit.json", "w", encoding="utf-8") as out:
    json.dump(found, out, indent=2, ensure_ascii=False)

print(f"Places findings: {len(found)}")
for item in found:
    print(f"[{item['name']}] -> {item['target']} | {item['file']} idx={item['index']}")
    print(f"   ORIG: {item['original']}")
    print(f"   STR : {item['string']}")
    print("-" * 50)
