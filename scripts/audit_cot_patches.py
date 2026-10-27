import json
import glob

patch_files = [
    r"data/user/database/french/Citizens of Tamriel - More Immersive Edit - French/CitizensComplete-MIE.esp.json",
    r"data/user/database/french/Modpocalypse NPCs - Citizens of Tamriel/modpocalypse npcs (v3) citizens of tamriel.esp.json",
    r"data/user/database/french/RS Children Overhaul - Citizens of Tamriel Patch/citizenscomplete_rschildrenpatch.esp.json",
    r"data/user/database/french/The Great City of Winterhold Patch Collection - French/TGC Winterhold - Citizens of Tamriel patch.esp.json",
    r"data/user/database/french/The JK's Interiors of EEK's Whiterun - French/JKEEKBanneredMare - Citizens of Tamriel patch.esp.json",
    r"data/user/database/french/JKs Guild HQ Interiors Patch Collection/jks bards college - citizens complete patch.esp.json",
    r"data/user/database/french/Lux Interiora Distincta - JK's Silver-Blood Inn Variante - French/LuxID-JKs Silver-Blood Inn - Citizens Complete patch.esp.json",
]

for p in patch_files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        untrans = [e for e in data if e.get('status') != 'TranslationComplete' or e.get('original') == e.get('string')]
        print(f"=== {p} ===")
        print(f"  Total: {len(data)}, Untranslated/Identical: {len(untrans)}")
        for u in untrans:
            print(f"    [{u.get('type')}] {u.get('editor_id')}: {repr(u.get('original'))} -> {repr(u.get('string'))} ({u.get('status')})")
    except Exception as ex:
        print(f"Error {p}: {ex}")
