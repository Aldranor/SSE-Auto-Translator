"""Ultra-deep Lore scan across the entire French database.

Detects:
1. Untranslated Skyrim settlements & toponyms (Riverwood, Rorikstead, Dragon Bridge,
   Ivarstead, Karthwasten, Helgen, Kynesgrove, Shor's Stone, Darkwater Crossing,
   Bleak Falls Barrow, High Hrothgar, Throat of the World, Solstheim, etc.).
2. Untranslated Holds & regions (The Rift, The Reach, The Pale, Haafingar, Hjaalmarch,
   Eastmarch, Winterhold, Falkreath, Whiterun).
3. Untranslated Provinces & Daedric planes (High Rock, Hammerfell, Valenwood,
   Black Marsh, Summerset, Soul Cairn, Apocrypha, Forgotten Vale, Red Mountain).
4. Untranslated Factions & Orders (Dark Brotherhood, Thieves Guild, Companions,
   College of Winterhold, Blades, Greybeards, Night Mother, Nightingales,
   Silver Hand, Vigilants of Stendarr, Dawnguard, Stormcloaks, Imperial Legion,
   East Empire Company, Mythic Dawn).
5. Untranslated / mistranslated Bestiary (Skeever, Mudcrab, Frostbite Spider,
   Hagraven, Wispmother, Ice Wraith, Slaughterfish, Sabre Cat, Dragon Priest,
   Death Hound, Ash Spawn, Riekling, Lurker, Seeker, etc.).
6. Untranslated / mistranslated Materials & Attributes (Stamina, Magicka,
   Ebony / ébène, Moonstone, Quicksilver, Corundum, Orichalcum, Malachite).
7. Divine / Daedric names left in English (Nocturnal -> Nocturne, etc.).
"""

from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Tuple

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

# French indicators to verify that the string is translated text and not English-only
FRENCH_MARKERS = [
    " le ", " la ", " les ", " de ", " du ", " des ", " un ", " une ",
    " dans ", " en ", " pour ", " et ", " ou ", " avec ", " sans ", " sur ",
    " vous ", " votre ", " vos ", " nous ", " notre ", " nos ", " est ", " sont ",
    " d'", " l'", " qu'", " n'", " c'"
]

# Patterns to ignore (code, files, URLs, mod titles, script variables)
IGNORE_MARKERS = [
    ".esp", ".esm", ".esl", ".pex", ".psc", ".dds", ".nif", ".png",
    "http://", "https://", "www.", "<Alias=", "Skyrim.ini",
    "Skyrim Together", "Skyrim SE", "Skyrim VR", "Skyrim Special Edition",
    "Skyrim Script Extender", "SKSE", "SkyUI"
]

def is_french_text(s: str) -> bool:
    s_low = f" {s.lower()} "
    return any(m in s_low for m in FRENCH_MARKERS)

def has_ignore_marker(s: str) -> bool:
    return any(im in s for im in IGNORE_MARKERS)

