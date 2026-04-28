---
title: "Vector Calculus in a Nutshell"
slug: vorwissen/geometrie-analysis/vektoranalysis
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: en
tags:
  - vector-calculus
  - gradient
  - divergence
  - laplacian
---

# Vector Calculus in a Nutshell

> *"Gradient, divergence, and the Laplacian are the three tools that
> let differential geometry and analysis speak the same language."*

Vector calculus provides the analytical tools without which neither the
heat equation nor the Ricci flow could be formulated. Here the
$\mathbb{R}^n$ concepts are recalled briefly and immediately
generalised to Riemannian manifolds.

## 1. Gradient

On $\mathbb{R}^n$: for a smooth function $f$,
$$
\nabla f = \big(\partial_1 f, \dots, \partial_n f\big).
$$

On a Riemannian manifold $(M, g)$: the gradient is the vector
representing the differential,
$$
g(\nabla f, X) = \mathrm{d}f(X) = X(f) \quad \forall X.
$$
In coordinates: $(\nabla f)^i = g^{ij}\, \partial_j f$. The gradient is
the vector field of *steepest ascent* of $f$.

## 2. Divergence

On $\mathbb{R}^n$: $\operatorname{div} X = \sum_i \partial_i X^i$.

On $(M, g)$ in local coordinates:
$$
\operatorname{div} X = \frac{1}{\sqrt{\det g}}\, \partial_i \big(\sqrt{\det g}\, X^i\big).
$$
Intuitively $\operatorname{div} X$ measures how much volume is "lost" or
"gained" per unit time under the flow of $X$ – the infinitesimal source
strength of the vector field.

## 3. Laplacian

On $\mathbb{R}^n$:
$$
\Delta f = \operatorname{div}(\nabla f) = \sum_i \partial_i^2 f.
$$

On $(M, g)$ – the **Laplace–Beltrami operator**:
$$
\Delta_g f = \frac{1}{\sqrt{\det g}}\, \partial_i\!\Big(\sqrt{\det g}\, g^{ij}\, \partial_j f\Big).
$$
The Laplacian measures the deviation of a function from its *local
average*. Functions with $\Delta f \equiv 0$ are called **harmonic**.

## 4. Integral theorems

Three classical integral theorems are the foundation of every
analytical geometry:

**Divergence theorem (Gauss).** For $X$ on a compact domain
$\Omega \subset M$ with boundary $\partial \Omega$:
$$
\int_\Omega \operatorname{div} X\, \mathrm{d}V_g = \int_{\partial \Omega} g(X, \nu)\, \mathrm{d}A,
$$
where $\nu$ is the outward unit normal.

**Green's identity.** For $f, h$ on $\Omega$:
$$
\int_\Omega (f\, \Delta h - h\, \Delta f)\, \mathrm{d}V_g = \int_{\partial \Omega} (f\, \partial_\nu h - h\, \partial_\nu f)\, \mathrm{d}A.
$$

**Stokes** (general): for an $(n-1)$-form $\omega$
$$
\int_M \mathrm{d}\omega = \int_{\partial M} \omega.
$$

These theorems allow partial derivatives to be controlled *on average*
by boundary values – a mechanism that appears in every energy estimate
of the Ricci flow.

## 5. Important identities

| Identity | Content |
|----------|---------|
| $\operatorname{div}(fX) = f\operatorname{div} X + g(\nabla f, X)$ | product rule |
| $\Delta(fh) = f\Delta h + h\Delta f + 2 g(\nabla f, \nabla h)$ | product rule for $\Delta$ |
| $\int_M f\, \Delta f\, \mathrm{d}V = -\int_M |\nabla f|^2\, \mathrm{d}V$ | integration by parts (compact $M$, no boundary) |
| $\partial_t \int_M f\, \mathrm{d}V_{g(t)} = \int_M (\partial_t f - f\, R_g)\, \mathrm{d}V_{g(t)}$ | Ricci-flow variant (with $\partial_t g = -2\mathrm{Ric}$, hence $\partial_t \log\sqrt{\det g} = -R$) |

The last line is the elementary identity used in *every* variation of
an integral under the Ricci flow – e.g. in Perelman's monotonicity
proofs ([Act 2, Article 05](../../poincare/ricci-fluss/05-perelman-entropie.md)).

## 6. Why this is central in the Ricci flow

The Ricci flow is a *parabolic* differential equation
$\partial_t g = -2 \mathrm{Ric}$. Its linearisation contains $\Delta$,
and Perelman's energy/entropy functionals are evaluated in closed form
by integration by parts. Without Gauss's divergence theorem and Green's
identities there would be neither the $\mathcal{F}$- nor the
$\mathcal{W}$-functional.

## Cross-references

- Previous: [Tangent Space and Tensors](tangentialraum-tensoren.md), [Curvature of Surfaces](kruemmung-flaechen-gauss.md).
- Continue: [The Heat Equation – Intuition](waermeleitung.md).
- Application: [Act 2, Hamilton's Ricci flow](../../poincare/ricci-fluss/03-hamiltons-ricci-fluss.md), [Act 2, Perelman entropy](../../poincare/ricci-fluss/05-perelman-entropie.md).

## Sources

- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2nd ed. Ch. 2.
- Forster, Otto (2017). *Analysis 3.* Springer Spektrum, 8th ed.
- Marsden, J. & Tromba, A. (2011). *Vector Calculus.* W. H. Freeman, 6th ed.
- do Carmo, Manfredo P. (1992). *Riemannian Geometry.* Birkhäuser. App. A.
