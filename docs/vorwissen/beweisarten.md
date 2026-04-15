---
title: "Proof Techniques"
description: "Direct proof, proof by contradiction, mathematical induction, and counterexample"
lang: en
type: vorwissen
---

# Proof Techniques

## Direct Proof

A **direct proof** establishes a statement $A \Rightarrow B$ by deriving $B$ from the assumption $A$ through logical steps.

**Example.** *Claim:* The sum of two even numbers is even.

*Proof.* Let $a = 2m$ and $b = 2n$ with $m, n \in \mathbb{Z}$. Then:

$$
a + b = 2m + 2n = 2(m + n)
$$

Since $m + n \in \mathbb{Z}$, the sum $a + b$ is even. $\square$

## Proof by Contradiction (Reductio ad Absurdum)

A **proof by contradiction** assumes the negation of the statement to be proved and derives a logical contradiction. Formally: to prove $A$, assume $\neg A$ and show that this leads to a contradiction.

**Example.** *Claim:* $\sqrt{2}$ is irrational.

*Proof.* Assume $\sqrt{2} = \frac{p}{q}$ with $p, q \in \mathbb{Z}$, $q \neq 0$, $\gcd(p, q) = 1$ (fully reduced). Then $2 = \frac{p^2}{q^2}$, so $p^2 = 2q^2$. Thus $p^2$ is even, so $p$ is even, so $p = 2k$. Substituting: $(2k)^2 = 2q^2$, so $4k^2 = 2q^2$, so $q^2 = 2k^2$. Thus $q$ is also even. Contradiction to $\gcd(p, q) = 1$. $\square$

## Proof by Contrapositive

**Proof by contrapositive** uses the logical equivalence $(A \Rightarrow B) \iff (\neg B \Rightarrow \neg A)$. Instead of proving $A \Rightarrow B$ directly, one proves $\neg B \Rightarrow \neg A$.

**Example.** *Claim:* If $n^2$ is even, then $n$ is even.

*Proof (contrapositive).* To show: if $n$ is odd, then $n^2$ is odd. Let $n = 2k + 1$. Then $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is odd. $\square$

## Mathematical Induction

**Mathematical induction** proves statements of the form "for all $n \geq n_0$, $P(n)$ holds" in two steps:

1. **Base case:** $P(n_0)$ is true.
2. **Inductive step:** For arbitrary $n \geq n_0$: if $P(n)$ is true (**inductive hypothesis**), then $P(n+1)$ is true.

**Example.** *Claim:* $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ for all $n \geq 1$.

*Base case:* $n = 1$: $\sum_{k=1}^{1} k = 1 = \frac{1 \cdot 2}{2}$. ✓

*Inductive step:* Assume the formula holds for $n$ (inductive hypothesis). Then:

$$
\sum_{k=1}^{n+1} k = \underbrace{\sum_{k=1}^{n} k}_{\frac{n(n+1)}{2}} + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}
$$

This is the formula for $n+1$. $\square$

## Proof by Counterexample

A **proof by counterexample** refutes a universal statement "for all $x$, $P(x)$ holds" by exhibiting a specific $x_0$ for which $P(x_0)$ is false.

**Example.** *Claim:* "All prime numbers are odd." *Counterexample:* $2$ is prime and even. $\square$

A single counterexample suffices to refute a universal statement.

---

## Summary

| Proof Technique | Approach |
|----------------|----------|
| Direct proof | Derive $B$ from $A$ directly |
| Contradiction | Assume $\neg A$ → derive contradiction |
| Contrapositive | Show $\neg B \Rightarrow \neg A$ |
| Induction | Base case + inductive step ($n$ to $n+1$) |
| Counterexample | Exhibit $x_0$ with $\neg P(x_0)$ |

## References

- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3rd edition, 2019.
- Hammack, Richard: *Book of Proof.* 3rd edition, 2018. (freely available)
