---
title: "Die Taniyama-Shimura-Vermutung"
slug: fermat-wiles/01-taniyama-shimura
series: fermat-wiles
part: 1
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - taniyama-shimura
  - modularitaet
  - vermutung
requires:
  - elliptische-kurven/01-elliptische-kurven
  - modulformen/01-modulformen
---
# Die Taniyama-Shimura-Vermutung

!!! abstract "Zusammenfassung"
    Die Taniyama-Shimura-Vermutung behauptet, dass jede elliptische Kurve
    über $\mathbb{Q}$ modular ist – dass also die $L$-Reihe jeder solchen Kurve
    mit der $L$-Reihe einer Modulform übereinstimmt. Diese Brücke zwischen
    Geometrie und Analysis ist der Schlüssel zu Wiles' Beweis von Fermats
    letztem Satz.

## Voraussetzungen

- [Elliptische Kurven](../werkzeuge/elliptische-kurven.md) – Grundbegriffe: Weierstraß-Gleichung, Gruppenstruktur, Reduktion modulo $p$
- [Modulformen](../werkzeuge/modulformen.md) – Modulformen, Neuformen, $q$-Entwicklung, Hecke-Operatoren

---

## 1. Zwei getrennte Welten

Die Mathematik des 20. Jahrhunderts kannte zwei scheinbar unabhängige Gebiete, die beide eine tiefe Struktur besaßen – aber auf den ersten Blick nichts miteinander zu tun hatten.

### Die Welt der elliptischen Kurven

Eine **elliptische Kurve** über $\mathbb{Q}$ ist (vereinfacht) die Lösungsmenge einer Gleichung der Form

$$
E: \quad y^2 = x^3 + ax + b, \qquad a, b \in \mathbb{Q}, \quad 4a^3 + 27b^2 \neq 0.
$$

Sie lebt in der **algebraischen Geometrie** und der **Zahlentheorie**: Man untersucht ihre rationalen Punkte, ihre Struktur als abelsche Gruppe, ihre Reduktion modulo Primzahlen. Für jede Primzahl $p$ zählt man die Punkte der reduzierten Kurve über $\mathbb{F}_p$ und definiert

$$
a_p(E) = p - \#E(\mathbb{F}_p),
$$

wobei $\#E(\mathbb{F}_p)$ die Anzahl der Punkte (inklusive des Punkts im Unendlichen) auf der reduzierten Kurve ist. Diese Zahlen $a_p$ kodieren die **lokale Arithmetik** der Kurve bei jeder Primzahl.

### Die Welt der Modulformen

Eine **Modulform** vom Gewicht $k$ und Stufe $N$ ist eine holomorphe Funktion

$$
f: \mathcal{H} \to \mathbb{C}
$$

auf der oberen Halbebene $\mathcal{H} = \{z \in \mathbb{C} : \text{Im}(z) > 0\}$, die sich unter der Wirkung der Kongruenzuntergruppe $\Gamma_0(N) \subset \text{SL}_2(\mathbb{Z})$ in einer bestimmten Weise transformiert. Sie lebt in der **komplexen Analysis** und hat eine Fourier-Entwicklung (auch **$q$-Entwicklung** genannt):

$$
f(z) = \sum_{n=0}^{\infty} b_n q^n, \qquad q = e^{2\pi i z}.
$$

Die Koeffizienten $b_n$ kodieren die Struktur der Modulform. Besonders wichtig sind die **Neuformen** – normalisierte Hecke-Eigenformen, die „irreduzibel" sind in dem Sinne, dass sie nicht von niedrigerer Stufe kommen.

### Warum getrennt?

Elliptische Kurven gehören zur algebraischen Geometrie und Zahlentheorie. Modulformen gehören zur komplexen Analysis und Darstellungstheorie. Ihre Werkzeuge, ihre Intuitionen, ihre Fachsprachen – alles scheint verschieden. Dass zwischen diesen Welten eine tiefe Verbindung bestehen könnte, war bis Mitte des 20. Jahrhunderts kaum vorstellbar.

---

## 2. Die $L$-Reihen-Brücke

