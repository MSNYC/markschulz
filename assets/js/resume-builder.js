/**
 * Interactive Resume Builder - Executive Format
 * Generates comprehensive 3-page executive resumes with profile-specific content
 */

class ResumeBuilder {
  constructor(resumeData, profilesData) {
    this.resumeData = resumeData;
    this.profiles = profilesData.profiles;
    this.filteringRules = profilesData.filtering_rules;
  }

  /**
   * Calculate relevance score for an achievement item based on priority tags
   */
  calculateScore(itemTags, priorityTags) {
    if (!itemTags || !Array.isArray(itemTags)) return 0;
    return itemTags.filter(tag => priorityTags.includes(tag)).length;
  }

  /**
   * Filter experience by priority tags - NOW RETURNS MORE BULLETS (10-12)
   * @param {Array} priorityTags - Tags to prioritize
   * @param {Number} maxBulletsPerRole - Max bullets to show per position
   * @returns {Array} Filtered experience with scored bullets
   */
  filterExperience(priorityTags, maxBulletsPerRole = 12) {
    const filteredExperience = [];

    for (const exp of this.resumeData.experience) {
      for (const position of exp.positions) {
        const scoredAchievements = [];

        // Score all achievements
        for (const achievementGroup of position.achievements || []) {
          for (const item of achievementGroup.items || []) {
            if (typeof item === 'object' && item.text) {
              const score = this.calculateScore(item.tags, priorityTags);
              scoredAchievements.push({
                score,
                text: item.text,
                tags: item.tags || [],
                category: achievementGroup.category
              });
            }
          }
        }

        // Sort by score (descending)
        scoredAchievements.sort((a, b) => b.score - a.score);

        // Prefer bullets with tag matches; fallback to top N if none match
        const topWithTags = scoredAchievements.filter(a => a.score > 0);
        const chosen = topWithTags.length > 0 ? topWithTags : scoredAchievements;
        const topBullets = chosen.slice(0, maxBulletsPerRole);

        filteredExperience.push({
          company: exp.company,
          companyParent: exp.company_parent,
          location: exp.location,
          title: position.title,
          startDate: position.start_date,
          endDate: position.end_date || 'Present',
          current: position.current,
          bullets: topBullets,
          totalBullets: scoredAchievements.length,
          matchedBullets: topWithTags.length
        });
      }
    }

    return filteredExperience;
  }

  /**
   * Filter projects by keyword matches - show more projects
   */
  filterProjects(priorityTags, maxProjects = 6) {
    const scoredProjects = [];

    for (const project of this.resumeData.projects) {
      const keywords = project.keywords || [];
      const score = keywords.filter(kw =>
        priorityTags.includes(kw.toLowerCase())
      ).length;

      if (score > 0) {
        scoredProjects.push({ ...project, score });
      }
    }

    scoredProjects.sort((a, b) => b.score - a.score);
    return scoredProjects.slice(0, maxProjects);
  }

  /**
   * Get ALL relevant skills organized by category
   */
  getAllSkills() {
    return {
      core_competencies: this.resumeData.skills.core_competencies || [],
      technical: this.resumeData.skills.technical || {},
      marketing_specialized: this.resumeData.skills.marketing_specialized || [],
      leadership: this.resumeData.skills.leadership || [],
      methodologies: this.resumeData.skills.methodologies || []
    };
  }

