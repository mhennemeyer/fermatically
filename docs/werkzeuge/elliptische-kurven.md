---
title: "Elliptic Curves – From Diophantus to Cryptography"
slug: elliptische-kurven/01-elliptische-kurven
series: elliptische-kurven
part: 1
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - elliptic-curves
  - group-law
  - l-series
requires:
  - gruppen-und-symmetrie/01-gruppen
  - ringe-und-koerper/01-ringe-koerper
---

# Elliptic Curves

!!! abstract "Summary"
    Elliptic curves are algebraic curves with a natural group structure.
    They stand at the centre of Wiles' proof – the Frey curve, the Taniyama–Shimura conjecture,
    and the Galois representations all involve elliptic curves.

## Prerequisites

- [Groups – Symmetry as the Language of Mathematics](gruppen.md)
- [Rings and Fields](ringe-koerper.md)

---

## 1. What Is an Elliptic Curve?

An **elliptic curve** over a field $K$ is a smooth, projective curve of genus $1$ with a distinguished point. In practice, one works with the **Weierstraß form**:

$$
E: \quad y^2 = x^3 + ax + b \qquad (a, b \in K)
$$

For the curve to be "smooth" (no cusps or self-intersections), the **discriminant** must be non-zero:

$$
\Delta = -16(4a^3 + 27b^2) \neq 0
$$

Geometrically, an elliptic curve over $\mathbb{R}$ is a smooth curve in the plane consisting either of one component (when $x^3 + ax + b$ has one real root) or of two components.

!!! note "Why 'elliptic'?"
    The name has nothing to do with ellipses. It originates historically from **elliptic integrals** – integrals of the form $\int \frac{dx}{\sqrt{x^3 + ax + b}}$, which arise in computing the circumference of an ellipse.

### Examples

| Curve | $a$ | $b$ | $\Delta$ |
|-------|-----|-----|----------|
| $y^2 = x^3 - x$ | $-1$ | $0$ | $64$ |
| $y^2 = x^3 + 1$ | $0$ | $1$ | $-432$ |
| $y^2 = x^3 - x + 1$ | $-1$ | $1$ | $-368$ |

### The Point at Infinity

Technically, an elliptic curve lives in **projective space** $\mathbb{P}^2$. Besides the affine points $(x, y)$ with $y^2 = x^3 + ax + b$, there is an additional **point at infinity** $\mathcal{O}$, which serves as the identity element of the group structure.

## 2. The Group Operation

The most remarkable feature of elliptic curves: their points form an **abelian group**. The operation is defined geometrically by the **secant-tangent method**:

**Addition of two points $P + Q$:**
1. Draw the line through $P$ and $Q$
2. This line intersects the curve in exactly one third point $R'$
3. Reflect $R'$ across the $x$-axis: the result is $P + Q$

**Doubling $2P = P + P$:**
1. Draw the tangent to the curve at $P$
2. This tangent intersects the curve in a second point $R'$
3. Reflect: the result is $2P$

**Identity element:** The point $\mathcal{O}$ at infinity. We have $P + \mathcal{O} = P$ for all $P$.

**Inverse:** The inverse of $P = (x, y)$ is $-P = (x, -y)$ (reflection across the $x$-axis).

!!! tip "Algebraic Formulas"
    For $P = (x_1, y_1)$ and $Q = (x_2, y_2)$ with $P \neq \pm Q$:

    $$
    \lambda = \frac{y_2 - y_1}{x_2 - x_1}, \quad x_3 = \lambda^2 - x_1 - x_2, \quad y_3 = \lambda(x_1 - x_3) - y_1
    $$

    For $P = Q$ (doubling):

    $$
    \lambda = \frac{3x_1^2 + a}{2y_1}
    $$

    These formulas work over **any** field – including $\mathbb{F}_p$ or $\mathbb{Q}_p$.

## 3. Rational Points and Mordell's Theorem

The set of rational points $E(\mathbb{Q}) = \{(x, y) \in \mathbb{Q}^2 \mid y^2 = x^3 + ax + b\} \cup \{\mathcal{O}\}$ is a subgroup of $E$.

**Theorem (Mordell, 1922).** $E(\mathbb{Q})$ is a finitely generated abelian group.

By the structure theorem for finitely generated abelian groups:

$$
E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus E(\mathbb{Q})_{\text{tors}}
$$

where:
- $r = \text{rank}(E)$ is the **rank** of the curve (the number of independent points of infinite order)
- $E(\mathbb{Q})_{\text{tors}}$ is the finite **torsion subgroup** (points of finite order)

**Theorem (Mazur, 1977).** The torsion subgroup $E(\mathbb{Q})_{\text{tors}}$ is isomorphic to one of the following groups:

$$
\mathbb{Z}/n\mathbb{Z} \text{ for } n \in \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12\}
$$
$$
\text{or } \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2n\mathbb{Z} \text{ for } n \in \{1, 2, 3, 4\}
$$

The rank $r$, by contrast, is hard to compute, and it remains unknown to this day whether elliptic curves of arbitrarily large rank exist.

## 4. Reduction Modulo $p$

An elliptic curve $E: y^2 = x^3 + ax + b$ with $a, b \in \mathbb{Z}$ can be reduced modulo a prime $p$:

$$
\tilde{E}: \quad y^2 \equiv x^3 + ax + b \pmod{p}
$$

