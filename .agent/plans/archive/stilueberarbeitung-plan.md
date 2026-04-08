# Plan: Stilüberarbeitung aller Artikel nach Guideline

Erstellt: 2026-04-01
Status: Abgeschlossen

## Referenz

Guideline: `.agent/guideline.md`

## Identifizierte Stilprobleme (Bestandsaufnahme)

Anhand von Artikel 01 (repräsentativ für alle 18 Artikel):

### 1. Perspektive: „Wir"/„Ich"-Verwendung
- Häufig: „kennen wir", „tauchen wir ein", „behandeln wir", „besprechen wir"
- **Ziel:** Rein beschreibende Formulierungen ohne Personalpronomen

### 2. Unnötige Adjektive und schmückendes Beiwerk
- Beispiele: „kühne Vermutung", „spektakuläre Idee", „dramatische Vorlesungsreihe", „tiefgreifend", „abenteuerliche Geschichte", „hervorragend erzählt"
- **Ziel:** Adjektive nur, wenn sie die technische Aussage schärfen

### 3. Metaphern und narrative Wendungen
- Beispiele: „Jagd nach dem Beweis", „als hätte man eine unsichtbare Barriere überschritten", „Der Teufel steckt im Detail", „davon geträumt, FLT zu beweisen", „fast gab er auf"
- **Ziel:** Sachliche, direkte Darstellung ohne erzählerische Ausschmückung

### 4. Fehlende Fachzitate
- Guideline verlangt Zitate aus Fachliteratur zur Stützung von Thesen (Blockquote mit Quellenangabe)
- Aktuell: Nur das Fermat-Originalzitat und die Landau-Anekdote, keine Fachzitate
- **Ziel:** Pro Artikel 2–4 prägnante Zitate aus der Fachliteratur (Boston, Wiles, Singh, Serre, Mazur etc.)

### 5. Nominalstil in Teasern/Zusammenfassungen
- Aktuell: „Die Geschichte einer Vermutung, die 358 Jahre lang unbewiesen blieb"
- **Ziel:** Direkte Feststellungen statt erzählerischer Einleitungen

## Vorgehen

### Schritt 1: Muster-Überarbeitung (Artikel 01)
- [x] `topics/elementare-zahlentheorie/01-was-ist-flt/article_de.md` überarbeiten
- [x] Feedback einholen

### Schritt 2: Grundlagen-Artikel (02–04)
- [x] `02-beweis-n4`
- [x] `03-primzahlen-reduktion`
- [x] `04-beweis-n3`

### Schritt 3: Werkzeug-Artikel (6 Stück)
- [x] `gruppen-und-symmetrie/01-gruppen`
- [x] `ringe-und-koerper/01-ringe-koerper`
- [x] `galois-theorie/01-galois-theorie`
- [x] `p-adische-zahlen/01-p-adische-zahlen`
- [x] `elliptische-kurven/01-elliptische-kurven`
- [x] `modulformen/01-modulformen`

### Schritt 4: Beweis-Artikel (8 Stück)
- [x] `fermat-wiles/01-taniyama-shimura`
- [x] `fermat-wiles/02-frey-ribet`
- [x] `fermat-wiles/03-galois-darstellungen`
- [x] `fermat-wiles/04-deformationstheorie`
- [x] `fermat-wiles/05-r-gleich-t`
- [x] `fermat-wiles/06-taylor-wiles-trick`
- [x] `fermat-wiles/07-3-5-switch`
- [x] `fermat-wiles/08-was-danach-kam`

### Schritt 5: Sync nach docs/
- [x] `scripts/sync_topics_to_docs.sh` + `scripts/fix_docs_links.py` ausführen
- [x] MkDocs build verifizieren (0 Warnings, 0 Errors)

## Transformationsregeln (Kurzreferenz)

| Vorher | Nachher |
|--------|---------|
| „kennen wir" | „es gibt" / „bekannt sind" |
| „tauchen wir ein" | Satz entfällt oder „im Folgenden:" |
| „behandeln wir in" | „Thema von Artikel X" / „siehe Artikel X" |
| „kühne Vermutung" | „Vermutung" |
| „spektakuläre Idee" | „Idee" / „Beobachtung" |
| „der Teufel steckt im Detail" | entfällt |
| „als hätte man eine unsichtbare Barriere überschritten" | entfällt |
| „davon geträumt" | „sich zum Ziel gesetzt" |
| Fehlende Zitate | 2–4 Blockquotes pro Artikel mit Quellenangabe |
