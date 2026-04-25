#!/usr/bin/env python3
"""Build _data/cv.yml from professor.yml + members.yml + papers.bib.

The site's source of truth lives in:
  - _data/professor.yml          : bio, education, experience, talks, service
  - _data/members.yml            : roster (name, image, links)
  - _bibliography/papers.bib     : publications

This script flattens those into a single _data/cv.yml in RenderCV's
schema (https://rendercv.com/) so the GitHub Action can produce a PDF
CV without duplicating content.

Run locally:
  python bin/build_cv.py

The generated _data/cv.yml is a build artifact: do not edit by hand.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
import bibtexparser

ROOT = Path(__file__).resolve().parent.parent
PROF_YAML = ROOT / "_data" / "professor.yml"
MEMBERS_YAML = ROOT / "_data" / "members.yml"
BIB_FILE = ROOT / "_bibliography" / "papers.bib"
CV_OUT = ROOT / "_data" / "cv.yml"

# Match either "Shin, Youngjoo" or "Youngjoo Shin" in BibTeX author fields.
PROF_NAME_RE = re.compile(r"\bShin,\s*Youngjoo\b|\bYoungjoo\s+Shin\b")


def load_yaml(p: Path):
    with p.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def strip_md(s: str) -> str:
    """Strip basic markdown markers but keep the text."""
    if not s:
        return ""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)               # bold
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)\*(?!\*)", r"\1", s)  # italic
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)        # [t](u) -> t
    return s.strip()


def split_where(where: str) -> tuple[str, str]:
    """'KAIST, Korea' -> ('KAIST', 'Korea')."""
    if not where:
        return "", ""
    if "," in where:
        inst, loc = where.split(",", 1)
        return inst.strip(), loc.strip()
    return where.strip(), ""


def build_education(prof) -> list[dict]:
    out = []
    for e in prof.get("education", []):
        inst, loc = split_where(e.get("where", ""))
        entry = {
            "institution": inst or "Unknown",
            "area": e.get("desc", ""),
            "degree": (e.get("period") or "").rstrip("."),
        }
        if loc:
            entry["location"] = loc
        out.append(entry)
    return out


def build_experience(prof) -> list[dict]:
    out = []
    for x in prof.get("experience", []):
        out.append({
            "company": x.get("where", ""),
            "position": x.get("desc", ""),
            "date": x.get("period", ""),
        })
    return out


def build_invited_talks(prof) -> list[dict]:
    """One OneLineEntry per year: label=year, details=joined items."""
    out = []
    for y in prof.get("invited_talks", []):
        year = y.get("year")
        items = [strip_md(it) for it in y.get("items", [])]
        if not items:
            continue
        out.append({"label": str(year), "details": "; ".join(items)})
    return out


def build_service_sections(prof) -> dict[str, list]:
    """Each service heading -> its own section as BulletEntry list."""
    out = {}
    for s in prof.get("service", []):
        heading = s.get("heading", "Service")
        items = [strip_md(it) for it in s.get("items", [])]
        out[heading] = [{"bullet": it} for it in items if it]
    return out


def parse_authors(raw: str) -> list[str]:
    """'Last, First and Last, First' -> ['First Last', 'First Last']."""
    out = []
    for a in re.split(r"\s+and\s+", raw):
        a = a.strip().strip("{}")
        if "," in a:
            last, first = [p.strip() for p in a.split(",", 1)]
            out.append(f"{first} {last}")
        elif a:
            out.append(a)
    return out


def parse_bib(bib_path: Path) -> list[dict]:
    """Return RenderCV PublicationEntry list, newest first."""
    if not bib_path.exists():
        return []
    with bib_path.open(encoding="utf-8") as f:
        db = bibtexparser.load(f)
    pubs = []
    for entry in db.entries:
        author = entry.get("author", "")
        if not PROF_NAME_RE.search(author):
            continue
        title = entry.get("title", "").strip().strip("{}")
        venue = entry.get("booktitle", "") or entry.get("journal", "")
        venue = re.sub(r"^Proceedings of (the )?", "", venue).strip().strip("{}")
        year = entry.get("year", "").strip()
        pub = {
            "title": title,
            "authors": parse_authors(author),
        }
        if year:
            pub["date"] = year
        if venue:
            pub["journal"] = venue
        pubs.append((int(year) if year.isdigit() else 0, pub))
    pubs.sort(key=lambda kv: -kv[0])
    return [p for _, p in pubs]


def extract_username(url: str) -> str:
    """Last non-empty path segment of a URL, used as social-network username."""
    return url.rstrip("/").rsplit("/", 1)[-1] or url


def build_social_networks(prof_member) -> list[dict]:
    """Map roster `links:` to RenderCV social_networks entries."""
    out = []
    links = prof_member.get("links", {}) or {}
    if v := links.get("github"):
        out.append({"network": "GitHub", "username": extract_username(v)})
    if v := links.get("linkedin"):
        out.append({"network": "LinkedIn", "username": extract_username(v)})
    if v := links.get("orcid"):
        out.append({"network": "ORCID", "username": extract_username(v)})
    return out


def build_cv() -> dict:
    prof = load_yaml(PROF_YAML)
    members = load_yaml(MEMBERS_YAML)
    prof_member = members["professor"][0]

    contact = prof.get("contact", {})
    affil = prof.get("affiliation", {})

    cv = {
        "name": prof_member["name"],
        "location": f"{affil.get('university', '')}",
        "email": f"{contact.get('email_local')}@{contact.get('email_domain')}",
        "phone": contact.get("phone"),
        "website": "https://syoungjoo.github.io",
    }
    socials = build_social_networks(prof_member)
    if socials:
        cv["social_networks"] = socials

    sections: dict = {}
    if bio := strip_md(prof.get("biography", "")):
        sections["summary"] = [bio]
    if interests := prof.get("interests"):
        sections["interests"] = [", ".join(interests)]
    if education := build_education(prof):
        sections["education"] = education
    if experience := build_experience(prof):
        sections["experience"] = experience
    if pubs := parse_bib(BIB_FILE):
        sections["publications"] = pubs
    if talks := build_invited_talks(prof):
        sections["invited talks"] = talks
    for heading, items in build_service_sections(prof).items():
        if items:
            sections[heading.lower()] = items
    cv["sections"] = sections

    return {
        "cv": cv,
        "design": {"theme": "sb2nov"},
        "locale": {"language": "en"},
        "rendercv_settings": {"date": None},
    }


def main() -> int:
    out = build_cv()
    CV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CV_OUT.open("w", encoding="utf-8") as f:
        f.write("# AUTO-GENERATED by bin/build_cv.py — do not edit by hand.\n")
        f.write("# Source of truth: _data/professor.yml + _data/members.yml + _bibliography/papers.bib\n\n")
        yaml.dump(
            out,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=100,
        )
    print(f"Wrote {CV_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
