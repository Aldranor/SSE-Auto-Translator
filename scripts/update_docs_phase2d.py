import re

# 1. Update PLAN_RELECTURE_FINALE.md
with open('PLAN_RELECTURE_FINALE.md', 'r', encoding='utf-8') as f:
    plan = f.read()

plan = plan.replace(
    "| **Phase 2** | **Audit Exhaustif de TOUS les Patchs Créés Localement & d'Intégration Nolvus** | 🟡 **EN COURS** (2A, 2B & 2C validées, 2D suivante) |",
    "| **Phase 2** | **Audit Exhaustif de TOUS les Patchs Créés Localement & d'Intégration Nolvus** | 🟡 **EN COURS** (2A, 2B, 2C & 2D validées, 2E suivante) |"
)
plan = plan.replace(
    "### 🔹 Sous-phase 2D : Patchs de Conflits PNJs, Races & Apparences\n",
    "### 🔹 Sous-phase 2D : Patchs de Conflits PNJs, Races & Apparences (✅ VALIDÉE — recap_modifications_phase2d.md)\n"
)

with open('PLAN_RELECTURE_FINALE.md', 'w', encoding='utf-8') as f:
    f.write(plan)
print("Updated PLAN_RELECTURE_FINALE.md.")

# 2. Update TRADUCTIONS_VERIFIEES.md
with open('TRADUCTIONS_VERIFIEES.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_row = "| **Patchs de Conflits PNJs, Races & Apparences (Phase 2D)** | `Modpocalypse NPCs - Patch Collection` (13 plugins), `True Sons of Skyrim Refined Patches` (7 plugins), `Fanatical Enemies - Patches` (4 plugins), `DIbella's Blessing - RSV Exclusion Patches`, `AI Overhaul - Nithi NPC Enhancements Patch Hub` (4 plugins) | **Audit d'impact et harmonisation validés (Phase 2D) :** Contrôle systématique de 1 902 enregistrements de PNJs (`NPC_ FULL` et `NPC_ SHRT`) sur 29 plugins avec ciblage unitaire strict `(form_id, type, index, original)`. Harmonisation rigoureuse avec le canon officiel Bethesda et USSEP France (*Endarië*, *Érikur*, *Capitaine Nautonier*, *Taarië*, *Skaggi le Balafré*, *Léontius Salvius*, *Suvaris Athéron*, *Michelle Lylvieve*, *Sévério Pélagia*, *Érik*, *Gardienne Carcette*, *Valkynaz drémora*, *Laelette la vampire*). Rétablissement des accents officiels et de l'intégrité des rôles. Zéro collision multi-enregistrements, récapitulatif détaillé consigné dans `recap_modifications_phase2d.md`. |\n"

# Insert after line 143 (which is Phase 2C)
for i, l in enumerate(lines):
    if "Méta-Hubs de Patchs & Cohérence Monde / Éclairage (Phase 2C)" in l:
        lines.insert(i + 1, new_row)
        break

with open('TRADUCTIONS_VERIFIEES.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated TRADUCTIONS_VERIFIEES.md.")
