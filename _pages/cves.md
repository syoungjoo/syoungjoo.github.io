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

<div class="cve-intro">
  The following list summarizes software vulnerabilities that members of the
  Computer Systems Security Lab discovered and reported through
  <a href="https://cve.mitre.org/" target="_blank" rel="noopener">CVE</a> (global)
  and <a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE</a>
  (Korea). Entries link to the corresponding advisory; where the finding was
  the basis for — or derived from — a lab publication, the related paper is
  highlighted below the description.
</div>

<!-- =============== 2025 =============== -->
<h2 class="cve-year">2025</h2>
<ul class="cve-list">

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2025-0470</a></div>
    <div class="cve-body">
      <div class="cve-title">Remote Code Execution in AhnLab V3 Lite</div>
      <div class="cve-meta"><span class="tag rce">RCE</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Remote code execution vulnerability identified in AhnLab V3 Lite, a
        consumer anti-malware product widely deployed in Korea. Reported to
        the vendor and coordinated through KrCERT/CC.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2025-0471</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in AhnLab V3 Lite</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service flaw in AhnLab V3 Lite enabling a local attacker to
        crash or disable the anti-malware agent.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2025-0472</a></div>
    <div class="cve-body">
      <div class="cve-title">Remote Code Execution in AhnLab V3 Lite</div>
      <div class="cve-meta"><span class="tag rce">RCE</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Second RCE primitive affecting AhnLab V3 Lite, distinct from
        KVE-2025-0470. Disclosed in coordination with the vendor.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2025-0473</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in SGA EPS Virus Chaser</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service vulnerability in SGA Solutions' EPS Virus Chaser
        endpoint protection product that allows the security service to be
        terminated or left in an inconsistent state.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-45856" target="_blank" rel="noopener">CVE-2025-45856</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in CatchPulse Pro</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service flaw in the CatchPulse Pro endpoint security product
        (formerly SecureAge APEX) allowing a local attacker to disable the
        protection driver.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-51620" target="_blank" rel="noopener">CVE-2025-51620</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in IObit Malware Fighter</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service vulnerability in IObit Malware Fighter that
        terminates or destabilizes the security agent's kernel-mode driver.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-55456" target="_blank" rel="noopener">CVE-2025-55456</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in iTop Easy Desktop</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Flaw in iTop Easy Desktop that can be abused to crash the
        application's helper service, leading to denial of service.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-55457" target="_blank" rel="noopener">CVE-2025-55457</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in iTop VPN</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service vulnerability in the iTop VPN client that allows an
        attacker to terminate the service from an unprivileged context.
      </div>
    </div>
  </li>

</ul>

