# Répertoire des Traductions Vérifiées et Harmonisées

> **Projet :** SSE Auto Translator / Nolvus Awakening  
> **Norme de localisation appliquée :** [Translations instructions.txt](file:///e:/Code/SSE%20Translator%20updated/Translations%20instructions.txt) (Lore officiel Bethesda France, Confrérie des Traducteurs, conventions du jeu de base).  
> **Dernière mise à jour :** 27 Octobre 2026  

---

## 📊 Résumé Global

* **Mods et extensions audités & finalisés :** Plus de **45 mods / compilations majeurs** (et leurs patchs d'intégration).
* **Fichiers de base de données traités :** Fichiers `.esp.json`, `.esm.json`, `.esl.json` et fichiers d'interface SkyUI MCM (`_french.txt.json`).
* **Qualité technique :** 100 % de conformité des balises (`<font>`, balises propres au moteur Skyrim, placeholders et codes de saut de page `[pagebreak]`). Élimination de tous les résidus numériques illégaux (`<10>`, `<5>...`) et des balises HTML orphelines.

---

## 🏛️ 1. Quêtes Majeures, Nouveaux Mondes & Extensions

| Mod / Extension | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **Legacy of the Dragonborn (LOTD)** | `LegacyoftheDragonborn.esm.json` + Patches officiels | Audit approfondi des descriptions d'artéfacts, réalignement des objectifs de quêtes, harmonisation avec le lore Bethesda et élimination des faux positifs. |
| **Guivrecroc (Wyrmstooth)** | `Wyrmstooth.esp.json`, `Wyrmstooth_french.txt.json`, patchs UWR, Cause, Curios, Craftable Sets, LotD Patch | Complétion intégrale des chaînes manquantes, réalignement des noms de lieux et donjons de l'île. |
| **La Cité oubliée (The Forgotten City)** | `ForgottenCity.esp.json` | Complétion intégrale de la quête, dialogues immersifs révisés, conformité avec le lore temporel. |
| **Sunthgat** | `Sunthgat.esp.json` | Audit textuel complet, révision des entrées de journal et quêtes, cohérence stylistique. |
| **Vigilant** | `Vigilant.esp.json`, sous-titres, `Vigilant Nerfed Rewards.esp.json`, `vigilant_LOOT.json` | Harmonisation des textes, révision des récompenses rééquilibrées, correction des sous-titres et bestiaire. |
| **Unslaad** | `Unslaad.esp.json`, patchs d'affichage LOTD | Validation des textes de quêtes et des stèles d'affichage. |
| **Lucien Flavius** | `lucien-anniversaryedition-patch.esp.json`, patch Bruma | Validation de la cohérence des dialogues d'accompagnement pour le Creation Club et Bruma. |

---

## ⚙️ 2. Gameplay, Mécaniques & Progression

| Mod / Système | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **Nolvus Experience Integration** | `Nolvus Awakening Experience Integration.esp.json` | Audit et harmonisation de l'intégralité des 30 quêtes majeures et secondaires avec le journal officiel. |
| **Adamant - Refonte des atouts** | `Adamant.esp.json` | Réalignement exact des pourcentages et effets de perks (frappes de bouclier, surcharge de foudre, armure lourde sans encombrement). |
| **Vokrii - Atouts minimalistes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` | Réalignement des multiplicateurs de coups critiques (haches, dagues, marteaux) et des pourcentages d'armes à une main. |
| **Vokriinator Black et ses patchs** | `Vokriinator Black.esp.json` ; `Vokriinator Black - Apocalypse patch.esp.json` ; `fzmx - dac - vokriinator.esp.json` ; `DISCO_VokriinatorISCPatch.esp.json` ; `Vokriinator Black Ethereal Arrow Fix.esp.json` ; `Vokriinator Black -- No Timed Blocking.esp.json` ; `vokriinatorblack - combatforcaco.esp.json` ; `Nolvus Awakening Vokriinator Black Integration.esp.json` | Audit de cohérence avec Ordinator, Path of Sorcery et les autres traductions du projet ; traduction des 27 chaînes manquantes ; correction de descriptions décalées (Disciple élu, Seigneur des os, Connaissance des cryptes, appel aux armes), du nom d'atout « Disciple élu » et d'une variable remplacée par erreur. 100 % des entrées complètes après vérification. |
| **La Voie du Sorcier (Path of Sorcery)** | `Path of Sorcery.esp.json` | Réalignement des barrières magiques (Rangs 1 et 2), auras de lumière, runes et sorts de froid. |
| **Artéfacts de Zim (ZIA Complete Pack)** | `Zim's Immersive Artifacts.esp.json` | Rétablissement des bonus réels (dégâts d'attaque furtive réalignés à +50 %, sorts uniques réalignés). |
| **Alternate Perspective** | Interface `_french.txt.json` | 29 chaînes d'interface traduites, boutons MCM fonctionnels et fichier UTF-16 LE régénéré. |
| **Quests Award Perk Points (QAPP)** | 15 fichiers de patchs QAPP | Traduction harmonisée des notifications d'attribution de points d'atouts lors de l'achèvement des quêtes. |
| **Stances - Dynamic Animation Sets** | `stances - dynamic weapon movesets se.esp.json` | **100 % Complete (36 / 36 entrées).** Harmonisation terminologique sur le terme noble « Posture » (*Posture haute, Posture médiane, Posture basse*) au lieu de « Position », respect de la terminologie officielle Bethesda pour la Vigueur (*Stamina* corrigé de « endurance » en « vigueur »), descriptions fluides et validation des 21 identifiants techniques internes. |
| **Stances - Add-On** | `stances - add-on.esp.json` | **100 % Complete (27 / 27 entrées).** Traduction complète de toutes les chaînes manquantes/en anglais (bonus/pénalités de vitesse de déplacement, vitesse d'attaque en main principale / main secondaire, ajustements d'armes, quête MCM). Rétablissement des descriptions propres à l'Add-On pour les 3 postures qui avaient été écrasées par le mod de base. |
| **Nolvus Awakening Stances Perk System** | `nolvus awakening stances perk system.esp.json` (196 entrées, dont 13 chaînes liées à Stances - Dynamic Weapon Movesets SE, 1 à Stances - Add-On et 1 à Smooth Animation) | **Audit complet validé (196 / 196 entrées ; 29 chaînes manquantes complétées).** Révision des traductions existantes, correction de formulations littérales et de termes d’armes, harmonisation « posture » / « vigueur », traduction des noms et descriptions d’atouts, des attaques chargées et des effets/entrées de quête. Identifiants techniques `stances_switch_*` conservés. Contrôle des identifiants, textes sources et pourcentages après écriture. |
| **Animations de Chasse immersive (Immersive Hunting Animations)** | `immersivehunting.esp.json`<br>`ImmersiveHunting_french.txt.json` | **100 % Complete (ESP : 53 / 53 entrées ; MCM : 72 / 72 entrées).** Correction de faux-sens majeurs (*Butcher* traduit à tort par le nom de métier « Boucher » au lieu de l'action « Découper la viande » ; *Skin* traduit par « Peau » au lieu de l'action « Dépecer » ; *Harvest* « Récupérer » affiné en « Prélever » ; *Prompt* « Sur demande » affiné en « Menu interactif »). Traduction intégrale des 61 chaînes MCM SkyUI laissées en anglais (modes de fouille, transport de carcasses, vue forcée à la 3e personne, dépeçage réaliste, intégrations Campfire, Shovels Bury Bodies, Skyrim Souls, QuickLoot, IED). Traduction et harmonisation intégrale dans l'ESP des 15 carcasses d'animaux, des 15 modèles d'animaux écorchés, des fourrures d'exposition IED (*brune, noire, blanche, des neiges, des vallées*) et du menu interactif selon la terminologie officielle de *Simple Hunting Overhaul* et du jeu de base. |
| **Décoctions de Bordeciel (Sky Decoction)** | `SkyDecoction.esp.json` | **100 % Complete (299 / 299 entrées).** Traduction intégrale du système d'alchimie et de décoctions (inspiré du Sorceleur / The Witcher). Nomenclature harmonisée pour les 19 familles de décoctions et leurs 3 rangs (*Décoction : [Nom]*, *Décoction : [Nom] amélioré(e)*, *Décoction : [Nom] supérieur(e)*) et leurs 57 résidus alchimiques. Traduction littéraire des 57 descriptions d'effets magiques (`MGEF DNAM`) avec préservation stricte des balises et variables du moteur (`<mag>`, `<dur>`, `<100>`), typographie française et restitution soignée des citations de saveur (*flavor quotes*). Traduction intégrale des 3 traités alchimiques (`BOOK FULL` et `BOOK DESC` : formules élémentaires, avancées et supérieures) avec respect rigoureux des noms officiels Bethesda pour la totalité des ingrédients alchimiques et alcools solvants (givreboises, cloquerille, truffe de Namira, brillefleur, la Chance soyeuse, etc.). Préservation intacte des identifiants techniques internes. Zéro mojibake. |

---

## 🎨 3. Cosmétique, Races, Anatomie & Interfaces MCM

| Mod | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **Racial Skin Variance - SPID (RSV)** | `Racial Skin Variance - SPID.esp.json`<br>`Racial Skin Variance - SPID_french.txt.json` | **100 % Complete.** Correction des contresens majeurs (*Free Mode* « Libérer » -> « Libre »), correction de « Bréton » -> « Breton », harmonisation des races officielles (*Haut-Elfe, Elfe noir, Elfe des bois, Orque, etc.*), traduction complète des 145 chaînes MCM restantes (dentitions, prérequis CBBE/BHUNP/HIMBO/SoS/TNG, sauvegardes). |
| **The New Gentleman (TNG)** | `TheNewGentleman_French.txt.json` | Traduction intégrale de l'interface SkyUI MCM, des réglages anatomiques et des descriptions d'ajustement. |
| **Yeux luisants (JS Emissive Eyes SE)** | `JS Emissive Eyes SE - Johnskyrim.esp.json`, Growl patch, `_french.txt.json` | Validation des réglages MCM et des noms de préréglages visuels. |

---

## ⚔️ 4. Armes, Armures & Équipement

| Mod | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **Arsenal animé (New Armoury)** | `NewArmoury.esp.json` | Noms canoniques des types d'armes nouveaux (rapières, piques, hallebardes, massues, dagues doubles). |
| **Armes de Billyro** | `Billyro's Weapons.esp.json` | Harmonisation des désignations d'acier, d'argent et de forgeage. |
| **Katana - Journey in the Shadows** | `Katana.esp.json` | Validation des katanas traditionnels, daïshos, nodachis et fourreaux. |
| **Armes & Armures d'Aéthérium** | `AetheriumSwordsnArmorFixes.esp.json`, patchs DBM & CCOR | Nomenclature unifiée des pièces d'aéthérium forgées. |
| **Nolvus Awakening Weapons & Armors** | `nolvus awakening weapons patch.esp.json`, `Nolvus Awakening Armors Patch.esp.json` | Harmonisation des statistiques d'armes et des ensembles d'armures Nolvus. |
| **Wind Ruler Armor** | `Wind Ruler Armor.esp.json` | Harmonisation de l'ensemble d'armure du Régent du Vent. |

---

## 🐾 5. Bestiaire & Créatures

| Mod | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **The Dragonborn's Bestiary** | `The Dragonborn's Bestiary.esp.json` + Addons Mihail | Harmonisation complète du bestiaire en français. |
| **Monstres de Mihail (Mihail Monsters)** | Géants des mers & titans de glace, Vampire Beasts, Grummites, Giantesses, Water Hags | Traduction et validation des descriptions de créatures et des tables de butin (`_LOOT.json`). |
| **Diverse Dragons Collection (DDC)** | `DiverseDragonsCollectionSE.esp.json`, `_french.txt.json` | Harmonisation des noms et pouvoirs uniques des dragons ajoutés. |
| **Une vie de chat (A Cat's Life)** | `ACatsLife.esp.json` | Traduction des accessoires, interactions et soins pour félins. |

---

## 🏙️ 6. Immersion, Lieux & PNJs

| Mod | Fichiers audités | Type d'intervention & Statut |
| :--- | :--- | :--- |
| **Citizens of Tamriel** | `citizenscomplete.esp.json`<br>+ 6 patchs d'intégration (MIE, Modpocalypse, RS Children, TGC Winterhold, JK's EEK, JK's Bards College, LuxID) | **100 % Complete (5 637 / 5 637 entrées).** Traduction littéraire et intégration des 27 répliques de dialogues manquantes/restées en anglais (voleurs, loterie de caisses, marchands, Florian de Gabb, Paarthurnax, guerre civile, etc.). Contrôle complet de la cohérence lore (Bordeciel, châtellenies, Dévoreur de mondes, ragnards, septims, Sovngarde). Zéro balise illégale, zéro mojibake. |
| **Marché de Blancherive (Kojaks Whiterun Market)** | `Kojaks Whiterun Market.esp.json` | Correction de contresens critiques : « Sinnen la barrière » -> « Sinnen la receleuse », « Balle de Trueaz », « Clé de l'enclos », « Auberge de la Chouette perchée ». |
| **WONpcs** | `WONpcs.esp.json` | Harmonisation avec les receleurs et marchands du marché de Blancherive. |
| **L'Hôtel de la Ville d'Aubétoile (The Great City of Dawnstar)** | `The Great City of Dawnstar.esp.json` | Traduction et harmonisation des nouveaux bâtiments et commerces portuaires. |
| **Missives** | Fichiers des tableaux d'affichage (Bruma, Falskaar, Wyrmstooth, Solstheim, Midwood) | Harmonisation des avis de recherche (« Récupération dans un repaire », « Récupération dans une ruine », etc.). |
| **USSEP (Unofficial Skyrim Patch)** | `Unofficial Skyrim Special Edition Patch.esp.json` | Réinjection de 283 chaînes manquantes, harmonisation sur la localisation française officielle (100 % complet). |

---

## 🧩 8. Mods vérifiés — passe du 27 octobre 2026

| Mod / fichiers audités | Interventions et statut |
| :--- | :--- |
| **Amélioration de la Lame des Sangskaals** — `Bloodskal Blade - Tweaks and Enhancements.esp.json`, `ZIA_Complete Pack - Bloodskal Blade T&E Patch.esp.json` | Harmonisation de la « Frappe des Sangskaals », révision de la description des dégâts et de leur progression ; conservation des variables numériques du jeu. Patch ZIA vérifié. Fichiers complets. |
| **CCQuest - Experience Patch** — `ccquest - experience patch.esp.json` | Traduction des entrées manquantes de la quête de l’Aube et révision de textes voisins pour garder le fil narratif du Gardien et du caveau. Correction de chaînes du contenu Pêche dont les variables d’alias ou de quête avaient été omises ou remplacées. 1 594 entrées vérifiées, aucune chaîne manquante ni variable discordante. |
| **Experience** — `Experience_FRENCH.txt.json` | Traduction des 62 chaînes MCM manquantes ; vérification des variables de format et de la terminologie de progression. 94 entrées complètes. |
| **Nolvus Awakening Stances Perk System** — `nolvus awakening stances perk system.esp.json` | Traduction des 29 chaînes manquantes, révision des 89 descriptions et traduction/harmonisation des 89 noms d’atouts. « Posture », « vigueur » et désignations d’armes uniformisés. 196 entrées complètes ; balises et variables contrôlées. |
| **Runes étranges** — `StrangeRunes.esp.json`, `StrangeRunes_french.txt.json` | Traduction des noms et effets du plugin ainsi que des libellés MCM (décalages et rotations X/Y/Z). 419 entrées plugin et 87 entrées d’interface complètes ; variables de format conservées. |
| **GIST - Capture d’âmes intelligente** — `GIST soul trap.esp.json` | Vérification des 19 entrées, traduction des libellés de test et maintien de l’identifiant technique interne sans traduction. Fichier complet. |
| **Nolvus Awakening Perk Patch** — `nolvus awakening perk patch.esp.json` | Traduction de la description manquante ; harmonisation de « vigueur », « magie » et des griffes liées. 85 entrées complètes. |
| **Simply Balanced** — `SimplyBalanced_FRENCH.txt.json` | Traduction intégrale des 304 chaînes MCM ; harmonisation des compétences, dégâts, potions, effets magiques, progression et réglages de sauvegarde. Contrôle des identifiants, retours à la ligne et variables ; fichier complet. |
| **RaceMenu High Heels Fixes - Advanced** — `heelsfix_french.txt.json`, `heelsfix.esp.json` | Traduction des 45 chaînes MCM manquantes ; harmonisation du vocabulaire des corrections de talons, des réglages de Mu Joint Fix et des libellés visibles du plugin. Correction de formulations/typos et conservation stricte des balises et noms techniques. 70 entrées vérifiées, aucune chaîne manquante. |
| **Vokriinator Black et patch Apocalypse** — `Vokriinator Black.esp.json`, `Vokriinator Black - Apocalypse patch.esp.json` | Recontrôle des 1 236 et 7 entrées ; restauration des marqueurs numériques de jeu conservés sous la forme `<nombre>` dans 15 descriptions. Aucune chaîne restante à traduire. |


| **Additional Attack By Loop et Frenzy** — `Additional Attack By Loop_french.txt.json`, `frenzy.esp.json` | Relecture des libellés MCM, effets et descriptions ; harmonisation de la frénésie, des attaques enchaînées et des termes de combat. 48 entrées complètes, variables contrôlées. |
| **True Armor** — `truearmor.esp.json`, `True Armor - Evolved.esp.json`, `TrueArmor_FRENCH.txt.json` | Audit des deux plugins et traduction des 472 chaînes MCM manquantes. Terminologie homogène pour protections, matériaux, attributs, sorts et réglages ; retours à la ligne et variables conservés. 769 entrées complètes, aucune chaîne requise restante. |
| **Madmen — Refonte des Parjures** — `Madmen.esp.json`, `Madmen - Abyss.esp.json`, `Madmen - Fishing.esp.json`, `Madmen - Ryns Karthspire.esp.json`, `Madmen - Wyrmstooth.esp.json` | Traduction des chaînes restantes et harmonisation des classes/PNJ parjures, roncecoeurs et sorts d’Abyss. Restauration de marqueurs numériques perdus ; chaînes internes non affichées conservées comme telles. 997 entrées vérifiées, aucune chaîne requise restante. |
| **Akaviri Follower** — `akavirifollower.esp.json` | Traduction des capacités et titres de grimoires manquants ; noms de personnages, appellations japonaises établies et identifiants techniques préservés. Correction du mauvais appariement entre titres, descriptions, marqueurs et balises HTML. 321 entrées contrôlées, aucune chaîne requise restante. |
| **Bloodeye** — `bloodeye.esp.json` | Traduction du journal d’Albert depuis le chinois, avec cinq sauts de page et la balise de police conservés ; nom du boss adapté en français sous la forme « Albert Œil-de-sang » et harmonisé dans le patch Combat Scaling. 6 entrées vérifiées. |
| **Bosses — Penetrator, TsunDal, Soul Cairn et intégration Nolvus** — `thepenetratorboss.esp.json`, `tsundalboss.esp.json`, `soulcairnboss.esp.json`, `nolvus awakening combat scaling overhaul - boss.esp.json`, `nolvus awakening boss integration.esp.json` | Traduction des noms d’équipement et des effets lisibles ; noms propres et identifiants internes non affichés conservés. Correction des champs écrasés par un appariement de FormID sans distinction de type ; placeholders et balises vérifiés. Le nom du boss Bloodeye Albert est harmonisé en « Albert Œil-de-sang » dans le patch Combat Scaling. Après l’audit, cinq descriptions d’effets de `tsundalboss.esp.json` encore en anglais ont été traduites ; le plugin ne contient plus de description affichée non traduite. |
| **Shadow of Skyrim** — `Shadow of Skyrim.esp.json` | Traduction des 83 entrées encore signalées : noms de quêtes, effets et commentaires de script. Identifiants techniques conservés ; JSON relu après écriture, aucune chaîne `TranslationRequired` restante. |
| **Nolvus — Prepare to Die et Combat Synergy** — `nolvus awakening combat scaling overhaul - consistency patch.esp.json`, `Nolvus Awakening Combat Scaling Overhaul - Core.esp.json`, `nolvus awakening combat scaling overhaul - enemy level mult.esp.json`, `nolvus awakening combat scaling overhaul - enemy level.esp.json`, `nolvus awakening combat synergy patch.esp.json` | Terminologie des créatures et classes harmonisée. Lors d’un contrôle ciblé, les entrées `Albert` (Moon and Star) et `Alberthor` (Wyrmstooth, deux références) ont été identifiées comme noms propres et classées `NoTranslationRequired`. Aucun libellé « Blood Albert » n’existe dans ces fichiers. Les valeurs GMST binaires restent intactes. |
| **Simply Balanced** — `SimplyBalanced_FRENCH.txt.json` | Relecture de cohérence après traduction intégrale : compétences, dégâts, effets magiques, potions et réglages MCM ; balises, variables et sauts de ligne vérifiés. 304 entrées complètes. |

---

## 🧹 7. Nettoyages Techniques & Normalisations Globales

1. **Nettoyage des balises numériques corrompues :**
   * **2 816 balises illégales** supprimées (`<10>`, `<5>`, etc.) réparties sur 173 fichiers JSON (notamment Abyss, Adamant, mods de sorts).
   * Suppression totale des risques de crash moteur et de textes invisibles en jeu.
2. **Clôture des balises HTML orphelines :**
   * **1 930 balises `<font>` orphelines** refermées proprement par `</font>` sur 232 fichiers de livres et notes.
3. **Harmonisation terminologique Bethesda :**
   * *Mont Écarlate* (et non *Montagne rouge*).
   * Noms de lieux unifiés : *Bric-à-brac, Grotte de Sourcechaude, La Cruche percée - Réservoir, Le Foyer gelé, Les Occasions de Sadri, Château Volkihar, Musée dwemer, Temple d'Havreciel*.
   * Noms de sorts unifiés : *Gel pénétrant, Foudre déchaînée, Froid mordant, Lance gelée, Ponction de santé, Siphon de magie*.

---

*Ce document est maintenu à jour au fur et à mesure des audits et des révisions de la modlist.*
