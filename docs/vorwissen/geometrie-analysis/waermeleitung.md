---
title: "The Heat Equation – Intuition"
slug: vorwissen/geometrie-analysis/waermeleitung
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: en
tags:
  - heat-equation
  - pde
  - intuition
---

# The Heat Equation – Intuition

> *"The Ricci flow is – roughly – the heat equation for the Riemannian
> metric. Whoever sees heat spreading sees curvature being evened out."*

The heat equation is the simplest *parabolic* partial differential
equation. Its qualitative properties – smoothing, maximum principle,
energy decay – are the didactic blueprint for everything that happens
in the Ricci flow.

## 1. The equation

On $\mathbb{R}^n$ or a Riemannian manifold $(M, g)$:
$$
\partial_t u = \Delta u, \qquad u(0, x) = u_0(x).
$$
Here $u(t, x)$ is, e.g., the temperature at point $x$ at time $t$, and
$\Delta$ is the Laplacian (see
[Vector Calculus in a Nutshell](vektoranalysis.md)).

The equation says: the time derivative of $u$ equals the Laplacian of
$u$ – i.e. the deviation of $u$ from its local average. *If $u$ is
higher in the surroundings than at the point, $u$ grows; if it is
lower, $u$ falls.*

## 2. Three basic properties

**Smoothing.** Even if $u_0$ is merely continuous (or $L^2$),
$u(t, \cdot)$ is infinitely differentiable for $t > 0$. The heat
equation creates regularity from nothing.

**Maximum principle.** On a compact domain without sources,
$$
\min_x u_0 \le u(t, x) \le \max_x u_0 \qquad \forall t > 0.
$$
Intuitively: hot does not get hotter, cold does not get colder, unless
heat enters from outside.

**Energy decay.** On a compact $M$ without boundary:
$$
\frac{\mathrm{d}}{\mathrm{d}t} \int_M u^2\, \mathrm{d}V = 2\int_M u\, \Delta u\, \mathrm{d}V = -2\int_M |\nabla u|^2\, \mathrm{d}V \le 0.
$$
The $L^2$-norm decreases monotonically; the solution "spreads out".

## 3. Heat kernel on $\mathbb{R}^n$

The fundamental solution with initial datum $\delta_y$ is the **heat
kernel**
$$
K(t, x, y) = (4\pi t)^{-n/2}\, \exp\!\Big(-\frac{|x - y|^2}{4t}\Big).
$$
Every solution with sufficiently nice $u_0$ can be written as
$$
u(t, x) = \int_{\mathbb{R}^n} K(t, x, y)\, u_0(y)\, \mathrm{d}y.
$$
$K$ is a Gaussian whose standard deviation grows like $\sqrt{t}$ –
the characteristic **parabolic scaling** $x \sim \sqrt{t}$, which also
appears in Ricci-flow blow-up
([Act 2, Article 04](../../poincare/ricci-fluss/04-singularitaeten-blowup.md)).

## 4. On a manifold

On $(M, g)$ one replaces $\Delta$ by the Laplace–Beltrami operator
$\Delta_g$. Smoothing and the maximum principle remain valid. The heat
kernel exists too and encodes geometry: on $S^n$ and on hyperbolic
spaces $K_M(t, x, y)$ is known explicitly; in general its asymptotics
yield the **heat-kernel expansion** with curvature invariants as
coefficients – the bridge between spectral and differential geometry.

## 5. Why "Ricci flow = heat equation for the metric"

Linearising the Ricci-flow equation
$\partial_t g = -2\mathrm{Ric}$ around a flat solution in a suitable
gauge (e.g. via DeTurck's trick) yields
$$
\partial_t h_{ij} \approx \Delta_g h_{ij} + \text{curvature terms}.
$$
Up to gauge corrections the Ricci flow is a *heat equation for the
metric tensor*. Its qualitative properties – smoothing, maximum
principle on scalar curvature
([Act 3, Article 02](../../poincare/beweis/02-singularitaeten-dim3.md)),
energy monotonicity of the functionals $\mathcal{F}$, $\mathcal{W}$
([Act 2, Article 05](../../poincare/ricci-fluss/05-perelman-entropie.md))
– are direct relatives of the three heat-equation properties listed
above.

## 6. Conjugate heat equation

For a time-dependent metric $g(t)$ following the Ricci flow, the
**conjugate heat equation**
$$
\partial_\tau u = -\Delta_g u + R\, u, \qquad \tau = T - t,
$$
is the natural counterpart. It appears in the definition of Perelman's
entropy and the reduced length
([Act 2, Article 07](../../poincare/ricci-fluss/07-reduzierte-laenge.md)).

## Cross-references

- Previous: [Vector Calculus in a Nutshell](vektoranalysis.md).
- Application: [Act 2, Hamilton's Ricci flow](../../poincare/ricci-fluss/03-hamiltons-ricci-fluss.md), [Act 2, Singularities and blow-up](../../poincare/ricci-fluss/04-singularitaeten-blowup.md), [Act 2, Perelman entropy](../../poincare/ricci-fluss/05-perelman-entropie.md).

## Sources

- Evans, Lawrence C. (2010). *Partial Differential Equations.* AMS GSM 19, 2nd ed. Ch. 2.3.
- John, Fritz (1991). *Partial Differential Equations.* Springer, 4th ed.
- Grigor'yan, Alexander (2009). *Heat Kernel and Analysis on Manifolds.* AMS/IP.
- Topping, Peter (2006). *Lectures on the Ricci Flow.* Cambridge University Press, Ch. 1.
