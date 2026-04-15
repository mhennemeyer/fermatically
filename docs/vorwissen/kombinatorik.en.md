---
title: "Combinatorics"
description: "Factorial, binomial coefficient, and the binomial theorem"
lang: en
type: vorwissen
---

# Combinatorics

## Factorial

The **factorial** of a natural number $n$ is the product of all positive integers up to $n$:

$$
n! = 1 \cdot 2 \cdot 3 \cdots n = \prod_{k=1}^{n} k
$$

By convention, $0! = 1$.

**Example.** $5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$.

### Combinatorial Meaning

$n!$ is the number of **permutations** of an $n$-element set — the number of ways to arrange $n$ distinct objects in order.

**Example.** The set $\{a, b, c\}$ has $3! = 6$ permutations: $abc, acb, bac, bca, cab, cba$.

In group theory: the symmetric group $S_n$ (the group of all permutations of $n$ elements) has **order** $|S_n| = n!$.

## Binomial Coefficient

The **binomial coefficient** $\binom{n}{k}$ gives the number of ways to choose $k$ elements from an $n$-element set (without regard to order):

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!} \quad \text{for } 0 \leq k \leq n
$$

Read as "$n$ choose $k$".

**Example.** $\binom{5}{2} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \cdot 6} = 10$. From five elements, ten distinct pairs can be formed.

### Properties

- **Symmetry:** $\binom{n}{k} = \binom{n}{n-k}$
- **Boundary cases:** $\binom{n}{0} = \binom{n}{n} = 1$
- **Recursion (Pascal's rule):**

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

This recursion generates **Pascal's triangle**:

$$
\begin{array}{ccccccc}
& & & 1 & & & \\
& & 1 & & 1 & & \\
& 1 & & 2 & & 1 & \\
1 & & 3 & & 3 & & 1 \\
\end{array}
$$

## Binomial Theorem

For any $a, b$ and $n \in \mathbb{N}_0$:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

> "The binomial theorem is one of the most useful formulas in all of mathematics."
> — Ronald L. Graham, Donald E. Knuth, Oren Patashnik, *Concrete Mathematics*, Addison-Wesley, 1994.

**Example.** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$.

### Special Cases

- **$a = 1, b = 1$:** $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ (total number of subsets of an $n$-element set).
- **$a = 1, b = -1$:** $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$.

## Application in Number Theory

Binomial coefficients appear in number theory in several contexts:

- **Fermat's little theorem:** From $\binom{p}{k} \equiv 0 \pmod{p}$ for $0 < k < p$ (with $p$ prime), it follows that $(a+b)^p \equiv a^p + b^p \pmod{p}$.
- **Symmetric group:** The order $|S_n| = n!$ determines the structure of Galois groups of finite extensions.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Factorial | $n! = 1 \cdot 2 \cdots n$, $0! = 1$ |
| Permutations | $n!$ arrangements of $n$ elements |
| Binomial coefficient | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| Pascal's rule | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ |
| Binomial theorem | $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k}b^k$ |

## References

- Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren: *Concrete Mathematics.* Addison-Wesley, 2nd edition, 1994. Chapter 5.
- Aigner, Martin: *Discrete Mathematics.* Springer, 2007. Chapter 1.
