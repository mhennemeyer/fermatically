---
title: "The 3-5 Switch and the Conclusion"
slug: fermat-wiles/07-3-5-switch
series: fermat-wiles
part: 7
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - 3-5-switch
  - langlands-tunnell
  - modularity
requires:
  - fermat-wiles/06-taylor-wiles-trick
---
# The 3-5 Switch and the Conclusion

!!! abstract "Summary"
    The 3-5 switch is the elegant final building block in Wiles' proof.
    The Langlands–Tunnell theorem provides residual modularity
    for $p = 3$. When the 3-representation is reducible, Wiles switches
    to $p = 5$ and constructs an auxiliary curve that provides the entry
    point. In this way, every semistable elliptic curve is recognised as modular
    – and Fermat's Last Theorem is proved.

## Prerequisites

- [The Taylor–Wiles Trick](../06-taylor-wiles-trick/article_en.md) – patching argument and $R = T$

---

## 1. The Problem with $p = 3$

### Recall: The proof strategy

Wiles' proof of the modularity of semistable curves has two stages:

1. **Residual modularity**: Show that $\bar{\rho}_{E,p}$ is modular.
2. **Lifting**: Prove $R = T$ to pass from residual to full modularity.

Stage 2 is done (Taylor–Wiles trick). Stage 1 remains: where does residual modularity come from?

### Langlands–Tunnell

For $p = 3$ there is a powerful result:

!!! note "Theorem (Langlands–Tunnell)"
    Let $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_3)$ be a continuous,
    odd representation. Then $\bar{\rho}$ is modular – there exists a
    modular form $f$ of weight 1 with $\bar{\rho} \cong \bar{\rho}_f$.

The proof uses a special property of $\text{GL}_2(\mathbb{F}_3)$: this group is **solvable** (it has order 48 and is isomorphic to an extension of $S_3$ by $\mathbb{Z}/2\mathbb{Z}$). For solvable groups, the tools of the **Langlands programme** are available – in particular base change for $\text{GL}_2$.

Langlands proved the modular forms correspondence for solvable Galois representations in 1980, and Tunnell refined the result in 1981.

### From weight 1 to weight 2

Langlands–Tunnell provides a modular form of **weight 1**, but we need weight 2 (for the connection with elliptic curves). Wiles solves this via a lifting argument:

From the weight-1 form $f$, one constructs a weight-2 form $g$ with $\bar{\rho}_g \cong \bar{\rho}_{E,3}$. This uses Hida's theory of ordinary $p$-adic modular forms.

---

## 2. Why $p = 3$ Is Not Enough

### The irreducibility condition

Wiles' proof of $R = T$ (and the Taylor–Wiles patching) requires that $\bar{\rho}_{E,p}$ be **irreducible**. For the Frey curve, this is automatically satisfied for $p \geq 5$ (by Mazur). But for a general semistable curve $E$, $\bar{\rho}_{E,3}$ can be **reducible**.

### When is $\bar{\rho}_{E,3}$ reducible?

The representation $\bar{\rho}_{E,3}$ is reducible if and only if $E$ has a rational **3-isogeny kernel** – a $G_{\mathbb{Q}}$-stable subspace of $E[3]$ of dimension 1 over $\mathbb{F}_3$. Geometrically, this means: there is an isogeny $E \to E'$ of degree 3 with rational kernel.

This does occur – there are infinitely many such curves. For these curves, the proof with $p = 3$ fails.

### The situation

| $\bar{\rho}_{E,3}$ | Modular? | Irreducible? | $R = T$ possible? |
|---------------------|----------|--------------|-------------------|
| irreducible | Yes (Langlands–Tunnell) | Yes | ✓ Proof works |
| reducible | Yes (Langlands–Tunnell) | **No** | ✗ Irreducibility missing |

---

## 3. The Switch to $p = 5$

### The idea

When $\bar{\rho}_{E,3}$ is reducible, consider $\bar{\rho}_{E,5}$ instead. The 5-representation has a good chance of being irreducible – because a curve having both a 3-isogeny kernel and a 5-isogeny kernel would be very special.

