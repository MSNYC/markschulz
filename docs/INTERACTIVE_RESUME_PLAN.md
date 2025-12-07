# Interactive Resume Feature - Integration Plan

**Goal:** Add an interactive resume builder to the GitHub Pages website, allowing visitors to generate tailored versions of your resume for different focus areas (Brand Management, Strategy, CX & Engagement).

---

## Executive Summary

Your existing `cv-generator` repo is a sophisticated Streamlit app that uses:
- **YAML data bank** (experience, skills, roles, snippets)
- **Tag-based filtering** (bullets scored by priority_tags per role)
- **Jinja2 templates** for rendering
- **Python backend** with Streamlit UI

**For GitHub Pages** (static hosting, no Python backend), we'll create a **JavaScript-based client-side version** that:
1. Uses JSON data (converted from your YAML or synced with resume.json)
2. Implements the same tag-based filtering logic in JavaScript
3. Renders resumes dynamically in the browser
4. Allows PDF download via browser print or jsPDF library

---

## Architecture Overview

### Current cv-generator Flow
```
YAML Data → Python Selector → Jinja2 Template → Markdown → Pandoc → DOCX/PDF
   ↓              ↓                    ↓
experience.yml  filter by         resume_modern.md.j2
skills.yml      priority_tags
roles.yml       + score bullets
```

### Proposed GitHub Pages Flow
```
JSON Data → JavaScript Selector → Client-side Template → HTML → Print/PDF
   ↓              ↓                        ↓
resume.json   filter by              Handlebars.js or
              priority_tags           custom renderer
              + score bullets
```

---

## Data Strategy: Two Approaches

### Option A: Single Source of Truth (resume.json)
**Pros:**
- Only maintain one data file
- Already has comprehensive structure (v2.1.0)
- Consistent with current markschulz website

**Cons:**
- Need to map resume.json structure to cv-generator's tag-based filtering
- May need to add tags to resume.json bullets

**Implementation:**
1. Add `tags` field to each achievement item in resume.json
2. Define role profiles in a new `role_profiles.json`
3. JavaScript filter logic mimics cv-generator's selector.py

### Option B: Dual System (Keep Both, Sync Strategically)
**Pros:**
- Preserve cv-generator's proven YAML structure
- Can use cv-generator's Streamlit app for private/advanced use
- Website uses simplified JSON for public interactive feature

**Cons:**
- Maintain two systems
- Risk of data drift

**Implementation:**
1. Create sync script: `scripts/sync_to_website.py`
2. Converts cv-generator YAML → website JSON
3. Run manually or via git hook when updating data

---

## Recommended Approach: **Option B (Dual System with Sync Script)**

**Rationale:**
- cv-generator has rich YAML with many roles (manufacturer, agency, publisher perspectives)
- Website only needs 3-4 focus areas (simpler)
- Keep full cv-generator for personal use (job applications, tailoring)
- Website gets a curated, visitor-friendly subset

---

## Component Breakdown

### 1. Data Layer

#### Create: `/markschulz/data/resume_profiles.json`
```json
{
  "profiles": [
    {
      "id": "brand_management",
      "label": "Brand Management",
      "description": "Pharmaceutical brand strategy, launch excellence, and portfolio management",
      "priority_tags": ["strategy", "brand", "oncology", "launch", "portfolio", "leadership"],
      "headline": "Pharmaceutical Brand Leader | Oncology, Launch Excellence, Commercial Strategy",
      "focus_skills": ["Brand Strategy", "Portfolio Management", "Launch Excellence", "Oncology Marketing"]
    },
    {
      "id": "strategy_innovation",
      "label": "Strategy & Innovation",
      "description": "Digital transformation, AI/ML implementation, and strategic planning",
      "priority_tags": ["strategy", "ai", "innovation", "digital", "analytics", "transformation"],
      "headline": "Strategic Innovation Leader | AI/ML, Digital Transformation, Pharmaceutical Marketing",
      "focus_skills": ["AI/ML Strategy", "Digital Transformation", "Innovation Leadership", "Strategic Planning"]
    },
    {
      "id": "cx_engagement",
      "label": "Customer Experience & Engagement",
      "description": "Omnichannel engagement, experience planning, and journey optimization",
      "priority_tags": ["cx", "xp", "experience_planning", "omnichannel", "journey_mapping", "engagement"],
      "headline": "CX & Engagement Leader | Omnichannel Strategy, Experience Planning, Behavioral Design",
      "focus_skills": ["Experience Planning", "Omnichannel Marketing", "Customer Journey Mapping", "CRM Optimization"]
    }
  ]
}
```

