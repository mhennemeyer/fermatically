---
title: "What Is the Poincaré Conjecture?"
slug: poincare/topologie/04-was-ist-poincare-vermutung
series: poincare
part: 4
act: topologie
date: 2026-04-25
status: draft
lang: en
tags:
  - poincare-conjecture
  - history
---

# What Is the Poincaré Conjecture?

!!! abstract "Summary"
    At the end of his fifth *Complément à l'Analysis Situs* (1904)
    Henri Poincaré posed a question about the 3-sphere that remained
    open for a century. In dimensions $n \geq 5$ and $n = 4$ it was
    long since solved, but dimension 3 resisted every classical
    approach. This article tells the story – from the original
    formulation through the homology sphere to Hamilton's Ricci flow
    programme.

## 1. The original formulation, 1904

Between 1895 and 1904 Poincaré laid the foundations of algebraic
topology in *Analysis Situs* and five complements. In an earlier paper
(1900) he had asserted that any closed 3-manifold with the same
**homology** as $S^3$ must be homeomorphic to $S^3$. In 1904 he
disproved his own assertion with a counter-example: the
**Poincaré homology sphere**, a closed 3-manifold with
$H_*(M) = H_*(S^3)$ but a nontrivial fundamental group (the binary
icosahedral group of order 120).

At the end of the fifth Complément he therefore phrased a question in
which "homology" is replaced by the stronger "fundamental group":

> *"Est-il possible que le groupe fondamental de $V$ se réduise à la
> substitution identique, et que pourtant $V$ ne soit pas simplement
> connexe?"*
> — Henri Poincaré, *Cinquième complément à l'Analysis Situs* (1904)

Loosely: can a closed 3-manifold with trivial fundamental group be
different from the 3-sphere? Poincaré ends with the famous line: *"Mais
cette question nous entraînerait trop loin"* – this question would
take us too far afield.

In modern language:

> **Poincaré Conjecture (1904).** Every closed, simply connected
> 3-manifold is homeomorphic to $S^3$.

## 2. What the conjecture rules out

The conjecture does not say that $S^3$ is the only closed 3-manifold –
that is plainly false. Infinitely many exist:

- the 3-torus $T^3$ with $\pi_1(T^3) = \mathbb{Z}^3$,
- the lens spaces $L(p, q)$ with $\pi_1 = \mathbb{Z}/p$,
- the Poincaré homology sphere with $\pi_1$ of order 120,
- the quotient $S^2 \times S^1$ with $\pi_1 = \mathbb{Z}$,
- and all constructions from Heegaard splittings or Dehn surgery.

What they share: $\pi_1 \neq 0$. The conjecture claims that *among the
simply connected ones* only one manifold remains. Anyone familiar with
the Geometrization Conjecture
([Article 05](05-geometrisierungs-vermutung.md)) will recognise:
Poincaré is precisely the "spherical" special case.

## 3. Why was it hard?

The apparent simplicity of the conjecture stands in stark contrast to
the difficulty of its proof.

**No direct construction.** From "$\pi_1(M) = 0$" a homeomorphism to
$S^3$ does not follow directly. The fundamental group only sees loops;
identifying a 3-dimensional manifold with $S^3$ requires
2-dimensional gluings.

**Classical tools fail.** Heegaard splittings, Dehn surgery, end
theory – none yielded a decisive breakthrough. The characterisation
via homotopy equivalence did not help either: in 1934 Whitehead
published a notorious "proof" showing that the obvious approach fails
without additional assumptions.

**Changing dimensions does not help.** In dimensions 1 and 2 the
conjecture is trivial or classical (the classification of surfaces).
In dimension $\geq 5$ techniques are available that are absent in
dimension 3, and dimension 4 admits yet other methods. Dimension 3 is
exactly "too narrow" for the higher tricks and "too wide" for
elementary arguments.

> "Dimension three is at once the most and the least mysterious of the
> dimensions; we live in it, yet have struggled for over a century to
> understand its global topology."
> — John W. Morgan, *Recent progress on the Poincaré Conjecture and
> the classification of 3-manifolds*, BAMS (2005)

## 4. The generalisation – higher dimensions

Once algebraic and differential topology were mature, Poincaré's
question could be posed in any dimension:

