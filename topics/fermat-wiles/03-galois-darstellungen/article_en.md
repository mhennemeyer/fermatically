---
title: "Galois Representations"
slug: fermat-wiles/03-galois-darstellungen
series: fermat-wiles
part: 3
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - galois-representations
  - representation-theory
  - modularity
requires:
  - gruppen-und-symmetrie/01-gruppen
  - ringe-und-koerper/01-ringe-koerper
  - galois-theorie/01-galois-theorie
  - elliptische-kurven/01-elliptische-kurven
---
# Galois Representations

!!! abstract "Summary"
    Galois representations translate the symmetries of algebraic equations into
    the language of linear algebra: homomorphisms from Galois groups into
    matrix groups. Every elliptic curve yields a natural 2-dimensional
    representation, and Wiles' proof establishes modularity at precisely this level.

## Prerequisites

- [Groups and Symmetry](../../gruppen-und-symmetrie/01-gruppen/article_en.md) – homomorphisms, normal subgroups, quotient groups
- [Rings and Fields](../../ringe-und-koerper/01-ringe-koerper/article_en.md) – field extensions, finite fields $\mathbb{F}_p$, $p$-adic numbers $\mathbb{Z}_p$
- [Galois Theory](../../galois-theorie/01-galois-theorie/article_en.md) – Galois groups, Frobenius elements, ramification
- [Elliptic Curves](../../elliptische-kurven/01-elliptische-kurven/article_en.md) – group structure, torsion points, reduction modulo $p$

---

## 1. From Galois Groups to Matrices

### What is a representation?

A **representation** of a group $G$ is a homomorphism

$$
\rho: G \to \text{GL}_n(K),
$$

where $\text{GL}_n(K)$ is the group of invertible $n \times n$ matrices over a field (or ring) $K$. The representation "translates" the abstract group structure into the concrete language of linear algebra.

### Why representations?

Galois groups – in particular the absolute Galois group $G_{\mathbb{Q}}$ – are infinite and highly complex. Working with them directly is often impossible. Representations provide a tractable tool: instead of studying the group itself, one studies its **action on vector spaces**.

The central insight of Wiles' proof is: modularity of an elliptic curve can be formulated as a property of its Galois representation – and proved at that level.

---

## 2. The Absolute Galois Group

### Definition

The **absolute Galois group** of $\mathbb{Q}$ is

$$
G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}),
$$

where $\overline{\mathbb{Q}}$ is the algebraic closure of $\mathbb{Q}$ (the set of all algebraic numbers). $G_{\mathbb{Q}}$ consists of all field automorphisms of $\overline{\mathbb{Q}}$ that fix $\mathbb{Q}$ element-wise.

### Profinite structure

$G_{\mathbb{Q}}$ is a **profinite group** – the inverse limit of all finite Galois groups $\text{Gal}(K/\mathbb{Q})$:

$$
G_{\mathbb{Q}} = \varprojlim_{K/\mathbb{Q} \text{ finite, Galois}} \text{Gal}(K/\mathbb{Q}).
$$

It is uncountable and carries a natural topology (the Krull topology), under which it is compact and totally disconnected. Every open subgroup has finite index.

### Decomposition groups and Frobenius

For every prime $p$ there is a **decomposition group** $D_p \subset G_{\mathbb{Q}}$ and an **inertia group** $I_p \subset D_p$. The Frobenius element

$$
\text{Frob}_p \in D_p / I_p
$$

is the "signature" of the prime $p$ in $G_{\mathbb{Q}}$. It acts on reductions modulo $p$ as $x \mapsto x^p$.

For a representation $\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)$, one can compute the **trace of the Frobenius**

$$
\text{tr}(\rho(\text{Frob}_p))
$$

– and this number encodes the arithmetic information of the representation at $p$.

---

## 3. $p$-Torsion of Elliptic Curves

### The Galois module $E[p]$

Let $E$ be an elliptic curve over $\mathbb{Q}$ and $p$ a prime. The **$p$-torsion points** are:

