---
title: "Equations and Equivalent Transformations"
description: "The equals sign, permitted operations, and equivalence transformations"
lang: en
type: vorwissen
---

# Equations and Equivalent Transformations

## What Is an Equation?

An **equation** is a statement of the form $A = B$, where $A$ and $B$ are mathematical expressions. The equals sign "$=$" means: both sides represent the same value.

**Examples.**

- $3 + 4 = 7$ — a true statement.
- $2x + 1 = 9$ — a statement whose truth value depends on $x$. For $x = 4$: true. For $x = 3$: false.

## Equivalence Transformations

An **equivalence transformation** modifies an equation while preserving its solution set. The new equation has exactly the same solutions as the original.

### Permitted Operations

| Operation | Formula | Condition |
|-----------|---------|-----------|
| Add to both sides | $A = B \iff A + c = B + c$ | — |
| Subtract from both sides | $A = B \iff A - c = B - c$ | — |
| Multiply both sides | $A = B \iff A \cdot c = B \cdot c$ | $c \neq 0$ |
| Divide both sides | $A = B \iff \frac{A}{c} = \frac{B}{c}$ | $c \neq 0$ |

The principle: the same operation is applied to **both** sides. The equation remains balanced.

### Example: Solving $2x + 3 = 11$

| Step | Equation | Operation |
|------|----------|-----------|
| 1 | $2x + 3 = 11$ | Starting equation |
| 2 | $2x = 8$ | $-3$ on both sides |
| 3 | $x = 4$ | $\div 2$ on both sides |

Every line has the same solution set: $\{4\}$.

## Non-Equivalence Transformations

Not every operation preserves the solution set:

- **Multiplication by 0:** From $x = 3$ one obtains $0 = 0$ — every $x$ is now a "solution". Solution set enlarged.
- **Squaring:** From $x = -2$ one obtains $x^2 = 4$, which also admits $x = 2$. Solution set enlarged.
- **Division by an expression containing the variable:** From $x^2 = 2x$, dividing by $x$ yields $x = 2$. The solution $x = 0$ is lost.

## Equations with Fractions

For equations involving fractions, multiply both sides by the least common denominator:

**Example.** $\frac{x}{3} + \frac{1}{2} = \frac{5}{6}$

Multiply by $6$ (lcm of $3, 2, 6$):

$$
2x + 3 = 5 \implies 2x = 2 \implies x = 1
$$

## Systems of Equations

A **system of equations** consists of several equations with several unknowns. The solution must satisfy all equations simultaneously.

**Example.** $\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$

Adding both equations: $2x = 6$, so $x = 3$. Substituting: $y = 2$.

---

## Summary

| Concept | Meaning |
|---------|---------|
| Equation | Statement $A = B$ |
| Equivalence transformation | Operation preserving the solution set |
| Permitted | $+c$, $-c$, $\cdot c$ ($c \neq 0$), $\div c$ ($c \neq 0$) on both sides |
| Not permitted | $\cdot 0$, squaring, division by variable (without case distinction) |

## References

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2nd edition, 1996.
