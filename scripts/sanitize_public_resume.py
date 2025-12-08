#!/usr/bin/env python3
"""
Create a sanitized public version of resume.json
Removes sensitive personal information while keeping professional data
"""
import json
import sys
from pathlib import Path

def sanitize_resume(input_file, output_file):
    """Create public-safe version of resume.json"""

    with open(input_file, 'r') as f:
        resume = json.load(f)

    # SANITIZE PERSONAL INFORMATION
    if 'personal' in resume:
        personal = resume['personal']

        # Remove phone and email
        if 'contact' in personal:
            contact = personal['contact']

            # Replace with contact form or generic
            contact['phone'] = None  # Remove phone
            contact['email'] = 'contact@markschulz.me'  # Generic contact email

            # Keep city/state, remove street address if present
            if 'location' in contact:
                loc = contact['location']
                # Keep only city and state
                safe_location = {
                    'city': loc.get('city', ''),
                    'state': loc.get('state', ''),
                    'country': loc.get('country', 'USA')
                }
                # Remove any address fields
                contact['location'] = safe_location

    # Check for salary/compensation in achievements
    # (Just a safety check - shouldn't be there)
    salary_keywords = ['salary', 'compensation', 'wage', 'pay grade', '$XXX,XXX']

    print("🔍 Scanning for sensitive information...")
    warnings = []

    for exp in resume.get('experience', []):
        for pos in exp.get('positions', []):
            for ach_cat in pos.get('achievements', []):
                if isinstance(ach_cat, dict):
                    for item in ach_cat.get('items', []):
                        text = item.get('text', '') if isinstance(item, dict) else str(item)
                        for keyword in salary_keywords:
                            if keyword.lower() in text.lower():
                                warnings.append(f"⚠️  Possible salary reference: {text[:80]}...")

    if warnings:
        print("\n⚠️  WARNINGS - Review these before publishing:")
        for w in warnings:
            print(f"   {w}")
        print()

    # Save sanitized version
    with open(output_file, 'w') as f:
        json.dump(resume, f, indent=2, ensure_ascii=False)

    print(f"✅ Created sanitized public resume")
    print(f"   Input:  {input_file}")
    print(f"   Output: {output_file}")
    print()
    print("📋 What was removed:")
    print("   ❌ Phone number")
    print("   ❌ Personal email (replaced with contact@markschulz.me)")
    print()
    print("✅ What was kept:")
    print("   ✅ Name and professional title")
    print("   ✅ City/State location (New York, NY)")
    print("   ✅ Website URL")
    print("   ✅ All work experience and achievements")
    print("   ✅ Skills, education, projects")
    print()
    print("🔍 Next steps:")
    print("   1. Review the sanitized file")
    print("   2. Check for any other sensitive info")
    print("   3. Copy to public location when ready:")
    print(f"      cp {output_file} assets/data/resume.json")

if __name__ == '__main__':
    script_dir = Path(__file__).parent.parent
    input_file = script_dir / 'data' / 'resume.json'
    output_file = script_dir / 'data' / 'resume_public.json'

    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        sys.exit(1)

    sanitize_resume(input_file, output_file)
