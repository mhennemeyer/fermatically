---
title: "Singularity Analysis in Dimension 3"
slug: poincare/beweis/02-singularitaeten-dim3
series: poincare
part: 2
act: beweis
date: 2026-04-27
status: draft
lang: en
tags:
  - dim-3
  - kappa-loesungen
  - kanonische-nachbarschaften
  - hamilton-ivey
---
# Singularity Analysis in Dimension 3

!!! abstract "Summary"
    This article resolves the two obstacles **O2** (classification of
    ancient $\kappa$-solutions) and **O3** (canonical neighbourhood
    theorem) from [Article 01](01-hamiltons-programm.md). It combines
    three ingredients: (i) the **Hamilton–Ivey pinching**, which in
    dimension 3 forces curvature to become asymptotically
    non-negative; (ii) Perelman's
    [$\kappa$-non-collapsing theorem](../ricci-fluss/06-kappa-nichtkollaps.md),
    providing volume lower bounds; and (iii) the
    [reduced $\mathcal{L}$-geometry](../ricci-fluss/07-reduzierte-laenge.md),
    which identifies blow-up limits as $\kappa$-solutions. The result
    is the **classification of ancient $\kappa$-solutions in
    dimension 3** and the **canonical neighbourhood theorem**: at
    every point of sufficiently large scalar curvature the flow is,
    up to $\varepsilon$, modelled on one of three standard pieces –
    a neck, a cap, or a spherical space form.

## 1. Hamilton–Ivey pinching: positive curvature wins

On a closed 3-manifold the Riemann tensor has only three independent
eigenvalues $\lambda_1 \leq \lambda_2 \leq \lambda_3$ of the
curvature operator. Hamilton 1995 / Ivey 1993 proved:

> **Pinching estimate.** For every Ricci flow on a closed
> 3-manifold there is a function $\phi:[0,\infty)\to\mathbb{R}$ with
> $\phi(s)/s \to 0$ as $s\to\infty$ such that at every space-time
> point
> $$
>   \lambda_1 \;\geq\; -\phi(\lambda_3).
> $$

In words: the most negative curvature direction is only
logarithmically worse than the most positive. In particular, **as
curvature blows up every sectional curvature becomes non-negative in
the limit**. This is why singularity analysis in dimension 3 – and
only there – can be carried out using the theory of ancient
solutions with non-negative curvature.

## 2. Ancient $\kappa$-solutions: the list of models

An **ancient solution** is a Ricci flow $(M, g(t))_{t \in (-\infty, 0]}$
with bounded curvature on finite intervals. It is
**$\kappa$-non-collapsed** if at every scale $r$
$$
\frac{\mathrm{Vol}(B(p,t,r))}{r^n} \;\geq\; \kappa
\quad\text{whenever}\quad |\mathrm{Rm}|\leq r^{-2}.
$$

For blow-up limits Hamilton–Ivey additionally gives
$\mathrm{Rm}\geq 0$.

> **Classification (Perelman 0211159 §11).** Every ancient
> $\kappa$-solution in dimension 3 with non-negative curvature
> operator is one of the following:
>
> 1. the **round cylinder** $S^2 \times \mathbb{R}$ or its
>    $\mathbb{Z}_2$-quotient;
> 2. a **shrinking spherical quotient** $S^3/\Gamma$;
> 3. an **ancient non-cylindrical model** with non-compact topology
>    $\mathbb{R}^3$, asymptotically cylindrical (Bryant-type).

