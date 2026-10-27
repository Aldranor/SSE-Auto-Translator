import json
from pathlib import Path

# Load files to get previous translations or diffs
db = Path("data/user/database/french")

# We can construct the exact before/after for all the patches
recap_data = []

# 1. Armors Balance Patch
p_armors = db / "Nolvus Awakening Armors Balance Patch.esp - French" / "nolvus awakening armors balance patch.esp.json"
# We know the diff from git diff!
# 2. Weapons Balance Patch
# We know from git diff!

# Let's write the generator script that pulls the exact before/after from git diff where available,
# and from the fixes dict for the non-git-tracked files!
import subprocess

def clean_md(s):
    if not s:
        return ""
    return str(s).replace("\r", "").replace("\n", " ").replace("|", " - ").strip()

def format_fid(fid, rec_type):
    parts = str(fid).split("|")
    if len(parts) == 2:
        return f"`{parts[0]}` ({parts[1]})<br>*{clean_md(rec_type)}*"
    return f"`{clean_md(fid)}`<br>*{clean_md(rec_type)}*"

def get_git_diff_entries(file_rel):
    cmd = ["git", "show", f"HEAD:{file_rel}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    if res.returncode != 0:
        return []
    old_data = json.loads(res.stdout)
    new_data = json.load(open(file_rel, "r", encoding="utf-8"))
    
    old_map = {}
    for it in old_data:
        key = (it.get("form_id"), it.get("type"))
        old_map[key] = it.get("string") or it.get("translation")
        
    diffs = []
    for it in new_data:
        key = (it.get("form_id"), it.get("type"))
        new_val = it.get("string") or it.get("translation")
        old_val = old_map.get(key)
        if old_val is not None and old_val != new_val:
            diffs.append({
                "form_id": it.get("form_id"),
                "type": it.get("type"),
                "original": it.get("original"),
                "avant": old_val,
                "apres": new_val,
                "nature": "Balises illégales / Variantes de nom / Distinction de type"
            })
    return diffs


lines = []
lines.append("# Récapitulatif Détaillé des Modifications — Phase 1 (Avant ➔ Après)")
lines.append("")
lines.append("> **Date :** 27 Octobre 2026")
lines.append("> **Périmètre :** Systèmes Nolvus & Patchs d'Équilibrage (`Armors`, `Weapons`, `Vokriinator Black Integration`, `Clothes`, `DLC`, `Experience`, etc.)")
lines.append("> **Objectifs appliqués :** Élimination des balises illégales, synchronisation des chiffres modifiés par Nolvus, élimination des calques/anglais, rétablissement des noms réels d'armes et d'atouts.")
lines.append("")
lines.append("---")
lines.append("")

# Section 1 : Vokriinator Black Nolvus Integration
p_vok = db / "Nolvus Awakening Vokriinator Black Integration.esp - French" / "nolvus awakening vokriinator black integration.esp.json"
if p_vok.is_file():
    vok_items = json.load(open(p_vok, encoding="utf-8"))
    # The perks that were rebalanced in Phase 1
    # We documented the old vs new in our analysis!
    vok_diffs = [
        {
            "form_id": "0103A15B|SPERG-SSE.esp",
            "type": "PERK DESC",
            "original": "Attacks with war axes deal 25% more critical damage. Attacks with all weapons are 5% more likely to critically hit. Cannot be taken with Bone Breaker or Bladesman.",
            "avant": "Les attaques à la hache à une main infligent 50 % de dégâts critiques en plus. Les attaques avec les autres armes ont 5 % de chances de faire un coup critique. Ne peut être pris avec Brise-os ou Fine lame.",
            "apres": "Les attaques à la hache de guerre infligent 25 % de dégâts critiques supplémentaires. Les attaques avec toutes les armes ont 5 % de chances en plus de porter un coup critique. Incompatible avec Brise-os ou Fine lame.",
            "nature": "Chiffre réaligné sur le patch Nolvus (+25% au lieu de +50%), terminologie canonique"
        },
        {
            "form_id": "01027727|SPERG-SSE.esp",
            "type": "PERK DESC",
            "original": "Critical damage is increased by 10% when wielding one or more one-handed weapons.",
            "avant": "Toutes les armes frappent 15 % plus vite et les dégâts critiques augmentent de 50 % si vous maniez une ou plusieurs armes à une main.",
            "apres": "Les dégâts critiques augmentent de 10 % lorsque vous maniez une ou plusieurs armes à une main.",
            "nature": "Mise à jour d'effet Nolvus (+10% dégâts critiques au lieu de l'ancien effet composite +15%/+50%)"
        },
        {
            "form_id": "04002E07|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a sword cause targets to bleed for 10 seconds. When a bleeding target falls below 25% Health, your attacks against that target are critical strikes that deals 25% more critical damage.",
            "avant": "Les attaques puissantes vers l'avant avec une épée font saigner les cibles pendant 20 secondes. Lorsque la cible tombe sous les 25 % de santé, vos attaques lui infligent une frappe critique qui inflige 10 fois plus de dégâts critiques.",
            "apres": "Les attaques puissantes à l'épée font saigner la cible pendant 10 secondes. Lorsque sa santé passe sous les 25 %, vos attaques contre elle deviennent des frappes critiques infligeant 25 % de dégâts critiques supplémentaires.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (10s au lieu de 20s, +25% au lieu de 10x)"
        },
        {
            "form_id": "04003911|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with warhammers reduce the armor rating of armored enemies by 60 points for 10 seconds.",
            "avant": "Les attaques au marteau diminuent la valeur d'armure des ennemis en armure de 125 points pendant 15 secondes.",
            "apres": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 60 points pendant 10 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (60 pts / 10s au lieu de 125 pts / 15s)"
        },
        {
            "form_id": "04003910|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with warhammers reduce the armor rating of armored enemies by 40 points for 10 seconds.",
            "avant": "Les attaques au marteau diminuent la valeur d'armure des ennemis en armure de 100 points pendant 15 secondes.",
            "apres": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 40 points pendant 10 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (40 pts / 10s au lieu de 100 pts / 15s)"
        },
        {
            "form_id": "0400390F|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with warhammers reduce the armor rating of armored enemies by 30 points for 10 seconds.",
            "avant": "Les attaques au marteau diminuent la valeur d'armure des ennemis en armure de 75 points pendant 15 secondes.",
            "apres": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 30 points pendant 10 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (30 pts / 10s au lieu de 75 pts / 15s)"
        },
        {
            "form_id": "07003380|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with maces reduce the armor rating of armored enemies by 20 points for 5 seconds.",
            "avant": "Les attaques à la masse diminuent la valeur d'armure des ennemis en armure de 50 points pendant 15 secondes.",
            "apres": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 20 points pendant 5 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (20 pts / 5s au lieu de 50 pts / 15s)"
        },
        {
            "form_id": "07003381|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with maces reduce the armor rating of armored enemies by 30 points for 5 seconds.",
            "avant": "Les attaques à la masse diminuent la valeur d'armure des ennemis en armure de 75 points pendant 15 secondes.",
            "apres": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 30 points pendant 5 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (30 pts / 5s au lieu de 75 pts / 15s)"
        },
        {
            "form_id": "07003382|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with maces reduce the armor rating of armored enemies by 50 points for 5 seconds.",
            "avant": "Les attaques à la masse diminuent la valeur d'armure des ennemis en armure de 100 points pendant 15 secondes.",
            "apres": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 50 points pendant 5 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (50 pts / 5s au lieu de 100 pts / 15s)"
        },
        {
            "form_id": "0003AF81|Skyrim.esm",
            "type": "PERK DESC",
            "original": "Power attack damage is increased by 0.05% per point of Stamina.(requires Disciplined Fighter)",
            "avant": "Les dégâts infligés par une attaque puissante avec les armes à une main augmentent de 15 % plus 0,1 % par point de vigueur. Débloque les décapitations.",
            "apres": "Les dégâts des attaques puissantes augmentent de 0,05 % par point de vigueur (requiert Combattant discipliné).",
            "nature": "Chiffres réalignés sur le scaling Nolvus (0,05 % sans résidu de décapitation)"
        },
        {
            "form_id": "00052D52|Skyrim.esm",
            "type": "PERK DESC",
            "original": "Power attack damage with two-handed weapons is increased by 0.05% per point of Stamina.",
            "avant": "Les dégâts infligés par une attaque puissante avec les armes à deux mains augmentent de 15 % plus 0,1 % par point de vigueur. Débloque les décapitations.",
            "apres": "Les dégâts des attaques puissantes avec les armes à deux mains augmentent de 0,05 % par point de vigueur.",
            "nature": "Chiffres réalignés sur le scaling Nolvus (0,05 % par point de vigueur)"
        },
        {
            "form_id": "04003E7B|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a greatsword destabilize a target, increasing the damage of your regular attacks against the target by 15% for 4 seconds.",
            "avant": "Les attaques puissantes à l'espadon déstabilisent une cible, augmentent les dégâts infligés par vos attaques ordinaires contre la cible de 25 % pendant 5 secondes.",
            "apres": "Les attaques puissantes à l'espadon déstabilisent la cible, augmentant les dégâts de vos attaques ordinaires contre elle de 15 % pendant 4 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (15% / 4s au lieu de 25% / 5s)"
        },
        {
            "form_id": "04003E7C|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a greatsword destabilize a target, increasing the damage of your regular attacks against the target by 25% for 4 seconds.",
            "avant": "Les attaques puissantes à l'espadon déstabilisent une cible, augmentent les dégâts infligés par vos attaques ordinaires contre la cible de 50 % pendant 5 secondes.",
            "apres": "Les attaques puissantes à l'espadon déstabilisent la cible, augmentant les dégâts de vos attaques ordinaires contre elle de 25 % pendant 4 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (25% / 4s au lieu de 50% / 5s)"
        },
        {
            "form_id": "07003909|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with greatswords reduce the target's attack damage by 10% for 3 seconds.",
            "avant": "Les attaques à l'espadon diminuent les dégâts d'attaque de la cible de 15 % pendant 3 secondes.",
            "apres": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 10 % pendant 3 secondes.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (10% au lieu de 15%)"
        },
        {
            "form_id": "0700390A|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with greatswords reduce the target's attack damage by 15% for 3 seconds.",
            "avant": "Les attaques à l'espadon diminuent les dégâts d'attaque de la cible de 20 % pendant 3 secondes.",
            "apres": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 15 % pendant 3 secondes.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (15% au lieu de 20%)"
        },
        {
            "form_id": "0700390B|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Attacks with greatswords reduce the target's attack damage by 20% for 3 seconds.",
            "avant": "Les attaques à l'espadon diminuent les dégâts d'attaque de la cible de 25 % pendant 3 secondes.",
            "apres": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 20 % pendant 3 secondes.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (20% au lieu de 25%)"
        },
        {
            "form_id": "04003E74|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a mace deliver a critical strike that deals 20% more critical damage (45% against the undead). Targets can only be struck by Smite once every 30 seconds.",
            "avant": "Les attaques puissantes à la masse infligent un triple coup critique et un quadruple aux morts-vivants. Les cibles ne peuvent être touchées par Foudroiement qu'une fois toutes les 30 secondes.",
            "apres": "Les attaques puissantes à la masse délivrent une frappe critique qui inflige 20 % de dégâts critiques supplémentaires (45 % contre les morts-vivants). Ne peut frapper une même cible par Châtiment qu'une fois toutes les 30 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (+20%/+45% au lieu de triple/quadruple)"
        },
        {
            "form_id": "07003E75|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a mace deliver a critical strike that deals 40% more critical damage (55% against the undead). Targets can only be struck by Smite once every 30 seconds.",
            "avant": "Les attaques puissantes à la masse infligent un sextuple coup critique et un octuple aux morts-vivants. Les cibles ne peuvent être touchées par Foudroiement qu'une fois toutes les 30 secondes.",
            "apres": "Les attaques puissantes à la masse délivrent une frappe critique qui inflige 40 % de dégâts critiques supplémentaires (55 % contre les morts-vivants). Ne peut frapper une même cible par Châtiment qu'une fois toutes les 30 secondes.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (+40%/+55% au lieu de sextuple/octuple)"
        },
        {
            "form_id": "07003E7F|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a warhammer have 15% chance of a critical strike. All critical strikes with a warhammer deal 75% more critical damage.",
            "avant": "Les attaques puissantes au marteau ont 15 % de chances d'infliger un double coup critique. Tous les coups critiques avec un marteau font le double de dégâts critiques.",
            "apres": "Les attaques puissantes au marteau de guerre ont 15 % de chances d'infliger une frappe critique. Tous les coups critiques au marteau de guerre infligent 75 % de dégâts critiques supplémentaires.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (+75% de dégâts critiques au lieu de dégâts doublés)"
        },
        {
            "form_id": "07003E80|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a warhammer have 25% chance of a critical strike. All critical strikes with a warhammer deal 75% more critical damage.",
            "avant": "Les attaques puissantes au marteau ont 25 % de chances d'infliger un double coup critique. Tous les coups critiques avec un marteau font le double de dégâts critiques.",
            "apres": "Les attaques puissantes au marteau de guerre ont 25 % de chances d'infliger une frappe critique. Tous les coups critiques au marteau de guerre infligent 75 % de dégâts critiques supplémentaires.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (+75% de dégâts critiques au lieu de dégâts doublés)"
        },
        {
            "form_id": "0700B149|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "One-handed weapons do 20% more damage.",
            "avant": "Les armes à une main infligent 25 % de dégâts supplémentaires.",
            "apres": "Les armes à une main infligent 20 % de dégâts supplémentaires.",
            "nature": "Chiffre réaligné sur le nerf Nolvus (20% au lieu de 25%)"
        },
        {
            "form_id": "0700B14A|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "One-handed weapons do 40% more damage, and critical strikes with one-handed weapons do 0.5% more critical damage per level of One-Handed.",
            "avant": "Les armes à une mains infligent 50 % de dégâts supplémentaires et les coups critiques infligés avec ces dernières font 2 % de dégâts critiques supplémentaires par niveau de compétence d'arme à une main.",
            "apres": "Les armes à une main infligent 40 % de dégâts supplémentaires, et les coups critiques portés avec elles infligent 0,5 % de dégâts critiques supplémentaires par niveau d'Arme à une main.",
            "nature": "Chiffres réalignés sur le nerf Nolvus (40% au lieu de 50%, 0,5% au lieu de 2%)"
        },
        {
            "form_id": "0700B14B|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Two-handed weapons do 20% more damage.",
            "avant": "Les armes à deux mains infligent 25 % de dégâts supplémentaires.",
            "apres": "Les armes à deux mains infligent 20 % de dégâts supplémentaires.",
            "nature": "Chiffre réaligné sur le nerf Nolvus (20% au lieu de 25%)"
        },
        {
            "form_id": "0700B14C|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Two-handed weapons do 40% more damage, and critical strikes with two-handed weapons do 0.5% more critical damage per level of Two-Handed.",
            "avant": "Les armes à deux mains infligent 50 % de dégâts supplémentaires et les coups critiques infligés avec ces dernières font 2 % de dégâts critiques supplémentaires par niveau de compétence à Deux mains.",
            "apres": "Les armes à deux mains infligent 40 % de dégâts supplémentaires, et les coups critiques portés avec elles infligent 0,5 % de dégâts critiques supplémentaires par niveau d'Arme à deux mains.",
            "nature": "Chiffres réalignés sur le nerf Nolvus (40% au lieu de 50%, 0,5% au lieu de 2%)"
        },
        {
            "form_id": "06000B93|Vokrii - Minimalistic Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Two-handed power attacks have 25% chance to paralyze targets, inflicting a critical strike that deals 40% more damage.",
            "avant": "Les attaques puissantes à deux mains vers l'avant ont 25 % de chances de paralyser les cibles, infligeant un coup critique pour le double de dégâts critiques.",
            "apres": "Les attaques puissantes à deux mains ont 25 % de chances de paralyser la cible, portant une frappe critique qui inflige 40 % de dégâts supplémentaires.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (+40% au lieu de double)"
        },
        {
            "form_id": "06000BA0|Vokrii - Minimalistic Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "One-handed power attacks have 25% chance to knock targets down, inflicting a critical strike inflicting a critical strike that deals 40% more damage.",
            "avant": "Les attaques puissantes en avant à une main ont 25 % de chances de renverser la cible et d'infliger un coup critique pour le double de dégâts critiques.",
            "apres": "Les attaques puissantes à une main ont 25 % de chances de renverser la cible, portant une frappe critique qui inflige 40 % de dégâts supplémentaires.",
            "nature": "Chiffre réaligné sur l'équilibrage Nolvus (+40% au lieu de double)"
        },
        {
            "form_id": "040B0D40|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Hitting a target with a power attack with a dagger has a 15% chance to paralyze the target for 3 seconds. Your attacks against the paralyzed target are critical strikes that deal 50% more critical damage.",
            "avant": "Les attaques puissantes à la dague vers l'avant, latérales ou vers l'arrière qui touchent leur cible dans les 30 secondes la paralysent pendant 20 secondes. Les attaques contre les cibles paralysées leur infligent un nonuple coup critique.",
            "apres": "Toucher une cible avec une attaque puissante à la dague a 15 % de chances de la paralyser pendant 3 secondes. Vos attaques contre la cible paralysée sont des frappes critiques infligeant 50 % de dégâts critiques supplémentaires.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (15% / 3s / +50% au lieu de 30s / 20s / 9x)"
        },
        {
            "form_id": "040B0D3F|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "Power attacks with a dagger have a 25% chance to inflict distracting wounds, draining 75 points of Magicka and Stamina and halting regeneration for 5 seconds.",
            "avant": "Les attaques latérales puissantes à la dague infligent des blessures distrayantes, drainant 75 points de magie et de vigueur et arrêtant la régénération pendant 5 secondes.",
            "apres": "Les attaques puissantes à la dague ont 25 % de chances d'infliger des blessures distrayantes, drainant 75 points de magie et de vigueur et interrompant leur régénération pendant 5 secondes.",
            "nature": "Condition d'attaque puissante sans restriction de direction, formulation fluide"
        },
        {
            "form_id": "04000D63|Ordinator - Combat Styles.esp",
            "type": "PERK DESC",
            "original": "Take 30% less attack damage while power attacking with a one-handed weapon in one hand and nothing in the other",
            "avant": "Lorsque vous utilisez une arme à une main dans une main et rien dans l'autre, la vitesse d'attaque augmente de 40 %.",
            "apres": "Vous subissez 30 % de dégâts en moins lors d'une attaque puissante si vous maniez une arme à une main et avez l'autre main vide.",
            "nature": "Effet corrigé : réduction de dégâts subis (-30%) au lieu d'augmentation de vitesse d'attaque (+40%)"
        },
        {
            "form_id": "04000D62|Ordinator - Combat Styles.esp",
            "type": "PERK DESC",
            "original": "Take 15% less attack damage while power attacking with a one-handed weapon in one hand and nothing in the other",
            "avant": "Lorsque vous utilisez une arme à une main dans une main et rien dans l'autre, la vitesse d'attaque augmente de 20 %.",
            "apres": "Vous subissez 15 % de dégâts en moins lors d'une attaque puissante si vous maniez une arme à une main et avez l'autre main vide.",
            "nature": "Effet corrigé : réduction de dégâts subis (-15%) au lieu d'augmentation de vitesse d'attaque (+20%)"
        },
        {
            "form_id": "07004EEF|Ordinator - Perks of Skyrim.esp",
            "type": "PERK DESC",
            "original": "While dual wielding in combat, enter a murderous frenzy every 20 to 40 seconds. For 4 seconds, dual wield power attacks deal 30% more damage and 50% more critical damage.",
            "avant": "Lorsque vous combattez à deux armes, vous entrez dans une rage meurtrière toutes les 20 à 40 secondes, augmentant de 50 % les dégâts infligés par vos attaques puissantes et de 100 % ceux de vos coups critiques pendant 8 secondes.",
            "apres": "Lorsque vous combattez avec deux armes, vous entrez dans une frénésie meurtrière toutes les 20 à 40 secondes. Pendant 4 secondes, vos attaques puissantes avec deux armes infligent 30 % de dégâts et 50 % de dégâts critiques supplémentaires.",
            "nature": "Chiffres réalignés sur l'équilibrage Nolvus (4s / +30% / +50% au lieu de 8s / +50% / +100%)"
        },
        {
            "form_id": "08000819|Ordinator - Combat Styles.esp",
            "type": "SPEL FULL",
            "original": "Celerity",
            "avant": "Augmente la vitesse de course de 10 %.",
            "apres": "Célérité",
            "nature": "Rétablissement du nom du sort (la description avait écrasé le titre)"
        }
    ]
    
    lines.append("## 📁 Nolvus Awakening Vokriinator Black Integration (`nolvus awakening vokriinator black integration.esp.json`)")
    lines.append(f"*Nombre de modifications majeures :* **{len(vok_diffs)} atouts et sorts réalignés**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne traduction désynchronisée) | Après (Traduction réalignée sur Nolvus) | Nature du correctif |")
    lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for c in vok_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        nat_str = clean_md(c['nature'])
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} | {nat_str} |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Section 2 : Armors Balance Patch (from git diff)
armors_diffs = get_git_diff_entries("data/user/database/french/Nolvus Awakening Armors Balance Patch.esp - French/nolvus awakening armors balance patch.esp.json")
if armors_diffs:
    lines.append("## 📁 Nolvus Awakening Armors Balance Patch (`nolvus awakening armors balance patch.esp.json`)")
    lines.append(f"*Nombre de modifications :* **{len(armors_diffs)} entrées corrigées**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne traduction) | Après (Traduction corrigée & validée) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for c in armors_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Section 3 : Weapons Balance Patch (from git diff)
weap_diffs = get_git_diff_entries("data/user/database/french/Nolvus Awakening Weapons Balance Patch.esp - French/nolvus awakening weapons balance patch.esp.json")
if weap_diffs:
    lines.append("## 📁 Nolvus Awakening Weapons Balance Patch (`nolvus awakening weapons balance patch.esp.json`)")
    lines.append(f"*Nombre de modifications :* **{len(weap_diffs)} entrées corrigées**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne traduction) | Après (Traduction corrigée & validée) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for c in weap_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Section 4 : Weapons Patch (Dragonbane)
weap_p_diffs = get_git_diff_entries("data/user/database/french/Nolvus Awakening Weapons Patch - French/nolvus awakening weapons patch.esp.json")
if weap_p_diffs:
    lines.append("## 📁 Nolvus Awakening Weapons Patch (`nolvus awakening weapons patch.esp.json`)")
    lines.append(f"*Nombre de modifications :* **{len(weap_p_diffs)} entrées corrigées**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne traduction avec balises illégales) | Après (Traduction propre sans crash) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for c in weap_p_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Section 5 : Experience Integration (Dawnfang Quest)
lines.append("## 📁 Nolvus Awakening Experience Integration (`nolvus awakening experience integration.esp.json`)")
lines.append("*Nombre de modifications :* **1 entrée majeure (quête Croc-du-Matin restée en anglais)**")
lines.append("")
lines.append("| FormID / Type | Texte Original (EN) | Avant (Non traduit / 100% anglais) | Après (Traduction littéraire officielle) |")
lines.append("| :--- | :--- | :--- | :--- |")
lines.append("| `1D000F18` (ccbgssse013-dawnfang.esl)<br>*QUST CNAM* | Having followed the apparition, I have found myself inside an abandoned vault. A mysterious sword floats suspended in a magical field at the heart of the vault. Judging by the condition of this place, it looks as if it has lain undisturbed for a very long time. Perhaps if I proceed forward, I may find some answers and a way to unlock the sword. | Having followed the apparition, I have found myself inside an abandoned vault. A mysterious sword floats suspended in a magical field at the heart of the vault. Judging by the condition of this place, it looks as if it has lain undisturbed for a very long time. Perhaps if I proceed forward, I may find some answers and a way to unlock the sword. | **Après avoir suivi l'apparition, je me suis retrouvé dans un caveau abandonné. Une épée mystérieuse flotte, suspendue dans un champ magique au cœur de la salle. À en juger par l'état des lieux, personne n'y a pénétré depuis une éternité. Si je m'avance, je trouverai peut-être des réponses et un moyen de libérer l'épée.** |")
lines.append("")
lines.append("---")
lines.append("")

# Section 6 : Combat Scaling Overhaul (Romanov)
cso_diffs = get_git_diff_entries("data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level.esp.json")
if cso_diffs:
    lines.append("## 📁 Nolvus Awakening Combat Scaling Overhaul (`nolvus awakening combat scaling overhaul - enemy level.esp.json`)")
    lines.append(f"*Nombre de modifications :* **{len(cso_diffs)} entrée**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Anglais) | Après (Français) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for c in cso_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
    lines.append("")
    lines.append("---")
    lines.append("")

# Section 7 : Crafting Patch
craft_diffs = get_git_diff_entries("data/user/database/french/Nolvus Awakening Crafting Patch - French/nolvus awakening crafting patch.esp.json")
if craft_diffs:
    lines.append("## 📁 Nolvus Awakening Crafting Patch (`nolvus awakening crafting patch.esp.json`)")
    lines.append(f"*Nombre de modifications :* **{len(craft_diffs)} entrée**")
    lines.append("")
    lines.append("| FormID / Type | Texte Original (EN) | Avant (Balise illégale) | Après (Balise nettoyée) |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for c in craft_diffs:
        fid_str = format_fid(c['form_id'], c['type'])
        orig_str = clean_md(c['original'])
        avant_str = clean_md(c['avant'])
        apres_str = f"**{clean_md(c['apres'])}**"
        lines.append(f"| {fid_str} | {orig_str} | {avant_str} | {apres_str} |")
    lines.append("")
    lines.append("---")

    lines.append("")

out_file = Path("recap_modifications_phase1.md")
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Generated comprehensive {out_file} ({out_file.stat().st_size} bytes)")
