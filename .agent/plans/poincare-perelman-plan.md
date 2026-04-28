# Plan: Poincaré-Vermutung – Der Beweis von Perelman

Erstellt: 2026-04-25
Status: Freigegeben (2026-04-25) – Umsetzung läuft

## Ausgangslage

### Vision-Anker
Im `artikelserie-plan.md` ist die Poincaré-Vermutung bereits als zweites großes
Beweis-Topic neben Fermat/Wiles vorgesehen (`topics/poincare-perelman/`,
Phase „Zukunft"). Dieser Plan konkretisiert die Umsetzung **parallel zur
FLT-Storyline** in der bestehenden Sidebar-Struktur (siehe
`sidebar-restructuring.md`).

### Quellenlage – Prüfung des PDFs
Der User hat `resources/perelman.pdf` abgelegt und ist nicht sicher, ob es der
Originaltext ist. Prüfung:

- **Datei:** `resources/perelman.pdf`, 39 Seiten, 326 KB
- **Identifikation (PDF-Metadaten + erste Seite):**
  - arXiv-ID: `math/0211159v1 [math.DG]`, eingereicht 11. Nov. 2002
  - Titel: *"The entropy formula for the Ricci flow and its geometric applications"*
  - Autor: Grisha Perelman (St. Petersburg branch of Steklov Mathematical Institute)
- **Bewertung:** Es ist **ein** Originaltext von Perelman – aber nur der **erste
  von drei** arXiv-Preprints, in denen Perelman 2002/2003 den Beweis der
  Geometrisierungs-/Poincaré-Vermutung skizziert hat. Der Beweis ist erst in
  der Kombination aller drei Papers vollständig:
  1. **0211159** (11.11.2002) – *„The entropy formula for the Ricci flow and
     its geometric applications"* – ✅ vorhanden
     → Entropie-Formel, No-local-collapsing-Theorem, κ-Lösungen, kanonische
     Nachbarschaften.
  2. **0303109** (10.03.2003) – *„Ricci flow with surgery on three-manifolds"*
     – ❌ fehlt
     → Definition der Ricci-Fluss-Chirurgie, Long-time-Verhalten,
     Geometrisierung im allgemeinen Fall.
  3. **0307245** (17.07.2003) – *„Finite extinction time for the solutions to
     the Ricci flow on certain three-manifolds"* – ❌ fehlt
     → Spezialfall, der direkt für die Poincaré-Vermutung (einfach
     zusammenhängend) ausreicht; verkürzter Weg.
- **Empfehlung:** Vor Schreibbeginn beide fehlenden Papers von arXiv ergänzen
  (frei verfügbar) und als Sekundärliteratur die ausführlichen Ausarbeitungen
  heranziehen, die für die Sektor-Verständlichkeit unverzichtbar sind:
  - Kleiner / Lott: *„Notes on Perelman's papers"* (Geom. Topol. 2008)
  - Cao / Zhu: *„A Complete Proof of the Poincaré and Geometrization
    Conjectures"* (Asian J. Math. 2006)
  - Morgan / Tian: *„Ricci Flow and the Poincaré Conjecture"* (AMS, 2007) –
    Buchform, didaktisch am zugänglichsten
  - Optional populärwissenschaftlich: Donal O'Shea, *„The Poincaré
    Conjecture"*

→ **Antwort an den User:** Ja, das PDF ist ein Original-Preprint von Perelman,
aber nicht der gesamte Beweis. Es ist Paper 1 von 3.

## Designentscheidungen (Vorschläge, zu bestätigen)

### Entscheidung 1: Drei-Akt-Struktur analog zu FLT
Die FLT-Storyline ist in drei Akte gegliedert (Elementare Zahlentheorie →
Werkzeuge → Der Beweis). Die Poincaré-Storyline lässt sich natürlich in dieselbe
Drei-Akt-Form bringen:

1. **Akt 1 – Topologie und die Vermutung** (Was wird behauptet?)
   - Was ist Topologie? Mannigfaltigkeiten anschaulich
   - Die Sphäre $S^n$, einfacher Zusammenhang, Homotopie
   - Was ist die Poincaré-Vermutung? (Original 1904, Verallgemeinerung)
   - Warum war sie so schwer? (höhere Dimensionen vs. Dimension 3)
   - Geometrisierungs-Vermutung von Thurston (das größere Bild)

2. **Akt 2 – Werkzeuge: Ricci-Fluss und Geometrische Analysis**
   - Riemannsche Metrik, Krümmung, Ricci-Tensor
   - Hamiltons Ricci-Fluss als Wärmeleitungsgleichung für Metriken
   - Singularitäten und Blow-up-Limits
   - Perelmans Entropie $\mathcal{F}$ und $\mathcal{W}$
   - $\kappa$-Nichtkollaps und kanonische Nachbarschaften
   - Reduzierte Länge $\mathcal{L}$ und reduziertes Volumen

3. **Akt 3 – Der Beweis: Ricci-Fluss mit Chirurgie**
   - Hamiltons Programm und seine Hindernisse
   - Singularitätsanalyse in Dimension 3 ($\kappa$-Lösungen)
   - Chirurgie am Hals: Ausschneiden und Aufkleben
   - Long-time-Verhalten, dünne/dicke Zerlegung
   - Endlich-Zeit-Auslöschung im einfach zusammenhängenden Fall (Paper 3)
   - Schluss: Geometrisierung impliziert Poincaré

### Entscheidung 2: Sidebar-Position
Die FLT-Storyline ist aktuell der erste große Story-Bereich, gefolgt von
Vorwissen. Vorschlag:

```
- Startseite
- Über das Projekt
- Fermats letzter Satz   (bestehend, dreigliedrig)
- Poincaré-Vermutung      (NEU, dreigliedrig parallel)
  - Überblick
  - Topologie und die Vermutung
  - Werkzeuge: Ricci-Fluss
  - Der Beweis
- Vorwissen
- Quellen
```

`navigation.sections` ohne `navigation.expand` (wie nach Sidebar-Restrukturierung
beschlossen) – beide Storylines sind eingeklappt, der Leser sieht die Auswahl
„zwei große Beweise" sofort.

### Entscheidung 3: Verzeichnislayout
Konsequent zur FLT-Struktur (`docs/fermat-wiles/…`, `docs/werkzeuge/…`):

```
docs/
  poincare/
    index.md                       ← Überblick (Roadmap, drei Akte)
    topologie/
      01-was-ist-topologie.md
      02-mannigfaltigkeiten.md
      03-sphaere-einfacher-zusammenhang.md
      04-was-ist-poincare-vermutung.md
      05-geometrisierungs-vermutung.md
    ricci-fluss/
      01-riemannsche-metrik.md
      02-kruemmung-ricci-tensor.md
      03-hamiltons-ricci-fluss.md
      04-singularitaeten-blowup.md
      05-perelman-entropie.md
      06-kappa-nichtkollaps.md
      07-reduzierte-laenge.md
    beweis/
      01-hamiltons-programm.md
      02-singularitaeten-dim3.md
      03-chirurgie.md
      04-long-time-verhalten.md
      05-endliche-extinktion.md
      06-poincare-aus-geometrisierung.md
```

(Slugs/Reihenfolge/Anzahl der Artikel sind Vorschlag – vor dem Schreiben final
mit dem User abstimmen.)

### Entscheidung 4: Vorwissen – was fehlt?
Der bestehende Vorwissen-Bereich (22 Themen) deckt FLT-Bedarf ab. Für Poincaré
fehlen geometrisch-analytische Grundlagen. Vorschlag: **eigene Vorwissen-Unter-
Sektion „Geometrie & Analysis (Aufbau)"**, die nach Bedarf wachsen kann:

- Vektoranalysis kompakt (Gradient, Divergenz, Laplace)
- Wärmeleitungsgleichung – Intuition
- Was ist eine Mannigfaltigkeit? (anschaulich – falls nicht in Akt 1)
- Tangentialraum und Tensoren – Minimalvariante
- Krümmung von Flächen (Gauß) als Sprungbrett

Alternative: Keine eigene Vorwissen-Erweiterung, sondern alle benötigten
Konzepte direkt in Akt 1/2 der Poincaré-Storyline einführen (analog dazu, wie
„Werkzeuge" bei FLT eigene Story-Akte sind statt Vorwissen). **Empfehlung:**
diese Alternative – konsistent mit FLT, hält Vorwissen schlank.

### Entscheidung 5: i18n
- Neue nav_translations in `mkdocs.yml`:
  - „Poincaré-Vermutung" → „Poincaré Conjecture"
  - „Topologie und die Vermutung" → „Topology and the Conjecture"
  - „Werkzeuge: Ricci-Fluss" → „Tools: Ricci Flow"
  - „Der Beweis" existiert schon (FLT)
- Jeder Artikel zweisprachig (`*.de.md`, `*.en.md`) gemäß `docs_structure: suffix`.

### Entscheidung 6: Tiefe und Stil
- **Stil:** wie FLT-Artikel – sachlich, mit Intuition vor Formalismus, KaTeX,
  Querverweise statt Duplikation (siehe `guideline.md` / `rules.md`).
- **Tiefe:** Ziel ist *Verständnis der Architektur* des Beweises, nicht ein
  vollständiges Skript. Schwere technische Beweise (z. B. Monotonie der
  Entropie) werden skizziert mit Quellenverweis auf Morgan-Tian / Kleiner-Lott.
- **Längen-Richtwert:** pro Artikel 1.500–2.500 Wörter (analog FLT-Beweis-Akt).

## Auswirkungen / zu ändernde Dateien

1. `mkdocs.yml`
   - Neue Top-Level-Section „Poincaré-Vermutung" mit drei Unter-Sektionen
   - `nav_translations` ergänzen
2. `docs/poincare/…` neu anlegen (Struktur s. o.)
3. `resources/`
   - `perelman_0303109.pdf` ergänzen (arXiv:math/0303109)
   - `perelman_0307245.pdf` ergänzen (arXiv:math/0307245)
   - Optional: Morgan-Tian PDF / Kleiner-Lott Notes
   - `.agent/agent.md` Knowledgebase-Sektion um Poincaré-Quellen erweitern
4. `categories/` (falls genutzt)
   - Eventuell neue Kategorie „Topologie" und „Geometrische Analysis"
5. `topics/poincare-perelman/` Platzhalter aus `artikelserie-plan.md` materialisieren
   (falls Topics-Spiegelung wie bei FLT angestrebt wird – offen, siehe Frage 3)

## Beantwortete Fragen (User-Feedback 2026-04-25)

1. **Tiefe & Zielgruppe:** Anspruchsvollere Variante – Zielgruppe Studierende
   ab ca. 4. Semester. Eine zugänglichere Zweitfassung („Lücke schließen") ist
   später optional denkbar.
2. **Akt 2 vs. Vorwissen:** Vorwissen-Bereich wird erweitert. Differential-
   geometrische und analytische Grundlagen kommen in eine neue Vorwissen-
   Sektion „Geometrie & Analysis (Aufbau)". Akt 2 der Storyline kann sich
   damit auf Ricci-Fluss-spezifische Inhalte konzentrieren und auf Vorwissen
   verlinken.
3. **Topics-Verzeichnis:** Vorerst kein Spiegel in `topics/poincare-perelman/`.
   Nur `docs/poincare/`.
4. **Quellen beschaffen:** Ja – fehlende Perelman-Papers (0303109, 0307245)
   von arXiv nach `resources/` ergänzen.
5. **Reihenfolge:** Frei wählbar. Vorgehen: erst Strukturgerüst (Stubs + Nav +
   Überblicksseite), dann Akt für Akt füllen.
6. **Geometrisierung:** Vollständig behandeln – Perelmans Beweis der
   Geometrisierungs-Vermutung als das eigentliche Resultat, Poincaré als
   Korollar. (Der Kurzweg über finite extinction time wird zusätzlich
   erwähnt, aber nicht als Hauptweg.)

## Umsetzungsschritte

1. [x] Antworten auf offene Fragen einholen
2. [x] Fehlende Quell-PDFs nach `resources/` ablegen (0303109, 0307245)
3. [x] `.agent/agent.md` Knowledgebase um Poincaré-Quellen erweitern
4. [x] `docs/poincare/` mit Stub-Dateien anlegen (de + en) – 44 Dateien
5. [x] Vorwissen-Sektion „Geometrie und Analysis (Aufbau)" mit 5 Stubs (DE+EN) angelegt
6. [x] `mkdocs.yml` Nav + nav_translations erweitern
7. [x] Lokalen Build (`mkdocs build --strict`) erfolgreich getestet – keine neuen Warnungen
8. [x] Überblicksseite `docs/poincare/index.md` + `index.de.md` ausformuliert (Drei-Akt-Roadmap, Tabellen, Vorwissen- und FLT-Querverweise, Quellen mit arXiv-Links; mkdocs build --strict grün, 0 Warnings) – 2026-04-26
9. [x] Akt 1 schreiben (Topologie + Vermutung) – alle 5 Artikel + Akt-Index DE+EN ausformuliert (Stand 2026-04-27): 01 Was ist Topologie?, 02 Mannigfaltigkeiten, 03 Sphäre & einfacher Zusammenhang, 04 Was ist die Poincaré-Vermutung?, 05 Geometrisierungs-Vermutung von Thurston, `topologie/index.md` als Akt-1-Übersicht. Quellen, Querverweise, mkdocs build --strict grün (0 Warnings).
10. [x] Akt 2 schreiben (Ricci-Fluss-Werkzeuge) – alle 7 Artikel + Akt-Index DE+EN ausformuliert (Stand 2026-04-27): 01 Riemannsche Metrik, 02 Krümmung und Ricci-Tensor, 03 Hamiltons Ricci-Fluss, 04 Singularitäten/Blow-up-Limits, 05 Perelman-Entropie, 06 κ-Nichtkollaps und kanonische Nachbarschaften (Definition, Perelman-Theorem 2002 §4, Beweisidee über $\mathcal{W}$, antike $\kappa$-Lösungen, Klassifikation Dim 3, Hals/Kappe/sphärische Raumform, Surgery-Bezug), 07 Reduzierte Länge und reduziertes Volumen ($\mathcal{L}$-Geometrie, $\mathcal{L}$-Geodäten, $\ell$-Funktion, $\tilde V$, Monotonie-Theorem, lokaler $\kappa$-Nichtkollaps-Beweis, Blow-up-Konvergenz, asymptotische Solitonen, Vergleichstabelle $\mathcal{W}$ vs. reduzierte Länge), `ricci-fluss/index.md` als Akt-2-Übersicht (Idee in einem Satz, Tabelle der 7 Artikel, ASCII-Logikdiagramm, Vorwissen, Übergang zu Akt 3). Quellen Lee 2018, do Carmo, Petersen, Morgan-Tian 2007, Hamilton 1982/1995, Chow-Knopf 2004, Perelman 0211159/0303109, Kleiner-Lott 2008, Cao-Zhu 2006, Topping 2006, Angenent-Knopf 2004, Chow et al. 2007; mkdocs build --strict grün (0 Warnings, 2.67 s).
11. [x] Akt 3 schreiben (Der Beweis) – alle 6 Artikel + Akt-Index DE+EN ausformuliert (Stand 2026-04-28): 01 Hamiltons Programm, 02 Singularitätsanalyse Dim 3, 03 Ricci-Fluss mit Chirurgie, 04 Long-time-Verhalten/dünn-dick, 05 Endliche Auslöschungszeit (Perelman 0307245: $W_2$/$W_3$-Funktionale, Gauß-Bonnet-Differentialungleichung $\partial_t W \le -4\pi - \tfrac{1}{2}R_{\min}W$, Hauptsatz + Korollar einfach zusammenhängend, Vergleich Colding–Minicozzi 2008, Tabelle „Vermutungen vs. benötigte Werkzeuge", Quellen Sacks–Uhlenbeck, Morgan–Tian Kap. 18), 06 Geometrisierung impliziert Poincaré (lange Route via Thurston-Klassifikation aller 8 Modellgeometrien + inkompressible-Tori-Argument; Kurzweg via finite Extinktion + Van-Kampen + Hopf/Wolf; Vergleichstabelle, Hindernis-Auflösung, Epilog mit FLT-Querverweis), `beweis/index.md` als Akt-Index (Idee in einem Satz, Tabelle der 6 Artikel, ASCII-Logikdiagramm Hamilton → Singularität → Surgery → {long-time, extinction} → Poincaré, Hindernis-Mapping H1–H5, Vorwissen, Ausblick 4-dim/Bamler/Brendle, Quellen-Sammlung). Quellen Perelman 0307245, Colding–Minicozzi 2005/2008, Sacks–Uhlenbeck 1981, Kneser 1929, Milnor 1962, Hopf 1926, Wolf 2011, Morgan–Tian 2007/2014; mkdocs build --strict grün (0 Warnings, 2.73 s).
12. [x] Vorwissen „Geometrie und Analysis (Aufbau)" inhaltlich gefüllt (Stand 2026-04-28): alle 5 Artikel + EN-Übersetzungen ausformuliert (10 Dateien, je ~110–135 Zeilen). `mannigfaltigkeit-anschaulich` (Karten/Atlas/Kartenwechsel/glatte Mannigfaltigkeit, Beispiele $S^n,T^n,\mathbb{RP}^n$, Orientierbarkeit/Rand/Kompaktheit), `tangentialraum-tensoren` ($T_pM$ via Kurvenäquivalenzklassen, Vektorfelder/Kotangentialraum/Tensorfelder, Riemannsche Metrik, Index hoch/runter), `kruemmung-flaechen-gauss` (Hauptkrümmungen, erste/zweite Fundamentalform, Theorema Egregium, Gauß-Bonnet, Übergang zu Schnitt-/Ricci-/Skalarkrümmung), `vektoranalysis` (Gradient/Divergenz/Laplace-Beltrami auf $(M,g)$, Divergenzsatz/Greensche Identität/Stokes, Identitäten-Tabelle inkl. Ricci-Fluss-Variante), `waermeleitung` ($\partial_t u=\Delta u$, Glättung/Maximum-Prinzip/Energie-Abnahme, Wärmekern, parabolische Skalierung, Linearisierung des Ricci-Flusses, konjugierte Wärmeleitung). Querverweise in beide Richtungen zu Akt 1/2/3.
13. [x] Querverweise zu/von Vorwissen ergänzt (2026-04-28): Vorwissen-Index `vorwissen/index.{de.,}md` um Sektion „F. Geometrie und Analysis (Aufbau)" mit Tabelle der 5 Artikel und Verweis auf `poincare/index.md` erweitert; Poincaré-Übersichtsseite verweist bereits auf den Vorwissen-Block; alle 10 neuen Artikel verlinken auf passende Akt-1/2/3-Artikel.
14. [x] Review, Stilabgleich, Deployment-Vorbereitung (2026-04-28): Frontmatter-Konsistenz (`status: ready`, slug, lang, tags), Stilreferenz `komplexe-zahlen.de.md` befolgt (KaTeX, knappe Definitionen, Beispiel-Tabellen, Quellen), interne Pfade gegen tatsächliche Dateinamen geprüft (`02-singularitaeten-dim3.md`, `04-was-ist-poincare-vermutung.md`); mkdocs build --strict grün (0 Warnings, 2.74 s, DE+EN, 90 Nav-Elemente übersetzt) — bereit für Commit/Push.

**Strukturgerüst-Phase abgeschlossen (2026-04-25).** Inhalte werden in
Folge-Sessions geschrieben.

**Inhaltliche Phase abgeschlossen (2026-04-28).** Alle 18 Storyline-Artikel
+ 3 Akt-Indizes (DE+EN) und alle 5 Vorwissen-Artikel „Geometrie und
Analysis (Aufbau)" (DE+EN) sind ausformuliert; Vorwissen-Index ergänzt.
mkdocs build --strict grün, 0 Warnings. Plan abgeschlossen.
