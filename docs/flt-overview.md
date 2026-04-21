# Fermat's Last Theorem – The Road to the Proof

!!! abstract "Overview"
    From a 17th-century lawyer's conjecture to Andrew Wiles' 109-page proof (1995). This article series traces the entire journey – from elementary number theory through the language of modern mathematics to the famous \(R = T\) theorem.

## The Conjecture

**Fermat's Last Theorem** states:

\[
x^n + y^n = z^n
\]

has **no** solution in positive integers \(x, y, z\) for \(n \geq 3\).

Pierre de Fermat noted in 1637 in the margin of his copy of Diophantus' *Arithmetica* that he had found a "truly marvelous proof" that the margin was too small to contain. 358 years later, Andrew Wiles' proof appeared in the *Annals of Mathematics*.

---

## The Journey in Three Acts

### 🔢 Act 1: Elementary Number Theory

The starting point: What does the conjecture state, and which special cases could be proven early on?

| # | Article | Topic |
|---|---------|-------|
| 1 | [What Is Fermat's Last Theorem?](grundlagen/elementare-zahlentheorie/01-was-ist-flt.md) | History, Fermat, 350 years of searching |
| 2 | [The Proof for \(n=4\)](grundlagen/elementare-zahlentheorie/02-beweis-n4.md) | Fermat's own proof (Infinite Descent) |
| 3 | [Primes and Why They Suffice](grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md) | Reduction to prime exponents |
| 4 | [The Proof for \(n=3\)](grundlagen/elementare-zahlentheorie/04-beweis-n3.md) | Euler, Gauss, algebraic numbers |

### 🔧 Act 2: Tools of Modern Mathematics

Before the proof come the tools. Each of these topics is self-contained and is referenced in the proof articles.

→ [Tools Overview](werkzeuge/index.md)

- [Groups – Symmetry as Language](werkzeuge/gruppen.md)
- [Rings and Fields](werkzeuge/ringe-koerper.md)
- [Galois Theory](werkzeuge/galois-theorie.md)
- [p-adic Numbers](werkzeuge/p-adische-zahlen.md)
- [Elliptic Curves](werkzeuge/elliptische-kurven.md)
- [Modular Forms](werkzeuge/modulformen.md)

### 🏔️ Act 3: The Proof

From the Taniyama-Shimura Conjecture through Galois representations to the \(R = T\) theorem.

| # | Article | Topic |
|---|---------|-------|
| 1 | [The Taniyama-Shimura Conjecture](fermat-wiles/01-taniyama-shimura.md) | Every elliptic curve is modular |
| 2 | [Frey's Idea and Ribet's Theorem](fermat-wiles/02-frey-ribet.md) | TSC ⟹ FLT |
| 3 | [Galois Representations](fermat-wiles/03-galois-darstellungen.md) | Elliptic curves as matrices |
| 4 | [Deformation Theory](fermat-wiles/04-deformationstheorie.md) | How to deform representations |
| 5 | [\(R = T\) – The Heart of the Proof](fermat-wiles/05-r-gleich-t.md) | Wiles' central theorem |
| 6 | [The Taylor-Wiles Trick](fermat-wiles/06-taylor-wiles-trick.md) | The minimal case |
| 7 | [The 3-5 Switch and the Conclusion](fermat-wiles/07-3-5-switch.md) | The finale |
| 8 | [What Came After](fermat-wiles/08-was-danach-kam.md) | Full TSC, Langlands program |

---

## Recommended Order

The articles build on each other. The recommended path:

1. **Elementary Number Theory** (Act 1) – as an introduction
2. **Tools** (Act 2) – as needed, or when a proof article refers to them
3. **The Proof** (Act 3) – strictly in order

!!! tip "Prerequisites"
    For mathematical foundations (logic, sets, arithmetic, algebra) there is the [Prerequisites](vorwissen/index.md) section. Those articles are linked from the storyline when needed.
