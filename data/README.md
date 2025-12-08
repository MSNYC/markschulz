# Resume Databank

This directory contains the **single source of truth** for all professional resume and career information.

## Structure

### `resume.json`
The master databank containing all professional information in a structured, machine-readable format.

## Schema Overview

```
resume.json
├── meta              # Version info, last updated date
├── personal          # Name, contact, location, social profiles
├── summary           # Professional summary (short, long, perspectives)
├── experience[]      # Work history with detailed achievements
│   ├── company info
│   ├── positions[]   # Multiple positions per company
│   │   ├── title, dates
│   │   ├── responsibilities[]
│   │   ├── achievements[]    # Categorized accomplishments
│   │   └── skills_used[]
│   └── ...
├── education[]       # Degrees and institutions
├── skills            # Comprehensive skill taxonomy
│   ├── core_competencies[]
│   ├── technical{}   # Subcategorized (ai_ml, analytics, etc.)
│   ├── marketing_specialized[]
│   ├── leadership[]
│   └── methodologies[]
├── languages[]       # Language proficiencies
├── professional_interests[]
├── certifications[]
├── publications[]
├── speaking[]
├── awards[]
├── projects[]        # Major projects with outcomes
└── keywords[]        # SEO/ATS keywords
```

## Usage

### 1. **Updating Information**
Edit `resume.json` directly or use scripts to update specific sections.

**Example: Adding a new achievement**
```json
{
  "category": "New Category",
  "items": [
    "Specific accomplishment with measurable impact"
  ]
}
```

### 2. **Extracting from Documents**
When you have new documents (performance reviews, project summaries, etc.):
1. Place document in `/docs/`
2. Run extraction script (to be created) or manually update JSON
3. Update `meta.last_updated` date
4. Increment `meta.version` if significant changes

### 3. **Generating Outputs**

From this databank, you can generate:
- **Website resume** (`about.md` on Jekyll site)
- **PDF resumes** (different formats/lengths)
- **LinkedIn profile** (optimized copy)
- **Cover letters** (pulling relevant experience)
- **Portfolio case studies** (from projects section)
- **Job applications** (tailored to specific roles)

## Maintenance Guidelines

### Keep It Current
- Update immediately after completing major projects
- Review quarterly for accuracy
- Add new skills as acquired
- Document quantifiable achievements

### Data Quality
- Use consistent date formats: `YYYY-MM` or `YYYY-MM-DD`
- Quantify achievements when possible (%, $, numbers)
- Keep language action-oriented and metric-driven
- Maintain parallel structure in lists

### Categories for Achievements
- **AI Innovation & Enterprise Enablement**
- **Strategy & Marketing Expertise**
- **Data Engineering & Analytics Leadership**
- **Automation & Workflow Optimization**
- **Creative & Concept Development**
- **Technical Problem-Solving & Tool Development**
- **Leadership, Collaboration & Innovation Culture**

## Version History

- **1.0.0** (2024-12-03): Initial databank created from resume.pdf and accomplishments documents

## 🔥 Achievement Extraction System

**NEW:** Automated tool for extracting achievements from old resumes and performance reviews using Claude API.

### Quick Start
1. **Install:** `pip install -r requirements.txt`
2. **Setup API:** `export ANTHROPIC_API_KEY='your-key'`
3. **Extract:** See [QUICK_START.md](QUICK_START.md) for detailed guide
4. **Verify:** `python verify_achievements.py`

### Documentation
- **[QUICK_START.md](QUICK_START.md)** - Setup and basic usage
- **[POSITION_REFERENCE.md](POSITION_REFERENCE.md)** - Position IDs and commands
- **[EXTRACTION_INSTRUCTIONS.md](EXTRACTION_INSTRUCTIONS.md)** - Detailed methodology
- **[achievement_extraction_schema.json](achievement_extraction_schema.json)** - JSON schema

### Tools
- ✅ **`batch_process.py`** - 🌟 **NEW!** Automated batch processor - just drop files in `raw_inputs/` and run!
- ✅ **`extract_and_load.py`** - AI-powered extraction from PDF/DOCX/TXT (supports image-based PDFs!)
- ✅ **`verify_achievements.py`** - Coverage analysis and gap identification
- ✅ **`load_achievements.py`** - Manual JSON loader

### Quick Start: Batch Processing (Recommended!)

**NEW: Automated batch processing!** Just drop all your files in `raw_inputs/` and run:

```bash
# 1. Put your PDFs, DOCs, TXT files in raw_inputs/
ls data/raw_inputs/

# 2. Run the batch processor
python3 data/batch_process.py

# That's it! Claude will:
# - Identify which position each document belongs to
# - Extract achievements automatically
# - Update resume.json
# - Handle image PDFs with vision
```

See **[BATCH_PROCESSING.md](BATCH_PROCESSING.md)** for detailed guide.

### Manual Processing (for specific files)

```bash
python extract_and_load.py ~/Documents/old_resume_2019.pdf \
  --company "WebMD/Medscape" \
  --title "Team Leader, Sr. Dir., Commercial Clinical Strategy" \
  --start-date 2018-01 --end-date 2019-12 --exp-id exp_003
```

### 🖼️ Image-Based PDF Support

The extraction tool now automatically handles **scanned PDFs** and **image-based PDFs** (where text is not selectable) using Claude's vision capabilities!

**How it works:**
1. The tool first attempts to extract text using PyPDF2
2. If little/no text is extracted (< 100 characters), it automatically switches to vision mode
3. PDF pages are converted to images using `pdf2image`
4. Images are sent to Claude API with vision for text extraction and analysis
5. Same extraction quality and schema as text-based PDFs

**System Requirements:**
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install poppler (required by pdf2image)
# macOS:
brew install poppler

# Ubuntu/Debian:
sudo apt-get install poppler-utils

# Windows:
# Download from https://github.com/oschwartz10612/poppler-windows/releases/
```

**Usage:**
No changes needed! Just run the same command with image-based PDFs:
```bash
python extract_and_load.py scanned_performance_review.pdf \
  --company "Company Name" \
  --title "Your Title" \
  --start-date 2020-01 --exp-id exp_001
```

The tool will automatically detect and handle image-based PDFs.

## Future Enhancements

- [x] ~~Python script to validate JSON schema~~ ✅ Built into extract_and_load.py
- [x] ~~Extraction pipeline for performance reviews~~ ✅ extract_and_load.py
- [ ] Script to generate markdown resume from JSON
- [ ] Script to generate LaTeX/PDF resume
- [ ] LinkedIn profile generator
- [ ] Cover letter template system
- [ ] ATS keyword optimizer
- [ ] Diff tool to compare versions over time

## File Naming Conventions

When adding supporting documents to `/docs/`:
- `resume_[version]_[date].pdf` - Generated resumes
- `source_[company]_[type]_[date].[ext]` - Source documents
- `achievements_[project]_[date].md` - Project notes

Example: `source_biolumina_performance_review_2024-06.pdf`