  /**
   * Generate complete resume for a profile
   */
  generateResume(profileId) {
    const profile = this.profiles.find(p => p.id === profileId);
    if (!profile) {
      throw new Error(`Profile ${profileId} not found`);
    }

    const maxBullets = 12; // Increased from 5
    const maxProjects = 6; // Increased from 4
    const maxRoles = 10; // Show ALL roles, not just 3

    const filteredExp = this.filterExperience(profile.priority_tags, maxBullets);
    const filteredProjects = this.filterProjects(profile.priority_tags, maxProjects);
    const allSkills = this.getAllSkills();

    return {
      profile: {
        id: profile.id,
        label: profile.label,
        headline: profile.headline,
        tagline: profile.tagline,
        description: profile.description,
        competencies: profile.competencies,
        focusSkills: profile.focus_skills,
        idealFor: profile.ideal_for || []
      },
      personal: this.resumeData.personal,
      summary: this.resumeData.summary,
      experience: filteredExp.slice(0, maxRoles),
      projects: filteredProjects,
      allSkills: allSkills,
      education: this.resumeData.education,
      languages: this.resumeData.languages || [],
      stats: {
        experienceCount: filteredExp.length,
        projectCount: filteredProjects.length,
        totalBullets: filteredExp.reduce((sum, exp) => sum + exp.bullets.length, 0),
        matchRate: this.calculateMatchRate(filteredExp)
      }
    };
  }

  /**
   * Calculate overall match rate across experience
   */
  calculateMatchRate(filteredExperience) {
    let totalBullets = 0;
    let matchedBullets = 0;

    for (const exp of filteredExperience) {
      totalBullets += exp.totalBullets;
      matchedBullets += exp.matchedBullets;
    }

    return totalBullets > 0 ? (matchedBullets / totalBullets * 100).toFixed(1) : 0;
  }
}

/**
 * Resume Renderer - Executive Format
 * Converts data to professional 3-page HTML resume
 */
class ResumeRenderer {
  /**
   * Render complete resume as HTML
   */
  static render(resumeData) {
    const html = [];

    // Header with contact info
    html.push(this.renderHeader(resumeData));

    // Executive Snapshot
    html.push(this.renderExecutiveSnapshot(resumeData));

    // Targeted Highlights
    html.push(this.renderTargetedHighlights(resumeData));

    // Professional Experience (comprehensive)
    html.push(this.renderExperience(resumeData));

    // Skills (organized paragraphs)
    html.push(this.renderSkills(resumeData));

    // Education
    html.push(this.renderEducation(resumeData));

    return html.join('\n');
  }

  static renderHeader(data) {
    const p = data.personal;
    return `
      <div class="resume-header">
        <h1 class="resume-name">${p.name.full}</h1>
        <div class="resume-headline">${data.profile.headline}</div>
        <div class="resume-contact">
          ${p.contact.location.city}, ${p.contact.location.state} •
          LinkedIn: <a href="https://linkedin.com/in/mschulz" target="_blank">linkedin.com/in/mschulz</a>
        </div>
      </div>
    `;
  }

  static renderExecutiveSnapshot(data) {
    const profile = data.profile;
    return `
      <div class="resume-section executive-snapshot">
        <h2 class="section-title">Executive Snapshot</h2>
        <div class="section-content">
          <p class="snapshot-tagline"><strong>${profile.tagline}</strong></p>

          <p class="snapshot-description">${data.summary.long}</p>

          <p><strong>Core Strengths:</strong> ${profile.focusSkills.slice(0, 3).join(' • ')}</p>
        </div>
      </div>
    `;
  }

