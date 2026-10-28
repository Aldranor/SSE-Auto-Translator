import json
import os
import re

ROOT = os.path.join("data", "user", "database", "french")

# ---------------------------------------------------------------------------
# 1. Explicit translation overrides for Empty Strings (phase1_empty_strings.json)
#    Any empty string NOT in EMPTY_SPECIFIC_OVERRIDES, NOLVUS_ENEMY_TRANSLATE,
#    INTERNAL_EMPTY_FILES, or INTERNAL_EMPTY_ORIGS will default to restoring
#    `string = original` with `status = "TranslationComplete"` (proper nouns).
# ---------------------------------------------------------------------------

# Key: (rel_path, form_id, rec_type, index, original) -> (new_string, new_status)
EMPTY_SPECIFIC_OVERRIDES = {
    # (FR) Palace of the Kings
    (r"(FR) Palace of the Kings\jk's palace of the kings.esp.json", "010C5EE9", "ARMO FULL", None, "Manakin"):
        ("Mannequin", "TranslationComplete"),
    # Abyss - Sorts obscurs
    (r"Abyss - Sorts obscurs\Abyss.esp.json", "04000857|dareniiis.esp", "PERK FULL", None, "Aspection"):
        ("Maîtrise des aspects", "TranslationComplete"),
    (r"Abyss - Sorts obscurs\Abyss.esp.json", "04000857|dareniiis.esp", "PERK DESC", None, "Aspection"):
        ("Maîtrise des aspects", "TranslationComplete"),
    (r"Abyss - Sorts obscurs\Abyss.esp.json", "01EA6007|Abyss.esp", "SPEL FULL", None, "Aspection"):
        ("Maîtrise des aspects", "TranslationComplete"),
    # Atlas - Marqueurs de carte (MCM)
    (r"Atlas - Marqueurs de carte\interface\translations\atlas map markers_french.txt.json", None, None, None,
     "-- Active Imperial and Stormcloak Camps --\\nUp to 16 markers (there are 16 camps, but only the active ones will be visible)"):
        ("-- Camps impériaux et sombrages actifs --\\nJusqu'à 16 marqueurs (il existe 16 camps, mais seuls ceux qui sont actifs seront affichés)", "TranslationComplete"),
    # Commerce & Troc (MCM + ESP)
    (r"Commerce & Troc\interface\translations\trade & barter_french.txt.json", None, None, None, ":\tBuying prices:"):
        (":\tPrix d'achat :", "TranslationComplete"),
    (r"Commerce & Troc\interface\translations\trade & barter_french.txt.json", None, None, None, ":\tSelling prices:"):
        (":\tPrix de vente :", "TranslationComplete"),
    (r"Commerce & Troc\interface\translations\trade & barter_french.txt.json", None, None, None, "fBarterMax"):
        ("fBarterMax", "NoTranslationRequired"),
    (r"Commerce & Troc\interface\translations\trade & barter_french.txt.json", None, None, None, "fBarterMin"):
        ("fBarterMin", "NoTranslationRequired"),
    (r"Commerce & Troc\trade & barter.esp.json", "0000DDF8|trade & barter.esp", "QUST FULL", None, "Individualized Merchant Inventories"):
        ("Inventaires de marchands individualisés", "TranslationComplete"),
    # Granite Hill Village
    (r"Granite Hill Village - French\Granite Hill.esp.json", "000CA6AC|Granite Hill.esp", "ENCH FULL", None, "Foecrusher"):
        ("Broyeur d'ennemis", "TranslationComplete"),
    (r"Granite Hill Village - French\Granite Hill.esp.json", "000B0FD5|Granite Hill.esp", "ENCH FULL", None, "Pursuer"):
        ("Poursuivant", "TranslationComplete"),
    # LOTD - Patches officiels
    (r"LOTD - Patches officiels\DBM_ISC_Patch.esp.json", "0655B273|Immersive Sounds - Compendium.esp", "MISC FULL", None, "Coral"):
        ("Corail", "TranslationComplete"),
    (r"LOTD - Patches officiels\DBM_ISC_Patch.esp.json", "0655B274|Immersive Sounds - Compendium.esp", "MISC FULL", None, "Ivory"):
        ("Ivoire", "TranslationComplete"),
    # La Sorcière et le Labyrinthe
    (r"La Sorcière et le Labyrinthe\ksws03_quest.esp.json", "0226BB5F|ksws03_quest.esp", "MESG FULL", None, "The Witch's Hut can't travel there."):
        ("La cabane de la sorcière ne peut pas voyager jusqu'ici.", "TranslationComplete"),
    (r"La Sorcière et le Labyrinthe\ksws03_quest.esp.json", "020BD64C|ksws03_quest.esp", "RACE FULL", None, "Angel Race"):
        ("Race d'ange", "TranslationComplete"),
    # Ode à la Nature - Compagne Auri
    (r"Ode à la Nature - Compagne Auri\018AuriVIGILANTpatch.esp.json", "03005900|018AuriVIGILANTpatch.esp", "QUST FULL", None, "Auri Vigilant commentary"):
        ("Commentaires d'Auri - Vigilant", "TranslationComplete"),
    # Saleté et sang
    (r"Saleté et sang - Effets visuels dynamiques\Dirt and Blood - Dynamic Visuals.esp.json", "0000DA0D|Dirt and Blood - Dynamic Visuals.esp", "MESG FULL", None, "Longer Hair"):
        ("Cheveux plus longs", "TranslationComplete"),
    # amatteroftime
    (r"amatteroftime_english.txt - French\interface\translations\amatteroftime_english.txt.json", None, None, None, "Compass"):
        ("Boussole", "TranslationComplete"),
}

