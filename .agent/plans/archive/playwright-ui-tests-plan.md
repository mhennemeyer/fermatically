# Plan: Playwright UI-Tests für fermatically

Erstellt: 2026-04-09
Status: ✅ Abgeschlossen (2026-04-09)

## Ziel

Echte Browser-basierte UI-Tests via Playwright einrichten – **nicht headless**, sondern mit sichtbarem Chrome-Browser. Da der HTML-Source statisch vorliegt (`site/`), ist dies ein idealer Testfall, um:

1. **Erfahrung mit Playwright-Feedback** zu sammeln (Was sieht man? Was kann man prüfen?)
2. **Tooling-Patterns** zu entwickeln (Setup, Konfiguration, CI-taugliche vs. lokale Tests)
3. **Erkenntnisse dokumentieren** für `~/.agent/` (projektübergreifend nutzbar)

## Ergebnis

**38 Tests** in 3 Spec-Dateien, alle grün (~10s Laufzeit):
- `smoke.spec.ts` – 6 Tests (Landing Page, Titel, Theme-Toggle, Grundlagen-Artikel, Vorwissen, Navigation)
- `content.spec.ts` – 26 Tests (MathJax-Rendering ×18 Artikel, interne Links ×3, Bilder, Responsive ×3+1)
- `interaction.spec.ts` – 6 Tests (Theme-Toggle, Such-Dialog, Search-Index, TOC, Navigation, Deep-Links)

**Erkenntnisse** dokumentiert in `~/.agent/learnings/playwright-ui-testing.md` (183 Zeilen).

## Phasen

### Phase 1: Setup & Infrastruktur ✅

- [x] `package.json` initialisiert (im Projektroot)
- [x] Playwright installiert (`@playwright/test` + `serve`)
- [x] Playwright-Config erstellt (`playwright.config.ts`)
  - `headless: true` (Default), `--headed` Flag für sichtbaren Browser
  - Chromium als Zielbrowser
  - BaseURL: `http://127.0.0.1:8100`
  - Screenshot/Video/Trace on-failure aktiviert
- [x] Test-Verzeichnis angelegt: `tests/ui/` + `tests/ui/helpers/`
- [x] npm-Scripts definiert: `test:ui`, `test:ui:headless`, `test:ui:debug`
- [x] `.gitignore` erweitert: `node_modules/`, `test-results/`, `playwright-report/`, `playwright/.cache/`
- [x] Serve-Mechanismus via `npx serve site -p 8100` (webServer in Config)

### Phase 2: Grundlegende Smoke-Tests ✅

- [x] **Landing Page** – Titel „fermatically", Navigation sichtbar
- [x] **Theme-Toggle** vorhanden
- [x] **Grundlagen-Artikel** – Seite lädt, Überschrift vorhanden
- [x] **MathJax** – Formeln gerendert (mjx-container sichtbar)
- [x] **Vorwissen-Seite** – Seite lädt, Admonitions geprüft
- [x] **Navigation** – Sidebar vorhanden, Link klickbar

### Phase 3: Content-Verifikation ✅

- [x] **MathJax-Rendering** über alle 18 Artikel geprüft
  - mjx-container vorhanden + keine Raw-LaTeX-Commands im Text
  - **Erkenntnis**: MathJax v3 lässt $$-Delimiter als Textknoten im DOM (Artefakte)
  - **Lösung**: DOM-Klon bereinigen + $$-Blöcke per Regex entfernen, nur Commands prüfen
- [x] **Interne Links** – Keine toten Links auf Landing Page, Grundlagen, Beweis-Bereich
  - **Erkenntnis**: Relative Links müssen gegen `window.location.href` aufgelöst werden
- [x] **Bilder & Assets** – Alle Bilder laden erfolgreich
- [x] **Responsive Layout** – Desktop, Tablet, Mobil ohne Overflow (Landing Page)
  - **Erkenntnis**: MathJax-Formeln überlaufen bei 375px (dokumentiert, CSS-Fix empfohlen)

### Phase 4: Interaktions-Tests ✅

- [x] **Theme-Toggle** – Klick wechselt Farbschema (default → slate)
- [x] **Such-Dialog** – Öffnet sich, Search-Index ladbar und enthält Inhalte
  - **Erkenntnis**: MkDocs Search Worker initialisiert sich nicht mit `npx serve`
  - **Workaround**: Search-Index direkt via HTTP prüfen
- [x] **Table of Contents** – Einträge vorhanden, klickbar, Anker-Navigation
- [x] **Navigation** – Sections expandiert (navigation.expand), Deep-Links funktionieren

### Phase 5: Erkenntnisse & Dokumentation ✅

- [x] **Erkenntnisse-Dokument** erstellt: `~/.agent/learnings/playwright-ui-testing.md`
  - Setup-Patterns, MkDocs Material DOM-Struktur, MathJax-Fallstricke
  - Headless vs. Headed, Screenshot/Video-Nutzen, Selektoren-Best-Practices
  - Relative Links, Search-Worker-Problem, Mobile-Overflow
- [x] **Wiederverwendbare Helpers**: `mathjax.ts` + `navigation.ts`
