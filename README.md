# CSL Website — Maintainer's Guide

This is the source of the [Computer Systems Security Lab](https://syoungjoo.github.io) website, built on [Jekyll](https://jekyllrb.com/) with the [al-folio](https://github.com/alshedivat/al-folio) theme and served from GitHub Pages.

Most day-to-day edits are just changes to a few text files — you do **not** need to touch HTML or CSS. This guide covers the three tasks you will do most often:

1. **Updating members** (`_data/members.yml`)
2. **Adding publications** (`_bibliography/papers.bib`)
3. **Adding gallery photos** (`assets/img/gallery/` + optional `_data/gallery/`)

Plus shorter sections on news, repositories, and local previewing.

---

## Quick workflow (all edits)

1. Create a branch (or edit directly on GitHub via the web editor for small changes).
2. Edit the relevant file (see sections below).
3. Commit and push to `main`.
4. GitHub Actions rebuilds the site in ~1–2 minutes. Refresh the page.

If something looks broken after your push, check the **Actions** tab of the repo for the red build log.

---

## 1. Updating members

All member information lives in a single YAML file:

```
_data/members.yml
```

It has six sections: `professor`, `phd`, `ms`, `undergrad`, `staff`, `alumni`.
Entries appear on the site in the same order as they appear in the file.

### 1.1 Adding a new student

Find the right section (`phd`, `ms`, or `undergrad`) and append an entry using this template:

```yaml
  - name: Gildong Hong               # English name, "First Last"
    cohort: "52nd"                   # enrollment cohort; omit for undergrads
    email: ghong                     # KU email local-part only (no @korea.ac.kr)
    image: members/ghong.jpg         # profile photo filename (see 1.3)
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

**Rules:**
- Every field except `name` is optional. Leave out any key you don't need — icons auto-hide.
- `links:` must be present even if empty; use `links: {}`.
- `email` is shown as `<email> [at] korea.ac.kr` on the card. It is **not** a clickable link.
- Supported link types and their icons are: `homepage`, `scholar`, `github`, `linkedin`, `twitter`, `orcid`, `dblp`. Other keys are ignored.

### 1.2 Moving a student to Alumni

When a student graduates:

1. Delete their entry from `phd` / `ms` / `undergrad`.
2. Add a new entry to `alumni:`:

```yaml
  - name: Gildong Hong
    degree: M.S. Course              # or "Ph.D. Course"
    cohort: "50th"
    affiliation: Samsung Research    # current employer
```

Alumni are rendered as a simple table (no photo, no links).

### 1.3 Profile photos

- Put photos in: `assets/img/members/`
- Filename convention: `<email_local_part>.jpg` (e.g. `ghong.jpg`).
- Use a **square crop**, ~400×400 px is plenty. Bigger files just slow down the page.
- `.jpg`, `.png`, and `.webp` all work — match the extension in the `image:` field.

---

## 2. Adding publications

All publications live in a single BibTeX file:

```
_bibliography/papers.bib
```

The file is grouped by year with `%` comment banners. When adding a new paper, put it under the correct year block, newest year at the top of the file.

### 2.1 Template

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

### 2.2 Optional fields

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

### 2.3 Listing authors

**All authors must be listed in full** — never use `and others`. The site is configured
(`max_author_limit:` empty in `_config.yml`) to always display every author, and a
truncated list would silently hide co-authors.

Use the `Last, First and Last, First and …` format:

```bibtex
author = {Kim, Taehun and Jang, Hyerean and Shin, Youngjoo},
```

### 2.4 Typical flow for a new paper

1. Drop the PDF (and any slides) into `assets/pdf/`.
2. Add the `@inproceedings{...}` entry at the top of the correct year block in `papers.bib`.
3. List every co-author (see 2.3).
4. Add `code = {…}` if the artifact repo is public on [github.com/koreacsl](https://github.com/koreacsl).
5. Add `additional_info = {[BK21 IF=N]}` if the paper has a BK21 evaluation score.
6. If it's a flagship result, add `selected = {true}`.
7. Commit and push.

---

## 3. Adding gallery photos

The gallery page (`/gallery/`) is **folder-based** — in most cases you just drop
photos into a folder and the site auto-discovers them. No YAML editing required.

### 3.1 The easy path (no metadata)

1. Create a folder under `assets/img/gallery/` with a slug.
   **Prefix with `YYYY-MM-DD-` so events sort chronologically:**
   ```
   assets/img/gallery/2026-03-15-kickoff/
   ```
2. Drop your photos in. `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif` are all auto-detected.
3. Commit and push. Done.

The folder name becomes the event title (hyphens → spaces). Events are sorted
newest-first. Photos within an event are sorted alphabetically by filename —
name them `01-group.jpg`, `02-stage.jpg`, … if you want a specific order.

### 3.2 With metadata (title / date / place)

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

### 3.3 Photo tips

- Downsize large files (> 3 MB) before committing. Roughly 1600 px on the long
  edge is plenty. Heavy pages load slowly and eat GitHub Pages bandwidth.
- Tiles are displayed as a uniform square grid, so center-weighted photos look best.
- Clicking a tile opens a full-screen lightbox (←/→ to navigate, Esc to close).

See also `_data/gallery/README.md` for a shorter reference.

---

## 4. News items (home page announcements)

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

## 5. Repositories page

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

## 6. Previewing locally (optional)

You can build the site without pushing if you want to check something first. Requirements: Ruby 3.x + Bundler.

```bash
bundle install          # first time only
bundle exec jekyll serve
```

Then open `http://localhost:4000`. The site rebuilds automatically when you save files.

If `bundle install` fails with a version error, update the Ruby/Bundler versions in the error message and try again. Using [rbenv](https://github.com/rbenv/rbenv) to manage Ruby is easiest.

You do **not** have to preview locally — pushing to `main` will rebuild on GitHub Pages and any errors show up in the **Actions** tab.

---

## 7. Common gotchas

- **YAML is indentation-sensitive.** Use 2 spaces per level and never use tabs. If the site stops building after a members edit, 99% of the time this is why.
- **Strings with a colon, `#`, or leading/trailing spaces must be quoted.** Example: `cohort: "45th"`. When in doubt, wrap in double quotes.
- **BibTeX keys must be unique.** If two entries share a key, only one will be rendered.
- **Image filenames are case-sensitive on GitHub Pages.** `Foo.jpg` and `foo.jpg` are different files.
- **Don't edit `_config.yml` unless you know what you're doing.** Site-wide settings live there; a typo can break the whole build.

---

## 8. Who to ask

- Build failing or something broken after a push → check the GitHub **Actions** tab, post the red log in the lab chat.
- Adding a new section, navbar item, or changing the layout → ping Prof. Shin first.

---

## 9. Further reference

This site is built on the **al-folio** Jekyll theme. For anything beyond the day-to-day edits covered above — deeper theme customization, new layouts, plugin configuration, advanced features, or upstream updates — refer to the upstream project:

👉 [https://github.com/alshedivat/al-folio](https://github.com/alshedivat/al-folio)

Happy maintaining.
