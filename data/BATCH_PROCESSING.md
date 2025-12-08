# Automated Batch Processing Guide

## Overview

The batch processor automatically:
1. ✅ Scans `data/raw_inputs/` for PDFs, DOCs, and TXT files
2. ✅ Uses Claude AI to identify which position each document belongs to
3. ✅ Extracts achievements automatically (with vision support for image PDFs!)
4. ✅ Updates `resume.json` with extracted data
5. ✅ Tracks processed files to avoid duplicates

## Quick Start

### 1. Put Your Files in raw_inputs/

```bash
# Your files are already there! Just add more as needed:
data/raw_inputs/
  ├── old_resume_2010.pdf
  ├── performance_review_2008.PDF
  ├── Myers_Briggs_assessment.pdf
  └── ... (any PDF, DOC, DOCX, or TXT files)
```

### 2. Make Sure API Key is Set

Check that you have your Claude API key in `.env`:
```bash
cat .env
# Should show: ANTHROPIC_API_KEY=sk-ant-...
```

### 3. Run the Batch Processor

```bash
python3 data/batch_process.py
```

That's it! The script will:
- Show you which files it found
- Ask for confirmation before processing
- Process each file automatically
- Show you the results

## How It Works

### Step 1: Position Identification

For each document, Claude analyzes:
- **Company names** mentioned in the document
- **Job titles** and role descriptions
- **Dates and time periods**
- **Project names** and context clues
- **Filename** for additional hints

Then matches against your existing positions in `resume.json`.

### Step 2: Confidence Check

Claude assigns confidence:
- **High**: Clear match with specific company, title, and dates
- **Medium**: Likely match with some ambiguity
- **Low**: Cannot confidently identify position

**Files with low confidence are skipped** and you can process them manually.

### Step 3: Achievement Extraction

Once position is identified, uses the same extraction logic as `extract_and_load.py`:
- Extracts specific, quantified achievements
- Applies appropriate tags for profile differentiation
- Validates output quality

### Step 4: Update Resume

- Creates backup of `resume.json`
- Loads new achievements into the identified position
- Saves updated resume
- Tracks file as processed

## Processed Files Tracking

The script maintains `data/processed_files.json`:

```json
{
  "processed": [
    {
      "filename": "old_resume_2019.pdf",
      "status": "success",
      "processed_at": "2024-12-07T18:30:00",
      "identification": {
        "company": "WebMD/Medscape",
        "title": "Team Leader, Sr. Dir., Commercial Clinical Strategy",
        "confidence": "high"
      },
      "achievements_count": 12
    }
  ],
  "failed": [],
  "last_run": "2024-12-07T18:30:00"
}
```

This ensures files are only processed once.

## What Gets Processed Automatically?

✅ **Will process automatically:**
- Old resumes with clear company/title/dates
- Performance reviews with position context
- Project summaries tied to specific roles

⏭️ **Will skip (manual processing needed):**
- Generic career documents without clear position markers
- Cover letters or reference letters
- Documents Claude can't confidently match (confidence: low)
- Personality assessments (Myers-Briggs, FIRO-B) - these need special handling

## Manual Processing for Skipped Files

If a file is skipped, you'll see:
```
⚠️  Low confidence - skipping automatic extraction
   Please process manually with extract_and_load.py
```

Then process it manually:
```bash
python3 data/extract_and_load.py data/raw_inputs/filename.pdf \
  --company "Company Name" \
  --title "Job Title" \
  --start-date 2020-01 \
  --exp-id exp_001
```

## Re-running the Batch Processor

Safe to run multiple times!
- Already processed files are skipped automatically
- Only new files in `raw_inputs/` will be processed
- Check `processed_files.json` to see what's been done

To reprocess a file:
1. Remove its entry from `processed_files.json`
2. Run batch processor again

To reprocess everything:
```bash
rm data/processed_files.json
python3 data/batch_process.py
```

## Example Output

```
================================================================================
AUTOMATED BATCH PROCESSOR
================================================================================
✅ API key loaded

📋 Loading processed files tracking...
   Previously processed: 3 files
   Previously failed: 0 files

🔍 Scanning raw_inputs/ directory...
   Found 17 total files
   Unprocessed: 14 files

📝 Will process:
   - 2010 6 9 MARK_SCHULZ_RESUME.pdf
   - MARK_SCHULZ_Dir_Mkt_Strat.pdf
   - Mark_Schulz_RESUME_20191107_final.pdf
   ... (11 more)

⚠️  This will use Claude API and update resume.json
Continue? [y/N]: y

📦 Creating backup of resume.json...
📦 Backup created: resume_backup_20241207_183045.json

================================================================================
Processing file 1/14
================================================================================
📄 Processing: Mark_Schulz_RESUME_20191107_final.pdf
================================================================================
  📖 Reading document...
  ✅ Read 8,453 characters
  🤖 Asking Claude to identify position...

  ✅ Identified Position:
     Company: WebMD/Medscape
     Title: Team Leader, Sr. Dir., Commercial Clinical Strategy
     Period: 2018-01 to 2019-12
     Confidence: high
     Reasoning: Document contains explicit WebMD/Medscape branding,
                references to clinical strategy role, and dates align
                with 2018-2019 timeframe.

  🔍 Extracting achievements...
  🤖 Sending to Claude API for extraction...
  ✅ Claude extraction complete
  ✅ Extracted 15 achievements

  🔍 Validating extracted data...
  ✅ Validation passed

  📊 Extracted Achievements:
     1. Led cross-functional analytics team processing 500K+ HCP engagement records...
        Tags: analytics, data_engineering, leadership, strategy
     2. Developed predictive models achieving 85% accuracy in targeting optimization...
        Tags: analytics, roi_modeling, data_science, strategy
     ... (13 more)

  💾 Loading into resume.json...
  ✅ Loaded successfully

[... continues for each file ...]

================================================================================
PROCESSING COMPLETE
================================================================================

📊 Results:
   ✅ Successfully processed: 12
   ⏭️  Skipped (low confidence): 2
   ❌ Failed: 0

   🎯 Total achievements extracted: 147

⚠️  Some files were skipped due to low confidence.
   Review and process manually

✅ Done! Check resume.json for updates.
   Run: python3 scripts/resume_manager.py summary
```

## Cost Estimate

Claude API usage (approximate):
- **Position identification**: ~$0.01 per document
- **Achievement extraction**: ~$0.01-0.03 per document
- **Total for 15 documents**: ~$0.30-0.60

Very affordable for automated processing of your entire career history!

## Troubleshooting

### "Directory not found: raw_inputs"
Your files are already in `data/raw_inputs/` so this shouldn't happen. If it does, check the path.

### "No API key found"
Make sure `.env` file exists in project root with:
```
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

### All files showing as "already processed"
Check `data/processed_files.json` - remove entries to reprocess files.

### Low extraction quality
- Check if source document is readable (not corrupted)
- For image PDFs, ensure poppler is installed: `brew install poppler`
- Review extracted achievements and manually edit `resume.json` if needed

## Next Steps After Batch Processing

1. **Review the results:**
   ```bash
   python3 scripts/resume_manager.py summary
   ```

2. **Verify achievement coverage:**
   ```bash
   python3 data/verify_achievements.py
   ```

3. **Generate updated resume:**
   ```bash
   python3 scripts/generate_resume_markdown.py
   ```

4. **Check the interactive resume:**
   Open `resume-interactive.html` in your browser to see the tag-filtered experience.
