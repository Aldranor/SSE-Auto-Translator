import json
from collections import defaultdict

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

by_quest = defaultdict(list)
for idx, e in enumerate(data):
    edid = e.get("editor_id")
    fid = e.get("form_id")
    qkey = f"{fid} ({edid})"
    by_quest[qkey].append((idx, e))

print(f"Total quests overridden in patch: {len(by_quest)}")

with open("all_quests_in_exp_patch.txt", "w", encoding="utf-8") as out:
    for qkey, entries in by_quest.items():
        out.write(f"\n=======================================================\n")
        out.write(f"QUEST: {qkey} (Total strings: {len(entries)})\n")
        out.write(f"=======================================================\n")
        for idx, e in entries:
            out.write(f"  [{idx}] {e.get('type')} idx={e.get('index')} status={e.get('status')}\n")
            out.write(f"    ORIG: {repr(e.get('original'))}\n")
            out.write(f"    TRAD: {repr(e.get('string'))}\n")

print("Saved all quests to all_quests_in_exp_patch.txt")
