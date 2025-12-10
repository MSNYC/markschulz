---
layout: home
title: Mark Schulz - Pharma Marketing & Advertising Professional | Interactive Resume
description: Interactive resume showcasing 20+ years in pharmaceutical marketing across oncology, AI integration, brand strategy, and omnichannel engagement. Filter by role to see relevant experience.
keywords: pharmaceutical marketing, oncology brand management, AI integration pharma, patient marketing, HCP marketing, omnichannel strategy, brand launch, customer experience pharma
---

<link rel="stylesheet" href="{{ '/assets/css/resume-builder.css' | relative_url }}">

<style>

/* ===== CENTER THE TITLE ===== */
.home h1 {
  text-align: center;
}

/* ===== HIDE DEFAULT THEME HEADER ===== */
.site-header {
  display: none !important;
}

/* ===== STICKY NAVIGATION ===== */
.sticky-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(10, 14, 39, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 240, 255, 0.2);
  padding: 1rem 0;
  margin-bottom: 2rem;
}

.sticky-nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1rem;
  gap: 1rem;
}

.sticky-nav nav {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  flex: 1;
}

.sticky-nav a {
  color: var(--text-secondary, #A0A0C0);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: color 0.3s ease;
  padding: 0.5rem 1rem;
  border-radius: 6px;
}

.sticky-nav a:hover {
  color: #00F0FF;
  background: rgba(0, 240, 255, 0.1);
}

.sticky-nav .linkedin-icon {
  display: flex;
  align-items: center;
  padding: 0.5rem;
  color: #00F0FF;
  font-size: 1.5rem;
  transition: all 0.3s ease;
  border-radius: 6px;
}

.sticky-nav .linkedin-icon:hover {
  background: rgba(0, 240, 255, 0.15);
  transform: scale(1.1);
}

html {
  scroll-behavior: smooth;
}

@media (max-width: 768px) {
  .sticky-nav nav {
    gap: 0.5rem;
  }
  .sticky-nav a {
    font-size: 0.85rem;
    padding: 0.4rem 0.8rem;
  }
  .sticky-nav .linkedin-icon {
    font-size: 1.3rem;
    padding: 0.4rem;
  }
}

/* ===== HERO SECTION ===== */
.hero-section {
  text-align: left;
  padding: 3rem 1.5rem;
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.05), rgba(183, 148, 246, 0.05));
  border-radius: 16px;
  margin-bottom: 4rem;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.hero-title {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, #00F0FF, #B794F6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1.3;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: var(--text-secondary, #A0A0C0);
  margin-bottom: 1.5rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
}

.hero-hook {
  font-size: 1rem;
  color: #ff6b6b;
  font-style: italic;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

/* ===== INTERACTIVE TOOL SECTION ===== */
#interactive-tool {
  margin: 4rem 0;
  scroll-margin-top: 80px;
}

.tool-intro {
  text-align: left;
  margin-bottom: 3rem;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.tool-intro h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #00F0FF;
}

.tool-intro p {
  font-size: 1.1rem;
  color: var(--text-secondary);
  max-width: 1200px;
}

.export-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.export-btn {
  padding: 0.8rem 1.5rem;
  border: 2px solid #00F0FF;
  background: rgba(0, 240, 255, 0.1);
  color: #00F0FF;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.export-btn:hover {
  background: #00F0FF;
  color: #0A0E27;
  transform: translateY(-2px);
}

.export-btn .icon {
  font-size: 1.2rem;
}

/* ===== BEHIND THE TOOL SECTION ===== */
#behind-the-tool {
  margin: 6rem auto;
  padding: 3rem 2rem;
  background: rgba(26, 31, 58, 0.3);
  border-radius: 12px;
  border-left: 4px solid #B794F6;
  scroll-margin-top: 80px;
  max-width: 1200px;
}

#behind-the-tool h2 {
  font-size: 2rem;
  color: #B794F6;
  margin-bottom: 1.5rem;
}

