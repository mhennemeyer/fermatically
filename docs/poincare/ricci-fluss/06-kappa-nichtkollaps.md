---
title: "κ-Non-collapsing and Canonical Neighborhoods"
slug: poincare/ricci-fluss/06-kappa-nichtkollaps
series: poincare
part: 6
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - kappa-nichtkollaps
  - kanonische-nachbarschaften
---

# κ-Non-collapsing and Canonical Neighborhoods

!!! abstract "Summary"
    Hamilton's compactness theorem ([Article 04](04-singularitaeten-blowup.md))
    yields blow-up limits **only** if the volume does not degenerate
    locally. Exactly that bound is delivered by Perelman's
    **$\kappa$-non-collapsing theorem**: on every finite scale, the
    ratio volume/curvature-radius stays above a universal constant
    $\kappa>0$. Combined with Hamilton's Harnack inequality, the
    theorem implies the **classification of ancient $\kappa$-solutions**
    in dimension 3 – and therefore that every high-curvature region
    of a 3-dimensional Ricci flow looks like one of finitely many
    model geometries (neck, cap, spherical space form). These
    "canonical neighborhoods" are the geometric prerequisite for
    surgery ([Act 3, Article 03](../beweis/03-chirurgie.md)).

## 1. The Collapsing Problem

A sequence $(M_i, g_i, p_i)$ of Riemannian manifolds **collapses**
at $p_i$ on scale $r$ if

$$
\frac{\mathrm{Vol}\big(B_{g_i}(p_i, r)\big)}{r^{n}} \longrightarrow 0,
$$

while curvature on $B_{g_i}(p_i, r)$ remains bounded
($|\mathrm{Rm}|\le r^{-2}$). Geometrically, some directions become
so thin that the manifold locally degenerates to a lower-dimensional
object (think of a long thin cylinder converging to a circle).

For the blow-up analysis from
[Article 04](04-singularitaeten-blowup.md), collapsing is fatal:
without a lower volume bound, Hamilton's compactness theorem fails,
and the blow-up limit does not exist as a Riemannian manifold at
all – it degenerates to a space of strictly lower dimension.

## 2. Definition: $\kappa$-Non-collapsing

Let $\kappa > 0$ and $r_0 > 0$. A Ricci flow $(M, g(t))$ is called
**$\kappa$-non-collapsed at $(p, t)$ on scale $r_0$** if for every
$0 < r < r_0$,

$$
\sup_{B_{g(t)}(p, r)} |\mathrm{Rm}| \le r^{-2}
\;\Longrightarrow\;
\frac{\mathrm{Vol}\big(B_{g(t)}(p, r)\big)}{r^{n}} \ge \kappa.
$$

In words: whenever curvature inside the ball of radius $r$ is at
most $r^{-2}$, the ball is at least $\kappa$-full.

## 3. Perelman's $\kappa$-Non-collapsing Theorem

!!! note "Theorem (Perelman 2002, §4)"
    Let $g(t)$ be a smooth solution of Ricci flow on a closed
    $n$-manifold $M$, defined on $[0, T)$ with $T < \infty$. Then
    there exists $\kappa = \kappa(g(0), T) > 0$ such that $g(t)$ is
    $\kappa$-non-collapsed at every point and on every scale
    $r < \sqrt{T}$.

The theorem holds **without** curvature assumptions – it follows
solely from monotonicity of the $\mathcal{W}$-entropy and is thus
a qualitative conservation law of the flow itself.

## 4. Proof Strategy via $\mathcal{W}$

The idea connects [Article 05](05-perelman-entropie.md) with volume
geometry:

1. If the flow were collapsed at $(p, t)$, one could construct a
   test function $f$ concentrated on $B(p, r)$.
2. Plugging $f$ into $\mathcal{W}(g, f, \tau)$ with $\tau \sim r^2$
   yields

   $$
   \mu(g(t), r^2) \le \mathcal{W}(g(t), f, r^2) \to -\infty
   \quad\text{as}\quad
   \frac{\mathrm{Vol}\, B(p, r)}{r^n} \to 0.
   $$

3. On the other hand, $\mu(g(t), \tau)$ is **monotonically
   non-decreasing** along Ricci flow and bounded below by
   $\mu(g(0), \tau + t)$.

The contradiction between 2 and 3 forces a universal
$\kappa(g(0), T)$. The argument is in Perelman 0211159 §4 and is
worked out in Kleiner–Lott §13 and Morgan–Tian §8.

