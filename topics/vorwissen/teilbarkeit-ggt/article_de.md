---
title: "Teilbarkeit und ggT"
description: "Division mit Rest, größter gemeinsamer Teiler und der Euklidische Algorithmus"
lang: de
type: vorwissen
---

# Teilbarkeit und ggT

## Teilbarkeit

Eine ganze Zahl $a$ **teilt** eine ganze Zahl $b$, wenn ein $k \in \mathbb{Z}$ existiert mit $b = k \cdot a$. Notation: $a \mid b$.

$$
a \mid b \iff \exists\, k \in \mathbb{Z}: b = k \cdot a
$$

**Beispiel.** $3 \mid 12$, denn $12 = 4 \cdot 3$. Dagegen $3 \nmid 7$, denn es gibt kein ganzzahliges $k$ mit $7 = k \cdot 3$.

### Grundlegende Eigenschaften

- **Reflexivität:** $a \mid a$ für alle $a \neq 0$.
- **Transitivität:** Aus $a \mid b$ und $b \mid c$ folgt $a \mid c$.
- **Linearität:** Aus $a \mid b$ und $a \mid c$ folgt $a \mid (b + c)$ und $a \mid (b - c)$.

## Division mit Rest

Für beliebige ganze Zahlen $a$ und $b$ mit $b > 0$ existieren eindeutige ganze Zahlen $q$ (Quotient) und $r$ (Rest) mit:

$$
a = q \cdot b + r, \quad 0 \leq r < b
$$

**Beispiel.** $17 = 2 \cdot 7 + 3$. Hier ist $q = 2$ und $r = 3$.

Die Division mit Rest ist die Grundlage der modularen Arithmetik und des Euklidischen Algorithmus.

## Größter gemeinsamer Teiler (ggT)

Der **größte gemeinsame Teiler** zweier ganzer Zahlen $a$ und $b$ (nicht beide $0$) ist die größte positive ganze Zahl, die sowohl $a$ als auch $b$ teilt:

$$
\gcd(a, b) = \max\{d \in \mathbb{N} : d \mid a \text{ und } d \mid b\}
$$

**Beispiel.** Die Teiler von $12$ sind $\{1, 2, 3, 4, 6, 12\}$, die Teiler von $18$ sind $\{1, 2, 3, 6, 9, 18\}$. Gemeinsame Teiler: $\{1, 2, 3, 6\}$. Also $\gcd(12, 18) = 6$.

### Teilerfremdheit

Zwei Zahlen $a$ und $b$ heißen **teilerfremd**, wenn $\gcd(a, b) = 1$.

**Beispiel.** $\gcd(8, 15) = 1$, also sind $8$ und $15$ teilerfremd.

## Der Euklidische Algorithmus

Der Euklidische Algorithmus berechnet $\gcd(a, b)$ durch wiederholte Division mit Rest. Die zentrale Eigenschaft:

$$
\gcd(a, b) = \gcd(b, a \bmod b)
$$

### Ablauf

Gegeben: $a, b \in \mathbb{Z}$ mit $a \geq b > 0$.

1. Berechne $r = a \bmod b$.
2. Falls $r = 0$: $\gcd(a, b) = b$. Fertig.
3. Sonst: Setze $a \leftarrow b$, $b \leftarrow r$ und wiederhole ab Schritt 1.

### Beispiel: $\gcd(252, 105)$

| Schritt | $a$   | $b$   | $r = a \bmod b$ |
|---------|-------|-------|------------------|
| 1       | 252   | 105   | 42               |
| 2       | 105   | 42    | 21               |
| 3       | 42    | 21    | 0                |

Ergebnis: $\gcd(252, 105) = 21$.

### Korrektheit

Der Algorithmus terminiert, weil die Reste streng monoton fallen ($r < b$ in jedem Schritt). Er ist korrekt, weil $\gcd(a, b) = \gcd(b, r)$ gilt: Jeder gemeinsame Teiler von $a$ und $b$ teilt auch $r = a - q \cdot b$, und umgekehrt.

## Lemma von Bézout

Für alle $a, b \in \mathbb{Z}$ (nicht beide $0$) existieren $x, y \in \mathbb{Z}$ mit:

$$
\gcd(a, b) = x \cdot a + y \cdot b
$$

Die Koeffizienten $x, y$ lassen sich durch den **erweiterten Euklidischen Algorithmus** berechnen.

**Beispiel.** $\gcd(252, 105) = 21$. Es gilt $21 = 1 \cdot 252 + (-2) \cdot 105$, also $x = 1, y = -2$.

Das Lemma von Bézout ist ein zentrales Werkzeug in der Zahlentheorie. Es impliziert unter anderem: Sind $a$ und $b$ teilerfremd und $a \mid bc$, dann $a \mid c$.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| $a \mid b$ | Es existiert $k \in \mathbb{Z}$ mit $b = ka$ |
| Division mit Rest | $a = qb + r$ mit $0 \leq r < b$ |
| $\gcd(a,b)$ | Größter gemeinsamer Teiler |
| Teilerfremd | $\gcd(a,b) = 1$ |
| Euklidischer Algorithmus | $\gcd(a,b) = \gcd(b, a \bmod b)$ |
| Bézout | $\gcd(a,b) = xa + yb$ für geeignete $x, y \in \mathbb{Z}$ |

## Quellen

- Hardy, G.H.; Wright, E.M.: *An Introduction to the Theory of Numbers.* Oxford University Press, 6. Auflage, 2008. Kapitel 1–2.
- Burton, David M.: *Elementary Number Theory.* McGraw-Hill, 7. Auflage, 2010. Kapitel 2.
