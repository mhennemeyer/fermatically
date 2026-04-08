---
title: "Propositional Logic"
description: "Propositions, truth values, conjunction, disjunction, and negation"
lang: en
type: vorwissen
---

# Propositional Logic

## Propositions and Truth Values

A **proposition** is a statement that can be assigned exactly one of the truth values **true** (T) or **false** (F).

**Examples of propositions:**

- "7 is a prime number." → true
- "4 is odd." → false
- "$2 + 3 = 5$." → true

**Not propositions:** questions ("Is 7 prime?"), commands ("Compute the GCD!"), or indeterminate expressions ("$x > 3$" — depends on $x$).

## Negation (¬)

The **negation** of a proposition $A$ reverses its truth value. Notation: $\neg A$.

| $A$ | $\neg A$ |
|-----|----------|
| T   | F        |
| F   | T        |

**Example.** $A$: "5 is even." (false) → $\neg A$: "5 is not even." (true)

## Conjunction (∧)

The **conjunction** $A \land B$ ("$A$ and $B$") is true if and only if **both** propositions are true.

| $A$ | $B$ | $A \land B$ |
|-----|-----|-------------|
| T   | T   | T           |
| T   | F   | F           |
| F   | T   | F           |
| F   | F   | F           |

**Example.** "7 is prime **and** 7 is odd." → true ∧ true = true.

## Disjunction (∨)

The **disjunction** $A \lor B$ ("$A$ or $B$") is true when **at least one** of the propositions is true.

| $A$ | $B$ | $A \lor B$ |
|-----|-----|------------|
| T   | T   | T          |
| T   | F   | T          |
| F   | T   | T          |
| F   | F   | F          |

The mathematical "or" is **inclusive**: even if both are true, the disjunction is true.

**Example.** "4 is even **or** 4 is prime." → true ∨ false = true.

## De Morgan's Laws

Two fundamental transformation rules:

$$
\neg (A \land B) \iff (\neg A) \lor (\neg B)
$$

$$
\neg (A \lor B) \iff (\neg A) \land (\neg B)
$$

In words: the negation of an "and" becomes an "or" of the negations — and vice versa.

---

## Summary

| Connective | Symbol | True when… |
|------------|--------|-----------|
| Negation | $\neg A$ | $A$ is false |
| Conjunction | $A \land B$ | both true |
| Disjunction | $A \lor B$ | at least one true |

## References

- Ebbinghaus, H.-D.; Flum, J.; Thomas, W.: *Mathematical Logic.* Springer, 3rd edition, 2021. Chapter 1.
