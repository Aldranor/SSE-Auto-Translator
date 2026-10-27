import json

esp_path = r"data/user/database/french/Immersive Hunting Animations/immersivehunting.esp.json"
txt_path = r"data/user/database/french/ImmersiveHunting_french.txt - French/interface/translations/ImmersiveHunting_french.txt.json"

with open(esp_path, "r", encoding="utf-8") as f:
    esp_data = json.load(f)

with open(txt_path, "r", encoding="utf-8") as f:
    txt_data = json.load(f)

print(f"=== ESP JSON: {len(esp_data)} entries ===")
esp_status = {}
for e in esp_data:
    st = e.get("status")
    esp_status[st] = esp_status.get(st, 0) + 1
print("ESP statuses:", esp_status)

print(f"\n=== TXT JSON: {len(txt_data)} entries ===")
txt_status = {}
for e in txt_data:
    st = e.get("status")
    txt_status[st] = txt_status.get(st, 0) + 1
print("TXT statuses:", txt_status)

print("\n--- Non-complete or identical in ESP ---")
for i, e in enumerate(esp_data):
    if e.get("status") != "TranslationComplete" or e.get("original") == e.get("string"):
        print(f"[{i}] {e.get('status')} | {e.get('type')} | {e.get('editor_id')} | {repr(e.get('original'))} -> {repr(e.get('string'))}")

print("\n--- Non-complete or identical in TXT ---")
for i, e in enumerate(txt_data):
    if e.get("status") != "TranslationComplete" or e.get("original") == e.get("string"):
        print(f"[{i}] {e.get('status')} | {e.get('mcm_id')} | {repr(e.get('original'))} -> {repr(e.get('string'))}")
