---
title: "The Taniyama–Shimura Conjecture"
slug: fermat-wiles/01-taniyama-shimura
series: fermat-wiles
part: 1
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - taniyama-shimura
  - modularity
  - conjecture
requires:
  - elliptische-kurven/01-elliptische-kurven
  - modulformen/01-modulformen
---
# The Taniyama–Shimura Conjecture

!!! abstract "Summary"
    The Taniyama–Shimura conjecture asserts that every elliptic curve
    over $\mathbb{Q}$ is modular – that the $L$-series of every such curve
    coincides with the $L$-series of a modular form. This bridge between
    geometry and analysis is the key to Wiles' proof of Fermat's
    Last Theorem.

## Prerequisites

- [Elliptic Curves](../../elliptische-kurven/01-elliptische-kurven/article_en.md) – basic concepts: Weierstraß equation, group structure, reduction modulo $p$
- [Modular Forms](../../modulformen/01-modulformen/article_en.md) – modular forms, newforms, $q$-expansion, Hecke operators

---

## 1. Two Separate Worlds

Twentieth-century mathematics knew two seemingly independent domains, both possessing deep structure – but at first glance having nothing to do with each other.

### The world of elliptic curves

An **elliptic curve** over $\mathbb{Q}$ is (in simplified form) the solution set of an equation of the form

$$
E: \quad y^2 = x^3 + ax + b, \qquad a, b \in \mathbb{Q}, \quad 4a^3 + 27b^2 \neq 0.
$$

It lives in **algebraic geometry** and **number theory**: one studies its rational points, its structure as an abelian group, its reduction modulo primes. For each prime $p$, one counts the points of the reduced curve over $\mathbb{F}_p$ and defines

$$
a_p(E) = p - \#E(\mathbb{F}_p),
$$

where $\#E(\mathbb{F}_p)$ is the number of points (including the point at infinity) on the reduced curve. These numbers $a_p$ encode the **local arithmetic** of the curve at each prime.

### The world of modular forms

A **modular form** of weight $k$ and level $N$ is a holomorphic function

$$
f: \mathcal{H} \to \mathbb{C}
$$

on the upper half-plane $\mathcal{H} = \{z \in \mathbb{C} : \text{Im}(z) > 0\}$ that transforms in a prescribed way under the action of the congruence subgroup $\Gamma_0(N) \subset \text{SL}_2(\mathbb{Z})$. It lives in **complex analysis** and has a Fourier expansion (also called a **$q$-expansion**):

$$
f(z) = \sum_{n=0}^{\infty} b_n q^n, \qquad q = e^{2\pi i z}.
$$

The coefficients $b_n$ encode the structure of the modular form. Particularly important are the **newforms** – normalised Hecke eigenforms that are "irreducible" in the sense that they do not arise from lower level.

### Why separate?

Elliptic curves belong to algebraic geometry and number theory. Modular forms belong to complex analysis and representation theory. Their tools, their intuitions, their languages – everything seems different. That a deep connection might exist between these worlds was scarcely imaginable until the mid-20th century.

---

## 2. The $L$-Series Bridge

The key to the connection lies in the **$L$-series** – analytic objects that equip both worlds with a common language.

### The $L$-series of an elliptic curve

For an elliptic curve $E/\mathbb{Q}$, one defines the **$L$-series** as an Euler product:

$$
L(E, s) = \prod_{p \text{ prime}} L_p(E, s)^{-1},
$$

where the local factors for primes of good reduction take the form:

$$
L_p(E, s) = 1 - a_p p^{-s} + p^{1-2s}.
$$

The $a_p$ are precisely the point-counting coefficients defined above. For the finitely many primes of bad reduction (which make up the **conductor** $N_E$ of $E$), the local factor is simpler.

### The $L$-series of a modular form

For a newform $f = \sum b_n q^n$ of weight 2 and level $N$, one defines analogously:

$$
L(f, s) = \sum_{n=1}^{\infty} b_n n^{-s} = \prod_{p \text{ prime}} \left(1 - b_p p^{-s} + p^{1-2s}\right)^{-1}.
$$

### The bridge

The central observation is: both $L$-series have exactly the same structure. If there exists a newform $f$ of weight 2 with

