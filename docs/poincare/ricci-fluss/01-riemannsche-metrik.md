---
title: "Riemannian Metric"
slug: poincare/ricci-fluss/01-riemannsche-metrik
series: poincare
part: 1
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - riemannian-geometry
  - metric
---

# Riemannian Metric

!!! abstract "Summary"
    A Riemannian metric is the additional structure that endows a smooth
    manifold with lengths, angles and volumes. It is the fundamental
    object that Hamilton's Ricci flow deforms in time — without a metric
    there is no curvature, and without curvature there is no Ricci flow.

## 1. From Topology to Geometry

In Act 1 ([Article 02](../topologie/02-mannigfaltigkeiten.md))
manifolds were introduced as spaces that locally look like
$\mathbb{R}^n$. A smooth manifold knows only its topological and
differentiable structure: which functions are smooth, which vector
fields exist. It does **not** know how *long* a vector is or what
*angle* two vectors enclose.

This is exactly what a **Riemannian metric** supplies. It turns a
smooth manifold into a **Riemannian manifold** $(M, g)$ and is the
smallest extra structure with which one can do classical geometry.

## 2. Definition

Let $M$ be a smooth $n$-manifold. A **Riemannian metric** $g$ assigns
to every point $p \in M$ an inner product
$g_p \colon T_pM \times T_pM \to \mathbb{R}$ on the tangent space that
is

- **bilinear** in both arguments,
- **symmetric** ($g_p(v,w) = g_p(w,v)$),
- **positive definite** ($g_p(v,v) \ge 0$ with equality only for $v = 0$),

and depends **smoothly** on $p$. In local coordinates $(x^1,\dots,x^n)$
one writes

$$g = g_{ij}(x)\, dx^i \otimes dx^j,$$

with $\bigl(g_{ij}(p)\bigr)$ symmetric and positive definite.
Einstein's summation convention is used silently throughout.

> "A Riemannian metric on a smooth manifold $M$ is a smooth, symmetric,
> positive-definite 2-tensor field on $M$."
> — John M. Lee, *Introduction to Riemannian Manifolds* (2018), p. 11

## 3. What the Metric Buys Us

Once $g$ is in place, all classical geometric quantities are defined.

**Length of a vector.** For $v \in T_pM$:
$\lvert v\rvert_g = \sqrt{g_p(v,v)}$.

**Angle.** Between $v, w \in T_pM \setminus\{0\}$:

$$\cos\theta = \frac{g_p(v,w)}{\lvert v\rvert_g\,\lvert w\rvert_g}.$$

**Arc length** of a curve $\gamma\colon [a,b]\to M$:

$$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}\bigl(\dot\gamma(t),\dot\gamma(t)\bigr)}\,dt.$$

**Riemannian distance.** $d_g(p,q) = \inf_\gamma L(\gamma)$, the
infimum being taken over all piecewise smooth curves from $p$ to $q$.
$(M, d_g)$ becomes a metric space whose topology agrees with the
underlying manifold topology.

**Volume form.** In oriented charts:

$$d\mathrm{vol}_g = \sqrt{\det(g_{ij})}\,dx^1 \wedge \cdots \wedge dx^n.$$

This gives volumes of subsets, integrals of smooth functions and –
through the Hessian of $g$ – curvature quantities (see
[Article 02](02-kruemmung-ricci-tensor.md)).

## 4. Examples

**Euclidean space.** On $\mathbb{R}^n$ the flat standard metric is
$g_{\mathrm{eucl}} = \delta_{ij}\,dx^i\,dx^j$ — lengths, angles and
volume are the familiar ones.

**Sphere $S^n$.** Embedded in $\mathbb{R}^{n+1}$, $S^n$ inherits the
**round metric** $g_{\mathrm{round}}$ as the restriction of the
Euclidean inner product to the tangent space. Great circles are
geodesics; the sectional curvature is constant equal to $1$ on the
unit sphere.

**Hyperbolic space $\mathbb{H}^n$.** On the upper half space
$\{(x^1,\dots,x^n) : x^n > 0\}$ the metric
$g_{\mathrm{hyp}} = (x^n)^{-2}\,\delta_{ij}\,dx^i\,dx^j$
has constant sectional curvature $-1$.

**Product metrics.** On $M \times N$, $g_M \oplus g_N$ combines the
factors — for example the standard metric on $T^2 = S^1 \times S^1$ or
on $S^2 \times \mathbb{R}$.

**Squashed sphere.** Scaling the round $S^2$ in one direction yields
an ellipsoid. Topologically still a 2-sphere; geometrically curvature,
geodesics and volume change.

## 5. Existence and Variety

A basic observation: every paracompact smooth manifold admits at least
one Riemannian metric. The proof glues local coordinate metrics with a
partition of unity, transferring positive definiteness to the global
object (Lee 2018, Prop. 2.4).

More importantly: on a fixed smooth manifold the **infinite-dimensional**
space $\mathcal{M}(M)$ of Riemannian metrics is the actual playground
of the Ricci flow: a starting metric $g_0$ becomes a one-parameter
family $g(t)$ — a trajectory in $\mathcal{M}(M)$ (see
[Article 03](03-hamiltons-ricci-fluss.md)).

## 6. The Levi-Civita Connection

A Riemannian metric canonically induces a **connection** $\nabla$ on
the tangent bundle — the **Levi-Civita connection**. It is
characterised by two properties:

- **Torsion-free:** $\nabla_X Y - \nabla_Y X = [X,Y]$.
- **Metric-compatible:** $X(g(Y,Z)) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$.

The fundamental theorem of Riemannian geometry says these two
conditions determine $\nabla$ uniquely. The associated Christoffel
symbols

$$\Gamma^k_{ij} = \tfrac{1}{2}\,g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr)$$

are the computational backbone of curvature and geodesics.

## 7. Geodesics

A **geodesic** is a curve $\gamma$ with
$\nabla_{\dot\gamma}\dot\gamma = 0$ — it travels "as straight as
possible". Geodesics generalise straight lines in $\mathbb{R}^n$ and
great circles on $S^n$. In coordinates:

$$\ddot\gamma^k + \Gamma^k_{ij}\,\dot\gamma^i\,\dot\gamma^j = 0.$$

Locally geodesics are the shortest connections; globally that holds
only with extra assumptions (such as completeness). The Hopf-Rinow
theorem ties metric completeness to geodesic completeness.

## 8. Why the Metric Is Central in Act 2

Hamilton's Ricci flow is the evolution equation

$$\frac{\partial g(t)}{\partial t} = -2\,\mathrm{Ric}(g(t)).$$

It is a partial differential equation **for the metric itself**. All
geometric quantities the next articles work with — curvature tensors,
volume, diameter, entropy functionals — are functions of $g$. Anyone
who wants to understand the flow must first understand what a metric
is and how it changes when one "wiggles" it.

## Sources

- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer (2018), Ch. 2.
- Manfredo do Carmo, *Riemannian Geometry*, Birkhäuser (1992), Ch. 1–3.
- Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer (2016), Ch. 2.

## Cross References

- Prerequisite: [Article 02 – Manifolds](../topologie/02-mannigfaltigkeiten.md)
- Next article: [Curvature and the Ricci tensor](02-kruemmung-ricci-tensor.md)
- Background: [Geometry and Analysis (build-up)](../../vorwissen/index.md)
