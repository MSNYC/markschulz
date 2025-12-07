#!/usr/bin/env python3
"""
Achievement Loader
Loads extracted achievements from individual JSON files into resume.json
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import shutil

def load_json(filepath):
    """Load and parse JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath, indent=2):
    """Save JSON with consistent formatting"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
    print(f"✅ Saved: {filepath}")

def create_backup(filepath):
    """Create timestamped backup of resume.json"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.parent / f"resume_backup_{timestamp}.json"
    shutil.copy2(filepath, backup_path)
    print(f"📦 Backup created: {backup_path}")
    return backup_path

def validate_extraction(data):
    """Validate extracted achievement data"""
    errors = []

    # Check required fields
    if 'position_metadata' not in data:
        errors.append("Missing 'position_metadata'")
    else:
        required_meta = ['company', 'title', 'start_date', 'experience_id']
        for field in required_meta:
            if field not in data['position_metadata']:
                errors.append(f"Missing position_metadata.{field}")

    if 'achievements' not in data:
        errors.append("Missing 'achievements' array")
    elif not isinstance(data['achievements'], list):
        errors.append("'achievements' must be an array")
    else:
        # Validate each achievement
        for i, ach in enumerate(data['achievements']):
            if 'text' not in ach or not ach['text']:
                errors.append(f"Achievement {i}: Missing or empty 'text'")
            if 'tags' not in ach or not isinstance(ach['tags'], list) or len(ach['tags']) == 0:
                errors.append(f"Achievement {i}: Missing or empty 'tags' array")

    return errors

def find_position_in_resume(resume_data, exp_id, company, title, start_date):
    """Find the matching position in resume.json"""
    for exp in resume_data['experience']:
        if exp['id'] == exp_id:
            # Found matching experience, now find position
            for pos in exp['positions']:
                if pos['title'] == title and pos['start_date'] == start_date:
                    return exp, pos
            # If no exact position match, try just by start_date
            for pos in exp['positions']:
                if pos['start_date'] == start_date:
                    print(f"⚠️  Matched by start_date only (title mismatch)")
                    return exp, pos
    return None, None

def merge_achievements(existing_achievements, new_achievements, merge_strategy='append'):
    """
    Merge new achievements into existing ones

    merge_strategy:
        'append': Add all new achievements to the end
        'deduplicate': Only add achievements with unique text
        'replace': Replace all existing achievements
    """
    if merge_strategy == 'replace':
        return new_achievements

    if merge_strategy == 'append':
        return existing_achievements + new_achievements

    if merge_strategy == 'deduplicate':
        # Create set of existing achievement texts
        existing_texts = {ach['text'].lower().strip() for items in existing_achievements
                         for ach in items.get('items', [])} if existing_achievements else set()

        # Only add achievements with new text
        deduplicated = []
        for ach in new_achievements:
            if ach['text'].lower().strip() not in existing_texts:
                deduplicated.append(ach)
            else:
                print(f"⚠️  Skipping duplicate: {ach['text'][:60]}...")

        return existing_achievements + deduplicated

    return existing_achievements

def organize_achievements_by_category(achievements):
    """
    Organize flat achievement list into categorized structure
    Returns list of category dicts matching resume.json format
    """
    # For now, put all in a single "Extracted Achievements" category
    # Later we could use AI to categorize, or let user categorize manually
    if not achievements:
        return []

    return [
        {
            "category": "Key Achievements",
            "items": [
                {
                    "text": ach['text'],
                    "tags": ach['tags'],
                    **({"context": ach['context']} if 'context' in ach else {}),
                    **({"metric_type": ach['metric_type']} if 'metric_type' in ach else {}),
                    **({"source_confidence": ach['source_confidence']} if 'source_confidence' in ach else {})
                }
                for ach in achievements
            ]
        }
    ]

def main():
    if len(sys.argv) < 2:
        print("Usage: python load_achievements.py <extraction_file.json> [--strategy append|deduplicate|replace]")
        print("\nExample:")
        print("  python load_achievements.py achievements_webmd_2018.json")
        print("  python load_achievements.py achievements_webmd_2018.json --strategy deduplicate")
        sys.exit(1)

    extraction_file = Path(sys.argv[1])
    merge_strategy = 'append'  # default

    # Parse strategy argument if provided
    if len(sys.argv) > 2 and sys.argv[2] == '--strategy' and len(sys.argv) > 3:
        merge_strategy = sys.argv[3]
        if merge_strategy not in ['append', 'deduplicate', 'replace']:
            print(f"❌ Invalid strategy: {merge_strategy}")
            print("   Valid options: append, deduplicate, replace")
            sys.exit(1)

    if not extraction_file.exists():
        print(f"❌ File not found: {extraction_file}")
        sys.exit(1)

    # Load extraction data
    print(f"\n📂 Loading extraction file: {extraction_file}")
    try:
        extraction_data = load_json(extraction_file)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)

    # Validate extraction data
    print("🔍 Validating extraction data...")
    errors = validate_extraction(extraction_data)
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    print("✅ Validation passed")

    # Load resume.json
    resume_path = Path(__file__).parent / 'resume.json'
    if not resume_path.exists():
        print(f"❌ resume.json not found at: {resume_path}")
        sys.exit(1)

    print(f"\n📂 Loading resume.json...")
    resume_data = load_json(resume_path)

    # Create backup
    create_backup(resume_path)

    # Find matching position
    meta = extraction_data['position_metadata']
    print(f"\n🔍 Finding position: {meta['title']} at {meta['company']} ({meta['start_date']})")

    exp, pos = find_position_in_resume(
        resume_data,
        meta['experience_id'],
        meta['company'],
        meta['title'],
        meta['start_date']
    )

    if not exp or not pos:
        print(f"❌ Could not find matching position in resume.json")
        print(f"   Looking for: exp_id={meta['experience_id']}, company={meta['company']}, title={meta['title']}")
        sys.exit(1)

    print(f"✅ Found position: {pos['title']}")

    # Organize new achievements
    new_achievements_organized = organize_achievements_by_category(extraction_data['achievements'])

    # Get existing achievements
    existing = pos.get('achievements', [])

    print(f"\n📊 Current state:")
    print(f"   Existing achievement categories: {len(existing)}")
    print(f"   New achievements to add: {len(extraction_data['achievements'])}")
    print(f"   Merge strategy: {merge_strategy}")

    # Merge achievements
    if merge_strategy == 'replace':
        pos['achievements'] = new_achievements_organized
        print(f"   ⚠️  REPLACED all existing achievements")
    else:
        # Append new category
        pos['achievements'] = existing + new_achievements_organized
        print(f"   ✅ Added new achievement category")

    # Save updated resume.json
    print(f"\n💾 Saving updated resume.json...")
    save_json(resume_data, resume_path, indent=2)

    # Summary
    print(f"\n✅ SUCCESS!")
    print(f"   Position: {pos['title']} at {meta['company']}")
    print(f"   Achievement categories now: {len(pos['achievements'])}")
    total_items = sum(len(cat.get('items', [])) for cat in pos['achievements'])
    print(f"   Total achievement items: {total_items}")
    print(f"\n💡 Next steps:")
    print(f"   1. Review the updated resume.json")
    print(f"   2. Run: python data/verify_achievements.py (when created)")
    print(f"   3. Load more extractions or proceed with resume generation")

if __name__ == '__main__':
    main()
