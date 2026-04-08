---
title: "Abbildungen (Funktionen)"
description: "Definitions- und Wertebereich, injektiv, surjektiv, bijektiv"
lang: de
type: vorwissen
---

# Abbildungen (Funktionen)

## Definition

Eine **Abbildung** (oder **Funktion**) $f: A \to B$ ordnet jedem Element $a \in A$ genau ein Element $f(a) \in B$ zu.

- $A$ heißt **Definitionsbereich** (Domain).
- $B$ heißt **Wertebereich** (Codomain).
- $f(A) = \{f(a) : a \in A\} \subseteq B$ heißt **Bild** (Image).

**Beispiel.** $f: \mathbb{Z} \to \mathbb{Z}$ mit $f(x) = x^2$. Hier ist $f(3) = 9$ und $f(-3) = 9$.

## Injektivität

Eine Abbildung $f$ ist **injektiv** (eineindeutig), wenn verschiedene Eingaben verschiedene Ausgaben liefern:

$$
f(a_1) = f(a_2) \implies a_1 = a_2
$$

**Beispiel.** $f(x) = 2x$ ist injektiv: Aus $2a = 2b$ folgt $a = b$.

**Gegenbeispiel.** $f(x) = x^2$ auf $\mathbb{Z}$ ist nicht injektiv: $f(3) = f(-3) = 9$, aber $3 \neq -3$.

## Surjektivität

Eine Abbildung $f: A \to B$ ist **surjektiv**, wenn jedes Element in $B$ mindestens ein Urbild hat:

$$
\forall b \in B\; \exists a \in A: f(a) = b
$$

Äquivalent: $f(A) = B$.

**Beispiel.** $f: \mathbb{Z} \to \mathbb{Z}$ mit $f(x) = x + 1$ ist surjektiv: Für jedes $b \in \mathbb{Z}$ ist $a = b - 1$ ein Urbild.

**Gegenbeispiel.** $f: \mathbb{Z} \to \mathbb{Z}$ mit $f(x) = x^2$ ist nicht surjektiv: $-1$ hat kein Urbild, da $x^2 \geq 0$ für alle $x$.

## Bijektivität

Eine Abbildung ist **bijektiv**, wenn sie sowohl injektiv als auch surjektiv ist. Jedes Element in $B$ hat dann genau ein Urbild.

Bijektive Abbildungen besitzen eine **Umkehrabbildung** $f^{-1}: B \to A$ mit $f^{-1}(f(a)) = a$ und $f(f^{-1}(b)) = b$.

**Beispiel.** $f: \mathbb{R} \to \mathbb{R}$ mit $f(x) = 2x + 1$ ist bijektiv. Die Umkehrfunktion ist $f^{-1}(y) = \frac{y - 1}{2}$.

## Komposition

Die **Komposition** zweier Abbildungen $f: A \to B$ und $g: B \to C$ ist die Abbildung $g \circ f: A \to C$ mit:

$$
(g \circ f)(a) = g(f(a))
$$

**Beispiel.** $f(x) = x + 1$ und $g(x) = x^2$. Dann $(g \circ f)(3) = g(f(3)) = g(4) = 16$.

Die Reihenfolge ist relevant: $(f \circ g)(3) = f(g(3)) = f(9) = 10 \neq 16$.

---

## Zusammenfassung

| Eigenschaft | Bedeutung |
|-------------|-----------|
| Injektiv | Verschiedene Eingaben → verschiedene Ausgaben |
| Surjektiv | Jedes $b \in B$ hat ein Urbild |
| Bijektiv | Injektiv und surjektiv; Umkehrabbildung existiert |
| $g \circ f$ | Komposition: erst $f$, dann $g$ |

## Quellen

- Hammack, Richard: *Book of Proof.* 3. Auflage, 2018. Kapitel 12.
