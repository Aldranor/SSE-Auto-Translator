# Récapitulatif des Modifications — Phase 8 : Passe Finale de Propagation Cascade Source → Patchs

> **Date :** 28 Octobre 2026  
> **Statut :** ✅ Validé & Vérifié sur disque  
> **Périmètre audité :** 4 935 fichiers patchs (312 079 entrées analysées)  
> **Fichiers patchs harmonisés :** 300 fichiers  
> **Total modifications unitaires :** 1209 entrées  
> **Protocole de sécurité :** Ciblage unitaire strict `(form_id, type, index, original)` avec assertion `count == 1` et relecture physique post-écriture.  

## 1. Synthèse par Mod Maître Source d'Harmonisation

| Mod Maître Validé | Nombre d'injections cascade | Impact en jeu |
| :--- | :---: | :--- |
| `USSEP - Traduction Francaise` | **423** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `LOTD - L'Héritage de l'Enfant de dragon` | **371** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Vokrii - Atouts minimalistes` | **140** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Fanatical Enemies.esp - French` | **97** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Arsenal animé` | **59** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Guivrecroc` | **31** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Mysticisme - Refonte de la magie` | **26** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Citizens of Tamriel` | **24** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)` | **19** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Thaumaturgie - Refonte de l'enchantement` | **9** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Vokriinateur - Morceaux choisis` | **5** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Adamant - Refonte des atouts` | **3** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `SkyDecoctionEN3.0 fr` | **1** | Alignement des patchs dépendants sur la version française canonique du mod maître |
| `Inigo` | **1** | Alignement des patchs dépendants sur la version française canonique du mod maître |

---

## 2. Synthèse par Type d'Enregistrement

| Type d'enregistrement | Nombre de corrections | Objectif |
| :--- | :---: | :--- |
| `CELL FULL` | **540** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `ARMO FULL` | **209** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `NPC_ FULL` | **123** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `SPEL FULL` | **105** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `WEAP FULL` | **54** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `PERK FULL` | **53** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `BOOK FULL` | **31** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `QUST FULL` | **30** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `ALCH FULL` | **28** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `MGEF FULL` | **19** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |
| `NPC_ SHRT` | **17** | Prévention d'écrasement des noms canoniques par l'ordre de chargement |

---

## 3. Top 20 des Patchs les Plus Corrigés

