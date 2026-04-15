# fermatically – Understanding Great Proofs

> *From elementary school mathematics to the great proofs of mathematics.*

!!! note "Notice"
    The articles on this platform are created with the assistance of **Artificial Intelligence** and editorially reviewed.

---

## What Is This About?

This platform explores mathematics step by step – from the Pythagorean theorem to the proof of **Fermat's Last Theorem** by Andrew Wiles (1995).

The goal is to make higher mathematics accessible without oversimplifying it. Each topic builds on the previous one: the starting point is school mathematics, the endpoint is the core results of modern number theory.

## Article Overview

### 🔢 Foundations – Elementary Number Theory

Starting point of the series: What does Fermat's Last Theorem state? Why did it resist every proof attempt for 350 years? Which special cases were proven early on?

- [What Is Fermat's Last Theorem?](grundlagen/elementare-zahlentheorie/01-was-ist-flt.md) – History, Fermat, 350 years of searching
- [The Proof for \(n=4\)](grundlagen/elementare-zahlentheorie/02-beweis-n4.md) – Fermat's own proof (Infinite Descent)
- [Primes and Why They Suffice](grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md) – Reduction to prime exponents
- [The Proof for \(n=3\)](grundlagen/elementare-zahlentheorie/04-beweis-n3.md) – Euler, Gauss, algebraic numbers

### 🔧 Tools – The Language of Modern Mathematics

Before the proof come the tools. Each of these topics is self-contained and is referenced in multiple proof articles.

- [Groups](werkzeuge/gruppen.md) – Symmetry as the language of mathematics
- [Rings and Fields](werkzeuge/ringe-koerper.md) – The world beyond the rational numbers
- [Galois Theory](werkzeuge/galois-theorie.md) – Why equations have no solution formulas
- [p-adic Numbers](werkzeuge/p-adische-zahlen.md) – A different way of looking at numbers
- [Elliptic Curves](werkzeuge/elliptische-kurven.md) – From Diophantus to cryptography
- [Modular Forms](werkzeuge/modulformen.md) – Symmetric functions of the upper half-plane

### 🏔️ The Proof – Fermat's Last Theorem (Wiles, 1995)

From the Taniyama-Shimura Conjecture through Galois representations to the \(R = T\) theorem.

- [The Taniyama-Shimura Conjecture](fermat-wiles/01-taniyama-shimura.md) – Every elliptic curve is modular
- [Frey's Idea and Ribet's Theorem](fermat-wiles/02-frey-ribet.md) – TSC ⟹ FLT
- [Galois Representations](fermat-wiles/03-galois-darstellungen.md) – Elliptic curves as matrices
- [Deformation Theory](fermat-wiles/04-deformationstheorie.md) – How to deform representations
- [\(R = T\) – The Heart of the Proof](fermat-wiles/05-r-gleich-t.md) – Wiles' central theorem
- [The Taylor-Wiles Trick](fermat-wiles/06-taylor-wiles-trick.md) – The minimal case
- [The 3-5 Switch and the Conclusion](fermat-wiles/07-3-5-switch.md) – The finale
- [What Came After](fermat-wiles/08-was-danach-kam.md) – Full TSC, Langlands program

---

!!! info "Status"
    This platform is under construction. Articles are being published gradually.

!!! note "AI-Generated Content"
    The content on this platform is created with the assistance of Artificial Intelligence (AI). All articles are carefully reviewed but may contain errors. We welcome feedback on questions or corrections.

## Fermat's Last Theorem

**Fermat's Last Theorem** states:

\[
x^n + y^n = z^n
\]

has **no** solution in positive integers \(x, y, z\) for \(n \geq 3\).

Pierre de Fermat noted in 1637 in the margin of his copy of Diophantus' *Arithmetica* that he had found a "truly marvelous proof" that the margin was too small to contain. 358 years later, Andrew Wiles' proof appeared in the *Annals of Mathematics* – spanning 109 pages, using methods from algebraic geometry and number theory that did not exist in Fermat's time.
