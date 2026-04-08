---
title: "Gruppen – Symmetrie als Sprache der Mathematik"
slug: gruppen-und-symmetrie/01-gruppen
series: gruppen-und-symmetrie
part: 1
date: 2026-03-30
status: draft
lang: de
category: algebra
tags:
  - gruppen
  - symmetrie
  - algebra
requires: []
---

# Gruppen – Symmetrie als Sprache der Mathematik

!!! abstract "Zusammenfassung"
    Gruppen als fundamentale algebraische Struktur: Von Drehungen regelmäßiger Polygone
    über Restklassen bis zu den Symmetrien, die Wiles' Beweis durchziehen.

## Voraussetzungen

Keine – dieser Artikel bildet den Einstieg in die abstrakte Algebra.

---

## 1. Symmetrie als mathematische Struktur

Ein Quadrat besitzt acht Symmetrien: vier Drehungen (um 0°, 90°, 180°, 270°) und vier Spiegelungen. Jede Symmetrie bildet das Quadrat auf sich selbst ab, und die Hintereinanderausführung zweier Symmetrien ergibt wieder eine Symmetrie.

Diese Beobachtung verallgemeinert sich: Überall, wo Symmetrien auftreten – in der Geometrie, der Physik, der Zahlentheorie –, gehorcht die zugrunde liegende Struktur denselben Regeln. Diese Struktur heißt **Gruppe**.

Beispiele, die auf den ersten Blick nichts miteinander verbindet:

- Die **Drehungen und Spiegelungen** eines regelmäßigen $n$-Ecks
- Die **Addition** ganzer Zahlen: $3 + 5 = 8$, $7 + (-7) = 0$
- Die **Permutationen** einer Menge: Umordnungen von $\{1, 2, 3\}$
- Die **Symmetrien der Nullstellen** eines Polynoms (→ Galois-Theorie)

All diese Beispiele erfüllen dieselben vier Axiome.

## 2. Die Gruppenaxiome

Eine **Gruppe** ist ein Paar $(G, \cdot)$ aus einer Menge $G$ und einer Verknüpfung $\cdot : G \times G \to G$, die vier Axiome erfüllt:

**(G1) Abgeschlossenheit.** Für alle $a, b \in G$ ist auch $a \cdot b \in G$.

**(G2) Assoziativität.** Für alle $a, b, c \in G$ gilt $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.

**(G3) Neutrales Element.** Es existiert ein Element $e \in G$ mit $e \cdot a = a \cdot e = a$ für alle $a \in G$.

**(G4) Inverse.** Für jedes $a \in G$ existiert ein Element $a^{-1} \in G$ mit $a \cdot a^{-1} = a^{-1} \cdot a = e$.

Wenn zusätzlich $a \cdot b = b \cdot a$ für alle $a, b \in G$ gilt, heißt die Gruppe **abelsch** (oder kommutativ) – benannt nach Niels Henrik Abel.

!!! note "Notation"
    Für abelsche Gruppen wird die Verknüpfung oft als $+$ statt $\cdot$ geschrieben und das neutrale Element als $0$ statt $e$. Das Inverse von $a$ ist dann $-a$.

## 3. Erste Beispiele

### Die ganzen Zahlen $(\mathbb{Z}, +)$

Die ganzen Zahlen mit der Addition bilden die einfachste unendliche Gruppe:

- **Abgeschlossen**: $a + b \in \mathbb{Z}$ für alle $a, b \in \mathbb{Z}$ ✓
- **Assoziativ**: $(a + b) + c = a + (b + c)$ ✓
- **Neutrales Element**: $0$ (denn $a + 0 = a$) ✓
- **Inverse**: $-a$ (denn $a + (-a) = 0$) ✓
- **Abelsch**: $a + b = b + a$ ✓

### Restklassen $(\mathbb{Z}/n\mathbb{Z}, +)$

