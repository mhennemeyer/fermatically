---
title: "Implication and Equivalence"
description: "Logical implication, contrapositive, and equivalence of propositions"
lang: en
type: vorwissen
---

# Implication and Equivalence

## Implication (⟹)

The **implication** $A \Rightarrow B$ ("if $A$, then $B$") is false only when $A$ is true and $B$ is false.

| $A$ | $B$ | $A \Rightarrow B$ |
|-----|-----|--------------------|
| T   | T   | T                  |
| T   | F   | F                  |
| F   | T   | T                  |
| F   | F   | T                  |

**Key observation:** If the hypothesis $A$ is false, the implication is always true — regardless of $B$. This convention is called **ex falso quodlibet**.

**Example.** "If $n$ is divisible by 6, then $n$ is divisible by 3." → For $n = 12$: true ⟹ true = true. For $n = 5$: false ⟹ false = true.

## Equivalence to ¬A ∨ B

The implication $A \Rightarrow B$ is **logically equivalent** to the disjunction $\neg A \lor B$:

$$
(A \Rightarrow B) \iff (\neg A \lor B)
$$

| $A$ | $B$ | $\neg A$ | $\neg A \lor B$ | $A \Rightarrow B$ |
|-----|-----|----------|------------------|--------------------|
| T   | T   | F        | T                | T                  |
| T   | F   | F        | F                | F                  |
| F   | T   | T        | T                | T                  |
| F   | F   | T        | T                | T                  |

The columns match. This means: "if $A$, then $B$" says the same as "$A$ is false or $B$ is true".

## Contrapositive

The **contrapositive** of an implication $A \Rightarrow B$ is $\neg B \Rightarrow \neg A$. Both are logically equivalent:

$$
(A \Rightarrow B) \iff (\neg B \Rightarrow \neg A)
$$

**Example.** "If $n^2$ is even, then $n$ is even." The contrapositive reads: "If $n$ is odd, then $n^2$ is odd." Both statements are equivalent.

The contrapositive is a frequently used proof technique: instead of showing $A \Rightarrow B$ directly, one shows $\neg B \Rightarrow \neg A$.

## Converse

The **converse** of $A \Rightarrow B$ is $B \Rightarrow A$. The converse is **not** automatically equivalent to the original statement.

**Example.** "If $n$ is divisible by 6, then $n$ is divisible by 3." → true. Converse: "If $n$ is divisible by 3, then $n$ is divisible by 6." → false ($n = 9$).

## Equivalence (⟺)

The **equivalence** $A \Leftrightarrow B$ ("$A$ if and only if $B$") is true when both propositions have the same truth value:

| $A$ | $B$ | $A \Leftrightarrow B$ |
|-----|-----|------------------------|
| T   | T   | T                      |
| T   | F   | F                      |
| F   | T   | F                      |
| F   | F   | T                      |

Equivalence corresponds to the conjunction of both directions:

$$
(A \Leftrightarrow B) \iff (A \Rightarrow B) \land (B \Rightarrow A)
$$

**Example.** "$n$ is even $\Leftrightarrow$ $n^2$ is even." Both directions hold, so equivalence obtains.

---

## Summary

| Connective | Symbol | Meaning |
|------------|--------|---------|
| Implication | $A \Rightarrow B$ | "if $A$, then $B$"; equivalent to $\neg A \lor B$ |
| Contrapositive | $\neg B \Rightarrow \neg A$ | equivalent to $A \Rightarrow B$ |
| Converse | $B \Rightarrow A$ | **not** equivalent to $A \Rightarrow B$ |
| Equivalence | $A \Leftrightarrow B$ | both directions hold |

## References

- Ebbinghaus, H.-D.; Flum, J.; Thomas, W.: *Mathematical Logic.* Springer, 3rd edition, 2021. Chapter 1.
- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3rd edition, 2019. Chapter 2.
