---
title: "Inequalities"
description: "Order on the real numbers, computation rules, and absolute value"
lang: en
type: vorwissen
---

# Inequalities

## Order on ℝ

The real numbers $\mathbb{R}$ carry a **total order**: for any two numbers $a, b \in \mathbb{R}$, exactly one of $a < b$, $a = b$, or $a > b$ holds.

| Symbol | Meaning |
|--------|---------|
| $a < b$ | $a$ is strictly less than $b$ |
| $a \leq b$ | $a$ is less than or equal to $b$ |
| $a > b$ | $a$ is strictly greater than $b$ |
| $a \geq b$ | $a$ is greater than or equal to $b$ |

## Computation Rules

### Addition and Subtraction

The order is preserved:

$$
a < b \implies a + c < b + c \quad \text{for all } c \in \mathbb{R}
$$

### Multiplication by a Positive Number

The order is preserved:

$$
a < b \text{ and } c > 0 \implies a \cdot c < b \cdot c
$$

### Multiplication by a Negative Number

The order **reverses**:

$$
a < b \text{ and } c < 0 \implies a \cdot c > b \cdot c
$$

**Example.** $2 < 5$. Multiplying by $-3$: $-6 > -15$. The inequality sign flips.

### Reciprocal

For $a, b > 0$:

$$
a < b \implies \frac{1}{a} > \frac{1}{b}
$$

**Example.** $2 < 5 \implies \frac{1}{2} > \frac{1}{5}$.

## Example: Solving an Inequality

$-3x + 6 \leq 12$

| Step | Inequality | Operation |
|------|-----------|-----------|
| 1 | $-3x + 6 \leq 12$ | Starting inequality |
| 2 | $-3x \leq 6$ | $-6$ on both sides |
| 3 | $x \geq -2$ | $\div (-3)$, sign flips |

Solution set: $[-2, \infty)$.

## Absolute Value

The **absolute value** of a real number $a$ is defined as:

$$
|a| = \begin{cases} a & \text{if } a \geq 0 \\ -a & \text{if } a < 0 \end{cases}
$$

Geometrically: $|a|$ is the distance from $a$ to zero on the number line.

### Triangle Inequality

For all $a, b \in \mathbb{R}$:

$$
|a + b| \leq |a| + |b|
$$

**Example.** $|3 + (-5)| = |-2| = 2 \leq |3| + |-5| = 3 + 5 = 8$. ✓

### Absolute Value Inequalities

$$
|x| < c \iff -c < x < c \quad (c > 0)
$$

$$
|x| > c \iff x < -c \text{ or } x > c \quad (c > 0)
$$

---

## Summary

| Rule | Condition |
|------|-----------|
| $a < b \implies a + c < b + c$ | Always |
| $a < b \implies ac < bc$ | $c > 0$ |
| $a < b \implies ac > bc$ | $c < 0$ (sign flips) |
| $\|a + b\| \leq \|a\| + \|b\|$ | Triangle inequality |

## References

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2nd edition, 1996.
