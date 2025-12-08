#!/usr/bin/env python3
"""
Add 'patient' tag to Patients & Purpose achievements that explicitly mention patient/consumer work
"""

import json
from pathlib import Path
from datetime import datetime

def fix_patients_purpose_tags(resume_path):
    """Add patient tag to explicit consumer/DTC achievements"""

    print("Loading resume.json...")
    with open(resume_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = resume_path.parent / f'resume_backup_{timestamp}.json'
    print(f"Creating backup at {backup_path}...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    changes_made = 0

    # Keywords that indicate patient/consumer work
    patient_keywords = [
        'consumer',
        'dtc',
        'caregiver',
        'savings card',
        'voucher',
        'non-representative',
        'patient segment',
        'digital asset creative',
        'html5 sites',
        'responsive web design',
        'rwd'
    ]

    for exp in data.get('experience', []):
        if 'patients' in exp['company'].lower() or 'cdmi' in exp['company'].lower():
            print(f"\n{'='*80}")
            print(f"Processing: {exp['company']}")
            print(f"{'='*80}")

            for position in exp.get('positions', []):
                print(f"\nPosition: {position['title']}")

                for group in position.get('achievements', []):
                    for item in group.get('items', []):
                        if isinstance(item, dict) and 'text' in item:
                            text = item['text']
                            text_lower = text.lower()
                            tags = item.get('tags', [])

                            # Check if mentions patient/consumer keywords
                            matches = [kw for kw in patient_keywords if kw in text_lower]

                            if matches and 'patient' not in tags:
                                tags.append('patient')
                                item['tags'] = tags
                                changes_made += 1
                                print(f"✓ Added 'patient' tag to:")
                                print(f"  {text[:70]}...")
                                print(f"  Keywords found: {matches}")

    # Save
    if changes_made > 0:
        print(f"\n📝 Writing changes to resume.json...")
        with open(resume_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Successfully made {changes_made} tag changes!")
    else:
        print("\nℹ️  No changes needed.")

    return changes_made

if __name__ == '__main__':
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not resume_path.exists():
        print(f"❌ Error: {resume_path} not found")
        exit(1)

    print("🔧 Patients & Purpose Patient Tag Fixer")
    print("=" * 80)
    print("Adding 'patient' tag to consumer/DTC achievements...")
    print("=" * 80)

    changes = fix_patients_purpose_tags(resume_path)

    print("\n" + "=" * 80)
    print(f"✨ Done! {changes} tags updated.")
