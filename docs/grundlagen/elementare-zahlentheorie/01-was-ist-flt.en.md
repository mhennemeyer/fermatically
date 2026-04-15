---
title: "What Is Fermat's Last Theorem?"
slug: elementare-zahlentheorie/01-was-ist-flt
series: elementare-zahlentheorie
part: 1
date: 2026-03-31
status: draft
lang: en
category: zahlentheorie
tags:
  - fermat
  - number-theory
  - history
requires: []
---

# What Is Fermat's Last Theorem?

!!! abstract "Summary"
    The story of a conjecture that remained unproven for 358 years –
    from Fermat's marginal note to Andrew Wiles' proof in 1995.

## Prerequisites

None – this article is the entry point to the series.

---

## 1. Fermat's Marginal Note (1637)

In 1637, Pierre de Fermat wrote in the margin of his copy of Diophantus' *Arithmetica* a statement that would occupy mathematics for over three centuries:

> *"Cubum autem in duos cubos, aut quadratoquadratum in duos quadratoquadratos, et generaliter nullam in infinitum ultra quadratum potestatem in duos eiusdem nominis fas est dividere. Cuius rei demonstrationem mirabilem sane detexi. Hanc marginis exiguitas non caperet."*

In English:

> *"It is impossible to separate a cube into two cubes, or a fourth power into two fourth powers, or in general, any power higher than the second, into two like powers. I have discovered a truly marvellous proof of this, which this margin is too narrow to contain."*

This marginal note was only published after Fermat's death (1665) by his son Clément-Samuel. It established one of the most famous unsolved problems in mathematics – and a 358-year hunt for a proof.

Fermat himself was not a professional mathematician. He was a jurist at the Parliament of Toulouse and pursued mathematics as a passion. Yet his contributions to number theory were so profound that he is often called the "Prince of Amateurs." He stated many claims without proof – nearly all turned out to be correct. Only this one, the most famous of all, resisted every attempt at proof.

## 2. The Formal Statement

What Fermat claimed can be stated precisely as follows:

$$
x^n + y^n = z^n \quad \text{has no solution for } n \geq 3 \text{ with } x, y, z \in \mathbb{Z}^+
$$

That is: there are no three positive integers $x$, $y$, and $z$ that satisfy this equation for any integer exponent $n \geq 3$.

For $n = 2$, by contrast, we know infinitely many solutions – the **Pythagorean triples**:

$$
3^2 + 4^2 = 5^2, \quad 5^2 + 12^2 = 13^2, \quad 8^2 + 15^2 = 17^2, \quad \ldots
$$

The Pythagorean theorem even guarantees that infinitely many such triples exist, and they can be completely parametrised. But as soon as the exponent rises from $2$ to $3$, all solutions seem to vanish – as if an invisible barrier had been crossed.

## 3. Why Is This Hard?

At first glance, the claim appears harmless. One might think a clever algebraic trick would suffice. But the devil is in the details.

**The problem of non-existence.** Finding a proof that *something exists* is often easier than showing that *something does not exist*. One would need to show that among infinitely many combinations of $x$, $y$, $z$, and $n$, not a single one satisfies the equation. A single counterexample would have sufficed to disprove the theorem – but nobody found one.

**Computer searches.** In the 20th century, systematic searches were conducted. Up into the trillions – no solution. That is strong evidence, but not a proof. In mathematics, there are conjectures that fail only at astronomically large numbers.

**The asymmetry with the Pythagorean theorem.** For $n = 2$, the equation has a rich geometric structure: every solution corresponds to a right triangle with integer sides. For $n \geq 3$, a comparable geometric interpretation is absent – and with it, the tools.

**Fermat's "marvellous proof."** Almost all historians of mathematics agree: Fermat could not have possessed a correct proof. Wiles' actual proof uses concepts – elliptic curves, modular forms, Galois representations – that were not developed until the 19th and 20th centuries. Fermat probably had an idea that worked for $n = 4$ (we know that proof), but was flawed for general $n$.

## 4. The History of Partial Proofs

The history of Fermat's Last Theorem is also a history of the development of mathematics. Every partial proof required new methods and drove entire fields of research forward.

### Fermat himself: $n = 4$ (ca. 1640)

Fermat proved the only case for which we have a complete proof from him. He used the method of **infinite descent** (*descente infinie*): Suppose a solution existed. Then one could construct from it a *smaller* solution, and from that an even smaller one – ad infinitum. Since positive integers cannot become infinitely small, the assumption is false. We treat this proof in detail in the [next article](02-beweis-n4.md).

### Leonhard Euler: $n = 3$ (1770)

Euler extended Fermat's method to the case $n = 3$. But to do so, he had to take a crucial step: he left the ordinary integers $\mathbb{Z}$ and computed instead with the **Eisenstein integers** $\mathbb{Z}[\omega]$, where $\omega = e^{2\pi i/3}$ is a primitive cube root of unity. In this extended number domain, he could factorise the equation and carry out the descent. Euler's proof did contain a gap, however: he implicitly assumed that unique prime factorisation holds in $\mathbb{Z}[\omega]$ – which happens to be true, but needs to be proved. We discuss the complete proof in [Article 4](04-beweis-n3.md).

### Sophie Germain: A New Strategy (1823)

Sophie Germain – one of the first prominent female mathematicians – developed a more general approach. She proved: if $p$ is an odd prime and $2p + 1$ is also prime (a so-called **Germain prime**), then $x^p + y^p = z^p$ has no solution in which $p$ divides none of the values $x$, $y$, $z$ (**Case 1** of FLT). This was the first partial success that applied to infinitely many exponents simultaneously.

