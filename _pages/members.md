---
layout: page
permalink: /members/
title: members
description: Members of the Computer Systems Security Lab at Korea University.
nav: true
nav_order: 1
---

<style>
  .member-group { margin-top: 2rem; }
  .member-group h2 {
    border-bottom: 1px solid var(--global-divider-color);
    padding-bottom: 0.3rem;
    margin-bottom: 1.2rem;
  }
  .member-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 1.2rem;
  }
  .member-card {
    padding: 1rem 1.1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
  }
  .member-card .name {
    font-weight: 600;
    font-size: 1.05rem;
    margin-bottom: 0.15rem;
  }
  .member-card .cohort {
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    margin-bottom: 0.35rem;
  }
  .member-card .email {
    font-size: 0.85rem;
    font-family: var(--global-code-font-family, monospace);
    margin-bottom: 0.35rem;
    word-break: break-all;
  }
  .member-card .interests {
    font-size: 0.85rem;
    color: var(--global-text-color);
    line-height: 1.4;
  }
  .member-professor {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    padding: 1.2rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
  }
  .member-professor img {
    width: 140px;
    border-radius: 6px;
    flex-shrink: 0;
  }
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
        <div class="name" style="font-size: 1.25rem;">
          {% if p.website %}<a href="{{ p.website }}">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
        </div>
        <div style="color: var(--global-text-color-light); margin-bottom: 0.5rem;">{{ p.role }}</div>
        {% if p.email %}<div class="email">{{ p.email }} [at] korea.ac.kr</div>{% endif %}
        {% if p.interests %}<div class="interests"><strong>Research:</strong> {{ p.interests }}</div>{% endif %}
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
        <div class="name">{{ s.name }}</div>
        {% if s.cohort %}<div class="cohort">{{ s.cohort }} semester</div>{% endif %}
        {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
        {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
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
        <div class="name">{{ s.name }}</div>
        {% if s.cohort %}<div class="cohort">{{ s.cohort }} semester</div>{% endif %}
        {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
        {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
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
        <div class="name">{{ s.name }}</div>
        {% if s.email %}<div class="email">{{ s.email }} [at] korea.ac.kr</div>{% endif %}
        {% if s.interests %}<div class="interests">{{ s.interests }}</div>{% endif %}
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
        <div class="name">{{ s.name }}</div>
        {% if s.role %}<div class="cohort">{{ s.role }}</div>{% endif %}
      </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<!-- Alumni -->
{% if m.alumni and m.alumni.size > 0 %}
<div class="member-group">
  <h2>Alumni</h2>
  {% for a in m.alumni %}
    {% if a.note %}<p>{{ a.note }}</p>{% endif %}
  {% endfor %}
</div>
{% endif %}
