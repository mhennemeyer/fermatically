---
title: "Relationen und Äquivalenzklassen"
description: "Äquivalenzrelation, Partition, Restklassen als Beispiel, Faktorstrukturen"
lang: de
type: vorwissen
---

# Relationen und Äquivalenzklassen

## Relationen

Eine **(binäre) Relation** auf einer Menge $M$ ist eine Teilmenge $R \subseteq M \times M$. Für $(a, b) \in R$ schreibt man $a \sim b$ (oder $aRb$).

**Beispiel.** Auf $\mathbb{Z}$ definiert „$a$ teilt $b$" eine Relation: $a \mid b$ genau dann, wenn $(a, b)$ in der Relation liegt.

## Äquivalenzrelationen

Eine Relation $\sim$ auf $M$ heißt **Äquivalenzrelation**, wenn sie drei Eigenschaften erfüllt:

| Eigenschaft | Bedingung |
|-------------|-----------|
| **Reflexivität** | $a \sim a$ für alle $a \in M$ |
| **Symmetrie** | $a \sim b \implies b \sim a$ |
| **Transitivität** | $a \sim b$ und $b \sim c \implies a \sim c$ |

**Beispiel.** „Gleicher Rest bei Division durch $n$" ist eine Äquivalenzrelation auf $\mathbb{Z}$:

$$
a \sim b \iff n \mid (a - b)
$$

Diese Relation heißt **Kongruenz modulo $n$** und wird als $a \equiv b \pmod{n}$ geschrieben.

## Äquivalenzklassen

Die **Äquivalenzklasse** eines Elements $a \in M$ bezüglich $\sim$ ist die Menge aller zu $a$ äquivalenten Elemente:

$$
[a] = \{x \in M : x \sim a\}
$$

> „Equivalence relations are ubiquitous in mathematics. They provide the mechanism by which we identify objects that are 'essentially the same'."
> — Serge Lang, *Algebra*, Springer, 2002.

**Beispiel.** Für die Kongruenz modulo $3$ auf $\mathbb{Z}$:

$$
[0] = \{\ldots, -6, -3, 0, 3, 6, \ldots\}, \quad [1] = \{\ldots, -5, -2, 1, 4, 7, \ldots\}, \quad [2] = \{\ldots, -4, -1, 2, 5, 8, \ldots\}
$$

Diese drei Klassen sind die **Restklassen modulo 3**.

### Eigenschaften

- Jedes Element gehört zu genau einer Äquivalenzklasse.
- Zwei Äquivalenzklassen sind entweder identisch oder disjunkt: $[a] = [b]$ oder $[a] \cap [b] = \emptyset$.
- $[a] = [b]$ genau dann, wenn $a \sim b$.

## Partition

Eine **Partition** einer Menge $M$ ist eine Zerlegung von $M$ in nichtleere, paarweise disjunkte Teilmengen, deren Vereinigung ganz $M$ ergibt.

**Fundamentaler Zusammenhang:** Jede Äquivalenzrelation auf $M$ erzeugt eine Partition von $M$ (die Menge der Äquivalenzklassen), und umgekehrt definiert jede Partition eine Äquivalenzrelation.

Die Menge aller Äquivalenzklassen heißt **Quotientenmenge** (oder Faktormenge):

$$
M / {\sim} = \{[a] : a \in M\}
$$

**Beispiel.** $\mathbb{Z}/{\equiv_n} = \{[0], [1], \ldots, [n-1]\}$ ist die Menge der Restklassen modulo $n$, gewöhnlich als $\mathbb{Z}/n\mathbb{Z}$ geschrieben.

## Faktorstrukturen in der Algebra

Äquivalenzklassen ermöglichen die Konstruktion neuer algebraischer Strukturen:

- **Restklassenringe:** $\mathbb{Z}/n\mathbb{Z}$ entsteht durch die Kongruenzrelation modulo $n$. Addition und Multiplikation werden auf den Klassen definiert: $[a] + [b] = [a+b]$ und $[a] \cdot [b] = [a \cdot b]$.

- **Faktorgruppen:** In einer Gruppe $G$ mit Normalteiler $N$ bilden die Nebenklassen $gN$ eine Gruppe $G/N$.

- **Faktorringe:** In einem Ring $R$ mit Ideal $I$ bilden die Nebenklassen $a + I$ einen Ring $R/I$.

Diese Konstruktionen durchziehen die gesamte abstrakte Algebra und sind zentral für die Theorie der Ringe und Körper, die im Beweis von Fermats Letztem Satz eine Rolle spielen.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Relation | $R \subseteq M \times M$ |
| Äquivalenzrelation | Reflexiv, symmetrisch, transitiv |
| Äquivalenzklasse | $[a] = \{x \in M : x \sim a\}$ |
| Partition | Zerlegung in disjunkte, nichtleere Teilmengen |
| Quotientenmenge | $M/{\sim} = \{[a] : a \in M\}$ |
| Restklassen | $\mathbb{Z}/n\mathbb{Z} = \{[0], [1], \ldots, [n-1]\}$ |

## Quellen

- Lang, Serge: *Algebra.* Springer, 3. Auflage, 2002. Kapitel I.
- Bourbaki, Nicolas: *Éléments de mathématique: Théorie des ensembles.* Springer, 2006. Kapitel II, § 6.
