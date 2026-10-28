import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== APPLICATION DES FIXES PHASE 4 (BATCH PAR FICHIER) ===")

effective_mods = []
batches = {}

def add_fix(rel_path, form_id, rec_type, index, original, new_target):
    batches.setdefault(rel_path, []).append((form_id, rec_type, index, original, new_target))

# 1. EEKs Whiterun Interiors
eeks_file = os.path.join("EEKs Whiterun Interiors.esp - French", "eeks whiterun interiors.esp.json")
add_fix(eeks_file, "0602DDD6|EEKs Whiterun Interiors.esp", "NPC_ FULL", None, "Aalia", "Aalia")
add_fix(eeks_file, "0602DDD6|EEKs Whiterun Interiors.esp", "NPC_ SHRT", None, "Aalia", "Aalia")
add_fix(eeks_file, "0605B47B|EEKs Whiterun Interiors.esp", "FLOR FULL", None, "Red Mountain Flowers", "Fleurs rouges de montagne")
add_fix(eeks_file, "06058CCB|EEKs Whiterun Interiors.esp", "FLOR FULL", None, "Red Mountain Flowers", "Fleurs rouges de montagne")

# 2. DBM Identity Crisis Patch
idcrisis_file = os.path.join("DBM_IdentityCrisis_Patch.esp - French", "dbm_identitycrisis_patch.esp.json")
add_fix(idcrisis_file, "0700085A|DBM_IdentityCrisis_Patch.esp", "MISC FULL", None, "Heart of Arden-Sul (replica)", "Cœur d'Arden-Sul (réplique)")
add_fix(idcrisis_file, "07000856|DBM_IdentityCrisis_Patch.esp", "ARMO FULL", None, "Intriguer's Cowl (replica)", "Capuchon de l'Intrigant (réplique)")
add_fix(idcrisis_file, "07000857|DBM_IdentityCrisis_Patch.esp", "LIGH FULL", None, "Heart of Arden-Sul (replica)", "Cœur d'Arden-Sul (réplique)")
add_fix(idcrisis_file, "07000852|DBM_IdentityCrisis_Patch.esp", "CONT FULL", None, "Identity Crisis Items", "Objets de la Crise d'identité")

