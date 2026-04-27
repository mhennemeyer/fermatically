---
title: "What Is Topology?"
slug: poincare/topologie/01-was-ist-topologie
series: poincare
part: 1
act: topologie
date: 2026-04-25
status: draft
lang: en
tags:
  - topology
  - intuition
---

# What Is Topology?

!!! abstract "Summary"
    Topology studies properties of geometric objects that are preserved
    under continuous deformation. Concepts such as *homeomorphism*,
    *continuity*, *connectedness* and *compactness* form the language in
    which Poincaré stated his conjecture in 1904.

## 1. Geometry without a ruler

Classical geometry measures lengths, angles and areas. Topology dispenses
with every metric. It asks: *Which properties of a space survive when one
stretches, squeezes or bends it arbitrarily – just without tearing or
gluing?*

The standard anecdote: to a topologist, a coffee cup and a doughnut are the
same object. Both surfaces have exactly one hole, and a continuous
deformation carries one into the other. A sphere, by contrast, has no hole
and is topologically distinct from cup and doughnut.

> "Topology is the study of those properties of geometric objects that
> remain unchanged under continuous deformations."
> — John M. Lee, *Introduction to Topological Manifolds* (2011), p. 1

## 2. Continuity as a basic notion

In analysis, continuity is familiar as the $\varepsilon$-$\delta$ property
of functions $\mathbb{R} \to \mathbb{R}$. Topologically it can be phrased
more generally: a map $f \colon X \to Y$ between two spaces is **continuous**
if the preimage of every open set is open.

This definition only needs the notion of *open set*. A **topological space**
is accordingly a set $X$ together with a system of distinguished subsets –
the open sets – satisfying three simple conditions: $\emptyset$ and $X$ are
open, arbitrary unions of open sets are open, and finite intersections of
open sets are open.

From this thin foundation all topological notions grow.

## 3. Homeomorphism – topological equality

When are two spaces topologically equal? When there is a **homeomorphism**
between them: a bijection $f \colon X \to Y$ such that $f$ and $f^{-1}$ are
both continuous.

$$
X \cong Y \quad :\Longleftrightarrow \quad
\exists\, f \colon X \to Y \text{ a homeomorphism.}
$$

- A sphere and the boundary of a cube are homeomorphic: both are closed
  two-dimensional surfaces without a hole.
- An open interval $(0,1)$ is homeomorphic to $\mathbb{R}$.
- A circle and a line segment are *not* homeomorphic: removing an interior
  point from the segment splits it into two pieces; removing a point from
  the circle leaves it connected.

The last example illustrates the typical proof technique: identify a
property preserved under homeomorphism – a **topological invariant** – and
use it to distinguish spaces.

## 4. Topological invariants

A topological invariant is a quantity or property that agrees on
homeomorphic spaces. Three of the most basic ones:

**Connectedness.** A space is connected if it cannot be split into two
disjoint non-empty open subsets. A circle is connected, a union of two
disjoint circles is not.

**Compactness.** This generalises the idea "closed and bounded" to arbitrary
topological spaces. A sphere is compact, a plane is not.

**Dimension.** Intuitively the number of independent directions. That it is
indeed an invariant – $\mathbb{R}^m$ is homeomorphic to $\mathbb{R}^n$ if
and only if $m = n$ – is a non-trivial result (Brouwer 1911) and one of the
founding achievements of algebraic topology.

Beyond these, algebraic invariants such as the **fundamental group** (see
[Article 03](03-sphaere-einfacher-zusammenhang.md)) and the **homology and
cohomology groups** provide finer information. They assign to each space an
algebraic structure that is preserved under homeomorphism.

## 5. A short history

**Euler (1736).** The **Königsberg bridge problem** and the
**polyhedron formula** $V - E + F = 2$ count as the first topological
results – statements about combinatorial structure, independent of size or
shape.

**Riemann (1857).** In his work on algebraic functions Riemann introduced
the **Riemann surfaces** named after him and classified closed surfaces by
their **genus** $g$ – the number of handles.

**Poincaré (1895–1904).** In *Analysis Situs* Henri Poincaré laid the
foundations of modern algebraic topology: fundamental group, homology, Betti
numbers, triangulation. The paper ends with the question now known as the
Poincaré Conjecture (see
[Article 04](04-was-ist-poincare-vermutung.md)).

**Hausdorff (1914).** With *Grundzüge der Mengenlehre* Felix Hausdorff
established the axiomatic definition of topological spaces in the form
still used today.

> "Henri Poincaré, more than any other person, is responsible for the
> emergence of topology as an independent branch of mathematics."
> — Allen Hatcher, *Algebraic Topology* (2002), preface

## 6. Why topology for Poincaré?

The Poincaré Conjecture is a purely topological statement: it says nothing
about lengths, angles or curvature, only about the *shape* of a
three-dimensional manifold (see
[Article 02](02-mannigfaltigkeiten.md)). Concretely, it asserts that a
closed 3-manifold in which every loop can be continuously contracted to a
point must be homeomorphic to the 3-sphere $S^3$.

Remarkable is the route the proof takes: Perelman and Hamilton translate
the topological question via Riemannian metrics and the Ricci flow into
differential geometry. The topological statement is obtained by controlling
geometry – a pattern shared with Wiles's proof of Fermat's Last Theorem.

## 7. What comes next

The following articles introduce, systematically, the topological notions
needed for the conjecture:

| Article | Topic |
|---------|-------|
| [02 – Manifolds](02-mannigfaltigkeiten.md) | Locally Euclidean spaces, dimension, closed vs. with boundary |
| [03 – The Sphere and Simple Connectedness](03-sphaere-einfacher-zusammenhang.md) | $S^n$, fundamental group, homotopy |
| [04 – What Is the Poincaré Conjecture?](04-was-ist-poincare-vermutung.md) | Original 1904, generalisation, higher dimensions |
| [05 – Thurston's Geometrization Conjecture](05-geometrisierungs-vermutung.md) | Eight model geometries, Thurston |

!!! tip "Background knowledge"
    For a refresher on open sets, continuity or convergence, the
    [Background Knowledge](../../vorwissen/index.md) section provides
    entry points to set theory and analysis.

---

## Sources

- **Allen Hatcher**: *Algebraic Topology*, Cambridge University Press (2002)
- **John M. Lee**: *Introduction to Topological Manifolds*, 2nd ed.,
  Springer (2011)
- **Henri Poincaré**: *Analysis Situs*, Journal de l'École Polytechnique 1
  (1895), 1–123
- **Felix Hausdorff**: *Grundzüge der Mengenlehre*, Veit & Comp., Leipzig
  (1914)
