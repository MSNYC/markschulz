# Resume Databank Update Workflow

This guide explains how to update your resume databank when you have new information from documents, performance reviews, project completions, etc.

## Quick Reference

```bash
# View current databank summary
python3 scripts/resume_manager.py summary

# List all experience
python3 scripts/resume_manager.py experience

# List all skills
python3 scripts/resume_manager.py skills

# Search for specific keyword
python3 scripts/resume_manager.py search "analytics"
```

## Workflow: Adding New Information

### Step 1: Receive New Document
When you have a new document (performance review, project summary, recommendation letter, etc.):

1. Save it to `/docs/` with clear naming:
   ```
   source_[company]_[type]_[date].[ext]
   ```
   Example: `source_biolumina_performance_review_2024-12.pdf`

### Step 2: Extract Information
With Claude or manually, extract:
- New achievements
- New skills
- New projects
- Quantifiable metrics
- Updated responsibilities
- Awards or recognition

### Step 3: Update JSON
Edit `/data/resume.json` to add extracted information:

**For new achievements:**
```json
// In the relevant position's achievements array
{
  "category": "Category Name",
  "items": [
    "New achievement with quantifiable impact"
  ]
}
```

**For new skills:**
```json
// In skills.technical or other appropriate section
"new_category": [
  "New Skill 1",
  "New Skill 2"
]
```

**For new projects:**
```json
{
  "name": "Project Name",
  "description": "Clear description",
  "role": "Your role",
  "technologies": ["Tech1", "Tech2"],
  "outcomes": [
    "Measurable outcome 1",
    "Measurable outcome 2"
  ]
}
```

### Step 4: Update Metadata
Always update these fields after making changes:
```json
{
  "meta": {
    "version": "1.1.0",  // Increment appropriately
    "last_updated": "2024-12-15",
    "notes": "Added Q4 2024 achievements"
  }
}
```

### Step 5: Validate
Run the summary to ensure it updated correctly:
```bash
python3 scripts/resume_manager.py summary
```

### Step 6: Generate Outputs
Update generated files:
- Website resume: `/about.md`
- PDF resume: Generate new version
- LinkedIn: Update profile sections
- Portfolio: Add new case studies

## Example: Adding Performance Review Achievements

### Source Document
You receive: `2024_annual_review.pdf` with these highlights:
- Led AI transformation initiative reaching 200+ employees
- Increased client satisfaction score from 8.2 to 9.1
- Managed $2M in client accounts with 95% retention

### Update Process

1. **Save document:**
   ```bash
   mv 2024_annual_review.pdf docs/source_biolumina_performance_review_2024-12.pdf
   ```

2. **Update JSON** in `experience[0].positions[0].achievements`:
   ```json
   {
     "category": "Leadership, Collaboration & Innovation Culture",
     "items": [
       "Led AI transformation initiative reaching 200+ employees, increasing AI literacy and adoption across agency",
       "Increased client satisfaction score from 8.2 to 9.1 through improved strategic planning and execution",
       "Managed $2M portfolio of client accounts with 95% retention rate"
     ]
   }
   ```

3. **Update skills** if needed:
   ```json
   "leadership": [
     "Change Management",  // If new
     "Client Satisfaction Management"  // If new
   ]
   ```

4. **Update metadata:**
   ```json
   {
     "meta": {
       "version": "1.1.0",
       "last_updated": "2024-12-15",
       "notes": "Added 2024 annual review achievements"
     }
   }
   ```

5. **Verify:**
   ```bash
   python3 scripts/resume_manager.py summary
   python3 scripts/resume_manager.py search "AI transformation"
   ```

## Version Numbering

Use semantic versioning:
- **Major** (X.0.0): New job, major career change
- **Minor** (1.X.0): New project, significant achievement, new skills
- **Patch** (1.0.X): Small corrections, wording updates

Examples:
- `1.0.0` → `2.0.0`: Started new position at different company
- `1.0.0` → `1.1.0`: Completed major project with achievements
- `1.0.0` → `1.0.1`: Fixed typo or updated phone number

## Best Practices

### Quantify Everything
❌ "Improved client satisfaction"
✅ "Increased client satisfaction score from 8.2 to 9.1 (11% improvement)"

### Use Action Verbs
- Led, Managed, Developed, Created, Designed
- Optimized, Increased, Reduced, Improved
- Pioneered, Launched, Established, Built

### Be Specific
❌ "Worked on analytics projects"
✅ "Developed Python-based analytics pipeline processing 50K+ records daily, reducing reporting time by 75%"

### Keep Categories Consistent
Use existing achievement categories when possible:
- AI Innovation & Enterprise Enablement
- Strategy & Marketing Expertise
- Data Engineering & Analytics Leadership
- Automation & Workflow Optimization
- Creative & Concept Development
- Technical Problem-Solving & Tool Development
- Leadership, Collaboration & Innovation Culture

### Regular Review Schedule
- **Weekly**: Add completed projects/tasks
- **Monthly**: Review and refine wording
- **Quarterly**: Major update with metrics
- **Annually**: Comprehensive review and restructuring if needed

## Backup Strategy

Before major updates:
```bash
# Create backup
cp data/resume.json data/backup/resume_$(date +%Y%m%d).json

# Or commit to git
git add data/resume.json
git commit -m "Update: [description of changes]"
git push
```

## AI-Assisted Extraction Prompt

When working with Claude to extract information from documents:

```
I have a new document to update my resume databank with.

Document: [paste or attach document]

Please extract:
1. New achievements (with quantifiable metrics)
2. New skills or technologies used
3. New projects completed
4. Any awards or recognition
5. Updated responsibilities

Format as JSON additions to my resume.json structure at:
/home/kryphion/coding/markschulz/data/resume.json

Focus on:
- Action verbs
- Quantifiable results
- Specific technologies/methodologies
- Business impact
```

## Generating Outputs from Databank

### Website Resume
```bash
# Use Python script to generate markdown from JSON
python3 scripts/generate_website_resume.py > about.md
```

### PDF Resume
```bash
# Generate LaTeX or use template
python3 scripts/generate_pdf_resume.py --template modern
```

### LinkedIn Profile
```bash
# Extract LinkedIn-optimized sections
python3 scripts/generate_linkedin.py
```

*(Scripts to be created as needed)*

---

**Remember:** The databank is your single source of truth. Update it first, then generate all other formats from it.
