import os
import json
import re
import time
from pathlib import Path
from collections import defaultdict

db_base = Path("data/user/database/french")

# 1. Technical regexes
# Note: pure numeric tags like <10> or <5> are NOT engine variables; they are illegal tags
VAR_PATTERNS = [
    r"<(?![0-9]+>)[a-zA-Z0-9_\-=]+>", # <mag>, <dur>, <alias=...>, etc. (excluding <10>, <5>)
    r"\[[a-zA-Z0-9_\-]+\]",           # [pagebreak], [Sprint], [Activate]
    r"%[0-9]*[sdf]",                  # %s, %d, %1$s
    r"\$[a-zA-Z0-9_]+",              # $Prompt
    r"\{[0-9]+\}",                    # {0}, {1}
]
CORRUPT_TAG_RE = re.compile(r"<[0-9]+>")

FONT_TAG_OPEN_RE = re.compile(r"<font\b[^>]*>", re.IGNORECASE)
FONT_TAG_CLOSE_RE = re.compile(r"</font>", re.IGNORECASE)

# 2. Number extraction regex
NUMBER_RE = re.compile(r"\b\d+(?:[\.,]\d+)?%?\b")

# 3. Faux amis & calques
FAUX_AMIS = [
    (re.compile(r"\bbarri[eè]re\b", re.IGNORECASE), "fence", "Fence traduit par 'Barrière' (au lieu de Receleur/Receleuse)"),
    (re.compile(r"\bcl[oô]ture\b", re.IGNORECASE), "fence", "Fence traduit par 'Clôture' (au lieu de Receleur/Receleuse)"),
    (re.compile(r"\b(?:un|le|ce|votre)\s+anneau\b.*\bsonner\b", re.IGNORECASE), "ring", "Ring traduit par 'Sonner' (au lieu d'Anneau)"),
    (re.compile(r"\bboucher\b", re.IGNORECASE), "butcher", "Butcher traduit par 'Boucher' (au lieu de Découper/Prélever)"),
    (re.compile(r"\bsur demande\b", re.IGNORECASE), "prompt", "Prompt traduit par 'Sur demande' (au lieu de Menu interactif/Invite)"),
    (re.compile(r"\brapide\b", re.IGNORECASE), "prompt", "Prompt traduit par 'Rapide' (dans un contexte de menu)"),
]

# 4. Lore keywords to enforce
LORE_ISSUES = [
    (re.compile(r"\bmontagne\s+rouge\b", re.IGNORECASE), "Mont Écarlate (nom officiel Bethesda de Red Mountain)"),
    (re.compile(r"\bmana\b", re.IGNORECASE), "Magie (terme canonique dans Skyrim)"),
]

# 5. English dictionary markers for untranslated text
COMMON_ENGLISH_WORDS = {
    "the", "of", "and", "in", "to", "for", "with", "from", "at", "by", "this", "that",
    "sword", "shield", "boots", "cuirass", "gauntlets", "helmet", "ring", "amulet", "bow",
    "dagger", "mace", "axe", "chest", "key", "door", "shack", "dungeon", "bandit", "guard",
    "potion", "poison", "scroll", "staff", "spell", "book", "note", "letter", "journal",
    "you", "your", "when", "while", "during", "after", "before", "increase", "decreases",
    "reduces", "damage", "health", "stamina", "magicka", "target", "points", "seconds", "chance"
}

# 6. Concept mapping pairs (EN concept -> FR concept) for perks/spells/items
CONCEPT_PAIRS = [
    ("health", ["health", "life"], ["santé", "vie"]),
    ("magicka", ["magicka", "magic points"], ["magie", "points de magie"]),
    ("stamina", ["stamina", "endurance"], ["vigueur"]),
    ("fire", ["fire", "flame", "burn"], ["feu", "flamme", "brûl"]),
    ("frost", ["frost", "ice", "freeze", "cold"], ["froid", "glace", "gel"]),
    ("shock", ["shock", "lightning", "spark"], ["foudre", "électr", "étincel"]),
    ("one_handed", ["one-handed", "one handed"], ["une main"]),
    ("two_handed", ["two-handed", "two handed"], ["deux mains"]),
    ("bow_archery", ["bow", "archery", "marksman"], ["arc", "archerie"]),
    ("crossbow", ["crossbow"], ["arbalète"]),
    ("dagger", ["dagger"], ["dague"]),
    ("paralysis", ["paralyze", "paralysis"], ["paralys"]),
    ("invisible", ["invisib"], ["invisib"]),
    ("soul_trap", ["soul trap"], ["capture d'âme"]),
    ("reanimate", ["reanimate", "resurrect", "zombie"], ["réanim", "ressuscit", "zombie"]),
    ("disarm", ["disarm"], ["désarm"]),
    ("absorb", ["absorb"], ["absorb"]),
    ("silence", ["silent", "quiet", "muffle"], ["silenc", "discret", "étouff"]),
    ("stagger", ["stagger"], ["déstabilis", "déséquilibr", "vacill"]),
    ("poison", ["poison"], ["poison", "venin"]),
]

