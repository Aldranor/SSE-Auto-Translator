import json
from pathlib import Path

esm_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")
txt_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/interface/translations/legacyofthedragonborn_french.txt.json")

with open(esm_file, "r", encoding="utf-8") as f:
    esm_data = json.load(f)

with open(txt_file, "r", encoding="utf-8") as f:
    txt_data = json.load(f)

# Load existing prepared translations if present
translations = {}

# 1. Maps & Books Titles
for i in range(11, 26):
    r = ["XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV"][i-11]
    translations[f"Treasure Map {r}"] = f"Carte au trésor {r}"
translations["Treasure Map VI"] = "Carte au trésor VI"
translations["Treasure Map IX"] = "Carte au trésor IX"
translations["Black Book"] = "Livre noir"

# 2. Objects, Cells, Doors, Keys, Races
translations["Dwemer Junk"] = "Bric-à-brac dwemer"
translations["Wooly Mammoth"] = "Mammouth laineux"
translations["Coral"] = "Corail"
translations["Ivory"] = "Ivoire"
translations["Wanderlust (replica)"] = "Soif d'errance (réplique)"
translations["Raptor"] = "Raptor"
translations["Merrian's Sack"] = "Sac de Merrian"
translations["Barrel of Jars"] = "Tonneau de bocaux"
translations["Debug Portal"] = "Portail de débogage"
translations["Enable/Disable"] = "Activer/Désactiver"
translations["Hidden Wall"] = "Mur secret"
translations["Key to Dragonborn Gallery"] = "Clé de la galerie de l'Enfant de dragon"
translations["Riften Fishery"] = "Pêcherie de Faillaise"

# 3. Interface & Messages
translations["You must set a heading first."] = "Vous devez d'abord définir un cap."
translations["The Dev Aveza is currently travelling to <Alias=Current>. I can't change it's course until it arrives."] = "Le Dev Aveza voyage actuellement vers <Alias=Current>. Vous ne pouvez pas modifier son cap avant son arrivée."
translations["When I hold the beacon I can feel a link to another device, but it does nothing.\r\n"] = "Lorsque je tiens la balise, je sens un lien avec un autre appareil, mais rien ne se produit.\r\n"
translations["I should probably stand clear of the airship as it departs!"] = "Je devrais sans doute m'écarter du vaisseau volant lors de son départ !"
translations["The Dev Aveza will arrive at <Alias=Current> in %.0f hours."] = "Le Dev Aveza arrivera à <Alias=Current> dans %.0f heures."
translations["The Dev Aveza has arrived at <Alias=Current>."] = "Le Dev Aveza est arrivé à <Alias=Current>."
translations["The Dev Aveza can be docked at several key locations around Tamriel including the hold capitals of Skyrim and the Dragonborn Gallery. Each journey on board the Dev Aveza will take 4 hours to complete. As you continue on your advertures more stops will be unlocked. "] = "Le Dev Aveza peut accoster à plusieurs endroits clés de Tamriel, notamment les capitales de châtelleries de Bordeciel et la Galerie de l'Enfant de dragon. Chaque trajet à bord du Dev Aveza dure 4 heures. Au fil de vos aventures, d'autres escales seront déverrouillées."
translations["The Dev Aveza is already docked at <Alias=Current>."] = "Le Dev Aveza est déjà amarré à <Alias=Current>."
translations["What type of supply would you like to order?"] = "Quel type de fournitures souhaitez-vous commander ?"
translations["Ingots/Gems"] = "Lingots/Gemmes"
translations["Leather/hide etc"] = "Cuir/Peaux etc."
translations["Food/Drink"] = "Nourriture/Boisson"
translations["Check Orders"] = "Consulter les commandes"
translations["All displayable items added to your inventory, ya cheater! "] = "Tous les objets exposables ont été ajoutés à votre inventaire, sale tricheur !"
translations["This key gives access to the debug room in the Storeroom. It is strongly recommend you do not tinker with the controls found there unless you know exactly what you're doing!"] = "Cette clé donne accès à la salle de débogage dans la réserve. Il est fortement déconseillé de toucher aux commandes qui s'y trouvent, à moins de savoir exactement ce que vous faites !"

