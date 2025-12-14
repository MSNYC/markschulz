# Quick Select Resumes - NOW WITH COMPLETE CAREER HISTORY

**Generated:** 2025-12-12
**Status:** ✅ FIXED - All 13 positions now included
**Issue Resolved:** Missing Pfizer brand management positions

---

## What Was Wrong

The previous Quick Select resumes were **missing 8 positions**, including:

❌ **All 3 Pfizer brand management roles** (the most critical ones for Brand Management resume!)
❌ **All 3 Patients & Purpose PM roles** (relevant project/launch experience)
❌ **2 Pfizer early-career positions** (showing career progression)

This meant the Brand Management resume didn't even show your LIPITOR, CADUET, or VIAGRA marketing manager experience - the exact roles that define that profile!

---

## What's Fixed Now

✅ **ALL 13 positions are now included in every Quick Select resume**
✅ **Bullet counts vary by relevance** (smart filtering, not position filtering)
✅ **Complete career timeline** from 1998 to Present

---

## How It Works Now

### Relevance-Based Bullet Filtering

Instead of hiding entire positions, the script now:

1. **Includes every position** (13 total across all companies)
2. **Scores each position's achievements** based on how many profile tags they match
3. **Shows more bullets for highly relevant positions**, fewer for less relevant ones

**Bullet Count Logic:**
- **High relevance** (3+ tag matches): Up to **5 bullets**
- **Medium relevance** (1-2 tag matches): Up to **3 bullets**
- **Low/no relevance** (0 tag matches): **1 bullet minimum**

This ensures complete career history while emphasizing the most relevant experience.

---

## Brand Management Resume - Example

Here's how the bullet counts work out for Brand Management:

| Position | Bullets | Why |
|----------|---------|-----|
| **Marketing Manager, LIPITOR/CADUET** | **5** | Core brand role, $10M+ budget, CV franchise |
| **Assoc. MM, VIAGRA/REVATIO** | **5** | Brand management, $4.5M+ budget, HCP marketing |
| **Admin Assistant, VIAGRA/REVATIO** | **5** | Brand support across 4 major brands, $500K+ budgets |
| **VP, Experience Planner** (Biolumina) | **5** | Current role, brand planning for 9 oncology brands |
| **VP, PM, Group Supervisor** (P&P) | **5** | Managed LUCENTIS, TECFIDERA, BANZEL brand launches |
| **Team Leader, Commercial Strategy** (WebMD) | **3** | Strategic oversight, $30M portfolio, ROI modeling |
| **Director, Marketing Strategy** (WebMD) | **3** | Brand opportunity analysis, performance-guarantee deals |
| **Senior PM** (P&P) | **3** | Multi-client PM leadership, SOW management |
| **PM, Group Supervisor** (P&P) | **3** | Team leadership, financial management |
| **VP, Group Account Supervisor** (H&S) | **2** | Campaign oversight, cross-departmental alignment |
| **Sr. Dir., Data Strategy** (WebMD) | **2** | Ops/data focus, less brand-centric |
| **Assoc. MM, CADUET** | **1** | Brief role (1 year), less documented |
| **Temp Admin Assistant** | **1** | Early career, foundational experience |

---

## Strategic Planning Resume - Example

Different positions get emphasis based on strategy/analytics tags:

| Position | Bullets | Why |
|----------|---------|-----|
| **Team Leader, Commercial Strategy** (WebMD) | **5** | ROI modeling, IQVIA Rx analysis, strategic deals |
| **Director, Marketing Strategy** (WebMD) | **5** | Strategic frameworks, performance modeling |
| **Sr. Dir., Data Strategy** (WebMD) | **3** | Sprint management, pricing strategy |
| **Marketing Manager, LIPITOR/CADUET** | **3** | Budget management, strategic planning aspects |
| Etc. | Varies | Based on strategy tag matches |

---

## CX Innovation Resume - Example

CX/omnichannel/AI positions get the most bullets:

| Position | Bullets | Why |
|----------|---------|-----|
| **VP, Experience Planner** (Biolumina) | **5** | CX planning, omnichannel, AI/GPT development |
| **VP, PM, Group Supervisor** (P&P) | **5** | Digital launches, patient/caregiver experiences |
| Others | Varies | Based on CX/digital/innovation tags |

---

## Files Regenerated

All 3 Quick Select resumes now have complete career history:

1. **`resume/brand-management.md`** - 13 positions, 47 total bullets
2. **`resume/strategic-planning.md`** - 13 positions, varying bullets
3. **`resume/cx-innovation.md`** - 13 positions, varying bullets

---

## Verification

You can verify this by checking any of the files:

```bash
# Count positions in brand management resume
grep "^  - title:" resume/brand-management.md | wc -l
# Should show: 13

# List all positions
grep "^  - title:" resume/brand-management.md | sed 's/  - title: //'
```

**Expected output:**
```
VP, Experience Planner
VP, Group Account Supervisor
Senior Director, Data Strategy & Operations
Team Leader, Sr. Dir., Commercial Clinical Strategy
Director, Marketing Strategy & Analytics
VP, Project Management, Group Supervisor
Project Management, Group Supervisor
Senior Project Manager
Marketing Manager, LIPITOR / CADUET          ← NOW PRESENT!
Associate Marketing Manager, CADUET           ← NOW PRESENT!
Associate Marketing Manager, VIAGRA / REVATIO ← NOW PRESENT!
Administrative Assistant, VIAGRA / REVATIO    ← NOW PRESENT!
Temporary Administrative Assistant            ← NOW PRESENT!
```

---

## Next Steps

1. **Test locally:**
   ```bash
   bundle exec jekyll serve
   ```

2. **Visit each resume:**
   - http://localhost:4000/resume/brand-management/
   - http://localhost:4000/resume/strategic-planning/
   - http://localhost:4000/resume/cx-innovation/

3. **Verify:**
   - [ ] All 13 positions appear in each resume
   - [ ] Most relevant positions have more bullets
   - [ ] Less relevant positions still appear (minimum 1 bullet)
   - [ ] Career timeline is complete (1998 → Present)
   - [ ] Pfizer brand management roles are prominently featured

4. **If satisfied, commit:**
   ```bash
   git add resume/brand-management.md resume/strategic-planning.md resume/cx-innovation.md
   git commit -m "Fix Quick Select resumes to show complete career history

   - Include ALL 13 positions (previously missing 8)
   - Add missing Pfizer brand management roles (LIPITOR, CADUET, VIAGRA)
   - Add missing Patients & Purpose PM roles
   - Implement relevance-based bullet filtering (5/3/1 bullets)
   - Maintain complete career timeline from 1998 to Present

   Positions now emphasized by relevance, not filtered out entirely."
   git push
   ```

---

## Technical Details

**Script:** `scripts/regenerate_quick_select_complete.py`

**Key Change:** Instead of filtering positions based on tag matches, the script now:
- Includes **every position** from `resume.json`
- Filters **bullets within each position** based on relevance
- Ensures **minimum 1 bullet** per position (so nothing is hidden)
- Shows **up to 5 bullets** for highly relevant positions

This gives you the best of both worlds:
- ✅ Complete career history (nothing hidden)
- ✅ Focused on most relevant experience (smart bullet selection)
- ✅ Reasonable length (not overwhelming with every detail)

---

**Issue resolved!** Your complete career history is now represented across all three Quick Select resumes.
