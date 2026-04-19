---
layout: page
permalink: /members/
title: members
description: Members of the Computer Systems Security Lab at Korea University.
nav: true
nav_order: 1
---

<style>
  .member-group { margin-top: 2.2rem; }
  .member-group h2 {
    border-bottom: 1px solid var(--global-divider-color);
    padding-bottom: 0.3rem;
    margin-bottom: 1.2rem;
  }
  .member-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(155px, 1fr));
    gap: 1rem;
  }
  .member-card {
    padding: 0;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .member-card .photo {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    background: var(--global-divider-color);
  }
  .member-card .body { padding: 0.8rem 1rem 1rem; }
  .member-card .name {
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 0.15rem;
  }
  .member-card .cohort {
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    margin-bottom: 0.35rem;
  }
  .member-card .email {
    font-size: 0.8rem;
    font-family: var(--global-code-font-family, monospace);
    margin-bottom: 0.4rem;
    word-break: break-all;
  }
  .member-card .interests {
    font-size: 0.82rem;
    color: var(--global-text-color);
    line-height: 1.45;
  }
  .member-links {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
  }
  .member-links a {
    color: var(--global-text-color-light);
    font-size: 1rem;
    text-decoration: none;
    transition: color 0.15s ease;
  }
  .member-links a:hover {
    color: var(--global-theme-color, #b509ac);
  }
  .member-professor .member-links { margin-top: 0.6rem; font-size: 1.1rem; }
  .member-professor {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    padding: 1.2rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
  }
  .member-professor img {
    width: 170px;
    height: 170px;
    object-fit: cover;
    border-radius: 6px;
    flex-shrink: 0;
  }
  .alumni-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9rem;
  }
  .alumni-table th, .alumni-table td {
    padding: 0.5rem 0.7rem;
    text-align: left;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .alumni-table th { font-weight: 600; }
  @media (max-width: 576px) {
    .member-professor { flex-direction: column; align-items: center; text-align: center; }
  }
</style>

{% assign m = site.data.members %}

<!-- Professor -->
<div class="member-group">
  <h2>Professor</h2>
  {% for p in m.professor %}
    <div class="member-professor">
      {% if p.image %}
        <img src="{{ p.image | prepend: '/assets/img/' | relative_url }}" alt="{{ p.name }}">
      {% endif %}
      <div>
        <div style="font-weight: 600; font-size: 1.3rem; margin-bottom: 0.2rem;">
          {% if p.links.homepage %}<a href="{{ p.links.homepage }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
        </div>
        <div style="color: var(--global-text-color-light); margin-bottom: 0.5rem;">{{ p.role }}</div>
        {% if p.email %}<div style="font-family: var(--global-code-font-family, monospace); font-size: 0.9rem; margin-bottom: 0.5rem;">{{ p.email }} [at] korea.ac.kr</div>{% endif %}
        {% if p.interests %}<div><strong>Research:</strong> {{ p.interests }}</div>{% endif %}
        {% include member_links.liquid links=p.links %}
      </div>
    </div>
  {% endfor %}
</div>

<!-- Ph.D. Students -->
{% if m.phd and m.phd.size > 0 %}
<div class="member-group">
  <h2>Ph.D. Students</h2>
  <div class="member-grid">
    {% for s in m.phd %}
      <div class="member-card">
        {% if s.image %}<img class="photo" src="{{ s.image | prepend: '/assets/img/' | relative_url }}" alt="{{ s.name }}">{% endif %}
        <div class="body">
          <div class="name">
            {% if s.links.homepage %}<a href="{{ s.links.homepage }}">{{ s.name }}</a>{% else %}{{ s.name }}{% endif %}
          </div>
          {% if s.cohort %}<div class="cohort">{{ s.cohort }} semester</div>{% endif %}
          {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
          {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
          {% include member_links.liquid links=s.links %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<!-- M.S. Students -->
{% if m.ms and m.ms.size > 0 %}
<div class="member-group">
  <h2>M.S. Students</h2>
  <div class="member-grid">
    {% for s in m.ms %}
      <div class="member-card">
        {% if s.image %}<img class="photo" src="{{ s.image | prepend: '/assets/img/' | relative_url }}" alt="{{ s.name }}">{% endif %}
        <div class="body">
          <div class="name">
            {% if s.links.homepage %}<a href="{{ s.links.homepage }}">{{ s.name }}</a>{% else %}{{ s.name }}{% endif %}
          </div>
          {% if s.cohort %}<div class="cohort">{{ s.cohort }} semester</div>{% endif %}
          {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
          {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
          {% include member_links.liquid links=s.links %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<!-- Undergraduate Students -->
{% if m.undergrad and m.undergrad.size > 0 %}
<div class="member-group">
  <h2>Undergraduate Students</h2>
  <div class="member-grid">
    {% for s in m.undergrad %}
      <div class="member-card">
        {% if s.image %}<img class="photo" src="{{ s.image | prepend: '/assets/img/' | relative_url }}" alt="{{ s.name }}">{% endif %}
        <div class="body">
          <div class="name">
            {% if s.links.homepage %}<a href="{{ s.links.homepage }}">{{ s.name }}</a>{% else %}{{ s.name }}{% endif %}
          </div>
          {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
          {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
          {% include member_links.liquid links=s.links %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<!-- Staff -->
{% if m.staff and m.staff.size > 0 %}
<div class="member-group">
  <h2>Administrative Staff</h2>
  <div class="member-grid">
    {% for s in m.staff %}
      <div class="member-card">
        {% if s.image %}<img class="photo" src="{{ s.image | prepend: '/assets/img/' | relative_url }}" alt="{{ s.name }}">{% endif %}
        <div class="body">
          <div class="name">{{ s.name }}</div>
          {% if s.role %}<div class="cohort">{{ s.role }}</div>{% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<!-- Alumni -->
{% if m.alumni and m.alumni.size > 0 %}
<div class="member-group">
  <h2>Alumni</h2>
  <table class="alumni-table">
    <thead>
      <tr><th>Name</th><th>Degree / Cohort</th><th>Current Affiliation</th></tr>
    </thead>
    <tbody>
      {% for a in m.alumni %}
        <tr>
          <td>{{ a.name }}</td>
          <td>
            {% if a.degree %}{{ a.degree }}{% endif %}
            {% if a.cohort %} · {{ a.cohort }}{% endif %}
          </td>
          <td>{{ a.affiliation }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
{% endif %}
