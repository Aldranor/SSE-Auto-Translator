# Bilan de la Phase 1 — Intégrité Technique (Variables, Balises Moteur, Polices, Images & Chaînes Vides)

> [!TIP]
> **Statut de la Phase 1 : 100 % Terminée & Vérifiée sur disque**
> - **Périmètre audité :** 4 952 fichiers JSON de traduction (`397 383` entrées, hors `index.json`).
> - **Fichiers modifiés :** 55 fichiers JSON.
> - **Opérations chirurgicales appliquées :** **512 corrections** réparties en 8 catégories techniques critiques.
> - **Vérification indépendante post-écriture (`verify_clean_phase1.py`) :** **0 anomalie restante** sur les 8 catégories cibles.

---

## 1. Synthèse Quantitative par Catégorie

| Catégorie | Anomalies détectées | Corrections appliquées | Restant après vérification |
| :--- | :---: | :---: | :---: |
| **1. Chaînes vides (`string == ""` avec `original != ""`)** | 436 | 436 | **0** |
| **2. Balises numériques écrasées / corrompues (`<<3>raquelure>`, `Acco<1000>000>`, `pendan<5>`, `d<1500>0>`, `<100.`, `<dur>secondes`)** | 10 | 10 | **0** |
| **3. Variables `<Global=...>` altérées (`_Global_Global_`, `_Gracal_`, `_Chance` vs `_ChanceCurrent`)** | 12 | 12 | **0** |
| **4. Variables `<Alias=...>` corrompues (`< alias=...>`, mauvais alias cible)** | 5 | 5 | **0** |
| **5. Variables `<mag>` / `<dur>` omises ou ajoutées à tort** | 8 | 8 | **0** |
| **6. Spécificateurs `printf` (`%.0f`, `%d`) cassés & chevrons numériques illégaux** | 8 | 8 | **0** |
| **7. Polices de livres (`$BordecielBooks`, `$HandwritingFont`) & chemins d'images (`img://.../Livres/...`)** | 16 | 16 | **0** |
| **8. Balises `[pagebreak]` (`pagebreak]`, `[pause]`, sauts omis) & HTML déséquilibré (`</b>>`, `</font>`)** | 17 | 17 | **0** |
| **TOTAL PHASE 1** | **512** | **512** | **0** |

---

## 2. Détail des Corrections Chirurgicales

### A. Résolution des 436 Chaînes Vides (`EMPTY_FIX`)
Toute entrée marquée `TranslationComplete` avec `string: ""` écrase le nom ou la description par une chaîne vide dans l'ESP généré par SSE Translator :
- **Traductions françaises rétablies (60 entrées) :**
  - `Quests Award Perk Points\quests award perk points.esp.json` (43 entrées `MGEF/QUST/SPEL FULL`) : `"Points d'atout en récompense de quête"`.
  - `Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level.esp.json` : `"Corbeau noir"` (*Dark Raven*), `"Crovenin de feu"` (*Fire Aspfang*), `"Crovenin de glace"` (*Frost Aspfang*), `"Crovenin vermeil"` (*Ruddy Aspfang*), `"Aventurier d'Ustase"` (x2), `"Maître-chien d'Ustase"` (x2), `"Pillard d'Ustase"` (x4).
  - `Abyss - Sorts obscurs\Abyss.esp.json` (`04000857`, `01EA6007`) : `"Maîtrise des aspects"` (*Aspection*).
  - `Granite Hill Village - French\Granite Hill.esp.json` : `"Broyeur d'ennemis"` (*Foecrusher*), `"Poursuivant"` (*Pursuer*).
  - `LOTD - Patches officiels\DBM_ISC_Patch.esp.json` : `"Corail"` (*Coral*), `"Ivoire"` (*Ivory*).
  - `(FR) Palace of the Kings\jk's palace of the kings.esp.json` : `"Mannequin"` (*Manakin*).
  - `La Sorcière et le Labyrinthe\ksws03_quest.esp.json` : `"La cabane de la sorcière ne peut pas voyager jusqu'ici."`, `"Race d'ange"`.
  - `Saleté et sang - Effets visuels dynamiques\Dirt and Blood - Dynamic Visuals.esp.json` (`MESG FULL`) : `"Cheveux plus longs"`.
  - `Commerce & Troc` (`trade & barter.esp.json` & MCM) : `"Inventaires de marchands individualisés"`, `":\tPrix d'achat :"`, `":\tPrix de vente :"`.
  - `Atlas - Marqueurs de carte` (MCM) : `"-- Camps impériaux et sombrages actifs --\nJusqu'à 16 marqueurs (il existe 16 camps, mais seuls ceux qui sont actifs seront affichés)"`.
  - `amatteroftime_english.txt.json` (MCM) : `"Boussole"` (*Compass*).
  - `Ode à la Nature - Compagne Auri\018AuriVIGILANTpatch.esp.json` : `"Commentaires d'Auri - Vigilant"`.
