# Fermats letzter Satz – Der Weg zum Beweis

!!! abstract "Überblick"
    Von der Vermutung eines Juristen aus dem 17. Jahrhundert bis zum 109-seitigen Beweis von Andrew Wiles (1995). Diese Artikelserie zeichnet den gesamten Weg nach – von elementarer Zahlentheorie über die Sprache der modernen Mathematik bis zum berühmten \(R = T\)-Theorem.

## Die Vermutung

**Fermats letzter Satz** besagt:

\[
x^n + y^n = z^n
\]

hat **keine** Lösung in positiven ganzen Zahlen \(x, y, z\) für \(n \geq 3\).

Pierre de Fermat notierte 1637 am Rand seines Exemplars von Diophants *Arithmetica*, er habe einen „wahrhaft wunderbaren Beweis" gefunden, für den der Rand zu klein sei. 358 Jahre später erschien Andrew Wiles' Beweis in den *Annals of Mathematics*.

---

## Der Weg in drei Akten

### 🔢 Akt 1: Elementare Zahlentheorie

Der Einstieg: Was besagt die Vermutung, und welche Spezialfälle konnte man früh beweisen?

| # | Artikel | Thema |
|---|---------|-------|
| 1 | [Was ist Fermats letzter Satz?](grundlagen/elementare-zahlentheorie/01-was-ist-flt.md) | Geschichte, Fermat, 350 Jahre Suche |
| 2 | [Der Beweis für \(n=4\)](grundlagen/elementare-zahlentheorie/02-beweis-n4.md) | Fermats eigener Beweis (Infinite Descent) |
| 3 | [Primzahlen und warum sie reichen](grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md) | Reduktion auf Primzahl-Exponenten |
| 4 | [Der Beweis für \(n=3\)](grundlagen/elementare-zahlentheorie/04-beweis-n3.md) | Euler, Gauß, algebraische Zahlen |

### 🔧 Akt 2: Werkzeuge der modernen Mathematik

Bevor der Beweis kommt, braucht man die richtige Sprache. Jedes dieser Themen ist eigenständig und wird in den Beweis-Artikeln referenziert.

→ [Werkzeuge im Überblick](werkzeuge/index.md)

- [Gruppen – Symmetrie als Sprache](werkzeuge/gruppen.md)
- [Ringe und Körper](werkzeuge/ringe-koerper.md)
- [Galois-Theorie](werkzeuge/galois-theorie.md)
- [p-adische Zahlen](werkzeuge/p-adische-zahlen.md)
- [Elliptische Kurven](werkzeuge/elliptische-kurven.md)
- [Modulformen](werkzeuge/modulformen.md)

### 🏔️ Akt 3: Der Beweis

Von der Taniyama-Shimura-Vermutung über Galois-Darstellungen bis zum \(R = T\)-Theorem.

| # | Artikel | Thema |
|---|---------|-------|
| 1 | [Die Taniyama-Shimura-Vermutung](fermat-wiles/01-taniyama-shimura.md) | Jede elliptische Kurve ist modular |
| 2 | [Freys Idee und Ribets Theorem](fermat-wiles/02-frey-ribet.md) | TSV ⟹ FLT |
| 3 | [Galois-Darstellungen](fermat-wiles/03-galois-darstellungen.md) | Elliptische Kurven als Matrizen |
| 4 | [Deformationstheorie](fermat-wiles/04-deformationstheorie.md) | Wie man Darstellungen verbiegt |
| 5 | [\(R = T\) – Das Herz des Beweises](fermat-wiles/05-r-gleich-t.md) | Wiles' zentrales Theorem |
| 6 | [Der Taylor-Wiles-Trick](fermat-wiles/06-taylor-wiles-trick.md) | Der minimale Fall |
| 7 | [Der 3-5-Switch und der Abschluss](fermat-wiles/07-3-5-switch.md) | Das Finale |
| 8 | [Was danach kam](fermat-wiles/08-was-danach-kam.md) | Vollständige TSV, Langlands-Programm |

---

## Empfohlene Reihenfolge

Die Artikel bauen aufeinander auf. Der empfohlene Weg:

1. **Elementare Zahlentheorie** (Akt 1) – als Einstieg
2. **Werkzeuge** (Akt 2) – bei Bedarf, oder wenn in einem Beweis-Artikel darauf verwiesen wird
3. **Der Beweis** (Akt 3) – streng der Reihe nach

!!! tip "Vorwissen"
    Für mathematische Grundlagen (Logik, Mengen, Arithmetik, Algebra) gibt es den Bereich [Vorwissen](vorwissen/index.md). Die Artikel dort werden aus der Storyline heraus verlinkt, wenn sie benötigt werden.
