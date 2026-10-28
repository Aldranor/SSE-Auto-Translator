# Récapitulatif des Modifications — Phase 5 : Refontes de PNJs & Enfants

> **Date :** 28 Octobre 2026  
> **Statut :** ✅ Validé & Vérifié sur disque  
> **Total modifications unitaires :** 105 entrées  
> **Protocole de sécurité :** Ciblage unitaire strict `(form_id, type, index, original)` avec assertion `count == 1` et relecture physique post-écriture.  

## 1. Vue d'ensemble par mod / fichier

| Fichier | Nombre de corrections | Objectif principal |
| :--- | :---: | :--- |
| `Modpocalypse NPCs - All Vanilla NPCs - French/Modpocalypse NPCs (v3) SSE.esp.json` | **28** | Restauration des noms officiels vanilla Bethesda/USSEP (accents, titres, vigile, ordre de mots Drémora) |
| `Modpocalypse NPCs - All Vanilla NPCs/modpocalypse npcs (v3) sse.esp.json` | **9** | Restauration des noms officiels vanilla Bethesda/USSEP (accents, titres, vigile, ordre de mots Drémora) |
| `Modpocalypse NPCs - Added Quests Fixes - French/modpocalypse npcs - added quest fixes.esp.json` | **2** | Restauration des noms officiels vanilla Bethesda/USSEP (accents, titres, vigile, ordre de mots Drémora) |
| `True Sons of Skyrim Refined - French/tsosrefined.esp.json` | **30** | Harmonisation typographique 'Soldat Sombrage' (majuscule canonique), 'Bolgeir' et 'Vekel l'homme' |
| `True Sons of Skyrim Refined - Nolvus Patch - French/nolvus awakening tsos patch.esp.json` | **27** | Harmonisation typographique 'Soldat Sombrage' (majuscule canonique), 'Bolgeir' et 'Vekel l'homme' |
| `True Sons of Skyrim Refined - French/TSOS_AI_Overall_Patch.esp.json` | **1** | Harmonisation typographique 'Soldat Sombrage' (majuscule canonique), 'Bolgeir' et 'Vekel l'homme' |
| `Pride of Skyrim All In One - Merged - French/Pride of Skyrim - All In One.esp.json` | **8** | Restauration des accents et noms officiels (Érik, Léontius, Sévério, Capitaine Nautonier, Bolgeir) |

---

## 2. Tableau Exhaustif des Modifications Effectives

