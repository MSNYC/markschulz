#!/usr/bin/env python3
"""
Tag Validation Script
Validates tag coverage and quality for interactive resume builder
Usage: python3 scripts/validate_tags.py
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

def load_data():
    """Load resume and profiles data"""
    with open('data/resume.json') as f:
        resume = json.load(f)
    with open('data/resume_profiles.json') as f:
        profiles = json.load(f)
    return resume, profiles

def extract_all_tags(resume):
    """Extract all tags from resume achievements"""
    all_tags = []
    untagged_items = []

    for exp in resume['experience']:
        for position in exp['positions']:
            for achievement in position.get('achievements', []):
                if isinstance(achievement, dict) and 'items' in achievement:
                    for item in achievement['items']:
                        if isinstance(item, dict) and 'tags' in item:
                            all_tags.extend(item['tags'])
                        elif isinstance(item, dict):
                            untagged_items.append({
                                'company': exp['company'],
                                'category': achievement.get('category', 'Unknown'),
                                'text': item.get('text', str(item))[:80]
                            })

    return all_tags, untagged_items

def analyze_tag_coverage(all_tags, profiles):
    """Analyze how well tags cover profile priority tags"""
    tag_counts = Counter(all_tags)

    print("=" * 70)
    print("TAG COVERAGE ANALYSIS")
    print("=" * 70)

    print(f"\n📊 Overall Statistics:")
    print(f"  Total tags used: {len(all_tags)}")
    print(f"  Unique tags: {len(tag_counts)}")
    print(f"  Average tags per item: {len(all_tags) / max(len(set(all_tags)), 1):.1f}")

    print(f"\n🏆 Top 15 Most Used Tags:")
    for tag, count in tag_counts.most_common(15):
        bar = "█" * (count // 2)
        print(f"  {tag:25} {count:3} {bar}")

    # Check coverage for each profile
    print(f"\n🎯 Profile Tag Coverage:")
    for profile in profiles['profiles']:
        print(f"\n  {profile['label']} ({profile['id']}):")
        priority_tags = profile['priority_tags']

        matched_tags = []
        missing_tags = []

        for tag in priority_tags:
            count = tag_counts.get(tag, 0)
            if count > 0:
                matched_tags.append((tag, count))
            else:
                missing_tags.append(tag)

        print(f"    ✓ Matched: {len(matched_tags)}/{len(priority_tags)} priority tags")

        if matched_tags:
            print(f"    Top matches:")
            for tag, count in sorted(matched_tags, key=lambda x: x[1], reverse=True)[:5]:
                print(f"      • {tag}: {count} bullets")

        if missing_tags:
            print(f"    ⚠ Missing priority tags (no bullets): {', '.join(missing_tags)}")

    # Identify orphan tags (used but not in any profile)
    all_priority_tags = set()
    for profile in profiles['profiles']:
        all_priority_tags.update(profile['priority_tags'])

    orphan_tags = set(tag_counts.keys()) - all_priority_tags
    if orphan_tags:
        print(f"\n⚠ Orphan Tags (used but not in any profile priority_tags):")
        for tag in sorted(orphan_tags):
            print(f"    • {tag}: {tag_counts[tag]} bullets")

def check_untagged_items(untagged_items):
    """Report items missing tags"""
    if untagged_items:
        print(f"\n" + "=" * 70)
        print(f"⚠ UNTAGGED ITEMS ({len(untagged_items)} found)")
        print("=" * 70)

        for item in untagged_items:
            print(f"\n  Company: {item['company']}")
            print(f"  Category: {item['category']}")
            print(f"  Text: {item['text']}...")
    else:
        print(f"\n" + "=" * 70)
        print(f"✅ All items are tagged!")
        print("=" * 70)

def analyze_tag_distribution(all_tags):
    """Analyze tag distribution across categories"""
    tag_counts = Counter(all_tags)

    print(f"\n📈 Tag Distribution:")
    print(f"  Tags used 1-2 times: {sum(1 for c in tag_counts.values() if c <= 2)}")
    print(f"  Tags used 3-5 times: {sum(1 for c in tag_counts.values() if 3 <= c <= 5)}")
    print(f"  Tags used 6-10 times: {sum(1 for c in tag_counts.values() if 6 <= c <= 10)}")
    print(f"  Tags used 11+ times: {sum(1 for c in tag_counts.values() if c > 10)}")

    # Tags that may need review (too few or too many uses)
    underused = [tag for tag, count in tag_counts.items() if count == 1]
    if underused:
        print(f"\n⚠ Single-use tags (consider if they're useful):")
        print(f"    {', '.join(sorted(underused))}")

def simulate_profile_filtering(resume, profiles):
    """Simulate how many bullets each profile would show"""
    print(f"\n" + "=" * 70)
    print(f"🔍 PROFILE FILTERING SIMULATION")
    print("=" * 70)

    for profile in profiles['profiles']:
        print(f"\n{profile['label']} ({profile['id']}):")
        priority_tags = set(profile['priority_tags'])

        total_bullets = 0
        matched_bullets = 0

        for exp in resume['experience']:
            for position in exp['positions']:
                for achievement in position.get('achievements', []):
                    if isinstance(achievement, dict) and 'items' in achievement:
                        for item in achievement['items']:
                            if isinstance(item, dict) and 'tags' in item:
                                total_bullets += 1
                                item_tags = set(item['tags'])
                                score = len(item_tags & priority_tags)
                                if score > 0:
                                    matched_bullets += 1

        match_rate = (matched_bullets / total_bullets * 100) if total_bullets > 0 else 0
        print(f"  Matched: {matched_bullets}/{total_bullets} bullets ({match_rate:.1f}%)")

        if match_rate < 40:
            print(f"  ⚠ Low match rate - consider adding more tags")
        elif match_rate > 70:
            print(f"  ✓ Good match rate")

def main():
    resume, profiles = load_data()

    all_tags, untagged_items = extract_all_tags(resume)

    analyze_tag_coverage(all_tags, profiles)
    check_untagged_items(untagged_items)
    analyze_tag_distribution(all_tags)
    simulate_profile_filtering(resume, profiles)

    print(f"\n" + "=" * 70)
    print(f"✅ Validation Complete")
    print("=" * 70)

if __name__ == '__main__':
    main()
