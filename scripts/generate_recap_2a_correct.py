import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Definitive dictionary of all actual changes in Sub-phase 2A with REAL "Avant" values
actual_changes_2a = [
    # 1. nolvus awakening clothes patch.esp.json
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0303C0F1|Dragonborn.esm',
        'type': 'ARMO FULL',
        'original': "Miraak's Mask",
        'before': "Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique.",
        'after': "Masque de Miraak",
        'nature': "Restauration du nom d'objet Masque de Miraak (écrasé par la description de l'enchantement)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0303C0F1|Dragonborn.esm',
        'type': 'ARMO DESC',
        'original': "Increases Magic Resistance by <10>%.  Gives access to Benthic Scream.",
        'before': "Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique.",
        'after': "Augmente la résistance à la magie de <10> %. Confère l'accès au Cri benthique.",
        'nature': "Conservation de la variable <10> conforme à l'original"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '000AE087|Skyrim.esm',
        'type': 'WEAP DESC',
        'original': "<5> points of extra damage to Nords.",
        'before': "5 points de dégâts supplémentaires aux Nordiques.",
        'after': "<5> points de dégâts supplémentaires aux Nordiques.",
        'nature': "Conservation de la variable <5> conforme à l'original"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0010EB65|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Shield of Solitude",
        'before': "Rondache de Solitude",
        'after': "Bouclier de Solitude",
        'nature': "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0010EB64|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Shield of Solitude",
        'before': "Rondache de Solitude",
        'after': "Bouclier de Solitude",
        'nature': "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0010EB63|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Shield of Solitude",
        'before': "Rondache de Solitude",
        'after': "Bouclier de Solitude",
        'nature': "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0009E023|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Shield of Solitude",
        'before': "Rondache de Solitude",
        'after': "Bouclier de Solitude",
        'nature': "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '00013989|Skyrim.esm',
        'type': 'WEAP FULL',
        'original': "Steel Sword",
        'before': "Épée en acier",
        'after': "Épée d'acier",
        'nature': "Canon Bethesda : Épée d'acier (au lieu de en acier)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '000139B1|Skyrim.esm',
        'type': 'WEAP FULL',
        'original': "Ebony Sword",
        'before': "Épée en ébonite",
        'after': "Épée d'ébonite",
        'nature': "Canon Bethesda : Épée d'ébonite (au lieu de en ébonite)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0007947A|Skyrim.esm',
        'type': 'CELL FULL',
        'original': "Jorrvaskr Living Quarters",
        'before': "Jorrvaskr - Logements",
        'after': "Logements de Jorrvaskr",
        'nature': "Canon Bethesda : Logements de Jorrvaskr"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '000457F7|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Dark Elf",
        'before': "Elfe noir",
        'after': "Elfe noire",
        'nature': "Accord de genre : PNJ féminin (Elfe noire)"
    },
    {
        'file': 'nolvus awakening clothes patch.esp.json',
        'form_id': '0201684C|Dawnguard.esm',
        'type': 'NPC_ FULL',
        'original': "Ferryman",
        'before': "Passeur",
        'after': "Capitaine",
        'nature': "Canon Bethesda : Capitaine (Passeur vers Volkihar)"
    },

    # 2. nolvus awakening clothes balance patch.esp.json
    {
        'file': 'nolvus awakening clothes balance patch.esp.json',
        'form_id': '0100A317|Apachii_DivineEleganceStore.esm',
        'type': 'ARMO FULL',
        'original': "DE Robin Wolf Leather Armor NPC",
        'before': "DE Robin Wolf Leather Armor NPC",
        'after': "Armure en cuir de loup de Robin (PNJ)",
        'nature': "Traduction française de l'anglais résiduel Apachii"
    },
    {
        'file': 'nolvus awakening clothes balance patch.esp.json',
        'form_id': '0100A315|Apachii_DivineEleganceStore.esm',
        'type': 'ARMO FULL',
        'original': "DE Robin Gloves NPC",
        'before': "DE Robin Gloves NPC",
        'after': "Gants de Robin (PNJ)",
        'nature': "Traduction française de l'anglais résiduel Apachii"
    },
    {
        'file': 'nolvus awakening clothes balance patch.esp.json',
        'form_id': '0100A311|Apachii_DivineEleganceStore.esm',
        'type': 'ARMO FULL',
        'original': "DE Freja Armor NPC",
        'before': "DE Freja Armor NPC",
        'after': "Armure de Freja (PNJ)",
        'nature': "Traduction française de l'anglais résiduel Apachii"
    },

    # 3. nolvus awakening gourmet integration.esp.json
    {
        'file': 'nolvus awakening gourmet integration.esp.json',
        'form_id': '000D882D|Skyrim.esm',
        'type': 'CONT FULL',
        'original': "Thieves Guild Fence Chest",
        'before': "Thieves Guild Fence Chest",
        'after': "Coffre de receleur de la Guilde des voleurs",
        'nature': "Canon Bethesda : Traduction de Thieves Guild Fence Chest"
    },
    {
        'file': 'nolvus awakening gourmet integration.esp.json',
        'form_id': '000D882E|Skyrim.esm',
        'type': 'CONT FULL',
        'original': "Thieves Guild Fence Chest",
        'before': "Thieves Guild Fence Chest",
        'after': "Coffre de receleur de la Guilde des voleurs",
        'nature': "Canon Bethesda : Traduction de Thieves Guild Fence Chest"
    },

    # 4. Nolvus Awakening Seasonal Plant Mashup.esp.json
    {
        'file': 'Nolvus Awakening Seasonal Plant Mashup.esp.json',
        'form_id': '000BB949|Skyrim.esm',
        'type': 'TREE FULL',
        'original': "Jazbay",
        'before': "Jazbay",
        'after': "Raisin jazbay",
        'nature': "Canon Bethesda : Traduction de Jazbay"
    },
    {
        'file': 'Nolvus Awakening Seasonal Plant Mashup.esp.json',
        'form_id': '03010466|HearthFires.esm',
        'type': 'TREE FULL',
        'original': "Jazbay",
        'before': "Jazbay",
        'after': "Raisin jazbay",
        'nature': "Canon Bethesda : Traduction de Jazbay"
    },
    {
        'file': 'Nolvus Awakening Seasonal Plant Mashup.esp.json',
        'form_id': '09000844|Nolvus Awakening Seasonal Plant Mashup.esp',
        'type': 'TREE FULL',
        'original': "Jazbay",
        'before': "Jazbay",
        'after': "Raisin jazbay",
        'nature': "Canon Bethesda : Traduction de Jazbay"
    },
    {
        'file': 'Nolvus Awakening Seasonal Plant Mashup.esp.json',
        'form_id': '030110C8|HearthFires.esm',
        'type': 'TREE FULL',
        'original': "Nirnroot",
        'before': "Nirnroot",
        'after': "Racine de Nirn",
        'nature': "Canon Bethesda : Traduction de Nirnroot"
    },
    {
        'file': 'Nolvus Awakening Seasonal Plant Mashup.esp.json',
        'form_id': '030110BE|HearthFires.esm',
        'type': 'TREE FULL',
        'original': "Mora Tapinella",
        'before': "Mora Tapinella",
        'after': "Mora tapinella",
        'nature': "Canon Bethesda : Traduction de Mora Tapinella"
    },

    # 5. Nolvus Awakening AI Patch.esp.json
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00013B76|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Leontius",
        'before': "Leontius",
        'after': "Léontius",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00013B76|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Leontius Salvius",
        'before': "Leontius Salvius",
        'after': "Léontius Salvius",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00065657|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Erik",
        'before': "Erik",
        'after': "Érik",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00013818|Skyrim.esm',
        'type': 'CELL FULL',
        'original': "Jarl's Longhouse",
        'before': "Longère du jarl de Fortdhiver",
        'after': "Forteresse Froidepierre",
        'nature': "Canon Bethesda : Forteresse Froidepierre (Jarl's Longhouse Winterhold)"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001365F|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Dravynea the Stoneweaver",
        'before': "Dravynéa la Tisseuse-de-Pierre",
        'after': "Dravynea la Tisseuse de pierre",
        'nature': "Canon Bethesda : Suppression tirets superflus"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001365F|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Dravynea",
        'before': "Dravynéa",
        'after': "Dravynea",
        'nature': "Canon Dunmer : Dravynea sans accent"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00013380|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Vekel the Man",
        'before': "Vekel l'Homme",
        'after': "Vekel l'homme",
        'nature': "Typographie française : Vekel l'homme"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Brelyna Maryon",
        'before': "Brélyna Maryon",
        'after': "Brelyna Maryon",
        'nature': "Canon Dunmer : Brelyna sans accent"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Brelyna",
        'before': "Brélyna",
        'after': "Brelyna",
        'nature': "Canon Dunmer : Brelyna sans accent"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001413D|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Ravam Verethi",
        'before': "Ravam Véréthi",
        'after': "Ravam Verethi",
        'nature': "Canon Dunmer : Ravam Verethi"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001366B|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Sondas Drenim",
        'before': "Sondas Drénim",
        'after': "Sondas Drenim",
        'nature': "Canon Dunmer : Sondas Drenim"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001413A|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Revyn Sadri",
        'before': "Révyn Sadri",
        'after': "Revyn Sadri",
        'nature': "Canon Dunmer : Revyn Sadri"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '0001413A|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Revyn",
        'before': "Révyn",
        'after': "Revyn",
        'nature': "Canon Dunmer : Revyn"
    },
    {
        'file': 'Nolvus Awakening AI Patch.esp.json',
        'form_id': '00014123|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Niranye",
        'before': "Niranyë",
        'after': "Niranye",
        'nature': "Canon Altmer : Niranye sans tréma"
    },

    # 6. nolvus awakening combat scaling overhaul - consistency patch.esp.json
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '000BFB55|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Keeper Carcette",
        'before': "Carcette la Gardienne",
        'after': "Gardienne Carcette",
        'nature': "Canon Bethesda : Gardienne Carcette (Keeper Carcette)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00023AB2|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Exmoor Pony",
        'before': "Cheval",
        'after': "Poney Exmoor",
        'nature': "Restauration race de monture : Poney Exmoor (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D5B|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Exmoor Pony",
        'before': "Cheval",
        'after': "Poney Exmoor",
        'nature': "Restauration race de monture : Poney Exmoor (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D07|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Black Fell Pony",
        'before': "Cheval",
        'after': "Poney fell noir",
        'nature': "Restauration race de monture : Poney fell noir (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068CFA|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Black Fell Pony",
        'before': "Cheval",
        'after': "Poney fell noir",
        'nature': "Restauration race de monture : Poney fell noir (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D6E|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Palomino Horse",
        'before': "Cheval",
        'after': "Cheval palomino",
        'nature': "Restauration race de monture : Cheval palomino (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D04|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Palomino Horse",
        'before': "Cheval",
        'after': "Cheval palomino",
        'nature': "Restauration race de monture : Cheval palomino (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D6B|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Gypsy Horse",
        'before': "Cheval",
        'after': "Cheval gitan",
        'nature': "Restauration race de monture : Cheval gitan (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D02|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Gypsy Horse",
        'before': "Cheval",
        'after': "Cheval gitan",
        'nature': "Restauration race de monture : Cheval gitan (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D6D|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Grey Fell Pony",
        'before': "Cheval",
        'after': "Poney fell gris",
        'nature': "Restauration race de monture : Poney fell gris (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '00068D03|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Grey Fell Pony",
        'before': "Cheval",
        'after': "Poney fell gris",
        'nature': "Restauration race de monture : Poney fell gris (auparavant uniformisé en Cheval)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Brelyna Maryon",
        'before': "Brélyna Maryon",
        'after': "Brelyna Maryon",
        'nature': "Canon Dunmer : Brelyna sans accent"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Brelyna",
        'before': "Brélyna",
        'after': "Brelyna",
        'nature': "Canon Dunmer : Brelyna sans accent"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - consistency patch.esp.json',
        'form_id': '040179C7|Dragonborn.esm',
        'type': 'NPC_ FULL',
        'original': "Ralis Sedarys",
        'before': "Ralis Sédarys",
        'after': "Ralis Sedarys",
        'nature': "Canon Dunmer : Ralis Sedarys sans accent"
    },

    # 7. nolvus awakening combat scaling overhaul - enemy level mult.esp.json
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '000BFB55|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Keeper Carcette",
        'before': "Carcette la Gardienne",
        'after': "Gardienne Carcette",
        'nature': "Canon Bethesda : Gardienne Carcette"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001365F|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Dravynea the Stoneweaver",
        'before': "Dravynéa la Tisseuse-de-Pierre",
        'after': "Dravynea la Tisseuse de pierre",
        'nature': "Canon Bethesda : Dravynea"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '00013B76|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Leontius Salvius",
        'before': "Leontius Salvius",
        'after': "Léontius Salvius",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '00013B76|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Leontius",
        'before': "Leontius",
        'after': "Léontius",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0002C925|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Severio Pelagia",
        'before': "Severio Pelagia",
        'after': "Sévério Pélagia",
        'nature': "Accentuation officielle Skyrim"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '00016FF8|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Dremora Valkynaz",
        'before': "Drémora Valkynaz",
        'after': "Valkynaz drémora",
        'nature': "Canon Bethesda : Valkynaz drémora"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0007E87D|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Flame Thrall",
        'before': "Golem de feu",
        'after': "Monarque de feu",
        'nature': "Canon Bethesda : Monarque de feu (Flame Thrall)"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Brelyna Maryon",
        'before': "Brélyna Maryon",
        'after': "Brelyna Maryon",
        'nature': "Canon Dunmer : Brelyna Maryon"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Brelyna",
        'before': "Brélyna",
        'after': "Brelyna",
        'nature': "Canon Dunmer : Brelyna"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '040179C7|Dragonborn.esm',
        'type': 'NPC_ FULL',
        'original': "Ralis Sedarys",
        'before': "Ralis Sédarys",
        'after': "Ralis Sedarys",
        'nature': "Canon Dunmer : Ralis Sedarys"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0401777C|Dragonborn.esm',
        'type': 'NPC_ FULL',
        'original': "Varona Nelas",
        'before': "Varona Nélas",
        'after': "Varona Nelas",
        'nature': "Canon Dunmer : Varona Nelas"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '00014123|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Niranye",
        'before': "Niranyë",
        'after': "Niranye",
        'nature': "Canon Altmer : Niranye"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001413D|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Ravam Verethi",
        'before': "Ravam Véréthi",
        'after': "Ravam Verethi",
        'nature': "Canon Dunmer : Ravam Verethi"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001413A|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Revyn Sadri",
        'before': "Révyn Sadri",
        'after': "Revyn Sadri",
        'nature': "Canon Dunmer : Revyn Sadri"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
        'form_id': '0001413A|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Revyn",
        'before': "Révyn",
        'after': "Revyn",
        'nature': "Canon Dunmer : Revyn"
    },

    # 8. nolvus awakening combat scaling overhaul - enemy level.esp.json
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '000BFB55|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Keeper Carcette",
        'before': "Carcette la Gardienne",
        'after': "Gardienne Carcette",
        'nature': "Canon Bethesda : Gardienne Carcette"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '00016FF8|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Dremora Valkynaz",
        'before': "Drémora Valkynaz",
        'after': "Valkynaz drémora",
        'nature': "Canon Bethesda : Valkynaz drémora"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '0402C406|Dragonborn.esm',
        'type': 'NPC_ FULL',
        'original': "Redoran Guard",
        'before': "Garde des Rédorans",
        'after': "Garde Rédoran",
        'nature': "Canon Bethesda : Garde Rédoran"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '0003BCC7|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Stormcloak Courier",
        'before': "Messager des Sombrages",
        'after': "Messager sombrage",
        'nature': "Canon Bethesda : Messager sombrage"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Brelyna Maryon",
        'before': "Brélyna Maryon",
        'after': "Brelyna Maryon",
        'nature': "Canon Dunmer : Brelyna Maryon"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '0001C196|Skyrim.esm',
        'type': 'NPC_ SHRT',
        'original': "Brelyna",
        'before': "Brélyna",
        'after': "Brelyna",
        'nature': "Canon Dunmer : Brelyna"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '040179C7|Dragonborn.esm',
        'type': 'NPC_ FULL',
        'original': "Ralis Sedarys",
        'before': "Ralis Sédarys",
        'after': "Ralis Sedarys",
        'nature': "Canon Dunmer : Ralis Sedarys"
    },
    {
        'file': 'nolvus awakening combat scaling overhaul - enemy level.esp.json',
        'form_id': '00014123|Skyrim.esm',
        'type': 'NPC_ FULL',
        'original': "Niranye",
        'before': "Niranyë",
        'after': "Niranye",
        'nature': "Canon Altmer : Niranye"
    }
]

