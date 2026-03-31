# Plan: Mathematik-Plattform – Große Beweise verstehen

Erstellt: 2026-03-30
Aktualisiert: 2026-03-31
Status: Phase 1+2+3 abgeschlossen (v2 – Multi-Topic-Architektur)

## Vision

Eine umfangreiche **Mathematik-Plattform** mit dem Schwerpunkt auf das Verständnis der großen Beweise von lange Zeit unbewiesenen Vermutungen:

- **Fermats letzter Satz** (Wiles, 1995)
- **Poincaré-Vermutung** (Perelman, 2003) – *geplant*
- **Weitere** (Vier-Farben-Satz, Keplersche Vermutung, …) – *Zukunft*

Zusätzliches Ziel: Analyse, ob durch Anwendung **moderner Methoden** (z.B. Homotopie-Typentheorie / HoTT, formale Verifikation in Lean/Coq) alternative oder einfachere Beweismöglichkeiten existieren.

Die Artikel werden als Markdown im Source verwaltet, als Website veröffentlicht und mit medium.com synchronisiert – analog zur Topics-Struktur im LambdaPy-Projekt.

## Kernprinzip: Eigenständige, querverweisbare Topics

Statt einer monolithischen Serie mit 4 Teilen wird die Plattform in **eigenständige Topics** aufgeteilt:

1. **Grundlagen-Topics** (Elementare Mathematik, Algebra, Analysis, …) – wiederverwendbar für mehrere Beweis-Topics
2. **Werkzeug-Topics** (Galois-Theorie, Elliptische Kurven, Modulformen, …) – jeweils eigenständig, aber Voraussetzung für bestimmte Beweis-Topics
3. **Beweis-Topics** (Fermat/Wiles, Poincaré/Perelman, …) – das Herzstück, mit ausführlichen Querverweisen zu den Grundlagen- und Werkzeug-Topics
4. **Meta-Topics** (Moderne Methoden, HoTT, Formale Verifikation) – Querschnittsthemen

So kann z.B. das Topic „Gruppen" sowohl für den Fermat-Beweis als auch für Poincaré referenziert werden, ohne Inhalte zu duplizieren.

## Referenz: LambdaPy-Struktur

Das LambdaPy-Projekt verwendet folgende Konventionen:
- **Topics-Verzeichnis**: `topics/{serie-slug}/{nn-artikel-slug}/`
- **Pro Artikel**: `article_de.md`, `article_en.md`, optional `src/`, `tests/`, `outline.md`
- **Bilder**: `topics/img/` (shared)
- **Template**: `topics/TEMPLATE.md` (Anleitung für neue Topics)
- **Kategorien**: `topics/categories/{slug}/category_de.md` + `category_en.md`
- **Autoren**: `authors/{slug}/bio_de.md` + `bio_en.md`
- **Django-Import**: Management-Commands importieren Markdown → DB

## Vorgeschlagene Struktur

```
fermatically/
├── README.md
├── topics/
│   ├── TEMPLATE.md                         ← Vorlage für neue Artikel
│   ├── img/                                ← Shared Bilder
│   │
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │   GRUNDLAGEN (eigenständige Topics)
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │
│   ├── elementare-zahlentheorie/
│   │   ├── 01-was-ist-flt/                 ← Geschichte, Fermat, 350 Jahre
│   │   │   ├── article_de.md
│   │   │   ├── article_en.md
│   │   │   └── outline.md
│   │   ├── 02-beweis-n4/                   ← Fermats eigener Beweis (Infinite Descent)
│   │   ├── 03-primzahlen-reduktion/        ← Reduktion auf Primzahl-Exponenten
│   │   └── 04-beweis-n3/                   ← Euler, Gauß, algebraische Zahlen
│   │
│   ├── gruppen-und-symmetrie/
│   │   └── 01-gruppen/                     ← Symmetrie als Sprache der Mathematik
│   │
│   ├── ringe-und-koerper/
│   │   └── 01-ringe-koerper/               ← Die Welt jenseits der rationalen Zahlen
│   │
│   ├── galois-theorie/
│   │   └── 01-galois-theorie/              ← Warum Gleichungen keine Lösungsformeln haben
│   │
│   ├── p-adische-zahlen/
│   │   └── 01-p-adische-zahlen/            ← Eine andere Art, Zahlen zu betrachten
│   │
│   ├── elliptische-kurven/
│   │   └── 01-elliptische-kurven/          ← Von Diophant zu Kryptographie
│   │
│   ├── modulformen/
│   │   └── 01-modulformen/                 ← Symmetrische Funktionen der oberen Halbebene
│   │
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │   BEWEIS-TOPICS (das Herzstück)
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │
│   ├── fermat-wiles/                       ← DAS Fermat-Beweis-Topic
│   │   ├── 01-taniyama-shimura/            ← Jede elliptische Kurve ist modular
│   │   ├── 02-frey-ribet/                  ← TSV ⟹ FLT
│   │   ├── 03-galois-darstellungen/        ← Elliptische Kurven als Matrizen
│   │   ├── 04-deformationstheorie/         ← Wie man Darstellungen verbiegt
│   │   ├── 05-r-gleich-t/                  ← Das Herz von Wiles' Beweis
│   │   ├── 06-taylor-wiles-trick/          ← Der minimale Fall
│   │   ├── 07-3-5-switch/                  ← Das Finale
│   │   └── 08-was-danach-kam/              ← Vollständige TSV, Langlands
│   │
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │   META / QUERSCHNITT (Zukunft)
│   │── ── ── ── ── ── ── ── ── ── ── ── ── ── ──
│   │
│   ├── moderne-beweismethoden/             ← (Zukunft)
│   │   ├── 01-hott-einfuehrung/            ← Homotopie-Typentheorie
│   │   ├── 02-formale-verifikation/        ← Lean, Coq, Agda
│   │   └── 03-alternative-beweise/         ← Können moderne Methoden FLT vereinfachen?
│   │
│   └── poincare-perelman/                  ← (Zukunft)
│       └── ...
│
├── categories/                             ← Themen-Kategorien
│   ├── zahlentheorie/
│   │   ├── category_de.md
│   │   └── category_en.md
│   ├── algebra/
│   ├── analysis/
│   ├── topologie/
│   └── formale-methoden/
│
├── authors/
│   └── matthias-hennemeyer/
│       ├── bio_de.md
│       └── bio_en.md
│
└── resources/                              ← Bereits vorhanden
    ├── wiles.pdf
    ├── wiles_parsed/
    ├── Fermats-last-theorem-pdf.pdf
    └── fermats_last_theorem_boston.md
```

