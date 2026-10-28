# Récapitulatif des Modifications — Phase 4 (Quêtes, Nouveaux Mondes & LOTD)

> [!NOTE]
> **Protocole strict appliqué :**
> - Ciblage unitaire strict sur le quadruple `(form_id, type, index, original)` avec assertion formelle `count == 1`.
> - Vérification indépendante après écriture sur le disque de l'intégralité des 66 modifications.
> - Harmonisation rigoureuse des artéfacts exposés au Musée avec le master `Unslaad.esm`.

## Synthèse des fichiers audités et modifiés

| Module / Groupe | Total fichiers | Total lignes scannées | Modifs appliquées | Statut post-contrôle |
| :--- | :---: | :---: | :---: | :---: |
| **Legacy of the Dragonborn (Hall of Forgotten & Addons)** | 22 | 2 355 | **4** | **Validé (100%)** |
| **DBM Unslaad Display Patch (Harmonisation Master)** | 1 | 343 | **40** | **Validé (100%)** |
| **LOTD - Hall of Forgotten TCC (Outils du Conservateur)** | 18 | 36 | **18** | **Validé (100%)** |
| **LOTD Follower Room Patches (Auri, Inigo, Lucien, Remiel)** | 4 | 128 | 0 | **Conforme (100%)** |
| **Hjertesten Hall (Domaine joueur & Patches)** | 5 | 1 810 | 0 | **Conforme (100%)** |
| **EEKs Whiterun Interiors** | 1 | 261 | **4** | **Validé (100%)** |
| **Alternate Perspective (Base, Sovngarde, Beginnings)** | 3 | 701 | 0 | **Conforme (100%)** |
| **Quêtes, Villes & Lieux (Sky Haven, Witcher, Riften...)** | 41 | 182 | 0 | **Conforme (100%)** |

**Total lignes auditées dans la Phase 4 :** 5 816 entrées  
**Total modifications effectives validées :** 66 entrées  

---

## 1. EEKs Whiterun Interiors (4 corrections unitaires)

| Fichier | FormID | Type | Source (EN) | Ancienne valeur | Nouvelle valeur finale | Justification |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `eeks whiterun interiors.esp.json` | `0602DDD6\|EEKs Whiterun Interiors.esp` | `NPC_ FULL` | `Aalia` | `None` | `Aalia` | Correction valeur nulle / PNJ |
| `eeks whiterun interiors.esp.json` | `0602DDD6\|EEKs Whiterun Interiors.esp` | `NPC_ SHRT` | `Aalia` | `None` | `Aalia` | Correction valeur nulle / PNJ |
| `eeks whiterun interiors.esp.json` | `0605B47B\|EEKs Whiterun Interiors.esp` | `FLOR FULL` | `Red Mountain Flowers` | `Fleurs de montagne rouge` | `Fleurs rouges de montagne` | Lore officiel flore Skyrim |
| `eeks whiterun interiors.esp.json` | `06058CCB\|EEKs Whiterun Interiors.esp` | `FLOR FULL` | `Red Mountain Flowers` | `Fleurs de montagne rouge` | `Fleurs rouges de montagne` | Lore officiel flore Skyrim |

---

## 2. DBM Identity Crisis Patch (4 corrections unitaires)

| Fichier | FormID | Type | Source (EN) | Ancienne valeur | Nouvelle valeur finale | Justification |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `dbm_identitycrisis_patch.esp.json` | `0700085A\|DBM_IdentityCrisis_Patch.esp` | `MISC FULL` | `Heart of Arden-Sul (replica)` | `Coeur d'Arden-Sul (replica)` | `Cœur d'Arden-Sul (réplique)` | Anglais résiduel `(replica)` |
| `dbm_identitycrisis_patch.esp.json` | `07000856\|DBM_IdentityCrisis_Patch.esp` | `ARMO FULL` | `Intriguer's Cowl (replica)` | `Capuchon de l'Intrigant (replica)` | `Capuchon de l'Intrigant (réplique)` | Anglais résiduel `(replica)` |
| `dbm_identitycrisis_patch.esp.json` | `07000857\|DBM_IdentityCrisis_Patch.esp` | `LIGH FULL` | `Heart of Arden-Sul (replica)` | `Coeur d'Arden-Sul (replica)` | `Cœur d'Arden-Sul (réplique)` | Anglais résiduel `(replica)` |
| `dbm_identitycrisis_patch.esp.json` | `07000852\|DBM_IdentityCrisis_Patch.esp` | `CONT FULL` | `Identity Crisis Items` | `Items de "Identity crisis"` | `Objets de la Crise d'identité` | Harmonisation quête / conteneur |

---

## 3. DBM Unslaad Display Patch (40 harmonisations Master)

> [!IMPORTANT]
> Ces 40 ajustements garantissent que l'intitulé de la plaque d'exposition dans le Musée du Ralliement correspond exactement à l'objet détenu par le joueur dans son inventaire issu du master `Unslaad.esm`.

