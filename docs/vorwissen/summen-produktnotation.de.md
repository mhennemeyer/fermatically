---
title: "Summen- und Produktnotation"
description: "Summenzeichen Σ, Produktzeichen Π, Indexmengen, Doppelsummen und wichtige Formeln"
lang: de
type: vorwissen
---

# Summen- und Produktnotation

## Das Summenzeichen Σ

Das **Summenzeichen** $\Sigma$ (griechisch: Sigma) fasst die Addition mehrerer Terme in kompakter Form zusammen:

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n
$$

Dabei heißt $k$ der **Laufindex**, $1$ die **untere Grenze** und $n$ die **obere Grenze**. Der Ausdruck $a_k$ ist der **Summand**.

**Beispiel.**
$$
\sum_{k=1}^{4} k^2 = 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30
$$

### Rechenregeln

- **Linearität:**
$$
\sum_{k=1}^{n} (c \cdot a_k + b_k) = c \cdot \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k
$$

- **Konstante Summanden:**
$$
\sum_{k=1}^{n} c = n \cdot c
$$

- **Indexverschiebung:** Bei Substitution $j = k - 1$ wird aus $\sum_{k=1}^{n} a_k$ die Summe $\sum_{j=0}^{n-1} a_{j+1}$. Der Wert ändert sich nicht.

## Das Produktzeichen Π

Das **Produktzeichen** $\Pi$ (griechisch: Pi) fasst die Multiplikation mehrerer Faktoren zusammen:

$$
\prod_{k=1}^{n} a_k = a_1 \cdot a_2 \cdots a_n
$$

**Beispiel.** Die Fakultät lässt sich als Produkt schreiben:
$$
n! = \prod_{k=1}^{n} k = 1 \cdot 2 \cdot 3 \cdots n
$$

### Rechenregeln

- **Potenzierung:**
$$
\prod_{k=1}^{n} c = c^n
$$

- **Produkt von Potenzen:**
$$
\prod_{k=1}^{n} a_k^{m} = \left(\prod_{k=1}^{n} a_k\right)^{m}
$$

## Summen über allgemeine Indexmengen

Der Laufindex muss nicht bei $1$ beginnen oder ganzzahlig fortschreiten. Die allgemeine Form lautet:

$$
\sum_{k \in I} a_k
$$

Dabei ist $I$ eine endliche **Indexmenge**.

**Beispiel.** Summe über alle Primzahlen bis $10$:
$$
\sum_{p \in \{2,3,5,7\}} \frac{1}{p} = \frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7}
$$

## Doppelsummen

Bei zwei Laufindizes entsteht eine **Doppelsumme**:

$$
\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}
$$

Die Reihenfolge der Summation ist bei endlichen Summen vertauschbar:

$$
\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij}
$$

**Beispiel.**
$$
\sum_{i=1}^{2} \sum_{j=1}^{3} ij = \sum_{i=1}^{2} (i \cdot 1 + i \cdot 2 + i \cdot 3) = \sum_{i=1}^{2} 6i = 6 + 12 = 18
$$

## Wichtige Summenformeln

Die folgenden Formeln treten in der Zahlentheorie häufig auf:

**Arithmetische Summe (Gauß):**
$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
$$

**Geometrische Summe** (für $q \neq 1$):
$$
\sum_{k=0}^{n} q^k = \frac{q^{n+1} - 1}{q - 1}
$$

**Geometrische Reihe** (für $|q| < 1$):
$$
\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}
$$

> „The notation $\sum$ for summation was introduced by Euler in 1755."
> — Florian Cajori, *A History of Mathematical Notations*, Dover, 1993.

## Anwendung: Euler-Produkt

Ein zentrales Beispiel aus der Zahlentheorie verbindet Summen- und Produktnotation. Euler zeigte:

$$
\sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prim}} \frac{1}{1 - p^{-s}} \quad (s > 1)
$$

Die linke Seite ist eine unendliche Reihe (die Riemannsche Zetafunktion), die rechte Seite ein unendliches Produkt über alle Primzahlen.

---

## Zusammenfassung

| Notation | Bedeutung |
|----------|-----------|
| $\sum_{k=1}^{n} a_k$ | $a_1 + a_2 + \cdots + a_n$ |
| $\prod_{k=1}^{n} a_k$ | $a_1 \cdot a_2 \cdots a_n$ |
| $\sum_{k \in I} a_k$ | Summe über Indexmenge $I$ |
| $\sum_{i}\sum_{j} a_{ij}$ | Doppelsumme |
| $\sum_{k=0}^{\infty} q^k$ | Geometrische Reihe ($|q|<1$): $\frac{1}{1-q}$ |

## Quellen

- Cajori, Florian: *A History of Mathematical Notations.* Dover, 1993. Band 2, §§ 438–439.
- Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren: *Concrete Mathematics.* Addison-Wesley, 2. Auflage, 1994. Kapitel 2.
