#!/usr/bin/env python3
"""
Fix Podcast Attribution - Keep ONLY in VIAGRA positions
"""

import json
import sys
from pathlib import Path

def fix_podcast_attribution(resume_path):
    """Remove podcast achievements from all positions except VIAGRA"""

    print("Loading resume.json...")
    with open(resume_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Backup
    backup_path = resume_path.parent / 'resume.json.backup_podcast'
    print(f"Creating backup at {backup_path}...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    removed_count = 0
    kept_count = 0

    for exp in data.get('experience', []):
        for position in exp.get('positions', []):
            is_viagra_position = 'viagra' in position.get('title', '').lower()

            for group in position.get('achievements', []):
                items = group.get('items', [])
                new_items = []

                for item in items:
                    if isinstance(item, dict) and 'text' in item:
                        text_lower = item['text'].lower()
                        is_podcast = 'podcast' in text_lower

                        if is_podcast:
                            if is_viagra_position:
                                print(f"✓ KEEPING podcast in: {exp['company']} - {position['title']}")
                                print(f"  {item['text'][:70]}...")
                                new_items.append(item)
                                kept_count += 1
                            else:
                                print(f"✗ REMOVING podcast from: {exp['company']} - {position['title']}")
                                print(f"  {item['text'][:70]}...")
                                removed_count += 1
                        else:
                            new_items.append(item)
                    else:
                        new_items.append(item)

                group['items'] = new_items

    # Save
    print(f"\n📝 Writing corrected resume...")
    with open(resume_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Podcast attribution fixed!")
    print(f"   Kept {kept_count} in VIAGRA positions")
    print(f"   Removed {removed_count} from wrong positions")
    print(f"   Backup: {backup_path}")

    return removed_count

if __name__ == '__main__':
    resume_path = Path(__file__).parent.parent / 'assets' / 'data' / 'resume.json'

    if not resume_path.exists():
        print(f"❌ Error: {resume_path} not found")
        sys.exit(1)

    print("🔧 Podcast Attribution Fix")
    print("=" * 70)
    print("Keeping podcast ONLY in VIAGRA positions...")
    print("=" * 70)

    removed = fix_podcast_attribution(resume_path)

    print("\n" + "=" * 70)
    print(f"✨ Done! The podcast achievement now appears only in VIAGRA positions.")
