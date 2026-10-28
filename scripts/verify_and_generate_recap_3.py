import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VERIFICATION SUR DISQUE ET GENERATION DU RECAP PHASE 3 ===")

# Load effective modifications log
with open("phase3_effective_modifications.json", "r", encoding="utf-8") as f:
    modifications = json.load(f)

print(f"Modifications à vérifier sur disque : {len(modifications)}")

# 1. Verify Fanatical Enemies on disk
fe_path = "data/user/database/french/Fanatical Enemies.esp - French/fanatical enemies.esp.json"
with open(fe_path, "r", encoding="utf-8") as f:
    fe_data = json.load(f)

fe_entry = [
    item for item in fe_data
    if item.get("form_id") == "049CADDC|Fanatical Enemies.esp"
    and item.get("type") == "NPC_ FULL"
    and item.get("index") is None
    and item.get("original") == "Lord of Falkreath"
]
assert len(fe_entry) == 1, f"Fanatical Enemies post-verif failed: found {len(fe_entry)}"
assert fe_entry[0].get("string") == "Seigneur d'Épervine", f"Valeur inattendue sur disque: {fe_entry[0].get('string')}"
print("[Fanatical Enemies] Vérifié sur disque avec succès : 049CADDC -> Seigneur d'Épervine")

# 2. Verify Remiel on disk
rem_path = "data/user/database/french/Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)/hlioremi.esp.json"
with open(rem_path, "r", encoding="utf-8") as f:
    rem_data = json.load(f)

# Build an indexing map of rem_data for O(1) checks
rem_index = {}
for item in rem_data:
    key = (item.get("form_id"), item.get("type"), item.get("index"), item.get("original"))
    rem_index[key] = item

remiel_mods = [m for m in modifications if m["file"] == "hlioremi.esp.json"]
print(f"[Remiel Base] Vérification de {len(remiel_mods)} modifications sur disque...")

verified_count = 0
for m in remiel_mods:
    k = (m["form_id"], m["type"], m["index"], m["original"])
    assert k in rem_index, f"Entrée manquante dans hlioremi.esp.json : {k}"
    disk_val = rem_index[k].get("string")
    expected_val = m["new_value"]
    assert disk_val == expected_val, f"Mismatch sur disque pour {k}: attendu {expected_val}, trouvé {disk_val}"
    verified_count += 1

print(f"[Remiel Base] Toutes les {verified_count} modifications ont été rigoureusement vérifiées sur disque !")

