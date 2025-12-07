# Resume Databank Enhancement Plan
## Based on Executive Resume Optimization Report

After reviewing `/docs/resume_optimization.md`, several critical enhancements are needed to align the databank with 2024-2025 pharma executive resume best practices.

## Executive Summary

**Good News:** Our JSON databank approach is ideal for the recommended strategy!

The report emphasizes:
- ✅ Master resume + tailored versions (our databank does this!)
- ✅ Three format versions needed (can generate from databank)
- ✅ Consistency across platforms (single source ensures this)
- ❌ JSON Resume format for submission (NOT what we're doing - we generate Word/PDF)

**Our Use Case:** Internal JSON databank → Generate traditional Word/PDF formats
**Their Warning:** Don't submit JSON to ATS (we won't!)

## Critical Additions Needed

### 1. **Pharma-Specific Keywords Taxonomy**

**Current:** Generic `keywords[]` array
**Needed:** Structured pharma keyword categories

```json
"pharma_keywords": {
  "leadership": [
    "Strategic Planning",
    "Brand Strategy",
    "Portfolio Management",
    "Commercial Strategy",
    "P&L Management",
    "Digital Transformation"
  ],
  "marketing": [
    "HCP (Healthcare Professional) Marketing",
    "DTC (Direct-to-Consumer) Marketing",
    "KOL (Key Opinion Leader) Engagement",
    "Patient Journey Mapping",
    "Omnichannel Marketing",
    "Formulary Strategy"
  ],
  "regulatory_compliance": [
    "FDA Regulations",
    "OPDP Guidelines",
    "MLR (Medical-Legal-Regulatory) Review",
    "Fair Balance",
    "GMP/GCP Compliance",
    "HIPAA",
    "Sunshine Act Compliance"
  ],
  "commercial_analytics": [
    "Veeva CRM",
    "IQVIA Data",
    "Symphony Health",
    "Market Access",
    "HEOR Integration",
    "Marketing Mix Modeling",
    "Sales Force Effectiveness"
  ],
  "therapeutic_areas": [
    "Oncology",
    "Immunology",
    "HIV",
    "Cardiovascular",
    "Neurology",
    "Rare Disease"
  ]
}
```

### 2. **Resume Version Configurations**

**Purpose:** Define rules for generating 3 required versions

```json
"resume_versions": {
  "ats_optimized": {
    "purpose": "Online job portals, company career sites",
    "format": "docx",
    "rules": {
      "layout": "single_column",
      "fonts": ["Calibri", "Arial", "Georgia"],
      "font_size": "10-12pt",
      "avoid": ["tables", "text_boxes", "graphics", "columns", "headers_footers"],
      "emphasis": "keywords",
      "section_headers": "standard"
    },
    "length": "2-3 pages",
    "priority": "ATS parsing"
  },
  "formatted_professional": {
    "purpose": "Direct recruiter contact, networking, interviews",
    "format": "pdf",
    "rules": {
      "layout": "single_column_with_design",
      "design_elements": ["bold", "color_headings", "white_space", "callout_boxes"],
      "maintain_ats_readability": true
    },
    "length": "2-3 pages",
    "priority": "Human impression + ATS compatibility"
  },
  "linkedin_profile": {
    "purpose": "Always-on digital presence, recruiter searches",
    "format": "linkedin",
    "rules": {
      "headline": "include_industry_keywords",
      "activity": "thought_leadership",
      "consistency": "match_resume_facts"
    },
    "priority": "Searchability + executive presence"
  }
}
```

### 3. **Therapeutic Area Expertise Section**

**Current:** Mentioned in projects/experience
**Needed:** Dedicated section for prominence

```json
"therapeutic_areas": [
  {
    "area": "Oncology",
    "years_experience": 4,
    "brands": ["Brand A", "Brand B"],
    "expertise_level": "Expert",
    "key_achievements": [
      "Led 9 oncology accounts across 6 clients"
    ]
  },
  {
    "area": "HIV",
    "years_experience": 1,
    "brands": ["Leading HIV treatment"],
    "expertise_level": "Proficient",
    "key_achievements": [
      "Led mini-campaign launch for leading HIV treatment"
    ]
  },
  {
    "area": "Cardiovascular",
    "years_experience": 4,
    "brands": ["LIPITOR", "CADUET"],
    "expertise_level": "Expert",
    "key_achievements": [
      "Managed $10M+ LIPITOR/CADUET marketing budget",
      "Led brand through LOE transition"
    ]
  }
]
```

### 4. **Regulatory & Compliance Experience**

**Critical:** Every pharma resume must address this

```json
"regulatory_compliance": {
  "fda_regulations": {
    "experience": true,
    "details": "21+ CFR Part 202, OPDP enforcement, promotional material compliance"
  },
  "mlr_review": {
    "experience": true,
    "role": "Review Committee Marketing Captain",
    "details": "Led MLR review process for LIPITOR campaign materials"
  },
  "opdp_guidelines": {
    "experience": true,
    "details": "OPDP guideline compliance for HCP and DTC marketing"
  },
  "fair_balance": {
    "experience": true,
    "details": "Fair balance requirements in promotional materials across print and digital"
  },
  "sunshine_act": {
    "experience": true,
    "details": "Compliance with Sunshine Act reporting for KOL relationships"
  },
  "cross_functional": {
    "medical_affairs": true,
    "regulatory": true,
    "r_and_d": false,
    "market_access": true
  }
}
```

### 5. **Tailoring Templates**

**Purpose:** Store common customization patterns

