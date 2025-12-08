#!/usr/bin/env python3
"""
Fix Resume Tagging Issues
Automatically corrects tags based on comprehensive audit findings
"""

import json
import sys
from pathlib import Path

def fix_tags(resume_path):
    """Apply all tag fixes to resume.json"""

    print("Loading resume.json...")
    with open(resume_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changes_made = 0

    # TIER 1: Add "oncology" to Biolumina achievements
    oncology_additions = [
        "Created an AI ideation GPT using AIDA, PAS, FOMO, SCAMPER, FAB, StoryBrand",
        "Designed interactive game-based advertising concepts and WebAR strategies with 8th Wall",
        "Analyzed 36,000-row rep-triggered email dataset to understand subject-line performance",
        "Pioneered AI integration with Pharmetheus GPT assistant, democratizing 15+ years of brand strategy insights",
        "Led Curiosity-Driven Innovation Initiative with 12 team members over 18 months",
        "Built and executed omnichannel customer relationship marketing (CRM) programming aligned to brand strategic imperatives",
        "Created internal 'Xosystem' (experience ecosystem) process to optimize tactical planning",
    ]

    # TIER 2: Remove "patient" from sales training (partial match)
    remove_patient_keywords = [
        "group practice adherence program with national sales representative training",
    ]

    # TIER 2: Add "patient" to real patient marketing
    add_patient_texts = [
        "Managed complex timelines to deliver cutting-edge responsive and HTML5 sites for consumer digital asset creative",
        "Led integration of Caduet messaging maintaining extensive cross-functional partnerships across non-representative channels, media space, and consumer initiatives",
        "Drove final market testing and launch of a two-platform overhaul to Caduet messaging to position the product for a particular patient segment",
        "Created innovative unbranded EMR system guide that enabled one representative to identify 60 patients for follow-up",
    ]

    # Add "patient" to savings card/voucher programs
    add_patient_keywords = [
        "savings card program",
        "voucher ordering system",
    ]

    # TIER 3: Add "cardio" to LIPITOR/CADUET work
    add_cardio_keywords = [
        "CV franchise",
        "Caduet",
        "CADUET",
        "LIPITOR",
        "Lipitor",
    ]

    # Process all achievements
    for exp in data.get('experience', []):
        for position in exp.get('positions', []):
            for group in position.get('achievements', []):
                for item in group.get('items', []):
                    if not isinstance(item, dict) or 'text' not in item:
                        continue

                    text = item['text']
                    tags = item.get('tags', [])
                    original_tags = tags.copy()

                    # Fix 1: Add oncology to specific Biolumina achievements
                    for onc_text in oncology_additions:
                        if onc_text in text and 'oncology' not in tags:
                            tags.append('oncology')
                            changes_made += 1
                            print(f"✓ Added 'oncology' to: {text[:60]}...")
                            break

                    # Fix 2: Remove patient from sales training
                    for keyword in remove_patient_keywords:
                        if keyword in text.lower() and 'patient' in tags:
                            tags.remove('patient')
                            changes_made += 1
                            print(f"✓ Removed 'patient' from: {text[:60]}...")
                            break

                    # Fix 3: Add patient to real patient marketing
                    for patient_text in add_patient_texts:
                        if patient_text in text and 'patient' not in tags:
                            tags.append('patient')
                            changes_made += 1
                            print(f"✓ Added 'patient' to: {text[:60]}...")
                            break

                    # Fix 4: Add patient to savings card/voucher programs
                    for keyword in add_patient_keywords:
                        if keyword.lower() in text.lower() and 'patient' not in tags:
                            tags.append('patient')
                            changes_made += 1
                            print(f"✓ Added 'patient' to: {text[:60]}...")
                            break

                    # Fix 5: Add cardio to LIPITOR/CADUET work
                    for keyword in add_cardio_keywords:
                        if keyword in text and 'cardio' not in tags:
                            # Only add if not already cardiovascular tagged
                            if 'cardiovascular' not in tags:
                                tags.append('cardio')
                                changes_made += 1
                                print(f"✓ Added 'cardio' to: {text[:60]}...")
                            break

                    # Update tags if changed
                    if tags != original_tags:
                        item['tags'] = tags

    # Save updated resume
    if changes_made > 0:
        print(f"\n📝 Writing changes to resume.json...")
        with open(resume_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Successfully made {changes_made} tag changes!")
    else:
        print("ℹ️  No changes needed.")

    return changes_made

if __name__ == '__main__':
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not resume_path.exists():
        print(f"❌ Error: {resume_path} not found")
        sys.exit(1)

    print("🔧 Resume Tag Fixer")
    print("=" * 50)

    changes = fix_tags(resume_path)

    print("\n" + "=" * 50)
    print(f"✨ Complete! {changes} tags updated.")
    print("\nNext step: Rebuild Jekyll and test the custom resume generator!")
