---
title: "What Is a Proof?"
description: "Axioms, definitions, theorems, and lemmas – the building blocks of mathematical reasoning"
lang: en
type: vorwissen
---

# What Is a Proof?

## Definition

A **mathematical proof** is a complete chain of logical deductions that derives a claim from already accepted statements (axioms, definitions, previously proven theorems).

A proof is not an empirical verification. The fact that a statement holds for a thousand examples does not prove it. A proof shows that it holds for **all** admissible cases.

## The Building Blocks

### Axioms

**Axioms** are foundational assumptions accepted without proof. They form the basis of a mathematical system.

**Example.** Peano axioms for the natural numbers:
- $0$ is a natural number.
- Every natural number $n$ has a successor $S(n)$.
- $0$ is not the successor of any natural number.

### Definitions

**Definitions** establish the meaning of a term. They are neither true nor false — they are conventions.

**Example.** *Definition:* A natural number $p > 1$ is called a **prime number** if its only positive divisors are $1$ and $p$.

### Theorems

A **theorem** is a mathematical statement that has been proved.

**Example.** *Fundamental Theorem of Arithmetic:* Every natural number $n > 1$ can be uniquely represented as a product of prime numbers (up to the order of factors).

### Lemmas

A **lemma** is an auxiliary result — a proven statement that primarily serves as a stepping stone for a larger proof.

**Example.** *Bézout's Lemma:* For $a, b \in \mathbb{Z}$, there exist $x, y \in \mathbb{Z}$ with $\gcd(a, b) = xa + yb$.

### Corollaries

A **corollary** is a direct consequence of an already proven theorem.

**Example.** *Corollary:* If $a$ and $b$ are coprime and $a \mid bc$, then $a \mid c$. (Follows from Bézout's Lemma.)

## Conjecture vs. Theorem

| Term | Status | Example |
|------|--------|---------|
| **Conjecture** | Unproven statement with supporting evidence | Goldbach's conjecture (1742, open) |
| **Theorem** | Proven statement | Fermat's Last Theorem (stated 1637, proved 1995) |

A conjecture becomes a theorem once a valid proof is provided. "Fermat's Last Theorem" is historically called a "theorem" despite being a conjecture for 358 years.

## Structure of a Proof

A typical proof follows this pattern:

1. **Hypothesis:** What is assumed?
2. **Claim:** What is to be shown?
3. **Proof:** Logical chain from hypothesis to claim.
4. **QED / $\square$:** Marks the end of the proof.

**Example.**

*Hypothesis:* $a$ and $b$ are even numbers.

*Claim:* $a \cdot b$ is divisible by 4.

*Proof.* Since $a$ is even, there exists $m \in \mathbb{Z}$ with $a = 2m$. Since $b$ is even, there exists $n \in \mathbb{Z}$ with $b = 2n$. Then:

$$
a \cdot b = 2m \cdot 2n = 4mn
$$

Since $mn \in \mathbb{Z}$, the product $a \cdot b$ is divisible by 4. $\square$

---

## Summary

| Building Block | Role |
|---------------|------|
| Axiom | Foundational assumption without proof |
| Definition | Convention establishing a term's meaning |
| Theorem | Proven statement |
| Lemma | Auxiliary result for a larger proof |
| Corollary | Direct consequence of a theorem |
| Conjecture | Unproven statement with evidence |

## References

- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3rd edition, 2019. Chapter 1.
- Hammack, Richard: *Book of Proof.* 3rd edition, 2018. Chapter 1.
