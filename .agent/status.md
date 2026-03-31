# Projektstatus: fermatically
## Meta
- **Typ:** Content / Mathematik-Plattform
- **Phase:** Phase 1+2 abgeschlossen (Grundstruktur + Outlines), Phase 3 (Artikel schreiben) steht an
- **Priorität:** Mittel
- **Zuletzt aktualisiert:** 2026-03-31
## Beschreibung
Mathematik-Plattform mit eigenständigen, querverweisbaren Topics – von elementarer Zahlentheorie bis zu Wiles' Beweis von Fermats letztem Satz. 18 Artikel in 3 Kategorien (Grundlagen, Werkzeuge, Beweis). Detaillierter Plan: `.agent/plans/artikelserie-plan.md`.
## Aktueller Stand
- ✅ Quellen aufbereitet: Wiles-Original transkribiert (wiles.md, 350 KB), Boston-Lehrbuch extrahiert (180k Zeichen)
- ✅ Knowledgebase "fermat" mit Boston-Lehrbuch (180 Chunks)
- ✅ MkDocs-Plattform mit Material-Theme aufgesetzt (Port 8100, parallel zu LambdaPy)
- ✅ Landing Page, About, Quellen-Seite und 18 Artikel-Platzhalter in `docs/` erstellt
- ✅ MathJax-Integration für LaTeX-Formeln konfiguriert
- ✅ **Phase 1 – Grundstruktur:** `topics/TEMPLATE.md`, Verzeichnisstruktur für alle 18 Topics, `topics/img/`, `categories/` (5 × DE+EN)
- ✅ **Phase 2 – Outlines:** 18 × `article_de.md` (YAML-Frontmatter, Zusammenfassung, Voraussetzungen, Überblick), 18 × `outline.md` (detaillierte Gliederungen mit Ziel, Abschnitten, Kernaussagen, Querverweisen, Quellen), `topics/DEPENDENCIES.md` (Abhängigkeitsgraph + Lesereihenfolge)
- ✅ **Coolify-Deployment:** Dockerfile (multi-stage: Python-Build → nginx) und .dockerignore erstellt
- ✅ **Keine Autoren-Seiten:** `authors/` entfernt, `author`-Feld aus Frontmatter aller Artikel entfernt, `site_author` aus mkdocs.yml entfernt
- ✅ **KI-Hinweis auf Homepage:** Prominenter Hinweis auf docs/index.md und about.md, dass Artikel KI-generiert sind
- ✅ **Topic-Überblicksseiten:** index.md für Elementare Zahlentheorie, Werkzeuge und Fermat-Wiles erstellt, Navigation in mkdocs.yml aktualisiert
- ✅ **Namensfindung:** Domain **fermatically.com** gewählt und registriert (Plan archiviert: `.agent/plans/archive/namensfindung.md`)
- ✅ **Umbenennung:** Projekt in „fermatically" umbenannt (site_name, site_url, README, docs, status)
- ⬜ Noch keine Artikel inhaltlich ausgeschrieben (Outlines vorhanden, Volltext steht aus)
## Nächste Schritte
- [ ] Phase 3: Artikel schreiben – Grundlagen zuerst (`elementare-zahlentheorie` 4 Artikel DE)
- [ ] Phase 3: Werkzeug-Topics – je 1 Artikel (DE)
- [ ] Phase 3: Englische Versionen nachziehen
- [ ] Phase 4: `fermat-wiles` – 8 Artikel (DE) mit Querverweisen
- [ ] Wiles-Transkription in KB aufnehmen (via pandoc → PDF → kb add)
- [ ] `.gitignore` ergänzen (site/)
- [ ] Coolify-Deployment konfigurieren und testen
## Blocker
- Keine
