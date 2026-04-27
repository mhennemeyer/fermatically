---
title: "The Sphere and Simple Connectedness"
slug: poincare/topologie/03-sphaere-einfacher-zusammenhang
series: poincare
part: 3
act: topologie
date: 2026-04-25
status: draft
lang: en
tags:
  - sphere
  - homotopy
  - fundamental-group
---

# The Sphere and Simple Connectedness

!!! abstract "Summary"
    The $n$-sphere $S^n$ is the model manifold of topology and the
    central protagonist of the Poincaré Conjecture. Through **loops**
    and **homotopy** one defines the **fundamental group** $\pi_1(M)$;
    if it vanishes, $M$ is called **simply connected**. Precisely this
    property is supposed to single out the 3-sphere among all closed
    3-manifolds.

## 1. The $n$-sphere

The **$n$-sphere** is defined as the unit sphere in $\mathbb{R}^{n+1}$:

$$
S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}.
$$

It is a closed, smooth $n$-manifold. A convenient equivalent
description comes from **stereographic projection**: remove a single
point – say the north pole – and the rest is mapped homeomorphically
onto $\mathbb{R}^n$. The sphere is therefore the one-point
compactification of $\mathbb{R}^n$:

$$
S^n \cong \mathbb{R}^n \cup \{\infty\}.
$$

In low dimensions this gives familiar pictures. $S^0$ consists of two
points, $S^1$ is the circle, $S^2$ the ordinary sphere, $S^3$ sits in
$\mathbb{R}^4$ and can be visualised as two glued solid balls
$D^3 \cup_{S^2} D^3$. This very 3-sphere $S^3$ is the object whose
topological uniqueness Poincaré conjectured in 1904.

## 2. Paths and loops

A **path** in a topological space $X$ is a continuous map
$\gamma \colon [0,1] \to X$. If start and end agree, that is
$\gamma(0) = \gamma(1) = x_0$, one calls it a **loop** with base point
$x_0$. Intuitively: a connected thread that begins and ends at a fixed
point.

Loops can be combined. Given two loops $\alpha, \beta$ at the same base
point, the **concatenation** $\alpha \cdot \beta$ first traces $\alpha$
and then $\beta$ (each at double speed). The constant loop $c_{x_0}$
stays at $x_0$, and the **inverse** $\bar\alpha(t) = \alpha(1-t)$ runs
$\alpha$ backwards. After identifying homotopic loops, this structure
becomes a group.

## 3. Homotopy

Two continuous maps $f, g \colon X \to Y$ are **homotopic** if one can
be continuously deformed into the other. Formally:

> A **homotopy** between $f$ and $g$ is a continuous map
> $H \colon X \times [0,1] \to Y$ with $H(\cdot, 0) = f$ and
> $H(\cdot, 1) = g$.

For loops one additionally requires that the base point is held fixed
during the deformation (**base-point-preserving homotopy**).
Intuitively: the loop may stretch, shrink and bend arbitrarily, the
thread must not be cut, and the seam at the base point stays sewn.

The homotopy relation is an equivalence relation on loops. We write
$[\alpha]$ for the class of all loops homotopic to $\alpha$.

## 4. The fundamental group

On the set of homotopy classes the concatenation induces a well-defined
operation. This yields:

> The **fundamental group** of $X$ at base point $x_0$ is
> $$\pi_1(X, x_0) = \{[\alpha] : \alpha \text{ a loop at } x_0\}$$
> with operation $[\alpha][\beta] = [\alpha \cdot \beta]$, identity
> $[c_{x_0}]$ and inverse $[\alpha]^{-1} = [\bar\alpha]$.

For path-connected spaces $\pi_1(X, x_0)$ is independent of the base
point up to isomorphism; one then writes $\pi_1(X)$. The fundamental
group is a **topological invariant**: homeomorphic spaces have
isomorphic fundamental groups.

> "The fundamental group $\pi_1(X)$ is the most basic and most useful
> of the algebraic invariants associated to a topological space."
> — Allen Hatcher, *Algebraic Topology* (2002), p. 25

