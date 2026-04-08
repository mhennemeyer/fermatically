---
title: "The Proof for n=3"
slug: elementare-zahlentheorie/04-beweis-n3
series: elementare-zahlentheorie
part: 4
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - fermat
  - euler
  - gauss
  - algebraic-numbers
requires: []
---

# The Proof for $n = 3$

!!! abstract "Summary"
    Euler's proof of Fermat's Last Theorem for the case $n = 3$ – and why it forces us
    to leave the ordinary integers behind. The entry into algebraic number theory.

## Prerequisites

- [What Is Fermat's Last Theorem?](../01-was-ist-flt/article_en.md)
- [The Proof for $n = 4$](../02-beweis-n4/article_en.md)
- [Primes and Why They Suffice](../03-primzahlen-reduktion/article_en.md)

---

## 1. Why $n = 3$ Is Harder Than $n = 4$

In the proof for $n = 4$, we could treat the equation $x^4 + y^4 = z^2$ entirely within $\mathbb{Z}$. The key was the parametrisation of Pythagorean triples – a formula describing *all* solutions of $x^2 + y^2 = z^2$.

For $n = 3$, no analogue exists. The equation $x^3 + y^3 = z^3$ cannot be factorised in $\mathbb{Z}$ in a way that makes a descent possible. The reason: the factorisation

$$
x^3 + y^3 = (x + y)(x^2 - xy + y^2)
$$

yields two factors whose coprimality is hard to control. One would need information about $\gcd(x + y, \, x^2 - xy + y^2)$, which is not easy to obtain in $\mathbb{Z}$.

Euler's brilliant idea: instead of computing in $\mathbb{Z}$, we extend the number domain.

## 2. The Eisenstein Integers

Let $\omega = e^{2\pi i/3} = \frac{-1 + \sqrt{-3}}{2}$ be a primitive cube root of unity. The **Eisenstein integers** are the ring:

$$
\mathbb{Z}[\omega] = \{ a + b\omega \mid a, b \in \mathbb{Z} \}
$$

Geometrically, the Eisenstein integers form a regular triangular lattice in the complex plane. Every element has the form $a + b\omega$ with integer coordinates.

### Basic Properties

**Norm.** For $\alpha = a + b\omega$ we define the norm as:

$$
N(\alpha) = \alpha \cdot \bar{\alpha} = a^2 - ab + b^2
$$

where $\bar{\alpha} = a + b\bar{\omega} = a + b\omega^2$ is the conjugate (since $\omega^2 = \bar{\omega}$). The norm is always a non-negative integer and is multiplicative: $N(\alpha\beta) = N(\alpha) \cdot N(\beta)$.

**Units.** The units (invertible elements) of $\mathbb{Z}[\omega]$ are precisely the elements with norm $1$:

$$
\mathbb{Z}[\omega]^\times = \{ \pm 1, \pm \omega, \pm \omega^2 \}
$$

That is six units – more than the two units $\pm 1$ in $\mathbb{Z}$.

**Prime elements.** An Eisenstein element $\pi$ is called *prime* if it is not a unit and $\pi \mid \alpha\beta$ implies $\pi \mid \alpha$ or $\pi \mid \beta$. The prime structure of $\mathbb{Z}[\omega]$ differs from that of $\mathbb{Z}$:

- The prime $3$ decomposes specially: $3 = -\omega^2 (1 - \omega)^2$, so $\lambda := 1 - \omega$ is a prime element with $N(\lambda) = 3$.
- Primes $p \equiv 2 \pmod{3}$ remain prime in $\mathbb{Z}[\omega]$.
- Primes $p \equiv 1 \pmod{3}$ split: $p = \pi \bar{\pi}$ for some prime element $\pi$.

### The Decisive Advantage

In $\mathbb{Z}[\omega]$ we can factorise $x^3 + y^3$ *completely*:

$$
x^3 + y^3 = (x + y)(x + \omega y)(x + \omega^2 y)
$$

Three linear factors instead of two! This finer factorisation makes the descent possible.

## 3. Unique Factorisation

The proof works only if $\mathbb{Z}[\omega]$ is a **principal ideal domain** (PID) – that is, if every element has an essentially unique decomposition into prime elements.

**Theorem.** $\mathbb{Z}[\omega]$ is a Euclidean domain (with the norm function as Euclidean function) and therefore in particular a PID.

**Proof sketch.** For $\alpha, \beta \in \mathbb{Z}[\omega]$ with $\beta \neq 0$, consider $\alpha/\beta \in \mathbb{Q}(\omega)$. This element can be approximated by a lattice element $\gamma \in \mathbb{Z}[\omega]$ with $N(\alpha/\beta - \gamma) < 1$ (because the triangular lattice is dense enough). Then $\alpha = \beta\gamma + \rho$ with $N(\rho) < N(\beta)$ – exactly the division with remainder that is needed. $\square$

!!! warning "Not self-evident!"
    For $p = 3$, $\mathbb{Z}[\omega]$ is a PID – but $\mathbb{Z}[\zeta_p]$ is **not** a PID for general $p$. Already for $p = 23$, unique factorisation fails. This was the point where Lamé failed and Kummer invented ideal theory.

## 4. The Proof: Step by Step

We prove: $x^3 + y^3 = z^3$ has no solution in positive integers.

Equivalently (and more technically convenient), we prove the more general statement in $\mathbb{Z}[\omega]$:

$$
\alpha^3 + \beta^3 + \gamma^3 = 0 \quad \text{has no solution with } \alpha, \beta, \gamma \in \mathbb{Z}[\omega] \setminus \{0\} \text{ and } \lambda \nmid \alpha\beta\gamma
$$

where $\lambda = 1 - \omega$ is the prime element above $3$. (The symmetric form $\alpha^3 + \beta^3 + \gamma^3 = 0$ is equivalent to $x^3 + y^3 = z^3$ with the sign of $z$ reversed.)

In fact, we prove an even stronger version by infinite descent. The proof proceeds in several stages.

### Preparation: Cubic residues modulo $\lambda$

Since $N(\lambda) = 3$, we have $\mathbb{Z}[\omega]/(\lambda) \cong \mathbb{Z}/3\mathbb{Z} = \{0, 1, 2\}$. Every element of $\mathbb{Z}[\omega]$ not divisible by $\lambda$ is congruent to $\pm 1 \pmod{\lambda}$. It follows that every cube of such an element is likewise congruent to $\pm 1 \pmod{\lambda}$.

More precisely, for every $\alpha$ with $\lambda \nmid \alpha$:

$$
\alpha^3 \equiv \pm 1 \pmod{\lambda^4}
$$

This is the analogue of the statement "every square is $\equiv 0$ or $1 \pmod{4}$" in $\mathbb{Z}$ – but one level more intricate.

### The Descent

**Assumption.** Let $(\alpha, \beta, \gamma)$ be a solution of $\alpha^3 + \beta^3 + \gamma^3 = 0$ with $\lambda \nmid \alpha\beta\gamma$ and with *minimal* $\lambda$-valuation in one of the terms. More precisely: we assume that $\lambda \mid \gamma$ (after reordering), and write $\gamma = \lambda^n \delta$ with $\lambda \nmid \delta$ and minimal $n \geq 1$.

We show that from this solution a new solution with smaller $n$ can be constructed – contradiction.

**Step 1: Factorisation.** In $\mathbb{Z}[\omega]$:

$$
\alpha^3 + \beta^3 = -\gamma^3 = -\lambda^{3n} \delta^3
$$

$$
(\alpha + \beta)(\alpha + \omega\beta)(\alpha + \omega^2\beta) = -\lambda^{3n} \delta^3
$$

**Step 2: Coprimality of the factors.** One shows that the three factors $\alpha + \beta$, $\alpha + \omega\beta$, $\alpha + \omega^2\beta$ can be separated pairwise by $\lambda$: their pairwise differences are $(1 - \omega)\beta = \lambda\beta$ and $(1 - \omega^2)\beta$, so $\lambda$ is the only common factor. After careful analysis of the $\lambda$-valuation, one can show that exactly one of the three factors is divisible by $\lambda^{3n-2}$ and the other two are not divisible by $\lambda$.

**Step 3: Force cubic structure.** Since $\mathbb{Z}[\omega]$ is a PID and the three factors (up to $\lambda$-parts) are coprime, each factor (up to units and powers of $\lambda$) must be a cube. In particular, there exist $\alpha_1, \beta_1, \gamma_1 \in \mathbb{Z}[\omega]$ with:

$$
\alpha + \beta = \varepsilon_1 \lambda^{3n-2} \gamma_1^3, \quad \alpha + \omega\beta = \varepsilon_2 \alpha_1^3, \quad \alpha + \omega^2\beta = \varepsilon_3 \beta_1^3
$$

where $\varepsilon_1, \varepsilon_2, \varepsilon_3$ are units.

**Step 4: Derive a new equation.** From the three equations, one can (by skilful combination) derive an equation of the form

$$
\alpha_1^3 + \beta_1^3 + \varepsilon \lambda^{n'} \gamma_1^3 = 0
$$

where $n' < n$. The unit $\varepsilon$ can be absorbed by choosing suitable associates.

**Step 5: Contradiction.** We have found a solution with $\lambda$-valuation $n' < n$. Since $n$ was minimal, this is a contradiction. $\blacksquare$

## 5. The Gap in Euler's Original

Euler's proof, as it appeared in his 1770 *Algebra*, contained a subtle gap. In the decisive step of the descent, he used the fact that certain elements in $\mathbb{Z}[\omega]$ must be cubes – and thereby implicitly assumed **unique prime factorisation** in $\mathbb{Z}[\omega]$.

This assumption happens to be correct: $\mathbb{Z}[\omega]$ is indeed a PID. But Euler did not *prove* this; he took it for granted. The fact that UPF holds in $\mathbb{Z}[\omega]$ was rigorously established only later – among others by Gauss.

The gap is repairable: one can make Euler's proof completely correct by establishing the PID property of $\mathbb{Z}[\omega]$ first. But the gap reveals a deep conceptual problem: for general $p$, $\mathbb{Z}[\zeta_p]$ is not a PID, and Euler's strategy breaks down.

## 6. A Taste of Where the Method Fails

For $p = 5$, we consider $\mathbb{Z}[\zeta_5]$ with $\zeta_5 = e^{2\pi i/5}$. Here UPF still holds – the proof for $n = 5$ (Dirichlet/Legendre, 1825) uses this, albeit with considerably more effort.

For $p = 23$, the situation is dramatically different: $\mathbb{Z}[\zeta_{23}]$ has class number $h_{23} = 3 \neq 1$. UPF fails, and a naïve factorisation approach yields false results. This is precisely where Kummer's ideal theory stepped in, as we shall explore further in the [article on rings and fields](../../ringe-und-koerper/01-ringe-koerper/article_en.md).

The moral: **The proof for $n = 3$ works because we are lucky.** The Eisenstein integers are "good enough" – they have unique factorisation. For general $p$, an entirely different approach is needed.

## 7. From Euler to Kummer – and Beyond

The proof for $n = 3$ marks a turning point in the history of FLT:

| Aspect | $n = 4$ (Fermat) | $n = 3$ (Euler) |
|--------|-------------------|------------------|
| Number domain | $\mathbb{Z}$ | $\mathbb{Z}[\omega]$ |
| Factorisation | Pythagorean triples | cubic factorisation |
| Descent via | size of $z$ | $\lambda$-valuation |
| New mathematics | Infinite Descent | Algebraic Number Theory |

From here the path branches:

1. **Foundational tools**: To understand the proof for general $p$, we need groups, rings, fields, Galois theory – the "language" of modern algebra.
2. **Specialised tools**: Elliptic curves and modular forms – the objects that Wiles' proof connects.
3. **The proof itself**: Galois representations, deformation theory, the $R = T$ theorem – the heart of the matter.

In the following tool topics, we build these foundations piece by piece.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 2
- **Harold Edwards**: *Fermat's Last Theorem*, Ch. 3 – the most detailed account of Euler's proof
- **Kenneth Ireland, Michael Rosen**: *A Classical Introduction to Modern Number Theory* – the Eisenstein integers in context
