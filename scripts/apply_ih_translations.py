# -*- coding: utf-8 -*-
"""
Script d'audit, révision et traduction complète pour Immersive Hunting Animations :
1. ImmersiveHunting_french.txt.json (72 entrées MCM & Interface)
2. immersivehunting.esp.json (53 entrées Plugin)
"""

import json

ESP_PATH = r"data/user/database/french/Immersive Hunting Animations/immersivehunting.esp.json"
TXT_PATH = r"data/user/database/french/ImmersiveHunting_french.txt - French/interface/translations/ImmersiveHunting_french.txt.json"

# --- 1. INTERFACE TXT / MCM (72 entrées) ---
TXT_TRANSLATIONS = {
    ("$_ih_Title", "Immersive Hunting"): "Chasse immersive",
    ("$_ih_PageConfig", "Settings"): "Paramètres",
    ("$_ih_Animation", "Animations"): "Animations",
    ("$_ih_Support", "Support"): "Compatibilités",
    ("$_ih_Features", "Extras"): "Options supplémentaires",
    ("$_ih_Started", "STATUS: STARTED"): "ÉTAT : ACTIVÉ",
    ("$_ih_Stopped", "STATUS: STOPPED"): "ÉTAT : DÉSACTIVÉ",
    ("$_ih_Status", "START/STOP:"): "DÉMARRER / ARRÊTER :",
    ("$_ih_LootMode", "Loot Mode"): "Mode de fouille",
    ("$_ih_StartMod", "START MOD"): "Démarrer le mod",
    ("$_ih_StopMod", "STOP MOD"): "Arrêter le mod",
    ("$_ih_Process", "Process"): "Traitement automatique",
    ("$_ih_RemoveArrow", "Retrieve arrows"): "Récupérer les flèches",
    ("$_ih_Skin", "Skin"): "Dépecer",
    ("$_ih_Harvest", "Harvest"): "Prélever",
    ("$_ih_Butcher", "Butcher"): "Découper la viande",
    ("$_ih_Extract", "Extract"): "Extraire le venin",
    ("$_ih_PossibleAnimations", "Possible animations to play"): "Animations successives à jouer",
    ("$_ih_SheatheWeapons", "Sheathe weapons"): "Rengaîner les armes",
    ("$_ih_ForceThirdPerson", "Force third person"): "Forcer la vue à la 3e personne",
    ("$_ih_ForceThirdPersonOff", "Disabled"): "Désactivé",
    ("$_ih_ForceThirdPersonOn", "Just force"): "Vue 3e personne uniquement",
    ("$_ih_ForceThirdPersonOnAndReturn", "Force and return"): "Vue 3e personne avec retour",
    ("$_ih_RequireDagger", "Require dagger"): "Exiger une dague",
    ("$_ih_DaggerPosition", "Dagger position"): "Position de la dague",
    ("$_ih_DaggerAnkle", "Ankle"): "Cheville",
    ("$_ih_DaggerBackHip", "Back hip"): "Hanche arrière",
    ("$_ih_UpdateDagger", "Use last equipped dagger"): "Utiliser la dernière dague équipée",
    ("$_ih_EnablePickup", "Enable pick up"): "Autoriser le transport de carcasse",
    ("$_ih_EnablePickupAnim", "Enable pick up animations"): "Animations de ramassage",
    ("$_ih_EnablePlaceTorch", "Place torch on ground"): "Poser la torche au sol",
    ("$_ih_EnableCampfire", "Cooking animation for Campfire"): "Animation de cuisine pour Campfire",
    ("$_ih_EnableDispose", "Can dispose carcass"): "Possibilité d'éliminer la carcasse",
    ("$_ih_EnableShovelBury", "Shovel Bury Bodies"): "Enterrer avec une pelle",
    ("$_ih_EnableRealisticSkin", "Realistic skinning"): "Dépeçage réaliste",
    ("$_ih_EnableDisplay", "Displays"): "Affichages d'équipement (IED)",
    ("$_ih_IEDNotInstalled", "Immersive Equipment Displays is not installed"): "Immersive Equipment Displays n'est pas installé",
    ("$_ih_EnableSoulsSupport", "Skyrim Souls support"): "Prise en charge de Skyrim Souls",
    ("$_ih_EnableQuickLootSupport", "QuickLoot support"): "Prise en charge de QuickLoot",
    ("$_ih_EnableRequireBottle", "Requires bottle"): "Fiole requise",
    ("$_ih_EnableBowAnim", "Animations with bow"): "Animations avec un arc équipé",
    ("$_ih_Search", "Search"): "Fouiller",
    ("$_ih_Dispose", "Dispose"): "Éliminer la carcasse",
    ("$_ih_Vanilla", "Vanilla"): "Jeu de base (Vanilla)",
    ("$_ih_Prompt", "Prompt"): "Menu interactif",
    ("$_ih_StartModDesc", "Start or stop Immersive Hunting Animations."): 
        "Active ou désactive les animations de Chasse immersive.",
    ("$_ih_LootModeDesc", "Select the loot mode when interacting with carcasses.\\nVanilla: The inventory menu is opened; after removing an item, the corresponding animation will play.\\nPrompt: A prompt with options to choose from based on the items present in the carcass; after choosing an option, the corresponding animation will play.\\nProcess: All items will be looted from the carcass and an unique animation will play, if applicable."):
        "Sélectionnez le mode de fouille lors de l'interaction avec une carcasse.\\nJeu de base : le menu d'inventaire classique s'ouvre ; après avoir pris un objet, l'animation correspondante se déclenche.\\nMenu interactif : un menu propose différentes actions selon les éléments présents sur la carcasse ; l'animation correspondante se déclenche après votre choix.\\nTraitement automatique : tous les objets de la carcasse sont récupérés et une animation unique est jouée.",
    ("$_ih_ProcessDesc", "Toggle to enable animations when processing/removing all items from carcasses."):
        "Active les animations lors du traitement complet et de la récupération de tous les objets d'une carcasse.",
    ("$_ih_EnableRemoveArrowDesc", "Toggle to enable animations when removing arrows from carcasses."):
        "Active les animations pour retirer les flèches fichées dans la carcasse.",
    ("$_ih_EnableSkinDesc", "Toggle to enable animations when removing pelts from carcasses."):
        "Active les animations de dépeçage pour prélever les peaux et fourrures.",
    ("$_ih_EnableHarvestDesc", "Toggle to enable animations when removing materials from carcasses."):
        "Active les animations de prélèvement pour les ingrédients et matériaux.",
    ("$_ih_EnableButcherDesc", "Toggle to enable animations when removing food items from carcasses."):
        "Active les animations de découpe de la viande et des vivres.",
    ("$_ih_EnableExtractDesc", "Toggle to enable animations when removing potion/poison items from carcasses."):
        "Active les animations d'extraction pour les venins et poisons.",
    ("$_ih_PossibleAnimationsDesc", "Select the number of possible animations to play from a single carcass. Used only in Loot mode: Vanilla."):
        "Détermine le nombre maximal d'animations pouvant être jouées successivement sur une même carcasse. Utilisé uniquement en mode Jeu de base.",
    ("$_ih_ForceThirdPersonDesc", "Select the options to force(or not) third person camera when performing one of the animated actions in first person."):
        "Définit le basculement de la caméra à la 3e personne lors du déclenchement d'une animation en vue à la 1re personne.",
    ("$_ih_SheatheWeaponsDesc", "Toggle to sheathe weapons when interacting with carcasses."):
        "Rengaîne automatiquement vos armes lors de l'interaction avec une carcasse.",
    ("$_ih_EnableDisplayDesc", "Toggle to enable displays for daggers and hunting materials."):
        "Active l'affichage visuel des dagues et accessoires de chasse sur votre personnage (via IED).",
    ("$_ih_RequireDaggerDesc", "Toggle to require the use of a dagger (your last equipped one) when performing any of the actions that use it. If no dagger is present, then your character will use a rock (found on the ground) or their claws, if a Khajiit or Argonian."):
        "Exige la possession d'une dague (votre dernière dague équipée) pour accomplir les actions de chasse. Si vous ne possédez aucune dague, votre personnage utilisera une pierre trouvée au sol, ou ses griffes s'il s'agit d'un Khajiit ou d'un Argonien.",
    ("$_ih_DaggerPositionDesc", "Select the dagger position to be used during the animations (and IED displays)."):
        "Choisit l'emplacement de la dague durant les animations et son affichage d'équipement (IED).",
    ("$_ih_UpdateDaggerDesc", "Toggle to use last equipped dagger when interacting with carcasses."):
        "Met à jour la dague utilisée selon la dernière dague que vous avez équipée.",
    ("$_ih_EnablePickupDesc", "Toggle to enable carcass pick up. When this is enabled, you will be able to carry some carcasses while using the grab function (holding Activate)."):
        "Permet de transporter certaines carcasses d'animaux en maintenant la touche d'activation enfoncée (saisie physique de corps).",
    ("$_ih_EnablePlaceTorchDesc", "Toggle to place the current carried torch on the ground next to the player when performing one of the animated actions."):
        "Pose automatiquement la torche équipée au sol à côté de vous lors d'une action animée de chasse.",
    ("$_ih_EnableCampfireDesc", "Toggle to enable the cooking animation for \"Campfire - Complete Camping System\"."):
        "Active l'animation de cuisine immersive pour le mod « Campfire ».",
    ("$_ih_EnableDisposeDesc", "Toggle to enable the disposing of carcasses when interacting in Loot mode: Prompt or Loot mode: Process."):
        "Permet de faire disparaître ou d'évacuer la carcasse en mode Menu interactif ou Traitement automatique.",
    ("$_ih_EnableShovelBuryDesc", "Toggle to use the functionality from \"Shovels Bury Bodies\" when disposing a carcass."):
        "Utilise les fonctionnalités du mod « Shovels Bury Bodies » pour enterrer la carcasse avec une pelle.",
    ("$_ih_EnableRealisticSkinDesc", "Toggle to enable the realistic skinning system. After skinning certain carcasses, their models will be update (skin removed). If Hunting in Skyrim is installed, your character gains XP and skinning stats."):
        "Active le dépeçage réaliste : après avoir dépecé un animal, son modèle 3D est remplacé par une carcasse écorchée. Si « Hunting in Skyrim » est installé, vous gagnez de l'expérience et des statistiques de chasse.",
    ("$_ih_IEDNotInstalledDesc", "Immersive Equipment Displays is not installed. Displays option is unavailable."):
        "Immersive Equipment Displays n'est pas installé. Les options d'affichage sont indisponibles.",
    ("$_ih_EnableSoulsSupportDesc", "Toggle to enable Skyrim Souls unpaused menus support."):
        "Active la compatibilité avec Skyrim Souls (menus sans pause).",
    ("$_ih_EnableQuickLootSupportDesc", "Toggle to enable QuickLoot support."):
        "Active la compatibilité avec QuickLoot.",
    ("$_ih_EnableRequireBottleDesc", "Toggle to require bottles when extracting poisons, for Alchemy Requires Bottles."):
        "Exige d'avoir une fiole vide pour extraire les poisons (compatible avec Alchemy Requires Bottles).",
    ("$_ih_EnableBowAnimDesc", "Toggle to play animations when your character has a bow equipped."):
        "Joue les animations même lorsque votre personnage a un arc équipé en main.",
    ("$_ih_RequiresBottle", "You need an empty bottle to store the venom!"):
        "Vous avez besoin d'une fiole vide pour recueillir le venin !",
}

