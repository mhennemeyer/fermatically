---
title: "Zahlenbereiche"
description: "ℕ, ℤ, ℚ, ℝ, ℂ – die Erweiterungskette der Zahlensysteme"
lang: de
type: vorwissen
---

# Zahlenbereiche

## Die Erweiterungskette

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

Jede Erweiterung löst ein Problem, das im vorherigen Zahlenbereich unlösbar war.

## Natürliche Zahlen (ℕ)

$$
\mathbb{N} = \{0, 1, 2, 3, \ldots\}
$$

Geeignet für: Zählen, Addition, Multiplikation.

**Problem:** Die Gleichung $x + 3 = 1$ hat keine Lösung in $\mathbb{N}$.

## Ganze Zahlen (ℤ)

$$
\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}
$$

Erweiterung von $\mathbb{N}$ um negative Zahlen. Subtraktion ist uneingeschränkt möglich.

**Problem:** Die Gleichung $2x = 3$ hat keine Lösung in $\mathbb{Z}$.

## Rationale Zahlen (ℚ)

$$
\mathbb{Q} = \left\{\frac{a}{b} : a \in \mathbb{Z},\; b \in \mathbb{Z} \setminus \{0\}\right\}
$$

Erweiterung von $\mathbb{Z}$ um Brüche. Division (außer durch $0$) ist uneingeschränkt möglich.

Rationale Zahlen haben entweder eine endliche oder eine periodische Dezimaldarstellung: $\frac{1}{4} = 0{,}25$, $\frac{1}{3} = 0{,}\overline{3}$.

**Problem:** Die Gleichung $x^2 = 2$ hat keine Lösung in $\mathbb{Q}$ (denn $\sqrt{2}$ ist irrational).

## Reelle Zahlen (ℝ)

$\mathbb{R}$ umfasst alle Punkte auf der Zahlengeraden: rationale und irrationale Zahlen.

Irrationale Zahlen haben eine nicht-periodische, unendliche Dezimaldarstellung: $\sqrt{2} = 1{,}41421\ldots$, $\pi = 3{,}14159\ldots$

$\mathbb{R}$ ist **vollständig**: Jede Cauchy-Folge konvergiert in $\mathbb{R}$.

**Problem:** Die Gleichung $x^2 = -1$ hat keine Lösung in $\mathbb{R}$.

## Komplexe Zahlen (ℂ)

$$
\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}, \quad i^2 = -1
$$

Erweiterung von $\mathbb{R}$ um die **imaginäre Einheit** $i$. Jede polynomielle Gleichung hat in $\mathbb{C}$ eine Lösung (Fundamentalsatz der Algebra).

**Beispiel.** $x^2 + 1 = 0$ hat die Lösungen $x = i$ und $x = -i$.

---

## Zusammenfassung

| Zahlenbereich | Symbol | Neue Eigenschaft | Unlösbares Problem |
|---------------|--------|-------------------|--------------------|
| Natürliche Zahlen | $\mathbb{N}$ | Zählen | $x + 3 = 1$ |
| Ganze Zahlen | $\mathbb{Z}$ | Subtraktion | $2x = 3$ |
| Rationale Zahlen | $\mathbb{Q}$ | Division | $x^2 = 2$ |
| Reelle Zahlen | $\mathbb{R}$ | Vollständigkeit | $x^2 = -1$ |
| Komplexe Zahlen | $\mathbb{C}$ | Algebraisch abgeschlossen | — |

## Quellen

- Ebbinghaus, H.-D. et al.: *Numbers.* Springer, 1991.
- Courant, Richard; Robbins, Herbert: *What Is Mathematics?* Oxford University Press, 2. Auflage, 1996. Kapitel 2.
