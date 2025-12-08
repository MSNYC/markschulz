/**
 * Interactive Resume Initializer
 * Handles data loading, user interactions, and resume generation
 */

(function() {
  'use strict';

  let resumeBuilder = null;
  let currentResume = null;
  let currentProfileId = 'brand_management';

  /**
   * Load JSON data files
   */
  async function loadData() {
    try {
      const [resumeResponse, profilesResponse] = await Promise.all([
        fetch('/assets/data/resume.json'),
        fetch('/assets/data/resume_profiles.json')
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

  /**
   * Initialize the resume builder
   */
  async function init() {
    const data = await loadData();
    if (!data) return;

    resumeBuilder = new ResumeBuilder(data.resumeData, data.profilesData);

    // Set up event listeners
    setupEventListeners();

    // Check URL parameters for profile selection
    const urlParams = new URLSearchParams(window.location.search);
    const profileParam = urlParams.get('profile');
    if (profileParam) {
      const profileCard = document.querySelector(`input[value="${profileParam}"]`);
      if (profileCard) {
        profileCard.checked = true;
        currentProfileId = profileParam;
        // Auto-generate if profile is in URL
        setTimeout(() => generateResume(), 500);
      }
    }
  }

  /**
   * Set up all event listeners
   */
  function setupEventListeners() {
    // Generate button
    const generateBtn = document.getElementById('generateBtn');
    generateBtn.addEventListener('click', generateResume);

    // Profile selection
    const profileInputs = document.querySelectorAll('input[name="profile"]');
    profileInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        currentProfileId = e.target.value;
        updateURL();
      });
    });

    // Action buttons
    document.getElementById('downloadPdfBtn').addEventListener('click', downloadPDF);
    document.getElementById('emailBtn').addEventListener('click', emailResume);
    document.getElementById('copyLinkBtn').addEventListener('click', copyLink);
    document.getElementById('regenerateBtn').addEventListener('click', scrollToTop);
  }

  /**
   * Generate resume based on selected profile
   */
  function generateResume() {
    if (!resumeBuilder) {
      showError('Resume builder not initialized');
      return;
    }

    try {
      // Show loading state
      const generateBtn = document.getElementById('generateBtn');
      const originalText = generateBtn.querySelector('.btn-text').textContent;
      generateBtn.querySelector('.btn-text').textContent = 'Generating...';
      generateBtn.disabled = true;

      // Generate resume
      currentResume = resumeBuilder.generateResume(currentProfileId);

      // Render resume
      const resumeContent = document.getElementById('resumeContent');
      resumeContent.innerHTML = ResumeRenderer.render(currentResume);

      // Update stats
      updateStats(currentResume);

      // Show preview
      const preview = document.getElementById('resumePreview');
      preview.style.display = 'block';

      // Scroll to preview
      setTimeout(() => {
        preview.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);

      // Reset button
      setTimeout(() => {
        generateBtn.querySelector('.btn-text').textContent = originalText;
        generateBtn.disabled = false;
      }, 500);

    } catch (error) {
      console.error('Error generating resume:', error);
      showError('Failed to generate resume. Please try again.');
    }
  }

  /**
   * Update stats display
   */
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

  /**
   * Download resume as PDF
   */
  function downloadPDF() {
    if (!currentResume) return;

    // Simple print dialog (most reliable cross-browser)
    window.print();

    // Alternative: Use html2pdf.js if loaded
    /*
    if (typeof html2pdf !== 'undefined') {
      const element = document.getElementById('resumeContent');
      const opt = {
        margin: 0.5,
        filename: `MarkSchulz_Resume_${currentProfileId}.pdf`,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
      };
      html2pdf().set(opt).from(element).save();
    } else {
      window.print();
    }
    */
  }

  /**
   * Email resume
   */
  function emailResume() {
    if (!currentResume) return;

    const profile = currentResume.profile;
    const subject = encodeURIComponent(`Mark Schulz Resume - ${profile.label}`);
    const body = encodeURIComponent(
      `Hi,\n\nI've generated a tailored resume for Mark Schulz focused on ${profile.label}.\n\n` +
      `View it here: ${window.location.origin}/resume-interactive/?profile=${currentProfileId}\n\n` +
      `Profile highlights:\n${profile.competencies.slice(0, 2).map(c => `• ${c}`).join('\n')}\n\n` +
      `Best regards`
    );

    window.location.href = `mailto:?subject=${subject}&body=${body}`;
  }

  /**
   * Copy shareable link
   */
  function copyLink() {
    const url = `${window.location.origin}/resume-interactive/?profile=${currentProfileId}`;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(() => {
        showSuccess('Link copied to clipboard!');
      }).catch(err => {
        console.error('Failed to copy:', err);
        fallbackCopyLink(url);
      });
    } else {
      fallbackCopyLink(url);
    }
  }

  /**
   * Fallback copy method for older browsers
   */
  function fallbackCopyLink(url) {
    const textArea = document.createElement('textarea');
    textArea.value = url;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.select();

    try {
      document.execCommand('copy');
      showSuccess('Link copied to clipboard!');
    } catch (err) {
      console.error('Fallback copy failed:', err);
      prompt('Copy this link:', url);
    }

    document.body.removeChild(textArea);
  }

  /**
   * Update URL with profile parameter
   */
  function updateURL() {
    const url = new URL(window.location);
    url.searchParams.set('profile', currentProfileId);
    window.history.pushState({}, '', url);
  }

  /**
   * Scroll to top of page
   */
  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /**
   * Show error message
   */
  function showError(message) {
    alert('Error: ' + message);
    // TODO: Replace with nicer toast notification
  }

  /**
   * Show success message
   */
  function showSuccess(message) {
    // Simple temporary notification
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
