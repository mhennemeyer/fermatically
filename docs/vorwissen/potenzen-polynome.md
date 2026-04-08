---
title: "Potenzen und Polynome"
description: "Potenzgesetze, Polynomausdruck und Grad eines Polynoms"
lang: de
type: vorwissen
---

# Potenzen und Polynome

## Potenzen

Für $a \in \mathbb{R}$ und $n \in \mathbb{N}$ ist die **Potenz** $a^n$ definiert als:

$$
a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ Faktoren}}, \quad a^0 = 1 \;(a \neq 0)
$$

Dabei heißt $a$ die **Basis** und $n$ der **Exponent**.

### Potenzgesetze

Für $a, b \neq 0$ und $m, n \in \mathbb{Z}$:

| Gesetz | Formel |
|--------|--------|
| Gleiche Basis, Multiplikation | $a^m \cdot a^n = a^{m+n}$ |
| Gleiche Basis, Division | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potenz einer Potenz | $(a^m)^n = a^{m \cdot n}$ |
| Produkt | $(a \cdot b)^n = a^n \cdot b^n$ |
| Quotient | $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$ |
| Negativer Exponent | $a^{-n} = \frac{1}{a^n}$ |

**Beispiel.** $2^3 \cdot 2^4 = 2^7 = 128$.

**Beispiel.** $(3^2)^3 = 3^6 = 729$.

## Polynome

Ein **Polynom** in der Variablen $x$ ist ein Ausdruck der Form:

$$
p(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0 = \sum_{k=0}^{n} a_k x^k
$$

Die Zahlen $a_0, a_1, \ldots, a_n$ heißen **Koeffizienten**. Der Koeffizient $a_n$ ($a_n \neq 0$) heißt **Leitkoeffizient**.

### Grad

Der **Grad** eines Polynoms ist der höchste Exponent mit nicht-verschwindendem Koeffizienten:

$$
\deg(p) = n \quad \text{falls } a_n \neq 0
$$

**Beispiele.**

- $p(x) = 3x^4 - 2x + 7$ hat Grad $4$.
- $p(x) = 5$ (konstant, $\neq 0$) hat Grad $0$.
- Das Nullpolynom $p(x) = 0$ hat keinen definierten Grad (Konvention: $\deg(0) = -\infty$).

### Rechenregeln für den Grad

$$
\deg(p \cdot q) = \deg(p) + \deg(q)
$$

$$
\deg(p + q) \leq \max(\deg(p), \deg(q))
$$

### Nullstellen

Eine **Nullstelle** von $p(x)$ ist ein Wert $x_0$ mit $p(x_0) = 0$. Ein Polynom vom Grad $n$ hat höchstens $n$ Nullstellen (über $\mathbb{R}$, mit Vielfachheit gezählt über $\mathbb{C}$ genau $n$).

**Beispiel.** $p(x) = x^2 - 4 = (x-2)(x+2)$ hat Nullstellen $x = 2$ und $x = -2$.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| $a^n$ | $a$ multipliziert mit sich selbst, $n$-mal |
| Polynom | $\sum_{k=0}^n a_k x^k$ |
| Grad | Höchster Exponent mit $a_k \neq 0$ |
| Nullstelle | $x_0$ mit $p(x_0) = 0$ |

## Quellen

- Lang, Serge: *Algebra.* Springer, 3. Auflage, 2002. Kapitel 4.