### Irreducibility of $\bar{\rho}_{E,5}$

Wiles shows: if $E$ is semistable and $\bar{\rho}_{E,3}$ is reducible, then $\bar{\rho}_{E,5}$ is **irreducible**. This follows from Mazur's classification of possible torsion structures of rational elliptic curves:

!!! note "Theorem (Mazur, 1978)"
    Let $E/\mathbb{Q}$ be an elliptic curve. If $E$ has a rational isogeny
    of degree $\ell$ (for a prime $\ell$), then $\ell \leq 19$ or
    $\ell \in \{37, 43, 67, 163\}$.

For a **semistable** curve, the possibilities can be further restricted. In particular, there is no semistable curve with a simultaneous rational 3- and 5-isogeny kernel (this would imply a rational 15-isogeny, which Mazur excludes).

### The new problem

Now we have $\bar{\rho}_{E,5}$ irreducible – but where does **residual modularity** come from? Langlands–Tunnell works only for $p = 3$, not for $p = 5$ (because $\text{GL}_2(\mathbb{F}_5)$ is **not solvable**).

Here comes the ingenious trick.

---

## 4. Constructing an Auxiliary Curve

### The strategy

Wiles seeks a **second elliptic curve** $E'$ with the following properties:

1. $E'[5] \cong E[5]$ as a Galois module (the 5-torsion agrees)
2. $\bar{\rho}_{E',3}$ is **irreducible** (so that $p = 3$ works for $E'$)
3. $E'$ is semistable

### Why such a curve exists

The set of elliptic curves $E'$ with $E'[5] \cong E[5]$ is parametrised by a **modular curve** $X(5)$ – a curve of genus 0 (hence rational!). There are therefore infinitely many such curves $E'$.

