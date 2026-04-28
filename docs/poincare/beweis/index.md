---
title: "The Proof"
slug: poincare/beweis/index
series: poincare
date: 2026-04-28
status: active
lang: en
---

# The Proof

!!! abstract "What this third act is about"
    Act 1 explained **what** has to be shown (the Poincaré and
    geometrization conjectures in dim 3). Act 2 supplied the analytic
    and geometric **tools**: Ricci flow, Perelman entropy,
    $\kappa$-non-collapse, canonical neighborhoods, reduced length.
    Act 3 puts them together. Six articles run from Hamilton's original
    program and its five obstacles through singularity analysis,
    surgery, and long-time behavior to the Poincaré conjecture as a
    topological corollary.

## The idea in one sentence

Hamilton's vision in 1982 was: *let Ricci flow run until the manifold
takes a canonical form – and read off the topology.* Perelman shows
this **literally works**, provided one (a) classifies the singularities,
(b) cuts them out by **surgery**, and (c) reads the asymptotic picture
at $t \to \infty$ correctly.

## The six articles

| # | Article | What it covers |
|---|---------|----------------|
| 01 | [Hamilton's program and its obstacles](01-hamiltons-programm.md) | Hamilton's four-step vision (1982–1997); five structural obstacles H1–H5; tool-mapping Hamilton ↔ Perelman; act roadmap. |
| 02 | [Singularity analysis in dimension 3](02-singularitaeten-dim3.md) | Hamilton–Ivey pinching; classification of ancient $\kappa$-solutions (cylinder, $S^3/\Gamma$, Bryant model); canonical-neighborhood theorem. |
| 03 | [Ricci flow with surgery](03-chirurgie.md) | $\delta$-necks, standard solution on $\mathbb{R}^3$, surgery algorithm with parameter sequences $(\varepsilon_i, \delta_i, r_i, h_i)$, surgery theorem 0303109 §5. |
| 04 | [Long-time behavior and thin–thick decomposition](04-long-time-verhalten.md) | rescaled metric $\hat g = g/(4t)$; persistent hyperbolic pieces + JSJ tori; collapsing theorem; full geometrization. |
| 05 | [Finite extinction time](05-endliche-extinktion.md) | Perelman 0307245: $W_2$/$W_3$ monotonicity via Gauss–Bonnet; finite extinction for simply connected $M$ as a shortcut. |
| 06 | [Geometrization implies Poincaré](06-poincare-aus-geometrisierung.md) | Closing topological argument: prime decomposition + Van Kampen + spherical space forms ⇒ $M \cong S^3$. |

## Logic of the proof

```
                     Hamilton's program (1982)
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   Singularity analysis (02)         Perelman tools from Act 2
              │                      (entropy, κ, reduction)
              └───────────────┬───────────────┘
                              ▼
                  Ricci flow with surgery (03)
                       solution on [0, ∞)
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        long-time limit (04)        finite extinction (05)
        thin–thick → 8 geom.        π₁ = 0 ⇒ T < ∞
                │                           │
                └─────────────┬─────────────┘
                              ▼
              geometrization ⇒ Poincaré (06)
                          M ≅ S³
```

## Where each obstacle is resolved

| Obstacle (Article 01) | Resolved in |
|-----------------------|-------------|
| H1 classify singularities | 02 (canonical neighborhoods) |
| H2 remove singularities by surgery | 03 (surgery theorem) |
| H3 rule out infinite surgery accumulation | 03 (discrete parameter sequences) and 05 (finite extinction) |
| H4 asymptotic picture at $t \to \infty$ | 04 (thin–thick + collapsing theorem) |
| H5 read topology off the geometry | 06 (prime decomposition + spherical space forms) |

## Prerequisites

For this act the toolkit from
[Act 2 (Ricci flow)](../ricci-fluss/index.md) should be available, in
particular [$\kappa$-non-collapse](../ricci-fluss/06-kappa-nichtkollaps.md)
and [reduced length](../ricci-fluss/07-reduzierte-laenge.md).
Topologically the contents of
[Act 1](../topologie/index.md) (manifold, simply connected, geometrization
conjecture) suffice.

## What lies beyond Act 3

With Article 06 the Poincaré conjecture is fully proved in dimension 3.
However, related questions remain, which the proof does *not* directly
answer:

- **Smooth 4-dim Poincaré conjecture:** open.
- **Effective bounds** on the number of surgeries depending on the
  initial geometry: largely open (cf. Bamler 2018).
- **Ricci flow in higher dimensions:** Hamilton-style singularities are
  not fully classified in dim $\ge 4$ (Brendle 2020; Bamler 2020).

These topics are not part of the present article series but will be
linked in the sources where appropriate.

## Sources (act-wide)

- Perelman, G. (2002, 2003). arXiv:math/0211159, 0303109, 0307245.
- Hamilton, R. S. (1995). *The formation of singularities in the Ricci flow*. Surveys Diff. Geom. 2, 7–136.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. CMI/AMS.
- Morgan, J. & Tian, G. (2014). *The Geometrization Conjecture*. CMI/AMS.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12.
- Kleiner, B. & Lott, J. (2014). *Locally collapsed 3-manifolds*. Astérisque 365.
- Colding, T. H. & Minicozzi, W. P. (2008). *Width and finite extinction time of Ricci flow*. Geom. Topol. 12.
