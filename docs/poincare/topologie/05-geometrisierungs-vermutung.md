---
title: "Thurston's Geometrization Conjecture"
slug: poincare/topologie/05-geometrisierungs-vermutung
series: poincare
part: 5
act: topologie
date: 2026-04-25
status: draft
lang: en
tags:
  - thurston
  - geometrization
  - 3-manifolds
---

# Thurston's Geometrization Conjecture

!!! abstract "Summary"
    In 1982 William Thurston generalised the Poincaré Conjecture to a
    full classification statement for closed 3-manifolds: every such
    manifold can be cut canonically into pieces, each carrying one of
    **eight model geometries**. Perelman's proof concerns this
    geometrization conjecture; the Poincaré Conjecture follows as a
    special case.

## 1. From classifying surfaces to dimension 3

In dimension 2 the classification of closed surfaces is classical. The
**uniformisation theorem** (Klein, Poincaré, Koebe, 1907) sharpens it
geometrically: every closed surface admits a Riemannian metric of
constant curvature – spherical ($K = +1$), Euclidean ($K = 0$), or
hyperbolic ($K = -1$).

| Genus $g$ | Curvature | Model geometry |
|-----------|-----------|----------------|
| $0$ ($S^2$) | $+1$ | spherical $S^2$ |
| $1$ ($T^2$) | $0$ | Euclidean $\mathbb{E}^2$ |
| $\geq 2$ | $-1$ | hyperbolic $\mathbb{H}^2$ |

Can this geometric classification be carried over to dimension 3? The
answer is subtle – three constant curvatures do not suffice.

## 2. The eight model geometries

Thurston showed in 1982: a **maximal, simply connected, homogeneous
Riemannian 3-manifold** with compact stabiliser falls into exactly
eight isomorphism classes – the **eight Thurston geometries**:

| # | Geometry | Curvature | Example manifold |
|---|----------|-----------|------------------|
| 1 | $S^3$ – spherical | $+1$ | $S^3$, lens spaces, Poincaré homology sphere |
| 2 | $\mathbb{E}^3$ – Euclidean | $0$ | 3-torus $T^3$, Bieberbach manifolds |
| 3 | $\mathbb{H}^3$ – hyperbolic | $-1$ | "most" 3-manifolds |
| 4 | $S^2 \times \mathbb{R}$ | mixed | $S^2 \times S^1$ |
| 5 | $\mathbb{H}^2 \times \mathbb{R}$ | mixed | products with surfaces $g \geq 2$ |
| 6 | $\widetilde{\mathrm{SL}}_2(\mathbb{R})$ | negative | unit tangent bundles of hyperbolic surfaces |
| 7 | Nil | nilpotent | Heisenberg quotients |
| 8 | Sol | solvable | torus bundles over $S^1$ with Anosov monodromy |

Three of them have *constant* curvature ($S^3, \mathbb{E}^3, \mathbb{H}^3$),
two are products, and the remaining three are Lie groups with
left-invariant metrics. Exactly this list – no more, no less –
exhausts all homogeneous 3-geometries.

> "We may divide the geometries of three-manifolds into eight types."
> — William P. Thurston, *Three-dimensional manifolds, Kleinian
> groups and hyperbolic geometry*, BAMS (1982)

## 3. The Geometrization Conjecture

In 1982 Thurston dared to conjecture that these eight geometries
suffice to describe *every* closed 3-manifold – after a suitable
decomposition:

> **Geometrization Conjecture (Thurston, 1982).** Every closed,
> orientable 3-manifold can be cut canonically into pieces, each of
> which admits a complete, locally homogeneous Riemannian metric from
> one of the eight Thurston geometries.

The decomposition proceeds in two steps, each classical in its own
right:

1. **Prime decomposition** (Kneser 1929, Milnor 1962). Along
   embedded 2-spheres $M$ decomposes uniquely into a connected sum
   $M = M_1 \# M_2 \# \cdots \# M_k$ of **prime** pieces that admit
   no further spherical decomposition.
2. **JSJ decomposition** (Jaco–Shalen 1979, Johannson 1979). Along
   embedded tori one cuts each prime piece further until only
   **atoroidal** pieces remain.

Thurston's conjecture adds: every resulting piece carries exactly one
of the eight geometric structures.

## 4. Poincaré as a corollary

Apply the conjecture to a closed, simply connected 3-manifold $M$, and
one can rule out, step by step, which geometries are possible:

