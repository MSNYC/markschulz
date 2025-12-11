/**
 * Google Analytics 4 Event Tracking
 * Tracks user interactions with the interactive resume
 */

(function() {
  'use strict';

  // Helper function to safely send GA4 events
  function trackEvent(eventName, eventParams) {
    try {
      if (typeof gtag === 'function') {
        gtag('event', eventName, eventParams);
        console.log('GA4 Event:', eventName, eventParams);
      }
    } catch (error) {
      console.error('GA4 tracking error:', error);
      // Fail silently - don't break site functionality
    }
  }

  // Wait for DOM to be ready
  function initTracking() {

    // Track Quick Select clicks (3 pre-built resume links)
    try {
      const quickSelectLinks = document.querySelectorAll('.profile-card');
      quickSelectLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
          const profileTitle = this.querySelector('h4') ? this.querySelector('h4').textContent : 'Unknown';
          trackEvent('quick_select_click', {
            'profile_type': profileTitle,
            'event_category': 'Resume Generation',
            'event_label': 'Quick Select'
          });
        });
      });
    } catch (error) {
      console.error('Error setting up Quick Select tracking:', error);
    }

    // Track Custom Select generation button
    try {
      const generateBtn = document.getElementById('generateCustomBtn');
      if (generateBtn) {
        generateBtn.addEventListener('click', function() {
          // Get selected checkboxes
          const selectedCheckboxes = document.querySelectorAll('#checkboxCategories input[type="checkbox"]:checked');
          const selectedTags = Array.from(selectedCheckboxes).map(function(cb) {
            return cb.value || cb.id;
          });

          trackEvent('custom_resume_generate', {
            'selected_tags': selectedTags.join(', '),
            'tag_count': selectedTags.length,
            'event_category': 'Resume Generation',
            'event_label': 'Custom Select'
          });
        });
      }
    } catch (error) {
      console.error('Error setting up Custom Select tracking:', error);
    }

    // Track method selection (Quick vs Custom radio buttons)
    try {
      const methodRadios = document.querySelectorAll('input[name="method"]');
      methodRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
          if (this.checked) {
            trackEvent('method_selected', {
              'method_type': this.value, // 'quick' or 'custom'
              'event_category': 'User Flow',
              'event_label': 'Method Selection'
            });
          }
        });
      });
    } catch (error) {
      console.error('Error setting up method selection tracking:', error);
    }

    // Track LinkedIn clicks from navigation
    try {
      const linkedinLinks = document.querySelectorAll('a[href*="linkedin.com"]');
      linkedinLinks.forEach(function(link) {
        link.addEventListener('click', function() {
          const location = this.classList.contains('linkedin-icon') ? 'Navigation' :
                          this.closest('#contact') ? 'Contact Section' : 'Other';
          trackEvent('linkedin_click', {
            'link_location': location,
            'event_category': 'Engagement',
            'event_label': 'LinkedIn Profile'
          });
        });
      });
    } catch (error) {
      console.error('Error setting up LinkedIn tracking:', error);
    }

    // Track "Continue" button clicks (section navigation)
    try {
      const continueButtons = document.querySelectorAll('a[href^="#"]');
      continueButtons.forEach(function(btn) {
        // Only track the styled continue buttons, not all anchor links
        if (btn.textContent.includes('↓') || btn.textContent.includes('START HERE')) {
          btn.addEventListener('click', function() {
            const targetSection = this.getAttribute('href').replace('#', '');
            const buttonText = this.querySelector('span') ? this.querySelector('span').textContent : this.textContent;

            trackEvent('continue_button_click', {
              'target_section': targetSection,
              'button_text': buttonText.replace('↓', '').trim(),
              'event_category': 'User Flow',
              'event_label': 'Section Navigation'
            });
          });
        }
      });
    } catch (error) {
      console.error('Error setting up continue button tracking:', error);
    }

    // Track contact form submissions
    try {
      const contactForm = document.querySelector('.contact-form');
      if (contactForm) {
        contactForm.addEventListener('submit', function() {
          trackEvent('contact_form_submit', {
            'event_category': 'Conversion',
            'event_label': 'Contact Form'
          });
        });
      }
    } catch (error) {
      console.error('Error setting up form tracking:', error);
    }

  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTracking);
  } else {
    initTracking();
  }

})();
