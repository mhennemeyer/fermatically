---
title: "Finite Extinction Time"
slug: poincare/beweis/05-endliche-extinktion
series: poincare
part: 5
act: beweis
date: 2026-04-28
status: draft
lang: en
tags:
  - finite-extinction
  - poincare
  - perelman
  - minimal-surfaces
---

# Finite Extinction Time

> *"For any metric $g_0$ on a closed simply connected three-manifold $M$,
> the Ricci flow with surgery starting from $g_0$ becomes extinct in finite
> time."*
> — Perelman, *Finite extinction time for the solutions to the Ricci flow
> on certain three-manifolds*, arXiv:math/0307245, Theorem 1.1

In [Article 04](04-long-time-verhalten.md) we proved geometrization via
the thin–thick decomposition – Perelman's *actual* result. For the
**Poincaré conjecture** alone, however, there is a much shorter route:
if $M$ is simply connected, the Ricci flow with surgery already
disappears in **finite time**. This article follows Perelman *0307245*
together with the parallel work of Colding & Minicozzi (2005).

## 1. What does "extinction" mean?

A solution of Ricci flow with surgery is called **finitely extinct** if
there is a $T < \infty$ with $M_t = \emptyset$ for all $t \ge T$ – i.e.
from time $T$ on, *every* component has been recognized as a spherical
space form $S^3/\Gamma$ and discarded by surgery. In other words: the
algorithm of [Article 03](03-chirurgie.md) terminates instead of
accumulating infinitely many surgery times.

This is a *topological* statement in analytic disguise: if the manifold
consists only of spherical components, the flow detects this through a
globally growing positive curvature and extinguishes everything.

## 2. Key idea: area of minimal surfaces under the flow

Perelman's strategy is not analytic (volume or curvature estimates) but
**topological-geometric**: one considers 2-spheres in $M$ that would
function as obstacles to extinction under the flow, and shows that their
minimal area decreases monotonically – fast enough to hit zero in finite
time.

### 2.1 The functional $W_2$ (for $\pi_2(M) \neq 0$)

Let $M$ be compact with $\pi_2(M) \neq 0$. For each non-trivial class
$\alpha \in \pi_2(M)$ define
$$
W_2(g, \alpha) := \inf\{\,\mathrm{Area}_g(f)\ :\ f : S^2 \to M,\ [f] = \alpha\,\}.
$$
This is the minimal **harmonic 2-sphere area** in the class $\alpha$ –
existence by Sacks–Uhlenbeck (1981).

**Lemma (Perelman 0307245, §2).** Along Ricci flow the function
$t \mapsto W_2(g(t), \alpha)$ satisfies the differential inequality
$$
\frac{d}{dt} W_2(g(t), \alpha) \le -4\pi - \tfrac{1}{2} R_{\min}(t)\, W_2(g(t), \alpha),
$$
where $R_{\min}(t) = \min_{x \in M_t} R(x, t)$ is the minimal scalar
curvature.

This is the central differential inequality of the proof. It says: even
if $R_{\min} \le 0$, $W_2$ decreases by at least $4\pi$ per unit time,
because the mean curvature of the minimal surface is bounded by the
Gauss–Bonnet constant $4\pi \chi(S^2) / 2 = 4\pi$. Consequence:
$W_2 \to 0$ in finite time, which is only possible if the class $\alpha$
vanishes, i.e. the corresponding $S^2$ in the prime decomposition has
been encapsulated by surgery.

### 2.2 The functional $W_3$ (for $\pi_3(M) \neq 0$)

If $\pi_2(M) = 0$ but $\pi_1(M) = 0$ and $M$ is 3-dimensional, the
Hurewicz sequence yields $\pi_3(M) \cong H_3(M; \mathbb{Z}) \cong
\mathbb{Z}$. Instead of 2-spheres one then considers **families** of
2-spheres, parametrized by $S^1$ (continuous loops in the space of maps
$S^2 \to M$ with constant initial and terminal map). Such families
represent classes in $\pi_1(\Lambda M, *) \cong \pi_3(M)$.

For a non-trivial class $\beta \in \pi_3(M)$ define:
$$
W_3(g, \beta) := \inf_{[\gamma] = \beta}\ \max_{s \in S^1} \mathrm{Area}_g(\gamma(s)).
$$

