import json
from pathlib import Path

db_dir = Path('data/user/database/french')

# 1. Player facing fixes dictionary: (original) -> french translation
player_facing_fixes = {
    # Erik the Slayer
    "Erik the Slayer": "Erik le Massacreur",
    "Visit your spouse's house": "Rendre visite à votre conjoint(e)",
    
    # Petites annonces (Notice Board / Missives quests)
    "Recover From a Hideout": "Récupération dans un repaire",
    "Retrieve From a Ruin": "Récupération dans une ruine",
    "Retrieve From the Wilderness": "Récupération dans la nature",
    
    # Nolvus NPCs
    "Romanov the Gatekeeper": "Romanov le Gardien de la porte",
    "Romanov the Wolf Queen": "Romanov la Reine-Louve",
    
    # Trade and Barter rebalance
    "Prices are 10% better in cities where you are Thane.": "Les prix sont plus avantageux de 10 % dans les villes où vous êtes thane.",
    
    # Archerie locational damage rebalance
    "Attack damage -25% for 10 seconds.": "Dégâts d'attaque -25 % pendant 10 secondes.",
    
    # Adamant perks updated in newer versions
    "75% chance to resist stagger while under the effect of a flesh or a shield spell.": "75 % de chances de résister à la déstabilisation sous l'effet d'un sort d'armure ou de bouclier.",
    "Bows deal guaranteed critical damage to enemies at full Health.": "Les arcs infligent obligatoirement un coup critique aux ennemis ayant toute leur santé.",
    "You gather two extra ingredients from plants.": "Vous récoltez deux ingrédients supplémentaires sur les plantes.",
    "You receive a 25% bonus to armor rating when wearing three pieces of heavy armor.": "Vous recevez un bonus d'armure de 25 % lorsque vous portez trois pièces d'armure lourde.",
    "Bashing causes enemies to take 25% more damage for 10 seconds.": "Les frappes font subir aux ennemis 25 % de dégâts supplémentaires pendant 10 secondes.",
    "You have a 25% chance to absorb the Magicka from incoming spells while under the effects of an armor spell.": "Vous avez 25 % de chances d'absorber la magie des sorts adverses sous l'effet d'un sort d'armure.",
    "Dual casting a Destruction spell costs 25% less Magicka.": "Les doubles lancers de sorts de destruction coûtent 25 % de magie en moins.",
    
    # Vokrii rebalances
    "One-handed weapons do 60% more damage, and one-handed critical strikes deal 4 times critical damage.": "Les armes à une main infligent 60 % de dégâts en plus, et les coups critiques à une main infligent 4 fois les dégâts critiques.",
    "Power attacks with a mace interrupt spellcasting, inflicting a critical strike for 3 times critical damage and silencing the target for 5 seconds.": "Les attaques puissantes à la masse interrompent les sorts, infligeant un coup critique à 3 fois les dégâts critiques et rendant la cible muette pendant 5 secondes.",
    "Power attacks with a greatsword execute targets below 30% Health, inflicting a critical strike for 10 times critical damage and knocking the target down.": "Les attaques puissantes à l'espadon exécutent les cibles sous 30 % de santé, infligeant un coup critique à 10 fois les dégâts critiques et renversant la cible."
}

updated_files = 0
updated_strings = 0

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        file_modified = False
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            
            if orig in player_facing_fixes:
                new_val = player_facing_fixes[orig]
                if trans != new_val:
                    if 'string' in s:
                        s['string'] = new_val
                    if 'translation' in s:
                        s['translation'] = new_val
                    s['status'] = 'TranslationComplete'
                    file_modified = True
                    updated_strings += 1
                    
        if file_modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated_files += 1
            print(f"Updated {p.name}")
    except Exception as e:
        pass

print(f"Finished! Updated {updated_strings} strings across {updated_files} files.")
