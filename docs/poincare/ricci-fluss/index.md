---
title: "Tools: Ricci Flow"
slug: poincare/ricci-fluss/index
series: poincare
date: 2026-04-27
status: active
lang: en
---

# Tools: Ricci Flow

!!! abstract "What the second act is about"
    Act 1 explained **what** has to be shown: every simply
    connected closed 3-manifold is homeomorphic to $S^3$ – and more
    generally, every closed 3-manifold can be canonically
    decomposed into geometric pieces (Geometrization). Act 2 builds
    the analytic machinery that **does** the work: Hamilton's
    **Ricci flow** and its **refinement by Perelman** – entropy
    functionals, $\kappa$-non-collapsing, canonical neighborhoods,
    and reduced length.

## The Idea in One Sentence

Hamilton's Ricci flow
$$
\partial_t g_{ij} = -2\,R_{ij}
$$
is a geometric heat equation for the metric itself: curvature is
averaged out, high-curvature regions become smoother, and ideally
the flow converges to a particularly symmetric ("geometric")
limit metric. The difficulty is not the definition but the
**singularities**: localized places where curvature blows up in
finite time. Act 2 explains how Perelman classified these
singularities precisely – the preparation for *surgery* in Act 3.

## The Seven Articles

| # | Article | What it covers |
|---|---------|----------------|
| 1 | [Riemannian Metric](01-riemannsche-metrik.md) | Language and models: $\mathbb{R}^n$, $S^n$, $\mathbb{H}^n$, Levi-Civita, geodesics |
| 2 | [Curvature and the Ricci Tensor](02-kruemmung-ricci-tensor.md) | Riemann, sectional, Ricci, scalar curvature; comparison geometry |
| 3 | [Hamilton's Ricci Flow](03-hamiltons-ricci-fluss.md) | Definition, heat-equation heuristic, Hamilton's 1982 theorem, DeTurck |
| 4 | [Singularities and Blow-up Limits](04-singularitaeten-blowup.md) | Type I/II/III, neckpinch, parabolic rescaling, ancient $\kappa$-solutions |
| 5 | [Perelman's Entropy Functionals](05-perelman-entropie.md) | $\mathcal{F}$, $\mathcal{W}$, $\mu$/$\nu$, monotonicity, gradient-flow structure |
| 6 | [κ-Non-collapsing and Canonical Neighborhoods](06-kappa-nichtkollaps.md) | volume bound, classification of ancient $\kappa$-solutions, neck/cap/space form |
| 7 | [Reduced Length and Reduced Volume](07-reduzierte-laenge.md) | $\mathcal{L}$-geometry, $\ell$, $\tilde V$, local $\kappa$-non-collapsing, blow-up convergence |

The first two articles are pure language preparation; readers
familiar with Lee's *Introduction to Riemannian Manifolds* can
skim them. Article 3 is the historical entry point (Hamilton
1982). From Article 4 onwards Perelman's program begins, peaking
in Article 7.

## Logical Flow

```
01 Metric   ──►  02 Curvature ──►  03 Hamilton flow
                                         │
                                         ▼
                                04 Singularities / Blow-up
                                         │
                       ┌─────────────────┼─────────────────┐
                       ▼                 ▼                 ▼
                  05 Entropy        06 κ-Non-collapsing  07 Reduced length
                       │                 │                 │
                       └─────────────────┼─────────────────┘
                                         ▼
                                Act 3: Surgery + proof
```

Articles 5–7 are mutually intertwined: $\mathcal{W}$ and
$\tilde V$ are both Lyapunov quantities and each independently
imply $\kappa$-non-collapsing; reduced length is moreover the
actual vehicle for blow-up convergence and hence for the
existence of canonical neighborhoods.

## Prerequisites

For Act 2 the following topics from the
[prerequisites section](../../vorwissen/index.md) are useful:

- Riemannian geometry (metric, curvature, geodesics)
- Differential geometry on manifolds
- PDEs, especially the heat equation and parabolic rescaling
- Tensor calculus and index notation

Readers new to this language are best served by starting with
Article 01 and skipping the more formal identities in Article 02
on first reading.

## Transition to Act 3

With entropy, $\kappa$-non-collapsing, canonical neighborhoods,
and reduced length, the analytic machinery is complete. Act 3
([The Proof](../beweis/index.md)) uses it to:

- construct **Ricci flow with surgery**,
- prove the *continuity of the topological consequences* under
  surgery,
- establish **finite extinction time** for simply connected
  3-manifolds,
- and from this deduce the
  [Poincaré conjecture](../topologie/04-was-ist-poincare-vermutung.md)
  and
  [geometrization](../topologie/05-geometrisierungs-vermutung.md).
