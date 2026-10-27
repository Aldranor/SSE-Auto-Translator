import json
import re

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    trans = s.get("string") or ""
    orig = s.get("original") or ""
    for weird in ["<pagebreak]", "< ?>", "<intraduisible>", "<font=\"$Bordecielbooks\">", "<Alias=Player>", "<Alias=QuestGiver>", "<Alias=HoldCity>", "<Alias=ItemREF>"]:
        if weird in trans:
            print(f"[{s.get('type')}] FormID: {s.get('form_id')} | EDID: {s.get('editor_id')}")
            print(f"  Orig:  {orig}")
            print(f"  Trans: {trans}")
            print()
