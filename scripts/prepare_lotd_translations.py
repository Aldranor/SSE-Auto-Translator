import json
import re
from pathlib import Path

esm_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")
txt_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/interface/translations/legacyofthedragonborn_french.txt.json")

# Build dictionary of translations
# We map by (form_id, type, index, original) for ESM
# and by mcm_id for TXT

esm_translations = {}
txt_translations = {
    "$gen_XmasToggleInfo": "Active les décorations de Noël autour du Musée et de la cachette.",
    "$gen_BedToggle": "Lit à baldaquin de la cachette",
    "$gen_BedToggleInfo": "Remplace le lit à baldaquin de la cachette par un lit double standard pour assurer la compatibilité avec certains mods de sommeil.",
    "$gen_RadiantTours": "Visites guidées du Musée"
}

# 1. BOOKS & MAPS (BOOK FULL, ACTI FULL)
for i in range(11, 21):
    roman = ["XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX"][i - 11]
    esm_translations[f"Treasure Map {roman}"] = f"Carte au trésor {roman}"

for i in range(21, 26):
    roman = ["XXI", "XXII", "XXIII", "XXIV", "XXV"][i - 21]
    esm_translations[f"Treasure Map {roman}"] = f"Carte au trésor {roman}"

esm_translations["Treasure Map VI"] = "Carte au trésor VI"
esm_translations["Treasure Map IX"] = "Carte au trésor IX"
esm_translations["Black Book"] = "Livre noir"

# 2. MISC / ITEMS / DOORS / KEYS
esm_translations["Dwemer Junk"] = "Bric-à-brac dwemer"
esm_translations["Wooly Mammoth"] = "Mammouth laineux"
esm_translations["Coral"] = "Corail"
esm_translations["Ivory"] = "Ivoire"
esm_translations["Wanderlust (replica)"] = "Soif d'errance (réplique)"
esm_translations["Raptor"] = "Raptor"
esm_translations["Merrian's Sack"] = "Sac de Merrian"
esm_translations["Barrel of Jars"] = "Tonneau de bocaux"
esm_translations["Debug Portal"] = "Portail de débogage"
esm_translations["Enable/Disable"] = "Activer/Désactiver"
esm_translations["Hidden Wall"] = "Mur secret"
esm_translations["Key to Dragonborn Gallery"] = "Clé de la galerie de l'Enfant de dragon"
esm_translations["Riften Fishery"] = "Pêcherie de Faillaise"

# 3. INTERFACE / MESSAGES (MESG DESC / MESG ITXT)
esm_translations["You must set a heading first."] = "Vous devez d'abord définir un cap."
esm_translations["The Dev Aveza is currently travelling to <Alias=Current>. I can't change it's course until it arrives."] = "Le Dev Aveza voyage actuellement vers <Alias=Current>. Vous ne pouvez pas modifier son cap avant son arrivée."
esm_translations["When I hold the beacon I can feel a link to another device, but it does nothing.\r\n"] = "Lorsque je tiens la balise, je sens un lien avec un autre appareil, mais rien ne se produit.\r\n"
esm_translations["I should probably stand clear of the airship as it departs!"] = "Je devrais sans doute m'écarter du vaisseau volant lors de son départ !"
esm_translations["The Dev Aveza will arrive at <Alias=Current> in %.0f hours."] = "Le Dev Aveza arrivera à <Alias=Current> dans %.0f heures."
esm_translations["The Dev Aveza has arrived at <Alias=Current>."] = "Le Dev Aveza est arrivé à <Alias=Current>."
esm_translations["The Dev Aveza can be docked at several key locations around Tamriel including the hold capitals of Skyrim and the Dragonborn Gallery. Each journey on board the Dev Aveza will take 4 hours to complete. As you continue on your advertures more stops will be unlocked. "] = "Le Dev Aveza peut accoster à plusieurs endroits clés de Tamriel, notamment les capitales de châtelleries de Bordeciel et la Galerie de l'Enfant de dragon. Chaque trajet à bord du Dev Aveza dure 4 heures. Au fil de vos aventures, d'autres escales seront déverrouillées."
esm_translations["The Dev Aveza is already docked at <Alias=Current>."] = "Le Dev Aveza est déjà amarré à <Alias=Current>."
esm_translations["What type of supply would you like to order?"] = "Quel type de fournitures souhaitez-vous commander ?"
esm_translations["Ingots/Gems"] = "Lingots/Gemmes"
esm_translations["Leather/hide etc"] = "Cuir/Peaux etc."
esm_translations["Food/Drink"] = "Nourriture/Boisson"
esm_translations["Check Orders"] = "Consulter les commandes"
esm_translations["All displayable items added to your inventory, ya cheater! "] = "Tous les objets exposables ont été ajoutés à votre inventaire, sale tricheur !"
esm_translations["This key gives access to the debug room in the Storeroom. It is strongly recommend you do not tinker with the controls found there unless you know exactly what you're doing!"] = "Cette clé donne accès à la salle de débogage dans la réserve. Il est fortement déconseillé de toucher aux commandes qui s'y trouvent, à moins de savoir exactement ce que vous faites !"

