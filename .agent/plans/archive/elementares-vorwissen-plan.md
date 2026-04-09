# Plan: Elementares Vorwissen – Referenzbereich

## Ziel
Ein eigenständiger Bereich **„Vorwissen"** auf der Website, der grundlegende mathematische Konzepte als Nachschlagewerk bereitstellt. Dieser Bereich ist **nicht Teil der linearen Artikelfolge** (Grundlagen → Werkzeuge → Fermat-Wiles), sondern wird aus den Artikeln heraus **referenziert**.

**Kernprinzip:** Der Leser soll den Kontext nicht verlieren. Beim Lesen eines Beweises oder einer Erklärung soll ein unbekannter Grundbegriff schnell nachschlagbar sein – ohne die aktuelle Stelle zu verlassen.

## Zielgruppe
Leser ohne mathematische Vorbildung, die beim Lesen der Hauptartikel auf unbekannte Grundbegriffe stoßen.

## Entscheidungen (aus User-Feedback)
- **Vorgehen:** Schrittweise – erst ein Artikel, Review-Feedback, dann der Rest
- **Tiefe:** Knapp mit ein bis zwei Beispielen. Kein Schulbuch.
- **Sprachen:** DE und EN (wie Hauptartikel), später erweiterbar
- **Navigation:** „Vorwissen" ganz oben in der Seitenleiste (vor „Grundlagen")
- **Stil:** Gemäß `guideline.md` – sachlich-technisch

---

## Themen-Gliederung

### A. Logik und Beweistechniken
1. **Aussagenlogik** – Aussagen, Wahrheitswerte, Konjunktion (∧), Disjunktion (∨), Negation (¬)
2. **Implikation und Äquivalenz** – „A ⟹ B" ≡ „¬A ∨ B"; Kontraposition; Bikonditional (⟺)
3. **Beweisarten** – Direkter Beweis, Widerspruchsbeweis (reductio ad absurdum), Vollständige Induktion, Beweis durch Gegenbeispiel
4. **Was ist ein Beweis?** – Axiome, Definitionen, Sätze, Lemmata; Unterschied Vermutung vs. Satz

### B. Arithmetik und Zahlen
5. **Bruchrechnung** – Addition, Subtraktion, Multiplikation, Division; Erweitern und Kürzen; Hauptnenner
6. **Gleichungen und äquivalente Umformungen** – Was bedeutet „="; erlaubte Operationen auf beiden Seiten; Äquivalenzumformungen
7. **Ungleichungen** – Ordnung auf ℝ; Regeln beim Multiplizieren mit negativen Zahlen; Betrag
8. **Teilbarkeit und ggT** – Division mit Rest, größter gemeinsamer Teiler, Euklidischer Algorithmus
9. **Modulare Arithmetik (mod)** – Kongruenz, Rechnen modulo n, Restklassen

### C. Mengen und Strukturen
10. **Mengen und Mengenoperationen** – Notation (∈, ⊂, ∪, ∩, ∅), Teilmengen, Potenzmengen
11. **Abbildungen (Funktionen)** – Definitions-/Wertebereich, injektiv, surjektiv, bijektiv
12. **Zahlenbereiche** – ℕ, ℤ, ℚ, ℝ, ℂ; Erweiterungskette; warum jeder Bereich nötig ist

### D. Geometrie-Grundlagen
13. **Pythagoras und pythagoräische Tripel** – Satz des Pythagoras, ganzzahlige Lösungen, Bezug zu Fermats Gleichung
14. **Koordinatengeometrie** – Punkte, Geraden, Kurven in der Ebene (Vorbereitung auf elliptische Kurven)

### E. Algebra-Grundlagen
15. **Potenzen und Polynome** – Potenzgesetze, Polynomausdruck, Grad eines Polynoms
16. **Binomische Formeln und Faktorisierung** – (a+b)², (a-b)², a²-b²; Anwendung beim Umformen

### F. Weitere Themen (Ergebnis Phase 2b – Hauptartikel-Review)
*Alle 18 Hauptartikel wurden systematisch durchgelesen (2026-04-09). Die folgenden Themen werden in den Artikeln vorausgesetzt, sind aber noch nicht als Vorwissen-Artikel vorhanden.*

**Neue Themen (priorisiert nach Häufigkeit):**

17. **Komplexe Zahlen** – imaginäre Einheit $i$, Darstellung $a + bi$, Betrag, konjugiert; Einheitswurzeln $e^{2\pi i/n}$; obere Halbebene $\mathbb{H}$
    - *Benötigt in:* Artikel 04 (Eisenstein-Zahlen $\mathbb{Z}[\omega]$), Modulformen (obere Halbebene, holomorphe Funktionen), Galois-Theorie (Zerfällungskörper), Ringe/Körper (Kreisteilungsringe $\mathbb{Z}[\zeta_p]$)
    - *Priorität:* **Hoch** – wird ab Artikel 04 durchgängig verwendet

