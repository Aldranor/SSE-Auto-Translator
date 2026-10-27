# Récapitulatif des Modifications — Phase 2A : Patchs Systémiques Nolvus Awakening

> **Périmètre :** Sous-phase 2A de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).
> **Mods audités :** 11 mods d'intégration et patchs Nolvus Awakening (`Combat Scaling Overhaul`, `AI Patch`, `Clothes Patch`, `Clothes Balance Patch`, `Gourmet Integration`, `Stances Perk System`, `Ashes of War`, `Seasonal Plant Mashup`, `Custom Outfits`, `Lighting Patch`, `Northern Roads Grass Patches`).
> **Volume de vérification :** Plus de 18 000 enregistrements contrôlés, intégrité technique et lore officiel Bethesda.

---

## 📁 nolvus awakening clothes patch.esp.json
*Nombre d'ajustements majeurs :* **12**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `0303C0F1 (Dragonborn.esm)`<br>*ARMO FULL* | Miraak's Mask | Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique. | **Masque de Miraak** | Restauration du nom d'objet Masque de Miraak (écrasé par la description de l'enchantement) |
| `0303C0F1 (Dragonborn.esm)`<br>*ARMO DESC* | Increases Magic Resistance by <10>%.  Gives access to Benthic Scream. | Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique. | **Augmente la résistance à la magie de <10> %. Confère l'accès au Cri benthique.** | Conservation de la variable <10> conforme à l'original |
| `000AE087 (Skyrim.esm)`<br>*WEAP DESC* | <5> points of extra damage to Nords. | 5 points de dégâts supplémentaires aux Nordiques. | **<5> points de dégâts supplémentaires aux Nordiques.** | Conservation de la variable <5> conforme à l'original |
| `0010EB65 (Skyrim.esm)`<br>*ARMO FULL* | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | Canon Bethesda : Bouclier de Solitude (au lieu de Rondache) |
| `0010EB64 (Skyrim.esm)`<br>*ARMO FULL* | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | Canon Bethesda : Bouclier de Solitude (au lieu de Rondache) |
| `0010EB63 (Skyrim.esm)`<br>*ARMO FULL* | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | Canon Bethesda : Bouclier de Solitude (au lieu de Rondache) |
| `0009E023 (Skyrim.esm)`<br>*ARMO FULL* | Shield of Solitude | Rondache de Solitude | **Bouclier de Solitude** | Canon Bethesda : Bouclier de Solitude (au lieu de Rondache) |
| `00013989 (Skyrim.esm)`<br>*WEAP FULL* | Steel Sword | Épée en acier | **Épée d'acier** | Canon Bethesda : Épée d'acier (au lieu de en acier) |
| `000139B1 (Skyrim.esm)`<br>*WEAP FULL* | Ebony Sword | Épée en ébonite | **Épée d'ébonite** | Canon Bethesda : Épée d'ébonite (au lieu de en ébonite) |
| `0007947A (Skyrim.esm)`<br>*CELL FULL* | Jorrvaskr Living Quarters | Jorrvaskr - Logements | **Logements de Jorrvaskr** | Canon Bethesda : Logements de Jorrvaskr |
| `000457F7 (Skyrim.esm)`<br>*NPC_ FULL* | Dark Elf | Elfe noir | **Elfe noire** | Accord de genre : PNJ féminin (Elfe noire) |
| `0201684C (Dawnguard.esm)`<br>*NPC_ FULL* | Ferryman | Passeur | **Capitaine** | Canon Bethesda : Capitaine (Passeur vers Volkihar) |

---

