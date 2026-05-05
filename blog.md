---
layout: page
title: Blog
permalink: /blog/
---

<p class="blog-intro">Exploring interesting topics in modelling materials.</p>

{% if site.posts.size == 0 %}
<p>No posts yet. Add a file such as <code>_posts/2026-05-15-my-topic.md</code>.</p>
{% else %}
<ul class="post-list">
  {% for post in site.posts %}
  <li class="post-list-item">
    <span class="post-list-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h2 class="post-list-title"><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h2>
    <div class="post-list-excerpt">{{ post.excerpt | strip_html | normalize_whitespace | truncatewords: 45 }}</div>
  </li>
  {% endfor %}
</ul>
{% endif %}
