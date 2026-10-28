"""Phase 4 Clean: Lore Skyrim and Canonical Glossary Application Script.

Applies canonical Lore terminology across the entire French translation DB:
1. Systematic replacement of accented "Bréton(ne)(s)" with "Breton(ne)(s)".
2. Correction of untranslated/mismatched Skyrim toponyms (Whiterun, Winterhold,
   Falkreath, Riften, Windhelm, Dawnstar, Hammerfell, Valenwood, etc.).
3. Correction of fundamental Skyrim attributes (Stamina -> Vigueur, Mana -> Magie).
4. Correction of equipment materials (Arme/Armure en ébène -> d'ébonite).
5. Proper handling of internal quest scenes.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Tuple


DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

# 1. Breton regex replacements (preserving case)
BRETON_REPLACEMENTS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bBrétonnes\b"), "Bretonnes"),
    (re.compile(r"\bbrétonnes\b"), "bretonnes"),
    (re.compile(r"\bBrétonne\b"), "Bretonne"),
    (re.compile(r"\bbrétonne\b"), "bretonne"),
    (re.compile(r"\bBrétons\b"), "Bretons"),
    (re.compile(r"\bbrétons\b"), "bretons"),
    (re.compile(r"\bBréton\b"), "Breton"),
    (re.compile(r"\bbréton\b"), "breton"),
]

# 2. Specific file & index modifications for targeted Lore fixes
# Format: (relative_path_suffix_lowercase, index, expected_orig_sub, new_string, new_status)
TARGETED_LORE_FIXES: List[Tuple[str, int, str, str, str | None]] = [
    # Toponyms & Quest Lore
    ("3dnpc.esp.json", 17166, "Falkreath", "Depuis le jour où vous êtes venu à l'échoppe de Lod à Épervine, je vous ai aimé", None),
    ("ashlander apparel.esp.json", 46, "Riften", (
        "<font face='$HandwrittenFont'><p align=\"center\">\n"
        "Ce livre répertorie différentes méthodes de teinture naturelle des tissus en utilisant la flore trouvée à travers Tamriel.\n"
        "</p>\n"
        "[pagebreak]\n"
        "Pour tisser des tissus à partir de fibres végétales :\n"
        "3 coton toundra ou 3 blé\n\n"
        "Rouge:\n"
        "3 fleurs rouges des montagnes – faciles à trouver le long des sentiers de montagne et à travers la Faille\n\n"
        "Noir:\n"
        "2 Charbon de bois - feux de camp, ou acheté auprès de marchands et de forgerons\n\n"
        "Bleu:\n"
        "3 fleurs des Montagnes Bleues - plus communes dans le Nord ou à travers la Faille - beaucoup poussent sous le promontoire et l'arche maritime de Solitude\n\n"
        "Vert:\n"
        "3 Mousse suspendue – poussera dans les zones fraîches et humides, dans les grottes et à travers le Bief\n\n"
        "Jaune:\n"
        "2 Langues de dragon – poussent en abondance autour des sources chaudes entre Faillaise et Vendeaume\n\n"
        "Violet:\n"
        "2 Morelles noires - beaucoup trouvées dans Solitude, dans les cimetières et dans les régions marécageuses autour de Morthal</font>"
    ), None),
    ("balls - chapter 1.esp.json", 46, "Hammerfell", "-- Panthéon Rougegarde, Leki --\nLeki, la Sainte de l'Épée Spirituelle, est la déesse guerrière de Lenclume, fille du Grand Père. Les Rougegardes lui ont dédié de nombreux sanctuaires dans les déserts.", None),
    ("balls - chapter 1.esp.json", 115, "Hammerfell", "-- Panthéon Bosmeri, Ius --\nIus l'Extrêmement Agité est le Dieu des Animaux dans Lenclume et dans d'autres régions du sud-ouest de Tamriel. Il est généralement représenté comme un bœuf difforme.", None),
    ("apachii_divineelegancestore.esm.json", 1157, "Falkreath", "Épervine", None),
    ("undeath.esp.json", 636, "Falkreath", "Le maître nécromancien Antioche cherche à utiliser le tome volé aux Vigiles de Stendarr afin de devenir une liche. Il est déjà parti pour les montagnes de la Queue du Dragon à la recherche de quelque chose, mais a envoyé certains de ses partisans détruire un temple d'Arkay dans la châtellerie d'Épervine et prendre le cœur d'un de ses prêtres. Je devrais me dépêcher et les arrêter.", None),
    ("undeathfixes.esp.json", 362, "Falkreath", "Le maître nécromancien Antioche cherche à utiliser le tome volé aux Vigiles de Stendarr afin de devenir une liche. Il est déjà parti pour les montagnes de la Queue du Dragon à la recherche de quelque chose, mais a envoyé certains de ses partisans détruire un temple d'Arkay dans la châtellerie d'Épervine et prendre le cœur d'un de ses prêtres. Je devrais me dépêcher et les arrêter.", None),
    ("isd_ravensbeak.esp.json", 25, "Windhelm", (
        '<font face="$HandwrittenFont">\n'
        "J'ai demandé à mon assistant de vous remettre cet objet en mon nom. Je pense qu'il pourrait s'agir d'un artefact important relatif aux cultures des anciens peuples d'Estemarche.\n\n"
        "À première vue, il s'agit d'un dispositif de mesure du temps. Au centre se trouve une face circulaire représentant une image de Magnus en haut et un ciel nocturne étoilé en bas. Un cadran circulaire tourne autour de cette face intérieure, mais seulement lorsqu'on le possède.\n\n"
        "Il est décevant de constater que le cadran ne suit pas le temps. Il tourne périodiquement en boucle, sans utilité apparente, ce qui le fait ressembler davantage à une matraque qu'à une montre. Une lueur luminescente, peut-être magique, pulse en synchronisation avec la rotation du cadran, apparaissant lorsqu'il passe sur la partie inférieure du demi-cercle bleu. Observez vous-même ce comportement.\n\n"
        "Avant de procéder au démontage de cet appareil pour en examiner les entrailles, je vous demande de l'analyser d'un point de vue magique. De plus, l'endroit où il a été découvert pour la première fois pourrait vous être utile. J'ai trouvé cet objet alors que je me rendais dans les diverses ruines situées au sud de Vendeaume, dans la partie méridionale d'Estemarche. Il se trouvait dans la zone située directement au nord de la Pierre de l'Atronach et juste au sud de ce que je crois être des ruines nordiques, elles-mêmes situées sur un plateau surélevé. Je n'ai pas pu fouiller complètement la zone à la recherche d'autres découvertes significatives avant d'être attaqué par un dragon, qui semble résider dans la région. Si vous décidez de vous rendre vous-même dans la région pour faciliter votre analyse, soyez prudent.\n\n"
        "Vous pouvez utiliser ce livre comme bon vous semble, ajouter des notes, noter des analyses, tout ce que vous jugerez utile.\n"
        "</font>\n"
    ), None),
    ("legacyofthedragonborn.esm.json", 4628, "Falkreath", None, None),  # Will be handled via text replacement within string
    ("lucien.esp.json", 1502, "Riften", "Faillaise m'a toujours rendu nerveux. On reste longtemps ?", None),
    ("lucien.esp.json", 5494, "Winterhold", "Lucien : Académie de Fortdhiver", None),
    ("man those borders!.esp.json", 6, "Falkreath", "Porte nord d'Épervine", None),
    ("nolvus awakening combat scaling overhaul - enemy level mult.esp.json", 6232, "Falkreath", "Seigneur d'Épervine", None),
    ("nolvus awakening combat scaling overhaul - enemy level.esp.json", 3212, "Falkreath", "Seigneur d'Épervine", None),
    ("npcmodtowns.esp.json", 191, "Dragonsreach", "Ebonvale est un centre commercial florissant. Je fournis beaucoup de marchandises à Fort-Dragon, vous savez.", None),
    ("npcmodtowns.esp.json", 242, "Skyrim", "Helsmyrr est sûrement l'un des plus jolis villages de Bordeciel, vous ne trouvez pas ?", None),
    ("npcmodtowns.esp.json", 307, "Skyrim", "Ne faites pas attention à tous les potins. Granite Hill est l'un des meilleurs endroits de Bordeciel.", None),
    ("018auri.esp.json", 0, "Valenwood", "Rôdeur de Val-Boisé", None),
    ("katana.json.json", 1, "Skyrim", "Katana est un personnage mystérieux qui s'est rendu en Bordeciel à la recherche de son passé oublié.", None),

    # Vigilant Quests
    ("vigilant.esm.json", 6398, "Falkreath", "Envoyer la Vigile à Épervine", None),
    ("vigilant.esm.json", 6409, "Windhelm", "Envoyer la Vigile à Vendeaume", None),
    ("vigilant.esm.json", 6508, "Winterhold", "Envoyer la Vigile à Fortdhiver", None),
    ("vigilant.esm.json", 6537, "Dawnstar", "Envoyer la Vigile à Aubétoile", None),
    ("vigilant.esm.json", 6553, "Whiterun", "Envoyer la Vigile à Blancherive", None),
    ("vigilant.esm.json", 6571, "Riften", "Envoyer la Vigile à Faillaise", None),
    ("vigilant.esm.json", 515, "Falkreath", "Envoyer la Vigile à Épervine", None),
    ("vigilant.esm.json", 901, "Dawnstar", "Envoyer la Vigile à Aubétoile", None),
    ("vigilant.esm.json", 2825, "Winterhold", "Envoyer la Vigile à Fortdhiver", None),
    ("vigilant.esm.json", 5053, "Windhelm", "Envoyer la Vigile à Vendeaume", None),
    ("vigilant.esm.json", 5066, "Whiterun", "Envoyer la Vigile à Blancherive", None),
    ("vigilant.esm.json", 5353, "Riften", "Envoyer la Vigile à Faillaise", None),

    # Attributes (Stamina -> Vigueur, Mana -> Magie)
    ("additional attack by loop.esp.json", 8, "Stamina Cost", "Coût en vigueur", None),
    ("additional attack by loop.esp.json", 10, "Stamina Cost", "Coût en vigueur", None),
    ("fanatical enemies.esp.json", 203, "Magicka and Stamina Regeneration", "Régénération de magie et de vigueur", None),
    ("fanatical enemies.esp.json", 3195, "Magicka and Stamina Regeneration", "Régénération de magie et de vigueur", None),
    ("fanatical enemies.esp.json", 4228, "Magicka and Stamina Regeneration", "Régénération de magie et de vigueur", None),
    ("gray fox cowl.esm.json", 16, "Stamina", "La vigueur augmente de <mag> points.", None),
    ("gray fox cowl.esm.json", 41, "Stamina", "Restaure la vigueur de la cible de <mag> points. Ne fonctionne pas sur les créatures vivantes.", None),
    ("gray fox cowl.esm.json", 55, "Stamina", "Pouvoir de la pierre de vigueur", None),
    ("gray fox cowl.esm.json", 181, "Stamina", "Pierre de vigueur", None),
    ("dbm_amuletsofskyrim_patch.esp.json", 41, "Stamina", "Régénère la santé et la vigueur 15 % plus rapidement.", None),
    ("dbm_amuletsofskyrim_patch.esp.json", 42, "Stamina", "Régénère la santé et la vigueur 15 % plus rapidement.", None),
    ("ordinator - perks of skyrim.esp.json", 4425, "Mana Shield", "Bouclier de magie", None),
    ("vokrii - minimalistic perks of skyrim.esp.json", 1631, "Mana Stone", "Pierre de magie", None),
    ("vokrii - minimalistic perks of skyrim.esp.json", 1680, "Mana Shield", "Bouclier de magie", None),
    ("vokriinator black.esp.json", 1020, "Mana Shield", "Bouclier de magie", None),
    ("triumvirate - mage archetypes.esp.json", 1091, "Temple Grim Mana Scaling", "Progression de magie de Sinistre du temple", None),
    ("triumvirate - mage archetypes.esp.json", 1095, "Oathbreaker Ult Mana Cost", "Coût ultime en magie de Parjure", None),

    # Equipment Materials (Ebony -> Ébonite)
    ("fanatical enemies.esp.json", 777, "Ebony", "Grande épée d'ébonite du démon", None),
    ("fanatical enemies.esp.json", 2416, "Ebony", "Épée d'ébonite Volkihar", None),
    ("fanatical enemies.esp.json", 3298, "Ebony", "Grande épée d'ébonite du démon", None),
    ("dbm_inigo_patch.esp.json", 1, "Ebony", "L'arc d'ébonite d'Inigo", None),
    ("dbm_inigo_patch.esp.json", 10, "Ebony", "Un arc d'ébonite simple mais puissant. Propriété d'Iñigo le Généreux. S'adapte à son niveau.", None),
    ("dbm_inigo_patch.esp.json", 45, "Ebony", "L'arc d'ébonite d'Inigo", None),
    ("nolvus awakening armors balance patch.esp.json", 5, "Ebony", "Armure d'ébonite d'archimage noir (légère)", None),
    ("nolvus awakening armors balance patch.esp.json", 749, "Ebony", "Armure d'ébonite d'archimage noir (lourde)", None),
    ("nolvus awakening custom outfits.esp.json", 107, "Ebony", "Bottes d'ébonite de Nolvus", None),
    ("nolvus awakening custom outfits.esp.json", 112, "Ebony", "Gantelets d'ébonite de Nolvus", None),
]

# Internal quest scenes to keep technical and mark NoTranslationRequired
INTERNAL_SCENE_QUSTS: List[Tuple[str, int]] = [
    ("ai overhaul.esp.json", 659),
    ("timingiseverything.esp.json", 24),
    ("relationship dialogue overhaul.esp.json", 2232),
    ("relationship dialogue overhaul.esp.json", 3906),
    ("cutting room floor.esp.json", 516),
    ("cutting room floor.esp.json", 540),
    ("sunhelmsurvival.esp.json", 211),
    ("unofficial skyrim special edition patch.esp.json", 16177),
    ("unofficial skyrim special edition patch.esp.json", 16322),
    ("unofficial skyrim special edition patch.esp.json", 16396),
    ("unofficial skyrim special edition patch.esp.json", 16397),
    ("unofficial skyrim special edition patch.esp.json", 16398),
    ("unofficial skyrim special edition patch.esp.json", 16399),
    ("unofficial skyrim special edition patch.esp.json", 16400),
    ("unofficial skyrim special edition patch.esp.json", 16697),
    ("unofficial skyrim special edition patch.esp.json", 16833),
    ("unofficial skyrim special edition patch.esp.json", 16834),
    ("unofficial skyrim special edition patch.esp.json", 16984),
    ("unofficial skyrim special edition patch.esp.json", 17020),
    ("unofficial skyrim special edition patch.esp.json", 17021),
    ("unofficial skyrim special edition patch.esp.json", 17022),
    ("unofficial skyrim special edition patch.esp.json", 17023),
    ("unofficial skyrim special edition patch.esp.json", 17024),
    ("unofficial skyrim special edition patch.esp.json", 17025),
    ("unofficial skyrim special edition patch.esp.json", 17031),
    ("unofficial skyrim special edition patch.esp.json", 17049),
    ("unofficial skyrim special edition patch.esp.json", 17054),
    ("unofficial skyrim special edition patch.esp.json", 17056),
    ("unofficial skyrim special edition patch.esp.json", 17057),
    ("unofficial skyrim special edition patch.esp.json", 17231),
    ("unofficial skyrim special edition patch.esp.json", 17817),
    ("unofficial skyrim special edition patch.esp.json", 17877),
    ("unofficial skyrim special edition patch.esp.json", 17887),
    ("unofficial skyrim special edition patch.esp.json", 17898),
]


def apply_phase4() -> None:
    """Apply Phase 4 clean across all JSON translation files in DB_DIR."""
    total_breton_fixed = 0
    total_targeted_fixed = 0
    total_internal_marked = 0
    modified_files_count = 0

    # Build lookup table for targeted fixes
    targeted_map: Dict[Tuple[str, int], Tuple[str, str, str | None]] = {}
    for fn, idx, orig_sub, new_str, new_stat in TARGETED_LORE_FIXES:
        targeted_map[(fn.lower(), idx)] = (orig_sub, new_str, new_stat)

    # Build lookup for internal scenes
    internal_map: set[Tuple[str, int]] = {
        (fn.lower(), idx) for fn, idx in INTERNAL_SCENE_QUSTS
    }

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
                orig = row.get("original", "")
                s = row.get("string", "")
                status = row.get("status", "")

                # 1. Breton check & replacement
                if s and ("Bréton" in s or "bréton" in s):
                    new_s = s
                    for pat, rep in BRETON_REPLACEMENTS:
                        new_s = pat.sub(rep, new_s)
                    if new_s != s:
                        row["string"] = new_s
                        file_modified = True
                        total_breton_fixed += 1
                        s = new_s

                # 2. Targeted Lore fixes
                key = (fn_lower, idx)
                if key in targeted_map:
                    orig_sub, new_str, new_stat = targeted_map[key]
                    if orig_sub in orig:
                        if new_str is not None:
                            row["string"] = new_str
                        elif "legacyofthedragonborn.esm.json" in fn_lower and idx == 4628:
                            # Special case: LOTD book 4628 replace Falkreath -> Épervine
                            row["string"] = s.replace("te battre à Falkreath", "te battre à Épervine")
                        if new_stat is not None:
                            row["status"] = new_stat
                        elif status != "TranslationComplete":
                            row["status"] = "TranslationComplete"
                        file_modified = True
                        total_targeted_fixed += 1
                        s = row["string"]

                # 3. Internal scenes
                if key in internal_map:
                    if row.get("status") != "NoTranslationRequired":
                        row["status"] = "NoTranslationRequired"
                        file_modified = True
                        total_internal_marked += 1

            if file_modified:
                try:
                    with open(path, "w", encoding="utf-8", newline="\n") as fp:
                        json.dump(data, fp, indent=2, ensure_ascii=False)
                    modified_files_count += 1
                except Exception as e:
                    print(f"Error writing {path}: {e}")

    print("=" * 60)
    print("PHASE 4 CLEAN APPLICATION COMPLETED SUCCESSFULLY")
    print(f"Total Breton forms normalized to 'Breton': {total_breton_fixed}")
    print(f"Total targeted Lore & Toponym fixes:      {total_targeted_fixed}")
    print(f"Total internal quest scenes marked NTR:  {total_internal_marked}")
    print(f"Total modified files:                    {modified_files_count}")
    print("=" * 60)


if __name__ == "__main__":
    apply_phase4()
