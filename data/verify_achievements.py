#!/usr/bin/env python3
"""
Achievement Verification Tool
Analyzes tag coverage and differentiation potential across resume profiles
"""

import json
from pathlib import Path
from collections import defaultdict, Counter

def load_json(filepath):
    """Load and parse JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_all_tags_from_position(position):
    """Extract all tags from a position's achievements"""
    tags = []
    for category in position.get('achievements', []):
        for item in category.get('items', []):
            tags.extend(item.get('tags', []))
    return tags

def analyze_resume():
    """Analyze achievement coverage in resume.json"""

    # Load resume data
    resume_path = Path(__file__).parent / 'resume.json'
    resume_data = load_json(resume_path)

    # Load profile data
    profiles_path = Path(__file__).parent / 'resume_profiles.json'
    if profiles_path.exists():
        profiles_data = load_json(profiles_path)
        profiles = profiles_data.get('profiles', [])
    else:
        profiles = []
        print("⚠️  resume_profiles.json not found - skipping profile analysis\n")

    print("=" * 80)
    print("ACHIEVEMENT COVERAGE ANALYSIS")
    print("=" * 80)

    # Analyze each experience
    for exp in resume_data['experience']:
        company = exp['company']
        print(f"\n📍 {company}")
        print("-" * 80)

        for pos in exp['positions']:
            title = pos['title']
            start = pos['start_date']
            end = pos['end_date'] or 'Present'

            achievements = pos.get('achievements', [])
            total_categories = len(achievements)
            total_items = sum(len(cat.get('items', [])) for cat in achievements)

            # Get all tags
            all_tags = get_all_tags_from_position(pos)
            unique_tags = set(all_tags)
            tag_counts = Counter(all_tags)

            print(f"\n  {title} ({start} – {end})")
            print(f"  ├─ Achievement categories: {total_categories}")
            print(f"  ├─ Total achievements: {total_items}")
            print(f"  ├─ Unique tags: {len(unique_tags)}")

            if unique_tags:
                print(f"  └─ Tag breakdown:")
                # Show top tags
                for tag, count in tag_counts.most_common(10):
                    print(f"      • {tag}: {count}")
            else:
                print(f"  └─ ⚠️  NO TAGS - This position needs achievement extraction!")

    # Profile-specific analysis
    if profiles:
        print("\n" + "=" * 80)
        print("PROFILE DIFFERENTIATION POTENTIAL")
        print("=" * 80)

        for profile in profiles:
            profile_id = profile['id']
            profile_name = profile['name']
            priority_tags = set(profile.get('priority_tags', []))

            print(f"\n📋 {profile_name}")
            print("-" * 80)

            # Analyze tag coverage for each position
            position_scores = []

            for exp in resume_data['experience']:
                for pos in exp['positions']:
                    title = pos['title']
                    company = exp['company']
                    all_tags = set(get_all_tags_from_position(pos))

                    # Calculate overlap with profile priority tags
                    overlap = all_tags & priority_tags
                    overlap_count = len(overlap)

                    if all_tags:  # Only show positions with tags
                        coverage_pct = (overlap_count / len(priority_tags) * 100) if priority_tags else 0
                        position_scores.append({
                            'title': title,
                            'company': company,
                            'overlap_count': overlap_count,
                            'coverage_pct': coverage_pct,
                            'overlapping_tags': overlap
                        })

            # Sort by overlap count (descending)
            position_scores.sort(key=lambda x: x['overlap_count'], reverse=True)

            # Show top positions for this profile
            print(f"  Priority tags ({len(priority_tags)}): {', '.join(sorted(priority_tags))}\n")

            if position_scores:
                print(f"  Top positions for this profile:")
                for i, score in enumerate(position_scores[:5], 1):
                    icon = "🟢" if score['coverage_pct'] > 30 else "🟡" if score['coverage_pct'] > 15 else "🔴"
                    print(f"    {i}. {icon} {score['title']} @ {score['company']}")
                    print(f"       Tag overlap: {score['overlap_count']} ({score['coverage_pct']:.0f}% coverage)")
                    print(f"       Matching tags: {', '.join(sorted(score['overlapping_tags']))}")
            else:
                print(f"  ⚠️  NO POSITIONS WITH TAGS for this profile yet!")

    # Summary recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)

    positions_without_achievements = []
    positions_without_tags = []

    for exp in resume_data['experience']:
        for pos in exp['positions']:
            achievements = pos.get('achievements', [])
            total_items = sum(len(cat.get('items', [])) for cat in achievements)
            all_tags = get_all_tags_from_position(pos)

            if total_items == 0:
                positions_without_achievements.append(f"{pos['title']} @ {exp['company']}")
            elif len(all_tags) == 0:
                positions_without_tags.append(f"{pos['title']} @ {exp['company']}")

    if positions_without_achievements:
        print("\n⚠️  Positions needing achievement extraction:")
        for pos_name in positions_without_achievements:
            print(f"   • {pos_name}")
        print("\n   → Use the extraction schema to add achievements for these roles")

    if positions_without_tags:
        print("\n⚠️  Positions with achievements but NO tags:")
        for pos_name in positions_without_tags:
            print(f"   • {pos_name}")
        print("\n   → These achievements need tags to enable profile filtering")

    if not positions_without_achievements and not positions_without_tags:
        print("\n✅ All positions have tagged achievements!")
        print("   → Ready for tag-based resume generation")

    print("\n" + "=" * 80)

if __name__ == '__main__':
    analyze_resume()
