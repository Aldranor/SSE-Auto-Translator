import re

# 1. Update PLAN_RELECTURE_FINALE.md
with open('PLAN_RELECTURE_FINALE.md', 'r', encoding='utf-8') as f:
    plan = f.read()

plan = plan.replace(
    "| **Phase 2** | **Audit Exhaustif de TOUS les Patchs Créés Localement & d'Intégration Nolvus** | 🟡 **EN COURS** (2A, 2B, 2C & 2D validées, 2E suivante) |",
    "| **Phase 2** | **Audit Exhaustif de TOUS les Patchs Créés Localement & d'Intégration Nolvus** | ✅ **TERMINÉ & VALIDÉ** (2A, 2B, 2C, 2D & 2E validées) |"
)
plan = plan.replace(
    "### 🔹 Sous-phase 2E : Micro-Patchs de Compatibilité & Corrections Unitaires\n",
    "### 🔹 Sous-phase 2E : Micro-Patchs de Compatibilité & Corrections Unitaires (✅ VALIDÉE — recap_modifications_phase2e.md)\n"
)

with open('PLAN_RELECTURE_FINALE.md', 'w', encoding='utf-8') as f:
    f.write(plan)
print("Updated PLAN_RELECTURE_FINALE.md.")

# 2. Update TRADUCTIONS_VERIFIEES.md
with open('TRADUCTIONS_VERIFIEES.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_row = "| **Micro-Patchs de Compatibilité & Corrections Unitaires (Phase 2E)** | 110 plugins de micro-patchs de compatibilité locaux et corrections isolées (`AttackoDaedra`, `Wintersun Tribunal Integration`, `YOT - Your Own Thoughts` [Clockwork, Unslaad, Carved Brink, Wheels of Lull], `JK's College of Winterhold`, `DynDOLOD`, `For Honor in Skyrim`, `AP - Missile Additional Starts`, `Alternate Perspective - New Beginnings`, `Gray Quarter Overhaul`, etc.) | **Audit d'impact et harmonisation validés (Phase 2E) :** Contrôle systématique de 3 348 enregistrements sur 110 plugins avec protocole d'anti-collision unitaire `(form_id, type, index, original)` strict. Correction du contresens critique `Namiiric Slash` (`Flèche namiirique` corrigé en `Entaille namiirique`). Traduction intégrale de l'anglais résiduel sur les effets de cape Wintersun GotT (`Epic Killer - Cloak Proc` -> `Tueur épique - Déclenchement de la cape`). Correction de bégaiement orthographique dans YOT Clockwork (`arme une peut` -> `arme peut`). Conformité à 100 % des cellules et mondes Bethesda. Récapitulatif : `recap_modifications_phase2e.md`. |\n"

# Insert after line for Phase 2D
for i, l in enumerate(lines):
    if "Patchs de Conflits PNJs, Races & Apparences (Phase 2D)" in l:
        lines.insert(i + 1, new_row)
        break

with open('TRADUCTIONS_VERIFIEES.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated TRADUCTIONS_VERIFIEES.md.")
