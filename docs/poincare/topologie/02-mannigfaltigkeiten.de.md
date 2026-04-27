---
title: "Mannigfaltigkeiten"
slug: poincare/topologie/02-mannigfaltigkeiten
series: poincare
part: 2
act: topologie
date: 2026-04-25
status: draft
lang: de
tags:
  - topologie
  - mannigfaltigkeit
---

# Mannigfaltigkeiten

!!! abstract "Zusammenfassung"
    Eine Mannigfaltigkeit ist ein Raum, der lokal wie ein euklidischer
    Raum $\mathbb{R}^n$ aussieht, global aber kompliziert sein kann.
    Der Begriff ist die richtige Verallgemeinerung von „Kurve" und „Fläche"
    in beliebige Dimensionen und das Objekt, über das die Poincaré-Vermutung
    spricht.

## 1. Lokal euklidisch – die Grundidee

Eine Kreislinie sieht im Kleinen wie ein Stück Gerade aus, eine Kugelfläche
im Kleinen wie ein Stück Ebene. Diese lokale Übereinstimmung mit dem
euklidischen Raum macht solche Objekte handhabbar: Im Kleinen darf man wie
in $\mathbb{R}^n$ rechnen, im Großen liefert die Topologie das Verhalten.

Die formale Fassung:

> Ein Hausdorffraum $M$ heißt **$n$-dimensionale topologische
> Mannigfaltigkeit**, wenn jeder Punkt $p \in M$ eine offene Umgebung $U$
> besitzt, die zu einer offenen Teilmenge des $\mathbb{R}^n$ homöomorph ist.

Eine solche Homöomorphie $\varphi \colon U \to \varphi(U) \subseteq \mathbb{R}^n$
heißt **Karte**, eine Familie von Karten, die ganz $M$ überdeckt, ein
**Atlas**. Der Begriff der Karte und des Atlas stammt direkt aus der
Kartographie: Die Erdoberfläche – eine 2-Mannigfaltigkeit – wird durch
endlich viele flache Karten beschrieben.

> „A manifold is a topological space that locally looks like Euclidean
> space."
> — John M. Lee, *Introduction to Smooth Manifolds* (2013), S. 1

## 2. Beispiele in niedrigen Dimensionen

**Dimension 1.** Die einzigen zusammenhängenden geschlossenen
1-Mannigfaltigkeiten ohne Rand sind die Kreislinie $S^1$ und die Gerade
$\mathbb{R}$. Andere Beispiele: das offene und das halboffene Intervall.

**Dimension 2.** Geschlossene Flächen sind durch zwei Daten klassifiziert:
das **Geschlecht** $g$ (Anzahl der Henkel) und die Orientierbarkeit. Die
orientierbaren Vertreter sind die Sphäre $S^2$ ($g = 0$), der Torus
$T^2 = S^1 \times S^1$ ($g = 1$), die Doppeltorus-Fläche ($g = 2$), und so
fort. Nichtorientierbar sind die projektive Ebene $\mathbb{RP}^2$ und die
Kleinsche Flasche.

**Dimension 3.** Die Klassifikation ist hier ungleich schwieriger und das
Thema der Geometrisierungs-Vermutung (siehe
[Artikel 05](05-geometrisierungs-vermutung.md)). Die einfachsten Beispiele:
die 3-Sphäre $S^3$, der 3-Torus $T^3 = S^1 \times S^1 \times S^1$, und
$S^2 \times S^1$.

## 3. Geschlossen, offen, mit Rand

Drei Adjektive treten in jeder Diskussion über Mannigfaltigkeiten auf:

**Geschlossen.** Eine Mannigfaltigkeit heißt **geschlossen**, wenn sie
kompakt ist und keinen Rand besitzt. Sphäre, Torus und projektive Ebene
sind geschlossen, die offene Ebene $\mathbb{R}^2$ ist es nicht. Wichtig: Im
topologischen Sprachgebrauch ist „geschlossen" *nicht* das Gegenteil von
„offen" wie bei Teilmengen.

**Offen.** Im Kontext von Mannigfaltigkeiten meint *offen* meist
„nicht-kompakt und ohne Rand" – etwa $\mathbb{R}^n$ oder eine offene
Halbebene.

**Mit Rand.** Eine $n$-Mannigfaltigkeit *mit Rand* erlaubt zusätzlich
Karten, deren Bild im abgeschlossenen Halbraum
$\{x \in \mathbb{R}^n : x_n \geq 0\}$ liegt. Der Rand $\partial M$ ist
selbst eine geschlossene $(n-1)$-Mannigfaltigkeit. Beispiel: Die abgeschlossene
Vollkugel $D^3$ ist eine 3-Mannigfaltigkeit mit Rand $\partial D^3 = S^2$.

Die Poincaré-Vermutung handelt von **geschlossenen** 3-Mannigfaltigkeiten.

## 4. Glatte Mannigfaltigkeiten

Auf einer topologischen Mannigfaltigkeit lassen sich Begriffe wie
„Stetigkeit" und „Homöomorphie" definieren, aber noch keine Differentiation.
Dafür braucht man eine zusätzliche Struktur:

> Ein Atlas heißt **glatt** ($C^\infty$), wenn alle
> **Kartenwechsel** $\varphi_j \circ \varphi_i^{-1}$ – Homöomorphismen
> zwischen offenen Teilmengen des $\mathbb{R}^n$ – unendlich oft
> differenzierbar sind. Eine **glatte Mannigfaltigkeit** ist eine
> topologische Mannigfaltigkeit zusammen mit einer maximalen glatten
> Atlasstruktur.

