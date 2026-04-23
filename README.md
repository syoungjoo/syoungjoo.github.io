# CSL Website — Maintainer's Guide

This is the source of the [Computer Systems Security Lab](https://syoungjoo.github.io) website, built on [Jekyll](https://jekyllrb.com/) with the [al-folio](https://github.com/alshedivat/al-folio) theme and served from GitHub Pages.

This guide is organized around the four things lab members actually do:

1. **How to contribute updates** — the Fork + Pull Request workflow (read this first).
2. **Updating member profiles** — roster entries and per-student profile pages.
3. **Adding publications** — `_bibliography/papers.bib`.
4. **Adding CVEs** — entries on the `/cves/` disclosure page.
5. **Adding gallery photos** — `assets/img/gallery/` + optional per-event metadata.

Shorter sections on news, repositories, local preview, and common gotchas follow at the end.

---

## 1. How to contribute updates (Fork + Pull Request)

The repository lives under **Prof. Shin's personal GitHub account** (`syoungjoo/syoungjoo.github.io`). Students do **not** have direct write access. Instead, all contributions go through a standard GitHub **Fork + Pull Request** workflow — the same one used in open-source projects.

### 1.1 One-time setup

1. Open [https://github.com/syoungjoo/syoungjoo.github.io](https://github.com/syoungjoo/syoungjoo.github.io) while signed in with your own GitHub account and click **Fork** (top-right). GitHub creates a copy under your account: `https://github.com/<your-id>/syoungjoo.github.io`.
2. Clone **your fork** locally:

   ```bash
   git clone git@github.com:<your-id>/syoungjoo.github.io.git
   cd syoungjoo.github.io
   ```
3. Add the upstream repo (the professor's copy) as a second remote so you can pull in new changes:

   ```bash
   git remote add upstream https://github.com/syoungjoo/syoungjoo.github.io.git
   git remote -v   # sanity check
   ```

### 1.2 Every-time routine

Before you start editing, pull the latest `main` from upstream so you don't work on stale files:

```bash
git checkout main
git pull upstream main
git push origin main        # keep your fork's main in sync (optional but clean)
```

Then make a **new branch** named after the change you're about to do — never commit straight to `main`:

```bash
git checkout -b update/<short-topic>
# examples:
#   update/taehun-profile
#   update/pub-usenix26-pathfault
#   update/gallery-2026-kickoff
```

Edit the relevant files (see §2–§4 below). Commit in small logical chunks with a short, imperative subject:

```bash
git add <files>
git commit -m "add Taehun Kim biography and awards"
```

Push the branch to **your fork**:

```bash
git push origin update/taehun-profile
```

### 1.3 Opening the Pull Request

Go to your fork on GitHub — a yellow banner "Compare & pull request" appears. Click it (or open `https://github.com/<your-id>/syoungjoo.github.io` → *Pull requests* → *New pull request*).

- **Base repository:** `syoungjoo/syoungjoo.github.io`, **base:** `main`
- **Head repository:** `<your-id>/syoungjoo.github.io`, **compare:** `update/taehun-profile`

Write a short title (same as your commit subject is fine) and a one-paragraph description of what changed and why. Submit the PR.

Prof. Shin reviews the PR, requests changes if needed (just push more commits to the same branch — the PR updates automatically), and merges when it's ready. GitHub Actions then rebuilds the site in 1–2 minutes.

### 1.4 Contribution ground rules

- **Never push directly to `main`.** All changes go through a PR.
- **One PR = one logical change.** Don't bundle an unrelated bib update with a gallery upload.
- **Branch names:** `update/<topic>` is the convention. Use hyphens, lowercase, no spaces.
- **Commit messages:** short, imperative, present tense. "add Taehun Kim profile" — not "added" or "adding".
- **Check the Actions tab after merge.** If the build goes red, fix it in a new PR rather than force-pushing.
- **Large files** (photos, PDFs): downsize before committing. Aim for ≤ 500 KB per image, ≤ 5 MB per PDF. Heavy files eat GitHub Pages bandwidth.
- **Don't commit secrets** (API keys, personal emails, private photos). Repo history is public forever.
- **If your fork falls behind `main`:** on GitHub your fork shows a "This branch is N commits behind upstream" banner — click **Sync fork**. Or locally: `git checkout main && git pull upstream main && git push origin main`.

---

## 2. Updating member profiles

Member information is split across three places:

1. **`_data/members.yml`** — roster data (name, cohort, email, photo, links, etc.). Drives both the Members overview page and each individual profile page.
2. **`_pages/members/<first-last>.md`** — one stub page per student. Renders the individual profile page at `/members/<first-last>/`.
3. **`_pages/professor.md`** — standalone page at `/members/professor/` with the full professor profile (bio, timeline, talks, service).

### 2.1 How the pieces fit together

- The **Members page** (`/members/`) shows compact cards. Student cards intentionally show **only name + cohort + icons** (we hide email, research interests, homepage, and Google Scholar icons here to keep the page tidy — those are reserved for the per-student profile page). Clicking a name opens that student's profile.
- The **Professor card** on `/members/` also hides homepage/scholar/github/linkedin icons — clicking the professor's name opens `/members/professor/`.
- **Student profile pages** pull the hero block (photo, cohort, interests, icons) from `_data/members.yml` via the shared include `_includes/student_profile.liquid`. Biography, Education, and Honors & Awards sections live as plain HTML in each student's `.md` stub — placeholder `TBA` blocks are filled in manually as content arrives.

### 2.2 Adding a new student

**Step A — add the roster entry** in `_data/members.yml`. Find the right section (`phd`, `ms`, or `undergrad`) and append:

```yaml
  - name: Gildong Hong               # English name, "First Last"
    cohort: "52nd"                   # enrollment cohort; omit for undergrads
    email: ghong                     # KU email local-part only (no @korea.ac.kr)
    image: members/ghong.jpg         # profile photo filename (see 2.5)
    interests: System Security, Side-channel Attacks
    links:
      homepage: https://...          # optional — personal site / Notion CV
      scholar:  https://scholar.google.com/citations?user=XXXX
      github:   https://github.com/...
      linkedin: https://www.linkedin.com/in/...
      twitter:  https://x.com/...
      orcid:    https://orcid.org/...
      dblp:     https://dblp.org/pid/...
```

**Step B — create the profile stub** at `_pages/members/<first-last>.md` where the slug is the English name lowercased with spaces → hyphens (e.g. `gildong-hong.md`). Copy this template:

```markdown
---
layout: page
permalink: /members/gildong-hong/
title: Gildong Hong
nav: false
---

{% include student_profile.liquid group="phd" slug="ghong" %}

<div class="stu-section">
  <h2>Biography</h2>
  <p class="tba">TBA — to be filled in.</p>
</div>

<div class="stu-section">
  <h2>Education</h2>
  <p class="tba">TBA — to be filled in.</p>
</div>

<div class="stu-section">
  <h2>Honors &amp; Awards</h2>
  <p class="tba">TBA — to be filled in.</p>
</div>

{% include student_publications.liquid slug="ghong" %}
```

**Important details:**
- `permalink` must be `/members/<first-last>/` — this is what the Members page links to (it derives the slug from `name | downcase | replace: " ", "-"`).
- `group="phd"` must match the roster section (`phd`, `ms`, or `undergrad`).
- `slug="ghong"` must match the `email` field in the roster entry — that's how the include looks up the right person (used by both `student_profile.liquid` and `student_publications.liquid`).
- Fill in `Biography`, `Education`, and `Honors & Awards` whenever content is available; leave the `TBA` block in place otherwise.
- The trailing `{% include student_publications.liquid slug="..." %}` auto-renders that student's publication list at the bottom of the page, filtered from `_bibliography/papers.bib` via the `students` field (see §3.5).

### 2.3 Rules & tips for the roster entry

- Every field except `name` is optional. Leave out any key you don't need — icons auto-hide.
- `links:` must be present even if empty; use `links: {}`.
- Supported link types and their icons are: `homepage`, `scholar`, `github`, `linkedin`, `twitter`, `orcid`, `dblp`. Other keys are ignored.
- On the Members overview page, `homepage` and `scholar` are hidden for all members; the remaining icons appear on student cards if present. On each student's individual profile page, **all** link icons are shown.
- **Per-student publication lists** are driven from `_bibliography/papers.bib` via a custom `students` field on each entry — **not** from `_data/members.yml`. See §3.4 below.

### 2.4 Moving a student to Alumni

When a student graduates:

1. Delete their entry from `phd` / `ms` / `undergrad` in `_data/members.yml`.
2. Delete the matching stub file `_pages/members/<first-last>.md`.
3. Add a new entry under `alumni:`:

```yaml
  - name: Gildong Hong
    degree: M.S. Course              # or "Ph.D. Course"
    cohort: "50th"
    affiliation: Samsung Research    # current employer
```

Alumni are rendered as a simple table (no photo, no links, no profile page).

### 2.5 Profile photos

- Put photos in: `assets/img/members/`
- Filename convention: `<email_local_part>.jpg` (e.g. `ghong.jpg`).
- Use a **square crop**, ~400×400 px is plenty. Bigger files just slow down the page.
- `.jpg`, `.png`, and `.webp` all work — match the extension in the `image:` field.
- **Optional `card_image:` override** — if the main photo doesn't crop nicely into a square on the Members card (e.g. full-body portrait), add a square version and reference it via an extra `card_image:` field. The Members page uses `card_image` when present and falls back to `image` otherwise; the full profile page always uses `image`. Example:

  ```yaml
  image: members/ghong.jpg              # full-body / used on profile page
  card_image: members/ghong_card.jpg    # square crop / used on Members card
  ```

### 2.6 The professor profile page

The professor has a bespoke page at `_pages/professor.md` (`permalink: /members/professor/`). The roster entry in `_data/members.yml` still drives the hero block (photo, name, email, icons), but the body sections (Biography, Research Interests, Education, Professional Experience, Invited Talks, Professional Service, Publications) are hand-authored HTML in that file — edit them directly when updating the CV.

---

## 3. Adding publications

All publications live in a single BibTeX file:

```
_bibliography/papers.bib
```

The file is grouped by year with `%` comment banners. When adding a new paper, put it under the correct year block, newest year at the top of the file.

### 3.1 Template

```bibtex
@inproceedings{lastname2026shortkey,
  abbr      = {USENIX Sec},
  title     = {Your Paper Title},
  author    = {Last, First and Last, First and Shin, Youngjoo},
  booktitle = {Proceedings of the USENIX Security Symposium},
  year      = {2026},
  selected  = {true}
}
```

**Field notes:**

| Field        | Notes |
|--------------|-------|
| `@inproceedings` / `@article` | Use `@article` for journals, `@inproceedings` for conferences. |
| citation key (`lastname2026shortkey`) | Must be unique in the file. Convention: `firstauthorLastname` + `year` + short name. |
| `abbr`       | Short venue badge shown on the publication list (e.g. `USENIX Sec`, `ACM CCS`, `NDSS`, `ASIACCS`, `IEEE S&P`). Keep it short. |
| `author`     | Names separated by ` and `. Prof. Shin is usually last. Use `Last, First` format. |
| `booktitle` / `journal` | Full venue name. |
| `year`       | Four-digit year. |
| `selected`   | `{true}` makes the paper appear on the home page's featured list. Omit otherwise. |

### 3.2 Optional fields

```bibtex
  pdf             = {your_paper.pdf},              % file in /assets/pdf/
  html            = {https://arxiv.org/abs/...},   % external link (arxiv / publisher)
  code            = {https://github.com/koreacsl/YourRepo},
  slides          = {talk.pdf},                    % file in /assets/pdf/
  award           = {Best Paper Award},
  additional_info = {[BK21 IF=4]},                 % appears inline with the venue label
  note            = {to appear},
```

Each of these adds a small button (or inline tag, for `additional_info`) next to the entry on the publications page.

### 3.3 Listing authors

**All authors must be listed in full** — never use `and others`. The site is configured
(`max_author_limit:` empty in `_config.yml`) to always display every author, and a
truncated list would silently hide co-authors.

Use the `Last, First and Last, First and …` format:

```bibtex
author = {Kim, Taehun and Jang, Hyerean and Shin, Youngjoo},
```

### 3.4 Tagging lab-member authors (for profile pages)

Each student's profile page (`/members/<first-last>/`) auto-renders a "Publications" section filtered to papers they co-authored. The filter uses a custom `students` field on the BibTeX entry — a comma-separated list of the authors' **email local-parts** (the same slug used as the `email:` in `_data/members.yml`):

```bibtex
@inproceedings{park2026sysdiver,
  ...
  author   = {Park, Chanhee and Kim, Dongjoo and Shin, Youngjoo},
  students = {pch2180,d05004}        % <-- email local-parts, comma-separated, no spaces
}
```

Rules of thumb:

- Add one slug per current lab member who co-authored the paper.
- Do **not** list the professor, external collaborators, or alumni (alumni don't have profile pages, so tagging them has no effect).
- Use **no spaces** around the commas — the query matches literally.
- When a student graduates, leave the `students` field alone — past papers should still show on history even if the student is moved to alumni.

### 3.5 Typical flow for a new paper

1. Drop the PDF (and any slides) into `assets/pdf/`.
2. Add the `@inproceedings{...}` entry at the top of the correct year block in `papers.bib`.
3. List every co-author (see 3.3).
4. Add `code = {…}` if the artifact repo is public on [github.com/koreacsl](https://github.com/koreacsl).
5. Add `additional_info = {[BK21 IF=N]}` if the paper has a BK21 evaluation score.
6. If it's a flagship result, add `selected = {true}`.
7. Add `students = {slug1,slug2}` listing every current lab-member co-author (see §3.4) so the paper shows up on their profile pages.
8. Open a PR (see §1).

---

## 4. Adding CVEs

Vulnerabilities that lab members report through CVE (global) or KVE (Korea) are listed on `/cves/`. This page is hand-authored HTML (not data-driven), which keeps the formatting flexible but means each new entry is a small copy-paste job in one file:

```
_pages/cves.md
```

Entries are **grouped by year**, newest year at the top. Inside each year, list newest IDs first.

### 4.1 Adding a new entry

1. Open `_pages/cves.md`.
2. Find (or create) the `<h2 class="cve-year">YYYY</h2>` block for the disclosure year. The items for that year live in the `<ul class="cve-list"> … </ul>` right below.
3. Paste this template as a new `<li>` at the top of the list and fill it in:

   ```html
   <li class="cve-item">
     <div class="cve-id"><a href="https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN" target="_blank" rel="noopener">CVE-YYYY-NNNNN</a></div>
     <div class="cve-body">
       <div class="cve-title">One-line vulnerability title (product + what breaks)</div>
       <div class="cve-meta"><span class="tag dos">DoS</span> Reporter: Firstname Lastname · Binary analysis</div>
       <div class="cve-desc">
         2–3 sentences: affected product/version, the root cause, impact, and
         CVSS score if known. Keep it factual; this is a public page.
       </div>
     </div>
   </li>
   ```

4. For **KVE** entries, link to the KISA advisory portal:
   ```html
   <a href="https://knvd.krcert.or.kr/" target="_blank" rel="noopener">KVE-YYYY-NNNN</a>
   ```
5. If the finding is tied to a lab paper, add a highlighted block **inside** `cve-body`, right after `cve-desc`:

   ```html
   <div class="cve-pub">
     <strong>Related publication:</strong>
     Author A, Author B, Youngjoo Shin.
     <em>"Paper Title."</em>
     Venue YYYY.
     <a href="{{ '/publications/' | relative_url }}">[lab publications]</a>
     · <a href="https://github.com/koreacsl/Repo" target="_blank" rel="noopener">[code]</a>
   </div>
   ```

### 4.2 Tag conventions

The small colored pill next to the reporter uses one of these classes — pick the closest one (or add your own class in the `<style>` block at the top of the file):

| Class       | Use for                          |
|-------------|----------------------------------|
| `tag dos`   | Denial of service                |
| `tag rce`   | Remote / arbitrary code execution|
| `tag cmd`   | Command or shell injection       |
| `tag kbypass` | KASLR / ASLR / mitigation bypass |

### 4.3 Style & tone

- **Neutral, factual language.** This is a lab deliverables page, not marketing. Don't editorialize.
- **Use the vendor's real product name** and firmware/version string (e.g. *Tenda AC9 firmware 15.03.06.42*).
- **CVSS:** cite the numeric base score and severity band (e.g. "CVSS 8.8 (High)") when available.
- If the advisory is still in `RESERVED` status on NVD, leave the link as-is — it'll resolve once the entry is published.

---

## 5. Adding gallery photos

The gallery page (`/gallery/`) is **folder-based** — in most cases you just drop
photos into a folder and the site auto-discovers them. No YAML editing required.

### 5.1 The easy path (no metadata)

1. Create a folder under `assets/img/gallery/` with a slug.
   **Prefix with `YYYY-MM-DD-` so events sort chronologically:**
   ```
   assets/img/gallery/2026-03-15-kickoff/
   ```
2. Drop your photos in. `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif` are all auto-detected.
3. Open a PR.

The folder name becomes the event title (hyphens → spaces). Events are sorted
newest-first. Photos within an event are sorted alphabetically by filename —
name them `01-group.jpg`, `02-stage.jpg`, … if you want a specific order.

### 5.2 With metadata (title / date / place)

For a prettier title or to show a venue, add an optional YAML file:

```
_data/gallery/<same-slug>.yml
```

Example — `_data/gallery/2026-03-15-kickoff.yml`:

```yaml
title: Spring Semester Kickoff
date:  2026-03-15
place: Anam Campus, Korea University
# cover: 01-group.jpg   # optional; defaults to first photo alphabetically
```

Every field is optional. Missing fields fall back to the auto-derived values
from the folder name.

### 5.3 Photo tips

- Downsize large files (> 3 MB) before committing. Roughly 1600 px on the long
  edge is plenty. Heavy pages load slowly and eat GitHub Pages bandwidth.
- Tiles are displayed as a uniform square grid, so center-weighted photos look best.
- Clicking a tile opens a full-screen lightbox (←/→ to navigate, Esc to close).

See also `_data/gallery/README.md` for a shorter reference.

---

## 6. News items (home page announcements)

The scrollable list on the home page is built from `_news/`.
Each item is a separate Markdown file:

```
_news/announcement_2026-04-19.md
```

With this front matter:

```yaml
---
layout: post
date: 2026-04-19 10:00:00+0900
inline: true
related_posts: false
---

Our paper *Paper Title* has been accepted to **USENIX Security 2026**! 🎉
```

- `inline: true` means it's shown in the scrollable box rather than as a full blog post.
- Newest date appears at the top. The home page shows up to 8 items.
- Plain Markdown works for the body; you can use bold, italic, and links.

---

## 7. Repositories page

The repositories page (`/repositories/`) is driven by:

```
_data/repositories.yml
```

To add a new lab project: push the repo under the [koreacsl](https://github.com/koreacsl) GitHub organization, then append its `owner/name` to the `github_repos:` list:

```yaml
github_repos:
  - koreacsl/SysBumps
  - koreacsl/YourNewRepo    # <-- add here
```

Cards are rendered via `github-readme-stats.vercel.app`, so the repo must be **public**.

---

## 8. Previewing locally (optional)

You can build the site without opening a PR if you want to check something first. Requirements: Ruby 3.x + Bundler.

```bash
bundle install          # first time only
bundle exec jekyll serve
```

Then open `http://localhost:4000`. The site rebuilds automatically when you save files.

If `bundle install` fails with a version error, update the Ruby/Bundler versions in the error message and try again. Using [rbenv](https://github.com/rbenv/rbenv) to manage Ruby is easiest.

Local preview is **optional** — once your PR is merged, GitHub Pages rebuilds automatically, and any errors show up in the **Actions** tab.

---

## 9. Common gotchas

- **YAML is indentation-sensitive.** Use 2 spaces per level and never use tabs. If the site stops building after a members edit, 99% of the time this is why.
- **Strings with a colon, `#`, or leading/trailing spaces must be quoted.** Example: `cohort: "45th"`. When in doubt, wrap in double quotes.
- **BibTeX keys must be unique.** If two entries share a key, only one will be rendered.
- **Image filenames are case-sensitive on GitHub Pages.** `Foo.jpg` and `foo.jpg` are different files.
- **Don't edit `_config.yml` unless you know what you're doing.** Site-wide settings live there; a typo can break the whole build.
- **Keep your fork in sync.** If `main` has moved on and your branch is stale, GitHub will flag merge conflicts in the PR — pull from upstream, resolve, and push again.

---

## 10. Who to ask

- Build failing or something broken after merge → check the GitHub **Actions** tab, post the red log in the lab chat.
- Adding a new section, navbar item, or changing the layout → ping Prof. Shin first (open an issue rather than opening a surprise PR).

---

## 11. Further reference

This site is built on the **al-folio** Jekyll theme. For anything beyond the day-to-day edits covered above — deeper theme customization, new layouts, plugin configuration, advanced features, or upstream updates — refer to the upstream project:

👉 [https://github.com/alshedivat/al-folio](https://github.com/alshedivat/al-folio)

Happy maintaining.
