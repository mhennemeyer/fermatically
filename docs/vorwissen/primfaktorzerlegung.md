---
title: "Prime Factorization"
description: "Fundamental theorem of arithmetic, existence and uniqueness of factorization, failure in extended rings"
lang: en
type: vorwissen
---

# Prime Factorization

## Prime Numbers

A natural number $p > 1$ is called a **prime number** if it is divisible only by $1$ and itself. The first primes are:

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \ldots
$$

Every natural number $n > 1$ that is not prime is called **composite** and has at least one divisor $d$ with $1 < d < n$.

## Fundamental Theorem of Arithmetic

Every natural number $n > 1$ can be written as a product of primes, and this factorization is **unique up to the order of the factors**:

$$
n = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}
$$

Here $p_1 < p_2 < \cdots < p_k$ are primes and $e_1, e_2, \ldots, e_k \geq 1$ are the corresponding exponents.

> "The unique factorization of integers into primes is the foundation on which all of number theory rests."
> — Kenneth Ireland, Michael Rosen, *A Classical Introduction to Modern Number Theory*, Springer, 1990.

**Example.**
$$
360 = 2^3 \cdot 3^2 \cdot 5
$$

The factorization $360 = 8 \cdot 45 = 8 \cdot 9 \cdot 5$ leads to the same prime factors.

### Existence

Existence follows by strong induction: if $n$ is prime, then $n$ itself is the factorization. If $n$ is composite, there exists a divisor $1 < d < n$ with $n = d \cdot (n/d)$. Both factors are less than $n$ and have a prime factorization by the induction hypothesis.

### Uniqueness

Uniqueness relies on **Euclid's lemma**: if a prime $p$ divides a product $a \cdot b$, then $p$ divides at least one of the factors:

$$
p \mid ab \implies p \mid a \text{ or } p \mid b
$$

This lemma follows from Bézout's lemma (see: Divisibility and GCD).

## Applications

### GCD and LCM via Prime Factorization

Given the factorizations $a = \prod p_i^{\alpha_i}$ and $b = \prod p_i^{\beta_i}$:

$$
\gcd(a, b) = \prod p_i^{\min(\alpha_i, \beta_i)}, \quad \operatorname{lcm}(a, b) = \prod p_i^{\max(\alpha_i, \beta_i)}
$$

**Example.** $a = 2^3 \cdot 3 \cdot 5^2 = 600$ and $b = 2^2 \cdot 3^2 \cdot 7 = 252$:

$$
\gcd(600, 252) = 2^2 \cdot 3 = 12, \quad \operatorname{lcm}(600, 252) = 2^3 \cdot 3^2 \cdot 5^2 \cdot 7 = 12600
$$

### Number of Divisors

The number of positive divisors of $n = p_1^{e_1} \cdots p_k^{e_k}$ is:

$$
\tau(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)
$$

**Example.** $360 = 2^3 \cdot 3^2 \cdot 5$ has $\tau(360) = 4 \cdot 3 \cdot 2 = 24$ divisors.

## Failure of Unique Factorization in Extended Rings

The fundamental theorem holds in $\mathbb{Z}$, but **not in all number rings**. The classical counterexample:

In $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$:

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

Both factorizations consist of irreducible elements that cannot be transformed into each other. Unique prime factorization fails.

This problem motivated Kummer's introduction of **ideal numbers** (today: ideals in Dedekind domains), which restore unique factorization at the level of ideals. Kummer's work was a decisive step in the history of Fermat's Last Theorem.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Prime number | $p > 1$ with exactly two divisors: $1$ and $p$ |
| Fundamental theorem | Every $n > 1$ is a unique product of primes |
| Euclid's lemma | $p \mid ab \implies p \mid a$ or $p \mid b$ |
| $\gcd$ via factorization | $\prod p_i^{\min(\alpha_i, \beta_i)}$ |
| $\tau(n)$ | Number of divisors: $\prod (e_i + 1)$ |

## References

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6th edition, 2008. Chapter 2.
- Ireland, Kenneth; Rosen, Michael: *A Classical Introduction to Modern Number Theory.* Springer, 2nd edition, 1990. Chapter 1.
