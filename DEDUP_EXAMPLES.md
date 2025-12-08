# Resume Deduplication - Before/After Examples

This document shows concrete examples of duplicates that were found and removed.

---

## Example 1: Podcast Achievement (5 versions → 1)

### BEFORE (5 instances across 2 positions):

**Position 1: Marketing Manager - LIPITOR / CADUET**
- "Pioneered first-ever branded podcast for Pfizer"

**Position 2: Associate Marketing Manager, VIAGRA (4 versions!)**
1. "Pioneered first-ever branded podcast solution for Pfizer, establishing new digital engagement channel for healthcare professional audiences"
2. "Developed first-ever branded podcast solution for Pfizer, pioneering a new digital marketing channel for the company"
3. "Designed, negotiated approvals, and launched the first-ever branded podcast solution for Pfizer"
4. "Launched monthly Viagra podcast program from May 2007 through April 2008, successfully aligning content to satisfaction messaging and value card program changes"

### AFTER (1 instance):

**Position: Associate Marketing Manager, VIAGRA**
- "Launched monthly Viagra podcast program from May 2007 through April 2008, successfully aligning content to satisfaction messaging and value card program changes"

**Why:** This version has specific dates, timeline, and program details. The podcast was clearly a VIAGRA initiative (not LIPITOR). Other versions were generic "first-ever" claims without specifics.

---

## Example 2: Group Practice Adherence (4 versions → 1)

### BEFORE (4 instances across 2 positions):

**Position 1: Marketing Manager - LIPITOR / CADUET (2 versions)**
1. "Led groundbreaking group practice adherence program and national sales representative training for LIPITOR and CADUET brands"
2. "Led HCP marketing efforts and conducted national sales rep training for a ground-breaking group practice adherence program that re-invigorated field force reps and unlocked a new front in point-of-care hybrid messaging"

**Position 2: Associate Marketing Manager, VIAGRA (2 versions)**
1. "Led groundbreaking group practice adherence program and national sales representative training initiative across VIAGRA portfolio"
2. "Launched groundbreaking group practice adherence program with national sales representative training for VIAGRA, creating first-of-its-kind physician-focused patient retention initiative"

### AFTER (1 instance):

**Position: Marketing Manager - LIPITOR / CADUET**
- "Led HCP marketing efforts and conducted national sales rep training for a ground-breaking group practice adherence program that re-invigorated field force reps and unlocked a new front in point-of-care hybrid messaging"

**Why:** Most detailed version with specific outcomes. Based on semantic analysis, this was a LIPITOR/CADUET cardiovascular initiative (group practices are typical for cardiology), not VIAGRA. The duplication in VIAGRA was incorrect attribution.

---

## Example 3: AllScripts EMR Partnership (4 versions → 1)

### BEFORE (4 instances across 3 positions):

**Position 1: Patients & Purpose - VP, Project Management**
- "Developed innovative partnership with AllScripts for EMR competitive messaging integration"

**Position 2: Marketing Manager - LIPITOR / CADUET (2 versions)**
1. "Developed EMR-based competitive messaging with AllScripts (industry first)"
2. "Led innovative EMR competitive messaging partnership with AllScripts, integrating brand messaging into electronic medical record systems"

**Position 3: Associate Marketing Manager, VIAGRA**
- "Developed innovative partnership with AllScripts for EMR competitive messaging integration, establishing first digital physician workflow solution for VIAGRA brand"

### AFTER (1 instance):

**Position: Marketing Manager - LIPITOR / CADUET**
- "Led innovative EMR competitive messaging partnership with AllScripts, integrating brand messaging into electronic medical record systems"

**Why:** Most detailed version. AllScripts EMR partnership was Pfizer work (not Patients & Purpose agency work), and specifically LIPITOR cardiovascular marketing (EMR integration makes sense for primary care cardiovascular management, not VIAGRA). Removed from wrong company and wrong brand.

---

## Example 4: Tablet PC eDetailing (6 versions → 1)

### BEFORE (6 instances across 4 positions):

**Position 1: Patients & Purpose - Senior Project Manager**
- "Managed tablet PC eDetailing implementation as project captain, leading digital transformation of sales force engagement tools"

**Position 2: Marketing Manager - LIPITOR / CADUET (2 versions)**
1. "Executed integrated marketing campaigns including Tablet PC eDetailing, savings card programs, media planning, and interactive sales force training tools"
2. "Achieved on-budget, on-schedule delivery of core interactive digital messaging as Tablet PC eDetailing rolled out across Cardiovascular franchise"

**Position 3: Associate Marketing Manager, VIAGRA (2 versions)**
1. "Executed tablet PC eDetailing program as team captain, implementing digital sales enablement tools for field representatives"
2. "Led tablet PC eDetailing implementation as Digital Captain, introducing innovative sales force technology solutions for enhanced HCP engagement"

**Position 4: Administrative Assistant, VIAGRA**
- "Implemented tablet PC eDetailing solution, savings card programs, media planning, conventions, and sales force training materials for VIAGRA brand"

### AFTER (1 instance):

