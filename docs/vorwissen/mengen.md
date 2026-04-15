---
title: "Sets and Set Operations"
description: "Notation, subsets, union, intersection, and power sets"
lang: en
type: vorwissen
---

# Sets and Set Operations

## What Is a Set?

A **set** is a collection of well-defined, distinct objects (**elements**). Notation: curly braces.

$$
A = \{1, 2, 3\}
$$

The symbol $\in$ means "is an element of": $2 \in A$. The symbol $\notin$ means "is not an element of": $5 \notin A$.

### Set-Builder Notation

Sets can be defined by a property:

$$
B = \{x \in \mathbb{Z} : x > 0 \text{ and } x < 10\} = \{1, 2, 3, 4, 5, 6, 7, 8, 9\}
$$

### Standard Sets

| Symbol | Set |
|--------|-----|
| $\emptyset$ or $\{\}$ | Empty set (contains no element) |
| $\mathbb{N}$ | Natural numbers $\{0, 1, 2, 3, \ldots\}$ |
| $\mathbb{Z}$ | Integers $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ |
| $\mathbb{Q}$ | Rational numbers |
| $\mathbb{R}$ | Real numbers |
| $\mathbb{C}$ | Complex numbers |

## Subsets

$A$ is a **subset** of $B$ ($A \subseteq B$) if every element of $A$ is also in $B$:

$$
A \subseteq B \iff \forall x: x \in A \Rightarrow x \in B
$$

**Example.** $\{1, 3\} \subseteq \{1, 2, 3, 4\}$.

$A \subset B$ (**proper subset**) means $A \subseteq B$ and $A \neq B$.

## Set Operations

### Union (∪)

$$
A \cup B = \{x : x \in A \text{ or } x \in B\}
$$

**Example.** $\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$.

### Intersection (∩)

$$
A \cap B = \{x : x \in A \text{ and } x \in B\}
$$

**Example.** $\{1, 2, 3\} \cap \{2, 3, 4\} = \{2, 3\}$.

### Difference (∖)

$$
A \setminus B = \{x : x \in A \text{ and } x \notin B\}
$$

**Example.** $\{1, 2, 3\} \setminus \{2, 4\} = \{1, 3\}$.

### Complement

The **complement** $\overline{A}$ (or $A^c$) contains all elements **not** in $A$ (relative to a universal set $U$):

$$
\overline{A} = U \setminus A
$$

## Power Set

The **power set** $\mathcal{P}(A)$ is the set of all subsets of $A$:

$$
\mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}
$$

For a set with $n$ elements, the power set has $2^n$ elements.

## Cartesian Product

The **Cartesian product** $A \times B$ is the set of all ordered pairs:

$$
A \times B = \{(a, b) : a \in A, b \in B\}
$$

**Example.** $\{1, 2\} \times \{a, b\} = \{(1, a), (1, b), (2, a), (2, b)\}$.

---

## Summary

| Operation | Symbol | Result |
|-----------|--------|--------|
| Element of | $\in$ | $x \in A$ |
| Subset | $\subseteq$ | Every element of $A$ is in $B$ |
| Union | $\cup$ | Elements in $A$ or $B$ |
| Intersection | $\cap$ | Elements in $A$ and $B$ |
| Difference | $\setminus$ | Elements in $A$, not in $B$ |
| Power set | $\mathcal{P}(A)$ | All subsets of $A$ |

## References

- Halmos, Paul R.: *Naive Set Theory.* Springer, 1974.