# 4. DIALOGUE REPLIES (INFO NAM1)
esm_translations["Yes, hmmm, well, sad to say, this is just a single variety of pure ore with nothing else in it. Sorry."] = "Oui, hmm, ma foi, au regret de vous le dire, ce n'est qu'un simple échantillon de minerai ordinaire sans rien d'autre d'intéressant. Désolé."
esm_translations["There you go. If you have any more you want looked at, just let me know."] = "Et voilà. Si vous en avez d'autres à faire examiner, faites-le-moi savoir."

# 5. DIALOGUE TOPICS (DIAL FULL)
esm_translations["I need to borrow the Spear of the Snow Prince"] = "J'ai besoin d'emprunter la Lance du Prince des neiges."
esm_translations["Where did you say you found that spear?"] = "Où avez-vous dit que vous aviez trouvé cette lance ?"
esm_translations["Do you know where the ruins in the book could be?"] = "Savez-vous où pourraient se trouver les ruines mentionnées dans le livre ?"
esm_translations["What can you tell me about the relics you found?"] = "Que pouvez-vous me dire sur les reliques que vous avez trouvées ?"
esm_translations["I found an ancient shield in Fort Pale Pass."] = "J'ai trouvé un bouclier antique au fort du Col pâle."
esm_translations["I have the setting to the Amulet of Kings"] = "J'ai la monture de l'Amulette des rois."
esm_translations["Have you found out anything about the amulet and shield?"] = "Avez-vous appris quelque chose sur l'amulette et le bouclier ?"
esm_translations["Here's the fragmented Amulet of Kings and the Shield of Reman"] = "Voici l'Amulette des rois fragmentée et le Bouclier de Reman."
esm_translations["I've found Zurin Arctus' Ring"] = "J'ai trouvé l'anneau de Zurin Arctus."
esm_translations["Any leads on the Lord's Mail or Wulfharth's tomb?"] = "Des pistes sur l'Armure du Seigneur ou la tombe de Wulfharth ?"
esm_translations["I have all three relics"] = "J'ai les trois reliques."
esm_translations["I have the relics and the Lord's Mail"] = "J'ai les reliques et l'Armure du Seigneur."
esm_translations["What can you tell me about the Falmer ruins?"] = "Que pouvez-vous me dire sur ces ruines falmers ?"
esm_translations["What can you tell me about this temple?"] = "Que pouvez-vous me dire sur ce temple ?"
esm_translations["Let's talk about the Snow Elves."] = "Parlons des Elfes des neiges."
esm_translations["Let's head back to the museum."] = "Retournons au Musée."
esm_translations["Have you had any luck translating the Falmer tome?"] = "Avez-vous réussi à traduire le tome falmer ?"
esm_translations["I'm ready to head to the Glacial Crevice."] = "Je suis prêt à me rendre dans la Faille glaciaire."
esm_translations["We should make camp here."] = "Nous devrions établir notre camp ici."
esm_translations["Tell me about this shrine to Phynaster."] = "Parlez-moi de cet autel de Phynaster."
esm_translations["We did it. Neb-Crescen is ours."] = "Nous avons réussi. Neb-Crescen est à nous."

