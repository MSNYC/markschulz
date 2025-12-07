# Position Reference Guide

Quick reference for `--exp-id` and position details when running extraction.

## Experience IDs and Positions

### exp_001 - Biolumina (Omnicom)
**Status:** ✅ Has 50+ tagged achievements - **SKIP EXTRACTION**

- **VP, Experience Planner** (2021-01 to Present)
  - Already has comprehensive achievement data

---

### exp_002 - Harrison & Star (Omnicom)
**Status:** ⚠️ Empty achievements - **EXTRACT IF MATERIAL AVAILABLE**

- **VP, Group Account Supervisor** (2020-01 to 2021-01)
  - Command:
    ```bash
    python data/extract_and_load.py your_document.pdf \
      --company "Harrison & Star" \
      --company-parent "Omnicom" \
      --title "VP, Group Account Supervisor" \
      --start-date 2020-01 \
      --end-date 2021-01 \
      --exp-id exp_002
    ```

---

### exp_003 - WebMD/Medscape (Internet Brands)
**Status:** ❌ Empty achievements - **HIGH PRIORITY**

#### Position 1: Team Leader, Sr. Dir., Commercial Clinical Strategy
- **Period:** 2018-01 to 2019-12
- **Why priority:** $30M+ strategic deals, ROI modeling, team leadership
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "WebMD/Medscape" \
    --company-parent "Internet Brands" \
    --title "Team Leader, Sr. Dir., Commercial Clinical Strategy" \
    --start-date 2018-01 \
    --end-date 2019-12 \
    --exp-id exp_003
  ```

#### Position 2: Director, Commercial Clinical Strategy
- **Period:** 2016-01 to 2018-01
- **Why priority:** IQVIA impact analysis, partnership development
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "WebMD/Medscape" \
    --company-parent "Internet Brands" \
    --title "Director, Commercial Clinical Strategy" \
    --start-date 2016-01 \
    --end-date 2018-01 \
    --exp-id exp_003
  ```

---

### exp_004 - Patients & Purpose (Omnicom)
**Status:** ❌ Empty achievements - **MEDIUM PRIORITY**

#### Position 1: VP, Project Management, Group Supervisor
- **Period:** 2015-01 to 2016-12
- **Why priority:** Team leadership, $1M+ SOWs, department culture
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "Patients & Purpose" \
    --company-parent "Omnicom" \
    --title "VP, Project Management, Group Supervisor" \
    --start-date 2015-01 \
    --end-date 2016-12 \
    --exp-id exp_004
  ```

#### Position 2: Project Management, Group Supervisor
- **Period:** 2014-01 to 2015-01
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "Patients & Purpose" \
    --company-parent "Omnicom" \
    --title "Project Management, Group Supervisor" \
    --start-date 2014-01 \
    --end-date 2015-01 \
    --exp-id exp_004
  ```

#### Position 3: Senior Project Manager
- **Period:** 2012-01 to 2014-01
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "Patients & Purpose" \
    --company-parent "Omnicom" \
    --title "Senior Project Manager" \
    --start-date 2012-01 \
    --end-date 2014-01 \
    --exp-id exp_004
  ```

---

### exp_005 - Pfizer
**Status:** ⚠️ LIPITOR has 4 untagged achievements - **HIGH PRIORITY**

#### Position 1: Marketing Manager - LIPITOR / CADUET
- **Period:** 2008-01 to 2012-01
- **Why priority:** $10M budget, industry-first innovations, LOE strategy
- **Current state:** Has 4 achievements but NO TAGS
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "Pfizer" \
    --title "Marketing Manager - LIPITOR / CADUET" \
    --start-date 2008-01 \
    --end-date 2012-01 \
    --exp-id exp_005
  ```

#### Position 2: Associate Marketing Manager, VIAGRA
- **Period:** 2004-01 to 2008-01
- **Command:**
  ```bash
  python data/extract_and_load.py your_document.pdf \
    --company "Pfizer" \
    --title "Associate Marketing Manager, VIAGRA" \
    --start-date 2004-01 \
    --end-date 2008-01 \
    --exp-id exp_005
  ```

#### Position 3: Administrative Assistant, VIAGRA
- **Period:** 1998-01 to 2004-01
- **Note:** Lower priority - admin role with limited strategic scope

---

## Extraction Priority Recommendations

### 🔴 HIGH PRIORITY (Do First)
1. **exp_003** - WebMD Sr. Dir. (2018-2019)
   - Rich analytics, ROI modeling, strategic deals
2. **exp_003** - WebMD Director (2016-2018)
   - Impact analysis, partnerships
3. **exp_005** - Pfizer LIPITOR (2008-2012)
   - Brand management, budget, innovation

### 🟡 MEDIUM PRIORITY (Do Second)
4. **exp_004** - P&P VP (2015-2016)
   - Team leadership, project management
5. **exp_004** - P&P Group Supervisor (2014-2015)
6. **exp_005** - Pfizer VIAGRA Assoc Mgr (2004-2008)

### ⚪ LOWER PRIORITY (Optional)
7. **exp_002** - Harrison & Star (2020-2021) - Only 1 year
8. **exp_004** - P&P Sr PM (2012-2014)
9. **exp_005** - Pfizer Admin (1998-2004) - Admin role

---

## Quick Checklist

Track your extraction progress:

- [ ] exp_003: WebMD Sr. Dir. (2018-2019)
- [ ] exp_003: WebMD Director (2016-2018)
- [ ] exp_005: Pfizer LIPITOR (2008-2012)
- [ ] exp_004: P&P VP (2015-2016)
- [ ] exp_004: P&P Group Supervisor (2014-2015)
- [ ] exp_005: Pfizer VIAGRA (2004-2008)
- [ ] exp_002: Harrison & Star (2020-2021)
- [ ] exp_004: P&P Sr PM (2012-2014)

After each extraction, run: `python data/verify_achievements.py`
