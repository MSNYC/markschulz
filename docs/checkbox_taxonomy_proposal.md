# Interactive Resume Checkbox Taxonomy Proposal

## Analysis Summary

Based on analysis of `resume.json`, you have:
- **46 unique tags**
- **1,056 total tag occurrences**
- Strong concentration in brand/strategy, innovation/digital, and HCP marketing

## Proposed Checkbox Structure

### Design Principles
1. **Meaningful differentiation**: Each checkbox should filter for distinctly different experiences
2. **Balanced granularity**: 15-20 checkboxes total (not too few, not overwhelming)
3. **Frequency-weighted**: Prioritize tags with 10+ occurrences
4. **User intent-focused**: Group by what hiring managers actually search for

---

## Recommended Checkbox Categories (18 total)

### **Therapeutic Expertise** (3 checkboxes)
- ☐ **Oncology** (10 occurrences) - Cancer therapeutics and hematology
- ☐ **Cardiovascular** (28 occurrences as "cardio") - Heart disease and vascular conditions
- ☐ **HIV / Rare Disease** (2 HIV, other rare disease experience) - Specialty therapeutic areas

**Rationale**: Therapeutic area is often the #1 filter for pharma roles. These are your strongest areas.

---

### **Core Marketing Functions** (5 checkboxes)
- ☐ **Brand Strategy & Management** (78 occurrences) - Brand positioning, planning, strategy development
- ☐ **Product Launch Excellence** (22 occurrences) - Pre-launch planning, launch execution, uptake acceleration
- ☐ **Portfolio Management** (10 occurrences) - Multi-brand coordination, resource allocation, lifecycle management
- ☐ **Omnichannel Marketing** (10 occurrences) - Multi-channel orchestration, journey design, CX planning
- ☐ **Commercial Strategy** (60 occurrences as "strategy") - Go-to-market planning, commercial planning, competitive positioning

**Rationale**: Core job functions that directly map to job titles and responsibilities.

---

### **Audience & Stakeholder Marketing** (2 checkboxes)
- ☐ **HCP Marketing** (83 occurrences) - Healthcare professional targeting, KOL engagement, medical communications
- ☐ **Patient & Caregiver Marketing** (17 occurrences) - DTC, patient services, adherence programs

**Rationale**: Distinct audience types requiring different approaches, compliance considerations, and channel strategies.

---

### **Innovation & Technology** (4 checkboxes)
- ☐ **AI/ML & Automation** (12 AI + 17 automation = 29 combined) - Artificial intelligence, machine learning, process automation, GPT development
- ☐ **Digital Transformation** (76 occurrences) - Digital strategy, channel innovation, modern marketing techniques
- ☐ **Data & Analytics** (50 analytics + 21 data engineering = 71 combined) - Insights generation, data platforms, predictive modeling, business intelligence
- ☐ **Marketing Technology (MarTech)** (innovation tag: 76 occurrences) - Platform implementation, CRM, marketing automation, tech stack optimization

**Rationale**: Hot areas for pharma innovation. Combining AI+automation makes sense as they're often linked. Data+analytics is a natural pairing.

---

### **Leadership & Operations** (4 checkboxes)
- ☐ **Team Leadership & Development** (66 leadership + 24 team_management = 90 combined) - People management, mentoring, organizational development
- ☐ **Cross-Functional Collaboration** (project_management: 65 occurrences) - Matrix management, stakeholder alignment, agency partnership
- ☐ **Budget & Resource Management** (48 occurrences) - Financial planning, ROI optimization, resource allocation
- ☐ **Process & Performance Optimization** (35 process_improvement + 22 roi_modeling = 57 combined) - Workflow efficiency, performance measurement, continuous improvement

**Rationale**: Senior roles often require demonstrating operational excellence and leadership, not just marketing execution.

---

## Alternative: Condensed Version (15 checkboxes)

If 18 feels like too many, here's a streamlined version:

### **Therapeutic Expertise** (2)
- ☐ Oncology
- ☐ Cardiovascular

