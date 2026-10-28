import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = "data/user/database/french"

# Define Phase 4 files groups
phase4_file_defs = [
    # 1. LOTD & Hall of Forgotten
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/lotd_hub.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_aiolashields_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_babayaga_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_billyrow_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_carvedbrink_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_dcr_kingcrusader_4esl_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_faraamesl_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_kozakowy_cbbe_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_ksa_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_lunarg_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_onyxlancer_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_puaio.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_sirenroot_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_titus_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_velothi_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/dbm_hub_weapon_patch.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/lotd_hub_finh.esp.json"),
    ("LOTD - Hall of Forgotten", "Legacy of the Dragonborn - Hall of Forgotten/lotd_hub_st.esp.json"),
    ("LOTD - Hall of Forgotten Delayed", "Legacy of the Dragonborn - Hall of Forgotten - Delayed/lotd - hall of forgotten - delayed.esp.json"),
    ("LOTD - DBM Unslaad Display", "DBM_Unslaad_Display_Patch/dbm_unslaad_display_patch.esp.json"),
    ("LOTD - Midwood Isle Patch", "DBM_HUB_MidwoodIsle_Patch.esp - French/dbm_hub_midwoodisle_patch.esp.json"),
    ("LOTD - Replica Fixes AoB", "Legacy of the Dragonborn - Replica Fixes/dbm_aob_replicapatch.esp.json"),
    ("LOTD - Replica Fixes Base", "Legacy of the Dragonborn - Replica Fixes/dbm_replicapatch.esp.json"),
    ("LOTD - Replica Fixes ToK", "Legacy of the Dragonborn - Replica Fixes/dbm_tok_replicapatch.esp.json"),
    ("LOTD - NPC Overhaul", "Legacy of the Dragonborn - NPC Overhaul/legacyofthedragonborn - npc overhaul.esp.json"),
    ("LOTD - Safehouse Plus", "Legacy Safehouse Plus/dbm_safehouseplus_addon.esp.json"),
    ("LOTD - Identity Crisis", "DBM_IdentityCrisis_Patch.esp - French/dbm_identitycrisis_patch.esp.json"),
    ("LOTD - Clockwork Patch", "lotd_clockwork_patch.esp - French/lotd_clockwork_patch.esp.json"),
    ("LOTD - Dolls Fixes", "AdditionalHFDollsFixesLOTD.esp - French/additionalhfdollsfixeslotd.esp.json"),
    ("LOTD - Debaser Patch", "Debaser - LOTD Patch/11debaser - lotd patch by xtudo.esl.json"),
    ("LOTD - Wintersun Patch Fixed", "Unofficial Patch for DBM Wintersun Patch - French/DBM_Wintersun_Patch_Fixed.esp.json"),

    # 2. LOTD Follower Room Patches
    ("LOTD - Follower Room Auri", "Legacy of the Dragonborn - Follower Room Patches - French/dbm_auri_patch.esp.json"),
    ("LOTD - Follower Room Inigo", "Legacy of the Dragonborn - Follower Room Patches - French/dbm_inigo_patch.esp.json"),
    ("LOTD - Follower Room Lucien", "Legacy of the Dragonborn - Follower Room Patches - French/dbm_lucien_patch.esp.json"),
    ("LOTD - Follower Room Remiel", "Legacy of the Dragonborn - Follower Room Patches - French/dbm_remiel_patch.esp.json"),

    # 3. Hjertesten Hall (Domaine joueur & Quêtes)
    ("Hjertesten Hall Base", "Hjertesten Hall - French/dt_hjertesten hall.esp.json"),
    ("Hjertesten Hall Patch", "Hjertesten Hall - French/DTHjertestenLandscapeandWaterFixesPatch.esp.json"),
    ("Hjertesten Hall Patch", "Hjertesten Hall - French/DT_HjertestenHallComplementaryGrassFixes.esp.json"),
    ("Hjertesten Hall Patch", "Hjertesten Hall - French/DT_HjertestenHallUSSEPPatch.esp.json"),
    ("Hjertesten Hall Patch", "Hjertesten Hall - French/DT_HjertestenNorthernRoadsPatchSE.esp.json"),

    # 4. Villes, Intérieurs & Quêtes Nouveaux Mondes
    ("EEKs Whiterun Interiors", "EEKs Whiterun Interiors.esp - French/eeks whiterun interiors.esp.json"),
    ("Alternate Perspective Base", "FR - Alternate Perspective/AlternatePerspective.esp.json"),
    ("Alternate Perspective Sovngarde", "Alternate Perspective - Gate to Sovngarde Edition.esp - French/alternate perspective - gate to sovngarde edition.esp.json"),
    ("Alternate Perspective Beginnings", "Alternate Perspective -- New Beginnings.esp - French/alternate perspective -- new beginnings.esp.json"),
    ("Lucien Bruma Patch", "Lucien - Beyond Skyrim - Bruma Patch/lucien-bruma-patch.esp.json"),
    ("JK Sky Haven Temple", "JK's Sky Haven Temple/jk's sky haven temple.esp.json"),
    ("Ashley Witcher Whiterun", "ASHLEY - Witcher in Whiterun.esp - French/ashley - witcher in whiterun.esp.json"),
    ("Riften Laketown", "RiftenLaketown.esp - French/riftenlaketown.esp.json"),
    ("Deadly Shadows Riften", "Deadly Shadows in Riften/deadly shadows of  riften.esp.json"),
    ("Lilebonymace Patch 1", "Lilebonymace's Patches/houseofhorrorsquestexpansion - thechoiceisyours.esp.json"),
    ("Lilebonymace Patch 2", "Lilebonymace's Patches/thechoiceisyours - lod dialogue tweak.esp.json"),
    ("Moonpath Bruma Marker", "Moonpath - Bruma Map Marker.esp - French/moonpath - bruma map marker.esp.json"),
    ("Beyond Skyrim Cyrodiil", "Beyond Skyrim - Cyrodiil Patch - French/bruma name patch.esp.json"),
    ("Falskaar Guard Restored", "Falskaar - Guard Restored - French/falskaar guards restored.esp.json"),
]

