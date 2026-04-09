---
title: "Primfaktorzerlegung"
description: "Fundamentalsatz der Arithmetik, Existenz und Eindeutigkeit der Zerlegung, Versagen in erweiterten Ringen"
lang: de
type: vorwissen
---

# Primfaktorzerlegung

## Primzahlen

Eine natürliche Zahl $p > 1$ heißt **Primzahl**, wenn sie nur durch $1$ und sich selbst teilbar ist. Die ersten Primzahlen sind:

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \ldots
$$

Jede natürliche Zahl $n > 1$, die keine Primzahl ist, heißt **zusammengesetzt** und besitzt mindestens einen Teiler $d$ mit $1 < d < n$.

## Fundamentalsatz der Arithmetik

Jede natürliche Zahl $n > 1$ lässt sich als Produkt von Primzahlen schreiben, und diese Zerlegung ist **bis auf die Reihenfolge der Faktoren eindeutig**:

$$
n = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}
$$

Dabei sind $p_1 < p_2 < \cdots < p_k$ Primzahlen und $e_1, e_2, \ldots, e_k \geq 1$ die zugehörigen Exponenten.

> „The unique factorization of integers into primes is the foundation on which all of number theory rests."
> — Kenneth Ireland, Michael Rosen, *A Classical Introduction to Modern Number Theory*, Springer, 1990.

**Beispiel.**
$$
360 = 2^3 \cdot 3^2 \cdot 5
$$

Die Zerlegung $360 = 8 \cdot 45 = 8 \cdot 9 \cdot 5$ führt auf dieselben Primfaktoren.

### Existenz

Die Existenz folgt durch vollständige Induktion: Ist $n$ eine Primzahl, so ist $n$ selbst die Zerlegung. Ist $n$ zusammengesetzt, so existiert ein Teiler $1 < d < n$ mit $n = d \cdot (n/d)$. Beide Faktoren sind kleiner als $n$ und besitzen nach Induktionsvoraussetzung eine Primfaktorzerlegung.

### Eindeutigkeit

Die Eindeutigkeit beruht auf dem **Lemma von Euklid**: Teilt eine Primzahl $p$ ein Produkt $a \cdot b$, so teilt $p$ mindestens einen der Faktoren:

$$
p \mid ab \implies p \mid a \text{ oder } p \mid b
$$

Dieses Lemma folgt aus dem Lemma von Bézout (siehe: Teilbarkeit und ggT).

## Anwendungen

### ggT und kgV über Primfaktorzerlegung

Mit den Zerlegungen $a = \prod p_i^{\alpha_i}$ und $b = \prod p_i^{\beta_i}$ gilt:

$$
\gcd(a, b) = \prod p_i^{\min(\alpha_i, \beta_i)}, \quad \operatorname{lcm}(a, b) = \prod p_i^{\max(\alpha_i, \beta_i)}
$$

**Beispiel.** $a = 2^3 \cdot 3 \cdot 5^2 = 600$ und $b = 2^2 \cdot 3^2 \cdot 7 = 252$:

$$
\gcd(600, 252) = 2^2 \cdot 3 = 12, \quad \operatorname{lcm}(600, 252) = 2^3 \cdot 3^2 \cdot 5^2 \cdot 7 = 12600
$$

### Anzahl der Teiler

Die Anzahl der positiven Teiler von $n = p_1^{e_1} \cdots p_k^{e_k}$ beträgt:

$$
\tau(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)
$$

**Beispiel.** $360 = 2^3 \cdot 3^2 \cdot 5$ hat $\tau(360) = 4 \cdot 3 \cdot 2 = 24$ Teiler.

## Versagen der eindeutigen Zerlegung in erweiterten Ringen

Der Fundamentalsatz gilt in $\mathbb{Z}$, aber **nicht in allen Zahlringen**. Das klassische Gegenbeispiel:

In $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ gilt:

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

Beide Zerlegungen bestehen aus irreduziblen Elementen, die sich nicht ineinander überführen lassen. Die eindeutige Primfaktorzerlegung versagt.

Dieses Problem motivierte Kummers Einführung der **idealen Zahlen** (heute: Ideale in Dedekind-Ringen), die die eindeutige Zerlegung auf der Ebene der Ideale wiederherstellen. Kummers Arbeit war ein entscheidender Schritt in der Geschichte von Fermats Letztem Satz.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Primzahl | $p > 1$ mit genau zwei Teilern: $1$ und $p$ |
| Fundamentalsatz | Jede $n > 1$ ist eindeutiges Produkt von Primzahlen |
| Lemma von Euklid | $p \mid ab \implies p \mid a$ oder $p \mid b$ |
| $\gcd$ via Zerlegung | $\prod p_i^{\min(\alpha_i, \beta_i)}$ |
| $\tau(n)$ | Teileranzahl: $\prod (e_i + 1)$ |

## Quellen

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6. Auflage, 2008. Kapitel 2.
- Ireland, Kenneth; Rosen, Michael: *A Classical Introduction to Modern Number Theory.* Springer, 2. Auflage, 1990. Kapitel 1.