# 4. Dialogue replies
translations["Yes, hmmm, well, sad to say, this is just a single variety of pure ore with nothing else in it. Sorry."] = "Oui, hmm, ma foi, au regret de vous le dire, ce n'est qu'un simple minerai ordinaire sans rien d'autre d'intéressant. Désolé."
translations["There you go. If you have any more you want looked at, just let me know."] = "Et voilà. Si vous en avez d'autres à faire examiner, faites-le-moi savoir."

# 5. Dialogue topics
translations["I need to borrow the Spear of the Snow Prince"] = "J'ai besoin d'emprunter la Lance du Prince des neiges."
translations["Where did you say you found that spear?"] = "Où avez-vous dit que vous aviez trouvé cette lance ?"
translations["Do you know where the ruins in the book could be?"] = "Savez-vous où pourraient se trouver les ruines mentionnées dans le livre ?"
translations["What can you tell me about the relics you found?"] = "Que pouvez-vous me dire sur les reliques que vous avez trouvées ?"
translations["I found an ancient shield in Fort Pale Pass."] = "J'ai trouvé un bouclier antique au fort du Col pâle."
translations["I have the setting to the Amulet of Kings"] = "J'ai la monture de l'Amulette des rois."
translations["Have you found out anything about the amulet and shield?"] = "Avez-vous appris quelque chose sur l'amulette et le bouclier ?"
translations["Here's the fragmented Amulet of Kings and the Shield of Reman"] = "Voici l'Amulette des rois fragmentée et le Bouclier de Reman."
translations["I've found Zurin Arctus' Ring"] = "J'ai trouvé l'anneau de Zurin Arctus."
translations["Any leads on the Lord's Mail or Wulfharth's tomb?"] = "Des pistes sur l'Armure du Seigneur ou la tombe de Wulfharth ?"
translations["I have all three relics"] = "J'ai les trois reliques."
translations["I have the relics and the Lord's Mail"] = "J'ai les reliques et l'Armure du Seigneur."
translations["What can you tell me about the Falmer ruins?"] = "Que pouvez-vous me dire sur ces ruines falmers ?"
translations["What can you tell me about this temple?"] = "Que pouvez-vous me dire sur ce temple ?"
translations["Let's talk about the Snow Elves."] = "Parlons des Elfes des neiges."
translations["Let's head back to the museum."] = "Retournons au Musée."
translations["Have you had any luck translating the Falmer tome?"] = "Avez-vous réussi à traduire le tome falmer ?"
translations["I'm ready to head to the Glacial Crevice."] = "Je suis prêt à me rendre dans la Faille glaciaire."
translations["We should make camp here."] = "Nous devrions établir notre camp ici."
translations["Tell me about this shrine to Phynaster."] = "Parlez-moi de cet autel de Phynaster."
translations["We did it. Neb-Crescen is ours."] = "Nous avons réussi. Neb-Crescen est à nous."
translations["Other Locations"] = "Autres destinations"
translations["Stay here"] = "Rester ici"

for city in ["Solitude", "Whiterun", "Windhelm", "Falkreath", "Markarth", "Riften", "Winterhold", "Dawnstar", "Rorikstead", "High Hrothgar", "Castle Volkihar", "Deepholme", "Fort Dawnguard", "Karagas Tower", "Labryinthian", "Raven Rock", "Tel Mithryn", "Temple of Miraak", "Pale Pass"]:
    translations[f"<Alias={city}>"] = f"<Alias={city}>"