$$
a_p(E) = b_p(f) \quad \text{for (almost) all primes } p,
$$

then the $L$-series agree: $L(E, s) = L(f, s)$. In this case one says: **$E$ is modular**, and $f$ is the modular form associated to $E$.

---

## 3. Taniyama and Shimura – The Conjecture and Its History

### The Tokyo Symposium (1955)

In September 1955, an international symposium on algebraic number theory took place in Tokyo. There the young Japanese mathematician **Yutaka Taniyama** (1927–1958) formulated a series of problems suggesting a connection between elliptic curves and modular forms. His questions were somewhat vaguely stated, but the core was revolutionary: the $L$-series of elliptic curves should agree with those of modular forms.

Taniyama's colleague **Goro Shimura** (1930–2019) made the conjecture precise in the following years and supported it with calculations and theoretical arguments. In the Western literature, the conjecture is therefore often called the **Taniyama–Shimura conjecture** (TSC), sometimes also the Taniyama–Shimura–Weil conjecture, since André Weil made an important contribution to its precise formulation.

### The tragic history

Taniyama took his own life in 1958 at the age of only 31 – for reasons that remain not fully understood to this day. His mathematical vision, however, survived him and became one of the most influential conjectures of the 20th century.

### The conjecture, precisely stated

!!! note "Taniyama–Shimura Conjecture (Modularity Conjecture)"
    Every elliptic curve $E$ over $\mathbb{Q}$ is **modular**: there exists a
    newform $f$ of weight 2 and level $N_E$ (the conductor of $E$) with
    $$
    L(E, s) = L(f, s).
    $$
    Equivalently: $a_p(E) = b_p(f)$ for all primes $p$ of good reduction.

### Why did people believe it?

First, there was **numerical evidence**: for many explicitly computed elliptic curves, matching modular forms could be found, and the coefficients agreed – as far as one could compute.

Then there were **structural arguments**: the functional equation of the $L$-series of a modular form was known. If the $L$-series of an elliptic curve satisfies the same functional equation (as suggested by the work of Weil), then a connection seems likely.

Finally, there was the **philosophical conviction** underlying the Langlands programme: between automorphic forms (to which modular forms belong) and Galois representations (which elliptic curves yield), there should be a systematic correspondence.

---

## 4. What "Modular" Means – An Example

Consider the elliptic curve

$$
E: \quad y^2 = x^3 - x.
$$

This is a curve with **conductor** $N_E = 32$. We compute the coefficients $a_p$ by counting points modulo small primes:

| $p$ | $\#E(\mathbb{F}_p)$ | $a_p = p - \#E(\mathbb{F}_p)$ |
|-----|---------------------|-------------------------------|
| 3   | 4                   | $-1$                          |
| 5   | 4                   | $1$                           |
| 7   | 8                   | $-1$                          |
| 11  | 12                  | $-1$                          |
| 13  | 12                  | $1$                           |

Now we look for a modular form $f$ of weight 2 and level 32 with the same coefficients. Indeed, there is exactly one such newform, and its $q$-expansion begins with:

$$
f(q) = q - q^3 + q^5 - q^7 - q^{11} + q^{13} + \cdots
$$

The coefficients $b_3 = -1$, $b_5 = 1$, $b_7 = -1$, $b_{11} = -1$, $b_{13} = 1$ agree exactly with the $a_p$. The curve $y^2 = x^3 - x$ **is modular**.

This example illustrates the conjecture concretely: the arithmetic information of the curve (point counting over finite fields) is exactly mirrored by an analytic object (a modular form).

---

## 5. Why the TSC Is So Powerful

The Taniyama–Shimura conjecture is not merely an observation about individual examples – it is a **universal statement** about all elliptic curves over $\mathbb{Q}$:

### Infinitely many curves, one conjecture

There are infinitely many non-isomorphic elliptic curves over $\mathbb{Q}$, parametrised by the coefficients $a$ and $b$. For **every single one**, the TSC asserts the existence of a matching modular form. This is a breathtakingly strong statement.

### From geometry to analysis

