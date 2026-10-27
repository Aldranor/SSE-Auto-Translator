import json
from pathlib import Path
from collections import defaultdict

data = json.load(open("local_unverified_analysis.json", encoding="utf-8"))
unverif = data["unverified"]
unverif.sort(key=lambda x: (x["date"], x["name"].lower()))

# Enhanced classification
def classify(u):
    name_l = u["name"].lower()
    files_l = " ".join(u["unverified_files"]).lower()
    combined = name_l + " " + files_l
    
    if any(k in combined for k in ["remiel", "vigile", "fanatical", "enemy", "enemies", "boss", "follower", "companion", "inigo", "vilkas", "serana", "aedan"]):
        return "Compagnons majeurs, Créatures & Ennemis"
    elif "lotd" in combined or "dragonborn" in combined or "museum" in combined or "dbm" in combined:
        return "Legacy of the Dragonborn (LOTD) & Addons"
    elif "nolvus" in combined:
        return "Patchs & Intégrations spécifiques Nolvus"
    elif any(k in combined for k in ["modpocalypse", "rs children", "children", "npc", "citizens"]):
        return "Refontes de PNJs & Enfants (Modpocalypse, RS Children...)"
    elif any(k in combined for k in ["perk", "spell", "magic", "combat", "animation", "stance", "vokrii", "adamant", "stealth", "arrow", "enchant", "alchemy", "death", "dodge", "poise", "parry", "experience", "skill"]):
        return "Gameplay, Magie, Atouts & Combats"
    elif any(k in combined for k in ["armor", "weapon", "sword", "bow", "shield", "blade", "axe", "helm", "robe", "clothes", "outfit", "ring", "amulet", "craft", "smithing", "spear", "dismembering", "apparel"]):
        return "Armes, Armures, Vêtements & Forge"
    elif any(k in combined for k in ["quest", "dungeon", "city", "town", "wyrm", "falskaar", "bruma", "reach", "sanctum", "shack", "temple", "gate", "ruin", "interior", "market", "whiterun", "solitude", "windhelm", "riften"]):
        return "Quêtes, Villes, Intérieurs & Nouveaux Lieux"
    elif any(k in combined for k in ["audio", "sound", "music", "weather", "lighting", "water", "tree", "grass", "texture", "mesh", "fx", "immersion", "campfire", "hunter", "enb", "seasons", "greenery"]):
        return "Environnement, Graphismes, Audio & Immersion"
    elif any(k in combined for k in ["mcm", "menu", "ui", "hud", "key", "display", "font", "interface", "map", "navigation", "navmesh"]):
        return "Interface, Navigation & Utilitaires"
    else:
        return "Autres Patchs de Compatibilité & Corrections"

grouped = defaultdict(list)
for u in unverif:
    cat = classify(u)
    grouped[cat].append(u)

# Order categories logically
category_order = [
    "Compagnons majeurs, Créatures & Ennemis",
    "Legacy of the Dragonborn (LOTD) & Addons",
    "Patchs & Intégrations spécifiques Nolvus",
    "Refontes de PNJs & Enfants (Modpocalypse, RS Children...)",
    "Gameplay, Magie, Atouts & Combats",
    "Armes, Armures, Vêtements & Forge",
    "Quêtes, Villes, Intérieurs & Nouveaux Lieux",
    "Environnement, Graphismes, Audio & Immersion",
    "Interface, Navigation & Utilitaires",
    "Autres Patchs de Compatibilité & Corrections"
]

total_strings = sum(u["total_strings"] for u in unverif)
total_files = sum(u["total_files"] for u in unverif)

lines = []
lines.append("# Répertoire des Traductions Locales Non Vérifiées (< Octobre 2026)")
lines.append("")
lines.append("> **Contexte :** Traductions de type **Source Locale** (`Source.Local`) importées préalablement (antérieures au 01/10/2026) dans la base de données du traducteur, non auditées dans `TRADUCTIONS_VERIFIEES.md`.")
lines.append("> **Date d'analyse :** 27 Octobre 2026")
lines.append("")
lines.append("## 📊 Synthèse Globale")
lines.append("")
lines.append(f"* **Total de mods/traductions identifiés :** **{len(unverif)}**")
lines.append(f"* **Nombre total de fichiers de localisation (.json) :** **{total_files}**")
lines.append(f"* **Volume total de chaînes à auditer :** **{total_strings:,} chaînes**")
lines.append("* **Période des imports :** Principalement **décembre 2024**, **janvier 2025** et **avril/mai/novembre 2025** (toutes antérieures à octobre 2026).")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 📑 Répartition par Catégorie")
lines.append("")
lines.append("| Catégorie | Nombre de mods | Total fichiers | Total chaînes |")
lines.append("| :--- | :---: | :---: | :---: |")

for cat in category_order:
    items = grouped[cat]
    s_cnt = sum(it["total_strings"] for it in items)
    f_cnt = sum(it["total_files"] for it in items)
    lines.append(f"| **{cat}** | {len(items)} | {f_cnt} | {s_cnt:,} |")

lines.append("")
lines.append("---")
lines.append("")

for cat in category_order:
    items = grouped[cat]
    s_cnt = sum(it["total_strings"] for it in items)
    f_cnt = sum(it["total_files"] for it in items)
    lines.append(f"## 📁 {cat} ({len(items)} mods — {s_cnt:,} chaînes)")
    lines.append("")
    lines.append("| Nom dans la base | Date d'import | Fichiers concernés | Chaînes |")
    lines.append("| :--- | :---: | :--- | :---: |")
    
    # Sort items inside category by string count descending
    items_sorted = sorted(items, key=lambda x: x["total_strings"], reverse=True)
    for it in items_sorted:
        files_str = "<br>".join([f"`{f}`" for f in it["unverified_files"]]) if it["unverified_files"] else "*(dossier vide)*"
        lines.append(f"| **{it['name']}** | {it['date']} | {files_str} | {it['total_strings']:,} |")
    lines.append("")

artifact_content = "\n".join(lines)
output_path = Path(r"C:\Users\mouaw\.gemini\antigravity\brain\ac368bee-d202-4c72-87be-2434745643fb\listing_traductions_locales_non_verifiees.md")
output_path.write_text(artifact_content, encoding="utf-8")
project_path = Path("listing_traductions_locales_non_verifiees.md")
project_path.write_text(artifact_content, encoding="utf-8")
print(f"Artifact written to {output_path} ({len(artifact_content)} bytes)")
print(f"Project file written to {project_path} ({len(artifact_content)} bytes)")