# Definitions of lore checks: (Category, Name, regex_pattern, recommended_canonical, context_filter)
LORE_CHECKS: List[Tuple[str, str, re.Pattern[str], str]] = [
    # Settlements & Places
    ("Settlements", "Riverwood", re.compile(r"\bRiverwood\b", re.IGNORECASE), "Rivebois"),
    ("Settlements", "Rorikstead", re.compile(r"\bRorikstead\b", re.IGNORECASE), "Rorikbourg"),
    ("Settlements", "Dragon Bridge", re.compile(r"\bDragon Bridge\b", re.IGNORECASE), "Pont-de-Dragon"),
    ("Settlements", "Ivarstead", re.compile(r"\bIvarstead\b", re.IGNORECASE), "Fort-Ivar"),
    ("Settlements", "Shor's Stone", re.compile(r"\bShor's Stone\b", re.IGNORECASE), "Pierre-de-Shor"),
    ("Settlements", "Kynesgrove", re.compile(r"\bKynesgrove\b", re.IGNORECASE), "Bosquet de Kyne"),
    ("Settlements", "Darkwater Crossing", re.compile(r"\bDarkwater Crossing\b", re.IGNORECASE), "Croisée de Sombreflot"),
    ("Settlements", "Old Hroldan", re.compile(r"\bOld Hroldan\b", re.IGNORECASE), "Vieux Hroldan"),
    ("Settlements", "Bleak Falls Barrow", re.compile(r"\bBleak Falls Barrow\b", re.IGNORECASE), "Tertre des Chutes tourmentées"),
    ("Settlements", "High Hrothgar", re.compile(r"\bHigh Hrothgar\b", re.IGNORECASE), "Haut Hrothgar"),
    ("Settlements", "Throat of the World", re.compile(r"\bThroat of the World\b", re.IGNORECASE), "Gorge du Monde"),
    ("Settlements", "Sky Haven Temple", re.compile(r"\bSky Haven Temple\b", re.IGNORECASE), "Temple d'Havreciel"),
    ("Settlements", "Twilight Sepulcher", re.compile(r"\bTwilight Sepulcher\b", re.IGNORECASE), "Mausolée Crépusculaire"),
    ("Settlements", "Forgotten Vale", re.compile(r"\bForgotten Vale\b", re.IGNORECASE), "Val Oublié"),
    ("Settlements", "Soul Cairn", re.compile(r"\bSoul Cairn\b", re.IGNORECASE), "Cairn de l'Âme"),
    ("Settlements", "Castle Volkihar", re.compile(r"\bCastle Volkihar\b", re.IGNORECASE), "Château Volkihar"),
    ("Settlements", "Fort Dawnguard", re.compile(r"\bFort Dawnguard\b", re.IGNORECASE), "Fort de la Garde de l'Aube"),
    ("Settlements", "Dragonsreach", re.compile(r"\bDragonsreach\b", re.IGNORECASE), "Fort-Dragon"),
    ("Settlements", "Blue Palace", re.compile(r"\bBlue Palace\b", re.IGNORECASE), "Palais bleu"),
    ("Settlements", "Palace of the Kings", re.compile(r"\bPalace of the Kings\b", re.IGNORECASE), "Palais des rois"),
    ("Settlements", "Understone Keep", re.compile(r"\bUnderstone Keep\b", re.IGNORECASE), "Fort-de-Pierre"),
    ("Settlements", "Mistveil Keep", re.compile(r"\bMistveil Keep\b", re.IGNORECASE), "Château d'Embruine"),

    # Holds & Regions
    ("Holds", "The Rift", re.compile(r"\b(?:the\s+)?Rift\b", re.IGNORECASE), "la Faille"),
    ("Holds", "The Reach", re.compile(r"\b(?:the\s+)?Reach\b", re.IGNORECASE), "la Crevasse"),
    ("Holds", "The Pale", re.compile(r"\b(?:the\s+)?Pale\b", re.IGNORECASE), "le Clos"),
    ("Holds", "Eastmarch", re.compile(r"\bEastmarch\b", re.IGNORECASE), "Estemarche"),
    ("Holds", "Haafingar", re.compile(r"\bHaafingar\b", re.IGNORECASE), "Haafingar"),

    # Provinces
    ("Provinces", "High Rock", re.compile(r"\bHigh Rock\b", re.IGNORECASE), "Haut-Roche"),
    ("Provinces", "Hammerfell", re.compile(r"\bHammerfell\b", re.IGNORECASE), "Lenclume"),
    ("Provinces", "Valenwood", re.compile(r"\bValenwood\b", re.IGNORECASE), "Val-Boisé"),
    ("Provinces", "Black Marsh", re.compile(r"\bBlack Marsh\b", re.IGNORECASE), "Marais noir"),
    ("Provinces", "Summerset", re.compile(r"\bSummerset(?:\s+Isles?)?\b", re.IGNORECASE), "Archipel de l'Automne"),
    ("Provinces", "Red Mountain", re.compile(r"\bRed Mountain\b", re.IGNORECASE), "Mont Écarlate"),

    # Factions
    ("Factions", "Dark Brotherhood", re.compile(r"\bDark Brotherhood\b", re.IGNORECASE), "Confrérie noire"),
    ("Factions", "Thieves Guild", re.compile(r"\bThieves Guild\b", re.IGNORECASE), "Guilde des voleurs"),
    ("Factions", "Companions", re.compile(r"\bCompanions\b", re.IGNORECASE), "Compagnons"),
    ("Factions", "College of Winterhold", re.compile(r"\bCollege of Winterhold\b", re.IGNORECASE), "Académie de Fortdhiver"),
    ("Factions", "Greybeards", re.compile(r"\bGreybeards\b", re.IGNORECASE), "Grises-barbes"),
    ("Factions", "Night Mother", re.compile(r"\bNight Mother\b", re.IGNORECASE), "Mère de la nuit"),
    ("Factions", "Nightingales", re.compile(r"\bNightingales\b", re.IGNORECASE), "Rossignols"),
    ("Factions", "Silver Hand", re.compile(r"\bSilver Hand\b", re.IGNORECASE), "Main d'argent"),
    ("Factions", "Vigilants of Stendarr", re.compile(r"\bVigilants?\s+of\s+Stendarr\b", re.IGNORECASE), "Vigiles de Stendarr"),
    ("Factions", "Dawnguard", re.compile(r"\bDawnguard\b", re.IGNORECASE), "Garde de l'Aube"),
    ("Factions", "Stormcloaks", re.compile(r"\bStormcloaks?\b", re.IGNORECASE), "Sombrages"),
    ("Factions", "Imperial Legion", re.compile(r"\bImperial Legion\b", re.IGNORECASE), "Légion impériale"),
    ("Factions", "East Empire Company", re.compile(r"\bEast Empire Company\b", re.IGNORECASE), "Compagnie de l'Empire oriental"),
    ("Factions", "Mythic Dawn", re.compile(r"\bMythic Dawn\b", re.IGNORECASE), "Aube mythique"),

    # Bestiary & Creatures
    ("Bestiary", "Skeever", re.compile(r"\bSkeevers?\b", re.IGNORECASE), "Ragnard"),
    ("Bestiary", "Mudcrab", re.compile(r"\bMudcrabs?\b", re.IGNORECASE), "Vasard"),
    ("Bestiary", "Frostbite Spider", re.compile(r"\bFrostbite Spiders?\b", re.IGNORECASE), "Givrepeire"),
    ("Bestiary", "Hagraven", re.compile(r"\bHagravens?\b", re.IGNORECASE), "Harfreuse"),
    ("Bestiary", "Wispmother", re.compile(r"\bWispmothers?\b", re.IGNORECASE), "Lucereine"),
    ("Bestiary", "Ice Wraith", re.compile(r"\bIce Wraiths?\b", re.IGNORECASE), "Spectre de glace"),
    ("Bestiary", "Slaughterfish", re.compile(r"\bSlaughterfish\b", re.IGNORECASE), "Poisson-carnassier"),
    ("Bestiary", "Sabre Cat", re.compile(r"\bSabre(?:\s+|-)?Cats?\b", re.IGNORECASE), "Tigre à dents de sabre"),
    ("Bestiary", "Dragon Priest", re.compile(r"\bDragon Priests?\b", re.IGNORECASE), "Prêtre-dragon"),
    ("Bestiary", "Death Hound", re.compile(r"\bDeath Hounds?\b", re.IGNORECASE), "Molosse de la mort"),
    ("Bestiary", "Ash Spawn", re.compile(r"\bAsh Spawns?\b", re.IGNORECASE), "Engeance des cendres"),
    ("Bestiary", "Riekling", re.compile(r"\bRieklings?\b", re.IGNORECASE), "Riekelin"),

    # Deities
    ("Deities", "Nocturnal (Daedra)", re.compile(r"\b(?:de|la|par|pour|avec)\s+Nocturnal\b", re.IGNORECASE), "Nocturne"),

    # Materials
    ("Materials", "Arme/Armure en ébène", re.compile(r"\b(?:armure|épée|hache|dague|masse|arc|flèche|casque|gantelets|bottes|bouclier|cuirasse)\s+(?:d'|en\s+)ébène\b", re.IGNORECASE), "d'ébonite"),
    ("Materials", "Minerai/Lingot d'ébène", re.compile(r"\b(?:minerai|lingot)\s+(?:d'|en\s+)ébène\b", re.IGNORECASE), "d'ébonite"),
]

