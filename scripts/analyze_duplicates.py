#!/usr/bin/env python3
"""
Analyze resume.json for semantic duplicates
"""

import json
from collections import defaultdict
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate similarity ratio between two strings"""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def load_resume():
    """Load the resume JSON file"""
    with open('/Users/markschulz/Documents/My_Documents/My Coding/markschulz/assets/data/resume.json', 'r') as f:
        return json.load(f)

def extract_all_achievements(data):
    """Extract all achievements with their location metadata"""
    achievements = []

    for exp in data['experience']:
        company = exp['company']
        for pos in exp['positions']:
            title = pos['title']
            for cat in pos.get('achievements', []):
                category = cat.get('category', 'Unknown')
                for item in cat.get('items', []):
                    text = item.get('text', '') if isinstance(item, dict) else item
                    achievements.append({
                        'text': text,
                        'company': company,
                        'title': title,
                        'category': category,
                        'full_item': item,
                        'exp_id': exp['id'],
                        'position_obj': pos
                    })

    return achievements

def find_potential_duplicates(achievements, threshold=0.75):
    """Find achievements that are similar above threshold"""
    duplicates = []
    seen = set()

    for i, ach1 in enumerate(achievements):
        if i in seen:
            continue

        group = [ach1]

        for j, ach2 in enumerate(achievements[i+1:], i+1):
            if j in seen:
                continue

            sim = similarity(ach1['text'], ach2['text'])

            if sim >= threshold:
                group.append(ach2)
                seen.add(j)

        if len(group) > 1:
            duplicates.append(group)
            seen.add(i)

    return duplicates

def main():
    data = load_resume()
    achievements = extract_all_achievements(data)

    print(f"Total achievements found: {len(achievements)}")
    print("\n" + "="*80)
    print("SEARCHING FOR DUPLICATES")
    print("="*80)

    # Find high similarity duplicates (likely same achievement)
    high_sim = find_potential_duplicates(achievements, threshold=0.75)

    print(f"\n\nFound {len(high_sim)} groups of potential duplicates (75%+ similarity):\n")

    for i, group in enumerate(high_sim, 1):
        print(f"\n{'='*80}")
        print(f"DUPLICATE GROUP {i} ({len(group)} instances):")
        print('='*80)

        for ach in group:
            print(f"\nCompany: {ach['company']}")
            print(f"Position: {ach['title']}")
            print(f"Category: {ach['category']}")
            print(f"Text: {ach['text'][:200]}{'...' if len(ach['text']) > 200 else ''}")

        print()

    # Also look for medium similarity (50-75%) for manual review
    print("\n\n" + "="*80)
    print("MEDIUM SIMILARITY (50-75%) - MANUAL REVIEW NEEDED")
    print("="*80)

    medium_sim = find_potential_duplicates(achievements, threshold=0.50)
    # Filter out those already in high_sim
    medium_only = [g for g in medium_sim if len(g) > 1 and g not in high_sim]

    print(f"\nFound {len(medium_only)} groups needing manual review:\n")

    for i, group in enumerate(medium_only[:10], 1):  # Show first 10
        print(f"\n{'='*80}")
        print(f"REVIEW GROUP {i} ({len(group)} instances):")
        print('='*80)

        for ach in group:
            print(f"\nCompany: {ach['company']}")
            print(f"Position: {ach['title']}")
            print(f"Text: {ach['text'][:150]}{'...' if len(ach['text']) > 150 else ''}")

if __name__ == '__main__':
    main()
