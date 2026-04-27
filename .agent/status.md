# Projektstatus: fermatically
## Meta
- **Typ:** Content / Mathematik-Plattform
- **Phase:** Phase 5 weitgehend abgeschlossen (Website live, Deployment komplett). Offen: Navigation aus `requires`-Frontmatter.
- **Priorität:** Mittel
- **Zuletzt aktualisiert:** 2026-04-27 (Akt 2 der Poincaré-Storyline angefangen, 3/7 Artikel)
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
- ✅ **Deployment:** GitHub Pages live unter https://fermatically.com (GitHub Actions Workflow, Custom Domain, HTTPS). Dockerfile + .dockerignore entfernt.
- ✅ **Zweisprachig (DE/EN):** mkdocs-static-i18n Plugin, 48 englische `.en.md`-Dateien in docs/, Sprachumschalter im Header, Navigation mit nav_translations, englisches Glossar. Build: 0 Warnings.
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
- ✅ **Vorwissen-Bereich:** 22 Themen (DE+EN) vollständig in `topics/vorwissen/` und `docs/vorwissen/`. Alle Phasen 1–4 abgeschlossen. Phase 3: Glossar-Tooltips (`abbr`+`pymdownx.snippets`), Vorwissen-Tabellen in allen 18 Hauptartikeln, `requires:`-Frontmatter, Inline-Links bei Erstnennung. MkDocs build: 0 Warnings, 0 Errors.
- ✅ **Rechtsprüfung:** Keine urheberrechtlich geschützten Dateien im MkDocs-Output. `quellen.md` bereinigt (interne Ressource-Pfade → DOI/externe Links). `about.md` Guideline-Verstöße behoben. Alle 50 Zitate korrekt mit Quellenangabe.
## Nächste Schritte
- [ ] Navigation aus `requires`-Frontmatter automatisch generieren (artikelserie-plan.md Phase 5, Punkt 16)
- [ ] Wiles-Transkription in KB aufnehmen (via pandoc → PDF → kb add)
- [ ] Medium.com-Synchronisation evaluieren (artikelserie-plan.md Phase 6)
- [ ] Mobile Ansicht testen / CSS-Fix für MathJax-Overflow (deployment-plan.md Phase 4)
## Erledigte Meilensteine (zuletzt)
- [x] Phase 2d: 6 neue Vorwissen-Artikel erstellt – DE + EN, in docs/ synchronisiert, mkdocs.yml erweitert
- [x] Phase 3: Vorwissen-Referenzierung implementiert (Glossar-Tooltips, Vorwissen-Tabellen, Inline-Links, 0 Warnings)
- [x] Statisches Deployment eingerichtet → GitHub Pages live (Plan: `.agent/plans/deployment-plan.md`)
- [x] Zweisprachige Seite (DE/EN) mit Sprachumschalter eingerichtet (mkdocs-static-i18n)
- [x] Pläne-Review und Aktualisierung (2026-04-16)
- [x] Pläne-Review 2026-04-26: deployment-plan, sidebar-restructuring, playwright-ui-tests-plan ins Archiv verschoben
- [x] Poincaré-Überblicksseite (DE+EN) ausformuliert (Plan-Schritt 8, 2026-04-26): Drei-Akt-Roadmap, Quellen, FLT-Querverweis, mkdocs build --strict grün
- [x] Poincaré Akt 1, Artikel 01 (Was ist Topologie?) + 02 (Mannigfaltigkeiten) DE+EN ausformuliert (Plan-Schritt 9 in Arbeit, 2026-04-27): je ~165–195 Zeilen, Quellen, Querverweise; build --strict grün
- [x] Poincaré Akt 1 vollständig: Artikel 03 (Sphäre & einfacher Zusammenhang), 04 (Was ist die Poincaré-Vermutung?), 05 (Geometrisierungs-Vermutung von Thurston) und Akt-Index `topologie/index.md` DE+EN ausformuliert (Plan-Schritt 9 ✅, 2026-04-27): je ~195–210 Zeilen, Quellen (Thurston, Hatcher, Lee, Smale, Freedman, Hamilton, Morgan-Tian, Scott, Kneser); build --strict grün, 0 Warnings
- [x] Poincaré Akt 2 angefangen: Artikel 01 (Riemannsche Metrik), 02 (Krümmung und Ricci-Tensor), 03 (Hamiltons Ricci-Fluss) DE+EN ausformuliert (Plan-Schritt 10 in Arbeit, 3/7, 2026-04-27): je ~170–182 Zeilen mit Levi-Civita, Modellgeometrien, Bonnet–Myers/Bishop–Gromov, Einstein-Mannigfaltigkeiten, Hamilton-1982-Originalsatz, DeTurck-Trick, Beispielen; Quellen Lee 2018, do Carmo, Petersen, Morgan-Tian, Hamilton 1982, Chow-Knopf 2004; build --strict grün, 0 Warnings
- [x] Poincaré Akt 2 fortgesetzt: Artikel 04 (Singularitäten und Blow-up-Limits) und 05 (Perelmans Entropie-Funktionale) DE+EN ausformuliert (Plan-Schritt 10 in Arbeit, 5/7, 2026-04-27): je ~173–181 Zeilen mit Hamilton-Klassifikation Typ I/II/III, Neckpinch, parabolischem Reskalieren, Hamilton-Kompaktheit, antiken $\kappa$-Lösungen, Solitonen, $\mathcal{F}$/$\mathcal{W}$/$\lambda$/$\mu$/$\nu$-Funktionalen, Monotonie-Formel, konjugierter Wärmegleichung; Quellen Perelman 0211159, Hamilton 1995, Angenent–Knopf 2004, Morgan–Tian, Kleiner–Lott, Cao–Zhu, Topping 2006; build --strict grün, 0 Warnings
- [x] Poincaré Akt 2 abgeschlossen ✅: Artikel 06 (κ-Nichtkollaps und kanonische Nachbarschaften) und 07 (Reduzierte Länge und reduziertes Volumen) sowie Akt-Index `ricci-fluss/index.md` DE+EN ausformuliert (Plan-Schritt 10 ✅, 7/7, 2026-04-27): 06 ~201/207 Zeilen mit Definition, Perelman-Theorem 2002 §4, Beweisstrategie über $\mathcal{W}$, antike $\kappa$-Lösungen, Klassifikation Dim 3, $\varepsilon$-Hals/$\varepsilon$-Kappe/sphärische Raumform, Surgery-Bezug; 07 ~218/224 Zeilen mit $\mathcal{L}$-Funktional, $\mathcal{L}$-Geodäten, reduzierter Länge $\ell$, reduziertem Volumen $\tilde V$, Monotonie 0211159 §7, lokalem $\kappa$-Nichtkollaps-Beweis, Blow-up-Konvergenz, asymptotischen Solitonen; Akt-Index ~106/111 Zeilen mit Idee, Artikel-Tabelle, Logik-Diagramm, Vorwissen, Übergang zu Akt 3; Quellen Perelman 0211159/0303109, Morgan–Tian, Kleiner–Lott, Cao–Zhu, Topping, Chow et al.; build --strict grün, 0 Warnings (2.67 s)
## Blocker
- Keine
