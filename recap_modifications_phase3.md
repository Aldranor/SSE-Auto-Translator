# Récapitulatif des Modifications — Phase 3 (Poids Lourds Narratifs & Dialogues)

> [!NOTE]
> **Protocole strict appliqué :**
> - Ciblage unitaire strict sur le quadruple `(form_id, type, index, original)` avec assertion formelle `count == 1`.
> - Vérification indépendante après écriture sur le disque de l'intégralité des 289 modifications.
> - Aucune régression ni diffusion de traduction constatée.

## Synthèse des fichiers audités et modifiés

| Fichier audité | Registre FormID | Type de mod | Total lignes | Modifs appliquées | Statut post-contrôle |
| :--- | :--- | :--- | :---: | :---: | :---: |
| `fanatical enemies.esp.json` | `Fanatical Enemies.esp` | Ennemis & PNJ | 4 615 | 1 | **Validé (100%)** |
| `hlioremi.esp.json` | `HLIORemi.esp` | Compagnon Remiel | 8 300 | 288 | **Validé (100%)** |
| `hliiremilotd.esp.json` | `HLIIRemiLOTD.esp` | Patch LOTD Remiel | 945 | 0 | **Conforme (100%)** |
| `hlizremiarnima.esp.json` | `HLIZRemiArnima.esp` | Patch Beyond Reach | 406 | 0 | **Conforme (100%)** |
| `vigilant.esm.json` | `Vigilant.esm` | Quête narrative | 7 070 | 0 | **Conforme (100%)** |
| `vigilant voiced.esp.json` | `Vigilant Voiced.esp` | Voix & marchandage | 427 | 0 | **Conforme (100%)** |
| `vigilant - giant creatures.esp.json` | `Vigilant.esm` | Patch correctif | 5 | 0 | **Conforme (100%)** |
| `akavirifollower.esp.json` | `AkaviriFollower.esp` | Compagnon Akavirois | 321 | 0 | **Conforme (100%)** |

**Total lignes auditées dans la Phase 3 :** 22 089 entrées  
**Total modifications effectives validées :** 289 entrées  

---

## 1. Correction Lore Fanatical Enemies (1 entrée)

| Fichier | FormID | Type | Index | Texte Source (EN) | Ancienne valeur observée | Nouvelle valeur finale | Justification |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| `fanatical enemies.esp.json` | `049CADDC\|Fanatical Enemies.esp` | `NPC_ FULL` | `None` | `Lord of Falkreath` | `Seigneur de Faillaise` | `Seigneur d'Épervine` | Correction géographique lore : Falkreath = Épervine |

---

## 2. Traductions & Harmonisations Remiel (`hlioremi.esp.json`, 288 entrées)

### A. Quête & Perks de Ferraille (3 entrées)

| FormID | Type | Index | Source (EN) | Ancienne valeur | Nouvelle valeur finale |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `052985FD\|HLIORemi.esp` | `QUST FULL` | `None` | `Tamriel's Tastiest Stew` | `Tamriel's Tastiest Stew` | `Le ragoût le plus savoureux de Tamriel` |
| `052D5256\|HLIORemi.esp` | `PERK FULL` | `None` | `Scrap's Extra Damage 1.5` | `Scrap's Extra Damage 1.5` | `Dégâts supplémentaires de Ferraille (x1,5)` |
| `052D5257\|HLIORemi.esp` | `PERK FULL` | `None` | `Scrap's Extra Damage 2` | `Scrap's Extra Damage 2` | `Dégâts supplémentaires de Ferraille (x2)` |

### B. Commentaires de Quête & Lore (Gildergreen, Parjures, Marais Noir) (11 entrées)

