---
title: "Hamilton's Program and Its Obstacles"
slug: poincare/beweis/01-hamiltons-programm
series: poincare
part: 1
act: beweis
date: 2026-04-27
status: draft
lang: en
tags:
  - hamilton
  - programm
  - surgery
  - perelman
---
# Hamilton's Program and Its Obstacles

!!! abstract "Summary"
    Long before Perelman proved the Geometrization Conjecture in
    2002–2003, Richard **Hamilton** had laid out a clear plan: take
    any Riemannian metric on a closed 3-manifold $M^3$, run the
    **Ricci flow**, surgically excise singularities, and continue –
    until eventually a [Thurston-style
    geometrization](../topologie/05-geometrisierungs-vermutung.md)
    becomes visible. This article traces Hamilton's program,
    summarises his partial results and identifies the **five
    obstacles** that blocked it until 2002. Perelman's three
    preprints close exactly those gaps; the remaining articles of
    Act 3 implement his solutions one by one.

## 1. The 1982 vision

Hamilton's first paper on the Ricci flow ([Hamilton 1982,
*Three-manifolds with positive Ricci curvature*][hamilton1982]) is
also the birthplace of the program. He proved:

> **Theorem (Hamilton 1982).** Let $(M^3, g_0)$ be closed with
> strictly positive Ricci tensor. Then the Ricci flow
> $\partial_t g = -2\,\mathrm{Ric}(g)$ exists for all time and, after
> rescaling, converges to a metric of constant positive sectional
> curvature. In particular $M^3$ is diffeomorphic to a spherical
> space form $S^3/\Gamma$.

Already in the introduction Hamilton remarks that *in principle* the
same mechanism could prove the Geometrization Conjecture – provided
one understands singularities and removes them in a controlled way.
Over the following two decades he built the tools: short-time
existence via DeTurck's trick, maximum principles for tensors, the
[compactness theorem](../ricci-fluss/04-singularitaeten-blowup.md),
the differential Harnack inequality, and a first surgery theory in
dimension 4.

## 2. The program in one sentence

Let $(M^3, g_0)$ be closed and orientable. The Ricci flow is a
quasi-parabolic evolution equation; by Hamilton (cf.
[Act 2, Article 03](../ricci-fluss/03-hamiltons-ricci-fluss.md)) it
exists on a maximal interval $[0, T_{\max})$. The program consists of
four steps:

1. **Flow**, until $T_{\max}$ is reached or curvature blows up at
   finitely many points.
2. **Localise singularities**: show that every high-curvature region
   resembles one of finitely many model geometries (neck, cap,
   spherical space form).
3. **Surgery**: replace each neck by two round caps and discard
   spherical components.
4. **Repeat**, until after finitely many surgeries and possibly
   infinite time a geometrization becomes visible.

Geometrically: the flow should automatically execute the *prime*
decomposition of the 3-manifold into [connected
sums](../topologie/05-geometrisierungs-vermutung.md) and JSJ pieces.

## 3. Hamilton's tools by 2002

By the turn of the millennium Hamilton had assembled the central
building blocks:

| Tool | Source | Role in the program |
|------|--------|---------------------|
| Short-time existence, uniqueness | Hamilton 1982 / DeTurck 1983 | Start step 1 |
| Maximum principle for tensors | Hamilton 1986 | Curvature pinching |
| **Differential Harnack** | Hamilton 1993 | Classify ancient solutions |
| **Compactness theorem for flows** | Hamilton 1995 | Construct blow-up limits |
| Hamilton–Ivey pinching | Hamilton 1995, Ivey 1993 | $\sec \to {\geq}\,0$ in dim 3 |
| Classification of 2D ancient solutions | Hamilton 1995 | Model for neck/cigar |
| Surgery in dimension 4 | Hamilton 1997 | Prototype, $\mathrm{Rm}\geq 0$ |

[Hamilton 1995, *The formation of singularities in the Ricci flow*][hamilton1995]
is the most important survey article: it introduces the type
I/II/III terminology, proves the compactness theorem, and formulates
the structural conjecture that singularities in dim 3 should look
asymptotically cylindrical.

## 4. The five obstacles

Despite these tools the program remained incomplete until 2002.
Exactly five problems resisted Hamilton's methods:

### O1 – Collapse failure

Hamilton's compactness theorem produces blow-up limits **only** if
the volume ratios $\mathrm{Vol}(B_r)/r^n$ stay bounded below.
Without such a universal bound a sequence of rescaled metrics may
collapse onto a **lower-dimensional** object. Hamilton had handled
special cases but no general proof.

### O2 – Classifying ancient $\kappa$-solutions

Even granted a blow-up limit, one must know *what* it looks like.
Hamilton had the classification in 2D, but in dimension 3 only
conjectures: $S^3/\Gamma$, $S^2 \times \mathbb{R}$ and a
$\kappa$-non-collapsed Bryant soliton should exhaust all ancient
models.

### O3 – Canonical neighbourhoods

Even with a classified blow-up limit it is not clear that *every*
high-curvature region resembles one of those models. This structural
step – "large scalar curvature $\Rightarrow$ locally
$\varepsilon$-close to model" – is now called the **canonical
neighbourhood theorem**.

