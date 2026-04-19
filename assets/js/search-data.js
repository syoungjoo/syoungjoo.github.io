// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-members",
          title: "members",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/members/";
          },
        },{id: "nav-research",
          title: "research",
          description: "Research areas of the Computer Systems Security Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "Publications by the Computer Systems Security Lab, in reverse chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-repositories",
          title: "repositories",
          description: "Open-source code and artifacts from the Computer Systems Security Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "news-our-paper-devious-device-driven-side-channel-attacks-on-the-iommu-has-been-accepted-to-ieee-s-amp-amp-p-2023",
          title: 'Our paper DevIOus: Device-Driven Side-Channel Attacks on the IOMMU has been accepted to...',
          description: "",
          section: "News",},{id: "news-our-paper-sysbumps-exploiting-speculative-execution-in-system-calls-for-breaking-kaslr-in-macos-for-apple-silicon-has-been-accepted-to-acm-ccs-2024",
          title: 'Our paper SysBumps: Exploiting Speculative Execution in System Calls for Breaking KASLR in...',
          description: "",
          section: "News",},{id: "news-our-team-won-1st-place-at-the-2024-cybersecurity-paper-competition",
          title: 'Our team won 1st place at the 2024 Cybersecurity Paper Competition.',
          description: "",
          section: "News",},{id: "news-sysbumps-our-ccs-2024-paper-on-breaking-kaslr-in-macos-for-apple-silicon-was-selected-for-presentation-at-black-hat-europe-2024",
          title: 'SysBumps (our CCS 2024 paper on breaking KASLR in macOS for Apple Silicon)...',
          description: "",
          section: "News",},{id: "news-our-paper-mimiccall-bypassing-system-call-filters-via-kernel-function-redundancy-has-been-accepted-to-acsac-2025",
          title: 'Our paper MimicCall: Bypassing System Call Filters via Kernel Function Redundancy has been...',
          description: "",
          section: "News",},{id: "news-two-papers-accepted-to-esorics-2025-t-time-controlled-channel-attack-against-intel-tdx-and-cache-demote-for-fast-eviction-set-construction",
          title: 'Two papers accepted to ESORICS 2025: T-Time (controlled-channel attack against Intel TDX) and...',
          description: "",
          section: "News",},{id: "news-our-paper-timeslice-sandwich-a-gpu-side-channel-attack-exploiting-time-sliced-scheduling-has-been-accepted-to-usenix-security-symposium-2026",
          title: 'Our paper TIMESLICE-SANDWICH: A GPU Side-channel Attack Exploiting Time-Sliced Scheduling has been accepted...',
          description: "",
          section: "News",},{id: "news-our-paper-sysdiver-lightweight-and-fast-static-analysis-for-windows-kernel-drivers-has-been-accepted-to-asiaccs-2026",
          title: 'Our paper SysDiver: Lightweight and Fast Static Analysis for Windows Kernel Drivers has...',
          description: "",
          section: "News",},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
