---
title: "Pythagoras and Pythagorean Triples"
description: "The Pythagorean theorem, integer solutions, and the connection to Fermat's equation"
lang: en
type: vorwissen
---

# Pythagoras and Pythagorean Triples

## The Pythagorean Theorem

In a right triangle with legs $a$, $b$ and hypotenuse $c$:

$$
a^2 + b^2 = c^2
$$

The converse also holds: if the side lengths of a triangle satisfy this equation, the triangle is right-angled.

**Example.** A triangle with sides $3, 4, 5$: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$. ✓

## Pythagorean Triples

A **Pythagorean triple** is a tuple $(a, b, c)$ of natural numbers with $a^2 + b^2 = c^2$.

**Examples:**

| $a$ | $b$ | $c$ | Check |
|-----|-----|-----|-------|
| 3 | 4 | 5 | $9 + 16 = 25$ |
| 5 | 12 | 13 | $25 + 144 = 169$ |
| 8 | 15 | 17 | $64 + 225 = 289$ |

A triple is **primitive** if $\gcd(a, b, c) = 1$.

### Generating All Primitive Triples

All primitive Pythagorean triples have the form:

$$
a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2
$$

with $m > n > 0$, $\gcd(m, n) = 1$, and $m - n$ odd.

**Example.** $m = 2, n = 1$: $a = 4 - 1 = 3$, $b = 4$, $c = 4 + 1 = 5$. → $(3, 4, 5)$.

## Connection to Fermat's Equation

The equation $a^2 + b^2 = c^2$ has infinitely many integer solutions.

Fermat's Last Theorem states: for $n \geq 3$, the equation

$$
a^n + b^n = c^n
$$

has **no** solution with $a, b, c \in \mathbb{Z}^+$. The case $n = 2$ (Pythagoras) is thus the last exponent for which integer solutions exist.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Pythagorean theorem | $a^2 + b^2 = c^2$ in a right triangle |
| Pythagorean triple | $(a,b,c) \in \mathbb{N}^3$ with $a^2 + b^2 = c^2$ |
| Primitive triple | $\gcd(a,b,c) = 1$ |
| Parametrization | $a = m^2-n^2,\; b = 2mn,\; c = m^2+n^2$ |

## References

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6th edition, 2008. Chapter 13.
- Edwards, Harold M.: *Fermat's Last Theorem.* Springer, 1977. Chapter 1.