# Write accurate recap markdown file
md_lines = [
    "# Récapitulatif des Modifications — Phase 2A : Patchs Systémiques Nolvus Awakening",
    "",
    "> **Périmètre :** Sous-phase 2A de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).",
    "> **Mods audités :** 11 mods d'intégration et patchs Nolvus Awakening (`Combat Scaling Overhaul`, `AI Patch`, `Clothes Patch`, `Clothes Balance Patch`, `Gourmet Integration`, `Stances Perk System`, `Ashes of War`, `Seasonal Plant Mashup`, `Custom Outfits`, `Lighting Patch`, `Northern Roads Grass Patches`).",
    "> **Volume de vérification :** Plus de 18 000 enregistrements contrôlés, intégrité technique et lore officiel Bethesda.",
    "",
    "---",
    ""
]

def clean_cell(val):
    if val is None:
        return ""
    val_str = str(val).replace('\r', ' ').replace('\n', '<br>')
    return val_str.replace('|', '\\|')

by_file = {}
for entry in actual_changes_2a:
    by_file.setdefault(entry['file'], []).append(entry)

for fn, entries in by_file.items():
    md_lines.append(f"## 📁 {fn}")
    md_lines.append(f"*Nombre d'ajustements majeurs :* **{len(entries)}**\n")
    md_lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for e in entries:
        fid_formatted = e['form_id'].replace('|', ' (') + ')'
        orig = clean_cell(e['original'])
        before = clean_cell(e['before'])
        after = f"**{clean_cell(e['after'])}**"
        nat = clean_cell(e['nature'])
        md_lines.append(f"| `{fid_formatted}`<br>*{clean_cell(e['type'])}* | {orig} | {before} | {after} | {nat} |")
    md_lines.append("\n---\n")

with open('recap_modifications_phase2a.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"Generated recap_modifications_phase2a.md with {len(actual_changes_2a)} accurate Avant/Apres entries.")