| Fichier Patch Dépendant | Corrections injectées |
| :--- | :---: |
| `WACCF - Correctif des armes, armures, vêtements et objets\weapons armor clothing & clutter fixes.esp.json` | **150** |
| `Vokrii - Apply Spell Conditions Fix.esp - French\vokrii - apply spell conditions fix.esp.json` | **103** |
| `Lux - Refonte de l'éclairage intérieur\Lux.esp.json` | **77** |
| `Ordonnateur - Atouts de Bordeciel\Ordinator - Perks of Skyrim.esp.json` | **35** |
| `(FR - DSD) Lux - Patch Hub\Lux - Wyrmstooth.esp.json` | **28** |
| `Corrections de l'eau et du terrain\Landscape and Water Fixes.esp.json` | **25** |
| `Navigator - Navmesh Fixes\navigator-navfixes.esl.json` | **24** |
| `Navigator - Navmesh Fixes - French\Navigator-NavFixes.esl.json` | **24** |
| `3DNPC - PNJs intéressants\3DNPC.esp.json` | **21** |
| `Amélioration de l'IA\AI Overhaul.esp.json` | **21** |
| `Modpocalypse NPCs - All Vanilla NPCs - French\Modpocalypse NPCs (v3) SSE.esp.json` | **21** |
| `L'Héritage de l'Enfant de dragon - Patches officiels\dbm_isc_patch.esp.json` | **20** |
| `LOTD - Patches officiels\DBM_ISC_Patch.esp.json` | **20** |
| `Modpocalypse NPCs - All Vanilla NPCs\modpocalypse npcs (v3) sse.esp.json` | **19** |
| `(FR - DSD) Lux - Patch Hub\Lux - Legacy of the Dragonborn patch.esp.json` | **17** |
| `Water for ENB [4K]\water for enb (shades of skyrim).esp.json` | **15** |
| `Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level.esp.json` | **14** |
| `ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json` | **12** |
| `Nolvus Awakening Armors Patch - French\nolvus awakening armors patch.esp.json` | **11** |
| `Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | **11** |

---

## 4. Tableau Exhaustif des Modifications Effectives

| Fichier Patch | FormID | Type | Source (EN) | Ancienne valeur | Valeur canonique injectée | Mod Maître Référent |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `Lux - Great Village of Karthwasten patch.esp.json` | `00013979|Skyrim.esm` | `CELL FULL` | Miner's Barracks | Baraquements de Folpertuis | **Baraquements des mineurs** | `unofficial skyrim special edition patch.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `00058B4C|Skyrim.esm` | `CELL FULL` | Nchuand-Zel Control | Poste de contrôle de Nchuand-Zel | **Nchuand-Zel - Poste de contrôle** | `hlioremi.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `02008995|Dawnguard.esm` | `CELL FULL` | Sharpslope Cave | Grotte de la pente raide | **Grotte de la Pente raide** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `00078124|Skyrim.esm` | `CELL FULL` | Raldbthar Deep Market | Grand marché de Raldbthar | **Raldbthar - Grand marché** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0002F83E|Skyrim.esm` | `CELL FULL` | High Gate Ruins Catacombs | Catacombes de la Grande Porte | **Ruines de la Grande porte - Catacombes** | `fanatical enemies.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0001F358|Skyrim.esm` | `CELL FULL` | Ansilvund Burial Chambers | Chambres sépulcrales d'Ansilvund | **Ansilvund - Chambres sépulcrales** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `00054B70|Skyrim.esm` | `CELL FULL` | Mzulft Boilery | Brasserie de Mzulft | **Mzulft - Brasserie** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000152C3|Skyrim.esm` | `CELL FULL` | Alftand Glacial Ruins | Ruines gelées d'Alftand | **Alftand - Ruines gelées** | `Thaumaturgy.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0004C6DD|Skyrim.esm` | `CELL FULL` | Avanchnzel Boilery | Brasserie d'Avanchnzel | **Avanchnzel - Brasserie** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000336FB|Skyrim.esm` | `CELL FULL` | Valthume Catacombs | Catacombes de Valthume | **Valthume - Catacombes** | `fanatical enemies.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000527F2|Skyrim.esm` | `CELL FULL` | Irkngthand Slave Pens | Quartiers des esclaves d'Irkngthand | **Irkngthand - Quartiers des esclaves** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0002031A|Skyrim.esm` | `CELL FULL` | Volunruud Elder's Cairn | Cairn de l'Ancien de Volunruud | **Volunruud - Cairn de l'Ancien** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000466CB|Skyrim.esm` | `CELL FULL` | Irkngthand Sanctuary | Sanctuaire d'Irkngthand | **Irkngthand - Sanctuaire** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Legacy of the Dragonborn patch.esp.json` | `000361F9|Skyrim.esm` | `CELL FULL` | Bthardamz Lower District | Quartier inférieur de Bthardamz | **Bthardamz - Quartier inférieur** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Lucien.esp.json` | `00052CB5|Skyrim.esm` | `CELL FULL` | Irkngthand Arcanex | Arcanex d'Irkngthand | **Irkngthand - Arcanex** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Moon and Star patch.esp.json` | `00037B76|Skyrim.esm` | `CELL FULL` | Avanchnzel Animoncultory | Animachinerie d'Avanchnzel | **Avanchnzel - Animachinerie** | `LegacyoftheDragonborn.esm.json` |
| `Lux - This is Jorrvaskr patch.esp.json` | `0007947A|Skyrim.esm` | `CELL FULL` | Jorrvaskr Living Quarters | Logements de Jorrvaskr | **Jorrvaskr - Logements** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Wyrmstooth.esp.json` | `02124DF0|Wyrmstooth.esp` | `CELL FULL` | Laenius Household | Résidence des Laenius | **Foyer des Laenius** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `020063C5|Wyrmstooth.esp` | `CELL FULL` | The Handsome Hermit Cellar | Sous-sol du Bel Ermite | **Le Bel Ermite - Sous-sol** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02189F49|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Barrow Tower | Tour du tertre de Deinarr | **Tertre de Guivrecroc - Tour** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `021E4FC6|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Barrow Refectory | Réfectoire du tertre de Deinarr | **Tertre de Guivrecroc - Réfectoire** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02229DC4|Wyrmstooth.esp` | `CELL FULL` | Fort Valus Barracks | Baraquements de Valus | **Fort Valus - Baraquements** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `028E2E7C|Wyrmstooth.esp` | `CELL FULL` | Stonehollow Well | Puits du Creux-Pétrifié | **Puits de Valdepierre** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0222C236|Wyrmstooth.esp` | `CELL FULL` | Fort Valus Muster | Salle de rassemblement de Valus | **Fort Valus - Salle de rassemblement** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `020D08A6|Wyrmstooth.esp` | `CELL FULL` | Dimfrost Luminatory | Luminatorium d'Ombreglace | **Sombregivre - Luminatorium** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0200665B|Wyrmstooth.esp` | `CELL FULL` | East Empire Company Tradehouse | Comptoir commercial de la Compagnie de l'Empire... | **Chambre de commerce de la Compagnie de l'Empire...** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `023D7BC7|Wyrmstooth.esp` | `CELL FULL` | Dimfrost Aularium | Aularium d'Ombreglace | **Sombregivre - Aularium** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `022298A8|Wyrmstooth.esp` | `CELL FULL` | Fort Moonwatch Quarters | Quartiers de Gardelune | **Fort Gardelune - Quartiers** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0216EDAA|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Jail | Prison de Deinarr | **Prison de Guivrecroc** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `021B802C|Wyrmstooth.esp` | `CELL FULL` | Dimfrost Boilery | Brasserie d'Ombreglace | **Sombregivre - Brasserie** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `021E3B1F|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Barrow Crypt | Crypte du tertre de Deinarr | **Tertre de Guivrecroc - Crypte** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `028239A3|Wyrmstooth.esp` | `CELL FULL` | Frostwind Folly | Folie de Venglacé | **Folie de Glacevent** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02A810BF|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Barrow Altar | Autel du Tertre de Deinarr | **Tertre de Guivrecroc - Autel** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02006F3B|Wyrmstooth.esp` | `CELL FULL` | Coldwave Crescent | Croissant des Glaces Bleues | **Croissant d'Ondeglace** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `021CBE89|Wyrmstooth.esp` | `CELL FULL` | Dimfrost Boletarium | Boletarium d'Ombreglace | **Sombregivre - Boletarium** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0218E850|Wyrmstooth.esp` | `CELL FULL` | Cragwater Cavern | Caverne d'Eauroc | **Caverne d'Onderoc** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02070DD8|Wyrmstooth.esp` | `CELL FULL` | Wyrmstooth Barrow Temple | Temple du tertre de Deinarr | **Tertre de Guivrecroc - Temple** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02226FBB|Wyrmstooth.esp` | `CELL FULL` | Fort Moonwatch Muster | Salle de rassemblement de Gardelune | **Fort Gardelune - Salle de rassemblement** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `021BF479|Wyrmstooth.esp` | `CELL FULL` | Dimfrost Animonculatory | Animachinerie d'Ombreglace | **Sombregivre - Animachinerie** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02229B3F|Wyrmstooth.esp` | `CELL FULL` | Fort Valus Common House | Maison du peuple de Valus | **Fort Valus - Foyer** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0285A884|Wyrmstooth.esp` | `CELL FULL` | Frostwind Bastion | Bastion de Venglacé | **Bastion de Glacevent** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `024D6212|Wyrmstooth.esp` | `CELL FULL` | Herman's Holdout | Cachette d'Herman | **Refuge d'Herman** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0247C83F|Wyrmstooth.esp` | `CELL FULL` | Krakevisa Midden | Hyposcole de Krakevisa | **Dépotoir de Krakevisa** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `0200C4FD|Wyrmstooth.esp` | `CELL FULL` | Frostvein Mine | Mine de Givreveine | **Mine de Givrefilon** | `Wyrmstooth.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `02272AC1|Wyrmstooth.esp` | `CELL FULL` | Chillwater Mill | Scierie du Givre | **Scierie de Gèleflot** | `Wyrmstooth.esp.json` |
| `jk's palace of the kings.esp.json` | `00097298|Skyrim.esm` | `CELL FULL` | Palace of the Kings, Upstairs | Palais des Rois - Étage | **Palais des rois - Étage** | `unofficial skyrim special edition patch.esp.json` |
| `jk's palace of the kings.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `draugr armor warrior.esl.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00034864|Skyrim.esm` | `CELL FULL` | Fort Sungard Muster | Fort Gardesol - Zone d'appel | **Fort Gardesol - Salle de rassemblement** | `unofficial skyrim special edition patch.esp.json` |
| `3DNPC.esp.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `3DNPC.esp.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `000165AA|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `3DNPC.esp.json` | `000A1A61|Skyrim.esm` | `CELL FULL` | Shriekwind Bastion | Bastion d'Hurlevent | **Bastion de Hurlevent** | `fanatical enemies.esp.json` |
| `3DNPC.esp.json` | `0005554A|Skyrim.esm` | `CELL FULL` | Lost Prospect Mine | La mine perdue | **Mine perdue** | `unofficial skyrim special edition patch.esp.json` |
| `3DNPC.esp.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Ambassade du Thalmor - Chambre d'Elenwen | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00015224|Skyrim.esm` | `CELL FULL` | Redoran's Retreat | Refuge de Redoran | **Refuge de Rédoran** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `3DNPC.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00015295|Skyrim.esm` | `CELL FULL` | Dead Crone Rock | Rocher de la mégère | **Rocher de la Mégère** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `3DNPC.esp.json` | `00013A72|Skyrim.esm` | `CELL FULL` | Corpselight Farm | Ferme du grand voyage | **Ferme du Grand Voyage** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `00015265|Skyrim.esm` | `CELL FULL` | Halldir's Cairn | Cairn de Halldir | **Cairn d'Halldir** | `LegacyoftheDragonborn.esm.json` |
| `3DNPC.esp.json` | `000EF325|Skyrim.esm` | `CELL FULL` | Falkreath Barracks | Baraquements d'Épervine | **Baraquements des gardes d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `Abyss.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `waccf_armor and clothing extension.esp.json` | `000580A2|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `AcousticTemplateFixes.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `AcousticTemplateFixes.esp.json` | `000165B2|Skyrim.esm` | `CELL FULL` | House Gray-Mane | Maison Grisetoison | **Maison du clan Grisetoison** | `unofficial skyrim special edition patch.esp.json` |
| `AcousticTemplateFixes.esp.json` | `00016A03|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `AcousticTemplateFixes.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `AcousticTemplateFixes.esp.json` | `000161FB|Skyrim.esm` | `CELL FULL` | Hollyfrost Farm | Ferme des baies de givre | **Ferme des Baies de givre** | `LegacyoftheDragonborn.esm.json` |
| `AcousticTemplateFixes_Lux.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `AcousticTemplateFixes_Lux.esp.json` | `000165B2|Skyrim.esm` | `CELL FULL` | House Gray-Mane | Maison Grisetoison | **Maison du clan Grisetoison** | `unofficial skyrim special edition patch.esp.json` |
| `AcousticTemplateFixes_Lux.esp.json` | `00016A03|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `AcousticTemplateFixes_Lux.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `AcousticTemplateFixes_Lux.esp.json` | `000161FB|Skyrim.esm` | `CELL FULL` | Hollyfrost Farm | Ferme des baies de givre | **Ferme des Baies de givre** | `LegacyoftheDragonborn.esm.json` |
| `SL01AmuletsSkyrim.esp.json` | `000580A2|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `SL01AmuletsSkyrim.esp.json` | `00097298|Skyrim.esm` | `CELL FULL` | Palace of the Kings, Upstairs | Palais des Rois - Étage | **Palais des rois - Étage** | `unofficial skyrim special edition patch.esp.json` |
| `SL01AmuletsSkyrim.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `SL01AmuletsSkyrim.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `AI Overhaul.esp.json` | `0001365F|Skyrim.esm` | `NPC_ FULL` | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001365F|Skyrim.esm` | `NPC_ SHRT` | Dravynea | Dravynéa | **Dravynea** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001366B|Skyrim.esm` | `NPC_ FULL` | Sondas Drenim | Sondas Drénim | **Sondas Drenim** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `00013B76|Skyrim.esm` | `NPC_ FULL` | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `00013B76|Skyrim.esm` | `NPC_ SHRT` | Leontius | Leontius | **Léontius** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `00014123|Skyrim.esm` | `NPC_ FULL` | Niranye | Niranyë | **Niranye** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001413A|Skyrim.esm` | `NPC_ FULL` | Revyn Sadri | Révyn Sadri | **Revyn Sadri** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001413A|Skyrim.esm` | `NPC_ SHRT` | Revyn | Révyn | **Revyn** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001413D|Skyrim.esm` | `NPC_ FULL` | Ravam Verethi | Ravam Véréthi | **Ravam Verethi** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001C196|Skyrim.esm` | `NPC_ FULL` | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0001C196|Skyrim.esm` | `NPC_ SHRT` | Brelyna | Brélyna | **Brelyna** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `000877AF|Skyrim.esm` | `NPC_ FULL` | Edith | Édith | **Edith** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0401777C|Dragonborn.esm` | `NPC_ FULL` | Varona Nelas | Varona Nélas | **Varona Nelas** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `000138CB|Skyrim.esm` | `CELL FULL` | Thaumaturgist's Hut | La Hutte de la Thaumaturge | **Hutte du thaumaturge** | `citizenscomplete.esp.json` |
| `AI Overhaul.esp.json` | `0002C778|Skyrim.esm` | `CELL FULL` | Iron-Breaker Mine | Mine de Brise-Fer | **Mine de Brise-fer** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `000161EF|Skyrim.esm` | `CELL FULL` | Half-Moon Mill | Scierie Mi-Lune | **Scierie Mi-lune** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `0002C779|Skyrim.esm` | `CELL FULL` | Quicksilver Mine | Mine Vif-Argent | **Mine Vif-argent** | `unofficial skyrim special edition patch.esp.json` |
| `AI Overhaul.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `AI Overhaul.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `AI Overhaul.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `Bloodskal Blade - Tweaks and Enhancements.esp.json` | `0401AEA4|Dragonborn.esm` | `WEAP FULL` | Bloodskal Blade | Lame des Sangskaals | **Lame des Skalsangue** | `unofficial skyrim special edition patch.esp.json` |
| `COTN Addon - Anga's Mill.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Scierie d'Anga - Foyer | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `COTN Angas Mill Addon - Cheesemod Patch.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Scierie d'Anga - Foyer | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `COTN Angas Mill Addon - Embers XD patch.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Scierie d'Anga - Foyer | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `Animated Ice Floes - LotD Patch.esp.json` | `05125EE6|LegacyoftheDragonborn.esm` | `CELL FULL` | Hall of Heroes | Panthéon des héros | **Panthéon des Héros** | `LegacyoftheDragonborn.esm.json` |
| `ap - missile additional starts.esp.json` | `0005B88B|Skyrim.esm` | `CELL FULL` | Fort Greenwall Prison | Prison de Tiremuraille | **Fort Tiremuraille - Prison** | `unofficial skyrim special edition patch.esp.json` |
| `ap - missile additional starts.esp.json` | `0003016A|Skyrim.esm` | `CELL FULL` | Fort Hraggstad Prison | Prison de Hraggstad | **Fort Hraggstad - Prison** | `unofficial skyrim special edition patch.esp.json` |
| `ap - missile additional starts.esp.json` | `00052390|Skyrim.esm` | `CELL FULL` | Fort Dunstad Prison | Prison de Dunstad | **Fort Dunstad - Prison** | `unofficial skyrim special edition patch.esp.json` |
| `Apothecary.esp.json` | `0003EB42|Skyrim.esm` | `MGEF FULL` | Damage Health | Dégâts de santé | **Pénalité de santé** | `unofficial skyrim special edition patch.esp.json` |
| `Apothecary.esp.json` | `00073F5B|Skyrim.esm` | `ALCH FULL` | Potent Frenzy Poison | Poison de frénésie puissant | **Puissant poison de frénésie** | `unofficial skyrim special edition patch.esp.json` |
| `Faction Crossbows.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `Faction Crossbows.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Billyro's Weapons.esp.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `Billyro's Weapons.esp.json` | `00047817|Skyrim.esm` | `CELL FULL` | Skybound Watch Pass | Passage du Cap Célestal | **Passage du cap Célestal** | `LegacyoftheDragonborn.esm.json` |
| `KozakowyFalkaArmor.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `KozakowyFalkaArmor.esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `Eli_Battle Mage Armour.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `Black Mage Armor SE.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `Lords of Coldharbour.esp.json` | `02006429|Dawnguard.esm` | `CELL FULL` | Reaper's Lair | Repaire du Faucheur | **Repaire de faucheur** | `unofficial skyrim special edition patch.esp.json` |
| `DIS_Armor_Fractions.esp.json` | `000BFB55|Skyrim.esm` | `NPC_ FULL` | Keeper Carcette | Carcette la gardienne | **Gardienne Carcette** | `unofficial skyrim special edition patch.esp.json` |
| `WZOblivionArtifacts.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `WZOblivionArtifacts.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres de la Tour Clair-obscur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `ZIA_Complete Pack.esp.json` | `00045F96|Skyrim.esm` | `ARMO FULL` | Spellbreaker | Brise-Sort | **Brise-sort** | `unofficial skyrim special edition patch.esp.json` |
| `ZIA_Complete Pack.esp.json` | `000C891D|Skyrim.esm` | `ARMO FULL` | Necromancer's Amulet | Amulette du Nécromancien | **Amulette du nécromancien** | `unofficial skyrim special edition patch.esp.json` |
| `ZIA_Complete Pack.esp.json` | `0001C4E6|Skyrim.esm` | `WEAP FULL` | The Rueful Axe | Hache du Chagrin | **Hache du chagrin** | `unofficial skyrim special edition patch.esp.json` |
| `ZIA_Complete Pack.esp.json` | `000964C9|Skyrim.esm` | `WEAP FULL` | Blade of Woe | Lame de la Souffrance | **Lame de la souffrance** | `unofficial skyrim special edition patch.esp.json` |
| `ZIA_Complete Pack.esp.json` | `0009CCDC|Skyrim.esm` | `WEAP FULL` | Blade of Woe | Lame de la Souffrance | **Lame de la souffrance** | `unofficial skyrim special edition patch.esp.json` |
| `BOOBIES_potions.esp.json` | `00073F2B|Skyrim.esm` | `MGEF FULL` | Damage Magicka Regen | Dégâts Magie Récupération | **Dégâts de régénération de magie** | `unofficial skyrim special edition patch.esp.json` |
| `BOOBIES_potions.esp.json` | `00073F2C|Skyrim.esm` | `MGEF FULL` | Damage Stamina Regen | Dégâts Vigueur Récupération | **Dégâts de régénération de vigueur** | `unofficial skyrim special edition patch.esp.json` |
| `mihailbanekins.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `mihailbanekins.esp.json` | `00015283|Skyrim.esm` | `CELL FULL` | Fellglow Keep Dungeons | Cachots de Clairlande | **Château de Clairlande - Cachots** | `LegacyoftheDragonborn.esm.json` |
| `mihailbanekins.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres de Clair-Obscur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `BeardMaskFix.esp.json` | `0005ABC4|Skyrim.esm` | `ARMO FULL` | Shrouded Cowl Maskless | Coule sibylline ouverte | **Cagoule sibylline ouverte** | `unofficial skyrim special edition patch.esp.json` |
| `BeardMaskFix.esp.json` | `000D2842|Skyrim.esm` | `ARMO FULL` | Shrouded Cowl | Coule sibylline | **Cagoule sibylline** | `unofficial skyrim special edition patch.esp.json` |
| `BeardMaskFix.esp.json` | `000E1F17|Skyrim.esm` | `ARMO FULL` | Ancient Shrouded Cowl | Coule sibylline antique | **Cagoule sibylline antique** | `LegacyoftheDragonborn.esm.json` |
| `BeardMaskFix.esp.json` | `00105969|Skyrim.esm` | `ARMO FULL` | Worn Shrouded Cowl | Coule sibylline usée | **Cagoule sibylline usée** | `unofficial skyrim special edition patch.esp.json` |
| `BeardMaskFix.esp.json` | `0010EB5D|Skyrim.esm` | `ARMO FULL` | Worn Shrouded Cowl | Coule sibylline usée | **Cagoule sibylline usée** | `unofficial skyrim special edition patch.esp.json` |
| `SUDs.esp.json` | `00065C37|Skyrim.esm` | `ALCH FULL` | Velvet LeChance | La Chance soyeuse | **Chance soyeuse** | `LegacyoftheDragonborn.esm.json` |
| `SUDs.esp.json` | `00065C38|Skyrim.esm` | `ALCH FULL` | White-Gold Tower | La Tour d'Or blanc | **Tour d'Or blanc** | `LegacyoftheDragonborn.esm.json` |
| `SUDs.esp.json` | `00065C39|Skyrim.esm` | `ALCH FULL` | Cliff Racer | Le Course-Falaise | **Course-falaise** | `LegacyoftheDragonborn.esm.json` |
| `SUDs.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `Populated Dungeons Caves Ruins Reborn.esp.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `TreasureHunter.esp.json` | `000F33CE|Skyrim.esm` | `BOOK FULL` | Treasure Map II | Carte au trésor II | **Carte au trésor - Tours de Valtheim** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33D3|Skyrim.esm` | `BOOK FULL` | Treasure Map VIII | Carte au trésor VIII | **Carte au trésor - Rivière de Pondragon** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33D5|Skyrim.esm` | `BOOK FULL` | Treasure Map VII | Carte au trésor VII | **Carte au trésor - Gibet** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33E0|Skyrim.esm` | `BOOK FULL` | Treasure Map X | Carte au trésor X | **Carte au trésor - Lac Ilinalta** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33D0|Skyrim.esm` | `BOOK FULL` | Treasure Map VI | Carte au trésor VI | **Carte au trésor - Korvanjund** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33CF|Skyrim.esm` | `BOOK FULL` | Treasure Map III | Carte au trésor III | **Carte au trésor - Phare de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33D1|Skyrim.esm` | `BOOK FULL` | Treasure Map IV | Carte au trésor IV | **Carte au trésor - Blancherive** | `LegacyoftheDragonborn.esm.json` |
| `TreasureHunter.esp.json` | `000F33D4|Skyrim.esm` | `BOOK FULL` | Treasure Map V | Carte au trésor V | **Carte au trésor - Redoute de la Vallée perdue** | `LegacyoftheDragonborn.esm.json` |
| `ChillwindDephts.esp.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `BGCollectables.esp.json` | `00023FD4|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Markarth** | `hlioremi.esp.json` |
| `BGCollectables.esp.json` | `00013A79|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl de Fortdhiver | **Longère du jarl d'Épervine** | `LegacyoftheDragonborn.esm.json` |
| `mihailbonecolossiandgravelords.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `1FleshColossus.esl.json` | `001091AB|Skyrim.esm` | `NPC_ FULL` | Arch Necromancer | Maître nécromancien | **Archinécromancien** | `fanatical enemies.esp.json` |
| `CCOR_Ordinator.esp.json` | `00051B17|Skyrim.esm` | `PERK FULL` | Matching Light Set | Armure légère uniforme | **Panoplie légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `CCOR_Ordinator.esp.json` | `00107832|Skyrim.esm` | `PERK FULL` | Matching Heavy Set | Armure lourde uniforme | **Panoplie lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `dawnguardarsenal_ccor_patch.esp.json` | `0200DD55|Dawnguard.esm` | `WEAP FULL` | Dawnguard Warhammer | Marteau de la Garde de l'Aube | **Marteau de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `dawnguardarsenal_ccor_patch.esp.json` | `0200D098|Dawnguard.esm` | `WEAP FULL` | Dawnguard War Axe | Hache de la Garde de l'Aube | **Hache de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `dawnguardarsenal_waccf_patch.esp.json` | `0200DD55|Dawnguard.esm` | `WEAP FULL` | Dawnguard Warhammer | Marteau de la Garde de l'Aube | **Marteau de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `dawnguardarsenal_waccf_patch.esp.json` | `0200D098|Dawnguard.esm` | `WEAP FULL` | Dawnguard War Axe | Hache de la Garde de l'Aube | **Hache de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `ZimsImmersiveArtifacts_WACCF_Patch.esp.json` | `00045F96|Skyrim.esm` | `ARMO FULL` | Spellbreaker | Brise-Sort | **Brise-sort** | `unofficial skyrim special edition patch.esp.json` |
| `ZimsImmersiveArtifacts_WACCF_Patch.esp.json` | `0403D2AF|Dragonborn.esm` | `ARMO FULL` | Miraak's Boots | Chaussures de Miraak | **Bottes de Miraak** | `unofficial skyrim special edition patch.esp.json` |
| `ZimsImmersiveArtifacts_WACCF_Patch.esp.json` | `0001C4E6|Skyrim.esm` | `WEAP FULL` | The Rueful Axe | Hache du Chagrin | **Hache du chagrin** | `unofficial skyrim special edition patch.esp.json` |
| `ZimsImmersiveArtifacts_WACCF_Patch.esp.json` | `0401AEA4|Dragonborn.esm` | `WEAP FULL` | Bloodskal Blade | Lame des Sangskaals | **Lame des Skalsangue** | `unofficial skyrim special edition patch.esp.json` |
| `College of Winterhold Quest Start Fixes.esp.json` | `0006A097|Skyrim.esm` | `QUST FULL` | Arniel's Endeavor | L'entreprise d'Arniel | **L'expérience d'Arniel** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `00027F1A|Skyrim.esm` | `CELL FULL` | Reeking Cave | Grotte de Relent | **Grotte puante** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `0002D3E8|Skyrim.esm` | `CELL FULL` | Goldenglow Estate Second Floor | Domaine Lumidor - Premier étage | **Domaine Lumidor - Étage** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `Landscape and Water Fixes.esp.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00016A09|Skyrim.esm` | `CELL FULL` | Erikur's House | Maison d'Erikur | **Maison d'Érikur** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00036ED5|Skyrim.esm` | `CELL FULL` | Severio Pelagia's House | Maison de Severio Pelagia | **Maison de Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `000165AA|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `000A1A61|Skyrim.esm` | `CELL FULL` | Shriekwind Bastion | Bastion d'Hurlevent | **Bastion de Hurlevent** | `fanatical enemies.esp.json` |
| `Landscape and Water Fixes.esp.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Ambassade du Thalmor - Chambre d'Elenwen | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00015274|Skyrim.esm` | `CELL FULL` | Frostflow Lighthouse | Phare d'Hiveronde  | **Phare d'Hiveronde** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00015224|Skyrim.esm` | `CELL FULL` | Redoran's Retreat | Refuge de Redoran | **Refuge de Rédoran** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00015207|Skyrim.esm` | `CELL FULL` | Honningbrew Meadery | Hydromellerie d'hydrhonning | **Hydromellerie d'Hydrhonning** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `Landscape and Water Fixes.esp.json` | `000AE783|Skyrim.esm` | `CELL FULL` | The Midden Dark | L'Hyposcole noire | **Hyposcole noire** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `0003B87D|Skyrim.esm` | `CELL FULL` | Mistveil Keep Jarl's Chambers | Appartements du jarl d'Embruine | **Château d'Embruine - Quartiers du jarl** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `000371DD|Skyrim.esm` | `CELL FULL` | Bleak Falls Sanctum | Sanctuaire des chutes tourmentées | **Sanctuaire des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00047817|Skyrim.esm` | `CELL FULL` | Skybound Watch Pass | Passage du Cap Célestal | **Passage du cap Célestal** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `02007203|Dawnguard.esm` | `CELL FULL` | Volkihar North Tower | Volkihar - Tour nord | **Tour nord de Volkihar** | `fanatical enemies.esp.json` |
| `Landscape and Water Fixes.esp.json` | `0002D3E7|Skyrim.esm` | `CELL FULL` | Goldenglow Estate Basement | Domaine Lumidor - Sous-sol | **Domaine Lumidor - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `00015265|Skyrim.esm` | `CELL FULL` | Halldir's Cairn | Cairn de Halldir | **Cairn d'Halldir** | `LegacyoftheDragonborn.esm.json` |
| `Landscape and Water Fixes.esp.json` | `00015279|Skyrim.esm` | `CELL FULL` | Fort Kastav Prison | Fort Kastav - Prison | **Fort Kastav - Geôles** | `unofficial skyrim special edition patch.esp.json` |
| `Landscape and Water Fixes.esp.json` | `0401BBFB|Dragonborn.esm` | `CELL FULL` | Bristleback Cave | Grotte du sangliogre | **Grotte du Hirsute à broches** | `LegacyoftheDragonborn.esm.json` |
| `Crossbow Integration.esp.json` | `020041D4|Dawnguard.esm` | `NPC_ FULL` | Dawnguard Scout | Éclaireur de la Garde de l'Aube | **Éclaireur de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `man_molagBalShrine.esp.json` | `02019DFE|Dawnguard.esm` | `CELL FULL` | Volkihar Cathedral | Cathédrale de Volkihar | **Chapelle de Volkihar** | `unofficial skyrim special edition patch.esp.json` |
| `man_nocturnalShrine.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `man_nocturnalShrine.esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `4thUnknownAncientShroudedReplacer.esp.json` | `000E1F17|Skyrim.esm` | `ARMO FULL` | Ancient Shrouded Cowl | Coule sibylline antique | **Cagoule sibylline antique** | `LegacyoftheDragonborn.esm.json` |
| `Personalized Music v 6.0.esp.json` | `00016782|Skyrim.esm` | `CELL FULL` | Sadri's Used Wares | Les occasions de Sadri | **Les Occasions de Sadri** | `LegacyoftheDragonborn.esm.json` |
| `Personalized Music v 6.0.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Personalized Music v 6.0.esp.json` | `000161EB|Skyrim.esm` | `CELL FULL` | Sky Haven Temple | Őđŕě Íĺáĺńíîé ăŕâŕíč | **Temple d'Havreciel** | `NewArmoury.esp.json` |
| `Personalized Music v 6.0.esp.json` | `00016787|Skyrim.esm` | `CELL FULL` | Calixto's House of Curiosities | Bazar des curiosités | **Bazar des curiosités de Calixto** | `LegacyoftheDragonborn.esm.json` |
| `Personalized Music v 6.0.esp.json` | `00036ED5|Skyrim.esm` | `CELL FULL` | Severio Pelagia's House | Maison de Severio Pelagia | **Maison de Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `Personalized Music v 6.0.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `Cloaks.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Cloaks.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `DIbella's Blessing.esp.json` | `000274A0|Skyrim.esm` | `NPC_ FULL` | Laelette the Vampire | Laelette | **Laelette la vampire** | `fanatical enemies.esp.json` |
| `DIbella's Blessing.esp.json` | `000BFB55|Skyrim.esm` | `NPC_ FULL` | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `0001365F|Skyrim.esm` | `NPC_ FULL` | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `000877AF|Skyrim.esm` | `NPC_ FULL` | Edith | Édith | **Edith** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `0001C196|Skyrim.esm` | `NPC_ SHRT` | Brelyna | Brélyna | **Brelyna** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `0001365F|Skyrim.esm` | `NPC_ SHRT` | Dravynea | Dravynéa | **Dravynea** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `0001C196|Skyrim.esm` | `NPC_ FULL` | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | `unofficial skyrim special edition patch.esp.json` |
| `DIbella's Blessing.esp.json` | `00014123|Skyrim.esm` | `NPC_ FULL` | Niranye | Niranyë | **Niranye** | `unofficial skyrim special edition patch.esp.json` |
| `mihaildismemberthosemudcrabs.esp.json` | `00015281|Skyrim.esm` | `CELL FULL` | Sea Cave | Cave maritime | **Grotte maritime** | `unofficial skyrim special edition patch.esp.json` |
| `Distinct Interiors.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Distinct Interiors.esp.json` | `00013A71|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `Distinct Interiors - Alternative Steel Armor (CC) patch.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `Distinct Interiors - Embers XD patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Distinct Interiors - Embers XD patch.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `Dawn of Skyrim.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `Dunmeri Furniture.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `mihailesocenturion.esp.json` | `00078124|Skyrim.esm` | `CELL FULL` | Raldbthar Deep Market | Grand marché de Raldbthar | **Raldbthar - Grand marché** | `LegacyoftheDragonborn.esm.json` |
| `Dwueth'Var V2.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `Taberu Animation - LotD Patch.esp.json` | `00065C38|Skyrim.esm` | `ALCH FULL` | White-Gold Tower | Tour d'or blanc | **Tour d'Or blanc** | `LegacyoftheDragonborn.esm.json` |
| `Taberu Animation - LotD Patch.esp.json` | `000D055E|Skyrim.esm` | `ALCH FULL` | Stros M'Kai Rum | Stros M'Kai Rum | **Rhum de Stros M'Kai** | `LegacyoftheDragonborn.esm.json` |
| `Embers XD.esp.json` | `00097298|Skyrim.esm` | `CELL FULL` | Palace of the Kings, Upstairs | Palais des Rois - Étage | **Palais des rois - Étage** | `unofficial skyrim special edition patch.esp.json` |
| `Embers XD.esp.json` | `00015224|Skyrim.esm` | `CELL FULL` | Redoran's Retreat | Refuge Rédoran | **Refuge de Rédoran** | `LegacyoftheDragonborn.esm.json` |
| `Embers XD.esp.json` | `000161EF|Skyrim.esm` | `CELL FULL` | Half-Moon Mill | Scierie Mi-Lune | **Scierie Mi-lune** | `unofficial skyrim special edition patch.esp.json` |
| `Embers XD.esp.json` | `0002C779|Skyrim.esm` | `CELL FULL` | Quicksilver Mine | Mine Vif-Argent | **Mine Vif-argent** | `unofficial skyrim special edition patch.esp.json` |
| `Embers XD.esp.json` | `02007203|Dawnguard.esm` | `CELL FULL` | Volkihar North Tower | Volkihar - Tour nord | **Tour nord de Volkihar** | `fanatical enemies.esp.json` |
| `Embers XD.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `Embers XD.esp.json` | `03002FEC|HearthFires.esm` | `CELL FULL` | Lakeview Manor | Manoir du Lac | **Manoir du lac** | `unofficial skyrim special edition patch.esp.json` |
| `TimingIsEverything.esp.json` | `00090E36|Skyrim.esm` | `QUST FULL` | Kill the Giant (Jarl) | Tuez le géant (jarl) | **Tuez le géant (Jarl)** | `unofficial skyrim special edition patch.esp.json` |
| `TimingIsEverything.esp.json` | `00023EE4|Skyrim.esm` | `QUST FULL` | Shout - learn about word wall | Crier - s'informer sur le mot du mur | **Cri - s'informer sur le mur couvert d'inscriptions** | `unofficial skyrim special edition patch.esp.json` |
| `EpicSolitude.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | Bearclaw | Griffedours | **Bolgeir** | `unofficial skyrim special edition patch.esp.json` |
| `Epic Solitude - Nolvus Integration Patch.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | Bearclaw | Griffedours | **Bolgeir** | `unofficial skyrim special edition patch.esp.json` |
| `Experience Quests Tweak.esp.json` | `00035354|Skyrim.esm` | `QUST FULL` | Siege on the Dragon Cult | Assiégez le Culte du Dragon | **Le siège du culte du Dragon** | `unofficial skyrim special edition patch.esp.json` |
| `companions dialogue bundle - ayop companions patch.esp.json` | `0004B2D9|Skyrim.esm` | `QUST FULL` | Take Up Arms | Prenez les armes | **Prise d'armes** | `unofficial skyrim special edition patch.esp.json` |
| `Companions Dialogue Bundle.esp.json` | `0004B2D9|Skyrim.esm` | `QUST FULL` | Take Up Arms | Prenez les armes | **Prise d'armes** | `unofficial skyrim special edition patch.esp.json` |
| `fanatical enemies - modpocalypse patch.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `fanatical enemies - modpocalypse patch.esp.json` | `000728AD|Skyrim.esm` | `NPC_ FULL` | Thalmor Wizard | Sorcier Thalmor | **Sorcier thalmor** | `fanatical enemies.esp.json` |
| `mihailwraithsandspectres.esp.json` | `02007203|Dawnguard.esm` | `CELL FULL` | Volkihar North Tower | Volkihar - Tour nord | **Tour nord de Volkihar** | `fanatical enemies.esp.json` |
| `mihailwraithsandspectres.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `jks jorrvaskr - skyrim sewers patch.esp.json` | `0007947A|Skyrim.esm` | `CELL FULL` | Jorrvaskr Living Quarters | Logements de Jorrvaskr | **Jorrvaskr - Logements** | `LegacyoftheDragonborn.esm.json` |
| `yumcheese.esp.json` | `00016775|Skyrim.esm` | `CELL FULL` | Niranye's Basement | Sous-sol de Niranyë | **Sous-sol de Niranye** | `unofficial skyrim special edition patch.esp.json` |
| `yumcheese.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `yumcheese.esp.json` | `00016788|Skyrim.esm` | `CELL FULL` | Niranye's House | Maison de Niranyë | **Maison de Niranye** | `unofficial skyrim special edition patch.esp.json` |
| `yumcheese.esp.json` | `00036ED5|Skyrim.esm` | `CELL FULL` | Severio Pelagia's House | Maison de Severio Pelagia | **Maison de Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `yumcheese.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `yumcheese.esp.json` | `000138CB|Skyrim.esm` | `CELL FULL` | Thaumaturgist's Hut | La Hutte de la Thaumaturge | **Hutte du thaumaturge** | `citizenscomplete.esp.json` |
| `yumcheese.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `yumcheese.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `yumcheese.esp.json` | `00016787|Skyrim.esm` | `CELL FULL` | Calixto's House of Curiosities | Bazar des curiosités | **Bazar des curiosités de Calixto** | `LegacyoftheDragonborn.esm.json` |
| `yumcheese.esp.json` | `000C5AA0|Skyrim.esm` | `CELL FULL` | Honningbrew Boilery | Brasserie d'Hydrhonning | **Brasserie d'hydrhonning** | `unofficial skyrim special edition patch.esp.json` |
| `Guard Dialogue Overhaul.esp.json` | `00013986|Skyrim.esm` | `WEAP FULL` | Steel Dagger | Dague d'acier | **Dague en acier** | `unofficial skyrim special edition patch.esp.json` |
| `Guard Dialogue Overhaul.esp.json` | `000139B7|Skyrim.esm` | `WEAP FULL` | Daedric Greatsword | Espadon daedra | **Espadon daedrique** | `unofficial skyrim special edition patch.esp.json` |
| `GG's Thieves Guild Headquarters Lux patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - Additional Hearthfire Dolls patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - Distinct Interiors patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - Faction Crossbows patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - LOTD patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - Nocturnal Shrine patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - Oblivion Artifacts patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - USSEP Patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `GG's Thieves Guild HQ - WACCF Patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Gourmet - Sunhelm.esp.json` | `000722C7|Skyrim.esm` | `ALCH FULL` | Pheasant Roast | Blanc de faisan rôti | **Rôti de faisan** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `000669A2|Skyrim.esm` | `ALCH FULL` | Venison | Venaison crue | **Venaison** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `040248CE|Dragonborn.esm` | `ALCH FULL` | Mazte | Mazté | **Matze** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `000722C2|Skyrim.esm` | `ALCH FULL` | Rabbit Haunch | Cuisse de lapin rôtie | **Cuisse de lapin** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `0300353A|HearthFires.esm` | `ALCH FULL` | Jazbay Crostata | Tarte aux jazbays | **Tarte au jazbay** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `000F431B|Skyrim.esm` | `ALCH FULL` | Cabbage Potato Soup | Soupe de choux et de pommes de terre | **Soupe aux choux et pommes de terre** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `0403BD15|Dragonborn.esm` | `ALCH FULL` | Ash Hopper Meat | Chair de sautecendres | **Viande de sautecendres** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `0300353E|HearthFires.esm` | `ALCH FULL` | Clam Chowder | Soupe de palourdes | **Soupe aux palourdes** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet - Sunhelm.esp.json` | `00065C9C|Skyrim.esm` | `ALCH FULL` | Horse Meat | Cuissot de cheval | **Viande de cheval** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `000722C7|Skyrim.esm` | `ALCH FULL` | Pheasant Roast | Blanc de faisan rôti | **Rôti de faisan** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `040248CE|Dragonborn.esm` | `ALCH FULL` | Mazte | Mazté | **Matze** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `000722C2|Skyrim.esm` | `ALCH FULL` | Rabbit Haunch | Cuisse de lapin rôtie | **Cuisse de lapin** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `000F431B|Skyrim.esm` | `ALCH FULL` | Cabbage Potato Soup | Soupe de choux et de pommes de terre | **Soupe aux choux et pommes de terre** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `0300353E|HearthFires.esm` | `ALCH FULL` | Clam Chowder | Soupe de palourdes | **Soupe aux palourdes** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `00065C9C|Skyrim.esm` | `ALCH FULL` | Horse Meat | Cuissot de cheval | **Viande de cheval** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `000669A2|Skyrim.esm` | `ALCH FULL` | Venison | Venaison crue | **Venaison** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `0300353A|HearthFires.esm` | `ALCH FULL` | Jazbay Crostata | Tarte aux jazbays | **Tarte au jazbay** | `unofficial skyrim special edition patch.esp.json` |
| `Gourmet.esp.json` | `0403BD15|Dragonborn.esm` | `ALCH FULL` | Ash Hopper Meat | Chair de sautecendres | **Viande de sautecendres** | `unofficial skyrim special edition patch.esp.json` |
| `1HSS.esl.json` | `000161EB|Skyrim.esm` | `CELL FULL` | Sky Haven Temple | Őđŕě Íĺáĺńíîé ăŕâŕíč | **Temple d'Havreciel** | `NewArmoury.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000877A7|Skyrim.esm` | `ARMO FULL` | Silver Amethyst Ring | Anneau en argent et améthyste parfait | **Anneau d'argent et d'améthyste** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000877AB|Skyrim.esm` | `ARMO FULL` | Silver Garnet Ring | Anneau en argent et grenat parfait | **Anneau d'argent et de grenat** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F6904|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F690D|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F690E|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F6910|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F690F|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `0009DFF7|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000C5809|Skyrim.esm` | `ARMO FULL` | The Bond of Matrimony | Alliance (Gauche) | **Alliance** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `000F6911|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `0001C4E6|Skyrim.esm` | `WEAP FULL` | The Rueful Axe | Hache du Chagrin | **Hache du chagrin** | `unofficial skyrim special edition patch.esp.json` |
| `Immersive Sounds - Compendium.esp.json` | `00068C79|Skyrim.esm` | `WEAP FULL` | Nord Hero Battleaxe | Hache d'armes de héros nordique | **Hache d'armes du héros** | `unofficial skyrim special edition patch.esp.json` |
| `isd_ravensbeak.esp.json` | `0003F516|Skyrim.esm` | `CELL FULL` | Mistwatch North Tower | Tour nord d'Arquebrumes | **Arquebrumes - Tour nord** | `unofficial skyrim special edition patch.esp.json` |
| `JKs Palace of the Kings - BGCollectables Patch.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `JKs Temple of Dibella - ACE Patch.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `JK's Temple of Dibella.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `jks college of winterhold - 3dnpc patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - ace patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks college of winterhold - ai overhaul patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - ai overhaul patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks college of winterhold - amulets of skyrim patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks college of winterhold - cc - goldbrand patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - cheesemod patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - cheesemod patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks college of winterhold - cheesemod patch.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `jks college of winterhold - cloaks patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - dwueth var patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - konahrik accoutrements patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - lotd patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - remiel patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - sut patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks college of winterhold - tools of kagrenac patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `jks college of winterhold - ussep patch.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `jks college of winterhold - waccf patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `jks jorrvaskr - skyrim sewers patch.esp.json` | `0007947A|Skyrim.esm` | `CELL FULL` | Jorrvaskr Living Quarters | Logements de Jorrvaskr | **Jorrvaskr - Logements** | `LegacyoftheDragonborn.esm.json` |
| `JKs College of Winterhold - 3DNPC Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - ACE Patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs College of Winterhold - AI Overhaul Patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs College of Winterhold - AI Overhaul Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Amulets of Skyrim patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs College of Winterhold - Animated Armory Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - CC - Goldbrand Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Cheesemod patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs College of Winterhold - Cheesemod patch.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `JKs College of Winterhold - Cheesemod patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Cloaks Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Dwueth Var Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Konahrik Accoutrements patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - LOTD Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - Remiel patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - SUT Patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs College of Winterhold - Tools of Kagrenac Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `JKs College of Winterhold - USSEP patch.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `JKs College of Winterhold - WACCF patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `JKs Sky Haven Temple - BGCollectables Patch.esp.json` | `000161EB|Skyrim.esm` | `CELL FULL` | Sky Haven Temple | Őđŕě Íĺáĺńíîé ăŕâŕíč | **Temple d'Havreciel** | `NewArmoury.esp.json` |
| `konahrik_accoutrements.esp.json` | `000AE783|Skyrim.esm` | `CELL FULL` | The Midden Dark | L'Hyposcole noire | **Hyposcole noire** | `LegacyoftheDragonborn.esm.json` |
| `konahrik_accoutrements.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `dbm_relicnotifications.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_relicnotifications.esp.json` | `00095C44|Skyrim.esm` | `CELL FULL` | Hall of Valor | Panthéon des Braves | **Panthéon des braves** | `unofficial skyrim special edition patch.esp.json` |
| `lotd_tcc_clockwork.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_falskaar.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_graycowl.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_ka.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_mas.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_moonpath.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_projectaho.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_teldrynserious.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `lotd_tcc_wyrmstooth.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `bcs_tciy_patch.esp.json` | `000D1955|Skyrim.esm` | `BOOK FULL` | Note from Eltrys | Note d'Eltrys | **Lettre d'Eltrys** | `LegacyoftheDragonborn.esm.json` |
| `dbm_adamant_patch.esp.json` | `050628DE|LegacyoftheDragonborn.esm` | `PERK FULL` | Nerevar's Legacy | Héritage du Nérévar | **Héritage de Nérévar** | `LegacyoftheDragonborn.esm.json` |
| `dbm_aho_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_cheesemod_patch.esp.json` | `00083B04|Skyrim.esm` | `BOOK FULL` | Missive from Fort Snowhawk Stormcloaks | Missive des Sombrages du fort Busard | **Missive des Sombrages** | `LegacyoftheDragonborn.esm.json` |
| `dbm_clockwork_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_crf_patch.esp.json` | `0005D2EA|Skyrim.esm` | `BOOK FULL` | Journal - Faralda's | Journal de Faralda | **Notes de Faralda** | `LegacyoftheDragonborn.esm.json` |
| `dbm_crf_patch.esp.json` | `05125B0D|LegacyoftheDragonborn.esm` | `BOOK FULL` | Scribbled Notes | Note gribouillée | **Notes gribouillées** | `LegacyoftheDragonborn.esm.json` |
| `dbm_falskaar_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_forgottencity_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_iceblademonarch_patch.esp.json` | `0514D595|LegacyoftheDragonborn.esm` | `QUST FULL` | Auryen's Notes: Ice Blade of the Monarch | Notes d'Auryen : Lame glacée du Monarque | **Notes d'Auryen : la Lame glacée du Monarque** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B812|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Erudite (replica) | Anneau d'érudit (réplique) | **Anneau de l'Érudit (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B82A|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Iron Fist (replica) | Anneau de poing de fer (réplique) | **Anneau du Poing de fer (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `05125B05|LegacyoftheDragonborn.esm` | `ARMO FULL` | Vampiric Ring | Anneau vampirique  | **Anneau vampirique** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B813|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of The Beast (replica) | Anneau bestial (réplique) | **Anneau de la Bête (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B830|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind (replica) | Anneau du Vent (réplique) | **Anneau des Vents (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B856|LegacyoftheDragonborn.esm` | `ARMO FULL` | Charmed Necklace (replica) | Collier ensorcellé (réplique) | **Collier ensorcelé (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `051662B7|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone | Pierre-voie ayléide | **Pierre-Voie ayléide** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B829|LegacyoftheDragonborn.esm` | `ARMO FULL` | Wanderlust (replica) | Esprit d'aventure (réplique) | **Soif d'errance (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B825|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Surroundings (replica) | Anneau de mimétisme (réplique) | **Anneau du Caméléon (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B858|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone (replica) | Pierre-voie ayléide (réplique) | **Pierre-Voie ayléide (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0533D7E3|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind | Anneau du vent | **Anneau des Vents** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0533D7E8|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Iron Fist | Anneau de poing de fer | **Anneau du Poing de fer** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `05125AB7|LegacyoftheDragonborn.esm` | `ARMO FULL` | Daedric Sanctuary Amulet | Amulette du sanctuaire daedrique | **Amulette de Dregas Volar** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0533D7E4|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Surroundings | Anneau de mimétisme | **Anneau du Caméléon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `000C891D|Skyrim.esm` | `ARMO FULL` | Necromancer's Amulet | Amulette du Nécromancien | **Amulette du nécromancien** | `unofficial skyrim special edition patch.esp.json` |
| `dbm_isc_patch.esp.json` | `0500B820|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Vipereye (replica) | Anneau d'oeil vipère (réplique) | **Anneau d'Oeil-Vipère (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B831|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Phynaster (replica) | Anneau de Phynastre (réplique) | **Anneau de Phynaste (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0500B85B|LegacyoftheDragonborn.esm` | `ARMO FULL` | Daedric Sanctuary Amulet (replica) | Amulette du sanctuaire daedrique (réplique) | **Amulette de Dregas Volar (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `0503F019|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone | Pierre-voie ayléide | **Pierre-Voie ayléide** | `LegacyoftheDragonborn.esm.json` |
| `dbm_isc_patch.esp.json` | `051662A5|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Vipereye | Anneau d'oeil vipère | **Anneau d'Oeil-Vipère** | `LegacyoftheDragonborn.esm.json` |
| `dbm_mas_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_moonpath_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_newlegion_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_teldrynserious_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_thegraycowlofnocturnal_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_tok_patch.esp.json` | `0500B830|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind (replica) | Anneau du vent (réplique) | **Anneau des Vents (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33CE|Skyrim.esm` | `BOOK FULL` | Treasure Map II | Carte au trésor II | **Carte au trésor - Tours de Valtheim** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D3|Skyrim.esm` | `BOOK FULL` | Treasure Map VIII | Carte au trésor VIII | **Carte au trésor - Rivière de Pondragon** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33E0|Skyrim.esm` | `BOOK FULL` | Treasure Map X | Carte au trésor X | **Carte au trésor - Lac Ilinalta** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D0|Skyrim.esm` | `BOOK FULL` | Treasure Map VI | Carte au trésor VI | **Carte au trésor - Korvanjund** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D2|Skyrim.esm` | `BOOK FULL` | Treasure Map, Fort Neugrad | Carte au trésor de Fort Néograd | **Carte au trésor - Fort Néograd** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D1|Skyrim.esm` | `BOOK FULL` | Treasure Map IV | Carte au trésor IV | **Carte au trésor - Blancherive** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D5|Skyrim.esm` | `BOOK FULL` | Treasure Map VII | Carte au trésor VII | **Carte au trésor - Gibet** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33CF|Skyrim.esm` | `BOOK FULL` | Treasure Map III | Carte au trésor III | **Carte au trésor - Phare de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `dbm_treasurehunter_patch.esp.json` | `000F33D4|Skyrim.esm` | `BOOK FULL` | Treasure Map V | Carte au trésor V | **Carte au trésor - Redoute de la Vallée perdue** | `LegacyoftheDragonborn.esm.json` |
| `dbm_waccf_patch.esp.json` | `0006AF63|Skyrim.esm` | `WEAP FULL` | Trollsbane | Tueur-de-trolls | **Tueur-de-Trolls** | `LegacyoftheDragonborn.esm.json` |
| `dbm_waccf_patch.esp.json` | `000AE086|Skyrim.esm` | `WEAP FULL` | Poacher's Axe | Hache du braconnier | **Hache du Braconnier** | `LegacyoftheDragonborn.esm.json` |
| `dbm_waccf_patch.esp.json` | `000A4DCD|Skyrim.esm` | `ARMO FULL` | Predator's Grace | Grâce du prédateur | **Grâce du Prédateur** | `LegacyoftheDragonborn.esm.json` |
| `dbm_waccf_patch.esp.json` | `000E1643|Skyrim.esm` | `ARMO FULL` | Ironhand Gauntlets | Mains de fer | **Gantelets de Mains-de-Fer** | `LegacyoftheDragonborn.esm.json` |
| `dbm_waccf_patch.esp.json` | `000AB705|Skyrim.esm` | `WEAP FULL` | Bow of the Hunt | Arc du chasseur | **Arc du Chasseur** | `LegacyoftheDragonborn.esm.json` |
| `dbm_wyrmstooth_patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_MidwoodIsle_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DIS_Heavy_Legion.esp.json` | `000D3EAB|Skyrim.esm` | `ARMO FULL` | Penitus Oculatus Bracers | Gantelets du Penitus Oculatus | **Brassards du Penitus Oculatus** | `unofficial skyrim special edition patch.esp.json` |
| `PathOfSorcery.esp.json` | `0008F3EA|Skyrim.esm` | `MGEF FULL` | Muffle | Silence | **Aphasie** | `MysticismMagic.esp.json` |
| `PathOfSorcery.esp.json` | `000B729D|Skyrim.esm` | `MGEF FULL` | Slow | Lenteur | **Langueur** | `MysticismMagic.esp.json` |
| `PathOfSorcery.esp.json` | `000B729F|Skyrim.esm` | `MGEF FULL` | Slow | Lenteur | **Langueur** | `MysticismMagic.esp.json` |
| `PathOfSorcery.esp.json` | `000B72A0|Skyrim.esm` | `MGEF FULL` | Slow | Lenteur | **Lent** | `Thaumaturgy.esp.json` |
| `PathOfSorcery.esp.json` | `000FB992|Skyrim.esm` | `MGEF FULL` | Fortify Shouts | Renfort de Cri | **Renfort de cri** | `unofficial skyrim special edition patch.esp.json` |
| `PathOfSorcery.esp.json` | `00068BCC|Skyrim.esm` | `PERK FULL` | Ward Absorb | Absorption de barrière | **Absorption de protection** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `PathOfSorcery.esp.json` | `000D799C|Skyrim.esm` | `PERK FULL` | Oblivion Binding | Lien condamnatoire | **Lien d'Oblivion** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `RemnantsHammerfell.esp.json` | `0002C779|Skyrim.esm` | `CELL FULL` | Quicksilver Mine | Mine Vif-Argent | **Mine Vif-argent** | `unofficial skyrim special edition patch.esp.json` |
| `The Heart Of Dibella - Quest Expansion.esp.json` | `00023B6C|Skyrim.esm` | `QUST FULL` | The Heart of Dibella | Le Coeur de Dibella | **Le coeur de Dibella** | `unofficial skyrim special edition patch.esp.json` |
| `TheCleverPrisoner.esp.json` | `0009D5A0|Skyrim.esm` | `QUST FULL` | Imperials with Stormcloak Prisoner | Imperials with Stormcloak Prisoner | **Impériaux avec prisonnier Sombrage** | `unofficial skyrim special edition patch.esp.json` |
| `lotd_hub_finh.esp.json` | `000571B4|Skyrim.esm` | `CELL FULL` | Nchuand-Zel Armory | Armurerie de Nchuand-Zel | **Nchuand-Zel - Armurerie** | `hlioremi.esp.json` |
| `lotd_hub_finh.esp.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Quartiers d'Elenwen de l'ambassade | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `lotd_hub_st.esp.json` | `0002D3E8|Skyrim.esm` | `CELL FULL` | Goldenglow Estate Second Floor | Étage de Lumidor | **Domaine Lumidor - Étage** | `LegacyoftheDragonborn.esm.json` |
| `lotd_hub_st.esp.json` | `00065AB5|Skyrim.esm` | `CELL FULL` | Burguk's Cellar | Cave de Burguk | **Cave de Dushnikh Yal** | `unofficial skyrim special edition patch.esp.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `0558B970|LegacyoftheDragonborn.esm` | `NPC_ FULL` | Patero Marassi | Patéro Marassi | **Patero Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `0558B970|LegacyoftheDragonborn.esm` | `NPC_ SHRT` | Prof Marassi | Pr Marassi | **Professeur Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `05270366|LegacyoftheDragonborn.esm` | `NPC_ FULL` | Patero Marassi | Patéro Marassi | **Patero Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `05270366|LegacyoftheDragonborn.esm` | `NPC_ SHRT` | Prof Marassi | Pr Marassi | **Professeur Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `054D1808|LegacyoftheDragonborn.esm` | `NPC_ FULL` | Patero Marassi | Patéro Marassi | **Patero Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `054D1808|LegacyoftheDragonborn.esm` | `NPC_ SHRT` | Prof Marassi | Pr Marassi | **Professeur Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `0534D536|LegacyoftheDragonborn.esm` | `NPC_ FULL` | Patero Marassi | Patéro Marassi | **Patero Marassi** | `LegacyoftheDragonborn.esm.json` |
| `legacyofthedragonborn - npc overhaul.esp.json` | `0534D536|LegacyoftheDragonborn.esm` | `NPC_ SHRT` | Prof Marassi | Pr Marassi | **Professeur Marassi** | `LegacyoftheDragonborn.esm.json` |
| `dbm_tok_replicapatch.esp.json` | `0533D7E3|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind | Anneau du Vent (CC) | **Anneau des Vents** | `LegacyoftheDragonborn.esm.json` |
| `dbm_tok_replicapatch.esp.json` | `05125EE6|LegacyoftheDragonborn.esm` | `CELL FULL` | Hall of Heroes | Salle des Héros | **Panthéon des Héros** | `LegacyoftheDragonborn.esm.json` |
| `The Restless Dead.esp.json` | `0003725E|Skyrim.esm` | `NPC_ FULL` | Guardian Saerek | Saerek le Gardien | **Saerek gardien** | `fanatical enemies.esp.json` |
| `The Restless Dead.esp.json` | `0001528C|Skyrim.esm` | `CELL FULL` | Dustman's Cairn | Cairn des Poussiéreux | **Cairn des poussiéreux** | `unofficial skyrim special edition patch.esp.json` |
| `The Restless Dead.esp.json` | `00037231|Skyrim.esm` | `NPC_ FULL` | Guardian Torsten | Torsten le Gardien | **Torsten gardien** | `fanatical enemies.esp.json` |
| `The Restless Dead.esp.json` | `000CD63E|Skyrim.esm` | `NPC_ FULL` | Dragon Cultist | Adepte du Dragon | **Adepte du dragon** | `fanatical enemies.esp.json` |
| `The Restless Dead.esp.json` | `00015262|Skyrim.esm` | `CELL FULL` | High Gate Ruins | Ruines de la Grande Porte | **Ruines de la Grande porte** | `fanatical enemies.esp.json` |
| `Tools of Kagrenac.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `QuestsAreInSkyrimUSSEP.esp.json` | `00025252|Skyrim.esm` | `QUST FULL` | Striking the Heart | Au coeur de la cible | **Frapper en plein coeur** | `unofficial skyrim special edition patch.esp.json` |
| `QuestsAreInSkyrimUSSEP.esp.json` | `000C18E1|Skyrim.esm` | `QUST FULL` | Family Heirloom | Héritage de famille | **Héritage familial** | `unofficial skyrim special edition patch.esp.json` |
| `QuestsAreInSkyrimUSSEP.esp.json` | `000E3156|Skyrim.esm` | `QUST FULL` | Dragon Seekers | Les chercheurs de dragons | **Les chasseurs de dragons** | `unofficial skyrim special edition patch.esp.json` |
| `QuestsAreInSkyrimUSSEP.esp.json` | `020050BD|Dawnguard.esm` | `QUST FULL` | Deceiving the Herd | Tromper le troupeau | **Tromper la foule** | `unofficial skyrim special edition patch.esp.json` |
| `QuestsAreInSkyrimUSSEP.esp.json` | `0200CE06|Dawnguard.esm` | `QUST FULL` | Rings of Blood Magic | Les anneaux de Magie du sang | **Les Anneaux de Magie du sang** | `unofficial skyrim special edition patch.esp.json` |
| `DBM_RelicNotifications.esp.json` | `00095C44|Skyrim.esm` | `CELL FULL` | Hall of Valor | Panthéon des Braves | **Panthéon des braves** | `unofficial skyrim special edition patch.esp.json` |
| `DBM_RelicNotifications.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_Clockwork.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_Falskaar.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_GrayCowl.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_KA.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_MAS.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_Moonpath.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_ProjectAHO.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_TeldrynSerious.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD_TCC_Wyrmstooth.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `LOTD Skill Trees.esp.json` | `051C661C|LegacyoftheDragonborn.esm` | `PERK FULL` | Excavator Rank 1 | Excavateur I | **Excavation I** | `LegacyoftheDragonborn.esm.json` |
| `LOTD Skill Trees.esp.json` | `051C661D|LegacyoftheDragonborn.esm` | `PERK FULL` | Excavator Rank 2 | Excavateur II | **Excavation II** | `LegacyoftheDragonborn.esm.json` |
| `LOTD Skill Trees.esp.json` | `051C661E|LegacyoftheDragonborn.esm` | `PERK FULL` | Excavator Rank 3 | Excavateur III | **Excavation III** | `LegacyoftheDragonborn.esm.json` |
| `LOTD Skill Trees.esp.json` | `051C6632|LegacyoftheDragonborn.esm` | `PERK FULL` | Surveyor | Inspection | **Prospecteur** | `LegacyoftheDragonborn.esm.json` |
| `LOTD Skill Trees.esp.json` | `051C6633|LegacyoftheDragonborn.esm` | `PERK FULL` | Relic Hunter | Chasse aux reliques | **Chasseur de reliques** | `LegacyoftheDragonborn.esm.json` |
| `DBM_CC_HallOfWonders.esp.json` | `052469A6|LegacyoftheDragonborn.esm` | `BOOK FULL` |  Curator's Guide | Guide du conservateur | **Guide du Conservateur** | `LegacyoftheDragonborn.esm.json` |
| `DBM_CC_HallOfWonders.esp.json` | `05124FD8|LegacyoftheDragonborn.esm` | `QUST FULL` | Adding to the Collection | Adding to the Collection | **Enrichir la collection** | `LegacyoftheDragonborn.esm.json` |
| `BCS_TCIY_Patch.esp.json` | `000D1955|Skyrim.esm` | `BOOK FULL` | Note from Eltrys | Note d'Eltrys | **Lettre d'Eltrys** | `LegacyoftheDragonborn.esm.json` |
| `DBM_Adamant_Patch.esp.json` | `050628DE|LegacyoftheDragonborn.esm` | `PERK FULL` | Nerevar's Legacy | Héritage du Nérévar | **Héritage de Nérévar** | `LegacyoftheDragonborn.esm.json` |
| `DBM_AHO_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ArtifactsofBoethiah_Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `DBM_BGCollectables_Patch.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L’Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `DBM_CheeseMod_Patch.esp.json` | `00083B04|Skyrim.esm` | `BOOK FULL` | Missive from Fort Snowhawk Stormcloaks | Missive des Sombrages du fort Busard | **Missive des Sombrages** | `LegacyoftheDragonborn.esm.json` |
| `DBM_Clockwork_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_CRF_Patch.esp.json` | `0005D2EA|Skyrim.esm` | `BOOK FULL` | Journal - Faralda's | Journal de Faralda | **Notes de Faralda** | `LegacyoftheDragonborn.esm.json` |
| `DBM_CRF_Patch.esp.json` | `05125B0D|LegacyoftheDragonborn.esm` | `BOOK FULL` | Scribbled Notes | Notes griffonnées | **Notes gribouillées** | `LegacyoftheDragonborn.esm.json` |
| `DBM_Falskaar_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ForgottenCity_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_IceBladeMonarch_Patch.esp.json` | `0514D595|LegacyoftheDragonborn.esm` | `QUST FULL` | Auryen's Notes: Ice Blade of the Monarch | Notes d'Auryen : Lame glacée du Monarque | **Notes d'Auryen : la Lame glacée du Monarque** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `000C891D|Skyrim.esm` | `ARMO FULL` | Necromancer's Amulet | Amulette du Nécromancien | **Amulette du nécromancien** | `unofficial skyrim special edition patch.esp.json` |
| `DBM_ISC_Patch.esp.json` | `0500B812|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Erudite (replica) | Anneau d'érudit (réplique) | **Anneau de l'Érudit (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B813|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of The Beast (replica) | Anneau bestial (réplique) | **Anneau de la Bête (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B820|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Vipereye (replica) | Anneau d'oeil vipère (réplique) | **Anneau d'Oeil-Vipère (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B825|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Surroundings (replica) | Anneau de mimétisme (réplique) | **Anneau du Caméléon (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B829|LegacyoftheDragonborn.esm` | `ARMO FULL` | Wanderlust (replica) | Soif d’errance (réplique) | **Soif d'errance (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B82A|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Iron Fist (replica) | Anneau de poing de fer (réplique) | **Anneau du Poing de fer (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B830|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind (replica) | Anneau du Vent (réplique) | **Anneau des Vents (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B831|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Phynaster (replica) | Anneau de Phynastre (réplique) | **Anneau de Phynaste (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B856|LegacyoftheDragonborn.esm` | `ARMO FULL` | Charmed Necklace (replica) | Collier ensorcellé (réplique) | **Collier ensorcelé (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B858|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone (replica) | Pierre-voie ayléide (réplique) | **Pierre-Voie ayléide (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0500B85B|LegacyoftheDragonborn.esm` | `ARMO FULL` | Daedric Sanctuary Amulet (replica) | Amulette de Drégas Volar (réplique) | **Amulette de Dregas Volar (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0503F019|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone | Pierre-voie ayléide | **Pierre-Voie ayléide** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `05125AB7|LegacyoftheDragonborn.esm` | `ARMO FULL` | Daedric Sanctuary Amulet | Amulette de Drégas Volar | **Amulette de Dregas Volar** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `05125B05|LegacyoftheDragonborn.esm` | `ARMO FULL` | Vampiric Ring | Anneau vampirique  | **Anneau vampirique** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `051662A5|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Vipereye | Anneau d'oeil vipère | **Anneau d'Oeil-Vipère** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `051662B7|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ayleid Waystone | Pierre-voie ayléide | **Pierre-Voie ayléide** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0533D7E3|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind | Anneau du vent | **Anneau des Vents** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0533D7E4|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of Surroundings | Anneau de mimétisme | **Anneau du Caméléon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_ISC_Patch.esp.json` | `0533D7E8|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Iron Fist | Anneau de poing de fer | **Anneau du Poing de fer** | `LegacyoftheDragonborn.esm.json` |
| `DBM_MAS_Patch.esp.json` | `05125EE6|LegacyoftheDragonborn.esm` | `CELL FULL` | Hall of Heroes | Panthéon des héros | **Panthéon des Héros** | `LegacyoftheDragonborn.esm.json` |
| `DBM_MAS_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_Moonpath_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_NewLegion_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_TeldrynSerious_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_TheGrayCowlofNocturnal_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `DBM_TOK_Patch.esp.json` | `0500B830|LegacyoftheDragonborn.esm` | `ARMO FULL` | Ring of the Wind (replica) | Anneau du Vent (réplique) | **Anneau des Vents (réplique)** | `LegacyoftheDragonborn.esm.json` |
| `DBM_TOK_Patch.esp.json` | `000DDF7C|Skyrim.esm` | `CELL FULL` | Cellar | Cave d'Anise | **Cave** | `SkyDecoction.esp.json` |
| `DBM_WACCF_Patch.esp.json` | `000A4DCD|Skyrim.esm` | `ARMO FULL` | Predator's Grace | Grâce du prédateur | **Grâce du Prédateur** | `LegacyoftheDragonborn.esm.json` |
| `DBM_WACCF_Patch.esp.json` | `000E1643|Skyrim.esm` | `ARMO FULL` | Ironhand Gauntlets | Mains de fer | **Gantelets de Mains-de-Fer** | `LegacyoftheDragonborn.esm.json` |
| `DBM_WACCF_Patch.esp.json` | `0006AF63|Skyrim.esm` | `WEAP FULL` | Trollsbane | Tueur-de-trolls | **Tueur-de-Trolls** | `LegacyoftheDragonborn.esm.json` |
| `DBM_WACCF_Patch.esp.json` | `000AB705|Skyrim.esm` | `WEAP FULL` | Bow of the Hunt | Arc du chasseur | **Arc du Chasseur** | `LegacyoftheDragonborn.esm.json` |
| `DBM_WACCF_Patch.esp.json` | `000AE086|Skyrim.esm` | `WEAP FULL` | Poacher's Axe | Hache du braconnier | **Hache du Braconnier** | `LegacyoftheDragonborn.esm.json` |
| `DBM_Wyrmstooth_Patch.esp.json` | `05741ACF|LegacyoftheDragonborn.esm` | `CELL FULL` | Dragonborn Hall | Hall de l'Enfant de Dragon | **Hall de l'Enfant de dragon** | `LegacyoftheDragonborn.esm.json` |
| `Lux - USSEP patch.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `Lux - Anga's Mill COTN patch.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Foyer de la scierie d'Anga | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `Lux - Distinct Interiors patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Embers XD patch.esp.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Embers XD patch.esp.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Lux - JK's College patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `Lux - JK's Palace of Kings patch.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `Lux - Water for ENB patch.esp.json` | `000778F1|Skyrim.esm` | `CELL FULL` | Robber's Cove | Val des voleurs | **Val des Voleurs** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Water for ENB patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Lux - Water for ENB patch.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `Lux - Wyrmstooth.esp.json` | `024D6212|Wyrmstooth.esp` | `CELL FULL` | Herman's Holdout | Cachette d'Herman | **Refuge d'Herman** | `Wyrmstooth.esp.json` |
| `Lux.esp.json` | `00027F1A|Skyrim.esm` | `CELL FULL` | Reeking Cave | Grotte de Relent | **Grotte puante** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000580A2|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `Lux.esp.json` | `0002D3E8|Skyrim.esm` | `CELL FULL` | Goldenglow Estate Second Floor | Domaine Lumidor - Premier étage | **Domaine Lumidor - Étage** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00034864|Skyrim.esm` | `CELL FULL` | Fort Sungard Muster | Fort Gardesol - Zone d'appel | **Fort Gardesol - Salle de rassemblement** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000165B2|Skyrim.esm` | `CELL FULL` | House Gray-Mane | Maison Grisetoison | **Maison du clan Grisetoison** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0007284E|Skyrim.esm` | `CELL FULL` | Broken Tower Redoubt | Redoute de la Tour brisée | **Redoute de la tour brisée** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `02008995|Dawnguard.esm` | `CELL FULL` | Sharpslope Cave | Grotte de la pente raide | **Grotte de la Pente raide** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0001677F|Skyrim.esm` | `CELL FULL` | New Gnisis Cornerclub | New Gnisis Cornerclub | **Club de la Nouvelle Gnisis** | `NewArmoury.esp.json` |
| `Lux.esp.json` | `00016BD5|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Faillaise** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `04024D9D|Dragonborn.esm` | `CELL FULL` | Temple Ancestral Tomb | Tombeau ancestral du temple | **Tombeau du temple de Corberoc** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00016A09|Skyrim.esm` | `CELL FULL` | Erikur's House | Maison d'Erikur | **Maison d'Érikur** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00036ED5|Skyrim.esm` | `CELL FULL` | Severio Pelagia's House | Maison de Severio Pelagia | **Maison de Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `02009BDE|Dawnguard.esm` | `CELL FULL` | Dead Drop Falls | Chutes du saut mortel | **Chutes du Saut mortel** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00023FD4|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Markarth** | `hlioremi.esp.json` |
| `Lux.esp.json` | `000165AA|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `02019DFE|Dawnguard.esm` | `CELL FULL` | Volkihar Cathedral | Cathédrale de Volkihar | **Chapelle de Volkihar** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000778F1|Skyrim.esm` | `CELL FULL` | Robber's Cove | Val des voleurs | **Val des Voleurs** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000A1A61|Skyrim.esm` | `CELL FULL` | Shriekwind Bastion | Bastion d'Hurlevent | **Bastion de Hurlevent** | `fanatical enemies.esp.json` |
| `Lux.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Scierie d'Anga - Foyer | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0003D35A|Skyrim.esm` | `CELL FULL` | Honningbrew Basement | Hydromellerie - Sous-sol | **Hydromellerie d'hydrhonning - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0005554A|Skyrim.esm` | `CELL FULL` | Lost Prospect Mine | La mine perdue | **Mine perdue** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Ambassade du Thalmor - Chambre d'Elenwen | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `02008E52|Dawnguard.esm` | `CELL FULL` | Mossy Glen Cave | Grotte de la gorge moussue | **Grotte de la Gorge moussue** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00015274|Skyrim.esm` | `CELL FULL` | Frostflow Lighthouse | Phare d'Hiveronde  | **Phare d'Hiveronde** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `Lux.esp.json` | `00015224|Skyrim.esm` | `CELL FULL` | Redoran's Retreat | Refuge de Redoran | **Refuge de Rédoran** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `04021074|Dragonborn.esm` | `CELL FULL` | Hrodulf's Cellar | Maison de Hrodulf | **Maison de Hrodulf - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00013A79|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl d'Épervine** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `03004849|HearthFires.esm` | `CELL FULL` | Lakeview Manor, Cellar | Manoir du lac, cave | **Manoir du lac - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0002BCD7|Skyrim.esm` | `CELL FULL` | The Midden | L'Hyposcole | **Hyposcole** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00015207|Skyrim.esm` | `CELL FULL` | Honningbrew Meadery | Hydromellerie d'hydrhonning | **Hydromellerie d'Hydrhonning** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00016BD9|Skyrim.esm` | `CELL FULL` | Pawned Prawn | Pawned Prawn | **La Crevette sauteuse** | `Inigo.esp.json` |
| `Lux.esp.json` | `0001521B|Skyrim.esm` | `CELL FULL` | The Icerunner | Le Brise-glace | **Le Brise-Glace** | `NewArmoury.esp.json` |
| `Lux.esp.json` | `00016A03|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `Lux.esp.json` | `000A1793|Skyrim.esm` | `CELL FULL` | Red Wave | Vague rouge | **Le Vague rouge** | `Wyrmstooth.esp.json` |
| `Lux.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `03015154|HearthFires.esm` | `CELL FULL` | Windstad Manor, Cellar | Manoir Bourduvent, cave | **Manoir Bourduvent - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00015294|Skyrim.esm` | `CELL FULL` | Northwind Mine | Mine de Mistral | **Mine du Mistral** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `04017EC2|Dragonborn.esm` | `CELL FULL` | Caerellius House | Maison des Cérellius | **Maison des Caerellius** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0401844F|Dragonborn.esm` | `CELL FULL` | Morvayn Manor Chambers | Chambres du Manoir Morvayn | **Chambres du manoir Morvayn** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000A87C5|Skyrim.esm` | `CELL FULL` | Ravenscar Hollow | Perchoir du corbeau | **Perchoir du Corbeau** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000AE783|Skyrim.esm` | `CELL FULL` | The Midden Dark | L'Hyposcole noire | **Hyposcole noire** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0003B87D|Skyrim.esm` | `CELL FULL` | Mistveil Keep Jarl's Chambers | Appartements du jarl d'Embruine | **Château d'Embruine - Quartiers du jarl** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00065AB5|Skyrim.esm` | `CELL FULL` | Burguk's Cellar | Cave | **Cave de Dushnikh Yal** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00015281|Skyrim.esm` | `CELL FULL` | Sea Cave | Cave maritime | **Grotte maritime** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000371DD|Skyrim.esm` | `CELL FULL` | Bleak Falls Sanctum | Sanctuaire des chutes tourmentées | **Sanctuaire des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `03016A55|HearthFires.esm` | `CELL FULL` | Heljarchen Hall, Cellar | Manoir d'Heljarchen, cave | **Manoir d'Heljarchen - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00015295|Skyrim.esm` | `CELL FULL` | Dead Crone Rock | Rocher de la mégère | **Rocher de la Mégère** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0001529F|Skyrim.esm` | `CELL FULL` | Darklight Tower | Tour Clair-obscur | **Tour Clair-Obscur** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00047817|Skyrim.esm` | `CELL FULL` | Skybound Watch Pass | Passage du Cap Célestal | **Passage du cap Célestal** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `02007203|Dawnguard.esm` | `CELL FULL` | Volkihar North Tower | Volkihar - Tour nord | **Tour nord de Volkihar** | `fanatical enemies.esp.json` |
| `Lux.esp.json` | `04017EC3|Dragonborn.esm` | `CELL FULL` | Temple | Temple | **Temple de Corberoc** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00013A71|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000A9194|Skyrim.esm` | `CELL FULL` | Rebel's Cairn | Cairn du rebelle | **Cairn du Rebelle** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `Lux.esp.json` | `00013A72|Skyrim.esm` | `CELL FULL` | Corpselight Farm | Ferme du grand voyage | **Ferme du Grand Voyage** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `000161FB|Skyrim.esm` | `CELL FULL` | Hollyfrost Farm | Ferme des baies de givre | **Ferme des Baies de givre** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0002D3E7|Skyrim.esm` | `CELL FULL` | Goldenglow Estate Basement | Domaine Lumidor - Sous-sol | **Domaine Lumidor - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `00015265|Skyrim.esm` | `CELL FULL` | Halldir's Cairn | Cairn de Halldir | **Cairn d'Halldir** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00016787|Skyrim.esm` | `CELL FULL` | Calixto's House of Curiosities | Bazar des curiosités | **Bazar des curiosités de Calixto** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `00015279|Skyrim.esm` | `CELL FULL` | Fort Kastav Prison | Fort Kastav - Prison | **Fort Kastav - Geôles** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `000EF325|Skyrim.esm` | `CELL FULL` | Falkreath Barracks | Baraquements d'Épervine | **Baraquements des gardes d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `Lux.esp.json` | `0401BBFB|Dragonborn.esm` | `CELL FULL` | Bristleback Cave | Grotte du sangliogre | **Grotte du Hirsute à broches** | `LegacyoftheDragonborn.esm.json` |
| `Lux.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `Lux.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres Clair-osbcur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `Madmen.esp.json` | `00043BEE|Skyrim.esm` | `NPC_ FULL` | Forsworn Forager | Parjure fourrageur | **Fourrageur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00043BEF|Skyrim.esm` | `NPC_ FULL` | Forsworn Forager | Parjure fourrageur | **Fourrageur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00044263|Skyrim.esm` | `NPC_ FULL` | Forsworn Looter | Parjure rapineur | **Rapineur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00044264|Skyrim.esm` | `NPC_ FULL` | Forsworn Looter | Parjure rapineur | **Rapineur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00044274|Skyrim.esm` | `NPC_ FULL` | Forsworn Pillager | Parjure pilleur | **Pilleur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00044275|Skyrim.esm` | `NPC_ FULL` | Forsworn Pillager | Parjure pilleur | **Pilleur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00044276|Skyrim.esm` | `NPC_ FULL` | Forsworn Pillager | Parjure pilleur | **Pilleur parjure** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `00074F83|Skyrim.esm` | `NPC_ FULL` | Hag | Strige | **Strix** | `fanatical enemies.esp.json` |
| `Madmen.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `Magic of Vile Darkness - NPCS.esp.json` | `0002471A|Skyrim.esm` | `CELL FULL` | Volskygge Passages | Passages de Volskygge | **Volskygge - Passages** | `fanatical enemies.esp.json` |
| `Magic of Vile Darkness - NPCS.esp.json` | `0006CD54|Skyrim.esm` | `QUST FULL` | Coming of Age | L'âge de raison | **Coming of Age** | `unofficial skyrim special edition patch.esp.json` |
| `modpocalypse npcs - added quest fixes.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `modpocalypse npcs - added quest fixes.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `0001E610|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Guerrier pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00037C43|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Archer maraudeur | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `000274A0|Skyrim.esm` | `NPC_ FULL` | Laelette the Vampire | Laelette | **Laelette la vampire** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `0001BCD9|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Guerrier hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00039D4A|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Mage coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `000728AD|Skyrim.esm` | `NPC_ FULL` | Thalmor Wizard | Sorcier Thalmor | **Sorcier thalmor** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00039D43|Skyrim.esm` | `NPC_ FULL` | Bandit Thug | Mage scélérat | **Bandit scélérat** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00039D51|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Mage pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00039D58|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Mage maraudeur | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FFA|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00037C2E|Skyrim.esm` | `NPC_ FULL` | Bandit Thug | Archer scélérat | **Bandit scélérat** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00037C2D|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Archer hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `0001E611|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Guerrier mauradeur | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00037C3C|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Archer pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `0001E60D|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00039D38|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Mage hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `modpocalypse npcs (v3) sse.esp.json` | `00037C35|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Archer coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00016FFA|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001BCD9|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001E60D|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001E610|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001E611|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Malandrin | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000274A0|Skyrim.esm` | `NPC_ FULL` | Laelette the Vampire | Laelette | **Laelette la vampire** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00037C2D|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00037C2E|Skyrim.esm` | `NPC_ FULL` | Bandit Thug | Scélérat | **Bandit scélérat** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00037C35|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00037C3C|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00037C43|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Malandrin | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00039D38|Skyrim.esm` | `NPC_ FULL` | Bandit Outlaw | Hors-la-loi | **Bandit hors-la-loi** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00039D43|Skyrim.esm` | `NPC_ FULL` | Bandit Thug | Scélérat | **Bandit scélérat** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00039D4A|Skyrim.esm` | `NPC_ FULL` | Bandit Highwayman | Coupe-jarret | **Bandit coupe-jarret** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00039D51|Skyrim.esm` | `NPC_ FULL` | Bandit Plunderer | Pillard | **Bandit pillard** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00039D58|Skyrim.esm` | `NPC_ FULL` | Bandit Marauder | Malandrin | **Bandit maraudeur** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00045BE4|Skyrim.esm` | `NPC_ FULL` | Stormcloak Archer | Archer des Sombrages | **Archer sombrage** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000728AD|Skyrim.esm` | `NPC_ FULL` | Thalmor Wizard | Sorcier Thalmor | **Sorcier thalmor** | `fanatical enemies.esp.json` |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `001091AB|Skyrim.esm` | `NPC_ FULL` | Arch Necromancer | Maître nécromancien | **Archinécromancien** | `fanatical enemies.esp.json` |
| `mysticism - spell charge time lowered.esp.json` | `000F95EC|Skyrim.esm` | `SPEL FULL` | Turn Undead | Péril des morts supérieur | **Péril des morts** | `MysticismMagic.esp.json` |
| `Mysticism - Vokrii Compatibility Patch.esp.json` | `057D5826|MysticismMagic.esp` | `SPEL FULL` | Mara's Embrace | Étreinte de Mara | **Étreinte de Mara** | `MysticismMagic.esp.json` |
| `navigator-navfixes.esl.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `00027F1A|Skyrim.esm` | `CELL FULL` | Reeking Cave | Grotte de Relent | **Grotte puante** | `unofficial skyrim special edition patch.esp.json` |
| `navigator-navfixes.esl.json` | `00015295|Skyrim.esm` | `CELL FULL` | Dead Crone Rock | Rocher de la mégère | **Rocher de la Mégère** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `00015281|Skyrim.esm` | `CELL FULL` | Sea Cave | Cave maritime | **Grotte maritime** | `unofficial skyrim special edition patch.esp.json` |
| `navigator-navfixes.esl.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Ambassade du Thalmor - Chambre d'Elenwen | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres Clair-osbcur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `navigator-navfixes.esl.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `navigator-navfixes.esl.json` | `000336FB|Skyrim.esm` | `CELL FULL` | Valthume Catacombs | Catacombes de Valthume | **Valthume - Catacombes** | `fanatical enemies.esp.json` |
| `navigator-navfixes.esl.json` | `0007284E|Skyrim.esm` | `CELL FULL` | Broken Tower Redoubt | Redoute de la Tour brisée | **Redoute de la tour brisée** | `unofficial skyrim special edition patch.esp.json` |
| `navigator-navfixes.esl.json` | `000A1A61|Skyrim.esm` | `CELL FULL` | Shriekwind Bastion | Bastion d'Hurlevent | **Bastion de Hurlevent** | `fanatical enemies.esp.json` |
| `navigator-navfixes.esl.json` | `00015265|Skyrim.esm` | `CELL FULL` | Halldir's Cairn | Cairn de Halldir | **Cairn d'Halldir** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `00015274|Skyrim.esm` | `CELL FULL` | Frostflow Lighthouse | Phare d'Hiveronde  | **Phare d'Hiveronde** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000A87C5|Skyrim.esm` | `CELL FULL` | Ravenscar Hollow | Perchoir du corbeau | **Perchoir du Corbeau** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000A9194|Skyrim.esm` | `CELL FULL` | Rebel's Cairn | Cairn du rebelle | **Cairn du Rebelle** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `00015226|Skyrim.esm` | `CELL FULL` | Reachwater Rock | Rocher d'Eaulointaine  | **Rocher d'Eaulointaine** | `unofficial skyrim special edition patch.esp.json` |
| `navigator-navfixes.esl.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000466CB|Skyrim.esm` | `CELL FULL` | Irkngthand Sanctuary | Sanctuaire d'Irkngthand | **Irkngthand - Sanctuaire** | `LegacyoftheDragonborn.esm.json` |
| `navigator-navfixes.esl.json` | `000371DD|Skyrim.esm` | `CELL FULL` | Bleak Falls Sanctum | Sanctuaire des chutes tourmentées | **Sanctuaire des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `skyrimsewersnavfix.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `Navigator-NavFixes.esl.json` | `00027F1A|Skyrim.esm` | `CELL FULL` | Reeking Cave | Grotte de Relent | **Grotte puante** | `unofficial skyrim special edition patch.esp.json` |
| `Navigator-NavFixes.esl.json` | `0007284E|Skyrim.esm` | `CELL FULL` | Broken Tower Redoubt | Redoute de la Tour brisée | **Redoute de la tour brisée** | `unofficial skyrim special edition patch.esp.json` |
| `Navigator-NavFixes.esl.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000A1A61|Skyrim.esm` | `CELL FULL` | Shriekwind Bastion | Bastion d'Hurlevent | **Bastion de Hurlevent** | `fanatical enemies.esp.json` |
| `Navigator-NavFixes.esl.json` | `000336FB|Skyrim.esm` | `CELL FULL` | Valthume Catacombs | Catacombes de Valthume | **Valthume - Catacombes** | `fanatical enemies.esp.json` |
| `Navigator-NavFixes.esl.json` | `0007DCFC|Skyrim.esm` | `CELL FULL` | Thalmor Embassy, Elenwen's Solar | Ambassade du Thalmor - Chambre d'Elenwen | **Ambassade du Thalmor - Quartiers d'Elenwen** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00015274|Skyrim.esm` | `CELL FULL` | Frostflow Lighthouse | Phare d'Hiveronde  | **Phare d'Hiveronde** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `0001529D|Skyrim.esm` | `CELL FULL` | Dead Men's Respite | Répit des morts | **Répit des Morts** | `hlioremi.esp.json` |
| `Navigator-NavFixes.esl.json` | `00015226|Skyrim.esm` | `CELL FULL` | Reachwater Rock | Rocher d'Eaulointaine  | **Rocher d'Eaulointaine** | `unofficial skyrim special edition patch.esp.json` |
| `Navigator-NavFixes.esl.json` | `000A87C5|Skyrim.esm` | `CELL FULL` | Ravenscar Hollow | Perchoir du corbeau | **Perchoir du Corbeau** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00015281|Skyrim.esm` | `CELL FULL` | Sea Cave | Cave maritime | **Grotte maritime** | `unofficial skyrim special edition patch.esp.json` |
| `Navigator-NavFixes.esl.json` | `000371DD|Skyrim.esm` | `CELL FULL` | Bleak Falls Sanctum | Sanctuaire des chutes tourmentées | **Sanctuaire des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00015295|Skyrim.esm` | `CELL FULL` | Dead Crone Rock | Rocher de la mégère | **Rocher de la Mégère** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000A9194|Skyrim.esm` | `CELL FULL` | Rebel's Cairn | Cairn du rebelle | **Cairn du Rebelle** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `00015265|Skyrim.esm` | `CELL FULL` | Halldir's Cairn | Cairn de Halldir | **Cairn d'Halldir** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `000466CB|Skyrim.esm` | `CELL FULL` | Irkngthand Sanctuary | Sanctuaire d'Irkngthand | **Irkngthand - Sanctuaire** | `LegacyoftheDragonborn.esm.json` |
| `Navigator-NavFixes.esl.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres Clair-osbcur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Men.esp.json` | `0001366B|Skyrim.esm` | `NPC_ FULL` | Sondas Drenim | Sondas Drénim | **Sondas Drenim** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Men.esp.json` | `0001413A|Skyrim.esm` | `NPC_ FULL` | Revyn Sadri | Révyn Sadri | **Revyn Sadri** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Men.esp.json` | `0001413A|Skyrim.esm` | `NPC_ SHRT` | Revyn | Révyn | **Revyn** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Women.esp.json` | `0001365F|Skyrim.esm` | `NPC_ FULL` | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Women.esp.json` | `0001365F|Skyrim.esm` | `NPC_ SHRT` | Dravynea | Dravynéa | **Dravynea** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCS - Eastmarch - Women.esp.json` | `00014123|Skyrim.esm` | `NPC_ FULL` | Niranye | Niranyë | **Niranye** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCs - The Reach - Men.esp.json` | `00013B76|Skyrim.esm` | `NPC_ SHRT` | Leontius | Leontius | **Léontius** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCs - The Reach - Men.esp.json` | `00013B76|Skyrim.esm` | `NPC_ FULL` | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCs - The Thieves Guild - Men.esp.json` | `00013380|Skyrim.esm` | `NPC_ FULL` | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCs - Whiterun - Men.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `NITHI NPCs - Whiterun - Men.esp.json` | `00065657|Skyrim.esm` | `NPC_ SHRT` | Erik | Erik | **Érik** | `unofficial skyrim special edition patch.esp.json` |
| `Nolvus Awakening AI Patch.esp.json` | `000877AF|Skyrim.esm` | `NPC_ FULL` | Edith | Édith | **Edith** | `unofficial skyrim special edition patch.esp.json` |
| `Nolvus Awakening AI Patch.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Forteresse Froidepierre | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening armors balance patch.esp.json` | `0003E908|Skyrim.esm` | `CELL FULL` | Chillwind Depths | Tréfonds d'Aprebise | **Tréfonds d'Âprebise** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening armors patch.esp.json` | `0301E83D|Dragonborn.esm` | `NPC_ FULL` | Reaver Marauder | Archer maraudeur des Ravageurs | **Maraudeur ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E81F|Dragonborn.esm` | `NPC_ FULL` | Reaver Outlaw | Archer hors-la-loi des Ravageurs | **Hors-la-loi ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `000BFB55|Skyrim.esm` | `NPC_ FULL` | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E839|Dragonborn.esm` | `NPC_ FULL` | Reaver Plunderer | Guerrier pillard des Ravageurs | **Pillard ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E836|Dragonborn.esm` | `NPC_ FULL` | Reaver Highwayman | Guerrier coupe-jarret des Ravageurs | **Coupe-jarret ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E834|Dragonborn.esm` | `NPC_ FULL` | Reaver Thug | Archer scélérat des Ravageurs | **Voyou ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E837|Dragonborn.esm` | `NPC_ FULL` | Reaver Highwayman | Archer coupe-jarret des Ravageurs | **Coupe-jarret ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E83C|Dragonborn.esm` | `NPC_ FULL` | Reaver Marauder | Guerrier maraudeur des Ravageurs | **Maraudeur ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E833|Dragonborn.esm` | `NPC_ FULL` | Reaver Thug | Guerrier scélérat des Ravageurs | **Voyou ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E81E|Dragonborn.esm` | `NPC_ FULL` | Reaver Outlaw | Guerrier hors-la-loi des Ravageurs | **Hors-la-loi ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening armors patch.esp.json` | `0301E83A|Dragonborn.esm` | `NPC_ FULL` | Reaver Plunderer | Archer pillard des Ravageurs | **Pillard ravageur** | `fanatical enemies.esp.json` |
| `nolvus awakening clothes patch.esp.json` | `0007947A|Skyrim.esm` | `CELL FULL` | Jorrvaskr Living Quarters | Logements de Jorrvaskr | **Jorrvaskr - Logements** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening clothes patch.esp.json` | `00013987|Skyrim.esm` | `WEAP FULL` | Steel Greatsword | Espadon en acier | **Espadon d'acier** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening clothes patch.esp.json` | `000AE087|Skyrim.esm` | `WEAP FULL` | Briarheart Geis | 5 points de dégâts supplémentaires aux Nordiques. | **Geis de Roncecoeur** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening clothes patch.esp.json` | `0010EB62|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening combat & enemies patch.esp.json` | `000161EB|Skyrim.esm` | `CELL FULL` | Sky Haven Temple | Őđŕě Íĺáĺńíîé ăŕâŕíč | **Temple d'Havreciel** | `NewArmoury.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `0001366B|Skyrim.esm` | `NPC_ FULL` | Sondas Drenim | Sondas Drénim | **Sondas Drenim** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `000877AF|Skyrim.esm` | `NPC_ FULL` | Edith | Édith | **Edith** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `00023A97|Skyrim.esm` | `NPC_ FULL` | Dwarven Sphere Guardian | Sphère gardienne dwemer | **Sphère dwemer gardienne** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `0010EC86|Skyrim.esm` | `NPC_ FULL` | Dwarven Spider Worker | Araignée travailleuse dwemer | **Araignée dwemer ouvrière** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `000728AD|Skyrim.esm` | `NPC_ FULL` | Thalmor Wizard | Sorcier Thalmor | **Sorcier thalmor** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `00013380|Skyrim.esm` | `NPC_ FULL` | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `00104F46|Skyrim.esm` | `NPC_ FULL` | White Stag | Cerf blanc | **Renne blanc** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `000274A0|Skyrim.esm` | `NPC_ FULL` | Laelette the Vampire | Laelette | **Laelette la vampire** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `00027498|Skyrim.esm` | `NPC_ FULL` | Stormcloak Soldier | Soldat Sombrage | **Soldat des Sombrages** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level mult.esp.json` | `0001365F|Skyrim.esm` | `NPC_ SHRT` | Dravynea | Dravynéa | **Dravynea** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000EA32C|Skyrim.esm` | `NPC_ FULL` | Stormcloak Commander | Commandant sombrage | **Commandant Sombrage** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000F62F0|Skyrim.esm` | `NPC_ FULL` | Rift Guard | Garde de la Brèche | **Garde de Faillaise** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000F62EF|Skyrim.esm` | `NPC_ FULL` | Rift Guard | Garde de la Brèche | **Garde de Faillaise** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00051B4C|Skyrim.esm` | `NPC_ FULL` | Stormcloak Commander | Commandant sombrage | **Commandant Sombrage** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00023A97|Skyrim.esm` | `NPC_ FULL` | Dwarven Sphere Guardian | Sphère gardienne dwemer | **Sphère dwemer gardienne** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `0010EC86|Skyrim.esm` | `NPC_ FULL` | Dwarven Spider Worker | Araignée travailleuse dwemer | **Araignée dwemer ouvrière** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000728AD|Skyrim.esm` | `NPC_ FULL` | Thalmor Wizard | Sorcier Thalmor | **Sorcier thalmor** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `0200CFBB|Dawnguard.esm` | `NPC_ FULL` | Dwarven Spider Worker | Araignée travailleuse dwemer | **Araignée dwemer ouvrière** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | Dremora Valkynaz | Valkynaz drémora | **Drémora Valkynaz** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00013380|Skyrim.esm` | `NPC_ FULL` | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000274A0|Skyrim.esm` | `NPC_ FULL` | Laelette the Vampire | Laelette | **Laelette la vampire** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00027498|Skyrim.esm` | `NPC_ FULL` | Stormcloak Soldier | Soldat Sombrage | **Soldat des Sombrages** | `fanatical enemies.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `00060ABA|Skyrim.esm` | `NPC_ FULL` | Thalmor Soldier | Soldat thalmor | **Soldat Thalmor** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening combat scaling overhaul - enemy level.esp.json` | `000CD63E|Skyrim.esm` | `NPC_ FULL` | Dragon Cultist | Adepte du Dragon | **Adepte du dragon** | `fanatical enemies.esp.json` |
| `nolvus awakening crafting patch.esp.json` | `000F5CB6|Skyrim.esm` | `BOOK FULL` | Poison Recipe - Damage Health | Recette de poison : dégâts de santé | **Recette - Poison de pénalité de santé** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening crafting patch.esp.json` | `000F5CBD|Skyrim.esm` | `BOOK FULL` | Potion Recipe - Resist Fire | Recette de potion : résistance au feu | **Recette - Potion de résistance au feu** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening crafting patch.esp.json` | `000F5CB5|Skyrim.esm` | `BOOK FULL` | Poison Recipe - Damage Health | Recette de poison : dégâts de santé | **Recette - Poison de pénalité de santé** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening crafting patch.esp.json` | `000F5CAF|Skyrim.esm` | `BOOK FULL` | Potion Recipe - Restore Health | Recette de potion : restauration de santé | **Recette - Potion de restauration de santé** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening crafting patch.esp.json` | `000F5CBF|Skyrim.esm` | `BOOK FULL` | Potion Recipe - Resist Frost | Recette de potion : résistance au froid | **Recette - Potion de résistance à la glace** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening dlc patch.esp.json` | `000AE087|Skyrim.esm` | `WEAP FULL` | Briarheart Geis | 5 points de dégâts supplémentaires aux Nordiques. | **Geis de Roncecoeur** | `LegacyoftheDragonborn.esm.json` |
| `Nolvus Awakening Experience Integration.esp.json` | `00023B6C|Skyrim.esm` | `QUST FULL` | The Heart of Dibella | Le Cœur de Dibella | **Le coeur de Dibella** | `unofficial skyrim special edition patch.esp.json` |
| `Nolvus Awakening Experience Integration.esp.json` | `00035354|Skyrim.esm` | `QUST FULL` | Siege on the Dragon Cult | Le siège du culte des dragons | **Le siège du culte du Dragon** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening experience integration.esp.json` | `00023B6C|Skyrim.esm` | `QUST FULL` | The Heart of Dibella | Le Cœur de Dibella | **Le coeur de Dibella** | `unofficial skyrim special edition patch.esp.json` |
| `nolvus awakening experience integration.esp.json` | `00035354|Skyrim.esm` | `QUST FULL` | Siege on the Dragon Cult | Le siège du culte des dragons | **Le siège du culte du Dragon** | `unofficial skyrim special edition patch.esp.json` |
| `Nolvus Awakening Interior Patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Nolvus Awakening Interior Patch.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `Nolvus Awakening Interior Patch.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `nolvus awakening lighting patch.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `nolvus awakening lighting patch.esp.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening lighting patch.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening lighting patch.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `nolvus awakening perk patch.esp.json` | `00049507|Skyrim.esm` | `MGEF FULL` | Fortify Stamina | Renfort de vigueur | **Fortify Stamina** | `Thaumaturgy.esp.json` |
| `nolvus awakening perk patch.esp.json` | `00049504|Skyrim.esm` | `MGEF FULL` | Fortify Magicka | Renfort de magie | **Fortify Magicka** | `Thaumaturgy.esp.json` |
| `nolvus awakening perk patch.esp.json` | `0008F3EA|Skyrim.esm` | `MGEF FULL` | Muffle | Silence | **Aphasie** | `MysticismMagic.esp.json` |
| `nolvus awakening vokriinator black integration.esp.json` | `00106256|Skyrim.esm` | `PERK FULL` | Ravage | Ravage | **Ravager** | `Vokriinator Black.esp.json` |
| `nolvus awakening vokriinator black integration.esp.json` | `00106257|Skyrim.esm` | `PERK FULL` | Ravage | Ravage | **Ravager** | `Vokriinator Black.esp.json` |
| `nolvus awakening water patch.esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `nolvus awakening water patch.esp.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening weapons patch.esp.json` | `000F71CD|Skyrim.esm` | `WEAP FULL` | Dragonbane | Fléau des dragons | **Mort-Dragon** | `NewArmoury.esp.json` |
| `nolvus awakening weapons patch.esp.json` | `000F71CF|Skyrim.esm` | `WEAP FULL` | Dragonbane | Fléau des dragons | **Mort-Dragon** | `NewArmoury.esp.json` |
| `nolvus awakening weapons patch.esp.json` | `000F71CE|Skyrim.esm` | `WEAP FULL` | Dragonbane | Fléau des dragons | **Mort-Dragon** | `NewArmoury.esp.json` |
| `nolvus awakening weapons patch.esp.json` | `000F71D0|Skyrim.esm` | `WEAP FULL` | Dragonbane | Fléau des dragons | **Mort-Dragon** | `NewArmoury.esp.json` |
| `nolvus awakening weapons patch.esp.json` | `000F1AC1|Skyrim.esm` | `WEAP FULL` | Dragonbane | Fléau des dragons | **Mort-Dragon** | `NewArmoury.esp.json` |
| `mihailogrim.esp.json` | `00034955|Skyrim.esm` | `CELL FULL` | Fort Amol Prison | Prison d'Amol | **Fort Amol - Prison** | `LegacyoftheDragonborn.esm.json` |
| `mihailogrim.esp.json` | `00015279|Skyrim.esm` | `CELL FULL` | Fort Kastav Prison | Geôles de Kastav | **Fort Kastav - Geôles** | `unofficial skyrim special edition patch.esp.json` |
| `ordinator - no timed block.esp.json` | `00106253|Skyrim.esm` | `PERK FULL` | Block Runner | Courir en parant | **Course parée** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `ordinator - no directional power attacks - balanced.esp.json` | `0003AF81|Skyrim.esm` | `PERK FULL` | Furious Strength | Force incontrôlable | **Force furieuse** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000D8C32|Skyrim.esm` | `MGEF FULL` | Quick Reflexes On Target | Réflexes sur la cible | **Réflexes sur cible** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000B72A0|Skyrim.esm` | `MGEF FULL` | Slow | Langueur | **Lent** | `Thaumaturgy.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `0003AF81|Skyrim.esm` | `PERK FULL` | Furious Strength | Force incontrôlable | **Force furieuse** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00051B17|Skyrim.esm` | `PERK FULL` | Matching Light Set | Armure légère uniforme | **Panoplie légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00051B1B|Skyrim.esm` | `PERK FULL` | Light Armor Fit | Armure légère ajustée | **Tenue légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00052D50|Skyrim.esm` | `PERK FULL` | Disciplined Fighter | Combattant discipliné | **Discipline de combat** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00052D52|Skyrim.esm` | `PERK FULL` | Ferocious Strength | Force effroyable | **Force féroce** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00058201|Skyrim.esm` | `PERK FULL` | Trickster | Fourbe | **Arnaqueur** | `Vokriinator Black.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00058F63|Skyrim.esm` | `PERK FULL` | Ranger | Garde | **Garde forestier** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00058F6F|Skyrim.esm` | `PERK FULL` | Heavy Armor Fit | Armure lourde ajustée | **Tenue lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00058F75|Skyrim.esm` | `PERK FULL` | Kinship | Affinité | **Parenté** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00058F7A|Skyrim.esm` | `PERK FULL` | Salesman | Vendeur | **Vente universelle** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00059B76|Skyrim.esm` | `PERK FULL` | Master of the Mind | Maître de l'illusion | **Maîtrise psychique** | `Vokriinator Black.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079342|Skyrim.esm` | `PERK FULL` | One-Handed Mastery | Maîtrise à une main | **Maîtrise des armes à une main** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079343|Skyrim.esm` | `PERK FULL` | One-Handed Mastery | Maîtrise à une main | **Maîtrise des armes à une main** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079344|Skyrim.esm` | `PERK FULL` | One-Handed Mastery | Maîtrise à une main | **Maîtrise des armes à une main** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079345|Skyrim.esm` | `PERK FULL` | One-Handed Mastery | Maîtrise à une main | **Maîtrise des armes à une main** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079346|Skyrim.esm` | `PERK FULL` | Two-Handed Mastery | Maîtrise à deux mains | **Maîtrise des armes à deux mains** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079347|Skyrim.esm` | `PERK FULL` | Two-Handed Mastery | Maîtrise à deux mains | **Maîtrise des armes à deux mains** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079348|Skyrim.esm` | `PERK FULL` | Two-Handed Mastery | Maîtrise à deux mains | **Maîtrise des armes à deux mains** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `0007935E|Skyrim.esm` | `PERK FULL` | Heavy Armor Mastery | Maîtrise d'armure lourde | **Maîtrise de l'armure lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079361|Skyrim.esm` | `PERK FULL` | Heavy Armor Mastery | Maîtrise d'armure lourde | **Maîtrise de l'armure lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079362|Skyrim.esm` | `PERK FULL` | Heavy Armor Mastery | Maîtrise d'armure lourde | **Maîtrise de l'armure lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079374|Skyrim.esm` | `PERK FULL` | Heavy Armor Mastery | Maîtrise d'armure lourde | **Maîtrise de l'armure lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079376|Skyrim.esm` | `PERK FULL` | Light Armor Mastery | Maîtrise d'armure légère | **Maîtrise de l'armure légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079389|Skyrim.esm` | `PERK FULL` | Light Armor Mastery | Maîtrise d'armure légère | **Maîtrise de l'armure légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079391|Skyrim.esm` | `PERK FULL` | Light Armor Mastery | Maîtrise d'armure légère | **Maîtrise de l'armure légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00079392|Skyrim.esm` | `PERK FULL` | Light Armor Mastery | Maîtrise d'armure légère | **Maîtrise de l'armure légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000BABE4|Skyrim.esm` | `PERK FULL` | One-Handed Mastery | Maîtrise à une main | **Maîtrise des armes à une main** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000BABE8|Skyrim.esm` | `PERK FULL` | Two-Handed Mastery | Maîtrise à deux mains | **Maîtrise des armes à deux mains** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000BCD2A|Skyrim.esm` | `PERK FULL` | Heavy Armor Mastery | Maîtrise d'armure lourde | **Maîtrise de l'armure lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `000BE123|Skyrim.esm` | `PERK FULL` | Light Armor Mastery | Maîtrise d'armure légère | **Maîtrise de l'armure légère** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00105F26|Skyrim.esm` | `PERK FULL` | Treasure Hunter | Chasseur de trésor | **Chasseur de trésors** | `Vokriinator Black.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00106253|Skyrim.esm` | `PERK FULL` | Block Runner | Courir en bloquant | **Course parée** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `Ordinator - Perks of Skyrim.esp.json` | `00107832|Skyrim.esm` | `PERK FULL` | Matching Heavy Set | Armure lourde uniforme | **Panoplie lourde** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `PaarthurnaxQuestExpansion.esp.json` | `000E3E67|Skyrim.esm` | `QUST FULL` | Dragon Hunting | La traque du dragon | **La chasse au dragon** | `unofficial skyrim special edition patch.esp.json` |
| `AdditionalHearthfireDolls.esp.json` | `00097298|Skyrim.esm` | `CELL FULL` | Palace of the Kings, Upstairs | Palais des Rois - Étage | **Palais des rois - Étage** | `unofficial skyrim special edition patch.esp.json` |
| `AdditionalHearthfireDolls.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `AdditionalHearthfireDolls.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `raequestrequirements.esp.json` | `00045A1D|Skyrim.esm` | `CELL FULL` | Mistveil Keep Barracks | Baraquements de Fort-Voilance | **Baraquements d'Embruine** | `hlioremi.esp.json` |
| `raequestrequirements.esp.json` | `000EF325|Skyrim.esm` | `CELL FULL` | Falkreath Barracks | Baraquements des gardes d’Épervine | **Baraquements des gardes d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `raequestrequirements.esp.json` | `00036ED6|Skyrim.esm` | `CELL FULL` | Guard Barracks | Baraquements des gardes | **Baraquements de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `hliiremilotd.esp.json` | `05125C71|LegacyoftheDragonborn.esm` | `CELL FULL` | East Exhibit Halls | Salles d'exposition Est | **Salles d'Expositions Est** | `LegacyoftheDragonborn.esm.json` |
| `hliiremilotd.esp.json` | `05125EE6|LegacyoftheDragonborn.esm` | `CELL FULL` | Hall of Heroes | Panthéon des héros | **Panthéon des Héros** | `LegacyoftheDragonborn.esm.json` |
| `NW_Sons_of_Skyrim.esp.json` | `00013818|Skyrim.esm` | `CELL FULL` | Jarl's Longhouse | Longère du jarl | **Longère du jarl de Fortdhiver** | `unofficial skyrim special edition patch.esp.json` |
| `Ryn's White River Watch.esp.json` | `000151F9|Skyrim.esm` | `CELL FULL` | White River Watch | Observatoire de la Rivière blanche | **Observatoire de la rivière Blanche** | `LegacyoftheDragonborn.esm.json` |
| `1NamelessSaber.esl.json` | `000DD216|Skyrim.esm` | `CELL FULL` | Solitude Catacombs | Solitude Catacombs | **Catacombes de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `Sacrosanct - Vampires of Skyrim.esp.json` | `020149A9|Dawnguard.esm` | `MGEF FULL` | Tainted Blood of the Ancients | Sang souillé des Anciens | **Sang souillé des anciens** | `unofficial skyrim special edition patch.esp.json` |
| `mihailscampstandalone.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `mihailscampstandalone.esp.json` | `00015283|Skyrim.esm` | `CELL FULL` | Fellglow Keep Dungeons | Cachots de Clairlande | **Château de Clairlande - Cachots** | `LegacyoftheDragonborn.esm.json` |
| `mihailscampstandalone.esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Chambres de Clair-Obscur | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `Abyss_USSEP.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `Shadow of Skyrim.esp.json` | `00095C44|Skyrim.esm` | `CELL FULL` | Hall of Valor | Panthéon des Braves | **Panthéon des braves** | `unofficial skyrim special edition patch.esp.json` |
| `GG's Thieves Guild Headquarters.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Skyrim Food Expansion - Replacer.esp.json` | `0010D666|Skyrim.esm` | `ALCH FULL` | Gourd | Courge | **Gourde** | `unofficial skyrim special edition patch.esp.json` |
| `Skyrim Food Expansion Replacer - Gourmet Patch.esp.json` | `0010D666|Skyrim.esm` | `ALCH FULL` | Gourd | Courge | **Gourde** | `unofficial skyrim special edition patch.esp.json` |
| `Skyrim Food Expansion Replacer - Survival Mode.esp.json` | `0010D666|Skyrim.esm` | `ALCH FULL` | Gourd | Courge | **Gourde** | `unofficial skyrim special edition patch.esp.json` |
| `Sons of Nirn - Whiterun.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | `unofficial skyrim special edition patch.esp.json` |
| `NW_Sons_of_Skyrim - My fixes by Xtudo.esp.json` | `0009E023|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `NW_Sons_of_Skyrim - My fixes by Xtudo.esp.json` | `0010EB62|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `NW_Sons_of_Skyrim - My fixes by Xtudo.esp.json` | `0010EB63|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `NW_Sons_of_Skyrim - My fixes by Xtudo.esp.json` | `0010EB64|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `NW_Sons_of_Skyrim - My fixes by Xtudo.esp.json` | `0010EB65|Skyrim.esm` | `ARMO FULL` | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `SMIM-SE-Merged-All.esp.json` | `00016209|Skyrim.esm` | `CELL FULL` | Anga's Mill Common House | Scierie d'Anga - Foyer | **Scierie d'Anga** | `unofficial skyrim special edition patch.esp.json` |
| `SMIM-SE-Merged-All.esp.json` | `000161FB|Skyrim.esm` | `CELL FULL` | Hollyfrost Farm | Ferme des baies de givre | **Ferme des Baies de givre** | `LegacyoftheDragonborn.esm.json` |
| `SteelthornReplacer.esp.json` | `00013986|Skyrim.esm` | `WEAP FULL` | Steel Dagger | Dague d'acier | **Dague en acier** | `unofficial skyrim special edition patch.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `00016BD5|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Faillaise** | `unofficial skyrim special edition patch.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `00023FD4|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Markarth** | `hlioremi.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `000165AA|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Blancherive** | `unofficial skyrim special edition patch.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `000CAB92|Skyrim.esm` | `CELL FULL` | Arch-Mage's Quarters | Quartiers de l'archimage | **Quartiers de l'Archimage** | `MysticismMagic.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `00016A03|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Solitude** | `LegacyoftheDragonborn.esm.json` |
| `SolitudeTempleFrescoes.esp.json` | `00013A71|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole d'Épervine** | `unofficial skyrim special edition patch.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
| `SolitudeTempleFrescoes.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `SolitudeTempleFrescoes.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `Thaumaturgy - USSEP - Patch.esp.json` | `000DDD64|Skyrim.esm` | `WEAP FULL` | Honed Ancient Nord Battle Axe of Frost | Hache d'armes nordique antique affûtée de glace | **Hache d'armes nordique antique de glace affûtée** | `Thaumaturgy.esp.json` |
| `Distinct JK's Temple of Dibella.esp.json` | `0003EA9D|Skyrim.esm` | `CELL FULL` | Inner Sanctum | Sanctuaire intérieur | **Temple de Dibella - Sanctuaire intérieur** | `hlioremi.esp.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000AB702|Skyrim.esm` | `WEAP FULL` | Gauldur Blackblade | Gauldur Noirlame | **Lame noire de Gauldur** | `LegacyoftheDragonborn.esm.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000F5D1A|Skyrim.esm` | `WEAP FULL` | Gauldur Blackblade | Gauldur Noirlame | **Lame noire de Gauldur** | `LegacyoftheDragonborn.esm.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000F5D1B|Skyrim.esm` | `WEAP FULL` | Gauldur Blackblade | Gauldur Noirlame | **Lame noire de Gauldur** | `LegacyoftheDragonborn.esm.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000F5D1C|Skyrim.esm` | `WEAP FULL` | Gauldur Blackblade | Gauldur Noirlame | **Lame noire de Gauldur** | `LegacyoftheDragonborn.esm.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000F5D1D|Skyrim.esm` | `WEAP FULL` | Gauldur Blackblade | Gauldur Noirlame | **Lame noire de Gauldur** | `LegacyoftheDragonborn.esm.json` |
| `TRD Patch - Legacy of the Dragonborn.esp.json` | `000A9194|Skyrim.esm` | `CELL FULL` | Rebel's Cairn | Cairn du rebelle | **Cairn du Rebelle** | `LegacyoftheDragonborn.esm.json` |
| `school of bear.esp.json` | `00097299|Skyrim.esm` | `CELL FULL` | Palace of the Kings Upstairs | Palais des rois - Étage | **Palais des Rois - Étage** | `NewArmoury.esp.json` |
| `This Is Jorrvaskr - KASA.esp.json` | `0007947A|Skyrim.esm` | `CELL FULL` | Jorrvaskr Living Quarters | Logements de Jorrvaskr | **Jorrvaskr - Logements** | `LegacyoftheDragonborn.esm.json` |
| `nolvus awakening tsos patch.esp.json` | `0008BB91|Skyrim.esm` | `NPC_ FULL` | Movarth | Movarth | **Movarth Piquine** | `fanatical enemies.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `000138CB|Skyrim.esm` | `CELL FULL` | Thaumaturgist's Hut | La Hutte de la Thaumaturge | **Hutte du thaumaturge** | `citizenscomplete.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `000161EF|Skyrim.esm` | `CELL FULL` | Half-Moon Mill | Scierie Mi-Lune | **Scierie Mi-lune** | `unofficial skyrim special edition patch.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `0002C779|Skyrim.esm` | `CELL FULL` | Quicksilver Mine | Mine Vif-Argent | **Mine Vif-argent** | `unofficial skyrim special edition patch.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `00065AB5|Skyrim.esm` | `CELL FULL` | Burguk's Cellar | Cave de Burguk | **Cave de Dushnikh Yal** | `unofficial skyrim special edition patch.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `00013810|Skyrim.esm` | `CELL FULL` | The Arcanaeum | L'Arcanaeum | **Arcanaeum** | `NewArmoury.esp.json` |
| `SkyrimsUniqueTreasures.esp.json` | `00016787|Skyrim.esm` | `CELL FULL` | Calixto's House of Curiosities | Bazar des curiosités | **Bazar des curiosités de Calixto** | `LegacyoftheDragonborn.esm.json` |
| `Snazzy Skyrims Unique Treasures.esp.json` | `0002C779|Skyrim.esm` | `CELL FULL` | Quicksilver Mine | Mine Vif-Argent | **Mine Vif-argent** | `unofficial skyrim special edition patch.esp.json` |
| `TwistedFaithArmorAndSword.esp.json` | `000371DD|Skyrim.esm` | `CELL FULL` | Bleak Falls Sanctum | Sanctuaire des chutes tourmentées | **Sanctuaire des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `undeath conjuration absorb fix.esp.json` | `0010DDEC|Skyrim.esm` | `SPEL FULL` | Conjure Dremora Lord | Conjuration de seigneur Drémora | **Conjuration de seigneur drémora** | `MysticismMagic.esp.json` |
| `ACatsLife.esp.json` | `00013A7C|Skyrim.esm` | `CELL FULL` | Four Shields Tavern | Taverne des Quatre Boucliers | **Taverne des Quatre boucliers** | `citizenscomplete.esp.json` |
| `Vigilant.esm.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `vigilant.esm.json` | `0001677C|Skyrim.esm` | `CELL FULL` | Palace of the Kings | Palais des Rois | **Palais des rois** | `citizenscomplete.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B95|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF4|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD2|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B81|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000AC5|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Crowd Pleaser | Moisson sanglante | **Idole des foules** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B77|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BA7|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B96|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB9|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BBC|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Meteor Strike | Frappe météore | **Frappe de météore** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C06|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB8|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0B|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B80|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD0|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF3|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9C|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFB|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFA|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0C|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B78|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BAF|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B71|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B39|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B97|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFE|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C12|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD7|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD1|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BA8|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C10|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0E|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9D|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB4|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0D|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B94|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C08|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD3|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0A|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB1|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB7|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFC|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B82|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C02|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C09|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB2|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B79|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD6|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD5|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF1|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B7B|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BCC|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B98|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B75|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB0|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C01|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C03|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B6F|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9A|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF0|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B7A|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B8E|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B8B|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF6|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B83|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9E|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BD4|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BBB|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Windswept | Battu par les vents | **Balayé par les vents** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9F|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB5|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B99|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C00|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C11|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF9|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000953|Vokrii - Minimalistic Perks of Skyrim.esp` | `PERK FULL` | Breaching Shot | Tir fracassant | **Brèche** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C13|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF5|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C07|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B8C|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B8D|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF2|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B70|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C04|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000AC3|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Victory Rush | Ivresse de la victoire | **Ruée de la victoire** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB6|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B9B|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B38|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Crater Maker | Fracture | **Créateur de cratères** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C05|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BCD|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000969|Vokrii - Minimalistic Perks of Skyrim.esp` | `PERK FULL` | Flurry of Blows | Déluge de coups | **Rafale de coups** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BAE|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BA6|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFD|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BCF|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B76|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BCE|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BA9|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overbearing Assault | Assaut écrasant | **Assaut prédominant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF7|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000C0F|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BF8|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BFF|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Grievous Wounds | Blessures graves | **Blessures profondes** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000B7C|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Denting Blows | Coups déformants | **Coups lacérants** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `vokrii - apply spell conditions fix.esp.json` | `04000BB3|Vokrii - Minimalistic Perks of Skyrim.esp` | `SPEL FULL` | Overpowering Assault | Assaut surpuissant | **Assaut écrasant** | `Vokrii - Minimalistic Perks of Skyrim.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00045F96|Skyrim.esm` | `ARMO FULL` | Spellbreaker | Brise-Sort | **Brise-sort** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00047CBE|Skyrim.esm` | `ARMO FULL` | Leather Hood | Capuche de cuir | **Capuche en cuir** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00056B17|Skyrim.esm` | `ARMO FULL` | Ancient Nord Gauntlets | Gantelets nordiques antiques | **Brassards nordiques antiques** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0005B6A1|Skyrim.esm` | `ARMO FULL` | Barkeeper's Clothes | Vêtements d'aubergiste | **Vêtements de tavernier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00062311|Skyrim.esm` | `ARMO FULL` | Ulfric's Boots | Bottes d'Ulfric | **Bottes d'Ulfric Sombrage** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0006FF38|Skyrim.esm` | `ARMO FULL` | Barkeeper's Clothes | Vêtements d'aubergiste | **Vêtements de tavernier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0009DFF7|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000CF8A1|Skyrim.esm` | `ARMO FULL` | Shrouded Hood | Capuche sibylline | **Cagoule sibylline** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000D7A74|Skyrim.esm` | `ARMO FULL` | Dragonplate Helmet of Peerless Magicka | Casque pendragon de magie extrême | **Casque pendragon de magie absolue** | `Thaumaturgy.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000D8D55|Skyrim.esm` | `ARMO FULL` | Forsworn Gauntlets | Gantelets de Parjure | **Brassards de Parjure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000E40DE|Skyrim.esm` | `ARMO FULL` | Party Shoes | Bottes raffinées | **Chaussures festives** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000EAFD2|Skyrim.esm` | `ARMO FULL` | Gauntlets of the Old Gods | Gantelets des Anciennes Divinités | **Brassards des Anciennes divinités** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000EAFD3|Skyrim.esm` | `ARMO FULL` | Boots of the Old Gods | Bottes des Anciennes Divinités | **Bottes des Anciennes divinités** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F6904|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F690D|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F690E|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F690F|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F6910|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F6911|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000F9904|Skyrim.esm` | `ARMO FULL` | Diadem of the Savant | Diadème du Savant | **Diadème du savant** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00108543|Skyrim.esm` | `ARMO FULL` | Linwe's Boots | Bottes de Linwë | **Bottes de Linwe** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00108544|Skyrim.esm` | `ARMO FULL` | Linwe's Armor | Armure de Linwë | **Armure de Linwe** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00108545|Skyrim.esm` | `ARMO FULL` | Linwe's Gloves | Gants de Linwë | **Brassards de Linwe** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00108546|Skyrim.esm` | `ARMO FULL` | Linwe's Hood | Capuche de Linwë | **Capuche de Linwe** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0200E7FD|Dawnguard.esm` | `ARMO FULL` | Ring of the Beast | Anneau de la Bête | **Anneau bestial** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `02014757|Dawnguard.esm` | `ARMO FULL` | Dawnguard Heavy Boots | Bottes de la Garde de l'Aube lourdes | **Bottes lourdes de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `02014758|Dawnguard.esm` | `ARMO FULL` | Dawnguard Heavy Gauntlets | Gantelets de la Garde de l'Aube lourds | **Gantelets lourds de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `020150B8|Dawnguard.esm` | `ARMO FULL` | Dawnguard Shield | Bouclier de la Garde de l'Aube | **Bouclier de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0201989E|Dawnguard.esm` | `ARMO FULL` | Dawnguard Helmet | Casque de la Garde de l'Aube | **Casque de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401961C|Dragonborn.esm` | `ARMO FULL` | Neloth's Ring of Tracking | Anneau de localisation de Néloth | **Anneau de localisation de Neloth** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401CD9E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots | Bottes de stalhrim lourdes  | **Bottes lourdes de stalhrim** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401CD9F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor | Armure de stalhrim lourde | **Armure lourde de stalhrim** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401CDA0|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets | Gantelets de stalhrim lourds | **Gantelets lourds de stalhrim** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401CDA1|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet | Casque de stalhrim lourd | **Casque lourd de stalhrim** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401DB97|Dragonborn.esm` | `ARMO FULL` | Ahzidal's Armor of Retribution | Armure de châtiment d'Ahzidal | **Armure du châtiment d'Ahzidal** | `LegacyoftheDragonborn.esm.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040284D8|Dragonborn.esm` | `ARMO FULL` | Bonemold Armor of the Minor Knight | Armure d'ostalium d'humble écuyer | **Armure d'ostalium d'humble chevalier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040284D9|Dragonborn.esm` | `ARMO FULL` | Bonemold Armor of the Knight | Armure d'ostalium d'écuyer | **Armure d'ostalium de chevalier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040284DA|Dragonborn.esm` | `ARMO FULL` | Bonemold Armor of the Major Knight | Armure d'ostalium de grand écuyer | **Armure d'ostalium de grand chevalier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040291FC|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Brawn | Bottes de stalhrim lourdes de surhomme | **Bottes de stalhrim de surhomme** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040291FD|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of the Ox | Bottes de stalhrim lourdes du boeuf | **Bottes de stalhrim du boeuf** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040291FE|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of the Mammoth | Bottes de stalhrim lourdes du mammouth  | **Bottes lourdes de stalhrim du mammouth** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `040291FF|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Muffling | Bottes de stalhrim lourdes de silence  | **Solerets en stalhrim de silence** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029200|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Fire Suppression | Bottes de stalhrim lourdes de feu neutralisé  | **Bottes lourdes de stalhrim de feu neutralisé** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029201|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Fire Abatement | Bottes de stalhrim lourdes de feu anéanti  | **Bottes lourdes de stalhrim de feu anéanti** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029202|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of the Firewalker | Bottes de stalhrim lourdes de Marchefeu  | **Bottes lourdes de stalhrim de Marchefeu** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029203|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Frost Suppression | Bottes de stalhrim lourdes de glace neutralisée  | **Bottes lourdes de stalhrim de glace neutralisée** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029204|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Frost Abatement | Bottes de stalhrim lourdes de glace anéantie  | **Bottes lourdes de stalhrim de glace anéantie** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029205|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Warmth | Bottes de stalhrim lourdes de dégel  | **Bottes lourdes de stalhrim de dégel** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029206|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Shock Suppression | Bottes de stalhrim lourdes de foudre neutralisée  | **Bottes lourdes de stalhrim de foudre neutralisée** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029207|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Shock Abatement | Bottes de stalhrim lourdes de foudre anéantie  | **Bottes lourdes de stalhrim de foudre anéantie** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029208|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Grounding | Bottes de stalhrim lourdes d'isolation  | **Bottes lourdes de stalhrim d'isolation** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029209|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Eminent Stamina | Bottes de stalhrim lourdes de vigueur majeure  | **Bottes lourdes de stalhrim de vigueur majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920A|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Extreme Stamina | Bottes de stalhrim lourdes de vigueur extrême  | **Bottes lourdes de stalhrim de vigueur extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920B|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Boots of Peerless Stamina | Bottes de stalhrim lourdes de vigueur absolue  | **Bottes lourdes de stalhrim de vigueur absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920C|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Alteration | Armure de stalhrim lourde d'altération majeure | **Armure lourde de stalhrim d'altération majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920D|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Alteration | Armure de stalhrim lourde d'altération extrême | **Armure lourde de stalhrim d'altération extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Alteration | Armure de stalhrim lourde d'altération absolue | **Armure lourde de stalhrim d'altération absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402920F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Conjuring | Armure de stalhrim lourde de conjuration majeure | **Armure lourde de stalhrim de conjuration majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029210|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Conjuring | Armure de stalhrim lourde de conjuration extrême | **Armure lourde de stalhrim de conjuration extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029211|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Conjuring | Armure de stalhrim lourde de conjuration absolue | **Armure lourde de stalhrim de conjuration absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029212|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Destruction | Armure de stalhrim lourde de destruction majeure | **Armure lourde de stalhrim de destruction majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029213|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Destruction | Armure de stalhrim lourde de destruction extrême | **Armure lourde de stalhrim de destruction extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029214|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Destruction | Armure de stalhrim lourde de destruction absolue | **Armure lourde de stalhrim de destruction absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029215|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Health | Armure de stalhrim lourde de santé majeure | **Armure lourde de stalhrim de santé majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029216|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Health | Armure de stalhrim lourde de santé extrême | **Armure lourde de stalhrim de santé extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029217|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Revival | Armure de stalhrim lourde de renaissance | **Armure lourde de stalhrim de renaissance** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029218|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Health | Armure de stalhrim lourde de santé absolue | **Armure lourde de stalhrim de santé absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029219|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Mending | Armure de stalhrim lourde de soulagement | **Armure lourde de stalhrim de soulagement** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921A|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Regeneration | Armure de stalhrim lourde de régénération | **Armure lourde de stalhrim de régénération** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921B|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of the Eminent Knight | Armure de stalhrim lourde de noble chevalier | **Armure lourde de stalhrim de noble chevalier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921C|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of the Noble Knight | Armure de stalhrim lourde de preux chevalier | **Armure lourde de stalhrim de preux chevalier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921D|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of the Peerless Knight | Armure de stalhrim lourde de paladin | **Armure lourde de stalhrim de paladin** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Illusion | Armure de stalhrim lourde d'illusion majeure | **Armure lourde de stalhrim d'illusion majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402921F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Illusion | Armure de stalhrim lourde d'illusion extrême | **Armure lourde de stalhrim d'illusion extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029220|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Illusion | Armure de stalhrim lourde d'illusion absolue | **Armure lourde de stalhrim d'illusion absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029221|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Eminent Restoration | Armure de stalhrim lourde de guérison majeure | **Armure lourde de stalhrim de guérison majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029222|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Extreme Restoration | Armure de stalhrim lourde de guérison extrême | **Armure lourde de stalhrim de guérison extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029223|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Peerless Restoration | Armure de stalhrim lourde de guérison absolue | **Armure lourde de stalhrim de guérison absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029224|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Rejuvenation | Armure de stalhrim lourde de rétablissement | **Armure lourde de stalhrim de rétablissement** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029225|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Invigoration | Armure de stalhrim lourde de vivification | **Armure lourde de stalhrim de vivification** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029226|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Armor of Renewal | Armure de stalhrim lourde de renouveau | **Armure lourde de stalhrim de renouveau** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029227|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Eminent Alchemy | Gantelets de stalhrim lourds d'alchimie majeure | **Gantelets lourds de stalhrim d'alchimie majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029228|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Extreme Alchemy | Gantelets de stalhrim lourds d'alchimie extrême | **Gantelets lourds de stalhrim d'alchimie extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029229|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Peerless Alchemy | Gantelets de stalhrim lourds d'alchimie absolue | **Gantelets lourds de stalhrim d'alchimie absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922A|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Eminent Archery | Gantelets de stalhrim lourds d'archerie majeure | **Gantelets lourds de stalhrim d'archerie majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922B|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Extreme Archery | Gantelets de stalhrim lourds d'archerie extrême | **Gantelets lourds de stalhrim d'archerie extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922C|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Peerless Archery | Gantelets de stalhrim lourds d'archerie absolue | **Gantelets lourds de stalhrim d'archerie absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922D|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Eminent Wielding | Gantelets de stalhrim lourds de maniement majeur | **Gantelets lourds de stalhrim de maniement majeur** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Extreme Wielding | Gantelets de stalhrim lourds de maniement extrême | **Gantelets lourds de stalhrim de maniement extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402922F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Peerless Wielding | Gantelets de stalhrim lourds de maniement absolu | **Gantelets lourds de stalhrim de maniement absolu** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029230|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Eminent Smithing | Gantelets de stalhrim lourds de forgeage majeur | **Gantelets lourds de stalhrim de forgeage majeur** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029231|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Extreme Smithing | Gantelets de stalhrim lourds de forgeage extrême | **Gantelets lourds de stalhrim de forgeage extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029232|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Peerless Smithing | Gantelets de stalhrim lourds de forgeage absolu | **Gantelets lourds de stalhrim de forgeage absolu** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029233|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Eminent Sure Grip | Gantelets de stalhrim lourds de poigne majeure | **Gantelets lourds de stalhrim de poigne majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029234|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Extreme Sure Grip | Gantelets de stalhrim lourds de poigne extrême | **Gantelets lourds de stalhrim de poigne extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029235|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Gauntlets of Peerless Sure Grip | Gantelets de stalhrim lourds de poigne absolue | **Gantelets lourds de stalhrim de poigne absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029236|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Alchemy | Casque de stalhrim lourd d'alchimie majeure | **Casque lourd de stalhrim d'alchimie majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029237|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Alchemy | Casque de stalhrim lourd d'alchimie extrême | **Casque lourd de stalhrim d'alchimie extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029238|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Alchemy | Casque de stalhrim lourd d'alchimie absolue | **Casque lourd de stalhrim d'alchimie absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029239|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Alteration | Casque de stalhrim lourd d'altération majeure | **Casque lourd de stalhrim d'altération majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923A|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Alteration | Casque de stalhrim lourd d'altération extrême | **Casque lourd de stalhrim d'altération extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923B|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Alteration | Casque de stalhrim lourd d'altération absolue | **Casque lourd de stalhrim d'altération absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923C|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Conjuring | Casque de stalhrim lourd de conjuration majeure | **Casque lourd de stalhrim de conjuration majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923D|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Conjuring | Casque de stalhrim lourd de conjuration extrême | **Casque lourd de stalhrim de conjuration extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Conjuring | Casque de stalhrim lourd de conjuration absolue | **Casque lourd de stalhrim de conjuration absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402923F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Destruction | Casque de stalhrim lourd de destruction majeure | **Casque lourd de stalhrim de destruction majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029240|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Destruction | Casque de stalhrim lourd de destruction extrême | **Casque lourd de stalhrim de destruction extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029241|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Destruction | Casque de stalhrim lourd de destruction absolue | **Casque lourd de stalhrim de destruction absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029242|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Illusion | Casque de stalhrim lourd d'illusion majeure | **Casque lourd de stalhrim d'illusion majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029243|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Illusion | Casque de stalhrim lourd d'illusion extrême | **Casque lourd de stalhrim d'illusion extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029244|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Illusion | Casque de stalhrim lourd d'illusion absolue | **Casque lourd de stalhrim d'illusion absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029245|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Magicka | Casque de stalhrim lourd de magie majeure | **Casque lourd de stalhrim de magie majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029246|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Magicka | Casque de stalhrim lourd de magie extrême | **Casque lourd de stalhrim de magie extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029247|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Magicka | Casque de stalhrim lourd de magie extrême | **Casque lourd de stalhrim de magie absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029248|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Replenishing | Casque de stalhrim lourd d'emplissage | **Casque lourd de stalhrim d'emplissage** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029249|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Resurgence | Casque de stalhrim lourd de résurgence | **Casque lourd de stalhrim de résurgence** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924A|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Recovery | Casque de stalhrim lourd de regain | **Casque lourd de stalhrim de regain** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924B|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Archery | Casque de stalhrim lourd d'archerie majeure | **Casque lourd de stalhrim d'archerie majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924C|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Archery | Casque de stalhrim lourd d'archerie extrême | **Casque lourd de stalhrim d'archerie extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924D|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Archery | Casque de stalhrim lourd d'archerie absolue | **Casque lourd de stalhrim d'archerie absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924E|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Eminent Restoration | Casque de stalhrim lourd de guérison majeure | **Casque lourd de stalhrim de guérison majeure** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402924F|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Extreme Restoration | Casque de stalhrim lourd de guérison extrême | **Casque lourd de stalhrim de guérison extrême** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029250|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Peerless Restoration | Casque de stalhrim lourd de guérison absolue | **Casque lourd de stalhrim de guérison absolue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04029251|Dragonborn.esm` | `ARMO FULL` | Stalhrim Heavy Helmet of Waterbreathing | Casque de stalhrim lourd de respiration aquatique | **Heaume en stalhrim de respiration aquatique** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402AD31|Dragonborn.esm` | `ARMO FULL` | Blackguard's Hood | Capuchon de Gardenoir | **Capuche de Gardenoir** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402AD32|Dragonborn.esm` | `ARMO FULL` | Blackguard's Gloves | Gants de Gardenoir | **Brassards de Gardenoir** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00013986|Skyrim.esm` | `WEAP FULL` | Steel Dagger | Dague d'acier | **Dague en acier** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000139A8|Skyrim.esm` | `WEAP FULL` | Glass Mace | Masse de verre | **Masse en verre** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0001C4E6|Skyrim.esm` | `WEAP FULL` | The Rueful Axe | Hache du Chagrin | **Hache du chagrin** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00068C57|Skyrim.esm` | `WEAP FULL` | Nord Hero Bow | Arc de héros nordique | **Arc du héros** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00068C79|Skyrim.esm` | `WEAP FULL` | Nord Hero Battleaxe | Hache d'armes de héros nordique | **Hache d'armes du héros** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00068C7B|Skyrim.esm` | `WEAP FULL` | Nord Hero Sword | Épée de héros nordique | **Épée du héros** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000964C9|Skyrim.esm` | `WEAP FULL` | Blade of Woe | Lame de la Souffrance | **Lame de la souffrance** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0009CCDC|Skyrim.esm` | `WEAP FULL` | Blade of Woe | Lame de la Souffrance | **Lame de la souffrance** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `000A3115|Skyrim.esm` | `WEAP FULL` | Nord Hero Greatsword | Espadon de héros nordique | **Espadon du héros** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0200D098|Dawnguard.esm` | `WEAP FULL` | Dawnguard War Axe | Hache de la Garde de l'Aube | **Hache de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0200DD55|Dawnguard.esm` | `WEAP FULL` | Dawnguard Warhammer | Marteau de la Garde de l'Aube | **Marteau de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `02011BAD|Dawnguard.esm` | `WEAP FULL` | Dawnguard Rune Hammer | Marteau runique de la Garde de l'Aube | **Marteau runique de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `02014555|Dawnguard.esm` | `WEAP FULL` | Akaviri Sword | Katana akaviri | **Épée akaviroise** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `02014FCB|Dawnguard.esm` | `WEAP FULL` | Dragonbone Dagger | Dague d'os de dragon | **Dague en os de dragon** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0201668C|Dawnguard.esm` | `WEAP FULL` | Dawnguard Rune Axe | Hache runique de la Garde de l'Aube | **Hache runique de la Garde de l'aube** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401A578|Dragonborn.esm` | `WEAP FULL` | Champion's Cudgel | Marteau du Champion | **Marteau du champion** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0401AEA4|Dragonborn.esm` | `WEAP FULL` | Bloodskal Blade | Lame des Sangskaals | **Lame des Skalsangue** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0403CD5B|Dragonborn.esm` | `ALCH FULL` | Horker and Ash Yam Stew | Ragoût de horqueur aux ignames des cendres | **Ragoût de horqueur aux pommes de cendres** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `03004849|HearthFires.esm` | `CELL FULL` | Lakeview Manor, Cellar | Manoir du Lac - Cave | **Manoir du lac - Cave** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `03002FEC|HearthFires.esm` | `CELL FULL` | Lakeview Manor | Manoir du Lac | **Manoir du lac** | `unofficial skyrim special edition patch.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04024108|Dragonborn.esm` | `PERK FULL` | Smithing | Forgeage | **Forge** | `Adamant.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `04024109|Dragonborn.esm` | `PERK FULL` | Matching Set | Panoplie légère | **Panoplie** | `Adamant.esp.json` |
| `weapons armor clothing & clutter fixes.esp.json` | `0402410A|Dragonborn.esm` | `PERK FULL` | Matching Set | Panoplie lourde | **Panoplie** | `Adamant.esp.json` |
| `water for enb (shades of skyrim).esp.json` | `000A1793|Skyrim.esm` | `CELL FULL` | Red Wave | Vague rouge | **Le Vague rouge** | `Wyrmstooth.esp.json` |
| `water for enb (shades of skyrim).esp.json` | `02001DBA|Dawnguard.esm` | `CELL FULL` | Fort Dawnguard | Fort de la Garde de l'aube | **Fort de la Garde de l'Aube** | `NewArmoury.esp.json` |
| `water for enb (shades of skyrim).esp.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `water for enb (shades of skyrim).esp.json` | `02009BDE|Dawnguard.esm` | `CELL FULL` | Dead Drop Falls | Chutes du saut mortel | **Chutes du Saut mortel** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `000778F1|Skyrim.esm` | `CELL FULL` | Robber's Cove | Val des voleurs | **Val des Voleurs** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `0002A03A|Skyrim.esm` | `CELL FULL` | Dustman's Crypt | Crypte des poussiéreux | **Crypte des Poussiéreux** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `000A87C5|Skyrim.esm` | `CELL FULL` | Ravenscar Hollow | Perchoir du corbeau | **Perchoir du Corbeau** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `00015274|Skyrim.esm` | `CELL FULL` | Frostflow Lighthouse | Phare d'Hiveronde  | **Phare d'Hiveronde** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `0005B91B|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher | Mausolée du crépuscule | **Mausolée du Crépuscule** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `000A9194|Skyrim.esm` | `CELL FULL` | Rebel's Cairn | Cairn du rebelle | **Cairn du Rebelle** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `water for enb (shades of skyrim).esp.json` | `00015226|Skyrim.esm` | `CELL FULL` | Reachwater Rock | Rocher d'Eaulointaine  | **Rocher d'Eaulointaine** | `unofficial skyrim special edition patch.esp.json` |
| `water for enb (shades of skyrim).esp.json` | `000AA20C|Skyrim.esm` | `CELL FULL` | Liar's Retreat | Refuge du menteur | **Refuge du Menteur** | `LegacyoftheDragonborn.esm.json` |
| `water for enb - patch - jks ragged flagon.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `water for enb - patch - lux - jks ragged flagon.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `water for enb.esm.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB (Shades of Skyrim).esp.json` | `02009BDE|Dawnguard.esm` | `CELL FULL` | Dead Drop Falls | Chutes du saut mortel | **Chutes du Saut mortel** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB (Shades of Skyrim).esp.json` | `000778F1|Skyrim.esm` | `CELL FULL` | Robber's Cove | Val des voleurs | **Val des Voleurs** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB (Shades of Skyrim).esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB (Shades of Skyrim).esp.json` | `0003CBCB|Skyrim.esm` | `CELL FULL` | Darklight Chambers | Tour Clair-Obscur - Chambres | **Tour Clair-obscur - Chambres** | `unofficial skyrim special edition patch.esp.json` |
| `Water for ENB - Patch - JKs Ragged Flagon.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB - Patch - Lux - JKs Ragged Flagon.esp.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `Water for ENB.esm.json` | `00016BD0|Skyrim.esm` | `CELL FULL` | The Ragged Flagon - Cistern | La Cruche percée - Réservoir | **La Cruche percée - Citerne** | `LegacyoftheDragonborn.esm.json` |
| `WAVY Waterfalls Effect.esp.json` | `00041777|Skyrim.esm` | `CELL FULL` | Swindler's Den | Tanière de l'escroc | **Tanière de l'Escroc** | `LegacyoftheDragonborn.esm.json` |
| `WAVY Waterfalls Effect.esp.json` | `00015226|Skyrim.esm` | `CELL FULL` | Reachwater Rock | Rocher d'Eaulointaine  | **Rocher d'Eaulointaine** | `unofficial skyrim special edition patch.esp.json` |
| `WAVY Waterfalls Effect.esp.json` | `000371DE|Skyrim.esm` | `CELL FULL` | Bleak Falls Temple | Temple des chutes tourmentées | **Temple des Chutes tourmentées** | `LegacyoftheDragonborn.esm.json` |
| `WAVY Waterfalls Effect.esp.json` | `0005554A|Skyrim.esm` | `CELL FULL` | Lost Prospect Mine | La mine perdue | **Mine perdue** | `unofficial skyrim special edition patch.esp.json` |
| `WAVY Waterfalls Effect.esp.json` | `02009BDE|Dawnguard.esm` | `CELL FULL` | Dead Drop Falls | Chutes du saut mortel | **Chutes du Saut mortel** | `LegacyoftheDragonborn.esm.json` |
| `ISC WACCF Patch.esp.json` | `000877A7|Skyrim.esm` | `ARMO FULL` | Silver Amethyst Ring | Anneau d'argent et d'améthyste parfaite | **Anneau d'argent et d'améthyste** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000877AB|Skyrim.esm` | `ARMO FULL` | Silver Garnet Ring | Anneau d'argent et de grenat parfait | **Anneau d'argent et de grenat** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `0009DFF7|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F6904|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F690D|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F690E|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F690F|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F6910|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `000F6911|Skyrim.esm` | `ARMO FULL` | Amulet of Articulation | Amulette d'Intimidation | **Amulette d'articulation** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `0001C4E6|Skyrim.esm` | `WEAP FULL` | The Rueful Axe | Hache du Chagrin | **Hache du chagrin** | `unofficial skyrim special edition patch.esp.json` |
| `ISC WACCF Patch.esp.json` | `00068C79|Skyrim.esm` | `WEAP FULL` | Nord Hero Battleaxe | Hache d'armes de héros nordique | **Hache d'armes du héros** | `unofficial skyrim special edition patch.esp.json` |
| `Wintersun - Faiths of Skyrim.esp.json` | `000EEF58|Skyrim.esm` | `SPEL FULL` | The Gift of Charity | Le don de charité | **Don de charité** | `unofficial skyrim special edition patch.esp.json` |
| `Wintersun - Faiths of Skyrim.esp.json` | `000FB992|Skyrim.esm` | `MGEF FULL` | Fortify Shouts | Renfort de Cri | **Renfort de cri** | `unofficial skyrim special edition patch.esp.json` |
| `WornUndead.esl.json` | `000152C0|Skyrim.esm` | `CELL FULL` | Ansilvund Excavation | Site de fouilles d'Ansilvund | **Ansilvund - Site de fouilles** | `LegacyoftheDragonborn.esm.json` |
| `WornUndead.esl.json` | `0001F358|Skyrim.esm` | `CELL FULL` | Ansilvund Burial Chambers | Chambres sépulcrales d'Ansilvund | **Ansilvund - Chambres sépulcrales** | `LegacyoftheDragonborn.esm.json` |
| `YOT - Your Own Thoughts.esp.json` | `00049504|Skyrim.esm` | `MGEF FULL` | Fortify Magicka | Renfort de magie | **Fortify Magicka** | `Thaumaturgy.esp.json` |
| `YOT - Your Own Thoughts.esp.json` | `0008F3EA|Skyrim.esm` | `MGEF FULL` | Muffle | Silence | **Aphasie** | `MysticismMagic.esp.json` |
| `YOT - Your Own Thoughts.esp.json` | `0200C601|Dawnguard.esm` | `MGEF FULL` | Summon Arvak | Invocation d'Arvak | **Conjuration d'Arvak** | `MysticismMagic.esp.json` |
| `YOT - Your Own Thoughts.esp.json` | `00049507|Skyrim.esm` | `MGEF FULL` | Fortify Stamina | Renfort de vigueur | **Fortify Stamina** | `Thaumaturgy.esp.json` |
| `at your own pace - college of winterhold.esp.json` | `0001380E|Skyrim.esm` | `CELL FULL` | Hall of the Elements | Salle des Éléments | **Salle des éléments** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - companions.esp.json` | `000E3145|Skyrim.esm` | `QUST FULL` | Totems of Hircine | Les Totems d'Hircine | **Les totems d'Hircine** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - companions.esp.json` | `0004B2D9|Skyrim.esm` | `QUST FULL` | Take Up Arms | Prenez les armes | **Prise d'armes** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - companions.esp.json` | `000C18E1|Skyrim.esm` | `QUST FULL` | Family Heirloom | Héritage de famille | **Héritage familial** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - companions.esp.json` | `000E3156|Skyrim.esm` | `QUST FULL` | Dragon Seekers | Les chercheurs de dragons | **Les chasseurs de dragons** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - dawnguard.esp.json` | `0200CE06|Dawnguard.esm` | `QUST FULL` | Rings of Blood Magic | Les anneaux de Magie du sang | **Les Anneaux de Magie du sang** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - dawnguard.esp.json` | `020050BD|Dawnguard.esm` | `QUST FULL` | Deceiving the Herd | Tromper le troupeau | **Tromper la foule** | `unofficial skyrim special edition patch.esp.json` |
| `At Your Own Pace - Thane Overhaul.esp.json` | `00065BDF|Skyrim.esm` | `QUST FULL` | I Done Got Thaned! | Ils m'ont nommé thane ! | **Je suis thane !** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - thieves guild.esp.json` | `000138CB|Skyrim.esm` | `CELL FULL` | Thaumaturgist's Hut | La Hutte de la Thaumaturge | **Hutte du thaumaturge** | `citizenscomplete.esp.json` |
| `at your own pace - thieves guild.esp.json` | `000161EF|Skyrim.esm` | `CELL FULL` | Half-Moon Mill | Scierie Mi-Lune | **Scierie Mi-lune** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - thieves guild.esp.json` | `0002E521|Skyrim.esm` | `CELL FULL` | Twilight Sepulcher Inner Sanctum | Mausolée du Crépuscule - Sanctuaire | **Mausolée du crépuscule - Sanctuaire intérieur** | `unofficial skyrim special edition patch.esp.json` |
| `at your own pace - thieves guild.esp.json` | `00016787|Skyrim.esm` | `CELL FULL` | Calixto's House of Curiosities | Bazar des curiosités | **Bazar des curiosités de Calixto** | `LegacyoftheDragonborn.esm.json` |
| `at your own pace - thieves guild.esp.json` | `00065AB5|Skyrim.esm` | `CELL FULL` | Burguk's Cellar | Cave de Burguk | **Cave de Dushnikh Yal** | `unofficial skyrim special edition patch.esp.json` |
| `TheChoiceIsYours.esp.json` | `0001CF26|Skyrim.esm` | `QUST FULL` | Missing In Action | Absent au combat | **Porté disparu** | `unofficial skyrim special edition patch.esp.json` |
| `SkyrimSewers.esp.json` | `00016786|Skyrim.esm` | `CELL FULL` | Hall of the Dead | Nécropole | **Nécropole de Vendeaume** | `LegacyoftheDragonborn.esm.json` |
