# Achievement Audit - Quick Start Guide

## What This Is

You have **38 achievements without source documents** that cannot be traced back to original resumes/reviews. These may contain inaccurate details (like "12 team members over 18 months" when it was actually agency-wide).

## What You Need to Do

### Step 1: Review Each Achievement
Open `ACHIEVEMENT_AUDIT.md` and review each of the 38 achievements.

For each one, ask yourself:
- ✅ **Is this factually accurate?** (dates, numbers, details correct)
- ✅ **Can I defend this in an interview?** (have concrete examples/stories)
- ✅ **Is this specific enough?** (not too generic/vague)

### Step 2: Mark Your Decision

For each achievement, replace `[KEEP / EDIT / DELETE]` with ONE of:

**KEEP** - Achievement is accurate as written
```markdown
**DECISION:** KEEP
```

**EDIT** - Achievement needs corrections
```markdown
**DECISION:** EDIT
**EDIT (if applicable):**
Led agency-wide Curiosity-Driven Innovation Initiative with 500+ participants over 12 months, generating 5 client-facing innovations and fostering culture of continuous learning
```

**DELETE** - Achievement is inaccurate or cannot be verified
```markdown
**DECISION:** DELETE
```

### Step 3: Apply Your Decisions

Once you've reviewed all 38 achievements, run:

```bash
cd /Users/markschulz/Documents/My_Documents/My\ Coding/markschulz
python3 scripts/apply_audit_decisions.py
```

This will:
- Create a backup of your current resume.json
- Apply all your KEEP/EDIT/DELETE decisions
- Show you a summary of changes

## Known Issues to Fix

### Achievement 27 (DEFINITELY NEEDS EDITING)
**Current text:** "Led Curiosity-Driven Innovation Initiative with 12 team members over 18 months..."

**Your concern:** It wasn't 12 team members, it was agency-wide with 500 people

**Suggested fix:** Update to reflect actual scope

## Tips for Editing

### Be Specific
❌ "Led innovation initiatives"
✅ "Led agency-wide Curiosity-Driven Innovation Initiative reaching 500+ employees"

### Use Real Numbers
❌ "Supported multiple oncology brands"
✅ "Supported 9 oncology brands across 6 clients"

### Add Brand Names When Relevant
❌ "Built CRM programming for client brand"
✅ "Built CRM programming for TAGRISSO DTC brand"

### Keep Achievement Structure
All achievements should follow this pattern:
- Action verb (Led, Built, Developed, Managed, etc.)
- What you did
- Impact/outcome (with metrics when possible)

## What Happens Next

After running the script:
1. Your resume.json will be updated with your decisions
2. A backup will be created (resume_backup_TIMESTAMP.json)
3. The custom resume generator will immediately reflect the changes
4. You can test by selecting different checkbox combinations

## Need Help?

If you're unsure about an achievement:
- **When in doubt, DELETE it** - Better to have fewer accurate bullets
- You can always add it back later if you verify the details
- Focus on achievements you can confidently discuss in interviews

---

**Remember:** This tool will be your LinkedIn showcase. Every achievement needs to be defensible and accurate. Quality > Quantity.
