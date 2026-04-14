# fermatically

Eine umfangreiche Plattform mit dem Schwerpunkt auf das Verständnis der großen Beweise von lange Zeit unbewiesenen Vermutungen – von **elementarer Schulmathematik** bis zu den **fortgeschrittenen Methoden** in Andrew Wiles' Beweis von Fermats letztem Satz.

**Website:** [fermatically.com](https://fermatically.com)

## Lokal starten

```bash
# Dependencies installieren (einmalig)
pip install -r requirements.txt

# Plattform starten (Port 8100 – parallel zu LambdaPy auf 8000)
mkdocs serve
```

Dann im Browser öffnen: **http://127.0.0.1:8100/**

## Struktur

Die Plattform ist in **eigenständige, querverweisbare Topics** gegliedert:

### 🔢 Grundlagen – Elementare Zahlentheorie
1. **Was ist Fermats letzter Satz?** – Geschichte, Fermat, 350 Jahre Suche
2. **Der Beweis für n=4** – Fermats eigener Beweis (Infinite Descent)
3. **Primzahlen und warum sie reichen** – Reduktion auf Primzahl-Exponenten
4. **Der Beweis für n=3** – Euler, Gauß, algebraische Zahlen

### 🔧 Werkzeuge – Die Sprache der modernen Mathematik
5. **Gruppen** – Symmetrie als Sprache der Mathematik
6. **Ringe und Körper** – Die Welt jenseits der rationalen Zahlen
7. **Galois-Theorie** – Warum Gleichungen keine Lösungsformeln haben
8. **p-adische Zahlen** – Eine andere Art, Zahlen zu betrachten
9. **Elliptische Kurven** – Von Diophant zu Kryptographie
10. **Modulformen** – Symmetrische Funktionen der oberen Halbebene

### 🏔️ Der Beweis – Fermats letzter Satz (Wiles, 1995)
11. **Die Taniyama-Shimura-Vermutung** – Jede elliptische Kurve ist modular
12. **Freys Idee und Ribets Theorem** – TSV ⟹ FLT
13. **Galois-Darstellungen** – Elliptische Kurven als Matrizen
14. **Deformationstheorie** – Wie man Darstellungen verbiegt
15. **R = T** – Das Herz von Wiles' Beweis
16. **Der Taylor-Wiles-Trick** – Der minimale Fall
17. **Der 3-5-Switch und der Abschluss** – Das Finale
18. **Was danach kam** – Vollständige TSV, Langlands-Programm

### Zukünftige Themen
- **Poincaré-Vermutung** (Perelman, 2003)
- **Moderne Beweismethoden** (HoTT, formale Verifikation in Lean/Coq)

## Technologie

- **MkDocs** mit **Material for MkDocs** Theme
- **MathJax** für LaTeX-Rendering
- Port **8100** (kein Konflikt mit LambdaPy auf 8000)

## Quellen

- `resources/wiles.pdf` – Original-Scan des Wiles-Papers (Annals of Mathematics, 1995)
- `resources/wiles_parsed/wiles.md` – Vollständige Transkription (GPT-4o Vision, 350 KB, LaTeX-Formeln)
- `resources/Fermats-last-theorem-pdf.pdf` – Nigel Boston, "The Proof of Fermat's Last Theorem" (Lehrbuch, 2003)
- `resources/fermats_last_theorem_boston.md` – Markdown-Extraktion des Boston-Lehrbuchs (180k Zeichen)

## Aktueller Stand

**Phase 1–4 abgeschlossen** (März 2026):

- ✅ MkDocs-Plattform mit Material-Theme aufgesetzt (Port 8100)
- ✅ Vollständige `topics/`-Struktur mit 18 Topics (Multi-Topic-Architektur)
- ✅ 18 detaillierte Outlines (`outline.md`) mit Gliederung, Kernaussagen und Querverweisen
- ✅ `topics/TEMPLATE.md`, `topics/DEPENDENCIES.md`, Kategorien (5 × DE+EN)
- ✅ **4 Grundlagen-Artikel** geschrieben (elementare Zahlentheorie, ~700 Zeilen)
- ✅ **6 Werkzeug-Artikel** geschrieben (Gruppen, Ringe/Körper, Galois, p-adisch, Ell. Kurven, Modulformen, ~1260 Zeilen)
- ✅ **8 Beweis-Artikel** geschrieben (Fermat-Wiles, ~2060 Zeilen) – von Taniyama-Shimura bis zum Langlands-Programm
- ✅ Insgesamt **18 deutsche Artikel** mit ~4020 Zeilen, LaTeX-Formeln, MkDocs-Admonitions und Querverweisen

**Nächste Phase:** Statisches Deployment einrichten (z.B. GitHub Pages, Cloudflare Pages, Netlify), Navigation aus `requires`-Frontmatter generieren

## Projektverzeichnis

```
fermatically/
├── mkdocs.yml              ← MkDocs-Konfiguration (Port 8100)
├── requirements.txt        ← Python-Dependencies
├── docs/                   ← Website-Content (Markdown + MathJax)
│   ├── index.md            ← Landing Page
│   ├── about.md            ← Über das Projekt
│   ├── quellen.md          ← Quellenverzeichnis
│   ├── grundlagen/         ← Elementare Zahlentheorie (4 Artikel)
│   ├── werkzeuge/          ← Algebra, Analysis, … (6 Artikel)
│   └── fermat-wiles/       ← Der Beweis (8 Artikel)
├── topics/                 ← Eigenständige Topics (Artikel + Outlines)
│   ├── TEMPLATE.md         ← Vorlage für neue Artikel
│   ├── DEPENDENCIES.md     ← Abhängigkeitsgraph
│   ├── elementare-zahlentheorie/  ← 4 Grundlagen-Artikel
│   ├── gruppen-und-symmetrie/     ← Werkzeug-Topic
│   ├── ringe-und-koerper/         ← Werkzeug-Topic
│   ├── galois-theorie/            ← Werkzeug-Topic
│   ├── p-adische-zahlen/          ← Werkzeug-Topic
│   ├── elliptische-kurven/        ← Werkzeug-Topic
│   ├── modulformen/               ← Werkzeug-Topic
│   └── fermat-wiles/              ← 8 Beweis-Artikel
├── categories/             ← Themen-Kategorien (5 × DE+EN)
├── authors/                ← Autoren-Profile
└── resources/              ← Quellen (PDFs, Transkriptionen)
```