## 5. Local Variant and Ancient Solutions

The above statement is global. For singularity analysis
([Article 04](04-singularitaeten-blowup.md)) one needs a **local**,
**ancient** version:

!!! note "Corollary"
    Every blow-up limit of a finite-time singularity of Ricci flow
    on a closed 3-manifold is an **ancient $\kappa$-solution**:
    complete, defined on $t \in (-\infty, 0]$, with non-negative
    sectional curvature, $\kappa$-non-collapsed on all scales, and
    bounded curvature on every compact time interval.

Ancient $\kappa$-solutions inherit the volume bound from the
$\kappa$-non-collapsing theorem in the limit; without it, the
limit would not even be a Riemannian space.

## 6. Classification of Ancient $\kappa$-Solutions in Dimension 3

Combining $\kappa$-non-collapsing with Hamilton's differential
Harnack inequality and the splitting-theorem machinery, Perelman
(0211159 §11) shows:

!!! note "Classification Theorem"
    An ancient $\kappa$-solution in dimension 3 is one of:

    - the **shrinking round cylinder** $S^2 \times \mathbb{R}$,
    - its $\mathbb{Z}_2$-quotient,
    - a **Bryant-soliton-like** rotationally symmetric cap,
    - the **round shrinking** $S^3$ or a spherical quotient,
    - or every ball is asymptotically a neck or a cap.

This discrete list is the geometric substance from which the
"canonical neighborhoods" are extracted.

## 7. Canonical Neighborhoods

For small $\varepsilon > 0$, Perelman defines three model types:

| Type | Geometry | Topology |
|------|----------|----------|
| $\varepsilon$-**neck** | $\varepsilon$-close to a piece $S^2 \times [-\varepsilon^{-1}, \varepsilon^{-1}]$ of the round cylinder | $S^2 \times I$ |
| $\varepsilon$-**cap** | $\varepsilon$-close to a Bryant-like hemisphere with attached neck | $D^3$ or $\mathbb{RP}^3 \setminus \overline{D^3}$ |
| **spherical space form** | entire component $\varepsilon$-close to a round quotient $S^3/\Gamma$ | $S^3/\Gamma$ |

!!! note "Canonical Neighborhood Theorem (0211159 §12)"
    For every $\varepsilon > 0$ there exists $r_0 > 0$ such that on
    a Ricci flow on a closed 3-manifold, every point $(x, t)$ with
    $|\mathrm{Rm}|(x,t) \ge r_0^{-2}$ has an $\varepsilon$-neighborhood
    of one of the three types.

High-curvature regions are thus not arbitrary – up to $\varepsilon$
they always look like one of a finite list of models.

## 8. Significance for Surgery

Surgery ([Act 3, Article 03](../beweis/03-chirurgie.md)) cuts along
an $\varepsilon$-neck and glues in caps. For the procedure to be
**well-defined**, three conditions must hold:

1. High-curvature regions are **classified** (classification theorem,
   §6).
2. High-curvature regions admit **canonical neighborhoods** (§7).
3. After every cut, the result is **again $\kappa'$-non-collapsed**
   for a $\kappa'$ only slightly worse than before.

Point 3 requires a *Ricci-flow-with-surgery* version of the
$\kappa$-non-collapsing theorem – the subject of Perelman 0303109
§§5–7.

## 9. What Entropy and What Reduced Length Do

There are **two** independent proofs of $\kappa$-non-collapsing:

- via the $\mathcal{W}$-entropy ([Article 05](05-perelman-entropie.md), §4 above),
- via the **reduced length** $\ell(q, \tau)$ and the **reduced
  volume** $\tilde V(\tau)$ ([Article 07](07-reduzierte-laenge.md)).

Both rely on the same mechanism – monotonicity of a
scale-invariant quantity along the flow. Reduced length is better
suited for **local** statements and blow-up arguments because it
is path-based and does not depend on a globally defined test
function.

## Sources

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§4, 7, 11–12.
- Grigori Perelman, *Ricci flow with surgery on three-manifolds*, [arXiv:math/0303109](https://arxiv.org/abs/math/0303109), §§5–7.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§8, 9, 11.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§13, 25–28, 41–48.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §§4, 6.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), Ch. 8.

## Cross-references

- Previous article: [Perelman's Entropy Functionals](05-perelman-entropie.md)
- Next article: [Reduced Length and Reduced Volume](07-reduzierte-laenge.md)
- Act 3, Article 03: [Surgery on the Ricci Flow](../beweis/03-chirurgie.md)
