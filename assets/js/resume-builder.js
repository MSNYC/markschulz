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
   * Enhanced scoring with brand diversity and specificity
   * Prevents single-brand domination and prioritizes specific brand mentions
   */
  calculateEnhancedScore(item, priorityTags) {
    let score = this.calculateScore(item.tags, priorityTags);
    if (score === 0) return 0;

    const text = item.text.toLowerCase();

    // Define brand families
    const brands = {
      oncology: ['kisqali', 'tagrisso', 'brukinsa', 'imfinzi'],
      cardio: ['lipitor', 'caduet'],
      hiv: ['biktarvy', 'descovy', 'truvada'],
      rare: ['banzel', 'tecfidera', 'lucentis'],
      mens: ['viagra']
    };

    // Boost for specific brand mentions (combats generic "oncology-focused brands" bullets)
    let hasBrandMention = false;
    for (const brandList of Object.values(brands)) {
      for (const brand of brandList) {
        if (text.includes(brand)) {
          score += 2; // Significant boost for brand-specific achievements
          hasBrandMention = true;
          break;
        }
      }
      if (hasBrandMention) break;
    }

    // Small boost for quantified impact (numbers indicate measurable achievement)
    const hasMetrics = /\d+%|\$\d+|\d+\+|reduced|increased|grew|saved/i.test(item.text);
    if (hasMetrics) {
      score += 0.5;
    }

    return score;
  }

  /**
   * Filter experience by priority tags - ALWAYS SHOWS ALL POSITIONS
   * Now with brand diversity to prevent single-brand domination
   * @param {Array} priorityTags - Tags to prioritize
   * @param {Number} maxBulletsPerRole - Max bullets to show per position with matches
   * @param {Number} fallbackBullets - Number of bullets to show for non-matching positions
   * @returns {Array} Filtered experience with scored bullets
   */
  filterExperience(priorityTags, maxBulletsPerRole = 8, fallbackBullets = 2) {
    const filteredExperience = [];

    for (const exp of this.resumeData.experience) {
      for (const position of exp.positions) {
        const matchingAchievements = [];
        const allAchievements = [];

        // Score all achievements with enhanced scoring
        for (const achievementGroup of position.achievements || []) {
          for (const item of achievementGroup.items || []) {
            if (typeof item === 'object' && item.text) {
              const baseScore = this.calculateScore(item.tags, priorityTags);
              const enhancedScore = this.calculateEnhancedScore(item, priorityTags);

              const achievement = {
                score: enhancedScore,
                baseScore: baseScore,
                text: item.text,
                tags: item.tags || [],
                category: achievementGroup.category
              };

              // Track all achievements for fallback
              allAchievements.push(achievement);

              // Track only matching achievements
              if (baseScore > 0) {
                matchingAchievements.push(achievement);
              }
            }
          }
        }

        // ALWAYS include this position (even with 0 matches)
        let finalBullets = [];

        if (matchingAchievements.length > 0) {
          // Position has relevant achievements - sort by enhanced score
          matchingAchievements.sort((a, b) => b.score - a.score);

          // Apply brand diversity: don't show more than 2 bullets mentioning the same brand
          finalBullets = this.ensureBrandDiversity(matchingAchievements, maxBulletsPerRole);
        } else if (allAchievements.length > 0) {
          // Position has NO matches - show fallback bullets (highest impact generic achievements)
          // Sort by text length as proxy for impact (longer = more detailed/impressive)
          allAchievements.sort((a, b) => b.text.length - a.text.length);
          finalBullets = allAchievements.slice(0, fallbackBullets);
        }

        // Always add position to experience list
        filteredExperience.push({
          company: exp.company,
          companyParent: exp.company_parent,
          location: exp.location,
          title: position.title,
          startDate: position.start_date,
          endDate: position.end_date || 'Present',
          current: position.current,
          bullets: finalBullets,
          totalBullets: allAchievements.length,
          matchedBullets: matchingAchievements.length,
          hasMatches: matchingAchievements.length > 0 // Flag for styling
        });
      }
    }

    return filteredExperience;
  }

  /**
   * Ensure brand diversity - prevent single brand from dominating bullet list
   * Max 2 bullets per brand to ensure varied portfolio representation
   */
  ensureBrandDiversity(sortedAchievements, maxBullets) {
    const brands = ['kisqali', 'tagrisso', 'brukinsa', 'imfinzi', 'lipitor', 'caduet',
                    'biktarvy', 'descovy', 'truvada', 'banzel', 'tecfidera', 'lucentis', 'viagra'];

    const brandCounts = {};
    const selected = [];

    for (const achievement of sortedAchievements) {
      if (selected.length >= maxBullets) break;

      const text = achievement.text.toLowerCase();

      // Find which brand (if any) is mentioned
      let mentionedBrand = null;
      for (const brand of brands) {
        if (text.includes(brand)) {
          mentionedBrand = brand;
          break;
        }
      }

      // If no brand mentioned, or brand count under limit, include it
      if (!mentionedBrand) {
        selected.push(achievement);
      } else {
        const currentCount = brandCounts[mentionedBrand] || 0;
        if (currentCount < 2) { // Max 2 bullets per brand
          brandCounts[mentionedBrand] = currentCount + 1;
          selected.push(achievement);
        }
        // else: skip this bullet, brand already has 2 mentions
      }
    }

    return selected;
  }

  /**
   * Get top-scored achievements across ALL experience (for Targeted Highlights)
   * @param {Array} priorityTags - Tags to prioritize
   * @param {Number} maxHighlights - Number of highlights to return
   * @returns {Array} Top scored achievements with company context
   */
  getTopAchievements(priorityTags, maxHighlights = 5) {
    const allScoredAchievements = [];
    const seenTexts = new Set(); // Track achievement texts to avoid exact duplicates

    // Helper function to check if two texts are similar (near-duplicates)
    const isSimilar = (text1, text2, threshold = 0.7) => {
      const words1 = new Set(text1.toLowerCase().split(/\s+/));
      const words2 = new Set(text2.toLowerCase().split(/\s+/));
      const intersection = new Set([...words1].filter(w => words2.has(w)));
      const union = new Set([...words1, ...words2]);
      return intersection.size / union.size >= threshold;
    };

    // Collect and score ALL achievements across all positions
    for (const exp of this.resumeData.experience) {
      for (const position of exp.positions) {
        for (const achievementGroup of position.achievements || []) {
          for (const item of achievementGroup.items || []) {
            if (typeof item === 'object' && item.text) {
              let score = this.calculateScore(item.tags, priorityTags);
              const normalizedText = item.text.toLowerCase().trim();

              // BOOST SCORE for brand-specific achievements
              // When filtering by therapeutic area or audience, achievements mentioning specific brands should rank higher
              const oncologyBrands = ['tagrisso', 'kisqali', 'brukinsa', 'imfinzi'];
              const cardioBrands = ['lipitor', 'caduet'];
              const hivRareBrands = ['biktarvy', 'descovy', 'truvada', 'banzel'];
              const patientBrands = ['tagrisso', 'banzel', 'lucentis', 'tecfidera', 'lyrica'];
              const hcpBrands = ['kisqali', 'brukinsa', 'lipitor', 'caduet', 'viagra'];
              const mensHealthBrands = ['viagra'];

              // Check which tags are in priority
              const hasOncologyTag = priorityTags.includes('oncology');
              const hasCardioTag = priorityTags.includes('cardio') || priorityTags.includes('cardiovascular');
              const hasHivTag = priorityTags.includes('hiv') || priorityTags.includes('rare_disease') || priorityTags.includes('mens_health');
              const hasPatientTag = priorityTags.includes('patient');
              const hasHcpTag = priorityTags.includes('hcp');

              // Check which brands are mentioned
              const mentionsOncologyBrand = oncologyBrands.some(brand => normalizedText.includes(brand));
              const mentionsCardioBrand = cardioBrands.some(brand => normalizedText.includes(brand));
              const mentionsHivRareBrand = hivRareBrands.some(brand => normalizedText.includes(brand)) || normalizedText.includes('hiv') || normalizedText.includes('gilead');
              const mentionsPatientBrand = patientBrands.some(brand => normalizedText.includes(brand));
              const mentionsHcpBrand = hcpBrands.some(brand => normalizedText.includes(brand));
              const mentionsMensHealthBrand = mensHealthBrands.some(brand => normalizedText.includes(brand));

              // Apply boosts based on matches
              if (hasOncologyTag && mentionsOncologyBrand) {
                score += 3; // Strong boost for oncology brands when filtering by oncology
              }

              if (hasCardioTag && mentionsCardioBrand) {
                score += 3; // Strong boost for cardio brands when filtering by cardio
              }

              if (hasHivTag && (mentionsHivRareBrand || mentionsMensHealthBrand)) {
                score += 3; // Strong boost for HIV/rare disease brands
              }

              if (hasPatientTag && mentionsPatientBrand) {
                score += 2; // Boost patient brand-specific achievements
              }

              if (hasHcpTag && mentionsHcpBrand) {
                score += 2; // Boost HCP brand-specific achievements
              }

              // Only include achievements with tag matches AND not already seen (exact or similar)
              if (score > 0 && !seenTexts.has(normalizedText)) {
                // Check if this achievement is similar to any already added
                let isDuplicate = false;
                for (const seen of seenTexts) {
                  if (isSimilar(normalizedText, seen)) {
                    isDuplicate = true;
                    break;
                  }
                }

                if (!isDuplicate) {
                  seenTexts.add(normalizedText);
                  allScoredAchievements.push({
                    score,
                    text: item.text,
                    tags: item.tags || [],
                    category: achievementGroup.category,
                    company: exp.company,
                    title: position.title
                  });
                }
              }
            }
          }
        }
      }
    }

    // Sort by score (descending)
    allScoredAchievements.sort((a, b) => b.score - a.score);

    // Apply brand diversity to Targeted Highlights (prevent single-brand domination)
    return this.ensureBrandDiversity(allScoredAchievements, maxHighlights);
  }

  /**
   * Generate dynamic headline based on selected checkboxes and categories
   * @param {Array} selectedCheckboxes - Array of selected checkbox objects
   * @param {Object} selectedCategories - Category analysis object
   * @returns {String} Dynamic headline
   */
  static generateDynamicHeadline(selectedCheckboxes, selectedCategories) {
    if (!selectedCheckboxes || selectedCheckboxes.length === 0) {
      return 'Pharmaceutical Marketing Professional';
    }

    // Extract specific selections
    const therapeutic = selectedCheckboxes.find(cb =>
      ['oncology', 'cardio', 'hiv', 'mens_health'].includes(cb.id)
    );
    const hasAI = selectedCheckboxes.some(cb => cb.id === 'ai');
    const hasCX = selectedCheckboxes.some(cb => ['cx', 'xp', 'experience_planning', 'journey_mapping'].includes(cb.id));
    const hasOmnichannel = selectedCheckboxes.some(cb => cb.id === 'omnichannel');
    const hasBrand = selectedCheckboxes.some(cb => cb.id === 'brand');
    const hasStrategy = selectedCheckboxes.some(cb => cb.id === 'strategy');
    const hasLeadership = selectedCategories['Leadership & Operations']?.count > 0;
    const hasHCP = selectedCheckboxes.some(cb => cb.id === 'hcp');
    const hasMedia = selectedCheckboxes.some(cb => cb.id === 'media');

    // Headline generation logic based on combinations
    const parts = [];

    // Therapeutic area first (if selected)
    if (therapeutic) {
      parts.push(therapeutic.label);
    }

    // Primary expertise
    if (hasAI && hasCX) {
      parts.push('AI-Enabled Customer Experience Strategist');
    } else if (hasAI) {
      parts.push('AI Innovation & Marketing Technology Leader');
    } else if (hasCX && hasOmnichannel) {
      parts.push('Omnichannel Customer Experience Leader');
    } else if (hasBrand && hasStrategy) {
      parts.push('Brand Strategy & Commercial Excellence Leader');
    } else if (hasBrand) {
      parts.push('Brand Management Leader');
    } else if (hasStrategy) {
      parts.push('Strategic Planning & Marketing Leader');
    } else if (hasCX) {
      parts.push('Customer Experience Strategist');
    } else if (hasOmnichannel && hasHCP) {
      parts.push('Omnichannel HCP Marketing Expert');
    } else if (hasMedia && hasHCP) {
      parts.push('HCP Media & Marketing Strategist');
    } else if (hasLeadership) {
      parts.push('Marketing Leadership Professional');
    } else {
      // Fallback: use top 2-3 checkbox labels (excluding therapeutic if already added)
      const remainingCheckboxes = therapeutic
        ? selectedCheckboxes.filter(cb => cb.id !== therapeutic.id)
        : selectedCheckboxes;
      const topLabels = remainingCheckboxes.slice(0, 2).map(cb => cb.label);
      parts.push(...topLabels, 'Specialist');
    }

    // Remove any duplicate words
    const uniqueParts = [];
    const seen = new Set();
    for (const part of parts) {
      const words = part.split(' ');
      if (!words.some(word => seen.has(word.toLowerCase()))) {
        uniqueParts.push(part);
        words.forEach(word => seen.add(word.toLowerCase()));
      }
    }

    return uniqueParts.join(' ');
  }

  /**
   * Generate dynamic tagline based on selected checkboxes
   * @param {Array} selectedCheckboxes - Array of selected checkbox objects
   * @returns {String} Dynamic tagline
   */
  static generateDynamicTagline(selectedCheckboxes) {
    if (!selectedCheckboxes || selectedCheckboxes.length === 0) {
      return 'Pharmaceutical marketing professional with comprehensive expertise';
    }

    const labels = selectedCheckboxes.map(cb => cb.label);

    if (labels.length <= 3) {
      return `Pharmaceutical marketing professional specializing in ${labels.join(', ')}`;
    } else {
      const first = labels.slice(0, 2).join(', ');
      const last = labels[labels.length - 1];
      return `Pharmaceutical marketing professional specializing in ${first}, and ${last}`;
    }
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

    return this.generateResumeFromTags(profile);
  }

  /**
   * Generate resume from a custom profile object (used for checkbox selections)
   */
  generateResumeFromTags(profile) {
    if (!profile || !profile.priority_tags) {
      throw new Error('Invalid profile object');
    }

    const maxBullets = 6; // Show top 6 relevant bullets for matching positions
    const fallbackBullets = 2; // Show 2 bullets for non-matching positions (career continuity)
    const maxProjects = 6; // Increased from 4
    const maxRoles = 10; // Show ALL roles, not just 3

    const filteredExp = this.filterExperience(profile.priority_tags, maxBullets, fallbackBullets);
    const filteredProjects = this.filterProjects(profile.priority_tags, maxProjects);
    const allSkills = this.getAllSkills();
    const topHighlights = this.getTopAchievements(profile.priority_tags, 5);

    // Generate dynamic headline and tagline for custom profiles
    const isCustomProfile = profile.id === 'custom' && profile.selectedCheckboxes;
    const dynamicHeadline = isCustomProfile
      ? ResumeBuilder.generateDynamicHeadline(profile.selectedCheckboxes, profile.selectedCategories)
      : profile.headline;
    const dynamicTagline = isCustomProfile
      ? ResumeBuilder.generateDynamicTagline(profile.selectedCheckboxes)
      : profile.tagline;

    return {
      profile: {
        id: profile.id,
        label: profile.label,
        headline: dynamicHeadline,
        tagline: dynamicTagline,
        description: profile.description,
        competencies: profile.competencies,
        focusSkills: profile.focus_skills,
        idealFor: profile.ideal_for || [],
        selectedCheckboxes: profile.selectedCheckboxes || [], // For dynamic headline generation
        selectedCategories: profile.selectedCategories || {} // For category analysis
      },
      personal: this.resumeData.personal,
      summary: this.resumeData.summary,
      experience: filteredExp.slice(0, maxRoles),
      projects: filteredProjects,
      topHighlights: topHighlights, // Top 5 scored achievements
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
    const focusSkills = profile.focusSkills || profile.focus_skills || [];
    const coreStrengths = focusSkills.length > 0
      ? focusSkills.slice(0, 3).join(' • ')
      : 'Strategic Planning, Brand Management, Commercial Excellence';

    return `
      <div class="resume-section">
        <h2 class="section-title">Executive Snapshot</h2>
        <div class="section-content">
          <p class="snapshot-tagline"><strong>${profile.tagline || 'Pharmaceutical Marketing Professional'}</strong></p>

          <p class="snapshot-description">${data.summary?.long || data.summary?.short || ''}</p>

          <p><strong>Core Strengths:</strong> ${coreStrengths}</p>
        </div>
      </div>
    `;
  }

  static renderTargetedHighlights(data) {
    const profile = data.profile;
    const isCustomProfile = profile.id === 'custom' && data.topHighlights && data.topHighlights.length > 0;

    // Custom profile: show top-scored achievements from resume data
    if (isCustomProfile) {
      const highlightsHtml = data.topHighlights.map(highlight => `
        <p class="highlight-item"><strong>•</strong> ${highlight.text}</p>
      `).join('');

      return `
        <div class="resume-section">
          <h2 class="section-title">Targeted Highlights</h2>
          <div class="section-content">
            <p style="margin-bottom: 1rem; font-style: italic; color: #666;">Key achievements matching your selected focus areas:</p>
            ${highlightsHtml}
          </div>
        </div>
      `;
    }

    // Quick select profile: show competencies and projects (original behavior)
    const projects = data.projects.slice(0, 3);
    const competencies = profile.competencies || [];

    return `
      <div class="resume-section">
        <h2 class="section-title">Targeted Highlights</h2>
        <div class="section-content">
          <p class="highlight-item"><strong>• Core Fit:</strong> ${competencies[0] || profile.description || 'Pharmaceutical marketing professional with comprehensive expertise'}</p>

          ${competencies.slice(1, 3).map(comp => `
            <p class="highlight-item"><strong>• Key Capability:</strong> ${comp}</p>
          `).join('')}

          ${projects.length > 0 ? `
            <p class="highlight-item"><strong>• Selected Projects:</strong> ${projects.map(p => p.name).join(', ')}${projects.length > 0 && projects[0].outcomes && projects[0].outcomes.length > 0 ? '. ' + projects[0].outcomes[0] : ''}</p>
          ` : ''}
        </div>
      </div>
    `;
  }

  static renderExperience(data) {
    const expHtml = data.experience.map(exp => `
      <div class="experience-item">
        <div class="experience-header">
          <div class="experience-title"><strong>${exp.title} — ${exp.company}</strong>${exp.companyParent ? ` (${exp.companyParent})` : ''}</div>
          <div class="experience-meta">${exp.location} | ${exp.startDate} – ${exp.endDate}</div>
        </div>
        <ul class="experience-bullets">
          ${exp.bullets.map(bullet => `
            <li>${bullet.text}</li>
          `).join('')}
        </ul>
      </div>
    `).join('');

    return `
      <div class="resume-section">
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
      <div class="resume-section">
        <h2 class="section-title">Skills</h2>
        <div class="section-content">
          ${skillsHtml}
        </div>
      </div>
    `;
  }

  static renderEducation(data) {
    const eduHtml = data.education.map(edu => `
      <p class="education-item">
        <strong>${edu.degree}</strong> ${edu.field ? `in ${edu.field}` : ''} — ${edu.institution}
      </p>
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
