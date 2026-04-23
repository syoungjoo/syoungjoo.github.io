# CSL Website — Maintainer's Guide

Source of the [Computer Systems Security Lab](https://syoungjoo.github.io) website. Built on [Jekyll](https://jekyllrb.com/) + [al-folio](https://github.com/alshedivat/al-folio), served from GitHub Pages.

Most content is **data-driven**: edit YAML under `_data/`, don't touch HTML.

| To change…                           | Edit                                       |
|--------------------------------------|--------------------------------------------|
| Roster (photos, icons, interests)    | `_data/members.yml`                        |
| A student's bio / education / honors | `_data/profiles/<name-slug>.yml`           |
| CVE / KVE entries                    | `_data/cves.yml`                           |
| Publications                         | `_bibliography/papers.bib`                 |
| Repositories grid                    | `_data/repositories.yml`                   |
| Gallery event metadata               | `_data/gallery/<slug>.yml` (optional)      |
| Home-page news                       | `_news/announcement_YYYY-MM-DD.md`         |

---

## How to contribute (every time)

Students do **not** have write access. All changes go through a fork + PR.

**One-time:** fork `syoungjoo/syoungjoo.github.io`, clone your fork, add upstream:
```bash
git remote add upstream https://github.com/syoungjoo/syoungjoo.github.io.git
```

**Every time:**
```bash
git checkout main
git pull upstream main
git checkout -b update/<short-topic>     # e.g. update/taehun-profile
# ... edit files ...
git commit -m "short imperative subject"
git push origin update/<short-topic>
```

Open a PR against `syoungjoo/syoungjoo.github.io:main`. Prof. Shin reviews and merges. GitHub Pages rebuilds in 1–2 min.

Rules: never push to `main`; one PR = one logical change; no secrets; downsize images (≤ 500 KB) and PDFs (≤ 5 MB).

---

## How to add a new student

**1.** Append a roster entry to `_data/members.yml` under the right group (`phd` / `ms` / `undergrad`):

```yaml
  - name: Gildong Hong
    cohort: "52nd"                 # omit for undergrads
    email: ghong                   # KU email local-part
    image: members/ghong.jpg
    interests: System Security, Side-channel Attacks
    links:
      homepage: https://...
      scholar:  https://scholar.google.com/citations?user=XXXX
      github:   https://github.com/...
      # linkedin / twitter / orcid / dblp also supported; omit unused keys
```

Put the photo at `assets/img/members/ghong.jpg` — square crop, ~400×400 px.

**2.** Create `_data/profiles/gildong-hong.yml` (slug = name lowercased, spaces → hyphens):

```yaml
biography: |
  Gildong Hong is an M.S. student ... advised by Prof. Youngjoo Shin.

sections:
  - heading: Education
    type: timeline
    items:
      - { period: "2026.03 – present", desc: "M.S., School of Cybersecurity", where: "Korea University" }
      - { period: "2020 – 2026",        desc: "B.S.",                        where: "Some University" }

  - heading: Honors & Awards
    type: bullets
    items:
      - Award one
      - Award two
```

Section options:
- `type: timeline` — period + desc (+ optional `where`). Good for Education, Experience.
- `type: bullets` — plain list. Good for Honors, Projects.
- `tba: true` — renders "TBA — to be filled in." (use until content arrives).
- `note: "..."` — greyed-out footnote under a timeline.

**3.** Create `_pages/members/gildong-hong.md` — just the stub:

```markdown
---
layout: page
permalink: /members/gildong-hong/
title: Gildong Hong
nav: false
---

{% include student_profile.liquid group="phd" slug="ghong" %}
```

`group` must match the roster group; `slug` must match the `email` field.

---

## How to update a student's profile

Edit `_data/profiles/<name-slug>.yml`. Add items, edit bio, whatever. Never touch the `.md` stub — it's just a template invocation.

**To update the photo:** replace `assets/img/members/<slug>.jpg` (same filename as in `_data/members.yml` `image:` field). Square crop, ~400×400 px, ≤ 500 KB. Keep the filename — no YAML edit needed.

---

## How to move a student to Alumni

1. Delete their entry from `phd` / `ms` / `undergrad` in `_data/members.yml`.
2. Delete `_data/profiles/<name-slug>.yml`.
3. Delete `_pages/members/<name-slug>.md`.
4. Append under `alumni:` in `_data/members.yml`:

```yaml
  - name: Gildong Hong
    degree: M.S. Course            # or "Ph.D. Course"
    cohort: "50th"
    affiliation: Samsung Research  # current employer
```

Leave their `students: ghong` tag in existing BibTeX entries alone — past papers stay attributed.

---

## How to add a publication

Add an entry to `_bibliography/papers.bib` under the correct year block (newest year on top).

```bibtex
@inproceedings{park2026sysdiver,
  abbr      = {USENIX Sec},
  title     = {Your Paper Title},
  author    = {Park, Chanhee and Kim, Dongjoo and Shin, Youngjoo},
  booktitle = {Proceedings of the USENIX Security Symposium},
  year      = {2026},
  selected  = {true},              % optional — show on home page
  students  = {pch2180,d05004}     % comma-separated email slugs
}
```

**Rules:**
- List **every** author (never `and others`). Use `Last, First and Last, First`.
- Citation key must be unique. Convention: `firstauthorLastName` + `year` + `shortname`.
- `students` = current lab-member email slugs (comma-separated, no spaces). Drives per-student publication lists. Don't tag the professor, alumni, or external co-authors.

**Optional fields:**
```bibtex
  pdf             = {paper.pdf},                   % in assets/pdf/
  html            = {https://arxiv.org/abs/...},
  code            = {https://github.com/koreacsl/...},
  slides          = {talk.pdf},
  award           = {Best Paper Award},
  additional_info = {[BK21 IF=4]},
  note            = {to appear},
```

Drop PDFs/slides into `assets/pdf/`.

---

## How to add a CVE / KVE

Append to the right year's `items:` list in `_data/cves.yml` (newest ID on top):

```yaml
  - id: CVE-YYYY-NNNNN
    url: https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN
    title: One-line title (product + what breaks)
    tag: dos                    # dos | rce | cmd | kbypass
    tag_label: DoS              # optional — override badge text
    reporter: Firstname Lastname
    category: Binary analysis   # optional
    desc: |
      2–3 sentences: affected version, root cause, impact, CVSS if known.
```

**For KVE entries:** `url: https://knvd.krcert.or.kr/` (or omit — falls back to `kve_portal` at the top of the file).

**Linking to a paper:**
```yaml
    publication:
      text: |
        Author A, Author B, Youngjoo Shin.
        *"Paper Title."* Venue YYYY.
      links:
        - { label: "[lab publications]", url: "/publications/", relative: true }
        - { label: "[code]",             url: "https://github.com/koreacsl/Repo" }
```

Tags: `dos` (orange), `rce` (red), `cmd` (blue), `kbypass` (purple). Add a new CSS rule in `_pages/cves.md` if you need a new one.

---

## How to add gallery photos

**Simplest case (no metadata):**

```
assets/img/gallery/2026-03-15-kickoff/01-group.jpg
                                     /02-stage.jpg
                                     /...
```

Folder name becomes the event title (hyphens → spaces). Prefix with `YYYY-MM-DD-` for chronological sort. Photos sort alphabetically inside — name them `01-...`, `02-...` to control order.

**With metadata** — add `_data/gallery/2026-03-15-kickoff.yml`:

```yaml
title: Spring Semester Kickoff
date:  2026-03-15
place: Anam Campus, Korea University
# cover: 01-group.jpg   # optional
```

Downsize to ≤ 1600 px on the long edge before committing.

---

## How to add a news item

Drop a file in `_news/`:

```
_news/announcement_2026-04-19.md
```

```yaml
---
layout: post
date: 2026-04-19 10:00:00+0900
inline: true
related_posts: false
---

Our paper *Paper Title* has been accepted to **USENIX Security 2026**! 🎉
```

Newest date appears first; home page shows up to 8 items.

---

## Local preview (optional)

```bash
bundle install                               # first time
bundle exec jekyll serve --livereload        # every time
```

Open `http://127.0.0.1:4000`. Jekyll doesn't always detect `_data/` changes — restart if a YAML edit doesn't show. Stuck on stale output? `rm -rf _site .jekyll-cache`.

---

For theme customization, new layouts, or plugin config beyond this guide:
👉 [alshedivat/al-folio](https://github.com/alshedivat/al-folio)
