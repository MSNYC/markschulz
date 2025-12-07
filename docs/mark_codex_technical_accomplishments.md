# Mark Schulz – Applied Technical Accomplishments (Codex, Analytics, AI-Assisted Coding)

*Draft document capturing your technical work in a way that accurately reflects your role: not a software developer, but a strategist and applied technologist who uses AI, structured thinking, and analytical skills to guide and collaborate on technical solutions.*

---

## Positioning Statement
You are **not** a traditional software engineer. Your value lies in:
- Knowing *what* to build
- Structuring and communicating problems clearly
- Designing analytics workflows and data pipelines conceptually
- Using Codex, Claude Code, and ChatGPT to generate or modify code
- Debugging logically with AI assistance
- Managing repositories, folder structures, and documentation
- Combining data strategy, UX sensibility, and AI tooling
- Translating business needs into technical tasks
- Collaborating effectively with engineering resources

This document reflects your contributions as an **AI-assisted technologist**, **analytics architect**, and **technical collaborator**, *not* as a developer.

---

# 1. Analytics Engineering & Pipeline Architecture

### **GA4 → DuckDB Multi-Brand Analytics Pipeline**
- Guided the end-to-end design of a reusable DuckDB pipeline replacing one-off Excel scripts.
- Structured ETL flow across loaders for traffic, downloads, sources, pages, devices, and engagement.
- Directed the move toward timestamped output directories and consistent reporting folders.
- Collaborated with AI coding tools to:
  - Stabilize loader logic across inconsistent Excel schemas
  - Normalize header drift using YAML configs
  - Standardize CLIs for brand analyses
- Improved chart labeling, quarter boundaries, legend consistency, and output formatting.

### **Brand Workspaces & Environment Routing**
- Designed a multi-brand folder architecture (brands/<brand>/).
- Improved reliability by using brand-scoped YAML configs and environment variables.
- Collaborated with AI tools to fix multi-row header detection, date coercion, and audience normalization.

---

# 2. Repository Structure, Documentation, and Workflow Hygiene

### **Repo Organization & Technical Hygiene**
- Rebuilt repository layouts using industry-standard Python packaging patterns.
- Ensured clean separation between:
  - src/ modules
  - data/raw vs data/processed
  - credentials/
  - configs/
  - scripts/ and CLI utilities
  - docs/ and templates/
- Added .gitignore patterns that prevent data leakage and keep repos clean.
- Established placeholder scaffolding (.gitkeep) for empty folders.
- Produced clear documentation and README updates for future maintainers.

### **Product Overview Documentation**
- Authored a comprehensive PRODUCT_OVERVIEW.md outlining:
  - Architecture
  - Tooling
  - Risks
  - Roadmap
  - Operational model
  - Team responsibilities

---

# 3. AI-Assisted Coding & Problem-Solving

### **Using Codex/ChatGPT/Claude Code to Accelerate Technical Work**
Your strengths:
- Translating business or analytics needs into clear instructions AI coding tools can act on.
- Reviewing, editing, and debugging AI-generated code with logical thinking.
- Making decisions about architecture, naming, and workflow design.
- Understanding enough Python, pandas, DuckDB, Streamlit, and YAML to evaluate output.

Examples:
- Directed Codex to generate Python modules for analytics migration.
- Collaborated with AI to fix legend mismatches, date parsing, trailing-label issues.
- Guided header-normalization logic across multiple Excel loader types.
- Co-created CLI tools for running brand analyses.
- Used AI to refactor Streamlit UI components for channel-weighting visualizers.

---

# 4. UX/UI Oversight & Applied Front-End Logic

### **Streamlit App – HCP Channel Visualization Tool**
- Worked with AI tools to:
  - Rebuild UI state logic
  - Improve preset handling
  - Add manual channel weighting
  - Adjust layout, export options, and tab ordering
  - Tune Plotly/HSL color schemes for clarity
- Ensured the visualization accurately reflected active/inactive states.

### **ThroughLine UX & Interface Polish**
- Collaborated with AI to implement:
  - Task dialog redesigns
  - Dark-theme consistency
  - Flex layout improvements
  - Sorting logic fixes
  - Hover overlay corrections
  - Help/bug dialog copy refinements

---

# 5. ETL Debugging & Schema Stabilization

Examples from your Codex transcript:
- Diagnosed TEVIMBRA traffic loader failures due to audience/header drift.
- Uncovered extra tables embedded in Excel sheets causing date pollution.
- Repaired pages/downloads metadata stripping.
- Directed creation of defensive Excel ingestion logic.
- Built validation approaches using DuckDB for cross-brand reconciliation.

---

# 6. High-Level Technical Skills Demonstrated

### **Technical Strategy & Architecture**
- Pipeline design
- Multi-brand configuration systems
- Documentation architecture
- Workflow standardization

### **AI-Assisted Development**
- Prompt engineering for coding tasks
- Code review and iterative refinement
- Debugging with AI

### **Analytics Engineering**
- Data normalization
- Date/audience mapping
- Chart and reporting consistency rules
- Schema reconciliation

### **Tools & Technologies**
- Python (pandas, DuckDB, CLI utilities)
- Streamlit (UI logic, state management)
- Plotly (visualizations)
- YAML (schema configs)
- Git (repo hygiene, branching, tagging)
- Quarto (docs/reporting)
- Excel schema debugging

---

# 7. How This Translates Professionally (Non-Developer Positioning)
You can confidently claim:
- **Technical collaborator using AI tools**
- **Analytics workflow architect**
- **Data-driven problem solver**
- **AI-assisted coder (not traditional coder)**
- **Technical communicator and documentarian**
- **Product thinker with cross-functional understanding**

And you can truthfully state:
> "I work with AI coding tools to build analytics workflows, design pipelines, and solve data problems — but I am not a traditional software engineer. My strength is in structuring problems and guiding AI toward high-quality code solutions."

---

*Let me know when you're ready, and I can add:*
- résumé-optimized bullet points
- an executive summary
- a portfolio-ready project list
- a ‘skills without overclaiming’ version
- or edits to tune tone and positioning.