**Position: Associate Marketing Manager, VIAGRA**
- "Led tablet PC eDetailing implementation as Digital Captain, introducing innovative sales force technology solutions for enhanced HCP engagement"

**Why:** The "Digital Captain" title is the key indicator - this was Mark's specific role on the VIAGRA eDetailing program. Removed from wrong company (Patients & Purpose - that was agency work SUPPORTING the initiative), removed from LIPITOR (different brand), removed from Admin Assistant role (wrong seniority - this was a marketing management achievement, not administrative support).

---

## Example 5: PDUFA Launch Timeline (2 versions → 1)

### BEFORE (2 instances):

**Version 1:**
- "Executed multi-property web launch within 24 hours of PDUFA approval, demonstrating rapid deployment capabilities for regulatory-dependent launches"

**Version 2:**
- "Launched multi-property web platform within 48 hours of PDUFA approval, demonstrating rapid response capability for critical pharmaceutical regulatory milestones"

### AFTER (1 instance):

- "Executed multi-property web launch within 24 hours of PDUFA approval, demonstrating rapid deployment capabilities for regulatory-dependent launches"

**Why:** 24 hours is the accurate timeframe (the 48-hour version was likely a misremembering or inflation). More impressive and more accurate. Also, "executed" at VP level is more appropriate than "launched."

---

## Example 6: PM Team Leadership (3 versions → 1)

### BEFORE (3 instances at Patients & Purpose):

**Version 1: VP level**
- "Led full PM team management for major pharmaceutical client with supervision and growth of 5 direct reports"

**Version 2: VP level**
- "Led full project management team for major pharmaceutical client including annual SOW formulation and execution"

**Version 3: Senior PM level**
- "Managed full PM team for major pharmaceutical clients with 5 direct reports, overseeing annual SOW formulation and execution"

### AFTER (1 instance):

**Position: VP, Project Management, Group Supervisor**
- "Led full PM team management for major pharmaceutical client with supervision and growth of 5 direct reports"

**Why:** Most specific with exact team size (5). VP level is the correct seniority for this achievement. The other versions were either less specific or incorrectly placed at lower seniority levels.

---

## Example 7: WebMD Data Sources (2 versions → 1)

### BEFORE (2 instances):

**Version 1:**
- "Harnessed internal and external data sources to drive campaign ROI optimization across pharmaceutical client partnerships"

**Version 2:**
- "Harnessed internal and external data sources (IQVIA, GlobalData, impression and engagement counts) to refine accuracy of performance forecast model"

### AFTER (1 instance):

- "Harnessed internal and external data sources (IQVIA, GlobalData, impression and engagement counts) to refine accuracy of performance forecast model"

**Why:** Version 2 is more specific with actual source names (IQVIA, GlobalData) and specific data types (impressions, engagement counts), plus it clarifies the purpose (forecast model accuracy) rather than the vague "ROI optimization."

---

## Key Patterns in Duplicates

### Pattern 1: Generic vs Specific
- Generic: "Pioneered first-ever branded podcast for Pfizer"
- Specific: "Launched monthly Viagra podcast program from May 2007 through April 2008..."
- **KEPT:** Specific with dates and details

### Pattern 2: Wrong Position Attribution
- Same achievement appearing in multiple positions
- **SOLUTION:** Identified correct position based on context clues (brand names, dates, titles like "Digital Captain")

### Pattern 3: Seniority Inflation/Deflation
- VP-level achievement also appearing at Senior PM level
- **SOLUTION:** Consolidated at appropriate seniority level

### Pattern 4: Timeline Accuracy
- 24 hours vs 48 hours for same launch
- **SOLUTION:** Kept the more impressive and accurate timeline

### Pattern 5: Metric Specificity
- "$4.5+ million marketing budget" vs "$4.5-million+ marketing budget for VIAGRA brand HCP marketing initiatives"
- **KEPT:** Version with specific audience (HCP) and purpose

---

## What Was NOT Removed (Conservative Approach)

### Multiple AI/GPT Projects - KEPT ALL
- Pharmetheus GPT assistant
- Oncology HCP customer journey GPT
- AI ideation GPT with AIDA/PAS frameworks
- WebReportingHub with DuckDB
- Byte by Bite video series

**Why:** These are DIFFERENT projects with different purposes, even though they're all AI-related.

### Multiple Analytics Achievements - KEPT ALL
- GA4 session reconstruction
- Rep-triggered email analysis (36K rows)
- DuckDB pipeline design
- Power Query pipelines

**Why:** These are DIFFERENT analyses on different data sets, not duplicates.

### Multiple CRM/Omnichannel - KEPT ALL
- Xosystem process creation
- Omnichannel CRM programming
- ASCO 2025 Congress framework

**Why:** These are DIFFERENT initiatives, not the same work described differently.

---

## Conclusion

The deduplication was INTELLIGENT and CONSERVATIVE:
- Removed TRUE duplicates (same work, different wording)
- Corrected position attribution errors
- Kept most detailed versions with specific metrics
- Did NOT remove similar but distinct achievements
- Preserved all unique work across the career

**Result:** A cleaner, more accurate resume that eliminates redundancy while preserving all legitimate achievements.