Für $n \geq 1$ bilden die Restklassen modulo $n$ eine endliche abelsche Gruppe. Beispiel: $\mathbb{Z}/4\mathbb{Z} = \{0, 1, 2, 3\}$ mit der Addition modulo $4$:

| $+$   | $0$ | $1$ | $2$ | $3$ |
|-------|-----|-----|-----|-----|
| $0$   | $0$ | $1$ | $2$ | $3$ |
| $1$   | $1$ | $2$ | $3$ | $0$ |
| $2$   | $2$ | $3$ | $0$ | $1$ |
| $3$   | $3$ | $0$ | $1$ | $2$ |

Diese Gruppe hat **Ordnung** $4$ (vier Elemente). Sie ist zyklisch: Jedes Element lässt sich als Vielfaches von $1$ schreiben.

### Die symmetrische Gruppe $S_n$

Die **symmetrische Gruppe** $S_n$ besteht aus allen Permutationen (Umordnungen) der Menge $\{1, 2, \ldots, n\}$, mit der Komposition als Verknüpfung.

$S_3$ hat $3! = 6$ Elemente:

$$
\text{id}, \quad (12), \quad (13), \quad (23), \quad (123), \quad (132)
$$

Dabei bedeutet $(12)$: „vertausche $1$ und $2$", und $(123)$: „sende $1 \to 2 \to 3 \to 1$".

$S_3$ ist **nicht** abelsch: $(12) \circ (13) = (132)$, aber $(13) \circ (12) = (123)$.

### Die Diedergruppe $D_n$

Die Symmetriegruppe eines regelmäßigen $n$-Ecks heißt **Diedergruppe** $D_n$. Sie hat $2n$ Elemente: $n$ Drehungen und $n$ Spiegelungen. Für $n = 4$ (Quadrat) ist $|D_4| = 8$.

## 4. Untergruppen und Ordnung

Eine Teilmenge $H \subseteq G$ heißt **Untergruppe** von $G$, wenn $H$ selbst mit der eingeschränkten Verknüpfung eine Gruppe bildet. Notation: $H \leq G$.

**Beispiele:**
- $2\mathbb{Z} = \{\ldots, -4, -2, 0, 2, 4, \ldots\} \leq \mathbb{Z}$ (die geraden Zahlen)
- $\{e, (123), (132)\} \leq S_3$ (die Drehungen des Dreiecks)

Die **Ordnung** $|G|$ einer Gruppe ist die Anzahl ihrer Elemente. Die **Ordnung** $\text{ord}(a)$ eines Elements $a$ ist die kleinste positive Zahl $n$ mit $a^n = e$.

**Satz von Lagrange.** Ist $H \leq G$ mit $|G| < \infty$, dann teilt $|H|$ die Zahl $|G|$.

Konsequenz: In einer Gruppe mit $12$ Elementen kann eine Untergruppe nur $1$, $2$, $3$, $4$, $6$ oder $12$ Elemente haben. Die Ordnung jedes Elements teilt $|G|$.

> „The notion of a group is one of the great simplifying and unifying ideas in modern mathematics."
> — Michael Artin, *Algebra* (1991), S. 42

!!! tip "Lagrange in Aktion"
    Sei $G$ eine Gruppe mit $|G| = p$ (Primzahl). Dann hat $G$ keine echten Untergruppen außer $\{e\}$ und $G$ selbst. Also ist $G$ zyklisch: $G \cong \mathbb{Z}/p\mathbb{Z}$.

## 5. Homomorphismen

Ein **Gruppenhomomorphismus** ist eine Abbildung $\varphi: G \to H$ zwischen zwei Gruppen, die die Struktur erhält:

$$
\varphi(a \cdot b) = \varphi(a) \cdot \varphi(b) \quad \text{für alle } a, b \in G
$$

Homomorphismen transportieren algebraische Beziehungen von einer Gruppe in eine andere.