**Lemma (Perelman 0307245, §3; Colding–Minicozzi 2005).**
$$
\frac{d}{dt} W_3(g(t), \beta) \le -4\pi - \tfrac{1}{2} R_{\min}(t)\, W_3(g(t), \beta).
$$

The inequality is *structurally identical* to the one for $W_2$: it
follows from a min-max construction and the Gauss–Bonnet theorem. Again
it forces $W_3 \to 0$ in finite time.

## 3. Main theorem and corollary

**Theorem (Perelman 0307245, Theorem 1.1).** Let $M$ be a closed
oriented 3-manifold without aspherical or infinite-$\pi_1$ factors in its
prime decomposition. Then the Ricci flow with surgery from
[Article 03](03-chirurgie.md) becomes extinct in finite time for *every*
initial metric.

**Corollary (the case relevant to the proof).** If $M$ is simply
connected, the flow becomes extinct in finite time.

Sketch of the corollary: from $\pi_1(M) = 0$ and Hurewicz one obtains
$\pi_3(M) \neq 0$ ($\cong \mathbb{Z}$ for a sphere, $\cong \mathbb{Z}^k$
for a connected sum). The $W_3$-inequality forces finite extinction: the
flow cannot exist for all times without resolving every non-trivial
class in $\pi_2$ and $\pi_3$ via surgery. Since the algorithm discards
every such resolution as a spherical space form, nothing remains in the
end.

## 4. Two independent proofs

| Author | Preprint | Strategy |
|--------|----------|----------|
| Perelman (2003) | arXiv:math/0307245, 7 pp. | min-max over loops, Gauss–Bonnet, $W_3$ |
| Colding & Minicozzi (2005) | arXiv:math/0308090, 16 pp. | Birkhoff min-max, harmonic replacement |

Both use the idea "2-spheres shrink under Ricci flow because of
Gauss–Bonnet"; Colding & Minicozzi provide a fully worked-out version
that today serves as the standard reference (*Annals of Math.* 2008).

## 5. What extinction does *not* deliver

Finite extinction only detects *that* the manifold consists of spherical
space forms. It yields no **structural statement about hyperbolic or
Seifert-fibered pieces** – for that one still needs the thin–thick
decomposition from [Article 04](04-long-time-verhalten.md). For the full
geometrization the extinction argument is *not* sufficient.

| Conjecture | needs extinction? | needs thin–thick? |
|------------|-------------------|--------------------|
| Poincaré (simply connected) | yes (shortcut) | no |
| Spherical space-form ($\pi_1$ finite) | yes | no |
| Full geometrization | no | yes |

## 6. Which obstacles fall now

| Obstacle (cf. [Article 01](01-hamiltons-programm.md)) | Resolution |
|-----------|------------|
| O5: read topology off the limit, *especially* for simply connected $M$ | $\pi_3 \neq 0 \Rightarrow$ $W_3$-monotonicity $\Rightarrow$ finite extinction |
| O3' (variant): rule out infinitely many surgery times | $W_3 \to 0$ in finite time terminates the algorithm |

## Cross-references

- Previous: [Ricci flow with surgery](03-chirurgie.md) – supplies the algorithm whose termination we prove here.
- Previous: [Long-time behavior](04-long-time-verhalten.md) – the long route via full geometrization.
- Topology background: [sphere & simple connectivity](../topologie/03-sphaere-einfacher-zusammenhang.md), [the Poincaré conjecture](../topologie/04-was-ist-poincare-vermutung.md).
- Next: [Geometrization implies Poincaré](06-poincare-aus-geometrisierung.md) – the closing topological argument.

## Sources

- Perelman, G. (2003). *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds*. arXiv:math/0307245.
- Colding, T. H. & Minicozzi, W. P. (2005). *Estimates for the extinction time for the Ricci flow on certain 3-manifolds and a question of Perelman*. J. Amer. Math. Soc. 18, 561–569. arXiv:math/0308090.
- Colding, T. H. & Minicozzi, W. P. (2008). *Width and finite extinction time of Ricci flow*. Geom. Topol. 12, 2537–2586.
- Sacks, J. & Uhlenbeck, K. (1981). *The existence of minimal immersions of 2-spheres*. Ann. of Math. 113, 1–24.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. AMS, Chapter 18 – worked-out extinction proof.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, §§94–96.
