# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a professional portfolio website built with Jekyll for Mark Schulz, a pharmaceutical marketing and advertising professional. The site is structured around a data-driven resume system that maintains a single source of truth (`data/resume.json`) and generates various outputs including web pages, markdown resumes, and an interactive resume builder.

## Key Architecture

### Resume Databank System

The core architecture centers on **`data/resume.json`** as the single source of truth for all professional information:

- **Structure**: Comprehensive JSON schema containing personal info, experience, skills, projects, education, therapeutic areas, and more
- **Version controlled**: Uses semantic versioning (major.minor.patch) tracked in `meta.version`
- **Achievement categorization**: Grouped into categories like "AI Innovation & Enterprise Enablement", "Strategy & Marketing Expertise", etc.

### Python Scripts

Located in `scripts/`:

1. **`resume_manager.py`** - CLI tool for viewing and searching resume data
   - Commands: `summary`, `experience`, `skills`, `projects`, `search <term>`
   - Usage: `python3 scripts/resume_manager.py summary`

2. **`generate_resume_markdown.py`** - Generates ATS-optimized markdown from resume.json
   - Supports `--full` flag for extended version
   - Outputs to `output/MarkSchulz_Resume.md` by default
   - Usage: `python3 scripts/generate_resume_markdown.py [--full] [--output FILE]`

3. **`validate_tags.py`** - Validates resume tags against profile taxonomy

### Interactive Resume

- **`resume-interactive.html`** - Client-side interactive resume that filters experience/skills based on role profiles
- **`data/resume_profiles.json`** - Defines three role profiles (Brand Management, Strategy & Innovation, CX & Engagement) with priority tags and filtering rules
- Uses tag matching algorithm to dynamically filter and score resume bullets by relevance to selected profile

### Jekyll Site Structure

- **Collections**: `_portfolio` for case studies, `_posts` for blog articles
- **Custom layouts**: `portfolio-item.html` for portfolio pieces
- **Navigation**: Defined in `_config.yml` under `header_pages`
- **Theme**: Uses Minima theme with custom CSS overlays

## Common Development Commands

### Local Development

```bash
# Install dependencies (first time only)
gem install bundler jekyll
bundle install

# Run local development server
bundle exec jekyll serve
# Site available at http://localhost:4000

# Build site without serving
bundle exec jekyll build
```

### Resume Management

```bash
# View resume databank summary
python3 scripts/resume_manager.py summary

# List all experience entries with achievement counts
python3 scripts/resume_manager.py experience

# Search for keyword across entire resume
python3 scripts/resume_manager.py search "analytics"

# Generate markdown resume from databank
python3 scripts/generate_resume_markdown.py

# Generate full version with all projects
python3 scripts/generate_resume_markdown.py --full

# Convert markdown to PDF (requires pandoc)
pandoc output/MarkSchulz_Resume.md -o output/MarkSchulz_Resume.pdf -V geometry:margin=0.5in
```

### Python Virtual Environment

Python scripts should be run with Python 3. A venv exists at `.venv/` if needed:

```bash
source .venv/bin/activate  # Activate if needed
python3 scripts/resume_manager.py summary
```

## Data Update Workflow

When adding new achievements, skills, or projects:

1. **Update `data/resume.json` directly** - This is the single source of truth
2. **Increment `meta.version`** appropriately:
   - Major (X.0.0): New job or major career change
   - Minor (1.X.0): New project, significant achievement
   - Patch (1.0.X): Small corrections, typos
3. **Update `meta.last_updated`** to current date (YYYY-MM-DD)
4. **Verify changes**: Run `python3 scripts/resume_manager.py summary`
5. **Regenerate outputs**: Run markdown generator, update website pages as needed

Detailed workflow in `data/UPDATE_WORKFLOW.md`.

## Achievement Guidelines

When adding achievements to `data/resume.json`:

- **Quantify everything**: Include percentages, dollar amounts, time savings
- **Use action verbs**: Led, Managed, Developed, Optimized, Increased, etc.
- **Be specific**: Include technologies, methodologies, and measurable outcomes
- **Categorize consistently**: Use existing categories for achievements

Example:
```json
{
  "category": "AI Innovation & Enterprise Enablement",
  "items": [
    "Developed custom GPT framework processing 50K+ records daily, reducing reporting time by 75%"
  ]
}
```

## Resume Profiles System

The interactive resume uses a tag-based filtering system:

- **Profiles** defined in `data/resume_profiles.json`: Brand Management, Strategy & Innovation, CX & Engagement
- **Tags** applied to experience bullets in `resume.json` (e.g., "brand", "ai", "oncology", "analytics")
- **Filtering** happens client-side in `resume-interactive.html` using tag matching scores
- **Scoring**: Bullets are ranked by how many priority tags they match for the selected profile

## Important File Paths

- **Resume databank**: `data/resume.json`
- **Resume profiles**: `data/resume_profiles.json`
- **Jekyll config**: `_config.yml`
- **Homepage**: `index.md`
- **Interactive resume**: `resume-interactive.html`
- **About page**: `about.md`
- **Python scripts**: `scripts/`
- **Documentation**: `data/README.md`, `data/UPDATE_WORKFLOW.md`
- **Supporting docs**: `docs/` (performance reviews, source materials)
- **Generated output**: `output/`
- **Built site**: `_site/` (git-ignored)

## Testing Changes

Before committing:

1. Test Jekyll build: `bundle exec jekyll build` (should complete without errors)
2. Test local server: `bundle exec jekyll serve` and check http://localhost:4000
3. Verify resume manager: `python3 scripts/resume_manager.py summary`
4. Test markdown generation: `python3 scripts/generate_resume_markdown.py`
5. If changing JSON schemas, validate with `python3 scripts/validate_tags.py`

## Deployment

Site is configured for GitHub Pages:

- Deploys from `main` branch
- Build happens automatically on push
- Changes visible in 1-2 minutes at configured URL

When making content changes:
```bash
git add .
git commit -m "Update: [description]"
git push
```

## Content Guidelines

- **Portfolio items**: Create files in `_portfolio/` with frontmatter (title, client, industry, date, excerpt)
- **Blog posts**: Create files in `_posts/` with format `YYYY-MM-DD-title.md`
- **Resume updates**: Always edit `data/resume.json` first, then regenerate other formats
- **Skills**: Maintain consistent categorization in JSON (core_competencies, technical, marketing_specialized, leadership, methodologies)

## Specialized Knowledge

### Pharmaceutical Marketing Context

This resume/portfolio is optimized for pharmaceutical marketing roles with specific attention to:

- **Therapeutic areas**: Oncology, Cardiovascular, HIV, Men's Health (tracked in resume.json)
- **Regulatory**: MLR (Medical-Legal-Regulatory) review processes
- **Audiences**: HCP (Healthcare Professional) vs Patient marketing
- **Compliance**: FDA regulations and compliance considerations
- **Commercial perspectives**: Agency, Manufacturer, Publisher (three key industry viewpoints)

### ATS Optimization

Resume generation focuses on Applicant Tracking System compatibility:

- Keywords from `resume.json` keywords array
- Clean markdown formatting
- Skills sections formatted for parsing
- Quantified achievements with metrics
- Action verb usage throughout