# 6. Quest Names
translations["Shattered Legacy"] = "L'Héritage brisé"
translations["Museum Startup"] = "Lancement du Musée"
translations["Kegbreaker Effect Tracker"] = "Suivi de l'effet du Brise-baril"
translations["Ruins of Rkund"] = "Les ruines de Rkund"
translations["Field Station - Falkreath"] = "Poste de terrain - Épervine"
translations["Field Station - The Reach"] = "Poste de terrain - La Crevasse"
translations["Field Station - The Pale"] = "Poste de terrain - Le Clos"
translations["Night at the Museum"] = "Une nuit au Musée"
translations["Ongar's Kegbreaker"] = "Le Brise-baril d'Ongar"
translations["The Amulet of Kings"] = "L'Amulette des rois"
translations["The Dragonborn Gallery"] = "La Galerie de l'Enfant de dragon"
translations["Excavation 2 Scene Handler"] = "Gestionnaire de scène - Fouille 2"
translations["MASTER DEBUGGING HANDLER"] = "GESTIONNAIRE PRINCIPAL DE DÉBOGAGE"
translations["Restocks Writing Stuff"] = "Réapprovisionnement du matériel d'écriture"
translations["Malrus' Codex Manager"] = "Gestionnaire du codex de Malrus"
translations["Haunted Museum"] = "Le Musée hanté"
translations["Airship Remote Calling"] = "Appel à distance du vaisseau volant"
translations["Household Planner Menu Handler"] = "Gestionnaire de menu de l'intendance"
translations["Radiant Museum Tour"] = "Visite guidée du Musée"
translations["Airship Navigation"] = "Navigation du vaisseau volant"
translations["Airship Beacon Handler"] = "Gestionnaire de la balise du vaisseau volant"
translations["Museum Display Manager"] = "Gestionnaire des expositions du Musée"
translations["Dragonborn Museum Quest Handler"] = "Gestionnaire des quêtes du Musée"
translations["Relic Tracker"] = "Traqueur de reliques"
translations["Dev Avesa Travel Controls"] = "Commandes de voyage du Dev Aveza"
translations["Ten Septim Tour"] = "La visite à dix septims"
translations["Adding to the Collection"] = "Enrichir la collection"
translations["Holds Utility Function Scripts"] = "Scripts utilitaires du Musée"
translations["Dynamic Checklist"] = "Liste de contrôle dynamique"
translations["Contributors Controller"] = "Contrôleur des donateurs"
translations["Sell Chest Handler"] = "Gestionnaire du coffre de vente"
translations["Sets up thane rewards and levels up weapons"] = "Initialise les récompenses de thane et améliore les armes"
translations["adds luca pick axe to mining tools list"] = "Ajoute la pioche de Luca aux outils de minage"
translations["quartermaster perk handler"] = "Gestionnaire d'atout d'intendant"
translations["Ongar's Kegbreaker Handler."] = "Gestionnaire du Brise-baril d'Ongar"
translations["Exhume Handler"] = "Gestionnaire d'exhumation"
translations["explorer follower handler"] = "Gestionnaire de compagnon explorateur"
translations["Museum Guide count handler"] = "Gestionnaire du décompte des guides du Musée"
translations["doomstone and shrine display handler"] = "Gestionnaire d'exposition des pierres levées et autels"
translations["Legacy of the Dragonborn NPC dialogue"] = "Dialogues des PNJs de l'Héritage de l'Enfant de dragon"
translations["Configuration Menu"] = "Menu de configuration"
translations["adds scales to unique dragons for displays"] = "Ajoute des écailles aux dragons uniques pour l'exposition"
translations["Skaal Delivery Handler"] = "Gestionnaire de livraison skaale"
translations["DBM Radiant Quest Handler"] = "Gestionnaire des quêtes radiantes du Musée"

