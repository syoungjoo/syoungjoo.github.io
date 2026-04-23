---
layout: page
permalink: /gallery/
title: gallery
nav: true
nav_order: 7
---

<style>
  .gal-event { margin: 2.2rem 0 2.8rem; }
  .gal-head {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 0.9rem;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid var(--global-divider-color);
  }
  .gal-head h3 {
    font-weight: 600;
    font-size: 1.15rem;
    margin: 0;
  }
  .gal-meta {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
  }
  .gal-meta .date { font-family: var(--global-code-font-family, monospace); }
  .gal-meta .dot { margin: 0 0.4rem; }

  .gal-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    gap: 0.6rem;
  }
  .gal-tile { flex: 0 1 324px; }
  .gal-tile {
    position: relative;
    aspect-ratio: 3 / 2;
    overflow: hidden;
    border-radius: 4px;
    background: var(--global-divider-color);
    cursor: zoom-in;
  }
  .gal-tile img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.25s ease;
  }
  .gal-tile:hover img { transform: scale(1.04); }

  .gal-empty {
    padding: 2rem;
    text-align: center;
    color: var(--global-text-color-light);
    border: 1px dashed var(--global-divider-color);
    border-radius: 6px;
  }
  .gal-empty code {
    background: var(--global-divider-color);
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
  }

  /* Lightbox */
  .gal-lightbox {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.9);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    cursor: zoom-out;
  }
  .gal-lightbox.open { display: flex; }
  .gal-lightbox img {
    max-width: 92vw;
    max-height: 92vh;
    object-fit: contain;
    border-radius: 4px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.6);
  }
  .gal-lightbox .nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    color: white;
    background: rgba(0,0,0,0.35);
    border: none;
    font-size: 2rem;
    padding: 0.4rem 0.9rem;
    cursor: pointer;
    border-radius: 4px;
  }
  .gal-lightbox .prev { left: 1.5rem; }
  .gal-lightbox .next { right: 1.5rem; }
  .gal-lightbox .close {
    position: absolute;
    top: 1rem;
    right: 1.2rem;
    color: white;
    background: none;
    border: none;
    font-size: 1.8rem;
    cursor: pointer;
  }
  .gal-lightbox .counter {
    position: absolute;
    bottom: 1rem;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 0.85rem;
    opacity: 0.75;
  }
</style>

