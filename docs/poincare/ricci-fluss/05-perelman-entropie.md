---
title: "Perelman's Entropy Functionals"
slug: poincare/ricci-fluss/05-perelman-entropie
series: poincare
part: 5
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - entropie
  - perelman
---

# Perelman's Entropy Functionals

!!! abstract "Summary"
    Perelman's first paper *The entropy formula for the Ricci flow*
    (2002) showed: the Ricci flow is the gradient flow of two
    functionals, $\mathcal{F}$ and $\mathcal{W}$. Both are
    **monotone** along the flow, providing the conserved structure
    Hamilton lacked: a Lyapunov function. From $\mathcal{W}$ the
    $\kappa$-non-collapsing theorem follows directly — the central
    lever for compactness of blow-up sequences.

## 1. The point

The Ricci flow (see [Article 03](03-hamiltons-ricci-fluss.md))
smooths curvature locally but can produce singularities. Before any
blow-up analysis (see
[Article 04](04-singularitaeten-blowup.md)) is possible one needs a
**controlling quantity** that has a definite direction along the flow
— analogous to energy in a gradient flow. Perelman found two such
quantities.

## 2. The $\mathcal{F}$-functional

For a metric $g$ and a function $f \in C^\infty(M)$ Perelman defines

$$\mathcal{F}(g, f) := \int_M \bigl(R + \lvert\nabla f\rvert^2\bigr)\, e^{-f}\, dV.$$

Here $R$ is the scalar curvature and
$d\mu := e^{-f}\, dV$ is a weighted measure. Varying $g$ and $f$
under the constraint $\int_M e^{-f}\, dV = 1$ yields the
Euler–Lagrange equations

$$\partial_t g = -2\,(\mathrm{Ric} + \nabla^2 f),\qquad \partial_t f = -R - \Delta f + \lvert\nabla f\rvert^2.$$

> **Key observation (Perelman §1).** Modulo a diffeomorphism gauge,
> the pair $(g, f)$ is a gradient flow of $\mathcal{F}$ with respect
> to the metric $\int_M (\cdots)\, e^{-f}\, dV$ on configuration space.
> In particular $\mathcal{F}$ increases monotonically:
>
> $$\frac{d}{dt}\mathcal{F} = 2\int_M \bigl\lvert\mathrm{Ric} + \nabla^2 f\bigr\rvert^2\, e^{-f}\, dV \ge 0.$$

The critical points are exactly the **steady solitons**
$\mathrm{Ric} + \nabla^2 f = 0$.

## 3. From $\mathcal{F}$ to the $\lambda$-functional

Optimising $\mathcal{F}$ over $f$ subject to the constraint produces
a geometric invariant of the metric:

$$\lambda(g) := \inf_{f}\, \mathcal{F}(g, f),\qquad \int_M e^{-f}\, dV = 1.$$

$\lambda(g)$ is the lowest eigenvalue of the Schrödinger operator
$-4\Delta + R$. Along the Ricci flow $\frac{d}{dt}\lambda \ge 0$.

**Consequence.** On a closed manifold with $\lambda(g_0) > 0$ the
Ricci flow can never have a steady soliton with non-positive scalar
curvature as limit. Whole classes of putative limit geometries are
already excluded.

## 4. The step to the $\mathcal{W}$-functional

$\mathcal{F}$ controls steady solitons; for the analysis of
singularities one needs **shrinking solitons**. Perelman therefore
replaces $\mathcal{F}$ with the scale-aware
**$\mathcal{W}$-functional**:

$$\mathcal{W}(g, f, \tau) := \int_M \Bigl[\tau\bigl(R + \lvert\nabla f\rvert^2\bigr) + f - n\Bigr]\, (4\pi\tau)^{-n/2}\, e^{-f}\, dV.$$

Here $\tau > 0$ is a **backwards-time parameter** (typically
$\tau = T - t$), $n$ is the dimension, and the constraint is
$\int_M (4\pi\tau)^{-n/2}\, e^{-f}\, dV = 1$.