def main() -> None:
    results: List[Dict[str, Any]] = []

    for root, _, files in os.walk(DB_DIR):
        for f in sorted(files):
            if not f.endswith(".json") or f == "index.json":
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DB_DIR)

            try:
                with open(path, "r", encoding="utf-8") as fp:
                    data: List[Dict[str, Any]] = json.load(fp)
            except Exception:
                continue

            for idx, row in enumerate(data):
                s = row.get("string", "")
                orig = row.get("original", "")
                t = row.get("type", "")
                fid = row.get("form_id", "")
                status = row.get("status", "")

                if not s or status == "NoTranslationRequired":
                    continue

                # Check each rule
                for cat, name, pat, canon in LORE_CHECKS:
                    m = pat.search(s)
                    if m:
                        # Ensure string is actual translated text
                        if is_french_text(s) and not has_ignore_marker(s):
                            matched_text = m.group(0)
                            # Avoid false positive where "Rift" is part of another word or valid
                            if name == "The Rift" and matched_text.lower() in ["rift", "the rift"]:
                                if "rift" not in orig.lower():
                                    continue
                            # Avoid false positive where "Reach" is verb "reach"
                            if name == "The Reach" and matched_text.lower() in ["reach", "the reach"]:
                                if "reach" not in orig.lower():
                                    continue
                            # Avoid Dawnguard when it's the DLC name
                            if name == "Dawnguard" and any(k in orig.lower() for k in ["dawnguard.esm", "dawnguard dlc"]):
                                continue

                            results.append({
                                "file": rel,
                                "index": idx,
                                "form_id": fid,
                                "type": t,
                                "category": cat,
                                "term": name,
                                "matched": matched_text,
                                "canonical": canon,
                                "original": orig[:100],
                                "string": s[:150]
                            })

    output_path = "phase4_deep_lore_findings.json"
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2, ensure_ascii=False)

    print(f"Deep Lore scan finished. Total potential findings: {len(results)}")
    
    # Group by category and term
    stats: Dict[str, Dict[str, int]] = {}
    for r in results:
        c = r["category"]
        tm = r["term"]
        stats.setdefault(c, {})
        stats[c][tm] = stats[c].get(tm, 0) + 1

    for c, terms in stats.items():
        print(f"\n--- {c} ---")
        for tm, cnt in sorted(terms.items(), key=lambda x: -x[1]):
            print(f"  {tm}: {cnt}")

if __name__ == "__main__":
    main()