- **Noms propres et termes identiques en français restaurés (`string = original`, `TranslationComplete` — 278 entrées) :**
  - Noms propres de PNJs et lieux dans *Beyond Reach* (`nolvus awakening combat scaling overhaul - enemy level.esp.json`), *Ryn's Saarthal*, *Strongholds - Dushnikh Yal*, *AnotherOakwood*, *Granite Hill*, *TreasureHunter*, *Bruma*, *Wintersun* (`Auriel`, `Jyggalag`, `Syrabane`), *Cutting Room Floor* (`Jen`), etc.
- **Identifiants techniques internes restaurés (`string = original`, `NoTranslationRequired` — 98 entrées) :**
  - `Eldritch Blast.esp.json` (27 entrées `EBpro1`, `EBeffect1`, etc.), `Divine Smite.esp.json` (9 entrées `DSench`, `DSrune`, etc.), `Dirt and Blood` (16 effets internes `Blood1..5`, `Soap FX`, etc.), `Apocalypse` (8 effets `FX`/`Test`), `Adamant - Animated Armory` (8 `Bound ... FX`), `BSHeartland.esm.json` (9 topics/notes de log internes), `Innocence Lost` (5 effets internes), `Wyrmstooth` (4 topics internes).

---

### B. Réparation des Balises Numériques Écrasées (`A_SPLICED_NUMERIC_TAG` — 10 entrées)
- `Conduit - Canalisation de sort\Conduit.esp.json` (`01074FB8|Conduit.esp`) :
  - Avant : `Les coups ajoutent 1 <<3>raquelure>, une fois toutes les 3 secondes maximum. L'attaque qui crée la <3e> <craquelure> inflige <mag> points de dégâts de glace et met fin à la <canalisation>.`
  - Après : `Les coups ajoutent <1 craquelure>, une fois toutes les <3> secondes maximum. L'attaque qui crée la <3e craquelure> inflige <mag> points de dégâts de glace et met fin à <Conduit>.`
- `Ordonnateur - Atouts de Bordeciel\Ordinator - Perks of Skyrim.esp.json` (`030AC6E9|Ordinator - Perks of Skyrim.esp`) :
  - Avant : `Pour le po<750>ur de la Flamme du guerrier : (<<5>nnemi>) Inflige 750 points de dégâts. (<Allié>) Acco<1000>000> % de dégâts d'attaque supplémentaires pendant 5 secondes...`
  - Après : `Pour le porteur de la Flamme du guerrier : (<Ennemi>) Inflige <750> points de dégâts. (<Allié>) Accorde <1000> % de dégâts d'attaque supplémentaires pendant <5> secondes. (<Joueur>) Restaure la totalité de votre santé, magie et vigueur.`
