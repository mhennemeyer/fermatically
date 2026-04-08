---
title: "Frey's Idea and Ribet's Theorem"
slug: fermat-wiles/02-frey-ribet
series: fermat-wiles
part: 2
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - frey-curve
  - ribet
  - level-lowering
requires:
  - fermat-wiles/01-taniyama-shimura
  - elliptische-kurven/01-elliptische-kurven
---
# Frey's Idea and Ribet's Theorem

!!! abstract "Summary"
    In 1985, Gerhard Frey recognised that a hypothetical solution to Fermat's
    Last Theorem leads to an elliptic curve with such extreme properties
    that it cannot be modular. In 1986, Kenneth Ribet proved that this
    intuition is correct. With that, FLT was reduced to the Taniyama–Shimura
    conjecture.

## Prerequisites

- [The Taniyama–Shimura Conjecture](../01-taniyama-shimura/article_en.md) – modularity, $L$-series, semistable curves
- [Elliptic Curves](../../elliptische-kurven/01-elliptische-kurven/article_en.md) – Weierstraß form, discriminant, conductor

---

## 1. Frey's Flash of Insight (1985)

### The decisive question

After centuries of direct attacks on Fermat's Last Theorem – proofs for $n = 4$ (Fermat), $n = 3$ (Euler), $n = 5$ (Dirichlet/Legendre), and so on – in 1985 a completely new idea came from an unexpected direction.

**Gerhard Frey**, a German mathematician at Saarland University, posed the following question: what if one did not have to directly refute a hypothetical FLT solution, but instead could show that it leads to a **contradiction** with another known (or conjectured) fact?

### The approach

Frey assumed there existed a non-trivial solution of the Fermat equation for a prime $p \geq 5$:

$$
a^p + b^p = c^p, \qquad a, b, c \in \mathbb{Z}, \quad abc \neq 0.
$$

Without loss of generality, one can assume:
- $\gcd(a, b, c) = 1$ (the solution is primitive)
- $a \equiv -1 \pmod{4}$ and $2 \mid b$ (by suitable choice of signs and permutations)

From these three numbers, Frey constructed an elliptic curve – and this curve would turn out to be the key to the entire proof.

---

## 2. The Frey Curve

### Construction

From the hypothetical solution $a^p + b^p = c^p$, Frey defines the elliptic curve:

$$
E_{a,b,c}: \quad y^2 = x(x - a^p)(x + b^p).
$$

This curve is in **Weierstraß form** (after a simple change of variables) and has three obvious 2-torsion points: $(0, 0)$, $(a^p, 0)$, and $(-b^p, 0)$.

### The discriminant

The **minimal discriminant** of the Frey curve is (up to powers of 2):

$$
\Delta = \frac{(abc)^{2p}}{2^8}.
$$

This is an extraordinarily large discriminant – much larger than for "normal" elliptic curves. The exponent $2p$ (with $p \geq 5$) ensures that the prime factorisation of $\Delta$ is extremely concentrated.

### The conductor

The **conductor** $N_E$ of the Frey curve is:

$$
N_E = \prod_{q \mid abc} q,
$$

where the product runs over all prime divisors of $abc$ (and the factor at $q = 2$ is somewhat more subtle). Crucially: $N_E$ is **squarefree** (or nearly so) – the Frey curve is **semistable**.

### Why semistable?

An elliptic curve is semistable if at every prime it has at most multiplicative reduction. For the Frey curve: at every odd prime $q$ dividing $abc$, the curve has multiplicative reduction (a node). At primes not dividing $abc$, it has good reduction. The semistability follows from the special form of the equation.

---

## 3. Serre's Epsilon Conjecture

### The modularity problem

**Suppose** the Frey curve $E$ were modular – that is, there existed a newform $f$ of weight 2 and level $N_E$ with $L(E, s) = L(f, s)$. What could one say about this newform?

### The Galois representation

Every elliptic curve yields for every prime $p$ a **residual Galois representation**:

$$
\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p),
$$

describing how the absolute Galois group $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ acts on the $p$-torsion points $E[p]$.

For the Frey curve, $\bar{\rho}_{E,p}$ has special properties:
1. It is **irreducible** (for $p \geq 5$, which follows from the special structure of the solution).
2. It is **little ramified**: at almost all places, the representation is unramified.
3. It comes (if $E$ is modular) from a newform of level $N_E$.

### Serre's conjecture

**Jean-Pierre Serre** formulated in the 1980s a general conjecture about what level a modular representation must have. Applied to the Frey curve, his conjecture (more precisely: a consequence he called the "$\varepsilon$-conjecture") states:

!!! note "Serre's $\varepsilon$-conjecture (for the Frey curve)"
    If the Frey curve is modular, then the representation $\bar{\rho}_{E,p}$
    comes from a newform of **level 2**.

This is dramatic: there are **no** newforms of weight 2 and level 2 (the space $S_2(\Gamma_0(2))$ is zero-dimensional). So if Serre's conjecture holds, then **the Frey curve cannot be modular**.

---

## 4. Ribet's Proof (1986)

### Level-lowering