## 5. Simple connectedness

If the fundamental group vanishes – that is, every loop can be
contracted continuously to a point – the space is called **simply
connected**:

$$
X \text{ simply connected} \;:\Longleftrightarrow\; X \text{ path-connected and } \pi_1(X) = 0.
$$

Visual criterion: a rubber band placed anywhere on $X$ can be pulled to
a point without leaving $X$ and without breaking.

## 6. Fundamental groups of some spaces

Three examples worth remembering for the Poincaré story:

**The sphere $S^n$ for $n \geq 2$.** Every loop on the sphere can be
contracted to a point: $\pi_1(S^n) = 0$. Intuitively, slide the rubber
band around the surface to a pole. So $S^n$ is simply connected for
$n \geq 2$.

**The circle $S^1$.** A loop that winds $k$ times around the circle
cannot be contracted without crossing through the other side. We have

$$
\pi_1(S^1) \cong \mathbb{Z},
$$

with the winding number giving the isomorphism. $S^1$ is *not* simply
connected.

**The torus $T^2 = S^1 \times S^1$.** There are two independent
generating loops, one around each $S^1$-factor. The fundamental group
is abelian:

$$
\pi_1(T^2) \cong \mathbb{Z} \oplus \mathbb{Z}.
$$

In dimension 3 the 3-torus $T^3$ has $\pi_1(T^3) \cong \mathbb{Z}^3$,
and the lens spaces $L(p, q)$ have finite fundamental groups
$\mathbb{Z}/p$.

## 7. Higher homotopy groups

Loops are maps $S^1 \to X$. Replacing $S^1$ by $S^k$ yields the
**higher homotopy groups** $\pi_k(X)$. For the sphere itself one has
$\pi_n(S^n) \cong \mathbb{Z}$, classified by the **mapping degree**.
The higher $\pi_k(S^n)$ for $k > n$ are highly nontrivial – their
study was one of the driving topics of algebraic topology in the
twentieth century.

For the Poincaré Conjecture only $\pi_1$ matters: $S^n$ is simply
connected for $n \geq 2$, that is, $\pi_1(S^n) = 0$. "Simply connected"
is precisely $\pi_1 = 0$.

## 8. Relation to the conjecture

The **Poincaré Conjecture in dimension 3** states:

$$
M^3 \text{ closed and simply connected} \;\Longrightarrow\; M^3 \cong S^3.
$$

This makes plain why the sphere and its fundamental-group profile are
central: $\pi_1(S^3) = 0$ is the *characterising* property that is
supposed to single it out among all closed 3-manifolds. In all other
dimensions $n \geq 5$ the analogous statement was proved by Smale
(1961), in dimension 4 by Freedman (1982). In dimension 3 it was
Perelman who succeeded.

> "The Poincaré Conjecture says that $S^3$ is the only closed
> 3-manifold whose fundamental group is trivial."
> — John W. Morgan, Gang Tian, *Ricci Flow and the Poincaré
> Conjecture* (2007), p. 3

## 9. Outlook

With manifold, sphere, homotopy and fundamental group in place, all the
ingredients are there to phrase the conjecture precisely. The next
article traces its history – from Poincaré's *Analysis Situs* (1904)
through the higher-dimensional resolutions to Hamilton's programme.

| Article | Topic |
|---------|-------|
| [04 – What Is the Poincaré Conjecture?](04-was-ist-poincare-vermutung.md) | Original formulation 1904, higher dimensions |
| [05 – Thurston's Geometrization Conjecture](05-geometrisierungs-vermutung.md) | Thurston's bigger picture |

---

## Sources

- **Allen Hatcher**: *Algebraic Topology*, Cambridge University Press
  (2002), Chapter 1
- **John M. Lee**: *Introduction to Topological Manifolds*, 2nd ed.,
  Springer (2011), Chapter 7
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007), Chapter 1
- **Henri Poincaré**: *Cinquième complément à l'Analysis Situs*,
  Rendiconti del Circolo Matematico di Palermo 18 (1904), 45–110
