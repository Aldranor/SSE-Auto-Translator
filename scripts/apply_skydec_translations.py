# -*- coding: utf-8 -*-
"""
Script complet d'application de la traduction française pour SkyDecoction.esp.json (299 entrées)
"""

import json

ESP_PATH = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"

DECOCTION_NAMES = {
    'Cat': ('Chat', 'm'),
    'Dragonmaw': ('Gueule de dragon', 'f'),
    'Hyphalosaurus': ('Hyphalosaure', 'm'),
    'Thunderstorm': ('Tempête', 'f'),
    'Testudo': ('Testudo', 'f'),
    'Termination': ('Terminaison', 'f'),
    'Equipartition': ('Équipartition', 'f'),
    'Rosmontis': ('Rosmontis', 'f'),
    'Strigiformes': ('Strigiformes', 'mp'),
    'Prism': ('Prisme', 'm'),
    'Herculiani': ('Herculiani', 'mp'),
    'Ioviani': ('Ioviani', 'mp'),
    'Exploratores': ('Exploratores', 'mp'),
    'Healer': ('Guérisseur', 'm'),
    'Sober': ('Lucidité', 'f'),
    'Eucles': ('Euclès', 'm'),
    'Defensores': ('Defensores', 'mp'),
    'Rejuvenation': ('Rajeunissement', 'm'),
    'Craftsman': ('Artisan', 'm'),
}

def get_decoction_tier_name(base_en, tier):
    fr_name, gender = DECOCTION_NAMES[base_en]
    if tier == 'base':
        return f"Décoction : {fr_name}"
    elif tier == 'enhanced':
        adj = 'amélioré' if gender == 'm' else ('améliorée' if gender == 'f' else 'améliorés')
        return f"Décoction : {fr_name} {adj}"
    elif tier == 'superior':
        adj = 'supérieur' if gender == 'm' else ('supérieure' if gender == 'f' else 'supérieurs')
        return f"Décoction : {fr_name} {adj}"

def get_residue_tier_name(base_en, tier):
    fr_name, gender = DECOCTION_NAMES[base_en]
    if tier == 'base':
        return f"Résidu : {fr_name}"
    elif tier == 'enhanced':
        adj = 'amélioré' if gender == 'm' else ('améliorée' if gender == 'f' else 'améliorés')
        return f"Résidu : {fr_name} {adj}"
    elif tier == 'superior':
        adj = 'supérieur' if gender == 'm' else ('supérieure' if gender == 'f' else 'supérieurs')
        return f"Résidu : {fr_name} {adj}"