18. **Summen- und Produktnotation (Σ, Π)** – Summenzeichen, Produktzeichen, Indexmengen, Doppelsummen
    - *Benötigt in:* Fast allen Artikeln ab Werkzeuge (Fourier-Entwicklungen, Euler-Produkte, L-Reihen, Parametrisierungen)
    - *Priorität:* **Hoch** – allgegenwärtig

19. **Primfaktorzerlegung und Fundamentalsatz der Arithmetik** – Existenz und Eindeutigkeit der Zerlegung; warum sie in erweiterten Ringen versagen kann
    - *Benötigt in:* Artikel 01–04 (Lamé, Kummer), Ringe/Körper (EPZ, HIR, Dedekind-Ringe), p-adische Zahlen
    - *Priorität:* **Hoch** – zentral für das Verständnis von Kummers Idealtheorie

20. **Grenzwerte und Konvergenz** – Folgen, Reihen, Cauchy-Folgen, Vervollständigung; geometrische Reihe
    - *Benötigt in:* p-adische Zahlen (Cauchy-Folgen, Vervollständigung, $p$-adische Reihen), Modulformen (Fourier-Reihen, $q$-Entwicklung), L-Reihen (Konvergenz)
    - *Priorität:* **Hoch** – ohne Konvergenzbegriff sind p-adische Zahlen und Modulformen nicht verständlich

21. **Relationen und Äquivalenzklassen** – Äquivalenzrelation, Partition, Restklassen als Beispiel
    - *Benötigt in:* Ringe/Körper (Faktorringe, Ideale), Gruppen (Nebenklassen, Faktorgruppen), Deformationstheorie (Äquivalenz von Liftungen)
    - *Priorität:* **Mittel** – wird implizit über Restklassen eingeführt, aber ein eigener Artikel wäre hilfreich

22. **Kombinatorik (Binomialkoeffizient, n!)** – Fakultät, Binomialkoeffizient, Binomialsatz
    - *Benötigt in:* Artikel 03 (symmetrische Gruppe $S_n$, $n! = 6$ Elemente), Gruppen (Ordnung von $S_n$)
    - *Priorität:* **Mittel** – punktuell benötigt

**Nicht benötigt (gestrichen):**
- ~~Stetigkeit~~ – wird in den Artikeln nur als Fachbegriff erwähnt ("stetige Darstellung"), aber nicht als Vorwissen vorausgesetzt. Kein eigener Artikel nötig.

---

## Referenzierung: Popup/Sidebar-Konzept (Refinement nötig)

### Problem
Normale HTML-Links navigieren weg von der aktuellen Seite. Der Leser verliert den Kontext – z.B. mitten in einem Beweis, wo eine Umformung auf Bruchrechnung basiert.

### Ziel
Der Leser bleibt an der aktuellen Stelle und kann Grundlagen-Begriffe **inline nachschlagen**, ohne die Seite zu verlassen.

### Optionen (zu evaluieren)

#### Option A: Tooltip-Popups
- Klick auf einen markierten Begriff öffnet ein kleines Popup/Tooltip mit der Kurzfassung des Vorwissen-Artikels
- Vorteil: Minimaler Kontextverlust, schnell
- Nachteil: Platz begrenzt, nur für kurze Definitionen geeignet
- Technisch: JavaScript + Custom MkDocs-Plugin oder Markdown-Extension

#### Option B: Sidebar-Panel (rechts)
- Klick auf einen Referenz-Link öffnet eine Seitenleiste rechts, die den Vorwissen-Artikel anzeigt
- Vorteil: Mehr Platz als Popup, Haupttext bleibt sichtbar
- Nachteil: Komplexere Implementierung, Layout-Anpassungen nötig
- Technisch: JavaScript + CSS, ggf. Custom Theme-Override

#### Option C: Hybrid (empfohlen als Ausgangspunkt)
- **Kurze Definitionen** (1–3 Sätze): Tooltip-Popup direkt inline
- **Längere Erklärungen** (mit Formeln/Beispielen): Sidebar-Panel oder Modal
- Fallback: Normaler Link zur Vorwissen-Seite für Leser, die tiefer einsteigen wollen

### Nächste Schritte für diesen Punkt
- [ ] MkDocs Material Theme auf vorhandene Popup-/Tooltip-Features prüfen (z.B. `abbreviations`, `tooltips`)
- [ ] Prototyp mit einer Referenz bauen und testen
- [ ] Entscheidung über finale Variante nach Prototyp-Review

---

## Umsetzung

