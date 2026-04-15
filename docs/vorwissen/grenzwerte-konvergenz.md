---
title: "Limits and Convergence"
description: "Sequences, series, Cauchy sequences, completion, and the geometric series"
lang: en
type: vorwissen
---

# Limits and Convergence

## Sequences

A **sequence** of real numbers is a mapping $\mathbb{N} \to \mathbb{R}$, written as $(a_n)_{n \geq 1}$ or simply $(a_n)$. The number $a_n$ is called the **$n$-th term** of the sequence.

**Example.** The sequence $a_n = \frac{1}{n}$ gives $1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots$

## Convergence

A sequence $(a_n)$ **converges** to the **limit** $L \in \mathbb{R}$ if for every $\varepsilon > 0$ there exists an $N \in \mathbb{N}$ such that:

$$
|a_n - L| < \varepsilon \quad \text{for all } n \geq N
$$

Notation: $\lim_{n \to \infty} a_n = L$ or $a_n \to L$.

The terms of the sequence approach $L$ to arbitrary precision — from some index onward, all terms lie in the interval $(L - \varepsilon, L + \varepsilon)$.

**Example.** $\lim_{n \to \infty} \frac{1}{n} = 0$, since for every $\varepsilon > 0$, $\frac{1}{n} < \varepsilon$ whenever $n > \frac{1}{\varepsilon}$.

A sequence that does not converge is called **divergent**.

### Rules of Computation

For convergent sequences with $a_n \to A$ and $b_n \to B$:

- $a_n + b_n \to A + B$
- $a_n \cdot b_n \to A \cdot B$
- $\frac{a_n}{b_n} \to \frac{A}{B}$ (provided $B \neq 0$)

## Series

An **(infinite) series** is the sequence of partial sums of a sequence $(a_k)$:

$$
S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n
$$

The series $\sum_{k=1}^{\infty} a_k$ **converges** if the sequence $(S_n)$ converges:

$$
\sum_{k=1}^{\infty} a_k = \lim_{n \to \infty} S_n
$$

### Geometric Series

The most important series in elementary analysis: for $|q| < 1$:

$$
\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}
$$

**Example.** $\sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k = \frac{1}{1 - 1/2} = 2$.

For $|q| \geq 1$, the geometric series diverges.

### Necessary Condition

If $\sum a_k$ converges, then $a_k \to 0$. The converse is false: the **harmonic series** $\sum_{k=1}^{\infty} \frac{1}{k}$ diverges, even though $\frac{1}{k} \to 0$.

## Cauchy Sequences

A sequence $(a_n)$ is a **Cauchy sequence** if its terms become arbitrarily close to each other: for every $\varepsilon > 0$ there exists an $N$ such that:

$$
|a_m - a_n| < \varepsilon \quad \text{for all } m, n \geq N
$$

> "The concept of Cauchy sequence captures convergence without reference to the limit itself."
> — Walter Rudin, *Principles of Mathematical Analysis*, McGraw-Hill, 1976.

In $\mathbb{R}$: a sequence converges if and only if it is a Cauchy sequence. This property is called the **completeness** of $\mathbb{R}$.

## Completion

Not every metric space is complete. The **completion** of a space constructs a larger space in which all Cauchy sequences converge.

The central example in number theory: the rational numbers $\mathbb{Q}$ are not complete. Their completion with respect to the ordinary absolute value yields $\mathbb{R}$. Their completion with respect to the **$p$-adic absolute value** yields the $p$-adic numbers $\mathbb{Q}_p$ — an entirely different number field that plays a central role in modern number theory.

---

## Summary

| Concept | Definition |
|---------|-----------|
| Convergence | $\lim_{n\to\infty} a_n = L$: $\forall\varepsilon>0\ \exists N: n\geq N \Rightarrow |a_n-L|<\varepsilon$ |
| Series | $\sum_{k=1}^{\infty} a_k = \lim_{n\to\infty} \sum_{k=1}^{n} a_k$ |
| Geometric series | $\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}$ for $|q|<1$ |
| Cauchy sequence | $\forall\varepsilon>0\ \exists N: m,n\geq N \Rightarrow |a_m-a_n|<\varepsilon$ |
| Completeness | Every Cauchy sequence converges |
| Completion | Construction of a complete space from an incomplete one |

## References

- Rudin, Walter: *Principles of Mathematical Analysis.* McGraw-Hill, 3rd edition, 1976. Chapter 3.
- Bartle, Robert G.; Sherbert, Donald R.: *Introduction to Real Analysis.* Wiley, 4th edition, 2011. Chapters 3–4.
