---
title: "Was ist Topologie?"
slug: poincare/topologie/01-was-ist-topologie
series: poincare
part: 1
act: topologie
date: 2026-04-25
status: draft
lang: de
tags:
  - topologie
  - intuition
---

# Was ist Topologie?

!!! abstract "Zusammenfassung"
    Topologie untersucht Eigenschaften geometrischer Objekte, die unter
    stetiger Verformung erhalten bleiben. Begriffe wie *homöomorph*,
    *Stetigkeit*, *Zusammenhang* und *kompakt* bilden die Sprache, in der
    Poincaré 1904 seine Vermutung formulierte.

## 1. Geometrie ohne Lineal

Klassische Geometrie misst Längen, Winkel und Flächen. Topologie verzichtet
auf jede Metrik. Sie fragt: *Welche Eigenschaften eines Raumes überleben,
wenn man ihn beliebig dehnt, staucht und biegt – nur ohne ihn zu zerreißen
oder zu verkleben?*

Die typische Anekdote: Für die Topologie sind eine Kaffeetasse und ein Donut
dasselbe Objekt. Beide Oberflächen besitzen genau ein Loch, und eine stetige
Verformung überführt die eine in die andere. Eine Kugel hingegen hat kein
Loch und ist topologisch von Tasse und Donut verschieden.

> „Topology is the study of those properties of geometric objects that
> remain unchanged under continuous deformations."
> — John M. Lee, *Introduction to Topological Manifolds* (2011), S. 1

## 2. Stetigkeit als Grundbegriff

Aus der Analysis ist Stetigkeit als $\varepsilon$-$\delta$-Eigenschaft von
Funktionen $\mathbb{R} \to \mathbb{R}$ vertraut. Topologisch lässt sie sich
allgemeiner fassen: Eine Abbildung $f \colon X \to Y$ zwischen zwei Räumen
heißt **stetig**, wenn das Urbild jeder offenen Menge offen ist.

Diese Definition setzt nur den Begriff *offene Menge* voraus. Ein
**topologischer Raum** ist entsprechend eine Menge $X$ zusammen mit einem
System ausgewählter Teilmengen – den offenen Mengen –, die drei einfache
Bedingungen erfüllen: $\emptyset$ und $X$ sind offen, beliebige
Vereinigungen offener Mengen sind offen, endliche Schnitte offener Mengen
sind offen.

Aus diesem schmalen Fundament wachsen sämtliche topologischen Begriffe.

## 3. Homöomorphie – die topologische Gleichheit

Wann sind zwei Räume topologisch gleich? Wenn es eine **Homöomorphie**
zwischen ihnen gibt: eine bijektive Abbildung $f \colon X \to Y$, sodass
$f$ und $f^{-1}$ stetig sind.

$$
X \cong Y \quad :\Longleftrightarrow \quad
\exists\, f \colon X \to Y \text{ Homöomorphismus.}
$$

- Eine Sphäre und ein Würfel-Rand sind homöomorph: Beide sind geschlossene
  zweidimensionale Flächen ohne Loch.
- Ein offenes Intervall $(0,1)$ ist homöomorph zu $\mathbb{R}$.
- Ein Kreis und eine Strecke sind *nicht* homöomorph: Entfernt man einen
  inneren Punkt aus der Strecke, zerfällt sie in zwei Stücke; entfernt man
  einen Punkt aus dem Kreis, bleibt er zusammenhängend.

Das letzte Beispiel illustriert die typische Beweistechnik: Man identifiziert
eine Eigenschaft, die unter Homöomorphie erhalten bleibt – eine
**topologische Invariante** –, und unterscheidet damit Räume.

## 4. Topologische Invarianten

Eine topologische Invariante ist eine Größe oder Eigenschaft, die für
homöomorphe Räume übereinstimmt. Drei der elementarsten:

**Zusammenhang.** Ein Raum heißt zusammenhängend, wenn er sich nicht in zwei
disjunkte nichtleere offene Teile zerlegen lässt. Eine Kreislinie ist
zusammenhängend, eine Vereinigung zweier disjunkter Kreise nicht.

**Kompaktheit.** Sie verallgemeinert die Vorstellung „abgeschlossen und
beschränkt" auf beliebige topologische Räume. Eine Sphäre ist kompakt, eine
Ebene nicht.