The TSC translates a **geometric-arithmetic** problem (structure of an elliptic curve) into an **analytic** problem (existence of a modular form). Since modular forms are well-understood objects – with a rich theory of Hecke operators, $L$-series, and functional equations – the modularity of a curve immediately unlocks a wealth of analytic tools.

### Consequences of modularity

If $E$ is modular, it follows automatically that:

1. **Analytic continuation**: $L(E, s)$ admits analytic continuation to all of $\mathbb{C}$.
2. **Functional equation**: $L(E, s)$ satisfies a functional equation relating $s$ and $2-s$.
3. **BSD conjecture**: The order of the zero of $L(E, s)$ at $s = 1$ should equal the rank of $E(\mathbb{Q})$ (Birch and Swinnerton-Dyer).

Before Wiles' proof, even the analytic continuation of $L(E, s)$ was known only for individual curves – not for all.

---

## 6. The Semistable Version

### Semistable elliptic curves

An elliptic curve $E/\mathbb{Q}$ is called **semistable** if at every prime $p$ it has either good or **multiplicative** (not additive) reduction. Geometrically, this means: at primes of bad reduction, the curve has at most an ordinary double point (a "self-crossing"), but no cusp.

The class of semistable curves is large enough to contain the **Frey curve** – this is decisive for the application to Fermat's Last Theorem.

### Wiles' Theorem (1995)

!!! note "Theorem (Wiles, Taylor–Wiles, 1995)"
    Every **semistable** elliptic curve over $\mathbb{Q}$ is modular.

Andrew Wiles proved this statement in his groundbreaking paper *"Modular elliptic curves and Fermat's Last Theorem"* (Annals of Mathematics, 1995), together with the companion article by Richard Taylor and Andrew Wiles.

The proof of the **full** Taniyama–Shimura conjecture – for all elliptic curves, not just the semistable ones – was achieved only in 2001 by **Breuil, Conrad, Diamond, and Taylor**, building on Wiles' methods.

### Why does the semistable version suffice for FLT?

The Frey curve, constructed from a hypothetical FLT solution, is semistable. Therefore the semistable version of the TSC suffices to prove Fermat's Last Theorem – nothing more was needed. The details of this reduction are the subject of the [next article](../02-frey-ribet/article_en.md).

---

## 7. From TSC to FLT – Preview of Frey's Argument

The logical chain from the TSC to Fermat's Last Theorem can be summarised concisely:

**Suppose** there existed a non-trivial solution $a^p + b^p = c^p$ for a prime $p \geq 5$.

1. **Frey (1985)**: Construct the elliptic curve $E: y^2 = x(x - a^p)(x + b^p)$.
2. **Frey/Serre**: This curve is semistable but has such an extreme discriminant that it is "too exotic" to be modular.
3. **Ribet (1986)**: Proves that $E$ indeed cannot be modular (level-lowering theorem).
4. **Wiles (1995)**: Proves that every semistable curve is modular.
5. **Contradiction**: $E$ is semistable (hence modular by Wiles), but not modular (by Ribet). Therefore the solution cannot exist.

$$
\boxed{\text{FLT solution} \xrightarrow{\text{Frey}} E \xrightarrow{\text{Ribet}} \text{not modular} \xleftarrow{\text{contradiction}} \xrightarrow{\text{Wiles}} \text{modular}}
$$

This beautiful proof by contradiction – which proves a conjecture in number theory via a detour through algebraic geometry and complex analysis – is one of the great intellectual masterpieces of mathematics.

---

## Outlook

This article has presented the Taniyama–Shimura conjecture as a bridge between elliptic curves and modular forms. In the next article, we dive deeper:

| Article | Topic |
|---------|-------|
| [02 – Frey's Idea and Ribet's Theorem](../02-frey-ribet/article_en.md) | How an FLT solution leads to the "impossible" Frey curve |
| [03 – Galois Representations](../03-galois-darstellungen/article_en.md) | How Wiles translates modularity into the language of representations |

---

## Sources

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Chapter 8 – Modularity and the TSC
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1–2
- **Fred Diamond, Jerry Shurman**: *A First Course in Modular Forms*, Springer (2005) – Detailed exposition of the TSC and its proofs
- **Barry Mazur**: *Number Theory as Gadfly*, The American Mathematical Monthly 98 (1991) – Motivation of the conjecture