#behind-the-tool p {
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--text-secondary, #A0A0C0);
  margin-bottom: 1.5rem;
  max-width: 1200px;
}

#behind-the-tool ul {
  list-style: none;
  padding: 0;
  margin: 1.5rem 0;
}

#behind-the-tool li {
  padding-left: 1.5rem;
  margin-bottom: 0.75rem;
  position: relative;
  color: var(--text-secondary);
}

#behind-the-tool li:before {
  content: "→";
  position: absolute;
  left: 0;
  color: #B794F6;
  font-weight: bold;
}

/* ===== ABOUT ME SECTION ===== */
#about {
  margin: 6rem 0;
  scroll-margin-top: 80px;
}

#about h2 {
  font-size: 2rem;
  color: #00F0FF;
  margin-bottom: 1.5rem;
  text-align: left;
}

.about-content {
  max-width: 1200px;
  margin: 0 auto;
  text-align: left;
}

.about-content p {
  font-size: 1.05rem;
  line-height: 1.8;
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
}

/* ===== CONTACT SECTION ===== */
#contact {
  margin: 6rem 0;
  padding: 3rem 2rem;
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.05), rgba(183, 148, 246, 0.05));
  border-radius: 16px;
  scroll-margin-top: 80px;
}

#contact h2 {
  font-size: 2rem;
  color: #00F0FF;
  margin-bottom: 1rem;
  text-align: left;
}

.contact-intro {
  text-align: center;
  max-width: 600px;
  margin: 0 auto 3rem;
  color: var(--text-secondary);
}

.contact-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 900px;
  margin: 0 auto;
}

.contact-card {
  background: rgba(26, 31, 58, 0.5);
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid rgba(42, 48, 80, 0.8);
  text-align: center;
}

.contact-card h3 {
  color: #00F0FF;
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.contact-card p {
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.contact-btn {
  display: inline-block;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #00F0FF, #B794F6);
  color: #0A0E27;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 700;
  transition: all 0.3s ease;
}

.contact-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 240, 255, 0.4);
}

.contact-form {
  background: rgba(26, 31, 58, 0.5);
  padding: 2rem;
  border-radius: 12px;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #00F0FF;
  font-weight: 600;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  background: rgba(10, 14, 39, 0.5);
  border: 1px solid rgba(42, 48, 80, 0.8);
  border-radius: 6px;
  color: #fff;
  font-family: inherit;
  font-size: 1rem;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #00F0FF;
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #00F0FF, #B794F6);
  color: #0A0E27;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 240, 255, 0.4);
}

/* ===== CONTINUE BUTTONS HOVER ===== */
a[href^="#"]:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 240, 255, 0.3);
}

/* ===== RESPONSIVE ===== */
@media (max-width: 768px) {
  .hero-title {
    font-size: 1.8rem;
  }
  .hero-subtitle {
    font-size: 1rem;
  }
  #behind-the-tool,
  #contact {
    padding: 2rem 1rem;
  }
  .contact-options {
    grid-template-columns: 1fr;
  }
}

/* ===== PRINT STYLES ===== */
@media print {
  body {
    background: white;
    color: black;
  }
  .hero-section,
  #behind-the-tool,
  #about,
  #contact,
  .export-buttons,
  .profile-selector,
  .resume-actions,
  nav,
  footer {
    display: none !important;
  }
  #resumePreview {
    display: block !important;
  }
  .resume-content {
    color: black;
  }
}
</style>

<!-- STICKY NAVIGATION -->
<div class="sticky-nav">
  <div class="sticky-nav-inner">
    <nav>
      <a href="#top">Home</a>
      <a href="#interactive-tool">Get Resume</a>
      <a href="#behind-the-tool">Why This?</a>
      <a href="#about">Working With Me</a>
      <a href="#contact">Let's Talk</a>
    </nav>
    <a href="https://linkedin.com/in/mschulz" target="_blank" rel="noopener" class="linkedin-icon" aria-label="Connect on LinkedIn">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
      </svg>
    </a>
  </div>
</div>

