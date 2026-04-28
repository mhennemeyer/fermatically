---
title: "Manifolds – an Intuitive View"
slug: vorwissen/geometrie-analysis/mannigfaltigkeit-anschaulich
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: en
tags:
  - mannigfaltigkeit
  - intuition
---

# Manifolds – an Intuitive View

> *"A manifold is a space that looks like the familiar $\mathbb{R}^n$ near
> every point – yet may be something altogether different globally."*

The Earth's surface is – roughly – a sphere $S^2$. Anyone drawing a
city map flattens it locally to a piece of $\mathbb{R}^2$. Glueing
several such city maps together yields an atlas. Exactly this picture
– locally like $\mathbb{R}^n$, glued globally by compatible charts –
is the notion of a **manifold**.

## 1. The local promise

A **topological space** $M$ is called an $n$-dimensional **topological
manifold** if every point $p \in M$ has an open neighbourhood
$U \subset M$ that is *homeomorphic* to an open subset of
$\mathbb{R}^n$. The associated map
$$
\varphi : U \to V \subset \mathbb{R}^n
$$
is called a **chart**. A family of charts whose domains cover $M$ is
called an **atlas**.

Additional technical requirements (Hausdorff, second countable) are
almost always satisfied and silently assumed here.

## 2. Smoothly compatible charts

Wherever two charts $\varphi : U \to V$ and $\psi : U' \to V'$ overlap
there is a **transition map**
$$
\psi \circ \varphi^{-1} : \varphi(U \cap U') \to \psi(U \cap U').
$$
This is a map between open subsets of $\mathbb{R}^n$. If we require all
transition maps to be **smooth** ($C^\infty$), $M$ is called a
**smooth manifold**.

Smoothness is the minimal requirement for notions like
*differentiability*, *tangent space*, or *curvature* to be defined at
all – independently of which chart one chooses.

## 3. Examples

| Manifold | Dimension | Description |
|----------|-----------|-------------|
| $\mathbb{R}^n$ | $n$ | Trivial case, one chart suffices. |
| Circle $S^1$ | 1 | Two charts (two overlapping arcs). |
| Sphere $S^2$ | 2 | Standard atlas: stereographic projection from north and south pole. |
| Torus $T^2$ | 2 | Square $[0,1]^2$ with opposite sides identified. |
| Möbius strip | 2 | non-orientable, has boundary. |
| Real projective space $\mathbb{RP}^n$ | $n$ | $S^n$ with antipodal identification. |

The first three examples are compact and boundaryless – exactly the
class for which the [Poincaré conjecture](../../poincare/topologie/04-was-ist-poincare-vermutung.md)
is formulated.

## 4. What a manifold is *not*

By definition a manifold has no *self-intersections*, *cusps*, or
*edges*: at every point it looks like a piece of $\mathbb{R}^n$. The
double cone $\{x^2 + y^2 = z^2\}$ is not a manifold at the apex
$(0,0,0)$; a cube fails to be one along its edges and corners.
*Topological* manifolds may not contain such singularities – but they
*do* arise during the Ricci flow's evolution, which is precisely what
Perelman's surgery has to repair.

## 5. Orientability, boundary, compactness

Three properties recur throughout the Poincaré storyline:

- **Orientability:** there is a globally consistent sense of rotation.
  $S^2$ and $T^2$ are orientable, the Möbius strip is not.
- **Boundary:** a manifold *with boundary* admits charts into the
  half-space $\mathbb{R}^n_{\ge 0}$. The boundary $\partial M$ itself
  is a manifold of dimension $n - 1$.
- **Compactness:** closed and bounded. The Poincaré conjecture
  concerns *closed, simply connected* 3-manifolds.

## 6. Why the notion is so powerful

On a manifold one can – via charts – locally apply every concept of
analysis: functions, vector fields, differential forms, integrals,
differential equations. Chart compatibility ensures that different
charts produce the same result – the notions are *intrinsic*. This is
the technical prerequisite for defining a Riemannian metric (see
[Tangent Space and Tensors](tangentialraum-tensoren.md)) and hence
curvature on $M$.

## Cross-references

- Continue with: [Tangent Space and Tensors](tangentialraum-tensoren.md), [Curvature of Surfaces](kruemmung-flaechen-gauss.md).
- Application in the storyline: [Act 1, Manifolds](../../poincare/topologie/02-mannigfaltigkeiten.md), [Act 1, Sphere & simple connectivity](../../poincare/topologie/03-sphaere-einfacher-zusammenhang.md).

## Sources

- Lee, John M. (2013). *Introduction to Smooth Manifolds.* Springer GTM 218, 2nd ed. Ch. 1–2.
- Tu, Loring W. (2011). *An Introduction to Manifolds.* Springer Universitext. Ch. 5–6.
- Spivak, Michael (1999). *A Comprehensive Introduction to Differential Geometry, Vol. 1.* Publish or Perish, 3rd ed.