NOLVUS_ENEMY_TRANSLATE = {
    "Dark Raven": "Corbeau noir",
    "Fire Aspfang": "Crovenin de feu",
    "Frost Aspfang": "Crovenin de glace",
    "Ruddy Aspfang": "Crovenin vermeil",
    "Ustase Aventurier": "Aventurier d'Ustase",
    "Ustase Hounder": "Maître-chien d'Ustase",
    "Ustase Ravenor": "Pillard d'Ustase",
}

INTERNAL_EMPTY_FILES = {
    r"Divine Smite   French\Divine Smite.esp.json",
    r"Eldritch Blast   French\Eldritch Blast.esp.json",
    r"Adamant - Refonte des atouts\Adamant - Animated Armory Bound Weapons.esp.json",
    r"Apocalypse - Magie de Bordeciel\Apocalypse - Magic of Skyrim.esp.json",
    r"Armors of the Velothi Pt. II - My patches (French)\Armors of the Velothi Pt2.esl.json",
    r"Armure de markynaz\1Markynaz.esl.json",
    r"Armures drémoras\mihaildremorasets.esp.json",
    r"Au-delà de Bordeciel - Bruma\BSHeartland.esm.json",
    r"La fin de l'innocence - Extension de la quête\Innocence Lost - Quest Expansion.esp.json",
    r"Statistiques des compagnons\Follower Stats.esp.json",
    r"Vigilant - English Addon Subtitle Patch\vigilant subtitle fix.esp.json",
}

INTERNAL_EMPTY_ORIGS = {
    "Shadow Atronach FX",
    "Shadow Eruption Tooltip",
    "Shadow Atronach abilities",
    "Shadow Wolf abilities",
    "Atlas Maps MCM Startup Quest",
    "DLC Script Patcher on mod load",
    "WTDialogueIdleSharedInfo",
    "WTDialogueIdleStealLinesNotCrime",
    "WTRandomEnc44Goodbyes",
    "WTRandomEnc44Hellos",
    "Walking Sound",
    "Witch's House Walking Sounds 1",
    "Witch's House Walking Sounds 2",
    "Blood1", "Blood2", "Blood3", "Blood4", "Blood5",
    "Raining Effect", "Swimming Effect1", "Quest Grooming",
    "Dirt and Blood Effects", "Dirt for NPCs", "Recently Washed Effects",
    "Soap FX", "Swimming1", "Washing",
}

