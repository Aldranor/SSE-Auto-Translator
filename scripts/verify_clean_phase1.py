import json
import os
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.join("data", "user", "database", "french")

GLOBAL_RE = re.compile(r"<Global(?:\.[a-zA-Z]+)?=([^>\s]+)>", re.IGNORECASE)
MAG_DUR_RE = re.compile(r"<(mag|dur|area)>", re.IGNORECASE)
PRINTF_RE = re.compile(r"%[0-9.]*[sdfi]")
NUM_BRACKET_RE = re.compile(r"<(\d+)%?>")
FONT_FACE_RE = re.compile(r"face=['\"]([^'\"]+)['\"]", re.IGNORECASE)

VALID_FONTS = {
    "$handwrittenfont", "$dwemerfont", "$handwrittenbold", "$dragonfont",
    "$daedricfont", "$skyrimbooks", "$magescriptfont", "$falmerfont",
    "$skyrimbooks_unreadablefont", "$printedfont"
}

empty_strings = []
spliced_tags = []
bad_globals = []
bad_mag_dur = []
bad_printf = []
bad_num_brackets = []
bad_fonts = []
bad_imgs_or_pb = []

total_files = 0
total_records = 0

for root, _, files in os.walk(ROOT):
    if ".git" in root:
        continue
    for fn in files:
        if not fn.endswith(".json") or fn == "index.json":
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, ROOT)
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            continue
        total_files += 1
        for e in data:
            total_records += 1
            orig = e.get("original") or ""
            curr = e.get("string") or ""
            fid = e.get("form_id") or ""
            t = e.get("type") or ""
            idx = e.get("index")

            if not orig.strip():
                continue

            # 1. Empty string
            if not curr.strip():
                empty_strings.append((rel, fid, t, idx, orig))
                continue

            # 2. Spliced / corrupted tags
            if (
                "<<" in curr
                or (">>" in curr and curr != "-->>")
                or re.search(r"[a-wyzA-WYZéèêàù]<[0-9]", curr)
                or re.search(r"<[0-9]+>[0-9]", curr)
                or "<dur>s" in curr
                or "< alias=" in curr.lower()
                or (
                    orig.count("<") == orig.count(">")
                    and curr.count("<") != curr.count(">")
                    and t != "BOOK DESC"
                    and " > " not in curr
                    and "ou >." not in curr
                )
            ):
                spliced_tags.append((rel, fid, t, idx, orig, curr))

            # 3. Bad Global variable name in curr
            o_glob = Counter(m.lower() for m in GLOBAL_RE.findall(orig))
            c_glob = Counter(m.lower() for m in GLOBAL_RE.findall(curr))
            extra_glob = set(c_glob.keys()) - set(o_glob.keys())
            if extra_glob and not (fid == "0205E483|Falskaar.esm"):
                bad_globals.append((rel, fid, t, idx, dict(o_glob), dict(c_glob)))

            # 4. <mag>, <dur>, <area> mismatch
            o_md = Counter(m.lower() for m in MAG_DUR_RE.findall(orig))
            c_md = Counter(m.lower() for m in MAG_DUR_RE.findall(curr))
            if o_md != c_md and fid != "030C0029|Apocalypse - Magic of Skyrim.esp":
                bad_mag_dur.append((rel, fid, t, idx, dict(o_md), dict(c_md)))

            # 5. printf mismatch
            o_pf = Counter(PRINTF_RE.findall(orig))
            c_pf = Counter(PRINTF_RE.findall(curr))
            if o_pf != c_pf:
                bad_printf.append((rel, fid, t, idx, dict(o_pf), dict(c_pf)))

            # 6. Illegal <num> brackets
            o_nb = NUM_BRACKET_RE.findall(orig)
            c_nb = NUM_BRACKET_RE.findall(curr)
            if c_nb and not o_nb:
                bad_num_brackets.append((rel, fid, t, idx, o_nb, c_nb))

            # 7. Bad font names
            for ff in FONT_FACE_RE.findall(curr):
                if ff.lower() not in VALID_FONTS:
                    bad_fonts.append((rel, fid, t, idx, ff))

            # 8. Corrupted image paths or pagebreaks
            if any(bad in curr for bad in (
                "Illuminated_Letters0", "sirencoronet. png", "/Livres/",
                "temper_fr.png", "\npagebreak]", "[pause]"
            )):
                bad_imgs_or_pb.append((rel, fid, t, idx))

print(f"Scanned {total_files} files ({total_records} records).")
print(f"1. Empty strings remaining: {len(empty_strings)}")
print(f"2. Spliced/corrupted tags remaining: {len(spliced_tags)}")
for x in spliced_tags:
    print("  ", x)
print(f"3. Corrupted <Global=...> names remaining: {len(bad_globals)}")
for x in bad_globals:
    print("  ", x)
print(f"4. <mag>/<dur>/<area> mismatches remaining: {len(bad_mag_dur)}")
for x in bad_mag_dur:
    print("  ", x)
print(f"5. printf mismatches remaining: {len(bad_printf)}")
for x in bad_printf:
    print("  ", x)
print(f"6. Illegal <num> brackets remaining: {len(bad_num_brackets)}")
for x in bad_num_brackets:
    print("  ", x)
print(f"7. Invalid font faces remaining: {len(bad_fonts)}")
for x in bad_fonts:
    print("  ", x)
print(f"8. Broken image paths / malformed pagebreaks remaining: {len(bad_imgs_or_pb)}")
for x in bad_imgs_or_pb:
    print("  ", x)
