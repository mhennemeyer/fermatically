---
title: "Rings and Fields – The World Beyond the Rational Numbers"
slug: ringe-und-koerper/01-ringe-koerper
series: ringe-und-koerper
part: 1
date: 2026-03-31
status: draft
lang: en
category: algebra
tags:
  - rings
  - fields
  - algebra
  - ideal-theory
requires:
  - gruppen-und-symmetrie/01-gruppen
---

# Rings and Fields

!!! abstract "Summary"
    From groups (one operation) to rings (two operations) and fields (with division).
    Why the integers are not always "enough" – and how ideal theory solves the problem
    of missing unique factorisation.

## Prerequisites

- [Groups – Symmetry as the Language of Mathematics](../../gruppen-und-symmetrie/01-gruppen/article_en.md)

---

## 1. From Groups to Rings

In a group we have *one* operation. But even the integers $\mathbb{Z}$ have *two*: addition and multiplication. To capture both simultaneously, we need a richer structure – the **ring**.

The motivation comes directly from number theory: Fermat's Last Theorem is about the equation $x^n + y^n = z^n$ in the integers. The proofs for $n = 3$ and $n = 4$ showed that sometimes one must extend the number domain – to $\mathbb{Z}[\omega]$ or $\mathbb{Z}[i]$. All these number domains are rings.

## 2. Ring Axioms and Examples

A **ring** $(R, +, \cdot)$ is a set $R$ with two operations satisfying the following axioms:

1. $(R, +)$ is an abelian group (with identity element $0$)
2. Multiplication is associative: $(ab)c = a(bc)$
3. There is a unity element: $1 \cdot a = a \cdot 1 = a$
4. The distributive laws hold: $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$

If additionally $ab = ba$ for all $a, b \in R$, the ring is called **commutative**.

### The Most Important Examples

| Ring | Description | Commutative? |
|------|------------|--------------|
| $\mathbb{Z}$ | Integers | ✓ |
| $\mathbb{Z}/n\mathbb{Z}$ | Residue classes modulo $n$ | ✓ |
| $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$ | Gaussian integers | ✓ |
| $\mathbb{Z}[\omega] = \{a + b\omega \mid a, b \in \mathbb{Z}\}$ | Eisenstein integers | ✓ |
| $\mathbb{Z}[\zeta_p]$ | Cyclotomic ring | ✓ |
| $K[x]$ | Polynomial ring over a field $K$ | ✓ |
| $M_n(\mathbb{R})$ | $n \times n$ matrices | ✗ (for $n \geq 2$) |

### Zero Divisors and Integral Domains

In $\mathbb{Z}$ we have: if $ab = 0$, then $a = 0$ or $b = 0$. This is not the case in every ring! In $\mathbb{Z}/6\mathbb{Z}$, $2 \cdot 3 = 6 \equiv 0$, even though neither $2$ nor $3$ is zero. Such elements are called **zero divisors**.

A commutative ring without zero divisors (other than $0$) is called an **integral domain**. The rings $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$, and $K[x]$ are integral domains; $\mathbb{Z}/6\mathbb{Z}$ is not.

## 3. Ideals and Quotient Rings

In $\mathbb{Z}$, divisibility is a central concept: $3 \mid 12$, because $12 = 3 \cdot 4$. The set of all multiples of $3$ forms a subset $3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$ with special properties:

- $3\mathbb{Z}$ is closed under addition
- For every $r \in \mathbb{Z}$ and $a \in 3\mathbb{Z}$, $ra \in 3\mathbb{Z}$

These properties define an **ideal**.

**Definition.** A subset $I \subseteq R$ is called an **ideal** if:
1. $(I, +)$ is a subgroup of $(R, +)$
2. For all $r \in R$ and $a \in I$, $ra \in I$ and $ar \in I$

Ideals play the same role in rings as normal subgroups in groups: one can form **quotient rings**:

$$
R/I = \{r + I \mid r \in R\}
$$

**Example:** $\mathbb{Z}/n\mathbb{Z} = \mathbb{Z}/(n)$ is the quotient ring of $\mathbb{Z}$ by the ideal $(n) = n\mathbb{Z}$.

### Principal Ideals and Principal Ideal Domains

An ideal of the form $(a) = \{ra \mid r \in R\}$ (all multiples of an element) is called a **principal ideal**. An integral domain in which every ideal is a principal ideal is called a **principal ideal domain** (PID).

**PID examples:** $\mathbb{Z}$, $K[x]$ (polynomials over a field), $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$

**Not a PID:** $\mathbb{Z}[\sqrt{-5}]$ – here the ideal $(2, 1 + \sqrt{-5})$ has no single generator.

!!! warning "The crux in FLT"
    In a PID, unique prime factorisation holds. In $\mathbb{Z}[\zeta_p]$ for general $p$, this is **not** the case – this is precisely where Lamé's proof failed and Kummer invented ideal theory.

## 4. Fields

A **field** is a commutative ring in which every element $a \neq 0$ has a multiplicative inverse: there exists $a^{-1}$ with $a \cdot a^{-1} = 1$.

