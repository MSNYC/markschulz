---
layout: home
title: Mark Schulz - Pharmaceutical Marketing Leader
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

.sticky-nav nav {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  padding: 0 1rem;
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
}

/* ===== HERO SECTION ===== */
.hero-section {
  text-align: center;
  padding: 3rem 1.5rem;
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.05), rgba(183, 148, 246, 0.05));
  border-radius: 16px;
  margin-bottom: 4rem;
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
  text-align: center;
  margin-bottom: 3rem;
}

.tool-intro h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #00F0FF;
}

.tool-intro p {
  font-size: 1.1rem;
  color: var(--text-secondary);
  max-width: 700px;
  margin: 0 auto;
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
  margin: 6rem 0;
  padding: 3rem 2rem;
  background: rgba(26, 31, 58, 0.3);
  border-radius: 12px;
  border-left: 4px solid #B794F6;
  scroll-margin-top: 80px;
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
  max-width: 900px;
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
  text-align: center;
}

.about-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
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
  text-align: center;
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
  <nav>
    <a href="#top">Home</a>
    <a href="#interactive-tool">Resume Tool</a>
    <a href="#behind-the-tool">Behind the Tool</a>
    <a href="#about">About Me</a>
    <a href="#contact">Contact</a>
  </nav>
</div>

<!-- HERO SECTION -->
<div class="hero-section">
  <h1 class="hero-title">Find the Experience That Matches Your Role</h1>

  <p class="hero-subtitle">
    This interactive resume filters my background to show the skills, projects, and achievements most relevant to your open position.
  </p>

  <p class="hero-hook">
    Select your focus area below to see a tailored view of my experience. Export or share as needed.
  </p>
</div>

<!-- INTERACTIVE RESUME TOOL -->
<section id="interactive-tool">
  <div class="tool-intro">
    <h2>Select Your Focus Area</h2>
    <p>Choose the role type that best matches your open position. The resume will instantly filter to show the most relevant experience.</p>
  </div>

  <div class="resume-builder-container">
    <!-- Step 1: Choose Your Path -->
    <div class="selection-method">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 0.5rem;">Step 1: Choose Your Path</h3>
      <p class="step-description">Pick a quick pre-built profile or customize your own focus areas</p>

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
            <p>Build your own using checkboxes (1-8 selections)</p>
          </div>
        </label>
      </div>
    </div>

    <!-- Step 2a: Quick Select (Profiles) -->
    <div id="quickSelectPanel" class="profile-selector">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 1.5rem;">Step 2: Select a Profile</h3>

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

        <a href="/resume/cx-engagement/" class="profile-card">
          <div class="card-content">
            <div class="card-icon">🚀</div>
            <h4>Customer Experience (CX) & Omnichannel Innovation</h4>
            <p>Omnichannel strategy, experience design, AI/ML implementation, and innovative engagement</p>
            <div class="card-tags">
              <span class="tag">CX</span>
              <span class="tag">Omnichannel</span>
              <span class="tag">AI/ML</span>
              <span class="tag">Innovation</span>
            </div>
          </div>
        </a>
      </div>

      <p style="text-align: center; color: var(--builder-text-secondary); margin-top: 1.5rem; font-size: 0.95rem;">
        Click any card above to view that tailored resume →
      </p>
    </div>

    <!-- Step 2b: Custom Select (Checkboxes) -->
    <div id="customSelectPanel" class="checkbox-selector" style="display:none;">
      <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 0.5rem;">Step 2: Select Your Focus Areas</h3>
      <p class="step-description">Choose 1-8 areas that best match what you're looking for <span id="selectionCount">(0 selected)</span></p>

      <div id="checkboxCategories" class="checkbox-categories">
        <!-- Dynamically populated from resume_profiles.json -->
      </div>

      <button id="generateCustomBtn" class="generate-btn" disabled>
        <span class="btn-text">Generate Custom Resume</span>
        <span class="btn-icon">→</span>
      </button>
    </div>

  </div>
</section>

<!-- BEHIND THE TOOL SECTION -->
<section id="behind-the-tool">
  <h2>Behind the Tool: Why I Built This</h2>

  <p>
    As someone who has hired for pharmaceutical marketing roles, I know the pain: scanning through pages of resume content trying to find evidence of specific skills. "Do they have oncology experience?" "Have they actually used AI tools, or just heard of them?" "Can they think strategically about omnichannel?"
  </p>

  <p>
    So I built this interactive resume to solve that problem—for <em>you</em>, the person evaluating candidates. Using <strong>Claude Code</strong> (Anthropic's AI coding assistant) and my basic developer skills, I "vibe-coded" this solution in a few hours. It demonstrates the same approach I bring to marketing challenges: understand the user's pain point, prototype quickly, and deliver something genuinely useful.
  </p>

  <p>
    <strong>Here's how it works:</strong>
  </p>
  <ul>
    <li><strong>Tag-based filtering:</strong> Every achievement in my resume databank is tagged (e.g., "ai", "oncology", "brand", "analytics"). When you select a profile, it scores each bullet by relevance.</li>
    <li><strong>Real-time generation:</strong> The resume you see is generated on-the-fly from a structured JSON databank—always current, never outdated.</li>
    <li><strong>User-centric design:</strong> Built specifically for recruiters and hiring managers who need to assess fit quickly.</li>
    <li><strong>Free, modern tools:</strong> Hosted on GitHub Pages (free), built with vanilla JavaScript, styled with CSS. No fancy frameworks, just effective solutions.</li>
  </ul>

  <p>
    This tool is itself a portfolio piece—it shows how I approach customer experience design, use AI effectively, and solve real problems with appropriate technology. The same skills that built this site are the skills I'd bring to your team: empathy for the end user, comfort with modern AI tools, and the ability to ship useful solutions fast.
  </p>
</section>

<!-- ABOUT ME SECTION -->
<section id="about">
  <h2>About My Approach</h2>

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

    <h3>Thinking Strategically, Delivering Clarity</h3>
    <p>
      I quickly make sense of complex environments and translate insights into actionable direction. I'm energized by big challenges, cross-functional problem-solving, and work that blends analytical rigor with creativity. My focus is always on helping teams move with intention and know exactly where we're headed.
    </p>

    <h3>Creating Alignment Through Inclusion</h3>
    <p>
      Progress accelerates when people feel connected to the mission. I bring teams together early, clarify expectations, and ensure information flows smoothly across functions. I aim to create an environment where people feel informed, valued, and aligned—not just involved.
    </p>

    <h3>Leading With Objectivity and Fairness</h3>
    <p>
      I approach decisions with structure, logic, and a wide-angle view of implications. I value competence, integrity, and transparency, and I hold myself to those same standards. My priority is reducing ambiguity so teams can focus their energy where it matters most.
    </p>

    <h3>Driving Momentum While Remaining Adaptable</h3>
    <p>
      I'm comfortable setting direction and making the tough calls, but equally willing to reassess assumptions and pivot when new information emerges. My leadership is action-oriented, ideas-driven, and aimed at building systems that support sustained performance.
    </p>

    <h3>Human-Centered, Even When Focused on the Big Picture</h3>
    <p>
      While I naturally orient toward logic and efficiency, I'm intentional about how decisions and change affect people. I work to create an environment of openness, recognition, and constructive dialogue—where individuals feel they're part of the journey, not just informed about it.
    </p>
  </div>
</section>

<!-- CONTACT SECTION -->
<section id="contact">
  <h2>Let's Connect</h2>

  <p class="contact-intro">
    Interested in discussing this role further? I'd love to hear from you.
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

      <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="contact-form">
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
