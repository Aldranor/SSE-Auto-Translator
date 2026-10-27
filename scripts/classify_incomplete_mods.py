import json
import re
from pathlib import Path
from collections import defaultdict

db = Path("data/user/database/french")

# Common English words indicating translatable content
ENGLISH_INDICATORS = [
    r"\bthe\b", r"\bof\b", r"\band\b", r"\bin\b", r"\bto\b", r"\bfor\b", r"\bwith\b",
    r"\bfrom\b", r"\byou\b", r"\byour\b", r"\bthis\b", r"\bthat\b", r"\bhave\b",
    r"\bhas\b", r"\bwill\b", r"\bcan\b", r"\bwhen\b", r"\bwhile\b", r"\bafter\b",
    r"\bbefore\b", r"\bsword\b", r"\bshield\b", r"\bbow\b", r"\baxe\b", r"\bboots\b",
    r"\bcuirass\b", r"\bgauntlets\b", r"\bhelmet\b", r"\bring\b", r"\bamulet\b",
    r"\bscroll\b", r"\bstaff\b", r"\bpotion\b", r"\bpoison\b", r"\bchest\b", r"\bkey\b",
    r"\bbook\b", r"\bjournal\b", r"\bletter\b", r"\bnote\b", r"\bdamage\b", r"\bhealth\b",
    r"\bstamina\b", r"\bmagicka\b", r"\bincrease\b", r"\breduce\b", r"\babsorb\b",
    r"\brestore\b", r"\bresist\b", r"\bpoints?\b", r"\bseconds?\b", r"\bpercent\b"
]
ENGLISH_REGEX = re.compile("|".join(ENGLISH_INDICATORS), re.IGNORECASE)

INTERNAL_KEYWORD_REGEX = re.compile(
    r"\b(dummy|template|controller|adjuster|monitor|cooldown|test|hidden|visual|sound|marker|script|placeholder|startup|tracker)\b",
    re.IGNORECASE
)

def is_technical_or_variable(s):
    if not s:
        return True
    s = str(s).strip()
    if not s:
        return True
    if re.match(r"^<[^>]+>$", s) or re.match(r"^\[[^\]]+\]$", s) or re.match(r"^\$[a-zA-Z0-9_]+$", s):
        return True
    if re.match(r"^\{[0-9]+\}$", s) or re.match(r"^%[0-9]*[sdf]$", s):
        return True
    if re.match(r"^[0-9\s\-_.:,;!?/\\|<>=\[\]\(\)\*#%+\'\"]+$", s):
        return True
    if re.match(r"^[a-zA-Z0-9]+_[a-zA-Z0-9_]+$", s):
        return True
    if s.startswith("<img") or s.startswith("[pagebreak]"):
        return True
    return False

def is_npc_proper_name(item):
    t = item.get("type", "")
    if t not in ("NPC_ FULL", "NPC_ SHRT"):
        return False
    orig = str(item.get("original") or "").strip()
    if not orig:
        return True
    
    # Common generic NPC roles that need translation
    generic_roles = [
        "guard", "bandit", "thug", "citizen", "child", "boy", "girl", "soldier", "warrior", "mage",
        "witch", "vampire", "skeleton", "ghost", "spirit", "cultist", "necromancer", "hunter",
        "farmer", "fisherman", "miner", "prisoner", "beggar", "priest", "patrol", "scout", "captain",
        "general", "commander", "elder", "apprentice", "adept", "master", "lord", "lady", "king",
        "queen", "assassin", "mercenary", "courier", "traveler", "pilgrim", "follower", "corpse",
        "dog", "wolf", "horse", "bear", "cat", "chicken", "cow", "goat", "spider", "mudcrab",
        "troll", "giant", "dragon", "hagraven", "draugr", "atronach", "dremora", "daedra", "phantom"
    ]
    orig_lower = orig.lower()
    for role in generic_roles:
        if re.search(r"\b" + re.escape(role) + r"\b", orig_lower):
            return False
    if re.search(r"\b(of|the|in|from|and|with)\b", orig_lower):
        return False
    
    return True

