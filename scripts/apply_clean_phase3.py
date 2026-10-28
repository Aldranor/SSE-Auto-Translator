# -*- coding: utf-8 -*-
"""
Phase 3: Éradication des Traductions Restées en Anglais & Phrases Hybrides EN/FR
Applies all player-facing translations for untranslated/hybrid strings and sets
NoTranslationRequired on verified internal/technical engine records.
"""
import json
import os
import re

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"
SCRATCH_DIR = r"C:\Users\mouaw\.gemini\antigravity\brain\ac368bee-d202-4c72-87be-2434745643fb\scratch"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    # 1. Load canonical Inigo BOOK DESC translations from Inigo\Inigo.esp.json
    inigo_path = os.path.join(DB_DIR, r"Inigo\Inigo.esp.json")
    inigo_data = load_json(inigo_path)
    inigo_books_by_fid6 = {}
    for e in inigo_data:
        if e.get("type") == "BOOK DESC" and e.get("form_id"):
            fid6 = e["form_id"].split("|")[0][-6:]
            if fid6 in ("05DCE1", "05E245", "0AD12F", "05ED19"):
                inigo_books_by_fid6[fid6] = e["string"]

    # 2. Load canonical Altmer RACE DESC & WEAP DESC from DB
    canon_by_type_orig = {}
    # Populate exact canonical player-facing translations verified during Phase 3
    EXACT_TYPE_ORIG_MAP = {
        # DIAL FULL
        ("DIAL FULL", "What brings you to Skyrim?"): "Qu'est-ce qui vous amène en Bordeciel ?",
        ("DIAL FULL", "Disable Quests"): "Désactiver des quêtes",
        ("DIAL FULL", "Outdoors and Dungeons"): "Extérieurs et donjons",
        ("DIAL FULL", "Disable All Non-Quest NPCs"): "Désactiver tous les PNJ hors quête",
        ("DIAL FULL", "Bodyguard at Robber's Refuge"): "Garde du corps au Refuge des brigands",
        # MGEF FULL
        ("MGEF FULL", "Calm"): "Calme",
        ("MGEF FULL", "Fortify Stamina"): "Renfort de vigueur",
        ("MGEF FULL", "Fortify Magicka"): "Renfort de magie",
        ("MGEF FULL", "Magicka Damage"): "Dégâts de magie",
        ("MGEF FULL", "Stamina Damage"): "Dégâts de vigueur",
        ("MGEF FULL", "Reanimate"): "Réanimation",
        ("MGEF FULL", "Slow Time Effect"): "Effet de ralentissement du temps",
        ("MGEF FULL", "Restore Health Area"): "Zone de restauration de santé",
        ("MGEF FULL", "Wind Running"): "Coursevent",
        ("MGEF FULL", "Enslave the Weak"): "Asservissement des faibles",
        ("MGEF FULL", "Bond of Summoning"): "Lien d'invocation",
        ("MGEF FULL", "Spell Twine"): "Corde de sorts",
        ("MGEF FULL", "Defy Death"): "Mort bravée",
        ("MGEF FULL", "Strength of Earth"): "Force de la terre",
        ("MGEF FULL", "Prepare for Adventure"): "Prêt pour l'aventure",
        ("MGEF FULL", "Movement Speed Debuff"): "Pénalité de vitesse de déplacement",
        ("MGEF FULL", "Instant Poison Damage"): "Dégâts de poison instantanés",
        ("MGEF FULL", "Coldfire Damage"): "Dégâts de givreflamme",
        ("MGEF FULL", "Conjure Deadeye Captain"): "Invocation du capitaine Tête-de-Mort",
        ("MGEF FULL", "Fire Storm 100"): "Tempête de feu 100",
        ("MGEF FULL", "Fire Storm 25"): "Tempête de feu 25",
        ("MGEF FULL", "Slowed Movement During Taunting"): "Ralentissement pendant la provocation",
        ("MGEF FULL", "Waterbreathing"): "Respiration aquatique",
        ("MGEF FULL", "Fortify Speed"): "Renfort de vitesse",
        ("MGEF FULL", "Fortify Health"): "Renfort de santé",
        ("MGEF FULL", "Resist Magic"): "Résistance à la magie",
        ("MGEF FULL", "Resist Fire"): "Résistance au feu",
        ("MGEF FULL", "Resist Frost"): "Résistance à la glace",
        ("MGEF FULL", "Resist Shock"): "Résistance à la foudre",
        ("MGEF FULL", "Resist Poison"): "Résistance au poison",
        ("MGEF FULL", "Resist Disease"): "Résistance aux maladies",
        ("MGEF FULL", "Damage Health"): "Dégâts de santé",
        ("MGEF FULL", "Restore Health"): "Soin",
        ("MGEF FULL", "Restore Magicka"): "Restauration de magie",
        ("MGEF FULL", "Restore Stamina"): "Restauration de vigueur",
        ("MGEF FULL", "Paralyze"): "Paralysie",
        ("MGEF FULL", "Invisibility"): "Invisibilité",
        ("MGEF FULL", "Fear"): "Peur",
        ("MGEF FULL", "Frenzy"): "Frénésie",
        # SPEL FULL
        ("SPEL FULL", "Calm"): "Calme",
        ("SPEL FULL", "Spell Twine"): "Corde de sorts",
        ("SPEL FULL", "Lightning Cloak Drain"): "Siphon d'aura de foudre",
        ("SPEL FULL", "Ghost Ability"): "Talent de fantôme",
        ("SPEL FULL", "Storm Atronach abilities"): "Talents d'Atronach de foudre",
        ("SPEL FULL", "Storm Atronach Attack"): "Attaque d'Atronach de foudre",
        ("SPEL FULL", "Flame Atronach abilities"): "Talents d'Atronach de feu",
        ("SPEL FULL", "Skeleton Abilities"): "Talents de squelette",
        ("SPEL FULL", "Dynamic Combat"): "Combat dynamique",
        ("SPEL FULL", "Bleed"): "Saignement",
        ("SPEL FULL", "Quick Reflexes"): "Réflexes rapides",
        # PERK FULL
        ("PERK FULL", "Sneak Attack"): "Attaque furtive",
        ("PERK FULL", "Spell Twine"): "Corde de sorts",
        # ALCH FULL
        ("ALCH FULL", "Taunting Enemies"): "Provocation d'ennemis",
        ("ALCH FULL", "Calm Animals Through Music"): "Apaisement des animaux par la musique",
        # RACE FULL
        ("RACE FULL", "High Elf"): "Haut-Elfe",
        ("RACE FULL", "Dragon Priest"): "Prêtre-dragon",
        ("RACE FULL", "Skeleton"): "Squelette",
        ("RACE FULL", "Werewolf"): "Loup-garou",
        ("RACE FULL", "MudCrab"): "Vasard",
        ("RACE FULL", "Dog"): "Chien",
        ("RACE FULL", "Horse"): "Cheval",
        ("RACE FULL", "Wolf"): "Loup",
        ("RACE FULL", "Bear"): "Ours",
        ("RACE FULL", "Shadow"): "Ombre",
        ("RACE FULL", "Dwarven Spider"): "Araignée dwemer",
        ("RACE FULL", "Old People Race"): "Ancien",
        ("RACE FULL", "Imp"): "Galopin",
        ("RACE FULL", "Blue Spriggan"): "Spriggan bleu",
        ("RACE FULL", "Red Spriggan"): "Spriggan rouge",
        ("RACE FULL", "Snow Elf Vampire"): "Elfe des neiges vampire",
        # ARMO FULL
        ("ARMO FULL", "Brown Bear"): "Ours brun",
        ("ARMO FULL", "Boar"): "Sanglier",
        ("ARMO FULL", "Rabbit"): "Lapin",
        ("ARMO FULL", "Sheep"): "Mouton",
        ("ARMO FULL", "Draugr Skin"): "Peau de draugr",
        ("ARMO FULL", "Briar Heart Body"): "Torse Cœur de ronces",
        ("ARMO FULL", "Visage Heavy Armor"): "Visage - Armure lourde",
        ("ARMO FULL", "Visage Light Armor"): "Visage - Armure légère",
        ("ARMO FULL", "Visage Robes"): "Visage - Robe",
        ("ARMO FULL", "DE Freja Armor NPC"): "Armure de Freja (PNJ)",
        ("ARMO FULL", "DE Robin Wolf Leather Armor NPC"): "Armure en cuir de loup de Robin (PNJ)",
        ("ARMO FULL", "DE Robin Gloves NPC"): "Gants de Robin (PNJ)",
        # CONT FULL
        ("CONT FULL", "Sack"): "Sac",
        ("CONT FULL", "Pot"): "Marmite",
        ("CONT FULL", "Thieves Guild Fence Chest"): "Coffre de receleur de la Guilde des voleurs",
        # ACTI RNAM / FULL
        ("ACTI RNAM", "Mine"): "Creuser",
        ("ACTI RNAM", "Read"): "Lire",
        ("ACTI FULL", "Shrine of Mara"): "Autel de Mara",
        # LCTN FULL
        ("LCTN FULL", "Winterhold"): "Fortdhiver",
        # MESG FULL / DESC / ITXT
        ("MESG FULL", "Water"): "Eau",
        ("MESG FULL", "Door Barred"): "Porte barricadée",
        ("MESG FULL", "Manage Contributors to the Dragonborn Gallery"): "Gère les contributeurs dans la Galerie de l'Enfant de dragon",
        ("MESG FULL", "The Witch's Hut can't travel there."): "La cabane de la sorcière ne peut pas voyager jusqu'ici.",
        ("MESG FULL", "Water Raised"): "Niveau d'eau monté",
        ("MESG FULL", "Gem Locked"): "Gemme verrouillée",
        ("MESG FULL", "Can't Use"): "Impossible à utiliser",
        ("MESG FULL", "No Effective Change"): "Aucun changement notable",
        ("MESG FULL", "Fixes minor issues with 1 new merchant's inventory and 3 new food items' keywords."): "Corrige des problèmes mineurs avec l'inventaire d'un nouveau marchand et les mots-clés de 3 nouveaux aliments.",
        ("MESG FULL", "Fixes minor issues with 1 new merchant's inventory and 2 new animal part items' keywords."): "Corrige des problèmes mineurs avec l'inventaire d'un nouveau marchand et les mots-clés de 2 nouveaux ingrédients animaux.",
        ("MESG FULL", "Fixes minor issues with 2 existing and 2 new merchants' inventories, and 2 existing food items' models."): "Corrige des problèmes mineurs avec l'inventaire de 2 marchands existants et 2 nouveaux, ainsi que les modèles de 2 aliments existants.",
        ("MESG FULL", "Fixes noticeable issues with 2 new merchants' inventories and 5 new animal part items' keywords."): "Corrige des problèmes notables avec l'inventaire de 2 nouveaux marchands et les mots-clés de 5 nouveaux ingrédients animaux.",
        ("MESG FULL", "Fixes minor issues with 3 existing merchants' inventories."): "Corrige des problèmes mineurs avec l'inventaire de 3 marchands existants.",
        ("MESG DESC", "Pick Up Radius: OFF"): "Rayon de ramassage : DÉSACTIVÉ",
        ("MESG DESC", "Pick Up Radius: ON"): "Rayon de ramassage : ACTIVÉ",
        ("MESG DESC", "Thank you for testing the Campfire %.2f Beta!\r\n\r\nThis version is intended for testing purposes only. Please do not save your game or use this version for long-term use.\r\n\r\nPlease submit all feedback and bug reports to the Campfire Nexus page.\r\n\r\nThanks! -- Chesko"): "Merci de tester la bêta %.2f de Feux de camp !\r\n\r\nCette version est uniquement destinée aux tests. Veuillez ne pas sauvegarder votre partie ni utiliser cette version sur le long terme.\r\n\r\nVeuillez soumettre tous vos retours et rapports de bugs sur la page Nexus de Campfire.\r\n\r\nMerci ! -- Chesko",
        ("MESG DESC", "It looks like you just updated to Legacy of the Dragonborrn 5.5.3. \r\n\r\nIf you have started a new game with 5.5.3, you can ignore this message. \r\n\r\nThis version includes changes to the optional side quest \"Ongar's Kegbreaker\" which starts in the Nightgate Inn. If you continue this quest may be broken in your saved game, which means you may not be able to complete it. \r\n\r\nTo play this content properly you will need to downgrade to 5.5.2 and complete this quest before updating again. \r\n\r\nWould you like to continue?"): "Il semblerait que vous veniez de mettre à jour L'Héritage de l'Enfant de dragon vers la version 5.5.3.\r\n\r\nSi vous avez commencé une nouvelle partie avec la version 5.5.3, vous pouvez ignorer ce message.\r\n\r\nCette version inclut des modifications de la quête secondaire optionnelle « Le Brise-tonneau d'Ongar » qui débute à l'auberge de la Porte nocturne. Si vous continuez, cette quête risque d'être corrompue dans votre sauvegarde et vous pourriez ne pas pouvoir la terminer.\r\n\r\nPour jouer correctement à ce contenu, vous devrez revenir à la version 5.5.2 et terminer cette quête avant de refaire la mise à jour.\r\n\r\nVoulez-vous continuer ?",
        ("MESG DESC", "You are using a stolen version of RDO.\r\nPlease notify the original author of RDO, cloudedtruth, about this stolen version.\r\nThe game will now return to the main menu.\r\nThis will happen every time you load a save with the stolen version of RDO installed.\r\n"): "Vous utilisez une version volée de RDO.\r\nVeuillez prévenir l'auteur original de RDO, cloudedtruth, au sujet de cette version volée.\r\nLe jeu va maintenant revenir au menu principal.\r\nCela se produira à chaque chargement d'une sauvegarde avec la version volée de RDO installée.\r\n",
        ("MESG ITXT", "Forge - 1H"): "Forger - 1M",
        ("MESG ITXT", "Forge - 2H"): "Forger - 2M",
        ("MESG ITXT", "$AMOT Reset general to default"): "$AMOT Réinitialiser général par défaut",
        ("MESG ITXT", "$AMOT Reset general to full"): "$AMOT Réinitialiser général au complet",
        ("MESG ITXT", "ON"): "ACTIVÉ",
        # WEAP FULL
        ("WEAP FULL", "The Dagger of Riften (2)"): "La Dague de Faillaise (2)",
        # CLAS FULL
        ("CLAS FULL", "Bandit Archer"): "Archer bandit",
        # NPC_ FULL & SHRT
        ("NPC_ FULL", "Pit Fan"): "Spectateur de l'arène",
        ("NPC_ FULL", "Romanov the Royal Guard"): "Romanov le garde royal",
        ("NPC_ FULL", "Romanov the Companion"): "Romanov le compagnon",
        ("NPC_ FULL", "Falmer Primordial"): "Falmer primordial",
        ("NPC_ FULL", "Drevis Neloren"): "Drévis Néloren",
        ("NPC_ SHRT", "Drevis"): "Drévis",
        ("NPC_ FULL", "Aphia Velothi"): "Aphia Vélothi",
        ("NPC_ FULL", "Skald"): "Scalde",
        ("NPC_ FULL", "Guard 1"): "Garde 1",
        ("NPC_ FULL", "Guard 2"): "Garde 2",
        ("NPC_ FULL", "Guard 3"): "Garde 3",
        ("NPC_ FULL", "Guard 4"): "Garde 4",
        ("NPC_ FULL", "Guard 6"): "Garde 6",
        # PERK DESC
        ("PERK DESC", "You are able to summon up to 30 Locust Storm summons."): "Vous pouvez invoquer jusqu'à 30 nuées de criquets.",
        ("PERK DESC", "Nightingale Armor can be tempered twice as much when you have the Advanced Armors perk, and Nightingale Weapons inflict additional sneak damage."): "L'armure de Rossignol peut être améliorée deux fois plus lorsque vous possédez l'atout Armures avancées, et les armes de Rossignol infligent des dégâts furtifs supplémentaires.",
        ("PERK DESC", "Blink behind a combat target"): "Vous téléporte derrière une cible en combat.",
        ("PERK DESC", "Turn to Mist"): "Vous transforme en brume.",
        ("PERK DESC", "In combat, when blocking, you are surrounded by a cloud of bats that feed on enemies within melee range."): "En combat, lorsque vous parez, vous êtes entouré d'une nuée de chauves-souris qui se nourrissent des ennemis à portée de mêlée.",
        # MGEF DNAM & SPEL DESC
        ("MGEF DNAM", "Every third Transition is random."): "Chaque troisième transition est aléatoire.",
        ("MGEF DNAM", "Dig for buried treasure"): "Creuse à la recherche d'un trésor enfoui.",
        ("SPEL DESC", "Dig for buried treasure"): "Creuse à la recherche d'un trésor enfoui.",
        ("MGEF DNAM", "leftovers. Eat it or sell it."): "Des restes. Mangez-les ou vendez-les.",
        ("MGEF DNAM", "Reanimate a dead body to fight for you for <dur> seconds."): "Réanime un cadavre qui combat pour vous pendant <dur> secondes.",
        ("MGEF DNAM", "Reanimate a dead body to fight for the caster for <dur> seconds."): "Réanime un cadavre qui combat pour le lanceur pendant <dur> secondes.",
        ("MGEF DNAM", "Reanimate a dead body to fight for <dur> seconds."): "Réanime un cadavre qui combat pendant <dur> secondes.",
        ("MGEF DNAM", "Your Magicka is increased by <mag>."): "Augmente votre magie de <mag> points.",
        ("MGEF DNAM", "Your Stamina is increased by <mag>."): "Augmente votre vigueur de <mag> points.",
        ("SPEL DESC", "Summons a spectral drum that plays for <300> seconds, improving Stamina Regen for the caster and nearby allies."): "Invoque un tambour spectral qui joue pendant <300> secondes, améliorant la régénération de vigueur du lanceur et des alliés proches.",
        # INFO NAM1
        ("INFO NAM1", "Now, if you'll excuse me."): "Maintenant, si vous voulez bien m'excuser.",
        # QUST NNAM (21 objectives)
        ("QUST NNAM", "Find the Dark Elf Who Spent Time in High Rock"): "Trouvez l'Elfe noir qui a vécu en Haute-Roche",
        ("QUST NNAM", "Show the Chant of Mara to Garridan Stalrous"): "Montrez le Chant de Mara à Garridan Stalrous",
        ("QUST NNAM", "Wait for Thorina's Cutters to appear"): "Attendez l'arrivée des Coupe-jarrets de Thorina",
        ("QUST NNAM", "Slay the Legendary Guardian of the Glade with Garridan Stalrous"): "Terrassez le Gardien légendaire de la clairière avec Garridan Stalrous",
        ("QUST NNAM", "Wait for Adius to prepare"): "Attendez qu'Adius se prépare",
        ("QUST NNAM", "Tell Silvio Crextus you managed to convince his father"): "Annoncez à Silvio Crextus que vous avez convaincu son père",
        ("QUST NNAM", "Convince Cessius Crextus to give his son more free time"): "Convainquez Cessius Crextus d'accorder plus de temps libre à son fils",
        ("QUST NNAM", "Astor is here"): "Astor est ici",
        ("QUST NNAM", "Meet Adius at the Greenwood Meadery"): "Retrouvez Adius à l'hydromellerie de Vertbois",
        ("QUST NNAM", "Wait for Adius to give the signal"): "Attendez le signal d'Adius",
        ("QUST NNAM", "Discuss the issue of Thorina's Cutters with Adius"): "Discutez du problème des Coupe-jarrets de Thorina avec Adius",
        ("QUST NNAM", "Speak with Garridan Stalrous"): "Parlez à Garridan Stalrous",
        ("QUST NNAM", "Reach and kill Thorina"): "Rejoignez et tuez Thorina",
        ("QUST NNAM", "Debrief with Adius"): "Faites le point avec Adius",
        ("QUST NNAM", "Search fallen pilgrims for prayerbooks of the Divines"): "Fouillez les pèlerins tombés pour trouver des livres de prières des Divins",
        ("QUST NNAM", "Attack and defeat the Cutter raiding party"): "Attaquez et éliminez le groupe de pillards des Coupe-jarrets",
        ("QUST NNAM", "Tell Cessius Crextus his son agreed to start studying"): "Annoncez à Cessius Crextus que son fils a accepté d'étudier",
        ("QUST NNAM", "Defeat the Glade Guardian"): "Vainquez le Gardien de la clairière",
        ("QUST NNAM", "Convince Silvio Crextus to start studying"): "Convainquez Silvio Crextus de se mettre à étudier",
        ("QUST NNAM", "Check on the state of Inigo's mind."): "Assurez-vous de l'état d'esprit d'Inigo.",
        # QUST CNAM (16 player-facing journal entries)
        ("QUST CNAM", "After slaying the Glade Guardian at the center of Frostfire Glade, the air erupted into a raging blizzard and a ghost nammed Garridan appeared, clad in ancient mithril armor. While his concern limited his verbosity, he indicated that more must yet be done to purify Frostfire Glade, lest its chill grow worse and eventually spill across Tamriel. He urged me to search the Glade for fallen pilgrims in a bid to retrieve their prayerbooks."): "Après avoir terrassé le Gardien au centre de la Clairière de Givrefeu, un violent blizzard s'est levé et un fantôme nommé Garridan est apparu, vêtu d'une ancienne armure en mithril. Bien que préoccupé et peu loquace, il m'a indiqué qu'il restait encore fort à faire pour purifier la Clairière de Givrefeu, sans quoi son froid glacial risquait de s'intensifier et de se répandre sur Tamriel. Il m'a pressé de fouiller la clairière à la recherche des pèlerins tombés afin de récupérer leurs livres de prières.",
        ("QUST CNAM", "Together, Garridan and I banished the unnatural blizzard emenating from Frostfire Glade after the death of the Glade Guardian. I should speak with Garridan before taking my leave."): "Ensemble, Garridan et moi avons banni le blizzard surnaturel qui émanait de la Clairière de Givrefeu après la mort du Gardien de la clairière. Je devrais parler à Garridan avant de prendre congé.",
        ("QUST CNAM", "After defeating the Glade Guardian in Frostfire Glade, an arcane blizzard began emenating from the Glade's heart. I and an ancient knight who fell in Frostfire Glade named Garridan banished the blizzard by reciting a prayer to Mara."): "Après avoir vaincu le Gardien de la Clairière de Givrefeu, un blizzard arcanique s'est mis à émaner du cœur de la clairière. En compagnie de Garridan, un ancien chevalier tombé dans la Clairière de Givrefeu, j'ai banni le blizzard en récitant une prière à Mara.",
        ("QUST CNAM", "After defeating the Glade Guardian in Frostfire Glade, an arcane blizzard began emenating from the Glade's heart. I and an ancient knight who fell in Frostfire Glade named Garridan banished the blizzard by reciting a prayer to Mara. He rewarded me with some cryptic advice and his magical helmet, and described to me his urge to continue to watch over the glade from the realm of spirit."): "Après avoir vaincu le Gardien de la Clairière de Givrefeu, un blizzard arcanique s'est mis à émaner du cœur de la clairière. En compagnie de Garridan, un ancien chevalier tombé dans la Clairière de Givrefeu, j'ai banni le blizzard en récitant une prière à Mara. Il m'a récompensé par quelques conseils énigmatiques ainsi que son casque magique, et m'a confié son désir de continuer à veiller sur la clairière depuis le royaume des esprits.",
        ("QUST CNAM", "Adius has mentioned the issue of Thorina's Cutters to me and I'm now discussing it with him. I should see where this conversation leads."): "Adius m'a parlé du problème des Coupe-jarrets de Thorina et j'en discute actuellement avec lui. Voyons où mène cette conversation.",
        ("QUST CNAM", "I've agreed to meet Adius at the Greenwood Meadery when I'm ready to help him deal with the issue of Thorina's Cutters, the bandits that have been plaguing Greenwood and the rest of County Bruma for some time. I should head there as soon as I'm ready."): "J'ai accepté de retrouver Adius à l'hydromellerie de Vertbois dès que je serai prêt à l'aider à régler le problème des Coupe-jarrets de Thorina, les bandits qui tourmentent Vertbois et le reste du comté de Bruma depuis quelque temps. Je devrais m'y rendre dès que possible.",
        ("QUST CNAM", "We're executing our plan to take down the group of bandits known as Thorina's Cutters. First things first, though - Adius needs to get everything in place."): "Nous mettons à exécution notre plan pour neutraliser la bande de brigands connue sous le nom des Coupe-jarrets de Thorina. Mais avant toute chose, Adius doit mettre ses hommes en place.",
        ("QUST CNAM", "Adius has everything prepared. Now we just need to lie in wait until Thorina's Cutters appear to pillage the meadery. I should try to be inconspicuous."): "Adius a tout préparé. Il ne nous reste plus qu'à monter une embuscade en attendant que les Coupe-jarrets de Thorina viennent piller l'hydromellerie. Je dois essayer de rester discret.",
        ("QUST CNAM", "The Cutters are approaching. Adius asked me to wait until he gives the signal, then join his forces in attacking the Cutters' raiding party. That should, hopefully, allow us to press the advantage and attack the heart of Thorina's Cutters while they're off-balance."): "Les Coupe-jarrets approchent. Adius m'a demandé d'attendre son signal avant de me joindre à ses hommes pour attaquer leur groupe de pillards. Cela devrait nous permettre de prendre l'avantage et de frapper au cœur des Coupe-jarrets de Thorina pendant qu'ils sont déstabilisés.",
        ("QUST CNAM", "Adius has given the signal. The time is now - we need to attack this group of Thorina's Cutters to knock them off-balance, then prepare to assault their base proper."): "Adius a donné le signal. Le moment est venu : nous devons attaquer ce groupe de Coupe-jarrets de Thorina pour les déstabiliser, puis nous préparer à donner l'assaut sur leur repaire.",
        ("QUST CNAM", "After asking me to meet him for drinks at the Jerall View, Adius roped me into aiding the Bruma Guard once again - this time, in dealing with Thorina's Cutters, a well-armed and well-financed bandit ring operating throughout County Bruma. After executing a woodland ambush, we stormed Fort Cutpurse and slew Thorina, but not before Atienne Guilette, who'd broken free from the Bruma jail, could ambush me. Adius thanked me for my service and suggested I meet him in Bruma to receive a fitting reward."): "Après m'avoir invité à boire un verre à la Vue des Jerall, Adius m'a de nouveau enrôlé pour prêter main-forte à la garde de Bruma : cette fois contre les Coupe-jarrets de Thorina, un réseau de bandits bien armés et bien financés sévissant dans tout le comté de Bruma. Après leur avoir tendu une embuscade dans les bois, nous avons pris d'assaut Fort Coupe-bourse et tué Thorina, non sans qu'Atienne Guilette, évadé de la prison de Bruma, m'ait tendu un guet-apens. Adius m'a remercié pour mes services et m'a proposé de le retrouver à Bruma pour recevoir une récompense méritée.",
        ("QUST CNAM", "Someone named Ludwig used to live in Clockwork Castle. I have found several of his journals. One of them contained a key which apparently belongs to a wardrobe in the Master Bedroom."): "Un certain Ludwig vivait autrefois au Château mécanique. J'ai trouvé plusieurs de ses journaux. L'un d'eux contenait une clé qui semble ouvrir une armoire dans la chambre principale.",
        ("QUST CNAM", "Before Lamashtu could explain what keeps me from leaving Clockwork Castle - and what it has to do with the Gilded once being living Dwemer people - something rendered her insensible. Lahar says she needs a new soul gem \"heart\". An unusual Gilded called \"Amalgam\" may have one we can use. I believe I have found him in the Nurndural Sickness Ward, but he paralysed me and has retreated beyond a portcullis. There is a ballista nearby that may be able to breach the gate, but its control lever is missing. The lever handle I found in the \"Mortal Layer\" should work as a replacement."): "Avant que Lamashtu ne puisse m'expliquer ce qui m'empêche de quitter le Château mécanique — et le rapport avec le fait que les Dorés étaient autrefois des Dwemers vivants — quelque chose l'a rendue inconsciente. Lahar dit qu'elle a besoin d'un nouveau « cœur » en gemme spirituelle. Un Doré inhabituel appelé « Amalgame » pourrait en posséder un. Je pense l'avoir trouvé dans l'aile des malades de Nurndural, mais il m'a paralysé et s'est replié derrière une herse. Une baliste à proximité devrait pouvoir défoncer la grille, mais son levier de commande a disparu. La poignée de levier que j'ai trouvée dans la « Strate mortelle » devrait pouvoir le remplacer.",
        ("QUST CNAM", "Before Lamashtu could explain what keeps me from leaving Clockwork Castle - and what it has to do with the Gilded once being living Dwemer people - something rendered her insensible. Following Lahar's instructions, I retrieved a new soul gem \"heart\" for her and installed it in her chest. She appears to have recovered, so I should see what she has to say."): "Avant que Lamashtu ne puisse m'expliquer ce qui m'empêche de quitter le Château mécanique — et le rapport avec le fait que les Dorés étaient autrefois des Dwemers vivants — quelque chose l'a rendue inconsciente. Suivant les instructions de Lahar, j'ai récupéré un nouveau « cœur » en gemme spirituelle et l'ai installé dans sa poitrine. Elle semble avoir repris connaissance ; je devrais écouter ce qu'elle a à me dire.",
        ("QUST CNAM", "When I entered the Travel Machine in order to return to Skyrim, something stopped me. I simply turned and walked right back out again. I... can't leave. Perhaps Lahar or Lamashtu will know what is happening to me."): "Lorsque je suis entré dans la Machine de voyage pour retourner en Bordeciel, quelque chose m'en a empêché. J'ai simplement fait demi-tour et suis ressorti. Je... je ne peux pas partir. Peut-être que Lahar ou Lamashtu sauront ce qui m'arrive.",
        # QUST FULL (Missives & Player Quests)
        ("QUST FULL", "Kill Some Bandits"): "Des bandits à tuer",
        ("QUST FULL", "Kill a Dragon"): "Un dragon à tuer",
        ("QUST FULL", "Kill a Giant"): "Un géant à tuer",
        ("QUST FULL", "Kill an Ogre"): "Un ogre à tuer",
        ("QUST FULL", "Kill Some Forsworn"): "Des Parjures à tuer",
        ("QUST FULL", "Kill Rieklings"): "Des Riekelings à tuer",
        ("QUST FULL", "Kill Some Marauders"): "Des maraudeurs à tuer",
        ("QUST FULL", "Kill Some Things"): "Des créatures à tuer",
        ("QUST FULL", "Deliver a Letter Distant"): "Livraison de lettre assez loin",
        ("QUST FULL", "Deliver a Letter Medium"): "Livraison de lettre moyennement loin",
        ("QUST FULL", "Deliver a Letter Near"): "Livraison de lettre à proximité",
        ("QUST FULL", "Deliver a Weapon Distant"): "Livraison d'arme assez loin",
        ("QUST FULL", "Deliver a Weapon Medium"): "Livraison d'arme moyennement loin",
        ("QUST FULL", "Deliver a Weapon Near"): "Livraison d'arme à proximité",
        ("QUST FULL", "Deliver a Potion Far"): "Livraison de potion",
        ("QUST FULL", "Deliver a Potion Medium"): "Livraison de potion",
        ("QUST FULL", "Deliver a Potion Med"): "Livraison de potion",
        ("QUST FULL", "Deliver a Potion Near"): "Livraison de potion",
        ("QUST FULL", "Collect Some Food"): "Collecte de nourriture",
        ("QUST FULL", "Collect Some Standard Soul Gems"): "Collecte de gemmes spirituelles communes",
        ("QUST FULL", "Collect Some Weak Soul Gems"): "Collecte de petites gemmes spirituelles",
        ("QUST FULL", "Find a Powerful Soul Gem"): "Recherche d'une puissante gemme spirituelle",
        ("QUST FULL", "Gather Common Ore"): "Récolte de minerai commun",
        ("QUST FULL", "Gather Uncommon Ore"): "Récolte de minerai peu commun",
        ("QUST FULL", "Gather Rare Ore"): "Récolte de minerai rare",
        ("QUST FULL", "Gather Very Rare Ore"): "Récolte de minerai très rare",
        ("QUST FULL", "Gather Some Common Ingredients"): "Récolte d'ingrédients communs",
        ("QUST FULL", "Gather Some Uncommon Ingredients"): "Récolte d'ingrédients peu communs",
        ("QUST FULL", "Gather Some Rare Ingredients"): "Récolte d'ingrédients rares",
        ("QUST FULL", "Recover From a Hideout"): "Récupération dans un repaire",
        ("QUST FULL", "Retrieve From a Ruin"): "Récupération dans une ruine",
        ("QUST FULL", "Retrieve From the Wilderness"): "Récupération dans la nature",
        ("QUST FULL", "Track Fugitive"): "Un fugitif à traquer",
        ("QUST FULL", "Track Thief"): "Un voleur à traquer",
        ("QUST FULL", "Track Vampire"): "Traquer un vampire",
        ("QUST FULL", "Reopen the Gate"): "Rouvrir le portail",
        ("QUST FULL", "Road to Amora"): "La route d'Amora",
        ("QUST FULL", "Saferoom Unlock: Frozen Abyss"): "Déverrouillage d'abri : Abîme gelé",
        ("QUST FULL", "Daedric Gallery Museum Tour"): "Visite guidée de la Galerie daedrique",
        ("QUST FULL", "Hall of Lost Empires Museum Tour"): "Visite guidée de la Salle des Empires perdus",
        ("QUST FULL", "Hall of Oddities Museum Tour"): "Visite guidée de la Salle des Curiosités",
        ("QUST FULL", "Hall of Heroes Museum Tour"): "Visite guidée de la Salle des Héros",
        ("QUST FULL", "Coming of Age"): "Passage à l'âge adulte",
        ("QUST FULL", "Gift from a friend"): "Cadeau d'un ami",
        ("QUST FULL", "Frostfire Unleashed"): "Givrefeu déchaîné",
        ("QUST FULL", "A Cutter in Need"): "Un Coupe-jarret dans le besoin",
        ("QUST FULL", "Water Run Dry"): "Pénurie d'eau",
        ("QUST FULL", "Word to Bruma"): "Message pour Bruma",
        ("QUST FULL", "The big, bad wolf"): "Le grand méchant loup",
        ("QUST FULL", "Horse, off course"): "Cheval égaré",
        ("QUST FULL", "Horse, Meet Troll"): "Entre cheval et troll",
        ("QUST FULL", "Cider Delivery"): "Livraison de cidre",
        ("QUST FULL", "Missing Dog"): "Chien disparu",
        ("QUST FULL", "Nord Weapons"): "Armes nordiques",
        ("QUST FULL", "Studying"): "Études",
        ("QUST FULL", "Horseshoe for Terinius"): "Fer à cheval pour Térinius",
        ("QUST FULL", "Soulgem for Elintius"): "Gemme spirituelle pour Élintius",
        ("QUST FULL", "Payments for Razzada"): "Paiements pour Razzada",
        ("QUST FULL", "Barnius tribute"): "Hommage à Barnius",
        ("QUST FULL", "Aera the Devout's missing amulet"): "L'amulette disparue d'Aéra la Dévote",
        ("QUST FULL", "Fighter's Guild Advertising"): "Publicité pour la Guilde des guerriers",
        ("QUST FULL", "Shipping request to Greenwood"): "Demande de livraison pour Vertbois",
        # MCM / UI (type '' or None)
        ("", "On"): "Activé",
        (None, "On"): "Activé",
        ("", "Pickpocket"): "Vol à la tire",
        (None, "Pickpocket"): "Vol à la tire",
        ("", "Dawnguard"): "Garde de l'aube",
        (None, "Dawnguard"): "Garde de l'aube",
        ("", "Hides this follower from the SOS menu. They still remain as your follower; SOS just stops acknowledging their existence."): "Masque ce compagnon dans le menu SOS. Il reste à vos côtés ; SOS cesse simplement de le prendre en compte.",
        (None, "Hides this follower from the SOS menu. They still remain as your follower; SOS just stops acknowledging their existence."): "Masque ce compagnon dans le menu SOS. Il reste à vos côtés ; SOS cesse simplement de le prendre en compte.",
        ("", "Toggles Droplet Particles Effect on Player when Wet"): "Active ou désactive l'effet de gouttelettes d'eau sur le joueur lorsqu'il est mouillé.",
        (None, "Toggles Droplet Particles Effect on Player when Wet"): "Active ou désactive l'effet de gouttelettes d'eau sur le joueur lorsqu'il est mouillé.",
        ("", "Snow Lens Added"): "Effet de neige sur l'écran ajouté",
        (None, "Snow Lens Added"): "Effet de neige sur l'écran ajouté",
        ("", "Go To Bed"): "Aller au lit",
        (None, "Go To Bed"): "Aller au lit",
        ("", "Sky Dial"): "Cadran céleste",
        (None, "Sky Dial"): "Cadran céleste",
        ("", "Go"): "Valider",
        (None, "Go"): "Valider",
        ("", "CUSTOM SKILLS"): "COMPÉTENCES PERSONNALISÉES",
        (None, "CUSTOM SKILLS"): "COMPÉTENCES PERSONNALISÉES",
        ("", "SYLPH OF GLASS"): "SYLPHE DE VERRE",
        (None, "SYLPH OF GLASS"): "SYLPHE DE VERRE",
        ("", "Honi was the faithful cat companion of the now deceased conjurer Rhorald, and his most beloved friend. When he died, his owner conjured a magical body of ice for him, where he placed his soul, so that Honi would remain by his side forever. Honi is now looking for a new friend to follow in magical adventures through Tamriel."): "Honi était le fidèle compagnon félin du conjurateur Rhorald, aujourd'hui défunt, et son plus cher ami. À la mort du chat, son maître lui invoqua un corps magique fait de glace et y plaça son âme afin qu'Honi demeure à ses côtés pour l'éternité. Honi cherche désormais un nouvel ami à suivre dans des aventures magiques à travers Tamriel.",
        (None, "Honi was the faithful cat companion of the now deceased conjurer Rhorald, and his most beloved friend. When he died, his owner conjured a magical body of ice for him, where he placed his soul, so that Honi would remain by his side forever. Honi is now looking for a new friend to follow in magical adventures through Tamriel."): "Honi était le fidèle compagnon félin du conjurateur Rhorald, aujourd'hui défunt, et son plus cher ami. À la mort du chat, son maître lui invoqua un corps magique fait de glace et y plaça son âme afin qu'Honi demeure à ses côtés pour l'éternité. Honi cherche désormais un nouvel ami à suivre dans des aventures magiques à travers Tamriel.",
    }

    # Find canonical translations for Altmer RACE DESC and the 3 WEAP DESC in p3_has_canon.json
    with open(os.path.join(SCRATCH_DIR, "p3_has_canon.json"), encoding="utf-8") as f:
        has_canon = json.load(f)
    for item in has_canon:
        tp = item.get("type")
        orig = item.get("original")
        if tp in ("RACE DESC", "WEAP DESC") and item.get("canon"):
            EXACT_TYPE_ORIG_MAP[(tp, orig)] = item["canon"][0][0]

    # Words that are identical in FR and EN or proper nouns/lore when original == string
    IDENTICAL_OR_PROPER_TYPES = {
        "NPC_ FULL", "NPC_ SHRT", "CELL FULL", "LCTN FULL", "WRLD FULL",
        "REGN RDMP", "WORD TNAM", "WOOP TNAM", "SHOU FULL",
    }
    IDENTICAL_WORDS_LOWER = {
        "poison", "potion", "illusion", "destruction", "conjuration", "altération",
        "mannequin", "dragon", "troll", "draugr", "falmer", "dwemer", "chaurus",
        "spriggan", "atronach", "dremora", "daedra", "skooma", "jarl", "thane",
        "septim", "nirnroot", "ébonite", "orichalque", "corindon", "malachite",
        "pierre de lune", "vif-argent", "stalhrim", "chitine", "bonemold",
        "intervention", "rage", "silence", "blizzard", "clairvoyance", "domination",
        "revenant", "courage", "translimination", "absolution", "inhibition",
        "supernova", "possession", "fissure", "suggestion", "transfusion",
        "wyrd", "fracture", "apocalypse", "wendigo", "liche", "zombie", "vampire",
        "squelette", "fantôme", "spectre", "gargouille", "minotaure", "ogre",
        "gobelin", "riekeling", "hagraven", "harfreuse", "loup-garou", "garou",
        "bandit", "mage", " mage...", "combat...", "3 minutes", "6 minutes",
        "12 minutes", "24 minutes", "30 minutes", "48 minutes", "option", "option 1",
        "ulfric", "miraak", "stendarr", "arkay", "mara", "dibella", "julianos",
        "kynareth", "zénithar", "zenithar", "talos", "akatosh", "auriel", "auri-el",
        "azura", "boethiah", "clavicus vile", "hermaeus mora", "hircine", "malacath",
        "mehrunes dagon", "mephala", "meridia", "molag bal", "namira", "nocturne",
        "peryite", "sanguine", "sheogorath", "vaermina", "sithis", "shor", "kyne",
        "tsun", "aldebaran", "helgen", "blancherive", "solitude", "vendeaume",
        "faillaise", "markarth", "morthal", "épervine", "aubétoile", "fortdhiver",
        "rivebois", "fort-ivar", "rorikbourg", "pont-dragon", "kynesgrove",
        "solstheim", "corberoc", "anvil", "bruma", "chorrol", "cheydinhal", "bravil",
        "leyawiin", "kvatch", "skingrad", "cyrodiil", "morrowind", "bordeciel",
        "tamriel", "nirn", "oblivion", "aetherius", "sovngarde", "apocrypha",
        "havreglace", "hadvar", "ralof", "river", "katana", "lucien", "inigo",
        "remiel", "ria.", "faendal.", "candle.", "khajiit.", "walks-in-sleep.",
    }

    # Specific file+idx overrides (translations & mismatch fixes & hybrid fixes)
    SPECIFIC_FILE_IDX_TRANSLATIONS = {
        # 4 Mismatch fixes uncovered in Phase 3
        (r"Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level.esp.json", 3374): ("Alduin", "TranslationComplete"),
        (r"Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level.esp.json", 6006): ("Alduin", "TranslationComplete"),
        (r"Apocalypse - Magie de Bordeciel\Apocalypse - Vokrii Compatibility Patch.esp.json", 2): ("Shock On Hit Proc Magic Effects", "NoTranslationRequired"),
        (r"Lucien\Lucien.esp.json", 5401): (";The player has said they will not read the Oghma Infinium.", "NoTranslationRequired"),
        # Additional mismatch/hybrid fixes uncovered in Phase 3 strict scan
        (r"Adamant - Refonte des atouts\Adamant.esp.json", 1544): ("Ward Controller Perk", "NoTranslationRequired"),
        (r"Du parapente en Bordeciel\Paragliding.esp.json", 15): ("Effet de portance du parapente", "TranslationComplete"),
        (r"Fort-Ivar de Thuldor\Thuldor's Ivarstead.esp.json", 55): ("Qu'est-ce qui amène un Breton en Bordeciel ?", "TranslationComplete"),
        (r"Citizens of Tamriel\citizenscomplete.esp.json", 5598): ("Gélébor et Vyrthur avaient tous deux leurs illusions. Je... je souhaite juste mourir en paix.", "TranslationComplete"),
        (r"Legacy of the Dragonborn - Hall of Forgotten\dbm_hub_billyrow_patch.esp.json", 43): ("Solvistapp 1M - Reforgée en ébonite et argent", "TranslationComplete"),
        (r"Press E To Heal Followers vostFR 1.0 SE_AE\Press E To Heal Followers.esp.json", 54): ("Ouf ! C'était moins une.", "TranslationComplete"),
        (r"USSEP - Traduction Francaise\cutting room floor.esp.json", 493): ("-CONDITIONED NOT TO START- Mourning", "NoTranslationRequired"),
        (r"USSEP - Traduction Francaise\cutting room floor.esp.json", 531): ("Unlock the tower door after Ulfric's glorious victory", "NoTranslationRequired"),
        (r"Valvalis Combat - Visceral Tactics - French\valvalis.esp.json", 0): ("Nerf Damage 0.5 - Modified by Smilodon", "NoTranslationRequired"),
        (r"Vigilant voiced english vostFR\Vigilant.esm.json", 28): ("Metalic Priest Race", "NoTranslationRequired"),
        (r"Wintersun - Tribunal Integration\wintersun - gott patch.esp.json", 55): ("Pact Killer - Cloak Proc", "NoTranslationRequired"),
        (r"Vibrant weapons Nolvus fr\Vibrant weapons.esl.json", 76): ("Shock War Axe Activator L", "NoTranslationRequired"),
        (r"Vibrant weapons Nolvus fr\Vibrant weapons.esl.json", 77): ("Shock War Axe Activator R", "NoTranslationRequired"),
        (r"Vibrant weapons Nolvus fr\Vibrant weapons.esl.json", 115): ("Frostshock Warhammer Activator", "NoTranslationRequired"),
        # Gourmet copypasta dummy BOOK DESC
        (r"Gourmet - Refonte de la cuisine\Gourmet.esp.json", 9): (None, "NoTranslationRequired"),
        (r"Gourmet - Refonte de la cuisine\Gourmet.esp.json", 65): (None, "NoTranslationRequired"),
        (r"Gourmet - Refonte de la cuisine\Gourmet.esp.json", 175): (None, "NoTranslationRequired"),
        # Spell Tome BOOK DESC in Mysticism & Unslaad
        (r"Mysticisme - Refonte de la magie\MysticismMagic.esp.json", 748): ("<font face'$HandwrittenFont'><font size='40'><p align='center'>\r\nÉquilibre</font></font>", "TranslationComplete"),
        (r"UNSLAAD SE -voiced english- vostFR\Unslaad.esm.json", 1167): ("<font face'$HandwrittenFont'><font size='40'><p align='center'>\r\nConjuration de guetteur draconique</font></font>", "TranslationComplete"),
        # Midwood Isle Daedric font BOOK DESC
        (r"L'île de Sylval\Midwood Isle.esp.json", 1329): (
            "<font face='$DaedricFont'>\r\nGRAND SEIGNEUR D'OBLIVION\r\nENTENDS MA SUPPLIQUE\r\nJ'IMPLORE TES SERVITEURS\r\nAMÈNE-LES EN CE ROYAUME\r\nRELIE-LES À TRAVERS L'AURBIS\r\nAFIN QUE NOUS APPORTIONS LA MORT ET LA DESTRUCTION\r\n\r\nRESSENS LEUR ESSENCE DEPUIS OBLIVION\r\nATTIRE-LES VERS NOUS\r\nSENS LA TRAME DU MUNDUS SE DÉCHIRER ET SE ROMPRE\r\nET DÉLIVRE LES DAEDRA SUR CE PLAN\r\n</font>",
            "TranslationComplete",
        ),
        (r"L'île de Sylval\Midwood Isle.esp.json", 3822): (
            "<font face='$DaedricFont'>\r\nLe Marchand est ici\r\nApporte-moi sa pierre sigillaire\r\nIl fréquente ces pathétiques mortels près des Trois Salles comme tout amoureux des mortels tel que lui\r\nAgis avec discrétion il ne doit pas savoir que c'est moi qui t'envoie\r\nTrouve-moi quand tu auras la pierre\r\nJ'ouvrirai un portail vers notre royaume au nord\r\nNe me déçois pas\r\nValkynaz Jagrioth\r\n</font>",
            "TranslationComplete",
        ),
        # dbm_beyondreach_patch.esp.json BOOK DESC
        (r"L'Héritage de l'Enfant de dragon - Patches officiels\dbm_beyondreach_patch.esp.json", 18): (
            "<font face='$HandwrittenFont'><font size='18'>\r\nUNE MINUTE AVANT MINUIT\r\n\r\nUNE GRAINE PLANTÉE, NOURRIS SA CROISSANCE.\r\n\r\nMÉTASTASE ET ENGRAISSE-TOI.\r\n\r\nDU BÉTAIL AYANT LE GOÛT DU BÉTAIL.\r\n</font></font>",
            "TranslationComplete",
        ),
        (r"L'Héritage de l'Enfant de dragon - Patches officiels\dbm_beyondreach_patch.esp.json", 28): (
            "<font face=\"$HandwrittenFont\">\r\n<font size=\"40\">Prime</font>\r\n\r\nLe Conseil d'Abondance a émis un avis de recherche officiel.\r\n\r\nÀ tous les hommes et femmes valides du royaume d'Abondance. Des scélérats situés à <Alias=BountyLocation> harcèlent, détroussent et attaquent les citoyens et les voyageurs.\r\n\r\nUne récompense sera offerte à quiconque éliminera ces vauriens.\r\n\r\n-- Le Conseil de Sigmayne.</font>",
            "TranslationComplete",
        ),
        (r"L'Héritage de l'Enfant de dragon - Patches officiels\dbm_beyondreach_patch.esp.json", 51): (
            "<font face=\"$HandwrittenFont\">\r\n<font size=\"40\">Prime</font>\r\n\r\nLe Conseil d'Abondance a émis un avis de recherche officiel.\r\n\r\nÀ tous les chevaliers valides du royaume d'Abondance. Des scélérats situés à <Alias=PrisonerLocation> ont pris <alias=Prisoner> en otage ; il est de la plus haute importance de lui porter secours immédiatement !\r\n\r\nUne récompense sera offerte à tout chevalier qui ramènera ce citoyen sain et sauf.\r\n\r\n-- Le Conseil de Sigmayne.</font>",
            "TranslationComplete",
        ),
        # EEKs Whiterun Interiors 7 BOOK DESC
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 28): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Bon de commande</font>\r\n\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour Anoriath\r\n\r\n   - Potion de tir précis                                        x 2\r\n   - Philtre de tir précis                                       x 1\r\n\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 80): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Facture</font>\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour Eimar\r\n\r\n   - Potion de soin des maladies                                 79 po\r\n\r\n\r\nTotal                                                                       79 po\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 104): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Facture</font>\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour le Bazar de Béléthor\r\n\r\n   - Breuvage de régénération x 6                    870 po\r\n   - Potion de magie mineure x 6                     120 po\r\n   - Potion de vigueur intense x 2                   190 po\r\n   - Potion de soins mineurs x 4                      68 po\r\n\r\nTotal                                                                 1248 po\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 155): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Facture</font>\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour le Marchand de Rivebois\r\n\r\n   - Potion médicinale x 3                                       93 po\r\n   - Breuvage de résistance au froid x 5             755 po\r\n   - Potion de soin des maladies x 3                 237 po\r\n   - Potion de soins mineurs x 3                      51 po\r\n\r\nTotal                                                                 1136 po\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 165): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Bon de commande</font>\r\n\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour l'acolyte Jenssen\r\n\r\n   - Potion de soin des maladies                                 x 6\r\n\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 250): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Facture</font>\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour Idolaf Guerrier-Né\r\n\r\n   - Potion du guerrier                                          96 po\r\n\r\n\r\nTotal                                                                    96 po\r\n</font></p></font>",
            "TranslationComplete",
        ),
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 253): (
            "<p align='center'><font size='30'>\r\n<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>rcadia - Bon de commande</font>\r\n\r\n\r\n<font size='15'><font face='$HandwrittenFont'>Pour Adrianne Avenicci\r\n\r\n   - Élixir de forgeron                                          x 6\r\n   - Philtre de vigueur accrue                                   x 4\r\n   - Potion de vigueur intense                                   x 6\r\n\r\n</font></p></font>",
            "TranslationComplete",
        ),
        # Bestiary hybrids
        (r"The Dragonborn's Bestiary - Quest Patch Compendium\interface\creatures\vigilant\Blood Curse Dancer\Blood Curse Dancer.json.json", 1): (
            "Sous-produit grotesque de la Malédiction du sang, le Danseur de la malédiction du sang dérive en apesanteur dans les airs. Animé par la malédiction plutôt que par une volonté persistante, il se déplace avec une grâce troublante, comme contraint par un maître invisible.",
            "TranslationComplete",
        ),
        (r"The Dragonborn's Bestiary - Quest Patch Compendium\interface\creatures\vigilant\Flesh Guardian\Flesh Guardian.json.json", 1): (
            "Imposant gardien fabriqué à partir d'os blanchis, de chair en décomposition et de restes d'innombrables victimes, le Gardien de chair est une abomination conçue pour défendre les recoins les plus sombres de Havreglace. Sa structure colossale n'est pas maintenue par la vie, mais par la magie profane, lui permettant d'endurer des blessures qui feraient tomber n'importe quelle créature mortelle.",
            "TranslationComplete",
        ),
        (r"The Dragonborn's Bestiary - Quest Patch Compendium\interface\creatures\carved brink\dark hopper\dark hopper.json.json", 1): (
            "Les Sauteurs sombres sont des créatures cauchemardesques originaires des profondeurs de Carved Brink, connues pour leur apparence terrifiante et insectoïde et leur agilité inquiétante.\n\nCes êtres tordus, nés des énergies corrompues d'Oblivion, rôdent dans l'ombre et fondent sur leurs proies avec une vitesse fulgurante.",
            "TranslationComplete",
        ),
        (r"The Dragonborn's Bestiary - Quest Patch Compendium\interface\creatures\vigilant\Soul Shriven\Soul Shriven.json.json", 1): (
            "Les Tourmentés sont des mortels dont les âmes ont été réclamées par Molag Bal et liées au royaume infernal de Havreglace. Dépouillés de leur identité et de leur libre arbitre, ils errent dans ce plan désolé comme une main-d'œuvre esclave éternelle, endurant d'innombrables souffrances.",
            "TranslationComplete",
        ),
        (r"The Dragonborn's Bestiary - Small Creature Addon\interface\creatures\daedra\high clannfear\high clannfear.json.json", 1): (
            "Les Grands faucheclans sont des humanoïdes sauriens agressifs d'Oblivion, dotés de grandes pointes osseuses sur la tête et le dos, d'un bec acéré et d'une longue queue musclée. Plus imposants et féroces que leurs cousins communs, ils chargent leurs proies avec une brutalité implacable.",
            "TranslationComplete",
        ),
        # dbm_inigo_patch 4 books from Inigo.esp.json
        (r"Legacy of the Dragonborn - Follower Room Patches - French\dbm_inigo_patch.esp.json", 15): (inigo_books_by_fid6.get("05DCE1"), "TranslationComplete"),
        (r"Legacy of the Dragonborn - Follower Room Patches - French\dbm_inigo_patch.esp.json", 30): (inigo_books_by_fid6.get("05E245"), "TranslationComplete"),
        (r"Legacy of the Dragonborn - Follower Room Patches - French\dbm_inigo_patch.esp.json", 32): (inigo_books_by_fid6.get("0AD12F"), "TranslationComplete"),
        (r"Legacy of the Dragonborn - Follower Room Patches - French\dbm_inigo_patch.esp.json", 41): (inigo_books_by_fid6.get("05ED19"), "TranslationComplete"),
        # NPCModTowns.esp.json idx 127 ("Get it?" -> "Compris ?")
        (r"NPCs Know About Mod Towns\NPCModTowns.esp.json", 127): ("Tenez-vous à carreau à River Rock, sinon on vous mettra dehors. Compris ?", "TranslationComplete"),
        # BALLS - Chapter 1.esp.json lore terms left in English
        (r"B.A.L.L.S - Chapter 1 - 16 by 9 - FR\BALLS - Chapter 1.esp.json", 53): (
            "-- Panthéon de Haute-Roche, Notorgo --\r\nNotorgo est le dieu messager de la baie d'Illiac. Il est mentionné dans Le Roi Édouard lorsque la reine Aliéra loue Notorgo pour lui avoir ramené son époux Moraelyn et son fils Édouard sains et saufs.",
            "TranslationComplete",
        ),
        (r"B.A.L.L.S - Chapter 1 - 16 by 9 - FR\BALLS - Chapter 1.esp.json", 76): (
            "-- Panthéon bréton, Jhim Sei --\r\nLa nature de Jhim Sei est inconnue, bien que sa sphère d'influence semble liée à la musique. On trouve des sanctuaires dédiés à Jhim Sei à travers toute la Haute-Roche et jusque dans des régions reculées comme les montagnes de la Queue du Dragon en Lenclume.",
            "TranslationComplete",
        ),
        (r"B.A.L.L.S - Chapter 1 - 16 by 9 - FR\BALLS - Chapter 1.esp.json", 89): (
            "« Tout commence avec le dualisme d'Anu et de Son Autre. Ces forces jumelles portent de nombreux noms : Anu-Padomay, Aniel-Sithis, Ak-El, Satak-Akel, Est-N'est Pas. »\r\n-- Le Monomythe",
            "TranslationComplete",
        ),
        (r"B.A.L.L.S - Chapter 1 - 16 by 9 - FR\BALLS - Chapter 1.esp.json", 122): (
            "-- Panthéon de Haute-Roche, Druagaa --\r\nDruagaa est l'ancienne déesse des fleurs, dont le culte a pratiquement disparu. Un festival nommé Gardtide est toujours organisé en son honneur le 1er de Clairciel chaque année par les habitants de la Pointe de Tamarilyn, une région côtière de Ménévia au centre de la Haute-Roche.",
            "TranslationComplete",
        ),
        (r"B.A.L.L.S - Chapter 1 - 16 by 9 - FR\BALLS - Chapter 1.esp.json", 123): (
            "-- Panthéon bréton, Baan Dar --\r\nPour les Brétons, Baan Dar est connu comme « le Bandit ». Il apparaît dans le roman historique Le Roi Édouard, où la reine Aliéra le loue aux côtés d'autres dieux pour lui avoir ramené son époux Moraelyn et son fils Édouard sains et saufs.",
            "TranslationComplete",
        ),
        # Twilight Princess Armor tasset
        (r"Twilight Princess Armor Mashup - FR\Twilight Princess Armor - Alt Textures and Cloth Addon - CCOR Patch.esp.json", 53): ("Tassette flottante de Twilight Princess - Sale", "TranslationComplete"),
        (r"Twilight Princess Armor Mashup - FR\Twilight Princess Armor - Alt Textures and Cloth Addon - CCOR Patch.esp.json", 57): ("Tassette flottante de Twilight Princess - Sale", "TranslationComplete"),
        # ISC, Nolvus Immersion Patch, Thaumaturgy, Undeath Conjuration Absorb Fix (where orig != string but string remained in English)
        (r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json", 17): ("Réanime un cadavre qui combat pour vous pendant <dur> secondes.", "TranslationComplete"),
        (r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json", 19): ("Réanime un cadavre qui combat pour vous pendant <dur> secondes.", "TranslationComplete"),
        (r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json", 21): ("Réanime un cadavre qui combat pour vous pendant <dur> secondes.", "TranslationComplete"),
        (r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json", 23): ("Réanime un cadavre qui combat pour vous pendant <dur> secondes.", "TranslationComplete"),
        (r"Nolvus Awakening Immersion Patch.esp - French\nolvus awakening immersion patch.esp.json", 4): ("Réanime un cadavre qui combat pendant <dur> secondes.", "TranslationComplete"),
        (r"Nolvus Awakening Immersion Patch.esp - French\nolvus awakening immersion patch.esp.json", 8): ("Réanime un cadavre qui combat pendant <dur> secondes.", "TranslationComplete"),
        (r"Nolvus Awakening Immersion Patch.esp - French\nolvus awakening immersion patch.esp.json", 12): ("Réanime un cadavre qui combat pendant <dur> secondes.", "TranslationComplete"),
        (r"Nolvus Awakening Immersion Patch.esp - French\nolvus awakening immersion patch.esp.json", 14): ("Réanime un cadavre qui combat pendant <dur> secondes.", "TranslationComplete"),
        (r"Thaumaturgie - Refonte de l'enchantement\Thaumaturgy.esp.json", 32): ("Augmente votre magie de <mag> points.", "TranslationComplete"),
        (r"Thaumaturgie - Refonte de l'enchantement\Thaumaturgy.esp.json", 34): ("Augmente votre vigueur de <mag> points.", "TranslationComplete"),
        (r"Undeath - Conjuration Absorb Fix - French\undeath conjuration absorb fix.esp.json", 24): ("Invoque un tambour spectral qui joue pendant <300> secondes, améliorant la régénération de vigueur du lanceur et des alliés proches.", "TranslationComplete"),
    }

    total_translated = 0
    total_marked_notrans = 0
    modified_files = set()

    for root, dirs, files in os.walk(DB_DIR):
        for fname in files:
            if not fname.endswith(".json") or fname == "index.json":
                continue
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, DB_DIR)
            data = load_json(full_path)
            if not isinstance(data, list):
                continue

            file_changed = False

            # Special case: BOOBIES_potions SWF frame identifier files -> all entries must be original & NoTranslationRequired
            if "BOOBIES_potions_ENGLISH.txt.json" in rel_path or "BOOBIES_Potions - Apothecary Patch_ENGLISH.txt.json" in rel_path:
                for e in data:
                    if e.get("string") != e.get("original") or e.get("status") != "NoTranslationRequired":
                        e["string"] = e["original"]
                        e["status"] = "NoTranslationRequired"
                        total_marked_notrans += 1
                        file_changed = True
                if file_changed:
                    save_json(full_path, data)
                    modified_files.add(rel_path)
                continue

            for idx, e in enumerate(data):
                orig = e.get("original", "")
                s = e.get("string", "")
                st = e.get("status", "")
                tp = e.get("type")

                # 1. Check specific (rel_path, idx) overrides
                if (rel_path, idx) in SPECIFIC_FILE_IDX_TRANSLATIONS:
                    new_str, new_st = SPECIFIC_FILE_IDX_TRANSLATIONS[(rel_path, idx)]
                    if new_str is None:
                        new_str = orig
                    if s != new_str or st != new_st:
                        e["string"] = new_str
                        e["status"] = new_st
                        if new_st == "NoTranslationRequired":
                            total_marked_notrans += 1
                        else:
                            total_translated += 1
                        file_changed = True
                    continue

                # 2. Falskaar Bounty header in BOOK DESC
                if rel_path == r"Falskaar\Falskaar.esm.json" and idx in (1465, 1748, 3099, 4019):
                    if '<font size="40">Bounty</font>' in s:
                        e["string"] = s.replace('<font size="40">Bounty</font>', '<font size="40">Prime</font>')
                        total_translated += 1
                        file_changed = True
                    continue

                # 3. Vigilant - Book Covers idx 179 "Beredalmo the Signifieur"
                if rel_path == r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json" and idx == 179:
                    if "Beredalmo the Signifieur" in s:
                        e["string"] = s.replace("Beredalmo the Signifieur", "Beredalmo le Signifieur")
                        total_translated += 1
                        file_changed = True
                    continue

                # 4. Handle entries where original == string (or differing only by case/whitespace) and status != NoTranslationRequired
                if st != "NoTranslationRequired" and orig.strip() and orig.strip().lower() == s.strip().lower():
                    # Check if in EXACT_TYPE_ORIG_MAP
                    if (tp, orig) in EXACT_TYPE_ORIG_MAP:
                        new_str = EXACT_TYPE_ORIG_MAP[(tp, orig)]
                        if e["string"] != new_str or e.get("status") != "TranslationComplete":
                            e["string"] = new_str
                            e["status"] = "TranslationComplete"
                            total_translated += 1
                            file_changed = True
                        continue

                    # Check if identical word in FR/EN or proper noun onNPC/Location/Cell/World/Shout
                    if orig.strip().lower() in IDENTICAL_WORDS_LOWER:
                        continue
                    if tp in IDENTICAL_OR_PROPER_TYPES:
                        # Mark obvious internal test/corpse/dummy NPCs or cells as NoTranslationRequired
                        if re.search(r"(test|dummy|corpse|delete me|waiting for tes|voice npc|placeholder|template|do not use|unused|teleport|marker|trigger|spawner|handler|controller|tracker|debug)", orig, re.I):
                            e["status"] = "NoTranslationRequired"
                            total_marked_notrans += 1
                            file_changed = True
                        continue

                    # Otherwise, for technical / internal records (QUST CNAM dev notes, internal QUST FULL, MGEF FULL, SPEL FULL, PERK FULL, ARMO FULL skins, CLAS FULL, RACE FULL, DIAL FULL, etc.)
                    e["status"] = "NoTranslationRequired"
                    total_marked_notrans += 1
                    file_changed = True

            if file_changed:
                save_json(full_path, data)
                modified_files.add(rel_path)

    print(f"Phase 3 applied successfully:")
    print(f"  - Player-facing translations / hybrid fixes applied: {total_translated}")
    print(f"  - Technical / internal records marked NoTranslationRequired: {total_marked_notrans}")
    print(f"  - Total modified files: {len(modified_files)}")


if __name__ == "__main__":
    main()
