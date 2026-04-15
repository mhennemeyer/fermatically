---
title: "Groups – Symmetry as the Language of Mathematics"
slug: gruppen-und-symmetrie/01-gruppen
series: gruppen-und-symmetrie
part: 1
date: 2026-03-31
status: draft
lang: en
category: algebra
tags:
  - groups
  - symmetry
  - algebra
requires: []
---

# Groups – Symmetry as the Language of Mathematics

!!! abstract "Summary"
    What do rotations of a square, addition of integers, and the symmetries of equations have in common?
    They are all **groups** – the most fundamental algebraic structure of modern mathematics.

## Prerequisites

None – this article is the entry point to abstract algebra.

---

## 1. Symmetry in Everyday Life

A square can be rotated (by 90°, 180°, 270°) and reflected (across four axes) – that makes a total of **eight symmetries**. Each individual symmetry maps the square onto itself, and two symmetries performed in succession yield another symmetry.

This observation can be generalised: wherever there are symmetries – in geometry, in physics, in number theory – there is a mathematical structure behind them that always obeys the same rules. This structure is called a **group**.

Some examples that at first glance seem to have nothing in common:

- The **rotations and reflections** of a regular $n$-gon
- **Addition** of integers: $3 + 5 = 8$, $7 + (-7) = 0$
- The **permutations** of a set: rearrangements of $\{1, 2, 3\}$
- The **symmetries of the roots** of a polynomial (→ Galois theory)

All these examples satisfy the same four rules.

## 2. The Group Axioms

A **group** is a pair $(G, \cdot)$ consisting of a set $G$ and an operation $\cdot : G \times G \to G$ satisfying four axioms:

**(G1) Closure.** For all $a, b \in G$, $a \cdot b \in G$.

**(G2) Associativity.** For all $a, b, c \in G$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.

**(G3) Identity element.** There exists an element $e \in G$ with $e \cdot a = a \cdot e = a$ for all $a \in G$.

**(G4) Inverses.** For every $a \in G$ there exists an element $a^{-1} \in G$ with $a \cdot a^{-1} = a^{-1} \cdot a = e$.

If additionally $a \cdot b = b \cdot a$ for all $a, b \in G$, the group is called **abelian** (or commutative) – named after Niels Henrik Abel.

!!! note "Notation"
    For abelian groups, the operation is often written as $+$ instead of $\cdot$ and the identity element as $0$ instead of $e$. The inverse of $a$ is then $-a$.

## 3. First Examples

### The integers $(\mathbb{Z}, +)$

The simplest infinite group: the integers under addition.

- **Closed**: $a + b \in \mathbb{Z}$ for all $a, b \in \mathbb{Z}$ ✓
- **Associative**: $(a + b) + c = a + (b + c)$ ✓
- **Identity element**: $0$ (since $a + 0 = a$) ✓
- **Inverses**: $-a$ (since $a + (-a) = 0$) ✓
- **Abelian**: $a + b = b + a$ ✓

### Residue classes $(\mathbb{Z}/n\mathbb{Z}, +)$

For $n \geq 1$, the residue classes modulo $n$ form a finite abelian group. For example, $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ with addition modulo $4$:

| $+$   | $0$ | $1$ | $2$ | $3$ |
|-------|-----|-----|-----|-----|
| $0$   | $0$ | $1$ | $2$ | $3$ |
| $1$   | $1$ | $2$ | $3$ | $0$ |
| $2$   | $2$ | $3$ | $0$ | $1$ |
| $3$   | $3$ | $0$ | $1$ | $2$ |

This group has **order** $4$ (four elements). It is cyclic: every element can be written as a multiple of $1$.

### The symmetric group $S_n$

The **symmetric group** $S_n$ consists of all permutations (rearrangements) of the set $\{1, 2, \ldots, n\}$, with composition as the operation.

$S_3$ has $3! = 6$ elements:

$$
\text{id}, \quad (12), \quad (13), \quad (23), \quad (123), \quad (132)
$$

Here $(12)$ means "swap $1$ and $2$", and $(123)$ means "send $1 \to 2 \to 3 \to 1$".

**Caution:** $S_3$ is **not** abelian! We have $(12) \circ (13) = (132)$, but $(13) \circ (12) = (123)$.

### The dihedral group $D_n$

The symmetry group of a regular $n$-gon is called the **dihedral group** $D_n$. It has $2n$ elements: $n$ rotations and $n$ reflections. For $n = 4$ (square), $|D_4| = 8$.

## 4. Subgroups and Order

