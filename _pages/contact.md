---
layout: page
permalink: /contact/
title: contact
nav: true
nav_order: 7
---

<style>
  .contact-card {
    margin-top: 1.5rem;
    padding: 1.4rem 1.6rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
  }
  .contact-row {
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    padding: 0.6rem 0;
    font-size: 0.93rem;
    line-height: 1.55;
    border-bottom: 1px dashed var(--global-divider-color);
  }
  .contact-row:last-child { border-bottom: none; }
  .contact-row .ico {
    width: 1.4rem;
    text-align: center;
    color: var(--global-theme-color, #b509ac);
    font-size: 1rem;
    padding-top: 0.15rem;
    flex-shrink: 0;
  }
  .contact-row .label {
    font-weight: 600;
    width: 5.5rem;
    flex-shrink: 0;
    color: var(--global-text-color-light);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    padding-top: 0.25rem;
  }
  .contact-row .val { flex: 1; }
  .contact-row .val .sub {
    display: block;
    font-size: 0.82rem;
    color: var(--global-text-color-light);
    margin-top: 0.15rem;
  }

  .directions {
    margin-top: 1.8rem;
    padding: 1.2rem 1.4rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
  }
  .directions h3 {
    font-size: 1rem;
    font-weight: 600;
    margin: 0 0 0.7rem;
  }
  .directions ul { margin: 0; padding-left: 1.2rem; font-size: 0.9rem; line-height: 1.7; }
  .directions li { margin-bottom: 0.25rem; }
  .directions li strong { color: var(--global-theme-color, #b509ac); }
</style>

<div class="contact-card">
  <div class="contact-row">
    <span class="ico"><i class="fa-solid fa-building"></i></span>
    <span class="label">Lab</span>
    <span class="val">
      Computer Systems Security Lab
      <span class="sub">School of Cybersecurity, Korea University</span>
    </span>
  </div>

  <div class="contact-row">
    <span class="ico"><i class="fa-solid fa-location-dot"></i></span>
    <span class="label">Office</span>
    <span class="val">
      Robot Convergence Bld., Room 212
      <span class="sub">145 Anam-ro, Seongbuk-gu, Seoul 02841, Republic of Korea</span>
      <span class="sub" lang="ko">서울특별시 성북구 안암로 145 고려대학교 로봇융합관 212호</span>
    </span>
  </div>

  <div class="contact-row">
    <span class="ico"><i class="fa-solid fa-envelope"></i></span>
    <span class="label">Email</span>
    <span class="val">
      syoungjoo [at] korea.ac.kr
      <span class="sub">General inquiries &amp; prospective students — contact Prof. Youngjoo Shin</span>
    </span>
  </div>

  <div class="contact-row">
    <span class="ico"><i class="fa-solid fa-phone"></i></span>
    <span class="label">Phone</span>
    <span class="val">
      +82-2-3290-XXXX
      <span class="sub">Office hours: Mon–Fri, 10:00–18:00 (KST)</span>
    </span>
  </div>

  <div class="contact-row">
    <span class="ico"><i class="fa-solid fa-globe"></i></span>
    <span class="label">Web</span>
    <span class="val">
      <a href="https://sites.google.com/view/youngjoo-shin/" target="_blank" rel="noopener">sites.google.com/view/youngjoo-shin</a>
    </span>
  </div>
</div>

<div class="directions">
  <h3>How to Find Us</h3>
  <ul>
    <li><strong>Subway</strong> — Line 6 <em>Korea Univ. Station</em> (Exit 1 or 3), about 10 min walk to Robot Convergence Building.</li>
    <li><strong>Bus</strong> — Green buses 1017, 1018, 7211; Blue bus 273 stop at <em>Korea Univ. Anam Hospital</em>.</li>
    <li><strong>By car</strong> — Enter through the main gate on Anam-ro; visitor parking is available in front of the Engineering Complex.</li>
    <li><strong>On campus</strong> — Robot Convergence Building (로봇융합관) is located near the Engineering Quad. Head to Room 212 on the 2nd floor.</li>
  </ul>
</div>
