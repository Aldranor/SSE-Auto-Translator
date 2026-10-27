# Récapitulatif des Modifications — Phase 2B : Quêtes, Expérience & Mécaniques Locales

> **Périmètre :** Sous-phase 2B de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).
> **Mods audités :** 10 mods locaux d'expérience, quêtes, religions et mécaniques (`CCQuest - Experience Patch`, `Nolvus Experience Integration`, `Lucien CC Patch`, `Vokrii Spell Conditions Fix`, `Wintersun Description Fixes & Tribunal Integration`, `CCOR Immersive Sounds Patch`, `Crossbow Integration`, `Navigator Navmesh Fixes`, `Eating Animations and Sounds Patch Collection`).
> **Volume de vérification :** 4 541 enregistrements contrôlés, intégrité des variables dynamiques, fidélité géographique et lore officiel Bethesda.

---

## 📁 ccquest - experience patch.esp.json
*Nombre d'ajustements majeurs :* **1**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `1000080F (ccbgssse020-graycowl.esl)`<br>*QUST CNAM* | At the Riften cemetery, I found a thief loitering near a tombstone. On his body was a note that mentioned the Gray Fox was dead, and his cowl was to be passed on to a new owner. I then spoke to a beggar who handed me a note. | At the Riften cemetery, I found a thief loitering near a tombstone. On his body was a note that mentioned the Gray Fox was dead, and his cowl was to be passed on to a new owner. I spoke to a beggar who handed me a note informing me of a job. | **Au cimetière de Faillaise, j'ai trouvé un voleur qui rôdait près d'une pierre tombale. Sur son corps se trouvait une note mentionnant que le Renard gris était mort et que son capuchon devait être transmis à un nouveau propriétaire. J'ai ensuite parlé à un mendiant qui m'a remis une note m'informant d'un travail.** | Traduction intégrale d'une étape de quête du Capuchon gris de Nocturne restée en anglais |

---

