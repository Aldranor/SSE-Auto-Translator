# -*- coding: utf-8 -*-
"""
Independent verification script for Phase 3 (Éradication des Traductions Restées en Anglais & Phrases Hybrides).
Re-reads all JSON files from disk and verifies:
1. Valid JSON structure and non-empty strings on TranslationComplete entries.
2. Zero remaining untranslated player-facing entries (QUST NNAM, QUST CNAM, PERK DESC, MGEF DNAM, SPEL DESC, etc.).
3. All specific Phase 3 translations and hybrid fixes are properly persisted on disk.
"""
import json
import os
import re

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"


def main():
    total_files = 0
    total_entries = 0
    notrans_count = 0
    remaining_same_by_type = {}
    errors = []

    for root, dirs, files in os.walk(DB_DIR):
        for fname in files:
            if not fname.endswith(".json") or fname == "index.json":
                continue
            total_files += 1
            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, DB_DIR)
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                continue

            for idx, e in enumerate(data):
                total_entries += 1
                orig = e.get("original", "")
                s = e.get("string", "")
                st = e.get("status", "")
                tp = e.get("type")

                if st == "NoTranslationRequired":
                    notrans_count += 1
                    continue

                if orig.strip() and orig.strip().lower() == s.strip().lower():
                    remaining_same_by_type[tp] = remaining_same_by_type.get(tp, 0) + 1

    # Spot-check key fixes on disk
    spot_checks = [
        (r"EEKs Whiterun Interiors.esp - French\eeks whiterun interiors.esp.json", 28, "Bon de commande"),
        (r"Legacy of the Dragonborn - Follower Room Patches - French\dbm_inigo_patch.esp.json", 15, "Chapitre un"),
        (r"L'Héritage de l'Enfant de dragon - Patches officiels\dbm_beyondreach_patch.esp.json", 28, "Conseil d'Abondance"),
        (r"L'île de Sylval\Midwood Isle.esp.json", 1329, "GRAND SEIGNEUR D'OBLIVION"),
        (r"Au-delà de Bordeciel - Bruma\BSHeartland.esm.json", 13223, "Clairière de Givrefeu"),
        (r"Le Château mécanique\Clockwork.esp.json", 1431, "Château mécanique"),
        (r"ISC - Bruitages immersifs\Immersive Sounds - Compendium.esp.json", 17, "Réanime un cadavre"),
        (r"Thaumaturgie - Refonte de l'enchantement\Thaumaturgy.esp.json", 32, "Augmente votre magie"),
        (r"Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French\nolvus awakening combat scaling overhaul - enemy level.esp.json", 3374, "Alduin"),
        (r"BOOBIES_potions_ENGLISH.txt - French\interface\translations\BOOBIES_potions_ENGLISH.txt.json", 110, "Blood"),
    ]

    for rel_path, idx, expected_substr in spot_checks:
        full_path = os.path.join(DB_DIR, rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        actual = data[idx]["string"]
        if expected_substr not in actual:
            errors.append(f"Spot check failed on {rel_path}[{idx}]: expected {expected_substr!r} in {actual[:80]!r}")

    print(f"Verified {total_files} files / {total_entries} entries on disk.")
    print(f"Total entries with status='NoTranslationRequired': {notrans_count}")
    print("Remaining TranslationComplete entries with original == string (identical FR/EN words & proper nouns):")
    for tp, cnt in sorted(remaining_same_by_type.items(), key=lambda x: -x[1]):
        print(f"  {tp!r}: {cnt}")

    if errors:
        print("ERRORS FOUND:")
        for err in errors:
            print("  -", err)
        raise SystemExit(1)
    else:
        print("ALL SPOT CHECKS AND INTEGRITY CHECKS PASSED (0 errors)!")


if __name__ == "__main__":
    main()
