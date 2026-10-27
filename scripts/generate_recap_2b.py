import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Definitive list of all actual changes in Sub-phase 2B with verified historical "Avant" values
actual_changes_2b = [
    # 1. CCQuest - Experience Patch
    {
        'file': 'ccquest - experience patch.esp.json',
        'form_id': '1000080F|ccbgssse020-graycowl.esl',
        'type': 'QUST CNAM',
        'original': "At the Riften cemetery, I found a thief loitering near a tombstone. On his body was a note that mentioned the Gray Fox was dead, and his cowl was to be passed on to a new owner. I then spoke to a beggar who handed me a note.",
        'before': "At the Riften cemetery, I found a thief loitering near a tombstone. On his body was a note that mentioned the Gray Fox was dead, and his cowl was to be passed on to a new owner. I spoke to a beggar who handed me a note informing me of a job.",
        'after': "Au cimetière de Faillaise, j'ai trouvé un voleur qui rôdait près d'une pierre tombale. Sur son corps se trouvait une note mentionnant que le Renard gris était mort et que son capuchon devait être transmis à un nouveau propriétaire. J'ai ensuite parlé à un mendiant qui m'a remis une note m'informant d'un travail.",
        'nature': "Traduction intégrale d'une étape de quête du Capuchon gris de Nocturne restée en anglais"
    },

    # 2. Eating Animations and Sounds - Dawn of Skyrim Patch
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '02020D57|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Falkreath Porridge",
        'before': "Porridge de Faillaise",
        'after': "Porridge d'Épervine",
        'nature': "Correction de contresens géographique critique : Falkreath = Épervine (et non Faillaise/Riften)"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '02020D54|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Haafingar Butter",
        'before': "Beure d'Haafingar",
        'after': "Beurre d'Haafingar",
        'nature': "Correction de coquille : Beurre (au lieu de Beure)"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE7F|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Pheasant Pie",
        'before': "Tarte au Faisant",
        'after': "Tourte au faisan",
        'nature': "Correction de coquille orthographique : faisan (au lieu de Faisant) et gastronomie médiévale"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE83|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Dawnstar Spiced Cake",
        'before': "Cake épicé d'Aubétoile",
        'after': "Gâteau aux épices d'Aubétoile",
        'nature': "Élimination de l'anglicisme 'Cake' -> Gâteau aux épices"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE85|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Midyear Cake",
        'before': "Cake de mi-l'an",
        'after': "Gâteau de mi-l'an",
        'nature': "Élimination de l'anglicisme 'Cake' -> Gâteau"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE87|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Ivarstead Loaf",
        'before': "Tourte de Fort-Ivar",
        'after': "Pain de Fort-Ivar",
        'nature': "Fidélité au mod source : Pain (Loaf) au lieu de Tourte"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE7A|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Solitude Dusted Bread",
        'before': "Pain Traditionnel de Solitude",
        'after': "Pain au poivre de Solitude",
        'nature': "Harmonisation Dawn of Skyrim : Dusted Bread = Pain au poivre"
    },
    {
        'file': 'taberu animation - dawn of skyrim patch.esp.json',
        'form_id': '0201DE81|Dawn of Skyrim.esp',
        'type': 'ALCH FULL',
        'original': "Snowberry Biscuit",
        'before': "Biscuit de Givreboise",
        'after': "Biscuit aux givreboises",
        'nature': "Terminologie officielle Bethesda : givreboises (Snowberry)"
    },

    # 3. Eating Animations and Sounds - Cheesemod Patch
    {
        'file': 'taberu animation - cheesemod patch.esp.json',
        'form_id': '02003782|yumcheese.esp',
        'type': 'ALCH FULL',
        'original': "Sliced Autumnshade Cheese",
        'before': "Brie des Ombres de l'Automne entamé",
        'after': "Brie de Vendombre entamé",
        'nature': "Harmonisation toponyme canonique : Autumnshade = Vendombre"
    },
    {
        'file': 'taberu animation - cheesemod patch.esp.json',
        'form_id': '02003786|yumcheese.esp',
        'type': 'ALCH FULL',
        'original': "Autumnshade Cheese Wedge",
        'before': "Brie des Ombres de l'Automne",
        'after': "Brie de Vendombre",
        'nature': "Harmonisation toponyme canonique : Autumnshade = Vendombre"
    },

    # 4. Navigator - Navmesh Fixes
    {
        'file': 'navigator-navfixes.esl.json',
        'form_id': '0001529F|Skyrim.esm',
        'type': 'CELL FULL',
        'original': "Darklight Tower",
        'before': "Tour Clair-osbcur",
        'after': "Tour Clair-Obscur",
        'nature': "Correction de coquille dans le nom de lieu : Clair-Obscur (au lieu de Clair-osbcur)"
    },
    {
        'file': 'navigator-navfixes.esl.json',
        'form_id': '000466CB|Skyrim.esm',
        'type': 'CELL FULL',
        'original': "Irkngthand Sanctuary",
        'before': "Irkngthand - Sanctuaire",
        'after': "Sanctuaire d'Irkngthand",
        'nature': "Canon officiel Bethesda : Sanctuaire d'Irkngthand"
    },
    {
        'file': 'navigator-navfixes.esl.json',
        'form_id': '0002164A|Skyrim.esm',
        'type': 'CELL FULL',
        'original': "Avanchnzel Boilery",
        'before': "Avanchnzel - Brasserie",
        'after': "Brasserie d'Avanchnzel",
        'nature': "Canon officiel Bethesda : Brasserie d'Avanchnzel"
    },

    # 5. Wintersun - Tribunal Integration
    {
        'file': 'wintersun - gott patch.esp.json',
        'form_id': '05000849|Wintersun - GotT Patch.esp',
        'type': 'MGEF DNAM',
        'original': "Items are enchanted <Global=WSN_Favor_Global_Fractional3>% stronger (based on favor with Sotha Sil).",
        'before': "Les objets sont enchantés jusqu'à 20% plus puissamment (basé sur la faveur de Sotha Sil).",
        'after': "Les enchantements d'objets sont <Global=WSN_Favor_Global_Fractional3> % plus puissants (selon votre ferveur envers Sotha Sil).",
        'nature': "Rétablissement de la variable dynamique moteur <Global=WSN_Favor_Global_Fractional3> écrasée à tort par une valeur fixe '20%'"
    },
    {
        'file': 'wintersun - gott patch.esp.json',
        'form_id': '05000879|Wintersun - GotT Patch.esp',
        'type': 'MGEF DNAM',
        'original': "When health falls below <25>% in combat, receive an automatic healing pulse.  Restored by prayer.",
        'before': "Lorsque la santé tombe en dessous de 25% en combat, recevez une impulsion de guérison automatique. Restauré par la prière.",
        'after': "Lorsque votre santé passe sous les <25> % en combat, vous recevez une pulsation de soins automatique. Se recharge par la prière.",
        'nature': "Conservation de la variable <25> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'wintersun - gott patch.esp.json',
        'form_id': '0406AD19|Wintersun - Faiths of Skyrim.esp',
        'type': 'MGEF DNAM',
        'original': "Your benevolence improves your Speech skill by <mag> points for <1> hour.",
        'before': "Votre générosité améliore votre éloquence de <mag> points pour 1 heure.",
        'after': "Votre bienveillance améliore votre éloquence de <mag> points pendant <1> heure.",
        'nature': "Conservation de la variable <1> conforme à l'original"
    },

    # 6. Complete Crafting Overhaul Remastered - Immersive Sounds Patch
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6904|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation (minuscule sur articulation)"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6904|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <10> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 10 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <10> points.",
        'nature': "Conservation de la variable <10> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690D|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690D|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <15> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 15 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <15> points.",
        'nature': "Conservation de la variable <15> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690E|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690E|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <20> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 20 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <20> points.",
        'nature': "Conservation de la variable <20> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690F|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F690F|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <25> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 25 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <25> points.",
        'nature': "Conservation de la variable <25> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6910|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6910|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <30> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 30 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <30> points.",
        'nature': "Conservation de la variable <30> conforme à l'original et tournure française naturelle"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6911|Skyrim.esm',
        'type': 'ARMO FULL',
        'original': "Amulet of Articulation",
        'before': "Amulette d'Articulation",
        'after': "Amulette d'articulation",
        'nature': "Canon officiel Bethesda : Amulette d'articulation"
    },
    {
        'file': 'ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
        'form_id': '000F6911|Skyrim.esm',
        'type': 'ARMO DESC',
        'original': "Persuade checks in dialogue will almost always succeed and increases Speech skill by <35> points.",
        'before': "Les persuasions lors des dialogues réussiront presque toujours et l'éloquence augmente de 35 points.",
        'after': "Les tentatives de persuasion réussissent presque toujours et l'éloquence augmente de <35> points.",
        'nature': "Conservation de la variable <35> conforme à l'original et tournure française naturelle"
    }
]

