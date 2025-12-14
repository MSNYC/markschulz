/**
 * Interactive Resume Initializer
 * Handles data loading, user interactions, and resume generation
 */

// Early scroll restoration - run IMMEDIATELY to prevent flash
(function() {
  // Check for both custom and quick select states
  const customState = sessionStorage.getItem('customResumeState');
  const quickState = sessionStorage.getItem('quickSelectState');

  const savedState = customState || quickState;

  if (savedState) {
    try {
      const state = JSON.parse(savedState);
      if (state.scrollPosition) {
        window.scrollTo(0, state.scrollPosition);
      }
    } catch (e) {
      // Silently fail
    }
  }
})();

(function() {
  'use strict';

  let resumeBuilder = null;
  let currentResume = null;
  let currentProfileId = 'brand_management';
  let customBuilderData = null;
  let selectedCheckboxes = [];
  let selectionMethod = 'quick'; // 'quick' or 'custom'

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
    customBuilderData = data.profilesData.custom_builder;

    // Set up event listeners
    setupEventListeners();

    // Initialize checkbox UI if custom builder is enabled
    if (customBuilderData && customBuilderData.enabled) {
      initializeCheckboxes();

      // Check if we're returning from a custom resume (restore state)
      const savedState = sessionStorage.getItem('customResumeState');
      if (savedState) {
        try {
          const state = JSON.parse(savedState);

          // Restore checkbox selections
          if (state.selectedCheckboxes && state.selectedCheckboxes.length > 0) {
            selectedCheckboxes = state.selectedCheckboxes;

            // Switch to custom select view
            selectionMethod = 'custom';
            const customRadio = document.querySelector('input[value="custom"]');
            if (customRadio) {
              customRadio.checked = true;
            }
            // Toggle the panels to show custom select
            toggleSelectionPanels();
            updateMethodCardStyles();

            // Re-check the checkboxes in the DOM
            state.selectedCheckboxes.forEach(checkboxId => {
              const checkbox = document.getElementById(`checkbox_${checkboxId}`);
              if (checkbox) {
                checkbox.checked = true;
                const item = checkbox.closest('.checkbox-item');
                if (item) item.classList.add('checked');
              }
            });

            // Update the counter and button state
            updateCheckboxCount();
            validateCustomSelection();

            // Restore scroll position immediately (no animation)
            window.scrollTo(0, state.scrollPosition);
          }

          // Clear the saved state so it doesn't persist
          sessionStorage.removeItem('customResumeState');
        } catch (e) {
          console.error('Error restoring state:', e);
          resetCustomSelections();
        }
      } else {
        // No saved state - reset as normal
        resetCustomSelections();
      }
    }

    // Check if we're returning from a Quick Select resume (restore state)
    const quickState = sessionStorage.getItem('quickSelectState');
    if (quickState) {
      try {
        const state = JSON.parse(quickState);

        // Restore Quick Select view
        if (state.viewMode === 'quick') {
          selectionMethod = 'quick';
          const quickRadio = document.querySelector('input[value="quick"]');
          if (quickRadio) {
            quickRadio.checked = true;
          }
          toggleSelectionPanels();
          updateMethodCardStyles();

          // Restore scroll position
          window.scrollTo(0, state.scrollPosition);
        }

        // Clear the saved state
        sessionStorage.removeItem('quickSelectState');
      } catch (e) {
        console.error('Error restoring quick select state:', e);
      }
    }

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
   * Reset all custom selections (checkboxes and state)
   */
  function resetCustomSelections() {
    // Clear the selected checkboxes array
    selectedCheckboxes = [];

    // Uncheck all checkbox inputs in the DOM (if they exist)
    const allCheckboxes = document.querySelectorAll('.checkbox-item input[type="checkbox"]');
    allCheckboxes.forEach(checkbox => {
      checkbox.checked = false;
    });

    // Remove 'checked' class from all checkbox items (if they exist)
    const allCheckboxItems = document.querySelectorAll('.checkbox-item');
    allCheckboxItems.forEach(item => {
      item.classList.remove('checked');
    });

    // Reset the selection count display (if element exists)
    const countSpan = document.getElementById('selectionCount');
    if (countSpan) {
      countSpan.textContent = '(0 of 3 selected)';
    }

    // Disable the generate button (if it exists)
    const generateBtn = document.getElementById('generateCustomBtn');
    if (generateBtn && customBuilderData) {
      const min = customBuilderData.min_selections || 1;
      generateBtn.disabled = true;
    }
  }

  /**
   * Set up all event listeners
   */
  function setupEventListeners() {
    // Method selector (Quick vs Custom)
    const methodInputs = document.querySelectorAll('input[name="method"]');
    methodInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        selectionMethod = e.target.value;
        toggleSelectionPanels();
        updateMethodCardStyles();
      });
    });

    // Quick Select - Generate button
    const generateBtn = document.getElementById('generateBtn');
    if (generateBtn) {
      generateBtn.addEventListener('click', generateResume);
    }

    // Custom Select - Generate button
    const generateCustomBtn = document.getElementById('generateCustomBtn');
    if (generateCustomBtn) {
      generateCustomBtn.addEventListener('click', generateCustomResume);
    }

    // Profile selection (Quick Select)
    const profileInputs = document.querySelectorAll('input[name="profile"]');
    profileInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        currentProfileId = e.target.value;
        updateURL();
      });
    });

    // Quick Select profile cards - save state when clicked
    const profileCards = document.querySelectorAll('.profile-card');
    profileCards.forEach(card => {
      card.addEventListener('click', (e) => {
        // Save state before navigating to quick select resume
        sessionStorage.setItem('quickSelectState', JSON.stringify({
          scrollPosition: window.scrollY,
          viewMode: 'quick',
          profileId: card.href.split('/').filter(Boolean).pop() // Extract profile ID from URL
        }));
      });
    });

    // Action buttons (may not exist until resume is generated)
    const downloadBtn = document.getElementById('downloadPdfBtn');
    if (downloadBtn) downloadBtn.addEventListener('click', downloadPDF);

    const emailBtn = document.getElementById('emailBtn');
    if (emailBtn) emailBtn.addEventListener('click', emailResume);

    const copyLinkBtn = document.getElementById('copyLinkBtn');
    if (copyLinkBtn) copyLinkBtn.addEventListener('click', copyLink);

    const regenerateBtn = document.getElementById('regenerateBtn');
    if (regenerateBtn) regenerateBtn.addEventListener('click', scrollToTop);
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
    if (!statsDiv) return; // Stats div is optional

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
      `View it here: ${window.location.origin}/?profile=${currentProfileId}\n\n` +
      `Profile highlights:\n${profile.competencies.slice(0, 2).map(c => `• ${c}`).join('\n')}\n\n` +
      `Best regards`
    );

    window.location.href = `mailto:?subject=${subject}&body=${body}`;
  }

  /**
   * Copy shareable link
   */
  function copyLink() {
    const url = `${window.location.origin}/?profile=${currentProfileId}`;

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

  /**
   * Toggle between Quick Select and Custom Select panels
   */
  function toggleSelectionPanels() {
    const quickPanel = document.getElementById('quickSelectPanel');
    const customPanel = document.getElementById('customSelectPanel');

    if (selectionMethod === 'quick') {
      quickPanel.style.display = 'block';
      customPanel.style.display = 'none';
    } else {
      quickPanel.style.display = 'none';
      customPanel.style.display = 'block';
    }
  }

  /**
   * Update active state on method cards
   */
  function updateMethodCardStyles() {
    const methodCards = document.querySelectorAll('.method-card');
    methodCards.forEach(card => {
      const method = card.getAttribute('data-method');
      if (method === selectionMethod) {
        card.classList.add('active');
      } else {
        card.classList.remove('active');
      }
    });
  }

  /**
   * Initialize checkbox UI from custom_builder data
   */
  function initializeCheckboxes() {
    console.log('initializeCheckboxes called', {
      customBuilderData: customBuilderData,
      hasCategories: customBuilderData?.checkbox_categories?.length
    });

    if (!customBuilderData || !customBuilderData.checkbox_categories) {
      console.error('No custom builder data or categories found');
      return;
    }

    const container = document.getElementById('checkboxCategories');
    if (!container) {
      console.error('checkboxCategories container not found');
      return;
    }

    console.log('Building checkboxes...');

    customBuilderData.checkbox_categories.forEach(category => {
      const categoryDiv = document.createElement('div');
      categoryDiv.className = 'checkbox-category';

      // Category header
      const header = document.createElement('div');
      header.className = 'category-header';
      header.innerHTML = `
        <span class="category-icon">${category.icon}</span>
        <h3 class="category-title">${category.category}</h3>
      `;
      categoryDiv.appendChild(header);

      // Checkbox grid
      const grid = document.createElement('div');
      grid.className = 'checkbox-grid';

      category.checkboxes.forEach(checkbox => {
        const item = document.createElement('label');
        item.className = 'checkbox-item';
        item.setAttribute('data-checkbox-id', checkbox.id);

        const input = document.createElement('input');
        input.type = 'checkbox';
        input.id = `checkbox_${checkbox.id}`;
        input.value = checkbox.id;
        input.addEventListener('change', handleCheckboxChange);

        const labelWrapper = document.createElement('div');
        labelWrapper.className = 'checkbox-label-wrapper';
        labelWrapper.innerHTML = `
          <span class="checkbox-label">${checkbox.label}</span>
          <p class="checkbox-description">${checkbox.description}</p>
        `;

        item.appendChild(input);
        item.appendChild(labelWrapper);
        grid.appendChild(item);
      });

      categoryDiv.appendChild(grid);
      container.appendChild(categoryDiv);
    });
  }

  /**
   * Handle checkbox selection changes
   */
  function handleCheckboxChange(e) {
    const checkboxId = e.target.value;
    const item = e.target.closest('.checkbox-item');

    if (e.target.checked) {
      selectedCheckboxes.push(checkboxId);
      item.classList.add('checked');
    } else {
      selectedCheckboxes = selectedCheckboxes.filter(id => id !== checkboxId);
      item.classList.remove('checked');
    }

    updateCheckboxCount();
    validateCustomSelection();
  }

  /**
   * Update checkbox selection count display
   */
  function updateCheckboxCount() {
    const countSpan = document.getElementById('selectionCount');
    if (countSpan) {
      countSpan.textContent = `(${selectedCheckboxes.length} of 3 selected)`;
    }
  }

  /**
   * Validate custom selection and enable/disable generate button
   */
  function validateCustomSelection() {
    const generateBtn = document.getElementById('generateCustomBtn');
    if (!generateBtn) return;

    const min = customBuilderData.min_selections || 1;
    const max = customBuilderData.max_selections || 8;
    const count = selectedCheckboxes.length;

    // Enable/disable button
    generateBtn.disabled = count < min || count > max;

    // Show/hide validation message
    let validationMsg = document.getElementById('customValidationMsg');

    if (count > max) {
      // Too many selections - show warning
      if (!validationMsg) {
        validationMsg = document.createElement('div');
        validationMsg.id = 'customValidationMsg';
        validationMsg.style.cssText = `
          margin-top: 0.75rem;
          padding: 0.75rem 1rem;
          background: rgba(255, 107, 107, 0.1);
          border: 1px solid rgba(255, 107, 107, 0.3);
          border-radius: 8px;
          color: #ff6b6b;
          font-size: 0.875rem;
          line-height: 1.5;
        `;
        generateBtn.parentElement.appendChild(validationMsg);
      }
      validationMsg.innerHTML = `
        <strong>⚠️ Too many selections</strong><br>
        Please select ${max} or fewer focus areas (currently ${count} selected)
      `;
    } else if (count < min) {
      // Too few selections - show info
      if (!validationMsg) {
        validationMsg = document.createElement('div');
        validationMsg.id = 'customValidationMsg';
        validationMsg.style.cssText = `
          margin-top: 0.75rem;
          padding: 0.75rem 1rem;
          background: rgba(0, 240, 255, 0.1);
          border: 1px solid rgba(0, 240, 255, 0.3);
          border-radius: 8px;
          color: #00F0FF;
          font-size: 0.875rem;
          line-height: 1.5;
        `;
        generateBtn.parentElement.appendChild(validationMsg);
      }
      validationMsg.innerHTML = `
        <strong>ℹ️ Select focus areas</strong><br>
        Choose at least ${min} focus area${min > 1 ? 's' : ''} to generate your custom resume
      `;
    } else {
      // Valid selection - remove message if it exists
      if (validationMsg) {
        validationMsg.remove();
      }
    }
  }

  /**
   * Show loading overlay with sparkle effect
   */
  function showLoadingOverlay(onComplete) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'resume-loading-overlay';

    const content = document.createElement('div');
    content.className = 'loading-content';

    const icon = document.createElement('div');
    icon.className = 'loading-icon';
    icon.textContent = '✨';

    const text = document.createElement('div');
    text.className = 'loading-text';
    text.textContent = 'Tailoring your resume...';

    const subtext = document.createElement('div');
    subtext.className = 'loading-subtext';
    subtext.textContent = '';

    content.appendChild(icon);
    content.appendChild(text);
    content.appendChild(subtext);
    overlay.appendChild(content);
    document.body.appendChild(overlay);

    // Stage 1: Tailoring (0-700ms)
    setTimeout(() => {
      text.textContent = 'Filtering experience...';
    }, 700);

    // Stage 2: Filtering (700-1500ms)
    setTimeout(() => {
      icon.textContent = '✅';
      icon.classList.add('done');
      text.textContent = 'Done!';
      subtext.textContent = 'Loading your custom resume...';
    }, 1500);

    // Stage 3: Complete (1500-2500ms, then callback)
    setTimeout(() => {
      onComplete();
    }, 2500);
  }

  /**
   * Generate custom resume based on checkbox selections
   */
  function generateCustomResume() {
    if (!resumeBuilder || selectedCheckboxes.length === 0) {
      showError('Please select at least one focus area');
      return;
    }

    try {
      // Collect all tags from selected checkboxes
      const selectedTags = [];
      customBuilderData.checkbox_categories.forEach(category => {
        category.checkboxes.forEach(checkbox => {
          if (selectedCheckboxes.includes(checkbox.id)) {
            selectedTags.push(...checkbox.tags);
          }
        });
      });

      // Save state before navigating (so we can restore when they come back)
      sessionStorage.setItem('customResumeState', JSON.stringify({
        selectedCheckboxes: selectedCheckboxes,
        scrollPosition: window.scrollY,
        viewMode: 'custom'
      }));

      // Show sparkle loading effect, then redirect
      showLoadingOverlay(() => {
        const tagsParam = selectedTags.join(',');
        window.location.href = `resume/custom/?tags=${encodeURIComponent(tagsParam)}`;
      });

    } catch (error) {
      console.error('Error generating custom resume:', error);
      showError('Failed to generate custom resume. Please try again.');

      // Reset button on error
      const generateBtn = document.getElementById('generateCustomBtn');
      if (generateBtn) {
        generateBtn.querySelector('.btn-text').textContent = 'Generate Custom Resume';
        generateBtn.disabled = false;
      }
    }
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

  // Handle browser back/forward cache (bfcache)
  // Reset selections when page is restored from cache
  window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
      // Page was loaded from bfcache (user hit back button)
      console.log('Page restored from cache, resetting selections...');
      resetCustomSelections();
    }
  });

})();

