---
title: "Pythagoras und pythagoräische Tripel"
description: "Satz des Pythagoras, ganzzahlige Lösungen und Bezug zu Fermats Gleichung"
lang: de
type: vorwissen
---

# Pythagoras und pythagoräische Tripel

## Der Satz des Pythagoras

In einem rechtwinkligen Dreieck mit Katheten $a$, $b$ und Hypotenuse $c$ gilt:

$$
a^2 + b^2 = c^2
$$

Die Umkehrung gilt ebenfalls: Erfüllen die Seitenlängen eines Dreiecks diese Gleichung, so ist das Dreieck rechtwinklig.

**Beispiel.** Ein Dreieck mit Seiten $3, 4, 5$: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$. ✓

## Pythagoräische Tripel

Ein **pythagoräisches Tripel** ist ein Tupel $(a, b, c)$ natürlicher Zahlen mit $a^2 + b^2 = c^2$.

**Beispiele:**

| $a$ | $b$ | $c$ | Prüfung |
|-----|-----|-----|---------|
| 3 | 4 | 5 | $9 + 16 = 25$ |
| 5 | 12 | 13 | $25 + 144 = 169$ |
| 8 | 15 | 17 | $64 + 225 = 289$ |

Ein Tripel heißt **primitiv**, wenn $\gcd(a, b, c) = 1$.

### Erzeugung aller primitiven Tripel

Alle primitiven pythagoräischen Tripel haben die Form:

$$
a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2
$$

mit $m > n > 0$, $\gcd(m, n) = 1$ und $m - n$ ungerade.

**Beispiel.** $m = 2, n = 1$: $a = 4 - 1 = 3$, $b = 4$, $c = 4 + 1 = 5$. → $(3, 4, 5)$.

## Bezug zu Fermats Gleichung

Die Gleichung $a^2 + b^2 = c^2$ hat unendlich viele ganzzahlige Lösungen.

Fermats letzter Satz besagt: Für $n \geq 3$ hat die Gleichung

$$
a^n + b^n = c^n
$$

**keine** Lösung mit $a, b, c \in \mathbb{Z}^+$. Der Fall $n = 2$ (Pythagoras) ist also der letzte Exponent, für den ganzzahlige Lösungen existieren.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Satz des Pythagoras | $a^2 + b^2 = c^2$ im rechtwinkligen Dreieck |
| Pythagoräisches Tripel | $(a,b,c) \in \mathbb{N}^3$ mit $a^2 + b^2 = c^2$ |
| Primitives Tripel | $\gcd(a,b,c) = 1$ |
| Parametrisierung | $a = m^2-n^2,\; b = 2mn,\; c = m^2+n^2$ |

## Quellen

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6. Auflage, 2008. Kapitel 13.
- Edwards, Harold M.: *Fermat's Last Theorem.* Springer, 1977. Kapitel 1.