### **Core Marketing** (4)
- ☐ Brand Strategy & Management
- ☐ Product Launch
- ☐ Omnichannel & Customer Experience
- ☐ HCP Marketing

### **Innovation & Tech** (3)
- ☐ AI/ML & Automation
- ☐ Digital Transformation
- ☐ Analytics & Data Engineering

### **Leadership** (3)
- ☐ Team Leadership
- ☐ Cross-Functional Collaboration
- ☐ Budget & Operations Management

### **Specialized** (3)
- ☐ Compliance & Regulatory (MLR)
- ☐ Media Strategy & Planning
- ☐ Sales Enablement & Training

---

## Implementation Notes

### Minimum/Maximum Selection Rules
- **Minimum**: 1 checkbox (at least some filtering)
- **Maximum**: 8 checkboxes (prevents "select all" behavior)
- **Recommended**: 3-5 checkboxes (optimal specificity)

### Scoring Algorithm
Same as current profiles:
1. Count tag matches for each bullet
2. Higher score = higher relevance
3. Show top N bullets per role based on score

### User Experience Flow
```
Step 1: Choose Your Path
  ( ) Quick Select: Pick a pre-built profile
      → Brand Management
      → Strategic Planning & Positioning
      → CX & Omnichannel Innovation

  ( ) Custom Select: Build your own focus
      → [Shows checkbox grid]

Step 2: Generate Resume
  [Preview, Download, Email options]
```

---

## Questions for Decision

1. **18 checkboxes or 15 checkboxes?** (I recommend 18 for better differentiation)

2. **Should "Compliance/MLR/Regulatory" be one checkbox or split?**
   - Combined: 36 occurrences (compliance + mlr + regulatory)
   - Useful for quality/compliance-focused roles

3. **Include "Sales Enablement" and "Training"?**
   - Combined: 52 occurrences
   - Relevant for commercial operations roles

4. **Separate "Analytics" from "Data Engineering"?**
   - Analytics (50): More business/insights
   - Data Engineering (21): More technical/platform
   - Could split for technical vs. business analytics roles

5. **Should we add any low-frequency but strategically important tags?**
   - Example: "Journey Mapping" only has 1 occurrence but is important for CX roles
   - Could combine with omnichannel

---

## Next Steps

1. **Decide on final checkbox list** (18 vs 15, which specific labels)
2. **Update `resume_profiles.json`** to add checkbox metadata
3. **Build UI** for two-step wizard (Quick vs Custom)
4. **Update filtering logic** to handle checkbox arrays instead of profile IDs
5. **Test with real data** to ensure quality differentiation

---

## Tag Coverage Analysis

**Tags with 10+ occurrences captured in 18-checkbox proposal:**
- ✅ hcp (83)
- ✅ brand (78)
- ✅ innovation (76)
- ✅ digital (76)
- ✅ leadership (66)
- ✅ project_management (65)
- ✅ strategy (60)
- ✅ analytics (50)
- ✅ budget_management (48)
- ✅ process_improvement (35)
- ✅ cardio (28)
- ⚠️  sales_enablement (27) - Could add as "Sales Enablement"
- ✅ training (25) - Combined with sales enablement
- ✅ team_management (24)
- ⚠️  media (24) - Could add as "Media Strategy"
- ⚠️  partnership (23) - Could fold into "Cross-Functional Collaboration"
- ✅ launch (22)
- ✅ roi_modeling (22)
- ✅ data_engineering (21)
- ⚠️  positioning (20) - Covered by "Brand Strategy"
- ⚠️  timeline_management (20) - Covered by "Project Management"
- ✅ automation (17)
- ✅ patient (17)
- ✅ ai (12)
- ✅ compliance (12)
- ✅ mlr (12)
- ✅ regulatory (12)
- ✅ oncology (10)
- ✅ omnichannel (10)
- ✅ portfolio (10)

**Coverage: 30 of 30 tags with 10+ occurrences represented** ✅