If $p \nmid \Delta$ (the discriminant), then $\tilde{E}$ is a smooth curve over $\mathbb{F}_p$ – one says $E$ has **good reduction** at $p$. Otherwise, $E$ has **bad reduction**.

### The $a_p$-Coefficients

For primes $p$ of good reduction, we define:

$$
a_p = p + 1 - \#\tilde{E}(\mathbb{F}_p)
$$

where $\#\tilde{E}(\mathbb{F}_p)$ is the number of points of $\tilde{E}$ over $\mathbb{F}_p$ (including $\mathcal{O}$).

**Theorem (Hasse, 1933).** We have $|a_p| \leq 2\sqrt{p}$.

The $a_p$-coefficients encode what the curve looks like "prime by prime". They are the building blocks of the $L$-series.

**Example:** For $E: y^2 = x^3 - x$ and $p = 5$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|-----|
| $x^3 - x \bmod 5$ | $0$ | $0$ | $1$ | $4$ | $0$ |
| $y^2 \equiv \ldots$? | $y = 0$ | $y = 0$ | $y = \pm 1$ | $y = \pm 2$ | $y = 0$ |

This gives $8$ affine points plus $\mathcal{O}$, so $\#\tilde{E}(\mathbb{F}_5) = 9$ and $a_5 = 5 + 1 - 9 = -3$.

## 5. The $L$-Series of an Elliptic Curve

The $a_p$-coefficients are assembled into an analytic function – the **$L$-series** (Hasse–Weil):

$$
L(E, s) = \prod_{p \text{ good}} \frac{1}{1 - a_p p^{-s} + p^{1-2s}} \cdot \prod_{p \text{ bad}} (\text{local factor})
$$

This $L$-series converges for $\text{Re}(s) > 3/2$ and encodes the entire arithmetic information of the curve.

**The BSD conjecture** (Birch and Swinnerton-Dyer, one of the Millennium Problems): The rank of $E(\mathbb{Q})$ equals the order of the zero of $L(E, s)$ at $s = 1$.

### The Connection to Modular Forms

The central question: is the $L$-series $L(E, s)$ *equal* to the $L$-series of a **modular form** $f$?

$$
L(E, s) \stackrel{?}{=} L(f, s) = \sum_{n=1}^{\infty} a_n n^{-s}
$$

If so, $E$ is called **modular**. The **Taniyama–Shimura conjecture** (now a theorem) states: **every** elliptic curve over $\mathbb{Q}$ is modular. This theorem – more precisely: the semistable case, proved by Wiles – implies Fermat's Last Theorem.

## 6. Torsion Points and Galois Representations

For a prime $\ell$, the **$\ell$-division points** are the points $P \in E(\overline{\mathbb{Q}})$ with $\ell P = \mathcal{O}$:

$$
E[\ell] = \{P \in E(\overline{\mathbb{Q}}) \mid \ell P = \mathcal{O}\}
$$

We have $E[\ell] \cong (\mathbb{Z}/\ell\mathbb{Z})^2$ – a two-dimensional group over $\mathbb{F}_\ell$.

The **absolute Galois group** $G_{\mathbb{Q}}$ acts on $E[\ell]$ by permuting the coordinates. This defines a **Galois representation**:

$$
\bar{\rho}_{E,\ell}: G_{\mathbb{Q}} \to \text{Aut}(E[\ell]) \cong \text{GL}_2(\mathbb{F}_\ell)
$$

For the **$\ell$-adic Tate modules** (the projective limit over all $\ell^n$-division points), one obtains an $\ell$-adic representation:

$$
\rho_{E,\ell}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_\ell) \hookrightarrow \text{GL}_2(\mathbb{Q}_\ell)
$$

These representations are the link between elliptic curves and Galois theory – and the central object of Wiles' proof.

## 7. Elliptic Curves and Cryptography

A brief excursion into applications: elliptic curves over finite fields $\mathbb{F}_p$ form the foundation of modern **cryptographic methods** (ECC – Elliptic Curve Cryptography).

The security rests on the **discrete logarithm problem**: given $P$ and $Q = nP$ on $E(\mathbb{F}_p)$, it is computationally extremely difficult to find $n$ – even though computing $nP$ from $n$ and $P$ is efficient (via repeated doubling and addition).

ECC offers the same security level as RSA, but with significantly shorter keys:

| Security level | RSA key | ECC key |
|----------------|---------|---------|
| 128 bit | 3072 bit | 256 bit |
| 256 bit | 15360 bit | 512 bit |

## 8. Outlook: Modularity

This article has presented elliptic curves as self-contained algebraic objects. Their true power unfolds in the interplay with **modular forms** – the subject of the next tool article.

The chain of connections:

$$
\text{Elliptic curve } E \xrightarrow{a_p} \text{$L$-series } L(E,s) \xleftarrow{?} L(f,s) \xleftarrow{a_n} \text{Modular form } f
$$

The Taniyama–Shimura conjecture asserts that the arrow in the middle always exists – that every elliptic curve has its "twin soul" in the realm of modular forms. Wiles' proof of this conjecture (for semistable curves) is the key to Fermat's Last Theorem.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 6
- **Joseph Silverman**: *The Arithmetic of Elliptic Curves* – the standard reference
- **Joseph Silverman, John Tate**: *Rational Points on Elliptic Curves* – accessible introduction
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, §1