### O4 – Surgery with controlled constants

Hamilton had constructed surgery in dim 4 only under
$\mathrm{Rm}\geq 0$. In dim 3 without this hypothesis it was unclear
whether the surgery scales $\delta, h, r$ can be chosen consistently
– and whether $\kappa$-non-collapsing survives each surgery step.

### O5 – Finitely many surgeries on a finite interval

Even with perfect surgery one must rule out that surgery times
accumulate on a finite interval. Otherwise the process would
"explode" in finite time and never give a geometrization.

## 5. Perelman's contribution

Perelman's three preprints solve these obstacles in the same order:

| Obstacle | Perelman's tool | Reference |
|----------|-----------------|-----------|
| O1 | Entropy $\mathcal{W}$ + reduced volume $\tilde V$ | [Act 2, Art. 05](../ricci-fluss/05-perelman-entropie.md), [Art. 07](../ricci-fluss/07-reduzierte-laenge.md) |
| O2 | Hamilton–Ivey + $\kappa$-non-collapse + $\mathcal{L}$-geometry | [Act 2, Art. 06](../ricci-fluss/06-kappa-nichtkollaps.md) |
| O3 | Canonical neighbourhood theorem (0211159 §12) | [Act 3, Art. 02](02-singularitaeten-dim3.md) |
| O4 | Surgery with $\delta(t)$-function (0303109 §3–§4) | [Act 3, Art. 03](03-chirurgie.md) |
| O5 | Long-time existence and thin–thick (0303109 §6, 0307245) | [Act 3, Art. 04](04-long-time-verhalten.md), [Art. 05](05-endliche-extinktion.md) |

That the same toolset simultaneously yields *geometrization* and –
via finite extinction time – the *Poincaré conjecture* is the
conceptual heart of Act 3.

## 6. What Hamilton had foreseen

It is instructive to see how much of the program Hamilton had
already sketched:

- The surgery architecture (detect a neck, cut, fill with a cap) is
  laid out in Hamilton 1997.
- The structural conjecture "singularities in dim 3 look like
  cylinders" is stated almost verbatim in Hamilton 1995.
- Hamilton himself emphasised that *volume non-collapse* was the
  missing global bound – and his Harnack work supplies half of the
  required ingredient.

What was missing was a **monotonicity principle** producing this
bound from the flow itself – Perelman's entropy and reduced length.

## 7. Roadmap through Act 3

The remaining articles execute the solution to the five obstacles:

- **02 – Singularity analysis in dim 3** classifies ancient
  $\kappa$-solutions and proves the canonical neighbourhood theorem
  (O2 + O3).
- **03 – Ricci flow with surgery** defines standard solutions,
  $\delta$-necks, and runs surgery on an interval with controlled
  constants (O4).
- **04 – Long-time behaviour** shows that surgery times do not
  accumulate, and produces the thin–thick decomposition as
  $t \to \infty$ (O5 + geometrization).
- **05 – Finite extinction time** is the shortcut to the Poincaré
  conjecture: for a simply connected initial manifold the flow
  becomes extinct in finite time (Perelman 0307245,
  Colding–Minicozzi 2005).
- **06 – Geometrization implies Poincaré** closes the loop and shows
  how the full geometrization theorem contains the original
  conjecture as a corollary.

## Sources

- **R. Hamilton**, *Three-manifolds with positive Ricci curvature*,
  J. Differential Geom. 17 (1982), 255–306. [PDF][hamilton1982]
- **R. Hamilton**, *The formation of singularities in the Ricci flow*,
  Surveys in Differential Geometry II (1995), 7–136.
  [PDF][hamilton1995]
- **R. Hamilton**, *Four-manifolds with positive isotropic curvature*,
  Comm. Anal. Geom. 5 (1997), 1–92. (Surgery prototype.)
- **G. Perelman**, *The entropy formula for the Ricci flow and its
  geometric applications*,
  [arXiv:math/0211159](https://arxiv.org/abs/math/0211159).
- **G. Perelman**, *Ricci flow with surgery on three-manifolds*,
  [arXiv:math/0303109](https://arxiv.org/abs/math/0303109).
- **G. Perelman**, *Finite extinction time for the solutions to the
  Ricci flow on certain three-manifolds*,
  [arXiv:math/0307245](https://arxiv.org/abs/math/0307245).
- **J. Morgan, G. Tian**, *Ricci Flow and the Poincaré Conjecture*,
  Clay Math. Monographs 3, AMS 2007. (Complete write-up.)
- **B. Kleiner, J. Lott**, *Notes on Perelman's papers*,
  Geom. Topol. 12 (2008), 2587–2855.
- **H.-D. Cao, X.-P. Zhu**, *A complete proof of the Poincaré and
  geometrization conjectures*, Asian J. Math. 10 (2006), 165–492.

[hamilton1982]: https://projecteuclid.org/euclid.jdg/1214436922
[hamilton1995]: https://www.intlpress.com/site/pub/files/_fulltext/journals/sdg/1995/0002/0001/SDG-1995-0002-0001-a002.pdf
