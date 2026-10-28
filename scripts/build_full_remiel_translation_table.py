import json
import re

with open("remiel_to_translate.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Static specific lines
direct_translations = {
    # Non-companion lines / specific lore lines
    "A few months after I joined. It wasn't one big incident that made me decide to leave; I just gradually stopped showing up.":
        "Quelques mois après avoir rejoint la guilde. Ce n'est pas un incident particulier qui m'a décidée à partir ; j'ai juste fini par ne plus m'y présenter, petit à petit.",
    "...Uh, I should clarify that the irony in my statement was unintentional.":
        "... Euh, je devrais préciser que l'ironie dans mes propos était involontaire.",
    "Here it is... I... I can barely believe we're here...":
        "Nous y voilà... Je... j'arrive à peine à croire que nous y sommes...",
    "No. I carry a sword. I'm from the swamps of Black Marsh. Do you need me to continue, or can you piece it together from here?":
        "Non. Je porte une épée. Je viens des marécages du Marais noir. Vous voulez que je continue, ou vous avez compris l'idée ?",
    "Maybe one day he'll be better at protecting me than you are?":
        "Peut-être qu'un jour il saura mieux me protéger que vous ?",
    "I've always felt the Forsworn were no better than Witchmen. Ever since Cidhna Mine, I've felt vindicated in that belief.":
        "J'ai toujours pensé que les Parjures ne valaient pas mieux que les sorciers. Depuis la mine de Cidhna, j'ai le sentiment d'avoir eu raison d'y croire.",
    "Are you very familiar with thieves, Yazakh?":
        "Vous connaissez bien les voleurs, Yazakh ?",
    "Ha-Ha. Do you have any more bad jokes? Because then I'd be out of a job.":
        "Ha-ha. Vous avez d'autres blagues nulles ? Parce que sinon je vais me retrouver au chômage.",
    "When it comes to mistakes, I understand. It doesn't really matter. We're still a company of fighters.":
        "Quand il s'agit d'erreurs, je comprends. Ça n'a pas vraiment d'importance. Nous restons une compagnie de combattants.",
    
    # Gildergreen commentary
    "I quite like the spooky dead tree near the Companions' guildhall. Although it doesn't quite fit the vision I have of Whiterun.":
        "J'aime plutôt bien ce vieil arbre mort sinistre près du sanctuaire des Compagnons. Même si ça ne colle pas tout à fait à l'image que j'avais de Blancherive.",
    "So did this hagraven forge Nettlebane? I can't imagine a hagraven near a forge. Their feathers would catch fire, I think.":
        "Alors, c'est cette harfreuse qui a forgé Fléau d'ortie ? J'ai du mal à imaginer une harfreuse près d'une forge. Leurs plumes prendraient feu, je pense.",
    "They really were sacrificing spriggans here. I'm not sure I'll ever understand hagravens' pastimes.":
        "Ils sacrifiaient vraiment des spriggans ici. Je ne suis pas sûre de comprendre un jour les passe-temps des harfreuses.",
    "They really were sacrificing spriggans here. I'm not sure I'll ever understand hagravens' pastimes. ":
        "Ils sacrifiaient vraiment des spriggans ici. Je ne suis pas sûre de comprendre un jour les passe-temps des harfreuses.",
    "I've been resisting saying this, but what is the point of reviving the Gildergreen? Just to attract pilgrims? Is the Temple not pretty enough?":
        "Je me retenais de le dire, mais quel est l'intérêt de ranimer Végétalia ? Juste pour attirer des pèlerins ? Le Temple n'est pas déjà assez joli comme ça ?",
    "This place is much prettier than the Temple! Perhaps they should just have pilgrims come here. Although it seems there's already some milling about.":
        "Cet endroit est bien plus joli que le Temple ! Peut-être qu'ils devraient juste faire venir les pèlerins ici. Même s'il semble y en avoir déjà qui traînent dans le coin.",
    "'A woman of violence,' he says. This is a tree, not his kin.":
        "« Une femme de violence », qu'il dit. C'est un arbre, pas sa propre famille.",
    "'A man of violence,' he says. This is a tree, not his kin.":
        "« Un homme de violence », qu'il dit. C'est un arbre, pas sa propre famille.",
    "Oh, the little new Gildergreen is... really great... It really was worth all the effort...":
        "Oh, le nouveau petit Végétalia est... vraiment génial... Ça valait vraiment toute cette peine...",
    "Well, let's let Danica know pilgrims will be running to Whiterun from all across Nirn. Do they pay her to look at the tree? I think I'm confused.":
        "Eh bien, allons prévenir Danica que les pèlerins vont affluer à Blancherive depuis tout Nirn. Est-ce qu'ils la paient pour regarder l'arbre ? Je crois que je suis un peu perdue.",
    "I will miss the spooky centerpiece to Whiterun, but I suppose an alive tree looks... nice enough.":
        "Cet ornement sinistre au centre de Blancherive va me manquer, mais je suppose qu'un arbre vivant est... assez joli.",
    "And where are they going to put the old Gildergreen? Are they going to chop it down? Do you suppose its wood holds any unique properties? Hm.":
        "Et où vont-ils mettre l'ancien Végétalia ? Vont-ils le débiter ? Pensez-vous que son bois possède des propriétés uniques ? Hm.",

    # Specific quirky lines
    "Doctor, are you okay? Knowing your name references a medic, it feels odd for me to be checking your wellbeing.":
        "Docteur, vous allez bien ? Sachant que votre nom évoque un médecin, c'est bizarre que ce soit moi qui m'inquiète de votre santé.",
    "Ilia, you are inhuman. And inmer. Is that a word? Well, you understand.":
        "Ilia, vous êtes inhumaine. Et inmer. Est-ce que ça existe comme mot ? Enfin, vous voyez ce que je veux dire.",
    "Buffy and Remi, an unstoppable killing team! That sounds bad, doesn't it? Oh well.":
        "Buffy et Remi, une équipe de choc impitoyable ! Ça sonne un peu violent, non ? Tant pis.",
    "Okay, Nar. If you could stop leading us into danger, I'd- Well, I'd be a hyprocrite to say that, so never mind.":
        "D'accord, Nar. Si vous pouviez arrêter de nous mener vers le danger, je... enfin, je serais bien hypocrite de dire ça, alors laissez tomber.",
    "I'm here, Joshua. If not in mind, at least in body. But I'll try to keep my mind here for you, too.":
        "Je suis là, Joshua. Si ce n'est en esprit, au moins en corps. Mais je vais essayer de garder mon esprit ici pour vous aussi.",
    "You know you don't need to try to kill Doctor? Or me?":
        "Vous savez que vous n'êtes pas obligés de tuer le Docteur ? Ni moi d'ailleurs ?",
    "You don't have to worry, Ilia. I'll keep up. Probably.":
        "Ne vous inquiétez pas, Ilia, je vais suivre le rythme. Probablement.",
    "We're done talking, then, Farillae?":
        "On a fini de parler, alors, Farillae ?",
    "Alright, Mortu, then we'll talk later.":
        "D'accord, Mortu, on se parlera plus tard alors.",
    
    # Specific perks & quest
    "Scrap's Extra Damage 1.5": "Dégâts supplémentaires de Ferraille (x1,5)",
    "Scrap's Extra Damage 2": "Dégâts supplémentaires de Ferraille (x2)",
    "Tamriel's Tastiest Stew": "Le ragoût le plus savoureux de Tamriel"
}

# Regex pattern transformers
patterns = [
    # Greetings / Needs / Banter
    (r"^Hello, (.+)\. What did you need\?$", lambda m: f"Bonjour, {m.group(1)}. De quoi aviez-vous besoin ?"),
    (r"^What did you need, (.+)\?$", lambda m: f"De quoi aviez-vous besoin, {m.group(1)} ?"),
    (r"^Did you need something, (.+)\?$", lambda m: f"Vous aviez besoin de quelque chose, {m.group(1)} ?"),
    (r"^Hi,?[ ]*(.+)\. Were you doing to ask me something\?$", lambda m: f"Salut {m.group(1)}. Vous alliez me demander quelque chose ?"),
    (r"^Perfect timing, (.+)\. Do you have any snacks\?$", lambda m: f"Tombe à pic, {m.group(1)}. Vous n'auriez pas un en-cas ?"),
    (r"^Oh, (.+), you're here! Perfect! Oh- Did you need something before I start asking questions\?$", lambda m: f"Oh, {m.group(1)}, vous êtes là ! Parfait ! Oh... vous aviez besoin de quelque chose avant que je commence à poser des questions ?"),
    (r"^Oh, good, you're here, (.+)!$", lambda m: f"Oh, super, vous êtes là, {m.group(1)} !"),
    (r"^Scrap says 'hello,' (.+)\.$", lambda m: f"Ferraille vous dit bonjour, {m.group(1)}."),
    (r"^(.+), Scrap is shy, but you should know he likes you\.$", lambda m: f"{m.group(1)}, Ferraille est timide, mais vous devez savoir qu'il vous aime bien."),
    (r"^(.+), you are a bit scary in battle\. Well, everything is scary in battle\. Am I scary in battle\?$", lambda m: f"{m.group(1)}, vous faites un peu peur au combat. Enfin, tout fait peur au combat. Est-ce que je fais peur au combat, moi ?"),

    # Moving / Leading
    (r"^Time to head out, (.+)\?$", lambda m: f"C'est l'heure de partir, {m.group(1)} ?"),
    (r"^Are we heading out, (.+)\?$", lambda m: f"On y va, {m.group(1)} ?"),
    (r"^Are we heading out, (.+)\? Let me know if we are\. I don't want to get left behind\.$", lambda m: f"On se met en route, {m.group(1)} ? Dites-le-moi si c'est le cas, je ne veux pas être laissée derrière."),
    (r"^So we're off,?[ ]*then,?[ ]*(.+)\? Lead the way\.$", lambda m: f"On est partis alors, {m.group(1)} ? Montrez le chemin."),
    (r"^Lead the way, (.+)\.$", lambda m: f"Montrez le chemin, {m.group(1)}."),
    (r"^Off we go, (.+)\.$", lambda m: f"C'est parti, {m.group(1)}."),
    (r"^Okay, (.+), lead the way!$", lambda m: f"D'accord, {m.group(1)}, montrez la voie !"),
    (r"^Alright, (.+), lead the way!$", lambda m: f"Très bien, {m.group(1)}, montrez la voie !"),
    (r"^I'm right behind you, (.+)\.$", lambda m: f"Je vous suis de près, {m.group(1)}."),
    (r"^I'll be right behind you, (.+)\.$", lambda m: f"Je vous suis de près, {m.group(1)}."),
    (r"^I'll just stick close to you, (.+)\.$", lambda m: f"Je vais juste rester près de vous, {m.group(1)}."),
    (r"^I'll admit, I forgot where we were going next\. I'll just stick close to you, (.+)\.$", lambda m: f"J'avoue que j'ai oublié où nous allions ensuite. Je vais juste rester près de vous, {m.group(1)}."),
    (r"^You don't have to worry, (.+), I'll keep up\. Probably\.$", lambda m: f"Ne vous inquiétez pas, {m.group(1)}, je vais suivre le rythme. Probablement."),
    (r"^Take us somewhere fun, (.+)!$", lambda m: f"Emmenez-nous dans un endroit sympa, {m.group(1)} !"),
    (r"^I'll be here, (.+)\. And also wherever you take me next\.$", lambda m: f"Je serai là, {m.group(1)}. Et partout où vous m'emmènerez ensuite."),
    (r"^Alright, Scrap, let's go\. (.+) is leading us somewhere fun, right\?$", lambda m: f"Très bien, Ferraille, on y va. {m.group(1)} nous emmène dans un endroit sympa, pas vrai ?"),
    (r"^(.+), you are very good at leading\. At least, I think you are\. I'm following you, in any case\.$", lambda m: f"{m.group(1)}, vous vous débrouillez très bien pour nous guider. Enfin, je crois. En tout cas, je vous suis."),
    (r"^Where are we headed next, (.+)\?$", lambda m: f"Où va-t-on maintenant, {m.group(1)} ?"),
    (r"^Alright, (.+), then off we go!$", lambda m: f"Très bien, {m.group(1)}, c'est parti !"),

    # Parting / Waiting
    (r"^Alright, (.+), we'll talk later\.$", lambda m: f"D'accord, {m.group(1)}, on se parlera plus tard."),
    (r"^Okay, (.+), we'll talk later\.$", lambda m: f"D'accord, {m.group(1)}, on se parlera plus tard."),
    (r"^Then we'll talk later, (.+)\.$", lambda m: f"On se reparlera plus tard, alors, {m.group(1)}."),
    (r"^We'll talk later, then, (.+)\?$", lambda m: f"On reparlera plus tard, alors, {m.group(1)} ?"),
    (r"^We'll talk some more later, then, (.+)\.$", lambda m: f"On reparlera un peu plus tard, alors, {m.group(1)}."),
    (r"^Well,?[ ]*bye,?[ ]*(.+)\. Bye for now, at least\.$", lambda m: f"Eh bien, au revoir, {m.group(1)}. Du moins pour l'instant."),
    (r"^See you later, (.+)\.$", lambda m: f"À plus tard, {m.group(1)}."),
    (r"^I'll be here, (.+)\.$", lambda m: f"Je serai là, {m.group(1)}."),
    (r"^If you leave me here too long, (.+), I will take no responsibility for the outcome\.$", lambda m: f"Si vous me laissez ici trop longtemps, {m.group(1)}, je décline toute responsabilité pour ce qui pourrait arriver."),
    (r"^Don't leave me here too long, (.+)\. You know I'll get bored and do something we both regret\.$", lambda m: f"Ne me laissez pas ici trop longtemps, {m.group(1)}. Vous savez que je vais m'ennuyer et faire une bêtise que nous regretterons tous les deux."),
    (r"^(.+), don't just leave me here forever\. I'll miss you\.$", lambda m: f"{m.group(1)}, ne me laissez pas ici pour toujours. Vous allez me manquer."),
    (r"^(.+)\. (.+),? look at me\. Do not forget I am standing here\. Don't forget me, (.+)\. *$", lambda m: f"{m.group(1)}. {m.group(2)}, regardez-moi. N'oubliez pas que je suis là. Ne m'oubliez pas, {m.group(3)}."),
    (r"^(.+)\. (.+)\. Look at me\. Do not forget me here\. (.+), I will be so sad\. Do not forget me\.$", lambda m: f"{m.group(1)}. {m.group(2)}. Regardez-moi. Ne m'oubliez pas ici. {m.group(3)}, je serais si triste. Ne m'oubliez pas."),
    (r"^(.+), please don't forget I'm standing here\. I'm serious, (.+)\. Don't forget me\.$", lambda m: f"{m.group(1)}, ne m'oubliez pas ici, s'il vous plaît. Je suis très sérieuse, {m.group(2)}. Ne m'oubliez pas."),
    (r"^We're done talking,?[ ]*(.+)\? Sometimes it's hard for me to tell\.$", lambda m: f"On a fini de parler, {m.group(1)} ? J'ai parfois du mal à le savoir."),
    (r"^Are we done talking,?[ ]*(.+)\? Sometimes it's hard for me to tell\.$", lambda m: f"On a fini de parler, {m.group(1)} ? J'ai parfois du mal à le savoir."),
    (r"^We're done talking then, (.+)\?$", lambda m: f"Notre conversation est terminée alors, {m.group(1)} ?"),
    (r"^Alright, now that we're done talking- Wait, (.+), we were done talking, right\? Sometimes it's hard for me to tell\.$", lambda m: f"Très bien, maintenant qu'on a fini de parler... Attendez, {m.group(1)}, on avait fini de parler, n'est-ce pas ? J'ai parfois du mal à le savoir."),
    (r"^And (.+)- Oh, you're walking away\.$", lambda m: f"Et {m.group(1)}... Oh, vous vous en allez."),
    (r"^Oh, and (.+)- Oh, you're walking away\. Were we done talking\?$", lambda m: f"Oh, et {m.group(1)}... Oh, vous vous en allez. Notre conversation était terminée ?"),
    (r"^And I was also thinking- Oh\. (.+), you're walking away\. Oh, were we done talking\? Oops\.$", lambda m: f"Et je pensais aussi à... Oh. {m.group(1)}, vous vous en allez. Oh, on avait fini de parler ? Oups."),
    (r"^(.+), before you go- Oh, you're already leaving\. Never mind\.$", lambda m: f"{m.group(1)}, avant que vous ne partiez... Oh, vous vous en allez déjà. Laissez tomber."),
    (r"^Oh, but (.+), I still wanted to tell you- Er\. I- I forgot\. Never mind\.$", lambda m: f"Oh, mais {m.group(1)}, je voulais encore vous dire... Euh... J'ai... j'ai oublié. Laissez tomber."),
    (r"^Okay, (.+), back to- What were we doing\? Don't tell me; I'll remember eventually\.$", lambda m: f"D'accord, {m.group(1)}, revenons à... Qu'est-ce qu'on faisait déjà ? Ne me dites rien, ça va me revenir."),
    (r"^Back to it\. Er\.\.\. (.+), what were we doing again\? I'll just follow you\.$", lambda m: f"Revenons-y. Euh... {m.group(1)}, qu'est-ce qu'on faisait déjà ? Je vais juste vous suivre."),
    (r"^Okay, (.+), back to- What were we doing\? Hm\.$", lambda m: f"D'accord, {m.group(1)}, revenons à... Qu'est-ce qu'on faisait ? Hm."),
    (r"^Okay, (.+), let me just remember what I was doing before talking to you\.$", lambda m: f"D'accord, {m.group(1)}, laissez-moi juste me rappeler ce que je faisais avant de vous parler."),
    (r"^Okay, (.+), then I will see you\.\.\. Well, I'll still \*see\* you, we just won't be talking\. I will \*talk\* to you later\.$", lambda m: f"D'accord, {m.group(1)}, alors on se verra... Enfin, je vais toujours vous *voir*, mais on ne se parlera pas. On se *reparlera* plus tard."),

    # Combat alerts
    (r"^Look out, (.+)! Someone wants to kill us!$", lambda m: f"Attention, {m.group(1)} ! Quelqu'un veut notre mort !"),
    (r"^Look out, (.+)! Something wants us dead!$", lambda m: f"Attention, {m.group(1)} ! Quelque chose veut notre mort !"),
    (r"^Look out, (.+)! Something is trying to kill us!$", lambda m: f"Attention, {m.group(1)} ! Quelque chose essaie de nous tuer !"),
    (r"^Ah! (.+), look out! We're being attacked!$", lambda m: f"Ah ! {m.group(1)}, attention ! On nous attaque !"),
    (r"^Ah! (.+), we seem to be under attack!$", lambda m: f"Ah ! {m.group(1)}, on dirait qu'on nous attaque !"),
    (r"^Ah! (.+)! Something is attacking us!$", lambda m: f"Ah ! {m.group(1)} ! Quelque chose nous attaque !"),
    (r"^Ah! (.+), something is attacking us! Again!$", lambda m: f"Ah ! {m.group(1)}, quelque chose nous attaque ! Encore !"),
    (r"^Um, (.+), I think we're being attacked!$", lambda m: f"Euh, {m.group(1)}, je crois qu'on nous attaque !"),
    (r"^(.+), something is trying to kill us again!$", lambda m: f"{m.group(1)}, quelque chose essaie encore de nous tuer !"),
    (r"^(.+), I think something is trying to kill us!$", lambda m: f"{m.group(1)}, je crois que quelque chose essaie de nous tuer !"),
    (r"^Oh no, oh no[!\.] (.+)! (.+)! Something is trying to kill us!$", lambda m: f"Oh non, oh non ! {m.group(1)} ! {m.group(2)} ! Quelque chose essaie de nous tuer !"),
    (r"^Is something- (.+), did you hear that\?$", lambda m: f"Il y a quelque... {m.group(1)}, vous avez entendu ça ?"),
    (r"^What was- (.+), did you hear something\?$", lambda m: f"C'était quoi... {m.group(1)}, vous avez entendu quelque chose ?"),
    (r"^(.+), shh\. I think I heard something\.$", lambda m: f"{m.group(1)}, chut... Je crois que j'ai entendu quelque chose."),

    # During combat
    (r"^Scrap, keep (.+) safe,?[ ]*okay\?!$", lambda m: f"Ferraille, protège {m.group(1)}, d'accord ?!"),
    (r"^Scrap, keep (.+) safe,?[ ]*okay\?$", lambda m: f"Ferraille, protège {m.group(1)}, d'accord ?"),
    (r"^Scrap, keep (.+) safe!$", lambda m: f"Ferraille, protège {m.group(1)} !"),
    (r"^Please be careful, (.+)!$", lambda m: f"Faites attention, {m.group(1)} !"),
    (r"^Oh, (.+), please be careful!$", lambda m: f"Oh, {m.group(1)}, soyez prudent(e) s'il vous plaît !"),
    (r"^(.+), please be careful!$", lambda m: f"{m.group(1)}, soyez prudent(e) s'il vous plaît !"),
    (r"^Don't die, (.+)! I'd be very upset with you!$", lambda m: f"Ne mourez pas, {m.group(1)} ! Je vous en voudrais beaucoup !"),
    (r"^Don't die, (.+)! I'll be very upset with you!$", lambda m: f"Ne mourez pas, {m.group(1)} ! Je vous en voudrais beaucoup !"),
    (r"^(.+), if you could kill them now, I'd appreciate it!$", lambda m: f"{m.group(1)}, si vous pouviez les tuer maintenant, j'apprécierais beaucoup !"),
    (r"^(.+), if you could kill them now, I'd really appreciate it!$", lambda m: f"{m.group(1)}, si vous pouviez les tuer maintenant, j'apprécierais vraiment !"),
    (r"^Keep it up, (.+)!$", lambda m: f"Continuez comme ça, {m.group(1)} !"),
    (r"^Okay, (.+)! We can do this!$", lambda m: f"D'accord, {m.group(1)} ! On peut le faire !"),
    (r"^Okay, (.+)! We can do this! They don't stand a chance! Right\?$", lambda m: f"D'accord, {m.group(1)} ! On peut y arriver ! Ils n'ont aucune chance, pas vrai ?"),
    (r"^We can do this, (.+)! Probably!$", lambda m: f"On peut le faire, {m.group(1)} ! Probablement !"),
    (r"^Do\. Not\. Hit\. (.+)!$", lambda m: f"Ne. Touchez. Pas. À {m.group(1)} !"),
    (r"^No, no, no! Do not attack (.+)! Do not attack me!$", lambda m: f"Non, non, non ! N'attaquez pas {m.group(1)} ! Ne m'attaquez pas !"),
    (r"^Ah! (.+)! Don't let me die! Wait, don't let you die!$", lambda m: f"Ah ! {m.group(1)} ! Ne me laissez pas mourir ! Enfin, ne mourez pas non plus !"),
    (r"^Ah! Fighting again! Don't let me die, (.+)! Don't let you die!$", lambda m: f"Ah ! Encore un combat ! Ne me laissez pas mourir, {m.group(1)} ! Ne mourez pas non plus !"),
    (r"^Ah! So much fighting! I'll just stay behind you, (.+)!$", lambda m: f"Ah ! Tant de violence ! Je vais juste rester derrière vous, {m.group(1)} !"),
    (r"^Ah! Fighting again! I'll just try to stay near you, (.+)!$", lambda m: f"Ah ! Encore une bagarre ! Je vais juste essayer de rester près de vous, {m.group(1)} !"),
    (r"^We are going to live, (.+)! Right\?$", lambda m: f"On va s'en sortir vivants, {m.group(1)} ! Pas vrai ?"),
    (r"^We won't die! At least, I don't think (.+) will let us die! So there!$", lambda m: f"On ne va pas mourir ! Enfin, je ne pense pas que {m.group(1)} va nous laisser mourir ! Alors voilà !"),
    (r"^(.+), why does everything want to kill us\?!$", lambda m: f"{m.group(1)}, pourquoi tout le monde cherche à nous tuer ?!"),
    (r"^(.+), what do we do that makes everything want us dead\?!$", lambda m: f"{m.group(1)}, qu'est-ce qu'on a fait pour que tout le monde veuille notre mort ?!"),
    (r"^(.+), what did we do to make everything want to kill us\?!$", lambda m: f"{m.group(1)}, qu'est-ce qu'on a fait pour que tout le monde cherche à nous tuer ?!"),
    (r"^(.+), if you don't die, then I won't die! Deal\?$", lambda m: f"{m.group(1)}, si vous ne mourez pas, alors je ne meurs pas non plus ! Marché conclu ?"),
    (r"^Okay, (.+), let's neither of us die!$", lambda m: f"D'accord, {m.group(1)}, ne mourons ni l'un ni l'autre !"),
    (r"^Just a little longer, (.+)! Stay alive a little longer!$", lambda m: f"Encore un petit effort, {m.group(1)} ! Restez en vie encore un instant !"),
    (r"^We just have to hold out a bit longer, (.+)!$", lambda m: f"On doit juste tenir encore un petit peu, {m.group(1)} !"),
    (r"^Are you doing okay out there, (.+)\?$", lambda m: f"Vous tenez le coup, {m.group(1)} ?"),
    (r"^Are you doing okay out there, (.+)\?!$", lambda m: f"Vous tenez le coup là-bas, {m.group(1)} ?!"),
    (r"^Are you doing okay, (.+)\?! Enough blood in your body still\?$", lambda m: f"Vous vous en sortez, {m.group(1)} ?! Il vous reste assez de sang dans le corps ?"),
    (r"^How are you faring, (.+)\?!$", lambda m: f"Comment vous vous en sortez, {m.group(1)} ?!"),
    (r"^How are you faring, (.+)\?! I'm getting tired!$", lambda m: f"Comment ça se passe pour vous, {m.group(1)} ?! Je commence à fatiguer !"),
    (r"^I'm getting really tired, (.+)! Can you kill them now\?$", lambda m: f"Je commence vraiment à fatiguer, {m.group(1)} ! Vous pouvez les achever maintenant ?"),
    (r"^(.+), can we end this soon\?! I'm getting tired!$", lambda m: f"{m.group(1)}, on peut abréger bientôt ?! Je commence à fatiguer !"),
    (r"^No! (.+), are you okay\? You don't look so great!$", lambda m: f"Non ! {m.group(1)}, vous allez bien ? Vous n'avez pas l'air en grande forme !"),
    (r"^Don't lie to me, (.+)\. Am I dying\? It feels like I'm dying\.$", lambda m: f"Ne me mentez pas, {m.group(1)}. Est-ce que je meurs ? J'ai l'impression de mourir."),
    (r"^I'm a bit lightheaded, (.+)\. You don't think I'm dying, do you\?$", lambda m: f"J'ai un peu la tête qui tourne, {m.group(1)}. Vous ne pensez pas que je suis en train de mourir, si ?"),
    (r"^(.+), do you think the amount of blood that left my body is acceptable\? (.+)\? (.+)\?$", lambda m: f"{m.group(1)}, vous pensez que la quantité de sang qui a quitté mon corps est acceptable ? {m.group(2)} ? {m.group(3)} ?"),
    (r"^\(Gasp\) When- When we're done fighting, (.+), I had an idea for- Never mind!$", lambda m: f"(Halète) Quand... quand ce combat sera fini, {m.group(1)}, j'ai eu une idée pour... Laissez tomber !"),

    # Taunts
    (r"^You do not want to fight (.+)! Or me!$", lambda m: f"Vous ne voulez vraiment pas vous battre contre {m.group(1)} ! Ni contre moi !"),
    (r"^What's wrong\? Are (.+) and I more than you can handle\?!$", lambda m: f"Qu'est-ce qu'il y a ? {m.group(1)} et moi, c'est plus que vous ne pouvez supporter ?!"),
    (r"^What's wrong\? Are (.+) and I more than you can handle\?$", lambda m: f"Qu'est-ce qu'il y a ? {m.group(1)} et moi, c'est trop pour vous ?"),
    (r"^What's wrong\? Regretting fighting me and (.+)\?$", lambda m: f"Qu'est-ce qui ne va pas ? Vous regrettez de nous avoir cherché des ennuis, à {m.group(1)} et moi ?"),
    (r"^Well, are you regretting attacking (.+),? yet\?$", lambda m: f"Alors, vous regrettez déjà d'avoir attaqué {m.group(1)} ?"),
    (r"^(.+) and I will kill you! You've made a terrible mistake!*$", lambda m: f"{m.group(1)} et moi allons vous tuer ! Vous avez fait une terrible erreur !"),
    (r"^(.+) and I will kill you! You've made a terrible mistake fighting us!$", lambda m: f"{m.group(1)} et moi allons vous tuer ! Vous avez fait une terrible erreur en nous affrontant !"),
    (r"^You're looking tired! Just let (.+) and I kill you, already!$", lambda m: f"Vous avez l'air fatigué ! Laissez {m.group(1)} et moi vous achever, qu'on en finisse !"),
    (r"^You're really going to fight me and (.+)\?!$", lambda m: f"Vous allez vraiment vous battre contre {m.group(1)} et moi ?!"),
    (r"^You're making a mistake attacking (.+)!$", lambda m: f"Vous faites une erreur en attaquant {m.group(1)} !"),
    (r"^You're picking a fight on (.+)\? You're in for a rude awakening!$", lambda m: f"Vous cherchez la bagarre avec {m.group(1)} ? Vous allez tomber de haut !"),
    (r"^You'd regret attacking me, if (.+) were going to let you live!$", lambda m: f"Vous regretteriez de m'avoir attaquée, si jamais {m.group(1)} vous laissait en vie !"),
    (r"^Don't you want to give up\?! Just tell (.+) you want to give up, and maybe we'll leave you alone!$", lambda m: f"Vous ne voulez pas abandonner ?! Dites simplement à {m.group(1)} que vous vous rendez, et on vous laissera peut-être tranquille !"),
    (r"^What did (.+) and I do for you to try to kill us\? You're so rude!$", lambda m: f"Qu'est-ce que {m.group(1)} et moi vous avons fait pour que vous essayiez de nous tuer ? Vous êtes tellement malpoli !"),
    (r"^You really shouldn't be fighting me or (.+)!$", lambda m: f"Vous ne devriez vraiment pas vous en prendre à moi ni à {m.group(1)} !"),
    (r"^You want to pick a fight with (.+)\?! That's rather stupid!$", lambda m: f"Vous voulez chercher des ennuis à {m.group(1)} ?! C'est plutôt stupide !"),
    (r"^Take that! (.+), did you see that\?!$", lambda m: f"Prends ça ! {m.group(1)}, vous avez vu ça ?!"),
    (r"^Hah, got you! (.+), did you see that\?!$", lambda m: f"Hah, touché ! {m.group(1)}, vous avez vu ça ?!"),
    (r"^Take this! Oh, (.+) will be proud of that hit!$", lambda m: f"Prends ça ! Oh, {m.group(1)} sera fier de ce coup !"),
    (r"^And this attack is for (.+)!$", lambda m: f"Et cette attaque, c'est pour {m.group(1)} !"),
    (r"^Hah! That's what you get for attacking me and (.+)!$", lambda m: f"Hah ! Voilà ce qui arrive quand on nous attaque, {m.group(1)} et moi !"),
    (r"^(.+) is going to kill you! You shouldn't have fought us!$", lambda m: f"{m.group(1)} va vous tuer ! Vous n'auriez pas dû nous chercher des ennuis !"),
    (r"^You're really going to regret fighting (.+)!$", lambda m: f"Vous allez vraiment regretter d'avoir combattu {m.group(1)} !"),

    # Post-combat relief / Victory
    (r"^Good work out there, (.+)!$", lambda m: f"Beau travail, {m.group(1)} !"),
    (r"^Excellent work, (.+)! We make a good team!$", lambda m: f"Excellent travail, {m.group(1)} ! Nous formons une bonne équipe !"),
    (r"^We work well together, don't we, (.+)\?$", lambda m: f"Nous travaillons bien ensemble, n'est-ce pas, {m.group(1)} ?"),
    (r"^I think we make a good team, (.+)!$", lambda m: f"Je trouve que nous faisons une bonne équipe, {m.group(1)} !"),
    (r"^We are a great team, (.+)!$", lambda m: f"Nous faisons une formidable équipe, {m.group(1)} !"),
    (r"^We are unstoppable, (.+)!$", lambda m: f"Nous sommes invincibles, {m.group(1)} !"),
    (r"^I'm happy you're on my side, (.+)\.$", lambda m: f"Je suis contente que vous soyez de mon côté, {m.group(1)}."),
    (r"^I'm glad to fight with you and not against you, (.+)\.$", lambda m: f"Je suis ravie de me battre à vos côtés et pas contre vous, {m.group(1)}."),
    (r"^And they're dead, and (.+) and I are alive\. We win!$", lambda m: f"Et ils sont morts, et {m.group(1)} et moi sommes vivants. On a gagné !"),
    (r"^\(Gasp\) Well, (.+), we aren't dead!$", lambda m: f"(Soupir) Eh bien, {m.group(1)}, nous ne sommes pas morts !"),
    (r"^\(Sigh\) Well, (.+), we aren't dead!$", lambda m: f"(Soupir) Eh bien, {m.group(1)}, nous ne sommes pas morts !"),
    (r"^Don't worry, (.+), I haven't died yet!$", lambda m: f"Ne vous inquiétez pas, {m.group(1)}, je ne suis pas encore morte !"),
    (r"^(.+)\? Oh, good\. You lived\. Me too, in case it wasn't obvious\.$", lambda m: f"{m.group(1)} ? Oh, tant mieux. Vous avez survécu. Moi aussi, au cas où ce ne serait pas évident."),
    (r"^(.+)\? (.+), you didn't die, did you\? Oh, you're alive\. Good\.$", lambda m: f"{m.group(1)} ? {m.group(2)}, vous n'êtes pas mort(e), rassurez-moi ? Oh, vous êtes en vie. Bien."),
    (r"^You haven't died, have you, (.+)\? Good\.$", lambda m: f"Vous n'êtes pas mort(e), n'est-ce pas, {m.group(1)} ? Bien."),
    (r"^(.+)\. (.+), are you alive\? Oh- Oh, good, you are\.$", lambda m: f"{m.group(1)}. {m.group(2)}, vous êtes en vie ? Oh... Oh, super, oui."),
    (r"^(.+), great news! We lived!$", lambda m: f"{m.group(1)}, bonne nouvelle ! On a survécu !"),
    (r"^(.+), we lived! Oh, maybe I should try to sound less surprised\. I'll work on that\.$", lambda m: f"{m.group(1)}, on a survécu ! Oh, je devrais peut-être paraître moins surprise. J'y travaillerai."),
    (r"^(.+), we lived!$", lambda m: f"{m.group(1)}, on a survécu !"),
    (r"^(.+), we lived! Not that I- Not that I doubted we would!$", lambda m: f"{m.group(1)}, on a survécu ! Non pas que... non pas que j'en aie douté !"),
    (r"^\(Gasp\) O-okay! I'm alive\. (.+) is alive\. Scrap is alive\. Everything is alive\. Well, except what we killed\.$", lambda m: f"(Halète) D-d'accord ! Je suis en vie. {m.group(1)} est en vie. Ferraille est en vie. Tout le monde est en vie. Enfin, sauf ce qu'on a tué."),
    (r"^O-okay! I'm alive\. (.+) is alive\. Scrap is alive\. Everyone is alive\.$", lambda m: f"D-d'accord ! Je suis en vie. {m.group(1)} est en vie. Ferraille est en vie. Tout le monde est en vie."),
    (r"^(.+) is alive\. I'm alive\. Everyone is alive\? Good\.$", lambda m: f"{m.group(1)} est en vie. Je suis en vie. Tout le monde est en vie ? Bien."),
    (r"^(.+) is alive\. I'm alive\. That means we win!$", lambda m: f"{m.group(1)} est en vie. Je suis en vie. Ça veut dire qu'on a gagné !"),
    (r"^We live another day! Unless we die in the next fight (.+) leads us to\.$", lambda m: f"Nous vivrons un jour de plus ! À moins que nous ne mourions dans le prochain combat où {m.group(1)} nous mènera."),
    (r"^Okay, that fight is done\. Now we wait for (.+) to lead us to another one\.$", lambda m: f"D'accord, ce combat est fini. Maintenant, on attend que {m.group(1)} nous entraîne dans le prochain."),
    (r"^That's done\. Well, until you lead us to another fight\. Anything to say for yourself, (.+)\? Hm\?$", lambda m: f"C'est réglé. Enfin, jusqu'à ce que vous nous meniez vers un autre combat. Quelque chose à dire pour votre défense, {m.group(1)} ? Hm ?"),
    (r"^Was that all, (.+)\?$", lambda m: f"C'était tout, {m.group(1)} ?"),
    (r"^(.+), you're always so impressive while fighting\.$", lambda m: f"{m.group(1)}, vous êtes toujours si impressionnant(e) au combat."),
    (r"^(.+), you're always impressive in fights!$", lambda m: f"{m.group(1)}, vous êtes toujours impressionnant(e) au combat !"),
    (r"^(.+), are you okay\? Alive and well\? At least alive\? *$", lambda m: f"{m.group(1)}, vous allez bien ? Sain(e) et sauf/sauve ? Au moins vivant(e) ?"),
    (r"^Are you okay, (.+)\?!$", lambda m: f"Vous allez bien, {m.group(1)} ?!"),
    (r"^Are you okay, (.+)\? No eyes poked out\? Enough blood to live\?$", lambda m: f"Vous allez bien, {m.group(1)} ? Aucun œil crevé ? Assez de sang pour survivre ?"),
    (r"^Are- Are you alright, (.+)\? Still have enough blood in your body to live\?$", lambda m: f"Vous... vous allez bien, {m.group(1)} ? Vous avez encore assez de sang dans le corps pour vivre ?")
]

unmatched = []
matched_map = {}

for it in items:
    exact_orig = it.get("original", "")
    orig = exact_orig.strip()
    fid = it.get("form_id")
    typ = it.get("type")
    idx = it.get("index")
    
    if orig in ["Khash...", "A, B, C, D, E, F, G, H..."]:
        # Keep verbatim
        matched_map[(fid, typ, idx, exact_orig)] = exact_orig
        continue
    if orig in direct_translations:
        matched_map[(fid, typ, idx, exact_orig)] = direct_translations[orig]
        continue
    
    found = False
    for pat, func in patterns:
        m = re.match(pat, orig, re.IGNORECASE)
        if m:
            tr = func(m)
            matched_map[(fid, typ, idx, exact_orig)] = tr
            found = True
            break
    if not found:
        unmatched.append(it)

print(f"Total matched: {len(matched_map)} / {len(items)}")
print(f"Unmatched remaining: {len(unmatched)}")
for u in unmatched:
    print(f"  {u['form_id']} | {u['type']} | {repr(u['original'])}")

# Save full mapping to json
with open("remiel_full_translation_map.json", "w", encoding="utf-8") as out:
    # keys as string for json
    export_data = [{"form_id": k[0], "type": k[1], "index": k[2], "original": k[3], "translation": v} for k, v in matched_map.items()]
    json.dump(export_data, out, ensure_ascii=False, indent=2)
print("Saved remiel_full_translation_map.json")