# Add TCC patches (17 files)
tcc_dir = os.path.join(base_dir, "Legacy of the Dragonborn - Hall of Forgotten - TCC - French")
if os.path.exists(tcc_dir):
    for f in os.listdir(tcc_dir):
        if f.endswith(".json"):
            phase4_file_defs.append(("LOTD - Hall of Forgotten TCC", os.path.relpath(os.path.join(tcc_dir, f), base_dir)))

# Add Make Your Riften patches (23 files)
myr_dir = os.path.join(base_dir, "Make Your Riften")
if os.path.exists(myr_dir):
    for f in os.listdir(myr_dir):
        if f.endswith(".json"):
            phase4_file_defs.append(("Make Your Riften", os.path.relpath(os.path.join(myr_dir, f), base_dir)))

print(f"Total fichiers Phase 4 identifiés : {len(phase4_file_defs)}")

total_records = 0
status_dist = {}
anomalies = []

en_words = [
    'the', 'and', 'with', 'from', 'what', 'where', 'when', 'why', 'who', 'how',
    'you', 'your', 'have', 'been', 'will', 'would', 'could', 'should',
    'sword', 'shield', 'helmet', 'boots', 'armor', 'dagger', 'bow',
    'damage', 'health', 'magicka', 'stamina', 'seconds', 'points'
]
en_pattern = re.compile(r'\b(' + '|'.join(en_words) + r')\b', re.IGNORECASE)

scanned_files = 0
for group_name, rel_path in phase4_file_defs:
    fpath = os.path.join(base_dir, rel_path)
    if not os.path.exists(fpath):
        print(f"[ATTENTION] Fichier introuvable : {rel_path}")
        continue
    scanned_files += 1
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as jf:
        data = json.load(jf)
    
    total_records += len(data)
    
    for item in data:
        st = item.get('status')
        status_dist[st] = status_dist.get(st, 0) + 1
        
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = str(item.get('original') or '')
        curr = item.get('string')
        
        # 1. Null or empty string
        if curr is None or not str(curr).strip():
            if st != 'NoTranslationRequired':
                anomalies.append({
                    "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                    "index": idx, "original": orig, "current": curr, "reason": "EMPTY_OR_NULL"
                })
            continue
            
        curr_str = str(curr)
        
        # 2. Status is TranslationRequired
        if st == 'TranslationRequired':
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr, "reason": "STATUS_REQUIRED"
            })
            
        # 3. Mojibake
        if any(c in curr_str for c in ['Ã©', 'Ã¨', 'Ã ', 'Ã¹', 'Ã®', 'Ã«', 'Ã¯']):
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr, "reason": "MOJIBAKE"
            })
            
        # 4. Untranslated English in player-facing dialog / text / item
        if orig == curr_str and len(orig) > 10 and st != 'NoTranslationRequired':
            if typ in ['INFO NAM1', 'DIAL FULL', 'BOOK DESC', 'MESG DESC', 'QUST FULL', 'QUST NNAM', 'QUST CNAM', 'ARMO FULL', 'WEAP FULL', 'ACTI FULL', 'ALCH FULL', 'AMMO FULL']:
                matches = en_pattern.findall(orig)
                if len(matches) >= 2 and not orig.startswith('...'):
                    anomalies.append({
                        "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                        "index": idx, "original": orig, "current": curr,
                        "reason": f"UNTRANSLATED_ENGLISH (matches: {matches[:3]})"
                    })
                
        # 5. Lore false friends
        curr_lower = curr_str.lower()
        orig_lower = orig.lower()
        if 'montagne rouge' in curr_lower:
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr,
                "reason": "LORE: Montagne rouge -> Mont Écarlate"
            })
        if 'falkreath' in orig_lower and 'faillaise' in curr_lower:
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr,
                "reason": "LORE: Falkreath -> Épervine (et non Faillaise)"
            })
        if 'clair-osbcur' in curr_lower:
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr,
                "reason": "TYPO: clair-osbcur -> Clair-Obscur"
            })
        if 'endurance' in curr_lower and 'stamina' in orig_lower:
            anomalies.append({
                "group": group_name, "file": rel_path, "form_id": fid, "type": typ,
                "index": idx, "original": orig, "current": curr,
                "reason": "LORE: endurance -> Vigueur (Skyrim)"
            })

print(f"\nScan terminé sur {scanned_files} fichiers.")
print(f"Total entrées scannées : {total_records}")
print(f"Distribution des statuts : {status_dist}")
print(f"Total anomalies détectées : {len(anomalies)}")

by_reason = {}
for a in anomalies:
    by_reason.setdefault(a["reason"], []).append(a)

for reason, items in by_reason.items():
    print(f"\n--- {reason} ({len(items)} items) ---")
    for it in items[:8]:
        print(f"  [{it['file']}] {it['form_id']} | {it['type']} | idx={it['index']}")
        print(f"     Orig: {repr(it['original'][:70])}")
        print(f"     Curr: {repr(it['current'][:70]) if it['current'] else None}")

with open("phase4_anomalies.json", "w", encoding="utf-8") as out:
    json.dump(anomalies, out, ensure_ascii=False, indent=2)

print("\nEnregistré dans phase4_anomalies.json.")
