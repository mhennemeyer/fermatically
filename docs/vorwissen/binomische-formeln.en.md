---
title: "Binomial Formulas and Factorization"
description: "The three binomial formulas and their use in algebraic manipulation"
lang: en
type: vorwissen
---

# Binomial Formulas and Factorization

## The Three Binomial Formulas

### First Binomial Formula

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

**Example.** $(x + 3)^2 = x^2 + 6x + 9$.

### Second Binomial Formula

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

**Example.** $(x - 5)^2 = x^2 - 10x + 25$.

### Third Binomial Formula

$$
(a + b)(a - b) = a^2 - b^2
$$

**Example.** $(x + 4)(x - 4) = x^2 - 16$.

## Factorization

The binomial formulas can also be read in reverse — for **factoring** (decomposing into factors):

| Expression | Factored Form |
|-----------|---------------|
| $a^2 + 2ab + b^2$ | $(a + b)^2$ |
| $a^2 - 2ab + b^2$ | $(a - b)^2$ |
| $a^2 - b^2$ | $(a + b)(a - b)$ |

**Example.** $x^2 - 9 = x^2 - 3^2 = (x + 3)(x - 3)$.

**Example.** $4x^2 - 12x + 9 = (2x)^2 - 2 \cdot 2x \cdot 3 + 3^2 = (2x - 3)^2$.

## Application: Quadratic Equations

The third binomial formula solves equations of the form $a^2 = b^2$:

$$
a^2 = b^2 \iff a^2 - b^2 = 0 \iff (a+b)(a-b) = 0 \iff a = b \text{ or } a = -b
$$

## Higher Powers (Preview)

For $(a + b)^n$ with $n > 2$, the **binomial theorem** applies:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

with the **binomial coefficient** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

**Example.** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$.

---

## Summary

| Formula | Equation |
|---------|----------|
| 1st binomial | $(a+b)^2 = a^2 + 2ab + b^2$ |
| 2nd binomial | $(a-b)^2 = a^2 - 2ab + b^2$ |
| 3rd binomial | $(a+b)(a-b) = a^2 - b^2$ |
| Binomial theorem | $(a+b)^n = \sum \binom{n}{k} a^{n-k} b^k$ |

## References

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2nd edition, 1996.
