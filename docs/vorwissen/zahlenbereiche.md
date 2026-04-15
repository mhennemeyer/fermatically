---
title: "Number Systems"
description: "ℕ, ℤ, ℚ, ℝ, ℂ – the chain of number system extensions"
lang: en
type: vorwissen
---

# Number Systems

## The Extension Chain

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

Each extension solves a problem that was unsolvable in the previous number system.

## Natural Numbers (ℕ)

$$
\mathbb{N} = \{0, 1, 2, 3, \ldots\}
$$

Suitable for: counting, addition, multiplication.

**Problem:** The equation $x + 3 = 1$ has no solution in $\mathbb{N}$.

## Integers (ℤ)

$$
\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}
$$

Extension of $\mathbb{N}$ by negative numbers. Subtraction is unrestricted.

**Problem:** The equation $2x = 3$ has no solution in $\mathbb{Z}$.

## Rational Numbers (ℚ)

$$
\mathbb{Q} = \left\{\frac{a}{b} : a \in \mathbb{Z},\; b \in \mathbb{Z} \setminus \{0\}\right\}
$$

Extension of $\mathbb{Z}$ by fractions. Division (except by $0$) is unrestricted.

Rational numbers have either a terminating or a repeating decimal expansion: $\frac{1}{4} = 0.25$, $\frac{1}{3} = 0.\overline{3}$.

**Problem:** The equation $x^2 = 2$ has no solution in $\mathbb{Q}$ (since $\sqrt{2}$ is irrational).

## Real Numbers (ℝ)

$\mathbb{R}$ comprises all points on the number line: rational and irrational numbers.

Irrational numbers have a non-repeating, infinite decimal expansion: $\sqrt{2} = 1.41421\ldots$, $\pi = 3.14159\ldots$

$\mathbb{R}$ is **complete**: every Cauchy sequence converges in $\mathbb{R}$.

**Problem:** The equation $x^2 = -1$ has no solution in $\mathbb{R}$.

## Complex Numbers (ℂ)

$$
\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}, \quad i^2 = -1
$$

Extension of $\mathbb{R}$ by the **imaginary unit** $i$. Every polynomial equation has a solution in $\mathbb{C}$ (Fundamental Theorem of Algebra).

**Example.** $x^2 + 1 = 0$ has solutions $x = i$ and $x = -i$.

---

## Summary

| Number System | Symbol | New Property | Unsolvable Problem |
|--------------|--------|--------------|-------------------|
| Natural numbers | $\mathbb{N}$ | Counting | $x + 3 = 1$ |
| Integers | $\mathbb{Z}$ | Subtraction | $2x = 3$ |
| Rational numbers | $\mathbb{Q}$ | Division | $x^2 = 2$ |
| Real numbers | $\mathbb{R}$ | Completeness | $x^2 = -1$ |
| Complex numbers | $\mathbb{C}$ | Algebraically closed | — |

## References

- Ebbinghaus, H.-D. et al.: *Numbers.* Springer, 1991.
- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2nd edition, 1996. Chapter 2.