```json
"tailoring_templates": {
  "vp_brand_management": {
    "title_variations": [
      "VP, Brand Management",
      "VP, Marketing",
      "Vice President, Commercial Strategy"
    ],
    "emphasize_skills": ["Brand Strategy", "P&L Management", "Team Leadership"],
    "emphasize_experience": ["exp_005"],
    "keywords_priority": ["leadership", "marketing", "commercial_analytics"]
  },
  "director_digital_marketing": {
    "title_variations": [
      "Director, Digital Marketing",
      "Director, Omnichannel Marketing",
      "Digital Strategy Director"
    ],
    "emphasize_skills": ["Digital Transformation", "Omnichannel Marketing", "AI/ML"],
    "emphasize_experience": ["exp_001", "exp_004"],
    "keywords_priority": ["marketing", "commercial_analytics"]
  },
  "experience_planning_lead": {
    "title_variations": [
      "VP, Experience Planning",
      "Experience Strategy Lead",
      "Customer Experience Director"
    ],
    "emphasize_skills": ["Experience Planning", "Customer Journey", "Segmentation"],
    "emphasize_experience": ["exp_001"],
    "keywords_priority": ["marketing", "therapeutic_areas"]
  }
}
```

### 6. **Metrics & Quantification Tracking**

**Purpose:** Ensure all achievements have numbers

```json
"metrics_bank": {
  "budgets_managed": [
    {"amount": "10M+", "context": "LIPITOR/CADUET HCP marketing", "years": "2008-2012"},
    {"amount": "30M+", "context": "WebMD strategic deals annually", "years": "2016-2019"},
    {"amount": "2M", "context": "Client portfolio at Biolumina", "years": "2021-present"}
  ],
  "team_sizes": [
    {"size": 4, "roles": "2 Sr PMs, 1 PM, 1 Assoc PM, 1 BC", "company": "Patients & Purpose"},
    {"size": 4, "roles": "3 Assoc Directors, 1 Analyst", "company": "WebMD"}
  ],
  "accounts_brands": [
    {"count": 9, "type": "oncology accounts", "context": "across 6 clients", "company": "Biolumina"},
    {"count": 30, "type": "strategic deals annually", "value": "30M+", "company": "WebMD"}
  ],
  "improvements": [
    {"metric": "client satisfaction", "from": 8.2, "to": 9.1, "change": "+11%"},
    {"metric": "retention rate", "value": "95%", "context": "$2M client portfolio"}
  ]
}
```

### 7. **ATS Compatibility Flags**

**Purpose:** Mark content by ATS safety

```json
"ats_metadata": {
  "safe_for_ats": {
    "formatting": ["bold", "italics", "standard_bullets", "color_in_headings"],
    "avoid": ["tables", "columns", "text_boxes", "graphics", "header_footer_contact"]
  },
  "section_headers_standard": [
    "Professional Experience",
    "Education",
    "Skills",
    "Certifications"
  ],
  "section_headers_alternative": [
    "Work History",
    "Career Highlights",
    "Core Competencies"
  ],
  "date_format": "MM/YYYY",
  "contact_placement": "top_of_page_body"
}
```

### 8. **Executive Search Firm Tracking**

**Purpose:** Track relationships and submissions

```json
"executive_search": {
  "tier_1_firms": [
    {"name": "Spencer Stuart", "contact": "", "status": "researching"},
    {"name": "Russell Reynolds", "contact": "", "status": "no_contact"},
    {"name": "Heidrick & Struggles", "contact": "", "status": "no_contact"}
  ],
  "pharma_specialist_firms": [
    {"name": "Klein Hersh", "contact": "", "specialty": "CMO and VP Marketing"},
    {"name": "Kaye/Bassman", "contact": "", "specialty": "40+ years pharma/biotech"},
    {"name": "Smith Hanley Associates", "contact": "", "specialty": "BioPharma commercial"},
    {"name": "JRG Partners", "contact": "", "specialty": "Pharma executive VP/Director/C-suite"}
  ],
  "submissions": []
}
```

## Implementation Priority

### Phase 1: Critical (Do Now)
1. ✅ Add pharma keywords taxonomy
2. ✅ Add regulatory/compliance section
3. ✅ Add therapeutic areas section
4. ✅ Add resume version configurations

### Phase 2: Important (This Week)
5. ⬜ Add tailoring templates
6. ⬜ Add metrics bank
7. ⬜ Create Word/PDF generators

### Phase 3: Ongoing
8. ⬜ Track executive search firms
9. ⬜ Build tailored resume variants
10. ⬜ Monitor ATS compatibility

## Generation Scripts Needed

Based on the report, we need scripts to generate:

1. **`generate_ats_docx.py`** - ATS-optimized Word document
2. **`generate_formatted_pdf.py`** - Professional PDF with design
3. **`generate_linkedin_profile.py`** - LinkedIn profile sections
4. **`tailor_for_job.py`** - Customize for specific job posting

## Key Principles from Report

✅ **DO:**
- Maintain master databank (our JSON)
- Generate 2-3 page resumes
- Include both acronyms and full terms
- Quantify every achievement
- Maintain consistency across platforms
- Use natural language (not keyword stuffing)
- Keep authentic voice

❌ **DON'T:**
- Submit JSON to ATS (generate Word/PDF instead!)
- Use tables, columns, text boxes, graphics
- Put contact info in headers/footers
- Use AI to write entire resume
- Make it sound robotic
- Fabricate metrics

---

**Next Step:** Should I implement Phase 1 enhancements to your resume.json now?
