---
layout: home
title: Mark Schulz - Pharmaceutical Marketing Leader
---

<link rel="stylesheet" href="{{ '/assets/css/resume-builder.css' | relative_url }}">

<style>
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
    <div class="profile-selector">
      <div class="profile-options">
        <label class="profile-card" data-profile="brand_management">
          <input type="radio" name="profile" value="brand_management" checked>
          <div class="card-content">
            <div class="card-icon">💊</div>
            <h3>Brand Management</h3>
            <p>Pharmaceutical brand strategy, launch excellence, and portfolio management</p>
            <div class="card-tags">
              <span class="tag">Strategy</span>
              <span class="tag">Oncology</span>
              <span class="tag">Launch</span>
              <span class="tag">Portfolio</span>
            </div>
          </div>
        </label>

        <label class="profile-card" data-profile="strategy_innovation">
          <input type="radio" name="profile" value="strategy_innovation">
          <div class="card-content">
            <div class="card-icon">🚀</div>
            <h3>Strategy & Innovation</h3>
            <p>Digital transformation, AI/ML implementation, and strategic planning</p>
            <div class="card-tags">
              <span class="tag">AI/ML</span>
              <span class="tag">Innovation</span>
              <span class="tag">Analytics</span>
              <span class="tag">Digital</span>
            </div>
          </div>
        </label>

        <label class="profile-card" data-profile="cx_engagement">
          <input type="radio" name="profile" value="cx_engagement">
          <div class="card-content">
            <div class="card-icon">🎯</div>
            <h3>Customer Experience</h3>
            <p>Omnichannel engagement, experience planning, and journey optimization</p>
            <div class="card-tags">
              <span class="tag">CX</span>
              <span class="tag">Omnichannel</span>
              <span class="tag">Journey Mapping</span>
              <span class="tag">HCP</span>
            </div>
          </div>
        </label>
      </div>

      <button id="generateBtn" class="generate-btn">
        <span class="btn-text">Generate Tailored Resume</span>
        <span class="btn-icon">→</span>
      </button>
    </div>

    <div id="resumePreview" class="resume-preview" style="display:none;">
      <div class="preview-header">
        <h2>Your Tailored Resume</h2>
        <div class="preview-stats" id="resumeStats"></div>
      </div>

      <div class="export-buttons">
        <button id="printPdfBtn" class="export-btn">
          <span class="icon">🖨️</span>
          <span>Print to PDF</span>
        </button>
        <button id="copyTextBtn" class="export-btn">
          <span class="icon">📋</span>
          <span>Copy to Clipboard</span>
        </button>
        <button id="copyLinkBtn" class="export-btn">
          <span class="icon">🔗</span>
          <span>Copy Shareable Link</span>
        </button>
      </div>

      <div id="resumeContent" class="resume-content">
        <!-- Dynamically rendered resume content goes here -->
      </div>

      <div class="resume-actions">
        <button id="regenerateBtn" class="action-btn tertiary">
          <span class="btn-icon">↻</span>
          <span class="btn-text">Try Another Profile</span>
        </button>
      </div>
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
  <h2>A Bit About Me (The Human Side)</h2>

  <div class="about-content">
    <p>
      Beyond the resume data and professional achievements, I'm someone who genuinely loves the craft of marketing—especially the puzzle of connecting the right message to the right person at the right moment. I get energized by data that tells a story, by AI tools that unlock new possibilities, and by teams that collaborate well.
    </p>

    <p>
      I'm also a lifelong learner who believes the best solutions come from understanding multiple perspectives. That's why I've intentionally worked across agency, manufacturer, and publisher roles—each taught me something the others couldn't. And it's why I'm constantly experimenting with new tools (like building this site with Claude Code) to stay ahead of where the industry is heading.
    </p>

    <p>
      When I'm not thinking about pharmaceutical marketing, you'll find me exploring new technologies, diving into data analysis for fun, or figuring out how to automate something that probably doesn't need automating (but should be anyway).
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
<script>
// Enhanced resume initialization with new export functions
(function() {
  'use strict';

  let resumeBuilder = null;
  let currentResume = null;
  let currentProfileId = 'brand_management';

  // Load JSON data files
  async function loadData() {
    try {
      const [resumeResponse, profilesResponse] = await Promise.all([
        fetch('/data/resume.json'),
        fetch('/data/resume_profiles.json')
      ]);

      if (!resumeResponse.ok || !profilesResponse.ok) {
        throw new Error('Failed to load data files');
      }

      const resumeData = await resumeResponse.json();
      const profilesData = await profilesResponse.json();

      return { resumeData, profilesData };
    } catch (error) {
      console.error('Error loading data:', error);
      showError('Failed to load resume data. Please refresh the page.');
      return null;
    }
  }

  // Initialize
  async function init() {
    const data = await loadData();
    if (!data) return;

    resumeBuilder = new ResumeBuilder(data.resumeData, data.profilesData);
    setupEventListeners();

    // Check URL for profile parameter
    const urlParams = new URLSearchParams(window.location.search);
    const profileParam = urlParams.get('profile');
    if (profileParam) {
      const profileCard = document.querySelector(`input[value="${profileParam}"]`);
      if (profileCard) {
        profileCard.checked = true;
        currentProfileId = profileParam;
        setTimeout(() => generateResume(), 500);
      }
    }
  }

  // Set up event listeners
  function setupEventListeners() {
    document.getElementById('generateBtn').addEventListener('click', generateResume);

    const profileInputs = document.querySelectorAll('input[name="profile"]');
    profileInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        currentProfileId = e.target.value;
      });
    });

    // New export buttons
    document.getElementById('printPdfBtn').addEventListener('click', printToPDF);
    document.getElementById('copyTextBtn').addEventListener('click', copyToClipboard);
    document.getElementById('copyLinkBtn').addEventListener('click', copyLink);
    document.getElementById('regenerateBtn').addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Generate resume
  function generateResume() {
    if (!resumeBuilder) return;

    try {
      const generateBtn = document.getElementById('generateBtn');
      const originalText = generateBtn.querySelector('.btn-text').textContent;
      generateBtn.querySelector('.btn-text').textContent = 'Generating...';
      generateBtn.disabled = true;

      currentResume = resumeBuilder.generateResume(currentProfileId);
      const resumeContent = document.getElementById('resumeContent');
      resumeContent.innerHTML = ResumeRenderer.render(currentResume);

      updateStats(currentResume);

      const preview = document.getElementById('resumePreview');
      preview.style.display = 'block';

      setTimeout(() => {
        preview.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);

      setTimeout(() => {
        generateBtn.querySelector('.btn-text').textContent = originalText;
        generateBtn.disabled = false;
      }, 500);

    } catch (error) {
      console.error('Error generating resume:', error);
      showError('Failed to generate resume. Please try again.');
    }
  }

  // Update stats
  function updateStats(resume) {
    const statsDiv = document.getElementById('resumeStats');
    statsDiv.innerHTML = `
      <div class="stat">
        <span class="stat-icon">📊</span>
        <span>${resume.stats.matchRate}% match rate</span>
      </div>
      <div class="stat">
        <span class="stat-icon">💼</span>
        <span>${resume.experience.length} roles</span>
      </div>
      <div class="stat">
        <span class="stat-icon">⭐</span>
        <span>${resume.stats.totalBullets} key achievements</span>
      </div>
      <div class="stat">
        <span class="stat-icon">🚀</span>
        <span>${resume.projects.length} projects</span>
      </div>
    `;
  }

  // Print to PDF
  function printToPDF() {
    if (!currentResume) return;
    window.print();
  }

  // Copy to Clipboard
  function copyToClipboard() {
    if (!currentResume) return;

    const resumeContent = document.getElementById('resumeContent');
    const textContent = resumeContent.innerText || resumeContent.textContent;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(textContent).then(() => {
        showSuccess('Resume copied to clipboard!');
      }).catch(err => {
        console.error('Failed to copy:', err);
        fallbackCopy(textContent);
      });
    } else {
      fallbackCopy(textContent);
    }
  }

  // Fallback copy method
  function fallbackCopy(text) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.select();

    try {
      document.execCommand('copy');
      showSuccess('Resume copied to clipboard!');
    } catch (err) {
      console.error('Fallback copy failed:', err);
      alert('Please manually copy the resume text.');
    }

    document.body.removeChild(textArea);
  }

  // Copy shareable link
  function copyLink() {
    const url = `${window.location.origin}/?profile=${currentProfileId}#interactive-tool`;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        showSuccess('Link copied to clipboard!');
      }).catch(err => {
        console.error('Failed to copy:', err);
        fallbackCopy(url);
      });
    } else {
      fallbackCopy(url);
    }
  }

  // Show error message
  function showError(message) {
    alert('Error: ' + message);
  }

  // Show success message
  function showSuccess(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
      position: fixed;
      top: 20px;
      right: 20px;
      background: #00F0FF;
      color: #0A0E27;
      padding: 1rem 1.5rem;
      border-radius: 8px;
      font-weight: 600;
      box-shadow: 0 4px 12px rgba(0, 240, 255, 0.4);
      z-index: 10000;
      animation: slideIn 0.3s ease;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
      notification.style.animation = 'slideOut 0.3s ease';
      setTimeout(() => {
        document.body.removeChild(notification);
      }, 300);
    }, 3000);
  }

  // Add CSS animations
  const style = document.createElement('style');
  style.textContent = `
    @keyframes slideIn {
      from {
        transform: translateX(400px);
        opacity: 0;
      }
      to {
        transform: translateX(0);
        opacity: 1;
      }
    }
    @keyframes slideOut {
      from {
        transform: translateX(0);
        opacity: 1;
      }
      to {
        transform: translateX(400px);
        opacity: 0;
      }
    }
  `;
  document.head.appendChild(style);

  // Initialize on page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
</script>
