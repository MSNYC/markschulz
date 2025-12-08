#!/usr/bin/env python3
"""
Test Resume Differentiation
Generates all 3 Quick Select resumes and analyzes their differentiation
"""

import json
from pathlib import Path
from collections import defaultdict
import re

def load_resume_data():
    """Load resume.json"""
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'
    with open(resume_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_profiles():
    """Load resume_profiles.json"""
    profiles_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume_profiles.json'
    with open(profiles_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_text(text):
    """Normalize text for comparison"""
    return re.sub(r'\s+', ' ', text.lower().strip())

def score_achievement(achievement, priority_tags):
    """Score an achievement based on tag matching (simplified version of JS logic)"""
    tags = achievement.get('tags', [])
    text = achievement.get('text', '').lower()

    score = 0

    # Base tag matching
    for tag in tags:
        if tag in priority_tags:
            score += 1

    # Brand boost logic
    oncology_brands = ['tagrisso', 'kisqali', 'brukinsa', 'imfinzi']
    cardio_brands = ['lipitor', 'caduet']
    hiv_rare_brands = ['biktarvy', 'descovy', 'truvada', 'banzel']
    patient_brands = ['tagrisso', 'banzel', 'lucentis', 'tecfidera', 'lyrica']
    hcp_brands = ['kisqali', 'brukinsa', 'lipitor', 'caduet', 'viagra']

    has_oncology = 'oncology' in priority_tags
    has_cardio = 'cardio' in priority_tags or 'cardiovascular' in priority_tags
    has_hiv = 'hiv' in priority_tags or 'rare_disease' in priority_tags or 'mens_health' in priority_tags
    has_patient = 'patient' in priority_tags
    has_hcp = 'hcp' in priority_tags

    if has_oncology and any(brand in text for brand in oncology_brands):
        score += 3
    if has_cardio and any(brand in text for brand in cardio_brands):
        score += 3
    if has_hiv and any(brand in text for brand in hiv_rare_brands):
        score += 3
    if has_patient and any(brand in text for brand in patient_brands):
        score += 2
    if has_hcp and any(brand in text for brand in hcp_brands):
        score += 2

    return score

def get_top_achievements_per_position(data, priority_tags, max_bullets=6):
    """Get top N achievements per position based on scoring"""
    results = []

    for exp in data.get('experience', []):
        for position in exp.get('positions', []):
            position_achievements = []

            for group in position.get('achievements', []):
                for item in group.get('items', []):
                    if isinstance(item, dict) and 'text' in item:
                        score = score_achievement(item, priority_tags)
                        position_achievements.append({
                            'text': item['text'],
                            'score': score,
                            'tags': item.get('tags', [])
                        })

            # Sort by score and take top N
            position_achievements.sort(key=lambda x: x['score'], reverse=True)
            top_achievements = position_achievements[:max_bullets]

            if top_achievements:
                results.append({
                    'company': exp['company'],
                    'title': position['title'],
                    'achievements': [a['text'] for a in top_achievements]
                })

    return results

def calculate_overlap(achievements1, achievements2):
    """Calculate what percentage of achievements overlap between two resumes"""
    set1 = set(normalize_text(a) for a in achievements1)
    set2 = set(normalize_text(a) for a in achievements2)

    if not set1 or not set2:
        return 0.0

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return (intersection / union) * 100 if union > 0 else 0.0

def analyze_resumes():
    """Main analysis function"""
    print("=" * 80)
    print("RESUME DIFFERENTIATION ANALYSIS")
    print("=" * 80)

    data = load_resume_data()
    profiles_data = load_profiles()
    profiles = profiles_data['profiles']

    # Generate achievements for each profile
    profile_achievements = {}

    for profile in profiles:
        profile_id = profile['id']
        priority_tags = profile['priority_tags']
        achievements = get_top_achievements_per_position(data, priority_tags, max_bullets=6)

        # Flatten to list of all achievement texts
        all_texts = []
        for pos in achievements:
            all_texts.extend(pos['achievements'])

        profile_achievements[profile_id] = {
            'name': profile['label'],
            'positions': achievements,
            'all_achievements': all_texts,
            'total_count': len(all_texts)
        }

    # Print summary for each profile
    print("\n" + "=" * 80)
    print("ACHIEVEMENTS PER PROFILE")
    print("=" * 80)

    for profile_id in ['brand_management', 'strategy_innovation', 'cx_engagement']:
        prof = profile_achievements[profile_id]
        print(f"\n{prof['name']}: {prof['total_count']} total achievements")
        print(f"Across {len(prof['positions'])} positions")

    # Calculate pairwise overlaps
    print("\n" + "=" * 80)
    print("OVERLAP ANALYSIS (Experience Section)")
    print("=" * 80)

    pairs = [
        ('brand_management', 'strategy_innovation'),
        ('brand_management', 'cx_engagement'),
        ('strategy_innovation', 'cx_engagement')
    ]

    for id1, id2 in pairs:
        prof1 = profile_achievements[id1]
        prof2 = profile_achievements[id2]

        overlap = calculate_overlap(prof1['all_achievements'], prof2['all_achievements'])

        print(f"\n{prof1['name']} vs {prof2['name']}")
        print(f"  Overlap: {overlap:.1f}%")
        print(f"  {prof1['name']}: {prof1['total_count']} achievements")
        print(f"  {prof2['name']}: {prof2['total_count']} achievements")

    # Show sample achievements from each profile
    print("\n" + "=" * 80)
    print("SAMPLE ACHIEVEMENTS (First 3 from first position)")
    print("=" * 80)

    for profile_id in ['brand_management', 'strategy_innovation', 'cx_engagement']:
        prof = profile_achievements[profile_id]
        print(f"\n{prof['name']}:")

        if prof['positions']:
            first_pos = prof['positions'][0]
            print(f"  Position: {first_pos['title']} at {first_pos['company']}")
            for i, ach in enumerate(first_pos['achievements'][:3], 1):
                print(f"    {i}. {ach[:100]}...")

    # VERDICT
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)

    avg_overlap = sum(
        calculate_overlap(
            profile_achievements[id1]['all_achievements'],
            profile_achievements[id2]['all_achievements']
        )
        for id1, id2 in pairs
    ) / len(pairs)

    print(f"\nAverage overlap: {avg_overlap:.1f}%")

    if avg_overlap < 40:
        print("✅ GOOD: Resumes are well-differentiated (< 40% overlap)")
    elif avg_overlap < 60:
        print("⚠️  MODERATE: Some differentiation but could be improved (40-60% overlap)")
    else:
        print("❌ POOR: Resumes are too similar (> 60% overlap)")

    print("\nTarget: ~30-40% overlap in Experience section")
    print("Note: Top sections (Executive Snapshot, Targeted Highlights, Skills) are")
    print("      fully differentiated and not measured here.")

    print("\n" + "=" * 80)

if __name__ == '__main__':
    analyze_resumes()
