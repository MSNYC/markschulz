# Achievement Extraction Instructions

## Purpose
Extract specific, quantified achievements from old resumes, performance reviews, and notes to enrich the resume data for tag-based filtering.

## Workflow

### Step 1: Prepare Source Materials
Gather for each position:
- Old resume versions
- Performance reviews
- Self-assessments
- Project summaries
- Any notes about accomplishments

### Step 2: LLM Extraction (Use in Separate Chat)

**Prompt Template:**
```
I need you to extract specific achievements from the attached resume/review for the following position:

Company: [Company Name]
Title: [Job Title]
Period: [Start Date] - [End Date]
Experience ID: [exp_XXX from resume.json]

Use the schema from achievement_extraction_schema.json.

For each achievement you extract:
1. Make it SPECIFIC - include metrics, outcomes, or concrete deliverables
2. Focus on ACCOMPLISHMENTS not responsibilities
3. Apply 2-6 relevant tags from the tag_taxonomy
4. Rate your confidence (high/medium/low) based on clarity in source

Output format: JSON following the achievement_extraction_schema.json structure
Filename: achievements_{company}_{start_year}.json

[Paste or attach source material here]
```

### Step 3: Review Extracted Data
Check each extracted file for:
- ✅ Specific metrics or outcomes (not vague statements)
- ✅ Appropriate tags that match taxonomy
- ✅ No duplicates across files
- ✅ Valid JSON format

### Step 4: Load into resume.json
Use the provided loader script:
```bash
python data/load_achievements.py data/achievements_webmd_2018.json
```

## Tag Strategy by Profile

### Brand Management Profile
Priority tags: `brand`, `portfolio`, `launch`, `positioning`, `budget_management`, `oncology`, `cardio`, `hcp`

### Strategic Planning Profile
Priority tags: `strategy`, `analytics`, `data_engineering`, `roi_modeling`, `innovation`, `ai`, `automation`, `digital`

### CX & Omnichannel Profile
Priority tags: `cx`, `xp`, `journey_mapping`, `omnichannel`, `experience_planning`, `patient`, `hcp`, `crm`

**Best achievements have tags from multiple profiles** - this enables smart filtering!

## Priority Roles to Extract

### High Priority (Most Differentiable)
1. **WebMD/Medscape (2018-2019)** - Team Leader, Sr. Dir., Commercial Clinical Strategy
   - You managed ~30 strategic deals worth $30M+
   - Focus: ROI modeling, IQVIA analysis, partnership structures, team leadership

2. **WebMD/Medscape (2016-2018)** - Director, Commercial Clinical Strategy
   - Focus: Impact analysis, media strategy, partnership development

3. **Pfizer LIPITOR/CADUET (2008-2012)** - Marketing Manager
   - Already have 4 achievements but need tags
   - Focus: $10M budget management, digital innovation (podcast, EMR messaging), LOE strategy, launch

### Medium Priority
4. **Patients & Purpose (2015-2016)** - VP, Project Management
   - Managed teams, $1M+ SOWs
   - Focus: Team leadership, budget management, digital evangelism, process improvement

5. **Patients & Purpose (2014-2015)** - PM Group Supervisor
   - Focus: New business onboarding, digital enablement, team development

### Lower Priority (Less Differentiable)
6. **Pfizer VIAGRA (2004-2008)** - Associate Marketing Manager
7. **Patients & Purpose (2012-2014)** - Senior PM

### Skip
- Administrative Assistant roles (limited strategic impact)

## Quality Examples

### ❌ BAD (Too Generic)
```json
{
  "text": "Managed strategic deals",
  "tags": ["strategy"]
}
```

### ✅ GOOD (Specific, Measurable)
```json
{
  "text": "Designed tiered ROI projection model for pharmaceutical partnerships that standardized evaluation of 60+ annual opportunities, reducing deal assessment time from 3 days to 4 hours while improving forecast accuracy by 28%",
  "tags": ["strategy", "analytics", "roi_modeling", "automation", "partnership"],
  "metric_type": "time_saved",
  "source_confidence": "high"
}
```

## Common Extraction Patterns

### From Performance Reviews
Look for:
- "Exceeded goal by X%"
- "Led initiative that resulted in..."
- "Recognized for..."
- Specific projects with outcomes

### From Old Resumes
Look for:
- Bullet points with numbers/percentages
- "First to..." or "Pioneered..."
- "Reduced/Increased [metric] by X%"
- Team size, budget size, # of accounts

### From Self-Assessments
Look for:
- Project accomplishments with business impact
- Process improvements
- Innovation initiatives
- Team development examples

## Validation Checklist

Before saving each extraction file:
- [ ] Every achievement is SPECIFIC (has metrics, deliverables, or concrete outcomes)
- [ ] Tags match the tag_taxonomy in schema
- [ ] No achievement is just a rephrased responsibility
- [ ] Company/title/dates match resume.json
- [ ] experience_id matches resume.json
- [ ] Valid JSON (test with `python -m json.tool filename.json`)
- [ ] Filename follows pattern: `achievements_{company}_{start_year}.json`

## After Loading

Run this command to see updated resume with new achievements:
```bash
python data/verify_achievements.py
```

This will show:
- Total achievements per role
- Tag coverage per profile
- Potential differentiation opportunities
