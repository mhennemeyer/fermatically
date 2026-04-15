---
title: "Was ist ein Beweis?"
description: "Axiome, Definitionen, Sätze und Lemmata – die Bausteine mathematischer Argumentation"
lang: de
type: vorwissen
---

# Was ist ein Beweis?

## Definition

Ein **mathematischer Beweis** ist eine lückenlose Kette logischer Schlüsse, die eine Behauptung aus bereits akzeptierten Aussagen (Axiomen, Definitionen, zuvor bewiesenen Sätzen) herleitet.

Ein Beweis ist keine empirische Überprüfung. Dass eine Aussage für tausend Beispiele gilt, beweist sie nicht. Ein Beweis zeigt, dass sie für **alle** zulässigen Fälle gilt.

## Die Bausteine

### Axiome

**Axiome** sind Grundannahmen, die ohne Beweis akzeptiert werden. Sie bilden das Fundament eines mathematischen Systems.

**Beispiel.** Peano-Axiome für die natürlichen Zahlen:
- $0$ ist eine natürliche Zahl.
- Jede natürliche Zahl $n$ hat einen Nachfolger $S(n)$.
- $0$ ist kein Nachfolger einer natürlichen Zahl.

### Definitionen

**Definitionen** legen die Bedeutung eines Begriffs fest. Sie sind weder wahr noch falsch – sie sind Festlegungen.

**Beispiel.** *Definition:* Eine natürliche Zahl $p > 1$ heißt **Primzahl**, wenn ihre einzigen positiven Teiler $1$ und $p$ sind.

### Sätze (Theoreme)

Ein **Satz** (oder **Theorem**) ist eine mathematische Aussage, die bewiesen wurde.

**Beispiel.** *Fundamentalsatz der Arithmetik:* Jede natürliche Zahl $n > 1$ lässt sich eindeutig als Produkt von Primzahlen darstellen (bis auf die Reihenfolge der Faktoren).

### Lemmata

Ein **Lemma** ist ein Hilfssatz – ein bewiesener Satz, der primär als Zwischenschritt für einen größeren Beweis dient.

**Beispiel.** *Lemma von Bézout:* Für $a, b \in \mathbb{Z}$ existieren $x, y \in \mathbb{Z}$ mit $\gcd(a, b) = xa + yb$.

### Korollare

Ein **Korollar** ist eine direkte Folgerung aus einem bereits bewiesenen Satz.

**Beispiel.** *Korollar:* Sind $a$ und $b$ teilerfremd und $a \mid bc$, dann $a \mid c$. (Folgt aus dem Lemma von Bézout.)

## Vermutung vs. Satz

| Begriff | Status | Beispiel |
|---------|--------|----------|
| **Vermutung** | Unbewiesene Aussage, für die es Evidenz gibt | Goldbachsche Vermutung (1742, offen) |
| **Satz** | Bewiesene Aussage | Fermats letzter Satz (1637 formuliert, 1995 bewiesen) |

Eine Vermutung wird zum Satz, sobald ein gültiger Beweis vorliegt. „Fermats letzter Satz" heißt historisch „Satz", obwohl er 358 Jahre lang eine Vermutung war.

## Struktur eines Beweises

Ein typischer Beweis folgt diesem Schema:

1. **Voraussetzung:** Was wird angenommen?
2. **Behauptung:** Was soll gezeigt werden?
3. **Beweis:** Logische Kette von der Voraussetzung zur Behauptung.
4. **QED / $\square$:** Markierung des Beweisendes.

**Beispiel.**

*Voraussetzung:* $a$ und $b$ sind gerade Zahlen.

*Behauptung:* $a \cdot b$ ist durch 4 teilbar.

*Beweis.* Da $a$ gerade ist, existiert $m \in \mathbb{Z}$ mit $a = 2m$. Da $b$ gerade ist, existiert $n \in \mathbb{Z}$ mit $b = 2n$. Dann:

$$
a \cdot b = 2m \cdot 2n = 4mn
$$

Da $mn \in \mathbb{Z}$, ist $a \cdot b$ durch 4 teilbar. $\square$

---

## Zusammenfassung

| Baustein | Rolle |
|----------|-------|
| Axiom | Grundannahme ohne Beweis |
| Definition | Festlegung eines Begriffs |
| Satz/Theorem | Bewiesene Aussage |
| Lemma | Hilfssatz für größeren Beweis |
| Korollar | Direkte Folgerung aus einem Satz |
| Vermutung | Unbewiesene Aussage mit Evidenz |

## Quellen

- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3. Auflage, 2019. Kapitel 1.
- Hammack, Richard: *Book of Proof.* 3. Auflage, 2018. Kapitel 1.