# 7. Quest Stages
translations["I've gotten the drop on Ezra. I should take her shard and look for clues about why she was here at Fort Pale Pass to begin with."] = "J'ai pris le dessus sur Ezra. Je devrais prendre son fragment et chercher des indices pour comprendre ce qu'elle faisait au fort du Col pâle."
translations["I should see what else of interest Ezra has or bide my time and return her to Argus"] = "Je devrais voir ce qu'Ezra possède d'autre d'intéressant ou attendre le bon moment pour la ramener à Argus."
translations["I've gotten another shard off Ezra. I'll have to decide what to do about her. I can either return to Argus and risk her discovering the missing items, or do something drastic"] = "J'ai récupéré un autre fragment sur Ezra. Je dois décider de son sort : retourner voir Argus au risque qu'elle découvre les objets manquants, ou prendre des mesures radicales."
translations["I've gotten another shard off Ezra. I'll have to decide what to do about her. I can either return to Argus and risk her spilling the beans, or silence her permanently."] = "J'ai récupéré un autre fragment sur Ezra. Je dois décider de son sort : la ramener à Argus au risque qu'elle raconte tout, ou la faire taire définitivement."
translations["I should see what else of interest Ezra has"] = "Je devrais voir ce qu'Ezra possède d'autre d'intéressant."
translations["I located Ezra who is very paranoid that I'm an assassin for some reason. She's reluctantly agreed to follow me, but insists on finding her missing shield before returning to Argus."] = "J'ai localisé Ezra, qui est particulièrement paranoïaque et craint que je ne sois un assassin. Elle a accepté à contrecœur de me suivre, mais insiste pour retrouver son bouclier avant de retourner voir Argus."
translations["I located Ezra who is very paranoid that I'm an assassin for some reason. She's reluctantly agreed to follow me, but insists on finding some item of importance in the dungeon beneath Fort Pale Pass."] = "J'ai localisé Ezra, qui est très méfiante et craint que je ne sois un assassin. Elle a accepté à contrecœur de me suivre, mais insiste pour retrouver un objet précieux dans les cachots sous le fort du Col pâle."
translations["I have found an ancient shield of some kind. Auryen may know more about it. I should track down the rest of the amulet pieces and then return to the museum."] = "J'ai trouvé une sorte de bouclier antique. Auryen en saura peut-être davantage. Je devrais rassembler les morceaux restants de l'amulette avant de retourner au Musée."
translations["I have found an ancient shield of some kind. Auryen may know more about it. I should track down the rest of the amulet pieces using Argus' journal first however."] = "J'ai trouvé une sorte de bouclier antique. Auryen en saura peut-être davantage. Je devrais cependant retrouver le reste des fragments de l'amulette en consultant d'abord le journal d'Argus."
translations["I've parted ways with Ezra, sending her to find Argus on her own while tend to other tasks. I may be able to locate all the pieces on my own."] = "Je me suis séparé d'Ezra, la renvoyant retrouver Argus seule pendant que je m'occupe d'autres tâches. Je pourrais bien retrouver tous les morceaux par moi-même."
translations["I've parted ways with Ezra, sending her to find Argus on her own while tend to other tasks. I may be able to locate all of what they are seeking on my own."] = "Je me suis séparé d'Ezra, la renvoyant retrouver Argus seule pendant que je m'occupe d'autres tâches. Je pourrais bien être en mesure de trouver par moi-même tout ce qu'ils recherchent."
translations["I've found the remains of Ulgarg who met his untimely end in a violent way inside some nordic cave. There seems to be something odd glowing from his gut."] = "J'ai trouvé la dépouille d'Ulgarg, qui a connu une fin violente au fond d'une grotte nordique. Quelque chose d'étrange semble briller dans ses entrailles."
translations["It seems that Ulgarg, in a moment of despiration, swallowed his fragment of the shard to keep it from the enemy. Fortunately I have a strong stomach. I now possess another fragment."] = "Il semble qu'Ulgarg, dans un geste désespéré, ait avalé son fragment pour empêcher l'ennemi de s'en emparer. Heureusement, j'ai l'estomac bien accroché. J'ai désormais un autre fragment en ma possession."
translations["It seems that Ulgarg, in a moment of despiration, swallowed his fragment of the shard to keep it from the enemy. Fortunately it seems to have worked. Luckily the shard began to glow as I approached due to the presence of the other shards. I should head back to Argus."] = "Il semble qu'Ulgarg, dans un geste désespéré, ait avalé son fragment pour empêcher l'ennemi de s'en emparer. Heureusement, cela a fonctionné. Par chance, le fragment s'est mis à briller à mon approche en résonance avec les autres. Je devrais retourner voir Argus."
translations["I managed to recover the setting for the Amulet of Kings. I've managed to gather all the missing fragments and should return to Auryen at the museum to see if he has found a way to reform it."] = "J'ai réussi à récupérer la monture de l'Amulette des rois. J'ai rassemblé tous les fragments manquants et devrais retourner voir Auryen au Musée pour savoir s'il a trouvé un moyen de la reconstituer."
translations["I managed to recover the setting for the Amulet of Kings. I've managed to gather all the missing fragments and should return to Argus to see what the next plan is."] = "J'ai réussi à récupérer la monture de l'Amulette des rois. J'ai rassemblé tous les fragments manquants et devrais retourner voir Argus pour connaître la suite du plan."
translations["Argus and Ezra have double crossed me and paid the price for it. Apparently they were mercenaries hired to finish a job I was caught in the middle of. Now that I have the fragments, I should see Auryen."] = "Argus et Ezra m'ont trahi et en ont payé le prix. C'étaient apparemment des mercenaires engagés pour terminer un contrat dans lequel je me suis retrouvé mêlé. Maintenant que j'ai les fragments, je devrais voir Auryen."
translations["Argus and Ezra have double crossed me and paid the price for it. Apparently they were mercenaries hired to finish a job the Morag Tong were supposed to do. I should take back the shards, setting and ancient shield."] = "Argus et Ezra m'ont trahi et en ont payé le prix. C'étaient apparemment des mercenaires engagés pour accomplir une tâche dévolue à la Morag Tong. Je devrais reprendre les fragments, la monture et le bouclier antique."
translations["Auryen identified the ancient shield I found in Fort Pale Pass as the shield of Reman Cyrodiil, and he indicated that the strange fragment I had found was part of the Amulet of Kings! He suggested I seek out the other fragments."] = "Auryen a identifié le bouclier antique trouvé au fort du Col pâle comme étant le Bouclier de Reman Cyrodiil, et il a confirmé que l'étrange fragment faisait partie de l'Amulette des rois ! Il m'a suggéré de partir en quête des autres fragments."
translations["Auryen identified the ancient shield I found in Fort Pale Pass as the shield of Reman Cyrodiil, and he indicated that the shield resonates with the shards of the amulet. He's told me to return in a day or two so he can research the details."] = "Auryen a identifié le bouclier antique trouvé au fort du Col pâle comme étant le Bouclier de Reman Cyrodiil, et il a remarqué que le bouclier résonnait avec les fragments de l'amulette. Il m'a demandé de revenir d'ici un jour ou deux afin d'étudier les détails."
translations["Auryen should have had time to research the details surrounding the Amulet of Kings and the Shield. I should check back with him and see what he's discovered."] = "Auryen a dû avoir le temps d'étudier les détails concernant l'Amulette des rois et le Bouclier. Je devrais retourner le voir pour découvrir ce qu'il a appris."
translations["Auryen should have had time to research the details surrounding the Amulet of Kings and the Shield. I should check back with him."] = "Auryen a dû avoir le temps d'étudier les détails concernant l'Amulette des rois et le Bouclier. Je devrais retourner le voir."
translations["I have obtained the helm of Tiber Septim but feel as though the dark power binding me here still has hold over me. I should investigate the catacombs further."] = "J'ai obtenu le casque de Tiber Septim, mais je sens que la puissance obscure qui me retient ici a toujours prise sur moi. Je devrais explorer les catacombes plus en profondeur."
translations["I have obtained the helm of Tiber Septim but feel as though the dark power binding me here still has hold over me. I should continue to investigate the source."] = "J'ai obtenu le casque de Tiber Septim, mais je sens que la puissance obscure qui me retient ici a toujours prise sur moi. Je devrais continuer d'enquêter sur la source du mal."
translations["I've defeated Zurin Arctus, the Underking, though the power binding me here seems to remain. Perhaps he has some clue on him."] = "J'ai vaincu Zurin Arctus, le Roi des Tréfonds, mais le pouvoir qui m'emprisonne ici semble persister. Peut-être trouverai-je un indice sur sa dépouille."
translations["I've found a very unique and interesting ring which I should show Auryen, but no other major clues as to why I am still trapped here. I must delve deeper."] = "J'ai trouvé un anneau tout à fait unique et fascinant que je devrais montrer à Auryen, mais aucun autre indice majeur sur les raisons de ma captivité. Je dois m'enfoncer plus profondément."
translations["I've found a very unique and interesting ring which I should show Auryen, but no other major clues as to why I am still bound here. Perhaps his dark influence has corrupted this place and I need to exit the fortress before the Waystone can be removed."] = "J'ai trouvé un anneau tout à fait fascinant que je devrais montrer à Auryen, mais aucun autre indice majeur sur les raisons de ma captivité. Peut-être que son influence maléfique a corrompu ces lieux et que je dois quitter la forteresse avant de pouvoir desceller la pierre de guidage."
translations["I've destroted Ysmir Wulfharth and obtained his boots. I need to get the Lord's Mail before I head back to Sancre Tor. I must search Castle Dour to see where it has gone."] = "J'ai terrassé Ysmir Wulfharth et obtenu ses bottes. Je dois mettre la main sur l'Armure du Seigneur avant de retourner à Sancre Tor. Je dois fouiller Mornétoile pour savoir ce qu'elle est devenue."
translations["I've destroted Ysmir Wulfharth and obtained his boots. I need to get the Lord's Mail before I head back to Sancre Tor. I must have it stashed somewhere."] = "J'ai terrassé Ysmir Wulfharth et obtenu ses bottes. Je dois mettre la main sur l'Armure du Seigneur avant de retourner à Sancre Tor. Elle doit être cachée quelque part."
translations["Sets up regular start and initialises some elements of the mod"] = "Configure le démarrage standard et initialise certains éléments du mod."
translations["Kegbreaker has been drawn, alias will fill to select random tavern."] = "Le Brise-baril a été dégainé, sélection d'une taverne aléatoire."
translations["Kegbreaker removed, recover from effect and stop quest."] = "Brise-baril retiré, récupération de l'effet et arrêt de la quête."
translations["Auryen brought the Spear of the Snow Prince along on the excavation. As a probable devout follower of Trinimac, his spear may be able to open the way into the temple."] = "Auryen a apporté la Lance du Prince des neiges lors de la fouille. En tant que fervent fidèle probable de Trinimac, sa lance pourrait bien nous ouvrir l'accès au temple."
translations["We attempted to overtake and fight Tulrin Deathweaver and his Falmer clan, but he proved to be as formidable as we feared. We were forced to fall back and regroup."] = "Nous avons tenté de surprendre et d'affronter Tulrin Tissetrempe et son clan falmer, mais il s'est avéré aussi redoutable que nous le redoutions. Nous avons été contraints de nous replier pour nous regrouper."
translations["We attempted to overtake and fight Tulrin Deathweaver and his Falmer clan, but he proved to be as formidable as we feared. After overtaking his followers, he fled."] = "Nous avons tenté de surprendre et d'affronter Tulrin Tissetrempe et son clan falmer, mais il s'est avéré aussi redoutable que nous le redoutions. Après avoir vaincu ses sbires, il a pris la fuite."
translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I should scout the designated location in Falkreath."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. Je devrais reconnaître le site désigné à Épervine."
translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I have built the Northern Field Station in Winterhold, I should now return to Marassi to let him know."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. J'ai bâti le poste du Nord à Fortdhiver, je devrais maintenant retourner voir Marassi pour le lui annoncer."
translations["Marassi is ready to get underway on establishing another field station. This time in the Reach. As I have other things to attend to, I should send word to him when I'm ready to assist."] = "Marassi est prêt à fonder un autre poste de terrain, cette fois dans la Crevasse. Comme j'ai d'autres affaires à régler, je devrais lui faire signe dès que je pourrai l'aider."
translations["Marassi is ready to get underway on establishing another field station. This time in the Reach. As I have other things to attend to, I have given him 2000 gold in order to build it for me. It's been a few days and I should check on the progress."] = "Marassi est prêt à fonder un autre poste de terrain, cette fois dans la Crevasse. Comme j'ai d'autres affaires à régler, je lui ai remis 2 000 pièces d'or afin qu'il le construise pour moi. Quelques jours ont passé, je devrais aller voir où en sont les travaux."
translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I should scout the designated location in the Pale."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. Je devrais reconnaître le site désigné dans le Clos."
translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I have built the Eastern Field Station in Eastmarch. I should now return to Marassi to let him know."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. J'ai bâti le poste de l'Est en Estemarche, je devrais maintenant retourner voir Marassi pour le lui annoncer."
translations["The Museum has been robbed! People from Avram's shady past have made off with the contents of the museum, and now we must track down where they've gone!"] = "Le Musée a été cambriolé ! Des individus issus du passé trouble d'Avram ont dérobé les trésors du Musée, et nous devons à présent retrouver leur trace !"
translations["The Museum has been robbed! People from Avram's shady past have made off with the contents of the museum, and now we must head to Windcaller Pass to try and locate them."] = "Le Musée a été cambriolé ! Des individus issus du passé trouble d'Avram ont dérobé les trésors du Musée, et nous devons maintenant nous rendre au défilé d'Ustengrav pour essayer de les localiser."
translations["I had been tasked by Ognar to retrieve his famous warhammer Kegbreaker. After investigating the Nightgate Inn, I've managed to find where it was hidden and claim it."] = "Ongar m'avait chargé de retrouver son fameux marteau de guerre, le Brise-baril. Après avoir fouillé l'auberge de la Porte nocturne, j'ai réussi à mettre la main dessus."
translations["I had been tasked by Ognar to retrieve a hammer to replace his Warhammer of Inebriation, however he died before I could do that. I managed to acquire his hammer anyway. Auryen may know something more about it."] = "Ongar m'avait chargé de retrouver un marteau pour remplacer son Marteau de guerre d'ivresse, mais il est mort avant que je ne puisse le faire. J'ai tout de même réussi à récupérer son marteau. Auryen en saura peut-être plus."
translations["The exploration continues as we delve into the ruins of Rkund. I should meet up with the expedition team inside."] = "L'exploration se poursuit au cœur des ruines de Rkund. Je devrais rejoindre l'équipe d'expédition à l'intérieur."
translations["The team has uncovered an ancient Snow Elf altar. We should investigate it and see if it can shed light on the fate of this fallen civilization."] = "L'équipe a mis au jour un antique autel des Elfes des neiges. Nous devrions l'examiner pour voir s'il peut nous éclairer sur le destin de cette civilisation déchue."
translations["I should check back with the Windcaller Pass excavation and see how the things are progressing."] = "Je devrais retourner voir les fouilles du défilé d'Ustengrav pour vérifier comment les travaux progressent."
translations["The excavation crew continue their dig. I should give them some more time to work and check back later or help them to clear the way."] = "L'équipe de fouille poursuit son déblaiement. Je devrais leur laisser un peu de temps et revenir plus tard, ou les aider à dégager le passage."
translations["I should give the team a few days to work on digging in the new site location, then return and see how they are doing. I can also help out with the digging to make shorter work of it."] = "Je devrais laisser à l'équipe quelques jours pour creuser sur le nouvel emplacement, puis revenir voir leurs progrès. Je peux aussi apporter mon aide au déblaiement pour accélérer les travaux."
translations["While searching the Temple of the Divines I came across a weird looking teddy bear that appears to belong to Freir. When I picked it up a bottle of Skooma fell out of its stuffing. Perhaps I can use it as leverage to get information from her?"] = "En fouillant le temple des Divins, je suis tombé sur un ours en peluche d'allure bizarre qui semble appartenir à Freir. Quand je l'ai ramassé, une fiole de skooma est tombée de son rembourrage. Peut-être pourrais-je m'en servir comme moyen de pression pour lui soutirer des informations ?"
translations["I have found several unusual books concerning the Dwemer but nothing that seems very useful. I should give them to Urag so he knows that this is NOT what I am looking for. Perhaps he will then have some other ideas on where to look."] = "J'ai trouvé plusieurs livres insolites sur les Dwemers, mais rien qui semble vraiment utile. Je devrais les confier à Urag pour qu'il voie que ce n'est PAS ce que je cherche. Peut-être aura-t-il d'autres pistes à me proposer."
translations["Dwemer History and Culture did not have the insights I had hoped for. I should ask Urag again for more leads."] = "L'Histoire et la culture des Dwemers ne m'ont pas apporté les réponses espérées. Je devrais redemander des pistes à Urag."
translations["Urag finally had a clue about some books which ended up being \"borrowed\" by some Synod mage. His assistant Ertzebet confirmed that they had come by and were asking about Mzulft. I should check out the Dwemer ruins there to see if I can locate the misplaced books."] = "Urag a fini par trouver une piste sur des livres qui auraient été « empruntés » par un mage du Synode. Son assistante Ertzebet m'a confirmé qu'ils étaient passés et posaient des questions sur Mzulft. Je devrais explorer les ruines dwemers là-bas pour retrouver ces ouvrages égarés."
translations["Turn off the debugger"] = "Désactiver le débogueur"
translations["Turn debugging ON"] = "Activer le débogage"
translations["Brother Ikard of the order of Arkay was requested by Auryen to investigate a haunting at the museum. Not being very fond of the supernatural I left him to his own devices to solve the issue. Ikard's work should be done and I should check in to see if things have been restored to normal."] = "Le frère Ikard de l'ordre d'Arkay a été appelé par Auryen pour enquêter sur un phénomène de hantise au Musée. N'ayant guère d'affinités avec le surnaturel, je l'ai laissé s'en charger. L'enquête d'Ikard devrait être achevée et je devrais vérifier si la situation est redevenue normale."

