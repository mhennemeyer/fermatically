---
title: "Freys Idee und Ribets Theorem"
slug: fermat-wiles/02-frey-ribet
series: fermat-wiles
part: 2
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - frey-kurve
  - ribet
  - level-lowering
requires:
  - fermat-wiles/01-taniyama-shimura
  - elliptische-kurven/01-elliptische-kurven
---
# Freys Idee und Ribets Theorem

!!! abstract "Zusammenfassung"
    Gerhard Frey erkannte 1985, dass eine hypothetische Lösung von Fermats
    letztem Satz zu einer elliptischen Kurve mit so extremen Eigenschaften führt,
    dass sie nicht modular sein kann. Kenneth Ribet bewies 1986, dass diese
    Intuition korrekt ist. Damit war FLT auf die Taniyama-Shimura-Vermutung
    reduziert.

## Voraussetzungen

- [Die Taniyama-Shimura-Vermutung](../01-taniyama-shimura/article_de.md) – Modularität, $L$-Reihen, semistabile Kurven
- [Elliptische Kurven](../../elliptische-kurven/01-elliptische-kurven/article_de.md) – Weierstraß-Form, Diskriminante, Konduktor

---

## 1. Freys Geistesblitz (1985)

### Die entscheidende Frage

Nach Jahrhunderten direkter Angriffe auf Fermats letzten Satz – Beweis für $n = 4$ (Fermat), $n = 3$ (Euler), $n = 5$ (Dirichlet/Legendre), und so weiter – kam 1985 eine völlig neue Idee aus einer unerwarteten Richtung.

**Gerhard Frey**, ein deutscher Mathematiker an der Universität des Saarlandes, stellte folgende Frage: Was wäre, wenn man eine hypothetische FLT-Lösung nicht direkt widerlegen müsste, sondern stattdessen zeigen könnte, dass sie zu einem **Widerspruch** mit einer anderen bekannten (oder vermuteten) Tatsache führt?

### Der Ansatz

Frey nahm an, es gäbe eine nichttriviale Lösung der Fermat-Gleichung für eine Primzahl $p \geq 5$:

$$
a^p + b^p = c^p, \qquad a, b, c \in \mathbb{Z}, \quad abc \neq 0.
$$

Ohne Einschränkung der Allgemeinheit kann man annehmen:

- $\gcd(a, b, c) = 1$ (die Lösung ist primitiv)
- $a \equiv -1 \pmod{4}$ und $2 \mid b$ (durch geeignete Vorzeichen- und Vertauschungswahl)

Aus diesen drei Zahlen konstruierte Frey eine elliptische Kurve – und diese Kurve sollte sich als der Schlüssel zum gesamten Beweis herausstellen.

---

## 2. Die Frey-Kurve

### Konstruktion

Aus der hypothetischen Lösung $a^p + b^p = c^p$ definiert Frey die elliptische Kurve:

$$
E_{a,b,c}: \quad y^2 = x(x - a^p)(x + b^p).
$$

Diese Kurve ist in **Weierstraß-Form** (nach einer einfachen Variablensubstitution) und hat drei offensichtliche 2-Torsionspunkte: $(0, 0)$, $(a^p, 0)$ und $(-b^p, 0)$.

### Die Diskriminante

Die **minimale Diskriminante** der Frey-Kurve ist (bis auf Potenzen von 2):

$$
\Delta = \frac{(abc)^{2p}}{2^8}.
$$

Dies ist eine außergewöhnlich große Diskriminante – viel größer als bei „normalen" elliptischen Kurven. Der Exponent $2p$ (mit $p \geq 5$) sorgt dafür, dass die Primfaktorzerlegung von $\Delta$ extrem konzentriert ist.

### Der Konduktor

Der **Konduktor** $N_E$ der Frey-Kurve ist:

$$
N_E = \prod_{q \mid abc} q,
$$

wobei das Produkt über alle Primteiler von $abc$ läuft (und der Faktor bei $q = 2$ etwas subtiler ist). Entscheidend ist: $N_E$ ist **quadratfrei** (oder fast quadratfrei) – die Frey-Kurve ist **semistabil**.

### Warum semistabil?