#### Enhance: `/markschulz/data/resume.json` - Add Tags
Add `tags` array to each achievement item:
```json
{
  "category": "AI Innovation & Enterprise Enablement",
  "items": [
    {
      "text": "Led creation, testing, and deployment of multiple custom GPTs...",
      "tags": ["ai", "innovation", "digital", "leadership"]
    }
  ]
}
```

---

### 2. Sync Script (Optional but Recommended)

#### Create: `/markschulz/scripts/sync_cv_to_website.py`
```python
#!/usr/bin/env python3
"""
Sync cv-generator YAML data to markschulz website JSON
Extracts relevant bullets, maps tags, creates website-friendly structure
"""

import yaml
import json
from pathlib import Path

CV_REPO = Path.home() / "coding" / "cv-generator"
WEBSITE_REPO = Path.home() / "coding" / "markschulz"

def load_cv_data():
    """Load YAML from cv-generator"""
    with open(CV_REPO / "data" / "experience.yml") as f:
        experience = yaml.safe_load(f)
    with open(CV_REPO / "data" / "roles.yml") as f:
        roles = yaml.safe_load(f)
    with open(CV_REPO / "data" / "skills.yml") as f:
        skills = yaml.safe_load(f)
    return experience, roles, skills

def convert_to_website_json(experience, roles, skills):
    """Convert cv-generator structure to website JSON"""
    # Map roles to website profiles
    # Extract bullets with tags
    # Generate website-friendly structure
    pass

def main():
    experience, roles, skills = load_cv_data()
    website_data = convert_to_website_json(experience, roles, skills)

    output_path = WEBSITE_REPO / "data" / "resume_interactive.json"
    with open(output_path, 'w') as f:
        json.dump(website_data, f, indent=2)

    print(f"✓ Synced cv-generator data to {output_path}")

if __name__ == '__main__':
    main()
```

---

### 3. Frontend Components

#### A. Interactive Resume Page

Create: `/markschulz/resume-interactive.html`

**UI Layout:**
```
┌─────────────────────────────────────────────────┐
│  Interactive Resume Builder                      │
├─────────────────────────────────────────────────┤
│  Choose Your Focus:                              │
│  ○ Brand Management                              │
│  ○ Strategy & Innovation                         │
│  ○ Customer Experience & Engagement              │
│                                                   │
│  [Generate Resume]                               │
├─────────────────────────────────────────────────┤
│  Generated Resume Preview:                       │
│  ┌─────────────────────────────────────────┐   │
│  │  Mark Schulz                             │   │
│  │  CX & Engagement Leader | ...            │   │
│  │  ─────────────────────────────────────   │   │
│  │  Experience (selected)                   │   │
│  │  • Designed end-to-end omnichannel...    │   │
│  │  • Built WebReportingHub reducing...     │   │
│  └─────────────────────────────────────────┘   │
│                                                   │
│  [Download PDF] [Email to Me]                    │
└─────────────────────────────────────────────────┘
```

**Technology Stack:**
- **HTML/CSS**: Layout and styling (match dark mode theme)
- **JavaScript**: Filtering logic, rendering
- **Handlebars.js** or **Mustache.js**: Client-side templating
- **jsPDF** or **html2pdf.js**: PDF generation
- **Jekyll front matter**: Integrate with site navigation

---

#### B. JavaScript Logic

Create: `/markschulz/assets/js/resume-builder.js`

**Key Functions:**

