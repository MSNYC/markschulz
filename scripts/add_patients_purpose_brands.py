#!/usr/bin/env python3
"""
Add brand-specific achievements to Patients & Purpose positions
"""

import json
from pathlib import Path
from datetime import datetime

def add_brand_achievements(resume_path):
    """Add BANZEL, LUCENTIS, and TECFIDERA achievements"""

    print("Loading resume.json...")
    with open(resume_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = resume_path.parent / f'resume_backup_{timestamp}.json'
    print(f"Creating backup at {backup_path}...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # New brand-specific achievements
    new_achievements = [
        {
            "text": "Led project management and digital strategy for BANZEL (epilepsy) patient website, social media campaigns, and email programs as lead PM and digital consultant",
            "tags": ["patient", "digital", "brand", "project_management", "leadership", "crm", "social_media"]
        },
        {
            "text": "Oversaw full digital promotion ecosystem for BANZEL brand spanning web, social, and CRM channels with cross-functional team coordination",
            "tags": ["patient", "digital", "brand", "project_management", "omnichannel", "leadership"]
        },
        {
            "text": "Managed major indication launch for LUCENTIS (wet AMD) treated as full brand launch, overseeing complete website redesign and digital ecosystem overhaul for patient and caregiver audiences",
            "tags": ["patient", "digital", "brand", "launch", "project_management", "leadership"]
        },
        {
            "text": "Led cross-functional teams to deliver responsive website and comprehensive digital asset suite for LUCENTIS new indication launch targeting patients and caregivers",
            "tags": ["patient", "digital", "brand", "launch", "project_management", "leadership", "innovation"]
        },
        {
            "text": "Led development of innovative mobile smartphone application for MS patients on TECFIDERA, pioneering one of the first-of-its-kind patient support apps in pharma",
            "tags": ["patient", "digital", "innovation", "mobile", "brand", "project_management", "leadership"]
        },
        {
            "text": "Managed full product lifecycle from concept to launch for groundbreaking TECFIDERA mobile app, establishing new standards for digital patient engagement in MS treatment",
            "tags": ["patient", "digital", "innovation", "mobile", "brand", "launch", "project_management"]
        }
    ]

    changes_made = 0

    # Find Patients & Purpose VP position to add achievements
    for exp in data.get('experience', []):
        if 'patients' in exp['company'].lower():
            print(f"\n{'='*80}")
            print(f"Processing: {exp['company']}")
            print(f"{'='*80}")

            for position in exp.get('positions', []):
                # Add to VP position (most senior role where this work happened)
                if 'vp' in position['title'].lower() and 'project management' in position['title'].lower():
                    print(f"\nAdding brand achievements to: {position['title']}")

                    # Create new category for brand work
                    new_category = {
                        "category": "Brand-Specific Patient Marketing Leadership",
                        "items": new_achievements
                    }

                    if 'achievements' not in position:
                        position['achievements'] = []

                    position['achievements'].append(new_category)
                    changes_made = len(new_achievements)

                    for ach in new_achievements:
                        print(f"✓ Added: {ach['text'][:70]}...")

    # Save
    if changes_made > 0:
        print(f"\n📝 Writing changes to resume.json...")
        with open(resume_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Successfully added {changes_made} brand-specific achievements!")
    else:
        print("\n⚠️  Could not find VP position to add achievements.")

    return changes_made

if __name__ == '__main__':
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not resume_path.exists():
        print(f"❌ Error: {resume_path} not found")
        exit(1)

    print("🔧 Patients & Purpose Brand Achievement Adder")
    print("=" * 80)
    print("Adding BANZEL, LUCENTIS, and TECFIDERA achievements...")
    print("=" * 80)

    changes = add_brand_achievements(resume_path)

    print("\n" + "=" * 80)
    print(f"✨ Done! {changes} brand achievements added.")
    print("\nBrands added:")
    print("  • BANZEL (epilepsy) - 2 achievements")
    print("  • LUCENTIS (wet AMD) - 2 achievements")
    print("  • TECFIDERA/MS - 2 achievements")
