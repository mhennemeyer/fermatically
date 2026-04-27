---
title: "Reduced Length and Reduced Volume"
slug: poincare/ricci-fluss/07-reduzierte-laenge
series: poincare
part: 7
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - reduzierte-laenge
  - reduziertes-volumen
---

# Reduced Length and Reduced Volume

!!! abstract "Summary"
    Perelman complements his entropy functionals
    ([Article 05](05-perelman-entropie.md)) with a second,
    path-based machinery: the **$\mathcal{L}$-length**, the derived
    **reduced length** $\ell(q, \tau)$, and the **reduced volume**
    $\tilde V(\tau)$. As with $\mathcal{W}$, these quantities are
    monotone along Ricci flow – this time backwards in time – and
    they yield a second, *local* proof of $\kappa$-non-collapsing
    ([Article 06](06-kappa-nichtkollaps.md)) as well as the technical
    tool that actually makes blow-up sequences converge.

## 1. What This Is About

Near a singularity at $T < \infty$ the natural time parameter is
not $t$ but the **remaining time** $\tau = T - t$. On the same
manifold $g(\tau)$ solves the *backward* Ricci equation

$$
\partial_\tau g_{ij} = 2\, R_{ij}.
$$

On $(M, g(\tau))$, Perelman considers the nonlinear path-integral
functional

$$
\mathcal{L}(\gamma)
= \int_0^{\bar\tau} \sqrt{\tau}\,\Big(R\big(\gamma(\tau), \tau\big) + |\dot\gamma(\tau)|_{g(\tau)}^{2}\Big)\, d\tau,
$$

defined for curves $\gamma : [0, \bar\tau] \to M$ with $\gamma(0) = p$.
The constants and the $\sqrt{\tau}$ factor are chosen exactly so
that the associated Euler-Lagrange equations match the conjugate
heat equation – the formal link to $\mathcal{W}$.

## 2. $\mathcal{L}$-Geodesics

A curve $\gamma$ rendering $\mathcal{L}$ stationary is called an
**$\mathcal{L}$-geodesic**. The Euler-Lagrange equation reads

$$
\nabla_{\dot\gamma}\dot\gamma - \tfrac12\,\nabla R + \tfrac{1}{2\tau}\dot\gamma + 2\,\mathrm{Ric}(\dot\gamma, \cdot)^{\sharp} = 0.
$$

Key features:

- The rescaled velocity $X(\tau) := \sqrt{\tau}\,\dot\gamma(\tau)$
  has a **finite limit** $X(0) \in T_p M$; every
  $\mathcal{L}$-geodesic is therefore determined by $(p, X(0))$.
- The **$\mathcal{L}$-exponential map**
  $\mathcal{L}\exp_p^\tau : T_p M \to M$, $X(0) \mapsto \gamma(\tau)$,
  is the parabolic analogue of the Riemannian exponential.

## 3. Reduced Length $\ell$

Let $L(q, \bar\tau)$ be the infimum of $\mathcal{L}(\gamma)$ over all
curves from $p$ to $q$ in time $\bar\tau$. The **reduced length**
is

$$
\ell(q, \bar\tau) := \frac{L(q, \bar\tau)}{2\sqrt{\bar\tau}}.
$$

$\ell$ is the right scale-invariant quantity: under parabolic
rescaling $g \to \lambda^{-2} g$, $\tau \to \lambda^{-2}\tau$ it is
unchanged. It is also **locally Lipschitz**, differentiable almost
everywhere, and satisfies the differential inequality

$$
\partial_\tau \ell - \Delta \ell + |\nabla \ell|^2 - R + \frac{n}{2\tau} \ge 0
\quad\text{(in the distributional sense).}
$$

This inequality is the analogue of the conjugate heat equation for
$u = (4\pi\tau)^{-n/2} e^{-f}$ from
[Article 05](05-perelman-entropie.md), §8.

## 4. Reduced Volume

The **reduced volume** based at $(p, T)$ is

$$
\tilde V(\tau) := \int_M (4\pi\tau)^{-n/2}\, e^{-\ell(q, \tau)}\, dV_{g(\tau)}(q).
$$

It measures how much mass of a "probability distribution"
concentrated at $p$ remains in the volume after backward-time
$\tau$.

## 5. The Monotonicity Formula

!!! note "Monotonicity Theorem (Perelman 2002, §7)"
    For every smooth solution of Ricci flow on a closed interval,
    $$
    \tau \;\longmapsto\; \tilde V(\tau)
    $$
    is **monotonically non-increasing**. Equality on an interval
    forces a **shrinking gradient soliton**.

