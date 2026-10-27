import json

path = "data/user/database/french/Sunthgat/Sunthgat.esp.json"
with open(path, "r", encoding="utf-8") as f:
    entries = json.load(f)

# Define improved translations mapping
# We will identify entries by (form_id, type) or editor_id or index
revised = {}

# 0: Chest -> Coffre (Identique)
# 1: Suspicious Crate -> Caisse suspecte (was: Caisse douteuse)
revised["050293E3|Sunthgat.esp", "MISC FULL"] = "Caisse suspecte"

# 2: Greatsword of Sister Hawk -> Espadon de Sœur Faucon (was: Espadon de la Soeur du Faucon)
revised["05029401|Sunthgat.esp", "WEAP FULL"] = "Espadon de Sœur Faucon"

# 3: Gamrik -> Gamrik
# 4: Aberlin Fox-Hide -> Aberlin Peau-de-Renard
# 5: Aberlin -> Aberlin
# 6: Gamrath -> Gamrath
# 7: Helrun -> Helrun
# 8: Wendela -> Wendela
# 9: Larunon -> Larunon
# 10: Key to Helrun's House -> Clé de la maison d'Helrun
# 11: Hall of the Dead Key -> Clé de la nécropole (ou Clé de la nécropole de Sunthgat)
revised["05005BA2|Sunthgat.esp", "KEYM FULL"] = "Clé de la nécropole de Sunthgat"

# 12: Clever Man's Cauldron Key -> Clé du Chaudron de l'érudit (was: Clé du Chaudron futé)
revised["0500AD45|Sunthgat.esp", "KEYM FULL"] = "Clé du Chaudron de l'érudit"

# 13: Clever Man's Cauldron -> Le Chaudron de l'érudit (was: Le Chaudron futé)
revised["05005B40|Sunthgat.esp", "CELL FULL"] = "Le Chaudron de l'érudit"

# 14: Hall of the Dead -> Nécropole de Sunthgat (was: Nécropole de Sunthgat)
revised["05005B41|Sunthgat.esp", "CELL FULL"] = "Nécropole de Sunthgat"

# 15: Hanged Man Inn -> Auberge du Pendu
# 16: Helrun's House -> Maison d'Helrun
# 17: Skyrim -> Bordeciel
# 18: Sunthgat -> Sunthgat

# 19: I have mammoth tusks to sell. -> J'ai des défenses de mammouth à vendre.
# 20: My partners will be pleased. -> Mes partenaires seront ravis. (was: Mes partenaires seront ravis !)
revised["05014FDB|Sunthgat.esp", "INFO NAM1", 0] = "Mes partenaires seront ravis."
# 21: Here is your share. -> Voici votre part.
revised["05014FDB|Sunthgat.esp", "INFO NAM1", 1] = "Voici votre part."

# 22: I have some skooma to sell. -> J'ai du skooma à vendre.
# 23: My partners will be pleased. -> Mes partenaires seront ravis.
revised["050293E1|Sunthgat.esp", "INFO NAM1", 0] = "Mes partenaires seront ravis."
# 24: Here is your share. -> Voici votre part.
revised["050293E1|Sunthgat.esp", "INFO NAM1", 1] = "Voici votre part."

# 25: How's business up here? -> Comment vont les affaires par ici ? (was: Comment vont les affaires ?)
revised["050293E5|Sunthgat.esp", "DIAL FULL"] = "Comment vont les affaires par ici ?"

# 26: Not many patrons, but there are other sources of income. -> Peu de clients, mais j'ai d'autres sources de revenus. (was: Peu de clients, mais on trouve d'autres sources de revenus.)
revised["050293EE|Sunthgat.esp", "INFO NAM1", 0] = "Peu de clients, mais j'ai d'autres sources de revenus."

# 27: Interested in recovering some stolen goods? -> Récupérer des marchandises volées, ça vous intéresse ? (was: Récupérer des biens volés, ça vous intéresse ?)
revised["050293EE|Sunthgat.esp", "INFO NAM1", 1] = "Récupérer des marchandises volées, ça vous intéresserait ?"

# 28: What do you need? -> De quoi avez-vous besoin ? (was: Que voulez-vous ?)
revised["050293E6|Sunthgat.esp", "DIAL FULL"] = "De quoi avez-vous besoin ?"