### Ernst Kummer: Regular Primes (1847–1857)

Kummer revolutionised algebraic number theory by developing **ideal theory** – a concept that compensates for the lack of unique factorisation in general number rings. He proved FLT for all **regular primes** – primes $p$ that do not divide the class number of the $p$-th cyclotomic field. Up to $p = 100$, all primes except $37$, $59$, and $67$ are regular. Yet there are infinitely many irregular primes, and Kummer's method fails for them.

### The 20th Century: Computer Proofs and Bounds

With the advent of computers, FLT was verified for ever-larger exponents. In 1993, shortly before Wiles' breakthrough, the theorem had been proved for all $n \leq 4{,}000{,}000$. Yet these results remained piecework – they could not cover the general case.

## 5. Failed Attempts and Dead Ends

The history of FLT is also a history of errors. Hundreds of incorrect proofs were submitted – by amateurs and professionals alike.

A typical mistake: one tries to factorise the equation $x^p + y^p = z^p$ directly in a number ring $\mathbb{Z}[\zeta_p]$ (with $\zeta_p = e^{2\pi i/p}$) and assumes that the factors are coprime. For $p = 3$ this works (because $\mathbb{Z}[\omega]$ is a principal ideal domain), but for general $p$ unique factorisation does not hold. Gabriel Lamé announced a supposed proof in 1847, which failed at precisely this point – Kummer identified the error the very same day.

These failures were not useless: they drove the development of algebraic number theory, ideal theory, and ultimately modern algebraic geometry.

## 6. The Wolfskehl Prize

In 1908, the Darmstadt industrialist **Paul Wolfskehl** endowed a prize of 100,000 gold marks for the proof of Fermat's Last Theorem. According to legend, Wolfskehl, suffering from an incurable illness, had planned his suicide for midnight. While waiting, he immersed himself in Kummer's work, lost track of time – and found new will to live. In gratitude, he endowed the prize.

The Wolfskehl Prize triggered a flood of submissions. The University of Göttingen, which administered the prize, received thousands of purported proofs – most with obvious errors. Edmund Landau is said to have had form postcards printed:

> *"Dear Sir/Madam ..., Your purported proof of Fermat's Last Theorem contains an error on page ..., line ..."*

After two World Wars and inflation, the prize was worth only a fraction of its original value. When Andrew Wiles finally received it in 1997, it amounted to roughly 50,000 DM – but its symbolic value was priceless.

## 7. The Modern Turn

The breakthrough came from a completely unexpected direction. It was not number theory itself that solved the problem, but a bridge between two seemingly unrelated fields of mathematics.

### The Taniyama–Shimura Conjecture (1955)

The Japanese mathematicians **Yutaka Taniyama** and **Goro Shimura** posed a bold conjecture: every **elliptic curve** over $\mathbb{Q}$ is **modular** – that is, it can be described by a **modular form**. At first, this sounded like a purely technical result with no connection to FLT. But three decades later, it became clear that this connection was the key.

### The Frey Curve and Ribet's Proof (1985–1986)

The German mathematician **Gerhard Frey** had a spectacular idea in 1985: if FLT were *false* – if a solution $a^p + b^p = c^p$ existed – then one could construct from it an elliptic curve:

$$
y^2 = x(x - a^p)(x + b^p)
$$

This "**Frey curve**" would have such exotic properties that it could not possibly be modular. So if the Taniyama–Shimura conjecture holds (all elliptic curves are modular), then the Frey curve cannot exist – and FLT must be true.

**Kenneth Ribet** proved in 1986 that Frey's intuition was correct: the Frey curve is indeed not modular. This secured the implication:

$$
\text{Taniyama–Shimura} \implies \text{Fermat's Last Theorem}
$$

### Andrew Wiles (1993–1995)

Andrew Wiles, a British mathematician at Princeton, had dreamed since childhood of proving FLT. After Ribet's result, he worked in secret for seven years on a proof of the Taniyama–Shimura conjecture – at least for the class of **semistable** elliptic curves, which suffices for FLT.

In June 1993, Wiles announced his proof in a dramatic lecture series in Cambridge. But during peer review, a gap was found. For months, Wiles tried to close it – he nearly gave up. Then, in September 1994, together with his former student **Richard Taylor**, he found the solution: the famous **Taylor–Wiles trick**.

On 25 October 1995, the corrected proof was published in the *Annals of Mathematics*. Fermat's Last Theorem was proved – after 358 years.

## 8. Outlook: What Comes in the Next Articles?

This first article has drawn the big picture. In the following articles, we dive into the details:

| Article | Topic |
|---------|-------|
| [02 – The Proof for $n = 4$](02-beweis-n4.md) | Fermat's own proof using the method of infinite descent |
| [03 – Primes and Why They Suffice](03-primzahlen-reduktion.md) | Why it suffices to prove FLT for prime exponents |
| [04 – The Proof for $n = 3$](04-beweis-n3.md) | Euler's proof and the entry into algebraic number theory |

After the fundamentals come the **tool topics** – self-contained articles on groups, rings, Galois theory, elliptic curves, and modular forms. And finally the **proof topics**, which guide step by step through Wiles' proof.

The goal: by the end, every reader – whether student, mathematics enthusiast, or fellow researcher – should understand *why* Wiles' proof works and what ideas sustain it.

---

## Further Reading

- **Simon Singh**: *Fermat's Last Theorem* – The story of a riddle that confounded the world's greatest minds for 358 years (popular science, brilliantly told)
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003) – Textbook with mathematical details
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), 443–551
