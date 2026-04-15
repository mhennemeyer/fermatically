---
title: "Divisibility and GCD"
description: "Division with remainder, greatest common divisor, and the Euclidean algorithm"
lang: en
type: vorwissen
---

# Divisibility and GCD

## Divisibility

An integer $a$ **divides** an integer $b$ if there exists a $k \in \mathbb{Z}$ with $b = k \cdot a$. Notation: $a \mid b$.

$$
a \mid b \iff \exists\, k \in \mathbb{Z}: b = k \cdot a
$$

**Example.** $3 \mid 12$, since $12 = 4 \cdot 3$. However, $3 \nmid 7$, since no integer $k$ satisfies $7 = k \cdot 3$.

### Basic Properties

- **Reflexivity:** $a \mid a$ for all $a \neq 0$.
- **Transitivity:** If $a \mid b$ and $b \mid c$, then $a \mid c$.
- **Linearity:** If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$ and $a \mid (b - c)$.

## Division with Remainder

For any integers $a$ and $b$ with $b > 0$, there exist unique integers $q$ (quotient) and $r$ (remainder) such that:

$$
a = q \cdot b + r, \quad 0 \leq r < b
$$

**Example.** $17 = 2 \cdot 7 + 3$. Here $q = 2$ and $r = 3$.

Division with remainder is the foundation of modular arithmetic and the Euclidean algorithm.

## Greatest Common Divisor (GCD)

The **greatest common divisor** of two integers $a$ and $b$ (not both $0$) is the largest positive integer that divides both $a$ and $b$:

$$
\gcd(a, b) = \max\{d \in \mathbb{N} : d \mid a \text{ and } d \mid b\}
$$

**Example.** The divisors of $12$ are $\{1, 2, 3, 4, 6, 12\}$, the divisors of $18$ are $\{1, 2, 3, 6, 9, 18\}$. Common divisors: $\{1, 2, 3, 6\}$. Thus $\gcd(12, 18) = 6$.

### Coprimality

Two numbers $a$ and $b$ are **coprime** if $\gcd(a, b) = 1$.

**Example.** $\gcd(8, 15) = 1$, so $8$ and $15$ are coprime.

## The Euclidean Algorithm

The Euclidean algorithm computes $\gcd(a, b)$ through repeated division with remainder. The key property:

$$
\gcd(a, b) = \gcd(b, a \bmod b)
$$

### Procedure

Given: $a, b \in \mathbb{Z}$ with $a \geq b > 0$.

1. Compute $r = a \bmod b$.
2. If $r = 0$: $\gcd(a, b) = b$. Done.
3. Otherwise: Set $a \leftarrow b$, $b \leftarrow r$ and repeat from step 1.

### Example: $\gcd(252, 105)$

| Step | $a$   | $b$   | $r = a \bmod b$ |
|------|-------|-------|------------------|
| 1    | 252   | 105   | 42               |
| 2    | 105   | 42    | 21               |
| 3    | 42    | 21    | 0                |

Result: $\gcd(252, 105) = 21$.

### Correctness

The algorithm terminates because the remainders are strictly decreasing ($r < b$ at each step). It is correct because $\gcd(a, b) = \gcd(b, r)$ holds: every common divisor of $a$ and $b$ also divides $r = a - q \cdot b$, and conversely.

## Bézout's Lemma

For all $a, b \in \mathbb{Z}$ (not both $0$), there exist $x, y \in \mathbb{Z}$ with:

$$
\gcd(a, b) = x \cdot a + y \cdot b
$$

The coefficients $x, y$ can be computed using the **extended Euclidean algorithm**.

**Example.** $\gcd(252, 105) = 21$. We have $21 = 1 \cdot 252 + (-2) \cdot 105$, so $x = 1, y = -2$.

Bézout's lemma is a central tool in number theory. Among other things, it implies: if $a$ and $b$ are coprime and $a \mid bc$, then $a \mid c$.

---

## Summary

| Concept | Definition |
|---------|-----------|
| $a \mid b$ | There exists $k \in \mathbb{Z}$ with $b = ka$ |
| Division with remainder | $a = qb + r$ with $0 \leq r < b$ |
| $\gcd(a,b)$ | Greatest common divisor |
| Coprime | $\gcd(a,b) = 1$ |
| Euclidean algorithm | $\gcd(a,b) = \gcd(b, a \bmod b)$ |
| Bézout | $\gcd(a,b) = xa + yb$ for suitable $x, y \in \mathbb{Z}$ |

## References

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6th edition, 2008. Chapters 1–2.
- Burton, David M.: *Elementary Number Theory.* McGraw-Hill, 7th edition, 2010. Chapter 2.
