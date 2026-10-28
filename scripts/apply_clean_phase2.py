"""
Apply Phase 2 surgical fixes across the French translation database:
- Category A: Lexical & Conceptual Mismatches (Fire/Frost/Shock, Hood/Boots, Amulet/Ring, Sword/Axe/Hammer)
- Category B: Swapped FULL/DESC, Truncated/Overwritten Books (BOOK DESC), and Truncated/Swapped Dialogues, Messages, Locations & Bestiary
- Category C: Shifted Quest Stages (QUST CNAM & QUST NNAM) across Base Mods, Patches, USSEP, LOTD & Creation Club
- Category D: Gameplay Numeric & Effect Discrepancies (PERK DESC, MGEF DNAM, SPEL DESC, WEAP DESC, MESG DESC)
"""

import json
import os
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")

DB_ROOT = r"e:\Code\SSE Translator updated\data\user\database\french"


def load_json(rel_path: str):
    full_path = os.path.join(DB_ROOT, rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(rel_path: str, data):
    full_path = os.path.join(DB_ROOT, rel_path)
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    modified_files = set()
    fix_counts_by_cat = defaultdict(int)
    fix_counts_by_file = defaultdict(int)
    fix_log = []

    def apply_entry_fix(rel_path, data, match_fn, new_str_or_fn, cat_label):
        count = 0
        for entry in data:
            if match_fn(entry):
                old_str = entry.get("string")
                new_str = new_str_or_fn(entry) if callable(new_str_or_fn) else new_str_or_fn
                if old_str != new_str and new_str is not None:
                    entry["string"] = new_str
                    count += 1
                    fix_counts_by_cat[cat_label] += 1
                    fix_counts_by_file[rel_path] += 1
                    modified_files.add(rel_path)
                    fix_log.append({
                        "category": cat_label,
                        "file": rel_path,
                        "form_id": entry.get("form_id") or entry.get("mcm_id") or entry.get("bestiary_id"),
                        "type": entry.get("type"),
                        "index": entry.get("index"),
                        "original": entry.get("original"),
                        "old_string": old_str,
                        "new_string": new_str,
                    })
        return count

    # Pre-load files we will modify or reference
    file_cache = {}

    def get_file(rel_path):
        if rel_path not in file_cache:
            file_cache[rel_path] = load_json(rel_path)
        return file_cache[rel_path]

    # Build a canonical DB lookup for (type, original) -> Counter of FR strings
    print("Building canonical translation lookup table across DB...")
    canonical_counts = defaultdict(Counter)
    for root, _, files in os.walk(DB_ROOT):
        for fn in sorted(files):
            if not fn.endswith(".json") or fn == "index.json":
                continue
            rel = os.path.relpath(os.path.join(root, fn), DB_ROOT)
            try:
                d = load_json(rel)
            except Exception:
                continue
            if not isinstance(d, list):
                continue
            for e in d:
                tp = e.get("type")
                orig = e.get("original")
                st = e.get("string")
                if tp in ("QUST CNAM", "QUST NNAM", "BOOK DESC", "INFO NAM1", "DIAL FULL") and orig and st and orig != st:
                    canonical_counts[(tp, orig)][st] += 1

    # =========================================================================
    # CATEGORY A: Lexical Concept Mismatches
    # =========================================================================
    cat_a = "Catégorie A : Contresens lexicaux & élémentaires"

    # 1. ACE
    f_ace = r"ACE - Extension des vêtements et armures\waccf_armor and clothing extension.esp.json"
    apply_entry_fix(
        f_ace, get_file(f_ace),
        lambda e: e.get("form_id") == "05185BC5|waccf_armor and clothing extension.esp" and e.get("type") == "ARMO FULL" and e.get("original") == "Embellished Mage Hood, Fur-Lined",
        "Capuche de mage embellie à fourrure", cat_a
    )

    # 2. Amulettes de Bordeciel
    f_amu = r"Amulettes de Bordeciel\SL01AmuletsSkyrim.esp.json"
    apply_entry_fix(
        f_amu, get_file(f_amu),
        lambda e: e.get("form_id") == "04013C1A|SL01AmuletsSkyrim.esp" and e.get("type") == "ARMO FULL" and e.get("original") == "Shrouded Amulet",
        "Amulette sibylline", cat_a
    )
    apply_entry_fix(
        f_amu, get_file(f_amu),
        lambda e: e.get("form_id") in ("0402AB92|SL01AmuletsSkyrim.esp", "04046C65|SL01AmuletsSkyrim.esp") and e.get("type") == "ARMO FULL" and e.get("original") == "Savior's Amulet",
        "Amulette du Sauveur", cat_a
    )
    apply_entry_fix(
        f_amu, get_file(f_amu),
        lambda e: e.get("form_id") == "0401E962|SL01AmuletsSkyrim.esp" and e.get("type") == "MGEF FULL" and e.get("original") == "The Warrior Amulet",
        "Amulette du Guerrier", cat_a
    )

    # 3. UndeathFixes
    f_und_fix = r"Immortel - Lichification classique\UndeathFixes.esp.json"
    apply_entry_fix(
        f_und_fix, get_file(f_und_fix),
        lambda e: e.get("form_id") in ("0501EEA1|UndeathFixes.esp", "0501EEA5|UndeathFixes.esp") and e.get("type") == "MGEF FULL" and e.get("original") == "Lich Weakness to Fire",
        "Vulnérabilité au feu de liche", cat_a
    )

    # 4. Vibrant weapons
    f_vib = r"Vibrant weapons Nolvus fr\Vibrant weapons.esl.json"
    apply_entry_fix(
        f_vib, get_file(f_vib),
        lambda e: e.get("form_id") == "03000842|Vibrant weapons.esl" and e.get("type") == "MGEF FULL" and e.get("original") == "Frost Greatsword Activator",
        "Espadon de givre Activator", cat_a
    )
    apply_entry_fix(
        f_vib, get_file(f_vib),
        lambda e: e.get("form_id") in ("0300085C|Vibrant weapons.esl", "030008AE|Vibrant weapons.esl") and e.get("original") == "Shock War Axe R",
        "Hache de guerre de foudre R", cat_a
    )

    # 5. Vigilant - Nerfed Rewards
    f_vig_nerf = r"Vigilant - Nerfed Rewards\vigilant nerfed rewards.esp.json"
    apply_entry_fix(
        f_vig_nerf, get_file(f_vig_nerf),
        lambda e: e.get("form_id") == "030E2CFB|Vigilant.esm" and e.get("type") == "MGEF FULL" and e.get("original") == "Frost Sword",
        "Épée de glace", cat_a
    )

    # =========================================================================
    # CATEGORY B: Swapped FULL/DESC, Overwritten/Truncated Books & Dialogues/Messages
    # =========================================================================
    cat_b = "Catégorie B : Inversions FULL/DESC, Livres écrasés & Dialogues/Messages tronqués ou décalés"

    # 1. Swapped FULL receiving DESC
    f_fan = r"Fanatical Enemies.esp - French\fanatical enemies.esp.json"
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") == "045BD72E|Fanatical Enemies.esp" and e.get("type") == "MGEF FULL" and e.get("original") == "Shadow Dancer",
        "Danseur de l'ombre", cat_b
    )
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") == "04C2A88B|Fanatical Enemies.esp" and e.get("type") == "ARMO FULL" and e.get("original") == "Ring of the Defiler",
        "Anneau du profanateur", cat_b
    )
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") == "04E85153|Fanatical Enemies.esp" and e.get("type") == "ARMO FULL" and e.get("original") == "Ring of the Corruptor",
        "Anneau du corrupteur", cat_b
    )

    f_nac = r"Nolvus Awakening Clothes Balance Patch - French\nolvus awakening clothes balance patch.esp.json"
    apply_entry_fix(
        f_nac, get_file(f_nac),
        lambda e: e.get("form_id") == "0102D990|Apachii_DivineEleganceStore.esm" and e.get("type") == "ARMO FULL" and e.get("original") == "DE Avallach Mask Silver Armor",
        "Masque d'Avallac'h en argent renforcé", cat_b
    )
    apply_entry_fix(
        f_nac, get_file(f_nac),
        lambda e: e.get("form_id") == "0102D98E|Apachii_DivineEleganceStore.esm" and e.get("type") == "ARMO FULL" and e.get("original") == "DE Avallach Mask Gold Armor",
        "Masque d'Avallac'h en or renforcé", cat_b
    )
    apply_entry_fix(
        f_nac, get_file(f_nac),
        lambda e: e.get("form_id") == "0102D989|Apachii_DivineEleganceStore.esm" and e.get("type") == "ARMO FULL" and e.get("original") == "DE Avallach Mask Bronze Armor",
        "Masque d'Avallac'h en bronze renforcé", cat_b
    )
    apply_entry_fix(
        f_nac, get_file(f_nac),
        lambda e: e.get("form_id") == "0102D98B|Apachii_DivineEleganceStore.esm" and e.get("type") == "ARMO FULL" and e.get("original") == "DE Avallach Mask Ebony Armor",
        "Masque d'Avallac'h en ébonite renforcé", cat_b
    )

    f_nadlc = r"Nolvus Awakening DLC Patch - French\nolvus awakening dlc patch.esp.json"
    apply_entry_fix(
        f_nadlc, get_file(f_nadlc),
        lambda e: e.get("form_id") == "07125B04|LegacyoftheDragonborn.esm" and e.get("type") == "ARMO FULL" and e.get("original") == "Ring of Phynaster",
        "Anneau de Phynaster", cat_b
    )
    apply_entry_fix(
        f_nadlc, get_file(f_nadlc),
        lambda e: e.get("form_id") == "071253C0|LegacyoftheDragonborn.esm" and e.get("type") == "WEAP FULL" and e.get("original") == "Fang of Haynekhtnamet (CC Replaced)",
        "Croc de Haynekhtnamet", cat_b
    )

    f_coin = r"COIN - Monnaies de Bordeciel\C.O.I.N.esp.json"
    apply_entry_fix(
        f_coin, get_file(f_coin),
        lambda e: e.get("form_id") == "01DE5021|Update.esm" and e.get("type") == "MISC FULL" and e.get("original") == "Mede",
        "Mede", cat_b
    )

    f_ddc = r"Dragons divers et variés\DiverseDragonsCollectionSE.esp.json"
    apply_entry_fix(
        f_ddc, get_file(f_ddc),
        lambda e: e.get("form_id") == "040DF552|DiverseDragonsCollectionSE.esp" and e.get("type") == "MGEF FULL" and e.get("original") == "Solar Breath Burn Undead",
        "Souffle solaire brûle-morts-vivants", cat_b
    )

    f_apo = r"Apocalypse - Magie de Bordeciel\Apocalypse - Magic of Skyrim.esp.json"
    apply_entry_fix(
        f_apo, get_file(f_apo),
        lambda e: e.get("form_id") == "0303E5FF|Apocalypse - Magic of Skyrim.esp" and e.get("type") == "BOOK DESC",
        "<font face='$HandwrittenFont'><font size='40'><p align='center'>\r\nMalédiction de silence", cat_b
    )

    # 2. Books Overwritten or Truncated (BOOK DESC)
    # 2a. LOTD 04028275|Dragonborn.esm ('The True Noble's Code' -> 'Le Code de la noblesse')
    f_bs_assets = r"Au-delà de Bordeciel - Bruma\BSAssets.esm.json"
    f_lotd = r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json"
    noble_code_fr = None
    for e in get_file(f_bs_assets):
        if e.get("type") == "BOOK DESC" and "The True Noble's Code" in (e.get("original") or ""):
            noble_code_fr = e.get("string")
            break
    if noble_code_fr:
        apply_entry_fix(
            f_lotd, get_file(f_lotd),
            lambda e: e.get("form_id") == "04028275|Dragonborn.esm" and e.get("type") == "BOOK DESC",
            noble_code_fr, cat_b
        )

    # 2b. Vigilant books (*054ECE|Vigilant.esm and *4A8AFE|Vigilant.esm)
    f_vig_173 = r"vigile_1.7.3_sse\vigilant.esm.json"
    f_vig_vost = r"Vigilant voiced english vostFR\Vigilant.esm.json"
    f_vig_bc = r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json"
    f_dbm_uns = r"DBM_Unslaad_Display_Patch\dbm_unslaad_display_patch.esp.json"

    vig_054ece_fr = None
    vig_4a8afe_fr = None
    for e in get_file(f_vig_173):
        if e.get("type") == "BOOK DESC" and (e.get("form_id") or "").endswith("054ECE|Vigilant.esm"):
            vig_054ece_fr = e.get("string").replace("son recouvertes", "sont recouvertes")
        elif e.get("type") == "BOOK DESC" and (e.get("form_id") or "").endswith("4A8AFE|Vigilant.esm"):
            vig_4a8afe_fr = e.get("string")

    for target_f in (f_vig_173, f_vig_vost, f_vig_bc, f_dbm_uns):
        if vig_054ece_fr:
            apply_entry_fix(
                target_f, get_file(target_f),
                lambda e: e.get("type") == "BOOK DESC" and (e.get("form_id") or "").endswith("054ECE|Vigilant.esm"),
                vig_054ece_fr, cat_b
            )
    for target_f in (f_vig_vost, f_vig_bc, f_dbm_uns):
        if vig_4a8afe_fr:
            apply_entry_fix(
                target_f, get_file(target_f),
                lambda e: e.get("type") == "BOOK DESC" and (e.get("form_id") or "").endswith("4A8AFE|Vigilant.esm"),
                vig_4a8afe_fr, cat_b
            )

    # 2c. Elemental Destruction Magic Redux spell tomes & broken font tag
    f_edmr = r"Magie de destruction élémentale II\Elemental Destruction Magic Redux.esp.json"
    apply_entry_fix(
        f_edmr, get_file(f_edmr),
        lambda e: e.get("form_id") == "03000964|Elemental Destruction Magic Redux.esp" and e.get("type") == "BOOK DESC",
        lambda e: e.get("string", "").replace("Rocher", "Explosion de pierre").replace("face'$HandwrittenFont'", "face='$HandwrittenFont'"),
        cat_b
    )
    apply_entry_fix(
        f_edmr, get_file(f_edmr),
        lambda e: e.get("form_id") == "03000965|Elemental Destruction Magic Redux.esp" and e.get("type") == "BOOK DESC",
        lambda e: e.get("string", "").replace("Rune de vent", "Rune de terre").replace("face'$HandwrittenFont'", "face='$HandwrittenFont'"),
        cat_b
    )
    apply_entry_fix(
        f_edmr, get_file(f_edmr),
        lambda e: e.get("type") == "BOOK DESC" and "face'$HandwrittenFont'" in (e.get("string") or ""),
        lambda e: e.get("string", "").replace("face'$HandwrittenFont'", "face='$HandwrittenFont'"),
        cat_b
    )

    # 3. Truncated/Swapped Dialogues, Messages, Locations, Weapons, Bestiary & Campfire
    f_cit = r"Citizens of Tamriel\citizenscomplete.esp.json"
    apply_entry_fix(
        f_cit, get_file(f_cit),
        lambda e: e.get("form_id") == "0500C1C8|CitizensComplete.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Ma dame, je suis Florian de Gabb : barde extraordinaire et pourvoyeur d'élégance, sous toutes ses formes.",
        cat_b
    )

    f_inigo = r"Inigo\Inigo.esp.json"
    apply_entry_fix(
        f_inigo, get_file(f_inigo),
        lambda e: e.get("form_id") == "02069B47|Inigo.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "What did you see?",
        "Qu'as-tu vu ?", cat_b
    )
    apply_entry_fix(
        f_inigo, get_file(f_inigo),
        lambda e: e.get("form_id") == "0206A549|Inigo.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 5,
        "Stupide, stupide, stupide, stupide araignée. Il n’y a jamais eu une araignée aussi stupide. Fin.", cat_b
    )
    apply_entry_fix(
        f_inigo, get_file(f_inigo),
        lambda e: e.get("form_id") == "0206DBEB|Inigo.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 3,
        "J'ai honte. J'espère qu'avec le temps, je pourrai mériter ton pardon.", cat_b
    )

    f_ftle = r"Extension des dialogues des Parjures et des Thalmors\Forsworn and Thalmor Lines Expansion.esp.json"
    apply_entry_fix(
        f_ftle, get_file(f_ftle),
        lambda e: e.get("form_id") == "02000885|Forsworn and Thalmor Lines Expansion.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Stupide Orque.", cat_b
    )
    apply_entry_fix(
        f_ftle, get_file(f_ftle),
        lambda e: e.get("form_id") == "020008B7|Forsworn and Thalmor Lines Expansion.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Ha ! Ils meurent trop vite. J'essaierai peut-être de me retenir la prochaine fois. Histoire d'avoir une cible mouvante. Un bon entraînement !", cat_b
    )
    apply_entry_fix(
        f_ftle, get_file(f_ftle),
        lambda e: e.get("form_id") == "020008A4|Forsworn and Thalmor Lines Expansion.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Je vais me faire des bottes avec votre peau !", cat_b
    )

    f_pos = r"La Voie du Sorcier\PathOfSorcery.esp.json"
    apply_entry_fix(
        f_pos, get_file(f_pos),
        lambda e: e.get("form_id") == "0A000BA0|PathOfSorcery.esp" and e.get("type") == "PERK DESC" and e.get("original") == "Can learn enchantments without destroying the base item.",
        "Vous pouvez apprendre des enchantements sans détruire les objets.", cat_b
    )

    f_soap = r"Savons des auberges\Inn Soaps.esp.json"
    apply_entry_fix(
        f_soap, get_file(f_soap),
        lambda e: e.get("form_id") == "01000852|Dirt and Blood - Dynamic Visuals.esp" and e.get("type") == "MESG DESC",
        "J'ai besoin de savon, je devrais en fabriquer dans une marmite ou en acheter dans une auberge.", cat_b
    )

    f_oah_p = r"Projet OAH\DwarfsphereImprovedPatch.esp.json"
    apply_entry_fix(
        f_oah_p, get_file(f_oah_p),
        lambda e: (e.get("form_id") or "").startswith("06000B09|") and e.get("type") == "MESG DESC",
        "Choisissez ce que vous souhaitez faire dans les bains dwemers :", cat_b
    )

    f_lull = r"Les Roues de Lull\lullfish.esp.json"
    apply_entry_fix(
        f_lull, get_file(f_lull),
        lambda e: e.get("form_id") == "08000C88|lullfish.esp" and e.get("type") == "LCTN FULL" and e.get("original") == "Lull-Mor",
        "Lull-Mor", cat_b
    )

    f_crf = r"USSEP - Traduction Francaise\cutting room floor.esp.json"
    apply_entry_fix(
        f_crf, get_file(f_crf),
        lambda e: e.get("form_id") in ("00017785|Skyrim.esm", "00018A4F|Skyrim.esm") and e.get("original") == "Heljarchen",
        "Heljarchen", cat_b
    )
    apply_entry_fix(
        f_crf, get_file(f_crf),
        lambda e: e.get("form_id") == "0001EA4F|Skyrim.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 100 and e.get("original") == "I have resolved the conflict between the jester Cicero and Loreius the farmer.",
        "J'ai résolu la dispute entre Cicéron le bouffon et Loreius le fermier.", cat_b
    )

    f_ussep = r"USSEP - Traduction Francaise\unofficial skyrim special edition patch.esp.json"
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "02019913|Dawnguard.esm" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "J'espère qu'Alvide ne m'en voudra pas, mais je ne peux pas la protéger tout seul. Nous sommes plus en sécurité ici.", cat_b
    )
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "0001BB99|Skyrim.esm" and e.get("type") == "INFO NAM1" and e.get("index") == 1 and e.get("original") == "Pelagius III.",
        "Pélagius III.", cat_b
    )

    f_remi_lotd = r"Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)\hliiremilotd.esp.json"
    apply_entry_fix(
        f_remi_lotd, get_file(f_remi_lotd),
        lambda e: e.get("form_id") == "07000824|HLIIRemiLOTD.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Oh, cette statue de jade est magnifique ! Si vous vouliez dire à cet Auryen qu'elle était introuvable, je garderais le secret.", cat_b
    )
    apply_entry_fix(
        f_remi_lotd, get_file(f_remi_lotd),
        lambda e: e.get("form_id") == "07000A29|HLIIRemiLOTD.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "À quoi pensez-vous que l'artéfact ressemble ? Je n'ai pas vu beaucoup d'objets d'Elfes des neiges. Surtout des artéfacts de... ce que sont les Falmers aujourd'hui.", cat_b
    )
    apply_entry_fix(
        f_remi_lotd, get_file(f_remi_lotd),
        lambda e: e.get("form_id") == "07000C08|HLIIRemiLOTD.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Oh ! Je crois que c'est ça ! C'est... une sorte de manuel d'instruction pour enseigner la magie.", cat_b
    )
    apply_entry_fix(
        f_remi_lotd, get_file(f_remi_lotd),
        lambda e: e.get("form_id") == "07000C73|HLIIRemiLOTD.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Qu'est-ce que ça veut dire, par Oblivion ? Calcelmo ne m'a jamais montré ce symbole !", cat_b
    )

    f_remi = r"Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)\hlioremi.esp.json"
    apply_entry_fix(
        f_remi, get_file(f_remi),
        lambda e: e.get("form_id") == "0546FA55|HLIORemi.esp" and e.get("type") == "QUST CNAM" and e.get("index") in (85, 93) and "poison" in (e.get("string") or ""),
        lambda e: e.get("string", "").replace(
            "J'ai reçu une sorte de poison et me suis réveillé piégé et Rémiel blessée. C'est clair que c'était le plan de Morvic.",
            "Il semble que Rémi soit tombée sur Morvic sans moi. La situation s'annonce mal."
        ),
        cat_b
    )

    f_necro = r"Réactions à la nécromancie\NPCs React To Necromancy.esp.json"
    apply_entry_fix(
        f_necro, get_file(f_necro),
        lambda e: e.get("form_id") == "03000858|NPCs React To Necromancy.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Il est... vraiment mort ?", cat_b
    )
    apply_entry_fix(
        f_necro, get_file(f_necro),
        lambda e: e.get("form_id") in ("03000877|NPCs React To Necromancy.esp", "030008E9|NPCs React To Necromancy.esp") and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "De la nécromancie ! Honte à vous !", cat_b
    )

    f_frenzy = r"Réactions à la frénésie\NPCsReactToFrenzy.esp.json"
    apply_entry_fix(
        f_frenzy, get_file(f_frenzy),
        lambda e: e.get("form_id") == "01000D64|NPCsReactToFrenzy.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Traîtres ! Vous êtes tous des traîtres !", cat_b
    )

    f_3dnpc = r"3DNPC - PNJs intéressants\3DNPC.esp.json"
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("form_id") == "0523D691|3DNPC.esp" and e.get("type") == "QUST NNAM" and e.get("index") == 60,
        "Localisez et tuez une cible dont le nom commence par la lettre « C »", cat_b
    )
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("form_id") == "053788A9|3DNPC.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Eh bien, si j'étais un livre, c'est ici que je dormirais.", cat_b
    )
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("form_id") == "0518CB53|3DNPC.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Je ne suis pas un grand cuisinier, mais je ne pense pas que cela vous tuera.", cat_b
    )
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("form_id") == "05071BF9|3DNPC.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 6,
        "Ce sont aussi des imbéciles. Mon plan initial était d'entrer dans une taverne bondée et de jeter une hache de bonne facture sur le sol.", cat_b
    )
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("form_id") in ("0504405A|3DNPC.esp", "0514465F|3DNPC.esp", "0526F792|3DNPC.esp") and e.get("type") == "DIAL FULL" and e.get("original") == "I can respect that.",
        "Je peux respecter ça.", cat_b
    )
    apply_entry_fix(
        f_3dnpc, get_file(f_3dnpc),
        lambda e: e.get("type") == "INFO NAM1" and e.get("index") == 5 and (e.get("original") or "").endswith("as the moonlight's dark hunter."),
        "Ainsi la meute naquit à nouveau comme les Loups de Jorrvaskr ; pour décider de la vie et servir la mort, comme le sombre chasseur du clair de lune.", cat_b
    )

    f_mas = r"Astre-Lune\MoonAndStar_MAS.esp.json"
    apply_entry_fix(
        f_mas, get_file(f_mas),
        lambda e: e.get("form_id") == "0400C048|MoonAndStar_MAS.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "I can respect that.",
        "Je peux respecter ça.", cat_b
    )

    f_bsh = r"Au-delà de Bordeciel - Bruma\BSHeartland.esm.json"
    apply_entry_fix(
        f_bsh, get_file(f_bsh),
        lambda e: e.get("form_id") in ("0202DAE3|BSHeartland.esm", "0202DAE5|BSHeartland.esm") and e.get("type") == "INFO NAM1" and e.get("index") == 1 and e.get("original") == "*gasp*",
        "(halète)", cat_b
    )
    apply_entry_fix(
        f_bsh, get_file(f_bsh),
        lambda e: e.get("form_id") == "02064F61|BSHeartland.esm" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Je suis le plus illustre barde de tout Tamriel, je vous le promets !", cat_b
    )

    f_fse = r"ChickenMike's Random Assortment of Patches - French\Face Sculptor Expanded - Growl Patch.esp.json"
    apply_entry_fix(
        f_fse, get_file(f_fse),
        lambda e: e.get("form_id") == "0100696F|Dawnguard.esm" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Ah oui... Les gardes connaissent votre visage. Voyons ce que nous pouvons faire.", cat_b
    )

    f_wyrm = r"Guivrecroc\Wyrmstooth.esp.json"
    apply_entry_fix(
        f_wyrm, get_file(f_wyrm),
        lambda e: e.get("form_id") == "02119A55|Wyrmstooth.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 3,
        "Revenez nous rendre visite dans un futur proche. Dès que nous commencerons à reconstruire, certains ici auront peut-être besoin d'un aventurier compétent comme vous.", cat_b
    )
    apply_entry_fix(
        f_wyrm, get_file(f_wyrm),
        lambda e: e.get("form_id") == "023A1476|Wyrmstooth.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "Wait here.",
        "Attendez ici.", cat_b
    )

    f_kat = r"Katana - Journey in the Shadows vostFR 2-0-4 SE\Katana.esp.json"
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") in ("05B93062|Katana.esp", "05E4D49C|Katana.esp") and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Attendez, je pense que je devrais vous dire quelque chose avant que ça ne vous prenne au dépourvu.", cat_b
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "056E2B50|Katana.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 2,
        "Je plaisante. Peut-être. Vous vous souvenez, quand je vous ai dit que j'avais une ombre ?", cat_b
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "056E2B50|Katana.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 3,
        "Son emprise sur moi s'est relâchée, c'est le moins qu'on puisse dire. Mais assez parlé de ça.", cat_b
    )

    f_mp_patch = r"Le voyage en Elsweyr\JRMoonpathtoElsweyrPatch.esp.json"
    apply_entry_fix(
        f_mp_patch, get_file(f_mp_patch),
        lambda e: e.get("form_id") == "01085C9B|moonpath.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "Excuse me?",
        "Excusez-moi ?", cat_b
    )
    apply_entry_fix(
        f_mp_patch, get_file(f_mp_patch),
        lambda e: e.get("form_id") == "0101EE9E|moonpath.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "I'd better get going.",
        "Je ferais mieux d'y aller.", cat_b
    )
    apply_entry_fix(
        f_mp_patch, get_file(f_mp_patch),
        lambda e: e.get("form_id") == "0101EE9A|moonpath.esp" and e.get("type") == "DIAL FULL" and e.get("original") == "Does that mean I'm one of the Pahmar now too?",
        "Est-ce que cela veut dire que je fais aussi partie des Pahmars, maintenant ?", cat_b
    )

    f_rdo = r"RDO - Extension des dialogues relationnels\Relationship Dialogue Overhaul.esp.json"
    apply_entry_fix(
        f_rdo, get_file(f_rdo),
        lambda e: e.get("form_id") == "0007A50B|Skyrim.esm" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Je ferais mieux de retourner auprès de maître Neloth, dans ce cas. Qui sait ce qui s'est passé depuis mon départ.", cat_b
    )

    f_ayop_tg = r"À votre rythme\at your own pace - thieves guild.esp.json"
    apply_entry_fix(
        f_ayop_tg, get_file(f_ayop_tg),
        lambda e: e.get("form_id") == "0002D88E|Skyrim.esm" and e.get("type") == "DIAL FULL" and e.get("original") == "What else you got?",
        "Qu'avez-vous d'autre ?", cat_b
    )

    f_sgt = r"Bordeciel a un incroyable talent\SkyrimsGotTalent-Bards.esp.json"
    apply_entry_fix(
        f_sgt, get_file(f_sgt),
        lambda e: e.get("form_id") == "04014CC0|SkyrimsGotTalent-Bards.esp" and e.get("type") == "INFO NAM1" and e.get("index") == 1,
        "Ha ha ! C'est triste.", cat_b
    )

    f_aeth = r"Compilation d'armures et d'armes en aethérium\AetheriumSwordsnArmor.esp.json"
    apply_entry_fix(
        f_aeth, get_file(f_aeth),
        lambda e: e.get("form_id") == "03000991|AetheriumSwordsnArmor.esp" and e.get("type") == "MGEF DNAM",
        "Vous êtes <mag> % plus difficile à détecter.", cat_b
    )

    for f_thau in (
        r"Thaumaturgie - Refonte de l'enchantement\Thaumaturgy.esp.json",
        r"Thaumaturgie - Refonte de l'enchantement\Thaumaturgy - USSEP - Patch.esp.json",
    ):
        apply_entry_fix(
            f_thau, get_file(f_thau),
            lambda e: e.get("form_id") == "000BE17F|Skyrim.esm" and e.get("type") == "WEAP FULL" and e.get("original") == "Sanctified Elven Bow",
            "Arc elfique sanctifié", cat_b
        )
        apply_entry_fix(
            f_thau, get_file(f_thau),
            lambda e: e.get("form_id") == "000BEEE6|Skyrim.esm" and e.get("type") == "WEAP FULL" and e.get("original") == "Sanctified Glass Bow",
            "Arc de verre sanctifié", cat_b
        )
        apply_entry_fix(
            f_thau, get_file(f_thau),
            lambda e: e.get("form_id") in ("000BF41C|Skyrim.esm", "000BF41D|Skyrim.esm") and e.get("type") == "WEAP FULL" and e.get("original") == "Sanctified Ebony Bow",
            "Arc d'ébonite sanctifié", cat_b
        )

    f_camp_mcm = r"Feux de camp\Interface\translations\campfire_french.txt.json"
    apply_entry_fix(
        f_camp_mcm, get_file(f_camp_mcm),
        lambda e: e.get("mcm_id") == "$CampfireOptionHighlightCampfireMode",
        "Rapide : 4 bûches ou bois morts sont utilisés et le feu de camp s'allume automatiquement.\\nRéaliste : Vous devez utiliser de l'amadou et du petit bois, et allumer le feu de camp demande du talent et du temps.\\nPar défaut : Réaliste",
        cat_b
    )

    # Bestiary truncated descriptions
    bestiary_fixes = [
        (
            r"Le Bestiaire de l'Enfant de dragon\interface\creatures\undead\sentry\sentry shock.json.json",
            "sentry shock-description",
            "Imaginez un chevalier sentinelle, non seulement vêtu d'une armure traditionnelle, mais incarnant la foudre elle-même. Cette sentinelle se dresse fièrement, gardienne des portes d'un royaume où les nuages d'orage ne se dissipent jamais. Son armure crépite de l'énergie brute d'un millier d'orages, illuminant les ténèbres à chacun de ses mouvements. Dans sa main, une lance bourdonne d'une puissance électrique, prête à foudroyer tout ennemi avec la rapidité de l'éclair. Ce chevalier n'est pas un simple protecteur : c'est une force de la nature, un spectacle éblouissant de puissance et de lumière."
        ),
        (
            r"Le Bestiaire de l'Enfant de dragon\interface\creatures\undead\sentry\sentry.json.json",
            "sentry-description",
            "Une sentinelle enflammée se dresse tel un redoutable gardien, sa silhouette enveloppée de flammes dansantes qui projettent une lueur féroce. Cette sentinelle apparaît souvent dans les contes et les légendes, où elle garde des lieux sacrés ou importants, sa présence ardente dissuadant tous les intrus à l'exception des plus braves ou des plus téméraires. Les flammes qui l'entourent ne sont pas là que pour le spectacle : elles servent de barrière et d'arme, capables d'incinérer toute menace osant s'approcher de trop près. Malgré son apparence intimidante, une sentinelle de feu est un symbole de protection, illuminant les ténèbres et veillant sur les trésors qui lui sont confiés."
        ),
        (
            r"Le Bestiaire de l'Enfant de dragon\interface\creatures\undead\draugr\frozen worker.json.json",
            "frozen worker-description",
            "Imaginez une silhouette émergeant des profondeurs glacées, un ouvrier d'une époque révolue, désormais réduit à l'état de mort-vivant. Figé dans le temps, son visage est un souvenir obsédant du passé, le givre s'accrochant à ses vêtements en lambeaux et son regard aussi froid que la glace qui l'ensevelit. Ce travailleur spectral est un témoignage glaçant de la marche implacable du temps, une silhouette qui poursuit ses tâches éreintantes même au-delà du voile de la mort, éternellement liée aux terres désolées et gelées qui furent autrefois son foyer."
        ),
        (
            r"Le Bestiaire de l'Enfant de dragon\interface\creatures\undead\rotten corpse\rotten corpse.json.json",
            "rotten corpse-description",
            "Un cadavre pourri se présente comme un corps réanimé à la chair en décomposition. Ces créatures ont généralement une apparence grotesque, avec des os apparents et une peau décolorée qui pèle. Elles se déplacent d'une démarche traînante, poussées par une faim primaire, et poursuivent implacablement les vivants."
        ),
    ]
    for b_file, b_id, b_text in bestiary_fixes:
        apply_entry_fix(
            b_file, get_file(b_file),
            lambda e, bid=b_id: e.get("bestiary_id") == bid,
            b_text, cat_b
        )

    # =========================================================================
    # CATEGORY C: Shifted Quest Stages (QUST CNAM & QUST NNAM)
    # =========================================================================
    cat_c = "Catégorie C : Décalages d'index de quêtes (QUST CNAM / QUST NNAM)"

    # 1. SUDs
    f_suds = r"Boissons uniques de Bordeciel\SUDs.esp.json"
    apply_entry_fix(
        f_suds, get_file(f_suds),
        lambda e: e.get("form_id") == "050008C8|SUDs.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 79,
        "À quoi d'autre pouvais-je m'attendre de la part d'une boisson servie dans un égout... C'est ce que l'on pourrait penser au premier abord en découvrant la « Décapeuse », une spécialité vendue à la Cruche percée de Faillaise dans son humble mais jolie bouteille en terre cuite. Ce breuvage n'est guère plus qu'un grog, mais il possède finalement un certain charme rustique, en plus d'être bon marché et fort. Je vais tâcher de découvrir d'autres spécialités locales dans les tavernes et auberges de la province.",
        cat_c
    )
    apply_entry_fix(
        f_suds, get_file(f_suds),
        lambda e: e.get("form_id") == "050008C8|SUDs.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 103,
        "Le Dard de l'abeille à Faillaise est le foyer de l'innovation alcoolisée. L'une de leurs spécialités s'appelle le « Course-Falaise », capable d'assommer un troll de glace. Il est composé de vin de Tison, de cognac cyrodilien, de flin et de sujamma. Comment ils ont réussi à concocter ce breuvage me dépasse, mais d'une manière ou d'une autre, cela fonctionne. Je vais tâcher de découvrir d'autres spécialités locales dans les tavernes et auberges de la province.",
        cat_c
    )
    apply_entry_fix(
        f_suds, get_file(f_suds),
        lambda e: e.get("form_id") == "050008C8|SUDs.esp" and e.get("type") == "QUST NNAM" and e.get("index") == 16 and "Valdimar" in (e.get("original") or ""),
        "Buvez une Folie de Valdimar au Foyer gelé",
        cat_c
    )

    # 2. Falskaar
    f_falsk = r"Falskaar\Falskaar - Bug Fixes.esp.json"
    apply_entry_fix(
        f_falsk, get_file(f_falsk),
        lambda e: e.get("form_id") == "0205E483|Falskaar.esm" and e.get("type") == "QUST NNAM" and e.get("index") == 30 and e.get("original") == "Clear the fort of its troops",
        "Éliminez les troupes du fort", cat_c
    )

    # 3. Gray Cowl
    f_gfc = r"Gray Cowl of Nocturnal VF Partielle\Gray Fox Cowl.esm.json"
    apply_entry_fix(
        f_gfc, get_file(f_gfc),
        lambda e: e.get("form_id") == "02001E61|Gray Fox Cowl.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 80 and e.get("string") == "J'ai réussi à m'échapper d'Havreglace.",
        "J'ai enfin obtenu le Capuchon gris de Nocturne. Maintenant, je dois retourner voir Seviana en utilisant le portail magique.", cat_c
    )

    # 4. Inigo
    apply_entry_fix(
        f_inigo, get_file(f_inigo),
        lambda e: e.get("form_id") == "020695C5|Inigo.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 98 and (e.get("original") or "").startswith("We found the wooden posts"),
        "Nous avons trouvé les piliers en bois de la vision d'Inigo. Heureusement, ils nous guident vers ce qui cause les troubles dans son cerveau.", cat_c
    )
    apply_entry_fix(
        f_inigo, get_file(f_inigo),
        lambda e: e.get("form_id") == "020695C5|Inigo.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 80 and e.get("original", "").startswith("Inigo has suggested I ask Langley"),
        "Inigo a suggéré que je demande à Langley son sort d'Invocation. Peut-être que je peux le persuader de me donner une copie.", cat_c
    )

    # 5. Katana
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058BB421|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 87 and (e.get("original") or "").startswith("I think we should be receiving"),
        "Je pense que nous devrions recevoir quelque chose sous peu... Par un messager, peut-être ?", cat_c
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058BB421|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 87 and (e.get("original") or "").startswith("Even Chadryn couldn't ruin"),
        "Même Chadryn n'a pas pu gâcher un si beau moment. Tout le monde est heureux et fait la fête. Je devrais me joindre à eux et discuter un moment.", cat_c
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058E1B19|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 85 and e.get("original") == "I don't understand why I must remain seated.",
        "Je ne comprends pas pourquoi je dois rester assis.", cat_c
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058E1B19|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 98 and e.get("original") == "Megara gave me another note. I should read it.",
        "Megara m’a donné une autre note. Je devrais la lire.", cat_c
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058E1B19|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 87 and e.get("original", "").startswith("I've defeated Runir Wulfhart"),
        "J’ai vaincu Runir Wulfhart. Je dois récupérer ma récompense auprès de Megara ; elle aura peut-être d’autres renseignements pour moi.", cat_c
    )
    apply_entry_fix(
        f_kat, get_file(f_kat),
        lambda e: e.get("form_id") == "058E1B19|Katana.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 76 and e.get("original", "").startswith("River got away"),
        "River s'est enfuie, mais on dirait que Katana est en paix avec cet état de fait. Je suis simplement content que nous nous en soyons sortis vivants, et je parie que Mégara le sera aussi. Prendre un verre avec elle et Katana au Chasseur ivre serait merveilleux maintenant. Nous fêterons ça et apprendrons à mieux nous connaître ! Peut-être même qu'elle aimerait se joindre à nous.", cat_c
    )

    # 6. LOTD quests (05121573, 052D1170, 054D1811, 0558B96A)
    lotd_qust_fixes = [
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 101, "The chain I found", "La chaîne que j'ai trouvée a permis d'ouvrir une pièce secrète des catacombes du fort du Col pâle, où un bouclier antique était remisé, qu'Ezra s'est empressée de récupérer. Comme Argus est mort, les choses vont mal tourner si je la ramène là-bas. Je devrais la voler, la tuer, lui tendre une embuscade au camp d'Argus ou me séparer d'elle."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 88, "I've arrived in Sancre Tor", "Je suis arrivé à Sancre Tor et une force mystérieuse s'est immédiatement liée à la Pierre-Voie ayléide, m'empêchant de la retirer. Je devrais trouver un moyen d'entrer dans la forteresse et localiser le tombeau de Tiber Septim."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 105, "I spoke with Auryen", "J'ai parlé de l'étrange fragment à Auryen, et il cherche actuellement à confirmer qu'il s'agit bien d'un éclat de l'Amulette des Rois. Je devrais repasser demain pour voir s'il a découvert quelque chose."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 92, "I have found three sword keys", "J'ai trouvé trois clés-lames à Sancre Tor. Je dois trouver des indices sur ce à quoi elles mènent."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 108, "I've taken out Ezra. I should take", "J'ai éliminé Ezra. Je devrais prendre le fragment et le bouclier et utiliser le journal d'Argus pour retrouver les autres morceaux."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 80, "I've taken out Ezra and have the shard", "J'ai éliminé Ezra et récupéré le fragment et le bouclier. Je dois trouver d'autres indices sur l'emplacement des autres fragments. Le journal d'Argus contient probablement ce qu'il me faut."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 103, "I found a note Ulgarg", "J'ai trouvé une note qu'Ulgarg a apparemment laissée aux siens à Dushnikh Yal, indiquant qu'il se dirige vers l'est pour éviter la Morag Tong. Je devrais voir s'il y a des traces de son passage dans les environs."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 66, "I've destroted Ysmir Wulfharth", "J'ai terrassé Ysmir Wulfharth et obtenu ses bottes. Je dois maintenant suivre les pistes permettant de retrouver l'Armure du Seigneur."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 83, "I've unlocked the tomb of the Underking", "J'ai déverrouillé le tombeau du Roi des Tréfonds et dois maintenant le détruire pour pouvoir quitter Sancre Tor."),
        ("05121573|LegacyoftheDragonborn.esm", "QUST CNAM", 110, "I've gathered all the shards", "J'ai rassemblé tous les fragments de l'Amulette des Rois, sa monture ainsi qu'un bouclier inhabituel qui semble entrer en résonance avec eux. Je devrais interroger Auryen à ce sujet."),
        ("052D1170|LegacyoftheDragonborn.esm", "QUST CNAM", 69, "Marassi has the idea", "Marassi a eu l'idée d'établir un certain nombre de stations d'exploration en Bordeciel pour servir de refuges et de comptoirs d'approvisionnement aux explorateurs. J'ai construit la station d'exploration occidentale dans la Crevasse. Je devrais retourner voir Marassi pour le lui dire."),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST CNAM", 87, "I recovered a Nordic door claw", "J'ai récupéré une griffe de porte nordique au col de Parlevent. Je devrais retourner voir Marassi avant de continuer."),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST CNAM", 92, "The team is back on the job", "L'équipe est de retour au travail. Je devrais retourner les voir dans quelques jours pour constater les progrès accomplis ou les aider à creuser pour continuer à progresser."),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST CNAM", 100, "I should check back with the Windcaller", "Je devrais retourner voir les fouilles du col de Parlevent pour vérifier comment les travaux progressent."),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST CNAM", 72, "The excavation has hit a dead stop", "Les fouilles sont au point mort en raison de la présence de deux dragons dans une clairière du col. Je devrais m'occuper d'eux et découvrir ce qu'ils gardent."),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST NNAM", 50, "Return to Marassi before continuing", "Retournez voir Marassi avant de continuer"),
        ("054D1811|LegacyoftheDragonborn.esm", "QUST NNAM", 110, "Return to Marassi and report the barrier", "Retournez voir Marassi et signalez la barrière"),
        ("052DA4B9|LegacyoftheDragonborn.esm", "ACTI FULL", None, "Zainsubani's Notes", "Notes de Zainsubani"),
        ("0558B96A|LegacyoftheDragonborn.esm", "QUST CNAM", 82, "We have finally done it", "Nous avons enfin réussi, et l'entrée se trouvait juste derrière nous depuis le début !"),
        ("0558B96A|LegacyoftheDragonborn.esm", "QUST CNAM", 77, "The explorers will begin their dig", "Les explorateurs vont commencer à creuser sur le site que j'ai marqué. Je devrais revenir dans quelques jours pour voir l'avancement des travaux ou les aider pour accélérer les choses."),
    ]
    for fid, tp, idx, orig_pref, new_s in lotd_qust_fixes:
        apply_entry_fix(
            f_lotd, get_file(f_lotd),
            lambda e, f=fid, t=tp, i=idx, p=orig_pref: e.get("form_id") == f and e.get("type") == t and e.get("index") == i and (e.get("original") or "").startswith(p),
            new_s, cat_c
        )

    # 7. Moonpath to Elsweyr
    f_mp_base = r"Le voyage en Elsweyr\moonpath.esp.json"
    mp_nnam_map = {}
    for e in get_file(f_mp_base):
        if e.get("type") == "QUST NNAM" and (e.get("form_id") or "").endswith("06A8CA|moonpath.esp"):
            mp_nnam_map[e.get("original")] = e.get("string")

    for f_mp in (f_mp_base, f_mp_patch):
        apply_entry_fix(
            f_mp, get_file(f_mp),
            lambda e: (e.get("form_id") or "").endswith("06A8CA|moonpath.esp") and e.get("type") == "QUST CNAM" and e.get("index") == 87,
            "Le gué que j'ai trouvé est profond, mais le Thérium devrait pouvoir le traverser, même si nous devrons porter une grande partie des marchandises nous-mêmes. C'est déjà un progrès. Je ferais mieux d'en informer Ku'rana. Cette jungle semble dangereuse, peuplée d'araignées géantes et de ce qui ressemble à des lézards agressifs.",
            cat_c
        )
    apply_entry_fix(
        f_mp_patch, get_file(f_mp_patch),
        lambda e: e.get("form_id") == "0106A8CA|moonpath.esp" and e.get("type") == "QUST NNAM" and e.get("original") in mp_nnam_map,
        lambda e: mp_nnam_map[e.get("original")],
        cat_c
    )

    # 8. Lucien
    f_lucien = r"Lucien\Lucien.esp.json"
    apply_entry_fix(
        f_lucien, get_file(f_lucien),
        lambda e: e.get("form_id") == "0500AA3A|Lucien.esp" and e.get("type") == "QUST CNAM" and (e.get("original") or "").startswith(";"),
        lambda e: e.get("original"),
        cat_c
    )
    apply_entry_fix(
        f_lucien, get_file(f_lucien),
        lambda e: e.get("form_id") == "052B13ED|Lucien.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 86 and e.get("original", "").startswith("Lucien and I are in Dumzbthar, a Dwemer ruin"),
        "Lucien et moi sommes dans Dumzbthar, une ruine dwemer gouvernée par une intelligence mystérieuse. Nous devrions découvrir ce qui s'y passe exactement.",
        cat_c
    )
    apply_entry_fix(
        f_lucien, get_file(f_lucien),
        lambda e: e.get("form_id") == "052B13ED|Lucien.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 93 and e.get("original", "").startswith("Lucien and I are locked in Dumzbthar"),
        "Lucien et moi sommes enfermés dans Dumzbthar, une ruine dwemer gouvernée par une intelligence daedrique qui semble vouloir nous tuer. Maintenant que nous avons atteint son coeur, je devrais la distraire pendant que Lucien essaie de la désactiver.",
        cat_c
    )

    # 9. Missives
    for f_miss in (
        r"Petites annonces\Missives.esp.json",
        r"Petites annonces\Missives - Falskaar Patch.esp.json",
        r"Petites annonces\Missives - Gray Cowl Patch.esp.json",
        r"Petites annonces\Missives - Heartland.esp.json",
        r"Petites annonces\Missives - Midwood Isle.esp.json",
        r"Petites annonces\Missives - Solstheim.esp.json",
        r"Petites annonces\Missives - Wyrmstooth.esp.json",
    ):
        if os.path.exists(os.path.join(DB_ROOT, f_miss)):
            apply_entry_fix(
                f_miss, get_file(f_miss),
                lambda e: e.get("type") == "QUST NNAM" and e.get("original") == "Collect <Alias=Item>",
                "Récupérez : <Alias=Item>", cat_c
            )

    # 10. Projet OAH Dwarfsphere.esp.json duplicate entries on 058159F6|Dwarfsphere.esp
    f_oah = r"Projet OAH\Dwarfsphere.esp.json"
    oah_first_seen = {}
    for e in get_file(f_oah):
        if e.get("form_id") == "058159F6|Dwarfsphere.esp" and e.get("type") == "QUST CNAM":
            key = (e.get("index"), e.get("original"))
            if key not in oah_first_seen:
                oah_first_seen[key] = e.get("string")
    apply_entry_fix(
        f_oah, get_file(f_oah),
        lambda e: e.get("form_id") == "058159F6|Dwarfsphere.esp" and e.get("type") == "QUST CNAM" and (e.get("index"), e.get("original")) in oah_first_seen,
        lambda e: oah_first_seen[(e.get("index"), e.get("original"))],
        cat_c
    )

    # 11. USSEP Kolbjorn Barrow (0401810B|Dragonborn.esm) + 040209AE + 00096E71 + 05000AD6
    kolbjorn_fixes = {
        (85, "I agreed to fund Ralis Sedarys' expedition to excavate Kolbjorn Barrow. I should visit the site and see how the work is going."):
            "J'ai accepté de financer l'expédition de Ralis Sedarys pour excaver le Tertre de Kolbjorn. Je devrais me rendre sur le site pour voir où en sont les travaux.",
        (83, "I agreed to fund Ralis Sedarys' expedition to excavate Kolbjorn Barrow. He told me to return in a few days to see how work was progressing."):
            "J'ai accepté de financer l'expédition de Ralis Sedarys pour excaver le Tertre de Kolbjorn. Il m'a dit de revenir dans quelques jours pour voir l'avancée des travaux.",
        (87, "I agreed to fund Ralis Sedarys' expedition to excavate Kolbjorn Barrow, but work on the site has stopped. At his request, I dealt with the draugr and found the bodies of the missing miners."):
            "J'ai accepté de financer l'expédition de Ralis Sedarys pour excaver le Tertre de Kolbjorn, mais les travaux ont été interrompus. À sa demande, j'ai éliminé les draugr et retrouvé les corps des mineurs disparus.",
        (74, "I agreed to fund Ralis Sedarys' expedition to excavate Kolbjorn Barrow, but the ongoing draugr attacks means he needs more gold in order to hire more miners and guards to protect them."):
            "J'ai accepté de financer l'expédition de Ralis Sedarys pour excaver le Tertre de Kolbjorn, mais en raison des attaques incessantes de draugr, il a besoin de plus d'or pour engager davantage de mineurs et de gardes pour les protéger.",
        (86, "Ralis Sedarys came to Solstheim hoping to find the Relics of Ahzidal and release their maker from his imprisonment in Kolbjorn Barrow. When he found the barrow buried by the ash, he convinced me to fund its excavation, using the miners as blood sacrifices for his rituals. I saw through his lies and killed him for his crimes."):
            "Ralis Sedarys est venu à Solstheim dans l'espoir de trouver les Reliques d'Ahzidal et de libérer leur créateur emprisonné dans le Tertre de Kolbjorn. Découvrant le tertre enseveli sous les cendres, il m'a convaincu de financer son excavation et a utilisé les mineurs comme sacrifices sanglants pour ses rituels. J'ai percé ses mensonges à jour et je l'ai tué pour ses crimes.",
        (80, "I agreed to continue funding Ralis Sedarys' excavation of Kolbjorn Barrow. He told me to return in a few days to see how work was progressing."):
            "J'ai accepté de continuer à financer Ralis Sedarys et l'excavation du Tertre de Kolbjorn. Il m'a demandé de repasser dans quelques jours après l'avancée des travaux.",
        (89, "I agreed to continue funding Ralis Sedarys' ill-fated excavation of Kolbjorn Barrow, but when I returned to his mining camp, I found only blood and corpses. Ralis himself was nowhere to be seen."):
            "J'ai accepté de continuer à financer la funeste excavation du Tertre de Kolbjorn menée par Ralis Sedarys, mais à mon retour à son campement minier, je n'ai trouvé que du sang et des cadavres. Ralis lui-même était introuvable.",
        (99, "I agreed to fund Ralis Sedarys' ill-fated excavation of Kolbjorn Barrow, but when I returned to his mining camp, I found only blood and corpses. Deep within the barrow, I found Ralis performing a ritual to release Ahzidal, the Dragon Priest that had been sealed there."):
            "J'ai accepté de financer la funeste excavation du Tertre de Kolbjorn menée par Ralis Sedarys, mais à mon retour à son campement minier, je n'ai trouvé que du sang et des cadavres. Au plus profond du tertre, j'ai surpris Ralis en train d'accomplir un rituel visant à libérer Ahzidal, le prêtre-dragon qui y avait été scellé.",
        (84, "I agreed to fund Ralis Sedarys' ill-fated excavation of Kolbjorn Barrow, but when I returned to his mining camp, I found only blood and corpses. Deep within the barrow, I found Ralis performing a ritual that released Ahzidal, a powerful Dragon Priest I fought and defeated."):
            "J'ai accepté de financer la funeste excavation du Tertre de Kolbjorn menée par Ralis Sedarys, mais à mon retour à son campement minier, je n'ai trouvé que du sang et des cadavres. Au plus profond du tertre, j'ai surpris Ralis en train d'accomplir un rituel qui a libéré Ahzidal, un puissant prêtre-dragon que j'ai combattu et vaincu.",
        (88, "Ralis Sedarys came to Solstheim hoping to find the Relics of Ahzidal and release their maker from his imprisonment in Kolbjorn Barrow. When he found the barrow buried by the ash, he convinced me to fund its excavation, using the miners as blood sacrifices for his rituals. I saw through his lies and decided to kill him for his crimes."):
            "Ralis Sedarys est venu à Solstheim dans l'espoir de trouver les Reliques d'Ahzidal et de libérer leur créateur emprisonné dans le Tertre de Kolbjorn. Découvrant le tertre enseveli sous les cendres, il m'a convaincu de financer son excavation et a utilisé les mineurs comme sacrifices sanglants pour ses rituels. J'ai percé ses mensonges à jour et j'ai décidé de le tuer pour ses crimes.",
    }
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "0401810B|Dragonborn.esm" and e.get("type") == "QUST CNAM" and (e.get("index"), e.get("original")) in kolbjorn_fixes,
        lambda e: kolbjorn_fixes[(e.get("index"), e.get("original"))],
        cat_c
    )
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "040209AE|Dragonborn.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 92,
        "J'ai rencontré Lupe Sang-Féroce, qui m'a parlé de son frère Torkild, disparu il y a bien longtemps. Lupe est mort avant que je ne puisse l'aider à découvrir la vérité au sujet de son frère.",
        cat_c
    )
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "00096E71|Skyrim.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 87 and e.get("original") == "We have captured Solitude, killed General Tullius, and destroyed the final bastion of Imperial influence in Skyrim.",
        "Nous avons capturé Solitude, tué le général Tullius et détruit le dernier bastion de l'influence impériale en Bordeciel.",
        cat_c
    )
    apply_entry_fix(
        f_ussep, get_file(f_ussep),
        lambda e: e.get("form_id") == "05000AD6|ccBGSSSE001-Fish.esm" and e.get("type") == "QUST CNAM" and "avoir finir" in (e.get("string") or ""),
        lambda e: e.get("string", "").replace("avoir finir", "avoir fini"),
        cat_c
    )

    # 12. Vigilant 02038524|Vigilant.esm QUST NNAM
    apply_entry_fix(
        f_vig_173, get_file(f_vig_173),
        lambda e: e.get("form_id") == "02038524|Vigilant.esm" and e.get("type") == "QUST NNAM" and e.get("original") == "Talk to the <Alias=Courier>",
        "Parlez à : <Alias=Courier>", cat_c
    )

    # 13. Thieves Guild radiant objectives (Delvin / Vex)
    f_qais = r"Les quêtes restent en Bordeciel\QuestsAreInSkyrimUSSEP.esp.json"
    for f_tg in (f_ayop_tg, f_qais, f_ussep):
        apply_entry_fix(
            f_tg, get_file(f_tg),
            lambda e: e.get("form_id") == "00028922|Skyrim.esm" and e.get("type") == "QUST NNAM" and e.get("original") == "Return <Alias=ItemToGet> to Delvin",
            "Rapportez l'objet à Delvin (<Alias=ItemToGet>)", cat_c
        )
        apply_entry_fix(
            f_tg, get_file(f_tg),
            lambda e: e.get("form_id") in ("0002893B|Skyrim.esm", "0002893E|Skyrim.esm") and e.get("type") == "QUST NNAM" and e.get("original") == "Return the <Alias=ItemtoGet> to Vex",
            "Rapportez l'objet à Vex (<Alias=ItemtoGet>)", cat_c
        )

    # 14. Moon and Star (0200696B / 0600696B|MoonAndStar_MAS.esp)
    f_mas_imm = r"Astre-Lune\MoonAndStar_ImmersionPatch.esp.json"
    f_dbm_mas1 = r"LOTD - Patches officiels\DBM_MAS_Patch.esp.json"
    f_dbm_mas2 = r"LOTD - Patches officiels\dbm_mas_patch.esp.json"
    mas_imm_map = {}
    for e in get_file(f_mas_imm):
        if e.get("type") == "QUST CNAM" and (e.get("form_id") or "").endswith("00696B|MoonAndStar_MAS.esp"):
            mas_imm_map[(e.get("index"), e.get("original"))] = e.get("string")

    for f_m in (f_mas, f_dbm_mas1, f_dbm_mas2):
        if os.path.exists(os.path.join(DB_ROOT, f_m)):
            apply_entry_fix(
                f_m, get_file(f_m),
                lambda e: (e.get("form_id") or "").endswith("00696B|MoonAndStar_MAS.esp") and e.get("type") == "QUST CNAM" and (e.get("index"), e.get("original")) in mas_imm_map,
                lambda e: mas_imm_map[(e.get("index"), e.get("original"))],
                cat_c
            )
    for f_m in (f_mas_imm, f_mas, f_dbm_mas1, f_dbm_mas2):
        if os.path.exists(os.path.join(DB_ROOT, f_m)):
            apply_entry_fix(
                f_m, get_file(f_m),
                lambda e: (e.get("form_id") or "").endswith("00696B|MoonAndStar_MAS.esp") and e.get("type") == "QUST CNAM" and e.get("index") == 102 and (e.get("original") or "").startswith("I found a Writ of Execution"),
                "J'ai trouvé un ordre d'exécution sur un Dunmer appelé Mandyn Hlaalu. Il semble que Mandyn était un assassin de la Morag Tong à la poursuite de nul autre que le Nérévarine, le héros légendaire de Morrowind. Une note au bas de l'ordre suggère que le Nérévarine est passé par une ville appelée Petite Vivec. Si je veux suivre sa trace, je devrais aller y chercher des indices.",
                cat_c
            )
            apply_entry_fix(
                f_m, get_file(f_m),
                lambda e: (e.get("form_id") or "").endswith("00696B|MoonAndStar_MAS.esp") and e.get("type") == "QUST CNAM" and e.get("index") == 106 and (e.get("original") or "").endswith("Maybe we can uncover his trail there."),
                "Un chasseur de primes du nom de Mandyn Hlaalu m'a demandé de l'aider à traquer un criminel connu uniquement sous le nom de « l'Étranger ». La dernière fois que le criminel a été aperçu, il se dirigeait vers le bosquet de Sorcereine. Nous pourrons peut-être y retrouver sa trace.",
                cat_c
            )
            apply_entry_fix(
                f_m, get_file(f_m),
                lambda e: (e.get("form_id") or "").endswith("00696B|MoonAndStar_MAS.esp") and e.get("type") == "QUST CNAM" and e.get("index") == 111 and (e.get("original") or "").endswith("He has suggested we begin our investigation by questioning the locals."),
                "Un chasseur de primes du nom de Mandyn Hlaalu m'a demandé de l'aider à traquer un criminel connu uniquement sous le nom de « l'Étranger ». La dernière fois que le criminel a été aperçu, il se dirigeait vers la petite ville de Rivebois. Il nous a suggéré de commencer notre enquête en interrogeant les habitants.",
                cat_c
            )

    # 15. Whispering Door, Nilheim, BCS_TCIY_Patch, TCIY_Wintersun_Patch
    f_wd = r"La Porte murmurante - Extension de la quête\The Whispering Door - Quest Expansion.esp.json"
    apply_entry_fix(
        f_wd, get_file(f_wd),
        lambda e: e.get("form_id") == "0004A37B|Skyrim.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 114 and e.get("original") == "I decided to give Mephala's Ebony Blade to the Vigilant of Stendarr for safekeeping.",
        "J'ai décidé de confier la Lame d'ébonite de Méphala aux Vigiles de Stendarr pour qu'ils la gardent en lieu sûr.", cat_c
    )

    f_nil = r"Nilheim - Extension de la quête\Nilheim_MiscQuestExpansion.esp.json"
    apply_entry_fix(
        f_nil, get_file(f_nil),
        lambda e: e.get("form_id") == "0001BAEC|Skyrim.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 89 and e.get("original") == "I extorted Telrav.",
        "J'ai extorqué de l'argent à Telrav.", cat_c
    )

    for f_bcs in (
        r"LOTD - Patches officiels\BCS_TCIY_Patch.esp.json",
        r"LOTD - Patches officiels\bcs_tciy_patch.esp.json",
        r"Le choix est vôtre\TCIY_Wintersun_Patch.esp.json",
    ):
        if os.path.exists(os.path.join(DB_ROOT, f_bcs)):
            apply_entry_fix(
                f_bcs, get_file(f_bcs),
                lambda e: e.get("form_id") == "0004D8D6|Skyrim.esm" and e.get("type") == "QUST CNAM" and e.get("index") == 90 and (e.get("original") or "").startswith("I have slain Boethiah's cultists"),
                "J'ai massacré les disciples de Boéthia. Molag Bal devrait être content. Je dois me rendre à son autel à Markarth pour voir s'il m'accorde une récompense pour cette victoire sur son ennemie.", cat_c
            )
            apply_entry_fix(
                f_bcs, get_file(f_bcs),
                lambda e: e.get("form_id") == "0004D8D6|Skyrim.esm" and e.get("type") == "QUST NNAM" and e.get("index") == 20 and e.get("original") == "Slay everyone at <Alias=Dungeon> stealthily",
                "<Alias=Dungeon> : Tuez tout le monde discrètement", cat_c
            )

    # 16. Vanilla / Dawnguard shifted stages in USSEP, Wintersun, Experience Quests Tweak, Nolvus Religion Patch, TCIY
    vanilla_stage_fixes = {
        ("0001F251|Skyrim.esm", "After joining the College of Winterhold and speaking with Tolfdir, I've learned a bit about wards and will soon join my fellow students on a field trip."):
            "Après avoir rejoint l'Académie de Fortdhiver et parlé à Tolfdir, j'ai appris les bases des barrières magiques et je vais accompagner les autres apprentis lors d'une expédition.",
        ("0001F252|Skyrim.esm", "While following Tolfdir through an unexplored section of Saarthal, a vision from the Psijic Order revealed to me that our excavations in Saarthal have set a strange chain of events into motion. I should speak with Tolfdir at once."):
            "En suivant Tolfdir dans un groupe de ruines inexplorées, une vision envoyée par l'Ordre des Psijiques m'a révélé que les fouilles de Saarthal avaient mis un étrange mécanisme en marche. Je dois en avertir Tolfdir.",
        ("0001F252|Skyrim.esm", "While following Tolfdir through an unexplored section of Saarthal, a vision from the Psijic Order has suggested that something strange has been set in motion by our excavations in Saarthal. I need to tell Tolfdir."):
            "En suivant Tolfdir dans un groupe de ruines inexplorées, une vision envoyée par l'Ordre des Psijiques m'a révélé que les fouilles de Saarthal avaient mis un étrange mécanisme en marche. Je dois en avertir Tolfdir.",
        ("0001F7A3|Skyrim.esm", "Windhelm is plagued by a shadowy killer. I have entered Hjerim and should investigate anything of interest."):
            "Vendeaume est en proie à un mystérieux tueur. Je suis entré dans Hjerim et je devrais examiner tout ce qui semble suspect.",
        ("0001F7A3|Skyrim.esm", "Windhelm is plagued by a shadowy killer. Jorleif has given me permission to investigate the crime scenes and search for clues."):
            "Vendeaume est en proie à un mystérieux tueur. Jorleif m'a donné la permission d'enquêter sur le meurtre.",
        ("0002D512|Skyrim.esm", "I met a strange hermit named Septimus Signus, who needed the knowledge of an Elder Scroll and various blood samples to unlock a Dwemer puzzle box he'd been studying for years. I helped him open the box. It didn't contain what he thought it did, instead yielding a work of great knowledge, the Oghma Infinium."):
            "J'ai rencontré un étrange ermite du nom de Septimus Signus, qui avait besoin du savoir d'un Parchemin des Anciens et de divers échantillons de sang pour ouvrir un coffret dwemer qu'il étudiait depuis des années. Je l'ai aidé à l'ouvrir. Il ne contenait pas ce qu'il pensait, mais il y a trouvé une oeuvre de grande érudition, l'Oghma Infinium.",
        ("0003B681|Skyrim.esm", "After escorting Yamarz to Fallowstone Cave and proving myself more worthy, Malacath has commanded me to return to Largashbur and deliver Shagrol's Hammer there."):
            "Après avoir escorté Yamarz jusqu'à la grotte de Rochebrune et m'être montré plus digne que lui, Malacath m'a ordonné de retourner à Largashbur pour y rapporter le marteau de Shagrol.",
        ("0003B681|Skyrim.esm", "Having returned Shagrol's Warhammer and placed it on the altar in Largashbur, the curse has been lifted from the stronghold and I have been named Blood-Kin to the Orcs."):
            "J'ai rapporté le marteau de guerre de Shagrol et je l'ai placé sur l'autel à Largashbur ; la malédiction qui pesait sur la forteresse a été levée et j'ai reçu le titre d'ami à la vie à la mort des Orques.",
        ("0004A37B|Skyrim.esm", "Rumors at the Bannered Mare in Whiterun say that Jarl Balgruuf's children have been acting strangely. In particular, the youngest child, Nelkir, seems to be the most troubled."):
            "D'après les rumeurs qui courent à la Jument pavoisée de Blancherive, les enfants du jarl Balgruuf auraient un comportement étrange. Le plus jeune, Nelkir, semble particulièrement perturbé.",
        ("0004E4E1|Skyrim.esm", "I defeated Sinding in Bloated Man's Grotto and claimed his skin, which Hircine transformed into the Savior's Hide."):
            "J'ai vaincu Sinding dans la grotte du Bouffi et j'ai récupéré sa peau, qu'Hircine a transformée en Peau du Sauveur.",
        ("0004E4E1|Skyrim.esm", "An otherworldly voice coming from Mount Kilkreath is commanding me to find a beacon and return it."):
            "Une voix venue d'un autre monde et émanant du mont Kilkreath m'ordonne de trouver un cristal et de le lui rapporter.",
        ("0007EDE5|Skyrim.esm", "Deliver the forged letter to Camilla Valerius"):
            "Donnez la fausse lettre à Camilla Valerius",
        ("000E4D31|Skyrim.esm", "An accident with the lexicon seems to have left me with some strange knowledge of the Dwemer."):
            "Suite à un accident avec le lexique, il semble que j'aie acquis d'étranges connaissances sur les Dwemers.",
        ("000E4D31|Skyrim.esm", "Septimus Signus used the lexicon I brought him to decipher the Elder Scroll and learn the secret of opening the Dwemer lockbox."):
            "Septimus Signus a utilisé le lexique que je lui ai apporté pour déchiffrer le Parchemin des Anciens et découvrir le secret permettant d'ouvrir le coffret dwemer.",
        ("02004C3D|Dawnguard.esm", "I decided not to give the radiant raiment to Sorine Jurard."):
            "J'ai décidé de ne pas donner l'habit radieux à Sorine Jurard.",
        ("02004C3D|Dawnguard.esm", "I recovered the Dwemer gyro and brought it back to Sorine Jurard."):
            "J'ai récupéré le gyroscope dwemer et l'ai rapporté à Sorine Jurard.",
        ("02004C3D|Dawnguard.esm", "Sorine Jurard has asked me to recover some schematics for a Dwemer crossbow."):
            "Sorine Jurard m'a demandé de récupérer les schémas d'une arbalète dwemer.",
        ("02004C3D|Dawnguard.esm", "With the Moth Priest safely back at Castle Volkihar, the time has come to hear the prophecies contained within the Elder Scroll."):
            "Maintenant que le prêtre de la Phalène est arrivé sain et sauf au château Volkihar, le moment est venu d'entendre les prophéties que renferme le Parchemin des Anciens.",
        ("020098CB|Dawnguard.esm", "I have slain Harkon and ended his tyrannical rule over the Volkihar clan."):
            "J'ai tué Harkon et mis fin à son règne tyrannique sur le clan Volkihar.",
        ("020098CB|Dawnguard.esm", "Harkon's agents have captured the Moth Priest! I have tracked them to Forebears' Holdout, but the vampires have enthralled the Moth Priest and I will have to confront him in order to break their hold."):
            "Les agents d'Harkon ont capturé le prêtre de la Phalène ! J'ai suivi leur trace jusqu'au Refuge des Aïeux, mais les vampires ont subjugué le prêtre de la Phalène et je vais devoir l'affronter pour briser leur emprise.",
        ("020098CB|Dawnguard.esm", "I rescued the Moth Priest from his vampire captors and asked him to meet me at Fort Dawnguard. I must return to Isran and tell him of our success."):
            "J'ai délivré le prêtre de la Phalène des vampires qui le retenaient prisonnier et lui ai demandé de me retrouver au fort de la Garde de l'Aube. Je dois retourner voir Isran pour lui annoncer notre victoire.",
        ("020098CB|Dawnguard.esm", "With the Moth Priest safely back at Fort Dawnguard, he can now read Serana's Elder Scroll and learn more about the prophecy."):
            "Maintenant que le prêtre de la Phalène est de retour sain et sauf au fort de la Garde de l'Aube, il peut lire le Parchemin des Anciens de Sérana et nous en apprendre davantage sur la prophétie.",
        ("02007201|Dawnguard.esm", "<Alias=QuestGiver> learned that a <Alias=Vampire> kidnapped <Alias=Prisoner>. I rescued <Alias.PronounObj=Prisoner> from in <Alias=Dungeon>."):
            "<Alias=QuestGiver> a appris qu'un <Alias=Vampire> avait enlevé <Alias=Prisoner>. Je l'ai secouru dans : <Alias=Dungeon>.",
        ("05000AD6|ccBGSSSE001-Fish.esm", "After using the Dwarven fishing rod near Bronze Water Cave and powering up an ancient mechanism using aetherium dynamo cores, a pedestal rose from beneath the surface revealing a submerged chest."):
            "Après avoir utilisé la canne à pêche dwemer près de la grotte de Bronzeflot et alimenté un ancien mécanisme à l'aide de noyaux de dynamo d'aethérium, un piédestal a émergé de l'eau, révélant un coffre submergé.",
        ("0001DBFC|Skyrim.esm", "I found the body of Reyda in the river near Ivarstead. I should let Narfi know what happened to his sister."):
            "J'ai trouvé le corps de Reyda dans la rivière près de Fort-Ivar. Je devrais annoncer à Narfi ce qui est arrivé à sa sœur.",
    }
    target_vanilla_files = [
        f_ussep,
        f_qais,
        r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        r"Wintersun - Religions de Bordeciel\Wintersun - USSEP Patch.esp.json",
        r"Experience Quests Tweak fr\Experience Quests Tweak.esp.json",
        r"Nolvus Awakening Religion Patch - French\Nolvus Awakening Religion Patch.esp.json",
        r"Le choix est vôtre\TheChoiceIsYours.esp.json",
    ]
    for tvf in target_vanilla_files:
        if os.path.exists(os.path.join(DB_ROOT, tvf)):
            apply_entry_fix(
                tvf, get_file(tvf),
                lambda e: (e.get("form_id"), e.get("original")) in vanilla_stage_fixes and e.get("type") in ("QUST CNAM", "QUST NNAM"),
                lambda e: vanilla_stage_fixes[(e.get("form_id"), e.get("original"))],
                cat_c
            )
            # Also check any other QUST CNAM in USSEP 02004C3D / 020098CB / 000E4D31 where canonical DB has a better translation
            apply_entry_fix(
                tvf, get_file(tvf),
                lambda e: e.get("form_id") in ("02004C3D|Dawnguard.esm", "020098CB|Dawnguard.esm", "000E4D31|Skyrim.esm", "0004A37B|Skyrim.esm")
                and e.get("type") == "QUST CNAM"
                and len(canonical_counts[(e.get("type"), e.get("original"))]) > 1
                and e.get("string") != canonical_counts[(e.get("type"), e.get("original"))].most_common(1)[0][0],
                lambda e: canonical_counts[(e.get("type"), e.get("original"))].most_common(1)[0][0],
                cat_c
            )

    # 17. Creation Club Shifted Quests
    f_naei_bad = r"Nolvus Awakening Experience Integration - French\Nolvus Awakening Experience Integration.esp.json"
    f_naei_good = r"Nolvus Awakening Experience Integration.esp - French\nolvus awakening experience integration.esp.json"
    f_cc_exp = r"CCQuest - Experience Patch.esp - French\ccquest - experience patch.esp.json"
    f_cci_ae = r"Creation Club Integration - Armours - French\creation club integration - anniversary edition.esp.json"
    f_dbm_bos = r"LOTD - Patches du Creation Club\DBM_CC_TheBowOfShadowsHOWPatch.esp.json"

    naei_good_map = {}
    for e in get_file(f_naei_good):
        if e.get("type") in ("QUST CNAM", "QUST NNAM"):
            naei_good_map[(e.get("type"), e.get("index"), e.get("original"))] = e.get("string")
            naei_good_map[(e.get("type"), e.get("original"))] = e.get("string")

    # Align Nolvus Awakening Experience Integration (upper-case folder) with the clean lower-case folder
    apply_entry_fix(
        f_naei_bad, get_file(f_naei_bad),
        lambda e: e.get("type") in ("QUST CNAM", "QUST NNAM") and (e.get("type"), e.get("index"), e.get("original")) in naei_good_map,
        lambda e: naei_good_map[(e.get("type"), e.get("index"), e.get("original"))],
        cat_c
    )

    # Fix 050990EF|ccasvsse001-almsivi.esm idx=81 & 2000089E|ccbgssse043-crosselv.esl idx=67 & 5 other CC quests across all 3 CC Experience files
    cc_extra_fixes = [
        ("0990ef|ccasvsse001-almsivi.esm", 81, "I found an Unenchanted Weapon", "J'ai trouvé une arme non enchantée et je l'ai placée dans un emplacement spécial de la forge dwemer. Une fois l'alimentation de la forge rétablie, elle devrait enchanter l'arme."),
        ("00089e|ccbgssse043-crosselv.esl", 67, "I found a letter penned by Kragrash", "J'ai trouvé une lettre écrite par Kragrash, le chasseur de vampires. Au cours d'une chasse, il a été blessé et a contracté le vampirisme. Le jour où il devait se transformer en vampire, il est allé dans les montagnes pour contempler un dernier lever de soleil. Il a laissé son équipement dans sa cave, qui reste verrouillée. La lettre indique que la clé de sa cave devrait se trouver sur sa dépouille."),
        ("000cc3|ccasvsse001-almsivi.esm", 84, "After finding information on a group of Tribunal heretics", "Après avoir trouvé des informations sur un groupe d'hérétiques du Tribunal, j'ai suivi leur piste jusqu'à un temple caché rempli d'adorateurs. En lisant une note écrite par la matriarche, j'ai appris l'existence de plusieurs activités à l'extérieur du temple sur lesquelles je peux enquêter."),
        ("19952a|ccbgssse067-daedinv.esm", 97, "I found the Oblivion Gate and defeated the leader of the Mythic Dawn, Vonos", "J'ai trouvé la porte d'Oblivion et vaincu le chef de l'Aube mythique, Vonos. Il semble qu'il s'agissait d'un rituel complexe conçu pour me tromper, et dont la mort de Vonos était l'étape finale. Sans le vouloir, j'ai servi la cause de Mehrunes Dagon et mes actions ont ouvert la porte d'Oblivion. J'ai franchi la porte et vaincu un drémora Valkynaz maniant l'arme Tourment."),
        ("000a39|ccafdsse001-dwesanctuary.esm", 91, "I provided the dwarven sphere overseer", "J'ai fourni les pièces requises à la sphère dwemer superviseuse et je peux désormais remettre la manufacture en service. Je devrais pouvoir utiliser la manufacture pour restaurer le sanctuaire grâce aux automates qui peuvent y être construits."),
        ("00088c|ccedhsse003-redguard.esl", 90, "I spoke the secret phrase to Josla", "J'ai prononcé la phrase secrète devant Josla, une espionne des Revenants à Karthwasten. Elle m'a remis une note qui devrait contenir des informations sur l'endroit où est détenu l'agent des Revenants capturé."),
        ("000a90|cckrtsse001_altar.esl", 86, "I received a letter from a rogue asking me to perform a job Markarth", "J'ai reçu une lettre d'un voleur me demandant d'accomplir un travail à Markarth. À l'aide d'un anneau à cacheter dérobé à un Haut-Elfe, j'ai falsifié une lettre et me suis fait passer pour un messager afin de piéger son garde du corps. Après la mort de son compagnon, le Haut-Elfe s'est réfugié dans sa chambre forte pour vérifier sa fortune. Je l'ai suivi à l'intérieur et ai accédé à la chambre forte, où j'ai affronté l'Altmer. Par la suite, j'ai parlé au voleur qui m'a remis une récompense."),
    ]
    for f_cc in (f_cc_exp, f_naei_bad, f_naei_good):
        for fid_suf, idx_val, orig_pref, new_fr in cc_extra_fixes:
            apply_entry_fix(
                f_cc, get_file(f_cc),
                lambda e, fs=fid_suf, iv=idx_val, op=orig_pref: (e.get("form_id") or "").lower().endswith(fs) and e.get("type") == "QUST CNAM" and e.get("index") == iv and (e.get("original") or "").startswith(op),
                new_fr, cat_c
            )

    # Align Creation Club Integration - Armours and DBM_CC_TheBowOfShadowsHOWPatch with canonical CC translations
    apply_entry_fix(
        f_cci_ae, get_file(f_cci_ae),
        lambda e: e.get("type") in ("QUST CNAM", "QUST NNAM") and (e.get("type"), e.get("original")) in naei_good_map,
        lambda e: naei_good_map[(e.get("type"), e.get("original"))],
        cat_c
    )
    apply_entry_fix(
        f_cci_ae, get_file(f_cci_ae),
        lambda e: (e.get("form_id") or "").lower().endswith("000830|ccbgssse055-ba_orcishscaled.esl") and e.get("type") == "QUST CNAM" and e.get("index") == 72 and (e.get("original") or "").endswith("whereabouts."),
        "J'ai entendu parler d'histoires concernant d'anciens bandits vivant comme des fugitifs à travers Tamriel. Si je me rends aux baraquements des gardes de Faillaise, je trouverai peut-être des informations sur l'endroit où ils se cachent.",
        cat_c
    )
    apply_entry_fix(
        f_dbm_bos, get_file(f_dbm_bos),
        lambda e: e.get("type") == "QUST CNAM" and (e.get("type"), e.get("original")) in naei_good_map,
        lambda e: naei_good_map[(e.get("type"), e.get("original"))],
        cat_c
    )

    # 18. Additional MESG ITXT, PERK EPF2, QUST NNAM, and Paragliding fixes
    f_para = r"Du parapente en Bordeciel\Paragliding.esp.json"
    apply_entry_fix(
        f_para, get_file(f_para),
        lambda e: e.get("form_id") == "0200801F|Paragliding.esp" and e.get("type") == "QUST CNAM" and e.get("index") == 82,
        "Comme je prends quotidiennement des décisions moralement discutables, il y a de fortes chances que je garde ce parapente pour mon usage personnel, malgré la possibilité bien réelle que Fred ait de la famille dans les environs pour qui cet objet aurait une grande valeur sentimentale. Par ailleurs, le fait que ma prise de possession soudaine des biens de Fred coïncide avec sa mort violente — dont j'ai été le seul témoin, faisant de moi la dernière personne à l'avoir vu en vie — et puisse éveiller les soupçons des gardes ne m'inquiète absolument pas. Quoi qu'il en soit, j'ai hâte de voler. Merci, Fred !",
        cat_c
    )
    apply_entry_fix(
        f_crf, get_file(f_crf),
        lambda e: e.get("form_id") == "000266F1|Skyrim.esm" and e.get("type") == "QUST NNAM" and e.get("original") == "Find <Alias=MGR01Item>",
        "Trouvez : <Alias=MGR01Item>", cat_c
    )
    apply_entry_fix(
        f_pos, get_file(f_pos),
        lambda e: e.get("form_id") == "0A000BA3|PathOfSorcery.esp" and e.get("type") == "PERK EPF2" and e.get("original") == "Access Inventory",
        "Accéder à l’inventaire", cat_c
    )
    f_vok_blk_epf = r"Vokriinateur - Morceaux choisis\Vokriinator Black.esp.json"
    apply_entry_fix(
        f_vok_blk_epf, get_file(f_vok_blk_epf),
        lambda e: e.get("form_id") == "07000BA3|PathOfSorcery.esp" and e.get("type") == "PERK EPF2" and e.get("original") == "Access Inventory",
        "Accéder à l’inventaire", cat_c
    )
    apply_entry_fix(
        f_oah, get_file(f_oah),
        lambda e: e.get("form_id") == "05091126|Dwarfsphere.esp" and e.get("type") == "MESG ITXT" and e.get("original") == "Nchardak",
        "Nchardak", cat_c
    )
    f_yot_aho = r"YOT - Vos propres pensées\YOT - Project AHO.esp.json"
    apply_entry_fix(
        f_yot_aho, get_file(f_yot_aho),
        lambda e: e.get("form_id") == "04091126|Dwarfsphere.esp" and e.get("type") == "MESG ITXT" and e.get("original") == "Nchardak",
        "Nchardak", cat_c
    )
    f_yot_lotd_itxt = r"YOT - Vos propres pensées\YOT - LOTD.esp.json"
    apply_entry_fix(
        f_yot_lotd_itxt, get_file(f_yot_lotd_itxt),
        lambda e: e.get("form_id") == "033D4CA8|LegacyoftheDragonborn.esm" and e.get("type") == "MESG ITXT" and e.get("original") == "Yes",
        "Oui", cat_c
    )
    f_yot_vig_itxt = r"YOT - Vos propres pensées\YOT - Vigilant.esp.json"
    apply_entry_fix(
        f_yot_vig_itxt, get_file(f_yot_vig_itxt),
        lambda e: e.get("type") == "MESG ITXT" and e.get("original") == "Strike" and e.get("string") == "Annuler",
        "Frapper", cat_c
    )
    for f_sac in (
        r"Sacrosanct - Vampires de Bordeciel\Sacrosanct - Vampires of Skyrim.esp.json",
        r"YOT - Vos propres pensées\YOT - Sacrosanct.esp.json",
    ):
        apply_entry_fix(
            f_sac, get_file(f_sac),
            lambda e: e.get("form_id") == "02009407|Dawnguard.esm" and e.get("type") == "MESG ITXT" and e.get("original") == "Protean Fury",
            "Fureur protéiforme", cat_c
        )

    # =========================================================================
    # CATEGORY D: Gameplay Numeric & Effect Discrepancies
    # =========================================================================
    cat_d = "Catégorie D : Écarts numériques & mécaniques de gameplay (Atouts, Sorts, Effets, Objets)"

    # 1. Abyss
    f_abyss = r"Abyss - Sorts obscurs\Abyss.esp.json"
    apply_entry_fix(
        f_abyss, get_file(f_abyss),
        lambda e: e.get("form_id") == "04000BE2|Abyss.esp" and e.get("type") == "MGEF DNAM",
        "Crée un mur qui inflige <mag> points de dégâts magiques par seconde et réduit la résistance à la magie de 10 % pendant 5 secondes.",
        cat_d
    )

    # 2. Adamant
    f_adam = r"Adamant - Refonte des atouts\Adamant.esp.json"
    apply_entry_fix(
        f_adam, get_file(f_adam),
        lambda e: e.get("form_id") == "06000A0E|Adamant.esp" and e.get("type") == "PERK DESC",
        "Lorsque vous êtes équipé d'un sort de glace, vous réduisez la résistance à la glace de tous les ennemis proches jusqu'à 100 %.",
        cat_d
    )
    apply_entry_fix(
        f_adam, get_file(f_adam),
        lambda e: e.get("form_id") == "06000A1A|Adamant.esp" and e.get("type") == "PERK DESC",
        "Lorsque vous êtes équipé d'un sort de poison, vous réduisez la résistance au poison de tous les ennemis proches jusqu'à 100 %.",
        cat_d
    )

    # 3. Armurerie du Roi Croisé
    f_dcr = r"Armurerie du Roi Croisé\DCR_KingCrusaderMegaPack_SSE.esp.json"
    apply_entry_fix(
        f_dcr, get_file(f_dcr),
        lambda e: e.get("form_id") == "0200084F|DCR_KingCrusaderMegaPack_SSE.esp" and e.get("type") == "SPEL DESC",
        "Abat sur votre ennemi une tempête pestilentielle de 2 sauterelles, pendant 30 secondes et dans un rayon de 15 mètres.",
        cat_d
    )

    # 4. Bruma (BSHeartland)
    apply_entry_fix(
        f_bsh, get_file(f_bsh),
        lambda e: e.get("form_id") == "0207233A|BSHeartland.esm" and e.get("type") == "MGEF DNAM",
        "Une boule de neige enflammée qui explose et inflige 22 points de dégâts de glace et 22 points de dégâts de feu. Endommage la santé et la vigueur du lanceur. Les cibles enflammées subissent des dégâts supplémentaires.",
        cat_d
    )
    apply_entry_fix(
        f_bsh, get_file(f_bsh),
        lambda e: e.get("form_id") == "02072331|BSHeartland.esm" and e.get("type") == "MGEF DNAM",
        "Une rafale de feu enneigé qui inflige 13 points de dégâts de glace et 13 points de dégâts de feu à l'impact. Endommage la santé et la vigueur du lanceur. Les cibles enflammées subissent des dégâts supplémentaires.",
        cat_d
    )

    # 5. Carved Brink
    f_cb = r"Carved Brink\Haem Projects Goblands.esp.json"
    apply_entry_fix(
        f_cb, get_file(f_cb),
        lambda e: e.get("form_id") == "052778DE|Haem Projects Goblands.esp" and e.get("type") == "MGEF DNAM",
        "Une explosion empoisonnée qui inflige <mag> points de dégâts dans un rayon de 4,5 mètres. Les cibles empoisonnées subissent des dégâts supplémentaires.",
        cat_d
    )

    # 6. Commerce & Troc
    f_tb = r"Commerce & Troc\trade & barter.esp.json"
    apply_entry_fix(
        f_tb, get_file(f_tb),
        lambda e: e.get("form_id") == "06002877|Trade & Barter.esp" and e.get("type") == "PERK DESC",
        "Les prix dans les grandes villes sont 10 % plus élevés que dans les petits villages.\r\n(6-7) Corberoc et Solstheim.",
        cat_d
    )
    apply_entry_fix(
        f_tb, get_file(f_tb),
        lambda e: e.get("form_id") == "06003341|Trade & Barter.esp" and e.get("type") == "PERK DESC",
        "Les prix varient en fonction de votre race et de celle du marchand avec qui vous commercez. Toutefois, si vous êtes son ami ou son supérieur, le marchand ignorera alors la race.\r\n\r\nCet atout couvre les marchands nordiques (0-4), altmers (7-8), impériaux (9) et orques (5-6).",
        cat_d
    )
    apply_entry_fix(
        f_tb, get_file(f_tb),
        lambda e: e.get("form_id") == "06005E65|Trade & Barter.esp" and e.get("type") == "PERK DESC",
        "Les prix varient en fonction de votre race et de celle du marchand avec qui vous commercez. Toutefois, si vous êtes son ami ou son supérieur, le marchand ignorera alors la race.\r\n\r\nCet atout couvre les marchands argoniens, bosmers, brétons et dunmers (8-12).",
        cat_d
    )
    apply_entry_fix(
        f_tb, get_file(f_tb),
        lambda e: e.get("form_id") == "06005E66|Trade & Barter.esp" and e.get("type") == "PERK DESC",
        "Les prix varient en fonction de votre race et de celle du marchand avec qui vous commercez. Toutefois, si vous êtes son ami ou son supérieur, le marchand ignorera alors la race.\r\n\r\nCet atout couvre les marchands khajiits (0-1) et rougegardes (2-4).",
        cat_d
    )

    # 7. Enfant du Tonnerre
    f_thun = r"Enfant du Tonnerre - Immersion et Cris épiques\Thunderchild - Epic Shout Package.esp.json"
    apply_entry_fix(
        f_thun, get_file(f_thun),
        lambda e: e.get("form_id") == "0438083C|Thunderchild - Epic Shout Package.esp" and e.get("type") == "MESG DESC",
        "Enfant du tonnerre - Mis à jour en version 3.25 !",
        cat_d
    )

    # 8. Fanatical Enemies
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") == "044A15C6|Fanatical Enemies.esp" and e.get("type") == "PERK DESC",
        "20 % de chances de porter un coup critique infligeant 50 % de dégâts critiques supplémentaires.",
        cat_d
    )
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") == "044A15C7|Fanatical Enemies.esp" and e.get("type") == "PERK DESC",
        "15 % de chances de porter un coup critique infligeant 25 % de dégâts critiques supplémentaires.",
        cat_d
    )
    apply_entry_fix(
        f_fan, get_file(f_fan),
        lambda e: e.get("form_id") in ("04DF23AC|Fanatical Enemies.esp", "04DFC5CE|Fanatical Enemies.esp") and e.get("type") == "MGEF DNAM",
        "Une explosion de lumière solaire qui inflige <mag> points de dégâts aux morts-vivants dans un rayon de 15 pieds.",
        cat_d
    )

    # 9. FlamingStrike
    f_flam = r"FlamingStrike.esp - French\flamingstrike.esp.json"
    apply_entry_fix(
        f_flam, get_file(f_flam),
        lambda e: e.get("form_id") == "01000807|FlamingStrike.esp" and e.get("type") == "MGEF DNAM",
        "Brûle la cible et inflige <mag> points de dégâts par seconde. Les cibles en feu subissent des dégâts supplémentaires.",
        cat_d
    )

    # 10. Growl
    f_growl = r"Grognement - Lycanthropes de Bordeciel\Growl - Werebeasts of Skyrim.esp.json"
    apply_entry_fix(
        f_growl, get_file(f_growl),
        lambda e: e.get("form_id") == "02007A3F|Dawnguard.esm" and e.get("type") == "PERK DESC",
        "Vos attaques infligent 30 % de dégâts supplémentaires lorsque vous êtes sous forme bestiale.",
        cat_d
    )
    apply_entry_fix(
        f_growl, get_file(f_growl),
        lambda e: e.get("form_id") == "020059A4|Dawnguard.esm" and e.get("type") == "PERK DESC",
        "Vos attaques infligent 20 % de dégâts supplémentaires lorsque vous êtes sous forme bestiale.",
        cat_d
    )
    apply_entry_fix(
        f_growl, get_file(f_growl),
        lambda e: e.get("form_id") == "02011CFB|Dawnguard.esm" and e.get("type") == "PERK DESC",
        "Vos attaques infligent 50 % de dégâts supplémentaires lorsque vous êtes sous forme bestiale.",
        cat_d
    )

    # 11. UndeathFixes dummy perk
    apply_entry_fix(
        f_und_fix, get_file(f_und_fix),
        lambda e: e.get("form_id") == "043326D5|Undeath.esp" and e.get("type") == "PERK DESC",
        "La description est fausse. Il s’agit d’un atout factice utilisé en interne pour vérifier si le joueur est devenu une liche ou non.",
        cat_d
    )

    # 12. ISC
    f_isc = r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json"
    apply_entry_fix(
        f_isc, get_file(f_isc),
        lambda e: e.get("form_id") == "0001EA76|Skyrim.esm" and e.get("type") == "MGEF DNAM",
        "Les cibles ne fuient pas pendant <dur> secondes et reçoivent un bonus de santé et de vigueur.",
        cat_d
    )
    apply_entry_fix(
        f_isc, get_file(f_isc),
        lambda e: e.get("form_id") == "0001EA79|Skyrim.esm" and e.get("type") == "MGEF DNAM",
        "La cible ne fuit pas pendant <dur> secondes et reçoit un bonus de santé et de vigueur.",
        cat_d
    )

    # 13. La Voie du Sorcier (PathOfSorcery & PoS_NecromanticGrimoire_Patch)
    pos_fixes = {
        "00058F7C|Skyrim.esm": "Les gemmes spirituelles fournissent 50 % de magie supplémentaire pour recharger.",
        "00058F7E|Skyrim.esm": "Les enchantements de compétences sur les armures et les vêtements sont 20 % plus puissants et font progresser les compétences 10 % plus vite lorsqu'ils sont portés. Ne se cumule pas pour les objets ayant le même type d'enchantement.",
        "000C367C|Skyrim.esm": "Les nouveaux enchantements sont 0,75 % plus puissants par niveau de compétence en enchantement.",
        "000CB41A|Skyrim.esm": "Les Atronachs conjurés sont plus puissants et ont accès à des sorts de plus haut niveau.",
        "000D7999|Skyrim.esm": "Si vous ne portez pas d'armure, les sorts d'armure sont deux fois plus puissants et confèrent 2 % de chances de ne subir aucun dégât lors d'une attaque.",
        "000D799A|Skyrim.esm": "Si vous ne portez pas d'armure, les sorts d'armure sont 2,5 fois plus puissants et confèrent 5 % de chances de ne subir aucun dégât lors d'une attaque.",
        "000D799B|Skyrim.esm": "Si vous ne portez pas d'armure, les sorts d'armure sont trois fois plus puissants et confèrent 9 % de chances de ne subir aucun dégât lors d'une attaque.",
        "00108A44|Skyrim.esm": "Les coups de grâce portés aux créatures et aux personnes capturent 10 % de l'âme de la victime, permettant de recharger l'arme.",
        "0A000BB5|PathOfSorcery.esp": "Les sorts coûtent de la santé au lieu de la magie. Votre santé maximale est augmentée de 50 % de votre réserve de magie (Novice = 8 PV, Apprenti = 12 PV, Spécialiste = 20 PV, Expert = 30 PV, Maître = 42 PV). N'a aucun effet sous forme de Seigneur vampire.",
        "0A000BC6|PathOfSorcery.esp": "Les personnes et les créatures alliées à moins de 10 mètres récupèrent 3 points de santé par seconde.",
        "0A000BCF|PathOfSorcery.esp": "Quand vous avez une arme liée équipée, vous avez 30 % de chances de devenir éthéré pendant 2 secondes quand votre adversaire effectue une attaque puissante.",
        "0A000C27|PathOfSorcery.esp": "La fabrication de parchemins produit désormais 1 parchemin supplémentaire et rend une gemme spirituelle vide.",
        "0A000C2D|PathOfSorcery.esp": "Vous subissez 25 % de dégâts en moins des attaques magiques lorsque vous lancez ou incantez un sort. Cette protection passe à 50 % pendant un double lancer ou l'incantation d'un sort de rituel.",
        "0A000C2F|PathOfSorcery.esp": "Alignez-vous avec la Tempête, délaissant l'Hiver et le Brasier. Tant qu'un sort de foudre est équipé, votre magie se régénère plus vite ; lancer des sorts de foudre augmente brièvement votre vitesse. Octroie le pouvoir « Tempête d'éclairs ». (Une seule maîtrise élémentale possible)",
        "0A000C30|PathOfSorcery.esp": "Alignez-vous avec le Brasier, délaissant l’Hiver et la Tempête. Tant qu’un sort de feu est équipé, votre santé se régénère plus vite ; lancer des sorts de feu augmente brièvement vos dégâts de feu. Octroie le pouvoir « Pluie de météores ». (Une seule maîtrise élémentale possible)",
    }
    apply_entry_fix(
        f_pos, get_file(f_pos),
        lambda e: e.get("form_id") in pos_fixes and e.get("type") == "PERK DESC",
        lambda e: pos_fixes[e.get("form_id")],
        cat_d
    )
    f_pos_ng = r"La Voie du Sorcier\PoS_NecromanticGrimoire_Patch.esp.json"
    apply_entry_fix(
        f_pos_ng, get_file(f_pos_ng),
        lambda e: e.get("form_id") == "02000821|ccvsvsse003-necroarts.esl" and e.get("type") == "MGEF DNAM",
        "Invoque pendant <dur> secondes un gardien de tombeau qui conjure une ombre lorsqu’il tue un ennemi.",
        cat_d
    )

    # 14. LOTD numeric/gameplay fixes
    lotd_num_fixes = {
        ("05699107|LegacyoftheDragonborn.esm", "SPEL DESC"):
            "Une fois toutes les 12 heures, octroie une chance de déverrouiller les serrures jusqu'au niveau expert avec la Clé d'Aleksey. La chance est basée sur votre niveau d'archéologie.",
        ("05236C5D|LegacyoftheDragonborn.esm", "WEAP DESC"):
            "Inflige 36 points de dégâts de glace et de foudre chacun en 6 secondes. La cible est également ralentie pendant 6 secondes.",
        ("05236C5F|LegacyoftheDragonborn.esm", "WEAP DESC"):
            "Vous avez une chance de paralyser la cible pendant 6 secondes, et infligez 6 points de dégâts de poison et de glace chacun pendant 6 secondes.",
        ("05119268|LegacyoftheDragonborn.esm", "MESG DESC"):
            "Le sextant de Schneider peut être utilisé depuis votre inventaire pour localiser la relique d'intérêt la plus proche.",
        ("0512E455|LegacyoftheDragonborn.esm", "MESG DESC"):
            "Vous devez attendre au moins 2 heures avant de pouvoir réutiliser le sextant.",
    }
    apply_entry_fix(
        f_lotd, get_file(f_lotd),
        lambda e: (e.get("form_id"), e.get("type")) in lotd_num_fixes,
        lambda e: lotd_num_fixes[(e.get("form_id"), e.get("type"))],
        cat_d
    )

    # 15. Marché de Rivebois en bazar
    f_riv = r"Marché de Rivebois en bazar\Riverwood Trader Is A Mess.esp.json"
    apply_entry_fix(
        f_riv, get_file(f_riv),
        lambda e: e.get("form_id") == "05000818|Riverwood Trader Is A Mess.esp" and e.get("type") == "MESG DESC",
        "Après 6 heures passées à aider Lucan, vous avez réussi à ranger toute la boutique avec lui.",
        cat_d
    )

    # 16. Ordinator - No Timed Block & Ordinator Reworked
    f_ontb = r"Ordinator - No Timed Block\ordinator - no timed block.esp.json"
    apply_entry_fix(
        f_ontb, get_file(f_ontb),
        lambda e: e.get("form_id") == "03008B33|Ordinator - Perks of Skyrim.esp" and e.get("type") == "PERK DESC",
        "Une frappe puissante avec une arme exaspère les cibles vivantes pendant 30 secondes. Elles ne fuient pas le combat, mais elles ne peuvent régénérer leur vigueur et en perdent 15 points par seconde. Vous subissez 30 % de dégâts en moins lorsque vous bloquez leurs attaques pendant cette durée.",
        cat_d
    )

    f_ondpa = r"Ordinator Reworked - Combat Mod Compatibility\ordinator - no directional power attacks - balanced.esp.json"
    ondpa_fixes = {
        "01002E05|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à l'épée éjectent les cibles jusqu'à 2 mètres, infligeant jusqu'à 40 % de dégâts supplémentaires d'après la distance parcourue.",
        "010B0D40|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la dague ont 20 % de chances de paralyser la cible pendant 10 secondes. Vos attaques contre la cible paralysée lui infligent un nonuple coup critique.",
        "01012846|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à l'espadon fatiguent une cible, arrêtant sa régénération pendant 3 secondes. De plus, il y a 30 % de chances d'absorber 150 points de magie et de vigueur.",
    }
    apply_entry_fix(
        f_ondpa, get_file(f_ondpa),
        lambda e: e.get("form_id") in ondpa_fixes and e.get("type") == "PERK DESC",
        lambda e: ondpa_fixes[e.get("form_id")],
        cat_d
    )

    # 17. Ordonnateur - Atouts de Bordeciel
    f_ord = r"Ordonnateur - Atouts de Bordeciel\Ordinator - Perks of Skyrim.esp.json"
    ord_fixes = {
        "000581DE|Skyrim.esm":
            "Les morts-vivants réanimés infligent 200 % de dégâts d'attaque supplémentaires pendant 15 secondes après leur réanimation. La limite de niveau des sorts et effets de réanimation est augmentée de 1 % par niveau de conjuration.",
        "000F3F0E|Skyrim.esm":
            "Les sorts de foudre laissant au moins 75 % de santé à leur cible infligent des dégâts de foudre supplémentaires pour compenser la différence.",
        "03003E8C|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes vers l'avant à l'espadon qui laisseraient la santé de la cible au-dessus de 60 % infligent suffisamment de dégâts pour compenser la différence.",
        "03014362|Ordinator - Perks of Skyrim.esp":
            "En combat, Flamme du guerrier touche périodiquement une cible au hasard dans un rayon de 30 mètres, vous y compris. Les cibles alliées sont bénies, régénérant 20 points de magie et de vigueur pendant 5 secondes. Les cibles hostiles sont maudites et perdent le même montant.",
        "030153EA|Ordinator - Perks of Skyrim.esp":
            "Si vous recevez un sort ou un effet de soin alors que votre santé est pleine, il vous sursoigne, renforçant votre santé de 1 point par niveau de Guérison pendant 20 secondes.",
        "03016436|Ordinator - Perks of Skyrim.esp":
            "Si un mort-vivant réanimé est détruit dans les 20 secondes, l'assaillant est maudit par une maladie daedrique qui inflige 40 points de dégâts par seconde pendant 20 secondes. Ceux possédant cet atout sont immunisés.",
        "0302CB20|Ordinator - Perks of Skyrim.esp":
            "Lancez des sorts comme les anciens mages. Vos 20 prochains sorts n'utilisent pas de magie et sont deux fois plus efficaces. Quand vous tombez à court de sorts, vous ne pouvez plus en lancer jusqu'à ce que vous vous reposiez en dormant à la taverne ou chez vous.",
        "0302D086|Ordinator - Perks of Skyrim.esp":
            "Votre Flamme du guerrier porte l'essence de la mort. Les morts-vivants ennemis maudits subissent 30 points de dégâts par seconde.",
        "0303173E|Ordinator - Perks of Skyrim.esp":
            "Vous accorde le pouvoir \"Appât\". À volonté, attire la cible hostile la plus proche dans un rayon de 20 mètres vers le piège à ours le plus proche, présent dans un rayon de 15 mètres (excepté en combat ou pendant les dialogues). Dure 30 secondes.",
        "03035E3D|Ordinator - Perks of Skyrim.esp":
            "Exécuter une roulade silencieuse augmente les dégâts des armes de 40 % et à mains nues de 40 points pendant 3 secondes.",
        "03038484|Ordinator - Perks of Skyrim.esp":
            "Les parchemins sont 2 % plus puissants ou durent 4 % plus longtemps par niveau d'Enchantement.",
        "0303E173|Ordinator - Perks of Skyrim.esp":
            "Pendant les 20 secondes suivant l'utilisation du laboratoire d'alchimie, les potions bénéfiques bues durent 15 fois plus longtemps et sont 25 % plus puissantes.",
        "0303ECB5|Ordinator - Perks of Skyrim.esp":
            "Les parchemins sont 4 % plus puissants ou durent 8 % plus longtemps par niveau d'Enchantement.",
        "030587A0|Ordinator - Perks of Skyrim.esp":
            "Vous créez des canons dwemers à la forge ou à l'enclume. Le pouvoir \"Canon automatique dwemer\" les déploie. Ils tirent sur les mêmes cibles que vous pendant 60 secondes, infligeant des dégâts égaux à 40 % de votre niveau de Forgeage, si vous êtes dans un rayon de 4 mètres.",
        "03061988|Ordinator - Perks of Skyrim.esp":
            "En combat, manier une arme à deux mains a 10 % de chances d'augmenter votre vitesse d'attaque de 175 % pendant 3 secondes.",
        "030842DD|Ordinator - Perks of Skyrim.esp":
            "Vous êtes un adepte de la dissimulation dans l'angle mort de votre victime. La furtivité est 15 % plus efficace dans un rayon de 10 mètres et 30 % plus efficace dans un rayon de 5 mètres.",
        "031C253E|Ordinator - Perks of Skyrim.esp":
            "Les parchemins sont 6 % plus puissants ou durent 12 % plus longtemps par niveau d'Enchantement.",
    }
    apply_entry_fix(
        f_ord, get_file(f_ord),
        lambda e: e.get("form_id") in ord_fixes and e.get("type") == "PERK DESC",
        lambda e: ord_fixes[e.get("form_id")],
        cat_d
    )

    # 18. SPERG
    f_sperg = r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json"
    sperg_fixes = {
        "04039110|SPERG-SSE.esp":
            "Les sorts de feu infligent 10 % de dégâts supplémentaires à la santé, les sorts de glace infligent 50 % de dégâts supplémentaires à la vigueur et les sorts de foudre infligent deux fois plus de dégâts à la magie.",
        "04044216|SPERG-SSE.esp":
            "Les sorts de destruction infligent 50 % de dégâts supplémentaires, mais coûtent 50 points de magie de plus à lancer.",
        "04007A94|SPERG-SSE.esp":
            "Les attaques puissantes à deux armes infligent 25 % de dégâts supplémentaires et les attaques à deux armes sont 25 % plus rapides.",
    }
    apply_entry_fix(
        f_sperg, get_file(f_sperg),
        lambda e: e.get("form_id") in sperg_fixes and e.get("type") in ("PERK DESC", "MGEF DNAM"),
        lambda e: sperg_fixes[e.get("form_id")],
        cat_d
    )

    # 19. UNSLAAD
    f_uns = r"UNSLAAD SE -voiced english- vostFR\Unslaad.esm.json"
    uns_fixes = {
        "0327716F|Unslaad.esm": "Quand la santé tombe en dessous de 30 %, la valeur d'armure augmente de 50 %.",
        "0327716E|Unslaad.esm": "Quand la santé tombe en dessous de 30 %, les dégâts infligés augmentent de 50 %.",
        "03008A63|Unslaad.esm": "Les sorts de froid infligent 30 % de dégâts supplémentaires.",
        "0341E378|Unslaad.esm": "Le temps entre les Cris est augmenté de 25 %.",
    }
    apply_entry_fix(
        f_uns, get_file(f_uns),
        lambda e: e.get("form_id") in uns_fixes and e.get("type") == "MGEF DNAM",
        lambda e: uns_fixes[e.get("form_id")],
        cat_d
    )

    # 20. Vigilant numeric/gameplay fixes
    apply_entry_fix(
        f_vig_nerf, get_file(f_vig_nerf),
        lambda e: e.get("form_id") == "033EA5DD|Vigilant.esm" and e.get("type") == "MGEF DNAM",
        "Crée des Épines de Molag Bal devant le lanceur. (Coût en magie : 200)",
        cat_d
    )
    apply_entry_fix(
        f_vig_vost, get_file(f_vig_vost),
        lambda e: e.get("form_id") == "021418B5|Vigilant.esm" and e.get("type") == "MGEF DNAM",
        "Tous les sorts infligent 50 % de dégâts supplémentaires.",
        cat_d
    )
    apply_entry_fix(
        f_vig_vost, get_file(f_vig_vost),
        lambda e: e.get("form_id") == "02101573|Vigilant.esm" and e.get("type") == "WEAP DESC" and e.get("original") == "Inflicts bleeding (Stamina) damage.",
        "Inflige des dégâts de saignement (vigueur).",
        cat_d
    )
    apply_entry_fix(
        f_vig_173, get_file(f_vig_173),
        lambda e: e.get("form_id") == "02363EDB|Vigilant.esm" and e.get("type") == "MESG DESC",
        "Acte III : Enfant d'Oblivion non démarré.\r\nVous ne pouvez commencer cet acte que si vous avez terminé les actes I et II et évité leurs mauvaises fins.",
        cat_d
    )

    # 21. Vokrii
    f_vok = r"Vokrii - Atouts minimalistes\Vokrii - Minimalistic Perks of Skyrim.esp.json"
    vok_fixes = {
        "000C1E97|Skyrim.esm":
            "Les attaques puissantes avec un marteau interrompent le lancement de sorts, infligeant un coup critique avec des dégâts critiques triplés, réduisant au silence et immobilisant la cible pendant 5 secondes.",
        "04000954|Vokrii - Minimalistic Perks of Skyrim.esp":
            "Les armes à distance interrompent les attaques puissantes, repoussant l'attaquant et infligeant un coup critique avec des dégâts critiques doublés.",
        "04000969|Vokrii - Minimalistic Perks of Skyrim.esp":
            "Les attaques puissantes avec deux mains vides coûtent 25 % de vigueur en moins et ont 50 % de chances de déstabiliser les adversaires, les désarmant potentiellement.",
        "04000AD2|Vokrii - Minimalistic Perks of Skyrim.esp":
            "Les attaques puissantes avec une dague provoquent une hémorragie sur les vivants pendant 30 secondes, infligeant un coup critique avec des dégâts critiques triplés.",
    }
    apply_entry_fix(
        f_vok, get_file(f_vok),
        lambda e: e.get("form_id") in vok_fixes and e.get("type") == "PERK DESC",
        lambda e: vok_fixes[e.get("form_id")],
        cat_d
    )

    # 22. Vokriinator Black
    f_vok_blk = r"Vokriinateur - Morceaux choisis\Vokriinator Black.esp.json"
    vok_blk_fixes = {
        "000D7999|Skyrim.esm":
            "Si vous ne portez pas d'armure, vous avez 5 % de chances de ne subir aucun dégât lors d'une attaque et les sorts d'armure sont deux fois plus puissants.",
        "000D799A|Skyrim.esm":
            "Les sorts de protection et de bouclier s'appliquent aux alliés proches. Si vous ne portez pas d'armure, vous avez 10 % de chances de ne subir aucun dégât lors d'une attaque et les sorts d'armure sont 2,5 fois plus puissants.",
        "000D799B|Skyrim.esm":
            "Si vous ne portez pas d'armure, vous avez 15 % de chances de ne subir aucun dégât lors d'une attaque et les sorts d'armure sont trois fois plus puissants.",
        "07000BB5|PathOfSorcery.esp":
            "Les sorts coûtent de la santé au lieu de la magie. Votre santé maximale est augmentée de 50 % de votre réserve de magie (Novice = 8 PV, Apprenti = 12 PV, Spécialiste = 20 PV, Expert = 30 PV, Maître = 42 PV). N'a aucun effet sous forme de Seigneur vampire. Incompatible avec Magie vancienne.",
        "07000BB6|PathOfSorcery.esp":
            "Réduit de moitié la quantité de santé consommée par le lancement de sorts (Novice = 4 PV, Apprenti = 6 PV, Spécialiste = 10 PV, Expert = 15 PV, Maître = 21 PV ; les sorts de concentration, comme Flammes, ne consomment qu’un tiers de santé).",
        "07000BC6|PathOfSorcery.esp":
            "Les personnes et les créatures alliées à moins de 10 mètres récupèrent 3 points de santé par seconde.",
        "07000BCF|PathOfSorcery.esp":
            "Quand vous avez une arme liée équipée, vous avez 30 % de chances de devenir éthéré pendant 2 secondes quand votre adversaire effectue une attaque puissante.",
        "07000BD2|PathOfSorcery.esp":
            "Les morts-vivants réanimés infligent 25 % de dégâts supplémentaires au combat, et se déplacent et attaquent 15 % plus vite.",
        "07000C2F|PathOfSorcery.esp":
            "Alignez-vous avec la Tempête, délaissant l'Hiver et le Brasier. Tant qu'un sort de foudre est équipé, votre magie se régénère plus vite ; lancer des sorts de foudre augmente brièvement votre vitesse. Octroie le pouvoir « Tempête d'éclairs ». (Une seule maîtrise élémentale possible)",
        "07000C30|PathOfSorcery.esp":
            "Alignez-vous avec le Brasier, délaissant l’Hiver et la Tempête. Tant qu’un sort de feu est équipé, votre santé se régénère plus vite ; lancer des sorts de feu augmente brièvement vos dégâts de feu. Octroie le pouvoir « Pluie de météores ». (Une seule maîtrise élémentale possible)",
        "0A0842DD|Ordinator - Perks of Skyrim.esp":
            "Vous êtes un adepte de la dissimulation dans l'angle mort de votre victime. La furtivité est 15 % plus efficace dans un rayon de 10 mètres et 30 % plus efficace dans un rayon de 5 mètres.",
    }
    apply_entry_fix(
        f_vok_blk, get_file(f_vok_blk),
        lambda e: e.get("form_id") in vok_blk_fixes and e.get("type") == "PERK DESC",
        lambda e: vok_blk_fixes[e.get("form_id")],
        cat_d
    )

    # 23. VokriinatorBlack - combatforcaco
    f_vok_caco = r"VokriinatorBlack - combatforcaco.esp - French\vokriinatorblack - combatforcaco.esp.json"
    vok_caco_fixes = {
        "030B0D3F|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la dague ont 30 % de chances d’infliger des blessures distrayantes, drainant 100 points de magie et de vigueur et arrêtant la régénération pendant 5 secondes.",
        "030B0D40|Ordinator - Perks of Skyrim.esp":
            "Toucher une cible avec une attaque puissante à la dague a 25 % de chances de la paralyser pendant 20 secondes. Vos attaques contre la cible paralysée lui infligent un nonuple coup critique.",
        "030043FF|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la hache de guerre ont 50 % de chances d’octroyer 15 % de dégâts d’attaque supplémentaires pendant 30 secondes. Cet effet est cumulable.",
        "03004EF9|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la dague ignorent 50 % de l'armure.",
        "03012846|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à l'espadon ont 25 % de chances de fatiguer une cible, drainant 150 points de magie et de vigueur et arrêtant la régénération pendant 5 secondes.",
        "0301284E|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la hache d'armes ont 30 % de chances d'infliger des dégâts bonus égaux à 25 % de la santé actuelle de la cible (maximum 150 points de dégâts).",
        "03002E05|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à l'épée ont 15 % de chances d'éjecter les cibles jusqu'à 2 mètres, infligeant jusqu'à 50 % de dégâts supplémentaires d'après la distance parcourue.",
        "0300440A|Ordinator - Perks of Skyrim.esp":
            "Les attaques puissantes à la masse ont 15 % de chances d'épuiser la totalité de votre vigueur lors de l'impact, infligeant 1 % de dégâts supplémentaires par point de vigueur épuisé et faisant un coup critique.",
    }
    apply_entry_fix(
        f_vok_caco, get_file(f_vok_caco),
        lambda e: e.get("form_id") in vok_caco_fixes and e.get("type") == "PERK DESC",
        lambda e: vok_caco_fixes[e.get("form_id")],
        cat_d
    )

    # 24. Vulcano
    f_vulc = r"Vulcano - Sorts de feu\Vulcano.esp.json"
    apply_entry_fix(
        f_vulc, get_file(f_vulc),
        lambda e: e.get("form_id") == "040009E3|Vulcano.esp" and e.get("type") == "MGEF DNAM",
        "Les dégâts de feu que vous subissez ont 30 % de chances de vous soigner pendant <dur> secondes. Requiert <50> points de magie.",
        cat_d
    )

    # 25. YOT - LOTD & YOT - Vigilant
    f_yot_lotd = r"YOT - Vos propres pensées\YOT - LOTD.esp.json"
    yot_lotd_fixes = {
        "03079D7F|LegacyoftheDragonborn.esm": "Je semble être à moins de 15 mètres du site de fouilles optimal.",
        "03079D80|LegacyoftheDragonborn.esm": "Je semble être à moins de 25 mètres du site de fouilles optimal.",
        "03079D81|LegacyoftheDragonborn.esm": "Je semble être à moins de 40 mètres du site de fouilles optimal.",
        "03079D82|LegacyoftheDragonborn.esm": "Je semble être à moins de 55 mètres du site de fouilles optimal.",
        "03079D83|LegacyoftheDragonborn.esm": "Je semble être à moins de 80 mètres du site de fouilles optimal.",
        "03166466|LegacyoftheDragonborn.esm": "Jeu de cartes - Araignées :\r\nProcure 15 % de chances de paralyser et d'empoisonner l'ennemi touché par une arme de mêlée, tant que le jeu est dans l'inventaire.",
    }
    apply_entry_fix(
        f_yot_lotd, get_file(f_yot_lotd),
        lambda e: e.get("form_id") in yot_lotd_fixes and e.get("type") == "MESG DESC",
        lambda e: yot_lotd_fixes[e.get("form_id")],
        cat_d
    )

    f_yot_vig = r"YOT - Vos propres pensées\YOT - Vigilant.esp.json"
    yot_vig_fixes = {
        "013F55C2|Vigilant.esm": "J'ai une occasion de le bannir. Dois-je le renvoyer en Oblivion ?\n \n- Bannir : Conjuration > 25\n- Frapper : Deux mains > 25 ou Une main > 40",
        "013F55C3|Vigilant.esm": "J'ai une occasion pendant qu'il est distrait par la conversation. Dois-je le renvoyer en Oblivion ?\n- Bannir : Conjuration > 25\n- Frapper : Deux mains > 25 ou Une main > 40",
        "013F2EB3|Vigilant.esm": "J'ai une occasion pendant qu'il parle. Dois-je le renvoyer en Oblivion ?\n- Bannir : Conjuration > 25\n- Frapper : Deux mains > 25 ou Une main > 40",
        "013F2EB2|Vigilant.esm": "J'ai une occasion pendant qu'il dort ! Dois-je le renvoyer en Oblivion ?\n- Bannir : Conjuration > 25\n- Frapper : Deux mains > 25 ou Une main > 40",
    }
    apply_entry_fix(
        f_yot_vig, get_file(f_yot_vig),
        lambda e: e.get("form_id") in yot_vig_fixes and e.get("type") == "MESG DESC",
        lambda e: yot_vig_fixes[e.get("form_id")],
        cat_d
    )

    # Save all modified files
    print(f"\nSaving {len(modified_files)} modified JSON files to disk...")
    for rel_path in sorted(modified_files):
        save_json(rel_path, file_cache[rel_path])

    total_fixes = sum(fix_counts_by_cat.values())
    print(f"\n=== PHASE 2 APPLY SUMMARY ===")
    print(f"Total entries fixed: {total_fixes} across {len(modified_files)} files")
    for cat, cnt in sorted(fix_counts_by_cat.items()):
        print(f"  - {cat}: {cnt}")
    print("\nBreakdown by file:")
    for rel, cnt in sorted(fix_counts_by_file.items()):
        print(f"  [{cnt:3d}] {rel}")

    with open("phase2_applied_log.json", "w", encoding="utf-8") as f:
        json.dump(fix_log, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
