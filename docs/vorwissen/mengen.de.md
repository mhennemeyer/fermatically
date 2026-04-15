---
title: "Mengen und Mengenoperationen"
description: "Notation, Teilmengen, Vereinigung, Durchschnitt und Potenzmengen"
lang: de
type: vorwissen
---

# Mengen und Mengenoperationen

## Was ist eine Menge?

Eine **Menge** ist eine Zusammenfassung wohlunterschiedener Objekte (**Elemente**) zu einem Ganzen. Notation: Geschweifte Klammern.

$$
A = \{1, 2, 3\}
$$

Das Symbol $\in$ bedeutet „ist Element von": $2 \in A$. Das Symbol $\notin$ bedeutet „ist kein Element von": $5 \notin A$.

### Beschreibende Notation

Mengen können durch eine Eigenschaft definiert werden:

$$
B = \{x \in \mathbb{Z} : x > 0 \text{ und } x < 10\} = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}
$$

### Besondere Mengen

| Symbol | Menge |
|--------|-------|
| $\emptyset$ oder $\{\}$ | Leere Menge (enthält kein Element) |
| $\mathbb{N}$ | Natürliche Zahlen $\{0, 1, 2, 3, \ldots\}$ |
| $\mathbb{Z}$ | Ganze Zahlen $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ |
| $\mathbb{Q}$ | Rationale Zahlen |
| $\mathbb{R}$ | Reelle Zahlen |
| $\mathbb{C}$ | Komplexe Zahlen |

## Teilmengen

$A$ ist **Teilmenge** von $B$ ($A \subseteq B$), wenn jedes Element von $A$ auch in $B$ liegt:

$$
A \subseteq B \iff \forall x: x \in A \Rightarrow x \in B
$$

**Beispiel.** $\{1, 3\} \subseteq \{1, 2, 3, 4\}$.

$A \subset B$ (**echte Teilmenge**) bedeutet $A \subseteq B$ und $A \neq B$.

## Mengenoperationen

### Vereinigung (∪)

$$
A \cup B = \{x : x \in A \text{ oder } x \in B\}
$$

**Beispiel.** $\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$.

### Durchschnitt (∩)

$$
A \cap B = \{x : x \in A \text{ und } x \in B\}
$$

**Beispiel.** $\{1, 2, 3\} \cap \{2, 3, 4\} = \{2, 3\}$.

### Differenz (∖)

$$
A \setminus B = \{x : x \in A \text{ und } x \notin B\}
$$

**Beispiel.** $\{1, 2, 3\} \setminus \{2, 4\} = \{1, 3\}$.

### Komplement

Das **Komplement** $\overline{A}$ (oder $A^c$) enthält alle Elemente, die **nicht** in $A$ liegen (bezogen auf eine Grundmenge $U$):

$$
\overline{A} = U \setminus A
$$

## Potenzmenge

Die **Potenzmenge** $\mathcal{P}(A)$ ist die Menge aller Teilmengen von $A$:

$$
\mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}
$$

Für eine Menge mit $n$ Elementen hat die Potenzmenge $2^n$ Elemente.

## Kartesisches Produkt

Das **kartesische Produkt** $A \times B$ ist die Menge aller geordneten Paare:

$$
A \times B = \{(a, b) : a \in A, b \in B\}
$$

**Beispiel.** $\{1, 2\} \times \{a, b\} = \{(1, a), (1, b), (2, a), (2, b)\}$.

---

## Zusammenfassung

| Operation | Symbol | Ergebnis |
|-----------|--------|----------|
| Element von | $\in$ | $x \in A$ |
| Teilmenge | $\subseteq$ | Alle Elemente von $A$ in $B$ |
| Vereinigung | $\cup$ | Elemente in $A$ oder $B$ |
| Durchschnitt | $\cap$ | Elemente in $A$ und $B$ |
| Differenz | $\setminus$ | Elemente in $A$, nicht in $B$ |
| Potenzmenge | $\mathcal{P}(A)$ | Alle Teilmengen von $A$ |

## Quellen

- Halmos, Paul R.: *Naive Set Theory.* Springer, 1974.
