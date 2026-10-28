# Récapitulatif des Modifications — Phase 6 : Équipements, Armes & Armures Dérivées

> **Date :** 28 Octobre 2026  
> **Statut :** ✅ Validé & Vérifié sur disque  
> **Périmètre audité :** 91 plugins (2 515 chaînes)  
> **Total modifications unitaires :** 65 entrées  
> **Protocole de sécurité :** Ciblage unitaire strict `(form_id, type, index, original)` avec assertion `count == 1` et relecture physique post-écriture.  

## 1. Vue d'ensemble par mod / fichier

| Fichier | Nombre de corrections | Objectif principal |
| :--- | :---: | :--- |
| `Breton Apparel - Imperial Renaissance/breton apparel - imperial renaissance.esp.json` | **11** | Correction orthographique lore 'Breton' (sans accent) et singulier 'Robe de mage / d'érudit' |
| `Imperial Battlemage Robes/imperialbattlemage.esp.json` | **1** | Uniformisation singulière 'Robe de mage de bataille impérial' |
| `Witcher Nilfgaardian Armor.esp - French/witcher nilfgaardian armor.esp.json` | **4** | Traduction 'nilfgaardiens / nilfgaardiennes' (ex-Nilfgaardian) et élimination de double espace |
| `[Ashtoreth] Duskrogue Armor.esp - French/[ashtoreth] duskrogue armor.esp.json` | **7** | Traduction 'Épaulières' (ex-Pauldrons), correction d'obsidienne (singulier) et singulier des vêtements |
| `NordWarUA's Vanilla Armor and Weapon Expansion - Craft Only.esp - French/nordwarua's vanilla armor and weapon expansion - craft only.esp.json` | **4** | Harmonisation Bethesda du Bouclier en fer renforcé nordique et pluriel officiel 'Armure / bottes / casque de plates' |
| `QND SPID Clothing Pack 1/tw3_femalearmors_zzjay.esp.json` | **3** | Traduction des coloris 'Blanc' et 'Violet' (ex-White / Purple) et suppression de coquille HTML |
| `Triss Armor Retextured/trissarmorretextured.esp.json` | **35** | Harmonisation 'Pourpoint' (ex-Jerkin), 'Rôdeur' (ex-Ranger), 'L'Annuel du tailleur' et rétablissement des balises moteur [pagebreak] |

---

## 2. Tableau Exhaustif des Modifications Effectives

