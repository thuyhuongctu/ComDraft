# ComDraft

**Teaching materials for *Communication and Document Drafting Skills* (EC1103)**
Bộ học liệu giảng dạy trực tiếp — Học phần Kỹ năng giao tiếp và soạn thảo văn bản

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22003676.svg)](https://doi.org/10.5281/zenodo.22003676)
![course](https://img.shields.io/badge/course-EC1103-AC4D33?style=flat-square)
![credits](https://img.shields.io/badge/credits-3%20(2%3A1)-DC756A?style=flat-square)
![license](https://img.shields.io/badge/license-All%20rights%20reserved-red?style=flat-square)

**Author** — Do Thuy Huong (Đỗ Thùy Hương), [ORCID 0000-0002-7711-2487](https://orcid.org/0000-0002-7711-2487)
Lecturer, Faculty of Economics and Law, Vinh Long University of Technology Education;
PhD Candidate, School of Economics, Can Tho University.

Every slide, figure, question, script and video in this repository was authored by the
lecturer named above for the classes she teaches in person. Nothing here is derived from
a colleague's material.

---

## The revision app

The repository root is also a small offline-first web app for students —
**ComDraft**, published from this repository via GitHub Pages. It serves the whole
200-question bank with the explanation for every question, and needs no account, no
server and no network once it has been opened for the first time.

- **Practice mode** marks each answer immediately and shows why it is right or wrong;
  **test mode** withholds the marking until the end.
- Pick a single chapter or mix all five, choose 10 / 20 / 40 / all questions, and
  filter by cognitive level (recall, comprehension, application).
- Questions and options are shuffled, so a second attempt is not the same paper.
- The result screen breaks the score down by cognitive level and reprints every
  missed question with its explanation; one button re-runs just the ones missed.
- Students can star hard questions and drill only those later.
- Progress and best scores live in the browser's own storage — nothing leaves the
  device, so no student data is collected.
- Installable to a phone's home screen, and works fully offline.

Built as plain HTML, CSS and JavaScript with no framework and no build step: the
question data is the same `registerBank(...)` format used by the author's earlier
EnQuiz app, so a chapter can be edited and reloaded without touching the code.

## What this repository holds

A complete, ready-to-teach package for a 3-credit undergraduate course (2 credits of
theory, 1 credit of computer-lab practice), built for the 261b cohort, first semester of
the 2026–2027 academic year.

| Folder | Contents |
|---|---|
| `slides/` | Five lecture decks, one per chapter — 16 to 20 slides each, every slide carrying a speaker-note script for PowerPoint Presenter View |
| `practice/` | Three computer-lab workbooks: document formality, administrative documents, commercial documents |
| `quiz/` | A 200-question bank (40 per chapter) in two Word editions — with answers for the lecturer, question-only for students — plus the same bank as JavaScript data ready for a quiz app |
| `videos/` | Eight Full-HD videos: five chapter revision videos and three lab walkthroughs, with the narration script in JSON |
| `figures/` | Eight author-drawn diagrams rendered from code, plus the course persona artwork |
| `scripts/` | The generators that produce everything above — decks, figures, question bank, videos |

### The five chapters

1. **Tổng quan về giao tiếp trong kinh doanh** — nature of communication, the five-stage model and noise, verbal and non-verbal channels, forms, influencing factors, five principles
2. **Các kỹ năng giao tiếp chuyên nghiệp** — first impressions and the 4×20 rule, business etiquette, presenting, listening and questioning, telephone skills
3. **Giao tiếp trong các tình huống đặc thù** — internal communication, customers and the LAST complaint procedure, partners, state agencies and press, banquet etiquette, cross-cultural work
4. **Đàm phán trong kinh doanh** — nature and styles of negotiation, the five-stage process, BATNA and ZOPA, negotiation skills, recognising common tactics
5. **Soạn thảo và trình bày văn bản** — document types, the nine formality components of Decree 30/2020/NĐ-CP, five administrative documents, commercial documents

### The three lab sessions

Each workbook carries a five-step teaching rhythm (demonstrate → follow along → work
alone → peer-review → submit and revise), the exact Word menu paths for each formatting
step, a list of the mistakes students actually make, an eight-point self-check list, the
assignment and the marking scheme.

A single business case — a company buying twenty computers — runs from the Chapter 4
negotiation role-play through the Chapter 5 document chain into both lab assignments, so
students see one continuous professional workflow rather than disconnected exercises.

---

## How the materials were built

Everything is generated from source, so the whole package can be rebuilt after any edit:

```bash
node scripts/build_decks.js          # chapters 1–4
node scripts/build_ch5_practice.js   # chapter 5 and the three lab workbooks
python3 scripts/make_figs.py         # the eight diagrams
python3 scripts/add_images.py        # place figures and persona artwork
python3 scripts/apply_upgrade.py     # speaker notes, section dividers, stat slides
node  scripts/build_bank_docx.js     # the question bank, both editions
python3 scripts/build_videos.py      # the eight videos
```

Decks are produced with **PptxGenJS**; figures are rendered from hand-written HTML and CSS
through headless Chromium; the question bank is written with **docx**; videos combine the
rendered slides with Vietnamese speech from **Piper** and are assembled with **FFmpeg**.
The visual identity — colour, typography, layout grammar — is the author's own and is
documented in `scripts/design.js`.

---

## Using these materials

Free to use for personal study and for teaching the students of this course. Any other
use — republishing the slides or the question bank elsewhere, uploading the videos to a
channel that is not the author's, reusing the material under another lecturer's or an
institution's name, commercial use, or derivative works — requires the author's written
permission.

When you use anything from this repository, cite it. See `CITATION.cff`, or:

> Do, T. H. (2026). *ComDraft: teaching materials for Communication and Document Drafting
> Skills (EC1103)* (Version 1.0) [Data set]. Vinh Long University of Technology Education.
> https://doi.org/10.5281/zenodo.22003676

The DOI above is the *concept DOI* — it always resolves to the newest release. To cite
this exact release instead, use [10.5281/zenodo.22003677](https://doi.org/10.5281/zenodo.22003677).

---

## Related work by the same author

- **[EnQuiz](https://github.com/thuyhuongctu/EnQuiz)** — an offline-first bilingual
  revision app for an Entrepreneurship course
  ([10.5281/zenodo.21850735](https://doi.org/10.5281/zenodo.21850735))

---

© 2026 Do Thuy Huong. All rights reserved. See `LICENSE`.