<!-- HERO SECTION -->
<div class="hero-section">
  <h1 class="hero-title">Want to skip the <br>"does this candidate fit?"<br> guesswork?</h1>

  <p class="hero-subtitle">
    Instead of reading a one-size-fits-all resume, get a personalized view of my 20+ year pharma marketing career filtered by what matters to <em>your</em> role.
  </p>

  <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(0, 240, 255, 0.05); border-left: 3px solid #00F0FF; border-radius: 8px;">
    <p style="font-size: 1rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.6;">
      <strong style="color: #00F0FF;">Here's how this works:</strong>
    </p>
    <ol style="color: var(--text-secondary); line-height: 1.8; margin-left: 1.5rem; font-size: 0.95rem;">
      <li><strong>Choose your path:</strong> Pick a pre-built resume (Brand Management, Strategic Planning, or CX Innovation) or build a custom version by selecting focus areas that match your role</li>
      <li><strong>Get a tailored resume:</strong> See only the experience, skills, and achievements relevant to what you're hiring for</li>
      <li><strong>Learn more (optional):</strong> Read about my approach, working style, and what drives me</li>
      <li><strong>Connect:</strong> Reach out via LinkedIn or the contact form if there's a fit</li>
    </ol>
  </div>

  <!-- START HERE BUTTON -->
  <div style="text-align: center; margin-top: 3rem;">
    <a href="#interactive-tool" style="display: inline-block; padding: 1.2rem 2.5rem; background: linear-gradient(135deg, #00F0FF, #B794F6); color: #0A0E27; text-decoration: none; border-radius: 12px; font-weight: 700; font-size: 1.1rem; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0, 240, 255, 0.3);">
      <span style="display: block; margin-bottom: 0.3rem;">START HERE</span>
      <span style="font-size: 1.5rem; display: block;">↓</span>
    </a>
  </div>
</div>