### Phase 1: Struktur anlegen ✅
- [x] Ordner `topics/vorwissen/` erstellen mit Unterordnern pro Thema
- [x] Ordner `docs/vorwissen/` für MkDocs-Output anlegen
- [x] `mkdocs.yml` erweitern: Neuen Nav-Bereich **„Vorwissen"** einfügen – ganz oben (nach Startseite, vor Grundlagen)
- [x] `docs/vorwissen/index.md` als Übersichtsseite erstellen

### Phase 2a: Ersten Artikel schreiben (Pilot) ✅
- [x] **Ein Thema** auswählen: „Teilbarkeit und ggT"
- [x] `topics/vorwissen/teilbarkeit-ggt/article_de.md` schreiben (DE)
- [x] `topics/vorwissen/teilbarkeit-ggt/article_en.md` schreiben (EN)
- [x] Nach `docs/vorwissen/` synchronisieren
- [x] Build testen
- [x] **→ Review-Feedback vom User einholen**

### Phase 2b: Hauptartikel-Review (Vorwissen-Lücken identifizieren) ✅
- [x] Alle 18 Hauptartikel systematisch durchgehen
- [x] Jede Stelle notieren, an der Grundwissen vorausgesetzt wird
- [x] Themen-Gliederung erweitert: 6 neue Themen (17–22), 1 gestrichen (Stetigkeit)
- [x] Ergebnis dokumentieren: Artikel-Vorwissen-Matrix (siehe unten)

### Phase 2c: Restliche Artikel schreiben ✅
- [x] Alle weiteren Vorwissen-Artikel erstellt (alle 16 Themen DE + EN in `topics/vorwissen/`)
- [x] Jeweils nach `docs/vorwissen/` synchronisiert

### Phase 2d: Neue Vorwissen-Artikel erstellen (6 Themen: 17–22) ✅
- [x] Komplexe Zahlen (17) – DE + EN
- [x] Summen- und Produktnotation (18) – DE + EN
- [x] Primfaktorzerlegung (19) – DE + EN
- [x] Grenzwerte und Konvergenz (20) – DE + EN
- [x] Relationen und Äquivalenzklassen (21) – DE + EN
- [x] Kombinatorik (22) – DE + EN
- [x] Nach `docs/vorwissen/` synchronisiert
- [x] `mkdocs.yml` Navigation erweitert (6 neue Einträge)
- [x] MkDocs build: 0 Warnings, 0 Errors

### Phase 3: Referenzierung implementieren ✅
- [x] MkDocs Material Theme geprüft: `abbr` + `pymdownx.snippets` (Glossar-Tooltips) + `content.tooltips` (verbesserte Darstellung)
- [x] `mkdocs.yml` erweitert: `abbr`, `pymdownx.snippets` mit auto_append, `content.tooltips`
- [x] Glossar-Datei `docs/includes/glossary.md` mit 35 Einträgen für alle 22 Vorwissen-Themen
- [x] Prototyp: Artikel 01 (Was ist FLT) mit Vorwissen-Tabelle + Inline-Links
- [x] Script `scripts/add_vorwissen_refs.py`: Alle 18 Hauptartikel mit `requires:`-Frontmatter + Vorwissen-Tabellen
- [x] `scripts/fix_docs_links.py` um 22 Vorwissen-Mappings erweitert
- [x] `scripts/fix_remaining_links.py` für Inline-Link-Korrekturen in docs/
- [x] Sync nach docs/, MkDocs build: 0 Warnings, 0 Errors

### Phase 4: Sync & Build ✅
- [x] `sync_topics_to_docs.sh` für Vorwissen-Ordner erweitert
- [x] `fix_docs_links.py` angepasst
- [x] MkDocs build: 0 Warnings, 0 Errors
- [x] Finaler Review

---

## Ergebnis Phase 2b: Artikel-Vorwissen-Matrix

*Erstellt 2026-04-09. Zeigt für jeden Hauptartikel die benötigten Vorwissen-Themen.*

### Grundlagen-Artikel

| Artikel | Benötigtes Vorwissen |
|---------|---------------------|
| 01 – Was ist FLT | Potenzen (15), Zahlenbereiche (12), Pythagoras (13), Gleichungen (6) |
| 02 – Beweis n=4 | Teilbarkeit/ggT (8), Beweisarten (3), Gleichungen (6), Pythagoras (13), Modulare Arithmetik (9) |
| 03 – Primzahlen/Reduktion | Teilbarkeit/ggT (8), Beweisarten (3), Modulare Arithmetik (9), **Primfaktorzerlegung (19)**, **Kombinatorik (22)** |
| 04 – Beweis n=3 | **Komplexe Zahlen (17)**, Teilbarkeit/ggT (8), Modulare Arithmetik (9), Beweisarten (3), Zahlenbereiche (12), **Primfaktorzerlegung (19)** |

### Werkzeug-Artikel

