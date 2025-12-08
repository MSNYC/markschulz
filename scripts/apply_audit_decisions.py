#!/usr/bin/env python3
"""
Apply Audit Decisions to resume.json
Reads ACHIEVEMENT_AUDIT.md and applies user's decisions (KEEP/EDIT/DELETE)
"""

import json
import re
from pathlib import Path
from datetime import datetime

def parse_audit_file(audit_path):
    """Parse the audit markdown file to extract decisions"""

    with open(audit_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into achievement blocks
    blocks = re.split(r'#### Achievement \d+', content)

    decisions = []

    for block in blocks[1:]:  # Skip header
        # Extract text
        text_match = re.search(r'\*\*Text:\*\* (.+?)(?:\n|$)', block)
        if not text_match:
            continue

        achievement_text = text_match.group(1).strip()

        # Extract decision
        decision_match = re.search(r'\*\*DECISION:\*\* \[?(KEEP|EDIT|DELETE)\]?', block, re.IGNORECASE)
        if not decision_match:
            continue

        decision = decision_match.group(1).upper()

        # Extract edited text if EDIT
        edited_text = None
        if decision == 'EDIT':
            edit_match = re.search(r'\*\*EDIT \(if applicable\):\*\*\s*(.+?)(?:\n---|\Z)', block, re.DOTALL)
            if edit_match:
                edited_text = edit_match.group(1).strip()
                # Remove empty lines
                edited_text = '\n'.join(line for line in edited_text.split('\n') if line.strip())
                if not edited_text:
                    print(f"⚠️  Achievement marked EDIT but no edited text provided, treating as KEEP:")
                    print(f"   {achievement_text[:80]}...")
                    decision = 'KEEP'

        decisions.append({
            'original_text': achievement_text,
            'decision': decision,
            'edited_text': edited_text
        })

    return decisions


def apply_decisions_to_resume(resume_path, decisions):
    """Apply audit decisions to resume.json"""

    print("Loading resume.json...")
    with open(resume_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = resume_path.parent / f'resume_backup_{timestamp}.json'
    print(f"Creating backup at {backup_path}...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    kept = 0
    edited = 0
    deleted = 0
    not_found = 0

    # Create lookup dict for faster searching
    decision_map = {d['original_text']: d for d in decisions}

    # Process all achievements
    for exp in data.get('experience', []):
        for position in exp.get('positions', []):
            for group in position.get('achievements', []):
                items_to_remove = []

                for idx, item in enumerate(group.get('items', [])):
                    if isinstance(item, dict) and 'text' in item:
                        text = item['text']

                        # Check if this achievement is in our audit
                        if text in decision_map:
                            decision_info = decision_map[text]
                            decision = decision_info['decision']

                            if decision == 'DELETE':
                                items_to_remove.append(idx)
                                deleted += 1
                                print(f"\n✗ DELETED:")
                                print(f"  {text[:70]}...")

                            elif decision == 'EDIT':
                                new_text = decision_info['edited_text']
                                if new_text:
                                    item['text'] = new_text
                                    edited += 1
                                    print(f"\n✏️  EDITED:")
                                    print(f"  OLD: {text[:60]}...")
                                    print(f"  NEW: {new_text[:60]}...")
                                else:
                                    kept += 1

                            elif decision == 'KEEP':
                                kept += 1

                        # Check if this is an unverified achievement not in audit
                        elif 'source_document' not in item and 'extracted_date' not in item:
                            # This is an unverified achievement that wasn't in the audit
                            not_found += 1
                            print(f"\n⚠️  WARNING: Unverified achievement not found in audit:")
                            print(f"  {text[:70]}...")

                # Remove deleted items (in reverse order)
                for idx in reversed(items_to_remove):
                    group['items'].pop(idx)

    # Clean empty categories
    for exp in data['experience']:
        for pos in exp['positions']:
            pos['achievements'] = [
                cat for cat in pos.get('achievements', [])
                if cat.get('items', [])
            ]

    # Save
    print(f"\n{'='*80}")
    print(f"📝 Writing changes to resume.json...")
    with open(resume_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print(f"AUDIT RESULTS")
    print(f"{'='*80}")
    print(f"✓ Kept:    {kept} achievements")
    print(f"✏️  Edited:  {edited} achievements")
    print(f"✗ Deleted: {deleted} achievements")
    if not_found > 0:
        print(f"⚠️  Not in audit: {not_found} achievements (may be from other positions)")
    print(f"\n✅ Resume updated successfully!")
    print(f"📦 Backup: {backup_path}")

    return kept, edited, deleted


if __name__ == '__main__':
    audit_file = Path(__file__).parent.parent / 'ACHIEVEMENT_AUDIT.md'
    resume_file = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not audit_file.exists():
        print(f"❌ Error: {audit_file} not found")
        print("Please complete the audit file first.")
        exit(1)

    if not resume_file.exists():
        print(f"❌ Error: {resume_file} not found")
        exit(1)

    print("🔍 Achievement Audit Applicator")
    print("=" * 80)
    print(f"Reading audit decisions from: {audit_file.name}")
    print("=" * 80)

    # Parse audit file
    decisions = parse_audit_file(audit_file)

    if not decisions:
        print("❌ No decisions found in audit file.")
        print("Please mark decisions as KEEP, EDIT, or DELETE in ACHIEVEMENT_AUDIT.md")
        exit(1)

    print(f"\nFound {len(decisions)} achievements with decisions:")
    keep_count = sum(1 for d in decisions if d['decision'] == 'KEEP')
    edit_count = sum(1 for d in decisions if d['decision'] == 'EDIT')
    delete_count = sum(1 for d in decisions if d['decision'] == 'DELETE')

    print(f"  KEEP:   {keep_count}")
    print(f"  EDIT:   {edit_count}")
    print(f"  DELETE: {delete_count}")

    # Check for --yes flag to skip confirmation
    import sys
    if '--yes' not in sys.argv:
        input("\nPress Enter to apply these decisions to resume.json (Ctrl+C to cancel)...")

    # Apply decisions
    apply_decisions_to_resume(resume_file, decisions)
