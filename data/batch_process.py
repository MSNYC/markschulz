#!/usr/bin/env python3
"""
Automated Batch Processor for Resume Documents
Scans raw_inputs/, identifies positions, and extracts achievements automatically
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
    load_into_resume, save_json, create_backup
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


def identify_position_with_claude(api_key, document_text, resume_data, filepath):
    """Use Claude to identify which position this document belongs to"""

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

    prompt = f"""You are analyzing a career document to identify which job position it belongs to.

AVAILABLE POSITIONS:
{json.dumps(positions_info, indent=2)}

DOCUMENT FILENAME: {filepath.name}

DOCUMENT CONTENT:
{'=' * 80}
{document_text[:8000] if len(document_text) > 8000 else document_text}
{'=' * 80}

TASK:
Analyze this document and determine which position from the list it most likely belongs to.
Look for company names, job titles, dates, projects, and context clues.

Return ONLY valid JSON (no markdown, no code blocks):
{{
  "identified_position": {{
    "exp_id": "exp_XXX",
    "company": "Company Name",
    "title": "Job Title",
    "start_date": "YYYY-MM",
    "end_date": "YYYY-MM or null",
    "confidence": "high|medium|low"
  }},
  "reasoning": "Brief explanation of why this position was selected"
}}

If you cannot identify the position with reasonable confidence, set confidence to "low" and explain why.
"""

    print(f"  🤖 Asking Claude to identify position...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
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
        print(response_text)
        return None


def process_file(filepath, api_key, resume_data, schema):
    """Process a single file"""

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

    # Identify position with Claude
    try:
        identification = identify_position_with_claude(
            api_key,
            document_text if document_text != 'IMAGE_PDF' else f"[Image PDF: {filepath.name}]",
            resume_data,
            filepath
        )

        if not identification:
            return {'status': 'failed', 'error': 'Could not identify position'}

        pos_info = identification['identified_position']

        # Rename exp_id to experience_id for compatibility with extract_with_claude
        if 'exp_id' in pos_info:
            pos_info['experience_id'] = pos_info['exp_id']

        # Ensure company_parent exists (may be empty string)
        if 'company_parent' not in pos_info:
            pos_info['company_parent'] = ''

        print(f"\n  ✅ Identified Position:")
        print(f"     Company: {pos_info['company']}")
        print(f"     Title: {pos_info['title']}")
        print(f"     Period: {pos_info['start_date']} to {pos_info.get('end_date', 'Present')}")
        print(f"     Confidence: {pos_info['confidence']}")
        print(f"     Reasoning: {identification['reasoning']}")

        if pos_info['confidence'] == 'low':
            print(f"\n  ⚠️  Low confidence - skipping automatic extraction")
            print(f"     Please process manually with extract_and_load.py")
            return {'status': 'skipped', 'reason': 'low confidence', 'identification': identification}

    except Exception as e:
        print(f"  ❌ Error identifying position: {e}")
        return {'status': 'failed', 'error': f'Identification error: {e}'}

    # Extract achievements
    print(f"\n  🔍 Extracting achievements...")
    try:
        extracted_data = extract_with_claude(
            api_key,
            document_text,
            pos_info,
            schema,
            source_filepath=filepath
        )
        print(f"  ✅ Extracted {len(extracted_data['achievements'])} achievements")

    except Exception as e:
        print(f"  ❌ Extraction failed: {e}")
        return {'status': 'failed', 'error': f'Extraction error: {e}'}

    # Validate
    print(f"  🔍 Validating extracted data...")
    errors = validate_extraction(extracted_data)
    if errors:
        print(f"  ❌ Validation errors:")
        for error in errors:
            print(f"     - {error}")
        return {'status': 'failed', 'error': 'Validation failed', 'validation_errors': errors}
    print(f"  ✅ Validation passed")

    # Show achievements
    print(f"\n  📊 Extracted Achievements:")
    for i, ach in enumerate(extracted_data['achievements'][:5], 1):  # Show first 5
        print(f"     {i}. {ach['text'][:80]}...")
        print(f"        Tags: {', '.join(ach['tags'])}")
    if len(extracted_data['achievements']) > 5:
        print(f"     ... and {len(extracted_data['achievements']) - 5} more")

    # Load into resume
    print(f"\n  💾 Loading into resume.json...")
    try:
        load_into_resume(extracted_data, resume_data)
        print(f"  ✅ Loaded successfully")

        return {
            'status': 'success',
            'identification': identification,
            'achievements_count': len(extracted_data['achievements'])
        }

    except Exception as e:
        print(f"  ❌ Failed to load into resume: {e}")
        return {'status': 'failed', 'error': f'Load error: {e}'}


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
            print("Usage: python3 batch_process.py [options]")
            print("\nOptions:")
            print("  --dry-run        Show what would be processed without making changes")
            print("  --limit N        Only process first N files (for testing)")
            print("  --help, -h       Show this help message")
            print("\nExamples:")
            print("  python3 batch_process.py --dry-run")
            print("  python3 batch_process.py --limit 1")
            print("  python3 batch_process.py --dry-run --limit 3")
            sys.exit(0)

    print("=" * 80)
    print("AUTOMATED BATCH PROCESSOR")
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

        result = process_file(filepath, api_key, resume_data, schema)
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
            print(f"\n🔍 DRY RUN: Would have saved {len(successes)} updates to resume.json")

    # Summary
    print(f"\n{'=' * 80}")
    print("PROCESSING COMPLETE")
    print(f"{'=' * 80}")

    success_count = len([r for r in results if r['status'] == 'success'])
    failed_count = len([r for r in results if r['status'] == 'failed'])
    skipped_count = len([r for r in results if r['status'] == 'skipped'])

    print(f"\n📊 Results:")
    print(f"   ✅ Successfully processed: {success_count}")
    print(f"   ⏭️  Skipped (low confidence): {skipped_count}")
    print(f"   ❌ Failed: {failed_count}")

    if successes:
        total_achievements = sum(r['achievements_count'] for r in successes)
        print(f"\n   🎯 Total achievements extracted: {total_achievements}")

    if skipped_count > 0:
        print(f"\n⚠️  Some files were skipped due to low confidence.")
        print(f"   Review and process manually with:")
        print(f"   python3 data/extract_and_load.py <file> --company ... --title ... --exp-id ...")

    print(f"\n✅ Done! Check resume.json for updates.")
    print(f"   Run: python3 scripts/resume_manager.py summary")


if __name__ == '__main__':
    main()
