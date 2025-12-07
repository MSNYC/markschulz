---
layout: page
title: Blog
permalink: /blog/
---

# Marketing Insights & Thoughts

Perspectives on marketing strategy, advertising trends, and what's working in the industry today.

---

<div class="blog-posts">
{% for post in site.posts %}
  <article class="blog-post-preview">
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="post-meta">{{ post.date | date: "%B %-d, %Y" }}</p>
    <p>{{ post.excerpt }}</p>
    <a href="{{ post.url | relative_url }}" class="read-more">Read more →</a>
  </article>
{% endfor %}
</div>

{% if site.posts.size == 0 %}
<div class="placeholder">
  <p><em>Blog posts coming soon. Subscribe to the <a href="{{ "/feed.xml" | relative_url }}">RSS feed</a> to be notified of new articles.</em></p>
</div>
{% endif %}

---

## Subscribe

Stay updated with new articles via [RSS feed]({{ "/feed.xml" | relative_url }}) - perfect for setting up automated LinkedIn cross-posting with tools like Zapier or Buffer.