A subset $H \subseteq G$ is called a **subgroup** of $G$ if $H$ itself forms a group under the restricted operation. One writes $H \leq G$.

**Examples:**
- $2\mathbb{Z} = \{\ldots, -4, -2, 0, 2, 4, \ldots\} \leq \mathbb{Z}$ (the even integers)
- $\{e, (123), (132)\} \leq S_3$ (the rotations of the triangle)

The **order** $|G|$ of a group is the number of its elements. The **order** $\text{ord}(a)$ of an element $a$ is the smallest positive integer $n$ with $a^n = e$.

**Lagrange's theorem.** If $H \leq G$ with $|G| < \infty$, then $|H|$ divides $|G|$.

Consequence: in a group with $12$ elements, a subgroup can only have $1$, $2$, $3$, $4$, $6$, or $12$ elements. The order of every element divides $|G|$.

!!! tip "Lagrange in action"
    Let $G$ be a group with $|G| = p$ (prime). Then $G$ has no proper subgroups other than $\{e\}$ and $G$ itself. Hence $G$ is cyclic: $G \cong \mathbb{Z}/p\mathbb{Z}$.

## 5. Homomorphisms

A **group homomorphism** is a map $\varphi: G \to H$ between two groups that preserves the structure:

$$
\varphi(a \cdot b) = \varphi(a) \cdot \varphi(b) \quad \text{for all } a, b \in G
$$

Homomorphisms transport algebraic relationships from one group to another.

**Examples:**
- $\varphi: \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $a \mapsto a \bmod n$ (reduction modulo $n$)
- $\det: \text{GL}_n(\mathbb{R}) \to \mathbb{R}^*$, $A \mapsto \det(A)$ (determinant)

The **kernel** of a homomorphism $\varphi: G \to H$ is:

$$
\ker(\varphi) = \{a \in G \mid \varphi(a) = e_H\}
$$

The kernel is always a subgroup of $G$ – and even a special kind of subgroup: a **normal subgroup**.

## 6. Normal Subgroups and Quotient Groups

A subgroup $N \leq G$ is called a **normal subgroup** (written $N \trianglelefteq G$) if $gNg^{-1} = N$ for all $g \in G$, that is, if $N$ is invariant under conjugation.

In abelian groups, every subgroup is a normal subgroup (since $gng^{-1} = n$ for all $g, n$).

Normal subgroups are important because they allow the formation of **quotient groups** (factor groups):

$$
G/N = \{gN \mid g \in G\}
$$

The elements of $G/N$ are the **cosets** $gN = \{gn \mid n \in N\}$, and the operation is $(gN)(hN) = (gh)N$.

**Example:** $\mathbb{Z}/n\mathbb{Z}$ is precisely the quotient group of $\mathbb{Z}$ by the normal subgroup $n\mathbb{Z}$.

**The isomorphism theorem.** For every homomorphism $\varphi: G \to H$:

$$
G / \ker(\varphi) \cong \text{Im}(\varphi)
$$

That is: the quotient group modulo the kernel is isomorphic to the image. This theorem connects homomorphisms, normal subgroups, and quotient groups into a unified picture.

### Simple Groups

A group $G \neq \{e\}$ is called **simple** if it has no normal subgroups other than $\{e\}$ and $G$ itself. Simple groups are the "atoms" of group theory – every finite group can be built from simple groups (Jordan–Hölder theorem).

The classification of all finite simple groups is one of the most monumental results in mathematics: it consists of the cyclic groups $\mathbb{Z}/p\mathbb{Z}$, the alternating groups $A_n$ ($n \geq 5$), 16 families of "Lie type" groups, and 26 sporadic groups.

## 7. Why Groups Matter for FLT

For Fermat's Last Theorem, groups play a key role through **Galois theory**: the symmetries of the roots of a polynomial form a group – the **Galois group**. This group controls the algebraic structure of the associated field extension.

In Wiles' proof, groups appear in several guises:

1. **The absolute Galois group** $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ – the central symmetry object of algebraic number theory. It acts on the division points of elliptic curves.

2. **Matrix groups** $\text{GL}_2(\mathbb{F}_p)$ and $\text{GL}_2(\mathbb{Z}_p)$ – as target groups of the Galois representations that link elliptic curves with linear algebra.

3. **Hecke algebras** – symmetries in the space of modular forms that generate algebraic structures on the Fourier coefficients.

The concept of a group is the common language in which all these objects communicate. Without groups, Wiles' proof would not even be formulable.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 3
- **Joseph Gallian**: *Contemporary Abstract Algebra* – accessible textbook
- **Michael Artin**: *Algebra* – comprehensive and deep
