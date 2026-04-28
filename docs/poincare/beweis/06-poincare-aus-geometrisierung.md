---
title: "Geometrization Implies Poincaré"
slug: poincare/beweis/06-poincare-aus-geometrisierung
series: poincare
part: 6
act: beweis
date: 2026-04-28
status: draft
lang: en
tags:
  - geometrization
  - corollary
  - poincare
  - prime-decomposition
---

# Geometrization Implies Poincaré

> *"The Poincaré conjecture is a consequence of the geometrization
> conjecture; in this sense Perelman proved much more than was asked."*
> — Morgan & Tian, *Ricci Flow and the Poincaré Conjecture*, 2007, preface

In Articles 01–05 of this act we built up Perelman's analytic and
geometric main result: every closed oriented 3-manifold has a
Thurston-style geometrization (Article 04), and for simply connected $M$
the flow even becomes extinct in finite time (Article 05). This closing
article extracts the **Poincaré conjecture** from both results as a
purely topological corollary.

## 1. What needs to be shown

**Poincaré conjecture (3-dim).** Let $M$ be a closed, oriented and
simply connected 3-manifold. Then $M \cong S^3$.

(Cf. [Act 1, Article 04](../topologie/04-was-ist-poincare-vermutung.md)
for Poincaré's original 1904 formulation.)

We give two proofs: one via full geometrization (Articles 01–04) and
the shortcut via finite extinction (Article 05). Both end at the same
point – the classification of **spherical space forms**.

## 2. Topological preliminaries: three building blocks

We need three classical theorems of 3-manifold topology. They hold
*independently* of Ricci flow and are treated more carefully in the
prerequisites and topology sections.

### 2.1 Prime decomposition (Kneser–Milnor 1962)

Every closed oriented 3-manifold decomposes uniquely (up to order) as a
connected sum of **prime** factors:
$$
M = M_1 \,\#\, M_2 \,\#\, \cdots \,\#\, M_k.
$$
A 3-manifold $N$ is *prime* if every embedded 2-sphere in $N$ bounds a
3-ball *or* if $N$ itself is $\cong S^2 \times S^1$.

### 2.2 Van Kampen for the connected sum

For $M = M_1 \# M_2$ one has
$$
\pi_1(M) \cong \pi_1(M_1) \ast \pi_1(M_2)
$$
(free product). **Consequence in our case:** if $\pi_1(M) = 0$, every
prime factor must itself be simply connected.

### 2.3 Spherical space-form theorem

A closed 3-manifold of constant sectional curvature $+1$ is isometric
to a **spherical space form** $S^3/\Gamma$ with $\Gamma \subset
\mathrm{SO}(4)$ a finite, freely acting subgroup (Hopf 1926;
classification: Wolf 2011, *Spaces of Constant Curvature*). In
particular $\pi_1(S^3/\Gamma) = \Gamma$.

## 3. The long route: geometrization $\Rightarrow$ Poincaré

Let $M$ be closed, oriented, $\pi_1(M) = 0$.

**Step 1: prime decomposition applies.** Write $M = M_1 \# \cdots \# M_k$.
Van Kampen (§2.2) gives $\pi_1(M_i) = 0$ for all $i$. It thus suffices to
classify prime simply connected 3-manifolds.

**Step 2: geometrization of each prime factor.** By Perelman
([Article 04](04-long-time-verhalten.md)), each prime factor $M_i$ has a
geometrization decomposition into **pieces of one of the eight Thurston
geometries**. A prime factor decomposes along *incompressible* tori into
pieces, each carrying one of the eight model geometries.

**Step 3: which geometries are compatible with $\pi_1(M_i) = 0$?**
We go through the eight Thurston model geometries (cf.
[Act 1, Article 05](../topologie/05-geometrisierungs-vermutung.md)):

| Model geometry | $\pi_1$ of a closed form |
|----------------|--------------------------|
| $\mathbb{H}^3$ (hyperbolic) | infinite |
| $\widetilde{\mathrm{SL}}_2(\mathbb{R})$ | infinite |
| $\mathbb{H}^2 \times \mathbb{R}$ | infinite ($\mathbb{Z}$ factor) |
| Sol | infinite |
| Nil | infinite (Heisenberg) |
| $\mathbb{E}^3$ (flat) | Bieberbach, infinite |
| $S^2 \times \mathbb{R}$ | infinite ($\mathbb{Z}$ factor) |
| $S^3$ (spherical) | finite |

Only **spherical** geometry $S^3$ admits closed forms with finite (in
particular trivial) fundamental group.

**Step 4: incompressible tori cannot occur.** A simply connected prime
factor contains no *incompressible* 2-torus: such a torus would have
$\pi_1 \cong \mathbb{Z}^2$ injecting into $\pi_1(M_i) = 0$ –
contradiction. So $M_i$ consists of *one* geometry piece.

**Step 5: classification as $S^3$.** Steps 3–4 yield: $M_i$ is a
spherical space form $S^3/\Gamma$. From $\pi_1(M_i) = \Gamma = \{e\}$
(Step 1) we get $M_i \cong S^3$.

**Step 6: $k$ spheres become one.** Since $S^3 \,\#\, S^3 = S^3$ (a
connected sum with $S^3$ does not change the manifold),
$$
M = \underbrace{S^3 \# S^3 \# \cdots \# S^3}_{k\ \text{factors}} = S^3.
$$

$\blacksquare$

## 4. The shortcut: finite extinction $\Rightarrow$ Poincaré

If one wants to avoid full geometrization, the argument shortens. Again
let $\pi_1(M) = 0$.

**Step A:** By [Article 03](03-chirurgie.md) there is a Ricci flow with
surgery $g(t)$ on $[0, \infty)$.

**Step B:** By [Article 05](05-endliche-extinktion.md) this solution
becomes extinct in finite time $T < \infty$ – exactly the content of
Perelman *0307245*.

**Step C:** Finite extinction means: every component that ever appeared
has been recognized as a spherical space form $S^3/\Gamma$ and discarded
by surgery. In particular $M$ is built from *finitely many* spherical
space forms via connected sums – $M = S^3/\Gamma_1 \# \cdots \#
S^3/\Gamma_k$.

**Step D:** Van Kampen yields $\pi_1(M) = \Gamma_1 \ast \cdots \ast
\Gamma_k$. From $\pi_1(M) = 0$ and the fact that free products of
non-trivial groups are non-trivial, we conclude $\Gamma_i = \{e\}$ for
all $i$. Hence $M_i = S^3$ for all $i$, and $M = S^3$.

$\blacksquare$

## 5. The two routes compared

| Aspect | Long route (§3) | Shortcut (§4) |
|--------|-----------------|---------------|
| Perelman papers used | 0211159 + 0303109 §§5–7 | 0211159 + 0303109 §5 + 0307245 |
| Ricci-flow time | $[0, \infty)$ + thin–thick limit | $[0, T]$ with $T < \infty$ |
| Topological heavy lifting | prime decomposition + Thurston classification of all 8 geometries | only prime decomposition + Van Kampen |
| Result | full geometrization of $M$ | only Poincaré for simply connected $M$ |
| Additional consequence | spherical space forms for $\pi_1$ finite | spherical space forms for $\pi_1$ finite |

Both routes are worked out in the literature. Morgan–Tian *Ricci Flow
and the Poincaré Conjecture* (AMS 2007) takes the shortcut as the main
line and treats full geometrization in a second volume (*The
Geometrization Conjecture*, AMS 2014). Cao–Zhu (AJM 2006) and
Kleiner–Lott (Geom. Topol. 2008) follow the long route.

## 6. What the Poincaré conjecture does *not* immediately give

- **Smooth 4-dim Poincaré conjecture:** still open. The techniques used
  here (Ricci flow, thin–thick) collapse in dimension 4 – Hamilton-style
  singularity analysis is not classified there.
- **Classification of all closed 3-manifolds:** geometrization *delivers*
  it, but only as a sum of *eight* geometries – not as a finite list of
  concrete examples. Hyperbolic geometry covers uncountably many
  manifolds.
- **Differential topology in 3-dim:** smooth and PL structures are
  equivalent in dimension 3 (Moise 1952), so "topologically $\cong S^3$"
  here means the same as "diffeomorphic to $S^3$". Hence in dimension 3
  there are no exotic spheres, unlike in dimensions $\ge 7$ (Milnor 1956).

## 7. Which obstacles fall now

| Obstacle (cf. [Article 01](01-hamiltons-programm.md)) | Resolution |
|-----------|------------|
| O5: read topology off the limit | geometrization *or* finite extinction $\Rightarrow$ each component is a spherical space form |
| Passage from "geometry" to "topology" | classical classifications (Hopf, Kneser–Milnor, Wolf) |

This completes Hamilton's program: all five obstacles from Article 01
have been overcome by Perelman's three preprints together with the
classical 3-manifold-topology toolkit.

## 8. Epilogue: what was actually proved

Perelman's proof contains *three* theorems that together imply the
Poincaré conjecture, but each of which is a result in its own right:

1. **Long-time existence of Ricci flow with surgery** for every closed
   3-manifold (0303109).
2. **Finite extinction time** for simply connected (and more generally
   spherically decomposable) manifolds (0307245).
3. **Geometrization** as asymptotic result of the flow (0303109 §§6–7
   + Shioya–Yamaguchi 2005 / Kleiner–Lott 2014).

The Poincaré conjecture is the *simplest* corollary of these. As with
Wiles' proof of Fermat's last theorem (cf.
[FLT article series](../../fermat-wiles/index.md)), the actual result
(modularity vs. geometrization) is much larger than the famous
consequence.

## Cross-references

- Previous: [Long-time behavior](04-long-time-verhalten.md) and [Finite extinction](05-endliche-extinktion.md) – the two routes.
- Topology: [What is the Poincaré conjecture?](../topologie/04-was-ist-poincare-vermutung.md), [Geometrization conjecture](../topologie/05-geometrisierungs-vermutung.md).
- Comparison: [FLT proof act](../../fermat-wiles/index.md) – analogous "big theorem $\Rightarrow$ classical conjecture" structure.
- Act overview: [The proof](index.md).

## Sources

- Perelman, G. (2002). *The entropy formula for the Ricci flow and its geometric applications*. arXiv:math/0211159.
- Perelman, G. (2003). *Ricci flow with surgery on three-manifolds*. arXiv:math/0303109.
- Perelman, G. (2003). *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds*. arXiv:math/0307245.
- Kneser, H. (1929). *Geschlossene Flächen in dreidimensionalen Mannigfaltigkeiten*. Jahresber. DMV 38, 248–260.
- Milnor, J. (1962). *A unique decomposition theorem for 3-manifolds*. Amer. J. Math. 84, 1–7.
- Hopf, H. (1926). *Zum Clifford-Kleinschen Raumproblem*. Math. Ann. 95, 313–339.
- Wolf, J. A. (2011). *Spaces of Constant Curvature*. AMS, 6th ed.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. CMI/AMS.
- Morgan, J. & Tian, G. (2014). *The Geometrization Conjecture*. CMI/AMS.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12.