# 8. Black Books Descriptions (matched by EDID)
black_books = {
    "DLC2BlackBook01DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Rêves éveillés d'un ciel sans étoiles

par Bilius Felcrex
</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/T_letter.png'>es yeux, autrefois décolorés par la chute d'étoiles de l'ultime révélation, apercevront à jamais la pâle étincelle suscitée par la question fondamentale, car seule la Véritable Quête façonne la frontière de la pensée. Le reste n'est que vulgaire fiction, vaine tentative d'imposer un ordre sur les faux-semblants d'une divinité indifférente.""",

    "DLC2BlackBook02DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Perspicacité épistolaire

par le Transparent
</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/B_letter.png'>ring you forth the lovestruck mute who preys with vigor on his love, and set the sky alight with all who dare to struggle 'gainst our move. Car nous sommes les maîtres de la nuit et tous ceux qui s'en éloignent périssent ; nous buvons les fruits de la pensée et hurlons notre tumulte sur les remparts.""",

    "DLC2BlackBook03DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Légendes oubliées
Les autres vies d'Ysgramor

</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>lors que les grands navires des hommes fendaient les flots vers leur destinée, un grand nombre de récits se perdirent dans les brumes matinales au fil des siècles. Même après l'oubli, quelques lambeaux d'histoire parviennent jusqu'aux oreilles attentives, car les secrets les plus enfouis ne meurent jamais vraiment.""",

    "DLC2BlackBook04DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Les vents du changement

par 
Liesl Cœur-Gris
</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/D_letter.png'>urant le règne d'Elgryr, j'ai observé les divers méandres de la pensée et des mœurs d'un peuple troublé, et j'ai entrepris d'en dresser une humble taxonomie afin de mieux en comprendre les desseins.""",

    "DLC2BlackBook05DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Le Régent blafard

par Hawfip l'Artisan
</p>


[pagebreak]
<p align="left">
Acte I, Scène i
(Entre Filémina, tenant un sceptre brisé)
Filémina--
     Malheur à mon cœur accablé par le destin,
     Qui ne saurait offrir nulle tendresse à celui
     Qui voua ses faveurs aux dieux anciens
     Et vint à moi l'esprit ivre de sang.""",

    "DLC2BlackBook06DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Filament et filigrane

par Jelketheris
</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/I_letter.png'>e contemplais mon reflet dans le métal poli, me demandant si mon visage s'était durci au rythme de mes tourments intérieurs. Je forgeais cette pièce depuis des jours, et la fournaise étouffante commençait à peser.""",

    "DLC2BlackBook07DUMMY": """<font face="$HandwrittenFont">
<p align="center">

Le crépuscule caché

par 
Carillius Melfus
</p>


[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/T_letter.png'>a Cité des Graines d'encre s'élevait du désert, resplendissante et décadente. Contre toute attente, elle tenait encore debout. Je franchis la porte, et la bête sut exactement où me mener : la voie empruntée par les mendiants et les poètes."""
}

txt_translations = {
    "$gen_XmasToggleInfo": "Active les décorations de Noël autour du Musée et de la cachette.",
    "$gen_BedToggle": "Lit à baldaquin de la cachette",
    "$gen_BedToggleInfo": "Remplace le lit à baldaquin de la cachette par un lit double standard pour assurer la compatibilité avec certains mods de sommeil.",
    "$gen_RadiantTours": "Visites guidées du Musée"
}

# Apply translations to ESM
esm_translated_count = 0
unmatched_esm = []

for s in esm_data:
    if s.get("status") == "TranslationRequired" or not s.get("string"):
        orig = s.get("original")
        edid = s.get("editor_id")
        
        translated_text = None
        if orig in translations:
            translated_text = translations[orig]
        elif edid in black_books:
            translated_text = black_books[edid]
            
        if translated_text is not None:
            s["string"] = translated_text
            # Status: TranslationIncomplete (To approve / À vérifier)
            s["status"] = "TranslationIncomplete"
            esm_translated_count += 1
        else:
            unmatched_esm.append(s)

print(f"ESM translated: {esm_translated_count} / {esm_translated_count + len(unmatched_esm)}")
if unmatched_esm:
    print(f"Unmatched ESM entries ({len(unmatched_esm)}):")
    for u in unmatched_esm:
        print(f"  [{u.get('type')}] ({u.get('form_id')}) {u.get('editor_id')}: {repr(u.get('original'))}")

# Apply translations to TXT
txt_translated_count = 0
for s in txt_data:
    if s.get("status") == "TranslationRequired" or not s.get("string"):
        mcm_id = s.get("mcm_id")
        if mcm_id in txt_translations:
            s["string"] = txt_translations[mcm_id]
            s["status"] = "TranslationIncomplete"
            txt_translated_count += 1

print(f"TXT translated: {txt_translated_count}")

# Save both files
with open(esm_file, "w", encoding="utf-8") as f:
    json.dump(esm_data, f, indent=2, ensure_ascii=False)

with open(txt_file, "w", encoding="utf-8") as f:
    json.dump(txt_data, f, indent=2, ensure_ascii=False)

print("Saved both files successfully!")
