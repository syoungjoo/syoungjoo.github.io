---
layout: page
permalink: /deadlines/
title: deadlines
description: Upcoming submission deadlines for security, privacy, and cryptography venues.
nav: true
nav_order: 6
---

<style>
  .dl-note {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    margin: 0 0 1.2rem;
  }
  .dl-filters {
    display: flex;
    gap: 1.2rem;
    flex-wrap: wrap;
    align-items: center;
    padding: 0.8rem 1rem;
    margin-bottom: 1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
  }
  .dl-filters .group { display: flex; gap: 0.8rem; flex-wrap: wrap; align-items: center; }
  .dl-filters label {
    font-size: 0.85rem;
    font-weight: normal;
    margin: 0;
    cursor: pointer;
    user-select: none;
  }
  .dl-filters input[type="checkbox"] { margin-right: 0.25rem; vertical-align: middle; }
  .dl-filters .sep { width: 1px; height: 1.3rem; background: var(--global-divider-color); }

  .dl-list { margin: 0; padding: 0; list-style: none; }
  .dl-entry {
    display: grid;
    grid-template-columns: 1.4fr 1.3fr 1.1fr 0.9fr;
    gap: 1rem;
    align-items: center;
    padding: 0.9rem 1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    margin-bottom: 0.6rem;
    background: var(--global-card-bg-color, transparent);
  }
  .dl-entry.past { opacity: 0.45; }
  .dl-conf .name { font-weight: 600; font-size: 1rem; }
  .dl-conf .desc {
    font-size: 0.8rem;
    color: var(--global-text-color-light);
    line-height: 1.4;
  }
  .dl-deadline .time {
    font-family: var(--global-code-font-family, monospace);
    font-size: 0.88rem;
  }
  .dl-deadline .comment {
    font-size: 0.75rem;
    color: var(--global-text-color-light);
    margin-top: 0.15rem;
  }
  .dl-countdown {
    font-weight: 600;
    font-size: 0.95rem;
    text-align: center;
  }
  .dl-countdown.urgent { color: #d93a3a; }
  .dl-countdown.soon   { color: #d9a13a; }
  .dl-countdown.past   { color: var(--global-text-color-light); font-weight: normal; }
  .dl-place {
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    line-height: 1.4;
  }
  .dl-place .date { font-weight: 500; color: var(--global-text-color); }

  @media (max-width: 768px) {
    .dl-entry { grid-template-columns: 1fr; gap: 0.3rem; }
    .dl-countdown { text-align: left; }
  }

  .dl-tag {
    display: inline-block;
    font-size: 0.68rem;
    padding: 0.1rem 0.4rem;
    border-radius: 3px;
    background: var(--global-divider-color);
    color: var(--global-text-color);
    margin-right: 0.3rem;
    vertical-align: middle;
  }
  .dl-tag.top4  { background: #b509ac; color: white; }
  .dl-tag.astar { background: #2a7be4; color: white; }
  .dl-tag.a     { background: #5aa469; color: white; }

  .dl-empty {
    text-align: center;
    padding: 2rem;
    color: var(--global-text-color-light);
    border: 1px dashed var(--global-divider-color);
    border-radius: 6px;
  }
</style>

<p class="dl-note">
  Countdowns are computed in your local timezone. Deadlines are typically given in <strong>AoE (Anywhere on Earth, UTC−12)</strong> — the timer below reflects that. Data adapted from
  <a href="https://sec-deadlines.github.io/" target="_blank" rel="noopener">sec-deadlines.github.io</a> (MIT licensed).
  {% if site.data.conferences_meta.last_updated %}<br>Last updated: {{ site.data.conferences_meta.last_updated }}.{% endif %}
</p>

<div class="dl-filters">
  <div class="group">
    <strong style="font-size: 0.85rem;">Topic:</strong>
    <label><input type="checkbox" class="flt" data-tag="SEC" checked> Security</label>
    <label><input type="checkbox" class="flt" data-tag="PRIV" checked> Privacy</label>
    <label><input type="checkbox" class="flt" data-tag="CRYPTO"> Crypto</label>
  </div>
  <div class="sep"></div>
  <div class="group">
    <strong style="font-size: 0.85rem;">Type:</strong>
    <label><input type="checkbox" class="flt" data-tag="CONF" checked> Conferences</label>
    <label><input type="checkbox" class="flt" data-tag="SHOP"> Workshops</label>
    <label><input type="checkbox" class="flt" data-tag="JRN"> Journals</label>
  </div>
  <div class="sep"></div>
  <div class="group">
    <strong style="font-size: 0.85rem;">Tier:</strong>
    <label><input type="checkbox" class="flt" data-tag="TOP4"> Top-4</label>
    <label><input type="checkbox" class="flt" data-tag="ASTAR"> A*</label>
    <label><input type="checkbox" class="flt" data-tag="CORE-A"> A</label>
    <label><input type="checkbox" class="flt" data-tag="CORE-B"> B</label>
  </div>
  <div class="sep"></div>
  <div class="group">
    <label><input type="checkbox" id="hide-past" checked> Hide past deadlines</label>
  </div>
</div>

<ul class="dl-list" id="dl-list">
{%- assign confs = site.data.conferences -%}
{%- for conf in confs -%}
  {%- if conf.deadline -%}
    {%- for dl in conf.deadline -%}
      {%- assign tags = conf.tags | join: ' ' -%}
      <li class="dl-entry" data-tags="{{ tags }}" data-deadline="{{ dl }}">
        <div class="dl-conf">
          <div class="name">
            <a href="{{ conf.link }}" target="_blank" rel="noopener">{{ conf.name }} {{ conf.year }}</a>
            {% if conf.tags contains 'TOP4' %}<span class="dl-tag top4">Top-4</span>{% elsif conf.tags contains 'ASTAR' %}<span class="dl-tag astar">A*</span>{% elsif conf.tags contains 'CORE-A' %}<span class="dl-tag a">A</span>{% endif %}
          </div>
          <div class="desc">{{ conf.description }}</div>
        </div>
        <div class="dl-deadline">
          <div class="time">{{ dl }}</div>
          {% if conf.comment %}<div class="comment">{{ conf.comment }}</div>{% endif %}
        </div>
        <div class="dl-countdown" data-deadline="{{ dl }}">—</div>
        <div class="dl-place">
          {% if conf.date %}<div class="date">{{ conf.date | replace: '-', '–' }}</div>{% endif %}
          {% if conf.place %}<div>{{ conf.place }}</div>{% endif %}
        </div>
      </li>
    {%- endfor -%}
  {%- endif -%}
{%- endfor -%}
</ul>

<div id="dl-empty" class="dl-empty" style="display:none;">No deadlines match the selected filters.</div>

<script>
(function() {
  var entries = Array.prototype.slice.call(document.querySelectorAll('#dl-list .dl-entry'));

  function parseAoe(str) {
    // "YYYY-MM-DD HH:MM" — treat as AoE (UTC-12).
    var m = str.match(/^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})$/);
    if (!m) return null;
    var utc = Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4], +m[5]);
    return new Date(utc + 12 * 3600 * 1000);
  }

  function fmtCountdown(deltaMs) {
    if (deltaMs <= 0) return { text: 'passed', cls: 'past' };
    var s = Math.floor(deltaMs / 1000);
    var d = Math.floor(s / 86400); s -= d * 86400;
    var h = Math.floor(s / 3600);  s -= h * 3600;
    var m = Math.floor(s / 60);
    var cls = '';
    if (d < 7) cls = 'urgent';
    else if (d < 30) cls = 'soon';
    var text;
    if (d > 0) text = d + 'd ' + h + 'h';
    else if (h > 0) text = h + 'h ' + m + 'm';
    else text = m + 'm';
    return { text: text + ' left', cls: cls };
  }

  entries.forEach(function(el) {
    var dl = parseAoe(el.getAttribute('data-deadline'));
    el._deadline = dl;
  });

  // Sort by soonest future deadline first, then past at the end.
  var now = Date.now();
  entries.sort(function(a, b) {
    var ad = a._deadline ? a._deadline.getTime() : Infinity;
    var bd = b._deadline ? b._deadline.getTime() : Infinity;
    var aFuture = ad >= now, bFuture = bd >= now;
    if (aFuture !== bFuture) return aFuture ? -1 : 1;
    return ad - bd;
  });
  var list = document.getElementById('dl-list');
  entries.forEach(function(el) { list.appendChild(el); });

  function tick() {
    var now = Date.now();
    entries.forEach(function(el) {
      var cd = el.querySelector('.dl-countdown');
      if (!el._deadline) { cd.textContent = 'TBA'; return; }
      var info = fmtCountdown(el._deadline.getTime() - now);
      cd.textContent = info.text;
      cd.className = 'dl-countdown ' + info.cls;
      if (info.cls === 'past') el.classList.add('past'); else el.classList.remove('past');
    });
  }
  tick();
  setInterval(tick, 60 * 1000);

  // Filtering
  var filters = Array.prototype.slice.call(document.querySelectorAll('.flt'));
  var hidePast = document.getElementById('hide-past');

  function apply() {
    var topics = filters.filter(function(f){return f.checked && ['SEC','PRIV','CRYPTO'].indexOf(f.dataset.tag)>=0;}).map(function(f){return f.dataset.tag;});
    var types  = filters.filter(function(f){return f.checked && ['CONF','SHOP','JRN'].indexOf(f.dataset.tag)>=0;}).map(function(f){return f.dataset.tag;});
    var tiers  = filters.filter(function(f){return f.checked && ['TOP4','ASTAR','CORE-A','CORE-B'].indexOf(f.dataset.tag)>=0;}).map(function(f){return f.dataset.tag;});
    var nowMs = Date.now();
    var shown = 0;
    entries.forEach(function(el) {
      var tags = (el.getAttribute('data-tags') || '').split(/\s+/);
      var okTopic = topics.length === 0 || topics.some(function(t){return tags.indexOf(t)>=0;});
      var okType  = types.length  === 0 || types.some(function(t){return tags.indexOf(t)>=0;});
      var okTier  = tiers.length  === 0 || tiers.some(function(t){return tags.indexOf(t)>=0;});
      var okPast  = !hidePast.checked || (el._deadline && el._deadline.getTime() >= nowMs);
      var show = okTopic && okType && okTier && okPast;
      el.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    document.getElementById('dl-empty').style.display = shown === 0 ? '' : 'none';
  }
  filters.forEach(function(f) { f.addEventListener('change', apply); });
  hidePast.addEventListener('change', apply);
  apply();
})();
</script>
