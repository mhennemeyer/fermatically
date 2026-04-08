---
title: "p-adic Numbers – A Different Way of Looking at Numbers"
slug: p-adische-zahlen/01-p-adische-zahlen
series: p-adische-zahlen
part: 1
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - p-adic
  - valuation
  - local-global
requires:
  - ringe-und-koerper/01-ringe-koerper
---

# $p$-adic Numbers

!!! abstract "Summary"
    There is not just one way to complete the rational numbers – besides the real numbers $\mathbb{R}$,
    for every prime $p$ there are the $p$-adic numbers $\mathbb{Q}_p$. In this world, "close to zero"
    means "divisible by high powers of $p$".

## Prerequisites

- [Rings and Fields](../../ringe-und-koerper/01-ringe-koerper/article_en.md)

---

## 1. A Different Metric

How do we measure the "distance" between two rational numbers? The usual answer uses the **ordinary absolute value** $|x|$: the number $1/1000$ is close to $0$ because $|1/1000|$ is small.

But there is a completely different way to define "closeness" – one based on divisibility rather than size.

**Definition.** Let $p$ be a prime. The **$p$-adic valuation** $v_p(n)$ of a non-zero integer $n$ is the highest power of $p$ dividing $n$:

$$
v_p(n) = \max\{k \geq 0 \mid p^k \mid n\}
$$

For example, with $p = 3$: $v_3(54) = 3$ (since $54 = 2 \cdot 3^3$), $v_3(7) = 0$, $v_3(81) = 4$.

The **$p$-adic absolute value** is then:

$$
|x|_p = p^{-v_p(x)} \quad \text{for } x \neq 0, \qquad |0|_p = 0
$$

The astonishing feature: the more powers of $p$ a number contains, the *smaller* its $p$-adic absolute value becomes. For $p = 5$:

| Number $x$ | $v_5(x)$ | $\|x\|_5$ | $\|x\|$ (ordinary) |
|-------------|-----------|------------|---------------------|
| $1$ | $0$ | $1$ | $1$ |
| $5$ | $1$ | $1/5$ | $5$ |
| $25$ | $2$ | $1/25$ | $25$ |
| $625$ | $4$ | $1/625$ | $625$ |
| $1/5$ | $-1$ | $5$ | $0.2$ |

Intuition is turned on its head: $625$ is $5$-adically tiny (close to $0$), but ordinarily large!

## 2. Convergence Turned Upside Down

The $p$-adic absolute value defines a metric on $\mathbb{Q}$: $d_p(x, y) = |x - y|_p$. In this metric, convergence statements hold that seem absurd from the perspective of analysis.

**Example: The series $\sum_{n=0}^{\infty} p^n$ converges in $\mathbb{Q}_p$.**

The partial sums $S_N = 1 + p + p^2 + \cdots + p^N$ converge $p$-adically because the summands $p^n$ tend to $0$ $p$-adically for large $n$: $|p^n|_p = p^{-n} \to 0$. In fact, the series converges to:

$$
\sum_{n=0}^{\infty} p^n = \frac{1}{1-p} = \frac{-1}{p-1}
$$

So in $\mathbb{Q}_5$, $1 + 5 + 25 + 125 + \cdots = -\frac{1}{4}$. This sounds paradoxical, but is $5$-adically perfectly correct.

### The Ultrametric Inequality

The $p$-adic absolute value satisfies a property stronger than the triangle inequality:

$$
|x + y|_p \leq \max(|x|_p, |y|_p)
$$

This is the **ultrametric inequality** (or "strong triangle inequality"). It has startling consequences:

- Every triangle in $\mathbb{Q}_p$ is **isosceles** (the two longest sides have equal length)
- Every point of a "disc" is its centre
- Series converge if and only if their terms tend to $0$ (no ratio test needed!)

## 3. Construction of $\mathbb{Q}_p$

The real numbers $\mathbb{R}$ arise as the **completion** of $\mathbb{Q}$ with respect to the ordinary absolute value $|\cdot|$: one adds the limits of all Cauchy sequences.

Entirely analogously: the **$p$-adic numbers** $\mathbb{Q}_p$ are the completion of $\mathbb{Q}$ with respect to the $p$-adic absolute value $|\cdot|_p$.

Formally: $\mathbb{Q}_p$ is the quotient field of Cauchy sequences in $(\mathbb{Q}, |\cdot|_p)$ modulo null sequences. Every element of $\mathbb{Q}_p$ can be uniquely written as a **$p$-adic expansion**:

$$
x = \sum_{n=k}^{\infty} a_n p^n \quad \text{with } a_n \in \{0, 1, \ldots, p-1\}, \quad k \in \mathbb{Z}
$$

This is like a "decimal expansion", but infinite to the left rather than to the right. The ordinary decimal representation $0.333\ldots = 1/3$ has finitely many digits before the decimal point and infinitely many after. In $\mathbb{Q}_p$ it is the other way round: finitely many digits after the "decimal point" (negative powers of $p$) and possibly infinitely many before.

## 4. Ostrowski's Theorem

How many essentially different absolute values are there on $\mathbb{Q}$?

**Theorem (Ostrowski, 1916).** Every non-trivial absolute value on $\mathbb{Q}$ is equivalent to one of the following:

- The **ordinary absolute value** $|\cdot|$ (whose completion yields $\mathbb{R}$)
- A **$p$-adic absolute value** $|\cdot|_p$ for some prime $p$ (whose completion yields $\mathbb{Q}_p$)

That is: $\mathbb{R}$ and the $\mathbb{Q}_p$ (for all primes $p$) are the **only** completions of $\mathbb{Q}$. Every place – every way to "enlarge" $\mathbb{Q}$ – corresponds either to the Archimedean absolute value ($\infty$-place) or to a $p$-adic absolute value ($p$-place).