Der Schlüssel zur Verbindung liegt in den **$L$-Reihen** – analytischen Objekten, die beide Welten mit einer gemeinsamen Sprache versehen.

### Die $L$-Reihe einer elliptischen Kurve

Für eine elliptische Kurve $E/\mathbb{Q}$ definiert man die **$L$-Reihe** als Euler-Produkt:

$$
L(E, s) = \prod_{p \text{ prim}} L_p(E, s)^{-1},
$$

wobei die lokalen Faktoren für Primzahlen guter Reduktion die Form haben:

$$
L_p(E, s) = 1 - a_p p^{-s} + p^{1-2s}.
$$

Die $a_p$ sind genau die oben definierten Punktezähl-Koeffizienten. Für endlich viele Primzahlen schlechter Reduktion (die den **Konduktor** $N_E$ von $E$ bilden) ist der lokale Faktor einfacher.

### Die $L$-Reihe einer Modulform

Für eine Neuform $f = \sum b_n q^n$ vom Gewicht 2 und Stufe $N$ definiert man analog:

$$
L(f, s) = \sum_{n=1}^{\infty} b_n n^{-s} = \prod_{p \text{ prim}} \left(1 - b_p p^{-s} + p^{1-2s}\right)^{-1}.
$$

### Die Brücke

Die zentrale Beobachtung ist: Beide $L$-Reihen haben exakt dieselbe Struktur. Wenn es eine Neuform $f$ vom Gewicht 2 gibt mit

$$
a_p(E) = b_p(f) \quad \text{für (fast) alle Primzahlen } p,
$$

dann stimmen die $L$-Reihen überein: $L(E, s) = L(f, s)$. In diesem Fall sagt man: **$E$ ist modular**, und $f$ ist die zu $E$ gehörige Modulform.

---

## 3. Taniyama und Shimura – Die Vermutung und ihre Geschichte

### Das Symposium von Tokio (1955)

Im September 1955 fand in Tokio ein internationales Symposium über algebraische Zahlentheorie statt. Dort formulierte **Yutaka Taniyama** (1927–1958) eine Reihe von Problemen, die eine Verbindung zwischen elliptischen Kurven und Modulformen andeuteten. Die Fragen waren zunächst vage formuliert, aber der Kern war klar: Die $L$-Reihen elliptischer Kurven sollten mit denen von Modulformen übereinstimmen.

Taniyamas Kollege **Goro Shimura** (1930–2019) präzisierte die Vermutung in den folgenden Jahren und untermauerte sie mit Berechnungen und theoretischen Argumenten. In der westlichen Literatur wurde die Vermutung daher oft als **Taniyama-Shimura-Vermutung** (TSV) bezeichnet, manchmal auch als Taniyama-Shimura-Weil-Vermutung, da André Weil einen wichtigen Beitrag zur Präzisierung leistete.

Taniyama starb 1958 im Alter von 31 Jahren. Seine mathematische Vision überlebte ihn und wurde zu einer der einflussreichsten Vermutungen des 20. Jahrhunderts.

> „I do not deny that there is an element of mystery in the conjecture [...] but I think, at the time, it was just a guess."
> — Goro Shimura, zitiert in Singh, *Fermat's Last Theorem* (1997), S. 174

### Die Vermutung, präzise formuliert

!!! note "Taniyama-Shimura-Vermutung (Modularitätsvermutung)"
    Jede elliptische Kurve $E$ über $\mathbb{Q}$ ist **modular**: Es existiert eine
    Neuform $f$ vom Gewicht 2 und Stufe $N_E$ (dem Konduktor von $E$) mit
    $$
    L(E, s) = L(f, s).
    $$
    Äquivalent: $a_p(E) = b_p(f)$ für alle Primzahlen $p$ guter Reduktion.

### Warum glaubte man daran?

Zunächst gab es **numerische Evidenz**: Für viele explizit berechnete elliptische Kurven ließen sich passende Modulformen finden, und die Koeffizienten stimmten überein – so weit man rechnen konnte.

