# Testing Guide for Batch Processor

Before processing all your files, let's test the system step by step.

## Step 1: Test Vision Capability (Quick Test)

First, verify that Claude Vision can read your PDFs:

```bash
python3 data/test_vision.py data/raw_inputs/2010\ 6\ 9\ MARK_SCHULZ_RESUME.pdf
```

**Expected result:**
- ✅ API key loaded confirmation
- ✅ PDF converted to image
- ✅ Claude extracts and shows text from the PDF

If this works, vision is working correctly!

---

## Step 2: Dry Run on Single File

Test the batch processor on **just 1 file** without making any changes:

```bash
python3 data/batch_process.py --dry-run --limit 1
```

**What this does:**
- Shows what the processor would do
- Uses Claude to identify which position the file belongs to
- Shows what achievements would be extracted
- **Does NOT update resume.json**
- **Does NOT track the file as processed**

**Expected output:**
```
🔍 DRY RUN MODE - No changes will be made
📊 LIMIT: Processing max 1 file(s)
...
✅ Identified Position:
   Company: ...
   Title: ...
   Confidence: high/medium/low
...
📊 Extracted Achievements:
   1. ...
   2. ...

🔍 DRY RUN: Would have saved 1 updates to resume.json
```

**Check:**
- ✅ Did Claude correctly identify the company/position?
- ✅ Are the extracted achievements relevant and high-quality?
- ✅ Are the tags appropriate?

---

## Step 3: Dry Run on 3 Files

Test on a few more files to see variety:

```bash
python3 data/batch_process.py --dry-run --limit 3
```

This will process 3 files and show you what would be extracted from each.

**Look for:**
- Position identification accuracy
- Achievement quality
- How it handles different file types (PDF vs DOC vs TXT)
- How it handles image PDFs vs text PDFs

---

## Step 4: Real Run on Single File

If dry runs look good, process **one file for real**:

```bash
python3 data/batch_process.py --limit 1
```

This will:
- ✅ Create backup of resume.json
- ✅ Process the file
- ✅ Update resume.json
- ✅ Track as processed

**After processing, verify:**

```bash
# Check what was added to resume.json
python3 scripts/resume_manager.py summary

# Or view specific experience
python3 scripts/resume_manager.py experience
```

**Inspect resume.json:**
- Open `data/resume.json` in your editor
- Find the position that was updated
- Review the achievements that were added
- Make sure they look good!

If anything looks wrong:
- Restore from backup: `data/resume_backup_YYYYMMDD_HHMMSS.json`
- Or manually edit `resume.json` to fix

---

## Step 5: Process All Files

Once you're confident it's working well:

```bash
python3 data/batch_process.py
```

This will process all unprocessed files in `raw_inputs/`.

**Monitor the output:**
- Watch position identifications
- Check confidence levels
- Review extracted achievements as they scroll by

The script will:
- Create a backup before starting
- Process each file
- Track successes/failures
- Save everything at the end

---

## Troubleshooting During Testing

### "Low confidence" warnings

Some files might get "low confidence" identification. This is **good** - it means Claude isn't sure and won't automatically process them.

For these files, process manually:
```bash
python3 data/extract_and_load.py data/raw_inputs/filename.pdf \
  --company "Company Name" \
  --title "Job Title" \
  --start-date 2020-01 \
  --exp-id exp_001
```

### Poor extraction quality

If extracted achievements look generic or low-quality:
- Check if the source document is readable
- Try a different source document for that position
- Manually edit resume.json after extraction

### Position identification errors

If Claude identifies the wrong position:
- Use `--dry-run` to see before committing
- Process manually with `extract_and_load.py` instead
- Add entry to `processed_files.json` to skip that file in batch

### Vision not working for image PDFs

Make sure poppler is installed:
```bash
# Check if installed
which pdfinfo

# Install if needed
brew install poppler
```

---

## Quick Reference: Testing Commands

```bash
# Test vision on one PDF
python3 data/test_vision.py data/raw_inputs/filename.pdf

# Dry run on 1 file (safe)
python3 data/batch_process.py --dry-run --limit 1

# Dry run on 3 files (safe)
python3 data/batch_process.py --dry-run --limit 3

# Real run on 1 file (creates backup)
python3 data/batch_process.py --limit 1

# Process everything (after testing)
python3 data/batch_process.py

# Check results
python3 scripts/resume_manager.py summary
```

---

## Recommended Testing Flow

1. ✅ Test vision with `test_vision.py` on one PDF
2. ✅ Dry run on 1 file
3. ✅ Review dry run output
4. ✅ Dry run on 3 files
5. ✅ If all looks good, real run on 1 file
6. ✅ Verify resume.json was updated correctly
7. ✅ If good, run full batch

**Take your time!** Better to test thoroughly than to have to restore from backup later.