| FormID | Type | Source (EN) | Ancienne valeur plaque | Valeur Master Unslaad alignée |
| :--- | :---: | :--- | :--- | :--- |
| `09000C02\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Magnar's Warrior Longspear | Espadon du guerrier Magnar | **Espadon du guerrier Magnar** |
| `09000825\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Gauntlets | Gantelets de Tueur de dragon | **Gantelets de Tueur de dragon** |
| `0900083F\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Half-Dragon Doll | Poupée demi-dragon | **Poupée demi-dragon** |
| `0900082E\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | The Owl Flies at Dusk | Le hibou vole au crépuscule | **Le hibou vole au crépuscule** |
| `09000827\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Armor | Armure de Tueur de dragon | **Armure de Tueur de dragon** |
| `0900083E\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Fang of the Old Dragon | Croc du Vieux dragon | **Croc du Vieux dragon** |
| `09000831\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Ja'cobee's Dragon Pipe | Pipeau draconique de Ja'cobee | **Pipeau draconique de Ja'cobee** |
| `09000807\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Boots | Bottes de Tueur de dragon | **Bottes de Tueur de dragon** |
| `09000811\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Alcaire Greatlance | Grande lance d'Alcaire | **Grande lance d'Alcaire** |
| `09000DCB\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | The 36 Lessons of Vivec: Sermon 37 | Les 36 Leçons de Vivec : Sermon 37 | **Les 36 Leçons de Vivec : Sermon 37** |
| `0900082B\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Silver Great Keyblade | Grande Clef-Lame d'argent | **Grande Clef-Lame d'argent** |
| `09000833\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Golden Pus | Masque de Purulence dorée | **Masque de Purulence dorée** |
| `09000C13\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Khemkel's Carving Knife | Couteau à sculpter de Khemkel | **Couteau à sculpter de Khemkel** |
| `09000829\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Greatshield | Grand bouclier de Tueur de dragon | **Grand bouclier de Tueur de dragon** |
| `09000820\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Orkey Greataxe | Grande hache d'Orkey | **Grande hache d'Orkey** |
| `09000826\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Helmet | Casque de Tueur de dragon | **Casque de Tueur de dragon** |
| `09000C15\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Ysgramor's Fork | Fourche d'Ysgramor | **Fourche d'Ysgramor** |
| `09000819\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Greatsword | Espadon de Tueur de dragon | **Espadon de Tueur de dragon** |
| `09000C0D\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Honeybee's Silver Sting | Piqûre d'argent d'Abeille | **Piqûre d'argent d'Abeille** |
| `0900080E\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Hoarfrost Scythe | Faux de Feralgide | **Faux de Feralgide** |
| `09000824\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Hands of Gods | Mains de Dieux | **Mains de Dieux** |
| `0900080C\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Festering Lesion | Couronne de Suppuration | **Couronne de Suppuration** |
| `09000809\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Frozen Dragon Soul | Âme de dragon gelé | **Âme de dragon gelé** |
| `0900081B\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Gray Owl's Mask | Masque du Hibou Gris | **Masque du Hibou Gris** |
| `09000821\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Festering Greatsword | Espadon de Suppuration | **Espadon de Suppuration** |
| `09000834\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Darkstalker's Staff | Bâton de Rôdeur sombre | **Bâton de Rôdeur sombre** |
| `09000818\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Zweihander | Claymore | **Claymore** |
| `0900082D\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Mage Shield | Bouclier du Mage | **Bouclier du Mage** |
| `09000836\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Curse Ward Greatsword | Espadon Barrière maudite | **Espadon Barrière maudite** |
| `09000C1E\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Roots of a Woodland Man | Racines d'un homme des bois | **Racines d'un homme des bois** |
| `09000C17\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Oracle-Oocyte Amulet | Amulette de l'Oracle Gamétocyte | **Amulette de l'Oracle Gamétocyte** |
| `09000DD6\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Oracle Iridescent Mask | Masque de l'Oracle Iridescent | **Masque de l'Oracle Iridescent** |
| `09000822\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Vermilion Bow | Arc Vermillon | **Arc Vermillon** |
| `0900090D\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Lingering Snow | Neige persistante | **Neige persistante** |
| `0900083A\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Curse Ward Greatshield | Grand bouclier de Maléfice | **Grand bouclier de Maléfice** |
| `09000828\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Dragonslayer Ring | Anneau de Tueur de dragon | **Anneau de Tueur de dragon** |
| `09000838\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Elden Helmet | Casque de l'Aîné | **Casque de l'Aîné** |
| `09000812\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Elden Shield | Bouclier de l'Aîné | **Bouclier de l'Aîné** |
| `09000841\|DBM_Unslaad_Display_Patch.esp` | `ARMO FULL` | Gray Egg | Œuf gris | **Œuf gris** |
| `0900081A\|DBM_Unslaad_Display_Patch.esp` | `ACTI FULL` | Frost Shield | Bouclier glacé | **Bouclier glacé** |

