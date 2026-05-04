# Plan-Archiv

Alle hier liegenden Pläne sind **vollständig abgeschlossen** und nur noch als Referenz gedacht (Begründungen, Quellenstrategie, Lessons Learned). Nicht mehr aktiv pflegen.

| Datei | Abgeschlossen | Inhalt |
|-------|---------------|--------|
| [`namensfindung.md`](namensfindung.md) | 2026-03-31 | Projektname & Domain – Entscheidung: `fermatically.com`. |
| [`wiles_pdf_parsing.md`](wiles_pdf_parsing.md) | 2026-03-28 | Erfassung & Strukturierung von `resources/wiles.pdf` (109 S.). Kein expliziter Status-Header, aber Aufgabe erledigt (PDF wurde geparst, Inhalte in `resources/wiles_outline.md` etc. geflossen). |
| [`stilueberarbeitung-plan.md`](stilueberarbeitung-plan.md) | 2026-04-01 | Stilüberarbeitung aller 18 Fermat-Artikel nach `guideline.md`. |
| [`elementares-vorwissen-plan.md`](elementares-vorwissen-plan.md) | 2026-04-09 | Aufbau des Vorwissen-Bereichs (22 Themen DE+EN). |
| [`playwright-ui-tests-plan.md`](playwright-ui-tests-plan.md) | 2026-04-09 | Playwright-UI-Tests (MathJax, Sprachumschalter, Navigation). |
| [`deployment-plan.md`](deployment-plan.md) | 2026-04-16 | Statisches Deployment via GitHub Actions, MkDocs Material. |
| [`github-pages-go-live.md`](github-pages-go-live.md) | 2026-04-16 | GitHub-Pages-Go-Live inkl. Custom-Domain `fermatically.com`. |
| [`sidebar-restructuring.md`](sidebar-restructuring.md) | 2026-04-21 | Seitenleiste auf FLT als Hauptstoryline umstrukturiert. |
| [`poincare-perelman-plan.md`](poincare-perelman-plan.md) | 2026-04-28 | Beweis-Topic Poincaré–Perelman: Akte 1–3 inhaltlich vollständig (DE+EN), Vorwissen „Geometrie und Analysis (Aufbau)" befüllt. |

## Konvention

Beim Archivieren eines Plans:

1. Status-Header auf `✅ Abgeschlossen (YYYY-MM-DD)` setzen.
2. Plan nach `archive/` verschieben.
3. Diese Tabelle ergänzen.
4. In `../README.md` den aktiven Eintrag entfernen, in `.agent/log.md` einen Eintrag spiegeln.
