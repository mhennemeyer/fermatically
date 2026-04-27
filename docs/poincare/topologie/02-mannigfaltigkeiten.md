---
title: "Manifolds"
slug: poincare/topologie/02-mannigfaltigkeiten
series: poincare
part: 2
act: topologie
date: 2026-04-25
status: draft
lang: en
tags:
  - topology
  - manifold
---

# Manifolds

!!! abstract "Summary"
    A manifold is a space that locally looks like Euclidean space
    $\mathbb{R}^n$ but may be globally complicated. The notion is the
    proper generalisation of "curve" and "surface" to arbitrary
    dimensions and is the kind of object the Poincaré Conjecture talks
    about.

## 1. Locally Euclidean – the basic idea

Up close, a circle looks like a piece of a line, and a sphere looks like a
piece of a plane. This local agreement with Euclidean space makes such
objects tractable: in the small one may compute as in $\mathbb{R}^n$, while
the topology controls global behaviour.

The formal definition:

> A Hausdorff space $M$ is an **$n$-dimensional topological manifold** if
> every point $p \in M$ has an open neighbourhood $U$ that is homeomorphic
> to an open subset of $\mathbb{R}^n$.

Such a homeomorphism $\varphi \colon U \to \varphi(U) \subseteq \mathbb{R}^n$
is called a **chart**, a family of charts covering all of $M$ an **atlas**.
The terminology comes directly from cartography: the surface of the Earth
– a 2-manifold – is described by finitely many flat charts.

> "A manifold is a topological space that locally looks like Euclidean
> space."
> — John M. Lee, *Introduction to Smooth Manifolds* (2013), p. 1

## 2. Examples in low dimensions

**Dimension 1.** The only connected closed 1-manifolds without boundary are
the circle $S^1$ and the line $\mathbb{R}$. Other examples: open and
half-open intervals.

**Dimension 2.** Closed surfaces are classified by two pieces of data: the
**genus** $g$ (number of handles) and orientability. Orientable
representatives are the sphere $S^2$ ($g = 0$), the torus
$T^2 = S^1 \times S^1$ ($g = 1$), the genus-2 surface, and so on.
Non-orientable examples are the projective plane $\mathbb{RP}^2$ and the
Klein bottle.

**Dimension 3.** Classification here is far harder and is the subject of
the Geometrization Conjecture (see
[Article 05](05-geometrisierungs-vermutung.md)). The simplest examples are
the 3-sphere $S^3$, the 3-torus $T^3 = S^1 \times S^1 \times S^1$, and
$S^2 \times S^1$.

## 3. Closed, open, with boundary

Three adjectives appear in every discussion of manifolds:

**Closed.** A manifold is **closed** if it is compact and has no boundary.
Sphere, torus and projective plane are closed; the open plane $\mathbb{R}^2$
is not. Important: in topology "closed" is *not* the opposite of "open" as
for subsets.

**Open.** In the context of manifolds, *open* usually means "non-compact and
without boundary" – e.g. $\mathbb{R}^n$ or an open half-plane.

**With boundary.** An $n$-manifold *with boundary* additionally allows
charts whose image lies in the closed half-space
$\{x \in \mathbb{R}^n : x_n \geq 0\}$. The boundary $\partial M$ is itself
a closed $(n-1)$-manifold. Example: the closed ball $D^3$ is a 3-manifold
with boundary $\partial D^3 = S^2$.

The Poincaré Conjecture concerns **closed** 3-manifolds.

## 4. Smooth manifolds

On a topological manifold one can define notions like "continuity" and
"homeomorphism", but not yet differentiation. For that one needs an extra
structure:

> An atlas is **smooth** ($C^\infty$) if all **transition maps**
> $\varphi_j \circ \varphi_i^{-1}$ – homeomorphisms between open subsets of
> $\mathbb{R}^n$ – are infinitely differentiable. A **smooth manifold** is
> a topological manifold equipped with a maximal smooth atlas.

On a smooth manifold one can speak of smooth functions $f \colon M \to
\mathbb{R}$, smooth maps $M \to N$, and **diffeomorphisms** –
homeomorphisms whose inverses are also smooth. Diffeomorphism is the
natural equivalence for smooth manifolds.

