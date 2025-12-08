#!/usr/bin/env python3
"""
Add TAGRISSO Brand Context to Biolumina Achievements
Updates patient/DTC achievements to explicitly mention TAGRISSO brand
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def add_tagrisso_context(resume_path):
    """Add TAGRISSO brand context to patient/DTC achievements"""

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

    # Define text replacements to add TAGRISSO context
    replacements = [
        {
            'old': 'Built and executed omnichannel customer relationship marketing (CRM) programming aligned to brand strategic imperatives',
            'new': 'Built and executed omnichannel customer relationship marketing (CRM) programming for TAGRISSO DTC brand aligned to strategic imperatives',
            'reason': 'Primary TAGRISSO DTC work'
        },
        {
            'old': "Created internal 'Xosystem' (experience ecosystem) process to optimize tactical planning and execution across omnichannel customer touchpoints",
            'new': "Created internal 'Xosystem' (experience ecosystem) process to optimize TAGRISSO DTC tactical planning and execution across omnichannel customer touchpoints",
            'reason': 'Developed for TAGRISSO DTC team'
        },
        {
            'old': 'Supported client brand initiatives by designing omnichannel, segmentation, CTV/OTT, and experiential congress frameworks',
            'new': 'Supported TAGRISSO DTC brand initiatives by designing omnichannel, segmentation, CTV/OTT, and experiential congress frameworks for patient/caregiver audiences',
            'reason': 'TAGRISSO brand work'
        },
        {
            'old': 'Designed interactive game-based advertising concepts and WebAR strategies with 8th Wall',
            'new': 'Designed interactive game-based advertising concepts and WebAR strategies with 8th Wall for TAGRISSO patient engagement',
            'reason': 'TAGRISSO patient-facing innovation'
        },
        {
            'old': 'Built WebReportingHub analytics platform reducing cross-brand reporting time 60% for 9-brand portfolio using DuckDB and Python automation',
            'new': 'Built WebReportingHub analytics platform reducing cross-brand reporting time 60% for 9-brand portfolio including TAGRISSO DTC performance tracking using DuckDB and Python automation',
            'reason': 'Included TAGRISSO metrics'
        }
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

                            # Check each replacement
                            for replacement in replacements:
                                if text == replacement['old']:
                                    item['text'] = replacement['new']
                                    changes_made += 1
                                    print(f"\n✓ Updated achievement:")
                                    print(f"  OLD: {replacement['old'][:70]}...")
                                    print(f"  NEW: {replacement['new'][:70]}...")
                                    print(f"  Reason: {replacement['reason']}")
                                    break

    # Save
    if changes_made > 0:
        print(f"\n📝 Writing changes to resume.json...")
        with open(resume_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Successfully updated {changes_made} achievements with TAGRISSO context!")
    else:
        print("\nℹ️  No changes needed.")

    return changes_made

if __name__ == '__main__':
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not resume_path.exists():
        print(f"❌ Error: {resume_path} not found")
        sys.exit(1)

    print("🔧 TAGRISSO Context Adder")
    print("=" * 80)
    print("Adding TAGRISSO brand context to patient/DTC achievements...")
    print("=" * 80)

    changes = add_tagrisso_context(resume_path)

    print("\n" + "=" * 80)
    print(f"✨ Done! {changes} achievements updated with TAGRISSO brand context.")
