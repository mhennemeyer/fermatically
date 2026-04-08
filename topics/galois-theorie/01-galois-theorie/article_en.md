---
title: "Galois Theory – Why Equations Have No Solution Formulas"
slug: galois-theorie/01-galois-theorie
series: galois-theorie
part: 1
date: 2026-03-31
status: draft
lang: en
category: algebra
tags:
  - galois
  - field-extensions
  - symmetry
requires:
  - gruppen-und-symmetrie/01-gruppen
  - ringe-und-koerper/01-ringe-koerper
---

# Galois Theory

!!! abstract "Summary"
    At the age of 19, Évariste Galois discovered that the solvability of an equation is determined
    by the symmetries of its roots. His theory connects field extensions
    with groups – and provides the conceptual framework for Wiles' proof.

## Prerequisites

- [Groups – Symmetry as the Language of Mathematics](../../gruppen-und-symmetrie/01-gruppen/article_en.md)
- [Rings and Fields](../../ringe-und-koerper/01-ringe-koerper/article_en.md)

---

## 1. The Problem of Solution Formulas

Everyone knows the **quadratic formula**:

$$
x^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4c}}{2}
$$

The roots can be expressed in terms of the coefficients – using addition, subtraction, multiplication, division, and root extraction.

For equations of degree three and four, there likewise exist (more complicated) solution formulas, discovered by Cardano (1545) and Ferrari. Naturally the question arises: do such formulas also exist for degree $5$ and higher?

The answer is **no** – and the justification leads directly to Galois theory.

## 2. Abel's Impossibility Proof

**Niels Henrik Abel** proved in 1824 that there is **no** general solution formula for polynomials of degree $\geq 5$ in radicals. That is: there exist fifth-degree polynomials whose roots cannot be expressed by finitely many root extractions from the coefficients.

Abel's proof was a milestone, but left a decisive question open: **which** polynomials can be solved by radicals and which cannot? A specific fifth-degree polynomial may well have a solution in radicals – for instance $x^5 - 2 = 0$ with $x = \sqrt[5]{2}$. Abel's theorem only says that no *general* procedure exists.

## 3. Galois' Idea

**Évariste Galois** (1811–1832) solved this problem completely – with an idea decades ahead of its time. He died at 20 in a duel; the night before, he feverishly wrote down his mathematical insights.

Galois' central insight: **The solvability of an equation is determined by the symmetries of its roots.**

Consider a polynomial $f \in \mathbb{Q}[x]$ with roots $\alpha_1, \ldots, \alpha_n \in \overline{\mathbb{Q}}$. The **splitting field** is the smallest field containing $\mathbb{Q}$ and all roots:

$$
L = \mathbb{Q}(\alpha_1, \ldots, \alpha_n)
$$

A **symmetry** of this field is an automorphism $\sigma: L \to L$ that fixes $\mathbb{Q}$ element-wise. Every such automorphism permutes the roots $\alpha_1, \ldots, \alpha_n$ – since it must preserve the equation $f(\alpha_i) = 0$.

## 4. The Galois Group

The **Galois group** of a field extension $L/K$ is the group of all $K$-automorphisms of $L$:

$$
\text{Gal}(L/K) = \{\sigma: L \to L \mid \sigma \text{ is an automorphism with } \sigma|_K = \text{id}\}
$$

The operation is composition of maps.

### Example: $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$

The extension $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ has degree $2$. The only $\mathbb{Q}$-automorphisms are:

- $\text{id}: \sqrt{2} \mapsto \sqrt{2}$
- $\sigma: \sqrt{2} \mapsto -\sqrt{2}$

Hence $\text{Gal}(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}$.

### Example: Splitting field of $x^3 - 2$

The roots of $x^3 - 2$ are $\sqrt[3]{2}$, $\omega\sqrt[3]{2}$, and $\omega^2\sqrt[3]{2}$ (with $\omega = e^{2\pi i/3}$). The splitting field is $L = \mathbb{Q}(\sqrt[3]{2}, \omega)$ with $[L:\mathbb{Q}] = 6$.

The Galois group is $\text{Gal}(L/\mathbb{Q}) \cong S_3$ – the symmetric group on $3$ elements. This is because the automorphisms can arbitrarily permute the three roots (subject to the constraint that $\omega \mapsto \omega$ or $\omega \mapsto \omega^2$).

### Example: Cyclotomic fields

The $p$-th cyclotomic field $\mathbb{Q}(\zeta_p)$ (with $\zeta_p = e^{2\pi i/p}$) has the Galois group:

