#!/usr/bin/env python3
"""
Fix Biolumina Patient Tags
Add 'patient' tag to Biolumina achievements that involve patient/caregiver work
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def fix_biolumina_patient_tags(resume_path):
    """Add patient tag to appropriate Biolumina achievements"""

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

    # Keywords that indicate patient/caregiver work
    patient_indicators = [
        'crm',  # CRM is patient-focused
        'patient',
        'caregiver',
        'dtc',
        'consumer',
        'segmentation',  # Often used for patient segmentation
        'omnichannel',  # Often includes patient channels
        'customer relationship',
        'experience ecosystem'  # Xosystem includes patient touchpoints
    ]

    # Achievements to add patient tag to (based on analysis)
    should_have_patient = [
        'Built and executed omnichannel customer relationship marketing (CRM)',
        'Created internal \'Xosystem\' (experience ecosystem)',
        'Supported client brand initiatives by designing omnichannel, segmentation',
        'Designed interactive game-based advertising concepts',
        'Led creation, testing, and deployment of multiple custom GPTs',  # GPTs used for patient work
        'Built WebReportingHub analytics platform',  # Reports on patient metrics
        'Led Curiosity-Driven Innovation Initiative'  # Generated patient-facing innovations
    ]

    for exp in data.get('experience', []):
        if exp['company'] == 'Biolumina':
            print(f"\n{'='*80}")
            print(f"Processing: {exp['company']}")
            print(f"{'='*80}")

            for position in exp.get('positions', []):
                print(f"\nPosition: {position['title']}")

                for group in position.get('achievements', []):
                    for item in group.get('items', []):
                        if isinstance(item, dict) and 'text' in item:
                            text = item['text']
                            tags = item.get('tags', [])

                            has_oncology = 'oncology' in tags
                            has_patient = 'patient' in tags

                            # Check if this achievement should have patient tag
                            text_lower = text.lower()
                            should_add = False

                            # Check if matches specific achievements
                            for indicator in should_have_patient:
                                if indicator.lower() in text_lower:
                                    should_add = True
                                    break

                            # Check for patient keywords
                            if not should_add:
                                for keyword in patient_indicators:
                                    if keyword in text_lower:
                                        should_add = True
                                        break

                            # Add patient tag if needed
                            if should_add and has_oncology and not has_patient:
                                tags.append('patient')
                                item['tags'] = tags
                                changes_made += 1
                                print(f"✓ Added 'patient' tag to:")
                                print(f"  {text[:70]}...")
                                print(f"  Updated tags: {tags}")

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
        sys.exit(1)

    print("🔧 Biolumina Patient Tag Fixer")
    print("=" * 80)
    print("Adding 'patient' tag to oncology achievements involving patient/caregiver work...")
    print("=" * 80)

    changes = fix_biolumina_patient_tags(resume_path)

    print("\n" + "=" * 80)
    print(f"✨ Done! {changes} tags updated.")
