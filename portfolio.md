---
layout: page
title: Portfolio
permalink: /portfolio/
---

# Portfolio & Case Studies

Explore examples of my work across various marketing and advertising projects. Each case study demonstrates strategic thinking, creative execution, and measurable results.

---

<div class="portfolio-grid">
{% for item in site.portfolio %}
  <div class="portfolio-card">
    <h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
    <p class="portfolio-meta">{{ item.client }} | {{ item.industry }}</p>
    <p>{{ item.excerpt }}</p>
    <a href="{{ item.url | relative_url }}" class="read-more">View Case Study →</a>
  </div>
{% endfor %}
</div>

{% if site.portfolio.size == 0 %}
<div class="placeholder">
  <p><em>Portfolio case studies coming soon. Check back for examples of successful campaigns and projects.</em></p>
</div>
{% endif %}

---

## Work Categories

I've delivered successful projects across multiple areas:

- **Brand Campaigns** - Integrated campaigns that build awareness and drive engagement
- **Digital Marketing** - Data-driven digital strategies across channels
- **Content Marketing** - Strategic content that educates and converts
- **Social Media** - Community building and social engagement campaigns
- **Lead Generation** - B2B and B2C campaigns that drive qualified leads

Interested in learning more about a specific type of project? [Let's talk](/contact/).
