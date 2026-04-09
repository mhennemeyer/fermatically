---
title: "Elliptische Kurven – Von Diophant zu Kryptographie"
slug: elliptische-kurven/01-elliptische-kurven
series: elliptische-kurven
part: 1
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - elliptische-kurven
  - gruppengesetz
  - l-reihen
requires:
  - koordinatengeometrie
  - bruchrechnung
  - modulare-arithmetik
  - abbildungen
  - summen-produktnotation
---

# Elliptische Kurven

!!! abstract "Zusammenfassung"
    Algebraische Kurven mit natürlicher Gruppenstruktur. Frey-Kurve, Taniyama-Shimura-Vermutung
    und Galois-Darstellungen – alle zentralen Objekte in Wiles' Beweis basieren auf elliptischen Kurven.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](gruppen.md)
- [Ringe und Körper](ringe-koerper.md)

| Thema | Beschreibung |
|-------|-------------|
| [Koordinatengeometrie](../vorwissen/koordinatengeometrie.md) | Punkte, Geraden, Kurven als Gleichungen |
| [Bruchrechnung](../vorwissen/bruchrechnung.md) | Rechnen mit Brüchen $a/b$ |
| [Modulare Arithmetik](../vorwissen/modulare-arithmetik.md) | Kongruenzen $a \equiv b \pmod{n}$ und Restklassen |
| [Abbildungen (Funktionen)](../vorwissen/abbildungen.md) | $f: A \to B$, injektiv, surjektiv, bijektiv |
| [Summen- und Produktnotation](../vorwissen/summen-produktnotation.md) | $\sum$- und $\prod$-Notation |

---

## 1. Definition

Eine **elliptische Kurve** über einem Körper $K$ ist eine glatte, projektive Kurve vom Geschlecht $1$ mit einem ausgezeichneten Punkt. In der Praxis die **Weierstraß-Form**:

$$
E: \quad y^2 = x^3 + ax + b \qquad (a, b \in K)
$$

Die Glattheitsbedingung (keine Spitzen oder Selbstüberschneidungen) erfordert eine nichtverschwindende **Diskriminante**:

$$
\Delta = -16(4a^3 + 27b^2) \neq 0
$$

Geometrisch über $\mathbb{R}$: eine glatte Kurve in der Ebene, bestehend aus einer oder zwei Komponenten.

!!! note "Warum „elliptisch"?"
    Der Name hat nichts mit Ellipsen zu tun. Er stammt von den **elliptischen Integralen** – Integralen der Form $\int \frac{dx}{\sqrt{x^3 + ax + b}}$, die bei der Berechnung des Umfangs einer Ellipse auftreten.

### Beispiele

| Kurve | $a$ | $b$ | $\Delta$ |
|-------|-----|-----|----------|
| $y^2 = x^3 - x$ | $-1$ | $0$ | $64$ |
| $y^2 = x^3 + 1$ | $0$ | $1$ | $-432$ |
| $y^2 = x^3 - x + 1$ | $-1$ | $1$ | $-368$ |

### Der Punkt im Unendlichen

Technisch lebt eine elliptische Kurve im **projektiven Raum** $\mathbb{P}^2$. Neben den affinen Punkten $(x, y)$ mit $y^2 = x^3 + ax + b$ gibt es einen zusätzlichen **Punkt im Unendlichen** $\mathcal{O}$, der als neutrales Element der Gruppenstruktur dient.

## 2. Die Gruppenoperation

Die Punkte einer elliptischen Kurve bilden eine **abelsche Gruppe**. Die Verknüpfung ist geometrisch über die **Sekanten-Tangenten-Methode** definiert:

**Addition zweier Punkte $P + Q$:**
1. Gerade durch $P$ und $Q$ legen
2. Diese Gerade schneidet die Kurve in genau einem dritten Punkt $R'$
3. $R'$ an der $x$-Achse spiegeln: Das Ergebnis ist $P + Q$

**Verdopplung $2P = P + P$:**
1. Tangente an die Kurve in $P$ legen
2. Diese Tangente schneidet die Kurve in einem zweiten Punkt $R'$
3. Spiegeln: Das Ergebnis ist $2P$

**Neutrales Element:** Der Punkt $\mathcal{O}$ im Unendlichen. Es gilt $P + \mathcal{O} = P$ für alle $P$.

**Inverses:** Das Inverse von $P = (x, y)$ ist $-P = (x, -y)$ (Spiegelung an der $x$-Achse).

> „It is a wonderful fact that this geometric construction gives a group law on the points of an elliptic curve."
> — Joseph Silverman, *The Arithmetic of Elliptic Curves* (1986), S. 51

