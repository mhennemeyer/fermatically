---
title: "What Came After"
slug: fermat-wiles/08-was-danach-kam
series: fermat-wiles
part: 8
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - bcdt
  - langlands-programme
  - outlook
requires:
  - fermat-wiles/07-3-5-switch
---
# What Came After

!!! abstract "Summary"
    Wiles' proof was not the end, but a beginning. Within six years,
    Breuil, Conrad, Diamond, and Taylor generalised the result to all
    elliptic curves. Serre's conjecture was proved in 2009. The Langlands
    programme – the natural generalisation of the Taniyama–Shimura
    conjecture – remains the grand vision of modern number theory.

## Prerequisites

- [The 3-5 Switch and the Conclusion](../07-3-5-switch/article_en.md) – the complete proof of FLT

---

## 1. From Semistable to General

### The open question

Wiles proved in 1995 the modularity of **semistable** elliptic curves over $\mathbb{Q}$. The full Taniyama–Shimura conjecture – modularity of **all** elliptic curves – initially remained open.

### The path to generalisation

After Wiles' breakthrough, several mathematicians turned to the generalisation. The methods were essentially the same (deformation theory, Taylor–Wiles patching), but the technical difficulties for non-semistable curves – particularly curves with **additive reduction** – required new ideas.

Important intermediate steps:

- **Fred Diamond (1996)**: Extended the proof to a broader range of deformation conditions and substantially simplified the Taylor–Wiles construction.
- **Conrad, Diamond, Taylor (1999)**: Treated many of the remaining cases, particularly curves with additive reduction at small primes.

### BCDT (2001)

!!! note "Theorem (Breuil–Conrad–Diamond–Taylor, 2001)"
    **Every** elliptic curve over $\mathbb{Q}$ is modular.

Christophe **Breuil** provided the decisive final building block: the treatment of cases with additive reduction at $p = 3$. His tool was the theory of **Breuil modules** (finite flat group schemes), which allowed finer control of the local deformation conditions.

The proof appeared in the *Journal of the AMS* and closed the chapter that Taniyama had opened in 1955.

### The full modularity conjecture

With BCDT, the Taniyama–Shimura conjecture became the **Modularity Theorem**:

$$
\boxed{\text{Every elliptic curve } E/\mathbb{Q} \text{ is modular.}}
$$

This has far-reaching consequences: for **every** elliptic curve over $\mathbb{Q}$, the analytic continuation and functional equation of the $L$-series hold, and the Birch–Swinnerton-Dyer conjecture becomes accessible.

---

## 2. Serre's Conjecture

### The conjecture

Jean-Pierre Serre formulated in 1987 a far more general conjecture than the $\varepsilon$-conjecture that Ribet had proved for the Frey curve:

!!! note "Serre's Conjecture (1987)"
    Every continuous, odd, irreducible representation
    $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p)$
    is modular – and Serre specifies explicitly the minimal weight $k(\bar{\rho})$
    and the minimal level $N(\bar{\rho})$ of the associated modular form.

This conjecture generalises the Taniyama–Shimura conjecture drastically: not only representations coming from elliptic curves, but **all** 2-dimensional representations over finite fields should be modular.

### The proof (2009)

**Chandrashekhar Khare** and **Jean-Pierre Wintenberger** proved Serre's conjecture in a series of papers (2006–2009). Their proof uses:

- Taylor–Wiles patching (in generalised form)
- Kisin's results on deformation rings
- Potential modularity results of Taylor
- An ingenious inductive strategy over weight and level

Khare received the 2011 Cole Prize of the AMS for this result.

### Consequences

Serre's conjecture has remarkable corollaries:

1. **Fontaine–Mazur conjecture** (special case): Every geometric $p$-adic representation that is irreducible modulo $p$ comes from a modular form.
2. **Artin's conjecture** (for 2-dimensional representations): The $L$-series of every irreducible 2-dimensional Artin representation has an analytic continuation.

---

## 3. The Langlands Programme

### The grand vision

The **Langlands programme**, formulated by Robert Langlands from 1967, is the natural generalisation of the ideas behind the Taniyama–Shimura conjecture. It postulates a systematic correspondence between:

- **Galois representations** (number theory / algebraic geometry)
- **Automorphic forms** (analysis / representation theory)

The TSC and the Modularity Theorem are a special case: 2-dimensional representations over $\mathbb{Q}$ ↔ modular forms of weight 2.

### The Langlands correspondence

In full generality, the Langlands programme postulates for every number field $F$ and every reductive group $G$:

$$
\left\{\begin{array}{c} n\text{-dimensional} \\ \text{Galois representations} \\ \text{of } G_F \end{array}\right\} \longleftrightarrow \left\{\begin{array}{c} \text{Automorphic} \\ \text{representations} \\ \text{of } G(\mathbb{A}_F) \end{array}\right\}
$$

where $\mathbb{A}_F$ is the adèle ring of $F$.

### Progress after Wiles

Wiles' methods and the Taylor–Wiles trick triggered a wave of results:

| Year | Result | Authors |
|------|--------|---------|
| 2001 | Modularity of all ell. curves / $\mathbb{Q}$ | BCDT |
| 2006 | Sato–Tate conjecture (many cases) | Taylor, Clozel, Harris, Shepherd-Barron |
| 2009 | Serre's conjecture | Khare–Wintenberger |
| 2013 | Potential automorphy in higher dimensions | Barnet-Lamb, Geraghty, Harris, Taylor |
| 2018 | Symmetric powers (all) | Newton–Thorne |
| 2022 | Modularity of abelian surfaces | Boxer–Calegari–Gee–Pilloni |