```javascript
class ResumeBuilder {
  constructor(resumeData, profiles) {
    this.data = resumeData;
    this.profiles = profiles;
  }

  // Mimics cv-generator's selector.py logic
  filterExperienceByTags(priorityTags, maxBulletsPerRole = 5) {
    const filteredExperience = [];

    for (const exp of this.data.experience) {
      for (const position of exp.positions) {
        const scoredAchievements = [];

        // Score each achievement by tag matches
        for (const achievementGroup of position.achievements) {
          for (const item of achievementGroup.items) {
            const score = this.calculateScore(item.tags, priorityTags);
            scoredAchievements.push({ score, item, category: achievementGroup.category });
          }
        }

        // Sort by score, take top N
        scoredAchievements.sort((a, b) => b.score - a.score);
        const topAchievements = scoredAchievements.slice(0, maxBulletsPerRole);

        filteredExperience.push({
          company: exp.company,
          title: position.title,
          period: `${position.start_date} - ${position.end_date || 'Present'}`,
          achievements: topAchievements
        });
      }
    }

    return filteredExperience;
  }

  calculateScore(itemTags, priorityTags) {
    if (!itemTags) return 0;
    return itemTags.filter(tag => priorityTags.includes(tag)).length;
  }

  renderResume(profileId) {
    const profile = this.profiles.find(p => p.id === profileId);
    const filteredExp = this.filterExperienceByTags(profile.priority_tags);
    const focusSkills = this.getSkillsByTags(profile.priority_tags);

    return {
      headline: profile.headline,
      experience: filteredExp,
      skills: focusSkills,
      projects: this.getRelevantProjects(profile.priority_tags)
    };
  }

  getSkillsByTags(priorityTags) {
    // Extract skills matching priority tags
  }

  getRelevantProjects(priorityTags) {
    // Filter projects by keywords
    return this.data.projects.filter(project =>
      project.keywords.some(kw => priorityTags.includes(kw.toLowerCase()))
    );
  }
}
```

---

#### C. HTML Template

```html
<!-- resume-interactive.html -->
---
layout: default
title: Interactive Resume
---

<div class="resume-builder-container">
  <h1>Interactive Resume Builder</h1>
  <p class="subtitle">Tailor my resume to your focus area</p>

  <div class="profile-selector">
    <h2>Choose Your Focus:</h2>
    <div class="profile-options">
      <label class="profile-card">
        <input type="radio" name="profile" value="brand_management" checked>
        <div class="card-content">
          <h3>Brand Management</h3>
          <p>Pharmaceutical brand strategy, launch excellence, portfolio management</p>
        </div>
      </label>

      <label class="profile-card">
        <input type="radio" name="profile" value="strategy_innovation">
        <div class="card-content">
          <h3>Strategy & Innovation</h3>
          <p>Digital transformation, AI/ML implementation, strategic planning</p>
        </div>
      </label>

      <label class="profile-card">
        <input type="radio" name="profile" value="cx_engagement">
        <div class="card-content">
          <h3>Customer Experience & Engagement</h3>
          <p>Omnichannel engagement, experience planning, journey optimization</p>
        </div>
      </label>
    </div>

    <button id="generateBtn" class="generate-btn">Generate Resume</button>
  </div>

  <div id="resumePreview" class="resume-preview" style="display:none;">
    <h2>Generated Resume</h2>
    <div id="resumeContent" class="resume-content">
      <!-- Dynamically rendered content -->
    </div>
    <div class="actions">
      <button id="downloadPdfBtn" class="action-btn">Download PDF</button>
      <button id="emailBtn" class="action-btn">Email to Me</button>
      <button id="copyLinkBtn" class="action-btn">Copy Shareable Link</button>
    </div>
  </div>
</div>

<script src="{{ '/assets/js/resume-builder.js' | relative_url }}"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
```

---

### 4. Styling (Dark Mode Compatible)

Create: `/markschulz/assets/css/resume-builder.css`

```css
.resume-builder-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.profile-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.profile-card {
  cursor: pointer;
  transition: all 0.3s ease;
}

.profile-card input[type="radio"] {
  display: none;
}

.profile-card .card-content {
  background: var(--bg-secondary, #1a1f3a);
  border: 2px solid var(--border-color, #2a3050);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.profile-card input[type="radio"]:checked + .card-content {
  border-color: var(--accent-cyan, #00F0FF);
  box-shadow: var(--glow-cyan, 0 0 20px rgba(0, 240, 255, 0.3));
}

.profile-card:hover .card-content {
  transform: translateY(-4px);
  border-color: var(--accent-purple, #B794F6);
}

.resume-preview {
  margin-top: 3rem;
  padding: 2rem;
  background: var(--bg-secondary);
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.resume-content {
  background: white;
  color: #1a1a1a;
  padding: 3rem;
  border-radius: 8px;
  font-family: 'Georgia', serif;
  line-height: 1.6;
}

/* Print-friendly styles */
@media print {
  .profile-selector,
  .actions {
    display: none;
  }

  .resume-content {
    box-shadow: none;
    border: none;
  }
}
```