!!! note "Hasse's Principle"
    In number theory one often writes $v \in \{\infty, 2, 3, 5, 7, \ldots\}$ for the places of $\mathbb{Q}$. The local fields $\mathbb{Q}_v$ (with $\mathbb{Q}_\infty = \mathbb{R}$) together form a complete picture of the rational numbers – one sees $\mathbb{Q}$ "from all sides simultaneously".

## 5. The $p$-adic Integers $\mathbb{Z}_p$

The **valuation ring** of $\mathbb{Q}_p$ consists of all elements with $p$-adic absolute value $\leq 1$:

$$
\mathbb{Z}_p = \{x \in \mathbb{Q}_p \mid |x|_p \leq 1\} = \left\{ \sum_{n=0}^{\infty} a_n p^n \mid a_n \in \{0, \ldots, p-1\} \right\}
$$

$\mathbb{Z}_p$ is a **local ring** with the unique maximal ideal $(p) = p\mathbb{Z}_p$. The residue field is:

$$
\mathbb{Z}_p / p\mathbb{Z}_p \cong \mathbb{F}_p
$$

The $p$-adic integers have an alternative description as a **projective limit**:

$$
\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n\mathbb{Z}
$$

An element of $\mathbb{Z}_p$ is thus a compatible system $(a_1, a_2, a_3, \ldots)$ of residue classes: $a_n \in \mathbb{Z}/p^n\mathbb{Z}$ with $a_{n+1} \equiv a_n \pmod{p^n}$.

**Properties of $\mathbb{Z}_p$:**

- $\mathbb{Z}_p$ is a principal ideal domain (in fact a discrete valuation ring)
- The units are $\mathbb{Z}_p^\times = \{x \in \mathbb{Z}_p \mid |x|_p = 1\} = \mathbb{Z}_p \setminus p\mathbb{Z}_p$
- $\mathbb{Z} \subset \mathbb{Z}_p$ is dense (every $p$-adic integer is the limit of a sequence of integers)
- $\mathbb{Z}_p$ is compact (as a topological space)

## 6. Hensel's Lemma

One of the most powerful tools of $p$-adic analysis is **Hensel's lemma** – the $p$-adic version of Newton's method.

**Theorem (Hensel).** Let $f \in \mathbb{Z}_p[x]$ be a polynomial. If $a \in \mathbb{Z}$ is a **simple** root of $f$ modulo $p$ (i.e., $f(a) \equiv 0 \pmod{p}$ and $f'(a) \not\equiv 0 \pmod{p}$), then there is a unique root $\alpha \in \mathbb{Z}_p$ of $f$ with $\alpha \equiv a \pmod{p}$.

The idea: from an approximate solution modulo $p$, an exact solution in $\mathbb{Z}_p$ is constructed step by step – by iteratively "lifting" modulo $p^2$, $p^3$, $p^4$, and so on.

**Example:** Does $\sqrt{2}$ exist in $\mathbb{Q}_7$? We check: $3^2 = 9 \equiv 2 \pmod{7}$ and $2 \cdot 3 = 6 \not\equiv 0 \pmod{7}$. By Hensel's lemma, $\sqrt{2} \in \mathbb{Z}_7$ exists. By contrast, $x^2 \equiv 2 \pmod{5}$ has no solution, so $\sqrt{2} \notin \mathbb{Q}_5$.

!!! tip "Hensel as a lever"
    Hensel's lemma reduces many $p$-adic questions to finite computations modulo $p$. Instead of working in the infinite field $\mathbb{Q}_p$, it often suffices to compute in the finite field $\mathbb{F}_p$ – and then lift.

## 7. The Local-Global Principle

The central idea: information about $\mathbb{Q}$ can be obtained from the combination of **all** local information (over $\mathbb{R}$ and all $\mathbb{Q}_p$).

**Hasse–Minkowski theorem.** A quadratic form over $\mathbb{Q}$ has a non-trivial solution in $\mathbb{Q}$ if and only if it has a solution in $\mathbb{R}$ **and** in $\mathbb{Q}_p$ for **all** primes $p$.

This local-global principle works perfectly for quadratic forms – but not always. For cubic equations and elliptic curves, it can fail: there are curves that have points everywhere locally but no global rational point. The measure of this failure is the **Tate–Shafarevich group** $\Sha$ – a deep object of arithmetic geometry.

### Local Conditions in Wiles' Proof

In Wiles' proof, the local fields $\mathbb{Q}_p$ play a fundamental role:

1. **Reduction modulo $p$**: An elliptic curve $E/\mathbb{Q}$ can be considered modulo each prime $p$, yielding a curve $\tilde{E}/\mathbb{F}_p$. Whether this reduction is smooth or has singularities determines the **type** of the curve at the place $p$.

2. **Local Galois representations**: The restriction $\rho|_{G_{\mathbb{Q}_p}}$ of a Galois representation to the local Galois group encodes the behaviour of the representation "at the place $p$". Mazur's **deformation theory** classifies representations by their local properties.

3. **Semistability**: An elliptic curve is called **semistable** if at every place $p$ it has either good or multiplicative reduction. Wiles initially proved the Taniyama–Shimura conjecture only for semistable curves – which suffices for FLT because the Frey curve is semistable.

The $p$-adic numbers provide the "local lens" through which one examines algebraic objects prime by prime. Without them, Wiles' proof would be inconceivable.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 5
- **Neal Koblitz**: *p-adic Numbers, p-adic Analysis, and Zeta-Functions* – the standard introduction
- **Fernando Gouvêa**: *p-adic Numbers: An Introduction* – accessible and motivating
