---
title: "Komplexe Zahlen"
description: "Imaginäre Einheit, Darstellung, Rechenoperationen, Einheitswurzeln und die obere Halbebene"
lang: de
type: vorwissen
---

# Komplexe Zahlen

## Die imaginäre Einheit

Die Gleichung $x^2 = -1$ besitzt keine Lösung in den reellen Zahlen. Die **imaginäre Einheit** $i$ wird als Lösung dieser Gleichung definiert:

$$
i^2 = -1
$$

Mit $i$ lassen sich alle quadratischen Gleichungen lösen, auch solche mit negativer Diskriminante.

## Darstellung und Grundbegriffe

Eine **komplexe Zahl** hat die Form $z = a + bi$ mit $a, b \in \mathbb{R}$. Dabei heißt $a = \operatorname{Re}(z)$ der **Realteil** und $b = \operatorname{Im}(z)$ der **Imaginärteil**.

Die Menge aller komplexen Zahlen wird mit $\mathbb{C}$ bezeichnet:

$$
\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}
$$

Jede reelle Zahl ist eine komplexe Zahl mit $b = 0$, daher gilt $\mathbb{R} \subset \mathbb{C}$.

### Konjugation und Betrag

Die **konjugiert komplexe Zahl** zu $z = a + bi$ ist:

$$
\bar{z} = a - bi
$$

Der **Betrag** (Absolutbetrag) von $z$ ist:

$$
|z| = \sqrt{a^2 + b^2} = \sqrt{z \cdot \bar{z}}
$$

**Beispiel.** Für $z = 3 + 4i$ gilt $\bar{z} = 3 - 4i$ und $|z| = \sqrt{9 + 16} = 5$.

## Rechenoperationen

Für $z_1 = a + bi$ und $z_2 = c + di$ gelten:

**Addition:**
$$
z_1 + z_2 = (a + c) + (b + d)i
$$

**Multiplikation** (unter Verwendung von $i^2 = -1$):
$$
z_1 \cdot z_2 = (ac - bd) + (ad + bc)i
$$

**Division** (Erweitern mit dem Konjugierten des Nenners):
$$
\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
$$

**Beispiel.** $(2 + 3i)(1 - i) = 2 - 2i + 3i - 3i^2 = 2 + i + 3 = 5 + i$.

## Polardarstellung

Jede komplexe Zahl $z \neq 0$ lässt sich in Polarform schreiben:

$$
z = r(\cos\varphi + i\sin\varphi) = r \cdot e^{i\varphi}
$$

Dabei ist $r = |z|$ der Betrag und $\varphi = \arg(z)$ das **Argument** (Winkel zur positiven reellen Achse). Die zweite Gleichung verwendet die **Eulersche Formel**:

$$
e^{i\varphi} = \cos\varphi + i\sin\varphi
$$

> „The formula $e^{i\pi} + 1 = 0$ connects the five most important constants in mathematics."
> — Eli Maor, *e: The Story of a Number*, Princeton University Press, 1994.

Die Polarform vereinfacht Multiplikation und Potenzierung: Beträge werden multipliziert, Argumente addiert.

## Einheitswurzeln

Die **$n$-ten Einheitswurzeln** sind die $n$ Lösungen der Gleichung $z^n = 1$:

$$
\zeta_k = e^{2\pi i k/n}, \quad k = 0, 1, \ldots, n-1
$$

Die Zahl $\zeta = e^{2\pi i/n}$ heißt **primitive $n$-te Einheitswurzel**. Alle $n$-ten Einheitswurzeln sind Potenzen von $\zeta$: $\{\zeta^0, \zeta^1, \ldots, \zeta^{n-1}\}$.

**Beispiel.** Die dritten Einheitswurzeln ($n = 3$) sind:

$$
\zeta_0 = 1, \quad \zeta_1 = e^{2\pi i/3} = -\frac{1}{2} + \frac{\sqrt{3}}{2}i, \quad \zeta_2 = e^{4\pi i/3} = -\frac{1}{2} - \frac{\sqrt{3}}{2}i
$$

In der Zahlentheorie spielen Einheitswurzeln eine zentrale Rolle, etwa als Basis der **Kreisteilungsringe** $\mathbb{Z}[\zeta_p]$, die in Kummers Ansatz zum Beweis von Fermats Letztem Satz auftreten.

## Die obere Halbebene

Die **obere Halbebene** ist die Menge aller komplexen Zahlen mit positivem Imaginärteil:

$$
\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}
$$

Die obere Halbebene ist der natürliche Definitionsbereich von Modulformen – komplexwertigen Funktionen mit speziellen Symmetrieeigenschaften.

---

## Zusammenfassung

| Begriff | Definition |
|---------|-----------|
| Imaginäre Einheit | $i^2 = -1$ |
| Komplexe Zahl | $z = a + bi$ mit $a, b \in \mathbb{R}$ |
| Konjugierte | $\overline{a + bi} = a - bi$ |
| Betrag | $|z| = \sqrt{a^2 + b^2}$ |
| Eulersche Formel | $e^{i\varphi} = \cos\varphi + i\sin\varphi$ |
| $n$-te Einheitswurzel | $\zeta = e^{2\pi i/n}$ |
| Obere Halbebene | $\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im}(z) > 0\}$ |

## Quellen

- Needham, Tristan: *Visual Complex Analysis.* Oxford University Press, 1997. Kapitel 1–4.
- Ahlfors, Lars V.: *Complex Analysis.* McGraw-Hill, 3. Auflage, 1979. Kapitel 1.
- Maor, Eli: *e: The Story of a Number.* Princeton University Press, 1994.