---

## 4. LOTD - Hall of Forgotten TCC (18 harmonisations Outils du Conservateur)

| Fichier | FormID | Notification originale (EN) | Notification française harmonisée |
| :--- | :--- | :--- | :--- |
| `lotd_tcc_aiolas.esp.json` | `02000801\|LOTD_TCC_AIOLAS.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Legendary Alpha Shields)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Boucliers alpha légendaires)</font>`** |
| `lotd_tcc_babayaga.esp.json` | `09000801\|LOTD_TCC_BabaYaga.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Baba Yaga and the Labyrinth)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Baba Yaga et le Labyrinthe)</font>`** |
| `lotd_tcc_billyrow.esp.json` | `09000803\|LOTD_TCC_BillyRoW.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (BillyRo Ultimate Swords Anthology)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Anthologie ultime d'épées de BillyRo)</font>`** |
| `lotd_tcc_carved brink.esp.json` | `09000803\|LOTD_TCC_Carved Brink.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Carved Brink)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Bord abrupt)</font>`** |
| `lotd_tcc_curseofthehoundamulet.esp.json` | `0A000803\|LOTD_TCC_CurseOfTheHoundAmulet.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Curse Of The Hound Amulet)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Malédiction de l'amulette du chien)</font>`** |
| `lotd_tcc_finh.esp.json` | `02000801\|LOTD_TCC_FINH.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Forgotten In History)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Oublié dans l'histoire)</font>`** |
| `lotd_tcc_kings crusader pack(4esl).esp.json` | `09000801\|LOTD_TCC_Kings Crusader Pack(4ESL).esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (King Crusader Mega Pack)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Méga pack du Roi croisé)</font>`** |
| `lotd_tcc_kozakowy_cbbe.esp.json` | `09000801\|LOTD_TCC_Kozakowy_CBBE.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Kozakowy's Falka Armor)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de Falka de Kozakowy)</font>`** |
| `lotd_tcc_ksa.esp.json` | `09000801\|LOTD_TCC_KSA.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Viridian Knight Armor)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de chevalier viridien)</font>`** |
| `lotd_tcc_lunar guard.esp.json` | `09000801\|LOTD_TCC_Lunar Guard.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Lunar Guard Armor)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de la Garde lunaire)</font>`** |
| `lotd_tcc_midwoodisle.esp.json` | `09000803\|LOTD_TCC_MidwoodIsle.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Midwood Isle)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Île de Midwood)</font>`** |
| `lotd_tcc_onyxlancer.esp.json` | `09000801\|LOTD_TCC_OnyxLancer.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Onyx Lancer)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Lancier d'onyx)</font>`** |
| `lotd_tcc_puaio.esp.json` | `09000803\|LOTD_TCC_PUAIO.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (PUAIO)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (PUAIO)</font>`** |
| `lotd_tcc_regal paladinesl.esp.json` | `09000801\|LOTD_TCC_Regal PaladinESL.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Regal Paladin Armor)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de paladin royal)</font>`** |
| `lotd_tcc_sirenroot.esp.json` | `09000801\|LOTD_TCC_SirenRoot.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (SirenRoot)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Racine des Sirènes)</font>`** |
| `lotd_tcc_titus mede.esp.json` | `09000803\|LOTD_TCC_Titus Mede.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Armor of Titus Mede)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armure de Titus Mede)</font>`** |
| `lotd_tcc_velothi.esp.json` | `09000803\|LOTD_TCC_Velothi.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Armors of the Velothi Pt. I)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Armures des Vélothis - Partie I)</font>`** |
| `lotd_tcc_vinditionaio.esp.json` | `09000801\|LOTD_TCC_VinditionAIO.esp` | `<font color='#<Alias=ColourAlias>'>The Curators Companion: Mod Complete (Vindition Weapons Collection)</font>` | **`<font color='#<Alias=ColourAlias>'>Les Outils du Conservateur - Mod complété (Collection d'armes de Vindition)</font>`** |

---

## 5. Statut des autres composants majeurs audités (Zéro anomalie joueur)

- **Hjertesten Hall (1 810 entrées) :** 100% traduit en français de qualité, zéros mojibake, zéro contresens lore.
- **Alternate Perspective (701 entrées) :** Base, Gate to Sovngarde Edition et New Beginnings entièrement traduits et cohérents.
- **Follower Room Patches (128 entrées) :** Auri, Inigo, Lucien et Remiel conformes.
- **Hall of Forgotten (1 740 entrées) :** Plaques et supports de displays conformes aux mods d'armes/armures respectifs.

---
**Phase 4 complètement vérifiée et validée.**