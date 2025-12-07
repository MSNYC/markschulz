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

## Future Enhancements

- [ ] Python script to validate JSON schema
- [ ] Script to generate markdown resume from JSON
- [ ] Script to generate LaTeX/PDF resume
- [ ] LinkedIn profile generator
- [ ] Cover letter template system
- [ ] ATS keyword optimizer
- [ ] Diff tool to compare versions over time
- [ ] Extraction pipeline for performance reviews

## File Naming Conventions

When adding supporting documents to `/docs/`:
- `resume_[version]_[date].pdf` - Generated resumes
- `source_[company]_[type]_[date].[ext]` - Source documents
- `achievements_[project]_[date].md` - Project notes

Example: `source_biolumina_performance_review_2024-06.pdf`