**Dimension.** Anschaulich die Anzahl unabhängiger Richtungen. Dass sie eine
Invariante ist – $\mathbb{R}^m$ ist genau dann homöomorph zu $\mathbb{R}^n$,
wenn $m = n$ – ist ein nichttriviales Ergebnis (Brouwer 1911) und gehört zu
den Gründungsleistungen der algebraischen Topologie.

Über diese drei hinaus liefern Algebraisierungen wie die **Fundamentalgruppe**
(siehe [Artikel 03](03-sphaere-einfacher-zusammenhang.md)) und die
**Homologie- und Kohomologiegruppen** feinere Invarianten. Sie ordnen jedem
Raum eine algebraische Struktur zu, die unter Homöomorphie erhalten bleibt.

## 5. Eine kurze Geschichte

**Euler (1736).** Das **Königsberger Brückenproblem** und die
**Polyederformel** $V - E + F = 2$ gelten als erste topologische
Resultate – Aussagen über kombinatorische Struktur, unabhängig von Maß und
Form.

**Riemann (1857).** Im Studium algebraischer Funktionen führte Riemann die
nach ihm benannten **Riemannschen Flächen** ein und unterschied geschlossene
Flächen nach ihrem **Geschlecht** $g$ – der Anzahl der Henkel.

**Poincaré (1895–1904).** In *Analysis Situs* legte Henri Poincaré das
Fundament der modernen algebraischen Topologie: Fundamentalgruppe,
Homologie, Bettische Zahlen, Triangulierung. Sein Aufsatz endet mit der
Frage, die heute als Poincaré-Vermutung bekannt ist (siehe
[Artikel 04](04-was-ist-poincare-vermutung.md)).

**Hausdorff (1914).** Mit *Grundzüge der Mengenlehre* etablierte Felix
Hausdorff die axiomatische Definition topologischer Räume in der bis heute
üblichen Form.

> „Henri Poincaré, more than any other person, is responsible for the
> emergence of topology as an independent branch of mathematics."
> — Allen Hatcher, *Algebraic Topology* (2002), Vorwort

## 6. Warum Topologie für Poincaré?

Die Poincaré-Vermutung ist eine rein topologische Aussage: Sie macht keine
Aussage über Längen, Winkel oder Krümmung, sondern nur über die *Form* einer
dreidimensionalen Mannigfaltigkeit (siehe
[Artikel 02](02-mannigfaltigkeiten.md)). Konkret behauptet sie, dass eine
geschlossene 3-Mannigfaltigkeit, in der jede Schleife stetig zu einem Punkt
zusammenziehbar ist, zur 3-Sphäre $S^3$ homöomorph sein muss.

Bemerkenswert ist der Weg, den der Beweis nimmt: Perelman und Hamilton
führen die topologische Frage über Riemannsche Metriken und den Ricci-Fluss
in die Differentialgeometrie zurück. Die topologische Aussage wird gewonnen,
indem Geometrie kontrolliert wird – ein Muster, das auch Wiles' Beweis von
Fermats letztem Satz prägt.

## 7. Ausblick

Die folgenden Artikel führen die für die Vermutung benötigten topologischen
Begriffe systematisch ein:

| Artikel | Thema |
|---------|-------|
| [02 – Mannigfaltigkeiten](02-mannigfaltigkeiten.md) | Lokal euklidische Räume, Dimension, geschlossen vs. mit Rand |
| [03 – Die Sphäre und einfacher Zusammenhang](03-sphaere-einfacher-zusammenhang.md) | $S^n$, Fundamentalgruppe, Homotopie |
| [04 – Was ist die Poincaré-Vermutung?](04-was-ist-poincare-vermutung.md) | Original 1904, Verallgemeinerung, höhere Dimensionen |
| [05 – Die Geometrisierungs-Vermutung](05-geometrisierungs-vermutung.md) | Acht Modellgeometrien, Thurston |

!!! tip "Vorwissen"
    Wer vorher Begriffe wie offene Menge, Stetigkeit oder Konvergenz
    auffrischen möchte, findet im [Vorwissen](../../vorwissen/index.md)
    Einstiege in Mengenlehre und Analysis.

---

## Quellen

- **Allen Hatcher**: *Algebraic Topology*, Cambridge University Press (2002)
- **John M. Lee**: *Introduction to Topological Manifolds*, 2. Auflage,
  Springer (2011)
- **Henri Poincaré**: *Analysis Situs*, Journal de l'École Polytechnique 1
  (1895), 1–123
- **Felix Hausdorff**: *Grundzüge der Mengenlehre*, Veit & Comp., Leipzig
  (1914)
