---
title: "Relations and Equivalence Classes"
description: "Equivalence relations, partitions, residue classes as example, quotient structures"
lang: en
type: vorwissen
---

# Relations and Equivalence Classes

## Relations

A **(binary) relation** on a set $M$ is a subset $R \subseteq M \times M$. For $(a, b) \in R$, one writes $a \sim b$ (or $aRb$).

**Example.** On $\mathbb{Z}$, "$a$ divides $b$" defines a relation: $a \mid b$ precisely when $(a, b)$ belongs to the relation.

## Equivalence Relations

A relation $\sim$ on $M$ is an **equivalence relation** if it satisfies three properties:

| Property | Condition |
|----------|-----------|
| **Reflexivity** | $a \sim a$ for all $a \in M$ |
| **Symmetry** | $a \sim b \implies b \sim a$ |
| **Transitivity** | $a \sim b$ and $b \sim c \implies a \sim c$ |

**Example.** "Same remainder upon division by $n$" is an equivalence relation on $\mathbb{Z}$:

$$
a \sim b \iff n \mid (a - b)
$$

This relation is called **congruence modulo $n$** and is written $a \equiv b \pmod{n}$.

## Equivalence Classes

The **equivalence class** of an element $a \in M$ with respect to $\sim$ is the set of all elements equivalent to $a$:

$$
[a] = \{x \in M : x \sim a\}
$$

> "Equivalence relations are ubiquitous in mathematics. They provide the mechanism by which we identify objects that are 'essentially the same'."
> — Serge Lang, *Algebra*, Springer, 2002.

**Example.** For congruence modulo $3$ on $\mathbb{Z}$:

$$
[0] = \{\ldots, -6, -3, 0, 3, 6, \ldots\}, \quad [1] = \{\ldots, -5, -2, 1, 4, 7, \ldots\}, \quad [2] = \{\ldots, -4, -1, 2, 5, 8, \ldots\}
$$

These three classes are the **residue classes modulo 3**.

### Properties

- Every element belongs to exactly one equivalence class.
- Two equivalence classes are either identical or disjoint: $[a] = [b]$ or $[a] \cap [b] = \emptyset$.
- $[a] = [b]$ if and only if $a \sim b$.

## Partitions

A **partition** of a set $M$ is a decomposition of $M$ into nonempty, pairwise disjoint subsets whose union is all of $M$.

**Fundamental connection:** Every equivalence relation on $M$ produces a partition of $M$ (the set of equivalence classes), and conversely every partition defines an equivalence relation.

The set of all equivalence classes is called the **quotient set** (or factor set):

$$
M / {\sim} = \{[a] : a \in M\}
$$

**Example.** $\mathbb{Z}/{\equiv_n} = \{[0], [1], \ldots, [n-1]\}$ is the set of residue classes modulo $n$, usually written $\mathbb{Z}/n\mathbb{Z}$.

## Quotient Structures in Algebra

Equivalence classes enable the construction of new algebraic structures:

- **Residue class rings:** $\mathbb{Z}/n\mathbb{Z}$ arises from the congruence relation modulo $n$. Addition and multiplication are defined on the classes: $[a] + [b] = [a+b]$ and $[a] \cdot [b] = [a \cdot b]$.

- **Quotient groups:** In a group $G$ with normal subgroup $N$, the cosets $gN$ form a group $G/N$.

- **Quotient rings:** In a ring $R$ with ideal $I$, the cosets $a + I$ form a ring $R/I$.

These constructions pervade abstract algebra and are central to the theory of rings and fields that plays a role in the proof of Fermat's Last Theorem.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Relation | $R \subseteq M \times M$ |
| Equivalence relation | Reflexive, symmetric, transitive |
| Equivalence class | $[a] = \{x \in M : x \sim a\}$ |
| Partition | Decomposition into disjoint, nonempty subsets |
| Quotient set | $M/{\sim} = \{[a] : a \in M\}$ |
| Residue classes | $\mathbb{Z}/n\mathbb{Z} = \{[0], [1], \ldots, [n-1]\}$ |

## References

- Lang, Serge: *Algebra.* Springer, 3rd edition, 2002. Chapter I.
- Bourbaki, Nicolas: *Éléments de mathématique: Theory of Sets.* Springer, 2006. Chapter II, § 6.