# --- 2. PLUGIN ESP (53 entrées exactes) ---
ESP_TRANSLATIONS = {
    # Quêtes et Atouts
    ('ImmersiveHuntingQuest', 'QUST FULL', 'Immersive Hunting Animations'):
        "Chasse immersive - Animations",
    ('ImmersiveHuntingSkinningQuest', 'QUST FULL', 'Immersive Hunting Skinning'):
        "Chasse immersive - Dépeçage",
    ('IH_PK_ImmersiveHunting', 'PERK FULL', 'ImmersiveHunting Perk'):
        "Chasse immersive",

    # Fourrures d'exposition (IED)
    ('IH_BrownFurDisplay', 'MISC FULL', 'Brown Fur Display'):
        "Fourrure brune",
    ('IH_SnowFurDisplay', 'MISC FULL', 'White Fur Display'):
        "Fourrure des neiges",
    ('IH_WhiteFurDisplay', 'MISC FULL', 'Snow Fur Display'):
        "Fourrure blanche",
    ('IH_ValeFurDisplay', 'MISC FULL', 'Vale Fur Display'):
        "Fourrure des vallées",
    ('IH_BlackFurDisplay', 'MISC FULL', 'Black Fur Display'):
        "Fourrure noire",

    # Jetons techniques (Tokens)
    ('IH_SkinnedToken', 'MISC FULL', 'Skinned Token'):
        "Jeton de dépeçage",
    ('IH_ProcessedToken', 'MISC FULL', 'Skinned Token'):
        "Jeton de traitement",
    ('IH_HarvestedToken', 'MISC FULL', 'Harvested Token'):
        "Jeton de prélèvement",
    ('IH_ButcheredToken', 'MISC FULL', 'Butchered Token'):
        "Jeton de découpe",
    ('IH_ExtractedToken', 'MISC FULL', 'Extracted Token'):
        "Jeton d'extraction",

    # Menu interactif Prompt (MESG)
    ('IH_MSG_LootPrompt', 'MESG FULL', 'IH_MSG_LootPrompt'):
        "Chasse immersive - Actions",
    ('IH_MSG_LootPrompt', 'MESG DESC', 'Choose an action:'):
        "Choisissez une action :",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$Cancel'):
        "Annuler",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_RemoveArrow'):
        "Récupérer les flèches",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Skin'):
        "Dépecer",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Harvest'):
        "Prélever",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Butcher'):
        "Découper la viande",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Extract'):
        "Extraire le venin",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Search'):
        "Fouiller",
    ('IH_MSG_LootPrompt', 'MESG ITXT', '$_ih_Dispose'):
        "Éliminer la carcasse",

    # Carcasses d'animaux (MISC FULL)
    ('IH_HareCarcassModel', 'MISC FULL', 'Hare Carcass'):
        "Carcasse de lapin",
    ('IH_DeerCarcassModel', 'MISC FULL', 'Deer Carcass'):
        "Carcasse de chevreuil",
    ('IH_GoatCarcassModel', 'MISC FULL', 'Goat Carcass'):
        "Carcasse de chèvre",
    ('IH_SkeeverCarcassModel', 'MISC FULL', 'Skeever Carcass'):
        "Carcasse de ragnard",
    ('IH_FishCarcassModel', 'MISC FULL', 'Slaughterfish Carcass'):
        "Carcasse de poisson-carnassier",
    ('IH_FoxSnowCarcassModel', 'MISC FULL', 'Fox Snow Carcass'):
        "Carcasse de renard des neiges",
    ('IH_DogCarcassModel', 'MISC FULL', 'Dog Carcass'):
        "Carcasse de chien",
    ('IH_WolfIceCarcassModel', 'MISC FULL', 'Wolf Ice Carcass'):
        "Carcasse de loup des glaces",
    ('IH_FoxCarcassModel', 'MISC FULL', 'Fox Carcass'):
        "Carcasse de renard",
    ('IH_ChickenCarcassModel', 'MISC FULL', 'Chicken Carcass'):
        "Carcasse de poulet",
    ('IH_ElkFemaleCarcassModel', 'MISC FULL', 'Elk Female Carcass'):
        "Carcasse d'élan femelle",
    ('IH_WolfCarcassModel', 'MISC FULL', 'Wolf Carcass'):
        "Carcasse de loup",
    ('IH_MudcrabCarcassModel', 'MISC FULL', 'Mudcrab Carcass'):
        "Carcasse de vasard",
    ('IH_ElkCarcassModel', 'MISC FULL', 'Elk Carcass'):
        "Carcasse d'élan",
    ('IH_ValeDeerCarcassModel', 'MISC FULL', 'Vale Deer Carcass'):
        "Carcasse de chevreuil des vallées",

    # Animaux écorchés (ARMO FULL - dépeçage réaliste)
    ('SHOSkinnedSkeeverSkinAll', 'ARMO FULL', 'Skinned Skeever'):
        "Ragnard écorché",
    ('SHOSkinnedWereWolfSkinAll', 'ARMO FULL', 'Skinned Werewolf'):
        "Loup-garou écorché",
    ('HISSkinnedWolfSkinAll', 'ARMO FULL', 'Skinned Wolf'):
        "Loup écorché",
    ('HISSkinnedDeerSkinAll', 'ARMO FULL', 'Skinned Deer'):
        "Chevreuil écorché",
    ('HISSkinnedHorseSkinAll', 'ARMO FULL', 'Skinned Horse'):
        "Cheval écorché",
    ('HISSkinnedSabreSkinAll', 'ARMO FULL', 'Skinned Sabre Cat'):
        "Smilodon écorché",
    ('HISSkinnedHorkerSkinAll', 'ARMO FULL', 'Skinned Horker'):
        "Horqueur écorché",
    ('HISSkinnedBearSkinAll', 'ARMO FULL', 'Skinned Bear'):
        "Ours écorché",
    ('HISSkinnedFoxSkinAll', 'ARMO FULL', 'Skinned Fox'):
        "Renard écorché",
    ('HISSkinnedGoatSkinAll', 'ARMO FULL', 'Skinned Goat'):
        "Chèvre écorchée",
    ('HISSkinnedMammothSkinAll', 'ARMO FULL', 'Skinned Mammoth'):
        "Mammouth écorché",
    ('HISSkinnedTrollSkinAll', 'ARMO FULL', 'Skinned Troll'):
        "Troll écorché",
    ('HISSkinnedRabbitSkinAll', 'ARMO FULL', 'Skinned Rabbit'):
        "Lapin écorché",
    ('HISSkinnedCowSkinAll', 'ARMO FULL', 'Skinned Cow'):
        "Vache écorchée",
    ('HISSkinnedElkSkinAll', 'ARMO FULL', 'Skinned Elk'):
        "Élan écorché",
}

