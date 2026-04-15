---
title: "Summation and Product Notation"
description: "Summation sign Σ, product sign Π, index sets, double sums, and important formulas"
lang: en
type: vorwissen
---

# Summation and Product Notation

## The Summation Sign Σ

The **summation sign** $\Sigma$ (Greek: Sigma) expresses the addition of multiple terms in compact form:

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n
$$

Here $k$ is the **index of summation**, $1$ is the **lower bound**, and $n$ is the **upper bound**. The expression $a_k$ is the **summand**.

**Example.**
$$
\sum_{k=1}^{4} k^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
$$

### Rules of Computation

- **Linearity:**
$$
\sum_{k=1}^{n} (c \cdot a_k + b_k) = c \cdot \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k
$$

- **Constant summands:**
$$
\sum_{k=1}^{n} c = n \cdot c
$$

- **Index shift:** Under the substitution $j = k - 1$, the sum $\sum_{k=1}^{n} a_k$ becomes $\sum_{j=0}^{n-1} a_{j+1}$. The value does not change.

## The Product Sign Π

The **product sign** $\Pi$ (Greek: Pi) expresses the multiplication of multiple factors:

$$
\prod_{k=1}^{n} a_k = a_1 \cdot a_2 \cdots a_n
$$

**Example.** The factorial can be written as a product:
$$
n! = \prod_{k=1}^{n} k = 1 \cdot 2 \cdot 3 \cdots n
$$

### Rules of Computation

- **Exponentiation:**
$$
\prod_{k=1}^{n} c = c^n
$$

- **Product of powers:**
$$
\prod_{k=1}^{n} a_k^{m} = \left(\prod_{k=1}^{n} a_k\right)^{m}
$$

## Sums over General Index Sets

The index need not start at $1$ or increase in integer steps. The general form is:

$$
\sum_{k \in I} a_k
$$

Here $I$ is a finite **index set**.

**Example.** Sum over all primes up to $10$:
$$
\sum_{p \in \{2,3,5,7\}} \frac{1}{p} = \frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7}
$$

## Double Sums

With two running indices, a **double sum** arises:

$$
\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}
$$

For finite sums, the order of summation is interchangeable:

$$
\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij}
$$

**Example.**
$$
\sum_{i=1}^{2} \sum_{j=1}^{3} ij = \sum_{i=1}^{2} (i \cdot 1 + i \cdot 2 + i \cdot 3) = \sum_{i=1}^{2} 6i = 6 + 12 = 18
$$

## Important Summation Formulas

The following formulas appear frequently in number theory:

**Arithmetic sum (Gauss):**
$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
$$

**Geometric sum** (for $q \neq 1$):
$$
\sum_{k=0}^{n} q^k = \frac{q^{n+1} - 1}{q - 1}
$$

**Geometric series** (for $|q| < 1$):
$$
\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}
$$

> "The notation $\sum$ for summation was introduced by Euler in 1755."
> — Florian Cajori, *A History of Mathematical Notations*, Dover, 1993.

## Application: Euler Product

A central example from number theory connects summation and product notation. Euler showed:

$$
\sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} \quad (s > 1)
$$

The left side is an infinite series (the Riemann zeta function), the right side an infinite product over all primes.

---

## Summary

| Notation | Meaning |
|----------|---------|
| $\sum_{k=1}^{n} a_k$ | $a_1 + a_2 + \cdots + a_n$ |
| $\prod_{k=1}^{n} a_k$ | $a_1 \cdot a_2 \cdots a_n$ |
| $\sum_{k \in I} a_k$ | Sum over index set $I$ |
| $\sum_{i}\sum_{j} a_{ij}$ | Double sum |
| $\sum_{k=0}^{\infty} q^k$ | Geometric series ($|q|<1$): $\frac{1}{1-q}$ |

## References

- Cajori, Florian: *A History of Mathematical Notations.* Dover, 1993. Volume 2, §§ 438–439.
- Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren: *Concrete Mathematics.* Addison-Wesley, 2nd edition, 1994. Chapter 2.
