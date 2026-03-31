---
title: "Ringe und Körper – Die Welt jenseits der rationalen Zahlen"
slug: ringe-und-koerper/01-ringe-koerper
series: ringe-und-koerper
part: 1
date: 2026-03-30
status: draft
lang: de
category: algebra
tags:
  - ringe
  - koerper
  - algebra
  - idealtheorie
requires:
  - gruppen-und-symmetrie/01-gruppen
---

# Ringe und Körper

!!! abstract "Zusammenfassung"
    Von Gruppen (eine Verknüpfung) zu Ringen (zwei Verknüpfungen) und Körpern (mit Division).
    Warum die ganzen Zahlen nicht immer „genug" sind – und wie die Idealtheorie das Problem
    der fehlenden eindeutigen Faktorisierung löst.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](../../gruppen-und-symmetrie/01-gruppen/article_de.md)

---

## 1. Von Gruppen zu Ringen

In einer Gruppe haben wir *eine* Verknüpfung. Doch schon die ganzen Zahlen $\mathbb{Z}$ haben *zwei*: Addition und Multiplikation. Um beide gleichzeitig zu erfassen, brauchen wir eine reichere Struktur – den **Ring**.

Die Motivation kommt direkt aus der Zahlentheorie: Fermats letzter Satz handelt von der Gleichung $x^n + y^n = z^n$ in den ganzen Zahlen. Die Beweise für $n = 3$ und $n = 4$ zeigten, dass man manchmal den Zahlbereich erweitern muss – auf $\mathbb{Z}[\omega]$ oder $\mathbb{Z}[i]$. All diese Zahlbereiche sind Ringe.

## 2. Ringaxiome und Beispiele

Ein **Ring** $(R, +, \cdot)$ ist eine Menge $R$ mit zwei Verknüpfungen, die folgende Axiome erfüllen:

1. $(R, +)$ ist eine abelsche Gruppe (mit neutralem Element $0$)
2. Die Multiplikation ist assoziativ: $(ab)c = a(bc)$
3. Es gibt ein Einselement: $1 \cdot a = a \cdot 1 = a$
4. Die Distributivgesetze gelten: $a(b + c) = ab + ac$ und $(a + b)c = ac + bc$

Wenn zusätzlich $ab = ba$ für alle $a, b \in R$ gilt, heißt der Ring **kommutativ**.

### Die wichtigsten Beispiele

| Ring | Beschreibung | Kommutativ? |
|------|-------------|-------------|
| $\mathbb{Z}$ | Ganze Zahlen | ✓ |
| $\mathbb{Z}/n\mathbb{Z}$ | Restklassen modulo $n$ | ✓ |
| $\mathbb{Z}[i] = \{a + bi \mid a, b \in \mathbb{Z}\}$ | Gaußsche ganze Zahlen | ✓ |
| $\mathbb{Z}[\omega] = \{a + b\omega \mid a, b \in \mathbb{Z}\}$ | Eisenstein-Zahlen | ✓ |
| $\mathbb{Z}[\zeta_p]$ | Kreisteilungsring | ✓ |
| $K[x]$ | Polynomring über einem Körper $K$ | ✓ |
| $M_n(\mathbb{R})$ | $n \times n$-Matrizen | ✗ (für $n \geq 2$) |

### Nullteiler und Integritätsbereiche

In $\mathbb{Z}$ gilt: Wenn $ab = 0$, dann $a = 0$ oder $b = 0$. Das ist nicht in allen Ringen so! In $\mathbb{Z}/6\mathbb{Z}$ ist $2 \cdot 3 = 6 \equiv 0$, obwohl weder $2$ noch $3$ null sind. Solche Elemente heißen **Nullteiler**.

Ein kommutativer Ring ohne Nullteiler (außer $0$) heißt **Integritätsbereich**. Die Ringe $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$ und $K[x]$ sind Integritätsbereiche; $\mathbb{Z}/6\mathbb{Z}$ ist keiner.

## 3. Ideale und Faktorringe

In $\mathbb{Z}$ ist Teilbarkeit ein zentrales Konzept: $3 \mid 12$, weil $12 = 3 \cdot 4$. Die Menge aller Vielfachen von $3$ bildet eine Teilmenge $3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$ mit besonderen Eigenschaften:

