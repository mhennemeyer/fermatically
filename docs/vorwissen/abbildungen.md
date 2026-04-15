---
title: "Maps (Functions)"
description: "Domain, codomain, injective, surjective, bijective"
lang: en
type: vorwissen
---

# Maps (Functions)

## Definition

A **map** (or **function**) $f: A \to B$ assigns to each element $a \in A$ exactly one element $f(a) \in B$.

- $A$ is the **domain**.
- $B$ is the **codomain**.
- $f(A) = \{f(a) : a \in A\} \subseteq B$ is the **image**.

**Example.** $f: \mathbb{Z} \to \mathbb{Z}$ with $f(x) = x^2$. Here $f(3) = 9$ and $f(-3) = 9$.

## Injectivity

A map $f$ is **injective** (one-to-one) if distinct inputs produce distinct outputs:

$$
f(a_1) = f(a_2) \implies a_1 = a_2
$$

**Example.** $f(x) = 2x$ is injective: from $2a = 2b$ it follows that $a = b$.

**Counterexample.** $f(x) = x^2$ on $\mathbb{Z}$ is not injective: $f(3) = f(-3) = 9$, but $3 \neq -3$.

## Surjectivity

A map $f: A \to B$ is **surjective** (onto) if every element in $B$ has at least one preimage:

$$
\forall b \in B\; \exists a \in A: f(a) = b
$$

Equivalently: $f(A) = B$.

**Example.** $f: \mathbb{Z} \to \mathbb{Z}$ with $f(x) = x + 1$ is surjective: for every $b \in \mathbb{Z}$, $a = b - 1$ is a preimage.

**Counterexample.** $f: \mathbb{Z} \to \mathbb{Z}$ with $f(x) = x^2$ is not surjective: $-1$ has no preimage, since $x^2 \geq 0$ for all $x$.

## Bijectivity

A map is **bijective** if it is both injective and surjective. Every element in $B$ then has exactly one preimage.

Bijective maps possess an **inverse map** $f^{-1}: B \to A$ with $f^{-1}(f(a)) = a$ and $f(f^{-1}(b)) = b$.

**Example.** $f: \mathbb{R} \to \mathbb{R}$ with $f(x) = 2x + 1$ is bijective. The inverse is $f^{-1}(y) = \frac{y - 1}{2}$.

## Composition

The **composition** of two maps $f: A \to B$ and $g: B \to C$ is the map $g \circ f: A \to C$ with:

$$
(g \circ f)(a) = g(f(a))
$$

**Example.** $f(x) = x + 1$ and $g(x) = x^2$. Then $(g \circ f)(3) = g(f(3)) = g(4) = 16$.

Order matters: $(f \circ g)(3) = f(g(3)) = f(9) = 10 \neq 16$.

---

## Summary

| Property | Meaning |
|----------|---------|
| Injective | Distinct inputs → distinct outputs |
| Surjective | Every $b \in B$ has a preimage |
| Bijective | Injective and surjective; inverse exists |
| $g \circ f$ | Composition: first $f$, then $g$ |

## References

- Hammack, Richard: *Book of Proof.* 3rd edition, 2018. Chapter 12.