BOOK_DESCRIPTIONS = {
    'zzSkyDecoction2Book': (
        "[pagebreak]\r\n"
        "<p align=\"center\">\r\n\r\n\r\n"
        "Formules de décoctions élémentaires\r\n\r\n\r\n\r\n"
        "</p>\r\n\r\n\r\n\r\n"
        "[pagebreak]\r\n"
        "<p align=\"left\">\r\n"
        "Guérisseur\r\n"
        "La décoction de base de notre école.\r\n"
        "Elle apaise la douleur et régénère les tissus meurtris.\r\n\r\n"
        "Décoction : Guérisseur -\r\n"
        "Bière : 1\r\n"
        "Cloquerille : 4\r\n"
        "Blé : 8\r\n\r\n"
        "Décoction : Guérisseur amélioré -\r\n"
        "Décoction : Guérisseur\r\n"
        "Hydromel nordique : 1\r\n"
        "Œuf de fauvette : 2\r\n"
        "Aile de papillon : 4\r\n\r\n"
        "Décoction : Guérisseur supérieur -\r\n"
        "Décoction : Guérisseur amélioré\r\n"
        "Bière : 1\r\n"
        "Œil de smilodon : 2\r\n"
        "Libellule bleue : 5\r\n\r\n"
        "Solvant : Tout alcool\r\n"
        "[pagebreak]\r\n"
        "Lucidité\r\n"
        "La Lucidité permet une récupération rapide de la magie.\r\n"
        "Une boisson revigorante particulièrement prisée des mages.\r\n\r\n"
        "Décoction : Lucidité -\r\n"
        "Hydromel nordique : 1\r\n"
        "Oreille d'Elfe : 6\r\n"
        "Fleur de montagne rouge : 8\r\n\r\n"
        "Décoction : Lucidité améliorée -\r\n"
        "Décoction : Lucidité\r\n"
        "Hydromel nordique : 1\r\n"
        "Chapeau-blanc : 5\r\n"
        "Lichen géant : 6\r\n\r\n"
        "Décoction : Lucidité supérieure -\r\n"
        "Décoction : Lucidité améliorée\r\n"
        "Hydromel nordique : 1\r\n"
        "Huile dwemer : 4\r\n"
        "Racine noueuse : 8\r\n\r\n"
        "Solvant : Tout alcool\r\n"
        "[pagebreak]\r\n"
        "Euclès\r\n"
        "Cette décoction insuffle une immense énergie, semblable à celle d'un stimulant.\r\n\r\n"
        "Décoction : Euclès -\r\n"
        "Bière : 1\r\n"
        "Chitine de vasard : 4\r\n"
        "Fleur de montagne violette : 6\r\n\r\n"
        "Décoction : Euclès amélioré -\r\n"
        "Décoction : Euclès\r\n"
        "Bière : 1\r\n"
        "Peau de ragnard carbonisée : 5\r\n"
        "Perche argentée : 5\r\n\r\n"
        "Décoction : Euclès supérieur -\r\n"
        "Décoction : Euclès amélioré\r\n"
        "Bière : 1\r\n"
        "Perle : 2\r\n"
        "Œuf de grive : 5\r\n\r\n"
        "Solvant : Tout alcool"
    ),
    'zzSkyDecoction2Book2': (
        "[pagebreak]\r\n"
        "<p align=\"center\">\r\n\r\n\r\n"
        "Formules de décoctions avancées\r\n\r\n\r\n\r\n"
        "</p>\r\n\r\n\r\n\r\n"
        "[pagebreak]\r\n"
        "<p align=\"left\">\r\n"
        "Herculiani\r\n"
        "Elle accroît la force physique et accélère la guérison des blessures en un court laps de temps.\r\n\r\n"
        "Décoction : Herculiani -\r\n"
        "Hydromel Roncenoir : 1\r\n"
        "Skooma : 1\r\n"
        "Blé : 5\r\n"
        "Genièvres : 8\r\n\r\n"
        "Décoction : Herculiani améliorés -\r\n"
        "Décoction : Herculiani\r\n"
        "Hydromel Roncenoir : 1\r\n"
        "Orteil de géant : 3\r\n"
        "Griffes d'ours : 4\r\n"
        "Truffe de Namira : 8\r\n\r\n"
        "Décoction : Herculiani supérieurs -\r\n"
        "Décoction : Herculiani améliorés\r\n"
        "Hydromel Roncenoir : 1\r\n"
        "La Chance soyeuse : 3\r\n"
        "Défense de sanglier : 3\r\n"
        "Poussière de vampire : 3\r\n"
        "Voiles éthérés : 4\r\n\r\n"
        "Solvant : Hydromel Roncenoir\r\n"
        "[pagebreak]\r\n"
        "Ioviani\r\n"
        "Les Ioviani constituent un puissant calmant qui fortifie la magie et renforce la puissance des sorts.\r\n\r\n"
        "Décoction : Ioviani -\r\n"
        "Skooma : 1\r\n"
        "Vin : 1\r\n"
        "Obscurcine : 4\r\n"
        "Raisin jazbay : 5\r\n"
        "Fleur de montagne rouge : 7\r\n\r\n"
        "Décoction : Ioviani améliorés -\r\n"
        "Décoction : Ioviani\r\n"
        "Vin : 1\r\n"
        "Sucre de lune : 3\r\n"
        "Racine noueuse : 4\r\n"
        "Carpe du Hist : 5\r\n\r\n"
        "Décoction : Ioviani supérieurs -\r\n"
        "Décoction : Ioviani améliorés\r\n"
        "Vin : 1\r\n"
        "Tour d'Or blanc : 3\r\n"
        "Œufs de saumon : 2\r\n"
        "Antennes de chasseur chaurus : 3\r\n"
        "Mousse de parasol de l'Empereur : 7\r\n\r\n"
        "Solvant : Vin\r\n"
        "[pagebreak]\r\n"
        "Exploratores\r\n"
        "Les Exploratores sont le breuvage favori des voyageurs : il accroît l'endurance et accorde le pouvoir magique de marcher sur l'eau.\r\n\r\n"
        "Décoction : Exploratores -\r\n"
        "Skooma : 1\r\n"
        "Hydromel d'Hydreliqueur : 1\r\n"
        "Bernacle nordique : 4\r\n"
        "Lavande : 6\r\n"
        "Amanite tue-mouches : 7\r\n\r\n"
        "Décoction : Exploratores améliorés -\r\n"
        "Décoction : Exploratores\r\n"
        "Hydromel d'Hydreliqueur : 1\r\n"
        "Œuf de poule : 4\r\n"
        "Thorax de Flammouche : 5\r\n"
        "Mora Tapinella : 6\r\n\r\n"
        "Décoction : Exploratores supérieurs -\r\n"
        "Décoction : Exploratores améliorés\r\n"
        "Hydromel d'Hydreliqueur : 1\r\n"
        "Le Course-Falaise : 3\r\n"
        "Œuf du faucon : 1\r\n"
        "Abeille : 3\r\n"
        "Grande ramure : 7\r\n\r\n"
        "Solvant : Hydromel d'Hydreliqueur\r\n"
        "[pagebreak]\r\n"
        "Prisme\r\n"
        "Une substance magique capable de vous rendre invisible.\r\n\r\n"
        "Décoction : Prisme -\r\n"
        "Sève d'Arbre dormant : 1\r\n"
        "Bière : 1\r\n"
        "Racine de Nirn : 3\r\n"
        "Aile de noctuelle : 5\r\n"
        "Œufs de chaurus : 8\r\n\r\n"
        "Décoction : Prisme amélioré -\r\n"
        "Décoction : Prisme\r\n"
        "Bière : 1\r\n"
        "Racine de Nirn cramoisie : 1\r\n"
        "Dent de spectre de glace : 4\r\n"
        "Racine de cendres : 7\r\n\r\n"
        "Décoction : Prisme supérieur -\r\n"
        "Décoction : Prisme amélioré\r\n"
        "Bière : 1\r\n"
        "Défense de mammouth en poudre : 2\r\n"
        "Ruche vide : 4\r\n"
        "Poussière de vampire : 6\r\n\r\n"
        "Solvant : Bière\r\n"
        "[pagebreak]\r\n"
        "Strigiformes\r\n"
        "Cette décoction confère une acuité visuelle digne des prédateurs nocturnes.\r\n\r\n"
        "Décoction : Strigiformes -\r\n"
        "Sève d'Arbre dormant : 1\r\n"
        "Hydromel nordique : 1\r\n"
        "Pholiote à écailles : 3\r\n"
        "Mora Tapinella : 4\r\n"
        "Raisin jazbay : 8\r\n\r\n"
        "Décoction : Strigiformes améliorés -\r\n"
        "Décoction : Strigiformes\r\n"
        "Hydromel nordique : 1\r\n"
        "Racine de Nirn : 3\r\n"
        "Tas de sel : 4\r\n"
        "Aile de noctuelle : 6\r\n\r\n"
        "Décoction : Strigiformes supérieurs -\r\n"
        "Décoction : Strigiformes améliorés\r\n"
        "Hydromel nordique : 1\r\n"
        "Racine de Nirn cramoisie : 2\r\n"
        "Champignon luisant : 5\r\n"
        "Huile dwemer : 6\r\n\r\n"
        "Solvant : Hydromel nordique\r\n"
        "[pagebreak]\r\n"
        "Defensores\r\n"
        "Elle insensibilise le buveur à la douleur pour lui offrir une bien meilleure résistance au combat.\r\n\r\n"
        "Décoction : Defensores -\r\n"
        "Sève d'Arbre dormant : 1\r\n"
        "Hydromel Roncenoir : 1\r\n"
        "Tige de chardon : 3\r\n"
        "Coton sauvage : 4\r\n"
        "Queue de ragnard : 6\r\n\r\n"
        "Décoction : Defensores améliorés -\r\n"
        "Décoction : Defensores\r\n"
        "Hydromel d'Hydreliqueur : 1\r\n"
        "Écailles de poisson carnassier : 4\r\n"
        "Aile de noctuelle : 6\r\n"
        "Couronne sanglante : 6\r\n\r\n"
        "Décoction : Defensores supérieurs -\r\n"
        "Décoction : Defensores améliorés\r\n"
        "Réserve Roncenoir : 1\r\n"
        "Cœur de ronces : 3\r\n"
        "Gelée de sautecendres : 4\r\n"
        "Dent de spectre de glace : 4\r\n\r\n"
        "Solvant : Hydromel Roncenoir\r\n"
        "[pagebreak]\r\n"
        "Artisan\r\n"
        "Elle aiguise la concentration et la clarté d'esprit du buveur, lui permettant de se surpasser lors des travaux d'artisanat de longue haleine.\r\n\r\n"
        "Décoction : Artisan -\r\n"
        "Sève d'Arbre dormant : 1\r\n"
        "Hydromel nordique : 1\r\n"
        "Langue de dragon : 6\r\n"
        "Cloquerille : 6\r\n"
        "Givreboises : 8\r\n\r\n"
        "Décoction : Artisan amélioré -\r\n"
        "Décoction : Artisan\r\n"
        "Hydromel aux genièvres : 1\r\n"
        "Sève de spriggan : 3\r\n"
        "Aile de papillon : 5\r\n"
        "Champignon luisant : 6\r\n\r\n"
        "Décoction : Artisan supérieur -\r\n"
        "Décoction : Artisan amélioré\r\n"
        "Hydromel de feu des cendres : 1\r\n"
        "Serre d'harfreuse : 3\r\n"
        "Cendres d'engeance : 4\r\n"
        "Sève de spriggan : 6\r\n\r\n"
        "Solvant : Hydromel nordique\r\n"
        "[pagebreak]\r\n"
        "Rajeunissement\r\n"
        "Meuh Meuh-meuh meuh, meuh meuh meuh meuh\r\n\r\n"
        "Décoction : Rajeunissement -\r\n"
        "Skooma d'Eau-rouge : 1\r\n"
        "Vin épicé : 1\r\n"
        "Plantes grimpantes : 4\r\n"
        "Mycène des marais : 6\r\n"
        "Fleur de montagne violette : 8\r\n\r\n"
        "Décoction : Rajeunissement amélioré -\r\n"
        "Décoction : Rajeunissement\r\n"
        "Vin épicé : 1\r\n"
        "Œuf de fauvette : 4\r\n"
        "Œuf de grive : 4\r\n"
        "Racine noueuse : 5\r\n\r\n"
        "Décoction : Rajeunissement supérieur -\r\n"
        "Décoction : Rajeunissement amélioré\r\n"
        "Vin épicé : 1\r\n"
        "Cœur de ronces : 4\r\n"
        "Gelée de netch : 4\r\n"
        "Œil de smilodon : 6\r\n\r\n"
        "Solvant : Vin épicé\r\n"
    ),
    'zzSkyDecoction2Book3': (
        "[pagebreak]\r\n"
        "<p align=\"center\">\r\n\r\n\r\n"
        "Formules de décoctions supérieures\r\n\r\n\r\n\r\n"
        "</p>\r\n\r\n\r\n\r\n"
        "[pagebreak]\r\n"
        "<p align=\"left\">\r\n"
        "Chat\r\n"
        "Il s'agit d'une décoction perfectionnée qui aiguise considérablement votre discrétion.\r\n\r\n"
        "Décoction : Chat -\r\n"
        "Élixir de sang de Falmer : 1\r\n"
        "Hydromel Roncenoir : 1\r\n"
        "Libellule orange : 4\r\n"
        "Truffe de Namira : 5\r\n"
        "Fleur de montagne violette : 6\r\n\r\n"
        "Décoction : Chat amélioré -\r\n"
        "Décoction : Chat\r\n"
        "Hydromel d'Hydreliqueur : 1\r\n"
        "Racine de trama : 5\r\n"
        "Œuf de grive : 6\r\n"
        "Abécéen à longue nageoire : 6\r\n"
        "Libellule bleue : 8\r\n\r\n"
        "Décoction : Chat supérieur -\r\n"
        "Décoction : Chat amélioré\r\n"
        "Réserve Roncenoir : 1\r\n"
        "Défense de mammouth en poudre : 4\r\n"
        "Plantes grimpantes : 10\r\n"
        "Cosse cendrée : 12\r\n\r\n"
        "Solvant : Hydromel Roncenoir\r\n"
        "[pagebreak]\r\n"
        "Gueule de dragon\r\n"
        "Je ressens une puissance formidable après avoir bu ce breuvage, mais j'ignore comment l'exploiter.\r\n\r\n"
        "Décoction : Gueule de dragon -\r\n"
        "Hydromel du Souffle du dragon : 1\r\n"
        "Mora Tapinella : 3\r\n"
        "Pholiote à écailles : 3\r\n"
        "Langue de dragon : 4\r\n"
        "Coton sauvage : 8\r\n\r\n"
        "Décoction : Gueule de dragon améliorée -\r\n"
        "Décoction : Gueule de dragon\r\n"
        "Hydromel nordique : 1\r\n"
        "Petite perle : 1\r\n"
        "Serre d'harfreuse : 2\r\n"
        "Rayon de miel : 3\r\n"
        "Œufs de saumon : 2\r\n\r\n"
        "Décoction : Gueule de dragon supérieure -\r\n"
        "Décoction : Gueule de dragon améliorée\r\n"
        "Hydromel aux genièvres : 1\r\n"
        "Sels du Néant : 2\r\n"
        "Défense de sanglier : 3\r\n"
        "Voiles éthérés : 3\r\n"
        "Gelée de netch : 4\r\n\r\n"
        "Solvant : Hydromel nordique\r\n"
        "[pagebreak]\r\n"
        "Équipartition\r\n"
        "Une puissante décoction d'abjuration antimagique.\r\n\r\n"
        "Décoction : Équipartition -\r\n"
        "Vin de Jessica : 1\r\n"
        "Coton sauvage : 4\r\n"
        "Œuf de poule : 5\r\n"
        "Hivernelle : 5\r\n"
        "Farine d'os : 6\r\n\r\n"
        "Décoction : Équipartition améliorée -\r\n"
        "Décoction : Équipartition\r\n"
        "Hydromel nordique : 1\r\n"
        "Sels de feu : 3\r\n"
        "Sels de givre : 3\r\n"
        "Sels du Néant : 3\r\n"
        "Poussière luisante : 3\r\n\r\n"
        "Décoction : Équipartition supérieure -\r\n"
        "Décoction : Équipartition améliorée\r\n"
        "Hydromel de feu des cendres : 1\r\n"
        "Gelée de sautecendres : 4\r\n"
        "Cendres d'engeance : 4\r\n"
        "Plumes de sterne de Felsaad : 4\r\n"
        "Brillefleur : 6\r\n\r\n"
        "Solvant : Hydromel nordique\r\n"
        "[pagebreak]\r\n"
        "Hyphalosaure\r\n"
        "Cette décoction enrichit grandement la teneur en oxygène de votre sang lorsque vous êtes immergé.\r\n\r\n"
        "Décoction : Hyphalosaure -\r\n"
        "Bière argonienne : 1\r\n"
        "Grande ramure : 2\r\n"
        "Œuf de poule : 2\r\n"
        "Cosse : 4\r\n"
        "Bernacle nordique : 6\r\n\r\n"
        "Décoction : Hyphalosaure amélioré -\r\n"
        "Décoction : Hyphalosaure\r\n"
        "Bière : 1\r\n"
        "Sève de spriggan : 2\r\n"
        "Chitine de vasard : 3\r\n"
        "Œuf de poisson carnassier : 3\r\n"
        "Œufs de chaurus : 8\r\n\r\n"
        "Décoction : Hyphalosaure supérieur -\r\n"
        "Décoction : Hyphalosaure amélioré\r\n"
        "Vin de sang argonien : 1\r\n"
        "Perle : 2\r\n"
        "Racine de cendres : 4\r\n"
        "Bec de faucon : 4\r\n"
        "Bois de spriggan brûlé : 5\r\n\r\n"
        "Solvant : Bière\r\n"
        "[pagebreak]\r\n"
        "Rosmontis\r\n"
        "Rosmontis est un contrepoison d'une remarquable puissance, dont l'étonnante efficacité est obtenue en neutralisant totalement la toxicité mortelle de la racine de jarrin.\r\n\r\n"
        "Décoction : Rosmontis -\r\n"
        "Racine de jarrin : 1\r\n"
        "Vin : 1\r\n"
        "Tige de chardon : 9\r\n"
        "Cosse : 12\r\n"
        "Ail : 18\r\n\r\n"
        "Décoction : Rosmontis améliorée -\r\n"
        "Décoction : Rosmontis\r\n"
        "Vin épicé : 1\r\n"
        "Peau de ragnard carbonisée : 5\r\n"
        "Oreille de Falmer : 5\r\n"
        "Plumes de faucon : 6\r\n"
        "Chitine de vasard : 12\r\n\r\n"
        "Décoction : Rosmontis supérieure -\r\n"
        "Décoction : Rosmontis améliorée\r\n"
        "Vin des frères Surilie : 1\r\n"
        "Plumes de sterne de Felsaad : 3\r\n"
        "Œuf de poisson carnassier : 4\r\n"
        "Fleur de montagne jaune : 5\r\n"
        "Poussière de vampire : 6\r\n\r\n"
        "Solvant : Vin\r\n"
        "[pagebreak]\r\n"
        "Terminaison\r\n"
        "Une décoction stupéfiante. Les expériences démontrent qu'elle permet au buveur de lancer brièvement des sorts dépassant son propre niveau de maîtrise magique.\r\n\r\n"
        "Décoction : Terminaison -\r\n"
        "Rhum de Stros M'Kai : 1\r\n"
        "Fleur de montagne bleue : 8\r\n"
        "Obscurcine : 4\r\n"
        "Langue de dragon : 5\r\n"
        "Petite ramure : 2\r\n\r\n"
        "Décoction : Terminaison améliorée -\r\n"
        "Décoction : Terminaison\r\n"
        "Vin blanc de marque : 1\r\n"
        "Plumes d'harfreuse : 4\r\n"
        "Sucre de lune : 4\r\n"
        "Poussière luisante : 4\r\n"
        "Huile dwemer : 4\r\n\r\n"
        "Décoction : Terminaison supérieure -\r\n"
        "Décoction : Terminaison améliorée\r\n"
        "Vin blanc de marque : 1\r\n"
        "Aile de noctuelle ancestrale : 2\r\n"
        "Cœur de ronces : 3\r\n"
        "Antennes de chasseur chaurus : 4\r\n"
        "Bois de spriggan brûlé : 4\r\n\r\n"
        "Solvant : Vin blanc de marque\r\n"
        "[pagebreak]\r\n"
        "Testudo\r\n"
        "Son pouvoir magique enveloppe la peau du buveur d'une pellicule protectrice impénétrable.\r\n\r\n"
        "Décoction : Testudo -\r\n"
        "Eau-de-vie cyrodiilienne : 1\r\n"
        "Queue de ragnard : 3\r\n"
        "Chapeau-blanc : 4\r\n"
        "Couronne sanglante : 5\r\n"
        "Tige de chardon : 2\r\n\r\n"
        "Décoction : Testudo améliorée -\r\n"
        "Décoction : Testudo\r\n"
        "Vin : 1\r\n"
        "Perle : 2\r\n"
        "Rayon de miel : 3\r\n"
        "Écailles de poisson carnassier : 4\r\n"
        "Aile de noctuelle : 6\r\n\r\n"
        "Décoction : Testudo supérieure -\r\n"
        "Décoction : Testudo améliorée\r\n"
        "Vin épicé : 1\r\n"
        "Floraison empoisonnée : 3\r\n"
        "Cœur de ronces : 4\r\n"
        "Gelée de sautecendres : 4\r\n"
        "Dent de smilodon : 6\r\n\r\n"
        "Solvant : Vin\r\n"
        "[pagebreak]\r\n\r\n"
        "Tempête\r\n"
        "Cette décoction décuple la puissance musculaire du buveur.\r\n\r\n"
        "Décoction : Tempête -\r\n"
        "Eau-de-vie colovienne : 1\r\n"
        "Racine de canis : 4\r\n"
        "Mousse barbue : 4\r\n"
        "Amanite tue-mouches : 4\r\n"
        "Pholiote à écailles : 8\r\n\r\n"
        "Décoction : Tempête améliorée -\r\n"
        "Décoction : Tempête\r\n"
        "Vin blanc de marque : 1\r\n"
        "Œil de smilodon : 3\r\n"
        "Œuf de fauvette : 4\r\n"
        "Griffes d'ours : 5\r\n"
        "Oreille d'Elfe : 8\r\n\r\n"
        "Décoction : Tempête supérieure -\r\n"
        "Décoction : Tempête améliorée\r\n"
        "Vin épicé : 1\r\n"
        "Orteil de géant : 4\r\n"
        "Petite perle : 5\r\n"
        "Œuf d'araignée : 5\r\n"
        "Mousse de parasol de l'Empereur : 8\r\n\r\n"
        "Solvant : Vin blanc de marque\r\n"
    )
}