This is the second pillar besides monotonicity of the
$\mathcal{W}$-entropy: a path-based, locally definable Lyapunov
function.

The model computation on flat $\mathbb{R}^n$ gives
$\ell(q, \tau) = |q-p|^2 / (4\tau)$, hence
$\tilde V(\tau) \equiv 1$ – the flat-space constant. On any
non-trivial flow, $\tilde V(\tau) \le 1$ measures a curvature
deficit.

## 6. Application 1: $\kappa$-Non-collapsing Reproved

From monotonicity of $\tilde V$ one directly obtains
[Article 06](06-kappa-nichtkollaps.md) §3:

1. If $g(t)$ collapsed at $(p, t)$, almost all the mass of
   $\tilde V(\tau)$ would lie in a small neighborhood, making
   $\tilde V(\tau)$ small for small $\tau$.
2. By monotonicity, $\tilde V$ would then be small for **all**
   later $\tau$ as well, contradicting the initial condition
   $\tilde V(\tau) \to 1$ as $\tau \to 0$.

This proof is *more local* than the entropy proof (it uses only
paths from $p$) and extends directly to **Ricci flow with surgery**
(Perelman 0303109 §6).

## 7. Application 2: Convergence of Blow-up Sequences

Let $(M, g_i(t), p_i)$ be a sequence of parabolically rescaled
flows around a singularity. From

- $\kappa$-non-collapsing (lower volume bound),
- Hamilton compactness (curvature bounds),
- monotonicity of $\tilde V$ (prevents mass loss),

one obtains: along a subsequence, $(M, g_i(t), p_i)$ converges
smoothly in the Cheeger-Gromov sense to a complete Ricci flow
limit – exactly the *ancient $\kappa$-solution* used in
[Article 06](06-kappa-nichtkollaps.md) §5.

Without $\tilde V$ one would have curvature bounds but no control
that the limit is complete – points could "escape to infinity".
Monotonicity of $\tilde V$ is the missing bound.

## 8. Asymptotic Solitons

A consequence of the equality clause in the monotonicity formula:

!!! note "Asymptotic Soliton Theorem (0211159 §11)"
    Every ancient $\kappa$-solution in dimension 3 has, after taking
    $\tau \to \infty$ and rescaling, an asymptotic shrinking
    gradient Ricci soliton limit.

Together with the splitting theorem this is the **actual** source
of the discrete classification of ancient $\kappa$-solutions in
[Article 06](06-kappa-nichtkollaps.md) §6: shrinking solitons in
dimension 3 form a finite list, and the entire ancient
$\kappa$-solution is "merely" the Ricci flow build-up to such a
soliton.

## 9. Relation to $\mathcal{W}$

| | $\mathcal{W}$-entropy | Reduced length / volume |
|--|------|------|
| Object | global function $f$ on $M$ | paths $\gamma$ from $p$ |
| Monotone quantity | $\mu(g(t), \tau)$ increases in $t$ | $\tilde V(\tau)$ decreases in $\tau$ |
| Main application | $\kappa$-non-collapsing (global) | $\kappa$-non-collapsing (local), blow-up convergence |
| Extends to surgery | with extra work | directly |
| Model | log-Sobolev / heat kernels | classical Riemannian $\exp$ |

Both machines speak about the same conjugate heat equation – once
from the **density** side $u$, once from the **characteristic
paths** $\gamma$.

## 10. What Comes Next

With the tools entropy, $\kappa$-non-collapsing, canonical
neighborhoods, and reduced length, the analytic machinery is
complete. Act 3
([Proof act overview](../beweis/index.md)) uses them to construct
**Ricci flow with surgery**, prove its smoothness, establish
**finite extinction time** for simply connected 3-manifolds, and
hence prove the
Poincaré conjecture
([Act 1, Article 04](../topologie/04-was-ist-poincare-vermutung.md))
together with geometrization
([Act 1, Article 05](../topologie/05-geometrisierungs-vermutung.md)).

## Sources

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§7–8, 11.
- Grigori Perelman, *Ricci flow with surgery on three-manifolds*, [arXiv:math/0303109](https://arxiv.org/abs/math/0303109), §§5–6.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§6–7.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§14–24.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §3.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), Ch. 7.
- Bennett Chow et al., *The Ricci Flow: Techniques and Applications, Part I*, AMS (2007), Ch. 7.

## Cross-references

- Previous article: [κ-Non-collapsing and Canonical Neighborhoods](06-kappa-nichtkollaps.md)
- Act overview: [Tools: Ricci Flow](index.md)
- Next act: [The Proof – Overview](../beweis/index.md)
