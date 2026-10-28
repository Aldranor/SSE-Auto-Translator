"""Phase 5 Clean Application Script.

Applies:
1. English calque removal and false friend corrections (Translations instructions.txt):
   - "Vous êtes capable de" -> "Vous pouvez" / "Permet de"
   - "fait X points de dégâts" -> "inflige X points de dégâts"
   - "Armure de plate" -> "Armure de plates"
   - "Assurez-vous de" -> "Veillez à" / "N'oubliez pas de" / "Pensez à"
2. Equipment sets intra-mod consistency and gender/number agreement:
   - Harmonize Khash-Ti Dhrur set
   - Correct daedric armor plural agreements (Gantelets/Bottes daedriques légers/légères)
   - Correct Dragon Infused Daedric Armor set across heavy/light/cloth variants
   - Correct "Cuirasse plaquées" -> "Cuirasse plaquée"
3. Book structural integrity (BOOK DESC pagebreaks):
   - Restore pagebreaks in Frostmere Crypt Journal (LOTD)
   - Restore pagebreaks in Japhet's Journal (LOTD & USSEP)
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Tuple

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

# Targeted string replacements: (rel_path_contains_lower, idx, old_substring, new_substring)
TARGETED_REPLACEMENTS: List[Tuple[str, int, str, str]] = [
    # 1. Calques & False Friends
    ("nolvus awakening armors balance patch.esp.json", 901, "Armure de plate des Paladins de Stendarr", "Armure de plates des paladins de Stendarr"),
    ("sl01amuletsskyrim.esp.json", 51, "L'arme équipée fait <15> points de dégâts de vigueur et de magie.", "L'arme équipée inflige <15> points de dégâts de vigueur et de magie."),
    ("tools of kagrenac.esp.json", 26, "Une énergie qui fait <mag> points de dégâts à la santé par seconde.", "Une force d'énergie qui inflige <mag> points de dégâts à la santé par seconde."),
    ("ordinator - perks of skyrim.esp.json", 909, "Vous êtes capable de marchander avec n'importe quel humanoïde.", "Permet de marchander avec n'importe quel humanoïde."),
    ("ordinator - perks of skyrim.esp.json", 3776, "Pendant un combat, vous êtes capable de lancer des sorts ciblés et des effets de guérison visant les ennemis, qui leur infligent des dégâts équivalent", "En combat, vous pouvez lancer des sorts et des effets de guérison ciblés sur les ennemis, qui leur infligent des dégâts équivalant"),
    ("ordinator - perks of skyrim.esp.json", 4378, "Vous êtes capable de créer des squelettes de feu, de glace ou de foudre, à un autel des ossements.", "Permet de créer des mages squelettes de feu, de glace ou de foudre, à un autel des ossements."),
    ("ordinator - perks of skyrim.esp.json", 4389, "Vous êtes capable de créer des squelettes de feu, de glace, de foudre, fielleux, pourfendeurs d'armure ou ravageurs, à un autel des ossements.", "Permet de créer des mages squelettes de feu, de glace, de foudre, fielleux, pourfendeurs d'armure ou ravageurs, à un autel des ossements."),
    ("apocalypse - ordinator compatibility patch.esp.json", 36, "vous êtes capable de lancer des sorts et effets de guérison ciblés", "vous pouvez lancer des sorts et effets de guérison ciblés"),
    ("gray fox cowl.esm.json", 688, "si vous êtes capable de vous échapper du royaume", "si vous pouvez vous échapper de ce plan"),
    ("3dnpc.esp.json", 39967, "vous êtes capable de vous débrouiller seule en combat.", "vous pouvez vous débrouiller seule en combat."),
    ("3dnpc.esp.json", 3621, "Assurez-vous de ne pas commettre la même erreur.", "Veillez à ne pas commettre la même erreur."),
    ("3dnpc.esp.json", 6119, "Assurez-vous de voir Colette si vous avez la moindre blessure.", "Pensez à voir Colette si vous avez la moindre blessure."),
    ("3dnpc.esp.json", 9648, "Assurez-vous de passer au tonneau du camp.", "N'oubliez pas de passer au tonneau du camp."),
    ("3dnpc.esp.json", 28488, "Assurez-vous de me rendre la faveur et de venir à mon mariage.", "N'oubliez pas de me rendre la pareille et de venir à mon mariage."),

    # 2. Equipment sets & agreement fixes
    ("mihailxivkynarmor.esp.json", 7, "Gantelets daedrique légers", "Gantelets daedriques légers"),
    ("mihailxivkynarmor.esp.json", 11, "Bottes daedrique légères", "Bottes daedriques légères"),
    ("nolvus awakening armors balance patch.esp.json", 97, "Gantelets daedrique légers", "Gantelets daedriques légers"),
    ("nolvus awakening armors balance patch.esp.json", 1192, "Bottes daedrique légères", "Bottes daedriques légères"),
    ("nolvus awakening armors balance patch.esp.json", 872, "Cuirasse plaquées en chitine de vasard", "Cuirasse plaquée en chitine de vasard"),
    ("ryn's crabber's shanty.esp.json", 3, "Cuirasse plaquées en chitine de vasard", "Cuirasse plaquée en chitine de vasard"),
    ("apocalypse - magic of skyrim.esp.json", 1730, "Armure de Khash-Ti", "Armure de Khash-Ti Dhrur"),

    # Dragon Infused Daedric Armor harmonization
    ("dragoninfuseddaedricarmor.esp.json", 2, "Bottes daedrique infusée du dragon (lourde)", "Bottes daedriques infusées du dragon (lourdes)"),
    ("dragoninfuseddaedricarmor.esp.json", 7, "Gantelets daedriques infusées du dragon (lourde)", "Gantelets daedriques infusés du dragon (lourds)"),
    ("dragoninfuseddaedricarmor.esp.json", 3, "Heaume Daedra de Dragon infusé (léger)", "Heaume daedrique infusé du dragon (léger)"),
    ("dragoninfuseddaedricarmor.esp.json", 4, "Gantelets Daedra de Dragon infusé (léger)", "Gantelets daedriques infusés du dragon (légers)"),
    ("dragoninfuseddaedricarmor.esp.json", 5, "Armure Daedra de Dragon infusé (léger)", "Armure daedrique infusée du dragon (légère)"),
    ("dragoninfuseddaedricarmor.esp.json", 6, "Bottes Daedra de Dragon infusé (léger)", "Bottes daedriques infusées du dragon (légères)"),
    ("dragoninfuseddaedricarmor.esp.json", 10, "Heaume Daedra de Dragon infusé (vêtements)", "Heaume daedrique infusé du dragon (tissu)"),
    ("dragoninfuseddaedricarmor.esp.json", 11, "Gantelets Daedra de Dragon infusé (vêtements)", "Gantelets daedriques infusés du dragon (tissu)"),
    ("dragoninfuseddaedricarmor.esp.json", 9, "Armure Daedra de Dragon infusé (vêtements)", "Armure daedrique infusée du dragon (tissu)"),
    ("dragoninfuseddaedricarmor.esp.json", 8, "Bottes Daedra de Dragon infusé (vêtements)", "Bottes daedriques infusées du dragon (tissu)"),
]

# Full replacement for books needing pagebreak restoration
FROSTMERE_CRYPT_JOURNAL = (
    '<font face="$HandwrittenFont" size="18"><b>Crypte de Givrelac, 12e semaine</b>\r\n\r\n'
    "Quel désastre, pas une seule caravane en vue depuis une semaine et nous avons perdu du terrain dans les tunnels. Thal et son équipe ont été écrasés lors de l'effondrement de leur section et les rumeurs de mutinerie grondent. Si la situation ne s'améliore pas la semaine prochaine...\n"
    "[pagebreak]\n"
    "<b>Crypte de Givrelac, 13e semaine</b>\r\n\r\n"
    "Nous avons deux nouvelles recrues, Eisa et Ra'jirr. La fille raconte qu'elle a purgé une peine à la mine de Cidhna, du côté de Markarth, et ça se voit... elle semble plus expérimentée que nous tous réunis ! Je l'ai nommée responsable des fouilles. Le chat est bon à l'épée, aussi l'ai-je mis à la tête des raids en surface.\n"
    "[pagebreak]\n"
    "<b>Crypte de Givrelac, 14e semaine</b>\r\n\r\n"
    "Le tunnel avance bien. Eisa a fait sa première grosse découverte hier, un coffre enfoui contenant quelques centaines de pièces d'or. À la surface, Ra'jirr et ses gars ont attaqué cinq marchands cette semaine, frappant si vite que les gardes n'ont rien pu faire. Finalement, les choses semblent s'arranger.\n"
    "[pagebreak]\n"
    "<b>Crypte de Givrelac, 15e semaine</b>\r\n\r\n"
    "Le tunnel a débouché sur une espèce de grotte géante. Il y a une forêt entière, là-dedans et j'ai trouvé une belle épée, posée dans une sorte de monument, mais c'est étrange... sinistre. Quel est donc cet endroit ? Je n'ai jamais vu de tombeau de ce genre.\n"
    "[pagebreak]\n"
    "<b>Crypte de Givrelac, 16e semaine</b>\r\n\r\n"
    "Je crois que le chat est en train de devenir fou. Tout d'un coup, il n'arrive plus à se concentrer et se met à parler tout seul. Rien qu'aujourd'hui, celui qui était notre meilleur combattant en est réduit à l'état de misérable épave. Eisa essaie de le couvrir, mais personne n'est dupe.\r\n\r\n"
    "Dernièrement, il me demande de lui montrer mon épée, me suppliant de la lui prêter. Comme si j'allais lui laisser poser ses sales pattes dessus... elle est belle, parfaitement équilibrée, c'est la meilleure que j'ai jamais eue entre les mains. S'il continue, il va l'avoir... plantée dans le ventre !\n"
    "</font>"
)

JAPHET_JOURNAL = (
    '<font face="$HandwrittenFont">À mon départ d\'Aubétoile, j\'ai été rejoint par un groupe plus modeste que prévu. Apparemment, la rumeur locale veut que l\'île soit totalement inhabitable : des histoires d\'esprits et de climat défavorable. Peu importe, cela ne laissera que plus d\'espace aux plus loyaux, bien que la construction de la citadelle en sera d\'autant plus laborieuse.\n'
    "[pagebreak]\n"
    "Le premier hiver a été rude et beaucoup ont préféré retourner auprès de leurs familles sur le continent. Voyons cela comme une sélection naturelle salutaire : que les hommes de peu de foi, les faibles et les moins courageux s'en aillent, nous nous passerons bien d'eux.\n"
    "[pagebreak]\n"
    "Les histoires de fantômes qui hantent cet endroit ne sont que des fables... qui en ont cependant fait fuir encore quelques-uns, prompts à pleurer comme des enfants effrayés par leur propre ombre au coin du feu. Mes plus proches partisans et moi restons sereins, et toujours vaillants.\n"
    "[pagebreak]\n"
    "Après tout, je n'ai guère besoin de compagnie. Le froid et le vent semblent s'être unis pour chasser les derniers spécimens de ceux qui se prétendaient mes compatriotes. Ces bons à rien, que les dieux les emportent ! Puissent tous ceux qui poseront le regard sur la forteresse de Japhet frémir en pensant au grand homme qui parvint à conquérir l'île maudite.\n"
    "[pagebreak]\n"
    "Voilà que même mes plus fidèles passeurs ont mis un terme aux ravitaillements réguliers en nourriture et en matériel à la forteresse. Je dois maintenant me suffire à moi-même et cultiver la terre, comme mon père l'a fait avant moi.\n"
    "[pagebreak]\n"
    "Les pierres sont partout et mes récoltes bien maigres, mais je n'abandonnerai pas ma plus grande création. Je tiendrai droit dans la tempête, et je repousserai les fantômes, et je hurlerai contre le vent, tant et si bien que l'on chantera longtemps les louanges de ma fière colonie.\n"
    "[pagebreak]\n"
    "Je commence à croire que ces histoires de fantômes ne sont pas tout à fait dénuées d'un certain fond de vérité. À moins que ce soit la faim qui parle...\n"
    "[pagebreak]\n"
    "Les fantômes me parlent maintenant, et plus je mange de ce lichen glacé, plus je les entends clairement. Ils me disent que j'ai fait une erreur en venant ici. Comme si je ne le savais déjà !\n"
    "[pagebreak]\n"
    "PAR LES DIEUX AIDEZ-MOI\n"
    "</font>"
)


def apply_phase5() -> None:
    """Execute Phase 5 clean across all database files."""
    modified_files = 0
    total_fixes = 0

    # Build lookup
    lookup: Dict[Tuple[str, int], Tuple[str, str]] = {}
    for fn, idx, old_txt, new_txt in TARGETED_REPLACEMENTS:
        lookup[(fn.lower(), idx)] = (old_txt, new_txt)

    for root, _, files in os.walk(DB_DIR):
        for f in sorted(files):
            if not f.endswith(".json") or f == "index.json":
                continue
            path = os.path.join(root, f)
            fn_lower = f.lower()

            try:
                with open(path, "r", encoding="utf-8") as fp:
                    data: List[Dict[str, Any]] = json.load(fp)
            except Exception as e:
                print(f"Error loading {path}: {e}")
                continue

            file_modified = False

            for idx, row in enumerate(data):
                key = (fn_lower, idx)
                if key in lookup:
                    old_txt, new_txt = lookup[key]
                    s = row.get("string", "")
                    if old_txt in s:
                        row["string"] = s.replace(old_txt, new_txt)
                        file_modified = True
                        total_fixes += 1

                # Specific books pagebreak restorations
                if fn_lower == "legacyofthedragonborn.esm.json" and idx == 3549:
                    row["string"] = FROSTMERE_CRYPT_JOURNAL
                    file_modified = True
                    total_fixes += 1
                elif fn_lower == "legacyofthedragonborn.esm.json" and idx == 3918:
                    row["string"] = JAPHET_JOURNAL
                    file_modified = True
                    total_fixes += 1
                elif fn_lower == "unofficial skyrim special edition patch.esp.json" and idx == 2630:
                    row["string"] = JAPHET_JOURNAL
                    file_modified = True
                    total_fixes += 1

            if file_modified:
                try:
                    with open(path, "w", encoding="utf-8", newline="\n") as fp:
                        json.dump(data, fp, indent=2, ensure_ascii=False)
                    modified_files += 1
                    print(f"Updated {f}")
                except Exception as e:
                    print(f"Error writing {path}: {e}")

    print("=" * 60)
    print("PHASE 5 CLEAN APPLICATION COMPLETED SUCCESSFULLY")
    print(f"Total fixes applied:   {total_fixes}")
    print(f"Total modified files: {modified_files}")
    print("=" * 60)


if __name__ == "__main__":
    apply_phase5()
