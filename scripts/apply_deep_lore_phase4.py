"""Phase 4 Deep Lore Extension: Exhaustive Lore & Canonical Glossary fixes.

Applies:
1. Hjertesten Hall: translates 10 occurrences of Ivarstead -> Fort-Ivar,
   and skeevers -> ragnards.
2. Bestiary loot: skeever meat -> Viande de ragnard crue.
3. Materials: remaining ebony -> ébonite.
4. Factions & Gods:
   - Dawnguard / Dragonborn containers in Amulets of Skyrim
   - Daedric Princes: Nocturnal -> Nocturne, Boethiah -> Boéthia,
     Meridia -> Méridia, Peryite -> Péryite, Zenithar -> Zénithar
   - Panthéon de Bretagne -> Panthéon breton
   - Hagraven -> harfreuse, Riekling -> Riekelin, companions -> compagnons
   - Summerset -> Archipel de l'Automne
   - Settlements: Darkwater Crossing -> Croisée de Sombreflot,
     Kynesgrove -> Bosquet de Kyne
"""

from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Tuple

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

# List of exact fixes: (filename_contains_lower, index, expected_substr_orig, replace_map, new_status)
# replace_map is a list of (old_substring, new_substring)
DETAILED_LORE_FIXES: List[Tuple[str, int, str, List[Tuple[str, str]], str | None]] = [
    # 1. Hjertesten Hall (dt_hjertesten hall.esp.json)
    ("dt_hjertesten hall.esp.json", 682, "Ivarstead", [("à Ivarstead", "à Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 684, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1067, "skeevers", [("des skeevers", "des ragnards")], None),
    ("dt_hjertesten hall.esp.json", 1138, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1249, "Ivarstead", [("Ivarstead", "Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1600, "Skeevers", [("Les skeevers", "Les ragnards")], None),
    ("dt_hjertesten hall.esp.json", 1705, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1707, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1708, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1709, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1714, "Ivarstead", [("à Ivarstead", "à Fort-Ivar")], None),
    ("dt_hjertesten hall.esp.json", 1733, "Ivarstead", [("d'Ivarstead", "de Fort-Ivar")], None),

    # 2. Bestiaire Loot & Addon
    ("skeever_loot.json.json", 1, "skeever", [("Viande de skeever crue", "Viande de ragnard crue")], None),
    ("gremlin.json.json", 1, "Summerset", [("Thalendor du Summerset", "Thalendor de l'Archipel de l'Automne")], None),
    ("shade daedra.json.json", 1, "Nocturnal", [
        ("associé au royaume de Nocturnal de Evergloam", "associé au domaine de Nocturne, le Crépuscule éternel")
    ], None),
    ("wraith-of-crows.json.json", 1, "Nocturnal", [("servant de Nocturnal", "serviteur de Nocturne")], None),
    ("auroran guardian.json.json", 1, "Meridia", [("Lumière de Meridia", "Lumière de Méridia")], None),
    ("auroran valkyrie.json.json", 1, "Meridia", [("de Meridia", "de Méridia")], None),
    ("auroran.json.json", 1, "Meridia", [("plan de Meridia", "plan de Méridia")], None),
    ("umaril the unfeathered.json.json", 1, "Meridia", [("champion de Meridia", "champion de Méridia")], None),
    ("ascended servitor.json.json", 1, "Meridia", [("service envers Meridia", "service envers Méridia")], None),

    # 3. Materials (Ebony -> Ébonite)
    ("fanatical enemies.esp.json", 3865, "ebony", [("grande épée en ébène normale", "grande épée d'ébonite normale")], None),
    ("dbm_inigo_patch.esp.json", 10, "ebony", [("Un arc en ébène", "Un arc d'ébonite")], None),
    ("nolvus awakening custom outfits.esp.json", 30, "Ebony", [("Cuirasse d'ébène", "Cuirasse d'ébonite")], None),

    # 4. Containers in Amulets of Skyrim
    ("sl01amuletsskyrim.esp.json", 584, "Dawnguard", [("Amulettes de Dawnguard", "Coffre d'amulettes de la Garde de l'Aube")], None),
    ("sl01amuletsskyrim.esp.json", 585, "Dragonborn", [("Amulettes de Dragonborn", "Coffre d'amulettes de l'Enfant de dragon")], None),

    # 5. Settlements in NPCModTowns
    ("npcmodtowns.esp.json", 67, "Darkwater Crossing", [("visitez Darkwater Crossing", "visitez la Croisée de Sombreflot")], None),
    ("npcmodtowns.esp.json", 110, "Kynesgrove", [("direction de Kynesgrove", "direction du Bosquet de Kyne")], None),

    # 6. BALLS Chapter 1 Lore
    ("balls - chapter 1.esp.json", 143, "Bretony", [
        ("Panthéon de Bretagne, Zénithar", "Panthéon breton, Zénithar")
    ], None),
    ("balls - chapter 1.esp.json", 94, "Nocturnal", [
        ("Nocturnal, le Voleur de l'Ombre", "Nocturne, voleuse de l'ombre")
    ], None),
    ("balls - chapter 1.esp.json", 73, "Meridia", [
        ("Meridia, la Dame Lumineuse", "Méridia, la Dame lumineuse")
    ], None),
    ("balls - chapter 1.esp.json", 22, "Peryite", [
        ("Peryite est le Prince Daedra", "Péryite est le Prince Daedra")
    ], None),
    ("balls - chapter 1.esp.json", 105, "Zenithar", [
        ("dieu impérial du commerce Zenithar", "dieu impérial du commerce Zénithar")
    ], None),

    # 7. Resources - The Great Cities (Boethiah & Nocturnal)
    ("resources - the great cities.esp.json", 62, "Boethiah", [("Honneur à Boethiah !", "Honneur à Boéthia !")], None),
    ("resources - the great cities.esp.json", 185, "Boethiah", [("âme à Boethiah !", "âme à Boéthia !")], None),
    ("resources - the great cities.esp.json", 218, "Boethiah", [("plaire à Boethiah !", "plaire à Boéthia !")], None),
    ("resources - the great cities.esp.json", 233, "Nocturnal", [
        ("béni par Nocturnal, n'est-ce pas ?", "béni par Nocturne, n'est-ce pas ?")
    ], None),

    # 8. 3DNPC Lore
    ("3dnpc.esp.json", 22584, "Nocturnal", [("Nocturnal offrit la richesse", "Nocturne offrit la richesse")], None),
    ("3dnpc.esp.json", 25096, "The Pale", [("(the Pale) ", "")], None),
    ("3dnpc.esp.json", 31184, "Riekling", [("serai un Riekling", "serai un Riekelin")], None),

    # 9. CCQuest Experience Patch (Hagraven)
    ("ccquest - experience patch.esp.json", 1559, "hagraven", [
        ("sur un autel hagraven", "sur un autel de harfreuse")
    ], None),

    # 10. Quick Light Followers
    ("quicklightforfollowers.esp.json", 13, "companions", [
        ("pour les companions", "pour les compagnons")
    ], None),

    # 11. Unslaad (Nocturnal)
    ("unslaad.esm.json", 1237, "Nocturnal", [
        ("manteau de Nocturnal", "manteau de Nocturne")
    ], None),

    # 12. Peryite / Péryite
    ("chevalier's armor set.esp.json", 29, "Peryite", [
        ("chevalier de Peryite", "chevalier de Péryite")
    ], None),
    ("skyshards.esp.json", 298, "Peryite", [
        ("serviteur de Peryite", "serviteur de Péryite")
    ], None),
]


def apply_deep_lore() -> None:
    """Apply deep Lore fixes across database files."""
    modified_files = 0
    total_fixes = 0

    # Build lookup
    lookup: Dict[Tuple[str, int], Tuple[str, List[Tuple[str, str]], str | None]] = {}
    for fn, idx, orig_sub, reps, stat in DETAILED_LORE_FIXES:
        lookup[(fn.lower(), idx)] = (orig_sub, reps, stat)

    for root, _, files in os.walk(DB_DIR):
        for f in sorted(files):
            if not f.endswith(".json") or f == "index.json":
                continue
            path = os.path.join(root, f)
            fn_lower = f.lower()

            try:
                with open(path, "r", encoding="utf-8") as fp:
                    data: List[Dict[str, Any]] = json.load(fp)
            except Exception as e:
                print(f"Error loading {path}: {e}")
                continue

            file_modified = False

            for idx, row in enumerate(data):
                key = (fn_lower, idx)
                if key in lookup:
                    orig_sub, reps, new_stat = lookup[key]
                    orig = row.get("original", "")
                    s = row.get("string", "")

                    if orig_sub.lower() in orig.lower():
                        new_s = s
                        for old_txt, new_txt in reps:
                            new_s = new_s.replace(old_txt, new_txt)

                        if new_s != s:
                            row["string"] = new_s
                            file_modified = True
                            total_fixes += 1

                        if new_stat is not None and row.get("status") != new_stat:
                            row["status"] = new_stat
                            file_modified = True

            if file_modified:
                try:
                    with open(path, "w", encoding="utf-8", newline="\n") as fp:
                        json.dump(data, fp, indent=2, ensure_ascii=False)
                    modified_files += 1
                    print(f"Updated {f}")
                except Exception as e:
                    print(f"Error writing {path}: {e}")

    print("=" * 60)
    print("PHASE 4 DEEP LORE EXTENSION COMPLETE")
    print(f"Total targeted Lore fixes applied: {total_fixes}")
    print(f"Total files updated:              {modified_files}")
    print("=" * 60)


if __name__ == "__main__":
    apply_deep_lore()