**Scale invariance.** $\mathcal{W}$ is invariant under
$(g, \tau) \mapsto (\lambda^2 g, \lambda^2 \tau)$ — exactly the
scaling of the Ricci flow (Article 03, §5). This makes $\mathcal{W}$
the natural tool for **blow-up limits**, whose scale diverges.

## 5. The monotonicity formula

> **Theorem (Perelman 2002, §3).** Let $g(t)$ be a Ricci flow on
> $[0, T)$, $\tau = T - t$, and let $f(t)$ satisfy the backward
> conjugate heat equation
> $\partial_\tau f = -\Delta f + \lvert\nabla f\rvert^2 - R + n/(2\tau)$.
> Then
>
> $$\frac{d}{dt}\mathcal{W}(g, f, \tau) = 2\tau \int_M \Bigl\lvert\mathrm{Ric} + \nabla^2 f - \frac{1}{2\tau} g\Bigr\rvert^2\, (4\pi\tau)^{-n/2}\, e^{-f}\, dV \ge 0.$$

This identity is the **entropy formula**. Its critical points are
exactly the **shrinking gradient solitons**
$\mathrm{Ric} + \nabla^2 f = \tfrac{1}{2\tau}\, g$.

## 6. The $\mu$- and $\nu$-functionals

As with $\mathcal{F}$ one optimises over $f$ and $\tau$:

$$\mu(g, \tau) := \inf_f \mathcal{W}(g, f, \tau),\qquad
\nu(g) := \inf_{\tau > 0} \mu(g, \tau).$$

$\mu$ and $\nu$ are geometric invariants. $\mu$ increases
monotonically along the flow; $\nu$ furnishes a genuine conformal
bound. Both are also logarithmic **Sobolev constants** of $(M, g)$ —
the bridge to functional-analytic machinery.

## 7. What the entropy rules out

Three structural consequences of monotonicity, central to Act 3:

1. **No finite-time shrinking soliton singularities other than the
   classified ones.** Every blow-up limit is a shrinking gradient
   soliton; in dim 3 the combination of $\mathcal{W}$-monotonicity
   and preservation of $R \ge 0$ forces these to be sphere quotients
   or round cylinders.
2. **No closed dim-3 steady solitons except the flat ones.**
   $\mathcal{F}$-monotonicity excludes non-flat closed steady
   solitons.
3. **Local volume bounds.** Entropy controls the ratio
   volume / curvature scale — the precursor of $\kappa$-non-collapsing
   (see [Article 06](06-kappa-nichtkollaps.md)).

## 8. Connection to the heat / Schrödinger operator

The equation for $f$ associated with $\mathcal{W}$ is the
**conjugate heat equation**

$$\Box^{*} u = (-\partial_t - \Delta + R)\, u = 0,\qquad u = (4\pi\tau)^{-n/2}\, e^{-f}.$$

It is dual to the heat equation $\Box u = (\partial_t - \Delta) u$
along the Ricci flow. This duality is the key to the construction of
**reduced length** (see [Article 07](07-reduzierte-laenge.md)) and
to the monotone volume quantity $\tilde V$.

## 9. Historical placement

Before Perelman the Ricci flow was a technical tool without
variational structure; Hamilton had several ad hoc maximum
principles. With $\mathcal{F}$ and $\mathcal{W}$ the flow becomes

- a **gradient flow** with a clearly defined variational space,
- equipped with a **Lyapunov function**,
- which is moreover **scale invariant** and therefore survives
  blow-ups.

These three properties together constitute the conceptual leap from
Hamilton 1982 to Perelman 2002.

## Sources

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§1–4.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§5–6.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§4–9.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §§3–4.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), ch. 6.

## Cross-references

- Previous article: [Singularities and Blow-up Limits](04-singularitaeten-blowup.md)
- Next article: [κ-Non-collapsing and Canonical Neighborhoods](06-kappa-nichtkollaps.md)
- Act 1, Article 04: [What is the Poincaré Conjecture?](../topologie/04-was-ist-poincare-vermutung.md)
