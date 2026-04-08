---
title: "Modular Arithmetic"
description: "Congruence, computing modulo n, and residue classes"
lang: en
type: vorwissen
---

# Modular Arithmetic

## Congruence

Two integers $a$ and $b$ are **congruent modulo $n$** if their difference is divisible by $n$:

$$
a \equiv b \pmod{n} \iff n \mid (a - b)
$$

Equivalently: $a$ and $b$ leave the same remainder upon division by $n$.

**Example.** $17 \equiv 5 \pmod{4}$, since $17 - 5 = 12$ and $4 \mid 12$. Both numbers leave remainder $1$ when divided by $4$.

## Computing Modulo n

### Addition

$$
a \equiv a' \pmod{n},\; b \equiv b' \pmod{n} \implies a + b \equiv a' + b' \pmod{n}
$$

**Example.** $7 \equiv 2 \pmod{5}$ and $8 \equiv 3 \pmod{5}$. Then $7 + 8 = 15 \equiv 2 + 3 = 5 \equiv 0 \pmod{5}$. ✓

### Multiplication

$$
a \equiv a' \pmod{n},\; b \equiv b' \pmod{n} \implies a \cdot b \equiv a' \cdot b' \pmod{n}
$$

**Example.** $7 \equiv 2 \pmod{5}$ and $8 \equiv 3 \pmod{5}$. Then $7 \cdot 8 = 56 \equiv 2 \cdot 3 = 6 \equiv 1 \pmod{5}$. ✓

### Exponentiation

$$
a \equiv b \pmod{n} \implies a^k \equiv b^k \pmod{n} \quad \text{for all } k \geq 0
$$

**Example.** $2^{10} = 1024$. Since $2 \equiv -1 \pmod{3}$, it follows that $2^{10} \equiv (-1)^{10} = 1 \pmod{3}$.

### Division (restricted)

Division is **not** generally permitted. From $ac \equiv bc \pmod{n}$ it follows that $a \equiv b \pmod{n}$ only if $\gcd(c, n) = 1$.

## Residue Classes

The **residue class** of $a$ modulo $n$ is the set of all integers congruent to $a$:

$$
[a]_n = \{a + kn : k \in \mathbb{Z}\} = \{\ldots, a - 2n, a - n, a, a + n, a + 2n, \ldots\}
$$

For $n = 3$ there are exactly three residue classes:

- $[0]_3 = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$
- $[1]_3 = \{\ldots, -5, -2, 1, 4, 7, \ldots\}$
- $[2]_3 = \{\ldots, -4, -1, 2, 5, 8, \ldots\}$

The set of all residue classes modulo $n$ is denoted $\mathbb{Z}/n\mathbb{Z}$ (or $\mathbb{Z}_n$).

## Application: Divisibility Rules

Modular arithmetic explains classical divisibility rules:

- **Divisibility by 3:** A number is divisible by $3$ $\iff$ its digit sum is divisible by $3$. Reason: $10 \equiv 1 \pmod{3}$, so $10^k \equiv 1 \pmod{3}$.
- **Divisibility by 9:** Analogous, since $10 \equiv 1 \pmod{9}$.

---

## Summary

| Concept | Definition |
|---------|-----------|
| $a \equiv b \pmod{n}$ | $n \mid (a-b)$ |
| Residue class $[a]_n$ | $\{a + kn : k \in \mathbb{Z}\}$ |
| Addition mod $n$ | $(a + b) \bmod n$ |
| Multiplication mod $n$ | $(a \cdot b) \bmod n$ |
| $\mathbb{Z}/n\mathbb{Z}$ | Set of residue classes modulo $n$ |

## References

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6th edition, 2008. Chapter 5.
- Burton, David M.: *Elementary Number Theory.* McGraw-Hill, 7th edition, 2010. Chapter 4.
