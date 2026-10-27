import json

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

untrans_books = [s for s in data if "BOOK" in (s.get("type") or "") and (not s.get("string") or s.get("string") == s.get("original") or s.get("status") == "TranslationRequired")]

print(f"Total untranslated/incomplete books: {len(untrans_books)}")
for b in untrans_books[:30]:
    orig_snippet = (b.get('original') or '')[:100].replace('\n', ' ')
    print(f"[{b.get('type')}] FormID: {b.get('form_id')} | EDID: {b.get('editor_id')} | Status: {b.get('status')}")
    print(f"  Orig: {orig_snippet}")
    print()
