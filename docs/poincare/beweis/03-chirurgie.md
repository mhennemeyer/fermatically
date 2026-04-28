---
title: "Ricci Flow with Surgery"
slug: poincare/beweis/03-chirurgie
series: poincare
part: 3
act: beweis
date: 2026-04-27
status: draft
lang: en
tags:
  - chirurgie
  - surgery
  - ricci-flow
  - perelman
---

# Ricci Flow with Surgery

> *"We construct a solution which is a smooth Ricci flow on its time-of-definition,
> punctuated by a discrete set of surgery times at which the metric is modified."*
> — Perelman, *Ricci flow with surgery on three-manifolds*, arXiv:math/0303109 (2003)

In [Article 02](02-singularitaeten-dim3.md) we understood the singularities of
the Ricci flow in dimension 3 locally: every high-curvature region looks like
a neck, a cap, or a spherical space form. In this article we follow Perelman's
second preprint *0303109* and assemble these local pieces into a **global
flow with surgery** that continues across each singularity – the technical
heart of the proof of the geometrization conjecture.

## 1. The idea: cut just before the singularity

Hamilton's original program failed at obstacle **O3** from
[Article 01](01-hamiltons-programm.md): understanding singularities locally is
not enough; one must *operatively* remove them, without the proof
disintegrating into endless special cases.

Perelman's solution is strikingly simple in principle:

1. **Watch** the flow until the curvature first exceeds a fixed threshold
    $\Omega$ at some point (just before the singularity).
2. **Localize** the high-curvature region using the canonical neighborhood
    theorem – it splits into necks, caps, and compact components that are
    spherical space forms.
3. **Cut** along the central 2-sphere of every neck and glue in a
    **standard solution** (a fixed, explicit metric on $D^3$).
4. **Discard** compact components already identified as spherical space
    forms – they are topologically known and contribute nothing further to
    the flow.
5. **Resume** the Ricci flow on the modified manifold smoothly until the
    next singularity occurs.

The result is a sequence $(M_t, g(t))$ of smooth Ricci flows on time
intervals $[t_{i-1}, t_i]$ separated by a **discrete** set of surgery times
$0 < t_1 < t_2 < \dots$.

## 2. δ-necks and the cut locus

A precise cut requires a neck that is "thin enough." Let $\delta > 0$ be a
small parameter.

**Definition (δ-neck).** A point $(x, t)$ lies in a $\delta$-neck of scale
$r$ if the parabolic rescaling of $g(t)$ around $x$ is $\delta$-close in
$C^{\lfloor 1/\delta \rfloor}$ to the round cylindrical model
$S^2_1 \times (-1/\delta, 1/\delta)$.

**Lemma (existence of a $\delta$-neck, 0303109 §4).** For all sufficiently
small $\delta$, there is a curvature bound $h(\delta)$ such that every point
with $|\mathrm{Rm}|(x,t) \ge h(\delta)$ that lies in an $\varepsilon$-neck
(in the sense of Act 2, [Article 06](../ricci-fluss/06-kappa-nichtkollaps.md))
contains a *central* $\delta$-neck.

The cut locus is chosen on the central 2-sphere $\Sigma$ of such a neck. The
finer condition $\delta \ll \varepsilon$ ensures that the neck is long and
thin enough to splice in a standard solution without disturbing the future
curvature evolution.

## 3. The standard solution

The *standard solution* is a fixed, complete, asymptotically cylindrical
metric $\bar g$ on $\mathbb{R}^3$ with the following properties (0303109 §2,
worked out in Cao–Zhu §7.3):

- $\bar g$ is rotationally symmetric and has positive sectional curvature.
- Outside a large ball, $(\mathbb{R}^3, \bar g)$ is isometric to the round
    half-cylinder $S^2_1 \times [0, \infty)$.
- The Ricci flow with initial datum $\bar g$ exists smoothly on $[0, 1)$,
    shrinks to a point at $t = 1$, and is $\kappa$-non-collapsed.

The standard solution serves as a **model cap**: after the cut, the
unwanted neck piece is replaced by a chunk of $\bar g$, smoothly glued
through a cut-off function. Existence and uniqueness of its flow is itself a
technical theorem (Cao–Zhu, Kleiner–Lott Ch. 12).

## 4. The surgery algorithm

The construction depends on three parameter sequences chosen
*simultaneously*:

| Parameter | Role |
|-----------|------|
| $\varepsilon_i \to 0$ | accuracy of the canonical neighborhood |
| $\delta_i \to 0$ | quality of the neck at the cut, $\delta_i \ll \varepsilon_i$ |
| $r_i \to 0$ | scale at which canonical neighborhoods kick in |
| $h_i \to 0$ | surgery threshold, $h_i \ll \delta_i r_i$ |

**Definition (Ricci flow with surgery).** A family
$\{(M_t, g(t))\}_{t \ge 0}$ is a *Ricci flow with $(r, \delta)$-surgery* if
on each interval $[t_{i-1}, t_i)$ it satisfies $\partial_t g = -2\,\mathrm{Ric}$
smoothly, surgery is performed at all $\delta_i$-necks at times $t_i$, and
the canonical neighborhood property with parameters $(\varepsilon_i, r_i)$
is preserved up to $t_i$.

## 5. The surgery theorem (0303109 §5)

**Theorem (Perelman, surgery exists globally).** For every closed,
oriented 3-manifold $(M, g_0)$ there exist sequences
$\varepsilon_i, \delta_i, r_i, h_i \to 0$ such that a Ricci flow with
$(r, \delta)$-surgery on $[0, \infty)$ exists.

The central difficulty is the **inductive loop**: to keep canonical
neighborhoods alive at the step $i \to i+1$ one needs $\kappa$-non-collapse
**despite** the previous surgeries. Perelman shows:

- Local $\kappa$-non-collapse ([Article 06 in Act 2](../ricci-fluss/06-kappa-nichtkollaps.md))
    persists under surgery, provided $\delta_i$ is chosen small enough.
- The number of surgeries on every finite time interval is finite, since
    each one removes a fixed amount of volume ($\ge c\, h_i^3$).

## 6. What surgery does *not* destroy

Surgery is designed to preserve every structure essential to the proof:

- **Hamilton–Ivey pinching** (cf. [Article 02](02-singularitaeten-dim3.md))
    survives every surgery step because the standard solution itself has
    positive curvature.
- **κ-non-collapse** survives with a smaller but positive constant $\kappa'$.
- **Topological bookkeeping**: every removed component is a spherical space
    form $S^3/\Gamma$; every surgery replaces a neck $S^2 \times I$ by two
    caps $D^3$. Both are exactly the two standard moves of a
    **prime decomposition** (cf.
    [geometrization conjecture](../topologie/05-geometrisierungs-vermutung.md)).

The topology of the original manifold can therefore be reconstructed
exactly from the removed pieces plus the long-time limit of the flow – the
bridge built in [Article 06](06-poincare-aus-geometrisierung.md).

## 7. What remains to show

With the surgery theorem the **flow as an analytic object** is rescued. Two
questions remain for Act 3:

- **What happens as $t \to \infty$?** – treated in
    [Article 04: long-time behavior](04-long-time-verhalten.md).
- **Does the flow stop in finite time when $M$ is simply connected?** –
    Perelman's third preprint *0307245*, treated in
    [Article 05: finite extinction](05-endliche-extinktion.md).

## Summary

| Obstacle (Act 3, [Article 01](01-hamiltons-programm.md)) | Resolution in this article |
|-----------|----------------------------|
| O3: remove singularities operatively | surgery algorithm with $(\delta, r, h)$ parameters |
| O3': algorithm yields only finitely many cuts | volume argument $\ge c\, h^3$ per surgery |
| O3'': pinching/κ-non-collapse after surgery | standard solution has positive curvature; local κ-non-collapse persists |
| O3''': topology stays trackable | cuts = prime decomposition, removed pieces = $S^3/\Gamma$ |

## Cross-references

- Previous: [Singularity analysis in dim 3](02-singularitaeten-dim3.md) – supplies the canonical neighborhoods.
- Tools: [κ-non-collapse](../ricci-fluss/06-kappa-nichtkollaps.md), [reduced length](../ricci-fluss/07-reduzierte-laenge.md).
- Topology: [geometrization conjecture](../topologie/05-geometrisierungs-vermutung.md), [what is the Poincaré conjecture?](../topologie/04-was-ist-poincare-vermutung.md).
- Next: [long-time behavior and thin–thick decomposition](04-long-time-verhalten.md).

## Sources

- Perelman, G. (2003). *Ricci flow with surgery on three-manifolds*. arXiv:math/0303109.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. AMS, Ch. 13–17.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, 2587–2855, §§57–72.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10, §7.
- Hamilton, R. (1997). *Four-manifolds with positive isotropic curvature*. Comm. Anal. Geom. 5 – original surgery idea in dim 4.