def scan_file(json_path: Path):
    rel_path = json_path.relative_to(db_base)
    mod_name = rel_path.parts[0]
    file_name = json_path.name
    
    file_findings = {
        "technical": [],
        "numeric_mismatches": [],
        "concept_mismatches": [],
        "faux_amis": [],
        "lore_issues": [],
        "untranslated_english": []
    }
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return None
        
    items = data if isinstance(data, list) else data.get("strings", [])
    
    for item in items:
        orig = str(item.get("original") or "").strip()
        trans = str(item.get("string") or item.get("translation") or "").strip()
        status = item.get("status")
        rec_type = item.get("type", "")
        form_id = item.get("form_id", "")
        editor_id = item.get("editor_id", "")
        
        if not orig:
            continue
            
        # 1. Technical check
        # Check broken variables
        for pat in VAR_PATTERNS:
            v_orig = set(re.findall(pat, orig))
            v_trans = set(re.findall(pat, trans))
            if v_orig != v_trans:
                file_findings["technical"].append({
                    "form_id": form_id,
                    "type": rec_type,
                    "kind": "variable_mismatch",
                    "original": orig,
                    "translation": trans,
                    "missing": list(v_orig - v_trans),
                    "added": list(v_trans - v_orig)
                })
                break
                
        # Check illegal tags <10>, <5>
        bad_tags = CORRUPT_TAG_RE.findall(trans)
        if bad_tags:
            file_findings["technical"].append({
                "form_id": form_id,
                "type": rec_type,
                "kind": "illegal_tag",
                "tags": bad_tags,
                "translation": trans
            })
            
        # Check unclosed font tags
        open_fonts = len(FONT_TAG_OPEN_RE.findall(trans))
        close_fonts = len(FONT_TAG_CLOSE_RE.findall(trans))
        if open_fonts != close_fonts:
            file_findings["technical"].append({
                "form_id": form_id,
                "type": rec_type,
                "kind": "unclosed_font_tag",
                "open_count": open_fonts,
                "close_count": close_fonts,
                "translation": trans[:100] + "..."
            })
            
        if not trans:
            continue
            
        # 2. Faux amis & Lore check
        for pat, en_trigger, desc in FAUX_AMIS:
            if pat.search(trans) and en_trigger in orig.lower():
                file_findings["faux_amis"].append({
                    "form_id": form_id,
                    "type": rec_type,
                    "desc": desc,
                    "original": orig,
                    "translation": trans
                })
                
        for pat, desc in LORE_ISSUES:
            if pat.search(trans):
                file_findings["lore_issues"].append({
                    "form_id": form_id,
                    "type": rec_type,
                    "desc": desc,
                    "original": orig,
                    "translation": trans
                })
                
        # 3. Untranslated English check (when marked complete or identical)
        if trans == orig and len(orig) > 3:
            # Check if original is clearly English words (not an acronym or pure proper name)
            words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", orig)]
            common_matches = [w for w in words if w in COMMON_ENGLISH_WORDS]
            if len(common_matches) >= 2 or (len(words) == 1 and words[0] in {"chest", "key", "sword", "shield", "bow", "helmet", "boots", "ring", "amulet", "dagger"}):
                file_findings["untranslated_english"].append({
                    "form_id": form_id,
                    "type": rec_type,
                    "kind": "identical_english",
                    "original": orig,
                    "translation": trans
                })
        elif trans != orig and len(trans) > 10:
            words = [w.lower() for w in re.findall(r"\b[a-zA-Z]{3,}\b", trans)]
            if len(words) >= 4:
                common_matches = [w for w in words if w in COMMON_ENGLISH_WORDS]
                ratio = len(common_matches) / len(words)
                if ratio >= 0.5:
                    file_findings["untranslated_english"].append({
                        "form_id": form_id,
                        "type": rec_type,
                        "kind": "mostly_english_text",
                        "ratio": round(ratio, 2),
                        "original": orig[:100],
                        "translation": trans[:100]
                    })
                    
        # 4. Numeric mismatches (gameplay & balance critical)
        if any(t in rec_type for t in ["PERK", "SPEL", "MGEF", "ENCH", "ALCH", "WEAP", "ARMO"]):
            nums_orig = set(NUMBER_RE.findall(orig))
            nums_trans = set(NUMBER_RE.findall(trans))
            if nums_orig != nums_trans:
                # Filter out pure variable tags like <1> or date-like numbers if identical
                diff_orig = nums_orig - nums_trans
                diff_trans = nums_trans - nums_orig
                if diff_orig or diff_trans:
                    file_findings["numeric_mismatches"].append({
                        "form_id": form_id,
                        "type": rec_type,
                        "original": orig,
                        "translation": trans,
                        "in_orig_not_trans": list(diff_orig),
                        "in_trans_not_orig": list(diff_trans)
                    })
                    
        # 5. Concept mismatches
        if any(t in rec_type for t in ["PERK", "SPEL", "MGEF", "ENCH", "ALCH"]):
            orig_low = orig.lower()
            trans_low = trans.lower()
            en_found = set()
            fr_found = set()
            for c_name, en_w, fr_w in CONCEPT_PAIRS:
                if any(re.search(r"\b" + re.escape(w) + r"\b", orig_low) for w in en_w):
                    en_found.add(c_name)
                if any(re.search(r"\b" + re.escape(w) + r"\b", trans_low) for w in fr_w):
                    fr_found.add(c_name)
            
            missing_in_fr = en_found - fr_found
            extra_in_fr = fr_found - en_found
            if missing_in_fr and extra_in_fr:
                file_findings["concept_mismatches"].append({
                    "form_id": form_id,
                    "type": rec_type,
                    "original": orig,
                    "translation": trans,
                    "en_concepts": list(en_found),
                    "fr_concepts": list(fr_found),
                    "missing_in_fr": list(missing_in_fr),
                    "extra_in_fr": list(extra_in_fr)
                })

    has_findings = any(len(v) > 0 for v in file_findings.values())
    if has_findings:
        return {
            "mod": mod_name,
            "file": file_name,
            "rel_path": str(rel_path),
            "findings": file_findings
        }
    return None