Eine elliptische Kurve ist semistabil, wenn sie bei jeder Primzahl höchstens multiplikative Reduktion hat. Für die Frey-Kurve gilt: Bei jeder ungeraden Primzahl $q$, die $abc$ teilt, hat die Kurve multiplikative Reduktion (einen Knotenpunkt). Bei Primzahlen, die $abc$ nicht teilen, hat sie gute Reduktion. Die Semistabilität folgt aus der speziellen Form der Gleichung.

---

## 3. Serres Epsilon-Vermutung

### Das Modularitätsproblem

**Angenommen**, die Frey-Kurve $E$ wäre modular – es gäbe also eine Neuform $f$ vom Gewicht 2 und Stufe $N_E$ mit $L(E, s) = L(f, s)$. Was könnte man über diese Neuform sagen?

### Die Galois-Darstellung

Jede elliptische Kurve liefert für jede Primzahl $p$ eine **residuale Galois-Darstellung**:

$$
\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p),
$$

die beschreibt, wie die absolute Galois-Gruppe $G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ auf den $p$-Torsionspunkten $E[p]$ wirkt.

Für die Frey-Kurve hat $\bar{\rho}_{E,p}$ besondere Eigenschaften:

1. Sie ist **irreduzibel** (für $p \geq 5$, was aus der speziellen Struktur der Lösung folgt).
2. Sie ist **wenig verzweigt**: An fast allen Stellen ist die Darstellung unverzweigt.
3. Sie kommt (wenn $E$ modular ist) von einer Neuform der Stufe $N_E$.

### Serres Vermutung

