---
title: "Binomische Formeln und Faktorisierung"
description: "Die drei binomischen Formeln und ihre Anwendung beim Umformen"
lang: de
type: vorwissen
---

# Binomische Formeln und Faktorisierung

## Die drei binomischen Formeln

### Erste binomische Formel

$$
(a + b)^2 = a^2 + 2ab + b^2
$$

**Beispiel.** $(x + 3)^2 = x^2 + 6x + 9$.

### Zweite binomische Formel

$$
(a - b)^2 = a^2 - 2ab + b^2
$$

**Beispiel.** $(x - 5)^2 = x^2 - 10x + 25$.

### Dritte binomische Formel

$$
(a + b)(a - b) = a^2 - b^2
$$

**Beispiel.** $(x + 4)(x - 4) = x^2 - 16$.

## Faktorisierung

Die binomischen Formeln lassen sich auch in umgekehrter Richtung lesen – zum **Faktorisieren** (Zerlegen in Faktoren):

| Ausdruck | Faktorisierte Form |
|----------|-------------------|
| $a^2 + 2ab + b^2$ | $(a + b)^2$ |
| $a^2 - 2ab + b^2$ | $(a - b)^2$ |
| $a^2 - b^2$ | $(a + b)(a - b)$ |

**Beispiel.** $x^2 - 9 = x^2 - 3^2 = (x + 3)(x - 3)$.

**Beispiel.** $4x^2 - 12x + 9 = (2x)^2 - 2 \cdot 2x \cdot 3 + 3^2 = (2x - 3)^2$.

## Anwendung: Quadratische Gleichungen

Die dritte binomische Formel löst Gleichungen der Form $a^2 = b^2$:

$$
a^2 = b^2 \iff a^2 - b^2 = 0 \iff (a+b)(a-b) = 0 \iff a = b \text{ oder } a = -b
$$

## Höhere Potenzen (Ausblick)

Für $(a + b)^n$ mit $n > 2$ gilt der **binomische Satz**:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

mit dem **Binomialkoeffizienten** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.

**Beispiel.** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$.

---

## Zusammenfassung

| Formel | Gleichung |
|--------|-----------|
| 1. binomische | $(a+b)^2 = a^2 + 2ab + b^2$ |
| 2. binomische | $(a-b)^2 = a^2 - 2ab + b^2$ |
| 3. binomische | $(a+b)(a-b) = a^2 - b^2$ |
| Binomischer Satz | $(a+b)^n = \sum \binom{n}{k} a^{n-k} b^k$ |

## Quellen

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996.