Proof idea: Hamilton–Harnack + Toponogov comparison force the
sectional curvature at infinity to be locally dominated by the
cylinder; the $\mathcal{L}$-geometry shows that every asymptotic
soliton is one of these models; $\kappa$-non-collapsing rules out
"cigars" (Hamilton's 2D soliton) and hence a fourth class.

## 3. Geometric building blocks: neck, cap, space form

From the classification Perelman extracts three local **model
geometries** against which every high-curvature region is measured.

| Model | Local form | Scale |
|-------|------------|-------|
| **$\varepsilon$-neck** | $\varepsilon$-close to $S^2 \times [-\varepsilon^{-1}, \varepsilon^{-1}]$, round $S^2$ | $r = R^{-1/2}$ |
| **$\varepsilon$-cap** | Diffeomorphic to $D^3$ or $\mathbb{RP}^3 \setminus \overline{B}$, with an $\varepsilon$-neck at the open end | $r$ |
| **Spherical space form** | $S^3/\Gamma$ with almost constant positive sectional curvature | whole component |

Here $R$ is the scalar curvature at the centre of the neck. The
precise definition (Cao–Zhu, Morgan–Tian) requires
$\varepsilon$-closeness in the $C^{[1/\varepsilon]}$-topology after
parabolic rescaling.

## 4. The canonical neighbourhood theorem

> **Theorem (Perelman 0211159 §12.1).** Given $\varepsilon > 0$
> there exists a function $r_0(t) > 0$ such that: every point
> $(x,t)$ in a Ricci flow on a closed 3-manifold with
> $R(x,t) \geq r_0(t)^{-2}$ lies in a **canonical neighbourhood**,
> i.e. after rescaling by $R(x,t)$ it is $\varepsilon$-close to one
> of the three models (neck, cap, spherical space form).

Sketch of proof:

1. Argue by contradiction: suppose there is a sequence
   $(x_i, t_i)$ with $R(x_i,t_i) \to \infty$ whose rescaling fits
   *no* model.
2. Hamilton compactness (volume lower bound from $\kappa$-non-
   collapsing, curvature bound from pinching) yields a Cheeger–
   Gromov subsequential limit.
3. Thanks to $\mathcal{L}$-geometry the limit is an ancient
   $\kappa$-solution with $\mathrm{Rm}\geq 0$ – hence by §2 one of
   the three models.
4. Contradiction.

The proof uses *every* tool from Act 2 jointly: without entropy no
$\kappa$-non-collapsing (step 2); without reduced length no
convergence to an asymptotic soliton (step 3); without Hamilton–Ivey
no non-negative curvature operator in the limit.

## 5. Local consequence: high curvature is canonical

Two direct corollaries structure the flow shortly before a
singularity:

**5.1 Structural decomposition.** On every time slice $t$ just below
a singular time $T$ the region $\{R(\cdot,t) \geq r_0(t)^{-2}\}$
splits into a disjoint union of $\varepsilon$-necks,
$\varepsilon$-caps and entire spherical components.

**5.2 Volume control.** The global volume $\mathrm{Vol}(M, g(t))$
remains controlled up to $T$ by the pinching estimate; in particular
necks contribute *small* volume.

Both statements are the geometric prerequisite for defining
**surgery** in the next article: necks are localised, their central
$S^2$ is explicit, and what survives a cut is topologically
controlled.

## 6. What surgery inherits from this analysis

§3 + §4 together yield the **local cutting plan**:

- Every $\varepsilon$-neck has a unique central $S^2$.
- The two components produced by a cut along that $S^2$ each have
  an $\varepsilon$-cap as their starting end.
- Spherical components ($S^3/\Gamma$) become extinct in finite time
  and may be discarded.

What remains open: the *global* choice of constants
$(\delta(t), h(t), r(t))$, the definition of the **standard
solution** (model used to fill in), and the preservation of
$\kappa$-non-collapsing + pinching after each surgery step. That is
the content of [Article 03](03-chirurgie.md).

## 7. Summary: obstacle → resolution

| Obstacle from Art. 01 | Tool | Result |
|-----------------------|------|--------|
| O2 (classify $\kappa$-solutions) | Hamilton–Ivey + $\mathcal{L}$-geom. | §2 (3 models) |
| O3 (canonical neighbourhood) | Hamilton compactness + §2 | §4 (theorem) |
| Preparation for O4 (surgery) | §3 + §5 | local cutting plan |

Act 3 is therefore fully prepared for the third article: we know
*where* to cut and *what* survives the cut.

## Sources

- **G. Perelman**, *The entropy formula for the Ricci flow and its
  geometric applications*, §§11–12,
  [arXiv:math/0211159](https://arxiv.org/abs/math/0211159).
- **R. Hamilton**, *The formation of singularities in the Ricci flow*,
  Surveys in Differential Geometry II (1995), 7–136.
- **T. Ivey**, *Ricci solitons on compact three-manifolds*,
  Differential Geom. Appl. 3 (1993), 301–307. (Early form of the
  pinching estimate.)
- **J. Morgan, G. Tian**, *Ricci Flow and the Poincaré Conjecture*,
  Clay Math. Monographs 3, AMS 2007, ch. 9 (standard solutions),
  ch. 10 (canonical neighbourhoods).
- **B. Kleiner, J. Lott**, *Notes on Perelman's papers*,
  §§40–53, Geom. Topol. 12 (2008).
- **H.-D. Cao, X.-P. Zhu**, *A complete proof of the Poincaré and
  geometrization conjectures*, Asian J. Math. 10 (2006), §§5–6.
- **B. Chow, P. Lu, L. Ni**, *Hamilton's Ricci Flow*,
  AMS GSM 77, 2006. (Detailed proof of Hamilton–Ivey.)
