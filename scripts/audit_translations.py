import json
import re
from pathlib import Path

db_base = Path("data/user/database/french")

# False friends and bad machine translation markers
FAUX_AMIS = [
    (r"\bbarri[eè]re\b", "fence", "Fence = Receleur / Receleuse (non barrière/clôture)"),
    (r"\bcl[oô]ture\b", "fence", "Fence = Receleur / Receleuse"),
    (r"\b(un|le|ce)\s+anneau\b.*\bsonner\b", "ring", "Ring = Anneau (non le verbe sonner)"),
    (r"\bv[eê]tement\b", "robes", "Robes = Robes (non vêtement générique)"),
]

# Patterns for variables
VAR_PATTERNS = [
    r"<[a-zA-Z0-9_\-=]+>", # <mag>, <dur>, <alias=...>
    r"\[[a-zA-Z0-9_\-]+\]", # [Sprint], [Activate]
    r"%[0-9]*[sdf]",        # %s, %d, %1$s
    r"\$[a-zA-Z0-9_]+",    # $Prompt
]

SUSPICIOUS_ENGLISH_WORDS = [
    "chest", "key", "sword", "shield", "bow", "boots", "cuirass", "gauntlets",
    "helmet", "ring", "amulet", "scroll", "staff", "potion", "poison",
    "the", "of", "and", "in", "to", "for", "with", "from", "at"
]

results = {
    "broken_variables": [],
    "false_friends": [],
    "untranslated_english": [],
    "internal_inconsistencies": {}, # original -> set of translations
    "bad_syntax_names": [] # e.g. "Name Boule"
}

def check_variables(orig, trans, context):
    for pat in VAR_PATTERNS:
        orig_vars = set(re.findall(pat, orig))
        trans_vars = set(re.findall(pat, trans))
        if orig_vars != trans_vars:
            results["broken_variables"].append({
                "context": context,
                "original": orig,
                "translation": trans,
                "orig_vars": list(orig_vars),
                "trans_vars": list(trans_vars)
            })

def is_mostly_english(text):
    words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
    if not words:
        return False
    eng_count = sum(1 for w in words if w in SUSPICIOUS_ENGLISH_WORDS)
    return (eng_count / len(words)) >= 0.5 and len(words) >= 2

def audit_file(jf):
    rel_path = jf.relative_to(db_base)
    mod_folder = rel_path.parts[0]
    
    # Skip huge known official mods if requested, focus on patches/imported
    mod_lower = mod_folder.lower()
    
    try:
        data = json.loads(jf.read_text(encoding="utf-8"))
    except Exception:
        return

    file_originals = {}
    for entry in data:
        orig = (entry.get("original") or "").strip()
        trans = (entry.get("string") or "").strip()
        if not orig or not trans:
            continue

        context = f"{mod_folder} > {jf.name}"

        # 1. Check variables
        check_variables(orig, trans, context)

        # 2. Check false friends
        if "fence" in orig.lower():
            if re.search(r"\bbarri[eè]re\b|\bcl[oô]ture\b", trans, re.IGNORECASE):
                results["false_friends"].append({
                    "context": context,
                    "original": orig,
                    "translation": trans,
                    "issue": "Fence traduit par barrière/clôture au lieu de receleur"
                })

        # 3. Check English remaining
        if orig != trans and is_mostly_english(trans):
            # Check if it looks like untranslated english title
            results["untranslated_english"].append({
                "context": context,
                "original": orig,
                "translation": trans
            })
        elif orig == trans and len(orig.split()) >= 2 and is_mostly_english(orig):
            # Same as original and english
            # Ignore proper names
            if not any(x in orig for x in ["DLC", "USKP", "USSEP", "SSE"]):
                results["untranslated_english"].append({
                    "context": context,
                    "original": orig,
                    "translation": trans,
                    "issue": "Identique à la source anglaise"
                })

        # 4. Check inversions like "Trueaz Boule"
        if re.search(r"\b[A-Z][a-z]+\s+(Boule|Hache|Épée|Dague|Arc|Casque|Armure|Clé)\b", trans):
            results["bad_syntax_names"].append({
                "context": context,
                "original": orig,
                "translation": trans,
                "issue": "Inversion syntaxique anglaise (ex: Trueaz Boule au lieu de Balle de Trueaz)"
            })

        # 5. Track inconsistencies within mod
        if len(orig) >= 4 and len(orig.split()) <= 4:
            if orig not in file_originals:
                file_originals[orig] = set()
            file_originals[orig].add(trans)

    for orig, trans_set in file_originals.items():
        if len(trans_set) > 1:
            if mod_folder not in results["internal_inconsistencies"]:
                results["internal_inconsistencies"][mod_folder] = []
            results["internal_inconsistencies"][mod_folder].append({
                "original": orig,
                "translations": list(trans_set),
                "file": jf.name
            })

def main():
    print("Starting translation audit...")
    all_files = list(db_base.rglob("*.json"))
    print(f"Total database files: {len(all_files)}")
    
    for jf in all_files:
        if jf.name == "index.json":
            continue
        audit_file(jf)

    print(f"\nAudit complete!")
    print(f"Broken variables found: {len(results['broken_variables'])}")
    print(f"False friends found: {len(results['false_friends'])}")
    print(f"Untranslated English found: {len(results['untranslated_english'])}")
    print(f"Bad syntax names found: {len(results['bad_syntax_names'])}")
    print(f"Mods with internal inconsistencies: {len(results['internal_inconsistencies'])}")

    with open("translation_audit_results.json", "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2, ensure_ascii=False)
    print("Saved results to translation_audit_results.json")

if __name__ == '__main__':
    main()
