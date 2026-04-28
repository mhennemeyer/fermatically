---
title: "Curvature of Surfaces (Gauss)"
slug: vorwissen/geometrie-analysis/kruemmung-flaechen-gauss
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: en
tags:
  - kruemmung
  - gauss
  - surfaces
---

# Curvature of Surfaces (Gauss)

> *"Theorema Egregium: Gaussian curvature is an intrinsic quantity – it
> depends only on the first fundamental form, not on *how* the surface
> is embedded."*
> — Carl Friedrich Gauss, *Disquisitiones generales circa superficies curvas*, 1827.

Gaussian curvature is the historical starting point of modern
differential geometry. It measures how a surface is bent at a point –
and Gauss's discovery that it is *intrinsic* is the springboard to
sectional, Ricci, and scalar curvature in higher dimensions.

## 1. Principal curvatures

Let $\Sigma \subset \mathbb{R}^3$ be a smooth surface and $p \in \Sigma$.
Choose a unit normal $\nu(p)$. Slicing $\Sigma$ with a plane through
$p$ that contains $\nu(p)$ yields a planar curve with a **normal
curvature** $\kappa$.

Rotating the slicing plane around $\nu(p)$, $\kappa$ varies between a
minimum $\kappa_2$ and a maximum $\kappa_1$. These extremal values are
the **principal curvatures** at $p$ (Euler 1760, elaborated by
Meusnier 1776).

From them one defines:

- **Gaussian curvature:** $K = \kappa_1 \kappa_2$.
- **Mean curvature:** $H = \tfrac{1}{2}(\kappa_1 + \kappa_2)$.

| Surface | $K$ | Sign |
|---------|-----|------|
| plane | $0$ | flat |
| sphere of radius $R$ | $1/R^2$ | positive |
| cylinder | $0$ | flat (one principal curvature vanishes) |
| saddle surface | $< 0$ | hyperbolic |
| pseudosphere | $-1$ constant | hyperbolic |

## 2. First and second fundamental form

Locally $\Sigma$ can be parametrised as $\mathbf r(u, v)$. The **first
fundamental form** describes length measurement on $\Sigma$:
$$
\mathrm{I} = E\, \mathrm{d}u^2 + 2F\, \mathrm{d}u\, \mathrm{d}v + G\, \mathrm{d}v^2,
\quad E = \mathbf r_u \cdot \mathbf r_u,\ F = \mathbf r_u \cdot \mathbf r_v,\ G = \mathbf r_v \cdot \mathbf r_v.
$$
It is the Riemannian metric of the surface (see
[Tangent Space and Tensors](tangentialraum-tensoren.md)).

The **second fundamental form** measures how the normal direction
changes with the point:
$$
\mathrm{II} = L\, \mathrm{d}u^2 + 2M\, \mathrm{d}u\, \mathrm{d}v + N\, \mathrm{d}v^2,
\quad L = \mathbf r_{uu} \cdot \nu, \dots
$$
It knows the embedding of the surface.

In this language
$$
K = \frac{LN - M^2}{EG - F^2}.
$$

## 3. Theorema Egregium

Gauss's surprising discovery (1827):
$$
K \text{ depends only on } E, F, G \text{ and their derivatives.}
$$
That is: someone living on the surface, equipped with length and angle
measurements but unaware of the surrounding $\mathbb{R}^3$, can still
compute $K$. So $K$ is *intrinsic* data of the Riemannian metric.

Consequence: a sphere cannot be unrolled into a plane without
distorting distances – every world map lies.

## 4. Geodesic triangles and Gauss–Bonnet

On a surface with curvature $K$ one obtains the **angle-sum theorem
for geodesic triangles**:
$$
\alpha + \beta + \gamma - \pi = \int_T K\, \mathrm{d}A.
$$
On the sphere ($K = 1/R^2 > 0$) the angle sum exceeds $\pi$; on a
hyperbolic surface ($K < 0$) it is smaller.

The **Gauss–Bonnet theorem** generalises this to closed surfaces:
$$
\int_\Sigma K\, \mathrm{d}A = 2\pi\, \chi(\Sigma),
$$
where $\chi(\Sigma)$ is the **Euler characteristic**. For
$\Sigma = S^2$ this gives $\chi(S^2) = 2$, for the torus
$\chi(T^2) = 0$. This formula is the bridge from curvature
(analysis) to topology (what the surface "is") – the same architectural
principle that Perelman's proof of finite extinction in
[Act 3, Article 05](../../poincare/beweis/05-endliche-extinktion.md)
re-uses on the 2-sphere.

## 5. From special case to higher-dimensional curvature

In $n$ dimensions $K$ generalises to the **sectional curvature**
$\sec(P)$ of a 2-plane $P \subset T_p M$. Averaging over all 2-planes
containing a vector $v$ yields the **Ricci curvature**
$\mathrm{Ric}(v, v)$. Averaging further over all directions yields the
**scalar curvature** $R$. Gaussian curvature is thus the
two-dimensional grandfather of the entire curvature zoo
([Act 2, Article 02](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md)).

## Cross-references

- Previous: [Tangent Space and Tensors](tangentialraum-tensoren.md).
- Continue: [Vector Calculus in a Nutshell](vektoranalysis.md), [The Heat Equation – Intuition](waermeleitung.md).
- Application: [Act 2, Curvature and the Ricci tensor](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md), [Act 3, Finite extinction](../../poincare/beweis/05-endliche-extinktion.md) (Gauss–Bonnet in the proof).

## Sources

- do Carmo, Manfredo P. (1976). *Differential Geometry of Curves and Surfaces.* Prentice Hall. Ch. 3–4.
- Spivak, Michael (1999). *A Comprehensive Introduction to Differential Geometry, Vol. 2.* Publish or Perish, 3rd ed.
- Gauss, Carl Friedrich (1827). *Disquisitiones generales circa superficies curvas.*
- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2nd ed. Ch. 8.
