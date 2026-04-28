---
title: "Tangent Space and Tensors"
slug: vorwissen/geometrie-analysis/tangentialraum-tensoren
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: en
tags:
  - tangentialraum
  - tensoren
  - riemannian-metric
---

# Tangent Space and Tensors

> *"The tangent space is the right derivative of a manifold at a point –
> and everything geometric we measure lives on it."*

On a smooth manifold (see
[Manifolds – an Intuitive View](mannigfaltigkeit-anschaulich.md))
functions can be differentiated. For that one needs the notion of a
*velocity* at a point. This idea is formalised by the **tangent
space**. On its tensor products live the concepts of length
(Riemannian metric), curvature, and volume.

## 1. Tangent vectors

Let $M$ be a smooth manifold, $p \in M$. A **smooth curve through $p$**
is a smooth map $\gamma : (-\varepsilon, \varepsilon) \to M$ with
$\gamma(0) = p$. Two curves $\gamma_1, \gamma_2$ are **equivalent** if
in some (equivalently, every) chart
$$
\frac{\mathrm{d}}{\mathrm{d}t}\Big|_{t=0}(\varphi \circ \gamma_1)
=
\frac{\mathrm{d}}{\mathrm{d}t}\Big|_{t=0}(\varphi \circ \gamma_2).
$$
An equivalence class is called a **tangent vector** at $p$. The set of
all tangent vectors is the **tangent space** $T_p M$.

$T_p M$ is a real vector space of dimension $n = \dim M$. In a chart
$(x^1, \dots, x^n)$ around $p$ a basis is
$$
\Big\{ \partial_1 \big|_p, \dots, \partial_n \big|_p \Big\},
\qquad
\partial_i \big|_p f := \frac{\partial(f \circ \varphi^{-1})}{\partial x^i}(\varphi(p)).
$$

**Picture:** $T_p M$ is the tangent line/plane to $M$ at $p$,
*detached* from the manifold and made into its own vector space.

## 2. Vector fields and the cotangent space

A **vector field** $X$ assigns to every point $p$ a vector
$X_p \in T_p M$ (smoothly). In coordinates: $X = X^i(x)\,\partial_i$
(Einstein summation).

The **cotangent space** $T_p^* M$ is the dual of $T_p M$. A **1-form**
assigns to every point a linear form on $T_p M$. The basis dual to
$\partial_i$ is the differentials $\mathrm{d}x^i$. Then a 1-form is
$\omega = \omega_i(x)\,\mathrm{d}x^i$, and
$\mathrm{d}x^i(\partial_j) = \delta^i_j$.

## 3. Tensors and tensor fields

An **$(r,s)$-tensor** at $p$ is a multilinear map
$$
T : \underbrace{T_p^* M \times \dots \times T_p^* M}_{r}
   \times \underbrace{T_p M \times \dots \times T_p M}_{s}
   \to \mathbb{R}.
$$
A **tensor field** assigns to every point such a tensor. In coordinates:
$$
T = T^{i_1 \dots i_r}{}_{j_1 \dots j_s}\,
\partial_{i_1} \otimes \dots \otimes \partial_{i_r} \otimes
\mathrm{d}x^{j_1} \otimes \dots \otimes \mathrm{d}x^{j_s}.
$$

| Tensor | Type | Examples |
|--------|------|----------|
| function | $(0,0)$ | scalar field |
| vector field | $(1,0)$ | $\partial_i$ |
| 1-form | $(0,1)$ | $\mathrm{d}f$, $\mathrm{d}x^i$ |
| Riemannian metric | $(0,2)$, symmetric | $g_{ij}$ |
| curvature tensor | $(1,3)$ | $R^l{}_{ijk}$ |
| Ricci tensor | $(0,2)$, symmetric | $R_{ij}$ |

## 4. The Riemannian metric

A **Riemannian metric** $g$ is a symmetric, positive definite
$(0,2)$-tensor field. At every point $g_p$ is an inner product on
$T_p M$, in coordinates $g_{ij}(x)$ with $g_{ij} = g_{ji}$ and
$g_{ij}\xi^i \xi^j > 0$ for $\xi \neq 0$.

This yields:

- **Length of a vector:** $|v|_g = \sqrt{g_{ij} v^i v^j}$.
- **Length of a curve:** $L(\gamma) = \int_a^b |\dot\gamma(t)|_g\, \mathrm{d}t$.
- **Volume form:** $\mathrm{d}V_g = \sqrt{\det g_{ij}}\, \mathrm{d}x^1 \wedge \dots \wedge \mathrm{d}x^n$.
- **Inverse metric:** $g^{ij}$, defined by $g^{ij}g_{jk} = \delta^i_k$.

Example: on $\mathbb{R}^n$ the Euclidean metric is $g_{ij} = \delta_{ij}$.
On the sphere $S^2 \subset \mathbb{R}^3$ the embedding gives, in
spherical coordinates, $g = \mathrm{d}\theta^2 + \sin^2\theta\,\mathrm{d}\phi^2$.

## 5. Raising and lowering indices

With $g_{ij}$ and $g^{ij}$ one can convert indices. From a vector field
$X^i$ one obtains the 1-form $X_i := g_{ij} X^j$. From the curvature
tensor $R^l{}_{ijk}$ one obtains the four-index Riemann tensor
$R_{lijk} := g_{lm} R^m{}_{ijk}$. Once you get used to this mechanism
you read almost every formula of differential geometry as a balance of
upper/lower indices.

## 6. What comes next

Once a metric is chosen there is a *unique* torsion-free, metric
compatible connection – the **Levi-Civita connection** – and hence
covariant derivatives, geodesics and the Riemann curvature tensor.
From these arise Ricci and scalar curvature, which play the central
role in the Ricci flow $\partial_t g_{ij} = -2 R_{ij}$.

## Cross-references

- Previous: [Manifolds – an Intuitive View](mannigfaltigkeit-anschaulich.md).
- Continue with: [Curvature of Surfaces (Gauss)](kruemmung-flaechen-gauss.md), [Vector Calculus in a Nutshell](vektoranalysis.md).
- Application: [Act 2, Riemannian metric](../../poincare/ricci-fluss/01-riemannsche-metrik.md), [Act 2, Curvature and the Ricci tensor](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md).

## Sources

- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2nd ed. Ch. 1–3.
- do Carmo, Manfredo P. (1992). *Riemannian Geometry.* Birkhäuser.
- Petersen, Peter (2016). *Riemannian Geometry.* Springer GTM 171, 3rd ed.
