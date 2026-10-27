import json
import re
from pathlib import Path
from collections import defaultdict

db = Path("data/user/database/french")

# English common words that strongly indicate a translatable English string
ENGLISH_WORDS = [
    "the", "of", "and", "in", "to", "for", "with", "from", "at", "by", "on", "about",
    "sword", "shield", "bow", "axe", "boots", "cuirass", "gauntlets", "helmet", "ring", "amulet",
    "armor", "armour", "cloak", "hood", "robes", "clothes", "dagger", "mace", "warhammer", "battleaxe",
    "arrow", "arrows", "bolt", "bolts", "quiver", "chest", "key", "door", "gate", "book", "journal",
    "letter", "note", "scroll", "staff", "potion", "poison", "ingredient", "pelt", "ore", "ingot",
    "damage", "health", "stamina", "magicka", "increase", "reduces?", "absorb", "restore", "resist",
    "points?", "seconds?", "percent", "you", "your", "they", "their", "we", "our", "he", "she",
    "when", "while", "after", "before", "during", "if", "then", "not", "no", "yes", "all", "each",
    "guard", "bandit", "thug", "citizen", "child", "boy", "girl", "soldier", "warrior", "mage",
    "witch", "vampire", "skeleton", "ghost", "spirit", "cultist", "necromancer", "hunter", "farmer",
    "miner", "prisoner", "beggar", "priest", "scout", "captain", "general", "commander", "elder",
    "master", "lord", "lady", "king", "queen", "assassin", "mercenary", "courier", "follower", "replica",
    "test version", "uses", "delete", "should never", "first place", "delivers", "upon returning"
]
ENGLISH_REGEX = re.compile(r"\b(" + "|".join(ENGLISH_WORDS) + r")\b", re.IGNORECASE)

INTERNAL_PATTERNS = [
    r"^<[^>]+>$",
    r"^\[[^\]]+\]$",
    r"^\$[a-zA-Z0-9_]+$",
    r"^\{[0-9]+\}$",
    r"^%[0-9]*[sdf]$",
    r"^[0-9\s\-_.:,;!?/\\|<>=\[\]\(\)\*#%+\'\"]+$",
    r"^[0-9a-zA-Z]+_[0-9a-zA-Z_]+$",
    r"^<img\s",
    r"^\[pagebreak\]"
]

def is_technical_variable(s):
    if not s:
        return True
    s = str(s).strip()
    if not s:
        return True
    if s == "[pagebreak]":
        return True
    if re.match(r"^<[^>]+>$", s) or re.match(r"^\[[^\]]+\]$", s) or re.match(r"^\$[a-zA-Z0-9_]+$", s):
        return True
    if re.match(r"^\{[0-9]+\}$", s) or re.match(r"^%[0-9]*[sdf]$", s):
        return True
    if re.match(r"^[0-9\s\-_.:,;!?/\\|<>=\[\]\(\)\*#%+\'\"]+$", s):
        return True
    if re.match(r"^[0-9a-zA-Z]+_[0-9a-zA-Z_]+$", s):
        return True
    # Only if it contains purely HTML tags and no actual English prose
    stripped_tags = re.sub(r"<[^>]+>", "", s)
    stripped_tags = stripped_tags.replace("[pagebreak]", "").strip()
    if not stripped_tags:
        return True
    return False

def is_npc_proper_name(item):
    if item.get("type") not in ("NPC_ FULL", "NPC_ SHRT"):
        return False
    orig = str(item.get("original") or "").strip()
    if not orig:
        return True
    # If contains common English title/profession/role, it's NOT a pure proper name
    if ENGLISH_REGEX.search(orig):
        return False
    return True

def is_engine_internal_dev(item):
    orig = str(item.get("original") or "").strip()
    t = item.get("type", "")
    
    # Internal dev quest names
    if t == "QUST FULL" and (orig.startswith("Dialogue") or "Startup" in orig or "Tracker" in orig or "Controller" in orig):
        return True
    
    # Dev / dummy effects / scripts
    if t in ("MGEF FULL", "SPEL FULL", "PERK FULL", "ACTI FULL", "MISC FULL", "TREE FULL"):
        if re.search(r"\b(dummy|template|controller|adjuster|monitor|cooldown|hidden|visual|marker|script|placeholder)\b", orig, re.I):
            return True
        # Code-like names: EquipTraderpackRed, RabbitWaterWalking, Speedmult
        if re.match(r"^[A-Z][a-z0-9]+([A-Z][a-z0-9]+)+$", orig):
            return True
            
    if t == "CELL FULL" and re.search(r"\b(test|warehouse|holding|dummy)\b", orig, re.I):
        return True
        
    return False

def check_item(item):
    orig = str(item.get("original") or "").strip()
    t = item.get("type", "")
    
    if is_technical_variable(orig):
        return ("tech_var", orig)
        
    if is_npc_proper_name(item):
        return ("npc_name", orig)
        
    if is_engine_internal_dev(item):
        return ("internal_dev", orig)
        
    # Long text / sentences / dialogue / book / quest log
    if t in ("INFO NAM1", "BOOK DESC", "QUST CNAM", "QUST NNAM", "MESG ITXT") or len(orig.split()) > 3:
        if ENGLISH_REGEX.search(orig):
            return ("translatable_text", orig)
            
    # Check English words
    if ENGLISH_REGEX.search(orig):
        return ("translatable_word", orig)
        
    # Single fantasy words (e.g. Aerondight, Atricor, Nagamaki)
    if len(orig.split()) == 1:
        return ("proper_noun", orig)
        
    # Default: needs check
    return ("needs_review", orig)

mods_analysis = []

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
            
        categories = defaultdict(list)
        for s in incomplete:
            cat, orig = check_item(s)
            categories[cat].append((s.get("type"), orig))
            
        mods_analysis.append({
            "mod": mod_dir.name,
            "file": f.name,
            "total_incomplete": len(incomplete),
            "categories": {k: len(v) for k, v in categories.items()},
            "cat_details": {k: v[:5] for k, v in categories.items()}
        })

print(f"Total mods/files analyzed: {len(mods_analysis)}")

# Filter pure false positives:
# Only contains tech_var, npc_name, internal_dev, proper_noun
pure_false_positives = []
has_translatable = []

for m in mods_analysis:
    cats = m["categories"]
    trans_count = cats.get("translatable_text", 0) + cats.get("translatable_word", 0) + cats.get("needs_review", 0)
    if trans_count == 0:
        pure_false_positives.append(m)
    else:
        has_translatable.append(m)

print(f"Pure false positives (NO translation needed): {len(pure_false_positives)}")
print(f"Has real translatable content: {len(has_translatable)}")

with open("detailed_analysis.json", "w", encoding="utf-8") as out:
    json.dump({
        "pure_false_positives": pure_false_positives,
        "has_translatable": has_translatable
    }, out, indent=2, ensure_ascii=False)