<!-- INTERACTIVE RESUME TOOL -->
<section id="interactive-tool">
  <div class="tool-intro">
    <p style="font-size: 0.9rem; color: #00F0FF; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Step 1: Get Your Tailored Resume</p>
    <h2 style="text-align: left;">Choose Your Focus Areas</h2>
    <p>Pick a pre-built profile optimized for a specific role, or build a custom resume by selecting the therapeutic areas, skills, and audiences that matter to your position. Either way, you'll see only the experience relevant to you.</p>
  </div>

  <div class="resume-builder-container">
    <!-- Selection Method -->
    <div class="selection-method">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 0.5rem;">First: Choose Your Method</h3>
      <p class="step-description"><strong>Quick Select:</strong> Pick from 3 pre-built resumes optimized for specific roles (Brand Management, Strategic Planning, or Customer Experience).<br><strong>Custom Select:</strong> Build your own by choosing 1-3 focus areas (therapeutic areas, audiences, skills) that match your needs.</p>

      <div class="method-selector">
        <label class="method-card active" data-method="quick">
          <input type="radio" name="method" value="quick" checked>
          <div class="method-content">
            <div class="method-icon">⚡</div>
            <h4>Quick Select</h4>
            <p>Choose from 3 pre-built professional profiles</p>
          </div>
        </label>

        <label class="method-card" data-method="custom">
          <input type="radio" name="method" value="custom">
          <div class="method-content">
            <div class="method-icon">🎨</div>
            <h4>Custom Select</h4>
            <p>Build your own using checkboxes (1-3 selections)</p>
          </div>
        </label>
      </div>
    </div>

    <!-- Quick Select (Profiles) -->
    <div id="quickSelectPanel" class="profile-selector">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 0.5rem;">Then: Select a Pre-Built Profile</h3>
      <p class="step-description">Click any card below to view that tailored resume on a new page</p>

      <div class="profile-options">
        <a href="/resume/brand-management/" class="profile-card">
          <div class="card-content">
            <div class="card-icon">💊</div>
            <h4>Brand Management</h4>
            <p>Brand strategy, portfolio management, launch excellence, and HCP/patient marketing</p>
            <div class="card-tags">
              <span class="tag">Brand Strategy</span>
              <span class="tag">Oncology</span>
              <span class="tag">Launch</span>
              <span class="tag">Portfolio</span>
            </div>
          </div>
        </a>

        <a href="/resume/strategic-planning/" class="profile-card">
          <div class="card-content">
            <div class="card-icon">📋</div>
            <h4>Strategic Planning & Positioning</h4>
            <p>Commercial strategy, messaging & positioning, go-to-market planning, and market analysis</p>
            <div class="card-tags">
              <span class="tag">Strategy</span>
              <span class="tag">Positioning</span>
              <span class="tag">Planning</span>
              <span class="tag">Analytics</span>
            </div>
          </div>
        </a>

        <a href="/resume/cx-innovation/" class="profile-card">
          <div class="card-content">
            <div class="card-icon">🚀</div>
            <h4>Customer Experience (CX) & Omnichannel Innovation</h4>
            <p>Omnichannel strategy, experience design, AI implementation, and innovative engagement</p>
            <div class="card-tags">
              <span class="tag">CX</span>
              <span class="tag">Omnichannel</span>
              <span class="tag">AI</span>
              <span class="tag">Innovation</span>
            </div>
          </div>
        </a>
      </div>
    </div>

    <!-- Custom Select (Checkboxes) -->
    <div id="customSelectPanel" class="checkbox-selector" style="display:none;">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 0.5rem;">Then: Choose Your Focus Areas</h3>
      <p class="step-description">Select 1-3 areas that match what you're looking for, then click "Generate Custom Resume" to see the tailored results below. (Selecting too many areas produces less focused results.) <span id="selectionCount">(0 selected)</span></p>

      <div id="checkboxCategories" class="checkbox-categories">
        <!-- Dynamically populated from resume_profiles.json -->
      </div>

      <button id="generateCustomBtn" class="generate-btn" disabled>
        <span class="btn-text">Generate Custom Resume</span>
        <span class="btn-icon">→</span>
      </button>
    </div>

  </div>

  <!-- CONTINUE BUTTON -->
  <div style="text-align: center; margin-top: 3rem;">
    <a href="#behind-the-tool" style="display: inline-block; padding: 1rem 2rem; background: rgba(183, 148, 246, 0.15); border: 2px solid #B794F6; color: #B794F6; text-decoration: none; border-radius: 10px; font-weight: 600; transition: all 0.3s ease;">
      <span style="display: block;">Curious how I approach problem-solving?</span>
      <span style="font-size: 1.3rem; display: block; margin-top: 0.3rem;">↓</span>
    </a>
  </div>
</section>