## Querverweissystem

Jeder Beweis-Artikel in `fermat-wiles/` enthält am Anfang einen **Voraussetzungen-Block**:

```markdown
---
title: "Galois-Darstellungen"
series: fermat-wiles
requires:
  - gruppen-und-symmetrie/01-gruppen
  - ringe-und-koerper/01-ringe-koerper
  - galois-theorie/01-galois-theorie
  - elliptische-kurven/01-elliptische-kurven
---
```

So wird klar, welche Grundlagen-Topics gelesen werden sollten, bevor man in den Beweis einsteigt. Die Website kann daraus automatisch Navigationshinweise generieren.

## Zuordnung: Alt → Neu

| Alter Plan (Teil/Nr.) | Neues Topic | Neuer Artikel |
|------------------------|-------------|---------------|
| Teil I / 01 – Was ist FLT? | `elementare-zahlentheorie` | `01-was-ist-flt` |
| Teil I / 02 – Beweis n=4 | `elementare-zahlentheorie` | `02-beweis-n4` |
| Teil I / 03 – Primzahlen | `elementare-zahlentheorie` | `03-primzahlen-reduktion` |
| Teil I / 04 – Beweis n=3 | `elementare-zahlentheorie` | `04-beweis-n3` |
| Teil II / 05 – Gruppen | `gruppen-und-symmetrie` | `01-gruppen` |
| Teil II / 06 – Ringe/Körper | `ringe-und-koerper` | `01-ringe-koerper` |
| Teil II / 07 – Galois-Theorie | `galois-theorie` | `01-galois-theorie` |
| Teil II / 08 – p-adische Zahlen | `p-adische-zahlen` | `01-p-adische-zahlen` |
| Teil II / 09 – Ell. Kurven | `elliptische-kurven` | `01-elliptische-kurven` |
| Teil II / 10 – Modulformen | `modulformen` | `01-modulformen` |
| Teil III / 11 – Taniyama-Shimura | `fermat-wiles` | `01-taniyama-shimura` |
| Teil III / 12 – Frey/Ribet | `fermat-wiles` | `02-frey-ribet` |
| Teil III / 13 – Galois-Darst. | `fermat-wiles` | `03-galois-darstellungen` |
| Teil III / 14 – Deformation | `fermat-wiles` | `04-deformationstheorie` |
| Teil III / 15 – R = T | `fermat-wiles` | `05-r-gleich-t` |
| Teil III / 16 – Taylor-Wiles | `fermat-wiles` | `06-taylor-wiles-trick` |
| Teil III / 17 – 3-5-Switch | `fermat-wiles` | `07-3-5-switch` |
| Teil IV / 18 – Ausblick | `fermat-wiles` | `08-was-danach-kam` |

## Vorteile der neuen Struktur

1. **Wiederverwendbarkeit**: Grundlagen-Topics (Gruppen, Galois, …) können für mehrere Beweis-Topics dienen
2. **Unabhängiges Wachstum**: Neue Topics (Poincaré, HoTT, …) können jederzeit hinzugefügt werden
3. **Eigenständige Lesbarkeit**: Jedes Topic ist in sich abgeschlossen verständlich
4. **Flexible Reihenfolge**: Leser können je nach Vorwissen Grundlagen überspringen
5. **Skalierbarkeit**: Die Plattform kann organisch wachsen, ohne bestehende Struktur zu brechen

## Umsetzungsschritte