# Write accurate recap markdown file
md_lines = [
    "# Récapitulatif des Modifications — Phase 2B : Quêtes, Expérience & Mécaniques Locales",
    "",
    "> **Périmètre :** Sous-phase 2B de l'audit final ([PLAN_RELECTURE_FINALE.md](file:///e:/Code/SSE%20Translator%20updated/PLAN_RELECTURE_FINALE.md)).",
    "> **Mods audités :** 10 mods locaux d'expérience, quêtes, religions et mécaniques (`CCQuest - Experience Patch`, `Nolvus Experience Integration`, `Lucien CC Patch`, `Vokrii Spell Conditions Fix`, `Wintersun Description Fixes & Tribunal Integration`, `CCOR Immersive Sounds Patch`, `Crossbow Integration`, `Navigator Navmesh Fixes`, `Eating Animations and Sounds Patch Collection`).",
    "> **Volume de vérification :** 4 541 enregistrements contrôlés, intégrité des variables dynamiques, fidélité géographique et lore officiel Bethesda.",
    "",
    "---",
    ""
]

def clean_cell(val):
    if val is None:
        return ""
    val_str = str(val).replace('\r', ' ').replace('\n', '<br>')
    return val_str.replace('|', '\\|')

by_file = {}
for entry in actual_changes_2b:
    by_file.setdefault(entry['file'], []).append(entry)

for fn, entries in by_file.items():
    md_lines.append(f"## 📁 {fn}")
    md_lines.append(f"*Nombre d'ajustements majeurs :* **{len(entries)}**\n")
    md_lines.append("| FormID / Type | Texte Original (EN) | Avant (Ancienne trad / Décalage) | Après (Traduction canonique validée) | Nature du correctif |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    for e in entries:
        fid_formatted = e['form_id'].replace('|', ' (') + ')'
        orig = clean_cell(e['original'])
        before = clean_cell(e['before'])
        after = f"**{clean_cell(e['after'])}**"
        nat = clean_cell(e['nature'])
        md_lines.append(f"| `{fid_formatted}`<br>*{clean_cell(e['type'])}* | {orig} | {before} | {after} | {nat} |")
    md_lines.append("\n---\n")

with open('recap_modifications_phase2b.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f"Generated recap_modifications_phase2b.md with {len(actual_changes_2b)} accurate entries.")