### What remains open

Despite enormous progress, the Langlands programme remains largely open:

- **Functoriality**: General Langlands functoriality is unproved.
- **Beyond totally real fields**: For general number fields, fundamental tools are missing.
- **Geometric Langlands programme**: The analogy over function fields (curves over finite fields) is further advanced (Fargues–Scholze, 2021).
- **$p$-adic Langlands programme**: A $p$-adic variant, initiated by Breuil and Colmez.

---

## 4. Formal Verification

### The question

Wiles' proof encompasses over 100 pages of dense mathematics and relies on hundreds of pages of prior work. Can such a proof be **formally verified** – that is, formalised in a machine-checkable form in a proof assistant (Lean, Coq, Isabelle)?

### The current state

A complete formalisation of Wiles' proof does not yet exist (as of 2026). The obstacles are considerable:

1. **Scope**: The proof presupposes algebraic geometry, representation theory, $p$-adic Hodge theory, and the theory of modular forms – areas that are not fully formalised in any proof assistant.
2. **Technical depth**: Even individual components (e.g., the theory of Hecke algebras or Mazur's deformation theory) require years of formalisation.
3. **Community capacity**: The number of mathematicians who master both the proof and formal verification is very small.

### Related successes

Nevertheless, there are impressive advances in formal verification of major proofs:

- **Four Colour Theorem** (Gonthier, 2005): Fully formalised in Coq.
- **Kepler Conjecture** (Hales/Flyspeck, 2014): Fully formalised in HOL Light/Isabelle.
- **Liquid Vector Space Theory** (Scholze, 2022): Central lemma formalised in Lean – a test for advanced mathematics.
- **FLT for regular primes** (Lean/Mathlib, 2024): Kummer's proof for regular primes was formalised – a first step towards FLT.

A complete formalisation of Wiles' proof would be a milestone for formal mathematics – but realistically it is still years, if not decades, away.

---

## 5. FLT and the Classroom

### The gap

Fermat's Last Theorem has a unique property: the **statement** is comprehensible to any school student ($x^n + y^n = z^n$ has no integer solution for $n \geq 3$), but the **proof** uses mathematics that is scarcely covered even in a master's programme.

### What can be understood

Without the proof details, one can still convey the **structure** of the proof:

1. The basic idea of proof by contradiction (Frey curve)
2. The role of modularity as a bridge between different mathematical worlds
3. The historical development – from Fermat through Euler and Kummer to Wiles
4. The human story – seven years of secret work, the gap, the rescue

This article series attempts precisely that: to present the proof at a level that requires mathematical maturity but not research expertise.

---

## 6. Open Questions

### Around FLT

- **ABC conjecture**: Mochizuki's claimed proof (2012) remains controversial. If confirmed, it would yield a completely different proof of FLT (for sufficiently large $n$).
- **Effective bounds**: Can one make the constants in Faltings' theorem or related results explicit?
- **Generalisations**: For which other Diophantine equations does the modular method work? (Example: Fermat's equation over number fields.)

### In number theory at large

- **Birch–Swinnerton-Dyer conjecture**: One of the Clay Millennium Problems. The Modularity Theorem makes the analytic side accessible, but the proof is still missing.
- **Riemann Hypothesis**: The deepest open problem in mathematics – connected to $L$-series, but with entirely different methods.
- **Langlands programme**: The grand unification project of number theory – wide open in its full generality.

---

## 7. Epilogue

### A proof and its consequences

Andrew Wiles' proof of Fermat's Last Theorem was more than the solution of a 358-year-old problem. It demonstrated the **unity of mathematics**: a question from elementary number theory was answered by tools from algebraic geometry, complex analysis, and representation theory.

The methods that Wiles and Taylor developed – in particular Taylor–Wiles patching – are now standard tools of algebraic number theory. The vision that Taniyama hinted at in 1955 – a deep connection between seemingly separate mathematical worlds – has proved prophetic and forms the core of the Langlands programme.

### Fermat's marginal note, revisited

Fermat wrote in 1637:

> *"I have discovered a truly marvellous proof of this, which this margin is too narrow to contain."*

358 years later we know: the margin probably did not **need** to contain Fermat's proof – because Fermat could not have known the tools required for the proof. Modular forms were developed only in the 19th century, Galois representations in the 20th, and deformation theory not until 1989.

Whether Fermat actually had a proof (possibly only for $n = 4$, which he did prove) will remain a mystery forever. What remains is Wiles' proof – and the insight that the deepest questions of mathematics often find the most surprising answers.

---

## Sources

- **Christophe Breuil, Brian Conrad, Fred Diamond, Richard Taylor**: *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises*, Journal of the AMS 14 (2001), 843–939
- **Chandrashekhar Khare, Jean-Pierre Wintenberger**: *Serre's modularity conjecture (I) and (II)*, Inventiones Mathematicae 178 (2009)
- **Robert Langlands**: *Problems in the theory of automorphic forms*, Lectures in Modern Analysis and Applications III, Springer (1970)
- **Peter Scholze, Dustin Clausen**: *Condensed Mathematics and Analytic Geometry*, lecture notes (2019–2022)
- **Kevin Buzzard**: *The Xena Project*, formalisation of mathematics in Lean
- **Simon Singh**: *Fermat's Last Theorem*, Fourth Estate (1997)
- **Andrew Wiles**: Abel Prize Lecture, Oslo (2016) – retrospective on the proof and its consequences
