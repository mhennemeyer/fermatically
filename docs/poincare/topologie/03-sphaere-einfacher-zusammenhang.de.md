---
title: "Die Sphäre und einfacher Zusammenhang"
slug: poincare/topologie/03-sphaere-einfacher-zusammenhang
series: poincare
part: 3
act: topologie
date: 2026-04-25
status: draft
lang: de
tags:
  - sphaere
  - homotopie
  - fundamentalgruppe
---

# Die Sphäre und einfacher Zusammenhang

!!! abstract "Zusammenfassung"
    Die $n$-Sphäre $S^n$ ist die Modellmannigfaltigkeit der Topologie und
    die zentrale Hauptdarstellerin der Poincaré-Vermutung. Über
    **Schleifen** und **Homotopie** definiert man die **Fundamentalgruppe**
    $\pi_1(M)$; verschwindet sie, heißt $M$ **einfach zusammenhängend**.
    Genau diese Eigenschaft soll die 3-Sphäre unter allen geschlossenen
    3-Mannigfaltigkeiten auszeichnen.

## 1. Die $n$-Sphäre

Die **$n$-Sphäre** ist definiert als die Einheitssphäre im
$\mathbb{R}^{n+1}$:

$$
S^n = \{x \in \mathbb{R}^{n+1} : \|x\| = 1\}.
$$

Sie ist eine geschlossene, glatte $n$-Mannigfaltigkeit. Eine bequeme,
äquivalente Beschreibung gewinnt man über die **stereographische
Projektion**: Aus $S^n$ wird ein einzelner Punkt – etwa der Nordpol –
entfernt, und der Rest wird homöomorph auf $\mathbb{R}^n$ abgebildet. Die
Sphäre ist damit die Einpunkt-Kompaktifizierung des $\mathbb{R}^n$:

$$
S^n \cong \mathbb{R}^n \cup \{\infty\}.
$$

In niedrigen Dimensionen liefert das vertraute Bilder. $S^0$ besteht aus
zwei Punkten, $S^1$ ist der Kreis, $S^2$ die gewöhnliche Kugeloberfläche,
$S^3$ liegt im $\mathbb{R}^4$ und kann als zwei verklebte Vollkugeln
$D^3 \cup_{S^2} D^3$ visualisiert werden. Genau diese 3-Sphäre $S^3$ ist
das Objekt, dessen topologische Eindeutigkeit Poincaré 1904 vermutete.

## 2. Schleifen und Wege

Ein **Weg** in einem topologischen Raum $X$ ist eine stetige Abbildung
$\gamma \colon [0,1] \to X$. Stimmen Anfangs- und Endpunkt überein, also
$\gamma(0) = \gamma(1) = x_0$, spricht man von einer **Schleife** mit
Basispunkt $x_0$. Anschaulich: ein zusammenhängender Faden, der in einem
festen Punkt beginnt und endet.

Schleifen lassen sich verknüpfen. Sind $\alpha, \beta$ Schleifen am
gleichen Basispunkt, definiert man die **Konkatenation**
$\alpha \cdot \beta$, indem zuerst $\alpha$ und anschließend $\beta$
durchlaufen wird (jeweils mit doppelter Geschwindigkeit). Die konstante
Schleife $c_{x_0}$ verharrt bei $x_0$, und die **Umkehrung**
$\bar\alpha(t) = \alpha(1-t)$ läuft $\alpha$ rückwärts. So entsteht eine
Struktur, die – nach Identifikation homotoper Schleifen – zu einer Gruppe
wird.

## 3. Homotopie

Zwei stetige Abbildungen $f, g \colon X \to Y$ heißen **homotop**, wenn
sich die eine stetig in die andere deformieren lässt. Formal:

> Eine **Homotopie** zwischen $f$ und $g$ ist eine stetige Abbildung
> $H \colon X \times [0,1] \to Y$ mit $H(\cdot, 0) = f$ und
> $H(\cdot, 1) = g$.

Für Schleifen verlangt man zusätzlich, dass der Basispunkt während der
Deformation festgehalten wird (**basispunkterhaltende Homotopie**).
Anschaulich: Die Schleife darf sich beliebig dehnen, stauchen und
verbiegen, der Faden darf sich aber nicht durchschneiden, und die Naht am
Basispunkt bleibt zugenäht.

Die Homotopierelation ist eine Äquivalenzrelation auf den Schleifen.
Schreibweise: $[\alpha]$ für die Klasse aller zu $\alpha$ homotopen
Schleifen.

## 4. Die Fundamentalgruppe

Auf der Menge der Homotopieklassen induziert die Konkatenation eine
wohldefinierte Verknüpfung. Damit erhält man:

> Die **Fundamentalgruppe** von $X$ am Basispunkt $x_0$ ist
> $$\pi_1(X, x_0) = \{[\alpha] : \alpha \text{ Schleife an } x_0\}$$
> mit der Verknüpfung $[\alpha][\beta] = [\alpha \cdot \beta]$,
> neutralem Element $[c_{x_0}]$ und Inversem $[\alpha]^{-1} = [\bar\alpha]$.

Für wegzusammenhängende Räume hängt $\pi_1(X, x_0)$ bis auf Isomorphie
nicht vom Basispunkt ab; man schreibt dann $\pi_1(X)$. Die
Fundamentalgruppe ist eine **topologische Invariante**: Homöomorphe
Räume haben isomorphe Fundamentalgruppen.