# 29: A former associate of mine thought it would be a good idea to disappear with a crate that belongs to me.
# was: Un de mes anciens associés a pensé que ce serait une bonne idée de disparaître avec une caisse qui m'appartient.
# Better: L'un de mes anciens associés s'est mis en tête de disparaître avec une caisse qui m'appartient.
revised["050293EF|Sunthgat.esp", "INFO NAM1", 0] = "L'un de mes anciens associés s'est mis en tête de disparaître avec une caisse qui m'appartient."

# 30: I want that crate back. I'll show you where to find it.
# was: Je veux récupérer cette caisse. Je vais vous montrer où la trouver.
# Better: Je veux récupérer cette caisse. Je vais vous indiquer où la trouver.
revised["050293EF|Sunthgat.esp", "INFO NAM1", 1] = "Je veux récupérer cette caisse. Je vais vous indiquer où la trouver."

# 31: Not my line of work. -> Ce genre de travail ne m'intéresse pas. (was: Ce n'est pas mon affaire.)
revised["050293E7|Sunthgat.esp", "DIAL FULL"] = "Ce n'est pas dans mes cordes."

# 32: Is there anything else you need? -> Avez-vous besoin d'autre chose ? (Good)

# 33: About that retrieval job. -> À propos de cette caisse à récupérer... (was: À propos de cette affaire de bien volés... [avec faute d'accord])
revised["050293E9|Sunthgat.esp", "DIAL FULL"] = "À propos de cette caisse à récupérer..."

# 34: Ready to get going? -> Vous êtes prêt à partir ? (was: On se met en route ? [Gamrik ne vient pas avec le joueur !])
revised["050293F1|Sunthgat.esp", "INFO NAM1"] = "Vous êtes prêt à partir ?"

# 35: I got your crate. -> J'ai récupéré votre caisse. (Good)

# 36: Here, take this. -> Tenez, c'est pour vous. (Good)

# 37: If you get your hands on any mammoth tusks or skooma, I'm your man.
# was: Si vous mettez la main sur des défenses de mammouth ou du skooma, je suis votre homme. (Good)

# 38: The innkeeper from Sunthgat tasked me with the retrieval of this crate.
# was: L'aubergiste de Sunthgat m'a demandé de récupérer cette caisse. (Good)

# 39: You better forget about this. -> Vous feriez mieux d'oublier tout ça. (was: Vous feriez mieux d'oublier ça.)
revised["050293F3|Sunthgat.esp", "INFO NAM1", 0] = "Vous feriez mieux d'oublier tout ça."

# 40: Take this coin and I will take care of the rest.
# was: Prenez cette pièce et je m'occuperai du reste. (Coin = de l'or/argent, pas 1 seule pièce !)
revised["050293F3|Sunthgat.esp", "INFO NAM1", 1] = "Prenez cet or et je m'occupe du reste."

# 41: A war axe, huh? Have you always been a priest?
# was: Une hache de guerre ? Avez-vous toujours été prêtre ? (Wendela est une femme / prêtresse !)
revised["050293F7|Sunthgat.esp", "DIAL FULL"] = "Une hache d'armes, hein ? Vous avez toujours été prêtresse ?"

# 42: I used to be part of a mercenary group. Not your average bandit rabble. We fought with honor. The Band of Kyne they called us.
# was: Avant, je faisais partie d'un groupe de mercenaires. Mais nous n'étions pas de vulgaires bandits ! Nous nous battions avec honneur. On nous appelait la bande de Kyne.
revised["050293FE|Sunthgat.esp", "INFO NAM1", 0] = "Jadis, je faisais partie d'une compagnie de mercenaires. Rien à voir avec de vulgaires bandits. Nous nous battions avec honneur. On nous appelait la Bande de Kyne."

# 43: But it has been almost three decades since then. We were betrayed by one of our own. Larunon, an elven mage. Not surprising.
# was: Mais c'était il y a presque trois décennies. Nous avons été trahis par l'un des nôtres. Larunon, un mage elfique. Pas étonnant...
revised["050293FE|Sunthgat.esp", "INFO NAM1", 1] = "Mais cela remonte à près de trente ans. Nous avons été trahis par l'un des nôtres : Larunon, un mage elfe. Rien de très surprenant..."

# 44: Everyone was dead. Except for that bastard and me. Continued to work as a mercenary for a while. But someday I couldn't do it anymore.
# was: Tout le monde était mort. Sauf ce félon et moi. Nous avons continué à travailler comme mercenaires pendant un certain temps. Mais un jour, je me suis rendue compte que je ne pouvais plus le faire. (GROS CONTRESENS sur le 'Nous')
revised["050293FE|Sunthgat.esp", "INFO NAM1", 2] = "Tout le monde est mort. Tous, sauf ce bâtard et moi. J'ai continué à louer mon épée comme mercenaire pendant un temps, mais un jour, je n'ai plus pu supporter tout ça."