def update_txt():
    print(f"Loading {TXT_PATH}...")
    with open(TXT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for entry in data:
        key = (entry.get("mcm_id"), entry.get("original"))
        if key in TXT_TRANSLATIONS:
            entry["string"] = TXT_TRANSLATIONS[key]
            entry["status"] = "TranslationComplete"
            updated += 1
        else:
            print("Unmapped in TXT:", key)

    print(f"TXT: updated {updated}/{len(data)} entries.")
    if updated != len(data):
        raise ValueError(f"Expected {len(data)} updates in TXT, got {updated}")

    with open(TXT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("TXT JSON saved successfully.\n")

def update_esp():
    print(f"Loading {ESP_PATH}...")
    with open(ESP_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for entry in data:
        key = (entry.get("editor_id"), entry.get("type"), entry.get("original"))
        if key in ESP_TRANSLATIONS:
            entry["string"] = ESP_TRANSLATIONS[key]
            entry["status"] = "TranslationComplete"
            updated += 1
        else:
            print("Unmapped in ESP:", key)

    print(f"ESP: updated {updated}/{len(data)} entries.")
    if updated != len(data):
        raise ValueError(f"Expected {len(data)} updates in ESP, got {updated}")

    with open(ESP_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    print("ESP JSON saved successfully.\n")

if __name__ == "__main__":
    update_txt()
    update_esp()