Dann gab es **strukturelle Argumente**: Die funktionalgleichung der $L$-Reihe einer modularen Form war bekannt. Wenn die $L$-Reihe einer elliptischen Kurve dieselbe Funktionalgleichung erfüllt (was durch die Arbeit von Weil nahegelegt wurde), dann liegt ein Zusammenhang nahe.

Schließlich gab es die **philosophische Überzeugung**, die dem Langlands-Programm zugrunde liegt: Zwischen automorphen Formen (zu denen Modulformen gehören) und Galois-Darstellungen (die elliptische Kurven liefern) sollte eine systematische Korrespondenz bestehen.

---

## 4. Was „modular" bedeutet – Ein Beispiel

Gegeben die elliptische Kurve

$$
E: \quad y^2 = x^3 - x.
$$

Diese Kurve hat **Konduktor** $N_E = 32$. Die Koeffizienten $a_p$ ergeben sich durch Punktezählung modulo kleiner Primzahlen:

| $p$ | $\#E(\mathbb{F}_p)$ | $a_p = p - \#E(\mathbb{F}_p)$ |
|-----|---------------------|-------------------------------|
| 3   | 4                   | $-1$                          |
| 5   | 4                   | $1$                           |
| 7   | 8                   | $-1$                          |
| 11  | 12                  | $-1$                          |
| 13  | 12                  | $1$                           |

Die zugehörige Modulform $f$ vom Gewicht 2 und Stufe 32 ist eindeutig bestimmt. Ihre $q$-Entwicklung beginnt mit:

$$
f(q) = q - q^3 + q^5 - q^7 - q^{11} + q^{13} + \cdots
$$

Die Koeffizienten $b_3 = -1$, $b_5 = 1$, $b_7 = -1$, $b_{11} = -1$, $b_{13} = 1$ stimmen exakt mit den $a_p$ überein. Die Kurve $y^2 = x^3 - x$ **ist modular**.

Dieses Beispiel illustriert die Vermutung konkret: Die arithmetische Information der Kurve (Punktezählung über endlichen Körpern) wird exakt von einem analytischen Objekt (einer Modulform) widergespiegelt.

---

## 5. Warum die TSV so mächtig ist

Die Taniyama-Shimura-Vermutung ist nicht einfach eine Beobachtung über einzelne Beispiele – sie ist eine **universelle Aussage** über alle elliptischen Kurven über $\mathbb{Q}$:

### Unendlich viele Kurven, eine Vermutung

Es gibt unendlich viele nicht-isomorphe elliptische Kurven über $\mathbb{Q}$, parametrisiert durch die Koeffizienten $a$ und $b$. Für **jede einzelne** behauptet die TSV die Existenz einer passenden Modulform.

### Von Geometrie zu Analysis

Die TSV übersetzt ein **geometrisch-arithmetisches** Problem (Struktur einer elliptischen Kurve) in ein **analytisches** Problem (Existenz einer Modulform). Da Modulformen gut verstandene Objekte sind – mit reicher Theorie der Hecke-Operatoren, $L$-Reihen und Funktionalgleichungen –, erschließt die Modularität einer Kurve sofort eine Fülle analytischer Werkzeuge.

### Konsequenzen der Modularität

Wenn $E$ modular ist, folgt automatisch:

1. **Analytische Fortsetzung**: $L(E, s)$ lässt sich auf ganz $\mathbb{C}$ analytisch fortsetzen.
2. **Funktionalgleichung**: $L(E, s)$ erfüllt eine Funktionalgleichung, die $s$ und $2-s$ verbindet.
3. **BSD-Vermutung**: Die Ordnung der Nullstelle von $L(E, s)$ bei $s = 1$ sollte gleich dem Rang von $E(\mathbb{Q})$ sein (Birch und Swinnerton-Dyer).

Vor Wiles' Beweis war selbst die analytische Fortsetzung von $L(E, s)$ nur für einzelne Kurven bekannt – nicht für alle.

---

## 6. Die semistabile Version

### Semistabile elliptische Kurven

