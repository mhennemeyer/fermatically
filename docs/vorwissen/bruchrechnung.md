---
title: "Bruchrechnung"
description: "Addition, Multiplikation, Kürzen und Erweitern von Brüchen"
lang: de
type: vorwissen
---

# Bruchrechnung

## Brüche als Zahlen

Ein **Bruch** $\frac{a}{b}$ mit $a \in \mathbb{Z}$ und $b \in \mathbb{Z} \setminus \{0\}$ repräsentiert das Ergebnis der Division $a \div b$. Dabei heißt $a$ der **Zähler** und $b$ der **Nenner**.

Zwei Brüche $\frac{a}{b}$ und $\frac{c}{d}$ sind **gleich**, wenn $a \cdot d = b \cdot c$.

**Beispiel.** $\frac{2}{3} = \frac{4}{6}$, denn $2 \cdot 6 = 3 \cdot 4 = 12$.

## Kürzen und Erweitern

### Kürzen

Ein Bruch wird **gekürzt**, indem Zähler und Nenner durch denselben Faktor $k \neq 0$ geteilt werden:

$$
\frac{a}{b} = \frac{a / k}{b / k}
$$

**Vollständig gekürzt** ist ein Bruch, wenn $\gcd(a, b) = 1$.

**Beispiel.** $\frac{12}{18} = \frac{12/6}{18/6} = \frac{2}{3}$.

### Erweitern

Ein Bruch wird **erweitert**, indem Zähler und Nenner mit demselben Faktor $k \neq 0$ multipliziert werden:

$$
\frac{a}{b} = \frac{a \cdot k}{b \cdot k}
$$

**Beispiel.** $\frac{2}{3} = \frac{2 \cdot 5}{3 \cdot 5} = \frac{10}{15}$.

## Addition und Subtraktion

Brüche mit **gleichem Nenner** werden direkt addiert:

$$
\frac{a}{n} + \frac{b}{n} = \frac{a + b}{n}
$$

Bei **verschiedenen Nennern** wird zunächst der **Hauptnenner** (kleinstes gemeinsames Vielfaches, kgV) gebildet:

$$
\frac{a}{b} + \frac{c}{d} = \frac{a \cdot d + c \cdot b}{b \cdot d}
$$

**Beispiel.** $\frac{2}{3} + \frac{1}{4} = \frac{2 \cdot 4 + 1 \cdot 3}{3 \cdot 4} = \frac{8 + 3}{12} = \frac{11}{12}$.

Die Subtraktion funktioniert analog: $\frac{a}{b} - \frac{c}{d} = \frac{a \cdot d - c \cdot b}{b \cdot d}$.

## Multiplikation

Brüche werden multipliziert, indem Zähler mit Zähler und Nenner mit Nenner multipliziert werden:

$$
\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}
$$

**Beispiel.** $\frac{2}{3} \cdot \frac{5}{7} = \frac{10}{21}$.

## Division

Die Division durch einen Bruch entspricht der Multiplikation mit dem **Kehrwert**:

$$
\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c}
$$

Voraussetzung: $c \neq 0$.

**Beispiel.** $\frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \cdot \frac{5}{2} = \frac{15}{8}$.

---

## Zusammenfassung

| Operation | Formel |
|-----------|--------|
| Kürzen | $\frac{a}{b} = \frac{a/k}{b/k}$ |
| Erweitern | $\frac{a}{b} = \frac{ak}{bk}$ |
| Addition | $\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}$ |
| Multiplikation | $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$ |
| Division | $\frac{a}{b} \div \frac{c}{d} = \frac{ad}{bc}$ |

## Quellen

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996. Kapitel 1.