**Jean-Pierre Serre** formulierte in den 1980er Jahren eine allgemeine Vermutung darüber, von welcher Stufe eine modulare Darstellung sein muss. Angewandt auf die Frey-Kurve besagt seine Vermutung (genauer: eine Konsequenz, die er „$\varepsilon$-Vermutung" nannte):

!!! note "Serres $\varepsilon$-Vermutung (für die Frey-Kurve)"
    Wenn die Frey-Kurve modular ist, dann kommt die Darstellung $\bar{\rho}_{E,p}$
    von einer Neuform der **Stufe 2**.

Das ist dramatisch: Es gibt **keine** Neuform vom Gewicht 2 und Stufe 2 (der Raum $S_2(\Gamma_0(2))$ ist null-dimensional). Wenn also Serres Vermutung stimmt, dann **kann die Frey-Kurve nicht modular sein**.

---

## 4. Ribets Beweis (1986)

### Level-Lowering

**Kenneth Ribet**, Professor an der University of California in Berkeley, bewies 1986 genau die Aussage, die Serre als $\varepsilon$-Vermutung formuliert hatte. Sein Werkzeug war das sogenannte **Level-Lowering** (Stufenabsenkung):

!!! note "Theorem (Ribet, 1986)"
    Sei $E$ eine semistabile elliptische Kurve über $\mathbb{Q}$ und $p$ eine Primzahl
    mit $p \geq 3$. Wenn $\bar{\rho}_{E,p}$ modular ist (d.h. von einer Neuform
    der Stufe $N$ kommt) und eine Primzahl $q \| N$ die Darstellung nicht teilt
    (d.h. $q \nmid N(\bar{\rho})$, den Artin-Konduktor der Darstellung),
    dann kommt $\bar{\rho}_{E,p}$ bereits von einer Neuform der **Stufe $N/q$**.

### Anwendung auf die Frey-Kurve

Für die Frey-Kurve $E$ mit Konduktor $N_E = \prod_{q \mid abc} q$ lässt sich das Level-Lowering iteriert anwenden: Bei jeder ungeraden Primzahl $q \mid abc$ gilt $q^p \mid \Delta$ (wegen des Exponenten $2p$ in der Diskriminante), was $q \nmid N(\bar{\rho}_{E,p})$ impliziert. Ribet erlaubt es, den Faktor $q$ aus der Stufe zu entfernen.

Nach Entfernung aller solchen Faktoren bleibt nur die Stufe **2** übrig. Da $S_2(\Gamma_0(2)) = 0$, gibt es keine passende Neuform – die Darstellung kann nicht modular sein.

### Die Bedeutung

Ribets Theorem verwandelte Serres Vermutung in ein **Theorem**:

$$
\text{Frey-Kurve modular} \implies \text{Neuform der Stufe 2 existiert} \implies \text{Widerspruch!}
$$

Damit war klar: **Die Frey-Kurve ist nicht modular** – vorausgesetzt, die Taniyama-Shimura-Vermutung ist falsch. Oder umgekehrt:

$$
\text{Taniyama-Shimura (semistabil)} \implies \text{keine Frey-Kurve} \implies \text{FLT.}
$$

---

## 5. Die logische Kette

Die gesamte Argumentationskette im Überblick – eine Kette von Implikationen:

### Schritt 1: Hypothetische FLT-Lösung → Frey-Kurve

Aus $a^p + b^p = c^p$ (mit $p \geq 5$, primitiv) konstruiert Frey:

$$
E: \quad y^2 = x(x - a^p)(x + b^p).
$$

Diese Kurve ist **semistabil** mit extrem großer Diskriminante.

### Schritt 2: Frey-Kurve + TSV → modulare Darstellung

Wenn die TSV (semistabile Version) gilt, ist $E$ modular. Dann kommt $\bar{\rho}_{E,p}$ von einer Neuform der Stufe $N_E$.

### Schritt 3: Level-Lowering → Stufe 2

Ribets Theorem erlaubt die schrittweise Reduktion der Stufe:

$$
N_E = \prod_{q \mid abc} q \quad \xrightarrow{\text{Ribet}} \quad 2.
$$

### Schritt 4: Widerspruch

Es gibt keine Neuform vom Gewicht 2 und Stufe 2. Also ist die Frey-Kurve nicht modular. Aber nach TSV müsste sie modular sein. **Widerspruch.**

### Das Diagramm

$$
\boxed{a^p + b^p = c^p} \xrightarrow{\text{Frey}} \boxed{E \text{ semistabil}} \xrightarrow{\text{TSV}} \boxed{E \text{ modular}} \xrightarrow{\text{Ribet}} \boxed{\text{Stufe 2}} \to \boxed{\bot}
$$

Der Widerspruch zeigt: Die Annahme einer FLT-Lösung war falsch. **Fermats letzter Satz ist wahr.**

---

## 6. Was bleibt zu tun?

Nach Ribets Durchbruch von 1986 war die Situation kristallklar:

> **Um Fermats letzten Satz zu beweisen, genügt es, die Taniyama-Shimura-Vermutung für semistabile elliptische Kurven zu beweisen.**

Das war gleichzeitig eine gute und eine schlechte Nachricht:

**Die gute Nachricht**: FLT war auf ein konkretes, klar formuliertes Problem reduziert – die Modularität semistabiler Kurven. Kein Raten mehr, kein Suchen nach dem „richtigen" Ansatz. Der Weg war vorgezeichnet.

**Die schlechte Nachricht**: Die TSV galt als hoffnungslos schwierig. Die meisten Experten hielten einen Beweis in absehbarer Zeit für unmöglich. Selbst André Weil, der zur Formulierung der Vermutung beigetragen hatte, äußerte sich skeptisch.

Doch ein Mathematiker nahm die Herausforderung an: **Andrew Wiles**, der seit seiner Kindheit von Fermats letztem Satz fasziniert war. Von 1986 bis 1993 arbeitete er im Geheimen an einem Beweis – mit Werkzeugen, die in den folgenden Artikeln entwickelt werden: Galois-Darstellungen, Deformationstheorie und der revolutionäre Taylor-Wiles-Trick.

---

## Ausblick

Die Reduktion von FLT auf die TSV war ein Triumph der strukturellen Mathematik. Aber der eigentliche Beweis – die Modularität semistabiler Kurven – erfordert eine völlig neue Sprache:

| Artikel | Thema |
|---------|-------|
| [03 – Galois-Darstellungen](../03-galois-darstellungen/article_de.md) | Wie elliptische Kurven Matrizen-Darstellungen liefern |
| [04 – Deformationstheorie](../04-deformationstheorie/article_de.md) | Wie man Darstellungen „verbiegt" |
| [05 – R = T](../05-r-gleich-t/article_de.md) | Das Herz von Wiles' Beweis |

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 9 – Frey-Kurve und Ribets Theorem
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), Introduction
- **Kenneth Ribet**: *On modular representations of $\text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ arising from modular forms*, Inventiones Mathematicae 100 (1990)
- **Gerhard Frey**: *Links between stable elliptic curves and certain Diophantine equations*, Annales Universitatis Saraviensis 1 (1986)
- **Jean-Pierre Serre**: *Sur les représentations modulaires de degré 2 de $\text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$*, Duke Mathematical Journal 54 (1987)