# 6. QUEST NAMES (QUST FULL)
esm_translations["Shattered Legacy"] = "L'Héritage brisé"
esm_translations["Museum Startup"] = "Lancement du Musée"
esm_translations["Kegbreaker Effect Tracker"] = "Suivi de l'effet du Brise-baril"
esm_translations["Ruins of Rkund"] = "Les ruines de Rkund"
esm_translations["Field Station - Falkreath"] = "Poste de terrain - Épervine"
esm_translations["Field Station - The Reach"] = "Poste de terrain - La Crevasse"
esm_translations["Field Station - The Pale"] = "Poste de terrain - Le Clos"
esm_translations["Night at the Museum"] = "Une nuit au Musée"
esm_translations["Ongar's Kegbreaker"] = "Le Brise-baril d'Ongar"
esm_translations["The Amulet of Kings"] = "L'Amulette des rois"
esm_translations["The Dragonborn Gallery"] = "La Galerie de l'Enfant de dragon"
esm_translations["Excavation 2 Scene Handler"] = "Gestionnaire de scène - Fouille 2"
esm_translations["MASTER DEBUGGING HANDLER"] = "GESTIONNAIRE PRINCIPAL DE DÉBOGAGE"
esm_translations["Restocks Writing Stuff"] = "Réapprovisionnement du matériel d'écriture"
esm_translations["Malrus' Codex Manager"] = "Gestionnaire du codex de Malrus"
esm_translations["Haunted Museum"] = "Le Musée hanté"
esm_translations["Airship Remote Calling"] = "Appel à distance du vaisseau volant"
esm_translations["Household Planner Menu Handler"] = "Gestionnaire de menu de l'intendance"
esm_translations["Radiant Museum Tour"] = "Visite guidée du Musée"
esm_translations["Airship Navigation"] = "Navigation du vaisseau volant"
esm_translations["Airship Beacon Handler"] = "Gestionnaire de la balise du vaisseau volant"
esm_translations["Museum Display Manager"] = "Gestionnaire des expositions du Musée"
esm_translations["Dragonborn Museum Quest Handler"] = "Gestionnaire des quêtes du Musée"
esm_translations["Relic Tracker"] = "Traqueur de reliques"

