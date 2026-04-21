# Plan: Seitenleiste umstrukturieren – FLT als Hauptstoryline

Erstellt: 2026-04-21
Status: Umgesetzt ✅

## Ausgangslage

### Aktuelle Nav-Struktur (mkdocs.yml)
```
Startseite
Über das Projekt
Vorwissen           ← steht VOR der Storyline
  ├── Logik und Beweistechniken (4 Artikel)
  ├── Arithmetik und Zahlen (7 Artikel)
  ├── Mengen und Strukturen (4 Artikel)
  ├── Geometrie (2 Artikel)
  ├── Algebra (4 Artikel)
  └── Analysis (1 Artikel)
Grundlagen
  └── Elementare Zahlentheorie (4 Artikel)
Werkzeuge (6 Artikel)
Fermats letzter Satz – Der Beweis (8 Artikel)
Quellen
```

### Problem
- Die **Hauptstoryline** (Von Schulmathematik bis FLT) geht unter, weil Vorwissen oben steht und den Einstieg dominiert.
- Ein Leser, der die Seite zum ersten Mal besucht, sieht zuerst 22+ Vorwissen-Artikel statt der eigentlichen Geschichte.
- Die Story – der rote Faden von "Was ist FLT?" bis "R=T und der Abschluss" – ist nicht als zusammenhängender Bereich erkennbar.

### Ziel
- **FLT als Hauptstoryline** klar erkennbar machen (ein aufklappbarer Bereich)
- **Vorwissen** als Nachschlagewerk unterhalb der Story positionieren (ebenfalls aufklappbar)
- Zukünftig: Bereich "Vor-Vorwissen" (tbd)
- Querverweise von Story-Artikeln zum Vorwissen statt linearer Abfolge

## Analyse & Designentscheidungen

### Frage 1: Was gehört zur FLT-Storyline?

Die Story hat drei natürliche Akte, die aktuell als separate Top-Level-Bereiche existieren:

1. **Grundlagen / Elementare Zahlentheorie** (4 Artikel) – "Was ist FLT?", Beweise für n=4 und n=3
2. **Werkzeuge** (6 Artikel) – Gruppen, Ringe, Galois, p-adisch, Ell. Kurven, Modulformen
3. **Fermats letzter Satz – Der Beweis** (8 Artikel) – Taniyama-Shimura bis Langlands

**Entscheidung:** Alle drei unter einem gemeinsamen Dach "Fermats letzter Satz" zusammenfassen. Die drei Akte werden zu Unter-Sektionen.

**Alternativ-Option:** Nur "Grundlagen" und "Der Beweis" unter FLT, "Werkzeuge" separat belassen. Das wäre weniger radikal, aber der User sagt explizit, die Story soll von Anfang bis Ende sichtbar sein.

**Empfehlung:** Alle drei unter FLT. Die Werkzeuge sind Teil des Weges zum Beweis und gehören narrativ dazu.

### Frage 2: Wie wird "Vorwissen" positioniert?

- **Unterhalb** von FLT in der Sidebar
- Als aufklappbarer Bereich mit den bestehenden Unterkategorien
- Wird primär durch **Querverweise** aus den Story-Artikeln angesteuert
- Behält seine interne Struktur (Logik, Arithmetik, Mengen, Geometrie, Algebra, Analysis)

### Frage 3: MkDocs Material – Aufklappbare Bereiche?

MkDocs Material mit `navigation.sections` rendert Top-Level-Einträge als **Sektionen** (nicht aufklappbar, immer sichtbar als Überschriften). Unter-Sektionen sind aufklappbar.

Für aufklappbares Verhalten gibt es zwei Wege:
- **`navigation.sections` + `navigation.expand`** → alle Sektionen sind standardmäßig aufgeklappt
- **`navigation.sections` ohne `navigation.expand`** → Sektionen sind eingeklappt, man kann sie aufklappen

Aktuell sind **beide** Features aktiv. Für das gewünschte Verhalten (aufklappbar, aber nicht standardmäßig offen) sollte `navigation.expand` **entfernt** werden.

**Empfehlung:** `navigation.expand` entfernen, damit FLT und Vorwissen standardmäßig eingeklappt sind und der Leser die Übersicht behält.

### Frage 4: Vor-Vorwissen (tbd)

Der User erwähnt einen zukünftigen Bereich "Vor-Vorwissen". Das ist jetzt noch nicht umzusetzen, aber die Struktur sollte so angelegt werden, dass ein dritter Bereich leicht hinzugefügt werden kann.

## Vorgeschlagene neue Nav-Struktur

