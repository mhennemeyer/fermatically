---
title: "Modulare Arithmetik"
description: "Kongruenz, Rechnen modulo n und Restklassen"
lang: de
type: vorwissen
---

# Modulare Arithmetik

## Kongruenz

Zwei ganze Zahlen $a$ und $b$ heißen **kongruent modulo $n$**, wenn ihre Differenz durch $n$ teilbar ist:

$$
a \equiv b \pmod{n} \iff n \mid (a - b)
$$

Äquivalent: $a$ und $b$ lassen bei Division durch $n$ denselben Rest.

**Beispiel.** $17 \equiv 5 \pmod{4}$, denn $17 - 5 = 12$ und $4 \mid 12$. Beide Zahlen lassen bei Division durch $4$ den Rest $1$.

## Rechnen modulo n

### Addition

$$
a \equiv a' \pmod{n},\; b \equiv b' \pmod{n} \implies a + b \equiv a' + b' \pmod{n}
$$

**Beispiel.** $7 \equiv 2 \pmod{5}$ und $8 \equiv 3 \pmod{5}$. Dann $7 + 8 = 15 \equiv 2 + 3 = 5 \equiv 0 \pmod{5}$. ✓

### Multiplikation

$$
a \equiv a' \pmod{n},\; b \equiv b' \pmod{n} \implies a \cdot b \equiv a' \cdot b' \pmod{n}
$$

**Beispiel.** $7 \equiv 2 \pmod{5}$ und $8 \equiv 3 \pmod{5}$. Dann $7 \cdot 8 = 56 \equiv 2 \cdot 3 = 6 \equiv 1 \pmod{5}$. ✓

### Potenzierung

$$
a \equiv b \pmod{n} \implies a^k \equiv b^k \pmod{n} \quad \text{für alle } k \geq 0
$$

**Beispiel.** $2^{10} = 1024$. Da $2 \equiv -1 \pmod{3}$, folgt $2^{10} \equiv (-1)^{10} = 1 \pmod{3}$.

### Division (eingeschränkt)

Division ist **nicht** allgemein erlaubt. Aus $ac \equiv bc \pmod{n}$ folgt nur dann $a \equiv b \pmod{n}$, wenn $\gcd(c, n) = 1$.

## Restklassen

Die **Restklasse** von $a$ modulo $n$ ist die Menge aller ganzen Zahlen, die zu $a$ kongruent sind:

$$
[a]_n = \{a + kn : k \in \mathbb{Z}\} = \{\ldots, a - 2n, a - n, a, a + n, a + 2n, \ldots\}
$$

Für $n = 3$ gibt es genau drei Restklassen:

- $[0]_3 = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$
- $[1]_3 = \{\ldots, -5, -2, 1, 4, 7, \ldots\}$
- $[2]_3 = \{\ldots, -4, -1, 2, 5, 8, \ldots\}$

Die Menge aller Restklassen modulo $n$ wird mit $\mathbb{Z}/n\mathbb{Z}$ (oder $\mathbb{Z}_n$) bezeichnet.

## Anwendung: Teilbarkeitsregeln

Modulare Arithmetik erklärt klassische Teilbarkeitsregeln:

- **Teilbarkeit durch 3:** Eine Zahl ist durch $3$ teilbar $\iff$ ihre Quersumme ist durch $3$ teilbar. Grund: $10 \equiv 1 \pmod{3}$, also $10^k \equiv 1 \pmod{3}$.
- **Teilbarkeit durch 9:** Analog, da $10 \equiv 1 \pmod{9}$.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| $a \equiv b \pmod{n}$ | $n \mid (a-b)$ |
| Restklasse $[a]_n$ | $\{a + kn : k \in \mathbb{Z}\}$ |
| Addition mod $n$ | $(a + b) \bmod n$ |
| Multiplikation mod $n$ | $(a \cdot b) \bmod n$ |
| $\mathbb{Z}/n\mathbb{Z}$ | Menge der Restklassen modulo $n$ |

## Quellen

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6. Auflage, 2008. Kapitel 5.
- Burton, David M.: *Elementary Number Theory.* McGraw-Hill, 7. Auflage, 2010. Kapitel 4.
