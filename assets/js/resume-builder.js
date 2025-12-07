/**
 * Interactive Resume Builder
 * Client-side resume filtering and rendering based on cv-generator logic
 */

class ResumeBuilder {
  constructor(resumeData, profilesData) {
    this.resumeData = resumeData;
    this.profiles = profilesData.profiles;
    this.filteringRules = profilesData.filtering_rules;
  }

  /**
   * Calculate relevance score for an achievement item based on priority tags
   * Mimics cv-generator's selector.py scoring logic
   */
  calculateScore(itemTags, priorityTags) {
    if (!itemTags || !Array.isArray(itemTags)) return 0;
    return itemTags.filter(tag => priorityTags.includes(tag)).length;
  }

  /**
   * Filter experience by priority tags, returning top N bullets per role
   * @param {Array} priorityTags - Tags to prioritize
   * @param {Number} maxBulletsPerRole - Max bullets to show per position
   * @returns {Array} Filtered experience with scored bullets
   */
  filterExperience(priorityTags, maxBulletsPerRole = 5) {
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
   * Filter projects by keyword matches
   * @param {Array} priorityTags - Tags to filter by
   * @param {Number} maxProjects - Maximum projects to return
   * @returns {Array} Filtered projects
   */
  filterProjects(priorityTags, maxProjects = 4) {
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
   * Get skills that match priority tags
   * @param {Array} priorityTags - Tags to filter by
   * @returns {Object} Categorized skills
   */
  getRelevantSkills(priorityTags) {
    // Map tags to skill categories
    const skillMapping = {
      ai: 'ai_ml',
      innovation: 'ai_ml',
      analytics: 'analytics',
      data_engineering: 'data_engineering',
      automation: 'tools_platforms',
      digital: 'web_digital'
    };

    const relevantCategories = new Set();
    for (const tag of priorityTags) {
      const category = skillMapping[tag];
      if (category) {
        relevantCategories.add(category);
      }
    }

    const skills = {};
    const technicalSkills = this.resumeData.skills.technical;

    for (const category of relevantCategories) {
      if (technicalSkills[category]) {
        skills[category] = technicalSkills[category];
      }
    }

    return skills;
  }

  /**
   * Generate complete resume for a profile
   * @param {String} profileId - Profile identifier
   * @returns {Object} Complete resume data
   */
  generateResume(profileId) {
    const profile = this.profiles.find(p => p.id === profileId);
    if (!profile) {
      throw new Error(`Profile ${profileId} not found`);
    }

    const maxBullets = this.filteringRules.max_bullets_per_role || 5;
    const maxProjects = this.filteringRules.max_projects_shown || 4;
    const maxRoles = this.filteringRules.max_roles_shown || 3;

    const filteredExp = this.filterExperience(profile.priority_tags, maxBullets);
    const filteredProjects = this.filterProjects(profile.priority_tags, maxProjects);
    const relevantSkills = this.getRelevantSkills(profile.priority_tags);

    return {
      profile: {
        id: profile.id,
        label: profile.label,
        headline: profile.headline,
        tagline: profile.tagline,
        description: profile.description,
        competencies: profile.competencies,
        focusSkills: profile.focus_skills
      },
      personal: this.resumeData.personal,
      experience: filteredExp.slice(0, maxRoles),
      projects: filteredProjects,
      skills: relevantSkills,
      coreCompetencies: this.resumeData.skills.core_competencies,
      education: this.resumeData.education,
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
 * Resume Renderer - Converts data to HTML
 */
class ResumeRenderer {
  /**
   * Render complete resume as HTML
   * @param {Object} resumeData - Output from ResumeBuilder.generateResume()
   * @returns {String} HTML string
   */
  static render(resumeData) {
    const html = [];

    // Header
    html.push(this.renderHeader(resumeData));

    // Professional Summary
    html.push(this.renderSummary(resumeData));

    // Core Competencies
    html.push(this.renderCompetencies(resumeData));

    // Professional Experience
    html.push(this.renderExperience(resumeData));

    // Key Initiatives/Projects
    if (resumeData.projects.length > 0) {
      html.push(this.renderProjects(resumeData));
    }

    // Skills
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
          ${p.contact.email} •
          ${p.contact.phone} •
          <a href="${p.contact.website}" target="_blank">${p.contact.website}</a>
        </div>
      </div>
    `;
  }

  static renderSummary(data) {
    return `
      <div class="resume-section">
        <h2 class="section-title">Professional Summary</h2>
        <div class="section-content">
          <p><strong>${data.profile.tagline}</strong></p>
          ${data.profile.competencies.map(c => `<p>• ${c}</p>`).join('')}
        </div>
      </div>
    `;
  }

  static renderCompetencies(data) {
    const competencies = data.profile.focusSkills.slice(0, 8);
    return `
      <div class="resume-section">
        <h2 class="section-title">Core Competencies</h2>
        <div class="section-content">
          <p>${competencies.join(' • ')}</p>
        </div>
      </div>
    `;
  }

  static renderExperience(data) {
    const expHtml = data.experience.map(exp => `
      <div class="experience-item">
        <div class="experience-header">
          <div class="experience-title">${exp.title}</div>
          <div class="experience-company">
            <strong>${exp.company}</strong>${exp.companyParent ? ` (${exp.companyParent})` : ''} | ${exp.location}
          </div>
          <div class="experience-dates">${exp.startDate} – ${exp.endDate}</div>
        </div>
        <ul class="experience-bullets">
          ${exp.bullets.map(bullet => `
            <li>
              ${bullet.text}
              <span class="bullet-score" title="Relevance: ${bullet.score} tag matches">${'★'.repeat(Math.min(bullet.score, 5))}</span>
            </li>
          `).join('')}
        </ul>
      </div>
    `).join('');

    return `
      <div class="resume-section">
        <h2 class="section-title">Professional Experience</h2>
        <div class="section-content">
          ${expHtml}
        </div>
      </div>
    `;
  }

  static renderProjects(data) {
    const projHtml = data.projects.map(proj => `
      <div class="project-item">
        <strong>${proj.name}</strong>${proj.period ? ` (${proj.period})` : ''} – ${proj.role}<br>
        ${proj.outcomes[0]}
      </div>
    `).join('');

    return `
      <div class="resume-section">
        <h2 class="section-title">Key Initiatives</h2>
        <div class="section-content">
          ${projHtml}
        </div>
      </div>
    `;
  }

  static renderSkills(data) {
    const skillLabels = {
      ai_ml: 'AI/ML',
      analytics: 'Analytics',
      data_engineering: 'Data Engineering',
      tools_platforms: 'Tools & Platforms',
      web_digital: 'Web/Digital'
    };

    const skillsHtml = Object.entries(data.skills).map(([key, skills]) => `
      <p><strong>${skillLabels[key] || key}:</strong> ${skills.join(', ')}</p>
    `).join('');

    return `
      <div class="resume-section">
        <h2 class="section-title">Technical Skills</h2>
        <div class="section-content">
          ${skillsHtml}
        </div>
      </div>
    `;
  }

  static renderEducation(data) {
    const eduHtml = data.education.map(edu => `
      <div class="education-item">
        <strong>${edu.degree} in ${edu.field}</strong><br>
        ${edu.institution} | ${edu.end_date ? edu.end_date.split('-')[0] : 'Present'}
      </div>
    `).join('');

    return `
      <div class="resume-section">
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
