#!/usr/bin/env python3
"""
Automated Batch Processor v2 - Multi-position aware
Handles multiple positions per document, deduplication, and achievement merging
"""
import json
import os
import sys
from pathlib import Path
from datetime import datetime
import anthropic
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Import from extract_and_load
from extract_and_load import (
    read_document, load_schema, load_resume,
    extract_with_claude, validate_extraction,
    save_json, create_backup
)


def load_processed_files():
    """Load tracking file for already processed documents"""
    processed_file = Path(__file__).parent / 'processed_files.json'
    if processed_file.exists():
        with open(processed_file, 'r') as f:
            return json.load(f)
    return {"processed": [], "failed": [], "last_run": None}


def save_processed_files(data):
    """Save tracking file"""
    processed_file = Path(__file__).parent / 'processed_files.json'
    data['last_run'] = datetime.now().isoformat()
    with open(processed_file, 'w') as f:
        json.dump(data, f, indent=2)


def scan_raw_inputs():
    """Scan raw_inputs directory for unprocessed files"""
    raw_inputs = Path(__file__).parent / 'raw_inputs'
    if not raw_inputs.exists():
        print(f"❌ Directory not found: {raw_inputs}")
        return []

    supported_extensions = ['.pdf', '.docx', '.doc', '.txt']
    files = []

    for ext in supported_extensions:
        files.extend(raw_inputs.glob(f'*{ext}'))

    return sorted(files)


def identify_all_positions_in_document(api_key, document_text, resume_data, filepath):
    """Use Claude to identify ALL positions mentioned in this document"""

    # Build list of positions from resume.json
    positions_info = []
    for exp in resume_data['experience']:
        for pos in exp['positions']:
            positions_info.append({
                'exp_id': exp['id'],
                'company': exp['company'],
                'company_parent': exp.get('company_parent', ''),
                'title': pos['title'],
                'start_date': pos['start_date'],
                'end_date': pos.get('end_date', 'Present')
            })

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are analyzing a career document that may contain information about MULTIPLE job positions across a person's career history.

KNOWN POSITIONS IN RESUME DATABASE:
{json.dumps(positions_info, indent=2)}

DOCUMENT FILENAME: {filepath.name}

DOCUMENT CONTENT:
{'=' * 80}
{document_text[:12000] if len(document_text) > 12000 else document_text}
{'=' * 80}

TASK:
Identify ALL positions mentioned in this document that match positions from the database.
A resume typically covers multiple jobs - extract information for ALL of them.

For each position you identify, assess:
1. Which database position it matches
2. Confidence level (high/medium/low)
3. Whether there appear to be achievements/details worth extracting

Return ONLY valid JSON (no markdown, no code blocks):
{{
  "positions_found": [
    {{
      "exp_id": "exp_XXX",
      "company": "Company Name",
      "title": "Job Title",
      "start_date": "YYYY-MM",
      "end_date": "YYYY-MM or null",
      "confidence": "high|medium|low",
      "has_extractable_content": true|false,
      "brief_summary": "What info this document contains about this position"
    }}
  ],
  "document_type": "resume|performance_review|assessment|other",
  "overall_quality": "high|medium|low"
}}

