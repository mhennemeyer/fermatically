---
title: "Kombinatorik"
description: "Fakultät, Binomialkoeffizient und Binomialsatz"
lang: de
type: vorwissen
---

# Kombinatorik

## Fakultät

Die **Fakultät** einer natürlichen Zahl $n$ ist das Produkt aller positiven ganzen Zahlen bis $n$:

$$
n! = 1 \cdot 2 \cdot 3 \cdots n = \prod_{k=1}^{n} k
$$

Per Konvention gilt $0! = 1$.

**Beispiel.** $5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$.

### Kombinatorische Bedeutung

$n!$ ist die Anzahl der **Permutationen** einer $n$-elementigen Menge – die Anzahl der Möglichkeiten, $n$ verschiedene Objekte in eine Reihenfolge zu bringen.

**Beispiel.** Die Menge $\{a, b, c\}$ hat $3! = 6$ Permutationen: $abc, acb, bac, bca, cab, cba$.

In der Gruppentheorie: Die symmetrische Gruppe $S_n$ (die Gruppe aller Permutationen von $n$ Elementen) hat die **Ordnung** $|S_n| = n!$.

## Binomialkoeffizient

Der **Binomialkoeffizient** $\binom{n}{k}$ gibt die Anzahl der Möglichkeiten an, $k$ Elemente aus einer $n$-elementigen Menge auszuwählen (ohne Beachtung der Reihenfolge):

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!} \quad \text{für } 0 \leq k \leq n
$$

Gelesen als „$n$ über $k$".

**Beispiel.** $\binom{5}{2} = \frac{5!}{2! \cdot 3!} = \frac{120}{2 \cdot 6} = 10$. Aus fünf Elementen lassen sich zehn verschiedene Zweiergruppen bilden.

### Eigenschaften

- **Symmetrie:** $\binom{n}{k} = \binom{n}{n-k}$
- **Randfälle:** $\binom{n}{0} = \binom{n}{n} = 1$
- **Rekursion (Pascalsche Regel):**

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$

Diese Rekursion erzeugt das **Pascalsche Dreieck**:

$$
\begin{array}{ccccccc}
& & & 1 & & & \\
& & 1 & & 1 & & \\
& 1 & & 2 & & 1 & \\
1 & & 3 & & 3 & & 1 \\
\end{array}
$$

## Binomialsatz

Für beliebige $a, b$ und $n \in \mathbb{N}_0$ gilt:

$$
(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k
$$

> „The binomial theorem is one of the most useful formulas in all of mathematics."
> — Ronald L. Graham, Donald E. Knuth, Oren Patashnik, *Concrete Mathematics*, Addison-Wesley, 1994.

**Beispiel.** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$.

### Spezialfälle

- **$a = 1, b = 1$:** $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ (Gesamtzahl aller Teilmengen einer $n$-elementigen Menge).
- **$a = 1, b = -1$:** $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$.

## Anwendung in der Zahlentheorie

In der Zahlentheorie treten Binomialkoeffizienten unter anderem auf bei:

- **Fermats kleiner Satz:** Aus $\binom{p}{k} \equiv 0 \pmod{p}$ für $0 < k < p$ (mit $p$ prim) folgt $(a+b)^p \equiv a^p + b^p \pmod{p}$.
- **Symmetrische Gruppe:** Die Ordnung $|S_n| = n!$ bestimmt die Struktur der Galois-Gruppen endlicher Erweiterungen.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Fakultät | $n! = 1 \cdot 2 \cdots n$, $0! = 1$ |
| Permutationen | $n!$ Anordnungen von $n$ Elementen |
| Binomialkoeffizient | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ |
| Pascalsche Regel | $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ |
| Binomialsatz | $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k}b^k$ |

## Quellen

- Graham, Ronald L.; Knuth, Donald E.; Patashnik, Oren: *Concrete Mathematics.* Addison-Wesley, 2. Auflage, 1994. Kapitel 5.
- Aigner, Martin: *Diskrete Mathematik.* Springer Spektrum, 6. Auflage, 2006. Kapitel 1.