| FormID | Type | Source (EN) | Valeur finale française |
| :--- | :--- | :--- | :--- |
| `058C2154\|HLIORemi.esp` | `INFO NAM1` | A few months after I joined. It wasn't one big incident that... | Quelques mois après avoir rejoint la guilde. Ce n'est pas un incident particulier qui m'a décidée à partir ; j'ai juste fini par ne plus m'y présenter, petit à petit. |
| `05810A00\|HLIORemi.esp` | `INFO NAM1` | No. I carry a sword. I'm from the swamps of Black Marsh. Do ... | Non. Je porte une épée. Je viens des marécages du Marais noir. Vous voulez que je continue, ou vous avez compris l'idée ? |
| `05940BE5\|HLIORemi.esp` | `INFO NAM1` | I've always felt the Forsworn were no better than Witchmen. ... | J'ai toujours pensé que les Parjures ne valaient pas mieux que les sorciers. Depuis la mine de Cidhna, j'ai le sentiment d'avoir eu raison d'y croire. |
| `05B2C4CA\|HLIORemi.esp` | `INFO NAM1` | Oh, the little new Gildergreen is... really great... It real... | Oh, le nouveau petit Végétalia est... vraiment génial... Ça valait vraiment toute cette peine... |
| `05B2C4C9\|HLIORemi.esp` | `INFO NAM1` | 'A man of violence,' he says. This is a tree, not his kin.... | « Un homme de violence », qu'il dit. C'est un arbre, pas sa propre famille. |
| `058B2E06\|HLIORemi.esp` | `INFO NAM1` | Are you very familiar with thieves, Yazakh?... | Vous connaissez bien les voleurs, Yazakh ? |
| `05B2C4CD\|HLIORemi.esp` | `INFO NAM1` | And where are they going to put the old Gildergreen? Are the... | Et où vont-ils mettre l'ancien Végétalia ? Vont-ils le débiter ? Pensez-vous que son bois possède des propriétés uniques ? Hm. |
| `05B2C4C8\|HLIORemi.esp` | `INFO NAM1` | 'A woman of violence,' he says. This is a tree, not his kin.... | « Une femme de violence », qu'il dit. C'est un arbre, pas sa propre famille. |
| `0581AD7D\|HLIORemi.esp` | `INFO NAM1` | Ha-Ha. Do you have any more bad jokes? Because then I'd be o... | Ha-ha. Vous avez d'autres blagues nulles ? Parce que sinon je vais me retrouver au chômage. |
| `05B2C4C4\|HLIORemi.esp` | `INFO NAM1` | So did this hagraven forge Nettlebane? I can't imagine a hag... | Alors, c'est cette harfreuse qui a forgé Fléau d'ortie ? J'ai du mal à imaginer une harfreuse près d'une forge. Leurs plumes prendraient feu, je pense. |
| `05B2C4C6\|HLIORemi.esp` | `INFO NAM1` | I've been resisting saying this, but what is the point of re... | Je me retenais de le dire, mais quel est l'intérêt de ranimer Végétalia ? Juste pour attirer des pèlerins ? Le Temple n'est pas déjà assez joli comme ça ? |

### C. Dialogues & Banter Compagnons (Échantillon représentatif de 25 entrées)