Guidelines:
- Include ALL positions you can identify with reasonable confidence
- Set has_extractable_content=false if position is just mentioned in passing
- Set confidence=low if you're not sure about the match
"""

    print(f"  🤖 Asking Claude to identify ALL positions in document...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = response.content[0].text.strip()

    # Remove markdown if present
    if response_text.startswith('```'):
        lines = response_text.split('\n')
        response_text = '\n'.join(lines[1:-1])
        if response_text.startswith('json'):
            response_text = response_text[4:].strip()

    try:
        result = json.loads(response_text)
        return result
    except json.JSONDecodeError as e:
        print(f"  ❌ Claude returned invalid JSON: {e}")
        print(response_text[:500])
        return None


def merge_achievements_into_position(new_achievements, existing_position, source_filename):
    """Merge new achievements into existing position, avoiding exact duplicates"""

    # Get existing achievement texts for comparison
    existing_texts = set()
    achievements_list = existing_position.get('achievements', [])

    # Handle both formats: list of strings OR list of dicts with 'items'
    if achievements_list:
        # Check if it's a list of strings (old format)
        if isinstance(achievements_list[0], str):
            existing_texts = set(str(item).lower().strip() for item in achievements_list)
        # Or list of category dicts (new format)
        elif isinstance(achievements_list[0], dict):
            for category in achievements_list:
                items = category.get('items', [])
                for item in items:
                    if isinstance(item, dict):
                        existing_texts.add(item.get('text', '').lower().strip())
                    else:
                        existing_texts.add(str(item).lower().strip())

    # Filter out exact duplicates
    genuinely_new = []
    duplicates = 0

    for ach in new_achievements:
        ach_text = ach['text'].lower().strip()
        if ach_text not in existing_texts:
            # Add source tracking
            ach['source_document'] = source_filename
            ach['extracted_date'] = datetime.now().strftime('%Y-%m-%d')
            genuinely_new.append(ach)
        else:
            duplicates += 1

    if genuinely_new:
        # Create new category for this extraction
        new_category = {
            "category": f"Extracted from {source_filename}",
            "source": source_filename,
            "extraction_date": datetime.now().strftime('%Y-%m-%d'),
            "items": [
                {
                    "text": ach['text'],
                    "tags": ach['tags'],
                    **({k: v for k, v in ach.items() if k not in ['text', 'tags']})
                }
                for ach in genuinely_new
            ]
        }

        if 'achievements' not in existing_position:
            existing_position['achievements'] = []

        # Convert old format (list of strings) to new format if needed
        if existing_position['achievements'] and isinstance(existing_position['achievements'][0], str):
            old_achievements = existing_position['achievements']
            existing_position['achievements'] = [{
                "category": "Previous achievements",
                "items": old_achievements
            }]

        existing_position['achievements'].append(new_category)

    return len(genuinely_new), duplicates


def process_file_multiposition(filepath, api_key, resume_data, schema):
    """Process a single file, extracting from ALL positions found"""

    print(f"\n{'=' * 80}")
    print(f"📄 Processing: {filepath.name}")
    print(f"{'=' * 80}")

    # Read document
    print("  📖 Reading document...")
    try:
        document_text = read_document(filepath)
        if document_text == 'IMAGE_PDF':
            print("  ⚠️  Image-based PDF detected - will use vision mode")
        else:
            print(f"  ✅ Read {len(document_text):,} characters")
    except Exception as e:
        print(f"  ❌ Error reading document: {e}")
        return {'status': 'failed', 'error': f'Read error: {e}'}

    # Identify ALL positions in document
    try:
        analysis = identify_all_positions_in_document(
            api_key,
            document_text if document_text != 'IMAGE_PDF' else f"[Image PDF: {filepath.name}]",
            resume_data,
            filepath
        )

        if not analysis or 'positions_found' not in analysis:
            return {'status': 'failed', 'error': 'Could not analyze document'}

        positions_found = analysis['positions_found']
        print(f"\n  ✅ Document Analysis:")
        print(f"     Type: {analysis.get('document_type', 'unknown')}")
        print(f"     Quality: {analysis.get('overall_quality', 'unknown')}")
        print(f"     Positions found: {len(positions_found)}")

        if not positions_found:
            print(f"  ⚠️  No positions identified in document")
            return {'status': 'skipped', 'reason': 'no positions found'}

        # Show all identified positions
        for i, pos in enumerate(positions_found, 1):
            print(f"\n  Position {i}:")
            print(f"     Company: {pos['company']}")
            print(f"     Title: {pos['title']}")
            print(f"     Period: {pos['start_date']} to {pos.get('end_date', 'Present')}")
            print(f"     Confidence: {pos['confidence']}")
            print(f"     Has content: {pos.get('has_extractable_content', True)}")
            print(f"     Summary: {pos.get('brief_summary', 'N/A')}")

    except Exception as e:
        print(f"  ❌ Error analyzing document: {e}")
        return {'status': 'failed', 'error': f'Analysis error: {e}'}

    # Filter to high-confidence positions with extractable content
    extractable_positions = [
        p for p in positions_found
        if p['confidence'] in ['high', 'medium'] and p.get('has_extractable_content', True)
    ]

    if not extractable_positions:
        print(f"\n  ⏭️  No high-confidence extractable positions found")
        return {
            'status': 'skipped',
            'reason': 'no extractable positions',
            'positions_found': len(positions_found)
        }

    print(f"\n  🎯 Will extract from {len(extractable_positions)} position(s)")

    # Extract achievements for each position
    extraction_results = []

    for pos_info in extractable_positions:
        print(f"\n  {'─' * 76}")
        print(f"  🔍 Extracting for: {pos_info['company']} - {pos_info['title']}")

        # Add required fields for extract_with_claude
        pos_info['experience_id'] = pos_info.get('exp_id', '')
        if 'company_parent' not in pos_info:
            pos_info['company_parent'] = ''

        try:
            extracted_data = extract_with_claude(
                api_key,
                document_text,
                pos_info,
                schema,
                source_filepath=filepath
            )

            # Validate
            errors = validate_extraction(extracted_data)
            if errors:
                print(f"  ⚠️  Validation errors: {errors}")
                extraction_results.append({
                    'position': pos_info,
                    'status': 'validation_failed',
                    'errors': errors
                })
                continue

            ach_count = len(extracted_data['achievements'])
            print(f"  ✅ Extracted {ach_count} achievements")

            # Show first few
            for i, ach in enumerate(extracted_data['achievements'][:3], 1):
                print(f"     {i}. {ach['text'][:70]}...")
            if ach_count > 3:
                print(f"     ... and {ach_count - 3} more")

            # Find matching position in resume and merge (fuzzy matching)
            merged_count, duplicate_count = 0, 0
            position_found = False

            for exp in resume_data['experience']:
                if exp['id'] == pos_info['experience_id']:
                    for position in exp['positions']:
                        # Match on title (exact) and company (via exp_id)
                        # Don't require exact date match - dates vary across resume versions
                        if position['title'] == pos_info['title']:
                            print(f"  ✅ Matched to position: {position['title']} ({position['start_date']})")

                            merged_count, duplicate_count = merge_achievements_into_position(
                                extracted_data['achievements'],
                                position,
                                filepath.name
                            )
                            position_found = True
                            break
                if position_found:
                    break

            if not position_found:
                print(f"  ⚠️  Warning: Could not find matching position in resume.json")
                extraction_results.append({
                    'position': pos_info,
                    'status': 'position_not_found',
                    'achievements_extracted': ach_count
                })
                continue

            print(f"  ✅ Merged: {merged_count} new, {duplicate_count} duplicates skipped")

            extraction_results.append({
                'position': pos_info,
                'status': 'success',
                'achievements_extracted': ach_count,
                'merged_new': merged_count,
                'duplicates_skipped': duplicate_count
            })

        except Exception as e:
            print(f"  ❌ Extraction failed: {e}")
            extraction_results.append({
                'position': pos_info,
                'status': 'extraction_failed',
                'error': str(e)
            })

    # Summarize results for this file
    successful = [r for r in extraction_results if r['status'] == 'success']
    failed = [r for r in extraction_results if r['status'] != 'success']

    return {
        'status': 'success' if successful else 'failed',
        'positions_processed': len(extraction_results),
        'successful_extractions': len(successful),
        'failed_extractions': len(failed),
        'total_new_achievements': sum(r.get('merged_new', 0) for r in successful),
        'total_duplicates_skipped': sum(r.get('duplicates_skipped', 0) for r in successful),
        'extraction_results': extraction_results
    }


def main():
    # Parse command line arguments
    dry_run = '--dry-run' in sys.argv
    limit = None

    for i, arg in enumerate(sys.argv):
        if arg == '--limit' and i + 1 < len(sys.argv):
            try:
                limit = int(sys.argv[i + 1])
            except ValueError:
                print(f"❌ Invalid --limit value: {sys.argv[i + 1]}")
                sys.exit(1)
        elif arg in ['--help', '-h']:
            print("Usage: python3 batch_process_v2.py [options]")
            print("\nOptions:")
            print("  --dry-run        Show what would be processed without making changes")
            print("  --limit N        Only process first N files (for testing)")
            print("  --help, -h       Show this help message")
            print("\nChanges in v2:")
            print("  ✅ Extracts from ALL positions found in a document")
            print("  ✅ Deduplicates achievements automatically")
            print("  ✅ Merges new achievements into existing positions")
            print("  ✅ Tracks source documents for each achievement")
            sys.exit(0)

    print("=" * 80)
    print("AUTOMATED BATCH PROCESSOR v2")
    print("Multi-position aware with deduplication")
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    if limit:
        print(f"📊 LIMIT: Processing max {limit} file(s)")
    print("=" * 80)

    # Check API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("\n❌ No API key found!")
        print("Set ANTHROPIC_API_KEY in your .env file")
        sys.exit(1)
    print(f"✅ API key loaded")

    # Load tracking data
    print("\n📋 Loading processed files tracking...")
    tracking = load_processed_files()
    print(f"   Previously processed: {len(tracking['processed'])} files")
    print(f"   Previously failed: {len(tracking['failed'])} files")

    # Scan for files
    print("\n🔍 Scanning raw_inputs/ directory...")
    all_files = scan_raw_inputs()
    print(f"   Found {len(all_files)} total files")

    # Filter to unprocessed files
    processed_names = [p['filename'] for p in tracking['processed']]
    unprocessed_files = [f for f in all_files if f.name not in processed_names]
    print(f"   Unprocessed: {len(unprocessed_files)} files")

    if not unprocessed_files:
        print("\n✅ All files already processed!")
        return

    # Apply limit if specified
    if limit and len(unprocessed_files) > limit:
        print(f"\n📊 Limiting to first {limit} file(s) for testing")
        unprocessed_files = unprocessed_files[:limit]

    # Show what will be processed
    print(f"\n📝 Will process:")
    for f in unprocessed_files:
        print(f"   - {f.name}")

    # Confirm
    if dry_run:
        print(f"\n🔍 DRY RUN: Will show what would be extracted (no changes to resume.json)")
    else:
        print(f"\n⚠️  This will use Claude API and update resume.json")
    response = input("Continue? [y/N]: ")
    if response.lower() != 'y':
        print("Cancelled")
        return

    # Load schema and resume
    print("\n📋 Loading schema and resume.json...")
    schema = load_schema()
    resume_data = load_resume()
    resume_path = Path(__file__).parent / 'resume.json'

    # Create backup (only if not dry run)
    if not dry_run:
        print("\n📦 Creating backup of resume.json...")
        create_backup(resume_path)
    else:
        print("\n🔍 DRY RUN: Skipping backup creation")

    # Process each file
    results = []
    for i, filepath in enumerate(unprocessed_files, 1):
        print(f"\n{'=' * 80}")
        print(f"Processing file {i}/{len(unprocessed_files)}")

        result = process_file_multiposition(filepath, api_key, resume_data, schema)
        result['filename'] = filepath.name
        result['processed_at'] = datetime.now().isoformat()
        results.append(result)

        # Update tracking (only if not dry run)
        if not dry_run:
            if result['status'] == 'success':
                tracking['processed'].append(result)
            elif result['status'] == 'failed':
                tracking['failed'].append(result)
            save_processed_files(tracking)

    # Save updated resume.json if any successes (only if not dry run)
    successes = [r for r in results if r['status'] == 'success']
    if successes:
        if not dry_run:
            print(f"\n💾 Saving updated resume.json...")
            save_json(resume_data, resume_path)
            print(f"✅ Saved")
        else:
            print(f"\n🔍 DRY RUN: Would have saved updates to resume.json")

    # Summary
    print(f"\n{'=' * 80}")
    print("PROCESSING COMPLETE")
    print(f"{'=' * 80}")

    success_count = len([r for r in results if r['status'] == 'success'])
    failed_count = len([r for r in results if r['status'] == 'failed'])
    skipped_count = len([r for r in results if r['status'] == 'skipped'])

    print(f"\n📊 File Results:")
    print(f"   ✅ Successfully processed: {success_count}")
    print(f"   ⏭️  Skipped: {skipped_count}")
    print(f"   ❌ Failed: {failed_count}")

    if successes:
        total_new = sum(r.get('total_new_achievements', 0) for r in successes)
        total_dupes = sum(r.get('total_duplicates_skipped', 0) for r in successes)
        total_positions = sum(r.get('positions_processed', 0) for r in successes)

        print(f"\n📊 Achievement Results:")
        print(f"   🎯 Total positions processed: {total_positions}")
        print(f"   ✨ New achievements added: {total_new}")
        print(f"   🔄 Duplicates skipped: {total_dupes}")

    if not dry_run:
        print(f"\n✅ Done! Check resume.json for updates.")
        print(f"   Run: python3 scripts/resume_manager.py summary")
    else:
        print(f"\n🔍 DRY RUN complete - no changes made")


if __name__ == '__main__':
    main()