---

## Implementation Phases

### Phase 1: Data Preparation (Week 1)
**Tasks:**
1. ✅ Review cv-generator data structure
2. Add `tags` to resume.json achievements
3. Create resume_profiles.json with 3 focus areas
4. Test tag coverage (ensure all achievements have relevant tags)

**Deliverables:**
- `data/resume_profiles.json`
- Updated `data/resume.json` with tags
- Tag coverage report

---

### Phase 2: Core JavaScript Logic (Week 2)
**Tasks:**
1. Implement ResumeBuilder class (filtering logic)
2. Create unit tests for tag scoring
3. Build rendering pipeline (data → HTML)
4. Add Handlebars templates for resume sections

**Deliverables:**
- `assets/js/resume-builder.js`
- `assets/js/resume-templates.js`
- Test suite

---

### Phase 3: UI Development (Week 3)
**Tasks:**
1. Create resume-interactive.html page
2. Style profile selector cards (dark mode)
3. Build resume preview pane
4. Add smooth transitions/animations
5. Mobile responsive design

**Deliverables:**
- `resume-interactive.html`
- `assets/css/resume-builder.css`
- Mobile-tested UI

---

### Phase 4: PDF Generation & Actions (Week 4)
**Tasks:**
1. Integrate jsPDF or html2pdf.js
2. Implement "Download PDF" functionality
3. Add "Email to Me" (mailto link with pre-filled subject)
4. Create shareable URLs (e.g., ?profile=cx_engagement)
5. Add analytics tracking (which profiles are viewed most)

**Deliverables:**
- Working PDF download
- Email integration
- URL parameter handling
- Google Analytics events

---

### Phase 5: Polish & Launch (Week 5)
**Tasks:**
1. Cross-browser testing (Chrome, Firefox, Safari)
2. Accessibility audit (WCAG 2.1 AA)
3. Performance optimization (lazy load data)
4. SEO metadata for resume-interactive page
5. Add prominent link from homepage
6. Create help/FAQ section

**Deliverables:**
- Production-ready feature
- Documentation
- Homepage integration
- Launch announcement

---

## Advanced Features (Future Enhancements)

### 1. AI-Powered Customization
**Concept:** Let visitors paste a job description, AI suggests best profile + custom bullet ordering

**Implementation:**
- Add job description textarea
- Call OpenAI API (client-side or via Netlify/Vercel function)
- Parse JD for keywords
- Map to priority tags
- Re-score bullets dynamically

**Benefits:**
- Highly personalized resume for visitor's specific role
- Showcases your AI expertise
- Differentiates from static resumes

---

### 2. Comparison View
**Concept:** Show 2-3 profile versions side-by-side

**Implementation:**
- Multi-select profiles
- Render in columns
- Highlight differences (bullets that appear in one vs. another)

**Benefits:**
- Helps recruiters understand your versatility
- Shows breadth of experience

---

### 3. Skills Graph Visualization
**Concept:** D3.js or Chart.js radar chart showing skill depth per profile

**Implementation:**
- Calculate skill scores from filtered bullets
- Render interactive radar chart
- Compare profiles visually

**Benefits:**
- Visual differentiation
- Engaging, modern UX

---

### 4. Export to LinkedIn (Pre-filled)
**Concept:** "Update My LinkedIn" button that generates formatted text for each section

**Implementation:**
- Generate LinkedIn About section from profile
- Create Experience bullet points
- Copy to clipboard with formatting
- Instructions modal: "Paste this into LinkedIn > About"

**Benefits:**
- Helps visitors who want to recommend you
- Streamlines sharing

---

## Technical Considerations

### Performance
- **Data Loading:** Lazy load resume.json (only when visiting interactive page)
- **Rendering:** Use DocumentFragment for efficient DOM updates
- **PDF Generation:** Debounce/throttle to prevent multiple triggers

