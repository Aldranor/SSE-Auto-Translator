# -*- coding: utf-8 -*-
"""
Script de mise à jour et validation de la traduction pour :
- Racial Skin Variance - SPID.esp.json
- Racial Skin Variance - SPID_french.txt.json
"""

import json
import os

ESP_JSON_PATH = r"data/user/database/french/Racial Skin Variance - SPID/Racial Skin Variance - SPID.esp.json"
TXT_JSON_PATH = r"data/user/database/french/Racial Skin Variance - SPID_french.txt - French/interface/translations/Racial Skin Variance - SPID_french.txt.json"

# Harmonisation ciblée pour l'ESP
ESP_UPDATES = {
    # Harmonisation bouton continuer à l'infinitif ("Oui, continuer." au lieu de l'impératif isolé "Oui, continuez.")
    ("0400085E|Racial Skin Variance - SPID.esp", "MESG ITXT", 0, "Yes, continue."): "Oui, continuer.",
}

# Traductions MCM complètes et vérifiées
MCM_TRANSLATIONS = {
    ("$Player_Options_Page", "Player Options"): "Options du joueur",
    ("$Controls_Page", "Controls & Debug"): "Commandes & Débogage",
    ("$Mod_Info_Page", "Mod Information"): "Informations",
    ("$Player_Mode_Header", "Player Skin"): "Peau du joueur",
    ("$Player_Age_Header", "Player Age"): "Âge du joueur",
    ("$Player_Teeth_Mode_Header", "Player Teeth"): "Dents du joueur",
    ("$Player_Controls_Header", "Player Controls"): "Commandes du joueur",
    ("$Debug_Header", "Debug"): "Débogage",
    ("$Info", "Information"): "Informations",
    ("$Mod_Info_Header", "Mod Information"): "Informations sur le mod",
    ("$Credits_Header", "Credits"): "Crédits",
    ("$Mod_Not_Ready_Title", "Mod Not Ready"): "Mod non prêt",
    ("$Player_Mode_Menu", "Skin Mode"): "Mode de peau",
    ("$Free_Skin_Menu", "Free Skin"): "Peau libre",
    ("$Player_Age_Menu", "Age"): "Âge",
    ("$Teeth_Mode_Menu", "Teeth Mode"): "Mode des dents",
    ("$Teeth_Type_Menu", "Teeth Type"): "Type de dents",
    ("$Please_Complete_Character_Creation", "Please, complete character creation"): "Veuillez terminer la création du personnage",
    ("$Get_Into_The_World", "and get into the World."): "et entrer dans le monde du jeu.",
    ("$MCM_Will_Be_Available_After", "MCM will be available after."): "Le MCM sera disponible ensuite.",
    ("$Manual_Start_Button", "Start RSV Manually"): "Initialiser RSV manuellement",
    ("$Manual_Start_Button_Info", 'Click to manually start RSV initialization. You can use this if you are stuck on the "Mod Not Ready" screen despite being in-game, or if you want to start the mod earlier. This bypasses the character creation check.'): 
        'Cliquez pour lancer manuellement l\'initialisation de RSV. À utiliser si vous êtes bloqué sur l\'écran « Mod non prêt » alors que vous êtes déjà en jeu, ou si vous souhaitez activer le mod plus tôt. Cela contourne la vérification de fin de création de personnage.',
    ("$Manual_Start_Header", "-- Or Start Manually --"): "-- Ou initialiser manuellement --",
    ("$Player_Reapply_KeyMap", "Reapply All Textures"): "Réappliquer toutes les textures",
    ("$Player_Skin_KeyMap", "Reapply Skin Textures"): "Réappliquer les textures de peau",
    ("$Player_Teeth_KeyMap", "Reapply Teeth Textures"): "Réappliquer les textures de dents",
    ("$Player_Schlong_KeyMap", "Reapply Schlong Textures"): "Réappliquer les textures SoS/TNG",
    ("$Notification_Switch", "Notifications"): "Notifications",
    ("$Debug_Mode_Switch", "Debug Mode"): "Mode débogage",
    ("$Force_Enable_Player_Options_Switch", "Forced Player Options"): "Forcer les options du joueur",
    ("$Racemenu_Slider_Reapply_Switch", "RaceMenu Slider Reapply"): "Réapplication curseur RaceMenu",
    ("$Uninstall_Button", "Uninstall RSV"): "Désinstaller RSV",
    ("$Player_Mode_Info", "It selects the Skin Player Mode. (This affects the way that the skin tetures for the player are applied)."): 
        "Sélectionne le mode de peau du joueur. (Détermine la façon dont les textures de peau sont appliquées au joueur).",
    ("$Player_Free_Skin_Info", "It selects the type of skin that the player will use when Free Mode is selected."): 
        "Sélectionne le type de peau appliqué au joueur lorsque le mode Libre est actif.",
    ("$Player_Age_Info", "It selects the skin for the face of the player between Default, Young or Old. (Only selectable for RSV and RSV Fantasy modes)."): 
        "Sélectionne la texture du visage du joueur parmi Par défaut, Jeune ou Âgé. (Disponible uniquement pour les modes RSV et RSV Fantaisie).",
    ("$Teeth_Mode_Info", "It selects the Teeth Player Mode. (This affects the way that the teeth textures for the player are applied)."): 
        "Sélectionne le mode de dents du joueur. (Détermine la façon dont les textures de dents sont appliquées au joueur).",
    ("$Teeth_Type_Info", "It selects the teeth textures when Free Teeth Mode is selected."): 
        "Sélectionne les textures de dents lorsque le mode Dents libres est actif.",
    ("$Player_Reapply_KeyMap_Info", "It reapplies ALL textures for the player according to current MCM selections."): 
        "Réapplique TOUTES les textures au joueur selon la configuration actuelle du MCM.",
    ("$Player_Skin_KeyMap_Info", "It reapplies ONLY the skin textures for the player according to current MCM selections."): 
        "Réapplique UNIQUEMENT les textures de peau au joueur selon la configuration actuelle du MCM.",
    ("$Player_Teeth_KeyMap_Info", "It reapplies ONLY the teeth textures for the player according to current MCM selections."): 
        "Réapplique UNIQUEMENT les textures de dents au joueur selon la configuration actuelle du MCM.",
    ("$Player_Schlong_KeyMap_Info", "It reapplies ONLY the schlong textures for the player according to current MCM selections."): 
        "Réapplique UNIQUEMENT les textures SoS/TNG au joueur selon la configuration actuelle du MCM.",
    ("$Info_Player_Skin_Mode_0", "The player skin is not modified by RSV. Choose this option if you don't want RSV to affect the player skin. This is the only possible option if you use a custom race for the player."): 
        "La peau du joueur n'est pas modifiée par RSV. Choisissez cette option si vous ne voulez pas que RSV affecte la peau de votre personnage. C'est l'unique option possible si vous jouez une race personnalisée.",
    ("$Info_Player_Skin_Mode_1", "The muscularity of the player changes depending on weight. It only affects normal map textures. It doesn't use racial variations of skin."): 
        "La musculature du joueur s'adapte en fonction de son poids. Affecte uniquement les textures de relief (normal maps), sans appliquer de variations raciales de peau.",
    ("$Info_Player_Skin_Mode_2", "The skin changes depending on the player race. Each vanilla race gets its own set of textures for the skin."): 
        "La peau change selon la race du joueur. Chaque race du jeu de base bénéficie de son propre ensemble de textures de peau.",
    ("$Info_Player_Skin_Mode_3", "The skin changes depending on the player race. Each vanila race gets its own set of textures for the skin. Dunmer, Altmer, Bosmer and Orsimer use fantasy skin."): 
        "La peau change selon la race du joueur. Chaque race du jeu de base bénéficie de son propre ensemble de textures. Les Elfes noirs, Hauts-Elfes, Elfes des bois et Orques utilisent des peaux fantaisies.",
    ("$Info_Player_Skin_Mode_4", "The skin selection is free. You can select any skin for the player independently of its race."): 
        "La sélection de peau est entièrement libre. Vous pouvez choisir n'importe quelle texture pour votre personnage, quelle que soit sa race.",
    ("$Info_Player_Teeth_Mode_0", "The player teeth textures are not modified by RSV. Choose this option if you don't want RSV to affect the player teeth. This is the only possible option if you use a custom race for the player."): 
        "Les textures de dents du joueur ne sont pas modifiées par RSV. Choisissez cette option si vous ne souhaitez pas que RSV affecte les dents du joueur. C'est l'unique option possible si vous utilisez une race personnalisée.",
    ("$Info_Player_Teeth_Mode_1", 'Teeth textures change to "Bloody" when the player becomes a vampire. Otherwise, teeth behave as default.'): 
        'Les textures de dents deviennent « Ensanglantées » lorsque le joueur devient un vampire. En dehors de cet état, les dents conservent leur apparence par défaut.',
    ("$Info_Player_Teeth_Mode_2", "Teeth textures change depending on the player race. Each vanilla race gets a different set of teeth textures."): 
        "Les textures de dents varient selon la race du joueur. Chaque race du jeu de base dispose d'une dentition distincte.",
    ("$Info_Player_Teeth_Mode_3", "Teeth textures selection is free. You can select any teeth modification for the player independently of its race."): 
        "Le choix des textures de dents est entièrement libre. Vous pouvez attribuer la dentition de votre choix à votre personnage, quelle que soit sa race.",
    ("$Info_Player_Teeth_Off", "Teeth options are disabled because you didn't choose teeth options for the player during installation."): 
        "Les options de dents sont désactivées car vous n'avez pas choisi les options de dentition pour le joueur lors de l'installation.",
    ("$Info_No_Options_Race", "Player options are disabled because RSV detected that the player is not a vanilla race."): 
        "Les options du joueur sont désactivées car RSV a détecté que votre personnage n'appartient pas à une race du jeu de base.",
    ("$Info_No_Options_Fem1", "Player options are disabled because the player is female but during installation you didn't choose RSV options for female player. Also, RSV hasn't detected any CBBE or BHUNP body installed."): 
        "Les options du joueur sont désactivées car votre personnage est une femme, mais vous n'avez pas sélectionné les options féminines lors de l'installation. De plus, RSV n'a détecté aucun corps CBBE ou BHUNP installé.",
    ("$Info_No_Options_Fem2", "Player options are disabled because the player is female but RSV hasn't detected any CBBE or BHUNP body installed."): 
        "Les options du joueur sont désactivées car votre personnage est une femme, mais RSV n'a détecté aucun corps CBBE ou BHUNP installé.",
    ("$Info_No_Options_Fem3", "Player options are disabled because the player is female but during installation you didn't choose RSV options for female player."): 
        "Les options du joueur sont désactivées car votre personnage est une femme, mais vous n'avez pas sélectionné les options féminines lors de l'installation de RSV.",
    ("$Info_No_Options_Mal1", "Player options are disabled because the player is male but during installation you didn't choose RSV options for male player. Also, RSV hasn't detected HIMBO and SoS or TNG."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais vous n'avez pas sélectionné les options masculines lors de l'installation. De plus, RSV n'a détecté ni HIMBO, ni SoS ou TNG.",
    ("$Info_No_Options_Mal2", "Player options are disabled because the player is male but RSV hasn't detected HIMBO and SoS or TNG installed."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais RSV n'a détecté ni HIMBO, ni SoS ou TNG installés.",
    ("$Info_No_Options_Mal3", "Player options are disabled because the player is male but RSV hasn't detected HIMBO installed."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais RSV n'a pas détecté HIMBO.",
    ("$Info_No_Options_Mal4", "Player options are disabled because the player is male but RSV hasn't detected SoS or TNG installed."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais RSV n'a détecté ni SoS ni TNG installés.",
    ("$Info_No_Options_Mal5", "Player options are disabled because the player is male but during installation you didn't choose RSV options for male player. Also, RSV hasn't detected HIMBO."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais vous n'avez pas sélectionné les options masculines lors de l'installation. De plus, RSV n'a pas détecté HIMBO.",
    ("$Info_No_Options_Mal6", "Player options are disabled because the player is male but during installation you didn't choose RSV options for male player. Also, RSV hasn't detected SoS or TNG."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais vous n'avez pas sélectionné les options masculines lors de l'installation. De plus, RSV n'a détecté ni SoS ni TNG.",
    ("$Info_No_Options_Mal7", "Player options are disabled because the player is male but during installation you didn't choose RSV options for male player."): 
        "Les options du joueur sont désactivées car votre personnage est un homme, mais vous n'avez pas sélectionné les options masculines lors de l'installation de RSV.",
    ("$Notification_Switch_Info", "This enables notifications to the player. Notifications will show when the mod is being initialized or updated, never during normal gameplay. It is recommended to keep this enabled. (Enabled by default)."): 
        "Active les notifications destinées au joueur. Elles s'affichent uniquement lors de l'initialisation ou des mises à jour du mod, jamais en jeu normal. Il est conseillé de laisser cette option activée. (Activé par défaut).",
    ("$Debug_Mode_Switch_Info", "This enables debug mode, which makes the mod to log entries to the papyrus log file. THIS OPTION ENABLED CAN TAX PERFORMANCE! IT IS RECOMMENDED TO KEEP THIS DISABLED AND OLY ENABLING IT FOR DEBUGGING PURPOSES! (Disabled by default)."): 
        "Active le mode de débogage, qui consigne les opérations du mod dans le journal Papyrus. L'ACTIVATION DE CETTE OPTION PEUT DÉGRADER LES PERFORMANCES ! IL EST RECOMMANDÉ DE LA LAISSER DÉSACTIVÉE ET DE NE L'ACTIVER QU'À DES FINS DE DÉBOGAGE ! (Désactivé par défaut).",
    ("$Force_Options_Switch_Info", "The mod should detect automatically when player options should be enabled or not. This toggle bypasses that detection and force player options to be enabled no matter what. WARNING! THE MOD CHECKS ARE THERE TO MAKE SURE THAT IT WILL WORK CORRECTLY. IT IS RECOMMENDED NOT TO ACTIVATE THIS TOGGLE. (Disabled by default)."): 
        "Le mod détecte normalement de manière automatique si les options du joueur doivent être activées. Ce paramètre contourne cette détection et force l'activation des options quoi qu'il arrive. ATTENTION ! CES VÉRIFICATIONS SONT INDISPENSABLES AU BON FONCTIONNEMENT DU MOD. IL EST FORTEMENT DÉCONSEILLÉ D'ACTIVER CETTE OPTION. (Désactivé par défaut).",
    ("$Racemenu_Slider_Reapply_Info", "When enabled, RSV reapplies player head and teeth textures every time a RaceMenu slider value changes. This prevents RaceMenu from reverting textures to vanilla but can cause stutters when moving sliders rapidly. Disable this if you experience lag in RaceMenu. Textures will still be reapplied when RaceMenu is closed. (Enabled by default)."): 
        "Lorsque cette option est activée, RSV réapplique les textures de tête et de dents du joueur à chaque modification d'un curseur de RaceMenu. Cela empêche RaceMenu de restaurer les textures d'origine, mais peut provoquer des micro-saccades lors d'un déplacement rapide des curseurs. Désactivez cette option si vous constatez des ralentissements dans RaceMenu. Les textures seront de toute façon réappliquées à la fermeture du menu. (Activé par défaut).",
    ("$Uninstall_Button_Info", "Click to uninstall RSV. This will shut down the mod's functionalities, stop quests, dispell the spells, reset the player to default and clean up global variables for safe uninstalling. WARNING!! IT IS NEVER RECOMMENDED TO UNINSTALL ANY MOD MID GAME. DO IT AT YOUR OWN RISK!"): 
        "Cliquez pour désinstaller RSV. Cette action arrêtera les fonctionnalités du mod, suspendra les quêtes, dissipera les sorts, restaurera le joueur par défaut et nettoiera les variables globales pour une désinstallation propre. ATTENTION ! IL N'EST JAMAIS RECOMMANDÉ DE DÉSINSTALLER UN MOD EN PLEINE PARTIE. FAITES-LE À VOS PROPRES RISQUES !",
    ("$Copyright_Info", "All assets contained within this mod are the property of their authors. YOU ARE NOT ALLOWED TO USE ANY ASSET INCLUDED IN THIS MOD WITHOUT THE EXPLICIT CONSENT OF THE OWNER/S OF SAID ASSET."): 
        "Toutes les ressources contenues dans ce mod demeurent la propriété de leurs auteurs respectifs. IL EST STRICTEMENT INTERDIT D'UTILISER TOUTE RESSOURCE DE CE MOD SANS LE CONSENTEMENT EXPLICITE DE SON OU SES PROPRIÉTAIRES.",
    ("$Mod_Description_Info", "This mod uses SPID to distribute a different set of skin textures to each humanoid race to give them an unique look. It also can distribute different arrangements of muscularity for each race depending on weight, if so you choose. Males and females supported."): 
        "Ce mod exploite SPID pour distribuer des textures de peau distinctes à chaque race humanoïde afin de lui conférer une apparence unique. Il peut également répartir différentes variations de musculature selon le poids de chaque race, si vous choisissez cette option. Compatible avec les personnages masculins et féminins.",
    ("$Nexus_Link_Info", "https://www.nexusmods.com/skyrimspecialedition/mods/81668"): "https://www.nexusmods.com/skyrimspecialedition/mods/81668",
    ("$Vanilla_Mode", "Vanilla"): "Jeu de base (Vanilla)",
    ("$Independent_Mode", "Independent"): "Indépendant",
    ("$RSV_Mode", "RSV"): "RSV",
    ("$RSV_Fantasy_Mode", "RSV Fantasy"): "RSV Fantaisie",
    ("$Free_Mode", "Free"): "Libre",
    ("$Info_Player_Mode_0", "Vanilla Skin Information"): "Informations sur la peau du jeu de base",
    ("$Info_Player_Mode_1", "Independent Skin Information"): "Informations sur la peau indépendante",
    ("$Info_Player_Mode_2", "RSV Skin Information"): "Informations sur la peau RSV",
    ("$Info_Player_Mode_3", "RSV Fantasy Skin Information"): "Informations sur la peau RSV Fantaisie",
    ("$Info_Player_Mode_4", "Free Skin Information"): "Informations sur la peau libre",
    ("$Breton_Skin", "Breton"): "Breton",
    ("$Dunmer_Skin", "Dunmer"): "Elfe noir",
    ("$Altmer_Skin", "Altmer"): "Haut-Elfe",
    ("$Imperial_Skin", "Imperial"): "Impérial",
    ("$Nord_Skin", "Nord"): "Nordique",
    ("$Orsimer_Skin", "Orsimer"): "Orque",
    ("$Redguard_Skin", "Redguard"): "Rougegarde",
    ("$Bosmer_Skin", "Bosmer"): "Elfe des bois",
    ("$Vampire_Skin", "Vampire"): "Vampire",
    ("$Elder_Skin", "Elder"): "Aîné",
    ("$Asian_Skin", "Asian"): "Asiatique",
    ("$Afflicted_Skin", "Afflicted"): "Infecté",
    ("$Dremora_Skin", "Dremora"): "Drémora",
    ("$Dunmer_Fantasy_Skin", "Dunmer Fantasy"): "Elfe noir fantaisie",
    ("$Altmer_Fantasy_Skin", "Altmer Fantasy"): "Haut-Elfe fantaisie",
    ("$Orsimer_Fantasy_Skin", "Orsimer Fantasy"): "Orque fantaisie",
    ("$Bosmer_Fantasy_Skin", "Bosmer Fantasy"): "Elfe des bois fantaisie",
    ("$Snow_Elf_Skin", "Snow Elf"): "Elfe des neiges",
    ("$Vampire_Beast_Skin", "Vampire Beast"): "Bête vampirique",
    ("$Default_Age", "Default"): "Par défaut",
    ("$Young_Age", "Young"): "Jeune",
    ("$Old_Age", "Old"): "Âgé",
    ("$Default_Teeth_Mode", "Default"): "Par défaut",
    ("$Vampire_Teeth_Mode", "Vampire"): "Vampire",
    ("$RSV_Teeth_Mode", "RSV"): "RSV",
    ("$Free_Teeth_Mode", "Free"): "Libre",
    ("$Info_Teeth_Mode_0", "Default Teeth Information"): "Informations sur les dents par défaut",
    ("$Info_Teeth_Mode_1", "Vampire Teeth Information"): "Informations sur les dents de vampire",
    ("$Info_Teeth_Mode_2", "RSV Teeth Information"): "Informations sur les dents RSV",
    ("$Info_Teeth_Mode_3", "Free Teeth Information"): "Informations sur les dents libres",
    ("$Default_Teeth", "Default"): "Par défaut",
    ("$White_Teeth", "White"): "Blanches",
    ("$Yellow_Teeth", "Yellow"): "Jaunes",
    ("$Heavy_Yellow_Teeth", "Heavy Yellow"): "Très jaunes",
    ("$Crocked_Teeth", "Crocked"): "Irrégulières",
    ("$Missing_Teeth", "Missing"): "Manquantes",
    ("$Missing_Yellow_Teeth", "Missing Yellow"): "Manquantes & jaunes",
    ("$Gap_Teeth", "Gap"): "Écartées",
    ("$Gold_Teeth", "Gold"): "En or",
    ("$Full_Gold_Teeth", "Full Gold"): "Intégralement en or",
    ("$Bloody_Teeth", "Bloody"): "Ensanglantées",
    ("$Heavy_Bloody_Teeth", "Heavy Bloody"): "Très ensanglantées",
    ("$Fangs_Teeth", "Fangs"): "Crocs",
    ("$Sharp_Teeth", "Sharp"): "Pointues",
    ("$Dremora_Teeth", "Dremora"): "Drémora",
    ("$Rotten_Teeth", "Rotten"): "Pourries",
    ("$Toothless_Teeth", "Toothless"): "Édenté",
    ("$Mod_Version", "Mod Version"): "Version du mod",
    ("$Version_Release_Date", "Version Release Date"): "Date de publication de la version",
    ("$Mod_Description", "Mod Description"): "Description du mod",
    ("$Nexus_Link", "Nexus Link"): "Lien Nexus",
    ("$Mod_Design", "Mod Design"): "Conception du mod",
    ("$Mod_NiOverride", "NiOverride Functions"): "Fonctions NiOverride",
    ("$Mod_Assets", "Texture Assets"): "Ressources de texture",
    ("$Mod_Contributors", "Contributor"): "Contributeurs",
    ("$Mod_MCM_Design", "MCM Design"): "Conception du MCM",
    ("$Mod_Development", "Development"): "Développement",
    ("$Copyright", "© Copyright Information RSV"): "© Droits d'auteur RSV",
    ("$Key_Already_Mapped", "This key is already mapped to:"): "Cette touche est déjà assignée à :",
    ("$Confirm_Key", "Are you sure you want to continue?"): "Voulez-vous vraiment continuer ?",
    ("$Yes", "Yes"): "Oui",
    ("$No", "No"): "Non",
    ("$Unselectable_Options", "Options are unselectable"): "Options non sélectionnables",
    ("$Not_Applicable", "Not Applicable"): "Non applicable",
    ("$Is_Installed", "<font color = '#4c9b4c'>Installed"): "<font color = '#4c9b4c'>Installé",
    ("$Not_Installed", "<font color = '#b00000'>Not Installed"): "<font color = '#b00000'>Non installé",
    ("$Warning", "WARNING!"): "AVERTISSEMENT !",
    ("$Warning_Desc", "You are missing one or more required mods."): "Un ou plusieurs mods requis sont manquants.",
    ("$Warning_RSV_Wont_Work", "RSV might not work as intended."): "RSV risque de ne pas fonctionner correctement.",
    ("$Warning_FemaleBody", "RSV could not detect either CBBE or BHUNP."): "RSV n'a détecté ni CBBE ni BHUNP.",
    ("$Warning_FemaleBody2", "You won't be able to use RSV for females."): "Vous ne pourrez pas utiliser RSV pour les femmes.",
    ("$Warning_MaleBody", "RSV could not detect HIMBO."): "RSV n'a pas pu détecter HIMBO.",
    ("$Warning_MaleBody2", "You won't be able to use RSV for males."): "Vous ne pourrez pas utiliser RSV pour les hommes.",
    ("$Warning_Schlong", "RSV could not detect either SoS or TNG."): "RSV n'a détecté ni SoS ni TNG.",
    ("$Warning_Schlong2", "You won't be able to use RSV for males."): "Vous ne pourrez pas utiliser RSV pour les hommes.",
    ("$Warning_JC", "RSV could not detect JContainers or wrong version."): "RSV n'a pas détecté JContainers ou la version est incorrecte.",
    ("$Warning_JC2", "The MCM might not work as intended."): "Le menu MCM risque de ne pas fonctionner correctement.",
    ("$All_Installed", "All required mods detected."): "Tous les mods requis sont détectés.",
    ("$Mod_Installing", "Installing Racial Skin Variance"): "Installation de Racial Skin Variance en cours",
    ("$Mod_Installed", "Racial Skin Variance Installed"): "Racial Skin Variance installé",
    ("$New_Version_Detected", "New Version of RSV Detected"): "Nouvelle version de RSV détectée",
    ("$Older_Version_Detected", "Pre-3.0.0 Version Detected. Upgrading RSV"): "Version antérieure à la 3.0.0 détectée. Mise à niveau de RSV",
    ("$Update_Start", "Updating Racial Skin Variance"): "Mise à jour de Racial Skin Variance en cours",
    ("$Update_Completed", "Racial Skin Variance Succesfully Updated"): "Racial Skin Variance mis à jour avec succès",
    ("$MCM_Updated", "RSV MCM Updated"): "MCM de RSV mis à jour",
    ("$Update_Error", "WARNING! RSV COULD NOT FINISH UPDATING"): "ATTENTION ! RSV N'A PAS PU TERMINER LA MISE À JOUR",
    ("$Initialization_Start", "Racial Skin Variance Initializing"): "Initialisation de Racial Skin Variance en cours",
    ("$Reaplying_Textures", "RSV - Reaplying Textures"): "RSV - Réapplication des textures en cours",
    ("$Initialization_Completed", "Racial Skin Variance Successfully Initialized"): "Racial Skin Variance initialisé avec succès",
    ("$Debug_Mode_Enabled", "RSV Debug Mode Enabled"): "Mode débogage de RSV activé",
    ("$Debug_Mode_Disabled", "RSV Debug Mode Disabled"): "Mode débogage de RSV désactivé",
    ("$Notifications_Enabled", "RSV Notification Mode Enabled"): "Notifications de RSV activées",
    ("$Mod_Uninstalling", "RSV Started Uninstallation"): "Désinstallation de RSV en cours",
    ("$Mod_Uninstalled", "RSV Uninstallation Completed"): "Désinstallation de RSV terminée",
    ("$Force_Enable_Player_Options_Prompt", "-- Racial Skin Variance --\\n\\nThe MCM is designed to detect automatically if player options should be enabled or not. This is a safeguard that depends on required mods, player race and sex, and installation choices.\\n\\nIf you decide to force enable these options, even though they may appear non selectable in this MCM, you should know that the mod may not work properly.\\n\\nIT IS RECOMMENDED NOT TO USE THIS OPTION."):
        "-- Racial Skin Variance --\\n\\nLe MCM est conçu pour détecter automatiquement si les options du joueur doivent être activées. Il s'agit d'une sécurité dépendant des mods requis, de la race et du sexe de votre personnage, ainsi que de vos choix d'installation.\\n\\nSi vous décidez de forcer l'activation de ces options alors qu'elles apparaissent grisées, sachez que le mod risque de ne pas fonctionner correctement.\\n\\nIL EST RECOMMANDÉ DE NE PAS UTILISER CETTE OPTION.",
    ("$Force_Enable_Confirm", "Confirm"): "Confirmer",
    ("$Force_Enable_Cancel", "Cancel"): "Annuler",
    ("$Uninstall_MCM_Prompt", "-- Racial Skin Variance --\\n\\nIf you decide to uninstall RSV, the uninstallation process will continue.\\n\\nThere should be no traces of scripts or properties after the uninstallation, which should keep this save in a good state.\\n\\nHowever, you should be aware that it never is completely safe to uninstall mods mid-game.\\nIF YOU DECIDE TO CONTINUE,\\n DO IT AT YOUR OWN RISK!"):
        "-- Racial Skin Variance --\\n\\nSi vous choisissez de désinstaller RSV, la procédure de désinstallation va se poursuivre.\\n\\nAucune trace de scripts ou de propriétés ne devrait subsister après la désinstallation, préservant ainsi l'intégrité de votre sauvegarde.\\n\\nGardez toutefois à l'esprit qu'il n'est jamais totalement sans risque de désinstaller des mods en cours de partie.\\nSI VOUS DÉCIDEZ DE CONTINUER,\\nFAITES-LE À VOS PROPRES RISQUES !",
    ("$Uninstall_Confirm", "Confirm"): "Confirmer",
    ("$Uninstall_Cancel", "Cancel"): "Annuler",
    ("$Uninstall_Close_MCM", "-- Racial Skin Variance --\\n\\nNow close the MCM menu and the uninstallation process will start.\\n\\nAfter RSV has been uninstalled, follow closely the instructions that will be provided when the process is completed."):
        "-- Racial Skin Variance --\\n\\nFermez maintenant le menu MCM pour lancer le processus de désinstallation.\\n\\nUne fois RSV désinstallé, suivez attentivement les instructions qui s'afficheront à la fin de la procédure.",
    ("$RSVUninstall_Aborted", "-- Racial Skin Variance --\\n\\nUninstallation aborted!\\n\\n"):
        "-- Racial Skin Variance --\\n\\nDésinstallation annulée !\\n\\n",
    ("$OK", "OK"): "OK",
    ("$Manual_Start_Prompt", '-- Racial Skin Variance --\\n\\nThis will manually start the RSV initialization process, bypassing the character creation detection.\\n\\nYou can use this if the mod is stuck on "Mod Not Ready" and you are already in the game world, or if you want to start the mod earlier.\\n\\nDo you want to continue?'):
        '-- Racial Skin Variance --\\n\\nCette action lancera manuellement le processus d\'initialisation de RSV, en contournant la détection de création du personnage.\\n\\nVous pouvez l\'utiliser si le mod reste bloqué sur « Mod non prêt » alors que vous êtes déjà dans le monde du jeu, ou si vous désirez démarrer le mod plus tôt.\\n\\nVoulez-vous continuer ?',
    ("$Manual_Start_Close_MCM", "-- Racial Skin Variance --\\n\\nClose the MCM menu now. RSV will begin initializing shortly."):
        "-- Racial Skin Variance --\\n\\nFermez le menu MCM dès maintenant. L'initialisation de RSV commencera dans un instant.",
}

def update_esp():
    print("=== Checking & Updating ESP JSON ===")
    with open(ESP_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    for entry in data:
        key = (entry.get("form_id"), entry.get("type"), entry.get("index"), entry.get("original"))
        if key in ESP_UPDATES:
            new_val = ESP_UPDATES[key]
            old_val = entry.get("string")
            if old_val != new_val:
                print(f"ESP Updated {entry.get('editor_id')} ({entry.get('type')}): '{old_val}' -> '{new_val}'")
                entry["string"] = new_val
                entry["status"] = "TranslationComplete"
                updated_count += 1

    with open(ESP_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))
    print(f"ESP JSON saved. Total entries: {len(data)}, updated: {updated_count}\n")


def update_txt():
    print("=== Checking & Updating MCM TXT JSON ===")
    with open(TXT_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    missing_mappings = []

    for i, entry in enumerate(data):
        mcm_id = entry.get("mcm_id")
        orig = entry.get("original")
        key = (mcm_id, orig)

        if key in MCM_TRANSLATIONS:
            new_trans = MCM_TRANSLATIONS[key]
            old_trans = entry.get("string")
            old_status = entry.get("status")
            if old_trans != new_trans or old_status != "TranslationComplete":
                entry["string"] = new_trans
                entry["status"] = "TranslationComplete"
                updated_count += 1
        else:
            missing_mappings.append((i, mcm_id, orig))

    if missing_mappings:
        print(f"WARNING: {len(missing_mappings)} entries in txt.json have no mapping:")
        for idx, mid, orig in missing_mappings:
            print(f"  [{idx}] {mid}: {orig}")
        raise ValueError("Incomplete mapping for MCM TXT JSON!")

    with open(TXT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"MCM TXT JSON saved. Total entries: {len(data)}, updated/completed: {updated_count}\n")


if __name__ == "__main__":
    update_esp()
    update_txt()