!!! tip "Algebraische Formeln"
    Für $P = (x_1, y_1)$ und $Q = (x_2, y_2)$ mit $P \neq \pm Q$:

    $$
    \lambda = \frac{y_2 - y_1}{x_2 - x_1}, \quad x_3 = \lambda^2 - x_1 - x_2, \quad y_3 = \lambda(x_1 - x_3) - y_1
    $$

    Für $P = Q$ (Verdopplung):

    $$
    \lambda = \frac{3x_1^2 + a}{2y_1}
    $$

    Diese Formeln gelten über **jedem** Körper – auch über $\mathbb{F}_p$ oder $\mathbb{Q}_p$.

## 3. Rationale Punkte und der Satz von Mordell

Die Menge der rationalen Punkte $E(\mathbb{Q}) = \{(x, y) \in \mathbb{Q}^2 \mid y^2 = x^3 + ax + b\} \cup \{\mathcal{O}\}$ ist eine Untergruppe von $E$.

**Satz (Mordell, 1922).** $E(\mathbb{Q})$ ist eine endlich erzeugte abelsche Gruppe.

Nach dem Struktursatz für endlich erzeugte abelsche Gruppen:

$$
E(\mathbb{Q}) \cong \mathbb{Z}^r \oplus E(\mathbb{Q})_{\text{tors}}
$$

wobei:
- $r = \text{rang}(E)$ der **Rang** der Kurve ist (Anzahl unabhängiger Punkte unendlicher Ordnung)
- $E(\mathbb{Q})_{\text{tors}}$ die endliche **Torsionsuntergruppe** ist (Punkte endlicher Ordnung)

**Satz (Mazur, 1977).** Die Torsionsuntergruppe $E(\mathbb{Q})_{\text{tors}}$ ist isomorph zu einer der folgenden Gruppen:

$$
\mathbb{Z}/n\mathbb{Z} \text{ für } n \in \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12\}
$$
$$
\text{oder } \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2n\mathbb{Z} \text{ für } n \in \{1, 2, 3, 4\}
$$

Der Rang $r$ ist schwer zu berechnen. Ob elliptische Kurven mit beliebig großem Rang existieren, ist eine offene Frage.

## 4. Reduktion modulo $p$

Eine elliptische Kurve $E: y^2 = x^3 + ax + b$ mit $a, b \in \mathbb{Z}$ kann modulo einer Primzahl $p$ reduziert werden:

$$
\tilde{E}: \quad y^2 \equiv x^3 + ax + b \pmod{p}
$$

Wenn $p \nmid \Delta$, ist $\tilde{E}$ eine glatte Kurve über $\mathbb{F}_p$ – $E$ hat **gute Reduktion** bei $p$. Andernfalls liegt **schlechte Reduktion** vor.

### Die $a_p$-Koeffizienten

Für Primzahlen $p$ guter Reduktion:

$$
a_p = p + 1 - \#\tilde{E}(\mathbb{F}_p)
$$

wobei $\#\tilde{E}(\mathbb{F}_p)$ die Anzahl der Punkte von $\tilde{E}$ über $\mathbb{F}_p$ ist (inklusive $\mathcal{O}$).

**Satz (Hasse, 1933).** Es gilt $|a_p| \leq 2\sqrt{p}$.

Die $a_p$-Koeffizienten kodieren das Verhalten der Kurve Primzahl für Primzahl. Sie bilden die Bausteine der $L$-Reihe.

**Beispiel:** Für $E: y^2 = x^3 - x$ und $p = 5$:

| $x$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|-----|-----|-----|-----|-----|-----|
| $x^3 - x \bmod 5$ | $0$ | $0$ | $1$ | $4$ | $0$ |
| $y^2 \equiv \ldots$? | $y = 0$ | $y = 0$ | $y = \pm 1$ | $y = \pm 2$ | $y = 0$ |

Das ergibt $8$ affine Punkte plus $\mathcal{O}$, also $\#\tilde{E}(\mathbb{F}_5) = 9$ und $a_5 = 5 + 1 - 9 = -3$.

## 5. Die $L$-Reihe einer elliptischen Kurve

Die $a_p$-Koeffizienten werden in einer analytischen Funktion gebündelt – der **$L$-Reihe** (Hasse-Weil):

$$
L(E, s) = \prod_{p \text{ gut}} \frac{1}{1 - a_p p^{-s} + p^{1-2s}} \cdot \prod_{p \text{ schlecht}} (\text{lokaler Faktor})
$$

