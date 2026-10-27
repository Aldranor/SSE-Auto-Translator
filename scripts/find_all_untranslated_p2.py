import json
import re

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

english_stopwords = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", 
    "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", 
    "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", 
    "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", 
    "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", 
    "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", 
    "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", 
    "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
}

untranslated = []
for idx, e in enumerate(data):
    s = e.get("string")
    orig = e.get("original")
    if not s:
        untranslated.append((idx, e, "Vide / None"))
        continue
    
    # Extract lower words
    words = re.findall(r"\b[a-zA-Z]{2,}\b", s.lower())
    if not words:
        continue
    
    en_count = sum(1 for w in words if w in english_stopwords)
    ratio = en_count / len(words)
    if ratio > 0.25 and len(words) > 5:
        untranslated.append((idx, e, f"Anglais détecté ({en_count}/{len(words)} stopwords)"))

print(f"Untranslated or English entries: {len(untranslated)}")
for u in untranslated:
    print(f"Entry {u[0]}: {u[2]}")
    print(f"  ORIG: {repr(u[1].get('original'))}")
    print(f"  TRAD: {repr(u[1].get('string'))}")