Eine elliptische Kurve $E/\mathbb{Q}$ heißt **semistabil**, wenn sie bei jeder Primzahl $p$ entweder gute oder **multiplikative** (nicht additive) Reduktion hat. Geometrisch bedeutet das: Bei schlechter Reduktion hat die Kurve höchstens einen gewöhnlichen Doppelpunkt (eine „Selbstkreuzung"), aber keinen Rückkehrpunkt.

Die Klasse der semistabilen Kurven ist groß genug, um die **Frey-Kurve** zu enthalten – das ist entscheidend für die Anwendung auf Fermats letzten Satz.

### Wiles' Theorem (1995)

!!! note "Theorem (Wiles, Taylor-Wiles, 1995)"
    Jede **semistabile** elliptische Kurve über $\mathbb{Q}$ ist modular.

Andrew Wiles bewies diese Aussage in seiner bahnbrechenden Arbeit *„Modular elliptic curves and Fermat's Last Theorem"* (Annals of Mathematics, 1995), zusammen mit dem ergänzenden Artikel von Richard Taylor und Andrew Wiles.

Der Beweis der **vollständigen** Taniyama-Shimura-Vermutung – für alle elliptischen Kurven, nicht nur die semistabilen – gelang erst 2001 durch **Breuil, Conrad, Diamond und Taylor**, aufbauend auf Wiles' Methoden.

### Warum reicht die semistabile Version für FLT?

Die Frey-Kurve, die aus einer hypothetischen FLT-Lösung konstruiert wird, ist semistabil. Daher genügt die semistabile Version der TSV, um Fermats letzten Satz zu beweisen – mehr war nicht nötig. Die Details dieser Reduktion sind Gegenstand des [nächsten Artikels](02-frey-ribet.md).

---

## 7. Von TSV zu FLT – Vorschau auf Freys Argument

Die logische Kette von der TSV zu Fermats letztem Satz lässt sich knapp so zusammenfassen:

**Angenommen**, es gäbe eine nichttriviale Lösung $a^p + b^p = c^p$ für eine Primzahl $p \geq 5$.

1. **Frey (1985)**: Konstruiere die elliptische Kurve $E: y^2 = x(x - a^p)(x + b^p)$.
2. **Frey/Serre**: Diese Kurve ist semistabil, hat aber eine so extreme Diskriminante, dass sie „zu exotisch" ist, um modular zu sein.
3. **Ribet (1986)**: Beweist, dass $E$ tatsächlich nicht modular sein kann (Level-Lowering-Theorem).
4. **Wiles (1995)**: Beweist, dass jede semistabile Kurve modular ist.
5. **Widerspruch**: $E$ ist semistabil (also modular nach Wiles), aber nicht modular (nach Ribet). Also kann die Lösung nicht existieren.

$$
\boxed{\text{FLT-Lösung} \xrightarrow{\text{Frey}} E \xrightarrow{\text{Ribet}} \text{nicht modular} \xleftarrow{\text{Widerspruch}} \xrightarrow{\text{Wiles}} \text{modular}}
$$

Dieser Widerspruchsbeweis – der eine Vermutung aus der Zahlentheorie über algebraische Geometrie und komplexe Analysis beweist – verbindet drei zentrale Gebiete der modernen Mathematik.

---

## Ausblick

Dieser Artikel hat die Taniyama-Shimura-Vermutung als Verbindung zwischen elliptischen Kurven und Modulformen dargestellt. Die folgenden Artikel vertiefen die einzelnen Schritte:

| Artikel | Thema |
|---------|-------|
| [02 – Freys Idee und Ribets Theorem](02-frey-ribet.md) | Wie eine FLT-Lösung zur „unmöglichen" Frey-Kurve führt |
| [03 – Galois-Darstellungen](03-galois-darstellungen.md) | Wie Wiles Modularität in die Sprache der Darstellungen übersetzt |

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 8 – Modularität und die TSV
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1–2
- **Fred Diamond, Jerry Shurman**: *A First Course in Modular Forms*, Springer (2005) – Ausführliche Darstellung der TSV und ihrer Beweise
- **Barry Mazur**: *Number Theory as Gadfly*, The American Mathematical Monthly 98 (1991) – Motivation der Vermutung
