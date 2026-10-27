import json
import re
from pathlib import Path
from collections import defaultdict

lotd_esm_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")

with open(lotd_esm_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total strings: {len(data)}")

# 1. BROKEN VARIABLES
# e.g., missing <mag>, <dur>, <alias=...>, %s, or invalid added <...>
VAR_REGEX = re.compile(r"<[a-zA-Z0-9_\-=]+>|\[[a-zA-Z0-9_\-]+\]|%[0-9]*[sdf]|\$[a-zA-Z0-9_]+")
ALL_TAGS_REGEX = re.compile(r"<[^>]+>")

broken_vars = []
for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans or trans == orig:
        continue
    
    orig_vars = set(VAR_REGEX.findall(orig))
    trans_vars = set(VAR_REGEX.findall(trans))
    
    # Also check if trans has bogus angle brackets around numbers like <10> when orig didn't
    bogus_tags = set(re.findall(r"<\d+>", trans))
    
    # Missing genuine variables
    missing_vars = orig_vars - trans_vars
    # Extra unexpected variables
    extra_vars = trans_vars - orig_vars
    
    if missing_vars or bogus_tags:
        broken_vars.append({
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "missing_vars": list(missing_vars),
            "bogus_tags": list(bogus_tags)
        })

print(f"Broken / corrupted variables: {len(broken_vars)}")

# 2. NUMERIC DISCREPANCIES (Gameplay impact: spells, perks, enchantments, weapons, armor)
numeric_discrepancies = []
for s in data:
    t = s.get("type") or ""
    if not any(k in t for k in ["DESC", "DNAM", "FULL", "ITXT"]):
        continue
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans or trans == orig:
        continue
    
    # Look for gameplay indicators
    if not re.search(r"\b(damage|health|magicka|stamina|armor|speed|resist|absorb|increase|reduce|cost|chance|critical|points?|seconds?|percent|%)\b", orig, re.I):
        continue
        
    orig_nums = re.findall(r"\b\d+(?:[\.,]\d+)?%?", orig)
    trans_nums = re.findall(r"\b\d+(?:[\.,]\d+)?%?", trans)
    
    # Normalize
    orig_norm = sorted([n.replace(",", ".").replace("%", "") for n in orig_nums])
    trans_norm = sorted([n.replace(",", ".").replace("%", "") for n in trans_nums])
    
    if orig_norm != trans_norm and orig_norm and trans_norm:
        numeric_discrepancies.append({
            "form_id": s.get("form_id"),
            "type": t,
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "orig_nums": orig_nums,
            "trans_nums": trans_nums
        })

print(f"Numeric discrepancies in gameplay texts: {len(numeric_discrepancies)}")

# 3. SEMANTIC / CONCEPT CONTRADICTIONS & INVERSIONS
# E.g. increase vs decrease, left vs right, light vs heavy, one-handed vs two-handed, etc.
CONCEPT_PAIRS = [
    ("increase_vs_decrease", [r"\bincreas", r"\brais", r"\bmore\b"], [r"\brédui", r"\bdiminu", r"\bbaiss", r"\bmoins\b"]),
    ("decrease_vs_increase", [r"\bdecreas", r"\breduc", r"\bless\b"], [r"\baugmente", r"\baccroît", r"\bplus\b"]),
    ("onehanded_vs_twohanded", [r"\bone[- ]handed\b"], [r"\bdeux mains\b"]),
    ("twohanded_vs_onehanded", [r"\btwo[- ]handed\b"], [r"\bune main\b"]),
    ("light_vs_heavy", [r"\blight armor\b"], [r"\barmure lourde\b"]),
    ("heavy_vs_light", [r"\bheavy armor\b"], [r"\barmure légère\b"]),
    ("male_vs_female", [r"\bmale\b"], [r"\bfemme\b", r"\bféminin\b"]),
    ("female_vs_male", [r"\bfemale\b"], [r"\bhomme\b", r"\bmasculin\b"]),
    ("cure_vs_cause", [r"\bcure\b"], [r"\binflige", r"\bprovoque"]),
]

semantic_mismatches = []
for s in data:
    orig = (s.get("original") or "").lower()
    trans = (s.get("string") or "").lower()
    if not trans or trans == orig:
        continue
        
    for name, en_pats, fr_pats in CONCEPT_PAIRS:
        has_en = any(re.search(p, orig) for p in en_pats)
        has_fr = any(re.search(p, trans) for p in fr_pats)
        if has_en and has_fr:
            semantic_mismatches.append({
                "rule": name,
                "form_id": s.get("form_id"),
                "type": s.get("type"),
                "edid": s.get("editor_id"),
                "orig": s.get("original"),
                "trans": s.get("string")
            })

print(f"Semantic inversions / contradictions: {len(semantic_mismatches)}")

# 4. UNTRANSLATED ENGLISH TEXT IN TRANSLATION FIELD
ENGLISH_SENTENCE_REGEX = re.compile(r"\b(the|and|with|from|which|your|when|while|this|that|their|they|have|been|will|could|would)\b", re.I)
untranslated_english = []
for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans:
        continue
    # If translation contains multiple common English grammatical words
    en_words = ENGLISH_SENTENCE_REGEX.findall(trans)
    if len(en_words) >= 3 and len(trans.split()) > 4:
        untranslated_english.append({
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "english_markers": en_words[:5]
        })

print(f"Untranslated English in translation field: {len(untranslated_english)}")

# 5. COMPLETELY MISMATCHED STRINGS (Where translation text is completely unrelated to original)
# Let's check records where original and translation clearly have no common ground
# (e.g. original is a book title and translation is a sword name, or original is a dialogue and translation is a quest stage)

lotd_audit = {
    "broken_vars": broken_vars,
    "numeric_discrepancies": numeric_discrepancies,
    "semantic_mismatches": semantic_mismatches,
    "untranslated_english": untranslated_english
}

with open("lotd_deep_audit.json", "w", encoding="utf-8") as out:
    json.dump(lotd_audit, out, indent=2, ensure_ascii=False)
