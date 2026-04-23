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

  .prof-section {
    margin: 2rem 0;
  }
  .prof-section h2 {
    font-size: 1.15rem;
    font-weight: 600;
    margin: 0 0 0.8rem;
    padding-bottom: 0.35rem;
    border-bottom: 1px solid var(--global-divider-color);
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

<div class="prof-hero">
  <img src="{{ prof.image | prepend: '/assets/img/' | relative_url }}" alt="{{ prof.name }}">
  <div class="meta">
    <div class="name">{{ prof.name }}</div>
    <div class="role">Associate Professor</div>
    <div class="affil">
      <a href="{{ '/' | relative_url }}">Computer Systems Security Lab</a><br>
      <a href="https://security.korea.ac.kr">School of Cybersecurity</a>, Korea University
    </div>
    <div class="contact">
      <div><strong>Email:</strong> syoungjoo [at] korea.ac.kr</div>
      <div><strong>Phone:</strong> +82-2-3290-4884</div>
      <div><strong>Office:</strong> Jung Un-Oh IT Building (정운오IT교양관), Room 320</div>
    </div>
    {% include member_links.liquid links=prof.links %}
  </div>
</div>

<div class="prof-section">
  <h2>Biography</h2>
  <p>
    <strong>Youngjoo Shin</strong> is an Associate Professor in the
    <a href="https://security.korea.ac.kr">School of Cybersecurity</a> at
    Korea University, where he directs the Computer Systems Security Lab.
    His research investigates the security of modern computer systems — from CPU
    microarchitecture to operating systems, virtualization platforms, and cloud
    infrastructure — with a particular focus on side-channel and transient-execution
    attacks, OS kernel defenses, and practical privacy-preserving system design.
  </p>
  <p>
    Before joining Korea University in 2020, he was an Assistant Professor at
    Kwangwoon University (2017–2020), a Senior Researcher at the National Security
    Research Institute (2008–2017), and a Researcher at LG Electronics' Digital
    Media Laboratory (2007–2008).
  </p>
</div>

<div class="prof-section">
  <h2>Research Interests</h2>
  <div class="interest-tags">
    <span>System Security</span>
    <span>Microarchitectural Side-channel Attacks</span>
    <span>Transient Execution Attacks</span>
    <span>OS &amp; Hypervisor Security</span>
    <span>Cloud &amp; Container Security</span>
    <span>Network Security</span>
    <span>Applied Cryptography</span>
  </div>
</div>

<div class="prof-section">
  <h2>Education</h2>
  <ul class="prof-timeline">
    <li>
      <div class="period">Ph.D.</div>
      <div class="desc">Computer Science<div class="where">KAIST, Korea</div></div>
    </li>
    <li>
      <div class="period">M.S.</div>
      <div class="desc">Computer Science<div class="where">KAIST, Korea</div></div>
    </li>
    <li>
      <div class="period">B.S.</div>
      <div class="desc">Computer Science and Engineering<div class="where">Korea University, Korea</div></div>
    </li>
  </ul>
</div>

<div class="prof-section">
  <h2>Professional Experience</h2>
  <ul class="prof-timeline">
    <li>
      <div class="period">2022.3 – present</div>
      <div class="desc">Associate Professor<div class="where">School of Cybersecurity, Korea University</div></div>
    </li>
    <li>
      <div class="period">2020.9 – 2022.2</div>
      <div class="desc">Assistant Professor<div class="where">School of Cybersecurity, Korea University</div></div>
    </li>
    <li>
      <div class="period">2017.3 – 2020.8</div>
      <div class="desc">Assistant Professor<div class="where">Kwangwoon University</div></div>
    </li>
    <li>
      <div class="period">2008.4 – 2017.2</div>
      <div class="desc">Senior Researcher<div class="where">National Security Research Institute (NSR)</div></div>
    </li>
    <li>
      <div class="period">2007.11 – 2008.3</div>
      <div class="desc">Researcher<div class="where">Digital Media Laboratory, LG Electronics</div></div>
    </li>
    <li>
      <div class="period">2006.3 – 2007.12</div>
      <div class="desc">Research Assistant<div class="where">Mobile Multimedia Platform Center, KAIST</div></div>
    </li>
  </ul>
</div>

<div class="prof-section">
  <h2>Invited Talks &amp; Seminars</h2>
  <ul class="prof-timeline">
    <li><div class="period">2026</div><div class="desc">NetSec-KR 2026, IITP Special Session (invited talk)</div></li>
    <li><div class="period">2025</div><div class="desc">WDSC 2025 (invited lecture); Drone Cybersecurity Seminar; Unification &amp; Sharing Policy Research Seminar</div></li>
    <li><div class="period">2024</div><div class="desc">NetSec-KR 2024</div></li>
    <li><div class="period">2023</div><div class="desc">KAIST Colloquium; KSC 2023; ROK Navy Cybersecurity Seminar; WebAssembly Security Seminar</div></li>
    <li><div class="period">2022</div><div class="desc">Hansung University</div></li>
    <li><div class="period">2021</div><div class="desc">IEEE ICOIN 2021; NSR; Hansung University; Sejong University</div></li>
    <li><div class="period">2020</div><div class="desc">IEEE INFOCOM 2020; Side-Channel Analysis Workshop; NSR; Hoseo University; SeoulTech; Hansung University; Sejong University; Kookmin University</div></li>
    <li><div class="period">2019</div><div class="desc">KAIST; Korea University; SeoulTech; Sejong University; Hansung University; Kookmin University; WISC 2019; Side-Channel Analysis Workshop</div></li>
    <li><div class="period">2018</div><div class="desc">ACM CCS 2018; NetSec-KR 2018; KICS; ETRI; NSR; WISC 2018; Side-Channel Analysis Workshop; Sejong / Kookmin / Hansung / Hannam Universities</div></li>
    <li><div class="period">2017</div><div class="desc">KCC 2017; SDN/NFV Forum Security WG; NSR; Korea / Kookmin / Hansung Universities</div></li>
    <li><div class="period">2016</div><div class="desc">Research Briefing on Security-Equipment Analysis</div></li>
    <li><div class="period">2015</div><div class="desc">Best of the Best (BoB) Lecture</div></li>
  </ul>
</div>

<div class="prof-section">
  <h2>Professional Service &amp; External Expertise</h2>

  <h3 style="font-size: 0.95rem; font-weight: 600; margin: 1rem 0 0.5rem;">Government &amp; Public-Sector Advisory</h3>
  <ul>
    <li>IITP Preliminary Feasibility Study, <em>Intelligent Cyber-Shield Dome</em> Program — Subcommittee Member (2025–)</li>
    <li>Cloud Security Assurance Program (CSAP) Certification Committee (2023–2024)</li>
    <li>National Security Research Institute (NSR) &amp; Ministry of the Interior — Digital-Signature Advisory (2022)</li>
    <li>National Intelligence Service — Mid-/Long-Term Security Strategy Advisory (2019)</li>
    <li>IITP Preliminary Feasibility Study on Connected-Device Security — Committee Member (2017)</li>
  </ul>

  <h3 style="font-size: 0.95rem; font-weight: 600; margin: 1rem 0 0.5rem;">Peer Review &amp; Evaluation</h3>
  <ul>
    <li>Korea Data Agency (KoData) — KOSDAQ Technology Assessment Advisor, ICT Sector</li>
    <li>National Research Foundation of Korea — Research Grant Reviewer (2021)</li>
    <li>Korean Institute of Information Security &amp; Cryptology (KIISC) — Reviewer, including CISC-W 2020 and the KIISC Journal</li>
    <li>Korean Institute of Communications and Information Sciences (KICS) — Paper Reviewer (2018)</li>
    <li>National Cryptography Contest 2018 — Judge</li>
    <li>Korea Internet &amp; Security Agency (KISA) — Evaluation Committee Member (2017, 2018)</li>
  </ul>

  <h3 style="font-size: 0.95rem; font-weight: 600; margin: 1rem 0 0.5rem;">Program Committee</h3>
  <ul>
    <li><strong>2026:</strong> PST 2026; SECRYPT 2026; SecureComm 2026 (EAI); IFIP SEC 2026</li>
    <li><strong>2024:</strong> ICISC 2024; SmartSP 2024</li>
    <li><strong>2023:</strong> ICISC 2023</li>
    <li><strong>2022:</strong> WoNEXT 2022; CISC-W 2022</li>
    <li><strong>2020:</strong> KCS 2020</li>
    <li><strong>2018:</strong> Security 2018 (사이버보안 논문 공모전)</li>
  </ul>

  <h3 style="font-size: 0.95rem; font-weight: 600; margin: 1rem 0 0.5rem;">Standards, Guidelines &amp; Industry</h3>
  <ul>
    <li>Korea Association for Industrial Technology Security (KAITS) — Contribution/Advisory on <em>The Future of Sovereign Cloud</em></li>
    <li>KISA — Key-Management Guidelines Review Advisory</li>
    <li>IDEC — External Advisor (2024)</li>
    <li>LG U+ — Security Advisory (2019)</li>
    <li>KANI; SDN/NFV Forum Security Working Group (2017)</li>
  </ul>

  <h3 style="font-size: 0.95rem; font-weight: 600; margin: 1rem 0 0.5rem;">Academia</h3>
  <ul>
    <li>Kwangwoon University — Faculty Recruitment Review Committee (2024)</li>
    <li>Kookmin University — Faculty Review Committee (2018)</li>
  </ul>
</div>

<div class="prof-section">
  <h2>Publications</h2>
  <p>
    See the <a href="{{ '/publications/' | relative_url }}">publications page</a> for a full list,
    or browse external profiles:
    <a href="{{ prof.links.scholar }}" target="_blank" rel="noopener">Google Scholar</a>,
    <a href="https://dblp.org/pid/33/2332.html" target="_blank" rel="noopener">DBLP</a>.
  </p>
</div>