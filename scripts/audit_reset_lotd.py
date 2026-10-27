import json
import re
from pathlib import Path
from collections import defaultdict

lotd_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")

with open(lotd_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entries in LegacyoftheDragonborn.esm.json: {len(data)}")

# ==========================================
# 1. STATUS SUMMARY
# ==========================================
status_counts = defaultdict(int)
for s in data:
    status_counts[s.get("status", "None")] += 1

print("\n--- STATUS BREAKDOWN ---")
for st, cnt in sorted(status_counts.items()):
    print(f"  {st}: {cnt}")

# ==========================================
# 2. VARIABLE INTEGRITY & BOGUS TAGS
# ==========================================
VAR_REGEX = re.compile(r"<[a-zA-Z0-9_\-=]+>|\[[a-zA-Z0-9_\-]+\]|%[0-9]*[sdf]|\$[a-zA-Z0-9_]+")
BOGUS_TAG_REGEX = re.compile(r"<\d+>")

missing_variables = []
bogus_tags_list = []

for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans or trans == orig:
        continue
        
    orig_vars = set(VAR_REGEX.findall(orig))
    trans_vars = set(VAR_REGEX.findall(trans))
    missing = orig_vars - trans_vars
    if missing:
        missing_variables.append({
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "missing": list(missing)
        })
        
    bogus = set(BOGUS_TAG_REGEX.findall(trans))
    if bogus:
        bogus_tags_list.append({
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "bogus": list(bogus)
        })

print(f"\n--- VARIABLES ---")
print(f"  Missing authentic variables: {len(missing_variables)}")
print(f"  Bogus number tags (<10>, <25>, etc.): {len(bogus_tags_list)}")

# ==========================================
# 3. BOOKS AUDIT (BCSLL & others)
# ==========================================
EN_STOPWORDS = re.compile(r"\b(the|and|with|from|which|they|their|when|would|could|should|this|that|chapter|page)\b", re.I)
FR_STOPWORDS = re.compile(r"\b(le|la|les|un|une|des|du|de|dans|avec|pour|qui|que|dans|chapitre)\b", re.I)

english_books = []
french_books = []
untranslated_books = []

for s in data:
    t = s.get("type") or ""
    if "BOOK" not in t:
        continue
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    status = s.get("status")
    
    if not trans or trans == orig or status == "TranslationRequired":
        untranslated_books.append(s)
        continue
        
    # Check language of book content
    clean_trans = re.sub(r"<[^>]+>", " ", trans).replace("[pagebreak]", " ")
    words = clean_trans.split()
    if len(words) < 20:
        continue
        
    en_count = len(EN_STOPWORDS.findall(clean_trans))
    fr_count = len(FR_STOPWORDS.findall(clean_trans))
    
    if en_count > 15 and en_count > fr_count * 2:
        english_books.append({
            "form_id": s.get("form_id"),
            "edid": s.get("editor_id"),
            "type": t,
            "status": status,
            "title_or_snippet": clean_trans[:100].strip(),
            "word_count": len(words),
            "en_count": en_count,
            "fr_count": fr_count
        })
    elif fr_count > 10:
        french_books.append(s)

print(f"\n--- BOOKS ---")
print(f"  Untranslated / empty books: {len(untranslated_books)}")
print(f"  Books with French translation: {len(french_books)}")
print(f"  Books with ENGLISH text in translation field: {len(english_books)}")

# ==========================================
# 4. QUEST STAGES & TEXT MISMATCHES
# ==========================================
# Detect cases where original and trans do not match each other (cross-wired)
quest_mismatches = []
other_mismatches = []

for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    t = s.get("type") or ""
    if not trans or trans == orig:
        continue
        
    clean_orig = re.sub(r"<[^>]+>", " ", orig).replace("[pagebreak]", " ").strip()
    clean_trans = re.sub(r"<[^>]+>", " ", trans).replace("[pagebreak]", " ").strip()
    
    orig_words = clean_orig.split()
    trans_words = clean_trans.split()
    
    if len(orig_words) < 4 or len(trans_words) < 4:
        continue
        
    # Check if translation is English text that doesn't match original English text
    is_trans_en = len(EN_STOPWORDS.findall(clean_trans)) >= 3
    is_orig_en = len(EN_STOPWORDS.findall(clean_orig)) >= 3
    
    if is_trans_en and is_orig_en:
        # Both in English, compare shared words
        w_orig = set(re.findall(r"\b[a-zA-Z]{4,}\b", clean_orig.lower()))
        w_trans = set(re.findall(r"\b[a-zA-Z]{4,}\b", clean_trans.lower()))
        overlap = w_orig & w_trans
        if len(w_orig) >= 4 and len(overlap) / len(w_orig) < 0.2:
            entry = {
                "form_id": s.get("form_id"),
                "type": t,
                "edid": s.get("editor_id"),
                "orig": clean_orig,
                "trans": clean_trans,
                "overlap": list(overlap)
            }
            if t == "QUST CNAM":
                quest_mismatches.append(entry)
            else:
                other_mismatches.append(entry)

print(f"\n--- MISMATCHES ORIGIN / TRAD ---")
print(f"  Cross-wired English quest stages (QUST CNAM): {len(quest_mismatches)}")
print(f"  Other mismatched English texts: {len(other_mismatches)}")

# ==========================================
# 5. NUMERIC DISCREPANCIES IN GAMEPLAY
# ==========================================
gameplay_num_diffs = []
for s in data:
    t = s.get("type") or ""
    if "BOOK" in t:
        continue
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans or trans == orig:
        continue
    if not re.search(r"\b(damage|health|magicka|stamina|armor|speed|resist|absorb|increase|reduce|cost|chance|points?|seconds?|percent|%)\b", orig, re.I):
        continue
        
    orig_nums = sorted([n.replace(",", ".").replace("%", "") for n in re.findall(r"\b\d+(?:[\.,]\d+)?%?", orig)])
    trans_nums = sorted([n.replace(",", ".").replace("%", "") for n in re.findall(r"\b\d+(?:[\.,]\d+)?%?", trans)])
    
    if orig_nums != trans_nums and orig_nums and trans_nums:
        # Check if difference is not purely bogus angle brackets like <10>
        gameplay_num_diffs.append({
            "form_id": s.get("form_id"),
            "type": t,
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "orig_nums": orig_nums,
            "trans_nums": trans_nums
        })

print(f"\n--- GAMEPLAY NUMERIC DISCREPANCIES ---")
print(f"  Count: {len(gameplay_num_diffs)}")

# Save detailed report
report = {
    "status_counts": dict(status_counts),
    "missing_variables": missing_variables,
    "bogus_tags_list": bogus_tags_list,
    "english_books": english_books,
    "quest_mismatches": quest_mismatches,
    "other_mismatches": other_mismatches,
    "gameplay_num_diffs": gameplay_num_diffs
}

with open("lotd_reset_audit_report.json", "w", encoding="utf-8") as out:
    json.dump(report, out, indent=2, ensure_ascii=False)

print("\nAudit report written to lotd_reset_audit_report.json")