# 7. QUEST STAGES (QUST CNAM)
esm_translations["I've gotten the drop on Ezra. I should take her shard and look for clues about why she was here at Fort Pale Pass to begin with."] = "J'ai pris le dessus sur Ezra. Je devrais prendre son fragment et chercher des indices pour comprendre ce qu'elle faisait au fort du Col pâle."
esm_translations["I should see what else of interest Ezra has or bide my time and return her to Argus"] = "Je devrais voir ce qu'Ezra possède d'autre d'intéressant ou attendre le bon moment pour la ramener à Argus."
esm_translations["I've gotten another shard off Ezra. I'll have to decide what to do about her. I can either return to Argus and risk her spilling the beans, or silence her permanently."] = "J'ai récupéré un autre fragment sur Ezra. Je dois décider de son sort : la ramener à Argus au risque qu'elle raconte tout, ou la faire taire définitivement."
esm_translations["I should see what else of interest Ezra has"] = "Je devrais voir ce qu'Ezra possède d'autre d'intéressant."
esm_translations["I located Ezra who is very paranoid that I'm an assassin for some reason. She's reluctantly agreed to follow me, but insists on finding her missing shield before returning to Argus."] = "J'ai localisé Ezra, qui est particulièrement paranoïaque et craint que je ne sois un assassin. Elle a accepté à contrecœur de me suivre, mais insiste pour retrouver son bouclier avant de retourner voir Argus."
esm_translations["I have found an ancient shield of some kind. Auryen may know more about it. I should track down the rest of the amulet pieces and then return to the museum."] = "J'ai trouvé une sorte de bouclier antique. Auryen en saura peut-être davantage. Je devrais rassembler les morceaux restants de l'amulette avant de retourner au Musée."
esm_translations["I've parted ways with Ezra, sending her to find Argus on her own while tend to other tasks. I may be able to locate all the pieces on my own."] = "Je me suis séparé d'Ezra, la renvoyant retrouver Argus seule pendant que je m'occupe d'autres tâches. Je pourrais bien retrouver tous les morceaux par moi-même."
esm_translations["I've found the remains of Ulgarg who met his untimely end in a violent way inside some nordic cave. There seems to be something odd glowing from his gut."] = "J'ai trouvé la dépouille d'Ulgarg, qui a connu une fin violente au fond d'une grotte nordique. Quelque chose d'étrange semble briller dans ses entrailles."
esm_translations["It seems that Ulgarg, in a moment of despiration, swallowed his fragment of the shard to keep it from the enemy. Fortunately I have a strong stomach. I now possess another fragment."] = "Il semble qu'Ulgarg, dans un geste désespéré, ait avalé son fragment pour empêcher l'ennemi de s'en emparer. Heureusement, j'ai l'estomac bien accroché. J'ai désormais un autre fragment en ma possession."
esm_translations["I managed to recover the setting for the Amulet of Kings. I've managed to gather all the missing fragments and should return to Auryen at the museum to see if he has found a way to reform it."] = "J'ai réussi à récupérer la monture de l'Amulette des rois. J'ai rassemblé tous les fragments manquants et devrais retourner voir Auryen au Musée pour savoir s'il a trouvé un moyen de la reconstituer."
esm_translations["Argus and Ezra have double crossed me and paid the price for it. Apparently they were mercenaries hired to finish a job I was caught in the middle of. Now that I have the fragments, I should see Auryen."] = "Argus et Ezra m'ont trahi et en ont payé le prix. C'étaient apparemment des mercenaires engagés pour terminer un contrat dans lequel je me suis retrouvé mêlé. Maintenant que j'ai les fragments, je devrais voir Auryen."
esm_translations["Auryen identified the ancient shield I found in Fort Pale Pass as the shield of Reman Cyrodiil, and he indicated that the strange fragment I had found was part of the Amulet of Kings! He suggested I seek out the other fragments."] = "Auryen a identifié le bouclier antique trouvé au fort du Col pâle comme étant le Bouclier de Reman Cyrodiil, et il a confirmé que l'étrange fragment faisait partie de l'Amulette des rois ! Il m'a suggéré de partir en quête des autres fragments."
esm_translations["Auryen should have had time to research the details surrounding the Amulet of Kings and the Shield. I should check back with him and see what he's discovered."] = "Auryen a dû avoir le temps d'étudier les détails concernant l'Amulette des rois et le Bouclier. Je devrais retourner le voir pour découvrir ce qu'il a appris."
esm_translations["I have obtained the helm of Tiber Septim but feel as though the dark power binding me here still has hold over me. I should investigate the catacombs further."] = "J'ai obtenu le casque de Tiber Septim, mais je sens que la puissance obscure qui me retient ici a toujours prise sur moi. Je devrais explorer les catacombes plus en profondeur."
esm_translations["I've defeated Zurin Arctus, the Underking, though the power binding me here seems to remain. Perhaps he has some clue on him."] = "J'ai vaincu Zurin Arctus, le Roi des Tréfonds, mais le pouvoir qui m'emprisonne ici semble persister. Peut-être trouverai-je un indice sur sa dépouille."
esm_translations["I've found a very unique and interesting ring which I should show Auryen, but no other major clues as to why I am still trapped here. I must delve deeper."] = "J'ai trouvé un anneau tout à fait unique et fascinant que je devrais montrer à Auryen, mais aucun autre indice majeur sur les raisons de ma captivité. Je dois m'enfoncer plus profondément."
esm_translations["I've destroted Ysmir Wulfharth and obtained his boots. I need to get the Lord's Mail before I head back to Sancre Tor. I must search Castle Dour to see where it has gone."] = "J'ai terrassé Ysmir Wulfharth et obtenu ses bottes. Je dois mettre la main sur l'Armure du Seigneur avant de retourner à Sancre Tor. Je dois fouiller Mornétoile pour savoir ce qu'elle est devenue."
esm_translations["Sets up regular start and initialises some elements of the mod"] = "Configure le démarrage standard et initialise certains éléments du mod."
esm_translations["Kegbreaker has been drawn, alias will fill to select random tavern."] = "Le Brise-baril a été dégainé, sélection d'une taverne aléatoire."
esm_translations["Kegbreaker removed, recover from effect and stop quest."] = "Brise-baril retiré, récupération de l'effet et arrêt de la quête."
esm_translations["Auryen brought the Spear of the Snow Prince along on the excavation. As a probable devout follower of Trinimac, his spear may be able to open the way into the temple."] = "Auryen a apporté la Lance du Prince des neiges lors de la fouille. En tant que fervent fidèle probable de Trinimac, sa lance pourrait bien nous ouvrir l'accès au temple."
esm_translations["We attempted to overtake and fight Tulrin Deathweaver and his Falmer clan, but he proved to be as formidable as we feared. We were forced to fall back and regroup."] = "Nous avons tenté de surprendre et d'affronter Tulrin Tissetrempe et son clan falmer, mais il s'est avéré aussi redoutable que nous le redoutions. Nous avons été contraints de nous replier pour nous regrouper."
esm_translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I should scout the designated location in Falkreath."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. Je devrais reconnaître le site désigné à Épervine."
esm_translations["Marassi is ready to get underway on establishing another field station. This time in the Reach. As I have other things to attend to, I should send word to him when I'm ready to assist."] = "Marassi est prêt à fonder un autre poste de terrain, cette fois dans la Crevasse. Comme j'ai d'autres affaires à régler, je devrais lui faire signe dès que je pourrai l'aider."
esm_translations["Marassi has the idea to establish a number of field stations across Skyrim to act as safehouses and supply stops for explorers. I should scout the designated location in the Pale."] = "Marassi a eu l'idée d'établir plusieurs postes de terrain à travers Bordeciel pour servir de refuges et de relais de ravitaillement aux explorateurs. Je devrais reconnaître le site désigné dans le Clos."
esm_translations["The Museum has been robbed! People from Avram's shady past have made off with the contents of the museum, and now we must track down where they've gone!"] = "Le Musée a été cambriolé ! Des individus issus du passé trouble d'Avram ont dérobé les trésors du Musée, et nous devons à présent retrouver leur trace !"
esm_translations["I had been tasked by Ognar to retrieve his famous warhammer Kegbreaker. After investigating the Nightgate Inn, I've managed to find where it was hidden and claim it."] = "Ongar m'avait chargé de retrouver son fameux marteau de guerre, le Brise-baril. Après avoir fouillé l'auberge de la Porte nocturne, j'ai réussi à mettre la main dessus."
esm_translations["The exploration continues as we delve into the ruins of Rkund. I should meet up with the expedition team inside."] = "L'exploration se poursuit au cœur des ruines de Rkund. Je devrais rejoindre l'équipe d'expédition à l'intérieur."
esm_translations["The team has uncovered an ancient Snow Elf altar. We should investigate it and see if it can shed light on the fate of this fallen civilization."] = "L'équipe a mis au jour un antique autel des Elfes des neiges. Nous devrions l'examiner pour voir s'il peut nous éclairer sur le destin de cette civilisation déchue."
esm_translations["I have found several unusual books concerning the Dwemer but nothing that seems very useful. I should give them to Urag so he knows that this is NOT what I am looking for. Perhaps he will then have some other ideas on where to look."] = "J'ai trouvé plusieurs livres insolites sur les Dwemers, mais rien qui semble vraiment utile. Je devrais les confier à Urag pour qu'il voie que ce n'est PAS ce que je cherche. Peut-être aura-t-il d'autres pistes à me proposer."
esm_translations["Dwemer History and Culture did not have the insights I had hoped for. I should ask Urag again for more leads."] = "L'Histoire et la culture des Dwemers ne m'ont pas apporté les réponses espérées. Je devrais redemander des pistes à Urag."
esm_translations["Urag finally had a clue about some books which ended up being \"borrowed\" by some Synod mage. His assistant Ertzebet confirmed that they had come by and were asking about Mzulft. I should check out the Dwemer ruins there to see if I can locate the misplaced books."] = "Urag a fini par trouver une piste sur des livres qui auraient été « empruntés » par un mage du Synode. Son assistante Ertzebet m'a confirmé qu'ils étaient passés et posaient des questions sur Mzulft. Je devrais explorer les ruines dwemers là-bas pour retrouver ces ouvrages égarés."
esm_translations["Turn off the debugger"] = "Désactiver le débogueur"
esm_translations["Turn debugging ON"] = "Activer le débogage"
esm_translations["Brother Ikard of the order of Arkay was requested by Auryen to investigate a haunting at the museum. Not being very fond of the supernatural I left him to his own devices to solve the issue. Ikard's work should be done and I should check in to see if things have been restored to normal."] = "Le frère Ikard de l'ordre d'Arkay a été appelé par Auryen pour enquêter sur un phénomène de hantise au Musée. N'ayant guère d'affinités avec le surnaturel, je l'ai laissé s'en charger. L'enquête d'Ikard devrait être achevée et je devrais vérifier si la situation est redevenue normale."

