import os
import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

# Define keyword mapping pairs: (concept_name, [en_keywords], [fr_keywords])
concept_mappings = [
    ('allies', ['allies', 'ally', 'nearby friends'], ['alliés', 'allié', 'compagnon']),
    ('dual_cast', ['dual cast', 'dual-cast'], ['double lancer', 'deux mains', 'lancer double']),
    ('paralysis', ['paralyze', 'paralysis'], ['paralys', 'paralysie', 'paralyse']),
    ('stagger', ['stagger'], ['déstabilis', 'déséquilibr', 'vacill']),
    ('fall_damage', ['falling damage', 'fall damage'], ['chute']),
    ('shout', ['shout', 'shouts', 'cooldown'], ['cri', 'cris', 'temps de recharge']),
    ('unarmed', ['unarmed', 'fists', 'brawling'], ['mains nues', 'poings']),
    ('sprint', ['sprint', 'running'], ['sprint', 'course', 'courir']),
    ('shield_charge', ['shield charge'], ['charge de bouclier', 'charge au bouclier']),
    ('disarm', ['disarm'], ['désarm']),
    ('reflect', ['reflect'], ['renvoi', 'réfléch']),
    ('absorb', ['absorb', 'absorption'], ['absorb']),
    ('invisibility', ['invisib'], ['invisib']),
    ('resurrect', ['reanimate', 'resurrect', 'zombie'], ['réanim', 'ressuscit', 'zombie']),
    ('soul_trap', ['soul trap', 'fill.*soul gem'], ['capture d\'âme', 'gemme spirituelle']),
    ('silent', ['silent', 'quiet'], ['silencieux', 'discret', 'bruit']),
    ('craft', ['craft', 'forge', 'smithing', 'temper'], ['forg', 'artisanat', 'amélio']),
    ('pickpocket', ['pickpocket', 'steal'], ['vol à la tire', 'dérober', 'subtilis']),
    ('lockpick', ['lockpick', 'locks', 'lock'], ['crochet', 'serrur']),
]

mismatches = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            rec_type = s.get('type') or ''
            # Target perks, spells, magic effects, enchantments, potions
            if not any(t in rec_type for t in ['PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH']):
                continue
            
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            
            if not trans or not orig or trans == orig:
                continue
            
            # Check for concept mismatch
            orig_lower = orig.lower()
            trans_lower = trans.lower()
            
            # Find concepts present in EN
            en_concepts = set()
            for c_name, en_words, fr_words in concept_mappings:
                if any(re.search(r'\b' + re.escape(w) + r'\b', orig_lower) for w in en_words):
                    en_concepts.add(c_name)
                    
            # Find concepts present in FR
            fr_concepts = set()
            for c_name, en_words, fr_words in concept_mappings:
                if any(w in trans_lower for w in fr_words):
                    fr_concepts.add(c_name)
                    
            # Check if there is a severe mismatch:
            # Concept in EN not in FR, or concept in FR not in EN
            missing_in_fr = en_concepts - fr_concepts
            extra_in_fr = fr_concepts - en_concepts
            
            # If length ratio is extreme (e.g. EN is 20 words, FR is 5 words or vice versa)
            en_len = len(orig.split())
            fr_len = len(trans.split())
            len_ratio = max(en_len, fr_len) / max(1, min(en_len, fr_len))
            
            if (missing_in_fr and extra_in_fr) or (len_ratio > 2.5 and en_len > 10):
                mismatches.append({
                    'mod': p.parent.name,
                    'file': p.name,
                    'form_id': form_id,
                    'type': rec_type,
                    'original': orig,
                    'translation': trans,
                    'en_concepts': list(en_concepts),
                    'fr_concepts': list(fr_concepts),
                    'len_ratio': round(len_ratio, 2)
                })
    except Exception:
        pass

print(f"Total concept/alignment mismatches found: {len(mismatches)}")
with open('concept_mismatches.json', 'w', encoding='utf-8') as f:
    json.dump(mismatches, f, indent=2, ensure_ascii=False)
