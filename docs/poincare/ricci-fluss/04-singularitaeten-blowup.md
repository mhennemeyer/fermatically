---
title: "Singularities and Blow-up Limits"
slug: poincare/ricci-fluss/04-singularitaeten-blowup
series: poincare
part: 4
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - singularitaeten
  - blow-up
---

# Singularities and Blow-up Limits

!!! abstract "Summary"
    The Ricci flow breaks down in finite time as soon as curvature
    diverges somewhere. To understand *how* it breaks down, one zooms
    in on the singularity: Hamilton's **blow-up procedure** produces
    parabolically rescaled limit flows. Classifying these limit
    models — in particular the notion of a $\kappa$-solution — is the
    key to Perelman's surgery program.

## 1. When does the flow break down?

Short-time existence (see [Article 03](03-hamiltons-ricci-fluss.md))
gives a maximal existence interval $[0, T)$. The terminal time $T$
is characterised by a **curvature blow-up**:

> **Lemma (Hamilton 1982).** If $T < \infty$ is the maximal existence
> time, then
> $\displaystyle \limsup_{t \to T} \max_M \lvert\mathrm{Rm}(\cdot, t)\rvert = +\infty.$

Equivalently: as long as the full Riemann curvature stays bounded the
flow can be extended. A finite singular time is therefore always a
**curvature concentration point**.

## 2. Type-I and Type-II singularities

Hamilton (1995) classified singularities by the growth rate of
curvature relative to the remaining time $T - t$:

| Type | Condition | Model picture |
|---|---|---|
| I | $\sup_{M\times[0,T)} (T-t)\,\lvert\mathrm{Rm}\rvert < \infty$ | round shrinking cylinder, $S^3$ shrinker |
| II | $\sup (T-t)\,\lvert\mathrm{Rm}\rvert = \infty$ | degenerate "cigar" and Bryant solitons |
| III | $\sup t\,\lvert\mathrm{Rm}\rvert < \infty$, $T = \infty$ | infinite time, hyperbolic pieces |

In dimension three Perelman shows that all finite-time singularities
are **Type I or II with $\kappa$-solution model** — Type III appears
only after all surgeries, as long-time behaviour.

## 3. The neckpinch as model singularity

The prototypical example: a **dumbbell-shaped** $S^3$ with a thin
neck. Under the Ricci flow the neck shrinks faster than the bells;
the metric converges locally to a round cylinder
$S^2 \times \mathbb{R}$ with vanishing $S^2$-radius (Angenent–Knopf
2004 give a rigorous construction).

In suitable coordinates the neck radius behaves as
$r(t) \sim \sqrt{2(T-t)}$ — the rescaled flow is a shrinking
cylinder, i.e. a **gradient shrinking soliton**.

## 4. Parabolic rescaling (blow-up)

Hamilton's idea for "looking inside" a singularity: choose a sequence
$(p_k, t_k)$ with $t_k \to T$ and
$Q_k := \lvert\mathrm{Rm}(p_k, t_k)\rvert \to \infty$, and define the
**parabolically rescaled** metrics

$$g_k(s) := Q_k \cdot g\!\left(t_k + \frac{s}{Q_k}\right),\qquad s \in [-Q_k\, t_k,\, 0].$$

This rescaling is the unique one that preserves the Ricci flow
(Article 03, §5): if $g$ satisfies $\partial_t g = -2\,\mathrm{Ric}(g)$,
so does each $g_k$. Curvature at the base point is normalised to 1.

## 5. Hamilton's compactness theorem

To extract a limit flow from $(M, g_k(s), p_k)$ one needs two
hypotheses:

1. **Curvature bounds on every backward time interval** (uniform in $k$).
2. **A lower injectivity-radius bound** $\mathrm{inj}(p_k) \ge \iota > 0$
   with respect to $g_k$.