Diese $L$-Reihe konvergiert für $\text{Re}(s) > 3/2$ und kodiert die gesamte arithmetische Information der Kurve.

**Die BSD-Vermutung** (Birch und Swinnerton-Dyer, eines der Millennium-Probleme): Der Rang von $E(\mathbb{Q})$ ist gleich der Ordnung der Nullstelle von $L(E, s)$ bei $s = 1$.

### Die Verbindung zu Modulformen

Die zentrale Frage: Ist die $L$-Reihe $L(E, s)$ *gleich* der $L$-Reihe einer **Modulform** $f$?

$$
L(E, s) \stackrel{?}{=} L(f, s) = \sum_{n=1}^{\infty} a_n n^{-s}
$$

Wenn ja, heißt $E$ **modular**. Die **Taniyama-Shimura-Vermutung** (jetzt Theorem) besagt: **Jede** elliptische Kurve über $\mathbb{Q}$ ist modular. Dieser Satz – genauer: der semistabile Fall, bewiesen von Wiles – impliziert Fermats letzten Satz.

## 6. Torsionspunkte und Galois-Darstellungen

Für eine Primzahl $\ell$ sind die **$\ell$-Teilungspunkte** die Punkte $P \in E(\overline{\mathbb{Q}})$ mit $\ell P = \mathcal{O}$:

$$
E[\ell] = \{P \in E(\overline{\mathbb{Q}}) \mid \ell P = \mathcal{O}\}
$$

Es gilt $E[\ell] \cong (\mathbb{Z}/\ell\mathbb{Z})^2$ – ein zweidimensionaler Vektorraum über $\mathbb{F}_\ell$.

Die **absolute Galois-Gruppe** $G_{\mathbb{Q}}$ wirkt auf $E[\ell]$ durch Permutation der Koordinaten. Dies definiert eine **Galois-Darstellung**:

$$
\bar{\rho}_{E,\ell}: G_{\mathbb{Q}} \to \text{Aut}(E[\ell]) \cong \text{GL}_2(\mathbb{F}_\ell)
$$

Für die **$\ell$-adischen Tate-Moduln** (den projektiven Limes über alle $\ell^n$-Teilungspunkte) ergibt sich eine $\ell$-adische Darstellung:

$$
\rho_{E,\ell}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_\ell) \hookrightarrow \text{GL}_2(\mathbb{Q}_\ell)
$$

Diese Darstellungen bilden das Bindeglied zwischen elliptischen Kurven und der Galois-Theorie – das zentrale Objekt in Wiles' Beweis.

## 7. Elliptische Kurven in der Kryptographie

Elliptische Kurven über endlichen Körpern $\mathbb{F}_p$ bilden die Grundlage moderner **kryptographischer Verfahren** (ECC – Elliptic Curve Cryptography).

Die Sicherheit beruht auf dem **diskreten Logarithmusproblem**: Gegeben $P$ und $Q = nP$ auf $E(\mathbb{F}_p)$, ist es rechnerisch extrem schwierig, $n$ zu bestimmen – obwohl die Berechnung von $nP$ aus $n$ und $P$ effizient möglich ist (durch wiederholtes Verdoppeln und Addieren).

ECC bietet dasselbe Sicherheitsniveau wie RSA, aber mit kürzeren Schlüsseln:

| Sicherheitsniveau | RSA-Schlüssel | ECC-Schlüssel |
|-------------------|---------------|---------------|
| 128 Bit | 3072 Bit | 256 Bit |
| 256 Bit | 15360 Bit | 512 Bit |

## 8. Ausblick: Modularität

Dieser Artikel hat elliptische Kurven als eigenständige algebraische Objekte vorgestellt. Ihre Verbindung zu **Modulformen** ist Thema des nächsten Werkzeug-Artikels.

Die Kette der Verbindungen:

$$
\text{Elliptische Kurve } E \xrightarrow{a_p} \text{$L$-Reihe } L(E,s) \xleftarrow{?} L(f,s) \xleftarrow{a_n} \text{Modulform } f
$$

Die Taniyama-Shimura-Vermutung behauptet, dass der mittlere Pfeil immer existiert – dass jede elliptische Kurve ein Gegenstück im Raum der Modulformen hat. Wiles' Beweis dieser Vermutung (für semistabile Kurven) ist der Schlüssel zu Fermats letztem Satz.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 6
- **Joseph Silverman**: *The Arithmetic of Elliptic Curves*, Springer (1986)
- **Joseph Silverman, John Tate**: *Rational Points on Elliptic Curves*, Springer (1992)
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1
