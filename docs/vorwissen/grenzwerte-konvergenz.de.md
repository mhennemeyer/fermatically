---
title: "Grenzwerte und Konvergenz"
description: "Folgen, Reihen, Cauchy-Folgen, Vervollständigung und geometrische Reihe"
lang: de
type: vorwissen
---

# Grenzwerte und Konvergenz

## Folgen

Eine **Folge** reeller Zahlen ist eine Abbildung $\mathbb{N} \to \mathbb{R}$, geschrieben als $(a_n)_{n \geq 1}$ oder kurz $(a_n)$. Die Zahl $a_n$ heißt das **$n$-te Glied** der Folge.

**Beispiel.** Die Folge $a_n = \frac{1}{n}$ ergibt $1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots$

## Konvergenz

Eine Folge $(a_n)$ **konvergiert** gegen den **Grenzwert** $L \in \mathbb{R}$, wenn für jedes $\varepsilon > 0$ ein $N \in \mathbb{N}$ existiert, sodass:

$$
|a_n - L| < \varepsilon \quad \text{für alle } n \geq N
$$

Notation: $\lim_{n \to \infty} a_n = L$ oder $a_n \to L$.

Die Folgenglieder nähern sich $L$ beliebig genau an – ab einem bestimmten Index liegen alle Glieder im Intervall $(L - \varepsilon, L + \varepsilon)$.

**Beispiel.** $\lim_{n \to \infty} \frac{1}{n} = 0$, denn für jedes $\varepsilon > 0$ gilt $\frac{1}{n} < \varepsilon$ sobald $n > \frac{1}{\varepsilon}$.

Eine Folge, die nicht konvergiert, heißt **divergent**.

### Rechenregeln

Für konvergente Folgen mit $a_n \to A$ und $b_n \to B$ gilt:

- $a_n + b_n \to A + B$
- $a_n \cdot b_n \to A \cdot B$
- $\frac{a_n}{b_n} \to \frac{A}{B}$ (falls $B \neq 0$)

## Reihen

Eine **(unendliche) Reihe** ist die Folge der Partialsummen einer Folge $(a_k)$:

$$
S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n
$$

Die Reihe $\sum_{k=1}^{\infty} a_k$ **konvergiert**, wenn die Folge $(S_n)$ konvergiert:

$$
\sum_{k=1}^{\infty} a_k = \lim_{n \to \infty} S_n
$$

### Geometrische Reihe

Die wichtigste Reihe der elementaren Analysis: Für $|q| < 1$ gilt:

$$
\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}
$$

**Beispiel.** $\sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k = \frac{1}{1 - 1/2} = 2$.

Für $|q| \geq 1$ divergiert die geometrische Reihe.

### Notwendige Bedingung

Konvergiert $\sum a_k$, dann gilt $a_k \to 0$. Die Umkehrung ist falsch: Die **harmonische Reihe** $\sum_{k=1}^{\infty} \frac{1}{k}$ divergiert, obwohl $\frac{1}{k} \to 0$.

## Cauchy-Folgen

Eine Folge $(a_n)$ heißt **Cauchy-Folge**, wenn die Folgenglieder untereinander beliebig nahe kommen: Für jedes $\varepsilon > 0$ existiert ein $N$ mit:

$$
|a_m - a_n| < \varepsilon \quad \text{für alle } m, n \geq N
$$

> „The concept of Cauchy sequence captures convergence without reference to the limit itself."
> — Walter Rudin, *Principles of Mathematical Analysis*, McGraw-Hill, 1976.

In $\mathbb{R}$ gilt: Eine Folge konvergiert genau dann, wenn sie eine Cauchy-Folge ist. Diese Eigenschaft heißt **Vollständigkeit** von $\mathbb{R}$.

## Vervollständigung

Nicht jeder metrische Raum ist vollständig. Die **Vervollständigung** eines Raums konstruiert einen größeren Raum, in dem alle Cauchy-Folgen konvergieren.

Das zentrale Beispiel in der Zahlentheorie: Die rationalen Zahlen $\mathbb{Q}$ sind nicht vollständig. Ihre Vervollständigung bezüglich des gewöhnlichen Betrags ergibt $\mathbb{R}$. Die Vervollständigung bezüglich des **$p$-adischen Betrags** ergibt die $p$-adischen Zahlen $\mathbb{Q}_p$ – einen völlig anderen Zahlkörper, der in der modernen Zahlentheorie eine zentrale Rolle spielt.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Konvergenz | $\lim_{n\to\infty} a_n = L$: $\forall\varepsilon>0\ \exists N: n\geq N \Rightarrow |a_n-L|<\varepsilon$ |
| Reihe | $\sum_{k=1}^{\infty} a_k = \lim_{n\to\infty} \sum_{k=1}^{n} a_k$ |
| Geometrische Reihe | $\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}$ für $|q|<1$ |
| Cauchy-Folge | $\forall\varepsilon>0\ \exists N: m,n\geq N \Rightarrow |a_m-a_n|<\varepsilon$ |
| Vollständigkeit | Jede Cauchy-Folge konvergiert |
| Vervollständigung | Konstruktion eines vollständigen Raums aus einem unvollständigen |

## Quellen

- Rudin, Walter: *Principles of Mathematical Analysis.* McGraw-Hill, 3. Auflage, 1976. Kapitel 3.
- Forster, Otto: *Analysis 1.* Springer Spektrum, 12. Auflage, 2016. Kapitel 2–4.
