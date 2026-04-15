---
title: "Complex Numbers"
description: "Imaginary unit, representation, arithmetic operations, roots of unity, and the upper half-plane"
lang: en
type: vorwissen
---

# Complex Numbers

## The Imaginary Unit

The equation $x^2 = -1$ has no solution in the real numbers. The **imaginary unit** $i$ is defined as a solution to this equation:

$$
i^2 = -1
$$

With $i$, all quadratic equations become solvable, including those with negative discriminant.

## Representation and Basic Concepts

A **complex number** has the form $z = a + bi$ with $a, b \in \mathbb{R}$. Here $a = \operatorname{Re}(z)$ is the **real part** and $b = \operatorname{Im}(z)$ is the **imaginary part**.

The set of all complex numbers is denoted $\mathbb{C}$:

$$
\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}
$$

Every real number is a complex number with $b = 0$, so $\mathbb{R} \subset \mathbb{C}$.

### Conjugation and Absolute Value

The **complex conjugate** of $z = a + bi$ is:

$$
\bar{z} = a - bi
$$

The **absolute value** (modulus) of $z$ is:

$$
|z| = \sqrt{a^2 + b^2} = \sqrt{z \cdot \bar{z}}
$$

**Example.** For $z = 3 + 4i$: $\bar{z} = 3 - 4i$ and $|z| = \sqrt{9 + 16} = 5$.

## Arithmetic Operations

For $z_1 = a + bi$ and $z_2 = c + di$:

**Addition:**
$$
z_1 + z_2 = (a + c) + (b + d)i
$$

**Multiplication** (using $i^2 = -1$):
$$
z_1 \cdot z_2 = (ac - bd) + (ad + bc)i
$$

**Division** (multiplying by the conjugate of the denominator):
$$
\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
$$

**Example.** $(2 + 3i)(1 - i) = 2 - 2i + 3i - 3i^2 = 2 + i + 3 = 5 + i$.

## Polar Form

Every complex number $z \neq 0$ can be written in polar form:

$$
z = r(\cos\varphi + i\sin\varphi) = r \cdot e^{i\varphi}
$$

Here $r = |z|$ is the modulus and $\varphi = \arg(z)$ is the **argument** (angle to the positive real axis). The second equality uses **Euler's formula**:

$$
e^{i\varphi} = \cos\varphi + i\sin\varphi
$$

> "The formula $e^{i\pi} + 1 = 0$ connects the five most important constants in mathematics."
> — Eli Maor, *e: The Story of a Number*, Princeton University Press, 1994.

The polar form simplifies multiplication and exponentiation: moduli are multiplied, arguments are added.

## Roots of Unity

The **$n$-th roots of unity** are the $n$ solutions of the equation $z^n = 1$:

$$
\zeta_k = e^{2\pi i k/n}, \quad k = 0, 1, \ldots, n-1
$$

The number $\zeta = e^{2\pi i/n}$ is called a **primitive $n$-th root of unity**. All $n$-th roots of unity are powers of $\zeta$: $\{\zeta^0, \zeta^1, \ldots, \zeta^{n-1}\}$.

**Example.** The cube roots of unity ($n = 3$) are:

$$
\zeta_0 = 1, \quad \zeta_1 = e^{2\pi i/3} = -\frac{1}{2} + \frac{\sqrt{3}}{2}i, \quad \zeta_2 = e^{4\pi i/3} = -\frac{1}{2} - \frac{\sqrt{3}}{2}i
$$

In number theory, roots of unity play a central role — for instance as the basis of **cyclotomic rings** $\mathbb{Z}[\zeta_p]$, which appear in Kummer's approach to proving Fermat's Last Theorem.

## The Upper Half-Plane

The **upper half-plane** is the set of all complex numbers with positive imaginary part:

$$
\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}
$$

The upper half-plane is the natural domain of modular forms — complex-valued functions with special symmetry properties.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Imaginary unit | $i^2 = -1$ |
| Complex number | $z = a + bi$ with $a, b \in \mathbb{R}$ |
| Conjugate | $\overline{a + bi} = a - bi$ |
| Absolute value | $|z| = \sqrt{a^2 + b^2}$ |
| Euler's formula | $e^{i\varphi} = \cos\varphi + i\sin\varphi$ |
| $n$-th root of unity | $\zeta = e^{2\pi i/n}$ |
| Upper half-plane | $\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}$ |

## References

- Needham, Tristan: *Visual Complex Analysis.* Oxford University Press, 1997. Chapters 1–4.
- Ahlfors, Lars V.: *Complex Analysis.* McGraw-Hill, 3rd edition, 1979. Chapter 1.
- Maor, Eli: *e: The Story of a Number.* Princeton University Press, 1994.
