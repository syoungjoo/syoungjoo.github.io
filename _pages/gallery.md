---
layout: page
permalink: /gallery/
title: gallery
description: Lab life — retreats, conferences, and moments worth remembering.
nav: true
nav_order: 6
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
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 0.6rem;
  }
  .gal-tile {
    position: relative;
    aspect-ratio: 1 / 1;
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

{% assign events = site.data.gallery %}
{% for event in events %}
<div class="gal-event">
  <div class="gal-head">
    <h3>{{ event.title }}</h3>
    <div class="gal-meta">
      <span class="date">{{ event.date }}</span>
      {% if event.place %}<span class="dot">·</span>{{ event.place }}{% endif %}
    </div>
  </div>
  <div class="gal-grid" data-event="{{ event.slug }}">
    {% for photo in event.photos %}
      {% assign src = photo | prepend: '/assets/img/gallery/' | prepend: event.slug | prepend: '/assets/img/gallery/' %}
      {% capture path %}/assets/img/gallery/{{ event.slug }}/{{ photo }}{% endcapture %}
      <div class="gal-tile" data-full="{{ path | relative_url }}">
        <img src="{{ path | relative_url }}" alt="{{ event.title }}" loading="lazy">
      </div>
    {% endfor %}
  </div>
</div>
{% endfor %}

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
