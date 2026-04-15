# fermatically – Große Beweise verstehen

> *Von elementarer Schulmathematik bis zu den großen Beweisen der Mathematik.*

!!! note "Hinweis"
    Die Artikel auf dieser Plattform werden mit Unterstützung von **Künstlicher Intelligenz** erstellt und redaktionell geprüft.

---

## Worum geht es?

Diese Plattform erschließt die Mathematik schrittweise – vom pythagoräischen Satz bis zum Beweis von **Fermats letztem Satz** durch Andrew Wiles (1995).

Ziel ist es, höhere Mathematik zugänglich zu machen, ohne sie zu vereinfachen. Jedes Thema baut auf dem vorherigen auf: Ausgangspunkt ist die Schulmathematik, Endpunkt sind die Kernresultate der modernen Zahlentheorie.

## Artikelübersicht

### 🔢 Grundlagen – Elementare Zahlentheorie

Ausgangspunkt der Serie: Was besagt Fermats letzter Satz? Warum widerstand er 350 Jahre lang jedem Beweisversuch? Welche Spezialfälle wurden früh bewiesen?

- [Was ist Fermats letzter Satz?](grundlagen/elementare-zahlentheorie/01-was-ist-flt.md) – Geschichte, Fermat, 350 Jahre Suche
- [Der Beweis für \(n=4\)](grundlagen/elementare-zahlentheorie/02-beweis-n4.md) – Fermats eigener Beweis (Infinite Descent)
- [Primzahlen und warum sie reichen](grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md) – Reduktion auf Primzahl-Exponenten
- [Der Beweis für \(n=3\)](grundlagen/elementare-zahlentheorie/04-beweis-n3.md) – Euler, Gauß, algebraische Zahlen

### 🔧 Werkzeuge – Die Sprache der modernen Mathematik

Vor dem Beweis stehen die Werkzeuge. Jedes dieser Themen ist eigenständig lesbar und wird in mehreren Beweis-Artikeln vorausgesetzt.

- [Gruppen](werkzeuge/gruppen.md) – Symmetrie als Sprache der Mathematik
- [Ringe und Körper](werkzeuge/ringe-koerper.md) – Die Welt jenseits der rationalen Zahlen
- [Galois-Theorie](werkzeuge/galois-theorie.md) – Warum Gleichungen keine Lösungsformeln haben
- [p-adische Zahlen](werkzeuge/p-adische-zahlen.md) – Eine andere Art, Zahlen zu betrachten
- [Elliptische Kurven](werkzeuge/elliptische-kurven.md) – Von Diophant zu Kryptographie
- [Modulformen](werkzeuge/modulformen.md) – Symmetrische Funktionen der oberen Halbebene

### 🏔️ Der Beweis – Fermats letzter Satz (Wiles, 1995)

Von der Taniyama-Shimura-Vermutung über Galois-Darstellungen bis zum \(R = T\)-Theorem.

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

## Fermats letzter Satz

**Fermats letzter Satz** besagt:

\[
x^n + y^n = z^n
\]

hat für \(n \geq 3\) **keine** Lösung in positiven ganzen Zahlen \(x, y, z\).

Pierre de Fermat notierte 1637 am Rand seines Exemplars der *Arithmetica* von Diophant, er habe einen „wahrhaft wunderbaren Beweis" gefunden, der aber auf dem Rand keinen Platz hätte. 358 Jahre später erschien Andrew Wiles' Beweis in den *Annals of Mathematics* – auf 109 Seiten, mit Methoden aus der algebraischen Geometrie und Zahlentheorie, die zu Fermats Zeit nicht existierten.
