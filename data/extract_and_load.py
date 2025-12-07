#!/usr/bin/env python3
"""
Automated Achievement Extractor & Loader
Uses Claude API to extract achievements from source documents and load into resume.json
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
import shutil
import anthropic

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load from .env in current directory or parent directories
except ImportError:
    pass  # dotenv not installed, will use system environment variables only

# Document reading libraries
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    from docx import Document as DocxDocument
except ImportError:
    DocxDocument = None


def read_text_file(filepath):
    """Read plain text file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def read_pdf_file(filepath):
    """Read PDF file"""
    if not PyPDF2:
        raise ImportError("PyPDF2 not installed. Run: pip install PyPDF2")

    text = []
    with open(filepath, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return '\n\n'.join(text)


def read_docx_file(filepath):
    """Read DOCX file"""
    if not DocxDocument:
        raise ImportError("python-docx not installed. Run: pip install python-docx")

    doc = DocxDocument(filepath)
    text = []
    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)
    return '\n'.join(text)


def read_document(filepath):
    """Read document based on file extension"""
    filepath = Path(filepath)
    suffix = filepath.suffix.lower()

    if suffix == '.txt':
        return read_text_file(filepath)
    elif suffix == '.pdf':
        return read_pdf_file(filepath)
    elif suffix in ['.docx', '.doc']:
        return read_docx_file(filepath)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def load_schema():
    """Load the extraction schema"""
    schema_path = Path(__file__).parent / 'achievement_extraction_schema.json'
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_resume():
    """Load resume.json"""
    resume_path = Path(__file__).parent / 'resume.json'
    with open(resume_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_extraction_prompt(document_text, position_info, schema):
    """Build the prompt for Claude to extract achievements"""

    prompt = f"""You are an expert resume analyst extracting specific, quantified achievements from career documents.

POSITION INFORMATION:
- Company: {position_info['company']}
- Title: {position_info['title']}
- Period: {position_info['start_date']} to {position_info.get('end_date', 'Present')}
- Experience ID: {position_info['experience_id']}

YOUR TASK:
Extract specific achievements from the source document below. Follow these rules:

1. QUALITY OVER QUANTITY
   - Each achievement must be SPECIFIC with metrics, outcomes, or concrete deliverables
   - Focus on ACCOMPLISHMENTS not just responsibilities
   - Look for: numbers, percentages, team sizes, budgets, improvements, innovations, firsts

2. TAGGING STRATEGY
   - Apply 2-6 tags per achievement from the tag taxonomy
   - Use tags that enable differentiation across these three profiles:
     * Brand Management: brand, portfolio, launch, positioning, budget_management, oncology, hcp
     * Strategic Planning: strategy, analytics, data_engineering, roi_modeling, innovation, ai, automation
     * CX & Omnichannel: cx, xp, journey_mapping, omnichannel, experience_planning, patient, crm

3. CONFIDENCE RATING
   - high: Directly stated with specifics in source
   - medium: Strongly implied or partially detailed
   - low: Inferred from context

TAG TAXONOMY:
{json.dumps(schema['tag_taxonomy'], indent=2)}

BAD EXAMPLE (too generic):
{json.dumps(schema['example_extraction']['bad_example'], indent=2)}

GOOD EXAMPLE (specific, measurable):
{json.dumps(schema['example_extraction']['good_example'], indent=2)}

OUTPUT FORMAT:
Return ONLY valid JSON matching this structure (no markdown, no code blocks, just raw JSON):
{{
  "position_metadata": {{
    "company": "{position_info['company']}",
    "company_parent": "{position_info.get('company_parent', '')}",
    "title": "{position_info['title']}",
    "start_date": "{position_info['start_date']}",
    "end_date": {json.dumps(position_info.get('end_date'))},
    "experience_id": "{position_info['experience_id']}"
  }},
  "achievements": [
    {{
      "text": "Specific achievement with metrics...",
      "tags": ["tag1", "tag2", "tag3"],
      "metric_type": "percentage|count|budget|time_saved|revenue (optional)",
      "source_confidence": "high|medium|low"
    }}
  ]
}}

SOURCE DOCUMENT:
{'=' * 80}
{document_text}
{'=' * 80}

Extract achievements now. Return ONLY the JSON, nothing else.
"""
    return prompt


def extract_with_claude(api_key, document_text, position_info, schema):
    """Use Claude API to extract achievements"""

    client = anthropic.Anthropic(api_key=api_key)

    prompt = build_extraction_prompt(document_text, position_info, schema)

    print("🤖 Sending to Claude API for extraction...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract text from response
    response_text = response.content[0].text.strip()

    # Remove markdown code blocks if present
    if response_text.startswith('```'):
        lines = response_text.split('\n')
        # Remove first and last lines (```)
        response_text = '\n'.join(lines[1:-1])
        # Remove 'json' if present
        if response_text.startswith('json'):
            response_text = response_text[4:].strip()

    # Parse JSON
    try:
        extracted_data = json.loads(response_text)
        return extracted_data
    except json.JSONDecodeError as e:
        print(f"❌ Claude returned invalid JSON:")
        print(response_text)
        raise e


def validate_extraction(data):
    """Validate extracted achievement data"""
    errors = []

    if 'position_metadata' not in data:
        errors.append("Missing 'position_metadata'")

    if 'achievements' not in data:
        errors.append("Missing 'achievements' array")
    elif not isinstance(data['achievements'], list):
        errors.append("'achievements' must be an array")
    else:
        for i, ach in enumerate(data['achievements']):
            if 'text' not in ach or not ach['text']:
                errors.append(f"Achievement {i}: Missing or empty 'text'")
            if 'tags' not in ach or not isinstance(ach['tags'], list) or len(ach['tags']) == 0:
                errors.append(f"Achievement {i}: Missing or empty 'tags' array")

    return errors


def create_backup(filepath):
    """Create timestamped backup of resume.json"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.parent / f"resume_backup_{timestamp}.json"
    shutil.copy2(filepath, backup_path)
    print(f"📦 Backup created: {backup_path}")
    return backup_path


def load_into_resume(extracted_data, resume_data):
    """Load extracted achievements into resume.json"""

    meta = extracted_data['position_metadata']

    # Find matching position
    for exp in resume_data['experience']:
        if exp['id'] == meta['experience_id']:
            for pos in exp['positions']:
                if pos['title'] == meta['title'] and pos['start_date'] == meta['start_date']:
                    # Found position - add achievements
                    new_category = {
                        "category": "Key Achievements",
                        "items": [
                            {
                                "text": ach['text'],
                                "tags": ach['tags'],
                                **({k: v for k, v in ach.items() if k not in ['text', 'tags']})
                            }
                            for ach in extracted_data['achievements']
                        ]
                    }

                    existing = pos.get('achievements', [])
                    pos['achievements'] = existing + [new_category]

                    print(f"✅ Loaded {len(extracted_data['achievements'])} achievements into position")
                    return True

    raise ValueError(f"Could not find matching position for {meta['title']} at {meta['company']}")


def save_json(data, filepath):
    """Save JSON with consistent formatting"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    print("=" * 80)
    print("AUTOMATED ACHIEVEMENT EXTRACTOR & LOADER")
    print("=" * 80)

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python extract_and_load.py <source_document> \\")
        print("    --company 'Company Name' \\")
        print("    --title 'Job Title' \\")
        print("    --start-date YYYY-MM \\")
        print("    --exp-id exp_XXX \\")
        print("    [--end-date YYYY-MM] \\")
        print("    [--company-parent 'Parent Company'] \\")
        print("    [--api-key YOUR_API_KEY]")
        print("\nExample:")
        print("  python extract_and_load.py old_resume_2018.pdf \\")
        print("    --company 'WebMD/Medscape' \\")
        print("    --title 'Team Leader, Sr. Dir., Commercial Clinical Strategy' \\")
        print("    --start-date 2018-01 \\")
        print("    --end-date 2019-12 \\")
        print("    --exp-id exp_003")
        print("\nAPI Key:")
        print("  Set via --api-key flag or ANTHROPIC_API_KEY environment variable")
        sys.exit(1)

    # Parse arguments
    source_file = Path(sys.argv[1])
    args = {}
    i = 2
    while i < len(sys.argv):
        if sys.argv[i].startswith('--'):
            key = sys.argv[i][2:].replace('-', '_')
            if i + 1 < len(sys.argv):
                args[key] = sys.argv[i + 1]
                i += 2
            else:
                print(f"❌ Missing value for {sys.argv[i]}")
                sys.exit(1)
        else:
            i += 1

    # Validate required args
    required = ['company', 'title', 'start_date', 'exp_id']
    missing = [r for r in required if r not in args]
    if missing:
        print(f"❌ Missing required arguments: {', '.join('--' + m.replace('_', '-') for m in missing)}")
        sys.exit(1)

    # Get API key
    api_key = args.get('api_key') or os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ No API key provided. Set ANTHROPIC_API_KEY environment variable or use --api-key flag")
        sys.exit(1)

    # Check source file exists
    if not source_file.exists():
        print(f"❌ Source file not found: {source_file}")
        sys.exit(1)

    print(f"\n📂 Source document: {source_file}")
    print(f"📋 Position: {args['title']}")
    print(f"🏢 Company: {args['company']}")
    print(f"📅 Period: {args['start_date']} to {args.get('end_date', 'Present')}\n")

    # Read source document
    print("📖 Reading source document...")
    try:
        document_text = read_document(source_file)
        print(f"✅ Read {len(document_text)} characters from document\n")
    except Exception as e:
        print(f"❌ Error reading document: {e}")
        sys.exit(1)

    # Load schema
    print("📋 Loading extraction schema...")
    schema = load_schema()
    print("✅ Schema loaded\n")

    # Prepare position info
    position_info = {
        'company': args['company'],
        'company_parent': args.get('company_parent', ''),
        'title': args['title'],
        'start_date': args['start_date'],
        'end_date': args.get('end_date'),
        'experience_id': args['exp_id']
    }

    # Extract with Claude
    try:
        extracted_data = extract_with_claude(api_key, document_text, position_info, schema)
        print("✅ Claude extraction complete\n")
    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        sys.exit(1)

    # Validate extraction
    print("🔍 Validating extracted data...")
    errors = validate_extraction(extracted_data)
    if errors:
        print("❌ Validation errors:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    print(f"✅ Validation passed - extracted {len(extracted_data['achievements'])} achievements\n")

    # Show extracted achievements
    print("📊 Extracted achievements:")
    for i, ach in enumerate(extracted_data['achievements'], 1):
        print(f"   {i}. {ach['text'][:80]}...")
        print(f"      Tags: {', '.join(ach['tags'])}")
        if 'source_confidence' in ach:
            print(f"      Confidence: {ach['source_confidence']}")
        print()

    # Load resume.json
    print("📂 Loading resume.json...")
    resume_path = Path(__file__).parent / 'resume.json'
    resume_data = load_resume()
    print("✅ Loaded\n")

    # Create backup
    create_backup(resume_path)

    # Load into resume
    print("💾 Loading achievements into resume.json...")
    try:
        load_into_resume(extracted_data, resume_data)
    except Exception as e:
        print(f"❌ Failed to load into resume: {e}")
        sys.exit(1)

    # Save updated resume.json
    print("💾 Saving updated resume.json...")
    save_json(resume_data, resume_path)
    print(f"✅ Saved: {resume_path}\n")

    print("=" * 80)
    print("✅ SUCCESS!")
    print("=" * 80)
    print(f"\nNext steps:")
    print(f"  1. Review the updated resume.json")
    print(f"  2. Run: python data/verify_achievements.py")
    print(f"  3. Extract more positions or proceed with resume generation")


if __name__ == '__main__':
    main()
