#!/usr/bin/env python3
"""
Analyze tags used in resume.json to help design checkbox taxonomy
"""

import json
from collections import Counter
from pathlib import Path

def analyze_tags():
    """Extract and count all tags from resume.json"""

    # Load resume data
    resume_path = Path(__file__).parent.parent / 'data' / 'resume.json'
    with open(resume_path, 'r') as f:
        resume = json.load(f)

    # Collect all tags
    all_tags = []
    tag_contexts = {}  # Track where each tag appears

    # From experience bullets (nested in positions)
    if 'experience' in resume:
        for exp in resume['experience']:
            # Check if achievements are at experience level or position level
            if 'positions' in exp:
                for position in exp['positions']:
                    if 'achievements' in position:
                        for category in position['achievements']:
                            if isinstance(category, dict) and 'items' in category:
                                for item in category['items']:
                                    if isinstance(item, dict) and 'tags' in item:
                                        tags = item['tags']
                                        all_tags.extend(tags)
                                        for tag in tags:
                                            if tag not in tag_contexts:
                                                tag_contexts[tag] = {'experience': 0, 'projects': 0, 'skills': 0}
                                            tag_contexts[tag]['experience'] += 1
            elif 'achievements' in exp:
                # Fallback for experience-level achievements
                for category in exp['achievements']:
                    if isinstance(category, dict) and 'items' in category:
                        for item in category['items']:
                            if isinstance(item, dict) and 'tags' in item:
                                tags = item['tags']
                                all_tags.extend(tags)
                                for tag in tags:
                                    if tag not in tag_contexts:
                                        tag_contexts[tag] = {'experience': 0, 'projects': 0, 'skills': 0}
                                    tag_contexts[tag]['experience'] += 1

    # From projects
    if 'projects' in resume:
        for project in resume['projects']:
            if 'tags' in project:
                tags = project['tags']
                all_tags.extend(tags)
                for tag in tags:
                    if tag not in tag_contexts:
                        tag_contexts[tag] = {'experience': 0, 'projects': 0, 'skills': 0}
                    tag_contexts[tag]['projects'] += 1

    # Count frequencies
    tag_counts = Counter(all_tags)

    # Print analysis
    print("=" * 80)
    print("RESUME TAG ANALYSIS")
    print("=" * 80)
    print(f"\nTotal unique tags: {len(tag_counts)}")
    print(f"Total tag occurrences: {sum(tag_counts.values())}")
    print("\n" + "=" * 80)
    print("TAG FREQUENCY (sorted by count)")
    print("=" * 80)
    print(f"{'Tag':<30} {'Count':>8} {'Experience':>12} {'Projects':>12}")
    print("-" * 80)

    for tag, count in tag_counts.most_common():
        exp_count = tag_contexts[tag]['experience']
        proj_count = tag_contexts[tag]['projects']
        print(f"{tag:<30} {count:>8} {exp_count:>12} {proj_count:>12}")

    # Group by logical categories based on resume_profiles.json taxonomy
    print("\n" + "=" * 80)
    print("SUGGESTED CHECKBOX CATEGORIES")
    print("=" * 80)

    categories = {
        'Therapeutic Areas': ['oncology', 'cardiovascular', 'hiv', 'mens_health', 'rare_disease'],
        'Core Functions': ['brand', 'strategy', 'cx', 'xp', 'experience_planning'],
        'Marketing Disciplines': ['omnichannel', 'launch', 'portfolio', 'hcp', 'patient', 'journey_mapping'],
        'Innovation & Tech': ['ai', 'innovation', 'digital', 'analytics', 'automation', 'data_engineering'],
        'Leadership & Collaboration': ['leadership', 'team_management', 'cross_functional', 'stakeholder_management'],
        'Specialized Skills': ['compliance', 'mlr', 'education', 'training']
    }

    for category, expected_tags in categories.items():
        print(f"\n{category}:")
        found_tags = [(tag, tag_counts.get(tag, 0)) for tag in expected_tags if tag in tag_counts]
        if found_tags:
            for tag, count in sorted(found_tags, key=lambda x: x[1], reverse=True):
                print(f"  • {tag:<25} ({count} occurrences)")
        else:
            print(f"  (No tags found in this category)")

    # Find tags not in our predefined categories
    categorized_tags = set()
    for tags in categories.values():
        categorized_tags.update(tags)

    uncategorized = set(tag_counts.keys()) - categorized_tags
    if uncategorized:
        print(f"\nUncategorized tags (may need new categories):")
        for tag in sorted(uncategorized, key=lambda x: tag_counts[x], reverse=True):
            if tag_counts[tag] >= 3:  # Only show if used 3+ times
                print(f"  • {tag:<25} ({tag_counts[tag]} occurrences)")

if __name__ == '__main__':
    analyze_tags()