# 45: Met an old priest up here and chose to assist him. He passed away of old age and I carried on his work.
# was: J'ai rencontré un vieux prêtre dans ce village et j'ai choisi de l'aider. Puis il est décédé, et j'ai continué son travail.
revised["050293FE|Sunthgat.esp", "INFO NAM1", 3] = "J'ai rencontré un vieux prêtre ici même et j'ai choisi de l'aider. Il s'est éteint de vieillesse, et j'ai perpétué son œuvre."

# 46: What is with Larunon. You don't want to avenge your dead friends?
# was: Que se passe-t-il avec Larunon ? Vous ne voulez pas venger vos camarades ?
revised["050293F8|Sunthgat.esp", "DIAL FULL"] = "Et pour Larunon ? Vous ne voulez pas venger vos compagnons ?"

# 47: I tried to track him down every now and then, before I settled down here. But he was always gone when i thought I got him.
# was: J'ai quelquefois essayé de retrouver sa trace avant de m'installer ici. Mais à chaque fois que je pensais avoir remis la main sur lui, il avait déjà filé.
revised["050293FF|Sunthgat.esp", "INFO NAM1", 0] = "J'ai bien essayé de le traquer de temps à autre, avant de m'établir ici. Mais chaque fois que je pensais le tenir, il m'échappait."

# 48: Last I heard he joined some coven. But I just don't want to fuel this hatred anymore...
# was: Aux dernières nouvelles, il a rejoint un cercle de mages. Mais je ne veux plus alimenter ma haine envers lui...
revised["050293FF|Sunthgat.esp", "INFO NAM1", 1] = "Aux dernières nouvelles, il aurait rejoint un convent de sorciers. Mais je ne veux plus entretenir cette haine..."

# 49: Larunon is dead. -> Larunon est mort. (Good)

# 50: I don't know how to feel about this. He was the only other one who could remember our golden days.
# was: Je ne sais pas trop qu'en penser. Il était le seul à pouvoir se souvenir de nos beaux jours.
revised["05029400|Sunthgat.esp", "INFO NAM1", 0] = "Je ne sais pas trop quoi en penser. C'était le seul autre témoin de nos jours de gloire."

# 51: But I guess all things have to come to an end. Take this sword. It belonged to our leader. Please remember me and also the Band of Kyne.
# was: Mais je suppose que toutes les bonnes choses ont une fin. Prenez cette épée. Elle appartenait à notre chef. Je vous en prie, souvenez-vous de moi et de la bande de Kyne.
revised["05029400|Sunthgat.esp", "INFO NAM1", 1] = "Mais toute chose a une fin, je suppose. Prenez cette épée : elle appartenait à notre meneuse. Ne m'oubliez pas, et n'oubliez pas la Bande de Kyne."

# 52: Do you need any help? -> Avez-vous besoin d'aide ? (was: Vous avez besoin d'aide ?)
revised["05029404|Sunthgat.esp", "DIAL FULL"] = "Avez-vous besoin d'aide ?"

# 53: How nice of you to ask. You look like you could indeed help me.
# was: C'est gentil à vous de me le demander. Vous semblez pouvoir m'aider !
revised["05029407|Sunthgat.esp", "INFO NAM1", 0] = "C'est aimable à vous de demander. Vous avez l'air de quelqu'un qui pourrait effectivement m'être utile."

# 54: I'm looking for a rare spell tome. It contains the knowledge of a rune that triggers an unbridled rage.
# was: Je cherche un rarissime livre de sort. Grâce à cet artéfact, il est possible de libérer une rune qui déclenche une rage effrénée !
revised["05029407|Sunthgat.esp", "INFO NAM1", 1] = "Je cherche un livre de sorts très rare. Il renferme les secrets d'une rune capable de déclencher une fureur incontrôlable."

# 55: There is a rumor that one copy is hidden in Shriekwind Bastion to the south.
# was: Une rumeur affirme qu'une copie est cachée dans le bastion de Hurlevent, au sud d'ici.
revised["05029407|Sunthgat.esp", "INFO NAM1", 2] = "La rumeur veut qu'un exemplaire soit dissimulé au Bastion de Hurlevent, vers le sud."

