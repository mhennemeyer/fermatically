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
  - mengen
  - abbildungen
  - gleichungen
  - teilbarkeit-ggt
  - primfaktorzerlegung
  - komplexe-zahlen
  - relationen-aequivalenzklassen
---

# Ringe und Körper

!!! abstract "Zusammenfassung"
    Von Gruppen (eine Verknüpfung) zu Ringen (zwei Verknüpfungen) und Körpern (mit Division).
    Idealtheorie als Antwort auf das Versagen der eindeutigen Faktorisierung.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](../../gruppen-und-symmetrie/01-gruppen/article_de.md)

| Thema | Beschreibung |
|-------|-------------|
| [Mengen und Mengenoperationen](../../vorwissen/mengen/article_de.md) | Mengennotation, $\cup, \cap, \setminus, \times$ |
| [Abbildungen (Funktionen)](../../vorwissen/abbildungen/article_de.md) | $f: A \to B$, injektiv, surjektiv, bijektiv |
| [Gleichungen](../../vorwissen/gleichungen/article_de.md) | Äquivalente Umformungen und Lösungsstrategien |
| [Teilbarkeit und ggT](../../vorwissen/teilbarkeit-ggt/article_de.md) | Teilerfremdheit, $\gcd$, Euklidischer Algorithmus |
| [Primfaktorzerlegung](../../vorwissen/primfaktorzerlegung/article_de.md) | Eindeutige Zerlegung in Primfaktoren (Fundamentalsatz der Arithmetik) |
| [Komplexe Zahlen](../../vorwissen/komplexe-zahlen/article_de.md) | Zahlen $a + bi$ mit $i^2 = -1$, Polarform, Einheitswurzeln |
| [Relationen und Äquivalenzklassen](../../vorwissen/relationen-aequivalenzklassen/article_de.md) | Äquivalenzrelationen, Restklassen, Quotientenmengen |

---

## 1. Von Gruppen zu Ringen

In einer Gruppe gibt es *eine* Verknüpfung. Die ganzen Zahlen $\mathbb{Z}$ besitzen jedoch *zwei*: Addition und Multiplikation. Um beide gleichzeitig zu erfassen, ist eine reichere Struktur nötig – der **Ring**.

Die Motivation stammt direkt aus der Zahlentheorie: Die Beweise von FLT für $n = 3$ und $n = 4$ zeigten, dass der Zahlbereich erweitert werden muss – auf $\mathbb{Z}[\omega]$ oder $\mathbb{Z}[i]$. All diese Zahlbereiche sind Ringe.

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

In $\mathbb{Z}$ gilt: Wenn $ab = 0$, dann $a = 0$ oder $b = 0$. Diese Eigenschaft gilt nicht in allen Ringen. In $\mathbb{Z}/6\mathbb{Z}$ ist $2 \cdot 3 = 6 \equiv 0$, obwohl weder $2$ noch $3$ null sind. Solche Elemente heißen **Nullteiler**.

Ein kommutativer Ring ohne Nullteiler (außer $0$) heißt **Integritätsbereich**. Die Ringe $\mathbb{Z}$, $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$ und $K[x]$ sind Integritätsbereiche; $\mathbb{Z}/6\mathbb{Z}$ ist keiner.

## 3. Ideale und Faktorringe

In $\mathbb{Z}$ ist Teilbarkeit ein zentrales Konzept: $3 \mid 12$, weil $12 = 3 \cdot 4$. Die Menge aller Vielfachen von $3$ bildet eine Teilmenge $3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$ mit besonderen Eigenschaften:

- $3\mathbb{Z}$ ist unter Addition abgeschlossen
- Für jedes $r \in \mathbb{Z}$ und $a \in 3\mathbb{Z}$ ist $ra \in 3\mathbb{Z}$

Diese Eigenschaften definieren ein **Ideal**.

**Definition.** Eine Teilmenge $I \subseteq R$ heißt **Ideal**, wenn:
1. $(I, +)$ ist eine Untergruppe von $(R, +)$
2. Für alle $r \in R$ und $a \in I$ gilt $ra \in I$ und $ar \in I$

Ideale spielen in Ringen dieselbe Rolle wie Normalteiler in Gruppen: Sie ermöglichen die Bildung von **Faktorrringen**:

$$
R/I = \{r + I \mid r \in R\}
$$

**Beispiel:** $\mathbb{Z}/n\mathbb{Z} = \mathbb{Z}/(n)$ ist der Faktorring von $\mathbb{Z}$ nach dem Ideal $(n) = n\mathbb{Z}$.

### Hauptideale und Hauptidealringe

Ein Ideal der Form $(a) = \{ra \mid r \in R\}$ (alle Vielfachen eines Elements) heißt **Hauptideal**. Ein Integritätsbereich, in dem jedes Ideal ein Hauptideal ist, heißt **Hauptidealring** (HIR).

**HIR-Beispiele:** $\mathbb{Z}$, $K[x]$ (Polynome über einem Körper), $\mathbb{Z}[i]$, $\mathbb{Z}[\omega]$

**Kein HIR:** $\mathbb{Z}[\sqrt{-5}]$ – das Ideal $(2, 1 + \sqrt{-5})$ hat kein erzeugendes Element.