| Fichier | FormID | Type | Index | Source (EN) | Ancienne valeur | Valeur validée | Justification Lore / Canon |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- | :--- |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00013264|Skyrim.esm` | `NPC_ FULL` | — | Bolgeir Bearclaw | Ser bolgeir bearclaw | **Bolgeir Griffedours** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | — | Bearclaw | Ourson | **Bolgeir** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00013281|Skyrim.esm` | `NPC_ FULL` | — | Giraud Gemane | Giraud Gemane | **Giraud Germane** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001365F|Skyrim.esm` | `NPC_ FULL` | — | Dravynea the Stoneweaver | Dravynéa la Tisseuse-de-Pierre | **Dravynea la Tisseuse de pierre** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001365F|Skyrim.esm` | `NPC_ SHRT` | — | Dravynea | Dravynéa | **Dravynea** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001366B|Skyrim.esm` | `NPC_ FULL` | — | Sondas Drenim | Sondas Drénim | **Sondas Drenim** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00013B76|Skyrim.esm` | `NPC_ FULL` | — | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00013B76|Skyrim.esm` | `NPC_ SHRT` | — | Leontius | Leontius | **Léontius** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00014123|Skyrim.esm` | `NPC_ FULL` | — | Niranye | Niranyë | **Niranye** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001413A|Skyrim.esm` | `NPC_ FULL` | — | Revyn Sadri | Révyn Sadri | **Revyn Sadri** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001413A|Skyrim.esm` | `NPC_ SHRT` | — | Revyn | Révyn | **Revyn** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001413D|Skyrim.esm` | `NPC_ FULL` | — | Ravam Verethi | Ravam Véréthi | **Ravam Verethi** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `00016FFA|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001C196|Skyrim.esm` | `NPC_ FULL` | — | Brelyna Maryon | Brélyna Maryon | **Brelyna Maryon** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0001C196|Skyrim.esm` | `NPC_ SHRT` | — | Brelyna | Brélyna | **Brelyna** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | — | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000877AF|Skyrim.esm` | `NPC_ FULL` | — | Edith | Édith | **Edith** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000BFB55|Skyrim.esm` | `NPC_ FULL` | — | Keeper Carcette | Carcette la Gardienne | **Gardienne Carcette** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000CD63E|Skyrim.esm` | `NPC_ FULL` | — | Dragon Cultist | Adepte du Dragon | **Adepte du dragon** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000D3E79|Skyrim.esm` | `NPC_ FULL` | — | Acolyte Jenssen | Acolyte Jenssen | **Jenssen l'acolyte** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000D55D3|Skyrim.esm` | `NPC_ FULL` | — | Bandit | Bandit | **Vigile** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `000E3EAD|Skyrim.esm` | `NPC_ FULL` | — | Leifnarr | Leifnarr | **Nordique** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `02003364|Dawnguard.esm` | `NPC_ FULL` | — | Garan Marethi | Garan Maréthi | **Garan Marethi** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `02003366|Dawnguard.esm` | `NPC_ FULL` | — | Feran Sadri | Féran Sadri | **Feran Sadri** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0201223E|Dawnguard.esm` | `NPC_ FULL` | — | Vampire | Vampire sanguinaire | **Vampire** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `0401777C|Dragonborn.esm` | `NPC_ FULL` | — | Varona Nelas | Varona Nélas | **Varona Nelas** | Harmonisation USSEP / Lore officiel |
| `Modpocalypse NPCs (v3) SSE.esp.json` | `04018278|Dragonborn.esm` | `NPC_ FULL` | — | Crescius Caerellius | Crescius Caerellius | **Crescius Cérellius** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `000F778F|Skyrim.esm` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `000D55D3|Skyrim.esm` | `NPC_ FULL` | — | Bandit | Bandit Gardeporte | **Vigile** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `000BFB55|Skyrim.esm` | `NPC_ FULL` | — | Keeper Carcette | Carcette la gardienne | **Gardienne Carcette** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FFA|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | — | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `00013B76|Skyrim.esm` | `NPC_ SHRT` | — | Leontius | Leontius | **Léontius** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs (v3) sse.esp.json` | `00013B76|Skyrim.esm` | `NPC_ FULL` | — | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs - added quest fixes.esp.json` | `00016FF9|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `modpocalypse npcs - added quest fixes.esp.json` | `00016FF8|Skyrim.esm` | `NPC_ FULL` | — | Dremora Valkynaz | Drémora Valkynaz | **Valkynaz drémora** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C06|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2A|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C07|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C4E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C0F|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C17|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C11|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `00013380|Skyrim.esm` | `NPC_ FULL` | — | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C18|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C05|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2D|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C53|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C5B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C10|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C0E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C0A|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2C|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `00095C44|Skyrim.esm` | `CELL FULL` | — | Hall of Valor | Panthéon des Braves | **Panthéon des braves** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C5D|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C1B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000B2F|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C41|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `00065657|Skyrim.esm` | `NPC_ SHRT` | — | Erik | Erik | **Érik** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C0B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | — | Bearclaw | Griffedours | **Bolgeir** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C29|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C15|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `tsosrefined.esp.json` | `02000C48|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2C|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C29|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2D|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | — | Bearclaw | Griffedours | **Bolgeir** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C5D|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C17|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C07|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C18|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C0A|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C41|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C0E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C06|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C4E|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C53|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C48|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C05|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C1B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C10|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C0B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C0F|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C5B|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2F|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000B2A|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C15|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `nolvus awakening tsos patch.esp.json` | `08000C11|TSOSRefined.esp` | `NPC_ FULL` | — | Stormcloak Soldier | Soldat sombrage | **Soldat Sombrage** | Harmonisation USSEP / Lore officiel |
| `TSOS_AI_Overall_Patch.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | — | Bearclaw | Griffedours | **Bolgeir** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00013264|Skyrim.esm` | `NPC_ SHRT` | — | Bearclaw | Griffedours | **Bolgeir** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00013296|Skyrim.esm` | `NPC_ SHRT` | — | Wayfinder | Navigateur | **Nautonier** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00013380|Skyrim.esm` | `NPC_ FULL` | — | Vekel the Man | Vekel l'Homme | **Vekel l'homme** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00013B76|Skyrim.esm` | `NPC_ FULL` | — | Leontius Salvius | Leontius Salvius | **Léontius Salvius** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00013B76|Skyrim.esm` | `NPC_ SHRT` | — | Leontius | Leontius | **Léontius** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `0002C925|Skyrim.esm` | `NPC_ FULL` | — | Severio Pelagia | Severio Pelagia | **Sévério Pélagia** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `000350A7|Skyrim.esm` | `NPC_ FULL` | — | Erik | Erik | **Érik** | Harmonisation USSEP / Lore officiel |
| `Pride of Skyrim - All In One.esp.json` | `00065657|Skyrim.esm` | `NPC_ SHRT` | — | Erik | Erik | **Érik** | Harmonisation USSEP / Lore officiel |