# 56: But beware, if you intend to recover it. The place is overrun by vampires.
# was: Mais prenez garde si vous avez l'intention de le récupérer. L'endroit grouille de vampires.
revised["05029407|Sunthgat.esp", "INFO NAM1", 3] = "Mais prenez garde si vous comptez le récupérer : les vampires ont envahi les lieux."

# 57: I got your spell tome. -> J'ai trouvé votre livre de sorts. (was: J'ai votre livre de sort.)
revised["05029406|Sunthgat.esp", "DIAL FULL"] = "J'ai votre livre de sorts."

# 58: So it really existed? That's good to know. Please keep the book and also take this potion as your reward.
# was: Donc, il existe vraiment ? C'est bon à savoir ! Gardez le livre et prenez cette potion comme récompense.
revised["05029408|Sunthgat.esp", "INFO NAM1"] = "Il existait donc réellement ? C'est bon à savoir. Gardez l'ouvrage, et acceptez cette potion en guise de récompense."

# 59: Expected Betrayal -> Trahison prévisible (was: Trahison escomptée)
revised["0500FED6|Sunthgat.esp", "QUST FULL"] = "Trahison prévisible"

# 60: Get the crate from <Alias=BanditCamp> -> Récupérez la caisse à <Alias=BanditCamp> (was: Trouvez la caisse à cet endroit : <Alias=BanditCamp>)
revised["0500FED6|Sunthgat.esp", "QUST NNAM", 0] = "Récupérez la caisse à <Alias=BanditCamp>"

# 61: Return the crate to Gamrik or a Falkreath Guard -> Rapportez la caisse à Gamrik ou à un garde d'Épervine
revised["0500FED6|Sunthgat.esp", "QUST NNAM", 1] = "Rapportez la caisse à Gamrik ou à un garde d'Épervine"

# 62: Mammoth Tusk and Skooma -> Défenses de mammouth et skooma (was: Des défenses de mammouth et du skooma)
revised["0500FED3|Sunthgat.esp", "QUST FULL"] = "Défenses de mammouth et skooma"

# 63: The Clever Craft -> L'art des mages (was: Art savant)
revised["0500FED5|Sunthgat.esp", "QUST FULL"] = "L'art des mages"

# 64: Get the spell tome from Shriekwind Bastion -> Récupérez le livre de sorts au Bastion de Hurlevent (was: Trouvez le livre de sort au Bastion de Hurlevent)
revised["0500FED5|Sunthgat.esp", "QUST NNAM", 0] = "Récupérez le livre de sorts au Bastion de Hurlevent"

# 65: Deliver the spell tome to Aberlin -> Rapportez le livre de sorts à Aberlin (was: Rapportez le livre de sort à Aberlin)
revised["0500FED5|Sunthgat.esp", "QUST NNAM", 1] = "Rapportez le livre de sorts à Aberlin"

# 66: Golden Days -> Jours de gloire (was: Jours dorés)
revised["0500FED4|Sunthgat.esp", "QUST FULL"] = "Jours de gloire"

# 67: Try to find Larunon at <Alias=WarlockLair> -> Retrouvez Larunon à <Alias=WarlockLair> (was: Trouvez Larunon à l'endroit suivant : <Alias=WarlockLair>)
revised["0500FED4|Sunthgat.esp", "QUST NNAM", 0] = "Retrouvez Larunon à <Alias=WarlockLair>"

# 68: Return to Wendela -> Retournez voir Wendela (Good)
revised["0500FED4|Sunthgat.esp", "QUST NNAM", 1] = "Retournez voir Wendela"

# 69: Helgrun's House -> Maison d'Helrun
revised["050008FA|Sunthgat.esp", "LCTN FULL"] = "Maison d'Helrun"

# 70: Hall of the Dead -> Nécropole de Sunthgat
revised["05005B3F|Sunthgat.esp", "LCTN FULL"] = "Nécropole de Sunthgat"

# 71: Hanged Man Inn -> Auberge du Pendu
revised["050008FB|Sunthgat.esp", "LCTN FULL"] = "Auberge du Pendu"

# 72: Clever Man's Cauldron -> Le Chaudron de l'érudit (was: Le Chaudron futé)
revised["05005B3E|Sunthgat.esp", "LCTN FULL"] = "Le Chaudron de l'érudit"

# 73: Sunthgat -> Sunthgat
revised["05000874|Sunthgat.esp", "LCTN FULL"] = "Sunthgat"

print("Done defining mapping.")