Auf einer glatten Mannigfaltigkeit kann man von glatten Funktionen
$f \colon M \to \mathbb{R}$, glatten Abbildungen $M \to N$ und
**Diffeomorphismen** sprechen – Homöomorphismen, deren Umkehrung ebenfalls
glatt ist. Diffeomorphie ist die natürliche Äquivalenz für glatte
Mannigfaltigkeiten.

Das Verhältnis von topologischer und glatter Klassifikation ist subtil:

- In Dimension $\leq 3$ besitzt jede topologische Mannigfaltigkeit eine
  eindeutige glatte Struktur (Moise 1952).
- In Dimension 4 existieren $\mathbb{R}^4$-Versionen, die homöomorph, aber
  nicht diffeomorph zum Standard-$\mathbb{R}^4$ sind – eine Entdeckung von
  Donaldson (1983) und Freedman.
- In Dimension 7 fand Milnor (1956) sieben paarweise nicht-diffeomorphe
  glatte Strukturen auf der topologischen 7-Sphäre – die berühmten
  **exotischen Sphären**.

Für die Poincaré-Vermutung in Dimension 3 spielt diese Unterscheidung keine
Rolle: topologisch und glatt fallen zusammen. Der Beweis von Perelman
arbeitet dennoch glatt, weil der Ricci-Fluss eine Differentialgleichung für
glatte Riemannsche Metriken ist.

## 5. Riemannsche Mannigfaltigkeiten

Auf einer glatten Mannigfaltigkeit lässt sich differenzieren, aber noch
nicht messen. Eine **Riemannsche Metrik** $g$ ordnet jedem Punkt
$p \in M$ ein Skalarprodukt $g_p$ auf dem Tangentialraum $T_pM$ zu, das
glatt von $p$ abhängt. Damit lassen sich Längen von Kurven, Winkel,
Volumina und – als Krümmungstensor – die lokale Geometrie definieren.

Eine **Riemannsche Mannigfaltigkeit** $(M, g)$ ist die zentrale Bühne von
Akt 2 der Poincaré-Storyline: Hamiltons Ricci-Fluss
$\partial_t g_{ij} = -2 R_{ij}$ ist eine Evolutionsgleichung gerade für
solche Metriken (siehe [Akt 2](../ricci-fluss/index.md)).

Wichtig für das Verständnis der Vermutung: *Welche* Riemannsche Metrik man
auf einer Mannigfaltigkeit wählt, ist topologisch unerheblich – die
Vermutung ist eine Aussage über die Mannigfaltigkeit, nicht über die
Metrik. Im Beweis aber wird gezielt eine Metrik gewählt, ihre Evolution
unter dem Ricci-Fluss kontrolliert und am Ende eine topologische
Schlussfolgerung gezogen.

## 6. Beispiele für die Storyline

Drei Mannigfaltigkeiten tauchen in der Poincaré-Diskussion immer wieder
auf:

**Die 3-Sphäre $S^3$.** Definierbar als
$\{x \in \mathbb{R}^4 : \|x\| = 1\}$ oder, dual dazu, als
Einpunkt-Kompaktifizierung von $\mathbb{R}^3$. Sie ist die einzige
geschlossene, einfach zusammenhängende 3-Mannigfaltigkeit – das ist
gerade die Aussage der Poincaré-Vermutung.

**Der 3-Torus $T^3$.** Das Produkt $S^1 \times S^1 \times S^1$, anschaulich
ein Würfel mit gegenüberliegenden Flächen verklebt. Geschlossen, aber
nicht einfach zusammenhängend; seine Fundamentalgruppe ist $\mathbb{Z}^3$.

**Linsenräume $L(p,q)$.** Quotienten der 3-Sphäre $S^3$ unter freier
Wirkung einer endlichen zyklischen Gruppe $\mathbb{Z}/p$. Sie liefern
Beispiele geschlossener 3-Mannigfaltigkeiten mit endlicher
Fundamentalgruppe – topologisch nicht-trivial, im Sinne der Vermutung
„nicht einfach zusammenhängend".

## 7. Ausblick

Im nächsten Artikel werden die Begriffe **Schleife**, **Homotopie** und
**Fundamentalgruppe** eingeführt und die $n$-dimensionale Sphäre $S^n$
genauer untersucht. Erst damit lässt sich präzise sagen, was *einfach
zusammenhängend* heißt und warum diese Eigenschaft die 3-Sphäre unter
allen geschlossenen 3-Mannigfaltigkeiten auszeichnet.

| Artikel | Thema |
|---------|-------|
| [03 – Die Sphäre und einfacher Zusammenhang](03-sphaere-einfacher-zusammenhang.md) | $S^n$, Fundamentalgruppe, Homotopie |
| [04 – Was ist die Poincaré-Vermutung?](04-was-ist-poincare-vermutung.md) | Originalformulierung 1904 |

!!! tip "Vorwissen"
    Tangentialräume, Tensoren und Krümmung werden im
    [Vorwissen](../../vorwissen/index.md), Block „Geometrie und Analysis
    (Aufbau)", anschaulich vorbereitet. Für die Lektüre dieses Artikels
    reicht die Vorstellung „lokal wie $\mathbb{R}^n$".

---

## Quellen

- **John M. Lee**: *Introduction to Topological Manifolds*, 2. Auflage,
  Springer (2011)
- **John M. Lee**: *Introduction to Smooth Manifolds*, 2. Auflage,
  Springer (2013)
- **John Milnor**: *On manifolds homeomorphic to the 7-sphere*, Annals of
  Mathematics 64 (1956), 399–405
- **Edwin E. Moise**: *Affine structures in 3-manifolds. V. The
  triangulation theorem and Hauptvermutung*, Annals of Mathematics 56
  (1952), 96–114
