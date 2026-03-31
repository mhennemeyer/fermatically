---
title: "Primzahlen und warum sie reichen"
slug: elementare-zahlentheorie/03-primzahlen-reduktion
series: elementare-zahlentheorie
part: 3
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - fermat
  - primzahlen
  - reduktion
requires: []
---

# Primzahlen und warum sie reichen

!!! abstract "Zusammenfassung"
    Warum es genügt, Fermats letzten Satz nur für Primzahl-Exponenten zu beweisen –
    und wie Kummer und Sophie Germain mit dieser Erkenntnis wichtige Teilerfolge erzielten.

## Voraussetzungen

- [Was ist Fermats letzter Satz?](../01-was-ist-flt/article_de.md)
- [Der Beweis für $n = 4$](../02-beweis-n4/article_de.md)

---

## 1. Die Idee der Reduktion

Fermats letzter Satz behauptet, dass $x^n + y^n = z^n$ für **alle** $n \geq 3$ keine Lösung in positiven ganzen Zahlen hat. Das klingt nach unendlich vielen Fällen – einen für jedes $n$. Doch ein einfaches Argument reduziert die Arbeit drastisch: Es genügt, den Satz für **Primzahl-Exponenten** $p$ zu beweisen.

Die Grundidee: Jede ganze Zahl $n \geq 3$ ist entweder selbst eine Primzahl, oder sie hat einen Primfaktor. Und wenn FLT für einen Exponenten gilt, dann gilt er auch für alle Vielfachen dieses Exponenten.

## 2. Das Reduktionsargument

**Satz.** Wenn FLT für $n = 4$ und für alle ungeraden Primzahlen $p$ gilt, dann gilt FLT für alle $n \geq 3$.

**Beweis.** Sei $n \geq 3$ beliebig. Wir unterscheiden zwei Fälle:

**Fall 1: $n$ ist durch $4$ teilbar.** Dann ist $n = 4k$ für ein $k \geq 1$, und eine Lösung $x^n + y^n = z^n$ wäre gleichbedeutend mit:

$$
(x^k)^4 + (y^k)^4 = (z^k)^4
$$

Das wäre eine Lösung von FLT für $n = 4$ – die es nach Fermats Beweis nicht gibt.

**Fall 2: $n$ hat einen ungeraden Primfaktor $p$.** Dann ist $n = pm$ für ein $m \geq 1$, und eine Lösung $x^n + y^n = z^n$ wäre gleichbedeutend mit:

$$
(x^m)^p + (y^m)^p = (z^m)^p
$$

Das wäre eine Lösung von FLT für den Primexponenten $p$ – die es nach Voraussetzung nicht gibt.

**Fall 3: Es gibt keinen dritten Fall.** Jede ganze Zahl $n \geq 3$ ist entweder durch $4$ teilbar, oder sie hat einen ungeraden Primfaktor (oder beides). Denn die einzigen Zahlen ohne ungeraden Primfaktor sind die Zweierpotenzen $2^k$, und für $k \geq 2$ ist $2^k$ durch $4$ teilbar. $\square$

!!! note "Warum genügt $n = 4$ statt $n = 2$?"
    Die Reduktion funktioniert über Primfaktoren. Die Zahl $n = 4$ ist keine Primzahl, aber sie deckt den Fall der Zweierpotenzen ab: $n = 4, 8, 12, 16, \ldots$ werden alle durch Fall 1 erfasst. Die einzigen verbleibenden Fälle sind die ungeraden Primzahlen $p = 3, 5, 7, 11, 13, \ldots$

## 3. Was bleibt zu tun?

Nach der Reduktion lautet die Aufgabe klar:

$$
\boxed{\text{Zeige: } x^p + y^p = z^p \text{ hat keine Lösung für alle ungeraden Primzahlen } p.}
$$

Zusammen mit Fermats Beweis für $n = 4$ wäre FLT damit vollständig bewiesen. Das klingt nach einer Vereinfachung – und das ist es auch. Statt alle natürlichen Zahlen ab $3$ abzudecken, muss man „nur" die Primzahlen behandeln. Aber es gibt unendlich viele Primzahlen, und einen Fall nach dem anderen abzuarbeiten ist keine Option.