```yaml
nav:
  - Startseite: index.md
  - Über das Projekt: about.md
  - Fermats letzter Satz:
    - Überblick: fermat-wiles/index.md          # oder neue Übersichtsseite
    - Elementare Zahlentheorie:
      - "Was ist Fermats letzter Satz?": grundlagen/elementare-zahlentheorie/01-was-ist-flt.md
      - "Der Beweis für n=4": grundlagen/elementare-zahlentheorie/02-beweis-n4.md
      - "Primzahlen und warum sie reichen": grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md
      - "Der Beweis für n=3": grundlagen/elementare-zahlentheorie/04-beweis-n3.md
    - Werkzeuge:
      - "Gruppen – Symmetrie als Sprache": werkzeuge/gruppen.md
      - "Ringe und Körper": werkzeuge/ringe-koerper.md
      - "Galois-Theorie": werkzeuge/galois-theorie.md
      - "p-adische Zahlen": werkzeuge/p-adische-zahlen.md
      - "Elliptische Kurven": werkzeuge/elliptische-kurven.md
      - "Modulformen": werkzeuge/modulformen.md
    - Der Beweis:
      - "Die Taniyama-Shimura-Vermutung": fermat-wiles/01-taniyama-shimura.md
      - "Freys Idee und Ribets Theorem": fermat-wiles/02-frey-ribet.md
      - "Galois-Darstellungen": fermat-wiles/03-galois-darstellungen.md
      - "Deformationstheorie": fermat-wiles/04-deformationstheorie.md
      - "R = T – Das Herz des Beweises": fermat-wiles/05-r-gleich-t.md
      - "Der Taylor-Wiles-Trick": fermat-wiles/06-taylor-wiles-trick.md
      - "Der 3-5-Switch und der Abschluss": fermat-wiles/07-3-5-switch.md
      - "Was danach kam": fermat-wiles/08-was-danach-kam.md
  - Vorwissen:
    - Übersicht: vorwissen/index.md
    - Logik und Beweistechniken:
      - "Aussagenlogik": vorwissen/aussagenlogik.md
      - "Implikation und Äquivalenz": vorwissen/implikation-aequivalenz.md
      - "Beweisarten": vorwissen/beweisarten.md
      - "Was ist ein Beweis?": vorwissen/was-ist-ein-beweis.md
    - Arithmetik und Zahlen:
      - "Bruchrechnung": vorwissen/bruchrechnung.md
      - "Gleichungen und äquivalente Umformungen": vorwissen/gleichungen.md
      - "Ungleichungen": vorwissen/ungleichungen.md
      - "Teilbarkeit und ggT": vorwissen/teilbarkeit-ggt.md
      - "Primfaktorzerlegung": vorwissen/primfaktorzerlegung.md
      - "Modulare Arithmetik": vorwissen/modulare-arithmetik.md
      - "Komplexe Zahlen": vorwissen/komplexe-zahlen.md
    - Mengen und Strukturen:
      - "Mengen und Mengenoperationen": vorwissen/mengen.md
      - "Abbildungen (Funktionen)": vorwissen/abbildungen.md
      - "Relationen und Äquivalenzklassen": vorwissen/relationen-aequivalenzklassen.md
      - "Zahlenbereiche": vorwissen/zahlenbereiche.md
    - Geometrie:
      - "Pythagoras und pythagoräische Tripel": vorwissen/pythagoras.md
      - "Koordinatengeometrie": vorwissen/koordinatengeometrie.md
    - Algebra:
      - "Potenzen und Polynome": vorwissen/potenzen-polynome.md
      - "Binomische Formeln und Faktorisierung": vorwissen/binomische-formeln.md
      - "Summen- und Produktnotation": vorwissen/summen-produktnotation.md
      - "Kombinatorik": vorwissen/kombinatorik.md
    - Analysis:
      - "Grenzwerte und Konvergenz": vorwissen/grenzwerte-konvergenz.md
  - Quellen: quellen.md
```

## Änderungen im Detail

### 1. mkdocs.yml – Nav-Struktur (Hauptänderung)
- **"Grundlagen"**, **"Werkzeuge"** und **"Fermats letzter Satz – Der Beweis"** → zusammengeführt unter **"Fermats letzter Satz"**
- **"Vorwissen"** → bleibt erhalten, rutscht nach unten (nach FLT)
- Drei Unter-Sektionen in FLT: "Elementare Zahlentheorie", "Werkzeuge", "Der Beweis"

### 2. mkdocs.yml – Features
- `navigation.expand` **entfernen** → Bereiche sind standardmäßig eingeklappt
- `navigation.sections` beibehalten → Top-Level-Einträge als Sektionen

### 3. nav_translations (i18n)
- Neue/geänderte Übersetzungen hinzufügen:
  - "Fermats letzter Satz" → "Fermat's Last Theorem"
  - "Der Beweis" → "The Proof"
  - "Elementare Zahlentheorie" bleibt (existiert schon)
  - "Werkzeuge" bleibt (existiert schon als "Tools")
- Alte Einträge bereinigen:
  - "Grundlagen: Foundations" → ggf. entfernen oder behalten für Abwärtskompatibilität
  - "Fermats letzter Satz – Der Beweis" → anpassen

### 4. Dateien – keine Verschiebung nötig
- Alle Markdown-Dateien bleiben an ihrem aktuellen Ort
- Nur die **nav-Referenzen** in mkdocs.yml ändern sich
- Die bisherigen Überblicksseiten (`grundlagen/elementare-zahlentheorie/index.md`, `werkzeuge/index.md`, `fermat-wiles/index.md`) bleiben bestehen

### 5. Optional: FLT-Überblicksseite
- Aktuell verweist der FLT-Überblick auf `fermat-wiles/index.md` (die Beweis-Sektion)
- Es könnte sinnvoll sein, eine **neue Überblicksseite** für den gesamten FLT-Bereich zu erstellen
- **Empfehlung:** Vorerst `fermat-wiles/index.md` als Überblick nutzen oder weglassen. Kann später ergänzt werden.

## Beantwortete Fragen

1. **Werkzeuge separat** – Eigener Bereich zwischen FLT und Vorwissen. Werkzeuge werden als Verweise in die FLT-Storyline eingebaut (Überblicksseite verlinkt auf Werkzeuge als "Akt 2").
2. **`navigation.expand` entfernt** – Bereiche sind standardmäßig eingeklappt.
3. **FLT-Überblicksseite erstellt** – `docs/flt-overview.md` zeigt den gesamten Weg in drei Akten als Roadmap.

## Umsetzungsschritte

1. [x] Feedback zu offenen Fragen einholen
2. [x] mkdocs.yml nav-Struktur umbauen
3. [x] `navigation.expand` entfernen
4. [x] nav_translations anpassen
5. [x] FLT-Überblicksseite erstellt (`docs/flt-overview.md`)
6. [x] Lokalen Build getestet (erfolgreich)
