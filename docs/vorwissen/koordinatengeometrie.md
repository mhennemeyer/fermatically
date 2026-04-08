---
title: "Koordinatengeometrie"
description: "Punkte, Geraden und Kurven in der Ebene"
lang: de
type: vorwissen
---

# Koordinatengeometrie

## Das kartesische Koordinatensystem

Die Ebene $\mathbb{R}^2$ wird durch zwei senkrecht aufeinander stehende Achsen ($x$-Achse, $y$-Achse) mit gemeinsamem Ursprung $O = (0, 0)$ beschrieben. Jeder Punkt hat ein eindeutiges Koordinatenpaar $(x, y)$.

## Abstand und Steigung

### Abstand zweier Punkte

Für $P_1 = (x_1, y_1)$ und $P_2 = (x_2, y_2)$:

$$
d(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

Dies folgt direkt aus dem Satz des Pythagoras.

**Beispiel.** $d((1, 2), (4, 6)) = \sqrt{9 + 16} = \sqrt{25} = 5$.

### Steigung einer Geraden

Die **Steigung** $m$ einer Geraden durch $P_1$ und $P_2$ (mit $x_1 \neq x_2$):

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

## Geraden

### Geradengleichung

Die allgemeine Form einer Geraden:

- **Normalform:** $y = mx + b$ (Steigung $m$, $y$-Achsenabschnitt $b$)
- **Punkt-Steigungs-Form:** $y - y_1 = m(x - x_1)$

**Beispiel.** Gerade durch $(1, 3)$ mit Steigung $2$: $y - 3 = 2(x - 1)$, also $y = 2x + 1$.

### Parallele und senkrechte Geraden

- **Parallel:** $m_1 = m_2$
- **Senkrecht:** $m_1 \cdot m_2 = -1$

## Kurven in der Ebene

Eine **Kurve** ist die Menge aller Punkte $(x, y)$, die eine Gleichung $F(x, y) = 0$ erfüllen.

### Kreis

$$
(x - a)^2 + (y - b)^2 = r^2
$$

Mittelpunkt $(a, b)$, Radius $r$.

### Parabel

$$
y = ax^2 + bx + c
$$

**Beispiel.** $y = x^2$ — Parabel mit Scheitel im Ursprung, nach oben geöffnet.

### Elliptische Kurven (Ausblick)

Gleichungen der Form $y^2 = x^3 + ax + b$ definieren **elliptische Kurven**. Diese spielen eine zentrale Rolle in der modernen Zahlentheorie und im Beweis von Fermats letztem Satz.

---

## Zusammenfassung

| Objekt | Gleichung |
|--------|-----------|
| Abstand | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ |
| Gerade | $y = mx + b$ |
| Kreis | $(x-a)^2 + (y-b)^2 = r^2$ |
| Parabel | $y = ax^2 + bx + c$ |
| Elliptische Kurve | $y^2 = x^3 + ax + b$ |

## Quellen

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996. Kapitel 4.