$$
E[p] = \{P \in E(\overline{\mathbb{Q}}) : pP = \mathcal{O}\},
$$

where $\mathcal{O}$ is the point at infinity (the identity element of the group structure).

As an abelian group, $E[p]$ is isomorphic to

$$
E[p] \cong (\mathbb{Z}/p\mathbb{Z})^2.
$$

It is a two-dimensional vector space over $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.

### The Galois action

The points in $E[p]$ have coordinates in $\overline{\mathbb{Q}}$, and the absolute Galois group acts on them through its action on the coordinates:

$$
\sigma(P) = (\sigma(x_P), \sigma(y_P)) \quad \text{for } \sigma \in G_{\mathbb{Q}}.
$$

This action respects the group structure: $\sigma(P + Q) = \sigma(P) + \sigma(Q)$. Thus $E[p]$ is a **Galois module** – an $\mathbb{F}_p$-vector space with a linear action of $G_{\mathbb{Q}}$.

---

## 4. The Residual Representation

### Definition

Choosing a basis $\{P_1, P_2\}$ of $E[p]$ over $\mathbb{F}_p$, the Galois action is described by a matrix:

$$
\sigma(P_j) = \sum_i a_{ij}(\sigma) P_i, \qquad (a_{ij}(\sigma)) \in \text{GL}_2(\mathbb{F}_p).
$$

This defines the **residual Galois representation**:

$$
\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p).
$$

It is a continuous group homomorphism (with respect to the Krull topology on $G_{\mathbb{Q}}$ and the discrete topology on $\text{GL}_2(\mathbb{F}_p)$). Up to conjugation, it is independent of the choice of basis.

### Irreducibility

The representation $\bar{\rho}_{E,p}$ is called **irreducible** if $E[p]$ has no non-trivial $G_{\mathbb{Q}}$-invariant subgroup (i.e., no $\mathbb{F}_p$-subspace stable under the Galois action).

Irreducibility is a crucial hypothesis for Wiles' proof. For the Frey curve, $\bar{\rho}_{E,p}$ is irreducible for $p \geq 5$ – a consequence of Mazur's groundbreaking work on isogenous elliptic curves.

### Ramification and conductor

The representation $\bar{\rho}_{E,p}$ is **unramified** at a prime $q \neq p$ if the inertia group $I_q$ acts trivially on $E[p]$. This happens precisely when $E$ has good reduction at $q$.

The **Artin conductor** $N(\bar{\rho}_{E,p})$ measures the ramification of the representation and is a divisor of the conductor $N_E$ of the curve.

---

## 5. The $p$-adic Representation

### The Tate module

Instead of considering only the $p$-torsion, one can capture all $p^n$-torsion points simultaneously. The **Tate module** is the inverse limit:

$$
T_p(E) = \varprojlim_{n} E[p^n],
$$

where the transition maps are the multiplication-by-$p$ maps $E[p^{n+1}] \to E[p^n]$.

As a $\mathbb{Z}_p$-module, $T_p(E)$ is free of rank 2:

$$
T_p(E) \cong \mathbb{Z}_p^2.
$$

### The $p$-adic representation

The Galois action on $T_p(E)$ yields the **$p$-adic Galois representation**:

$$
\rho_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p) \hookrightarrow \text{GL}_2(\mathbb{Q}_p).
$$

This is a continuous representation with respect to the $p$-adic topology. It is a "lift" of the residual representation: reduction modulo $p$ gives

$$
\rho_{E,p} \pmod{p} = \bar{\rho}_{E,p}.
$$

### The connection to $L$-series

The $p$-adic representation encodes the arithmetic information of the curve completely:

$$
\text{tr}(\rho_{E,p}(\text{Frob}_q)) = a_q(E), \qquad \det(\rho_{E,p}(\text{Frob}_q)) = q,
$$