### Phase 1: Grundstruktur anlegen
1. [x] `topics/TEMPLATE.md` erstellen (mit Frontmatter-Schema inkl. `requires`)
2. [x] Verzeichnisstruktur für alle Topics anlegen (Grundlagen + fermat-wiles)
3. [x] `topics/img/` Verzeichnis anlegen
4. [x] `categories/` mit Kategorie-Dateien anlegen
5. [x] `authors/matthias-hennemeyer/` mit Bio-Dateien anlegen

### Phase 2: Outlines erstellen
6. [x] Outlines für Grundlagen-Topics (elementare-zahlentheorie, gruppen, ringe, galois, p-adisch, ell. kurven, modulformen)
7. [x] Outlines für fermat-wiles Topic (8 Artikel)
8. [x] Abhängigkeitsgraph dokumentieren (welches Topic setzt welche voraus)

### Phase 3: Artikel schreiben (Grundlagen zuerst)
9. [x] `elementare-zahlentheorie` – 4 Artikel (DE)
10. [x] Werkzeug-Topics – je 1 Artikel (DE)
11. [ ] Englische Versionen nachziehen

### Phase 4: Artikel schreiben (Fermat-Beweis)
12. [ ] `fermat-wiles` – 8 Artikel (DE) mit Querverweisen
13. [ ] Englische Versionen nachziehen

### Phase 5: Website-Publikation
14. [ ] Entscheidung: Django (wie LambdaPy) vs. SSG (Hugo/Jekyll)
15. [ ] Build-Pipeline für Markdown → HTML (mit LaTeX-Rendering via KaTeX)
16. [ ] Automatische Navigation aus `requires`-Frontmatter generieren
17. [ ] Deployment-Setup

### Phase 6: Medium-Synchronisation
18. [ ] Medium.com API-Integration
19. [ ] Canonical-URL-Strategie

### Phase 7: Plattform erweitern (Zukunft)
20. [ ] `moderne-beweismethoden` Topic (HoTT, Lean/Coq, alternative Beweise)
21. [ ] `poincare-perelman` Topic
22. [ ] Weitere große Beweise

## Entscheidungen (offen)

- **Projektname**: `fermatically`
  → Empfehlung: Vorerst beibehalten, Umbenennung in Phase 5 wenn Website-Domain feststeht
- **LaTeX-Rendering**: KaTeX (schnell, statisch) vs. MathJax (vollständiger)?
  → Empfehlung: KaTeX für Website, MathJax als Fallback
- **Bilingual von Anfang an?** Oder erst DE, dann EN?
  → Empfehlung: Erst DE komplett pro Topic, dann EN nachziehen
- **Django vs. Static Site?** LambdaPy nutzt Django, aber für eine Artikelplattform könnte ein SSG ausreichen
  → Empfehlung: Zunächst nur Topics-Struktur (Markdown im Repo), Website-Entscheidung in Phase 5
- **Grundlagen-Topics: Einzel- oder Mehrartikel?** Aktuell je 1 Artikel pro Werkzeug-Topic. Bei Bedarf erweiterbar auf Serien (z.B. `galois-theorie/01-grundbegriffe`, `02-hauptsatz`, …)
  → Empfehlung: Mit je 1 Artikel starten, bei Bedarf erweitern

## Quellenstrategie

| Topic / Artikel | Primärquelle |
|-----------------|-------------|
| `elementare-zahlentheorie/01-was-ist-flt` | Allgemein / Geschichte |
| `elementare-zahlentheorie/02-beweis-n4` | Fermat (Infinite Descent), Boston Kap. 1 |
| `elementare-zahlentheorie/03-primzahlen` | Boston Kap. 1–2 |
| `elementare-zahlentheorie/04-beweis-n3` | Boston Kap. 2 (Euler/Gauß) |
| `gruppen-und-symmetrie/01-gruppen` | Boston Kap. 3 |
| `ringe-und-koerper/01-ringe-koerper` | Boston Kap. 3–4 |
| `galois-theorie/01-galois-theorie` | Boston Kap. 4 |
| `p-adische-zahlen/01-p-adische-zahlen` | Boston Kap. 5 |
| `elliptische-kurven/01-elliptische-kurven` | Boston Kap. 6, Wiles §1 |
| `modulformen/01-modulformen` | Boston Kap. 7, Wiles §1 |
| `fermat-wiles/01-taniyama-shimura` | Boston Kap. 8, Wiles §1–2 |
| `fermat-wiles/02-frey-ribet` | Boston Kap. 9, Wiles Intro |
| `fermat-wiles/03-galois-darstellungen` | Wiles §1, Boston Kap. 10 |
| `fermat-wiles/04-deformationstheorie` | Wiles §1.2–1.6 |
| `fermat-wiles/05-r-gleich-t` | Wiles §2–3 |
| `fermat-wiles/06-taylor-wiles-trick` | Wiles §3.3, Taylor-Wiles 1995 |
| `fermat-wiles/07-3-5-switch` | Wiles §5 |
| `fermat-wiles/08-was-danach-kam` | Breuil-Conrad-Diamond-Taylor 2001 |
