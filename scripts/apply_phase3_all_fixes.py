import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

print("=== DEBUT DE L'APPLICATION DES FIXES PHASE 3 ===")

# 1. FANATICAL ENEMIES
fanatical_path = "data/user/database/french/Fanatical Enemies.esp - French/fanatical enemies.esp.json"
assert os.path.exists(fanatical_path), f"File not found: {fanatical_path}"

with open(fanatical_path, "r", encoding="utf-8") as f:
    fanatical_data = json.load(f)

print(f"\n[Fanatical Enemies] Chargement de {len(fanatical_data)} entrées...")
# Search for target: ('049CADDC|Fanatical Enemies.esp', 'NPC_ FULL', None, 'Lord of Falkreath')
target_fe = {
    "form_id": "049CADDC|Fanatical Enemies.esp",
    "type": "NPC_ FULL",
    "index": None,
    "original": "Lord of Falkreath",
    "target": "Seigneur d'Épervine"
}

matches_fe = [
    item for item in fanatical_data
    if item.get("form_id") == target_fe["form_id"]
    and item.get("type") == target_fe["type"]
    and item.get("index") == target_fe["index"]
    and item.get("original") == target_fe["original"]
]

print(f"[Fanatical Enemies] Correspondances trouvées pour {target_fe['form_id']}: {len(matches_fe)}")
assert len(matches_fe) == 1, f"ERREUR: Attendu 1 correspondance, trouvé {len(matches_fe)}"

fe_old = matches_fe[0].get("string")
print(f"  Ancienne valeur observée : {repr(fe_old)}")
print(f"  Nouvelle valeur cible    : {repr(target_fe['target'])}")

matches_fe[0]["string"] = target_fe["target"]
matches_fe[0]["status"] = "TranslationComplete"

# Écriture Fanatical Enemies
with open(fanatical_path, "w", encoding="utf-8") as f:
    json.dump(fanatical_data, f, ensure_ascii=False, indent=2)
print("[Fanatical Enemies] Écrit avec succès sur le disque.")

# 2. REMIEL
remiel_path = "data/user/database/french/Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)/hlioremi.esp.json"
assert os.path.exists(remiel_path), f"File not found: {remiel_path}"

with open(remiel_path, "r", encoding="utf-8") as f:
    remiel_data = json.load(f)

print(f"\n[Remiel Base] Chargement de {len(remiel_data)} entrées...")

with open("remiel_full_translation_map.json", "r", encoding="utf-8") as f:
    remiel_targets = json.load(f)

print(f"[Remiel Base] Nombre de cibles à traiter: {len(remiel_targets)}")

applied_records = []
untouched_count = 0

for target in remiel_targets:
    fid = target["form_id"]
    t = target["type"]
    idx = target["index"]
    orig = target["original"]
    new_fr = target["translation"]
    
    # Strict quadruple matching
    matches = [
        item for item in remiel_data
        if item.get("form_id") == fid
        and item.get("type") == t
        and item.get("index") == idx
        and item.get("original") == orig
    ]
    
    assert len(matches) == 1, f"ERREUR Remiel: Attendu 1 match pour ({fid}, {t}, {idx}, {repr(orig)}), trouvé {len(matches)}"
    
    rec = matches[0]
    old_str = rec.get("string")
    
    if orig in ["Khash...", "A, B, C, D, E, F, G, H..."]:
        # Verbatim strings, no modification needed
        untouched_count += 1
        continue
        
    rec["string"] = new_fr
    rec["status"] = "TranslationComplete"
    applied_records.append({
        "file": "hlioremi.esp.json",
        "form_id": fid,
        "type": t,
        "index": idx,
        "original": orig,
        "old_value": old_str,
        "new_value": new_fr
    })

print(f"[Remiel Base] Modifiés : {len(applied_records)} entrées")
print(f"[Remiel Base] Laissés intacts (verbatim/nom) : {untouched_count} entrées")

# Écriture Remiel
with open(remiel_path, "w", encoding="utf-8") as f:
    json.dump(remiel_data, f, ensure_ascii=False, indent=2)
print("[Remiel Base] Écrit avec succès sur le disque.")

# Enregistrement des logs de modifications effectives
all_modifications = [{
    "file": "fanatical enemies.esp.json",
    "form_id": target_fe["form_id"],
    "type": target_fe["type"],
    "index": target_fe["index"],
    "original": target_fe["original"],
    "old_value": fe_old,
    "new_value": target_fe["target"]
}] + applied_records

with open("phase3_effective_modifications.json", "w", encoding="utf-8") as f:
    json.dump(all_modifications, f, ensure_ascii=False, indent=2)

print(f"\nTotal modifications effectives enregistrées : {len(all_modifications)}")
print("=== APPLICATION PHASE 3 TERMINEE AVEC SUCCES ===")
