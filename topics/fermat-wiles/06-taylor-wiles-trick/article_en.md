---
title: "The Taylor–Wiles Trick"
slug: fermat-wiles/06-taylor-wiles-trick
series: fermat-wiles
part: 6
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - taylor-wiles
  - patching
  - modularity-proof
requires:
  - fermat-wiles/05-r-gleich-t
---
# The Taylor–Wiles Trick

!!! abstract "Summary"
    The patching argument of Taylor and Wiles closed the gap in the
    original proof of 1993. By adding carefully chosen auxiliary
    primes, the deformation rings become "simpler", and in the
    inverse limit $R = T$ becomes provable. This argument revolutionised
    the methodology of algebraic number theory.

## Prerequisites

- [R = T – The Heart of the Proof](../05-r-gleich-t/article_en.md) – numerical criterion, Selmer groups, congruence ideals

---

## 1. The Gap (1993)

### Wiles' announcement

On 23 June 1993, Andrew Wiles ended his third lecture at the Newton Institute in Cambridge with the words: *"I think I'll stop here."* The audience burst into applause – Wiles had just announced the modularity of semistable elliptic curves, from which Fermat's Last Theorem follows.

The news went around the world. Newspapers headlined: "350-year-old puzzle solved." But the proof still had to survive peer review.

### The problem

During the review in autumn 1993, **Nick Katz** (Princeton) found an error in Chapter 3 of the manuscript. The gap concerned the decisive step: the upper bound for the Selmer group.

Wiles had tried to construct an **Euler system** – a family of coherent cohomology classes that, by Kolyvagin's method, yield upper bounds for Selmer groups. But the construction was incomplete at an essential point: the required compatibility property could not be verified.

### The dark months

From October 1993 to September 1994, Wiles tried desperately to close the gap – at first alone, then with various approaches. He was on the verge of giving up:

> *"I was sitting at my desk examining the Kolyvagin–Flach method. It wasn't working, it wasn't working, and I sat there thinking. [...] Suddenly, totally unexpectedly, I had this incredible revelation."*
> — Andrew Wiles

---

## 2. Taylor Enters the Stage

### The collaboration

In autumn 1994, Wiles asked his former doctoral student **Richard Taylor** for help. Taylor, then a professor in Cambridge, was one of the few mathematicians who understood the proof in detail.

Together they recognised: the Euler system approach was a dead end. Instead, they needed an entirely new route to the upper bound on the Selmer group.

### The decisive insight

The idea came from an unexpected direction: instead of estimating the Selmer group directly, one should embed the **entire problem** – the ring $R$, the Hecke algebra $T$, and the surjection $R \twoheadrightarrow T$ – into a **family** and prove the result "in the limit".

---

## 3. The Idea of Patching

### Auxiliary primes

The basic idea is strikingly simple: one **enlarges** the problem by adding extra primes.

Let $Q = \{q_1, \ldots, q_n\}$ be a finite set of primes satisfying certain properties:

1. $q_i \equiv 1 \pmod{p}$ (so that non-trivial characters modulo $q_i$ exist)
2. $q_i \nmid N$ (the primes are "new" – they do not divide the level)
3. $\bar{\rho}(\text{Frob}_{q_i})$ has distinct eigenvalues in $\mathbb{F}_p$

### Why such primes exist

The Čebotarëv density theorem guarantees: for every given conjugacy class in $\text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$, there are infinitely many primes $q$ with $\text{Frob}_q$ in that class. The condition $q \equiv 1 \pmod{p}$ selects a subset of positive density. So there are **arbitrarily many** suitable auxiliary primes.

### What the auxiliary primes achieve

For each set $Q$ one considers:

- The **augmented deformation ring** $R_Q$: deformations of $\bar{\rho}$ with the usual local conditions, but **additionally** with a prescribed structure at the primes $q \in Q$.
- The **augmented Hecke algebra** $T_Q$: the Hecke algebra of level $N \cdot \prod_{q \in Q} q$.

The surjection $R_Q \twoheadrightarrow T_Q$ is preserved, but the rings are "larger" and carry additional structure.

---

## 4. Augmented Deformation Rings

### The $\Delta_Q$-action

Each prime $q \in Q$ with $q \equiv 1 \pmod{p}$ yields a group

$$
\Delta_q = (\mathbb{Z}/q\mathbb{Z})^\times / (\mathbb{Z}/q\mathbb{Z})^{\times p} \cong \mathbb{Z}/p\mathbb{Z}.
$$

The product

$$
\Delta_Q = \prod_{q \in Q} \Delta_q \cong (\mathbb{Z}/p\mathbb{Z})^n
$$

acts on $R_Q$ and $T_Q$ via the Galois action at the auxiliary primes. The **augmentation ideal** $\mathfrak{a}_Q = \ker(\mathbb{F}_p[\Delta_Q] \to \mathbb{F}_p)$ has the property:

$$
R_Q / \mathfrak{a}_Q \cdot R_Q \cong R, \qquad T_Q / \mathfrak{a}_Q \cdot T_Q \cong T.
$$

The original rings $R$ and $T$ are thus quotients of the augmented rings. **The problem is recovered by "forgetting" the auxiliary primes.**

### The crucial property

Taylor and Wiles show: for suitably chosen sets $Q$, $R_Q$ is a **power series ring over $R$**:

$$
R_Q \cong R[[s_1, \ldots, s_n]],
$$

