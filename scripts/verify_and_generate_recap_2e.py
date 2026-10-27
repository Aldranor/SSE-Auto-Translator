import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('recap_phase2e_diffs.json', 'r', encoding='utf-8') as f:
    diffs = json.load(f)

print(f"Loaded {len(diffs)} diffs for Phase 2E.")

file_map = {
    'attackodaedra.esp.json': 'data/user/database/french/AttackoDaedra.esp - French/attackodaedra.esp.json',
    'wintersun - gott patch.esp.json': 'data/user/database/french/Wintersun - Tribunal Integration/wintersun - gott patch.esp.json',
    'yot - clockwork.esp.json': 'data/user/database/french/YOT - Clockwork.esp - French/yot - clockwork.esp.json'
}

print("\n--- INDEPENDENT ON-DISK POST-VERIFICATION ---")
verified_count = 0
for d in diffs:
    fpath = file_map[d['file']]
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    matches = [x for x in data if x.get('form_id') == d['form_id'] and 
                                  x.get('type') == d['type'] and 
                                  x.get('index') == d['index'] and 
                                  x.get('original') == d['original']]
    assert len(matches) == 1, f"Expected 1 match, found {len(matches)}"
    on_disk_str = matches[0].get('string')
    assert on_disk_str == d['after'], f"Mismatch on disk! Expected {d['after']}, got {on_disk_str}"
    verified_count += 1

print(f"All {verified_count} records verified directly on disk with 100% fidelity!")

# Generate recap markdown
md_lines = [
    "# Récapitulatif des Modifications — Phase 2E : Micro-Patchs de Compatibilité & Corrections Unitaires",
    "",
    "> **Périmètre :** Sous-phase 2E de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).",
    "> **Mods audités :** 110 plugins de micro-patchs de compatibilité locaux et corrections isolées répertoriés dans la Catégorie 10 de [`listing_traductions_locales_non_verifiees.md`](file:///e:/Code/SSE%20Translator%20updated/listing_traductions_locales_non_verifiees.md) (`AttackoDaedra`, `Wintersun Tribunal Integration`, `YOT - Your Own Thoughts` [Clockwork, Unslaad, Carved Brink, Wheels of Lull], `JK's College of Winterhold`, `DynDOLOD`, `For Honor in Skyrim`, `AP - Missile Additional Starts`, `Alternate Perspective - New Beginnings`, `Gray Quarter Overhaul`, etc.).",
    "> **Volume de contrôle :** 3 348 enregistrements vérifiés avec protocole d'anti-collision unitaire `(form_id, type, index, original)` strict.",
    "",
    "---",
    ""
]

def clean_cell(val):
    if val is None:
        return "*None*"
    s = str(val).replace('\r', ' ').replace('\n', '<br>')
    return s.replace('|', '\\|')

by_file = {}
for entry in diffs:
    by_file.setdefault(entry['file'], []).append(entry)

for fn, entries in by_file.items():
    md_lines.append(f"## 📁 `{fn}`")
    md_lines.append(f"*Nombre d'ajustements unitaires vérifiés :* **{len(entries)}**\n")
    md_lines.append("| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for e in entries:
        fid_formatted = f"`{clean_cell(e['form_id'])}`<br>*{clean_cell(e['type'])}*"
        orig = clean_cell(e['original'])
        before = clean_cell(e['before'])
        after = f"**{clean_cell(e['after'])}**"
        nat = clean_cell(e['nature'])
        md_lines.append(f"| {fid_formatted} | {orig} | {before} | {after} | {nat} |")
    md_lines.append("\n---\n")

with open('recap_modifications_phase2e.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print("recap_modifications_phase2e.md written successfully.")
