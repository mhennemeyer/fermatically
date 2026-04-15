# UI-Testing-Leitfaden

Erstellt: 2026-04-15
Status: Aktiv

## Überblick

Die Playwright-Tests prüfen die gebaute MkDocs-Seite gegen einen lokalen Webserver (`npx serve site -p 8100`). Vor dem Ausführen muss die Seite mit `mkdocs build --strict` gebaut werden.

## Voraussetzungen

```bash
npm install                # Playwright + serve installieren
npx playwright install     # Browser-Binaries installieren
pip3 install -r requirements.txt  # MkDocs + Plugins
```

## Tests ausführen

```bash
# 1. Seite bauen (0 Warnings = Pflicht)
python3 -m mkdocs build --strict

# 2. Alle Tests ausführen
npx playwright test

# 3. Nur eine Test-Datei ausführen
npx playwright test tests/ui/i18n.spec.ts

# 4. Mit sichtbarem Browser (Debug)
npx playwright test --headed

# 5. HTML-Report anzeigen
npx playwright show-report
```

## Test-Struktur

```
tests/ui/
├── smoke.spec.ts       – Grundlegende Seitenladung, Navigation, Theme-Toggle
├── content.spec.ts     – MathJax-Rendering, interne Links, Bilder, Responsive Layout
├── interaction.spec.ts – Interaktive Elemente (Suche, Dark Mode, etc.)
├── i18n.spec.ts        – Sprachumschalter, DE/EN-Seiten, 404-Prüfung
└── helpers/
    ├── mathjax.ts      – MathJax-Rendering-Prüfungen
    └── navigation.ts   – Sidebar, Link-Collection, Navigation-Helpers
```

## Wann Tests schreiben/anpassen?

| Änderung | Aktion |
|----------|--------|
| Neue Seite/Artikel hinzugefügt | Link-Tests in `content.spec.ts` decken das automatisch ab |
| Neue Sprache hinzugefügt | `i18n.spec.ts` erweitern |
| Navigation geändert | `smoke.spec.ts` prüfen |
| MathJax/Plugin-Konfiguration | `content.spec.ts` ausführen |
| Deployment-Änderung | Alle Tests gegen `mkdocs build` Output ausführen |

## Wichtige Hinweise

- **`npx serve`** hat kein Trailing-Slash-Redirect wie GitHub Pages. URLs wie `/en/` werden zu `/en` aufgelöst. Tests sollten daher `toContain('/en')` statt `toContain('/en/')` verwenden.
- **`mkdocs build --strict`** muss immer mit 0 Warnings durchlaufen, bevor Tests sinnvoll sind.
- Tests laufen gegen den lokalen Build in `site/`, nicht gegen die Live-Seite.
- Bei 404-Problemen nach Deploy: Erst lokal mit `mkdocs build --strict` + `npx playwright test` prüfen, dann ggf. auf GitHub Actions Workflow-Logs schauen.

## Workflow bei Änderungen

1. Änderungen an `docs/` oder `mkdocs.yml` vornehmen
2. `python3 -m mkdocs build --strict` → 0 Warnings
3. `npx playwright test` → alle Tests grün
4. Commit & Push → GitHub Actions baut und deployt automatisch
