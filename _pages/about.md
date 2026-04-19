---
layout: about
title: home
permalink: /
subtitle: <strong>Computer Systems Security Lab</strong> · School of Cybersecurity, Korea University

profile:
  align: right
  image:
  image_circular: false
  more_info:

selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<style>
  .hero {
    display: flex;
    align-items: center;
    gap: 2.5rem;
    padding: 2rem 0 2.5rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2.5rem;
  }
  .hero-logo img { max-height: 110px; width: auto; }
  .hero-text { flex: 1; }
  .hero-text h2 {
    font-weight: 600;
    font-size: 1.6rem;
    margin: 0 0 0.6rem;
    border: none;
  }
  .hero-text p { margin: 0 0 0.8rem; line-height: 1.6; }
  .hero-cta a {
    display: inline-block;
    padding: 0.45rem 1rem;
    border: 1px solid var(--global-theme-color);
    border-radius: 4px;
    font-size: 0.9rem;
    text-decoration: none;
    margin-right: 0.5rem;
  }
  .hero-cta a:hover { background: var(--global-theme-color); color: white; }

  .section-head {
    font-weight: 600;
    font-size: 1.25rem;
    margin: 2.5rem 0 1rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--global-divider-color);
  }

  .research-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1rem;
  }
  .research-card {
    padding: 1rem 1.1rem;
    border: 1px solid var(--global-divider-color);
    border-radius: 6px;
    background: var(--global-card-bg-color, transparent);
  }
  .research-card .icon {
    font-size: 1.4rem;
    color: var(--global-theme-color);
    margin-bottom: 0.5rem;
  }
  .research-card h4 {
    font-size: 0.98rem;
    font-weight: 600;
    margin: 0 0 0.35rem;
  }
  .research-card p {
    font-size: 0.85rem;
    line-height: 1.45;
    color: var(--global-text-color-light);
    margin: 0;
  }

  .twocol {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 2rem;
  }
  @media (max-width: 768px) {
    .hero { flex-direction: column; text-align: center; }
    .twocol { grid-template-columns: 1fr; }
  }

  .site-footer-block {
    margin: 3rem 0 1rem;
    padding-top: 2rem;
    border-top: 1px solid var(--global-divider-color);
    text-align: center;
  }
  .site-footer-block .logos {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
    margin-bottom: 1.2rem;
  }
  .site-footer-block .logos img { max-height: 60px; width: auto; }
  .site-footer-block .address {
    color: var(--global-text-color-light);
    font-size: 0.9rem;
    line-height: 1.6;
  }
</style>

<!-- HERO -->
<section class="hero">
  <div class="hero-logo">
    <img src="{{ '/assets/img/site/lab_logo.png' | relative_url }}" alt="CSL">
  </div>
  <div class="hero-text">
    <h2>Security of computer systems, from the microarchitecture to the cloud.</h2>
    <p>
      The <strong>Computer Systems Security Lab (CSS Lab)</strong> at
      <a href="https://korea.ac.kr">Korea University</a> is led by
      Prof. <a href="mailto:syoungjoo@korea.ac.kr">Youngjoo Shin</a> and based in the
      <a href="https://cybersecurity.korea.ac.kr">School of Cybersecurity</a>.
      We investigate how modern systems — from CPUs and GPUs to kernels, containers,
      and cloud fabrics — leak information or fail under adversarial conditions, and
      we design practical defenses against those failures.
    </p>
    <div class="hero-cta">
      <a href="{{ '/research/' | relative_url }}">Research</a>
      <a href="{{ '/publications/' | relative_url }}">Publications</a>
      <a href="{{ '/members/' | relative_url }}">Members</a>
    </div>
  </div>
</section>

<!-- RESEARCH AREAS -->
<div class="section-head">Research Areas</div>

<div class="research-grid">
  <div class="research-card">
    <div class="icon"><i class="fa-solid fa-microchip"></i></div>
    <h4>Microarchitectural Attacks</h4>
    <p>Side channels and transient execution on CPUs, GPUs, and TEEs (SGX / TDX, Apple Silicon).</p>
  </div>
  <div class="research-card">
    <div class="icon"><i class="fa-solid fa-shield-halved"></i></div>
    <h4>System Security</h4>
    <p>OS kernel defenses, system-call filtering, and secure execution.</p>
  </div>
  <div class="research-card">
    <div class="icon"><i class="fa-solid fa-cloud"></i></div>
    <h4>Cloud &amp; Container Security</h4>
    <p>Isolation and denial-of-service resilience in container/Kubernetes stacks.</p>
  </div>
  <div class="research-card">
    <div class="icon"><i class="fa-solid fa-network-wired"></i></div>
    <h4>Network Security</h4>
    <p>TLS, DNS, and network-function security in real deployments.</p>
  </div>
  <div class="research-card">
    <div class="icon"><i class="fa-solid fa-bug"></i></div>
    <h4>Binary Analysis &amp; Fuzzing</h4>
    <p>Static and dynamic program analysis for vulnerability discovery.</p>
  </div>
</div>

<!-- NEWS + SELECTED PUBLICATIONS -->
<div class="twocol">
  <div>
    <div class="section-head"><a href="{{ '/news/' | relative_url }}" style="color: inherit;">News</a></div>
    {% include news.liquid limit=true %}
  </div>
  <div>
    <div class="section-head"><a href="{{ '/publications/' | relative_url }}" style="color: inherit;">Selected Publications</a></div>
    {% include selected_papers.liquid %}
  </div>
</div>

<!-- JOIN US -->
<div class="section-head">Join Us</div>

**We are always looking for motivated students** interested in systems security.
If you are a Korea University undergraduate curious about research, or a prospective graduate
applicant, please reach out to Prof. Shin by email.

<!-- FOOTER LOGOS + ADDRESS -->
<div class="site-footer-block">
  <div class="logos">
    <img src="{{ '/assets/img/site/lab_logo.png' | relative_url }}" alt="Computer Systems Security Lab">
    <img src="{{ '/assets/img/site/ku_logo.png' | relative_url }}" alt="Korea University">
  </div>
  <div class="address">
    <strong>Robot Convergence Bld. Office 212</strong><br>
    145 Anam-ro, Seongbuk-gu, Seoul 02841, Korea
  </div>
</div>