The relation between topological and smooth classification is subtle:

- In dimension $\leq 3$ every topological manifold has a unique smooth
  structure (Moise 1952).
- In dimension 4 there exist versions of $\mathbb{R}^4$ that are
  homeomorphic but not diffeomorphic to standard $\mathbb{R}^4$ – a
  discovery of Donaldson (1983) and Freedman.
- In dimension 7 Milnor (1956) found seven pairwise non-diffeomorphic
  smooth structures on the topological 7-sphere – the famous
  **exotic spheres**.

For the Poincaré Conjecture in dimension 3 this distinction is irrelevant:
topological and smooth coincide. Perelman's proof nevertheless works in the
smooth category, because the Ricci flow is a differential equation for
smooth Riemannian metrics.

## 5. Riemannian manifolds

A smooth manifold supports differentiation but not yet measurement. A
**Riemannian metric** $g$ assigns to each point $p \in M$ an inner product
$g_p$ on the tangent space $T_pM$, depending smoothly on $p$. With it one
can define lengths of curves, angles, volumes, and – via the curvature
tensor – the local geometry.

A **Riemannian manifold** $(M, g)$ is the central stage of Act 2 of the
Poincaré storyline: Hamilton's Ricci flow
$\partial_t g_{ij} = -2 R_{ij}$ is precisely an evolution equation for such
metrics (see [Act 2](../ricci-fluss/index.md)).

Important for understanding the conjecture: *which* Riemannian metric one
chooses on a manifold is topologically irrelevant – the conjecture is a
statement about the manifold, not about the metric. In the proof, however,
a metric is chosen on purpose, its evolution under the Ricci flow is
controlled, and a topological conclusion is drawn at the end.

## 6. Examples for the storyline

Three manifolds appear repeatedly in the Poincaré discussion:

**The 3-sphere $S^3$.** Definable as
$\{x \in \mathbb{R}^4 : \|x\| = 1\}$ or, dually, as the one-point
compactification of $\mathbb{R}^3$. It is the only closed simply connected
3-manifold – this is precisely the Poincaré Conjecture.

**The 3-torus $T^3$.** The product $S^1 \times S^1 \times S^1$,
intuitively a cube with opposite faces identified. Closed but not simply
connected; its fundamental group is $\mathbb{Z}^3$.

**Lens spaces $L(p,q)$.** Quotients of the 3-sphere $S^3$ under a free
action of a finite cyclic group $\mathbb{Z}/p$. They provide examples of
closed 3-manifolds with finite fundamental group – topologically
non-trivial, in the sense of the conjecture "not simply connected".

## 7. What comes next

The next article introduces the notions of **loop**, **homotopy** and
**fundamental group** and examines the $n$-dimensional sphere $S^n$ in
greater detail. Only then can one say precisely what *simply connected*
means and why this property singles out the 3-sphere among all closed
3-manifolds.

| Article | Topic |
|---------|-------|
| [03 – The Sphere and Simple Connectedness](03-sphaere-einfacher-zusammenhang.md) | $S^n$, fundamental group, homotopy |
| [04 – What Is the Poincaré Conjecture?](04-was-ist-poincare-vermutung.md) | Original formulation 1904 |

!!! tip "Background knowledge"
    Tangent spaces, tensors and curvature are prepared informally in the
    [Background Knowledge](../../vorwissen/index.md) block "Geometry and
    Analysis (Advanced)". For this article the picture "locally like
    $\mathbb{R}^n$" suffices.

---

## Sources

- **John M. Lee**: *Introduction to Topological Manifolds*, 2nd ed.,
  Springer (2011)
- **John M. Lee**: *Introduction to Smooth Manifolds*, 2nd ed.,
  Springer (2013)
- **John Milnor**: *On manifolds homeomorphic to the 7-sphere*, Annals of
  Mathematics 64 (1956), 399–405
- **Edwin E. Moise**: *Affine structures in 3-manifolds. V. The
  triangulation theorem and Hauptvermutung*, Annals of Mathematics 56
  (1952), 96–114
