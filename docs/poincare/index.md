---
title: "The Poincaré Conjecture – Perelman's Proof"
slug: poincare/index
series: poincare
date: 2026-04-25
status: active
lang: en
---
# The Poincaré Conjecture – The Path to the Proof

!!! abstract "Overview"
    Henri Poincaré posed a deceptively simple question about the three-dimensional sphere in 1904. A century later, Grigori Perelman delivered a proof in three arXiv preprints (2002–2003) that obtains the Poincaré Conjecture as a corollary of a much deeper statement: Thurston's Geometrization Conjecture. This article series traces the path – from topology through Hamilton's Ricci flow to Ricci flow with surgery.

## The Conjecture

**Poincaré Conjecture (1904).** Every closed, simply connected, three-dimensional manifold is homeomorphic to the 3-sphere \(S^3\).

In plain terms: if every loop in a three-dimensional space without boundary can be continuously contracted to a point, then that space is topologically nothing other than the surface of a four-dimensional ball. In dimensions \(n \geq 5\) the analogous statement was proved by Stephen Smale in 1961, in dimension 4 by Michael Freedman in 1982. The original conjecture in dimension 3 resisted every attempt until Perelman uploaded three preprints to arXiv in 2002–2003 and cracked the problem.

Perelman's proof builds on a programme initiated by Richard Hamilton: the **Ricci flow**, a differential equation that "smooths" a Riemannian metric like a heat equation. Hamilton had shown how the flow works in favourable cases but could not control its singularities. Perelman supplied the missing analytic tools – entropy functionals, the \(\kappa\)-non-collapsing theorem, canonical neighbourhoods – and a surgery procedure that removes singularities in a controlled way and continues the flow.

---

## Three Acts

### 🌐 Act 1: Topology and the Conjecture

What exactly is being claimed? The first act sets up the language of topology and presents Thurston's Geometrization Conjecture as the larger picture in which Poincaré is merely a special case.

| # | Article | Topic |
|---|---------|-------|
| 1 | [What Is Topology?](topologie/01-was-ist-topologie.md) | Continuous deformation, homeomorphism, topological invariants |
| 2 | [Manifolds](topologie/02-mannigfaltigkeiten.md) | Locally Euclidean spaces, dimension, closed vs. with boundary |
| 3 | [The Sphere and Simple Connectedness](topologie/03-sphaere-einfacher-zusammenhang.md) | \(S^n\), fundamental group, homotopy |
| 4 | [What Is the Poincaré Conjecture?](topologie/04-was-ist-poincare-vermutung.md) | Original 1904, generalisation, higher dimensions |
| 5 | [Thurston's Geometrization Conjecture](topologie/05-geometrisierungs-vermutung.md) | Eight model geometries, decomposition of 3-manifolds |

→ [Act 1 overview](topologie/index.md)

### 🌊 Act 2: Tools – Ricci Flow and Geometric Analysis

Before the proof comes the differential equation that drives the whole machinery. Hamilton's Ricci flow and Perelman's extensions are developed self-contained here; the third act references them.

| # | Article | Topic |
|---|---------|-------|
| 1 | [Riemannian Metric](ricci-fluss/01-riemannsche-metrik.md) | Measuring lengths and angles on manifolds |
| 2 | [Curvature and the Ricci Tensor](ricci-fluss/02-kruemmung-ricci-tensor.md) | Sectional, Ricci and scalar curvature |
| 3 | [Hamilton's Ricci Flow](ricci-fluss/03-hamiltons-ricci-fluss.md) | \(\partial_t g_{ij} = -2 R_{ij}\) as a heat-type equation |
| 4 | [Singularities and Blow-up Limits](ricci-fluss/04-singularitaeten-blowup.md) | How the flow breaks down and what one reads from it |
| 5 | [Perelman's Entropy Functionals](ricci-fluss/05-perelman-entropie.md) | \(\mathcal{F}\), \(\mathcal{W}\) and their monotonicity |
| 6 | [κ-Non-Collapsing and Canonical Neighbourhoods](ricci-fluss/06-kappa-nichtkollaps.md) | Volume control, local models |
| 7 | [Reduced Length and Reduced Volume](ricci-fluss/07-reduzierte-laenge.md) | Perelman's \(\mathcal{L}\)-geometry |

→ [Act 2 overview](ricci-fluss/index.md)

### 🏔️ Act 3: The Proof – Ricci Flow with Surgery

How the tools become a proof: singularity analysis in dimension 3, controlled surgery, long-time behaviour, and finally the two routes to the Poincaré Conjecture.

| # | Article | Topic |
|---|---------|-------|
| 1 | [Hamilton's Programme and Its Obstacles](beweis/01-hamiltons-programm.md) | What worked, what was missing |
| 2 | [Singularity Analysis in Dimension 3](beweis/02-singularitaeten-dim3.md) | \(\kappa\)-solutions and their classification |
| 3 | [Ricci Flow with Surgery](beweis/03-chirurgie.md) | Neck surgeries, the surgery procedure |
| 4 | [Long-Time Behaviour and the Thin–Thick Decomposition](beweis/04-long-time-verhalten.md) | Asymptotics, hyperbolic and graph pieces |
| 5 | [Finite Extinction Time](beweis/05-endliche-extinktion.md) | The shortcut via arXiv:math/0307245 |
| 6 | [Geometrization Implies Poincaré](beweis/06-poincare-aus-geometrisierung.md) | How the corollary follows from the general result |

→ [Act 3 overview](beweis/index.md)

---

## Recommended Order

The acts build on each other. The recommended path:

1. **Topology** (Act 1) – as an entry point into the vocabulary.
2. **Ricci flow** (Act 2) – the analytic machinery, readable on its own.
3. **The proof** (Act 3) – strictly in order.

!!! tip "Background Knowledge"
    For the Riemannian geometry and partial differential equations Act 2 relies on, see the "Geometry and Analysis (Advanced)" block in the [Background Knowledge](../vorwissen/index.md) section. Articles there are linked from the storyline whenever they are needed.

!!! info "Relation to Fermat/Wiles"
    The Poincaré storyline can be read independently of [Fermat's Last Theorem](../flt-overview.md). Both proofs share a pattern, however: a number-theoretic or topological statement is obtained via a deeper structure (modularity or geometrization, respectively) that carries the main work.

---

## Sources

**Perelman's original papers (all freely available on arXiv).**

- Perelman, G. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:[math/0211159](https://arxiv.org/abs/math/0211159), 11 November 2002.
- Perelman, G. *Ricci flow with surgery on three-manifolds.* arXiv:[math/0303109](https://arxiv.org/abs/math/0303109), 10 March 2003.
- Perelman, G. *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds.* arXiv:[math/0307245](https://arxiv.org/abs/math/0307245), 17 July 2003.

**Expositions and textbooks.**

- Morgan, J.; Tian, G. *Ricci Flow and the Poincaré Conjecture.* Clay Mathematics Monographs 3, AMS 2007.
- Kleiner, B.; Lott, J. *Notes on Perelman's papers.* Geometry & Topology 12 (2008), 2587–2855.
- Cao, H.-D.; Zhu, X.-P. *A Complete Proof of the Poincaré and Geometrization Conjectures – Application of the Hamilton-Perelman Theory of the Ricci Flow.* Asian Journal of Mathematics 10 (2006), 165–492.
- Hamilton, R. S. *Three-manifolds with positive Ricci curvature.* Journal of Differential Geometry 17 (1982), 255–306.

**Popular science.**

- O'Shea, D. *The Poincaré Conjecture: In Search of the Shape of the Universe.* Walker & Company 2007.