- $\pi_1(M) = 0$ is finite. This excludes $\mathbb{E}^3$,
  $\mathbb{H}^3$, $\mathbb{H}^2 \times \mathbb{R}$,
  $\widetilde{\mathrm{SL}}_2$, Nil and Sol, all of which have infinite
  fundamental groups.
- $S^2 \times \mathbb{R}$ is also ruled out because its quotients have
  infinite $\pi_1$ ($\mathbb{Z}$) or $\mathbb{Z}/2$.
- In the prime decomposition $M = M_1$, since a connected sum
  $M_1 \# M_2$ with both summands $\neq S^3$ would always have
  nontrivial $\pi_1$ (van Kampen).

Only the **spherical geometry** remains: $M$ is a quotient
$S^3 / \Gamma$ by a finite free group action. The only action with
trivial group is the trivial one: $\Gamma = \{1\}$, so $M \cong S^3$.
That is the Poincaré Conjecture.

> "The Poincaré Conjecture is a special case of Thurston's
> Geometrization Conjecture."
> — John W. Morgan, Gang Tian, *Ricci Flow and the Poincaré
> Conjecture* (2007), p. 4

## 5. Hyperbolic is generic

Thurston himself proved large parts of his conjecture: for **Haken
manifolds** – a technical but broad class containing many knot
complements – he established the **hyperbolisation theorem**:
atoroidal Haken manifolds are hyperbolic. A striking empirical picture
emerged: among 3-manifolds the hyperbolic geometry is the *generic*
one; the other seven appear as special cases in which symmetry or
fibre structure obstructs hyperbolicity.

## 6. What Perelman proved

Perelman's three arXiv preprints supply the proof of the full
geometrization conjecture. The strategy is analytic, not topological:

1. **Start the Ricci flow.** Choose any Riemannian initial metric
   $g_0$ on $M$ and run the Ricci flow
   $\partial_t g = -2 \mathrm{Ric}(g)$ (see
   [Act 2](../ricci-fluss/index.md)).
2. **Classify singularities.** Whenever singularities occur,
   Perelman's classification of $\kappa$-solutions shows that they
   are locally of a few model types (necks, caps).
3. **Perform surgery.** Necks are excised, caps glued in; the flow
   continues on a modified manifold (see
   [Act 3](../beweis/index.md)).
4. **Analyse long-time behaviour.** As $t \to \infty$ the manifold
   splits into a **thick** part (hyperbolic, $\mathbb{H}^3$-pieces)
   and a **thin** part (locally collapsed, a graph manifold built
   from the other geometries).
5. **Read off the geometrization.** From the thick/thin split the
   geometric structure of each piece follows.

In the simply connected special case (Poincaré) the proof can be
shortened: the third Perelman paper (arXiv:math/0307245) shows
**finite extinction time** – the flow collapses completely in finite
time, which is possible only for $S^3$. This **shortcut** bypasses
the full geometrization machinery.

## 7. Significance for topology

With Thurston's conjecture – now a **theorem** – the classification of
closed 3-manifolds is effectively complete. Every such manifold is
described by its prime decomposition, its JSJ decomposition and the
geometric structure of each piece. The topology of dimension 3 thereby
leaves the status of a "miscellany of constructions" and is – as in
dimension 2 – structured by geometry.

## 8. Outlook

Act 1 is now complete. What is being claimed, what the conjecture is,
and why it was hard – all of that is in place. **Act 2** builds the
machinery that drives the proof: Riemannian metric, curvature tensors,
Hamilton's Ricci flow, Perelman's entropy functionals.

| Act | Topic |
|-----|-------|
| [Act 2 – Tools: Ricci Flow](../ricci-fluss/index.md) | A differential equation for metrics |
| [Act 3 – The Proof: Ricci Flow with Surgery](../beweis/index.md) | Singularity analysis, surgery, geometrization |

---

## Sources

- **William P. Thurston**: *Three-dimensional manifolds, Kleinian
  groups and hyperbolic geometry*, Bulletin of the American
  Mathematical Society 6 (1982), 357–381
- **William P. Thurston**: *Three-Dimensional Geometry and Topology,
  Volume 1*, Princeton University Press (1997)
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007), Chapter 1
- **Peter Scott**: *The geometries of 3-manifolds*, Bulletin of the
  London Mathematical Society 15 (1983), 401–487 – the canonical
  survey of the eight geometries
- **Hellmuth Kneser**: *Geschlossene Flächen in dreidimensionalen
  Mannigfaltigkeiten*, Jahresbericht DMV 38 (1929), 248–260 – prime
  decomposition