> **Generalised Poincaré Conjecture.** Every closed $n$-manifold that
> is homotopy-equivalent to $S^n$ is homeomorphic to $S^n$.

In dimensions $\geq 5$ the assumption "simply connected with the
homology of $S^n$" is already strong enough. Paradoxically the
resolution proceeded from the top down:

| Year | Dim | Author | Method |
|------|-----|--------|--------|
| 1961 | $n \geq 5$ | Stephen Smale | $h$-cobordism, handle theory |
| 1962 | $n \geq 5$ | John Stallings, Christopher Zeeman | PL version, engulfing |
| 1982 | $n = 4$ | Michael Freedman | Casson handles, topological category |
| 2002–2003 | $n = 3$ | Grigori Perelman | Ricci flow with surgery |

Smale, Freedman and Perelman each received a Fields Medal or the Clay
Millennium Prize. Notably, in the **smooth** category the question is
still open in dimension 4 – the *Smooth Poincaré Conjecture* in
dimension 4 is one of the most prominent open problems of topology.

## 5. The Clay Millennium Problems

In 2000 the **Clay Mathematics Institute** posted seven "Millennium
Prize Problems" with one million US dollars each. The Poincaré
Conjecture in dimension 3 was one of them – and is still the only one
that has been solved.

Between November 2002 and July 2003 Perelman uploaded three preprints
to arXiv that together provided the proof. After years of verification
by several teams (Kleiner–Lott; Cao–Zhu; Morgan–Tian) the Clay
Institute officially awarded the prize in 2010. Perelman declined both
the prize money and the Fields Medal awarded to him in 2006.

## 6. Hamilton's programme – the path that worked

The road to the proof did not lead through classical topological
methods but through **geometric analysis**. In 1982 Richard Hamilton
proposed evolving a Riemannian metric $g$ on $M$ under a heat-like
differential equation:

$$
\frac{\partial g_{ij}}{\partial t} = -2 R_{ij},
$$

the **Ricci flow**. Hamilton proved: if $M^3$ is simply connected and
admits an initial metric of **positive Ricci curvature**, the flow
smooths it out to a round sphere. Hence the manifold is $S^3$.

This hypothesis – *positive* Ricci curvature – is, however, strong.
Without it the flow produces **singularities**: regions where the
curvature blows up in finite time. Hamilton's programme called for
classifying these singularities and removing them by **surgery**
(controlled cut-and-paste) so the flow could be continued. Until 2002
the analytical tools were missing.

Perelman supplied them:

- an **entropy functional** $\mathcal{F}$ and its more mysterious
  sibling $\mathcal{W}$, whose monotonicity reveals a hidden
  variational structure of the flow;
- the **$\kappa$-non-collapsing theorem**, providing lower volume
  bounds;
- the classification of **$\kappa$-solutions**, that is, the possible
  singularity models in dimension 3;
- a precise surgery procedure together with long-time analysis.

Acts 2 and 3 of the Poincaré story will develop these tools in detail.

## 7. Outlook

The next article presents William Thurston's **Geometrization
Conjecture** (1982). This is the actual statement Perelman proved – the
Poincaré Conjecture follows as a corollary. Thurston proposed
decomposing every closed 3-manifold into geometric pieces, of which
there are exactly **eight model geometries**.

| Article | Topic |
|---------|-------|
| [05 – Thurston's Geometrization Conjecture](05-geometrisierungs-vermutung.md) | Eight model geometries, decomposition |
| [Act 2 – Tools: Ricci Flow](../ricci-fluss/index.md) | Riemannian metric, curvature, Hamilton's flow |

---

## Sources

- **Henri Poincaré**: *Cinquième complément à l'Analysis Situs*,
  Rendiconti del Circolo Matematico di Palermo 18 (1904), 45–110
- **Stephen Smale**: *Generalized Poincaré's conjecture in dimensions
  greater than four*, Annals of Mathematics 74 (1961), 391–406
- **Michael H. Freedman**: *The topology of four-dimensional
  manifolds*, Journal of Differential Geometry 17 (1982), 357–453
- **Richard S. Hamilton**: *Three-manifolds with positive Ricci
  curvature*, Journal of Differential Geometry 17 (1982), 255–306
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007)
- **Donal O'Shea**: *The Poincaré Conjecture: In Search of the Shape
  of the Universe*, Walker & Company (2007)