# ---------------------------------------------------------------------------
# 2. Surgical Fixes for Variables, Tags, Fonts, Images, Pagebreaks & HTML
# ---------------------------------------------------------------------------
SURGICAL_UNIT_FIXES = [
    # --- A. Spliced / Corrupted Numeric Tags ---
    {
        "file": r"Conduit - Canalisation de sort\Conduit.esp.json",
        "form_id": "01074FB8|Conduit.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Weapon strikes add <1 Crack>. This can occur once every <3>s. The attack that creates the <3rd Crack> causes <mag> frost damage and ends <Conduit>.",
        "new_string": "Les coups ajoutent <1 craquelure>, une fois toutes les <3> secondes maximum. L'attaque qui crée la <3e craquelure> inflige <mag> points de dégâts de glace et met fin à <Conduit>.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Magie de destruction élémentale II\Elemental Destruction Magic Redux.esp.json",
        "form_id": "03000853|Elemental Destruction Magic Redux.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "For <20> seconds, targets take <mag> points of earth damage per second, have Health regeneration stopped for <5> seconds, and are periodically staggered.",
        "new_string": "Pendant <20> secondes, les cibles subissent <mag> points de dégâts de terre par seconde, voient leur régénération de santé arrêtée pendant <5> secondes et sont périodiquement déstabilisées.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Ordonnateur - Atouts de Bordeciel\Ordinator - Perks of Skyrim.esp.json",
        "form_id": "030AC6E9|Ordinator - Perks of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "For the bearer of Warrior's Flame: (<Enemy>) Deals <750> damage. (<Ally>) Grants <1000>% attack damage for <5> seconds. (<You>) Grants full Health, Magicka and Stamina.",
        "new_string": "Pour le porteur de la Flamme du guerrier : (<Ennemi>) Inflige <750> points de dégâts. (<Allié>) Accorde <1000> % de dégâts d'attaque supplémentaires pendant <5> secondes. (<Joueur>) Restaure la totalité de votre santé, magie et vigueur.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Sacrosanct - Vampires de Bordeciel\Sacrosanct - Vampires of Skyrim.esp.json",
        "form_id": "03014558|Sacrosanct - Vampires of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Sneak feeding or feeding on a Seduced victim freezes them for <8> seconds, reducing armor by <1500> points.",
        "new_string": "Se nourrir en furtivité ou sur une victime séduite la laisse immobile pendant <8> secondes, réduisant sa valeur d'armure de <1500> points.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json",
        "form_id": "040225F1|SPERG-SSE.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Destruction spells deal <45>% more damage. Dual casting increases this to <100>% for  5 seconds, but ends the effect.",
        "new_string": "Les sorts de destruction infligent <45> % de dégâts supplémentaires. Le double lancement augmente les dégâts de <100> % pendant 5 secondes, mais met fin à l'effet.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json",
        "form_id": "040425E2|SPERG-SSE.esp",
        "type": "ARMO DESC",
        "index": None,
        "original": "Immune to disease and poison.",
        "new_string": "Confère une immunité aux maladies et aux poisons.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json",
        "form_id": "040425E3|SPERG-SSE.esp",
        "type": "ARMO DESC",
        "index": None,
        "original": "Immune to disease and poison.",
        "new_string": "Confère une immunité aux maladies et aux poisons.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Les Outils de Kagrénac\Tools of Kagrenac.esp.json",
        "form_id": "044D5A22|Tools of Kagrenac.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Summons a Dwarven Centurion for <dur> seconds wherever the caster is pointing.",
        "new_string": "Fait apparaître un centurion dwemer pendant <dur> secondes à l'endroit indiqué par le lanceur.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Les Outils de Kagrénac\Tools of Kagrenac.esp.json",
        "form_id": "042F405B|Tools of Kagrenac.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Summons a Dwarven Centurion for <dur> seconds wherever the caster is pointing.",
        "new_string": "Fait apparaître un centurion dwemer pendant <dur> secondes à l'endroit indiqué par le lanceur.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },
    {
        "file": r"Les Outils de Kagrénac\Tools of Kagrenac.esp.json",
        "form_id": "042F405C|Tools of Kagrenac.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Summons a Dwarven Centurion for <dur> seconds wherever the caster is pointing.",
        "new_string": "Fait apparaître un centurion dwemer pendant <dur> secondes à l'endroit indiqué par le lanceur.",
        "category": "A_SPLICED_NUMERIC_TAG"
    },

    # --- B. Corrupted <Global=...> Names ---
    {
        "file": r"Grognement - Lycanthropes de Bordeciel\Growl - Werebeasts of Skyrim.esp.json",
        "form_id": "0404C7A9|Growl - Werebeasts of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "At night, <Global=HRI_Mortal_Global_CallOfTheBlood_ChanceCurrent>% (based on the phases of the moon) chance that your curse manifests, forcing you to take the form of the beast.",
        "new_string": "De nuit, <Global=HRI_Mortal_Global_CallOfTheBlood_ChanceCurrent> % de chances (en fonction des phases des lunes) que votre malédiction se manifeste, vous obligeant à revêtir la forme de la bête.",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Growl.esp.json",
        "form_id": "0304C7A9|Growl - Werebeasts of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "At night, <Global=HRI_Mortal_Global_CallOfTheBlood_ChanceCurrent>% (based on the phases of the moon) chance that the curse manifests, forcing the caster to take the form of the beast.",
        "new_string": "De nuit, <Global=HRI_Mortal_Global_CallOfTheBlood_ChanceCurrent> % de chances (en fonction des phases des lunes) que la malédiction se manifeste, obligeant à revêtir la forme de la bête.",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "041308F3|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Daylight energizes a divine healing glow, which activates in darkness and indoors. (Energy: <Global=WSN_Effect_Global_LightOfAurielCharge>%)",
        "new_string": "La lumière du jour alimente une lueur de guérison divine, qui s'active dans l'obscurité et à l'intérieur. (Énergie : <Global=WSN_Effect_Global_LightOfAurielCharge> %)",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "0426FD3B|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "During prayer, you may spend <5>% favor to gain <Global=WSN_Favor_Global_Fractional>% melee damage (based on favor with Leki) for <10> minutes or <5> battles. Costs <5>% favor.",
        "new_string": "Prier vous permet de dépenser <5> % de faveur pour gagner <Global=WSN_Favor_Global_Fractional> % de dégâts de mêlée (selon la faveur de Leki) pendant <10> minutes ou <5> combats. Coûte <5> % de faveur.",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "040DF642|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Attacks deal <Global=WSN_Favor_Global_Fractional3>% more damage and critical damage to humans (based on favor with Trinimac).",
        "new_string": "Les attaques infligent <Global=WSN_Favor_Global_Fractional3> % de dégâts et de dégâts critiques en plus aux humains (basé sur la faveur de Trinimac).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "0400F93B|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Spells cost <Global=WSN_Favor_Global_Fractional>% less to cast (based on favor with Julianos).",
        "new_string": "Lancer des sorts coûte <Global=WSN_Favor_Global_Fractional> % de magie en moins (basé sur la faveur de Julianos).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "04284166|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Yokudan deities reduce attack damage taken by <Global=WSN_Favor_Global_Fractional>% (based on favor with the deity).",
        "new_string": "Les déités yokudanes réduisent les dégâts d'attaque subis de <Global=WSN_Favor_Global_Fractional> % (basé sur la faveur de la déité).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "04060AE5|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Attacks, spells, scrolls, shouts and enchantments are <Global=WSN_Favor_Global_Fractional3>% better against undead (based on favor with Meridia).",
        "new_string": "Les attaques, sorts, parchemins, Cris et enchantements sont <Global=WSN_Favor_Global_Fractional3> % plus efficaces contre les morts-vivants (basé sur la faveur de Méridia).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json",
        "form_id": "0404C690|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Your attacks deal <Global=WSN_Favor_Global_Fractional3>% more damage when fighting only one opponent (based on favor with Boethiah).",
        "new_string": "Vos attaques infligent <Global=WSN_Favor_Global_Fractional3> % de dégâts supplémentaires quand vous ne combattez qu'un seul adversaire (basé sur la faveur de Boéthia).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Wintersun.esp.json",
        "form_id": "03302DC1|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Pray to receive a Divine blessing of choice. Divine blessings are <Global=WSN_Favor_Global>% better (based on favor with St. Alessia).",
        "new_string": "Méditer pour obtenir la bénédiction divine choisie. Les bénédictions divines sont <Global=WSN_Favor_Global> % plus efficaces (basé sur la faveur de sainte Alessia).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Wintersun.esp.json",
        "form_id": "0304C690|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Attacks deal <Global=WSN_Favor_Global_Fractional3>% more damage when fighting only one opponent (based on favor with Boethiah).",
        "new_string": "Les attaques infligent <Global=WSN_Favor_Global_Fractional3> % de dégâts supplémentaires contre un seul adversaire (basé sur la faveur de Boéthia).",
        "category": "B_GLOBAL_VAR_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Wintersun.esp.json",
        "form_id": "0326FD3B|Wintersun - Faiths of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "When praying, the caster may spend <5>% favor to gain <Global=WSN_Favor_Global_Fractional>% melee damage (based on favor with Leki) for <10> minutes or <5> battles. Costs <5>% favor.",
        "new_string": "En méditation, le lanceur peut dépenser <5> % de faveur pour gagner <Global=WSN_Favor_Global_Fractional> % de dégâts de mêlée (selon la faveur de Leki) pendant <10> minutes ou <5> batailles. Coûte <5> % de faveur.",
        "category": "B_GLOBAL_VAR_FIX"
    },

    # --- C. Corrupted <Alias=...> Syntax & Names ---
    {
        "file": r"Armure d'onyx\ksws02.esp.json",
        "form_id": "03000828|ksws02.esp",
        "type": "QUST NNAM",
        "index": 400,
        "original": "Recover <alias=KeyBandit> from <alias=KeyLocationBandit>",
        "new_string": "Récupérez la clé d'onyx de cet endroit : <alias=KeyLocationBandit>",
        "category": "C_ALIAS_VAR_FIX"
    },
    {
        "file": r"Au-delà de Bordeciel - Bruma\BSHeartland.esm.json",
        "form_id": "02064EE7|BSHeartland.esm",
        "type": "DIAL FULL",
        "index": None,
        "original": "What trouble are you in?",
        "new_string": "Quel genre d'ennuis avez-vous ?",
        "category": "C_ALIAS_VAR_FIX"
    },
    {
        "file": r"Petites annonces\Missives.esp.json",
        "form_id": "020331A7|Missives.esp",
        "type": "BOOK FULL",
        "index": None,
        "original": "Missive: Hunt Vampire in <Alias=Hold>",
        "new_string": "Annonce - Recherche vampire (<Alias=Hold>)",
        "category": "C_ALIAS_VAR_FIX"
    },
    {
        "file": r"Petites annonces\Missives.esp.json",
        "form_id": "020331A9|Missives.esp",
        "type": "BOOK FULL",
        "index": None,
        "original": "Missive: Slay Werewolves at <Alias=Den>",
        "new_string": "Annonce - Un loup-garou à tuer (<Alias=Den>)",
        "category": "C_ALIAS_VAR_FIX"
    },
    {
        "file": r"Petites annonces\Missives - Wyrmstooth.esp.json",
        "form_id": "0400081D|Missives - Wyrmstooth.esp",
        "type": "BOOK FULL",
        "index": None,
        "original": "Missive: Slay Werewolves at <Alias=Den>",
        "new_string": "Annonce - Un loup-garou à tuer (<Alias=Den>)",
        "category": "C_ALIAS_VAR_FIX"
    },

    # --- D. Missing/Extra <mag> and <dur> Variables ---
    {
        "file": r"Abyss - Sorts obscurs\Abyss.esp.json",
        "form_id": "04000B00|Abyss.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Deals <mag> damage for <dur> seconds.",
        "new_string": "Inflige <mag> points de dégâts par seconde pendant <dur> secondes.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"Dovahkiin - Arbre de compétence du Thu'um\DragonbornShoutPerks.esp.json",
        "form_id": "04060B3F|DragonbornShoutPerks.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "You take <mag>% less damage for <dur> seconds.",
        "new_string": "Vous subissez <mag> % de dégâts en moins pendant <dur> secondes.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"Enfant du Tonnerre - Immersion et Cris épiques\Thunderchild - Epic Shout Package.esp.json",
        "form_id": "041535B3|Thunderchild - Epic Shout Package.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Restores <mag> points of Health to the living for <dur> seconds.",
        "new_string": "Rend <mag> points de santé par seconde aux êtres vivants pendant <dur> secondes.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"Enfant du Tonnerre - Immersion et Cris épiques\Thunderchild - Epic Shout Package.esp.json",
        "form_id": "041535B5|Thunderchild - Epic Shout Package.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Restores <mag> points of Health to the living for <dur> seconds.",
        "new_string": "Rend <mag> points de santé par seconde aux êtres vivants pendant <dur> secondes.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"Falskaar\Falskaar.esm.json",
        "form_id": "0111E108|Falskaar.esm",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Decreases Restoration spell effectiveness on targets by <mag>% for <dur> seconds.",
        "new_string": "Réduit l'efficacité des sorts de guérison sur les cibles de <mag> % pendant <dur> secondes.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"Nolvus Awakening Creatures Patch - French\Nolvus Awakening Creatures Patch.esp.json",
        "form_id": "11000837|mihailgrummite.esp",
        "type": "MGEF FULL",
        "index": None,
        "original": "Conjure Manic Grummite Swampbeater",
        "new_string": "Invocation de grummite maniaque briseur des marais",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json",
        "form_id": "0405D194|SPERG-SSE.esp",
        "type": "SPEL DESC",
        "index": None,
        "original": "Raises all dead around you to fight for you.",
        "new_string": "Tous les morts autour de vous s'animent et combattent à vos côtés.",
        "category": "D_MAG_DUR_FIX"
    },
    {
        "file": r"SPERG - Atouts et jouabilité améliorés\SPERG-SSE.esp.json",
        "form_id": "0402FE9A|SPERG-SSE.esp",
        "type": "SPEL DESC",
        "index": None,
        "original": "Raises all dead around you to fight for you.",
        "new_string": "Tous les morts autour de vous s'animent et combattent à vos côtés.",
        "category": "D_MAG_DUR_FIX"
    },

    # --- E. Broken printf Format Specifiers & Illegal <num> Brackets ---
    {
        "file": r"Immersive Spell Learning - DESTified\dest_isl.esp.json",
        "form_id": "01000B43|DEST_ISL.esp",
        "type": "MESG DESC",
        "index": None,
        "original": "I have already spent %.0f hour(s) studying this tome. With my current knowledge, it will take me approximately %.0f more hour(s) to learn this spell.\r\nHow long should I study?",
        "new_string": "J'ai déjà passé %.0f heure(s) à étudier ce tome. Avec mes connaissances actuelles, il me faudra environ %.0f heure(s) supplémentaire(s) pour apprendre ce sort.\r\nCombien de temps dois-je étudier ?",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"Immersive Spell Learning - DESTified\dest_isl.esp.json",
        "form_id": "01000801|DEST_ISL.esp",
        "type": "MESG DESC",
        "index": None,
        "original": "You have not studied this tome before. With your current knowledge, it will take you approximately %.0f hour(s) to learn this spell.\r\nHow long do you wish to study?",
        "new_string": "Vous n'avez jamais étudié ce tome auparavant. Avec vos connaissances actuelles, il vous faudra environ %.0f heure(s) pour apprendre ce sort.\r\nCombien de temps souhaitez-vous étudier ?",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"Immersive Spell Learning - DESTified\dest_isl.esp.json",
        "form_id": "01000802|DEST_ISL.esp",
        "type": "MESG DESC",
        "index": None,
        "original": "You have already spent %.0f hour(s) studying this tome. With your current knowledge, it will take you approximately %.0f more hour(s) to learn this spell.\r\nHow long do you wish to study?",
        "new_string": "Vous avez déjà passé %.0f heure(s) à étudier ce tome. Compte tenu de vos connaissances actuelles, il vous faudra environ %.0f heure(s) supplémentaire(s) pour apprendre ce sort.\r\nCombien de temps souhaitez-vous étudier ?",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Wintersun.esp.json",
        "form_id": "0302DFF0|Wintersun - Faiths of Skyrim.esp",
        "type": "MESG DESC",
        "index": None,
        "original": "%.0f animals have heeded my call.",
        "new_string": "%.0f animaux répondent à mon appel.",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"Apocalypse - Magie de Bordeciel\Apocalypse - Magic of Skyrim.esp.json",
        "form_id": "030B9E28|Apocalypse - Magic of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Strengthen your resolve for <dur> seconds, gaining <mag>% extra attack damage for each nearby undead when cast.",
        "new_string": "Renforce la détermination pendant <dur> secondes, gagnant <mag> % de dégâts d'attaque supplémentaires pour chaque mort-vivant proche quand lancé.",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"YOT - Vos propres pensées\YOT - Apocalypse.esp.json",
        "form_id": "020B9E28|Apocalypse - Magic of Skyrim.esp",
        "type": "MGEF DNAM",
        "index": None,
        "original": "Strengthens the caster's resolve for <dur> seconds, gaining <mag>% extra attack damage for each nearby undead when cast.",
        "new_string": "Renforce la détermination pendant <dur> secondes, gagnant <mag> % de dégâts d'attaque supplémentaires pour chaque mort-vivant proche quand lancé.",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"3DNPC - PNJs intéressants\3DNPC.esp.json",
        "form_id": "051564A9|3DNPC.esp",
        "type": "SPEL DESC",
        "index": None,
        "original": "Increases Fortify One-Handed Effects by 75%",
        "new_string": "Augmente les capacités de combat à une main de 75 %.",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
    {
        "file": r"Apothicaire - Refonte de l'alchimie\Apothecary.esp.json",
        "form_id": "0010F84C|Skyrim.esm",
        "type": "MGEF DNAM",
        "index": None,
        "original": "You create one additional potion or poison from the same number of ingredients.",
        "new_string": "Vous créez une potion ou un poison supplémentaire à partir du même nombre d'ingrédients.",
        "category": "E_PRINTF_NUMERIC_FIX"
    },
]


def main():
    with open("phase1_empty_strings.json", encoding="utf-8") as f:
        empty_items = json.load(f)

    file_ops = {}

    # 1. Queue all 436 Empty String fixes
    for item in empty_items:
        rel_path = item["file"]
        fid = item["form_id"]
        rtype = item["type"]
        idx = item["index"]
        orig = item["original"]

        key = (rel_path, fid, rtype, idx, orig)
        mcm_key = (rel_path, None, None, None, orig)

        if key in EMPTY_SPECIFIC_OVERRIDES:
            new_str, new_status = EMPTY_SPECIFIC_OVERRIDES[key]
        elif mcm_key in EMPTY_SPECIFIC_OVERRIDES:
            new_str, new_status = EMPTY_SPECIFIC_OVERRIDES[mcm_key]
        elif rel_path == r"Quests Award Perk Points\quests award perk points.esp.json" and orig == "Quests Award Perk Points":
            new_str, new_status = "Points d'atout en récompense de quête", "TranslationComplete"
        elif rel_path.endswith("nolvus awakening combat scaling overhaul - enemy level.esp.json") and orig in NOLVUS_ENEMY_TRANSLATE:
            new_str, new_status = NOLVUS_ENEMY_TRANSLATE[orig], "TranslationComplete"
        elif rel_path in INTERNAL_EMPTY_FILES or orig in INTERNAL_EMPTY_ORIGS:
            new_str, new_status = orig, "NoTranslationRequired"
        else:
            new_str, new_status = orig, "TranslationComplete"

        file_ops.setdefault(rel_path, []).append({
            "kind": "EMPTY_FIX",
            "form_id": fid,
            "type": rtype,
            "index": idx,
            "original": orig,
            "new_string": new_str,
            "new_status": new_status,
        })

    # 2. Queue Surgical Unit Fixes
    for fix in SURGICAL_UNIT_FIXES:
        file_ops.setdefault(fix["file"], []).append({
            "kind": fix["category"],
            "form_id": fix["form_id"],
            "type": fix["type"],
            "index": fix["index"],
            "original": fix["original"],
            "new_string": fix["new_string"],
            "new_status": "TranslationComplete",
        })

    # 3. Queue Book Font / Image / Pagebreak / HTML Surgical Fixes
    BOOK_REGEX_FIXES = [
        # Font name corruptions
        (r"Armure de chevalier griffon\GVLT_Gryphonknight.esp.json", "02000810|GVLT_Gryphonknight.esp", "BOOK DESC", None,
         "$HandwritingFont", "$HandwrittenFont", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "05236D5A|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "05236D5F|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "05236D60|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "05236D61|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "0571D14F|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "0571D150|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        (r"LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json", "0571D151|LegacyoftheDragonborn.esm", "BOOK DESC", None,
         "$BordecielBooks", "$SkyrimBooks", "F_FONT_IMG_FIX"),
        # Image path corruptions
        (r"Au-delà de Bordeciel - Bruma\BSAssets.esm.json", "01602556|BSAssets.esm", "BOOK DESC", None,
         "Illuminated_Letters0/L_letter.png", "Illuminated_Letters/L_letter.png", "F_FONT_IMG_FIX"),
        (r"Conduit - Canalisation de sort\Conduit.esp.json", "0109D7F6|Conduit.esp", "BOOK DESC", None,
         "Textures/Interface/Livres/Illuminated_Letters/A_letter.png", "Textures/Interface/Books/Illuminated_Letters/A_letter.png", "F_FONT_IMG_FIX"),
        (r"Conduit - Canalisation de sort\Conduit.esp.json", "0109D7F6|Conduit.esp", "BOOK DESC", None,
         "Illuminated_Letters/F_letter.png'>lace", "Illuminated_Letters/G_letter.png'>lace", "F_FONT_IMG_FIX"),
        (r"Conduit - Canalisation de sort\Conduit.esp.json", "0109D7F6|Conduit.esp", "BOOK DESC", None,
         "lorsque vous l'avez quittée.\r\n[pagebreak]",
         "lorsque vous l'avez quittée. Attention toutefois : si cette ancre est complètement détruite prématurément, vous serez perdu à jamais dans les courants dimensionnels.\r\n[pagebreak]", "F_FONT_IMG_FIX"),
        (r"Racirène\evgSIRENROOT.esm.json", "04374415|evgSIRENROOT.esm", "BOOK DESC", None,
         "sirencoronet. png", "sirencoronet.png", "F_FONT_IMG_FIX"),
        (r"Triss Armor Retextured\trissarmorretextured.esp.json", "02000809|TrissArmorRetextured.esp", "BOOK DESC", None,
         "Textures/Interface/Livres/psyold/triss/sorcière.png", "Textures/Interface/Books/psyold/triss/sorceress.png", "F_FONT_IMG_FIX"),
        (r"Triss Armor Retextured\trissarmorretextured.esp.json", "02000809|TrissArmorRetextured.esp", "BOOK DESC", None,
         "Textures/Interface/Livres/", "Textures/Interface/Books/", "F_FONT_IMG_FIX"),
        (r"Triss Armor Retextured\trissarmorretextured.esp.json", "02000809|TrissArmorRetextured.esp", "BOOK DESC", None,
         "temper_fr.png", "temper_en.png", "F_FONT_IMG_FIX"),
        # Malformed pagebreak] (missing opening bracket) & translated [pause] & dropped [pagebreak]
        (r"Au-delà de Bordeciel - Bruma\BSAssets.esm.json", "016024FB|BSAssets.esm", "BOOK DESC", None,
         "\npagebreak]", "\n[pagebreak]", "G_PAGEBREAK_HTML_FIX"),
        (r"LOTD - Synergie avec Bruma\DBM_BSHeartlandPatch - Main.esp.json", "066024FB|BSAssets.esm", "BOOK DESC", None,
         "\npagebreak]", "\n[pagebreak]", "G_PAGEBREAK_HTML_FIX"),
        (r"Chasseur de trésors\TreasureHunter.esp.json", "030067BC|TreasureHunter.esp", "BOOK DESC", None,
         "[pause]", "[pagebreak]", "G_PAGEBREAK_HTML_FIX"),
        (r"L'Héritage de l'Enfant de dragon - Patches officiels\dbm_treasurehunter_patch.esp.json", "060067BC|TreasureHunter.esp", "BOOK DESC", None,
         "[pause]", "[pagebreak]", "G_PAGEBREAK_HTML_FIX"),
        (r"Falskaar\Falskaar.esm.json", "010580B7|Falskaar.esm", "BOOK DESC", None,
         "\r\n\r\n<font size='40'>", "[pagebreak]\r\n\r\n<font size='40'>", "G_PAGEBREAK_HTML_FIX"),
        (r"Falskaar\comprehensive_falskaar_fixes.esp.json", "010580B7|Falskaar.esm", "BOOK DESC", None,
         "\r\n\r\n<font size='40'>", "[pagebreak]\r\n\r\n<font size='40'>", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "Le 2 plantaisons, 4E 180", "Le 12 plantaisons, 4E 180", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "\n\nLe 8 soufflegivre, 4E 182", "\n\n[pagebreak]\nLe 8 soufflegivre, 4E 182", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "\n\nLe 23 Mi-l'An, 4E 191", "\n\n[pagebreak]\nLe 23 Mi-l'An, 4E 191", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "\n\nLe 11 Âtrefeu, 4E 200", "\n\n[pagebreak]\nLe 11 Âtrefeu, 4E 200", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "\n\n(À partir d'ici", "\n\n[pagebreak]\n(À partir d'ici", "G_PAGEBREAK_HTML_FIX"),
        (r"Vigilant - Book Covers VF 1.3 SE\Vigilant - Book Covers.esp.json", "0101C7F7|Vigilant.esm", "BOOK DESC", None,
         "Moron a incendié une maison", "Cet abruti a incendié une maison", "G_PAGEBREAK_HTML_FIX"),
        # Unbalanced HTML tags
        (r"vigile_1.7.3_sse\vigilant.esm.json", "021CA545|Vigilant.esm", "BOOK DESC", None,
         '<p align="center">Comptine pour enfants d\'Anequina, Elsweyr</font>',
         '<p align="center">Comptine pour enfants d\'Anequina, Elsweyr</p>', "G_PAGEBREAK_HTML_FIX"),
        (r"Wintersun - Religions de Bordeciel\Wintersun - Faiths of Skyrim.esp.json", "042EE945|Wintersun - Faiths of Skyrim.esp", "BOOK DESC", None,
         "</b>>", "</b>", "G_PAGEBREAK_HTML_FIX"),
    ]

    for rel_path, fid, rtype, idx, old_sub, new_sub, cat in BOOK_REGEX_FIXES:
        file_ops.setdefault(rel_path, []).append({
            "kind": cat,
            "is_sub": True,
            "form_id": fid,
            "type": rtype,
            "index": idx,
            "old_sub": old_sub,
            "new_sub": new_sub,
        })

    SEWERS_IDS = [
        ("0504037D|SkyrimSewers.esp", "BOOK DESC", None),
        ("050403B8|SkyrimSewers.esp", "BOOK DESC", None),
        ("0504FE7F|SkyrimSewers.esp", "BOOK DESC", None),
    ]
    for fid, rtype, idx in SEWERS_IDS:
        file_ops.setdefault(r"Égouts de Bordeciel\SkyrimSewers.esp.json", []).append({
            "kind": "G_PAGEBREAK_HTML_FIX",
            "is_sewers_font": True,
            "form_id": fid,
            "type": rtype,
            "index": idx,
        })

    stats = {}
    modified_files = 0
    for rel_path, ops in sorted(file_ops.items()):
        full_path = os.path.join(ROOT, rel_path)
        with open(full_path, encoding="utf-8") as f:
            data = json.load(f)

        file_changed = False
        for op in ops:
            if op.get("is_sub"):
                matches = [
                    e for e in data
                    if e.get("form_id") == op["form_id"]
                    and e.get("type") == op["type"]
                    and e.get("index") == op["index"]
                ]
                assert len(matches) == 1, f"Expected 1 match for {op} in {rel_path}, got {len(matches)}"
                entry = matches[0]
                if op["old_sub"] in entry["string"]:
                    entry["string"] = entry["string"].replace(op["old_sub"], op["new_sub"])
                    file_changed = True
                    stats[op["kind"]] = stats.get(op["kind"], 0) + 1
                else:
                    assert op["new_sub"] in entry["string"], f"Neither {op['old_sub']!r} nor {op['new_sub']!r} found in {rel_path} {op['form_id']}"
                    stats[op["kind"]] = stats.get(op["kind"], 0) + 1
            elif op.get("is_sewers_font"):
                matches = [
                    e for e in data
                    if e.get("form_id") == op["form_id"]
                    and e.get("type") == op["type"]
                    and e.get("index") == op["index"]
                ]
                assert len(matches) == 1, f"Expected 1 match for {op} in {rel_path}, got {len(matches)}"
                entry = matches[0]
                en_close = len(re.findall(r"</font>", entry["original"], re.I))
                fr_close = len(re.findall(r"</font>", entry["string"], re.I))
                if fr_close < en_close:
                    entry["string"] = entry["string"] + ("</font>" * (en_close - fr_close))
                    file_changed = True
                stats[op["kind"]] = stats.get(op["kind"], 0) + 1
            else:
                if not op["form_id"] and op["type"] in (None, "", "MCM"):
                    matches = [
                        e for e in data
                        if e.get("original") == op["original"]
                    ]
                else:
                    matches = [
                        e for e in data
                        if (e.get("form_id") or "") == (op["form_id"] or "")
                        and (e.get("type") or "") == (op["type"] or "")
                        and e.get("index") == op["index"]
                        and e.get("original") == op["original"]
                    ]
                assert len(matches) == 1, f"Expected 1 match for {op['form_id']} {op['type']} in {rel_path}, got {len(matches)}"
                entry = matches[0]
                if entry.get("string") != op["new_string"] or entry.get("status") != op["new_status"]:
                    entry["string"] = op["new_string"]
                    entry["status"] = op["new_status"]
                    file_changed = True
                stats[op["kind"]] = stats.get(op["kind"], 0) + 1

        if file_changed:
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            modified_files += 1

    print(f"Modified {modified_files} files.")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