## 📁 nolvus awakening clothes balance patch.esp.json
*Nombre d'ajustements majeurs :* **3**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `0100A317 (Apachii_DivineEleganceStore.esm)`<br>*ARMO FULL* | DE Robin Wolf Leather Armor NPC | DE Robin Wolf Leather Armor NPC | **Armure en cuir de loup de Robin (PNJ)** | Traduction française de l'anglais résiduel Apachii |
| `0100A315 (Apachii_DivineEleganceStore.esm)`<br>*ARMO FULL* | DE Robin Gloves NPC | DE Robin Gloves NPC | **Gants de Robin (PNJ)** | Traduction française de l'anglais résiduel Apachii |
| `0100A311 (Apachii_DivineEleganceStore.esm)`<br>*ARMO FULL* | DE Freja Armor NPC | DE Freja Armor NPC | **Armure de Freja (PNJ)** | Traduction française de l'anglais résiduel Apachii |

---

## 📁 nolvus awakening gourmet integration.esp.json
*Nombre d'ajustements majeurs :* **2**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000D882D (Skyrim.esm)`<br>*CONT FULL* | Thieves Guild Fence Chest | Thieves Guild Fence Chest | **Coffre de receleur de la Guilde des voleurs** | Canon Bethesda : Traduction de Thieves Guild Fence Chest |
| `000D882E (Skyrim.esm)`<br>*CONT FULL* | Thieves Guild Fence Chest | Thieves Guild Fence Chest | **Coffre de receleur de la Guilde des voleurs** | Canon Bethesda : Traduction de Thieves Guild Fence Chest |

---

## 📁 Nolvus Awakening Seasonal Plant Mashup.esp.json
*Nombre d'ajustements majeurs :* **5**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000BB949 (Skyrim.esm)`<br>*TREE FULL* | Jazbay | Jazbay | **Raisin jazbay** | Canon Bethesda : Traduction de Jazbay |
| `03010466 (HearthFires.esm)`<br>*TREE FULL* | Jazbay | Jazbay | **Raisin jazbay** | Canon Bethesda : Traduction de Jazbay |
| `09000844 (Nolvus Awakening Seasonal Plant Mashup.esp)`<br>*TREE FULL* | Jazbay | Jazbay | **Raisin jazbay** | Canon Bethesda : Traduction de Jazbay |
| `030110C8 (HearthFires.esm)`<br>*TREE FULL* | Nirnroot | Nirnroot | **Racine de Nirn** | Canon Bethesda : Traduction de Nirnroot |
| `030110BE (HearthFires.esm)`<br>*TREE FULL* | Mora Tapinella | Mora Tapinella | **Mora tapinella** | Canon Bethesda : Traduction de Mora Tapinella |

---

## 📁 Nolvus Awakening AI Patch.esp.json
*Nombre d'ajustements majeurs :* **14**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `00013B76 (Skyrim.esm)`<br>*NPC_ SHRT* | Leontius | Leontius | **Léontius** | Accentuation officielle Skyrim |
| `00013B76 (Skyrim.esm)`<br>*NPC_ FULL* | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Accentuation officielle Skyrim |
| `00065657 (Skyrim.esm)`<br>*NPC_ SHRT* | Erik | Erik | **Érik** | Accentuation officielle Skyrim |
| `00013818 (Skyrim.esm)`<br>*CELL FULL* | Jarl's Longhouse | Longère du jarl de Fortdhiver | **Forteresse Froidepierre** | Canon Bethesda : Forteresse Froidepierre (Jarl's Longhouse Winterhold) |
| `0001365F (Skyrim.esm)`<br>*NPC_ FULL* | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | Canon Bethesda : Suppression tirets superflus |
| `0001365F (Skyrim.esm)`<br>*NPC_ SHRT* | Dravynea | Dravynéa | **Dravynea** | Canon Dunmer : Dravynea sans accent |
| `00013380 (Skyrim.esm)`<br>*NPC_ FULL* | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | Typographie française : Vekel l'homme |
| `0001C196 (Skyrim.esm)`<br>*NPC_ FULL* | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Canon Dunmer : Brelyna sans accent |
| `0001C196 (Skyrim.esm)`<br>*NPC_ SHRT* | Brelyna | Brélyna | **Brelyna** | Canon Dunmer : Brelyna sans accent |
| `0001413D (Skyrim.esm)`<br>*NPC_ FULL* | Ravam Verethi | Ravam Véréthi | **Ravam Verethi** | Canon Dunmer : Ravam Verethi |
| `0001366B (Skyrim.esm)`<br>*NPC_ FULL* | Sondas Drenim | Sondas Drénim | **Sondas Drenim** | Canon Dunmer : Sondas Drenim |
| `0001413A (Skyrim.esm)`<br>*NPC_ FULL* | Revyn Sadri | Révyn Sadri | **Revyn Sadri** | Canon Dunmer : Revyn Sadri |
| `0001413A (Skyrim.esm)`<br>*NPC_ SHRT* | Revyn | Révyn | **Revyn** | Canon Dunmer : Revyn |
| `00014123 (Skyrim.esm)`<br>*NPC_ FULL* | Niranye | Niranyë | **Niranye** | Canon Altmer : Niranye sans tréma |