| Fichier | FormID | Type | Index | Source (EN) | Ancienne valeur | Valeur validée | Justification Lore / Canon |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- | :--- |
| `breton apparel - imperial renaissance.esp.json` | `02000D71|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Scholar Hood | Capuchon d'érudit Bréton | **Capuchon d'érudit breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D64|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Mage Robes (Hooded) | Robes de mage Bréton (à capuche) | **Robe de mage breton (à capuche)** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D6F|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Scholar Gloves | Gants d'érudit Bréton | **Gants d'érudit breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D79|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Cardinal Hood (Julianos) | Capuchon de cardinal Bréton (Julianos) | **Capuchon de cardinal breton (Julianos)** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D72|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Scholar Boots | Bottes d'érudit Bréton | **Bottes d'érudit breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D78|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Cardinal Robes (Julianos) | Robe de cardinal Bréton (Julianos) | **Robe de cardinal breton (Julianos)** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D62|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Mage Gloves | Gants de mage Bréton | **Gants de mage breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D7A|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Cardinal Boots (Julianos) | Bottes de cardinal Bréton (Julianos) | **Bottes de cardinal breton (Julianos)** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D70|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Scholar Robes | Robes d'érudit Bréton | **Robe d'érudit breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D77|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Cardinal Gloves (Julianos) | Gants de cardinal Bréton (Julianos) | **Gants de cardinal breton (Julianos)** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `breton apparel - imperial renaissance.esp.json` | `02000D6A|Breton Apparel - Imperial Renaissance.esp` | `ARMO FULL` | — | Breton Mage Boots | Bottes de mage Bréton | **Bottes de mage breton** | LORE_BRETON_ACCENT_AND_ROBE_SINGULAR |
| `imperialbattlemage.esp.json` | `05000802|ImperialBattleMage.esp` | `ARMO FULL` | — | Imperial Battlemage Robes | Robes de mage de bataille impérial | **Robe de mage de bataille impérial** | EQUIPMENT_ROBE_SINGULAR |
| `witcher nilfgaardian armor.esp.json` | `01000D68|Witcher Nilfgaardian Armor.esp` | `ARMO FULL` | — | Nilfgaardian Boots(H) | Bottes Nilfgaardian (lourdes) | **Bottes nilfgaardiennes (lourdes)** | LORE_NILFGAARD_TRANSLATION |
| `witcher nilfgaardian armor.esp.json` | `01000D6A|Witcher Nilfgaardian Armor.esp` | `ARMO FULL` | — | Nilfgaardian Gloves(H) | Gants Nilfgaardian (lourds) | **Gants nilfgaardiens (lourds)** | LORE_NILFGAARD_TRANSLATION |
| `witcher nilfgaardian armor.esp.json` | `01000D69|Witcher Nilfgaardian Armor.esp` | `ARMO FULL` | — | Nilfgaardian Gloves(L) | Gants Nilfgaardian  (légers) | **Gants nilfgaardiens (légers)** | LORE_NILFGAARD_TRANSLATION_AND_SPACING |
| `witcher nilfgaardian armor.esp.json` | `01000D67|Witcher Nilfgaardian Armor.esp` | `ARMO FULL` | — | Nilfgaardian Boots(L) | Bottes Nilfgaardian (légères) | **Bottes nilfgaardiennes (légères)** | LORE_NILFGAARD_TRANSLATION |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D95|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Obsidian Pauldrons | Pauldrons du rôdeur crépusculaire d'obsidiennes | **Épaulières du rôdeur crépusculaire d'obsidienne** | TRANSLATION_PAULDRONS_TO_EPAULIERES |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D72|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Umber Pauldrons | Pauldrons du rôdeur crépusculaire d'ombre | **Épaulières du rôdeur crépusculaire d'ombre** | TRANSLATION_PAULDRONS_TO_EPAULIERES |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D93|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Obsidian Leg Guards | Garde-jambes du rôdeur crépusculaire d'obsidiennes | **Garde-jambes du rôdeur crépusculaire d'obsidienne** | GRAMMAR_OBSIDIENNE_SINGULAR |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D90|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Obsidian Bracers | Brassards du rôdeur crépusculaire d'obsidien | **Brassards du rôdeur crépusculaire d'obsidienne** | GRAMMAR_OBSIDIENNE_SPELLING |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D94|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Obsidian Trousers | Pantalons du rôdeur crépusculaire d'obsidiennes | **Pantalon du rôdeur crépusculaire d'obsidienne** | GRAMMAR_PANTALON_AND_OBSIDIENNE_SINGULAR |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D8F|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Obsidian Coat | Manteau du rôdeur crépusculaire d'obsidien | **Manteau du rôdeur crépusculaire d'obsidienne** | GRAMMAR_OBSIDIENNE_SPELLING |
| `[ashtoreth] duskrogue armor.esp.json` | `02000D71|[Ashtoreth] Duskrogue Armor.esp` | `ARMO FULL` | — | Duskrogue Umber Trousers | Pantalons du rôdeur crépusculaire d'ombre | **Pantalon du rôdeur crépusculaire d'ombre** | GRAMMAR_PANTALON_SINGULAR |
| `nordwarua's vanilla armor and weapon expansion - craft only.esp.json` | `0600095C|NordWarUA's Vanilla Armor and Weapon Expansion - Craft Only.esp` | `ARMO FULL` | — | Northern Banded Iron Shield | Bouclier en fer bandé en acier nordique | **Bouclier en fer renforcé nordique** | BETHOFF_BANDED_IRON_SHIELD |
| `nordwarua's vanilla armor and weapon expansion - craft only.esp.json` | `06000968|NordWarUA's Vanilla Armor and Weapon Expansion - Craft Only.esp` | `ARMO FULL` | — | Rusty Plate Armor | Armure de plaque rouillée | **Armure de plates rouillée** | BETHOFF_PLATE_ARMOR_PLURAL |
| `nordwarua's vanilla armor and weapon expansion - craft only.esp.json` | `06000967|NordWarUA's Vanilla Armor and Weapon Expansion - Craft Only.esp` | `ARMO FULL` | — | Rusty Plate Boots | Bottes de plaque rouillée | **Bottes de plates rouillées** | BETHOFF_PLATE_ARMOR_PLURAL |
| `nordwarua's vanilla armor and weapon expansion - craft only.esp.json` | `0600096A|NordWarUA's Vanilla Armor and Weapon Expansion - Craft Only.esp` | `ARMO FULL` | — | Rusty Plate Helmet | Casque à plaque rouillée | **Casque de plates rouillé** | BETHOFF_PLATE_ARMOR_PLURAL |
| `tw3_femalearmors_zzjay.esp.json` | `0200089A|TW3_femaleArmors_zzjay.esp` | `ARMO FULL` | — | Triss DLC Outfit - White | Habits DLC de Triss - White | **Habits DLC de Triss - Blanc** | RESIDUAL_ENGLISH_COLOR |
| `tw3_femalearmors_zzjay.esp.json` | `02000898|TW3_femaleArmors_zzjay.esp` | `ARMO FULL` | — | Triss DLC Outfit - Purple | Habits DLC de Triss - Purple | **Habits DLC de Triss - Violet** | RESIDUAL_ENGLISH_COLOR |
| `tw3_femalearmors_zzjay.esp.json` | `020008C0|TW3_femaleArmors_zzjay.esp` | `BOOK DESC` | — | [pagebreak] <p align="center">   Last Seed, 198 Sart... | [pagebreak] <p align="center">  Dernière graine, 198 Secr... | **[pagebreak] <p align="center">  Dernière graine, 198 Secr...** | TYPO_EXTRANEOUS_CHAR |
| `trissarmorretextured.esp.json` | `02000809|TrissArmorRetextured.esp` | `BOOK FULL` | — | Tailor's Yearly - 3E 177 Edition | Annuel du tailleur - 3E 177 Edition | **L'Annuel du tailleur - Édition 3E 177** | BOOK_TITLE_HARMONIZATION |
| `trissarmorretextured.esp.json` | `0200089C|TrissArmorRetextured.esp` | `ARMO FULL` | — | Night Strider's Jerkin (Shirtless) | Jerkin du Marcheur Nocturne (torse nu) | **Pourpoint de l'arpenteur nocturne (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000827|TrissArmorRetextured.esp` | `ARMO FULL` | — | Night Strider's Jerkin | Jerkin du Marcheur Nocturne | **Pourpoint de l'arpenteur nocturne** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000815|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ancient Assassin's Jerkin | Jerkin de l'assassin ancien | **Pourpoint d'assassin antique** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200080D|TrissArmorRetextured.esp` | `ARMO FULL` | — | Thief's Studded Jerkin | Jerkin clouté de voleur | **Pourpoint clouté de voleur** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200082E|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Boots | Bottes de Ranger | **Bottes de rôdeur** | BETHOFF_RANGER_TO_RODEUR |
| `trissarmorretextured.esp.json` | `0200082B|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Studded Jerkin | Jerkine cloutée de Ranger | **Pourpointe cloutée de rôdeur** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A3|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ancient Assassin's Studded Jerkin (Shirtless) | Jerkine cloutée de l'assassin ancien (torse nu) | **Pourpointe cloutée d'assassin antique (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A5|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Studded Jerkin (Shirtless) | Jerkin clouté du Ranger (torse nu) | **Pourpoint clouté du Ranger (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000831|TrissArmorRetextured.esp` | `ARMO FULL` | — | Mercenary's Studded Jerkin | Jerkine cloutée de mercenaire | **Pourpointe cloutée de mercenaire** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000813|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ancient Assassin's Studded Jerkin | Jerkin clouté de l'assassin ancien | **Pourpoint clouté d'assassin antique** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200082D|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Jerkin | Jerkin de Ranger | **Pourpoint de rôdeur** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000819|TrissArmorRetextured.esp` | `ARMO FULL` | — | Vagrant's Studded Jerkin | Jerkine cloutée de vagabond | **Pourpointe cloutée de vagabond** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200080F|TrissArmorRetextured.esp` | `ARMO FULL` | — | Thief's Jerkin | Jerkin de voleur | **Pourpoint de voleur** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200089F|TrissArmorRetextured.esp` | `ARMO FULL` | — | Mercenary's Jerkin (Shirtless) | Jerkin de mercenaire (torse nu) | **Pourpoint de mercenaire (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A7|TrissArmorRetextured.esp` | `ARMO FULL` | — | Mercenary's Studded Jerkin (Shirtless) | Jerkine cloutée de mercenaire (torse nu) | **Pourpointe cloutée de mercenaire (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200089A|TrissArmorRetextured.esp` | `ARMO FULL` | — | Forest Stalker's Jerkin (Shirtless) | Jerkin de chasseur forestier (torse nu) | **Pourpoint de traqueur forestier (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A1|TrissArmorRetextured.esp` | `ARMO FULL` | — | Vagrant's Studded Jerkin (Shirtless) | Jerkine cloutée de vagabond (torse nu) | **Pourpointe cloutée de vagabond (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200089D|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Jerkin (Shirtless) | Jerkin de Ranger (torse nu) | **Pourpoint de rôdeur (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200080A|TrissArmorRetextured.esp` | `ARMO FULL` | — | Sorceress' Jerkin | Jerkin de sorcière | **Pourpoint de sorcière** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200082C|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Studded Boots | Bottes cloutées de Ranger | **Bottes cloutées de rôdeur** | BETHOFF_RANGER_TO_RODEUR |
| `trissarmorretextured.esp.json` | `020008A2|TrissArmorRetextured.esp` | `ARMO FULL` | — | Forest Stalker's Studded Jerkin (Shirtless) | Jerkine cloutée de chasseur forestier (torse nu) | **Pourpointe cloutée de traqueur forestier (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200081F|TrissArmorRetextured.esp` | `ARMO FULL` | — | Forest Stalker's Studded Jerkin | Jerkin clouté de chasseur forestier | **Pourpoint clouté de traqueur forestier** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000899|TrissArmorRetextured.esp` | `ARMO FULL` | — | Vagrant's Jerkin (Shirtless) | Jerkin de vagabond (torse nu) | **Pourpoint de vagabond (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000825|TrissArmorRetextured.esp` | `ARMO FULL` | — | Night Strider's Studded Jerkin | Jerkin clouté du Marcheur Nocturne | **Pourpoint clouté de l'arpenteur nocturne** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200089B|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ancient Assassin's Jerkin (Shirtless) | Jerkin de l'assassin ancien (torse nu) | **Pourpoint d'assassin antique (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A6|TrissArmorRetextured.esp` | `ARMO FULL` | — | Sorceress' Studded Jerkin (Shirtless) | Jerkine cloutée de sorcière (torse nu) | **Pourpointe cloutée de sorcière (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200082F|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Gloves | Gants de Ranger | **Gants de rôdeur** | BETHOFF_RANGER_TO_RODEUR |
| `trissarmorretextured.esp.json` | `020008A4|TrissArmorRetextured.esp` | `ARMO FULL` | — | Night Strider's Studded Jerkin (Shirtless) | Jerkin clouté du Marcheur Nocturne (torse nu) | **Pourpoint clouté de l'arpenteur nocturne (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `0200089E|TrissArmorRetextured.esp` | `ARMO FULL` | — | Sorceress' Jerkin (Shirtless) | Jerkin de sorcière (torse nu) | **Pourpoint de sorcière (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000898|TrissArmorRetextured.esp` | `ARMO FULL` | — | Thief's Jerkin (Shirtless) | Jerkin de voleur (torse nu) | **Pourpoint de voleur (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000800|TrissArmorRetextured.esp` | `ARMO FULL` | — | Sorceress' Studded Jerkin | Jerkine cloutée de sorcière | **Pourpointe cloutée de sorcière** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `020008A0|TrissArmorRetextured.esp` | `ARMO FULL` | — | Thief's Studded Jerkin (Shirtless) | Jerkine cloutée de voleur (torse nu) | **Pourpointe cloutée de voleur (torse nu)** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000809|TrissArmorRetextured.esp` | `BOOK DESC` | — | [pagebreak] <p align="center">   <font size="25"><img... | [pagebreak] <p align="center">   <font size="25"><img src... | **[pagebreak] <p align="center">   <font size="25"><img src...** | BETHOFF_JERKIN_TO_POURPOINT |
| `trissarmorretextured.esp.json` | `02000830|TrissArmorRetextured.esp` | `ARMO FULL` | — | Ranger's Studded Gloves | Gants cloutés de Ranger | **Gants cloutés de rôdeur** | BETHOFF_RANGER_TO_RODEUR |
