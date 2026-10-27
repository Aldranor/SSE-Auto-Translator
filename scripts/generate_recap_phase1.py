import subprocess
import json
import re
from pathlib import Path

# We can query git to see the exact previous version of each modified file at HEAD!
git_files = [
    "data/user/database/french/Nolvus Awakening Armors Balance Patch.esp - French/nolvus awakening armors balance patch.esp.json",
    "data/user/database/french/Nolvus Awakening Weapons Balance Patch.esp - French/nolvus awakening weapons balance patch.esp.json",
    "data/user/database/french/Nolvus Awakening Weapons Patch - French/nolvus awakening weapons patch.esp.json",
    "data/user/database/french/Nolvus Awakening Clothes Balance Patch - French/nolvus awakening clothes balance patch.esp.json",
    "data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json",
    "data/user/database/french/Nolvus Awakening DLC Patch - French/nolvus awakening dlc patch.esp.json",
    "data/user/database/french/Nolvus Awakening Crafting Patch - French/nolvus awakening crafting patch.esp.json",
    "data/user/database/french/Nolvus Awakening Creatures Patch - French/Nolvus Awakening Creatures Patch.esp.json",
    "data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json",
    "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json",
    "data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level.esp.json",
    "data/user/database/french/Nolvus Awakening Vokriinator Black Integration.esp - French/nolvus awakening vokriinator black integration.esp.json",
]

lines = []
lines.append("# Récapitulatif Exhaustif des Modifications — Phase 1 (Avant ➔ Après)")
lines.append("")
lines.append("> **Date :** 27 Octobre 2026")
lines.append("> **Périmètre :** Systèmes Nolvus & Patchs d'Équilibrage (`Armors`, `Weapons`, `Vokriinator Black Integration`, `Clothes`, `DLC`, `Experience`, etc.)")
lines.append("> **Objectifs appliqués :** Élimination des balises illégales, synchronisation des chiffres modifiés par Nolvus, élimination des calques/anglais, rétablissement des noms réels d'armes et d'atouts.")
lines.append("")
lines.append("---")
lines.append("")

total_diff_count = 0

for file_rel in git_files:
    file_path = Path(file_rel)
    if not file_path.is_file():
        continue
        
    # Get HEAD content via git
    cmd = ["git", "show", f"HEAD:{file_rel}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if res.returncode != 0:
        continue
        
    old_data = json.loads(res.stdout)
    new_data = json.load(open(file_path, "r", encoding="utf-8"))
    
    # Map by form_id + type
    old_map = {}
    for it in old_data:
        key = (it.get("form_id"), it.get("type"), it.get("original"))
        old_map[key] = it.get("string") or it.get("translation")
        
    file_changes = []
    for it in new_data:
        key = (it.get("form_id"), it.get("type"), it.get("original"))
        new_val = it.get("string") or it.get("translation")
        old_val = old_map.get(key)
        
        if old_val is not None and old_val != new_val:
            file_changes.append({
                "form_id": it.get("form_id"),
                "type": it.get("type"),
                "original": it.get("original"),
                "avant": old_val,
                "apres": new_val
            })
            
    if file_changes:
        total_diff_count += len(file_changes)
        mod_name = file_path.parent.name
        lines.append(f"## 📁 {mod_name} (`{file_path.name}`)")
        lines.append(f"*Nombre de modifications :* **{len(file_changes)}**")
        lines.append("")
        lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne traduction) | Après (Traduction corrigée & validée) |")
        lines.append("| :--- | :--- | :--- | :--- |")
        
        for c in file_changes:
            fid_str = f"`{c['form_id']}`<br>*{c['type']}*"
            orig_str = c['original'].replace("\n", " ").replace("|", "\\|")
            avant_str = c['avant'].replace("\n", " ").replace("|", "\\|")
            apres_str = f"**{c['apres'].replace(chr(10), ' ').replace('|', '\\|')}**"
            lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
            
        lines.append("")
        lines.append("---")
        lines.append("")

lines.insert(6, f"* **Total des entrées réalignées et corrigées :** **{total_diff_count} modifications**\n")

out_file = Path("recap_modifications_phase1.md")
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated {out_file} with {total_diff_count} total diffs ({out_file.stat().st_size} bytes)")
