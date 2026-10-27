# -*- coding: utf-8 -*-
"""
Script d'application et validation des traductions manquantes pour :
Citizens of Tamriel (citizenscomplete.esp.json)
"""

import json

JSON_PATH = r"data/user/database/french/Citizens of Tamriel/citizenscomplete.esp.json"

TRANSLATIONS_MAP = {
    ("0500AF99|CitizensComplete.esp", "INFO NAM1", "I like to think that repossessing these things makes life more interesting. Well... for me, at least. "):
        "J'aime à penser que récupérer ces bricoles rend la vie plus intéressante. Enfin... pour moi, en tout cas. ",

    ("05015838|CitizensComplete.esp", "INFO NAM1", "How boring. They should listen Paarthurnax and take to meditating, the World-Eater can wait. "):
        "Comme c'est assommant. Ils devraient écouter Paarthurnax et se mettre à méditer, le Dévoreur de mondes peut bien attendre. ",

    ("0500DB14|CitizensComplete.esp", "INFO NAM1", "Wonderful! Let me just get your premium items out and the crate all ready for you to open. "):
        "Merveilleux ! Laissez-moi sortir vos articles de premier choix et préparer votre caisse, prête à être ouverte. ",

    ("0500E5F4|CitizensComplete.esp", "INFO NAM1", "Nonsense, you're very welcome here so long as you stay out of trouble! "):
        "Allons donc, vous êtes ici chez vous tant que vous ne cherchez pas d'ennuis ! ",

    ("0502E154|CitizensComplete.esp", "INFO NAM1", "10,453,561... 10,453,562... 10,453,563..."):
        "10 453 561... 10 453 562... 10 453 563...",

    ("050048F4|CitizensComplete.esp", "INFO NAM1", "What the-- what are you doing?! Look, stranger, I don't have any Septims but, uh... I suppose you're welcome to some fish? "):
        "Mais qu'est-ce que... qu'est-ce que vous faites ?! Écoutez, l'ami, j'ai pas un seul septim mais, euh... un peu de poisson, ça vous dirait ? ",

    ("051C382C|CitizensComplete.esp", "INFO NAM1", "Argh... but you didn't come to listen to a sermon from a fool like me, did you? "):
        "Argh... mais vous n'êtes pas venu écouter le sermon d'un vieil imbécile comme moi, n'est-ce pas ? ",

    ("0500B502|CitizensComplete.esp", "INFO NAM1", "*laughs* You don't need to say anything, the silence is your answer. "):
        "(rires) Pas la peine de dire quoi que ce soit, votre silence me suffit amplement. ",

    ("05005423|CitizensComplete.esp", "INFO NAM1", "She plays her cards even more close to her chest than I do, but don't mistake her reservedness for passivity: she's more deadly than she appears. "):
        "Elle cache encore mieux son jeu que moi, mais ne prenez pas sa réserve pour de la passivité : elle est bien plus redoutable qu'il n'y paraît. ",

    ("05008ABD|CitizensComplete.esp", "INFO NAM1", "I am from a small farming family in the southern Heartlands, not poor or rich but nowhere of note. "):
        "Je viens d'une petite famille d'agriculteurs du sud des Terres centrales. Ni pauvres, ni riches, et rien de remarquable. ",

    ("0500C1C6|CitizensComplete.esp", "INFO NAM1", "My lady, I am Florian de Gabb: Bard extraordinaire and purveyor of finery, no matter its form. "):
        "Ma dame, je suis Florian de Gabb : barde extraordinaire et pourvoyeur d'élégance, sous toutes ses formes. ",

    ("050173B8|CitizensComplete.esp", "INFO NAM1", "Where was the blood-starved lunatic that had committed acts beyond description and cast a shadow on our beautiful Hold? "):
        "Où était donc passé cet aliéné assoiffé de sang qui avait perpétré l'innommable et jeté une ombre funeste sur notre belle châtellenie ? ",

    ("050ACC38|CitizensComplete.esp", "INFO NAM1", "Oh, if only they knew... "):
        "Oh, si seulement ils savaient... ",

    ("0500A65D|CitizensComplete.esp", "INFO NAM1", "Wh-- what have you done to me? "):
        "Qu... qu'est-ce que vous m'avez fait ? ",

    ("050059A3|CitizensComplete.esp", "INFO NAM1", "Two swords: one from my side and the other taken from my brother's saddlebags. "):
        "Deux épées : une à mon côté, et l'autre tirée des fontes de selle de mon frère. ",

    ("0500490C|CitizensComplete.esp", "INFO NAM1", "I'm quite the chef, I'll have you know... "):
        "Je suis un sacré cuisinier, sachez-le... ",

    ("0500A661|CitizensComplete.esp", "INFO NAM1", "You weren't up at the Pass? The fools tried to ambush us, in our own territory no less! "):
        "Vous n'étiez pas là-haut au col ? Ces crétins ont tenté de nous tendre une embuscade, et sur notre propre territoire en plus ! ",

    ("05007FBF|CitizensComplete.esp", "INFO NAM1", "What if someone... or... or something... is controlling us this whole time? "):
        "Et si quelqu'un... ou... ou quelque chose... nous contrôlait depuis le tout début ? ",

    ("05008AD0|CitizensComplete.esp", "INFO NAM1", "Look not at each other or the blade within a hand, "):
        "Ne portez vos regards ni sur l'autre ni sur la lame au creux de la main, ",

    ("0501379C|CitizensComplete.esp", "INFO NAM1", "The woman and I ended up back to back, the group of mages almost having exhausted their Magicka reserves. "):
        "Cette femme et moi nous sommes retrouvés dos à dos, le groupe de mages ayant presque épuisé toutes ses réserves de magie. ",

    ("050074E7|CitizensComplete.esp", "INFO NAM1", "They say ol' Olmir can't defeat a glass of milk, but nothing gets a warrior pumping then a nip in the snow and a pint of the good stuff!  "):
        "On raconte que le père Olmir ne viendrait pas à bout d'un verre de lait, mais rien ne requinque un guerrier comme une bonne bourrasque dans la neige et une pinte de la meilleure cuvée ! ",

    ("0500CAAB|CitizensComplete.esp", "INFO NAM1", "There, there... it's not stealing, it's repossession of communal property! Your buddies won't need any of this in Sovngarde, after all. "):
        "Là, là... c'est pas du vol, c'est de la réquisition de bien public ! Vos copains n'auront plus besoin de tout ça en Sovngarde, après tout. ",

    ("0500A9FB|CitizensComplete.esp", "INFO NAM1", "I should hope not, considering the way all of them threw themselves before the cult. All the preaching and the shouting and the dragonfire... "):
        "J'espère bien que non, vu la façon dont ils se sont tous prosternés devant le culte. Tous ces sermons, ces vociférations et ce feu draconique... ",

    ("0501069D|CitizensComplete.esp", "INFO NAM1", "You fear the end of the Empire because it's all you know, but do not throw everything away for petty freedoms. "):
        "Vous craignez la chute de l'Empire parce que c'est tout ce que vous avez connu, mais ne jetez pas tout par la fenêtre pour de dérisoires libertés. ",

    ("05018445|CitizensComplete.esp", "INFO NAM1", "I laughed until I could barely breathe. He was white with embarrassment and I walked away with a small fortune before we even got the chance. "):
        "J'ai ri à en perdre le souffle. Il était blême de honte et je suis reparti avec une petite fortune avant même qu'on en ait l'occasion. ",

    ("0500B504|CitizensComplete.esp", "INFO NAM1", "Soon enough, someone else will be poking around in our ribcage. Hopefully not a troll or Skeevers. "):
        "D'ici peu, quelqu'un d'autre viendra farfouiller dans notre cage thoracique. En espérant que ce ne soit ni un troll ni des ragnards. ",

    ("0500DAFF|CitizensComplete.esp", "INFO NAM1", "All you need to do is hand across a small payment of 1,000 Septims and the very utmost bestest goods shall be yours! "):
        "Tout ce que vous avez à faire, c'est me verser la modique somme de 1 000 septims, et les marchandiiiiises les plus fabuleuses seront à vous ! ",
}

def run():
    print(f"Loading {JSON_PATH}...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    applied_count = 0
    matched_keys = set()
    for entry in data:
        key = (entry.get("form_id"), entry.get("type"), entry.get("original"))
        if key in TRANSLATIONS_MAP:
            new_text = TRANSLATIONS_MAP[key]
            entry["string"] = new_text
            entry["status"] = "TranslationComplete"
            applied_count += 1
            matched_keys.add(key)

    print(f"Applied {applied_count}/{len(TRANSLATIONS_MAP)} translations.")
    if applied_count != len(TRANSLATIONS_MAP):
        missing = set(TRANSLATIONS_MAP.keys()) - matched_keys
        print("Missing keys:", missing)
        raise ValueError(f"Mismatch: expected {len(TRANSLATIONS_MAP)} applications, got {applied_count}")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=None, separators=(',', ':'))

    print(f"Successfully saved {JSON_PATH} with compact JSON format.")

if __name__ == "__main__":
    run()
