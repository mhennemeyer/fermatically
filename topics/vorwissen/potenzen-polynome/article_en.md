---
title: "Powers and Polynomials"
description: "Laws of exponents, polynomial expressions, and degree"
lang: en
type: vorwissen
---

# Powers and Polynomials

## Powers

For $a \in \mathbb{R}$ and $n \in \mathbb{N}$, the **power** $a^n$ is defined as:

$$
a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ factors}}, \quad a^0 = 1 \;(a \neq 0)
$$

Here $a$ is the **base** and $n$ is the **exponent**.

### Laws of Exponents

For $a, b \neq 0$ and $m, n \in \mathbb{Z}$:

| Law | Formula |
|-----|---------|
| Same base, multiplication | $a^m \cdot a^n = a^{m+n}$ |
| Same base, division | $\frac{a^m}{a^n} = a^{m-n}$ |
| Power of a power | $(a^m)^n = a^{m \cdot n}$ |
| Product | $(a \cdot b)^n = a^n \cdot b^n$ |
| Quotient | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |
| Negative exponent | $a^{-n} = \frac{1}{a^n}$ |

**Example.** $2^3 \cdot 2^4 = 2^7 = 128$.

**Example.** $(3^2)^3 = 3^6 = 729$.

## Polynomials

A **polynomial** in the variable $x$ is an expression of the form:

$$
p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 = \sum_{k=0}^{n} a_k x^k
$$

The numbers $a_0, a_1, \ldots, a_n$ are called **coefficients**. The coefficient $a_n$ ($a_n \neq 0$) is the **leading coefficient**.

### Degree

The **degree** of a polynomial is the highest exponent with a non-zero coefficient:

$$
\deg(p) = n \quad \text{if } a_n \neq 0
$$

**Examples.**

- $p(x) = 3x^4 - 2x + 7$ has degree $4$.
- $p(x) = 5$ (constant, $\neq 0$) has degree $0$.
- The zero polynomial $p(x) = 0$ has no defined degree (convention: $\deg(0) = -\infty$).

### Rules for the Degree

$$
\deg(p \cdot q) = \deg(p) + \deg(q)
$$

$$
\deg(p + q) \leq \max(\deg(p), \deg(q))
$$

### Roots

A **root** (or zero) of $p(x)$ is a value $x_0$ with $p(x_0) = 0$. A polynomial of degree $n$ has at most $n$ roots (over $\mathbb{R}$; counted with multiplicity over $\mathbb{C}$, exactly $n$).

**Example.** $p(x) = x^2 - 4 = (x-2)(x+2)$ has roots $x = 2$ and $x = -2$.

---

## Summary

| Concept | Definition |
|---------|-----------|
| $a^n$ | $a$ multiplied by itself $n$ times |
| Polynomial | $\sum_{k=0}^n a_k x^k$ |
| Degree | Highest exponent with $a_k \neq 0$ |
| Root | $x_0$ with $p(x_0) = 0$ |

## References

- Lang, Serge: *Algebra.* Springer, 3rd edition, 2002. Chapter 4.
