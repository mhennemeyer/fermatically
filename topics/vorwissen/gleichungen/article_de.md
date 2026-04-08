---
title: "Gleichungen und äquivalente Umformungen"
description: "Gleichheitszeichen, erlaubte Operationen und Äquivalenzumformungen"
lang: de
type: vorwissen
---

# Gleichungen und äquivalente Umformungen

## Was ist eine Gleichung?

Eine **Gleichung** ist eine Aussage der Form $A = B$, wobei $A$ und $B$ mathematische Ausdrücke sind. Das Gleichheitszeichen „$=$" bedeutet: Beide Seiten repräsentieren denselben Wert.

**Beispiele.**

- $3 + 4 = 7$ — eine wahre Aussage.
- $2x + 1 = 9$ — eine Aussage, deren Wahrheitswert von $x$ abhängt. Für $x = 4$: wahr. Für $x = 3$: falsch.

## Äquivalenzumformungen

Eine **Äquivalenzumformung** verändert eine Gleichung so, dass die Lösungsmenge erhalten bleibt. Die neue Gleichung hat exakt dieselben Lösungen wie die ursprüngliche.

### Erlaubte Operationen

| Operation | Formel | Bedingung |
|-----------|--------|-----------|
| Addition auf beiden Seiten | $A = B \iff A + c = B + c$ | — |
| Subtraktion auf beiden Seiten | $A = B \iff A - c = B - c$ | — |
| Multiplikation auf beiden Seiten | $A = B \iff A \cdot c = B \cdot c$ | $c \neq 0$ |
| Division auf beiden Seiten | $A = B \iff \frac{A}{c} = \frac{B}{c}$ | $c \neq 0$ |

Das Prinzip: Dieselbe Operation wird auf **beide** Seiten angewandt. Die Gleichung bleibt im Gleichgewicht.

### Beispiel: Lösung von $2x + 3 = 11$

| Schritt | Gleichung | Operation |
|---------|-----------|-----------|
| 1 | $2x + 3 = 11$ | Ausgangsgleichung |
| 2 | $2x = 8$ | $-3$ auf beiden Seiten |
| 3 | $x = 4$ | $\div 2$ auf beiden Seiten |

Jede Zeile hat dieselbe Lösungsmenge: $\{4\}$.

## Keine Äquivalenzumformungen

Nicht jede Operation erhält die Lösungsmenge:

- **Multiplikation mit 0:** Aus $x = 3$ wird $0 = 0$ — jedes $x$ ist jetzt „Lösung". Lösungsmenge vergrößert.
- **Quadrieren:** Aus $x = -2$ wird $x^2 = 4$, was auch $x = 2$ als Lösung hat. Lösungsmenge vergrößert.
- **Division durch einen Ausdruck mit der Variablen:** Aus $x^2 = 2x$ folgt durch Division durch $x$: $x = 2$. Die Lösung $x = 0$ geht verloren.

## Gleichungen mit Brüchen

Bei Bruchgleichungen werden beide Seiten mit dem Hauptnenner multipliziert:

**Beispiel.** $\frac{x}{3} + \frac{1}{2} = \frac{5}{6}$

Multiplikation mit $6$ (kgV von $3, 2, 6$):

$$
2x + 3 = 5 \implies 2x = 2 \implies x = 1
$$

## Systeme von Gleichungen

Ein **Gleichungssystem** besteht aus mehreren Gleichungen mit mehreren Unbekannten. Die Lösung muss alle Gleichungen gleichzeitig erfüllen.

**Beispiel.** $\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$

Addition beider Gleichungen: $2x = 6$, also $x = 3$. Einsetzen: $y = 2$.

---

## Zusammenfassung

| Begriff | Bedeutung |
|---------|-----------|
| Gleichung | Aussage $A = B$ |
| Äquivalenzumformung | Operation, die die Lösungsmenge erhält |
| Erlaubt | $+c$, $-c$, $\cdot c$ ($c \neq 0$), $\div c$ ($c \neq 0$) auf beiden Seiten |
| Nicht erlaubt | $\cdot 0$, Quadrieren, Division durch Variable (ohne Fallunterscheidung) |

## Quellen

- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996.