DNAM_TRANSLATIONS = {
    # Dragonmaw
    'zxDragonmaw1': "Le délai entre deux cris est réduit de 20 % pendant 60 secondes.\r\n« Ça a le goût d'un sirop contre la toux. »",
    'zxDragonmaw2': "Le délai entre deux cris est réduit de 40 % pendant 60 secondes.\r\n« Ça a le goût d'un sirop contre la toux. »",
    'zxDragonmaw3': "Le délai entre deux cris est réduit de 80 % pendant 60 secondes.\r\n« Ça a le goût d'un sirop contre la toux. »",

    # Hyphalosaurus (Reynos' Fins)
    'zxHyphalosaurus1': "Vous pouvez respirer sous l'eau et nager <mag> % plus vite pendant <dur> secondes.\r\n« Avez-vous déjà vu un lézard avec de longues ouïes ? »",
    'zxHyphalosaurus2': "Vous pouvez respirer sous l'eau et nager <mag> % plus vite pendant <dur> secondes.\r\n« Avez-vous déjà vu un lézard avec de longues ouïes ? »",
    'zxHyphalosaurus3': "Vous pouvez respirer sous l'eau, bénéficiez de la vision nocturne et nagez <mag> % plus vite pendant <dur> secondes.\r\n« Avez-vous déjà vu un lézard avec de longues ouïes ? »",

    # Thunderstorm
    'zxThunderstorm1NT': "Inflige 20 % de dégâts supplémentaires et augmente la vitesse de déplacement de 40 pendant 60 secondes.\r\n« Tel un feu, telle une tempête. »",
    'zxThunderstorm2NT': "Inflige 30 % de dégâts supplémentaires et augmente la vitesse de déplacement de 55 pendant 60 secondes.\r\n« Tel un feu, telle une tempête. »",
    'zxThunderstorm3NT': "Les attaques puissantes ne coûtent aucune vigueur. Inflige 40 % de dégâts supplémentaires et augmente la vitesse de déplacement de 80 pendant 80 secondes.\r\n« Tel un feu, telle une tempête. »",

    # Testudo
    'zxTestudo1': "Le lanceur ignore <100> % de tous les dégâts physiques pendant <dur> secondes.\r\n« Si vous ne pouvez pas saigner, qu'est-ce qui pourrait vous tuer ? »",
    'zxTestudo2': "Le lanceur ignore <100> % de tous les dégâts physiques pendant <dur> secondes.\r\n« Si vous ne pouvez pas saigner, qu'est-ce qui pourrait vous tuer ? »",
    'zxTestudo3': "Le lanceur ignore <100> % de tous les dégâts physiques pendant <dur> secondes.\r\n« Si vous ne pouvez pas saigner, qu'est-ce qui pourrait vous tuer ? »",

    # Termination
    'zxTermination1NT': "Tous les sorts ne coûtent aucune magie pendant 15 secondes.\r\n« C'est mon tour, tas d'asticots. »",
    'zxTermination2NT': "Tous les sorts ne coûtent aucune magie pendant 30 secondes.\r\n« C'est mon tour, tas d'asticots. »",
    'zxTermination3NT': "Tous les sorts ne coûtent aucune magie pendant 60 secondes.\r\n« C'est mon tour, tas d'asticots. »",

    # Equipartition
    'zxEquipartition1': "Toutes les résistances élémentaires sont augmentées de 20 % pendant 60 secondes.\r\n« Équipartition ? NON ! Je veux tout ! »",
    'zxEquipartition2': "Toutes les résistances élémentaires sont augmentées de 40 % pendant 60 secondes.\r\n« Équipartition ? NON ! Je veux tout ! »",
    'zxEquipartition3': "Toutes les résistances élémentaires sont augmentées de 85 % pendant 60 secondes.\r\n« Équipartition ? NON ! Je veux tout ! »",

    # Rosmontis
    'zxRosmontis1': "Guérit du poison et confère une résistance de 100 % au poison pendant 1 200 secondes.\r\n« Le romarin a l'odeur d'une fille aux oreilles de chat blanc qui vous serre fort dans ses bras en vous chuchotant à l'oreille : N'oubliez pas de vous reposer, docteur. »",
    'zxRosmontis2': "Guérit du poison et des maladies. Confère une résistance de 100 % au poison et aux maladies pendant 1 800 secondes.\r\n« Le romarin a l'odeur d'une fille aux oreilles de chat blanc qui vous serre fort dans ses bras en vous chuchotant à l'oreille : N'oubliez pas de vous reposer, docteur. »",
    'zxRosmontis3': "Guérit du poison et des maladies. Confère une résistance de 100 % au poison et aux maladies pendant 3 600 secondes.\r\n« Le romarin a l'odeur d'une fille aux oreilles de chat blanc qui vous serre fort dans ses bras en vous chuchotant à l'oreille : N'oubliez pas de vous reposer, docteur. »",

    # Cat
    'zxCat1': "Le vol à la tire, le crochetage et la discrétion sont 40 % plus faciles pendant 60 secondes.\r\n« Qui vous a dit que cette potion pouvait vous donner la vision nocturne ? »",
    'zxCat2': "Le vol à la tire, le crochetage et la discrétion sont 40 % plus faciles et les attaques à mains nues infligent 20 points de dégâts supplémentaires pendant 60 secondes.\r\n« Qui vous a dit que cette potion pouvait vous donner la vision nocturne ? »",
    'zxCat3': "Le vol à la tire, le crochetage et la discrétion sont 40 % plus faciles, les attaques à mains nues infligent 40 points de dégâts supplémentaires et les dégâts d'attaque furtive avec les armes à une main sont doublés pendant 60 secondes.\r\n« Qui vous a dit que cette potion pouvait vous donner la vision nocturne ? »",

    # Strigiformes
    'zxxStrigiformes1': "Améliore la vision nocturne pendant <dur> secondes.\r\n« Hou-hou-hou... »",
    'zxxStrigiformes2': "Améliore la vision nocturne pendant <dur> secondes.\r\n« Hou-hou-hou... »",
    'zxxStrigiformes3': "Améliore la vision nocturne et permet de se déplacer silencieusement pendant <dur> secondes.\r\n« Hou-hou-hou... »",

    # Prism
    'zzxPrism1': "Rend invisible pendant <dur> secondes.\r\n« Pouvez-vous... me rendre invisible ? »",
    'zzxPrism2': "Rend invisible pendant <dur> secondes.\r\n« Pouvez-vous... me rendre invisible ? »",
    'zzxPrism3': "Rend invisible et permet de se déplacer silencieusement pendant <dur> secondes.\r\n« Pouvez-vous... me rendre invisible ? »",

    # Herculiani
    'zzxHerculiani1': "La santé augmente de 100 points et se régénère 80 % plus vite. La capacité d'emport augmente de 50 points pendant 80 secondes.\r\n« J'ai l'impression de pouvoir mourir douze fois. »",
    'zzxHerculiani2': "La santé augmente de 200 points et se régénère 120 % plus vite. La capacité d'emport augmente de 100 points pendant 100 secondes.\r\n« J'ai l'impression de pouvoir mourir douze fois. »",
    'zzxHerculiani3': "La santé augmente de 400 points et se régénère 180 % plus vite. La capacité d'emport augmente de 200 points pendant 120 secondes.\r\n« J'ai l'impression de pouvoir mourir douze fois. »",

    # Ioviani
    'zzxIoviani1': "La magie augmente de 100 points et se régénère 80 % plus vite. Les sorts sont 30 % plus puissants pendant 80 secondes.\r\n« Un nom étrange, mais puissant. »",
    'zzxIoviani2': "La magie augmente de 200 points et se régénère 120 % plus vite. Les sorts sont 40 % plus puissants pendant 100 secondes.\r\n« Un nom étrange, mais puissant. »",
    'zzxIoviani3': "La magie augmente de 400 points et se régénère 180 % plus vite. Les sorts sont 50 % plus puissants pendant 120 secondes.\r\n« Un nom étrange, mais puissant. »",

    # Exploratores
    'zzxExploratores1': "La vigueur augmente de 100 points et se régénère 80 % plus vite. Permet de marcher sur l'eau pendant 80 secondes.\r\n« Ouvrir une route à chaque montagne, bâtir un pont à chaque cours d'eau. »",
    'zzxExploratores2': "La vigueur augmente de 200 points et se régénère 120 % plus vite. Permet de marcher sur l'eau pendant 100 secondes.\r\n« Ouvrir une route à chaque montagne, bâtir un pont à chaque cours d'eau. »",
    'zzxExploratores3': "La vigueur augmente de 400 points et se régénère 180 % plus vite. Permet de marcher sur l'eau pendant 120 secondes.\r\n« Ouvrir une route à chaque montagne, bâtir un pont à chaque cours d'eau. »",

    # Healer
    'zzzxHealer1': "Rend 100 points de santé en 10 secondes.\r\n« La pierre angulaire de l'alchimie. »",
    'zzzxHealer2': "Rend 250 points de santé en 10 secondes.\r\n« La pierre angulaire de l'alchimie. »",
    'zzzxHealer3': "Rend 500 points de santé en 10 secondes.\r\n« La pierre angulaire de l'alchimie. »",

    # Sober
    'zzzxSober1': "Rend 100 points de magie en 10 secondes.\r\n« Une boisson revigorante. »",
    'zzzxSober2': "Rend 250 points de magie en 10 secondes.\r\n« Une boisson revigorante. »",
    'zzzxSober3': "Rend 500 points de magie en 10 secondes.\r\n« Une boisson revigorante. »",

    # Eucles
    'zzzxEucles1': "Rend 100 points de vigueur en 5 secondes.\r\n« Cette mixture pourrait me faire courir 40 kilomètres. »",
    'zzzxEucles2': "Rend 150 points de vigueur en 5 secondes.\r\n« Cette mixture pourrait me faire courir 40 kilomètres. »",
    'zzzxEucles3': "Rend 300 points de vigueur en 5 secondes.\r\n« Cette mixture pourrait me faire courir 40 kilomètres. »",

    # Rejuvenation
    'zzxRejuvenation1': "Rend 100 points de santé, de magie et de vigueur.\r\n« Surprise~~ »",
    'zzxRejuvenation2': "Rend 300 points de santé, de magie et de vigueur.\r\n« Surprise~~ »",
    'zzxRejuvenation3': "Restaure l'intégralité de la santé, de la magie et de la vigueur.\r\n« Surprise~~ »",

    # Defensores
    'zzxDefensores1': "Augmente la valeur d'armure de 100 points. Le blocage absorbe 25 % de dégâts supplémentaires pendant 300 secondes.\r\n« Les remparts faibliront peut-être un jour ; ces hommes, jamais. »",
    'zzxDefensores2': "Augmente la valeur d'armure de 150 points. Le blocage absorbe 30 % de dégâts supplémentaires pendant 300 secondes.\r\n« Les remparts faibliront peut-être un jour ; ces hommes, jamais. »",
    'zzxDefensores3': "Augmente la valeur d'armure de 200 points. Le blocage absorbe 35 % de dégâts supplémentaires pendant 300 secondes.\r\n« Les remparts faibliront peut-être un jour ; ces hommes, jamais. »",

    # Craftsman
    'zzxCraftsman1': "Les armes et armures peuvent être améliorées avec 30 % d'efficacité supplémentaire. Les enchantements sont 25 % plus puissants. Les prix sont 30 % plus avantageux pendant 600 secondes.\r\n« Attisez la forge, prenez l'acier, nous allons bâtir une armée. »",
    'zzxCraftsman2': "Les armes et armures peuvent être améliorées avec 40 % d'efficacité supplémentaire. Les enchantements sont 30 % plus puissants. Les prix sont 35 % plus avantageux pendant 600 secondes.\r\n« Attisez la forge, prenez l'acier, nous allons bâtir une armée. »",
    'zzxCraftsman3': "Les armes et armures peuvent être améliorées avec 50 % d'efficacité supplémentaire. Les enchantements sont 35 % plus puissants. Les prix sont 40 % plus avantageux pendant 600 secondes.\r\n« Attisez la forge, prenez l'acier, nous allons bâtir une armée. »",
}