Die Geschichte der Teilbeweise zeigt das Dilemma:

| Zeitraum | Ergebnis | Exponenten |
|----------|----------|------------|
| ca. 1640 | Fermat | $n = 4$ |
| 1770 | Euler | $p = 3$ |
| 1825 | Dirichlet, Legendre | $p = 5$ |
| 1839 | Lamé | $p = 7$ |
| 1847–1857 | Kummer | alle regulären $p$ |
| 1993 | Computer | alle $p \leq 4{,}000{,}000$ |

## 4. Sophie Germains Durchbruch

**Sophie Germain** (1776–1831) erzielte 1823 den ersten Teilerfolg, der unendlich viele Primzahlen gleichzeitig abdeckte. Ihre Idee: Statt direkt $x^p + y^p = z^p$ zu lösen, unterschied sie zwei Fälle:

- **Fall 1**: $p$ teilt keinen der Werte $x$, $y$, $z$ (d.h. $p \nmid xyz$)
- **Fall 2**: $p$ teilt mindestens einen der Werte $x$, $y$, $z$ (d.h. $p \mid xyz$)

**Satz (Sophie Germain).** Sei $p$ eine ungerade Primzahl mit der Eigenschaft, dass $q = 2p + 1$ ebenfalls prim ist. Dann hat $x^p + y^p = z^p$ keine Lösung mit $p \nmid xyz$.

Eine Primzahl $p$ mit der Eigenschaft, dass $2p + 1$ ebenfalls prim ist, heißt **Germain-Primzahl**. Beispiele: $2, 3, 5, 11, 23, 29, 41, 53, 83, 89, \ldots$

Es wird vermutet, dass es unendlich viele Germain-Primzahlen gibt – das ist aber bis heute unbewiesen. Dennoch war Germains Resultat ein konzeptueller Meilenstein: Es war die erste Methode, die systematisch für eine ganze Klasse von Exponenten gleichzeitig funktionierte.

**Die Beweisidee.** Germain nutzt, dass in $\mathbb{Z}/q\mathbb{Z}$ (den ganzen Zahlen modulo $q = 2p + 1$) die $p$-ten Potenzen eine besondere Struktur haben. Wenn $q$ prim ist und $q = 2p + 1$, dann gibt es in $\mathbb{Z}/q\mathbb{Z}$ nur drei $p$-te Potenzen: $0$, $1$ und $-1$. Daraus folgt, dass eine Lösung $x^p + y^p \equiv z^p \pmod{q}$ erzwingt, dass $q$ einen der Werte $x$, $y$, $z$ teilt. Mit weiterer Analyse kann Germain dann den Fall 1 ($p \nmid xyz$) ausschließen.

## 5. Kummers Revolution: Reguläre Primzahlen

**Ernst Eduard Kummer** (1810–1893) ging noch einen entscheidenden Schritt weiter. Seine Arbeit in den 1840er und 1850er Jahren revolutionierte die algebraische Zahlentheorie und lieferte den bis dahin umfassendsten Teilerfolg für FLT.

### Die Idee: Faktorisierung im Kreisteilungskörper

Für eine ungerade Primzahl $p$ sei $\zeta_p = e^{2\pi i/p}$ eine primitive $p$-te Einheitswurzel. Die Gleichung $x^p + y^p = z^p$ lässt sich im Ring $\mathbb{Z}[\zeta_p]$ faktorisieren:

$$
x^p + y^p = \prod_{k=0}^{p-1} (x + \zeta_p^k \, y) = z^p
$$

Wenn in $\mathbb{Z}[\zeta_p]$ die **eindeutige Primfaktorzerlegung** (EPZ) gelten würde, könnte man aus dieser Faktorisierung direkt einen Widerspruch herleiten – ähnlich wie im Beweis für $n = 4$.

### Das Problem: EPZ gilt nicht immer

