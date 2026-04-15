---
title: "Coordinate Geometry"
description: "Points, lines, and curves in the plane"
lang: en
type: vorwissen
---

# Coordinate Geometry

## The Cartesian Coordinate System

The plane $\mathbb{R}^2$ is described by two perpendicular axes ($x$-axis, $y$-axis) with common origin $O = (0, 0)$. Every point has a unique coordinate pair $(x, y)$.

## Distance and Slope

### Distance Between Two Points

For $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$:

$$
d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

This follows directly from the Pythagorean theorem.

**Example.** $d((1, 2), (4, 6)) = \sqrt{9 + 16} = \sqrt{25} = 5$.

### Slope of a Line

The **slope** $m$ of a line through $P_1$ and $P_2$ (with $x_1 \neq x_2$):

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

## Lines

### Line Equations

Common forms of a line equation:

- **Slope-intercept form:** $y = mx + b$ (slope $m$, $y$-intercept $b$)
- **Point-slope form:** $y - y_1 = m(x - x_1)$

**Example.** Line through $(1, 3)$ with slope $2$: $y - 3 = 2(x - 1)$, so $y = 2x + 1$.

### Parallel and Perpendicular Lines

- **Parallel:** $m_1 = m_2$
- **Perpendicular:** $m_1 \cdot m_2 = -1$

## Curves in the Plane

A **curve** is the set of all points $(x, y)$ satisfying an equation $F(x, y) = 0$.

### Circle

$$
(x - a)^2 + (y - b)^2 = r^2
$$

Center $(a, b)$, radius $r$.

### Parabola

$$
y = ax^2 + bx + c
$$

**Example.** $y = x^2$ — parabola with vertex at the origin, opening upward.

### Elliptic Curves (Preview)

Equations of the form $y^2 = x^3 + ax + b$ define **elliptic curves**. These play a central role in modern number theory and in the proof of Fermat's Last Theorem.

---

## Summary

| Object | Equation |
|--------|----------|
| Distance | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Line | $y = mx + b$ |
| Circle | $(x-a)^2 + (y-b)^2 = r^2$ |
| Parabola | $y = ax^2 + bx + c$ |
| Elliptic curve | $y^2 = x^3 + ax + b$ |

## References

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2nd edition, 1996. Chapter 4.