In other words: in a field one can add, subtract, multiply **and divide** (except by $0$).

### The Most Important Fields

| Field | Description | Property |
|-------|------------|----------|
| $\mathbb{Q}$ | Rational numbers | smallest field of characteristic $0$ |
| $\mathbb{R}$ | Real numbers | complete, ordered |
| $\mathbb{C}$ | Complex numbers | algebraically closed |
| $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ | Finite field with $p$ elements | characteristic $p$ |
| $\mathbb{Q}_p$ | $p$-adic numbers | completion of $\mathbb{Q}$ |

**Why is $\mathbb{Z}/p\mathbb{Z}$ a field?** Because $p$ is prime: for $a \not\equiv 0 \pmod{p}$, $\gcd(a, p) = 1$, so by the extended Euclidean algorithm there exists $b$ with $ab \equiv 1 \pmod{p}$. By contrast, $\mathbb{Z}/6\mathbb{Z}$ is not a field (because $2 \cdot 3 = 0$).

## 5. Field Extensions

A **field extension** is a pair $K \subseteq L$ of fields. One writes $L/K$ and calls $L$ an extension of $K$.

### Algebraic Extensions

An element $\alpha \in L$ is called **algebraic** over $K$ if there is a polynomial $f \in K[x]$ with $f(\alpha) = 0$. The extension $L/K$ is called algebraic if every element of $L$ is algebraic over $K$.

**Examples:**
- $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ – an extension of degree $2$
- $\mathbb{Q}(i) = \{a + bi \mid a, b \in \mathbb{Q}\}$ – also degree $2$
- $\mathbb{Q}(\zeta_p)$ – the $p$-th **cyclotomic field**, degree $p - 1$

### The Degree of an Extension

The **degree** $[L : K]$ is the dimension of $L$ as a $K$-vector space. It measures how "much larger" $L$ is compared to $K$.

**Degree formula (tower law).** For $K \subseteq M \subseteq L$:

$$
[L : K] = [L : M] \cdot [M : K]
$$

**Example:** $[\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}] = [\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}(\sqrt{2})] \cdot [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2 \cdot 2 = 4$.

### The Algebraic Closure

The **algebraic closure** $\overline{K}$ of $K$ is the smallest algebraically closed field containing $K$. For example:

- $\overline{\mathbb{R}} = \mathbb{C}$ (Fundamental Theorem of Algebra)
- $\overline{\mathbb{Q}}$ is the set of all algebraic numbers – countable, but not equal to $\mathbb{C}$

The **absolute Galois group** $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ – the symmetry group of $\overline{\mathbb{Q}}$ over $\mathbb{Q}$ – is the central object in Wiles' proof.

## 6. Principal Ideal Domains and Unique Factorisation

**Unique prime factorisation** (UPF) states: every element of an integral domain can be written essentially uniquely as a product of prime elements. In $\mathbb{Z}$, this is the Fundamental Theorem of Arithmetic: $60 = 2^2 \cdot 3 \cdot 5$.

**Theorem.** In every principal ideal domain, UPF holds.

The chain of implications:

$$
\text{Euclidean} \implies \text{Principal ideal domain} \implies \text{Unique factorisation domain (UPF)}
$$

### Where UPF Fails

In $\mathbb{Z}[\sqrt{-5}]$ we have two essentially different factorisations:

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

Here $2$, $3$, $1 + \sqrt{-5}$, and $1 - \sqrt{-5}$ are all irreducible, but the product has two different decompositions. UPF fails!

### Kummer's Rescue: Factorise Ideals

Kummer's insight: even if UPF fails at the **element level**, it holds at the **ideal level** in every Dedekind domain. The ideal $(6) = (2)(3)$ has a unique decomposition into prime ideals:

$$
(6) = (2, 1 + \sqrt{-5})^2 \cdot (3, 1 + \sqrt{-5}) \cdot (3, 1 - \sqrt{-5})
$$

The **class number** $h$ measures how far a ring is from being a PID: $h = 1$ if and only if the ring is a PID. For $\mathbb{Z}[\sqrt{-5}]$, $h = 2$.

## 7. Why Rings and Fields Matter for FLT

The algebraic structures of this article form the backdrop for Wiles' proof:

1. **Cyclotomic rings** $\mathbb{Z}[\zeta_p]$: Kummer's proof for regular primes uses the ideal structure of these rings.

2. **Field extensions**: Galois theory operates on field extensions – it is the bridge between equations and groups.

3. **Finite fields** $\mathbb{F}_p$: The reduction of elliptic curves modulo $p$ – that is, working over $\mathbb{F}_p$ instead of $\mathbb{Q}$ – yields the $a_p$-coefficients that appear in the $L$-series.

4. **Local rings** and **deformation rings**: In Wiles' proof, the rings $R$ and $T$ in the "$R = T$" theorem are local rings that parametrise families of Galois representations.

Ring theory provides the algebraic infrastructure on which the entire proof is built.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 3–4
- **Michael Artin**: *Algebra* – rings and fields treated comprehensively
- **Serge Lang**: *Algebra* – the standard reference for graduate students