**Kenneth Ribet**, professor at the University of California at Berkeley, proved in 1986 exactly the statement that Serre had formulated as the $\varepsilon$-conjecture. His tool was the so-called **level-lowering**:

!!! note "Theorem (Ribet, 1986)"
    Let $E$ be a semistable elliptic curve over $\mathbb{Q}$ and $p$ a prime
    with $p \geq 3$. If $\bar{\rho}_{E,p}$ is modular (i.e., comes from a newform
    of level $N$) and a prime $q \| N$ does not divide the representation
    (i.e., $q \nmid N(\bar{\rho})$, the Artin conductor of the representation),
    then $\bar{\rho}_{E,p}$ already comes from a newform of **level $N/q$**.

### Application to the Frey curve

For the Frey curve $E$ with conductor $N_E = \prod_{q \mid abc} q$, level-lowering can be applied iteratively: at every odd prime $q \mid abc$, we have $q^p \mid \Delta$ (because of the exponent $2p$ in the discriminant), which implies $q \nmid N(\bar{\rho}_{E,p})$. Ribet's theorem allows removing the factor $q$ from the level.

After removing all such factors, only level **2** remains. Since $S_2(\Gamma_0(2)) = 0$, there is no matching newform – the representation cannot be modular.

### The significance

Ribet's theorem turned Serre's conjecture into a **theorem**:

$$
\text{Frey curve modular} \implies \text{newform of level 2 exists} \implies \text{contradiction!}
$$

Thus it was clear: **the Frey curve is not modular** – provided the Taniyama–Shimura conjecture is false. Or conversely:

$$
\text{Taniyama–Shimura (semistable)} \implies \text{no Frey curve} \implies \text{FLT.}
$$

---

## 5. The Logical Chain

Let us summarise the entire chain of argument. It consists of a sequence of implications:

### Step 1: Hypothetical FLT solution → Frey curve

From $a^p + b^p = c^p$ (with $p \geq 5$, primitive), Frey constructs:

$$
E: \quad y^2 = x(x - a^p)(x + b^p).
$$

This curve is **semistable** with an extremely large discriminant.

### Step 2: Frey curve + TSC → modular representation

If the TSC (semistable version) holds, then $E$ is modular. Then $\bar{\rho}_{E,p}$ comes from a newform of level $N_E$.

### Step 3: Level-lowering → level 2

Ribet's theorem allows the stepwise reduction of the level:

$$
N_E = \prod_{q \mid abc} q \quad \xrightarrow{\text{Ribet}} \quad 2.
$$

### Step 4: Contradiction

There is no newform of weight 2 and level 2. So the Frey curve is not modular. But by the TSC it would have to be modular. **Contradiction.**

### The diagram

$$
\boxed{a^p + b^p = c^p} \xrightarrow{\text{Frey}} \boxed{E \text{ semistable}} \xrightarrow{\text{TSC}} \boxed{E \text{ modular}} \xrightarrow{\text{Ribet}} \boxed{\text{level 2}} \to \boxed{\bot}
$$

The contradiction shows: the assumption of an FLT solution was false. **Fermat's Last Theorem is true.**

---

## 6. What Remains to Be Done?

After Ribet's breakthrough of 1986, the situation was crystal clear:

> **To prove Fermat's Last Theorem, it suffices to prove the Taniyama–Shimura conjecture for semistable elliptic curves.**

This was simultaneously good and bad news:

**The good news**: FLT was reduced to a concrete, clearly formulated problem – the modularity of semistable curves. No more guessing, no more searching for the "right" approach. The path was laid out.

**The bad news**: The TSC was considered hopelessly difficult. Most experts thought a proof in the foreseeable future was impossible. Even André Weil, who had contributed to the formulation of the conjecture, expressed scepticism.

Yet one mathematician took up the challenge: **Andrew Wiles**, who had been fascinated by Fermat's Last Theorem since childhood. From 1986 to 1993, he worked in secret on a proof – with tools that are developed in the following articles: Galois representations, deformation theory, and the revolutionary Taylor–Wiles trick.

---

## Outlook

The reduction of FLT to the TSC was a triumph of structural mathematics. But the actual proof – the modularity of semistable curves – requires an entirely new language:

| Article | Topic |
|---------|-------|
| [03 – Galois Representations](../03-galois-darstellungen/article_en.md) | How elliptic curves yield matrix representations |
| [04 – Deformation Theory](../04-deformationstheorie/article_en.md) | How to "bend" representations |
| [05 – R = T](../05-r-gleich-t/article_en.md) | The heart of Wiles' proof |

---

## Sources

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Chapter 9 – Frey curve and Ribet's theorem
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), Introduction
- **Kenneth Ribet**: *On modular representations of $\text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms*, Inventiones Mathematicae 100 (1990)
- **Gerhard Frey**: *Links between stable elliptic curves and certain Diophantine equations*, Annales Universitatis Saraviensis 1 (1986)
- **Jean-Pierre Serre**: *Sur les représentations modulaires de degré 2 de $\text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*, Duke Mathematical Journal 54 (1987)