> **Theorem (Hamilton, *Compactness*, 1995).** Under these hypotheses
> there is a subsequence converging in $C^\infty_{\mathrm{loc}}$ (in
> the sense of pointed Cheeger–Gromov convergence) to a complete
> Ricci flow $(M_\infty, g_\infty(s), p_\infty)$ on an interval
> $(-\infty, 0]$.

This is the machine that **turns a singularity into an
"infinitely-old" limit flow** — a so-called **ancient solution**.

## 6. Where the compactness theorem fails: collapse

Hypothesis 2 is the delicate one: without a lower injectivity-radius
bound the limit can **collapse** (locally drop dimension). Example:
a thin torus whose $S^1$-factor shrinks — only the two-dimensional
factor survives the limit.

Perelman's breakthrough fixes precisely this gap: the
**$\kappa$-non-collapsing theorem** (see
[Article 06](06-kappa-nichtkollaps.md)) enforces a universal lower
injectivity-radius bound along the singularity, and only then is
Hamilton's compactness theorem applicable.

## 7. Ancient $\kappa$-solutions

The limit objects of the blow-up procedure are, in dimension three,
extremely constrained:

> **Definition.** An **ancient $\kappa$-solution** is a complete,
> non-flat Ricci flow $(M, g(s))$ on $(-\infty, 0]$ with non-negative
> curvature, bounded curvature on every compact time interval, and
> $\kappa$-non-collapsing.

Perelman (2002, §11) classifies all ancient $\kappa$-solutions in
dim 3: they are **quotients of the round sphere**, the **round
cylinder** $S^2 \times \mathbb{R}$, or special **Bryant solitons**
(rotationally symmetric, asymptotically cylindrical solitons).

Consequence: every singularity in dim 3 looks, up close, like one of
these three models — the **canonical neighbourhood** on which
Perelman's surgery construction is based.

## 8. Solitons: stationary model solutions

Self-similar solutions of the Ricci flow are called **Ricci solitons**:

$$\mathrm{Ric}(g) + \nabla^2 f = \lambda\, g,\qquad \lambda \in \{-1, 0, +1\}.$$

- $\lambda > 0$: **shrinking soliton** (model for Type-I
  singularities), e.g. the round sphere, the round cylinder, or the
  **Gaussian soliton** $(\mathbb{R}^n, g_{\text{flat}}, f = \lvert x \rvert^2/4)$.
- $\lambda = 0$: **steady soliton**, e.g. Hamilton's **cigar soliton**
  (model for Type-II in dim 2).
- $\lambda < 0$: **expanding soliton**, model for the resolution of a
  singularity after surgery.

Solitons form the **phase space** of the Ricci flow; Perelman's
$\mathcal{W}$-functional (see
[Article 05](05-perelman-entropie.md)) identifies shrinking solitons
as critical points.

## 9. From model to surgery

The red thread leading to the proof of the geometrisation conjecture:

1. Flow runs up to a singularity at $t = T_1$.
2. Blow-up at the singularity yields an ancient $\kappa$-solution.
3. Classification implies: locally the picture is a sphere/quotient,
   a round neck, or a Bryant cap.
4. **Surgery:** cut at a neck, glue in standard caps.
5. The remaining manifold has simpler topology; the flow restarts.
6. Iterate; Act 3 shows that this process terminates in finite time
   and reconstructs the topology.

## Sources

- Richard S. Hamilton, *The formation of singularities in the Ricci flow*, Surveys Diff. Geom. 2 (1995), 7–136.
- Sigurd Angenent & Dan Knopf, *An example of neckpinching for Ricci flow on $S^{n+1}$*, Math. Res. Lett. 11 (2004), 493–518.
- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §11.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§9–12.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§37–43.

## Cross-references

- Previous article: [Hamilton's Ricci Flow](03-hamiltons-ricci-fluss.md)
- Next article: [Perelman's Entropy Functionals](05-perelman-entropie.md)
- Act 3, Article 03: [Surgery on the Ricci Flow](../beweis/03-chirurgie.md)
