---
layout: page
permalink: /members/professor/
title: Prof. Youngjoo Shin
nav: false
---

<style>
  .prof-hero {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
    padding: 1.6rem 0 1.8rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2rem;
  }
  .prof-hero img {
    width: 200px;
    height: 300px;
    object-fit: cover;
    object-position: center top;
    border-radius: 6px;
    flex-shrink: 0;
  }
  .prof-hero .meta { flex: 1; }
  .prof-hero .name {
    font-weight: 600;
    font-size: 1.6rem;
    margin: 0 0 0.3rem;
  }
  .prof-hero .role {
    color: var(--global-text-color-light);
    margin-bottom: 0.8rem;
  }
  .prof-hero .affil {
    font-size: 0.95rem;
    line-height: 1.55;
    margin-bottom: 0.9rem;
  }
  .prof-hero .contact {
    font-size: 0.9rem;
    font-family: var(--global-code-font-family, monospace);
    line-height: 1.7;
  }
  .prof-hero .member-links { margin-top: 0.8rem; font-size: 1.15rem; }

  .prof-section { margin: 2rem 0; }
  .prof-section h2 {
    font-size: 1.15rem;
    font-weight: 600;
    margin: 0 0 0.8rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .prof-section h3 {
    font-size: 0.95rem;
    font-weight: 600;
    margin: 1rem 0 0.5rem;
  }
  .prof-timeline {
    list-style: none;
    padding-left: 0;
    margin: 0;
  }
  .prof-timeline li {
    display: flex;
    gap: 1rem;
    padding: 0.5rem 0;
    border-bottom: 1px dashed var(--global-divider-color);
    font-size: 0.93rem;
    line-height: 1.5;
  }
  .prof-timeline li:last-child { border-bottom: none; }
  .prof-timeline .period {
    flex: 0 0 11rem;
    font-family: var(--global-code-font-family, monospace);
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    padding-top: 0.1rem;
  }
  .prof-timeline .desc { flex: 1; }
  .prof-timeline .desc .where {
    color: var(--global-text-color-light);
    font-size: 0.88rem;
  }

  .interest-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.5rem;
  }
  .interest-tags span {
    padding: 0.25rem 0.7rem;
    font-size: 0.85rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    background: var(--global-card-bg-color, transparent);
  }

  @media (max-width: 576px) {
    .prof-hero { flex-direction: column; align-items: center; text-align: center; }
    .prof-timeline li { flex-direction: column; gap: 0.1rem; }
    .prof-timeline .period { flex: none; }
  }
</style>

{% assign prof = site.data.members.professor[0] %}
{% assign p = site.data.professor %}

<div class="prof-hero">
  <img src="{{ prof.image | prepend: '/assets/img/' | relative_url }}" alt="{{ prof.name }}">
  <div class="meta">
    <div class="name">{{ prof.name }}</div>
    <div class="role">{{ p.role_title }}</div>
    <div class="affil">
      <a href="{{ p.affiliation.lab.url | relative_url }}">{{ p.affiliation.lab.name }}</a><br>
      <a href="{{ p.affiliation.school.url }}">{{ p.affiliation.school.name }}</a>, {{ p.affiliation.university }}
    </div>
    <div class="contact">
      <div><strong>Email:</strong> {{ p.contact.email_local }} [at] {{ p.contact.email_domain }}</div>
      <div><strong>Phone:</strong> {{ p.contact.phone }}</div>
      <div><strong>Office:</strong> {{ p.contact.office }}</div>
    </div>
    {% include member_links.liquid links=prof.links %}
  </div>
</div>

<div class="prof-section">
  <h2>Biography</h2>
  {{ p.biography | markdownify }}
</div>

<div class="prof-section">
  <h2>Research Interests</h2>
  <div class="interest-tags">
    {% for t in p.interests %}<span>{{ t }}</span>{% endfor %}
  </div>
</div>

<div class="prof-section">
  <h2>Education</h2>
  <ul class="prof-timeline">
    {% for e in p.education %}
      <li><div class="period">{{ e.period }}</div>
          <div class="desc">{{ e.desc }}<div class="where">{{ e.where }}</div></div></li>
    {% endfor %}
  </ul>
</div>

<div class="prof-section">
  <h2>Professional Experience</h2>
  <ul class="prof-timeline">
    {% for e in p.experience %}
      <li><div class="period">{{ e.period }}</div>
          <div class="desc">{{ e.desc }}<div class="where">{{ e.where }}</div></div></li>
    {% endfor %}
  </ul>
</div>

<div class="prof-section">
  <h2>Invited Talks &amp; Seminars</h2>
  <ul class="prof-timeline">
    {% for y in p.invited_talks %}
      <li><div class="period">{{ y.year }}</div>
          <div class="desc">{{ y.items | join: "; " }}</div></li>
    {% endfor %}
  </ul>
</div>

<div class="prof-section">
  <h2>Professional Service &amp; External Expertise</h2>
  {% for s in p.service %}
    <h3>{{ s.heading }}</h3>
    <ul>
      {% for it in s.items %}<li>{{ it | markdownify | remove: '<p>' | remove: '</p>' }}</li>{% endfor %}
    </ul>
  {% endfor %}
</div>

<div class="prof-section">
  <h2>Publications</h2>
  <p>
    See the <a href="{{ '/publications/' | relative_url }}">publications page</a> for a full list,
    or browse external profiles:
    <a href="{{ prof.links.scholar }}" target="_blank" rel="noopener">Google Scholar</a>,
    <a href="{{ p.dblp_url }}" target="_blank" rel="noopener">DBLP</a>.
  </p>
</div>