<!-- =============== 2024 =============== -->
<h2 class="cve-year">2024</h2>
<ul class="cve-list">

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-54531" target="_blank" rel="noopener">CVE-2024-54531</a></div>
    <div class="cve-body">
      <div class="cve-title">KASLR Bypass in macOS for Apple Silicon</div>
      <div class="cve-meta"><span class="tag kbypass">KASLR Bypass</span> Reporter: Hyerean Jang · Kernel / microarchitecture</div>
      <div class="cve-desc">
        A memory-handling issue in macOS Sequoia (&lt; 15.2) that allows an
        application to bypass kernel address space layout randomization
        (KASLR). The flaw was reported to Apple and mitigated in macOS
        Sequoia 15.2 through improved memory handling. CVSS 5.5.
      </div>
      <div class="cve-pub">
        <strong>Related publication:</strong>
        Hyerean Jang, Taehun Kim, Youngjoo Shin.
        <em>"SysBumps: Exploiting Speculative Execution in System Calls for
        Breaking KASLR in macOS for Apple Silicon."</em>
        ACM CCS 2024 — also presented at Black Hat Europe 2024.
        <a href="{{ '/publications/' | relative_url }}">[lab publications]</a>
        · <a href="https://github.com/koreacsl/SysBumps" target="_blank" rel="noopener">[code]</a>
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-37027" target="_blank" rel="noopener">CVE-2024-37027</a></div>
    <div class="cve-body">
      <div class="cve-title">Improper Input Validation in Intel Developer Toolkits</div>
      <div class="cve-meta"><span class="tag rce">Local DoS / RCE</span> Reporter: Chanhee Park · Driver / toolchain</div>
      <div class="cve-desc">
        Improper input validation affecting Intel VTune Profiler
        (&lt; 2024.2.0), Intel OneAPI Base Toolkit (&lt; 2024.2), and Intel
        System Bring-Up Toolkit (&lt; 2024.2.0), which may allow an
        authenticated local user to trigger denial of service through the
        underlying Intel driver.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-42634" target="_blank" rel="noopener">CVE-2024-42634</a></div>
    <div class="cve-body">
      <div class="cve-title">Command Injection in Tenda AC9 (formWriteFacMac)</div>
      <div class="cve-meta"><span class="tag cmd">Command Injection</span> Reporter: Dongsoo Kim · Binary analysis</div>
      <div class="cve-desc">
        Command-injection flaw in the <code>formWriteFacMac</code> handler of
        the <code>httpd</code> binary in Tenda AC9 firmware 15.03.06.42.
        Remote attackers can execute OS commands with root privileges.
        CVSS 8.8 (High).
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-42633" target="_blank" rel="noopener">CVE-2024-42633</a></div>
    <div class="cve-body">
      <div class="cve-title">Command Injection in Linksys E1500 (do_upgrade_post)</div>
      <div class="cve-meta"><span class="tag cmd">Command Injection</span> Reporter: Dongsoo Kim · Binary analysis</div>
      <div class="cve-desc">
        Command-injection vulnerability in the <code>do_upgrade_post</code>
        function of the <code>httpd</code> binary in Linksys E1500 firmware
        1.0.06.001. An authenticated attacker can execute OS commands with
        root privileges. CVSS 8.8 (High).
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-25468" target="_blank" rel="noopener">CVE-2024-25468</a></div>
    <div class="cve-body">
      <div class="cve-title">Command Injection in TOTOLINK X5000R (NTPSyncWithHost)</div>
      <div class="cve-meta"><span class="tag cmd">Command Injection</span> Reporter: Taeho Kim · Binary analysis</div>
      <div class="cve-desc">
        Command-injection vulnerability in the <code>NTPSyncWithHost</code>
        component of TOTOLINK X5000R firmware 9.1.0u.6369_B20230113. A remote
        attacker can inject shell commands through the <code>host_time</code>
        parameter. CVSS 7.5 (High).
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-2024-22651" target="_blank" rel="noopener">CVE-2024-22651</a></div>
    <div class="cve-body">
      <div class="cve-title">Command Injection in D-Link DIR-815 (ssdpcgi_main)</div>
      <div class="cve-meta"><span class="tag cmd">Command Injection</span> Reporter: Dongsoo Kim · Binary analysis</div>
      <div class="cve-desc">
        Unauthenticated command-injection flaw in the <code>ssdpcgi_main</code>
        function of the <code>cgibin</code> binary in D-Link DIR-815 firmware
        1.04. Remote attackers can execute arbitrary commands without
        authentication. CVSS 9.8 (Critical).
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2024-0168</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in "Protect Online" Security Driver</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Denial-of-service flaw in the "Protect Online" kernel-mode security
        driver that allows an unprivileged local user to crash the driver.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2024-0169</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in "Protect Online" Security Driver</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Additional DoS primitive in the "Protect Online" security driver,
        independent of KVE-2024-0168.
      </div>
    </div>
  </li>

  <li class="cve-item">
    <div class="cve-id"><a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-2024-0170</a></div>
    <div class="cve-body">
      <div class="cve-title">Denial of Service in "Protect Online" Security Driver</div>
      <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Chanhee Park · Binary analysis</div>
      <div class="cve-desc">
        Third DoS vector disclosed against the "Protect Online" driver, rounding
        out a set of flaws that affect the driver's IOCTL interface.
      </div>
    </div>
  </li>

</ul>

<p style="margin-top: 2rem; font-size: 0.85rem; color: var(--global-text-color-light);">
  For KVE entries, the Korea Internet &amp; Security Agency (KISA) advisory
  portal is at
  <a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">knvd.krcert.or.kr</a>.
  Links above point to the canonical advisory when available; some recent
  CVE entries may still be in RESERVED status at the time of listing.
</p>
