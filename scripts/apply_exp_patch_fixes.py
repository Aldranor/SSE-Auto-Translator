import json
import shutil
from pathlib import Path

f1 = Path("data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json")
f2 = Path("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json")

# Backups
for f in [f1, f2]:
    if f.exists():
        bak = f.with_suffix(".json.bak")
        shutil.copy2(f, bak)
        print(f"Created backup: {bak}")

corrections = {
    # Dawnfang missing / corrupted CNAM
    ("1D000F18|ccbgssse013-dawnfang.esl", "QUST CNAM", 78): (
        "En regagnant la chambre de l'épée, j'ai constaté que le bouclier magique entourant l'arme s'était altéré, tout comme son emprise sur la lame. Se pourrait-il que la défaite du Gardien affaiblisse ce bouclier ? Puisqu'une autre porte s'est ouverte, je devrais explorer cette nouvelle zone pour vérifier cette théorie.",
        "TranslationComplete"
    ),
    ("1D000F18|ccbgssse013-dawnfang.esl", "QUST CNAM", 81): (
        "Une fois de plus, mon affrontement contre le Gardien a altéré le bouclier entourant l'épée. Je devrais fouiller la zone qui vient de s'ouvrir, où je risque de croiser le Gardien à nouveau.",
        "TranslationComplete"
    ),
    ("1D000F18|ccbgssse013-dawnfang.esl", "QUST CNAM", 87): (
        "En regagnant la chambre de l'épée, j'ai assisté à une réconciliation entre le Gardien et la femme : leurs esprits se sont enlacés avant de s'évanouir dans l'au-delà. En le terrassant, j'ai sans doute libéré son âme des liens qui l'enchaînaient à l'épée et à cette crypte. Il est désormais libre, et l'épée l'est aussi.",
        "TranslationComplete"
    ),
    ("1D000F18|ccbgssse013-dawnfang.esl", "QUST CNAM", 98): (
        "J'ai vaincu le Gardien. Je devrais retourner dans la chambre de l'épée pour voir si sa défaite a affecté le bouclier.",
        "TranslationComplete"
    ),

    # Quest Titles (Official Bethesda French / CC)
    ("20000D63|cckrtsse001_altar.esl", "QUST FULL", None): ("Dernières volontés", "TranslationComplete"),
    ("0F000D65|ccbgssse034-mntuni.esl", "QUST FULL", None): ("L'homme qui murmurait à l'oreille des chevaux", "TranslationComplete"),
    ("0700083D|ccbgssse003-zombies.esl", "QUST FULL", None): ("Morts d'outre-tombe", "TranslationComplete"),
    ("13000926|ccmtysse002-ve.esl", "QUST FULL", None): ("Veillée impie", "TranslationComplete"),
    ("1A000805|ccbgssse069-contest.esl", "QUST FULL", None): ("Pris dans la toile", "TranslationComplete"),
    ("1D000F18|ccbgssse013-dawnfang.esl", "QUST FULL", None): ("Âme divisée", "TranslationComplete"),
    ("00035354|Skyrim.esm", "QUST FULL", None): ("Le siège du culte des dragons", "TranslationComplete"),
    ("1500080E|ccbgssse038-bowofshadows.esl", "QUST FULL", None): ("Dans l'ombre", "TranslationComplete"),
    ("1B0008B7|ccvsvsse003-necroarts.esl", "QUST FULL", None): ("Arts nécromantiques", "TranslationComplete"),
    ("17000800|ccedhsse002-splkntset.esl", "QUST FULL", None): ("La crypte du Cœur", "TranslationComplete"),
    ("12000927|ccffbsse001-imperialdragon.esl", "QUST FULL", None): ("Le combat des champions", "TranslationComplete"),
    ("00023B6C|Skyrim.esm", "QUST FULL", None): ("Le Cœur de Dibella", "TranslationComplete"),

    # Objectives polish & Anglicism fixes
    ("1500080E|ccbgssse038-bowofshadows.esl", "QUST NNAM", 90): ("Récupérez l'Arc des ombres", "TranslationComplete"),
    ("17000800|ccedhsse002-splkntset.esl", "QUST NNAM", 80): ("(Optionnel) Purifiez le cœur sur l'autel", "TranslationComplete"),
}

for target_file in [f1, f2]:
    if not target_file.exists():
        continue
    with open(target_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    modified = 0
    for e in data:
        k = (e.get("form_id"), e.get("type"), e.get("index"))
        if k in corrections:
            new_str, new_stat = corrections[k]
            if e.get("string") != new_str or e.get("status") != new_stat:
                e["string"] = new_str
                e["status"] = new_stat
                modified += 1
                
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {target_file}: {modified} entries corrected.")

print("Done updating both database files.")