def is_internal_or_dev_string(item):
    orig = str(item.get("original") or "").strip()
    t = item.get("type", "")
    
    # Internal quest names for dialogue/startup
    if t == "QUST FULL" and (orig.startswith("Dialogue") or "Startup" in orig or "Tracker" in orig or "Controller" in orig):
        return True
    
    # Hidden / dummy / visual effects
    if t in ("MGEF FULL", "SPEL FULL", "PERK FULL", "ACTI FULL", "MISC FULL", "TREE FULL"):
        if INTERNAL_KEYWORD_REGEX.search(orig):
            return True
        # Things like HedgeColumn, RabbitWaterWalking, Speedmult
        if re.match(r"^[A-Z][a-zA-Z0-9]+[A-Z][a-zA-Z0-9]+$", orig): # PascalCase code-like
            return True
            
    # Cells that are test rooms
    if t == "CELL FULL" and ("Test" in orig or "Warehouse" in orig or "Holding" in orig):
        return True
        
    return False

def classify_string(item):
    orig = str(item.get("original") or "").strip()
    trans = str(item.get("string") or "").strip()
    t = item.get("type", "")
    
    if is_technical_or_variable(orig):
        return "tech_var"
    if is_npc_proper_name(item):
        return "npc_proper_name"
    if is_internal_or_dev_string(item):
        return "internal_dev"
    if orig.lower() == trans.lower() and trans:
        return "identical_valid"
    
    # Dialogue, books, messages, quest logs are definitely player-facing
    if t in ("INFO NAM1", "BOOK DESC", "QUST CNAM", "QUST NNAM", "MESG ITXT") or (t == "MESG FULL" and len(orig.split()) > 2):
        return "must_translate"
    
    # Check if English words
    if ENGLISH_REGEX.search(orig):
        return "must_translate"
    
    # Single fantasy words (e.g. unique weapon names like Clanbringer, Aerondight)
    if len(orig.split()) == 1 and t in ("WEAP FULL", "ARMO FULL", "INGR FULL", "ALCH FULL", "SPEL FULL"):
        return "proper_item_name"
        
    return "other_review"

classified_mods = {
    "NO_TRANSLATION_NEEDED": [], # 100% variables, NPC proper names, internal records, proper item names
    "HAS_REAL_STRINGS": []       # Contains actual translatable English text / player-facing content
}

for mod_dir in sorted(db.iterdir()):
    if not mod_dir.is_dir():
        continue
    for f in mod_dir.glob("*.json"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except Exception:
            continue
            
        incomplete = [s for s in data if s.get("status") in ("TranslationIncomplete", "TranslationRequired")]
        if not incomplete:
            continue
            
        class_counts = defaultdict(int)
        reasons = defaultdict(list)
        must_translate_items = []
        
        for s in incomplete:
            c = classify_string(s)
            class_counts[c] += 1
            if c in ("must_translate", "other_review"):
                must_translate_items.append(s)
            else:
                reasons[c].append(str(s.get("original") or ""))
                
        mod_entry = {
            "mod": mod_dir.name,
            "file": f.name,
            "total_incomplete": len(incomplete),
            "counts": dict(class_counts),
            "sample_skipped": {k: v[:3] for k, v in reasons.items()},
            "must_translate_samples": [f"[{s.get('type')}] {s.get('original')}" for s in must_translate_items[:6]]
        }
        
        if len(must_translate_items) == 0:
            classified_mods["NO_TRANSLATION_NEEDED"].append(mod_entry)
        else:
            classified_mods["HAS_REAL_STRINGS"].append(mod_entry)

print(f"Mods/files requiring NO translation (pure false positives): {len(classified_mods['NO_TRANSLATION_NEEDED'])}")
print(f"Mods/files having REAL strings to translate: {len(classified_mods['HAS_REAL_STRINGS'])}")

with open("classification_results.json", "w", encoding="utf-8") as out:
    json.dump(classified_mods, out, indent=2, ensure_ascii=False)
