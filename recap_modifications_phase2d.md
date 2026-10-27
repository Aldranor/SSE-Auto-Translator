# Récapitulatif des Modifications — Phase 2D : Patchs de Conflits PNJs, Races & Apparences

> **Périmètre :** Sous-phase 2D de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).
> **Mods audités :** 29 plugins d'intégration et patchs de conflits d'apparence (`Modpocalypse NPCs - Patch Collection` - 13 plugins, `True Sons of Skyrim Refined - Nolvus Patch & TSOS Patches` - 7 plugins, `Fanatical Enemies - Patches` - 4 plugins, `DIbella's Blessing - RSV Exclusion Patches`, `AI Overhaul - Nithi NPC Enhancements Patch Hub` - 4 plugins).
> **Volume de contrôle :** 1 902 enregistrements de PNJs (`NPC_ FULL`, `NPC_ SHRT`) audités avec protocole d'anti-collision unitaire `(form_id, type, index, original)` strict.

---

## 📁 `[xPatch] Modpocalypse NPCs (v3) SSE - AI Overhaul.esp.json`
*Nombre d'ajustements unitaires vérifiés :* **30**

| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |
| :--- | :--- | :--- | :--- | :--- |
| `0001326F\|Skyrim.esm`<br>*NPC_ FULL* | Endarie | Endarie | **Endarië** | Canon officiel Bethesda / Modpocalypse Vanilla : Endarië |
| `00013272\|Skyrim.esm`<br>*NPC_ FULL* | Erikur | Erikur | **Érikur** | Canon officiel Bethesda / TSOS / AI Overhaul : Érikur |
| `00013296\|Skyrim.esm`<br>*NPC_ SHRT* | Wayfinder | Navigateur | **Nautonier** | Canon officiel Bethesda / USSEP : Capitaine Nautonier (court: Nautonier) |
| `000132AB\|Skyrim.esm`<br>*NPC_ FULL* | Taarie | Taarie | **Taarië** | Canon officiel Bethesda / Modpocalypse Vanilla : Taarië |
| `000133B8\|Skyrim.esm`<br>*NPC_ FULL* | Skaggi Scar-Face | Skaggi Balafré | **Skaggi le Balafré** | Canon officiel Bethesda / USSEP / TSOS : Skaggi le Balafré |
| `00013B76\|Skyrim.esm`<br>*NPC_ FULL* | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Canon officiel Bethesda / USSEP : Léontius Salvius |
| `00013B76\|Skyrim.esm`<br>*NPC_ SHRT* | Leontius | Leontius | **Léontius** | Canon officiel Bethesda / USSEP : Léontius |
| `00014122\|Skyrim.esm`<br>*NPC_ FULL* | Suvaris Atheron | Suvaris Atheron | **Suvaris Athéron** | Canon officiel Bethesda / Modpocalypse Vanilla : Suvaris Athéron |
| `00014140\|Skyrim.esm`<br>*NPC_ FULL* | Aval Atheron | Aval Atheron | **Aval Athéron** | Canon officiel Bethesda / Modpocalypse Vanilla : Aval Athéron |
| `0001414E\|Skyrim.esm`<br>*NPC_ FULL* | Malthyr Elenil | Malthyr Elenil | **Malthyr Élénil** | Canon officiel Bethesda / Modpocalypse Vanilla : Malthyr Élénil |
| `00019A2E\|Skyrim.esm`<br>*NPC_ SHRT* | Michel | Michel | **Michelle** | Canon officiel Bethesda / USSEP : Michelle (PNJ Michelle Lylvieve) |
| `00019BFE\|Skyrim.esm`<br>*NPC_ FULL* | Avrusa Sarethi | Avrusa Sarethi | **Avrusa Saréthi** | Canon officiel Bethesda / Nithi / Dibella : Avrusa Saréthi |
| `00019BFF\|Skyrim.esm`<br>*NPC_ FULL* | Aduri Sarethi | Aduri Sarethi | **Aduri Saréthi** | Canon officiel Bethesda / Nithi / Dibella : Aduri Saréthi |
| `0001C182\|Skyrim.esm`<br>*NPC_ FULL* | Malur Seloth | Malur Seloth | **Malur Séloth** | Canon officiel Bethesda / Modpocalypse Vanilla : Malur Séloth |
| `0001C198\|Skyrim.esm`<br>*NPC_ FULL* | Drevis Neloren | Drevis Neloren | **Drévis Néloren** | Canon officiel Bethesda / Modpocalypse Vanilla : Drévis Néloren |
| `0001C198\|Skyrim.esm`<br>*NPC_ SHRT* | Drevis | Drevis | **Drévis** | Canon officiel Bethesda / Modpocalypse Vanilla : Drévis |
| `0002C925\|Skyrim.esm`<br>*NPC_ FULL* | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Canon officiel Bethesda / USSEP : Sévério Pélagia |
| `000350A7\|Skyrim.esm`<br>*NPC_ FULL* | Erik | Erik | **Érik** | Canon officiel Bethesda / USSEP : Érik |
| `0003A1D3\|Skyrim.esm`<br>*NPC_ FULL* | Etienne Rarnis | Etienne Rarnis | **Étienne Rarnis** | Canon officiel Bethesda / Modpocalypse Vanilla : Étienne Rarnis |
| `04017778\|Dragonborn.esm`<br>*NPC_ FULL* | Elynea Mothren | Elynea Mothren | **Élynéa Mothren** | Canon officiel Bethesda / Modpocalypse Vanilla : Élynéa Mothren |
| `04017778\|Dragonborn.esm`<br>*NPC_ SHRT* | Elynea | Elynea | **Élynéa** | Canon officiel Bethesda / Modpocalypse Vanilla : Élynéa |
| `0401777D\|Dragonborn.esm`<br>*NPC_ FULL* | Ulves Romoran | Ulves Romoran | **Ulvès Romoran** | Canon officiel Bethesda / Modpocalypse Vanilla : Ulvès Romoran |
| `0401777D\|Dragonborn.esm`<br>*NPC_ SHRT* | Ulves | Ulves | **Ulvès** | Canon officiel Bethesda / Modpocalypse Vanilla : Ulvès |
| `0401827C\|Dragonborn.esm`<br>*NPC_ FULL* | Aphia Velothi | Aphia Velothi | **Aphia Vélothi** | Canon officiel Bethesda / Modpocalypse Vanilla : Aphia Vélothi |
| `04039D10\|Dragonborn.esm`<br>*NPC_ FULL* | Evul Seloth | Evul Seloth | **Évul Séloth** | Canon officiel Bethesda / Modpocalypse Vanilla : Évul Séloth |
| `04039D10\|Dragonborn.esm`<br>*NPC_ SHRT* | Evul | Evul | **Évul** | Canon officiel Bethesda / Modpocalypse Vanilla : Évul |
| `04039D16\|Dragonborn.esm`<br>*NPC_ FULL* | Meden Maren | Meden Maren | **Méden Maren** | Canon officiel Bethesda / Modpocalypse Vanilla : Méden Maren |
| `04039D16\|Dragonborn.esm`<br>*NPC_ SHRT* | Meden | Meden | **Méden** | Canon officiel Bethesda / Modpocalypse Vanilla : Méden |
| `04039D18\|Dragonborn.esm`<br>*NPC_ FULL* | Tolenos Omoren | Tolenos Omoren | **Tolénos Omoren** | Canon officiel Bethesda / Modpocalypse Vanilla : Tolénos Omoren |
| `04039D18\|Dragonborn.esm`<br>*NPC_ SHRT* | Tolenos | Tolenos | **Tolénos** | Canon officiel Bethesda / Modpocalypse Vanilla : Tolénos |