for every prime $q$ of good reduction (with $q \neq p$). Thus the representation determines the $L$-series $L(E, s)$ – and vice versa.

---

## 6. Modular Representations

### Representations from modular forms

Not only elliptic curves yield Galois representations – **modular forms** do as well. For every newform $f$ of weight 2 and level $N$, Eichler and Shimura constructed an associated Galois representation:

$$
\rho_f: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p),
$$

with the property

$$
\text{tr}(\rho_f(\text{Frob}_q)) = b_q(f), \qquad \det(\rho_f(\text{Frob}_q)) = q,
$$

where $b_q$ is the $q$-th Fourier coefficient of $f$.

### Modularity as a property of representations

Now the connection becomes clear: an elliptic curve $E$ is **modular** if and only if its Galois representation $\rho_{E,p}$ agrees with the representation $\rho_f$ of a newform $f$:

$$
\rho_{E,p} \cong \rho_f \quad \iff \quad a_q(E) = b_q(f) \text{ for all } q \quad \iff \quad L(E, s) = L(f, s).
$$

The modularity conjecture (TSC) thus becomes a statement about Galois representations: **every representation coming from an elliptic curve also comes from a modular form.**

### Residual modularity

Analogously, $\bar{\rho}_{E,p}$ is called **modular** if it is isomorphic to the reduction modulo $p$ of a modular representation:

$$
\bar{\rho}_{E,p} \cong \bar{\rho}_f \pmod{p}
$$

for some newform $f$. This is a weaker condition than full modularity – and precisely the starting point of Wiles' proof strategy.

---

## 7. Wiles' Strategy

### The two steps

Wiles' proof of the modularity of semistable elliptic curves breaks into two major steps:

**Step 1: Establish residual modularity.** One must prove that $\bar{\rho}_{E,p}$ is modular – i.e., comes from a newform. For $p = 3$, this follows from a famous result of **Langlands and Tunnell**: since $\text{GL}_2(\mathbb{F}_3)$ is solvable, Langlands' base change techniques can be applied. For $p = 5$, Wiles uses the so-called **3-5 switch** (see [Article 07](../07-3-5-switch/article_en.md)).

**Step 2: "Lift" from residual to full modularity.** This is the heart of the proof: given that $\bar{\rho}_{E,p}$ is modular, one must show that the full representation $\rho_{E,p}$ is also modular. For this, Wiles introduces the language of **deformation theory** (see [Article 04](../04-deformationstheorie/article_en.md)).

### Why representations are the right framework

The reformulation of the TSC in the language of Galois representations has decisive advantages:

1. **Algebraic tools**: Representation theory, cohomology, and commutative algebra become applicable.
2. **Local-global principles**: One can study representations "locally" (at each prime) and "globally" (over $\mathbb{Q}$).
3. **Deformations**: The residual representation $\bar{\rho}$ has a "space of all lifts" – the deformation space, which can be analysed with algebraic methods.
4. **Reduction**: One can prove modularity step by step – first residually, then fully.

This perspective – modularity as a property of Galois representations – was Wiles' decisive conceptual innovation and has profoundly shaped number theory since 1995.

---

## Outlook

With Galois representations, we have the language in which Wiles' proof is formulated. The next step is the central question: how does one show that a residually modular representation can be lifted to a fully modular representation?

| Article | Topic |
|---------|-------|
| [04 – Deformation Theory](../04-deformationstheorie/article_en.md) | The universal deformation ring $R$ and Mazur's theory |
| [05 – R = T](../05-r-gleich-t/article_en.md) | Why $R = T$ proves modularity |

---

## Sources

- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Chapter 10 – Galois representations
- **Jean-Pierre Serre**: *Abelian $\ell$-adic representations and elliptic curves*, W.A. Benjamin (1968) – Classical reference for $\ell$-adic representations
- **Barry Mazur**: *Deforming Galois representations*, in: Galois Groups over $\mathbb{Q}$, MSRI Publications 16 (1989) – Foundational for the deformation approach
