---
title: "Long-time Behavior and Thin–Thick Decomposition"
slug: poincare/beweis/04-long-time-verhalten
series: poincare
part: 4
act: beweis
date: 2026-04-27
status: draft
lang: en
tags:
  - long-time
  - thin-thick
  - geometrization
  - perelman
---

# Long-time Behavior and Thin–Thick Decomposition

> *"The thick part has bounded geometry and consists of hyperbolic pieces, while
> the thin part collapses with bounded curvature."*
> — Perelman, *Ricci flow with surgery on three-manifolds*, arXiv:math/0303109, §§6–7

In [Article 03](03-chirurgie.md) we showed that the Ricci flow with surgery
exists on $[0, \infty)$ for every closed, oriented 3-manifold. With this
the flow is rescued as an analytic object – but we still do not know *what*
the manifold becomes as $t \to \infty$. This article follows Perelman
*0303109* §§6–7 and shows that the flow asymptotically falls into
identifiable pieces: hyperbolic components and so-called graph manifolds –
the last piece of the geometrization puzzle.

## 1. Rescaling and the right scale

Looking directly at $g(t)$ as $t \to \infty$ is meaningless: on a hyperbolic
piece the diameter grows linearly and the curvature decays like $1/t$. The
correct quantity is the **rescaled metric**

$$
\hat g(t) := \frac{1}{4t}\, g(t).
$$

The factor $1/(4t)$ is chosen so that a constant hyperbolic metric of
sectional curvature $-1/(4t)$ becomes stationary under $\hat g(t)$. The
Ricci-flow system is thereby turned into an *asymptotic soliton flow*
whose fixed points are exactly hyperbolic metrics of sectional curvature
$-1/4$.

## 2. The thin–thick decomposition

Let $w > 0$ be a small parameter. For each time $t > 0$ define

$$
M_{\text{thick}}(w, t) = \{\, x \in M_t \ \big| \ \mathrm{vol}(B_{\hat g(t)}(x, 1)) \ge w \,\},
\qquad
M_{\text{thin}}(w, t) = M_t \setminus M_{\text{thick}}(w, t).
$$

On the **thick part** the volume of a unit ball is bounded below – by the
$\kappa$-non-collapse theorem the curvature is then $C^k$-controlled and
Cheeger–Gromov convergence arguments apply. On the **thin part** the
volume collapses without the curvature blowing up: precisely the kind of
collapse forbidden locally by $\kappa$-non-collapse is *allowed* here
globally.

## 3. Convergence of the thick pieces to hyperbolic geometry

**Theorem (Perelman 0303109 §7.3, hyperbolization of the thick part).**
For every sequence $t_i \to \infty$ there is a subsequence, a finite
collection of complete hyperbolic 3-manifolds of finite volume
$(H_1, h_1), \dots, (H_k, h_k)$, and a sequence of smooth maps
$$
\varphi_i : H_1 \sqcup \dots \sqcup H_k \to M_{t_i}
$$
such that $\varphi_i^* \hat g(t_i) \to h_1 \sqcup \dots \sqcup h_k$ in
$C^\infty_{\text{loc}}$.

The images $\varphi_i(H_j)$ are called **persistent hyperbolic pieces**.
They are bounded by *embedded incompressible 2-tori* in $M_t$ – tori whose
fundamental group injects into $\pi_1(M)$. These tori become the cutting
surfaces of the **JSJ decomposition** in Act 3 (cf.
[geometrization conjecture](../topologie/05-geometrisierungs-vermutung.md)).

## 4. The thin part: collapse with bounded curvature

The thin part is analytically more dramatic. Here Perelman invokes a
theorem from the **Cheeger–Fukaya–Gromov theory of collapse**:

**Theorem (Perelman 0303109 §7.4, collapsing theorem).** There is
$w_0 > 0$ such that for $w < w_0$ and all sufficiently large $t$ the thin
part $M_{\text{thin}}(w, t)$ is a *graph manifold*, i.e. a 3-manifold that
decomposes along embedded incompressible tori into **Seifert-fibered**
pieces.

Perelman only sketched the full proof; it was completed in two independent
works:

- Shioya & Yamaguchi (2005), *Volume collapsed three-manifolds with a
    lower curvature bound*. Math. Ann. 333.
- Kleiner & Lott (2014), *Locally collapsed 3-manifolds*. Astérisque 365 –
    today's canonical proof, with no lower curvature bound assumed.

## 5. Putting it together: geometrization

Combining the thick (hyperbolic) and thin (Seifert-fibered) pieces with
the components removed by surgery in [Article 03](03-chirurgie.md) as
spherical space forms yields:

| Decomposition layer | Originates from |
|---------------------|------------------|
| prime decomposition | neck cuts of surgery |
| spherical space forms $S^3/\Gamma$ | discarded components |
| hyperbolic pieces | persistent thick part |
| Seifert-fibered pieces | thin part with bounded curvature |
| JSJ tori | boundary tori between thick and thin |

This is – piece by piece – exactly Thurston's
**geometrization conjecture** (cf. [Act 1, Article 05](../topologie/05-geometrisierungs-vermutung.md)).
The main theorem is therefore proved for *every* closed, oriented
3-manifold.

## 6. What does not follow immediately

The proof sketched here gives geometrization with possibly *infinitely
many* surgeries on $[0, \infty)$. For the Poincaré conjecture a much
shorter argument suffices: if $M$ is simply connected, the flow becomes
extinct in **finite time**. This **extinction theorem** is Perelman's
third preprint *0307245*; we treat it in
[Article 05: finite extinction](05-endliche-extinktion.md). Only with that
is the Poincaré conjecture provable *without* the full thin–thick
machinery (although geometrization will still need it).

## 7. Which obstacles fall now

| Obstacle (cf. [Article 01](01-hamiltons-programm.md)) | Resolution in this article |
|-----------|----------------------------|
| O4: long-time existence is not enough | rescaled metric $\hat g = g/(4t)$ |
| O4': convergence on hyperbolic pieces | Cheeger–Gromov on $M_{\text{thick}}$ |
| O4'': what happens on $M_{\text{thin}}$? | collapsing theorem → Seifert-fibered graph manifolds |
| O5 (partial): read topology off the limit | thick = hyperbolic, thin = Seifert, boundaries = JSJ tori |

## Cross-references

- Previous: [Ricci flow with surgery](03-chirurgie.md) – supplies the flow on $[0, \infty)$.
- Tools from Act 2: [κ-non-collapse](../ricci-fluss/06-kappa-nichtkollaps.md), [reduced length](../ricci-fluss/07-reduzierte-laenge.md).
- Topology from Act 1: [geometrization conjecture](../topologie/05-geometrisierungs-vermutung.md).
- Next: [finite extinction](05-endliche-extinktion.md) – the shortcut to the Poincaré conjecture.

## Sources

- Perelman, G. (2003). *Ricci flow with surgery on three-manifolds*. arXiv:math/0303109, §§6–7.
- Morgan, J. & Tian, G. (2014). *The Geometrization Conjecture*. CMI/AMS – worked-out long-time argument.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, §§90–93.
- Kleiner, B. & Lott, J. (2014). *Locally collapsed 3-manifolds*. Astérisque 365 – collapsing theorem without lower curvature bound.
- Shioya, T. & Yamaguchi, T. (2005). *Volume collapsed three-manifolds with a lower curvature bound*. Math. Ann. 333.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10, §§7.5–7.7.