<!-- BEHIND THE TOOL SECTION -->
<section id="behind-the-tool">
  <p style="font-size: 0.9rem; color: #B794F6; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Step 2: Understand My Approach</p>
  <h2 style="text-align: left;">Why I Built This (And What It Says About How I Work)</h2>
  <p style="font-size: 1.1rem; color: var(--text-secondary); margin-top: 0.5rem; margin-bottom: 2rem; line-height: 1.5; font-style: italic;">This tool isn't just a clever resume—it demonstrates how I solve problems: identify user pain, prototype fast, ship a working solution.</p>

  <p>
    I've been on both sides of pharma hiring—evaluating candidates and being evaluated. The frustration is universal: recruiters and hiring managers need specific evidence fast ("Do they have oncology launch experience? Real AI implementation, or just buzzwords?"), while candidates watch their tailored expertise get buried in generic resumes.
  </p>

  <p>
    Most people complain about this. I built a solution.
  </p>

  <p>
    <strong>The Approach: User Problem → Rapid Prototype → Ship It</strong>
  </p>

  <p>
    This interactive resume isn't a vanity project—it's a functional demonstration of how I work. When I see a user experience problem, I prototype fast, validate the concept, and iterate based on real needs. Using Claude Code (Anthropic's AI assistant) and basic developer skills, I "vibe-coded" this in a weekend. No overthinking, no perfect code—just a working solution that solves the actual problem.
  </p>

  <p>
    <strong>How It Actually Works:</strong>
  </p>

  <p>
    Every achievement in my career is tagged by skill, therapeutic area, and audience. When you select a focus (Brand Management, Oncology, AI Innovation), the system scores ~200 bullets by relevance and surfaces only what matters to you. The resume generates in real-time from structured JSON—always current, never a stale PDF floating around LinkedIn.
  </p>

  <p>
    It's hosted free on GitHub Pages. Vanilla JavaScript. No React, no backend, no complexity for complexity's sake. Just appropriate technology solving a real problem.
  </p>

  <p>
    <strong>Why This Matters</strong>
  </p>

  <ul>
    <li><strong>Empathy first:</strong> I understood your pain (finding signal in resume noise) before building anything</li>
    <li><strong>Prototype fast:</strong> Weekend project, not a 6-month perfect solution</li>
    <li><strong>AI as accelerant:</strong> Claude Code didn't replace thinking—it accelerated execution</li>
    <li><strong>Appropriate tech:</strong> Used the simplest tools that solve the problem</li>
  </ul>

  <p>
    The same mindset that built this resume builder is what I'd bring to your brand strategy, customer experience design, or omnichannel planning. See a problem, understand the user, ship a solution.
  </p>

  <!-- CONTINUE BUTTON -->
  <div style="text-align: center; margin-top: 3rem;">
    <a href="#about" style="display: inline-block; padding: 1rem 2rem; background: rgba(183, 148, 246, 0.15); border: 2px solid #B794F6; color: #B794F6; text-decoration: none; border-radius: 10px; font-weight: 600; transition: all 0.3s ease;">
      <span style="display: block;">Want to know more about my working style?</span>
      <span style="font-size: 1.3rem; display: block; margin-top: 0.3rem;">↓</span>
    </a>
  </div>
</section>

<!-- ABOUT ME SECTION -->
<section id="about">
  <p style="font-size: 0.9rem; color: #00F0FF; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem;">Step 3: Get to Know My Working Style</p>
  <h2>What's It Like to Work With Me?</h2>
  <p style="font-size: 1.1rem; color: var(--text-secondary); margin-top: 0.5rem; margin-bottom: 2rem; line-height: 1.5; font-style: italic;">Based on professional assessments (Myers-Briggs ENTJ, FIRO-B): strategic, inclusive, objective, and action-oriented.</p>

  <div class="about-content">
    <h3>Intro</h3>
    <p>
      I've been fortunate to work in organizations like Pfizer that take professional development seriously. Through that experience, I've had access to tools such as the Myers-Briggs (ENTJ) and FIRO-B assessments, which offer structured insight into how I think, collaborate, and lead. This section distills those findings into a clear, practical view of my approach to work.
    </p>

    <h3>My Assessment Snapshot</h3>
    <p>
      As a Myers-Briggs <strong>ENTJ</strong>, I'm wired for strategic thinking, structured problem-solving, and decisive action—traits that shape how I bring order to ambiguity and help teams move forward with clarity and purpose.
    </p>
    <p>
      My FIRO-B profile highlights <strong>Inclusion</strong> as my strongest interpersonal driver. I tend to lead by engaging people, creating alignment, and ensuring teams understand how their work connects to the overarching mission. With lower Control needs and moderate Affection needs, I collaborate by empowering others, emphasizing clarity and fairness, and avoiding unnecessary micromanagement.
    </p>
    <p>
      These results provide a concise, evidence-based understanding of why my professional style is consistently strategic, inclusive, objective, and geared toward building high-performing environments.
    </p>

    <div class="approach-cards">
      <div class="approach-card">
        <h3>Thinking Strategically, Delivering Clarity</h3>
        <p>
          I quickly make sense of complex environments and translate insights into actionable direction. I'm energized by big challenges, cross-functional problem-solving, and work that blends analytical rigor with creativity. My focus is always on helping teams move with intention and know exactly where we're headed.
        </p>
      </div>

      <div class="approach-card">
        <h3>Creating Alignment Through Inclusion</h3>
        <p>
          Progress accelerates when people feel connected to the mission. I bring teams together early, clarify expectations, and ensure information flows smoothly across functions. I aim to create an environment where people feel informed, valued, and aligned—not just involved.
        </p>
      </div>

      <div class="approach-card">
        <h3>Leading With Objectivity and Fairness</h3>
        <p>
          I approach decisions with structure, logic, and a wide-angle view of implications. I value competence, integrity, and transparency, and I hold myself to those same standards. My priority is reducing ambiguity so teams can focus their energy where it matters most.
        </p>
      </div>

      <div class="approach-card">
        <h3>Driving Momentum While Remaining Adaptable</h3>
        <p>
          I'm comfortable setting direction and making the tough calls, but equally willing to reassess assumptions and pivot when new information emerges. My leadership is action-oriented, ideas-driven, and aimed at building systems that support sustained performance.
        </p>
      </div>

      <div class="approach-card">
        <h3>Human-Centered, Even When Focused on the Big Picture</h3>
        <p>
          While I naturally orient toward logic and efficiency, I'm intentional about how decisions and change affect people. I work to create an environment of openness, recognition, and constructive dialogue—where individuals feel they're part of the journey, not just informed about it.
        </p>
      </div>
    </div>
  </div>

  <!-- CONTINUE BUTTON -->
  <div style="text-align: center; margin-top: 3rem;">
    <a href="#contact" style="display: inline-block; padding: 1rem 2rem; background: rgba(0, 240, 255, 0.15); border: 2px solid #00F0FF; color: #00F0FF; text-decoration: none; border-radius: 10px; font-weight: 600; transition: all 0.3s ease;">
      <span style="display: block;">Ready to connect?</span>
      <span style="font-size: 1.3rem; display: block; margin-top: 0.3rem;">↓</span>
    </a>
  </div>
</section>

<!-- CONTACT SECTION -->
<section id="contact">
  <p style="font-size: 0.9rem; color: #B794F6; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; text-align: left;">Step 4: Let's Talk</p>
  <h2 style="text-align: left;">See a Fit? Let's Connect</h2>

  <p class="contact-intro">
    If my experience aligns with what you're looking for, I'd love to hear about the role and explore how I can contribute.
  </p>

  <div class="contact-options">
    <div class="contact-card">
      <h3>Connect on LinkedIn</h3>
      <p>The fastest way to reach me and see my full professional network.</p>
      <a href="https://linkedin.com/in/mschulz" target="_blank" rel="noopener" class="contact-btn">
        View LinkedIn Profile →
      </a>
    </div>

    <div class="contact-card">
      <h3>Request Contact</h3>
      <p>Send a quick message and I'll get back to you within 24 hours.</p>

      <form action="https://formspree.io/f/mwpgnrjn" method="POST" class="contact-form">
        <div class="form-group">
          <label for="name">Your Name *</label>
          <input type="text" name="name" id="name" required>
        </div>

        <div class="form-group">
          <label for="email">Your Email *</label>
          <input type="email" name="_replyto" id="email" required>
        </div>

        <div class="form-group">
          <label for="message">Message *</label>
          <textarea name="message" id="message" required placeholder="Tell me about the role or what caught your interest..."></textarea>
        </div>

        <!-- Honeypot spam protection -->
        <input type="text" name="_gotcha" style="display:none">

        <button type="submit" class="submit-btn">Send Message</button>
      </form>
    </div>
  </div>

  <p style="text-align: center; margin-top: 2rem; color: var(--text-secondary); font-size: 0.9rem;">
    <strong>Privacy Note:</strong> I do not publicly display my email address or phone number. Please use LinkedIn or the contact form above.
  </p>
</section>

<script src="{{ '/assets/js/resume-builder.js' | relative_url }}"></script>
<script src="{{ '/assets/js/resume-init.js' | relative_url }}"></script>
