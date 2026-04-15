---
title: "Primes and Why They Suffice"
slug: elementare-zahlentheorie/03-primzahlen-reduktion
series: elementare-zahlentheorie
part: 3
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - fermat
  - primes
  - reduction
requires: []
---

# Primes and Why They Suffice

!!! abstract "Summary"
    Why it suffices to prove Fermat's Last Theorem only for prime exponents –
    and how Kummer and Sophie Germain achieved important partial results with this insight.

## Prerequisites

- [What Is Fermat's Last Theorem?](01-was-ist-flt.md)
- [The Proof for $n = 4$](02-beweis-n4.md)

---

## 1. The Idea of Reduction

Fermat's Last Theorem asserts that $x^n + y^n = z^n$ has no solution in positive integers for **all** $n \geq 3$. That sounds like infinitely many cases – one for each $n$. Yet a simple argument drastically reduces the work: it suffices to prove the theorem for **prime exponents** $p$.

The basic idea: every integer $n \geq 3$ is either itself a prime, or it has a prime factor. And if FLT holds for one exponent, it also holds for all multiples of that exponent.

## 2. The Reduction Argument

**Theorem.** If FLT holds for $n = 4$ and for all odd primes $p$, then FLT holds for all $n \geq 3$.

**Proof.** Let $n \geq 3$ be arbitrary. We distinguish two cases:

**Case 1: $n$ is divisible by $4$.** Then $n = 4k$ for some $k \geq 1$, and a solution $x^n + y^n = z^n$ would be equivalent to:

$$
(x^k)^4 + (y^k)^4 = (z^k)^4
$$

This would be a solution of FLT for $n = 4$ – which does not exist by Fermat's proof.

**Case 2: $n$ has an odd prime factor $p$.** Then $n = pm$ for some $m \geq 1$, and a solution $x^n + y^n = z^n$ would be equivalent to:

$$
(x^m)^p + (y^m)^p = (z^m)^p
$$

This would be a solution of FLT for the prime exponent $p$ – which does not exist by assumption.

**Case 3: There is no third case.** Every integer $n \geq 3$ is either divisible by $4$, or it has an odd prime factor (or both). For the only numbers without an odd prime factor are the powers of two $2^k$, and for $k \geq 2$, $2^k$ is divisible by $4$. $\square$

!!! note "Why does $n = 4$ suffice instead of $n = 2$?"
    The reduction works via prime factors. The number $n = 4$ is not a prime, but it covers the case of powers of two: $n = 4, 8, 12, 16, \ldots$ are all handled by Case 1. The only remaining cases are the odd primes $p = 3, 5, 7, 11, 13, \ldots$

## 3. What Remains to Be Done?

After the reduction, the task is clear:

$$
\boxed{\text{Show: } x^p + y^p = z^p \text{ has no solution for all odd primes } p.}
$$

Together with Fermat's proof for $n = 4$, this would completely prove FLT. That sounds like a simplification – and it is. Instead of covering all natural numbers from $3$ upwards, one "only" needs to handle the primes. But there are infinitely many primes, and working through them one by one is not an option.

The history of partial proofs illustrates the dilemma:

| Period | Result | Exponents |
|--------|--------|-----------|
| ca. 1640 | Fermat | $n = 4$ |
| 1770 | Euler | $p = 3$ |
| 1825 | Dirichlet, Legendre | $p = 5$ |
| 1839 | Lamé | $p = 7$ |
| 1847–1857 | Kummer | all regular $p$ |
| 1993 | Computer | all $p \leq 4{,}000{,}000$ |

## 4. Sophie Germain's Breakthrough

**Sophie Germain** (1776–1831) achieved in 1823 the first partial success covering infinitely many primes at once. Her idea: instead of directly solving $x^p + y^p = z^p$, she distinguished two cases:

- **Case 1**: $p$ divides none of the values $x$, $y$, $z$ (i.e., $p \nmid xyz$)
- **Case 2**: $p$ divides at least one of the values $x$, $y$, $z$ (i.e., $p \mid xyz$)

**Theorem (Sophie Germain).** Let $p$ be an odd prime such that $q = 2p + 1$ is also prime. Then $x^p + y^p = z^p$ has no solution with $p \nmid xyz$.

A prime $p$ with the property that $2p + 1$ is also prime is called a **Germain prime**. Examples: $2, 3, 5, 11, 23, 29, 41, 53, 83, 89, \ldots$

It is conjectured that there are infinitely many Germain primes – but this remains unproven to this day. Nevertheless, Germain's result was a conceptual milestone: it was the first method that systematically worked for an entire class of exponents simultaneously.

**The proof idea.** Germain uses the fact that in $\mathbb{Z}/q\mathbb{Z}$ (the integers modulo $q = 2p + 1$), the $p$-th powers have a special structure. If $q$ is prime and $q = 2p + 1$, then in $\mathbb{Z}/q\mathbb{Z}$ there are only three $p$-th powers: $0$, $1$, and $-1$. It follows that a solution $x^p + y^p \equiv z^p \pmod{q}$ forces $q$ to divide one of the values $x$, $y$, $z$. With further analysis, Germain can then exclude Case 1 ($p \nmid xyz$).

## 5. Kummer's Revolution: Regular Primes

**Ernst Eduard Kummer** (1810–1893) went one decisive step further. His work in the 1840s and 1850s revolutionised algebraic number theory and delivered the most comprehensive partial result for FLT up to that point.

### The idea: Factorisation in the cyclotomic field

For an odd prime $p$, let $\zeta_p = e^{2\pi i/p}$ be a primitive $p$-th root of unity. The equation $x^p + y^p = z^p$ can be factorised in the ring $\mathbb{Z}[\zeta_p]$:

$$
x^p + y^p = \prod_{k=0}^{p-1} (x + \zeta_p^k \, y) = z^p
$$

If **unique prime factorisation** (UPF) held in $\mathbb{Z}[\zeta_p]$, one could derive a contradiction directly from this factorisation – similarly to the proof for $n = 4$.

### The problem: UPF does not always hold

Lamé believed in 1847 that he had found a proof of FLT in precisely this way. But Kummer pointed out that UPF in $\mathbb{Z}[\zeta_p]$ does **not** hold for all primes. For $p = 23$, for example, it fails – there are elements with several essentially distinct factorisations.

### Kummer's solution: Ideal theory

To compensate for the failure of UPF, Kummer introduced **ideal numbers** – precursors of modern **ideals** in ring theory. The basic idea: instead of factorising elements, one factorises *ideals*. And for ideals, UPF **always** holds (in Dedekind domains).

The measure for the failure of UPF at the element level is the **class number** $h_p$ of the cyclotomic field $\mathbb{Q}(\zeta_p)$. We have: $h_p = 1$ if and only if UPF holds in $\mathbb{Z}[\zeta_p]$.

### Regular primes

Kummer called a prime $p$ **regular** if $p$ does not divide the class number $h_p$: $p \nmid h_p$.

**Theorem (Kummer, 1850).** If $p$ is a regular prime, then $x^p + y^p = z^p$ has no solution in positive integers.

**Examples of regular primes:** $3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, \ldots$

**Irregular primes (up to 100):** $37, 59, 67$

Kummer's method thus proved FLT for most small primes – but not all. The irregular primes turned out to be stubborn exceptions.

!!! note "How common are regular primes?"
    Heuristic arguments suggest that approximately $e^{-1/2} \approx 60.6\%$ of all primes are regular. It is conjectured that there are infinitely many regular (and infinitely many irregular) primes – neither has been proved.

## 6. The Limits of Elementary Methods

The history of partial proofs reveals a clear pattern: each new case required deeper tools.

- **$n = 4$**: Elementary descent in $\mathbb{Z}$ (Fermat)
- **$n = 3$**: Descent in $\mathbb{Z}[\omega]$ – entry into algebraic number theory (Euler)
- **$n = 5, 7$**: Elaborate case distinctions in cyclotomic fields (Dirichlet, Legendre, Lamé)
- **Regular $p$**: Ideal theory and class numbers (Kummer)
- **All $p$**: ???

Kummer's method hit a fundamental barrier: the class number $h_p$ grows with $p$, and there is no general way to force regularity. After Kummer, it was clear that an entirely new approach would be needed – one that no longer argues case by case, but treats the equation $x^p + y^p = z^p$ for *all* $p$ simultaneously.

This approach finally came via a detour that became clear only 100 years later: the connection between elliptic curves and modular forms. But before we get there, we first need to understand the proof for $n = 3$ – and see what happens when one extends the number domain for the first time.

---

## Further Reading

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Ch. 1–2
- **Harold Edwards**: *Fermat's Last Theorem* – detailed account of Kummer's work
- **Paulo Ribenboim**: *Fermat's Last Theorem for Amateurs* – accessible overview of the partial proofs