where $n = |Q|$. The augmented ring has exactly $n$ additional free variables – one for each auxiliary prime. This follows from a careful computation of the Selmer group: the $n$ auxiliary primes generate exactly $n$ new deformation directions.

---

## 5. The Limit Process

### Growing sets of primes

One now constructs a sequence of prime sets:

$$
Q_1 \subset Q_2 \subset Q_3 \subset \cdots
$$

with $|Q_m| = m$, each satisfying the conditions above.

### The inverse limit

One forms the inverse limits:

$$
R_\infty = \varprojlim_m R_{Q_m}, \qquad T_\infty = \varprojlim_m T_{Q_m}.
$$

The surjections $R_{Q_m} \twoheadrightarrow T_{Q_m}$ yield a surjection in the limit:

$$
R_\infty \twoheadrightarrow T_\infty.
$$

### Why the limit helps

In the limit, the rings become "simpler" in the following sense:

1. $R_\infty$ is a **formal power series ring** over $\mathbb{Z}_p$: $R_\infty \cong \mathbb{Z}_p[[x_1, x_2, \ldots]]$ (infinitely many variables, but the structure is explicit).
2. $T_\infty$ is a **free $R_\infty$-module** of finite rank.

In this situation, the numerical criterion is **automatically satisfied**: a power series ring surjecting onto a free module is necessarily an isomorphism (up to the correct dimension conditions).

---

## 6. Back to the Minimal Case

### The descent

From $R_\infty = T_\infty$ in the limit, one must descend to the finite case. This works as follows:

1. $R_\infty = T_\infty$ implies $R_{Q_m} = T_{Q_m}$ for each $m$ (by specialisation).
2. $R_{Q_m} = T_{Q_m}$ implies $R = T$ by taking the quotient modulo $\mathfrak{a}_{Q_m}$.

The inverse limit is thus not an end in itself, but a **detour** that makes the proof possible: in the limit, the structure is simple enough to verify $R = T$, and the descent transfers the result to the original case.

### The structure of the argument

$$
\boxed{R = T} \xleftarrow{\text{quotient}} \boxed{R_Q = T_Q} \xleftarrow{\text{limit}} \boxed{R_\infty = T_\infty \text{ (simple!)}}
$$

### Why the minimal case is decisive

The patching argument works most cleanly in the **minimal case** – when the local deformation conditions are as restrictive as possible. In the minimal case, $R_Q$ has exactly the right structure (power series ring over $R$), and the dimension calculations work out.

The general case is then reduced to the minimal one – a technically demanding but conceptually separate task.

---

## 7. The Significance of the Trick

### Revolutionary methodology

The Taylor–Wiles patching was not only the key to Fermat's Last Theorem – it established a **new method** in algebraic number theory that has since been applied in countless contexts:

- **BCDT (2001)**: Breuil, Conrad, Diamond, and Taylor generalised the proof to all elliptic curves over $\mathbb{Q}$ – using the same patching method.
- **Serre's conjecture (2009)**: Khare and Wintenberger used patching arguments for the proof.
- **Langlands programme**: Taylor–Wiles patching is a standard tool for modularity proofs in higher dimensions.
- **Calegari–Geraghty**: Generalisation to non-regular weights and other situations.

### What makes the trick so elegant

1. **Bypassing Euler systems**: Instead of constructing a complicated cohomological object, one uses the freedom to add auxiliary primes – a far more flexible method.
2. **Algebraic simplicity in the limit**: What is difficult in the finite case becomes trivial in the limit – a typical strategy of commutative algebra.
3. **Universal applicability**: The method depends not on the specific situation but only on general structural properties of deformation rings and Hecke algebras.

### The personal dimension

The story of the Taylor–Wiles trick is also a deeply human one. Wiles had worked in secret for seven years, announced his proof, found a gap, and stood on the brink of failure. The collaboration with Taylor and the discovery of the patching argument in September 1994 saved not only the proof but also Wiles' life's work.

On 25 October 1995 – after careful review by six referees – the two papers appeared in the *Annals of Mathematics*:

1. **Wiles**: *Modular elliptic curves and Fermat's Last Theorem* (109 pages)
2. **Taylor–Wiles**: *Ring-theoretic properties of certain Hecke algebras* (20 pages)

Together they form one of the most significant mathematical proofs of the 20th century.

---

## Outlook

With the Taylor–Wiles trick, the proof of $R = T$ in the minimal case is secured. But one decisive step is still missing: how do we know that $\bar{\rho}_{E,p}$ is modular in the first place? That is the starting point, and it requires the elegant 3-5 switch:

| Article | Topic |
|---------|-------|
| [07 – The 3-5 Switch](../07-3-5-switch/article_en.md) | Langlands–Tunnell and the completion of the proof |
| [08 – What Came After](../08-was-danach-kam/article_en.md) | From Wiles to BCDT and the Langlands programme |

---

## Sources

- **Richard Taylor, Andrew Wiles**: *Ring-theoretic properties of certain Hecke algebras*, Annals of Mathematics 141 (1995), 553–572
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §3.3
- **Fred Diamond**: *The Taylor-Wiles construction and multiplicity one*, Inventiones Mathematicae 128 (1997) – Simplification and generalisation
- **Chandrashekhar Khare**: *Serre's modularity conjecture*, Inventiones Mathematicae 178 (2009) – Application of the Taylor–Wiles method
- **Simon Singh**: *Fermat's Last Theorem*, Fourth Estate (1997) – The human story behind the proof