- `Magie de destruction élémentale II\Elemental Destruction Magic Redux.esp.json` (`03000853`) : `subissent 10 points ... pendan<5> 5 secondes` $\rightarrow$ `subissent <mag> points ... pendant <5> secondes`.
- `Sacrosanct - Vampires de Bordeciel\Sacrosanct - Vampires of Skyrim.esp.json` (`03014558`) : `d<1500>0> points` $\rightarrow$ `de <1500> points`.
- `SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json` :
  - `040225F1` : `d<100>00 %` $\rightarrow$ `de <100> %`.
  - `040425E2` & `040425E3` (`Immune to disease and poison.`) : `Augmente les résistances aux maladies et aux poisons de <100.` $\rightarrow$ `Confère une immunité aux maladies et aux poisons.`.
- `Les Outils de Kagrénac\Tools of Kagrenac.esp.json` (`044D5A22`, `042F405B`, `042F405C`) : `<dur>secondes` $\rightarrow$ `<dur> secondes`.

---

### C. Réparation des Variables `<Global=...>` et `<Alias=...>` (`B_GLOBAL_VAR_FIX` & `C_ALIAS_VAR_FIX` — 17 entrées)
- **Variables `<Global=...>` rétablies à l'identique de l'ESP maître (12 entrées) :**
  - `Grognement - Lycanthropes de Bordeciel\Growl - Werebeasts of Skyrim.esp.json` (`0404C7A9`) & `YOT - Growl.esp.json` (`0304C7A9`) : `<Global=HRI_Mortal_Global_CallOfTheBlood_ChanceCurrent>`.
  - `Wintersun - Faiths of Skyrim.esp.json` (`041308F3`, `0426FD3B`, `040DF642`, `0400F93B`, `04284166`, `04060AE5`, `0404C690`) & `YOT - Wintersun.esp.json` (`03302DC1`, `0304C690`, `0326FD3B`) : correction de `_Global_Global_`, `_Gracal_Fractional3`, `_Fractional_Fractional`, et des mauvais indices `Fractional2/3`.
- **Variables `<Alias=...>` rétablies (5 entrées) :**
  - `Armure d'onyx\ksws02.esp.json` (`03000828` idx=400) : `< alias=KeyLocationBandit>` $\rightarrow$ `<alias=KeyLocationBandit>`.
  - `Au-delà de Bordeciel - Bruma\BSHeartland.esm.json` (`02064EE7`) : correction du décalage `Je vais parler à <Alias=GuardCaptain>.` $\rightarrow$ `Quel genre d'ennuis avez-vous ?` (*What trouble are you in?*).
  - `Petites annonces\Missives.esp.json` (`020331A7`, `020331A9`) & `Missives - Wyrmstooth.esp.json` (`0400081D`) : `<Alias=OtherHold>` $\rightarrow$ `<Alias=Hold>` et `<Alias=Dungeon>` $\rightarrow$ `<Alias=Den>`.

---

### D. Variables `<mag>` / `<dur>`, `printf` (`%.0f`) & Chevrons Numériques (`D_MAG_DUR_FIX` & `E_PRINTF_NUMERIC_FIX` — 16 entrées)
- **Variables `<mag>` / `<dur>` rétablies (8 entrées) :**
  - `Abyss.esp.json` (`04000B00`), `DragonbornShoutPerks.esp.json` (`04060B3F`), `Thunderchild - Epic Shout Package.esp.json` (`041535B3`, `041535B5`), `Falskaar.esm.json` (`0111E108`), `Nolvus Awakening Creatures Patch.esp.json` (`11000837|mihailgrummite.esp`), `SPERG-SSE.esp.json` (`0405D194`, `0402FE9A`).