  static renderTargetedHighlights(data) {
    const profile = data.profile;
    const projects = data.projects.slice(0, 3);

    return `
      <div class="resume-section targeted-highlights">
        <h2 class="section-title">Targeted Highlights</h2>
        <div class="section-content">
          <div class="highlight-item">
            <p><strong>• Core Fit:</strong> ${profile.competencies[0] || profile.description}</p>
          </div>

          ${profile.competencies.slice(1, 3).map(comp => `
            <div class="highlight-item">
              <p><strong>• Key Capability:</strong> ${comp}</p>
            </div>
          `).join('')}

          ${projects.length > 0 ? `
            <div class="highlight-item">
              <p><strong>• Selected Projects:</strong> ${projects.map(p => p.name).join(', ')}${projects.length > 0 ? '. ' + projects[0].outcomes[0] : ''}</p>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  static renderExperience(data) {
    const expHtml = data.experience.map(exp => `
      <div class="experience-item">
        <div class="experience-header">
          <div class="experience-title-line">
            <span class="experience-title"><strong>${exp.title} — ${exp.company}</strong>${exp.companyParent ? ` (${exp.companyParent})` : ''}</span>
          </div>
          <div class="experience-meta">
            ${exp.location} | ${exp.startDate} – ${exp.endDate}
          </div>
        </div>
        <ul class="experience-bullets">
          ${exp.bullets.map(bullet => `
            <li>${bullet.text}</li>
          `).join('')}
        </ul>
      </div>
    `).join('');

    return `
      <div class="resume-section experience-section">
        <h2 class="section-title">Experience</h2>
        <div class="section-content">
          ${expHtml}
        </div>
      </div>
    `;
  }

  static renderSkills(data) {
    const skills = data.allSkills;

    // Build skill paragraphs based on profile
    const skillParagraphs = [];

    // Strategy skills
    if (data.profile.id === 'brand_management') {
      skillParagraphs.push({
        title: 'Brand & Commercial Strategy',
        content: 'Oncology brand strategy (HCP & patient), portfolio management, launch excellence, commercial strategy development, market analytics, competitive intelligence, HCP marketing, patient engagement, cross-functional collaboration'
      });
    } else if (data.profile.id === 'strategy_innovation') {
      skillParagraphs.push({
        title: 'Strategic Planning & Positioning',
        content: 'Commercial strategy, messaging & positioning, go-to-market planning, competitive analysis, market landscape synthesis, strategic narrative development, brand imperatives alignment, cross-functional orchestration'
      });
    } else {
      skillParagraphs.push({
        title: 'Customer Experience & Omnichannel Strategy',
        content: 'Omnichannel orchestration (media, CRM, digital, congress), experience planning & journey design, behavioral pathway modeling, touchpoint architecture, conversion-flow optimization, full-funnel engagement design, HCP and patient experience across channels'
      });
    }

    // Always include AI/Innovation for CX profile
    if (data.profile.id === 'cx_engagement') {
      skillParagraphs.push({
        title: 'AI & Innovation',
        content: 'AI enablement & education (Founder: BEACON), responsible AI adoption frameworks, custom GPT/LLM development, AI-assisted content production, workflow design for generative AI, agency-wide AI training, risk & MLR considerations for AI use, innovation workshop facilitation'
      });
    }

    // Analytics
    skillParagraphs.push({
      title: 'Analytics & Measurement',
      content: 'Experience analytics & behavioral funnel analysis, dashboard design, web analytics (GA4), cross-channel performance measurement, KPI frameworks, ROI modeling, regression modeling, data storytelling, insight synthesis for brand planning'
    });

    // Leadership
    skillParagraphs.push({
      title: 'Leadership',
      content: 'Cross-functional team leadership, stakeholder alignment, workstream governance, capability building, workshop facilitation, mentoring & coaching, agency-wide cultural transformation'
    });

    const skillsHtml = skillParagraphs.map(section => `
      <p class="skill-paragraph">
        <strong>${section.title}:</strong> ${section.content}
      </p>
    `).join('');

    return `
      <div class="resume-section skills-section">
        <h2 class="section-title">Skills</h2>
        <div class="section-content">
          ${skillsHtml}
        </div>
      </div>
    `;
  }

  static renderEducation(data) {
    const eduHtml = data.education.map(edu => `
      <div class="education-item">
        <strong>${edu.degree}</strong> ${edu.field ? `in ${edu.field}` : ''} — ${edu.institution}
      </div>
    `).join('');

    return `
      <div class="resume-section education-section">
        <h2 class="section-title">Education</h2>
        <div class="section-content">
          ${eduHtml}
        </div>
      </div>
    `;
  }
}

// Export for use in HTML
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { ResumeBuilder, ResumeRenderer };
}
