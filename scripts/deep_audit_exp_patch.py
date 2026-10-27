import json
import re

p2_data = json.load(open("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json", encoding="utf-8"))

findings = []

for idx, e in enumerate(p2_data):
    orig = e.get("original") or ""
    trad = e.get("string") or ""
    fid = e.get("form_id")
    qtype = e.get("type")
    edid = e.get("editor_id")
    stage = e.get("index")

    # 1. Missing / None
    if not trad or e.get("status") == "TranslationRequired":
        findings.append({
            "idx": idx,
            "category": "MISSING",
            "entry": e,
            "detail": "Traduction manquante"
        })
        continue

    # 2. English remaining
    # Look for common English words not part of proper nouns
    english_words = ["the", "and", "with", "from", "that", "this", "have", "been", "upon", "once", "again", "sword", "chamber"]
    # Check lowercase tokens
    tokens = re.findall(r"\b[a-zA-Z]+\b", trad.lower())
    suspicious_en = [w for w in tokens if w in english_words]
    if len(suspicious_en) >= 3 and len(orig.split()) > 3:
        findings.append({
            "idx": idx,
            "category": "ENGLISH_TEXT",
            "entry": e,
            "detail": f"Texte en anglais détecté: {suspicious_en}"
        })

    # 3. Weird / Bad translations
    if orig == "A Dying Wish" and "suicidaires" in trad:
        findings.append({
            "idx": idx,
            "category": "LORE_MISTRANSLATION",
            "entry": e,
            "detail": "A Dying Wish traduit par 'Des envies suicidaires' au lieu de 'Dernières volontés'"
        })

    if "Dovahkiin qui murmurait" in trad:
        findings.append({
            "idx": idx,
            "category": "INVENTED_TERM",
            "entry": e,
            "detail": "Dovahkiin inventé pour 'Horse Whisperer' (officiel: L'homme qui murmurait à l'oreille des chevaux)"
        })

    if orig == "The Rising Dead" and trad == "Les morts-vivants":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel CC: Morts d'outre-tombe"
        })

    if orig == "Siege on the Dragon Cult" and trad == "Assiégez le Culte du Dragon":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel Skyrim: Le siège du culte des dragons"
        })

    if orig == "Unholy Vigil" and trad == "Le Vigile impie":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel CC: Veillée impie (vigil = veille/veillée)"
        })

    if orig == "A Soul Divided" and trad == "Âme scindée":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel CC: Âme divisée"
        })

    if orig == "In the Shadows" and trad == "Dans les ombres":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel CC: Dans l'ombre"
        })

    if orig == "Caught in a Web" and trad == "Pris au piège":
        findings.append({
            "idx": idx,
            "category": "OFFICIAL_TITLE",
            "entry": e,
            "detail": "Titre officiel CC: Pris dans la toile"
        })

    # Check for punctuation inconsistencies in objectives (some end with period, some not)
    # Check for placeholder leaks or syntax issues
    # Check for typos: "coeur" without ligature vs "cœur", "Soeur" vs "Sœur"
    # Check for "Temple of Dibella" in trad
    if "Temple of Dibella" in trad:
        findings.append({
            "idx": idx,
            "category": "UNTRANSLATED_TERM",
            "entry": e,
            "detail": "'Temple of Dibella' non traduit"
        })

print(f"Total findings: {len(findings)}")
for f in findings:
    print(f"[{f['category']}] Entry {f['idx']} ({f['entry'].get('form_id')}) {f['entry'].get('editor_id')}")
    print(f"  ORIG: {repr(f['entry'].get('original'))}")
    print(f"  TRAD: {repr(f['entry'].get('string'))}")
    print(f"  Detail: {f['detail']}")
