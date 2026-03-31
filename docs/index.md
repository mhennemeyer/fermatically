# fermatically – Große Beweise verstehen

> *Von elementarer Schulmathematik bis zu den großen Beweisen der Mathematik.*

!!! note "Hinweis"
    Die Artikel auf dieser Plattform werden mit Unterstützung von **Künstlicher Intelligenz** erstellt und redaktionell geprüft.

---

## Worum geht es?

Diese Plattform nimmt dich mit auf eine Reise durch die Mathematik – vom pythagoräischen Satz bis zum Beweis von **Fermats letztem Satz** durch Andrew Wiles (1995).

Das Ziel: **Höhere Mathematik zugänglich machen**, ohne zu vereinfachen. Jedes Thema baut auf dem vorherigen auf, sodass du mit Schulmathematik starten und Schritt für Schritt bis zu den tiefsten Ergebnissen der modernen Zahlentheorie vordringen kannst.

## Die Reise

### 🔢 Grundlagen – Elementare Zahlentheorie

Hier beginnt alles: Was ist Fermats letzter Satz? Warum hat er 350 Jahre lang der Mathematik widerstanden? Und welche Spezialfälle konnte man schon früh beweisen?

- [Was ist Fermats letzter Satz?](grundlagen/elementare-zahlentheorie/01-was-ist-flt.md) – Geschichte, Fermat, 350 Jahre Suche
- [Der Beweis für \(n=4\)](grundlagen/elementare-zahlentheorie/02-beweis-n4.md) – Fermats eigener Beweis (Infinite Descent)
- [Primzahlen und warum sie reichen](grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md) – Reduktion auf Primzahl-Exponenten
- [Der Beweis für \(n=3\)](grundlagen/elementare-zahlentheorie/04-beweis-n3.md) – Euler, Gauß, algebraische Zahlen

### 🔧 Werkzeuge – Die Sprache der modernen Mathematik

Bevor wir Wiles' Beweis verstehen können, brauchen wir die richtigen Werkzeuge. Jedes dieser Themen ist eigenständig lesbar und wird in mehreren Beweis-Themen referenziert.

- [Gruppen](werkzeuge/gruppen.md) – Symmetrie als Sprache der Mathematik
- [Ringe und Körper](werkzeuge/ringe-koerper.md) – Die Welt jenseits der rationalen Zahlen
- [Galois-Theorie](werkzeuge/galois-theorie.md) – Warum Gleichungen keine Lösungsformeln haben
- [p-adische Zahlen](werkzeuge/p-adische-zahlen.md) – Eine andere Art, Zahlen zu betrachten
- [Elliptische Kurven](werkzeuge/elliptische-kurven.md) – Von Diophant zu Kryptographie
- [Modulformen](werkzeuge/modulformen.md) – Symmetrische Funktionen der oberen Halbebene

### 🏔️ Der Beweis – Fermats letzter Satz (Wiles, 1995)

Das Herzstück: Von der Taniyama-Shimura-Vermutung über Galois-Darstellungen bis zum berühmten \(R = T\)-Theorem.

- [Die Taniyama-Shimura-Vermutung](fermat-wiles/01-taniyama-shimura.md) – Jede elliptische Kurve ist modular
- [Freys Idee und Ribets Theorem](fermat-wiles/02-frey-ribet.md) – TSV ⟹ FLT
- [Galois-Darstellungen](fermat-wiles/03-galois-darstellungen.md) – Elliptische Kurven als Matrizen
- [Deformationstheorie](fermat-wiles/04-deformationstheorie.md) – Wie man Darstellungen verbiegt
- [\(R = T\) – Das Herz des Beweises](fermat-wiles/05-r-gleich-t.md) – Wiles' zentrales Theorem
- [Der Taylor-Wiles-Trick](fermat-wiles/06-taylor-wiles-trick.md) – Der minimale Fall
- [Der 3-5-Switch und der Abschluss](fermat-wiles/07-3-5-switch.md) – Das Finale
- [Was danach kam](fermat-wiles/08-was-danach-kam.md) – Vollständige TSV, Langlands-Programm

---

!!! info "Status"
    Diese Plattform befindet sich im Aufbau. Die Artikel werden nach und nach veröffentlicht.

!!! note "KI-generierte Inhalte"
    Die Inhalte dieser Plattform werden mit Unterstützung von Künstlicher Intelligenz (KI) erstellt. Alle Artikel werden sorgfältig geprüft, können aber Fehler enthalten. Bei Fragen oder Korrekturen freuen wir uns über Rückmeldungen.

## Fermats letzter Satz – kurz erklärt

**Fermats letzter Satz** besagt:

\[
x^n + y^n = z^n
\]

hat für \(n \geq 3\) **keine** Lösung in positiven ganzen Zahlen \(x, y, z\).

Pierre de Fermat notierte 1637 am Rand seines Exemplars der *Arithmetica* von Diophant, er habe einen „wahrhaft wunderbaren Beweis" gefunden, der aber auf dem Rand keinen Platz hätte. 358 Jahre später gelang Andrew Wiles der Beweis – auf 109 Seiten, mit Methoden, die Fermat sich nicht hätte vorstellen können.
