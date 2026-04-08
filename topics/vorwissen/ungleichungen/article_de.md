---
title: "Ungleichungen"
description: "Ordnung auf den reellen Zahlen, Rechenregeln und Betrag"
lang: de
type: vorwissen
---

# Ungleichungen

## Ordnung auf ℝ

Die reellen Zahlen $\mathbb{R}$ tragen eine **totale Ordnung**: Für je zwei Zahlen $a, b \in \mathbb{R}$ gilt genau eine der Aussagen $a < b$, $a = b$ oder $a > b$.

Die Symbole im Überblick:

| Symbol | Bedeutung |
|--------|-----------|
| $a < b$ | $a$ ist echt kleiner als $b$ |
| $a \leq b$ | $a$ ist kleiner oder gleich $b$ |
| $a > b$ | $a$ ist echt größer als $b$ |
| $a \geq b$ | $a$ ist größer oder gleich $b$ |

## Rechenregeln

### Addition und Subtraktion

Die Ordnung bleibt erhalten:

$$
a < b \implies a + c < b + c \quad \text{für alle } c \in \mathbb{R}
$$

### Multiplikation mit positiver Zahl

Die Ordnung bleibt erhalten:

$$
a < b \text{ und } c > 0 \implies a \cdot c < b \cdot c
$$

### Multiplikation mit negativer Zahl

Die Ordnung **kehrt sich um**:

$$
a < b \text{ und } c < 0 \implies a \cdot c > b \cdot c
$$

**Beispiel.** $2 < 5$. Multiplikation mit $-3$: $-6 > -15$. Das Ungleichheitszeichen dreht sich.

### Kehrwert

Für $a, b > 0$:

$$
a < b \implies \frac{1}{a} > \frac{1}{b}
$$

**Beispiel.** $2 < 5 \implies \frac{1}{2} > \frac{1}{5}$.

## Beispiel: Lösung einer Ungleichung

$-3x + 6 \leq 12$

| Schritt | Ungleichung | Operation |
|---------|-------------|-----------|
| 1 | $-3x + 6 \leq 12$ | Ausgangsungleichung |
| 2 | $-3x \leq 6$ | $-6$ auf beiden Seiten |
| 3 | $x \geq -2$ | $\div (-3)$, Zeichen dreht sich |

Lösungsmenge: $[-2, \infty)$.

## Betrag

Der **Betrag** (Absolutwert) einer reellen Zahl $a$ ist definiert als:

$$
|a| = \begin{cases} a & \text{falls } a \geq 0 \\ -a & \text{falls } a < 0 \end{cases}
$$

Geometrisch: $|a|$ ist der Abstand von $a$ zum Nullpunkt auf der Zahlengeraden.

### Dreiecksungleichung

Für alle $a, b \in \mathbb{R}$:

$$
|a + b| \leq |a| + |b|
$$

**Beispiel.** $|3 + (-5)| = |-2| = 2 \leq |3| + |-5| = 3 + 5 = 8$. ✓

### Betragsungleichungen

$$
|x| < c \iff -c < x < c \quad (c > 0)
$$

$$
|x| > c \iff x < -c \text{ oder } x > c \quad (c > 0)
$$

---

## Zusammenfassung

| Regel | Bedingung |
|-------|-----------|
| $a < b \implies a + c < b + c$ | Immer |
| $a < b \implies ac < bc$ | $c > 0$ |
| $a < b \implies ac > bc$ | $c < 0$ (Zeichen dreht sich) |
| $\|a + b\| \leq \|a\| + \|b\|$ | Dreiecksungleichung |

## Quellen

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996.