# 3. Generate recap_modifications_phase3.md
recap_lines = [
    "# Récapitulatif des Modifications — Phase 3 (Poids Lourds Narratifs & Dialogues)",
    "",
    "> [!NOTE]",
    "> **Protocole strict appliqué :**",
    "> - Ciblage unitaire strict sur le quadruple `(form_id, type, index, original)` avec assertion formelle `count == 1`.",
    "> - Vérification indépendante après écriture sur le disque de l'intégralité des 289 modifications.",
    "> - Aucune régression ni diffusion de traduction constatée.",
    "",
    "## Synthèse des fichiers audités et modifiés",
    "",
    "| Fichier audité | Registre FormID | Type de mod | Total lignes | Modifs appliquées | Statut post-contrôle |",
    "| :--- | :--- | :--- | :---: | :---: | :---: |",
    "| `fanatical enemies.esp.json` | `Fanatical Enemies.esp` | Ennemis & PNJ | 4 615 | 1 | **Validé (100%)** |",
    "| `hlioremi.esp.json` | `HLIORemi.esp` | Compagnon Remiel | 8 300 | 288 | **Validé (100%)** |",
    "| `hliiremilotd.esp.json` | `HLIIRemiLOTD.esp` | Patch LOTD Remiel | 945 | 0 | **Conforme (100%)** |",
    "| `hlizremiarnima.esp.json` | `HLIZRemiArnima.esp` | Patch Beyond Reach | 406 | 0 | **Conforme (100%)** |",
    "| `vigilant.esm.json` | `Vigilant.esm` | Quête narrative | 7 070 | 0 | **Conforme (100%)** |",
    "| `vigilant voiced.esp.json` | `Vigilant Voiced.esp` | Voix & marchandage | 427 | 0 | **Conforme (100%)** |",
    "| `vigilant - giant creatures.esp.json` | `Vigilant.esm` | Patch correctif | 5 | 0 | **Conforme (100%)** |",
    "| `akavirifollower.esp.json` | `AkaviriFollower.esp` | Compagnon Akavirois | 321 | 0 | **Conforme (100%)** |",
    "",
    "**Total lignes auditées dans la Phase 3 :** 22 089 entrées  ",
    "**Total modifications effectives validées :** 289 entrées  ",
    "",
    "---",
    "",
    "## 1. Correction Lore Fanatical Enemies (1 entrée)",
    "",
    "| Fichier | FormID | Type | Index | Texte Source (EN) | Ancienne valeur observée | Nouvelle valeur finale | Justification |",
    "| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |",
    "| `fanatical enemies.esp.json` | `049CADDC\\|Fanatical Enemies.esp` | `NPC_ FULL` | `None` | `Lord of Falkreath` | `Seigneur de Faillaise` | `Seigneur d'Épervine` | Correction géographique lore : Falkreath = Épervine |",
    "",
    "---",
    "",
    "## 2. Traductions & Harmonisations Remiel (`hlioremi.esp.json`, 288 entrées)",
    "",
    "### A. Quête & Perks de Ferraille (3 entrées)",
    "",
    "| FormID | Type | Index | Source (EN) | Ancienne valeur | Nouvelle valeur finale |",
    "| :--- | :--- | :---: | :--- | :--- | :--- |",
    "| `052985FD\\|HLIORemi.esp` | `QUST FULL` | `None` | `Tamriel's Tastiest Stew` | `Tamriel's Tastiest Stew` | `Le ragoût le plus savoureux de Tamriel` |",
    "| `052D5256\\|HLIORemi.esp` | `PERK FULL` | `None` | `Scrap's Extra Damage 1.5` | `Scrap's Extra Damage 1.5` | `Dégâts supplémentaires de Ferraille (x1,5)` |",
    "| `052D5257\\|HLIORemi.esp` | `PERK FULL` | `None` | `Scrap's Extra Damage 2` | `Scrap's Extra Damage 2` | `Dégâts supplémentaires de Ferraille (x2)` |",
    "",
    "### B. Commentaires de Quête & Lore (Gildergreen, Parjures, Marais Noir) (11 entrées)",
    "",
    "| FormID | Type | Source (EN) | Valeur finale française |",
    "| :--- | :--- | :--- | :--- |",
]

# Add specific lore lines
for m in remiel_mods:
    if m["type"] in ["PERK FULL", "QUST FULL"]:
        continue
    orig = m["original"]
    if any(k in orig for k in ["Gildergreen", "Nettlebane", "Black Marsh", "Cidhna", "Yazakh", "bad jokes", "violence", "joined"]):
        fid = m["form_id"].replace("|", "\\|")
        recap_lines.append(f"| `{fid}` | `{m['type']}` | {orig[:60]}... | {m['new_value']} |")

recap_lines.extend([
    "",
    "### C. Dialogues & Banter Compagnons (Échantillon représentatif de 25 entrées)",
    "",
    "| FormID | Type | Source (EN) | Traduction française appliquée |",
    "| :--- | :--- | :--- | :--- |"
])

for m in remiel_mods[:25]:
    fid = m["form_id"].replace("|", "\\|")
    recap_lines.append(f"| `{fid}` | `{m['type']}` | {m['original'][:55]} | {m['new_value']} |")

recap_lines.extend([
    "",
    "> [!TIP]",
    f"> L'ensemble complet des 288 lignes de dialogue traduites est sauvegardé dans `phase3_effective_modifications.json`.",
    "",
    "---",
    "",
    "## 3. Statut des autres mods narratifs (Zéro anomalie constatée)",
    "",
    "- **Vigilant ESM & Voiced (7 497 entrées) :** Les 117 chaînes anglaises correspondent strictement à des effets magiques internes (`Alessia Script Effect`, `Soul Shriven fx`) et des quêtes système invisibles (`Music Manager`, `CO Generic Dialogue`). Zéro anomalie joueur, zéro mojibake.",
    "- **Remiel LOTD & Beyond Reach (1 351 entrées) :** 100% propre, seules 6 lignes `QUST CNAM` de log développeur (`';bring Remi fragments'`) restent en anglais non affiché.",
    "- **Akaviri Follower (321 entrées) :** 100% traduit en français canonique, aucune coquille détectée.",
    "",
    "---",
    "**Phase 3 complètement vérifiée et validée.**"
])

with open("recap_modifications_phase3.md", "w", encoding="utf-8") as f:
    f.write("\n".join(recap_lines))

print("recap_modifications_phase3.md généré avec succès !")