---

## 📁 `DIbella's Blessing - RSV Exclusion Patch.esp.json`
*Nombre d'ajustements unitaires vérifiés :* **9**

| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |
| :--- | :--- | :--- | :--- | :--- |
| `000BFB55\|Skyrim.esm`<br>*NPC_ FULL* | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | Canon officiel Bethesda / USSEP / Nolvus : Gardienne Carcette |
| `0001365F\|Skyrim.esm`<br>*NPC_ FULL* | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | Canon officiel Bethesda / USSEP : Dravynea la Tisseuse de pierre |
| `0001365F\|Skyrim.esm`<br>*NPC_ SHRT* | Dravynea | Dravynéa | **Dravynea** | Canon officiel Bethesda / USSEP : Dravynea |
| `000877AF\|Skyrim.esm`<br>*NPC_ FULL* | Edith | Édith | **Edith** | Canon officiel Bethesda / USSEP : Edith (sans accent) |
| `0001C196\|Skyrim.esm`<br>*NPC_ FULL* | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Canon officiel Bethesda / USSEP : Brelyna Maryon (sans accent) |
| `0001C196\|Skyrim.esm`<br>*NPC_ SHRT* | Brelyna | Brélyna | **Brelyna** | Canon officiel Bethesda / USSEP : Brelyna (sans accent) |
| `00014123\|Skyrim.esm`<br>*NPC_ FULL* | Niranye | Niranyë | **Niranye** | Canon officiel Bethesda / USSEP : Niranye (sans tréma) |
| `000274A0\|Skyrim.esm`<br>*NPC_ FULL* | Laelette the Vampire | Laelette | **Laelette la vampire** | Canon officiel Bethesda / Fanatical Enemies : Laelette la vampire |
| `000D74F8\|Skyrim.esm`<br>*NPC_ SHRT* | Farmer | Fermier | **Fermière** | Accord en genre pour PNJ féminin : Fermière (canon Modpocalypse) |

---

## 📁 `fanatical enemies - modpocalypse patch.esp.json`
*Nombre d'ajustements unitaires vérifiés :* **1**

| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |
| :--- | :--- | :--- | :--- | :--- |
| `00016FF8\|Skyrim.esm`<br>*NPC_ FULL* | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Canon officiel Bethesda / USSEP / Nolvus Phase 2A : Valkynaz drémora |

---

## 📁 `NITHI NPCs - Whiterun - Complete - AI Overhaul.esp.json`
*Nombre d'ajustements unitaires vérifiés :* **2**

| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |
| :--- | :--- | :--- | :--- | :--- |
| `0002C925\|Skyrim.esm`<br>*NPC_ FULL* | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Canon officiel Bethesda / USSEP : Sévério Pélagia |
| `00065657\|Skyrim.esm`<br>*NPC_ SHRT* | Erik | Erik | **Érik** | Canon officiel Bethesda / USSEP : Érik (accent aigu) |

---

## 📁 `TSOS_AI_Overall_Patch.esp.json`
*Nombre d'ajustements unitaires vérifiés :* **1**

| FormID / Type | Texte Source (Original EN) | Avant (Ancienne valeur observée) | Après (Traduction canonique validée) | Justification & Canon |
| :--- | :--- | :--- | :--- | :--- |
| `00013380\|Skyrim.esm`<br>*NPC_ FULL* | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | Canon officiel Bethesda / USSEP : Vekel l'homme (minuscule) |

---