### SEO
- **Static Fallback:** Render default profile server-side (Jekyll build)
- **Meta Tags:** Unique title/description for each profile via URL params
- **Structured Data:** Add JSON-LD for ResumePosting schema

### Analytics
Track key metrics:
- Which profiles are most viewed?
- Download vs. email vs. copy link ratios
- Time spent on each profile
- Bounce rate from interactive page

### Accessibility
- Keyboard navigation for profile selection
- ARIA labels for dynamically rendered content
- High contrast mode support
- Screen reader testing

---

## Alternative: Embed Streamlit App

If you prefer to keep the full cv-generator Streamlit functionality:

**Option:** Deploy Streamlit app to Streamlit Cloud or Heroku, embed in iframe

**Pros:**
- No need to rewrite in JavaScript
- Keep all cv-generator features (AI analysis, job description upload)
- Faster to implement

**Cons:**
- Requires external hosting
- Slower load time (iframe + Python backend)
- Less integrated look/feel with website
- Privacy concerns (data leaves your site)

**Implementation:**
```html
<iframe
  src="https://your-app.streamlit.app"
  width="100%"
  height="1200px"
  style="border: none; border-radius: 12px;">
</iframe>
```

---

## Recommendation: Start with Phase 1-3

**Quickest Path to MVP:**
1. **Phase 1:** Add tags to resume.json + create profiles JSON (2-3 hours)
2. **Phase 2:** Build JavaScript filtering (4-6 hours)
3. **Phase 3:** Create basic UI (4-6 hours)

**Total Time to MVP:** ~12-15 hours

**Then iterate:**
- Add PDF download (Phase 4)
- Polish styling (Phase 5)
- Consider AI features (Advanced)

---

## Files to Create

### Data Files
- `/data/resume_profiles.json` - Focus area definitions
- `/data/resume.json` - Enhanced with tags (update existing)

### Scripts
- `/scripts/sync_cv_to_website.py` - Optional sync from cv-generator
- `/scripts/add_tags_to_resume.py` - Helper to bulk-add tags

### Frontend
- `/resume-interactive.html` - Main interactive page
- `/assets/js/resume-builder.js` - Core filtering logic
- `/assets/js/resume-templates.js` - Handlebars templates
- `/assets/css/resume-builder.css` - Styling

### Documentation
- `/docs/INTERACTIVE_RESUME_PLAN.md` - This file
- `/docs/TAG_SYSTEM.md` - Tag taxonomy and usage guide

---

## Success Metrics

**User Engagement:**
- \> 30% of visitors view interactive resume
- Average 3+ minutes on page
- \> 50% generate at least one profile

**Technical:**
- Page load < 2 seconds
- Zero JavaScript errors
- Mobile score > 90 (Lighthouse)

**Business:**
- Track recruiter feedback ("This is so useful!")
- Measure conversion: views → downloads → interview requests
- Compare with static resume download rates

---

## Questions to Answer Before Starting

1. **Data Source:** Single resume.json or sync from cv-generator?
   - **Recommendation:** Start with resume.json only, add sync later if needed

2. **Number of Profiles:** 3 (Brand, Strategy, CX) or more?
   - **Recommendation:** Start with 3, easy to add more

3. **PDF Quality:** Simple text-based or styled with brand colors?
   - **Recommendation:** Styled (use html2pdf with CSS)

4. **AI Features:** MVP or Phase 2?
   - **Recommendation:** Phase 2 (prove concept first)

5. **Analytics:** Google Analytics or custom?
   - **Recommendation:** Google Analytics (already have GA4?)

---

## Next Steps

**Immediate Actions:**
1. Review this plan and confirm approach
2. Decide: Pure JavaScript or iframe embed?
3. If JavaScript: Start tagging resume.json achievements
4. Create resume_profiles.json with 3 focus areas
5. Build proof-of-concept filtering logic

**Then:**
6. Build UI mockup in Figma/on paper
7. Implement Phase 1-3
8. Test with sample visitors (friends/colleagues)
9. Iterate based on feedback
10. Launch!

---

**Estimated Total Effort:** 20-30 hours for full MVP
**Estimated Timeline:** 3-4 weeks (part-time)
**Maintenance:** ~2 hours/month (update data, fix bugs)

Let me know which approach you prefer and I can start implementation immediately!
