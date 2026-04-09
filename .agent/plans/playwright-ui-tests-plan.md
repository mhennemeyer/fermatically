# Plan: Playwright UI-Tests für fermatically

Erstellt: 2026-04-09
Status: Neu

## Ziel

Echte Browser-basierte UI-Tests via Playwright einrichten – **nicht headless**, sondern mit sichtbarem Chrome-Browser. Da der HTML-Source statisch vorliegt (`site/`), ist dies ein idealer Testfall, um:

1. **Erfahrung mit Playwright-Feedback** zu sammeln (Was sieht man? Was kann man prüfen?)
2. **Tooling-Patterns** zu entwickeln (Setup, Konfiguration, CI-taugliche vs. lokale Tests)
3. **Erkenntnisse dokumentieren** für `~/.agent/` (projektübergreifend nutzbar)

## Nicht-Ziel

- Kein vollständiges E2E-Testing-Framework für Produktionseinsatz
- Keine CI/CD-Integration in dieser Phase (kommt später)

## Voraussetzungen

- Node.js + npm (für Playwright)
- Statisches `site/`-Verzeichnis bereits vorhanden (MkDocs build)
- Alternativ: `mkdocs serve` auf Port 8100

## Phasen

### Phase 1: Setup & Infrastruktur

- [ ] `package.json` initialisieren (im Projektroot)
- [ ] Playwright installieren (`@playwright/test`)
- [ ] Playwright-Config erstellen (`playwright.config.ts`)
  - `headed: true` (nicht headless!)
  - Chrome/Chromium als Zielbrowser
  - BaseURL: `http://127.0.0.1:8100` (MkDocs) oder lokaler Fileserver für `site/`
  - Screenshot-on-failure aktivieren
  - Video-Recording optional konfigurieren
- [ ] Test-Verzeichnis anlegen: `tests/ui/`
- [ ] npm-Scripts definieren:
  - `test:ui` – Tests im sichtbaren Browser
  - `test:ui:headless` – Headless-Variante (für spätere CI)
- [ ] `.gitignore` erweitern: `node_modules/`, `test-results/`, `playwright-report/`
- [ ] Einfachen Serve-Mechanismus für `site/` einrichten (z.B. `npx serve site -l 8100` oder `python -m http.server`)

### Phase 2: Grundlegende Smoke-Tests

Ziel: Sicherstellen, dass die Seiten laden und grundlegende Elemente vorhanden sind.

- [ ] **Landing Page** (`/`)
  - Titel „fermatically" vorhanden
  - Navigation sichtbar
  - Theme-Toggle (Hell/Dunkel) funktioniert
- [ ] **Grundlagen-Artikel** (`/grundlagen/elementare-zahlentheorie/01-was-ist-flt/`)
  - Seite lädt ohne Fehler (kein 404)
  - Überschrift vorhanden
  - MathJax-Formeln gerendert (nicht raw LaTeX sichtbar)
- [ ] **Vorwissen-Seite** (`/vorwissen/teilbarkeit-ggt/`)
  - Seite lädt
  - Admonitions gerendert (MkDocs-spezifisch)
- [ ] **Navigation**
  - Sidebar-Navigation vorhanden und klickbar
  - Mindestens ein Navigationslink führt zur richtigen Seite

### Phase 3: Content-Verifikation

Ziel: Inhaltliche Korrektheit der gerenderten Seiten prüfen.

- [ ] **MathJax-Rendering** über alle Artikel prüfen
  - Kein `$...$` oder `$$...$$` als Klartext sichtbar
  - MathJax-Container (`mjx-container` oder `.MathJax`) vorhanden
  - Stichproben: Mindestens 1 Formel pro Bereich (Grundlagen, Werkzeuge, Beweis)
- [ ] **Querverweise / interne Links**
  - Alle internen Links (`href` mit relativem Pfad) auf existierende Seiten prüfen
  - Kein toter Link (404-Prüfung)
- [ ] **Bilder & Assets**
  - Alle `<img>`-Tags laden erfolgreich (kein broken image)
- [ ] **Responsive / Layout**
  - Seite bei verschiedenen Viewports testen (Desktop, Tablet, Mobil)
  - Kein horizontales Overflow

### Phase 4: Interaktions-Tests