---

## 📁 nolvus awakening combat scaling overhaul - consistency patch.esp.json
*Nombre d'ajustements majeurs :* **14**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000BFB55 (Skyrim.esm)`<br>*NPC_ FULL* | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | Canon Bethesda : Gardienne Carcette (Keeper Carcette) |
| `00023AB2 (Skyrim.esm)`<br>*NPC_ FULL* | Exmoor Pony | Cheval | **Poney Exmoor** | Restauration race de monture : Poney Exmoor (auparavant uniformisé en Cheval) |
| `00068D5B (Skyrim.esm)`<br>*NPC_ FULL* | Exmoor Pony | Cheval | **Poney Exmoor** | Restauration race de monture : Poney Exmoor (auparavant uniformisé en Cheval) |
| `00068D07 (Skyrim.esm)`<br>*NPC_ FULL* | Black Fell Pony | Cheval | **Poney fell noir** | Restauration race de monture : Poney fell noir (auparavant uniformisé en Cheval) |
| `00068CFA (Skyrim.esm)`<br>*NPC_ FULL* | Black Fell Pony | Cheval | **Poney fell noir** | Restauration race de monture : Poney fell noir (auparavant uniformisé en Cheval) |
| `00068D6E (Skyrim.esm)`<br>*NPC_ FULL* | Palomino Horse | Cheval | **Cheval palomino** | Restauration race de monture : Cheval palomino (auparavant uniformisé en Cheval) |
| `00068D04 (Skyrim.esm)`<br>*NPC_ FULL* | Palomino Horse | Cheval | **Cheval palomino** | Restauration race de monture : Cheval palomino (auparavant uniformisé en Cheval) |
| `00068D6B (Skyrim.esm)`<br>*NPC_ FULL* | Gypsy Horse | Cheval | **Cheval gitan** | Restauration race de monture : Cheval gitan (auparavant uniformisé en Cheval) |
| `00068D02 (Skyrim.esm)`<br>*NPC_ FULL* | Gypsy Horse | Cheval | **Cheval gitan** | Restauration race de monture : Cheval gitan (auparavant uniformisé en Cheval) |
| `00068D6D (Skyrim.esm)`<br>*NPC_ FULL* | Grey Fell Pony | Cheval | **Poney fell gris** | Restauration race de monture : Poney fell gris (auparavant uniformisé en Cheval) |
| `00068D03 (Skyrim.esm)`<br>*NPC_ FULL* | Grey Fell Pony | Cheval | **Poney fell gris** | Restauration race de monture : Poney fell gris (auparavant uniformisé en Cheval) |
| `0001C196 (Skyrim.esm)`<br>*NPC_ FULL* | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Canon Dunmer : Brelyna sans accent |
| `0001C196 (Skyrim.esm)`<br>*NPC_ SHRT* | Brelyna | Brélyna | **Brelyna** | Canon Dunmer : Brelyna sans accent |
| `040179C7 (Dragonborn.esm)`<br>*NPC_ FULL* | Ralis Sedarys | Ralis Sédarys | **Ralis Sedarys** | Canon Dunmer : Ralis Sedarys sans accent |

---