> „The notion of an ideal [...] is the key to the whole of algebraic number theory."
> — Serge Lang, *Algebra* (2002), Kapitel II

!!! warning "Die Crux bei FLT"
    In einem HIR gilt die eindeutige Primfaktorzerlegung. In $\mathbb{Z}[\zeta_p]$ für allgemeines $p$ ist das **nicht** der Fall – genau hier scheiterte Lamés Beweis und Kummer entwickelte die Idealtheorie.

## 4. Körper

Ein **Körper** ist ein kommutativer Ring, in dem jedes Element $a \neq 0$ ein multiplikatives Inverses besitzt: Es gibt $a^{-1}$ mit $a \cdot a^{-1} = 1$.

In einem Körper sind Addition, Subtraktion, Multiplikation **und Division** (außer durch $0$) möglich.

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

Eine **Körpererweiterung** ist ein Paar $K \subseteq L$ von Körpern. Notation: $L/K$. $L$ heißt Erweiterung von $K$.

### Algebraische Erweiterungen

Ein Element $\alpha \in L$ heißt **algebraisch** über $K$, wenn ein Polynom $f \in K[x]$ mit $f(\alpha) = 0$ existiert. Die Erweiterung $L/K$ heißt algebraisch, wenn jedes Element von $L$ algebraisch über $K$ ist.

**Beispiele:**
- $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ – Erweiterung vom Grad $2$
- $\mathbb{Q}(i) = \{a + bi \mid a, b \in \mathbb{Q}\}$ – ebenfalls Grad $2$
- $\mathbb{Q}(\zeta_p)$ – der $p$-te **Kreisteilungskörper**, Grad $p - 1$

### Der Grad einer Erweiterung

Der **Grad** $[L : K]$ ist die Dimension von $L$ als $K$-Vektorraum. Er quantifiziert den „Abstand" zwischen $L$ und $K$.

**Gradformel (Turmsatz).** Für $K \subseteq M \subseteq L$ gilt:

$$
[L : K] = [L : M] \cdot [M : K]
$$

**Beispiel:** $[\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}] = [\mathbb{Q}(\sqrt{2}, \sqrt{3}) : \mathbb{Q}(\sqrt{2})] \cdot [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2 \cdot 2 = 4$.

### Der algebraische Abschluss

Der **algebraische Abschluss** $\overline{K}$ von $K$ ist der kleinste algebraisch abgeschlossene Körper, der $K$ enthält:

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

In $\mathbb{Z}[\sqrt{-5}]$ existieren zwei wesentlich verschiedene Faktorisierungen:

$$
6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})
$$

Die Elemente $2$, $3$, $1 + \sqrt{-5}$ und $1 - \sqrt{-5}$ sind alle irreduzibel, aber das Produkt hat zwei verschiedene Zerlegungen. Die EPZ versagt.

### Kummers Lösung: Ideale faktorisieren

Kummers Einsicht: Auch wenn die EPZ auf **Elementebene** versagt, gilt sie auf **Idealebene** in jedem Dedekind-Ring. Das Ideal $(6)$ hat eine eindeutige Zerlegung in Primideale:

$$
(6) = (2, 1 + \sqrt{-5})^2 \cdot (3, 1 + \sqrt{-5}) \cdot (3, 1 - \sqrt{-5})
$$

Die **Klassenzahl** $h$ misst, wie weit ein Ring von einem HIR entfernt ist: $h = 1$ genau dann, wenn der Ring ein HIR ist. Für $\mathbb{Z}[\sqrt{-5}]$ ist $h = 2$.

> „Kummer's theory of ideal numbers is rightly considered as one of the great achievements of nineteenth century mathematics."
> — Harold M. Edwards, *Fermat's Last Theorem* (1977), S. 76

## 7. Ringe und Körper im Kontext von FLT

Die algebraischen Strukturen dieses Artikels bilden den Hintergrund für Wiles' Beweis:

1. **Kreisteilungsringe** $\mathbb{Z}[\zeta_p]$: Kummers Beweis für reguläre Primzahlen nutzt die Idealstruktur dieser Ringe.

2. **Körpererweiterungen**: Die Galois-Theorie operiert auf Körpererweiterungen – die Brücke zwischen Gleichungen und Gruppen.

3. **Endliche Körper** $\mathbb{F}_p$: Die Reduktion elliptischer Kurven modulo $p$ – das Arbeiten über $\mathbb{F}_p$ statt über $\mathbb{Q}$ – liefert die $a_p$-Koeffizienten der $L$-Reihe.

4. **Lokale Ringe** und **Deformationsringe**: Die Ringe $R$ und $T$ im „$R = T$"-Theorem sind lokale Ringe, die Familien von Galois-Darstellungen parametrisieren.

Die Ringtheorie liefert die algebraische Infrastruktur, auf der der gesamte Beweis aufbaut.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 3–4
- **Harold M. Edwards**: *Fermat's Last Theorem: A Genetic Introduction to Algebraic Number Theory*, Springer (1977)
- **Michael Artin**: *Algebra*, Prentice Hall (1991)
- **Serge Lang**: *Algebra*, Springer (2002)
