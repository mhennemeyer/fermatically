# Projektstatus: fermatically
## Meta
- **Typ:** Content / Mathematik-Plattform
- **Phase:** Phase 5 in Arbeit (Website-Publikation: docs/ mit echten Artikeln, MkDocs build clean)
- **Priorität:** Mittel
- **Zuletzt aktualisiert:** 2026-04-08
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
- ✅ **Phase 3 – Grundlagen & Werkzeuge:** 4 Grundlagen-Artikel (elementare Zahlentheorie, ~700 Zeilen) + 6 Werkzeug-Artikel (Gruppen, Ringe/Körper, Galois, p-adisch, Ell. Kurven, Modulformen, ~1260 Zeilen)
- ✅ **Phase 4 – Fermat-Wiles-Beweis:** 8 Beweis-Artikel (~2060 Zeilen) mit Querverweisen, LaTeX-Formeln, MkDocs-Admonitions
- ✅ **Insgesamt 18 deutsche Artikel** mit ~4020 Zeilen inhaltlich ausgeschrieben
- ✅ **18 englische Artikel** (~4000 Zeilen) als Übersetzungen der deutschen Versionen erstellt
- ✅ **`.gitignore`** erstellt, Git-Repository sauber initialisiert (84 Dateien)
- ✅ **Phase 5a – docs/ befüllt:** 18 Artikel aus `topics/` nach `docs/` synchronisiert, interne Links auf docs/-Pfade umgeschrieben, MkDocs build mit 0 Warnings/Errors
- ✅ **Sync-Script:** `scripts/sync_topics_to_docs.sh` + `scripts/fix_docs_links.py` für wiederholbare Synchronisation
- ✅ **Stilüberarbeitung:** Alle 18 Artikel + Startseite (index.md) nach guideline.md überarbeitet – keine „Wir"-Formulierungen, keine Metaphern, Fachzitate ergänzt. Plan archiviert: `.agent/plans/archive/stilueberarbeitung-plan.md`
- ✅ **Vorwissen-Bereich:** 16 Themen (DE+EN) vollständig in `topics/vorwissen/` und `docs/vorwissen/`. Phase 1–2 und 4 abgeschlossen. Offen: Phase 2b (Hauptartikel-Review) und Phase 3 (Referenzierung/Popup).
## Nächste Schritte
- [ ] Phase 2b: Alle 18 Hauptartikel auf Vorwissen-Lücken prüfen und Referenzen notieren
- [ ] Phase 3: Popup/Sidebar-Referenzierung implementieren (MkDocs Material tooltips/abbreviations prüfen, Prototyp bauen)
- [ ] Coolify-Deployment konfigurieren und testen
- [ ] Navigation aus `requires`-Frontmatter automatisch generieren
- [ ] Wiles-Transkription in KB aufnehmen (via pandoc → PDF → kb add)
## Blocker
- Keine
