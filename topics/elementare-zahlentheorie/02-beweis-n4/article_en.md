---
title: "The Proof for n=4"
slug: elementare-zahlentheorie/02-beweis-n4
series: elementare-zahlentheorie
part: 2
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - fermat
  - infinite-descent
  - proof
requires: []
---

# The Proof for $n = 4$

!!! abstract "Summary"
    Fermat's own proof – the only case of FLT that he himself proved.
    We introduce the method of infinite descent and show:
    $x^4 + y^4 = z^2$ has no solution in positive integers.

## Prerequisites

- [What Is Fermat's Last Theorem?](../01-was-ist-flt/article_en.md)

---

## 1. The Method of Infinite Descent

**Infinite descent** (*descente infinie*) is a proof technique that Fermat himself invented – and which he called his favourite method. The basic idea is strikingly simple:

**Assume** an equation has a solution in positive integers. Then show that from this solution a *smaller* solution can be constructed – one in which the numbers involved are strictly smaller. From this smaller solution, an even smaller one could be constructed, and so on – *ad infinitum*.

But: positive integers cannot become infinitely small. There is no infinite descent in $\mathbb{Z}^+$. Therefore the assumption is false, and the equation has no solution.

Formally, the descent uses the **well-ordering principle**: every non-empty subset of $\mathbb{N}$ has a smallest element. An infinitely descending sequence of positive integers therefore cannot exist.

!!! note "Descent vs. Contradiction"
    Infinite descent is a special **proof by contradiction**: one assumes a solution exists and derives an impossible consequence (the infinite descending sequence). In modern formulation, equivalently: one considers a *minimal* solution and shows that an even smaller one would have to exist – contradiction.

## 2. Pythagorean Triples

Before we can carry out the proof for $n = 4$, we need a classical result: the complete description of all solutions of $x^2 + y^2 = z^2$.

**Theorem (Parametrisation of Pythagorean triples).** All *primitive* Pythagorean triples $(x, y, z)$ with $\gcd(x, y) = 1$ and $x$ even have the form:

$$
x = 2st, \quad y = s^2 - t^2, \quad z = s^2 + t^2
$$

where $s > t > 0$, $\gcd(s, t) = 1$, and $s \not\equiv t \pmod{2}$ (i.e., $s$ and $t$ have different parity).

**Proof sketch.** We write $x^2 = z^2 - y^2 = (z-y)(z+y)$. Since $(x, y, z)$ is primitive, $z - y$ and $z + y$ are coprime (up to a factor of 2). Since $x$ is even, $z$ and $y$ are both odd, so $z - y$ and $z + y$ are both even. Set $z - y = 2u$ and $z + y = 2v$, then $x^2 = 4uv$ with $\gcd(u, v) = 1$. Since the product $uv$ is a perfect square and the factors are coprime, $u$ and $v$ must themselves be perfect squares: $u = t^2$, $v = s^2$. Substituting yields the parametrisation. $\square$

**Examples:**

| $s$ | $t$ | $x = 2st$ | $y = s^2 - t^2$ | $z = s^2 + t^2$ |
|-----|-----|-----------|------------------|------------------|
| 2   | 1   | 4         | 3                | 5                |
| 3   | 2   | 12        | 5                | 13               |
| 4   | 1   | 8         | 15               | 17               |
| 4   | 3   | 24        | 7                | 25               |

## 3. From FLT to a Stronger Statement

Fermat's proof for $n = 4$ does not directly show that $x^4 + y^4 = z^4$ has no solution, but rather the **stronger** statement:

!!! tip "Theorem (Fermat)"
    The equation $x^4 + y^4 = z^2$ has no solution in positive integers.

Why is this stronger? Because $z^4 = (z^2)^2$ is a special perfect square. If there is no solution with $z^2$ on the right-hand side, then certainly not with $z^4$.

$$
x^4 + y^4 = z^4 \implies x^4 + y^4 = (z^2)^2
$$

Hence: $x^4 + y^4 = z^2$ has no solution $\implies$ $x^4 + y^4 = z^4$ has no solution.

## 4. The Proof in Detail

We prove: $x^4 + y^4 = z^2$ has no solution in $x, y, z \in \mathbb{Z}^+$.

**Assumption for contradiction.** Let $(x, y, z)$ be a solution with *minimal* $z$. Without loss of generality, let $\gcd(x, y) = 1$ (otherwise we cancel the common factor and obtain a smaller solution).

**Step 1: Apply Pythagorean triples.**

The equation $x^4 + y^4 = z^2$ can be read as $(x^2)^2 + (y^2)^2 = z^2$ – a Pythagorean triple! Since $\gcd(x, y) = 1$, the triple is primitive, and we can apply the parametrisation. Without loss of generality, let $x$ be even (otherwise swap $x$ and $y$). Then there exist $s, t$ with $s > t > 0$, $\gcd(s, t) = 1$, $s \not\equiv t \pmod{2}$, such that:

$$
x^2 = 2st, \quad y^2 = s^2 - t^2, \quad z = s^2 + t^2
$$

**Step 2: Another Pythagorean triple.**

From $y^2 = s^2 - t^2$ it follows that $y^2 + t^2 = s^2$ – again a Pythagorean triple! Since $\gcd(s, t) = 1$ and $s \not\equiv t \pmod{2}$, this triple is also primitive. Now $y$ is odd (because $x$ is even and $\gcd(x, y) = 1$), so $t$ is even. The parametrisation yields $u, v$ with $u > v > 0$, $\gcd(u, v) = 1$, $u \not\equiv v \pmod{2}$:

$$
t = 2uv, \quad y = u^2 - v^2, \quad s = u^2 + v^2
$$

**Step 3: Analyse $x^2$ as a product.**

Substituting $s = u^2 + v^2$ and $t = 2uv$ into $x^2 = 2st$:

$$
x^2 = 2 \cdot (u^2 + v^2) \cdot 2uv = 4uv(u^2 + v^2)
$$

Hence $(x/2)^2 = uv(u^2 + v^2)$. Since $\gcd(u, v) = 1$, the three factors $u$, $v$, and $u^2 + v^2$ are pairwise coprime. Their product is a perfect square, so *each individual* factor must be a perfect square:

$$
u = a^2, \quad v = b^2, \quad u^2 + v^2 = c^2
$$

for certain positive integers $a, b, c$.

**Step 4: The descent.**

From $u^2 + v^2 = c^2$ and $u = a^2$, $v = b^2$ it follows:

$$
a^4 + b^4 = c^2
$$

This is the same equation as our original one! And we have:

$$
c^2 = u^2 + v^2 = s \leq s^2 < s^2 + t^2 = z
$$

Hence $c < z$ – we have found a *smaller* solution.

**Contradiction.** We had chosen $(x, y, z)$ as a solution with minimal $z$, but $(a, b, c)$ is a solution with $c < z$. Contradiction! $\blacksquare$

## 5. Why the Descent Works

The proof has an elegant structure:

```
Solution (x, y, z) with z minimal
    → Parametrisation as Pyth. triple → (s, t)
    → Second Pyth. triple → (u, v)
    → Three coprime squares → (a², b², c²)
    → New solution (a, b, c) with c < z
    → CONTRADICTION
```

The key is that each step makes the numbers smaller. From $z$ via $s$ (which is smaller than $z$) via $u$ and $v$ (which are smaller than $s$) to $c$ (which is smaller than $z$). The well-ordering of $\mathbb{N}$ guarantees that this process cannot continue indefinitely.

!!! note "Why the stronger statement?"
    Fermat's trick of considering $z^2$ instead of $z^4$ is no coincidence. In the descent, an equation $a^4 + b^4 = c^2$ arises – only if the right-hand side is allowed to be a *general* perfect square (not just a fourth power) does the inductive loop close. Had we considered only $x^4 + y^4 = z^4$, the equation arising in the descent, $a^4 + b^4 = c^2$, would not have the same form – and the proof would break down.

## 6. Historical Context

This proof is the **only case of FLT** for which Fermat himself left a verifiable proof. It appears in his *Observationes* (appendix to the 1670 edition of the Arithmetica) and there proves the statement that the area of a right triangle with integer sides cannot be a perfect square – which is equivalent to $x^4 + y^4 = z^2$.

**What the proof shows – and what it doesn't:**

- ✅ FLT is true for $n = 4$ (and hence for all $n$ divisible by $4$: $n = 8, 12, 16, \ldots$)
- ❌ The method **cannot** be directly transferred to $n = 3$ – the simple parametrisation of "cubic triples" is lacking
- ❌ For general primes $p$, the elementary descent fails

The case $n = 3$ requires, as we shall see in [Article 4](../04-beweis-n3/article_en.md), a decisive conceptual leap: one must extend the number domain from $\mathbb{Z}$ to $\mathbb{Z}[\omega]$. Here begins the path to algebraic number theory.

---

## Further Reading

- **Fermat**: *Observationes ad Diophantum* (1670) – the original proof
- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 1
- **Harold Edwards**: *Fermat's Last Theorem* – historically detailed exposition