# 3. DBM Unslaad Display Patch
unslaad_file = os.path.join("DBM_Unslaad_Display_Patch", "dbm_unslaad_display_patch.esp.json")
unslaad_fixes = [
    ("09000C02|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Magnar's Warrior Longspear", "Espadon du guerrier Magnar"),
    ("09000825|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Gauntlets", "Gantelets de Tueur de dragon"),
    ("0900083F|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Half-Dragon Doll", "Poupée demi-dragon"),
    ("0900082E|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "The Owl Flies at Dusk", "Le hibou vole au crépuscule"),
    ("09000827|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Armor", "Armure de Tueur de dragon"),
    ("0900083E|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Fang of the Old Dragon", "Croc du Vieux dragon"),
    ("09000831|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Ja'cobee's Dragon Pipe", "Pipeau draconique de Ja'cobee"),
    ("09000807|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Boots", "Bottes de Tueur de dragon"),
    ("09000811|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Alcaire Greatlance", "Grande lance d'Alcaire"),
    ("09000DCB|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "The 36 Lessons of Vivec: Sermon 37", "Les 36 Leçons de Vivec : Sermon 37"),
    ("0900082B|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Silver Great Keyblade", "Grande Clef-Lame d'argent"),
    ("09000833|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Golden Pus", "Masque de Purulence dorée"),
    ("09000C13|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Khemkel's Carving Knife", "Couteau à sculpter de Khemkel"),
    ("09000829|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Greatshield", "Grand bouclier de Tueur de dragon"),
    ("09000820|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Orkey Greataxe", "Grande hache d'Orkey"),
    ("09000826|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Helmet", "Casque de Tueur de dragon"),
    ("09000C15|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Ysgramor's Fork", "Fourche d'Ysgramor"),
    ("09000819|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Greatsword", "Espadon de Tueur de dragon"),
    ("09000C0D|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Honeybee's Silver Sting", "Piqûre d'argent d'Abeille"),
    ("0900080E|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Hoarfrost Scythe", "Faux de Feralgide"),
    ("09000824|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Hands of Gods", "Mains de Dieux"),
    ("0900080C|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Festering Lesion", "Couronne de Suppuration"),
    ("09000809|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Frozen Dragon Soul", "Âme de dragon gelé"),
    ("0900081B|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Gray Owl's Mask", "Masque du Hibou Gris"),
    ("09000821|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Festering Greatsword", "Espadon de Suppuration"),
    ("09000834|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Darkstalker's Staff", "Bâton de Rôdeur sombre"),
    ("09000818|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Zweihander", "Claymore"),
    ("0900082D|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Mage Shield", "Bouclier du Mage"),
    ("09000836|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Curse Ward Greatsword", "Espadon Barrière maudite"),
    ("09000C1E|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Roots of a Woodland Man", "Racines d'un homme des bois"),
    ("09000C17|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Oracle-Oocyte Amulet", "Amulette de l'Oracle Gamétocyte"),
    ("09000DD6|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Oracle Iridescent Mask", "Masque de l'Oracle Iridescent"),
    ("09000822|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Vermilion Bow", "Arc Vermillon"),
    ("0900090D|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Lingering Snow", "Neige persistante"),
    ("0900083A|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Curse Ward Greatshield", "Grand bouclier de Maléfice"),
    ("09000828|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Dragonslayer Ring", "Anneau de Tueur de dragon"),
    ("09000838|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Elden Helmet", "Casque de l'Aîné"),
    ("09000812|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Elden Shield", "Bouclier de l'Aîné"),
    ("09000841|DBM_Unslaad_Display_Patch.esp", "ARMO FULL", None, "Gray Egg", "Œuf gris"),
    ("0900081A|DBM_Unslaad_Display_Patch.esp", "ACTI FULL", None, "Frost Shield", "Bouclier glacé")
]
for fid, rtype, idx, orig, target in unslaad_fixes:
    add_fix(unslaad_file, fid, rtype, idx, orig, target)

# 4. TCC Hall of Forgotten (18 fixes with exact verified FormIDs)
tcc_fixes = [
    ("lotd_tcc_aiolas.esp.json", "02000801|LOTD_TCC_AIOLAS.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Legendary Alpha Shields)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Boucliers alpha légendaires)</font>"),

    ("lotd_tcc_babayaga.esp.json", "09000801|LOTD_TCC_BabaYaga.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Baba Yaga and the Labyrinth)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Baba Yaga et le Labyrinthe)</font>"),

    ("lotd_tcc_billyrow.esp.json", "09000803|LOTD_TCC_BillyRoW.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (BillyRo Ultimate Swords Anthology)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Anthologie ultime d'épées de BillyRo)</font>"),

    ("lotd_tcc_carved brink.esp.json", "09000803|LOTD_TCC_Carved Brink.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Carved Brink)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Bord abrupt)</font>"),

    ("lotd_tcc_curseofthehoundamulet.esp.json", "0A000803|LOTD_TCC_CurseOfTheHoundAmulet.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Curse Of The Hound Amulet)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Malédiction de l'amulette du chien)</font>"),

    ("lotd_tcc_finh.esp.json", "02000801|LOTD_TCC_FINH.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Forgotten In History)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Oublié dans l'histoire)</font>"),

    ("lotd_tcc_kings crusader pack(4esl).esp.json", "09000801|LOTD_TCC_Kings Crusader Pack(4ESL).esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (King Crusader Mega Pack)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Méga pack du Roi croisé)</font>"),

    ("lotd_tcc_kozakowy_cbbe.esp.json", "09000801|LOTD_TCC_Kozakowy_CBBE.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Kozakowy's Falka Armor)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de Falka de Kozakowy)</font>"),

    ("lotd_tcc_ksa.esp.json", "09000801|LOTD_TCC_KSA.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Viridian Knight Armor)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de chevalier viridien)</font>"),

    ("lotd_tcc_lunar guard.esp.json", "09000801|LOTD_TCC_Lunar Guard.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Lunar Guard Armor)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de la Garde lunaire)</font>"),

    ("lotd_tcc_midwoodisle.esp.json", "09000803|LOTD_TCC_MidwoodIsle.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Midwood Isle)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Île de Midwood)</font>"),

    ("lotd_tcc_onyxlancer.esp.json", "09000801|LOTD_TCC_OnyxLancer.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Onyx Lancer)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Lancier d'onyx)</font>"),

    ("lotd_tcc_puaio.esp.json", "09000803|LOTD_TCC_PUAIO.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (PUAIO)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (PUAIO)</font>"),

    ("lotd_tcc_regal paladinesl.esp.json", "09000801|LOTD_TCC_Regal PaladinESL.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Regal Paladin Armor)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de paladin royal)</font>"),

    ("lotd_tcc_sirenroot.esp.json", "09000801|LOTD_TCC_SirenRoot.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (SirenRoot)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Racine des Sirènes)</font>"),

    ("lotd_tcc_titus mede.esp.json", "09000803|LOTD_TCC_Titus Mede.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Armor of Titus Mede)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de Titus Mede)</font>"),

    ("lotd_tcc_velothi.esp.json", "09000803|LOTD_TCC_Velothi.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Armors of the Velothi Pt. I)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armures des Vélothis - Partie I)</font>"),

    ("lotd_tcc_vinditionaio.esp.json", "09000801|LOTD_TCC_VinditionAIO.esp", "MESG DESC", None,
     "<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Vindition Weapons Collection)</font>",
     "<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Collection d'armes de Vindition)</font>")
]

tcc_base_dir = os.path.join("Legacy of the Dragonborn - Hall of Forgotten - TCC - French")
for fname, fid, rtype, idx, orig, target in tcc_fixes:
    rel = os.path.join(tcc_base_dir, fname)
    add_fix(rel, fid, rtype, idx, orig, target)

# Execution
base_dir = os.path.normpath("data/user/database/french")
print(f"Total fichiers à traiter : {len(batches)}")

for rel_path, fix_list in batches.items():
    full_path = os.path.join(base_dir, rel_path)
    assert os.path.exists(full_path), f"Fichier introuvable : {full_path}"
    
    with open(full_path, "r", encoding="utf-8") as jf:
        data = json.load(jf)
        
    print(f"\nTraitement de {rel_path} ({len(fix_list)} modifications ciblées)...")
    
    for fid, rtype, idx, orig, target in fix_list:
        matches = [
            item for item in data
            if item.get("form_id") == fid
            and item.get("type") == rtype
            and item.get("index") == idx
            and item.get("original") == orig
        ]
        assert len(matches) == 1, f"ERREUR: Attendu 1 correspondance pour ({fid}, {rtype}, {idx}, {repr(orig)}) dans {rel_path}, trouvé {len(matches)}"
        
        rec = matches[0]
        old_val = rec.get("string")
        rec["string"] = target
        rec["status"] = "TranslationComplete"
        
        effective_mods.append({
            "file": rel_path.replace("\\", "/"),
            "form_id": fid,
            "type": rtype,
            "index": idx,
            "original": orig,
            "old_value": old_val,
            "new_value": target
        })
        print(f"  {fid} ({rtype}) : {repr(old_val)} -> {repr(target)}")
        
    with open(full_path, "w", encoding="utf-8") as jf:
        json.dump(data, jf, ensure_ascii=False, indent=2)

with open("phase4_effective_modifications.json", "w", encoding="utf-8") as out:
    json.dump(effective_mods, out, ensure_ascii=False, indent=2)

print(f"\n=== APPLICATION TERMINEE AVEC SUCCES : {len(effective_mods)} MODIFICATIONS UNITAIRES EFFECTUEES ===")
