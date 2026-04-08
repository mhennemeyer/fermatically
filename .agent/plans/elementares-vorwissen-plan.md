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

### F. Weitere Themen (nach Artikel-Review zu ergänzen)
*Dieser Abschnitt wird in Phase 2b systematisch erweitert: Alle 18 Hauptartikel werden durchgelesen und jede Stelle, an der Vorwissen vorausgesetzt wird, wird notiert. Daraus ergeben sich ggf. weitere Themen.*

Mögliche Kandidaten (vorab):
- Kombinatorik (Binomialkoeffizient, n!)
- Grenzwerte und Konvergenz (für p-adische Zahlen, Modulformen)
- Stetigkeit (Grundbegriff für Analysis-Kontexte)
- Primfaktorzerlegung und Fundamentalsatz der Arithmetik
- Komplexe Zahlen (Grundlagen für Modulformen)
- Relationen und Äquivalenzklassen
- Summen- und Produktnotation (Σ, Π)

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

### Phase 2b: Hauptartikel-Review (Vorwissen-Lücken identifizieren)
- [ ] Alle 18 Hauptartikel systematisch durchgehen
- [ ] Jede Stelle notieren, an der Grundwissen vorausgesetzt wird
- [ ] Themen-Gliederung (oben) ggf. erweitern
- [ ] Ergebnis dokumentieren: Welcher Artikel braucht welche Vorwissen-Referenzen

### Phase 2c: Restliche Artikel schreiben ✅
- [x] Alle weiteren Vorwissen-Artikel erstellt (alle 16 Themen DE + EN in `topics/vorwissen/`)
- [x] Jeweils nach `docs/vorwissen/` synchronisiert

### Phase 3: Referenzierung implementieren
- [ ] MkDocs Material Theme auf vorhandene Popup-/Tooltip-Features prüfen (`abbreviations`, `tooltips`)
- [ ] Prototyp mit einer Referenz bauen und testen
- [ ] In den Hauptartikeln Referenzen einfügen
- [ ] Entscheidung über finale Variante nach Prototyp-Review
- [ ] Test und Iteration

### Phase 4: Sync & Build ✅
- [x] `sync_topics_to_docs.sh` für Vorwissen-Ordner erweitert
- [x] `fix_docs_links.py` angepasst
- [x] MkDocs build: 0 Warnings, 0 Errors
- [x] Finaler Review

---

## Status
- [x] Phase 1: Struktur anlegen
- [x] Phase 2a: Pilot-Artikel (Teilbarkeit und ggT)
- [ ] Phase 2b: Hauptartikel-Review (Vorwissen-Lücken identifizieren)
- [x] Phase 2c: Restliche Artikel (alle 16 Themen DE, EN in topics/)
- [ ] Phase 3: Referenzierung (Popup/Sidebar)
- [x] Phase 4: Build & Deploy (0 Warnings, 0 Errors)