| FormID | Type | Source (EN) | Traduction française appliquée |
| :--- | :--- | :--- | :--- |
| `05B4AC2D\|HLIORemi.esp` | `INFO NAM1` | Good work out there, Raven! | Beau travail, Raven ! |
| `05B4AC22\|HLIORemi.esp` | `INFO NAM1` | We are going to live, Doc! Right? | On va s'en sortir vivants, Doc ! Pas vrai ? |
| `05B4AC04\|HLIORemi.esp` | `INFO NAM1` | You do not want to fight Ria! Or me! | Vous ne voulez vraiment pas vous battre contre Ria ! Ni contre moi ! |
| `05B4FD55\|HLIORemi.esp` | `INFO NAM1` | Well bye, Joshua. Bye for now, at least. | Eh bien, au revoir, Joshua. Du moins pour l'instant. |
| `05B4FD4C\|HLIORemi.esp` | `INFO NAM1` | Scrap, keep Ganbald safe, okay?! | Ferraille, protège Ganbald, d'accord ?! |
| `05B4FD48\|HLIORemi.esp` | `INFO NAM1` | (Gasp) Well, Ganbald, we aren't dead! | (Soupir) Eh bien, Ganbald, nous ne sommes pas morts ! |
| `05B4FD62\|HLIORemi.esp` | `INFO NAM1` | Good work out there, Josh! | Beau travail, Josh ! |
| `05B4ABCB\|HLIORemi.esp` | `INFO NAM1` | I'm happy you're on my side, Buffy. | Je suis contente que vous soyez de mon côté, Buffy. |
| `05B4FD79\|HLIORemi.esp` | `INFO NAM1` | Ahmed, you are a bit scary in battle. Well, everything  | Ahmed, vous faites un peu peur au combat. Enfin, tout fait peur au combat. Est-ce que je fais peur au combat, moi ? |
| `05B4ABAB\|HLIORemi.esp` | `INFO NAM1` | Ubbe. Ubbe. Look at me. Do not forget me here. Ubbe, I  | Ubbe. Ubbe. Regardez-moi. Ne m'oubliez pas ici. Ubbe, je serais si triste. Ne m'oubliez pas. |
| `05B4ABDE\|HLIORemi.esp` | `INFO NAM1` | Well, bye, Revan. Bye for now, at least. | Eh bien, au revoir, Revan. Du moins pour l'instant. |
| `05B4ABFC\|HLIORemi.esp` | `INFO NAM1` | And they're dead, and Ria and I are alive. We win! | Et ils sont morts, et Ria et moi sommes vivants. On a gagné ! |
| `05B4AC0D\|HLIORemi.esp` | `INFO NAM1` | Okay, Doctor, we'll talk later. | D'accord, Doctor, on se parlera plus tard. |
| `05B45A9B\|HLIORemi.esp` | `INFO NAM1` | Don't die, Nar! I'd be very upset with you! | Ne mourez pas, Nar ! Je vous en voudrais beaucoup ! |
| `05B40986\|HLIORemi.esp` | `INFO NAM1` | Are you doing okay out there, Ilia? | Vous tenez le coup, Ilia ? |
| `05B4ABAD\|HLIORemi.esp` | `INFO NAM1` | So we're off then, Ubbe? Lead the way. | On est partis alors, Ubbe ? Montrez le chemin. |
| `05B4FD3D\|HLIORemi.esp` | `INFO NAM1` | I'll be here, Ganbald. And also wherever you take me ne | Je serai là, Ganbald. Et partout où vous m'emmènerez ensuite. |
| `05B4ABDC\|HLIORemi.esp` | `INFO NAM1` | Are we heading out, Revan? | On y va, Revan ? |
| `05B3B859\|HLIORemi.esp` | `INFO NAM1` | Alright, Scrap, let's go. Farillae is leading us somewh | Très bien, Ferraille, on y va. Farillae nous emmène dans un endroit sympa, pas vrai ? |
| `05B4AC1D\|HLIORemi.esp` | `INFO NAM1` | You know you don't need to try to kill Doctor? Or me? | Vous savez que vous n'êtes pas obligés de tuer le Docteur ? Ni moi d'ailleurs ? |
| `05B4ABAE\|HLIORemi.esp` | `INFO NAM1` | Ubbe? Oh, good. You lived. Me too, in case it wasn't ob | Ubbe ? Oh, tant mieux. Vous avez survécu. Moi aussi, au cas où ce ne serait pas évident. |
| `05B4AC0A\|HLIORemi.esp` | `INFO NAM1` | I'll be here, Doctor. And also wherever you take me nex | Je serai là, Doctor. Et partout où vous m'emmènerez ensuite. |
| `05B4ABD4\|HLIORemi.esp` | `INFO NAM1` | We are going to live, Buffy! Right? | On va s'en sortir vivants, Buffy ! Pas vrai ? |
| `05B3B86B\|HLIORemi.esp` | `INFO NAM1` | Ah! Una, look out! We're being attacked! | Ah ! Una, attention ! On nous attaque ! |
| `05B4FD6C\|HLIORemi.esp` | `INFO NAM1` | We won't die! At least, I don't think Josh will let us  | On ne va pas mourir ! Enfin, je ne pense pas que Josh va nous laisser mourir ! Alors voilà ! |

> [!TIP]
> L'ensemble complet des 288 lignes de dialogue traduites est sauvegardé dans `phase3_effective_modifications.json`.

---

## 3. Statut des autres mods narratifs (Zéro anomalie constatée)

- **Vigilant ESM & Voiced (7 497 entrées) :** Les 117 chaînes anglaises correspondent strictement à des effets magiques internes (`Alessia Script Effect`, `Soul Shriven fx`) et des quêtes système invisibles (`Music Manager`, `CO Generic Dialogue`). Zéro anomalie joueur, zéro mojibake.
- **Remiel LOTD & Beyond Reach (1 351 entrées) :** 100% propre, seules 6 lignes `QUST CNAM` de log développeur (`';bring Remi fragments'`) restent en anglais non affiché.
- **Akaviri Follower (321 entrées) :** 100% traduit en français canonique, aucune coquille détectée.

---
**Phase 3 complètement vérifiée et validée.**