Lamé glaubte 1847, genau auf diese Weise einen Beweis für FLT gefunden zu haben. Doch Kummer wies darauf hin, dass die EPZ in $\mathbb{Z}[\zeta_p]$ **nicht** für alle Primzahlen gilt. Für $p = 23$ beispielsweise versagt sie – es gibt Elemente mit mehreren wesentlich verschiedenen Faktorisierungen.

### Kummers Lösung: Idealtheorie

Um das Fehlen der EPZ zu kompensieren, führte Kummer die **idealen Zahlen** ein – Vorläufer der modernen **Ideale** in der Ringtheorie. Die Grundidee: Statt Elemente zu faktorisieren, faktorisiert man *Ideale*. Und für Ideale gilt die EPZ **immer** (in Dedekind-Ringen).

Das Maß für das Versagen der EPZ auf Elementebene ist die **Klassenzahl** $h_p$ des Kreisteilungskörpers $\mathbb{Q}(\zeta_p)$. Es gilt: $h_p = 1$ genau dann, wenn EPZ in $\mathbb{Z}[\zeta_p]$ gilt.

### Reguläre Primzahlen

Kummer nannte eine Primzahl $p$ **regulär**, wenn $p$ die Klassenzahl $h_p$ nicht teilt: $p \nmid h_p$.

**Satz (Kummer, 1850).** Wenn $p$ eine reguläre Primzahl ist, dann hat $x^p + y^p = z^p$ keine Lösung in positiven ganzen Zahlen.

**Beispiele regulärer Primzahlen:** $3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, \ldots$

**Irreguläre Primzahlen (bis 100):** $37, 59, 67$

Kummers Methode bewies FLT also für die meisten kleinen Primzahlen – aber nicht für alle. Die irregulären Primzahlen erwiesen sich als hartnäckige Ausnahmen.

!!! note "Wie häufig sind reguläre Primzahlen?"
    Heuristische Argumente legen nahe, dass etwa $e^{-1/2} \approx 60{,}6\%$ aller Primzahlen regulär sind. Es wird vermutet, dass es unendlich viele reguläre (und unendlich viele irreguläre) Primzahlen gibt – bewiesen ist beides nicht.

## 6. Die Grenzen elementarer Methoden

Die Geschichte der Teilbeweise macht ein Muster deutlich: Jeder neue Fall erforderte tiefere Werkzeuge.

- **$n = 4$**: Elementarer Abstieg in $\mathbb{Z}$ (Fermat)
- **$n = 3$**: Abstieg in $\mathbb{Z}[\omega]$ – Einstieg in die algebraische Zahlentheorie (Euler)
- **$n = 5, 7$**: Aufwendige Fallunterscheidungen in Kreisteilungskörpern (Dirichlet, Legendre, Lamé)
- **Reguläre $p$**: Idealtheorie und Klassenzahlen (Kummer)
- **Alle $p$**: ???

Kummers Methode stieß an eine fundamentale Grenze: Die Klassenzahl $h_p$ wächst mit $p$, und es gibt keinen allgemeinen Weg, die Regularität zu erzwingen. Nach Kummer war klar, dass ein völlig neuer Ansatz nötig sein würde – einer, der nicht mehr Fall für Fall argumentiert, sondern die Gleichung $x^p + y^p = z^p$ für *alle* $p$ gleichzeitig behandelt.

Dieser Ansatz kam schließlich über einen Umweg, der erst 100 Jahre später klar wurde: die Verbindung zwischen elliptischen Kurven und Modulformen. Aber bevor wir dorthin gelangen, müssen wir zuerst den Beweis für $n = 3$ verstehen – und sehen, was passiert, wenn man den Zahlbereich erstmals erweitert.

---

## Weiterführende Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Kap. 1–2
- **Harold Edwards**: *Fermat's Last Theorem* – detaillierte Darstellung von Kummers Arbeit
- **Paulo Ribenboim**: *Fermat's Last Theorem for Amateurs* – zugängliche Übersicht der Teilbeweise
