# Log: fermatically

## 2026-04-01 – Projektanalyse & Phase 5 Start

### Analyse
- Projekt vollständig gesichtet: 18 Topics (DE+EN) in `topics/` fertig geschrieben (~4000 Zeilen je Sprache)
- `docs/`-Verzeichnis enthält nur Platzhalter (~16 Zeilen pro Datei, "Artikel in Vorbereitung")
- MkDocs-Konfiguration (`mkdocs.yml`) funktional mit Material-Theme, MathJax, Navigation
- `topics/img/` existiert, aber enthält keine Header-Bilder
- Uncommittete Änderungen: EN-Status-Updates in `status.md` und `artikelserie-plan.md`
- Kein `log.md` vorhanden → erstellt

### Erledigt
- `scripts/sync_topics_to_docs.sh` erstellt: kopiert 18 `article_de.md` aus `topics/` nach `docs/`
- `scripts/fix_docs_links.py` erstellt: schreibt alle internen Links von topics/-Pfaden auf docs/-Pfade um
- MkDocs build: **0 Warnings, 0 Errors**
- `status.md` und `artikelserie-plan.md` aktualisiert (Phase 5a abgeschlossen)

### Nächste Schritte (Phase 5b)
- Navigation aus `requires`-Frontmatter automatisch generieren
- Coolify-Deployment konfigurieren und testen

## 2026-04-01 – Stilüberarbeitung nach Guideline

### Erledigt
- `.agent/guideline.md` gelesen: Sachlich-technischer Stil, kein „wir/ich", Fachzitate, Nominalstil
- `.agent/plans/stilueberarbeitung-plan.md` erstellt
- **18 Artikel überarbeitet** (4 Grundlagen + 6 Werkzeuge + 8 Beweis):
  - Alle „wir/ich"-Formulierungen durch beschreibende Konstruktionen ersetzt
  - Metaphern und schmückende Adjektive entfernt
  - Fachzitate als Blockquotes eingefügt (Singh, Boston, Edwards, Wiles, Artin, Serre, Mazur, etc.)
  - Zusammenfassungen auf Nominalstil umgestellt
- Sync nach `docs/` und MkDocs build: **0 Warnings, 0 Errors**

### Nächste Schritte
- Zweiter Zitat-Durchgang nach Aufbau der Mathematik-KB
- Statisches Hosting einrichten (Cloudflare Pages / Netlify)

## 2026-04-26 – Plan-Review & Archivierung

### Erledigt
- Alle aktiven Pläne in `.agent/plans/` gegen aktuellen Projektstand geprüft
- Drei abgeschlossene Pläne ins Archiv verschoben:
  - `deployment-plan.md` (GitHub Pages live, Status: Abgeschlossen ✅)
  - `sidebar-restructuring.md` (Nav umgebaut, Status: Umgesetzt ✅)
  - `playwright-ui-tests-plan.md` (UI-Tests grün, Status: ✅ Abgeschlossen)
- Aktiv verbleiben: `artikelserie-plan.md` (Master), `poincare-perelman-plan.md` (Akt 1–3 offen), `vor-vorwissen-plan.md` (geparkt)

### Empfohlener nächster Schritt
- Poincaré-Plan Schritt 8 angehen: Überblicksseite `docs/poincare/index.md` ausformulieren als Einstieg in den ersten geschriebenen Akt.

## 2026-04-26 – Poincaré-Überblicksseite (Plan-Schritt 8)

### Erledigt
- `docs/poincare/index.de.md` und `docs/poincare/index.md` von Stub auf vollständige Roadmap ausgebaut (~107 Zeilen je Sprache):
  - Vermutungs-Statement (1904, Smale 1961, Freedman 1982, Perelman 2002–2003) und Einordnung über Hamiltons Ricci-Fluss
  - Drei-Akt-Roadmap mit Tabellen für alle 18 Folgeartikel (Topologie, Ricci-Fluss, Beweis), analog zu `flt-overview.de.md`
  - Vorwissen-Tipp (Block „Geometrie und Analysis (Aufbau)"), Querverweis zu FLT-Storyline
  - Quellenblock: 3 arXiv-Preprints mit Links + Morgan/Tian, Kleiner/Lott, Cao/Zhu, Hamilton 1982, O'Shea
- Frontmatter-Status `stub` → `active` in beiden Sprachversionen
- Lokales venv (`.venv/`) eingerichtet (kein venv vorhanden), `pip install -r requirements.txt`
- `mkdocs build --strict`: 0 Warnings, 2.62 s (Vorwissen-Link auf `vorwissen/index.md` umgebogen, da `vorwissen/geometrie-analysis/` keine `index.md` hat)
- `.agent/plans/poincare-perelman-plan.md`: Schritt 8 als erledigt markiert

### Nächste Schritte
- Plan-Schritt 9: Akt 1 schreiben, beginnend mit `topologie/01-was-ist-topologie` und `02-mannigfaltigkeiten` (DE+EN)
- Optional: `vorwissen/geometrie-analysis/index.md` anlegen, damit aus dem Vorwissen-Block direkt verlinkt werden kann
- Mobile-CSS-Fix für MathJax-Overflow als Beifang

## 2026-04-27 – Akt 1, Artikel 01 + 02 (Plan-Schritt 9, Teil 1)

### Erledigt
- `docs/poincare/topologie/01-was-ist-topologie.{de.,}md` von Stub auf vollständigen Artikel ausgebaut (~165 Zeilen je Sprache):
  - 7 Abschnitte: Geometrie ohne Lineal, Stetigkeit, Homöomorphie, topologische Invarianten (Zusammenhang/Kompaktheit/Dimension), kurze Geschichte (Euler/Riemann/Poincaré/Hausdorff), Bezug zur Vermutung, Ausblick
  - Fachzitate Lee, Hatcher; Querverweise auf Artikel 02–05 und Vorwissen-Index
  - Quellenblock: Hatcher, Lee, Poincaré *Analysis Situs*, Hausdorff *Grundzüge*
- `docs/poincare/topologie/02-mannigfaltigkeiten.{de.,}md` von Stub auf vollständigen Artikel ausgebaut (~190 Zeilen je Sprache):
  - 7 Abschnitte: lokal euklidisch (Karte/Atlas), Beispiele Dim 1–3, geschlossen/offen/mit Rand, glatte Mannigfaltigkeiten (inkl. exotische 7-Sphäre, R^4-Phänomen), Riemannsche Mannigfaltigkeiten, Beispiele für die Storyline ($S^3$, $T^3$, Linsenräume), Ausblick
  - Quellen: Lee (Top./Smooth Manifolds), Milnor 1956, Moise 1952
- Frontmatter-Status `stub` → `draft` in allen vier Dateien
- `mkdocs build --strict`: 0 Warnings, 2.31 s
- `.agent/plans/poincare-perelman-plan.md`: Schritt 9 als „in Arbeit" markiert (2/5 Topologie-Artikel + Index offen)

### Nächste Schritte
- Akt 1 fortsetzen: `03-sphaere-einfacher-zusammenhang`, `04-was-ist-poincare-vermutung`, `05-geometrisierungs-vermutung` und `topologie/index.md` (DE+EN)
- Anschließend Akt 2 (Ricci-Fluss) – dort spätestens lohnt sich auch die inhaltliche Befüllung von Vorwissen „Geometrie und Analysis (Aufbau)"