Among these infinitely many candidates, Wiles needs to find one that:
- is semistable (at all primes), and
- has $\bar{\rho}_{E',3}$ irreducible.

Since the condition "$\bar{\rho}_{E',3}$ reducible" excludes a proper subset and the parametrisation runs over a rational curve, such a curve $E'$ exists.

### The construction

Concretely: over the function field $\mathbb{Q}(t)$ there is a "universal" curve with the correct 5-torsion. By specialising at suitable rational values $t = t_0$, one obtains the desired auxiliary curve $E'$.

---

## 5. Closing the Chain

### Step 1: $E'$ is modular (via $p = 3$)

Since $\bar{\rho}_{E',3}$ is irreducible, we can apply the entire proof apparatus for $p = 3$:

$$
\bar{\rho}_{E',3} \text{ irreducible} \xrightarrow{\text{Langlands–Tunnell}} \bar{\rho}_{E',3} \text{ modular} \xrightarrow{R = T} \rho_{E',3} \text{ modular} \implies E' \text{ modular.}
$$

### Step 2: $E[5]$ is modular

Since $E'$ is modular, in particular: $\bar{\rho}_{E',5}$ is modular (the 5-residual representation comes from a modular form). Since $E'[5] \cong E[5]$, it follows:

$$
\bar{\rho}_{E,5} \cong \bar{\rho}_{E',5} \quad \text{is modular.}
$$

### Step 3: $E$ is modular (via $p = 5$)

Now we have the entry point for $p = 5$: $\bar{\rho}_{E,5}$ is modular and irreducible. The Taylor–Wiles trick gives $R = T$ for $p = 5$:

$$
\bar{\rho}_{E,5} \text{ modular + irreducible} \xrightarrow{R = T} \rho_{E,5} \text{ modular} \implies E \text{ modular.}
$$

### The complete chain

$$
\boxed{E'[5] \cong E[5]} \quad + \quad \boxed{E' \text{ modular (via } p=3\text{)}} \implies \boxed{\bar{\rho}_{E,5} \text{ modular}} \xrightarrow{R=T} \boxed{E \text{ modular}}
$$

---

## 6. FLT Is Proved

### The case distinction

For every semistable elliptic curve $E/\mathbb{Q}$:

**Case 1: $\bar{\rho}_{E,3}$ irreducible.** Langlands–Tunnell + Taylor–Wiles ($p = 3$) → $E$ modular. ✓

**Case 2: $\bar{\rho}_{E,3}$ reducible.** Then $\bar{\rho}_{E,5}$ is irreducible. Construct auxiliary curve $E'$ with $E'[5] \cong E[5]$ and $\bar{\rho}_{E',3}$ irreducible. Then: $E'$ modular (Case 1) → $\bar{\rho}_{E,5}$ modular → Taylor–Wiles ($p = 5$) → $E$ modular. ✓

**In both cases, $E$ is modular.** Since the Frey curve is semistable, Fermat's Last Theorem follows.

### The complete proof diagram

$$
\text{FLT solution} \xrightarrow{\text{Frey}} E_{\text{Frey}} \xrightarrow{\text{Wiles (3 or 3-5)}} \text{modular} \xrightarrow{\text{Ribet}} \text{contradiction}
$$

!!! note "Theorem (Wiles, Taylor–Wiles, 1995)"
    Every semistable elliptic curve over $\mathbb{Q}$ is modular.

!!! note "Corollary (Fermat's Last Theorem)"
    The equation $x^n + y^n = z^n$ has no solution in positive integers for $n \geq 3$.

---

## 7. Retrospective: The Complete Proof Structure

### From Fermat to Wiles

The complete proof connects ideas from over four centuries of mathematics:

| Year | Mathematician | Contribution |
|------|--------------|-------------|
| 1637 | Fermat | The conjecture |
| 1640 | Fermat | Proof for $n = 4$ (infinite descent) |
| 1770 | Euler | Proof for $n = 3$ |
| 1955 | Taniyama, Shimura | TSC: elliptic curves ↔ modular forms |
| 1980 | Langlands, Tunnell | Modularity of solvable representations |
| 1985 | Frey | FLT solution → "impossible" elliptic curve |
| 1986 | Ribet | Level-lowering: TSC ⟹ FLT |
| 1989 | Mazur | Universal deformation rings |
| 1995 | Wiles | $R = T$ for semistable curves |
| 1995 | Taylor–Wiles | Patching argument (closing the gap) |

### The logical structure

```
FLT solution (hypothetical)
  ↓  [Frey 1985]
Frey curve E (semistable, extreme discriminant)
  ↓  [Wiles 1995: 3-5 switch + R=T + Taylor–Wiles]
E is modular
  ↓  [Ribet 1986: level-lowering]
ρ̄(E,p) comes from newform of level 2
  ↓  [S₂(Γ₀(2)) = 0]
Contradiction → FLT solution does not exist   □
```

### What makes the proof so remarkable

1. **Indirectness**: FLT is not proved directly but by contradiction – via the detour of elliptic curves, modular forms, and Galois representations.
2. **Unification**: The proof unifies number theory, algebraic geometry, complex analysis, and representation theory.
3. **Depth**: The methods (deformation theory, patching) are not specific to FLT but tools of general significance.
4. **Humanity**: The story of Wiles' seven-year secret project, the gap, and its closure is unique in the history of mathematics.

---

## Outlook

The next and final article looks beyond Wiles' proof:

| Article | Topic |
|---------|-------|
| [08 – What Came After](../08-was-danach-kam/article_en.md) | BCDT, Serre's conjecture, the Langlands programme |

---

## Sources

- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §5
- **Robert Langlands**: *Base change for GL(2)*, Annals of Mathematics Studies 96 (1980)
- **Jerrold Tunnell**: *Artin's conjecture for representations of octahedral type*, Bulletin of the AMS 5 (1981)
- **Barry Mazur**: *Rational isogenies of prime degree*, Inventiones Mathematicae 44 (1978)
- **Gary Cornell, Joseph Silverman, Glenn Stevens** (eds.): *Modular Forms and Fermat's Last Theorem*, Springer (1997), Chapters XV–XVI