Ziel: Interaktive Elemente testen.

- [ ] **Theme-Toggle** (Dunkel ↔ Hell)
  - Klick auf Toggle ändert das Farbschema
  - Preference wird gespeichert (localStorage prüfen)
- [ ] **Suche** (falls MkDocs-Search aktiv)
  - Suchfeld öffnen
  - Suchbegriff eingeben (z.B. „Fermat")
  - Ergebnisse erscheinen
  - Klick auf Ergebnis führt zur richtigen Seite
- [ ] **Table of Contents**
  - TOC-Einträge vorhanden
  - Klick scrollt zur richtigen Position
- [ ] **Navigation: Sections expandieren**
  - Sidebar-Sections auf-/zuklappen
  - Deep-Links funktionieren

### Phase 5: Erkenntnisse & Dokumentation

Ziel: Learnings für `~/.agent/` aufbereiten.

- [ ] **Erkenntnisse-Dokument** erstellen: `~/.agent/learnings/playwright-ui-testing.md`
  - Setup-Patterns (package.json, config, Verzeichnisstruktur)
  - Was gut testbar ist bei statischen Seiten
  - Typische Fallstricke (MathJax-Ladezeiten, async Rendering, Font-Loading)
  - Headless vs. Headed: Wann welches?
  - Screenshot/Video: Nutzen für Debugging
  - Playwright-Selektoren: Best Practices
  - Integration mit MkDocs / Material Theme
- [ ] **Wiederverwendbare Test-Utilities** identifizieren
  - Helper für Link-Checking
  - Helper für MathJax-Verification
  - Helper für Navigation-Tests
- [ ] **Template für Playwright-Setup** in `~/.agent/templates/` ablegen (optional)

## Technische Details

### Playwright-Config (Entwurf)

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/ui',
  timeout: 30_000,
  use: {
    baseURL: 'http://127.0.0.1:8100',
    headless: false,         // ← Sichtbarer Browser!
    channel: 'chrome',       // ← Echtes Chrome statt Chromium
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    trace: 'retain-on-failure',
  },
  webServer: {
    command: 'npx serve site -p 8100',
    port: 8100,
    reuseExistingServer: true,
  },
  projects: [
    { name: 'chrome', use: { channel: 'chrome' } },
  ],
});
```

### Verzeichnisstruktur

```
fermatically/
├── package.json
├── playwright.config.ts
├── tests/
│   └── ui/
│       ├── smoke.spec.ts          ← Phase 2: Smoke-Tests
│       ├── content.spec.ts        ← Phase 3: Content-Verifikation
│       ├── interaction.spec.ts    ← Phase 4: Interaktions-Tests
│       └── helpers/
│           ├── mathjax.ts         ← MathJax-Prüfhelfer
│           └── navigation.ts      ← Navigation-Prüfhelfer
├── test-results/                  ← (gitignored) Screenshots, Videos
└── playwright-report/             ← (gitignored) HTML-Report
```

### Testausführung

```bash
# Sichtbarer Browser (Standard)
npm run test:ui

# Einzelnen Test im sichtbaren Browser
npx playwright test smoke.spec.ts --headed

# Mit Playwright UI Mode (interaktiv!)
npx playwright test --ui

# Headless (für CI)
npm run test:ui:headless
```

## Offene Fragen

- **MathJax-Ladezeit**: MathJax rendert asynchron – wie lange warten? `waitForSelector` auf `.MathJax` oder `mjx-container`?
- **Lokaler Server**: `npx serve` vs. `python -m http.server` vs. `mkdocs serve`? → Empfehlung: `npx serve` (schnell, kein Python nötig, kein MkDocs-Rebuild)
- **Test-Daten**: Sollen Artikel-Inhalte hart-codiert geprüft werden oder nur strukturell?
  → Empfehlung: Strukturell (Element vorhanden, kein raw LaTeX), nicht inhaltlich (Texte ändern sich)

## Reihenfolge & Abhängigkeiten

```
Phase 1 (Setup) → Phase 2 (Smoke) → Phase 3 (Content) → Phase 4 (Interaktion) → Phase 5 (Doku)
```

Jede Phase kann einzeln reviewed und abgenommen werden. Phase 5 läuft parallel ab Phase 2.
