import json

p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for item in data:
    if item.get('form_id') == '1000080F|ccbgssse020-graycowl.esl' and item.get('type') == 'QUST CNAM':
        if item.get('original') == 'At the Riften cemetery, I found a thief loitering near a tombstone. On his body was a note that mentioned the Gray Fox was dead, and his cowl was to be passed on to a new owner. I then spoke to a beggar who handed me a note.':
            item['string'] = "Au cimetière de Faillaise, j'ai trouvé un voleur qui rôdait près d'une pierre tombale. Sur son corps se trouvait une note mentionnant que le Renard gris était mort et que son capuchon devait être transmis à un nouveau propriétaire. J'ai ensuite parlé à un mendiant qui m'a remis une note m'informant d'un travail."
            item['status'] = 'TranslationComplete'
            count += 1

print(f'Modified {count} entry in CCQuest.')
with open(p, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