# Main MGEF FULL names (effects displayed in active effects menu or spells)
MGEF_FULL_NAMES = {
    'zxDragonmaw1': 'Gueule de dragon',
    'zxDragonmaw2': 'Gueule de dragon',
    'zxDragonmaw3': 'Gueule de dragon',
    'WB_A025_ReynosFins_EffectSwim': 'Nageoires de Reynos - Invisible',
    'zxHyphalosaurus1': 'Nageoires de Reynos',
    'zxHyphalosaurus1Effect': 'Nageoires de Reynos - Invisible',
    'zxHyphalosaurusWB': 'HyphalosaurusWB',
    'zxHyphalosaurusNE': 'Vision nocturne',
    'zxHyphalosaurus2': 'Nageoires de Reynos',
    'zxHyphalosaurus3': 'Nageoires de Reynos',
    'zxThunderstorm1NT': 'Tempête',
    'zxThunderstorm2NT': 'Tempête',
    'zxThunderstorm3NT': 'Tempête',
    'zxTestudo1': 'Testudo',
    'zxTestudo2': 'Testudo',
    'zxTestudo3': 'Testudo',
    'zxTermination1NT': 'Terminaison',
    'zxTermination2NT': 'Terminaison',
    'zxTermination3NT': 'Terminaison',
    'zxEquipartition1': 'Équipartition',
    'zxEquipartition2': 'Équipartition',
    'zxEquipartition3': 'Équipartition',
    'zxRosmontis1': 'Rosmontis',
    'zxRosmontis2': 'Rosmontis',
    'zxRosmontis3': 'Rosmontis',
    'zxCatFS': 'Chat',
    'zxCat1': 'Chat',
    'zxCat2': 'Chat',
    'zxCat3': 'Chat',
    'zxxStrigiformes1': 'Vision nocturne',
    'zxxStrigiformes2': 'Vision nocturne',
    'zxxStrigiformes3': 'Vision nocturne',
    'zxxStrigiformesMU': 'Silence',
    'zzxPrism1': 'Prisme',
    'zzxPrism2': 'Prisme',
    'zzxPrism3': 'Prisme',
    'zzxHerculiani1': 'Herculiani',
    'zzxHerculiani2': 'Herculiani',
    'zzxHerculiani3': 'Herculiani',
    'zzxIoviani1': 'Ioviani',
    'zzxIoviani2': 'Ioviani',
    'zzxIoviani3': 'Ioviani',
    'zzxExploratores1': 'Exploratores',
    'zzxExploratores2': 'Exploratores',
    'zzxExploratores3': 'Exploratores',
    'zzzxHealer1': 'Guérisseur',
    'zzzxHealer2': 'Guérisseur',
    'zzzxHealer3': 'Guérisseur',
    'zzzxSober1': 'Lucidité',
    'zzzxSober2': 'Lucidité',
    'zzzxSober3': 'Lucidité',
    'zzzxEucles1': 'Euclès',
    'zzzxEucles2': 'Euclès',
    'zzzxEucles3': 'Euclès',
    'zzxRejuvenation1': 'Rajeunissement',
    'zzxRejuvenation2': 'Rajeunissement',
    'zzxRejuvenation3': 'Rajeunissement',
    'zzxRejuvenationRS': 'Rajeunissement',
    'zzxRejuvenationRH': 'Rajeunissement',
    'zzxRejuvenationRM': 'Rajeunissement',
    'zzxDefensores1': 'Defensores',
    'zzxDefensores2': 'Defensores',
    'zzxDefensores3': 'Defensores',
    'zzxCraftsman1': 'Artisan',
    'zzxCraftsman2': 'Artisan',
    'zzxCraftsman3': 'Artisan',
}