- **Spécificateurs `printf` & chevrons numériques corrigés (8 entrées) :**
  - `Immersive Spell Learning - DESTified\dest_isl.esp.json` (`01000B43`, `01000801`, `01000802`) : restauration des 5 jetons `%.0f` remplacés à tort par `% d'heure(s)` et `%,0f`.
  - `YOT - Wintersun.esp.json` (`0302DFF0`) : `%. 0f` $\rightarrow$ `%.0f`.
  - `Apocalypse - Magic of Skyrim.esp.json` (`030B9E28`) & `YOT - Apocalypse.esp.json` (`020B9E28`) : `<mag> %de dégâts` $\rightarrow$ `<mag> % de dégâts`.
  - `3DNPC.esp.json` (`051564A9`) : `<75> %` $\rightarrow$ `75 %`.
  - `Apothecary.esp.json` (`0010F84C`) : alignement de la traduction avec la version actuelle du mod (`Vous créez une potion ou un poison supplémentaire à partir du même nombre d'ingrédients.`).

---

### E. Polices de Livres, Chemins d'Images, `[pagebreak]` & HTML (`F_FONT_IMG_FIX` & `G_PAGEBREAK_HTML_FIX` — 33 opérations)
- **Polices de livres rétablies :**
  - `Armure de chevalier griffon\GVLT_Gryphonknight.esp.json` (`02000810`) : `$HandwritingFont` $\rightarrow$ `$HandwrittenFont`.
  - `LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json` (7 livres : `05236D5A`, `05236D5F`, `05236D60`, `05236D61`, `0571D14F`, `0571D150`, `0571D151`) : `$BordecielBooks` $\rightarrow$ `$SkyrimBooks`.
- **Chemins d'images (`img://`) réparés :**
  - `Triss Armor Retextured\trissarmorretextured.esp.json` (`02000809`) : restauration des 9 chemins d'images traduits par erreur (`/Livres/` $\rightarrow$ `/Books/`, `sorcière.png` $\rightarrow$ `sorceress.png`, `temper_fr.png` $\rightarrow$ `temper_en.png`).
  - `Conduit - Canalisation de sort\Conduit.esp.json` (`0109D7F6`) : correction de `Textures/Interface/Livres/Illuminated_Letters/A_letter.png` $\rightarrow$ `Books`, correction de la lettrine `F_letter.png'>lace` $\rightarrow$ `G_letter.png'>lace` (*Glace*), et ajout de la phrase finale manquante du paragraphe *Arcanes*.
  - `Au-delà de Bordeciel - Bruma\BSAssets.esm.json` (`01602556`) : `Illuminated_Letters0/L_letter.png` $\rightarrow$ `Illuminated_Letters/L_letter.png`.
  - `Racirène\evgSIRENROOT.esm.json` (`04374415`) : `sirencoronet. png` $\rightarrow$ `sirencoronet.png`.
- **Balises `[pagebreak]` et HTML réparées :**
  - `Chasseur de trésors\TreasureHunter.esp.json` (`030067BC`) & `dbm_treasurehunter_patch.esp.json` (`060067BC`) : remplacement des 6 `[pause]` traduits automatiquement par `[pagebreak]`.
  - `BSAssets.esm.json` (`016024FB`) & `DBM_BSHeartlandPatch - Main.esp.json` (`066024FB`) : `pagebreak]` $\rightarrow$ `[pagebreak]`.
  - `Falskaar.esm.json` & `comprehensive_falskaar_fixes.esp.json` (`010580B7`) : restauration du `[pagebreak]` initial.
  - `Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json` (`0101C7F7`) : restauration des 4 `[pagebreak]` manquants + correction de `Le 2 plantaisons` $\rightarrow$ `Le 12 plantaisons` et du faux-ami `Moron a incendié` $\rightarrow$ `Cet abruti a incendié`.
  - `vigile_1.7.3_sse\vigilant.esm.json` (`021CA545`) : `<p align="center">...</font>` $\rightarrow$ `</p>`.
  - `Wintersun - Faiths of Skyrim.esp.json` (`042EE945`) : `</b>>` $\rightarrow$ `</b>`.
  - `Égouts de Bordeciel\SkyrimSewers.esp.json` (`0504037D`, `050403B8`, `0504FE7F`) : ajout des balises fermantes `</font>` manquantes.