def main():
    start_time = time.time()
    print("Starting Phase 0 Global Scan across data/user/database/french...")
    
    all_json_files = [p for p in db_base.rglob("*.json") if p.name != "index.json"]
    print(f"Total JSON files to scan: {len(all_json_files)}")
    
    # Load unverified local mods set to tag findings
    unverif_data = json.load(open("local_unverified_analysis.json", encoding="utf-8"))
    unverif_mod_names = set(u["name"].lower() for u in unverif_data["unverified"])
    
    results = []
    scanned_count = 0
    
    summary_counts = {
        "technical": 0,
        "numeric_mismatches": 0,
        "concept_mismatches": 0,
        "faux_amis": 0,
        "lore_issues": 0,
        "untranslated_english": 0
    }
    
    for jf in all_json_files:
        scanned_count += 1
        res = scan_file(jf)
        if res:
            res["is_unverified_local_mod"] = res["mod"].lower() in unverif_mod_names
            results.append(res)
            for k in summary_counts:
                summary_counts[k] += len(res["findings"][k])
                
        if scanned_count % 1000 == 0:
            print(f"Scanned {scanned_count}/{len(all_json_files)} files...")
            
    elapsed = round(time.time() - start_time, 2)
    print(f"\nScan completed in {elapsed}s.")
    print(f"Files with anomalies: {len(results)} / {len(all_json_files)}")
    print("Summary of anomalies detected:")
    for k, v in summary_counts.items():
        print(f" - {k}: {v} anomalies")
        
    # Write full JSON findings
    out_file = "phase0_global_scan_results.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "elapsed_seconds": elapsed,
            "total_files_scanned": len(all_json_files),
            "files_with_findings": len(results),
            "summary_counts": summary_counts,
            "results": results
        }, f, indent=2, ensure_ascii=False)
        
    print(f"Detailed results saved to {out_file}")

if __name__ == "__main__":
    main()