{%- comment -%}
  Auto-discover events by scanning assets/img/gallery/<slug>/*.{jpg,png,...}
  Optional metadata: _data/gallery/<slug>.yml  (title / date / place / cover)
{%- endcomment -%}

{%- comment -%}
  Only count originals — al-folio auto-generates responsive .webp variants
  (-480/-800/-1400) that must be excluded from the gallery grid.
{%- endcomment -%}
{%- assign image_exts = "jpg,jpeg,png,gif,JPG,JPEG,PNG,GIF" | split: "," -%}
{%- assign gallery_files = site.static_files | where_exp: "f", "f.path contains '/assets/img/gallery/'" -%}

{%- comment -%} Build a comma-delimited blob of unique slugs {%- endcomment -%}
{%- assign slug_blob = "" -%}
{%- for f in gallery_files -%}
  {%- assign parts = f.path | split: '/' -%}
  {%- if parts.size >= 6 -%}
    {%- assign fname = parts[5] -%}
    {%- assign ext = fname | split: '.' | last -%}
    {%- if image_exts contains ext -%}
      {%- assign slug_blob = slug_blob | append: parts[4] | append: "," -%}
    {%- endif -%}
  {%- endif -%}
{%- endfor -%}
{%- assign slugs_raw = slug_blob | split: "," | uniq -%}

{%- comment -%} Build events list with a sortable key (date || slug), then sort desc {%- endcomment -%}
{%- assign ev_lines = "" -%}
{%- for slug in slugs_raw -%}
  {%- if slug == "" -%}{%- continue -%}{%- endif -%}
  {%- assign meta = site.data.gallery[slug] -%}
  {%- if meta.date -%}
    {%- assign sort_key = meta.date -%}
  {%- else -%}
    {%- assign sort_key = slug -%}
  {%- endif -%}
  {%- assign ev_lines = ev_lines | append: sort_key | append: "::" | append: slug | append: "|" -%}
{%- endfor -%}
{%- assign events_sorted = ev_lines | split: "|" | sort | reverse -%}

{%- assign rendered = 0 -%}
{%- for ev in events_sorted -%}
  {%- if ev == "" -%}{%- continue -%}{%- endif -%}
  {%- assign slug = ev | split: "::" | last -%}
  {%- assign meta = site.data.gallery[slug] -%}

  {%- comment -%} Defaults derived from slug if no meta {%- endcomment -%}
  {%- assign default_title = slug | replace: "-", " " | replace: "_", " " -%}
  {%- assign ev_title = meta.title | default: default_title -%}
  {%- assign ev_date = meta.date -%}
  {%- assign ev_place = meta.place -%}

  {%- comment -%} Collect photos for this slug, cover first {%- endcomment -%}
  {%- assign dir_path = "/assets/img/gallery/" | append: slug | append: "/" -%}
  {%- assign event_photos = gallery_files | where_exp: "f", "f.path contains dir_path" | sort: "path" -%}

  {%- assign valid_photos = "" -%}
  {%- for p in event_photos -%}
    {%- assign pname = p.path | split: '/' | last -%}
    {%- assign pext = pname | split: '.' | last -%}
    {%- if image_exts contains pext -%}
      {%- assign valid_photos = valid_photos | append: p.path | append: "|" -%}
    {%- endif -%}
  {%- endfor -%}
  {%- assign photo_paths = valid_photos | split: "|" -%}
  {%- if photo_paths.size == 0 -%}{%- continue -%}{%- endif -%}

  {%- assign rendered = rendered | plus: 1 -%}
<div class="gal-event">
  <div class="gal-head">
    <h3>{{ ev_title | markdownify | remove: '<p>' | remove: '</p>' }}</h3>
    <div class="gal-meta">
      {% if ev_date %}<span class="date">{{ ev_date | date: "%Y-%m" }}</span>{% endif %}
    </div>
  </div>
  <div class="gal-grid">
    {%- for path in photo_paths -%}
      {%- if path == "" -%}{%- continue -%}{%- endif -%}
      {%- assign fname = path | split: '/' | last -%}
      {%- if meta.cover and fname == meta.cover -%}{%- assign is_cover = true -%}{%- endif -%}
      <div class="gal-tile" data-full="{{ path | relative_url }}">
        <img src="{{ path | relative_url }}" alt="{{ ev_title }}" loading="lazy">
      </div>
    {%- endfor -%}
  </div>
</div>
{%- endfor -%}

{% if rendered == 0 %}
<div class="gal-empty">
  No photos yet. Drop images into <code>assets/img/gallery/&lt;event-slug&gt;/</code> and they'll appear here automatically.
  See <code>_data/gallery/README.md</code> for optional per-event metadata.
</div>
{% endif %}

<div class="gal-lightbox" id="gal-lightbox">
  <button class="close" aria-label="Close">×</button>
  <button class="nav prev" aria-label="Previous">‹</button>
  <img id="gal-lightbox-img" src="" alt="">
  <button class="nav next" aria-label="Next">›</button>
  <div class="counter" id="gal-counter"></div>
</div>

<script>
(function() {
  var lb = document.getElementById('gal-lightbox');
  var lbImg = document.getElementById('gal-lightbox-img');
  var counter = document.getElementById('gal-counter');
  var currentGroup = [];
  var currentIdx = 0;

  function open(group, idx) {
    currentGroup = group;
    currentIdx = idx;
    render();
    lb.classList.add('open');
  }
  function close() { lb.classList.remove('open'); }
  function step(delta) {
    currentIdx = (currentIdx + delta + currentGroup.length) % currentGroup.length;
    render();
  }
  function render() {
    lbImg.src = currentGroup[currentIdx];
    counter.textContent = (currentIdx + 1) + ' / ' + currentGroup.length;
  }

  document.querySelectorAll('.gal-grid').forEach(function(grid) {
    var tiles = Array.prototype.slice.call(grid.querySelectorAll('.gal-tile'));
    var urls = tiles.map(function(t) { return t.getAttribute('data-full'); });
    tiles.forEach(function(tile, i) {
      tile.addEventListener('click', function() { open(urls, i); });
    });
  });

  lb.addEventListener('click', function(e) {
    if (e.target === lb || e.target.classList.contains('close')) close();
    else if (e.target.classList.contains('prev')) { e.stopPropagation(); step(-1); }
    else if (e.target.classList.contains('next')) { e.stopPropagation(); step(1); }
  });
  document.addEventListener('keydown', function(e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });
})();
</script>
