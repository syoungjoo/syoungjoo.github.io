---
layout: page
permalink: /cves/
title: CVEs
nav: true
nav_order: 4
description: Vulnerabilities discovered and disclosed by members of the Computer Systems Security Lab.
---

<style>
  .cve-intro {
    font-size: 0.95rem;
    line-height: 1.6;
    margin-bottom: 1.6rem;
  }
  .cve-year {
    margin: 2rem 0 1rem;
    font-size: 1.2rem;
    font-weight: 600;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .cve-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
  }
  .cve-item {
    padding: 0.9rem 0;
    border-bottom: 1px dashed var(--global-divider-color);
    display: grid;
    grid-template-columns: 12rem 1fr;
    gap: 1rem;
  }
  .cve-item:last-child { border-bottom: none; }
  .cve-id {
    font-family: var(--global-code-font-family, monospace);
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--global-theme-color, #b509ac);
    padding-top: 0.15rem;
    word-break: break-all;
  }
  .cve-id a { color: inherit; text-decoration: none; }
  .cve-id a:hover { text-decoration: underline; }
  .cve-body .cve-title {
    font-weight: 600;
    font-size: 0.98rem;
    margin-bottom: 0.25rem;
  }
  .cve-body .cve-meta {
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    margin-bottom: 0.4rem;
  }
  .cve-body .cve-desc {
    font-size: 0.9rem;
    line-height: 1.55;
    margin: 0.25rem 0;
  }
  .cve-body .cve-pub {
    margin-top: 0.4rem;
    padding: 0.5rem 0.7rem;
    background: var(--global-card-bg-color, transparent);
    border-left: 3px solid var(--global-theme-color, #b509ac);
    border-radius: 3px;
    font-size: 0.85rem;
    line-height: 1.5;
  }
  .tag {
    display: inline-block;
    padding: 0.12rem 0.5rem;
    font-size: 0.72rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    margin-right: 0.3rem;
  }
  .tag.dos { color: #b36a00; }
  .tag.rce { color: #b30000; }
  .tag.cmd { color: #0057b3; }
  .tag.kbypass { color: #5f00b3; }

  @media (max-width: 600px) {
    .cve-item { grid-template-columns: 1fr; }
  }
</style>

{% assign c = site.data.cves %}

<div class="cve-intro">
  The following list summarizes software vulnerabilities that members of the
  Computer Systems Security Lab discovered and reported through
  <a href="https://cve.mitre.org/" target="_blank" rel="noopener">CVE</a> (global)
  and <a href="{{ c.kve_portal }}" target="_blank" rel="noopener">KVE</a>
  (Korea). Entries link to the corresponding advisory; where the finding was
  the basis for — or derived from — a lab publication, the related paper is
  highlighted below the description.
</div>

{% for g in c.groups %}
<h2 class="cve-year">{{ g.year }}</h2>
<ul class="cve-list">
  {% for e in g.items %}
    {% assign advisory_url = e.url | default: c.kve_portal %}
    {% assign tag_label = e.tag_label | default: e.tag | upcase %}
  <li class="cve-item">
    <div class="cve-id"><a href="{{ advisory_url }}" target="_blank" rel="noopener">{{ e.id }}</a></div>
    <div class="cve-body">
      <div class="cve-title">{{ e.title }}</div>
      <div class="cve-meta"><span class="tag {{ e.tag }}">{{ tag_label }}</span> Reporter: {{ e.reporter }}{% if e.category %} · {{ e.category }}{% endif %}</div>
      <div class="cve-desc">{{ e.desc | markdownify | remove: '<p>' | remove: '</p>' }}</div>
      {% if e.publication %}
        <div class="cve-pub">
          <strong>Related publication:</strong>
          {{ e.publication.text | markdownify | remove: '<p>' | remove: '</p>' }}
          {% for l in e.publication.links %}
            {% if l.relative %}
              <a href="{{ l.url | relative_url }}">{{ l.label }}</a>
            {% else %}
              <a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.label }}</a>
            {% endif %}
            {% unless forloop.last %} · {% endunless %}
          {% endfor %}
        </div>
      {% endif %}
    </div>
  </li>
  {% endfor %}
</ul>
{% endfor %}

<p style="margin-top: 2rem; font-size: 0.85rem; color: var(--global-text-color-light);">
  For KVE entries, the Korea Internet &amp; Security Agency (KISA) advisory
  portal is at
  <a href="{{ c.kve_portal }}" target="_blank" rel="noopener">knvd.krcert.or.kr</a>.
  Links above point to the canonical advisory when available; some recent
  CVE entries may still be in RESERVED status at the time of listing.
</p>