def translate_entry(it):
    t = it.get('type')
    orig = it.get('original')
    edid = it.get('editor_id')

    # 1. Livres
    if t == 'BOOK FULL':
        if edid == 'zzSkyDecoction2Book':
            return 'Formules de décoctions élémentaires'
        elif edid == 'zzSkyDecoction2Book2':
            return 'Formules de décoctions avancées'
        elif edid == 'zzSkyDecoction2Book3':
            return 'Formules de décoctions supérieures'
    elif t == 'BOOK DESC':
        if edid in BOOK_DESCRIPTIONS:
            return BOOK_DESCRIPTIONS[edid]

    # 2. ALCH FULL (Décoctions)
    elif t == 'ALCH FULL':
        tier = 'base'
        base = orig
        if orig.startswith('Enhanced '):
            tier = 'enhanced'
            base = orig.replace('Enhanced ', '')
        elif orig.startswith('Superior '):
            tier = 'superior'
            base = orig.replace('Superior ', '')
        if base in DECOCTION_NAMES:
            return get_decoction_tier_name(base, tier)

    # 3. MISC FULL (Résidus & Outils)
    elif t == 'MISC FULL':
        if 'Residue' in orig:
            clean = orig.replace(' Residue', '')
            tier = 'base'
            base = clean
            if clean.startswith('Enhanced '):
                tier = 'enhanced'
                base = clean.replace('Enhanced ', '')
            elif clean.startswith('Superior '):
                tier = 'superior'
                base = clean.replace('Superior ', '')
            if base in DECOCTION_NAMES:
                return get_residue_tier_name(base, tier)
        elif edid == 'zzzzzzDecoctionTools':
            return 'Outils de décoction'
        elif edid == 'zz1Canbemade':
            return 'Peut être préparé :'
        elif edid == 'zz1StatisticsDevice':
            return 'Décoctions pouvant être remplies :'
        elif edid == 'zzAlcohol':
            return 'Solvant universel'

    # 4. MGEF DNAM (Descriptions)
    elif t == 'MGEF DNAM':
        if edid in DNAM_TRANSLATIONS:
            return DNAM_TRANSLATIONS[edid]

    # 5. MGEF FULL (Noms des effets magiques)
    elif t == 'MGEF FULL':
        if edid in MGEF_FULL_NAMES:
            return MGEF_FULL_NAMES[edid]
        else:
            # Identifiant interne technique (Thunderstorm1bow, CatFL, etc.)
            return orig

    # 6. Registres spéciaux
    elif t == 'SPEL FULL' and edid == 'WB_A025_ReynosFins_Spell_PC':
        return "Nageoires de Reynos"
    elif t == 'PERK FULL' and edid == 'zzTestudoPerk':
        return "Testudo"
    elif t == 'MESG DESC' and edid == 'zzzzzzDecoctionToolsNoUse':
        return "Vous ne pouvez pas utiliser vos outils de décoction pour le moment."
    elif t == 'CELL FULL' and edid == 'AnisesCabin01':
        return "Cave"
    elif t == 'FLOR FULL' and edid == 'zzSkyDPileofbooks':
        return "Pile de livres"
    elif t == 'FLOR RNAM' and edid == 'zzSkyDPileofbooks':
        return "Prendre"
    elif t == 'FURN FULL' and edid == 'zzzzzzDecoctionTools01':
        return "Outils de décoction"

    raise ValueError(f"Unmapped entry: {t} | {edid} | {orig}")

def apply_translations():
    print(f"Loading {ESP_PATH}...")
    with open(ESP_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Total entries: {len(data)}")
    updated = 0
    for i, it in enumerate(data):
        fr_str = translate_entry(it)
        it['string'] = fr_str
        it['status'] = 'TranslationComplete'
        updated += 1

    print(f"Successfully processed {updated}/{len(data)} entries.")

    with open(ESP_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))

    print("File saved successfully.")

if __name__ == '__main__':
    apply_translations()
