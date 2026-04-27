---
title: "Hamilton's Ricci Flow"
slug: poincare/ricci-fluss/03-hamiltons-ricci-fluss
series: poincare
part: 3
act: ricci-fluss
date: 2026-04-27
status: draft
lang: en
tags:
  - ricci-flow
  - hamilton
---

# Hamilton's Ricci Flow

!!! abstract "Summary"
    Richard Hamilton introduced the evolution equation
    $\partial_t g = -2\,\mathrm{Ric}(g)$ in 1982. It deforms a
    Riemannian metric so that curvature "averages out" like heat. With
    it Hamilton showed that every closed 3-manifold of positive Ricci
    curvature is a spherical space form – the blueprint for Perelman's
    proof.

## 1. The Idea

A metric carries curvature inhomogeneities – strong curvature here,
weak there. In 1982 Hamilton asked: *is there a natural evolution
equation that redistributes a metric so that curvature becomes more
uniform – analogous to the heat equation smoothing out
temperatures?* His proposal:

$$\boxed{\,\frac{\partial g(t)}{\partial t} = -2\,\mathrm{Ric}\bigl(g(t)\bigr)\,}\quad\text{(Hamilton 1982).}$$

Initial condition $g(0) = g_0$. The equation is autonomous in $g$ –
the right-hand side depends on $g$ only through its Ricci curvature
(see [Article 02](02-kruemmung-ricci-tensor.md)).

## 2. Why "Minus Twice Ricci"?

Three observations explain the form.

**(a) Differential-topological naturality.** $\mathrm{Ric}$ is the
unique natural symmetric $(0,2)$-tensor field of second order in $g$
that depends pointwise only on derivatives of $g$ up to order 2. The
sign $-2$ makes the equation **parabolic in its linearisation** –
analogous to the heat equation $\partial_t u = \Delta u$.

**(b) Heat-equation heuristic.** In harmonic coordinates ($\Box x^k = 0$)
one has approximately

$$\frac{\partial g_{ij}}{\partial t} = \Delta_g g_{ij} + \text{lower-order terms}.$$

The metric diffuses like a scalar – with the effect that curvature
spikes get smoothed.

**(c) Variational principle.** Hamilton motivated the equation
through symmetry; later Perelman showed that the Ricci flow is the
**gradient flow** of the $\mathcal{F}$-functional (see
[Article 05](05-perelman-entropie.md)) – a retroactive variational
principle.

## 3. Hamilton's Original Theorem (1982)

In the seminal *Three-manifolds with positive Ricci curvature*
Hamilton proved:

> **Theorem (Hamilton 1982).** Let $(M^3, g_0)$ be a closed
> 3-manifold with $\mathrm{Ric}(g_0) > 0$. Then the Ricci flow
> $g(t)$ exists for all $t \in [0, T)$, and the **normalised** Ricci
> flow converges as $t \to T$ to a metric of constant positive
> sectional curvature. In particular $M$ is diffeomorphic to a
> spherical space form $S^3/\Gamma$.

— Hamilton, *J. Differential Geometry* 17 (1982), 255–306.

The proof combines maximum principles for tensors, careful analysis
of the curvature tensor under the flow, and the fact that in
dimension 3 the Ricci tensor determines the full curvature tensor
(Article 02, §6).

## 4. Short-Time Existence and Uniqueness

The equation is not strictly parabolic (it has a diffeomorphism gauge
freedom), but DeTurck's trick converts it into a parabolic one by
adding a Lie-derivative term that fixes a gauge. Hence:

> **Short-time existence.** For every smooth initial metric $g_0$ on
> a closed manifold there exists $T > 0$ and a unique solution
> $g(t)$ of the Ricci flow on $[0, T)$.

— Hamilton 1982 (existence), DeTurck 1983 (simplified proof).

## 5. Scaling Behaviour

The Ricci flow is not scale-invariant. Rescaling $g \mapsto \lambda^2 g$
also rescales time: $\mathrm{Ric}$ is scale-invariant, but $\partial_t$
carries the factor $\lambda^{-2}$. Consequences:

- On an **Einstein initial metric** $\mathrm{Ric}(g_0) = \lambda g_0$
  the solution is $g(t) = (1 - 2\lambda t)\, g_0$. For $\lambda > 0$
  the sphere collapses to a point in finite time; for $\lambda < 0$
  hyperbolic space expands without bound.
- The **normalised Ricci flow**
  $\partial_t g = -2\,\mathrm{Ric} + \tfrac{2}{n}\bar R\, g$
  preserves volume; Einstein metrics become genuine fixed points.

## 6. Examples

**Round sphere.** On $(S^3, g_{\mathrm{round}})$,
$\mathrm{Ric} = 2\, g_{\mathrm{round}}$. Solution:
$g(t) = (1 - 4t)\, g_{\mathrm{round}}$, singular at $T = 1/4$
(shrinking soliton).

**Flat torus.** On $T^3$ with the flat metric, $\mathrm{Ric} = 0$,
so $g(t) \equiv g_0$ – static.

**Hyperbolic space form.** $\mathrm{Ric} = -2\, g$ gives
$g(t) = (1 + 4t)\, g$ – eternal expansion.

**Cylinder $S^2 \times \mathbb{R}$.** The $S^2$ factor shrinks, the
$\mathbb{R}$ factor stays still – the solution degenerates after
finite time to a line. This "neck pinch" is the model case of a
**neckpinch singularity** (see [Article 04](04-singularitaeten-blowup.md)).

## 7. What the Flow Controls

Under the Ricci flow many curvature quantities satisfy their own
evolution equations, inviting **maximum principle arguments**:

- $\partial_t R = \Delta R + 2\,\lvert\mathrm{Ric}\rvert^2$
  – scalar curvature satisfies a heat equation with non-negative
  source term; in particular $R \ge 0$ is preserved.
- $\partial_t \mathrm{Ric} = \Delta_L \mathrm{Ric}$
  (Lichnerowicz Laplacian) – the Ricci tensor diffuses.
- Diameter, volume and curvature bounds propagate through explicit
  comparison estimates.

This is the toolbox Hamilton used in 1982 and that Perelman expanded
decisively in 2002–03.

## 8. What the Flow *Cannot* Do

Three problems remained open after Hamilton and shaped the research
programme of the next twenty years:

1. **Singularity formation.** The flow breaks down in finite time
   before a smooth limit metric is reached – e.g. the neckpinch.
2. **Collapse.** Volume can vanish locally, invalidating comparison
   theorems.
3. **Topology change.** To continue past a singularity one must cut
   the manifold ("surgery"), change topology and restart the flow.

The tools to address these – the $\mathcal{F}$- and
$\mathcal{W}$-entropy, $\kappa$-non-collapse, reduced length and
canonical neighbourhoods – follow in Articles 04–07.

## Sources

- Richard S. Hamilton, *Three-manifolds with positive Ricci curvature*, J. Differential Geom. 17 (1982), 255–306.
- Richard S. Hamilton, *The formation of singularities in the Ricci flow*, Surveys Diff. Geom. 2 (1995), 7–136.
- Bennett Chow & Dan Knopf, *The Ricci Flow: An Introduction*, AMS Math. Surveys 110 (2004).
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §3.

## Cross References

- Previous article: [Curvature and the Ricci tensor](02-kruemmung-ricci-tensor.md)
- Next article: [Singularities and blow-up limits](04-singularitaeten-blowup.md)
- Act 1, Article 04: [What is the Poincaré conjecture?](../topologie/04-was-ist-poincare-vermutung.md)