**Beispiele:**
- $\varphi: \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $a \mapsto a \bmod n$ (Reduktion modulo $n$)
- $\det: \text{GL}_n(\mathbb{R}) \to \mathbb{R}^*$, $A \mapsto \det(A)$ (Determinante)

Der **Kern** eines Homomorphismus $\varphi: G \to H$ ist:

$$
\ker(\varphi) = \{a \in G \mid \varphi(a) = e_H\}
$$

Der Kern ist immer eine Untergruppe von $G$ – und sogar ein **Normalteiler**.

## 6. Normalteiler und Faktorgruppen

Eine Untergruppe $N \leq G$ heißt **Normalteiler** (geschrieben $N \trianglelefteq G$), wenn $gNg^{-1} = N$ für alle $g \in G$, also wenn $N$ unter Konjugation invariant ist.

In abelschen Gruppen ist jede Untergruppe ein Normalteiler (weil $gng^{-1} = n$ für alle $g, n$).

Normalteiler ermöglichen die Bildung von **Faktorgruppen** (Quotientengruppen):

$$
G/N = \{gN \mid g \in G\}
$$

Die Elemente von $G/N$ sind die **Nebenklassen** $gN = \{gn \mid n \in N\}$, und die Verknüpfung ist $(gN)(hN) = (gh)N$.

**Beispiel:** $\mathbb{Z}/n\mathbb{Z}$ ist die Faktorgruppe von $\mathbb{Z}$ nach dem Normalteiler $n\mathbb{Z}$.

**Der Homomorphiesatz.** Für jeden Homomorphismus $\varphi: G \to H$ gilt:

$$
G / \ker(\varphi) \cong \text{Bild}(\varphi)
$$

Die Faktorgruppe nach dem Kern ist isomorph zum Bild. Dieser Satz verbindet Homomorphismen, Normalteiler und Faktorgruppen.

### Einfache Gruppen

Eine Gruppe $G \neq \{e\}$ heißt **einfach**, wenn sie keine Normalteiler außer $\{e\}$ und $G$ selbst besitzt. Einfache Gruppen sind die Grundbausteine der Gruppentheorie – jede endliche Gruppe lässt sich aus einfachen Gruppen zusammensetzen (Jordan-Hölder-Satz).

Die Klassifikation aller endlichen einfachen Gruppen ist eines der umfangreichsten Ergebnisse der Mathematik: Sie umfasst die zyklischen Gruppen $\mathbb{Z}/p\mathbb{Z}$, die alternierenden Gruppen $A_n$ ($n \geq 5$), 16 Familien von „Lie-Typ"-Gruppen und 26 sporadische Gruppen.

## 7. Gruppen im Kontext von FLT

Für Fermats letzten Satz sind Gruppen über die **Galois-Theorie** zentral: Die Symmetrien der Nullstellen eines Polynoms bilden eine Gruppe – die **Galois-Gruppe**. Diese Gruppe kontrolliert die algebraische Struktur der zugehörigen Körpererweiterung.

In Wiles' Beweis treten Gruppen in mehreren Formen auf:

1. **Die absolute Galois-Gruppe** $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ – das zentrale Symmetrieobjekt der algebraischen Zahlentheorie. Sie wirkt auf den Teilungspunkten elliptischer Kurven.

2. **Matrizengruppen** $\text{GL}_2(\mathbb{F}_p)$ und $\text{GL}_2(\mathbb{Z}_p)$ – Zielgruppen der Galois-Darstellungen, die elliptische Kurven mit linearer Algebra verbinden.

3. **Hecke-Algebren** – Symmetrien im Raum der Modulformen, die algebraische Strukturen auf den Fourier-Koeffizienten erzeugen.

> „Groups, as men, will be known by their actions."
> — Guillermo Moreno, zitiert in Joseph Rotman, *An Introduction to the Theory of Groups* (1995)

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 3
- **Michael Artin**: *Algebra*, Prentice Hall (1991)
- **Joseph Gallian**: *Contemporary Abstract Algebra*, Cengage (2020)