$$
\text{Gal}(\mathbb{Q}(\zeta_p)/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^*
$$

This is the group of units modulo $p$ – an abelian group of order $p - 1$. Each automorphism $\sigma_a$ sends $\zeta_p \mapsto \zeta_p^a$ for some $a \in \{1, \ldots, p-1\}$.

## 5. The Fundamental Theorem of Galois Theory

The **fundamental theorem** is the heart of the theory. It establishes a perfect correspondence between the algebraic structure of the field extension and the group structure of the Galois group.

**Theorem (Galois correspondence).** Let $L/K$ be a finite Galois extension with Galois group $G = \text{Gal}(L/K)$. Then there is an inclusion-reversing bijection:

$$
\{\text{intermediate fields } K \subseteq M \subseteq L\} \longleftrightarrow \{\text{subgroups } H \leq G\}
$$

given by:

$$
M \longmapsto \text{Gal}(L/M), \qquad H \longmapsto L^H = \{x \in L \mid \sigma(x) = x \text{ for all } \sigma \in H\}
$$

Moreover:
- $[M : K] = [G : H]$ (index of the subgroup = degree of the extension)
- $M/K$ is a Galois extension if and only if $H \trianglelefteq G$ (normal subgroup)
- In that case, $\text{Gal}(M/K) \cong G/H$

!!! tip "The correspondence visualised"
    ```
    Fields                  Groups
    L                       {e}
    |                        |
    M₂                     H₂
    |    \                 /    |
    M₁     M₃          H₁    H₃
    |    /                 \    |
    K                       G
    ```
    Larger fields correspond to *smaller* subgroups (and vice versa).

## 6. Solvability

Galois' original question was: when can an equation be solved by radicals? The fundamental theorem provides the answer.

**Definition.** A group $G$ is called **solvable** if it possesses a chain of subgroups:

$$
\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G
$$

where each factor $G_{i+1}/G_i$ is abelian (cyclic of prime order).

**Theorem (Galois).** A polynomial $f \in K[x]$ is solvable by radicals if and only if its Galois group is solvable.

**Consequence for degree $\geq 5$:** The symmetric group $S_n$ is **not** solvable for $n \geq 5$ (because the alternating group $A_n$ is simple and non-abelian for $n \geq 5$). Since there exist polynomials with Galois group $S_5$, these are not solvable by radicals.

**Consequence for degree $\leq 4$:** The groups $S_1, S_2, S_3, S_4$ are all solvable – hence solution formulas exist for polynomials up to degree $4$.

## 7. The Absolute Galois Group

For number theory – and in particular for Wiles' proof – it is not the Galois group of a single extension that matters, but the **absolute Galois group**:

$$
G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})
$$

This is the Galois group of the extension of all algebraic numbers over $\mathbb{Q}$. It is an infinite, profinite group – the projective limit of all finite Galois groups $\text{Gal}(L/\mathbb{Q})$.

$G_{\mathbb{Q}}$ is one of the most mysterious objects in mathematics. Despite intensive research, its complete structure is unknown. What we do know are its **representations** – homomorphisms from $G_{\mathbb{Q}}$ into matrix groups.

### Galois Representations

A **(continuous) Galois representation** is a homomorphism:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)
$$

for a suitable field or ring $K$. For Wiles' proof, the **two-dimensional** representations ($n = 2$) are central:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p) \quad \text{or} \quad \rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p)
$$

Every elliptic curve $E$ over $\mathbb{Q}$ yields such representations – via the action of $G_{\mathbb{Q}}$ on the $p$-division points $E[p]$. And every modular form likewise yields a Galois representation. The **Taniyama–Shimura conjecture** states in essence: the representation of the elliptic curve *is* the representation of a modular form.

### Local Galois Groups

For every prime $p$ there is a **local Galois group** $G_{\mathbb{Q}_p} = \text{Gal}(\overline{\mathbb{Q}_p}/\mathbb{Q}_p)$. It controls the behaviour of algebraic objects "at the place $p$". Every global representation $\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)$ induces by restriction local representations:

$$
\rho|_{G_{\mathbb{Q}_p}}: G_{\mathbb{Q}_p} \to \text{GL}_n(K)
$$

The **local-global principle** asks: when do the local representations determine the global one? This question lies at the centre of Wiles' proof.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 4
- **Ian Stewart**: *Galois Theory* – accessible introduction
- **Emil Artin**: *Galois Theory* – the classical approach