- $3\mathbb{Z}$ ist unter Addition abgeschlossen
- Für jedes $r \in \mathbb{Z}$ und $a \in 3\mathbb{Z}$ ist $ra \in 3\mathbb{Z}$

Diese Eigenschaften definieren ein **Ideal**.

**Definition.** Eine Teilmenge $I \subseteq R$ heißt **Ideal**, wenn:
1. $(I, +)$ ist eine Untergruppe von $(R, +)$
2. Für alle $r \in R$ und $a \in I$ gilt $ra \in I$ und $ar \in I$

Ideale spielen in Ringen dieselbe Rolle wie Normalteiler in Gruppen: Man kann **Faktorringe** bilden:

$$
R/I = \{r + I \mid r \in R\}
$$

**Beispiel:** $\mathbb{Z}/n\mathbb{Z} = \mathbb{Z}/(n)$ ist der Faktorring von $\mathbb{Z}$ nach dem Ideal $(n) = n\mathbb{Z}$.

### Hauptideale und Hauptidealringe

Ein Ideal der Form $(a) = \{ra \mid r \in R\}$ (alle Vielfachen eines Elements) heißt **Hauptideal**. Ein Integritätsbereich, in dem jedes Ideal ein Hauptideal ist, heißt **Hauptidealring** (HIR).

**HIR-Beispiele:** $\mathbb{Z}$, $K[x]$ (Polynome über einem Körper), $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$

**Kein HIR:** $\mathbb{Z}[\sqrt{-5}]$ – hier hat das Ideal $(2, 1 + \sqrt{-5})$ kein erzeugendes Element.

!!! warning "Die Crux bei FLT"
    In einem HIR gilt die eindeutige Primfaktorzerlegung. In $\mathbb{Z}[\zeta_p]$ für allgemeines $p$ ist das **nicht** der Fall – genau hier scheiterte Lamés Beweis und Kummer erfand die Idealtheorie.

## 4. Körper

Ein **Körper** ist ein kommutativer Ring, in dem jedes Element $a \neq 0$ ein multiplikatives Inverses besitzt: Es gibt $a^{-1}$ mit $a \cdot a^{-1} = 1$.

Anders gesagt: In einem Körper kann man addieren, subtrahieren, multiplizieren **und dividieren** (außer durch $0$).

### Die wichtigsten Körper

| Körper | Beschreibung | Eigenschaft |
|--------|-------------|-------------|
| $\mathbb{Q}$ | Rationale Zahlen | kleinster Körper der Charakteristik $0$ |
| $\mathbb{R}$ | Reelle Zahlen | vollständig, geordnet |
| $\mathbb{C}$ | Komplexe Zahlen | algebraisch abgeschlossen |
| $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ | Endlicher Körper mit $p$ Elementen | Charakteristik $p$ |
| $\mathbb{Q}_p$ | $p$-adische Zahlen | Vervollständigung von $\mathbb{Q}$ |

**Warum ist $\mathbb{Z}/p\mathbb{Z}$ ein Körper?** Weil $p$ prim ist: Für $a \not\equiv 0 \pmod{p}$ ist $\gcd(a, p) = 1$, also existiert nach dem erweiterten euklidischen Algorithmus ein $b$ mit $ab \equiv 1 \pmod{p}$. Dagegen ist $\mathbb{Z}/6\mathbb{Z}$ kein Körper (weil $2 \cdot 3 = 0$).

## 5. Körpererweiterungen

Ein **Körpererweiterung** ist ein Paar $K \subseteq L$ von Körpern. Man schreibt $L/K$ und nennt $L$ eine Erweiterung von $K$.

### Algebraische Erweiterungen

Ein Element $\alpha \in L$ heißt **algebraisch** über $K$, wenn es ein Polynom $f \in K[x]$ mit $f(\alpha) = 0$ gibt. Die Erweiterung $L/K$ heißt algebraisch, wenn jedes Element von $L$ algebraisch über $K$ ist.

**Beispiele:**
- $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ – eine Erweiterung vom Grad $2$
- $\mathbb{Q}(i) = \{a + bi \mid a, b \in \mathbb{Q}\}$ – ebenfalls Grad $2$
- $\mathbb{Q}(\zeta_p)$ – der $p$-te **Kreisteilungskörper**, Grad $p - 1$

### Der Grad einer Erweiterung