> „The fundamental group $\pi_1(X)$ is the most basic and most useful of
> the algebraic invariants associated to a topological space."
> — Allen Hatcher, *Algebraic Topology* (2002), S. 25

## 5. Einfacher Zusammenhang

Verschwindet die Fundamentalgruppe, lässt sich also jede Schleife stetig
auf einen Punkt zusammenziehen, heißt der Raum **einfach
zusammenhängend**:

$$
X \text{ einfach zusammenhängend} \;:\Longleftrightarrow\; X \text{ wegzusammenhängend und } \pi_1(X) = 0.
$$

Anschauliches Kriterium: Ein Gummiband, das man irgendwo auf $X$ legt,
lässt sich – ohne $X$ zu verlassen und ohne zu reißen – auf einen Punkt
zusammenziehen.

## 6. Fundamentalgruppen einiger Räume

Drei Beispiele, die sich für die Poincaré-Diskussion einprägen sollte:

**Die Sphäre $S^n$ für $n \geq 2$.** Jede Schleife auf der Kugelfläche
lässt sich auf einen Punkt zusammenziehen: $\pi_1(S^n) = 0$. Anschaulich
kann man das Gummiband um die Kugel herum zu einem Pol verschieben. Die
$S^n$ ist für $n \geq 2$ einfach zusammenhängend.

**Der Kreis $S^1$.** Eine Schleife, die $k$-mal um den Kreis läuft, lässt
sich nicht auf einen Punkt zusammenziehen, ohne die andere Seite zu
durchqueren. Es gilt:

$$
\pi_1(S^1) \cong \mathbb{Z},
$$

mit der Windungszahl als Isomorphismus. $S^1$ ist *nicht* einfach
zusammenhängend.

**Der Torus $T^2 = S^1 \times S^1$.** Es gibt zwei unabhängige
Grundschleifen, die jeweils einen $S^1$-Faktor umrunden. Die
Fundamentalgruppe ist abelsch:

$$
\pi_1(T^2) \cong \mathbb{Z} \oplus \mathbb{Z}.
$$

In Dimension 3 hat der 3-Torus $T^3$ entsprechend
$\pi_1(T^3) \cong \mathbb{Z}^3$, und die Linsenräume $L(p, q)$ haben
endliche Fundamentalgruppen $\mathbb{Z}/p$.

## 7. Höhere Homotopiegruppen

Schleifen sind Abbildungen $S^1 \to X$. Ersetzt man $S^1$ durch $S^k$,
erhält man die **höheren Homotopiegruppen** $\pi_k(X)$. Für die Sphäre
selbst gilt $\pi_n(S^n) \cong \mathbb{Z}$, klassifiziert durch den
**Abbildungsgrad**. Höhere $\pi_k(S^n)$ für $k > n$ sind hochgradig
nichttrivial – ihr Studium war eines der treibenden Themen der
algebraischen Topologie im 20. Jahrhundert.

Für die Poincaré-Vermutung relevant ist die Eigenschaft, dass $S^n$ für
$n \geq 2$ in $\pi_1$ trivial ist. Erst diese Trivialität macht die
Vermutung formulierbar: „einfach zusammenhängend" ist exakt
$\pi_1 = 0$.

## 8. Bezug zur Vermutung

Die **Poincaré-Vermutung in Dimension 3** besagt:

$$
M^3 \text{ geschlossen, einfach zusammenhängend} \;\Longrightarrow\; M^3 \cong S^3.
$$

Damit ist klar, warum die Sphäre und ihr Fundamentalgruppen-Profil
zentral sind: $\pi_1(S^3) = 0$ ist die *kennzeichnende* Eigenschaft, die
sie unter allen geschlossenen 3-Mannigfaltigkeiten auszeichnen soll. In
allen anderen Dimensionen $n \geq 5$ wurde die analoge Aussage von Smale
(1961) bewiesen, in Dimension 4 von Freedman (1982). In Dimension 3
gelang sie erst Perelman.

> „The Poincaré Conjecture says that $S^3$ is the only closed
> 3-manifold whose fundamental group is trivial."
> — John W. Morgan, Gang Tian, *Ricci Flow and the Poincaré
> Conjecture* (2007), S. 3

## 9. Ausblick

Mit Mannigfaltigkeit, Sphäre, Homotopie und Fundamentalgruppe sind alle
Bausteine bereit, um die Vermutung präzise zu formulieren. Der nächste
Artikel zeichnet ihre Geschichte nach – von Poincarés *Analysis Situs*
1904 über die höherdimensionalen Lösungen bis zu Hamiltons Programm.

| Artikel | Thema |
|---------|-------|
| [04 – Was ist die Poincaré-Vermutung?](04-was-ist-poincare-vermutung.md) | Originalformulierung 1904, höhere Dimensionen |
| [05 – Die Geometrisierungs-Vermutung](05-geometrisierungs-vermutung.md) | Thurstons größeres Bild |

---

## Quellen

- **Allen Hatcher**: *Algebraic Topology*, Cambridge University Press
  (2002), Kapitel 1
- **John M. Lee**: *Introduction to Topological Manifolds*, 2. Auflage,
  Springer (2011), Kapitel 7
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007), Kapitel 1
- **Henri Poincaré**: *Cinquième complément à l'Analysis Situs*,
  Rendiconti del Circolo Matematico di Palermo 18 (1904), 45–110