| Artikel | Benötigtes Vorwissen |
|---------|---------------------|
| Gruppen | Mengen (10), Abbildungen (11), Zahlenbereiche (12), Modulare Arithmetik (9), **Kombinatorik (22)**, **Relationen (21)** |
| Ringe/Körper | Mengen (10), Abbildungen (11), Gleichungen (6), Teilbarkeit/ggT (8), **Primfaktorzerlegung (19)**, **Komplexe Zahlen (17)**, **Relationen (21)** |
| Galois-Theorie | Potenzen/Polynome (15), Abbildungen (11), **Komplexe Zahlen (17)**, Zahlenbereiche (12) |
| p-adische Zahlen | Teilbarkeit/ggT (8), Modulare Arithmetik (9), **Grenzwerte/Konvergenz (20)**, **Summennotation (18)**, Potenzen (15) |
| Elliptische Kurven | Koordinatengeometrie (14), Bruchrechnung (5), Modulare Arithmetik (9), Abbildungen (11), **Summennotation (18)** |
| Modulformen | **Komplexe Zahlen (17)**, **Summennotation (18)**, **Grenzwerte/Konvergenz (20)**, Abbildungen (11) |

### Beweis-Artikel (Fermat-Wiles)

| Artikel | Benötigtes Vorwissen |
|---------|---------------------|
| 01 – Taniyama-Shimura | **Summennotation (18)**, Modulare Arithmetik (9), **Komplexe Zahlen (17)** |
| 02 – Frey-Ribet | Teilbarkeit/ggT (8), **Primfaktorzerlegung (19)**, Beweisarten (3) |
| 03 – Galois-Darstellungen | Abbildungen (11), Mengen (10), Modulare Arithmetik (9) |
| 04 – Deformationstheorie | **Grenzwerte/Konvergenz (20)**, **Relationen (21)** |
| 05 – R=T | **Summennotation (18)** |
| 06 – Taylor-Wiles-Trick | **Grenzwerte/Konvergenz (20)**, Modulare Arithmetik (9) |
| 07 – 3-5-Switch | Beweisarten (3) |
| 08 – Was danach kam | (keine zusätzlichen) |

### Zusammenfassung: Häufigkeit der Vorwissen-Themen

| Rang | Thema | Artikelzahl | Status |
|------|-------|-------------|--------|
| 1 | Modulare Arithmetik (9) | 10 | ✅ vorhanden |
| 2 | Teilbarkeit/ggT (8) | 8 | ✅ vorhanden |
| 3 | Abbildungen (11) | 7 | ✅ vorhanden |
| 4 | Beweisarten (3) | 7 | ✅ vorhanden |
| 5 | Komplexe Zahlen (17) | 7 | ✅ vorhanden |
| 6 | Summennotation (18) | 6 | ✅ vorhanden |
| 7 | Zahlenbereiche (12) | 5 | ✅ vorhanden |
| 8 | Primfaktorzerlegung (19) | 5 | ✅ vorhanden |
| 9 | Mengen (10) | 4 | ✅ vorhanden |
| 10 | Potenzen/Polynome (15) | 4 | ✅ vorhanden |
| 11 | Gleichungen (6) | 4 | ✅ vorhanden |
| 12 | Grenzwerte/Konvergenz (20) | 4 | ✅ vorhanden |
| 13 | Pythagoras (13) | 2 | ✅ vorhanden |
| 14 | Koordinatengeometrie (14) | 2 | ✅ vorhanden |
| 15 | Bruchrechnung (5) | 2 | ✅ vorhanden |
| 16 | Relationen (21) | 3 | ✅ vorhanden |
| 17 | Kombinatorik (22) | 2 | ✅ vorhanden |

### Empfehlung: Priorität für neue Artikel

1. **Komplexe Zahlen** (17) – Hoch, ab Artikel 04 durchgängig
2. **Summen- und Produktnotation** (18) – Hoch, allgegenwärtig in Werkzeug- und Beweis-Artikeln
3. **Primfaktorzerlegung** (19) – Hoch, zentral für Kummers Idealtheorie
4. **Grenzwerte und Konvergenz** (20) – Hoch, ohne diesen Begriff kein Verständnis von p-adisch/Modulformen
5. **Relationen und Äquivalenzklassen** (21) – Mittel
6. **Kombinatorik** (22) – Mittel

---

## Status
- [x] Phase 1: Struktur anlegen
- [x] Phase 2a: Pilot-Artikel (Teilbarkeit und ggT)
- [x] Phase 2b: Hauptartikel-Review (Vorwissen-Lücken identifizieren)
- [x] Phase 2c: Restliche Artikel (alle 16 Themen DE, EN in topics/)
- [x] Phase 2d: Neue Vorwissen-Artikel erstellen (6 Themen: 17–22)
- [x] Phase 3: Referenzierung (Tooltips + Vorwissen-Tabellen + Inline-Links)
- [x] Phase 4: Build & Deploy (0 Warnings, 0 Errors)