Der **Grad** $[L : K]$ ist die Dimension von $L$ als $K$-Vektorraum. Er misst, wie „viel größer" $L$ im Vergleich zu $K$ ist.

**Gradformel (Turmsatz).** Für $K \subseteq M \subseteq L$ gilt:

$$
[L : K] = [L : M] \cdot [M : K]
$$

**Beispiel:** $[\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}] = [\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}(\sqrt{2})] \cdot [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2 \cdot 2 = 4$.

### Der algebraische Abschluss

Der **algebraische Abschluss** $\overline{K}$ von $K$ ist der kleinste algebraisch abgeschlossene Körper, der $K$ enthält. Zum Beispiel:

- $\overline{\mathbb{R}} = \mathbb{C}$ (Fundamentalsatz der Algebra)
- $\overline{\mathbb{Q}}$ ist die Menge aller algebraischen Zahlen – abzählbar, aber nicht gleich $\mathbb{C}$

Die **absolute Galois-Gruppe** $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ – die Symmetriegruppe von $\overline{\mathbb{Q}}$ über $\mathbb{Q}$ – ist das zentrale Objekt in Wiles' Beweis.

## 6. Hauptidealringe und eindeutige Faktorisierung

Die **eindeutige Primfaktorzerlegung** (EPZ) besagt: Jedes Element eines Integritätsbereichs lässt sich im Wesentlichen eindeutig als Produkt von Primelementen schreiben. In $\mathbb{Z}$ ist das der Fundamentalsatz der Arithmetik: $60 = 2^2 \cdot 3 \cdot 5$.

**Satz.** In jedem Hauptidealring gilt die EPZ.

Die Kette der Implikationen:

$$
\text{Euklidisch} \implies \text{Hauptidealring} \implies \text{Faktorieller Ring (EPZ)}
$$

### Wo die EPZ versagt

In $\mathbb{Z}[\sqrt{-5}]$ hat man zwei wesentlich verschiedene Faktorisierungen:

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

Hier sind $2$, $3$, $1 + \sqrt{-5}$ und $1 - \sqrt{-5}$ alle irreduzibel, aber das Produkt hat zwei verschiedene Zerlegungen. Die EPZ versagt!

### Kummers Rettung: Ideale faktorisieren

Kummers Einsicht: Auch wenn die EPZ auf **Elementebene** versagt, gilt sie auf **Idealebene** in jedem Dedekind-Ring. Das Ideal $(6) = (2)(3)$ hat eine eindeutige Zerlegung in Primideale:

$$
(6) = (2, 1 + \sqrt{-5})^2 \cdot (3, 1 + \sqrt{-5}) \cdot (3, 1 - \sqrt{-5})
$$

Die **Klassenzahl** $h$ misst, wie weit ein Ring von einem HIR entfernt ist: $h = 1$ genau dann, wenn der Ring ein HIR ist. Für $\mathbb{Z}[\sqrt{-5}]$ ist $h = 2$.

## 7. Warum Ringe und Körper für FLT wichtig sind

Die algebraischen Strukturen dieses Artikels sind der Hintergrund für Wiles' Beweis:

1. **Kreisteilungsringe** $\mathbb{Z}[\zeta_p]$: Kummers Beweis für reguläre Primzahlen nutzt die Idealstruktur dieser Ringe.

2. **Körpererweiterungen**: Die Galois-Theorie operiert auf Körpererweiterungen – sie ist die Brücke zwischen Gleichungen und Gruppen.

3. **Endliche Körper** $\mathbb{F}_p$: Die Reduktion elliptischer Kurven modulo $p$ – das heißt, das Arbeiten über $\mathbb{F}_p$ statt über $\mathbb{Q}$ – liefert die $a_p$-Koeffizienten, die in der $L$-Reihe auftauchen.

4. **Lokale Ringe** und **Deformationsringe**: In Wiles' Beweis sind die Ringe $R$ und $T$ im „$R = T$"-Theorem lokale Ringe, die Familien von Galois-Darstellungen parametrisieren.

Die Ringtheorie liefert die algebraische Infrastruktur, auf der der gesamte Beweis aufbaut.

---

## Weiterführende Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Kap. 3–4
- **Michael Artin**: *Algebra* – Ringe und Körper umfassend behandelt
- **Serge Lang**: *Algebra* – das Standardwerk für Graduierte