## 📁 taberu animation - dawn of skyrim patch.esp.json
*Nombre d'ajustements majeurs :* **8**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `02020D57 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Falkreath Porridge | Porridge de Faillaise | **Porridge d'Épervine** | Correction de contresens géographique critique : Falkreath = Épervine (et non Faillaise/Riften) |
| `02020D54 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Haafingar Butter | Beure d'Haafingar | **Beurre d'Haafingar** | Correction de coquille : Beurre (au lieu de Beure) |
| `0201DE7F (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Pheasant Pie | Tarte au Faisant | **Tourte au faisan** | Correction de coquille orthographique : faisan (au lieu de Faisant) et gastronomie médiévale |
| `0201DE83 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Dawnstar Spiced Cake | Cake épicé d'Aubétoile | **Gâteau aux épices d'Aubétoile** | Élimination de l'anglicisme 'Cake' -> Gâteau aux épices |
| `0201DE85 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Midyear Cake | Cake de mi-l'an | **Gâteau de mi-l'an** | Élimination de l'anglicisme 'Cake' -> Gâteau |
| `0201DE87 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Ivarstead Loaf | Tourte de Fort-Ivar | **Pain de Fort-Ivar** | Fidélité au mod source : Pain (Loaf) au lieu de Tourte |
| `0201DE7A (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Solitude Dusted Bread | Pain Traditionnel de Solitude | **Pain au poivre de Solitude** | Harmonisation Dawn of Skyrim : Dusted Bread = Pain au poivre |
| `0201DE81 (Dawn of Skyrim.esp)`<br>*ALCH FULL* | Snowberry Biscuit | Biscuit de Givreboise | **Biscuit aux givreboises** | Terminologie officielle Bethesda : givreboises (Snowberry) |

---

## 📁 taberu animation - cheesemod patch.esp.json
*Nombre d'ajustements majeurs :* **2**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `02003782 (yumcheese.esp)`<br>*ALCH FULL* | Sliced Autumnshade Cheese | Brie des Ombres de l'Automne entamé | **Brie de Vendombre entamé** | Harmonisation toponyme canonique : Autumnshade = Vendombre |
| `02003786 (yumcheese.esp)`<br>*ALCH FULL* | Autumnshade Cheese Wedge | Brie des Ombres de l'Automne | **Brie de Vendombre** | Harmonisation toponyme canonique : Autumnshade = Vendombre |

---

## 📁 navigator-navfixes.esl.json
*Nombre d'ajustements majeurs :* **3**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `0001529F (Skyrim.esm)`<br>*CELL FULL* | Darklight Tower | Tour Clair-osbcur | **Tour Clair-Obscur** | Correction de coquille dans le nom de lieu : Clair-Obscur (au lieu de Clair-osbcur) |
| `000466CB (Skyrim.esm)`<br>*CELL FULL* | Irkngthand Sanctuary | Irkngthand - Sanctuaire | **Sanctuaire d'Irkngthand** | Canon officiel Bethesda : Sanctuaire d'Irkngthand |
| `0002164A (Skyrim.esm)`<br>*CELL FULL* | Avanchnzel Boilery | Avanchnzel - Brasserie | **Brasserie d'Avanchnzel** | Canon officiel Bethesda : Brasserie d'Avanchnzel |

---

## 📁 wintersun - gott patch.esp.json
*Nombre d'ajustements majeurs :* **3**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `05000849 (Wintersun - GotT Patch.esp)`<br>*MGEF DNAM* | Items are enchanted <Global=WSN_Favor_Global_Fractional3>% stronger (based on favor with Sotha Sil). | Les objets sont enchantés jusqu'à 20% plus puissamment (basé sur la faveur de Sotha Sil). | **Les enchantements d'objets sont <Global=WSN_Favor_Global_Fractional3> % plus puissants (selon votre ferveur envers Sotha Sil).** | Rétablissement de la variable dynamique moteur <Global=WSN_Favor_Global_Fractional3> écrasée à tort par une valeur fixe '20%' |
| `05000879 (Wintersun - GotT Patch.esp)`<br>*MGEF DNAM* | When health falls below <25>% in combat, receive an automatic healing pulse.  Restored by prayer. | Lorsque la santé tombe en dessous de 25% en combat, recevez une impulsion de guérison automatique. Restauré par la prière. | **Lorsque votre santé passe sous les <25> % en combat, vous recevez une pulsation de soins automatique. Se recharge par la prière.** | Conservation de la variable <25> conforme à l'original et tournure française naturelle |
| `0406AD19 (Wintersun - Faiths of Skyrim.esp)`<br>*MGEF DNAM* | Your benevolence improves your Speech skill by <mag> points for <1> hour. | Votre générosité améliore votre éloquence de <mag> points pour 1 heure. | **Votre bienveillance améliore votre éloquence de <mag> points pendant <1> heure.** | Conservation de la variable <1> conforme à l'original |

---

## 📁 ImmersiveSoundsCompendium_CCOR_Patch.esp.json
*Nombre d'ajustements majeurs :* **12**

| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |
| :--- | :--- | :--- | :--- | :--- |
| `000F6904 (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation (minuscule sur articulation) |
| `000F6904 (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <10> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 10 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <10> points.** | Conservation de la variable <10> conforme à l'original et tournure française naturelle |
| `000F690D (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation |
| `000F690D (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <15> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 15 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <15> points.** | Conservation de la variable <15> conforme à l'original et tournure française naturelle |
| `000F690E (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation |
| `000F690E (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <20> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 20 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <20> points.** | Conservation de la variable <20> conforme à l'original et tournure française naturelle |
| `000F690F (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation |
| `000F690F (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <25> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 25 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <25> points.** | Conservation de la variable <25> conforme à l'original et tournure française naturelle |
| `000F6910 (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation |
| `000F6910 (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <30> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 30 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <30> points.** | Conservation de la variable <30> conforme à l'original et tournure française naturelle |
| `000F6911 (Skyrim.esm)`<br>*ARMO FULL* | Amulet of Articulation | Amulette d'Articulation | **Amulette d'articulation** | Canon officiel Bethesda : Amulette d'articulation |
| `000F6911 (Skyrim.esm)`<br>*ARMO DESC* | Persuade checks in dialogue will almost always succeed and increases Speech skill by <35> points. | Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 35 points. | **Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <35> points.** | Conservation de la variable <35> conforme à l'original et tournure française naturelle |

---
