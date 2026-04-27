---
title: "Curvature and the Ricci Tensor"
slug: poincare/ricci-fluss/02-kruemmung-ricci-tensor
series: poincare
part: 2
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - curvature
  - ricci-tensor
---

# Curvature and the Ricci Tensor

!!! abstract "Summary"
    Curvature measures how far a Riemannian manifold deviates locally
    from Euclidean space. Out of the Riemann curvature tensor one
    obtains, by tracing, sectional curvature, the Ricci tensor and the
    scalar curvature. The Ricci tensor – an averaged notion of
    curvature – is the right-hand side of Hamilton's Ricci flow.

## 1. Why Curvature?

A flat plane differs from a sphere because geodesics on the sphere
converge while in the plane they remain parallel. Curvature makes this
behaviour quantitative. On a Riemannian manifold $(M, g)$ the
Levi-Civita connection ([Article 01](01-riemannsche-metrik.md), §6)
encodes the **failure of covariant derivatives to commute**.

## 2. The Riemann Curvature Tensor

For vector fields $X, Y, Z$:

$$R(X,Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z.$$

$R$ is tensorial – $R_p(X,Y)Z$ depends only on the values of $X,Y,Z$
at $p$. In index notation:

$$R^l{}_{ijk} = \partial_i \Gamma^l_{jk} - \partial_j \Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}.$$

With lowered index $R_{lijk} = g_{lm} R^m{}_{ijk}$ the **symmetries**
read

- antisymmetry: $R_{lijk} = -R_{iljk}$ and $R_{lijk} = -R_{likj}$,
- block symmetry: $R_{lijk} = R_{jkli}$,
- first Bianchi identity: $R_{l[ijk]} = 0$,
- second Bianchi identity: $\nabla_{[m} R_{li]jk} = 0$.

These reduce, on an $n$-manifold, the number of independent components
from $n^4$ to $\tfrac{1}{12}n^2(n^2-1)$.

## 3. Sectional Curvature

For two linearly independent $u, v \in T_pM$ the **sectional
curvature** of the plane spanned by $u, v$ is

$$K(u, v) = \frac{g\bigl(R(u,v)v, u\bigr)}{g(u,u)\,g(v,v) - g(u,v)^2}.$$

It generalises the Gaussian curvature of surfaces. Constant sectional
curvature characterises the three **model geometries**:

| Sectional curvature | Model space (dim. $n$)            | Geometry     |
|---------------------|-----------------------------------|--------------|
| $K \equiv +1$       | sphere $S^n$                      | spherical    |
| $K \equiv 0$        | Euclidean space $\mathbb{R}^n$    | flat         |
| $K \equiv -1$       | hyperbolic space $\mathbb{H}^n$   | hyperbolic   |

In dimension 3 constant sectional curvature is *not* the end of the
story – Thurston's classification recognises eight model geometries
(see [Act 1, Article 05](../topologie/05-geometrisierungs-vermutung.md)).

## 4. The Ricci Tensor

Tracing two indices of the curvature tensor produces the **Ricci
tensor**:

$$\mathrm{Ric}_{jk} = R^i{}_{jik} = g^{im}\,R_{mjik}.$$

Geometrically, $\mathrm{Ric}_p(v,v)$ is the *average sectional
curvature* of all 2-planes containing $v$. Pictorially: for a small
geodesic "trumpet" emanating in direction $v$, the Ricci tensor
measures how the infinitesimal volume element evolves along the
geodesics – positive Ricci pulls volumes together, negative Ricci
spreads them out.

> "The Ricci tensor measures the average way in which the volume
> element distorts as you move along a geodesic."
> — John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture* (2007), §1.2

The Ricci tensor is a symmetric $(0,2)$-tensor field – exactly the
shape that, when added to a metric, produces a metric variation. This
is what makes it suitable as the right-hand side of an evolution
equation for $g$.

## 5. Scalar Curvature

A further trace yields the **scalar curvature**:

$$R = g^{jk}\,\mathrm{Ric}_{jk}.$$

It is a smooth function on $M$. On the round $S^n$, $R = n(n-1)$; on
$\mathbb{R}^n$, $R = 0$; on $\mathbb{H}^n$, $R = -n(n-1)$. In
dimension 2, $R$ equals twice the Gaussian curvature and, via
Gauss–Bonnet, completely determines the topology of a closed surface.

## 6. The Special Role of Dimension 3

In dimension 3 the Riemann curvature tensor and the Ricci tensor have
the same number of independent components (six each). This implies a
key identity:

> **In dimension 3 the full curvature tensor $R$ is algebraically
> determined by the Ricci tensor and the metric.**

This is the very reason Hamilton's Ricci flow can be used for
classification in 3D: an evolution equation *for $\mathrm{Ric}$*
alone is enough to control the entire geometry. In higher dimensions
this reduction fails – the Weyl tensor remains, making the problem
substantially harder.

## 7. Volume and Diameter Comparison

Curvature bounds translate into geometric and topological
consequences.

- **Bonnet–Myers:** if $\mathrm{Ric} \ge (n-1) k\, g$ with $k > 0$,
  then $M$ is compact and $\mathrm{diam}(M) \le \pi/\sqrt{k}$.
- **Bishop–Gromov:** a lower bound on $\mathrm{Ric}$ gives an upper
  bound on the volume growth of geodesic balls.
- **Cheeger–Gromoll splitting:** if $\mathrm{Ric} \ge 0$ and $M$
  contains a complete geodesic line, then $M$ splits isometrically as
  $N \times \mathbb{R}$.

These comparison theorems are central tools in Perelman's analysis of
Ricci flow singularities.

## 8. Einstein Manifolds

A Riemannian manifold is **Einstein** if

$$\mathrm{Ric} = \lambda\, g \quad \text{for some } \lambda \in \mathbb{R}.$$

Such metrics are fixed points of the normalised Ricci flow (see
[Article 03](03-hamiltons-ricci-fluss.md)). The round sphere,
Euclidean space and hyperbolic space are Einstein, as are symmetric
spaces more generally. Finding Einstein metrics on a given manifold
is a research field in itself (Yamabe problem).

## 9. Towards the Flow

With Riemannian metric (Article 01), curvature tensor and Ricci
tensor in hand, all building blocks are in place to formulate the
evolution equation

$$\frac{\partial g}{\partial t} = -2\,\mathrm{Ric}(g)$$

and to analyse its action. That is the topic of the next article.

## Sources

- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer (2018), Ch. 7.
- Manfredo do Carmo, *Riemannian Geometry*, Birkhäuser (1992), Ch. 4–6.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS Clay Math. Monographs Vol. 3 (2007), §1–2.
- Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer (2016), Ch. 3 & 9.

## Cross References

- Previous article: [Riemannian metric](01-riemannsche-metrik.md)
- Next article: [Hamilton's Ricci flow](03-hamiltons-ricci-fluss.md)
- Act 1, Article 05: [Geometrisation conjecture](../topologie/05-geometrisierungs-vermutung.md)