## 📁 nolvus awakening combat scaling overhaul - enemy level mult.esp.json
*Nombre d'ajustements majeurs :* **15**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000BFB55 (Skyrim.esm)`<br>*NPC_ FULL* | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | Canon Bethesda : Gardienne Carcette |
| `0001365F (Skyrim.esm)`<br>*NPC_ FULL* | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | Canon Bethesda : Dravynea |
| `00013B76 (Skyrim.esm)`<br>*NPC_ FULL* | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Accentuation officielle Skyrim |
| `00013B76 (Skyrim.esm)`<br>*NPC_ SHRT* | Leontius | Leontius | **Léontius** | Accentuation officielle Skyrim |
| `0002C925 (Skyrim.esm)`<br>*NPC_ FULL* | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Accentuation officielle Skyrim |
| `00016FF8 (Skyrim.esm)`<br>*NPC_ FULL* | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Canon Bethesda : Valkynaz drémora |
| `0007E87D (Skyrim.esm)`<br>*NPC_ FULL* | Flame Thrall | Golem de feu | **Monarque de feu** | Canon Bethesda : Monarque de feu (Flame Thrall) |
| `0001C196 (Skyrim.esm)`<br>*NPC_ FULL* | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Canon Dunmer : Brelyna Maryon |
| `0001C196 (Skyrim.esm)`<br>*NPC_ SHRT* | Brelyna | Brélyna | **Brelyna** | Canon Dunmer : Brelyna |
| `040179C7 (Dragonborn.esm)`<br>*NPC_ FULL* | Ralis Sedarys | Ralis Sédarys | **Ralis Sedarys** | Canon Dunmer : Ralis Sedarys |
| `0401777C (Dragonborn.esm)`<br>*NPC_ FULL* | Varona Nelas | Varona Nélas | **Varona Nelas** | Canon Dunmer : Varona Nelas |
| `00014123 (Skyrim.esm)`<br>*NPC_ FULL* | Niranye | Niranyë | **Niranye** | Canon Altmer : Niranye |
| `0001413D (Skyrim.esm)`<br>*NPC_ FULL* | Ravam Verethi | Ravam Véréthi | **Ravam Verethi** | Canon Dunmer : Ravam Verethi |
| `0001413A (Skyrim.esm)`<br>*NPC_ FULL* | Revyn Sadri | Révyn Sadri | **Revyn Sadri** | Canon Dunmer : Revyn Sadri |
| `0001413A (Skyrim.esm)`<br>*NPC_ SHRT* | Revyn | Révyn | **Revyn** | Canon Dunmer : Revyn |

---

## 📁 nolvus awakening combat scaling overhaul - enemy level.esp.json
*Nombre d'ajustements majeurs :* **8**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000BFB55 (Skyrim.esm)`<br>*NPC_ FULL* | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | Canon Bethesda : Gardienne Carcette |
| `00016FF8 (Skyrim.esm)`<br>*NPC_ FULL* | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Canon Bethesda : Valkynaz drémora |
| `0402C406 (Dragonborn.esm)`<br>*NPC_ FULL* | Redoran Guard | Garde des Rédorans | **Garde Rédoran** | Canon Bethesda : Garde Rédoran |
| `0003BCC7 (Skyrim.esm)`<br>*NPC_ FULL* | Stormcloak Courier | Messager des Sombrages | **Messager sombrage** | Canon Bethesda : Messager sombrage |
| `0001C196 (Skyrim.esm)`<br>*NPC_ FULL* | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Canon Dunmer : Brelyna Maryon |
| `0001C196 (Skyrim.esm)`<br>*NPC_ SHRT* | Brelyna | Brélyna | **Brelyna** | Canon Dunmer : Brelyna |
| `040179C7 (Dragonborn.esm)`<br>*NPC_ FULL* | Ralis Sedarys | Ralis Sédarys | **Ralis Sedarys** | Canon Dunmer : Ralis Sedarys |
| `00014123 (Skyrim.esm)`<br>*NPC_ FULL* | Niranye | Niranyë | **Niranye** | Canon Altmer : Niranye |

---
