# Achievement Extraction - Quick Start Guide

## One-Time Setup

### 1. Install Dependencies
```bash
cd ~/coding/markschulz/data
pip install -r requirements.txt
```

### 2. Set API Key
Option A - Environment variable (recommended):
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Option B - Add to your shell profile (~/.zshrc or ~/.bashrc):
```bash
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

Option C - Pass via command line flag (less secure):
```bash
python extract_and_load.py ... --api-key your-api-key-here
```

## Usage

### Basic Workflow
For each old resume or performance review:

1. **Identify the position** in `resume.json` and note:
   - experience_id (e.g., `exp_003` for WebMD)
   - Company name
   - Job title
   - Start/end dates

2. **Run extraction:**
```bash
python data/extract_and_load.py path/to/old_resume.pdf \
  --company "WebMD/Medscape" \
  --title "Team Leader, Sr. Dir., Commercial Clinical Strategy" \
  --start-date 2018-01 \
  --end-date 2019-12 \
  --exp-id exp_003
```

3. **Review results** - Script will show extracted achievements before loading

4. **Verify coverage:**
```bash
python data/verify_achievements.py
```

## Real Examples

### WebMD Position (2018-2019)
```bash
python data/extract_and_load.py ~/Documents/old_resumes/resume_2019.pdf \
  --company "WebMD/Medscape" \
  --company-parent "Internet Brands" \
  --title "Team Leader, Sr. Dir., Commercial Clinical Strategy" \
  --start-date 2018-01 \
  --end-date 2019-12 \
  --exp-id exp_003
```

### Pfizer LIPITOR (2008-2012)
```bash
python data/extract_and_load.py ~/Documents/old_resumes/pfizer_review_2011.pdf \
  --company "Pfizer" \
  --title "Marketing Manager - LIPITOR / CADUET" \
  --start-date 2008-01 \
  --end-date 2012-01 \
  --exp-id exp_005
```

### Patients & Purpose (2015-2016)
```bash
python data/extract_and_load.py ~/Documents/old_resumes/resume_2016.docx \
  --company "Patients & Purpose" \
  --company-parent "Omnicom" \
  --title "VP, Project Management, Group Supervisor" \
  --start-date 2015-01 \
  --end-date 2016-12 \
  --exp-id exp_004
```

## Supported File Types
- **PDF**: `.pdf` files
- **Word**: `.docx` files
- **Text**: `.txt` files

## Workflow Tips

### Priority Order
Extract in this order for maximum impact:
1. WebMD/Medscape roles (2016-2019) - Rich in analytics/strategy
2. Pfizer LIPITOR (2008-2012) - Brand management excellence
3. Patients & Purpose VP (2015-2016) - Leadership/PM
4. Other positions as needed

### Multiple Documents per Position
If you have multiple documents for one position (resume + performance review):
```bash
# First document
python data/extract_and_load.py old_resume_2018.pdf --company "WebMD/Medscape" ...

# Second document (adds more achievements)
python data/extract_and_load.py performance_review_2019.pdf --company "WebMD/Medscape" ...
```

The tool will append new achievements to existing ones.

### Checking Progress
After each extraction, run:
```bash
python data/verify_achievements.py
```

This shows:
- ✅ Which positions have achievements
- 📊 Tag coverage per position
- 🎯 Profile differentiation potential
- ⚠️  Which positions still need extraction

## Troubleshooting

### "PyPDF2 not installed"
```bash
pip install PyPDF2
```

### "python-docx not installed"
```bash
pip install python-docx
```

### "No API key provided"
Set the ANTHROPIC_API_KEY environment variable (see Setup above)

### "Could not find matching position"
Check that:
- `--exp-id` matches the id in resume.json (e.g., exp_003)
- `--company` matches exactly
- `--title` matches exactly
- `--start-date` matches exactly (format: YYYY-MM)

### Extraction Quality Issues
If Claude extracts low-quality achievements:
1. Check source document quality (is it readable?)
2. Try a different source document with more detail
3. Manually review and edit resume.json after extraction

## After Extraction Complete

Once you've extracted achievements for key positions:

1. **Verify coverage:**
   ```bash
   python data/verify_achievements.py
   ```

2. **Proceed to tag-based resume generation** (Phase 3)
   - Build Liquid templating in Jekyll layouts
   - Filter achievements by profile tags
   - Generate differentiated resumes

## Cost Estimate

Claude API costs (approximate):
- Small doc (1 page resume): ~$0.01 per extraction
- Large doc (3 page review): ~$0.03 per extraction
- Total for ~5-8 positions: **~$0.10 - $0.30**

Very affordable for the value of automated, high-quality extraction!