# 8. BLACK BOOKS DESCRIPTIONS (BOOK DESC)
esm_translations["DLC2BlackBook01DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Rêves éveillés d'un ciel sans étoiles

par Bilius Felcrex
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/T_letter.png'>es yeux, autrefois décolorés par la chute d'étoiles de l'ultime révélation, apercevront à jamais la pâle étincelle suscitée par la question fondamentale, car seule la Véritable Quête façonne la frontière de la pensée. Le reste n'est que vulgaire fiction, vaine tentative d'imposer un ordre sur les faux-semblants d'une divinité indifférente."""

esm_translations["DLC2BlackBook02DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Perspicacité épistolaire

par le Transparent
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/O_letter.png'>n entendit parler pour la première fois de la Pierre démente de la Baie du miroir lors des massacres de la Deuxième Compagnie des Terres de l'Est."""

esm_translations["DLC2BlackBook03DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Légendes oubliées
Les autres vies d'Ysgramor

</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/O_letter.png'>n dit qu'après l'assaut de Saarthal, Ysgramor le Grand prit la mer vers le Nord avec ses deux fils. Mais une tempête sans égale les sépara des autres nefs."""

esm_translations["DLC2BlackBook04DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Les vents du changement

par 
Liesl Cœur-Gris
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/T_letter.png'>out voyageur traversant les étendues désolées d'Atmora finit par entendre les murmures portés par la bise polaire."""

esm_translations["DLC2BlackBook05DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Le Régent blafard

par Hawfip l'Artisan
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/A_letter.png'>u-delà des rives de Solstheim, là où les brumes s'épaississent comme du suif froid, se dresse l'ombre de celui qu'on ne nomme qu'à voix basse."""

esm_translations["DLC2BlackBook06DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Filament et filigrane

par Jelketheris
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/D_letter.png'>ans la trame du destin, les fils les plus ténus supportent parfois le fardeau des mondes."""

esm_translations["DLC2BlackBook07DUMMY"] = """<font face="$HandwrittenFont">
<p align="center">

Le crépuscule caché

par 
Carillius Melfus
</p>

[pagebreak]
<p align="left">
<img src='img://Textures/Interface/Books/Illuminated_Letters/L_letter.png'>orsque les ombres s'allongent à la fin du jour, le voile entre Tamriel et Apocrypha devient translucide comme l'aile d'une libellule."""

with open("lotd_generated_translations.json", "w", encoding="utf-8") as f:
    json.dump({
        "esm": esm_translations,
        "txt": txt_translations
    }, f, indent=2, ensure_ascii=False)

print(f"Generated translations for {len(esm_translations)} ESM strings and {len(txt_translations)} TXT strings.")
