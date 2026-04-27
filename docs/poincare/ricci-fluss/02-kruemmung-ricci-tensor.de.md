---
title: "Krümmung und Ricci-Tensor"
slug: poincare/ricci-fluss/02-kruemmung-ricci-tensor
series: poincare
part: 2
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - kruemmung
  - ricci-tensor
---

# Krümmung und Ricci-Tensor

!!! abstract "Zusammenfassung"
    Krümmung misst, wie weit eine Riemannsche Mannigfaltigkeit lokal
    vom euklidischen Raum abweicht. Aus dem Riemannschen Krümmungstensor
    entstehen durch Spurbildung Schnittkrümmung, Ricci-Tensor und
    Skalarkrümmung. Der Ricci-Tensor – ein gemittelter Krümmungsbegriff –
    ist die rechte Seite von Hamiltons Ricci-Fluss.

## 1. Warum Krümmung?

Eine flache Ebene unterscheidet sich von einer Sphäre dadurch, dass
Geodäten dort konvergieren, hier aber parallel bleiben würden. Krümmung
fasst dieses Verhalten quantitativ. Auf einer Riemannschen
Mannigfaltigkeit $(M, g)$ liefert der Levi-Civita-Zusammenhang
([Artikel 01](01-riemannsche-metrik.md), §6) ein Maß für das
**Versagen der Vertauschbarkeit** kovarianter Ableitungen.

## 2. Der Riemannsche Krümmungstensor

Für Vektorfelder $X, Y, Z$ ist

$$R(X,Y)Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z.$$

$R$ ist tensoriell – $R_p(X,Y)Z$ hängt nur von den Werten von $X,Y,Z$
am Punkt $p$ ab. In Indexschreibweise:

$$R^l{}_{ijk} = \partial_i \Gamma^l_{jk} - \partial_j \Gamma^l_{ik} + \Gamma^l_{im}\Gamma^m_{jk} - \Gamma^l_{jm}\Gamma^m_{ik}.$$

Mit gesenktem Index $R_{lijk} = g_{lm} R^m{}_{ijk}$ gelten die
**Symmetrien**

- Antisymmetrie: $R_{lijk} = -R_{iljk}$ und $R_{lijk} = -R_{likj}$,
- Block-Symmetrie: $R_{lijk} = R_{jkli}$,
- erste Bianchi-Identität: $R_{l[ijk]} = 0$,
- zweite Bianchi-Identität: $\nabla_{[m} R_{li]jk} = 0$.

Diese Symmetrien reduzieren auf einer $n$-Mannigfaltigkeit die Anzahl
unabhängiger Komponenten von $n^4$ auf $\tfrac{1}{12}n^2(n^2-1)$.

## 3. Schnittkrümmung

Für zwei linear unabhängige Vektoren $u, v \in T_pM$ ist die
**Schnittkrümmung** der von $u, v$ aufgespannten Ebene

$$K(u, v) = \frac{g\bigl(R(u,v)v, u\bigr)}{g(u,u)\,g(v,v) - g(u,v)^2}.$$

Sie verallgemeinert den Gauß-Krümmungsbegriff aus der Flächentheorie.
Konstante Schnittkrümmung kennzeichnet die drei
**Modellgeometrien**:

| Schnittkrümmung | Modellraum (Dim. $n$)        | Geometrie    |
|-----------------|------------------------------|--------------|
| $K \equiv +1$   | Sphäre $S^n$                 | sphärisch    |
| $K \equiv 0$    | Euklidischer Raum $\mathbb{R}^n$ | flach    |
| $K \equiv -1$   | Hyperbolischer Raum $\mathbb{H}^n$ | hyperbolisch |

Auf 3-Mannigfaltigkeiten ist konstante Schnittkrümmung *nicht* das
Ende der Geschichte – Thurstons Klassifikation kennt acht
Modellgeometrien (siehe [Artikel 05 in Akt 1](../topologie/05-geometrisierungs-vermutung.md)).

## 4. Der Ricci-Tensor

Durch Spurbildung über zwei Indizes des Krümmungstensors entsteht der
**Ricci-Tensor**:

$$\mathrm{Ric}_{jk} = R^i{}_{jik} = g^{im}\,R_{mjik}.$$

Geometrisch beschreibt $\mathrm{Ric}_p(v,v)$, gemittelt über alle
Ebenen durch $v$, die *durchschnittliche Schnittkrümmung* in Richtung
$v$. Anschaulicher: Bei einer kleinen Geodäten-„Trompete", die in
Richtung $v$ ausgeht, misst der Ricci-Tensor, wie das infinitesimale
Volumenelement entlang der Geodäten verändert wird – positiver
Ricci-Tensor zieht zusammen, negativer streut auseinander.

> „The Ricci tensor measures the average way in which the volume
> element distorts as you move along a geodesic."
> — John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture* (2007), §1.2

Der Ricci-Tensor ist ein symmetrisches $(0,2)$-Tensorfeld – genau die
Form, die zu einer Metrik addiert wieder eine Metrik(-Variation)
ergibt. Genau das macht ihn als rechte Seite einer Evolutionsgleichung
für $g$ geeignet.

## 5. Skalarkrümmung

Eine weitere Spur liefert die **Skalarkrümmung**:

$$R = g^{jk}\,\mathrm{Ric}_{jk}.$$

Sie ist eine glatte Funktion auf $M$. Auf $S^n$ mit Rundmetrik ist
$R = n(n-1)$, auf $\mathbb{R}^n$ ist $R = 0$, auf $\mathbb{H}^n$ ist
$R = -n(n-1)$. In Dimension $2$ stimmt $R$ bis auf den Faktor $2$ mit
der Gauß-Krümmung überein und bestimmt nach Gauß-Bonnet die
Topologie der Fläche vollständig.

## 6. Spezialfall Dimension 3

In Dimension 3 hat der Riemannsche Krümmungstensor genauso viele
unabhängige Komponenten wie der Ricci-Tensor (jeweils 6). Daraus
folgt eine zentrale Identität:

> **In Dimension 3 ist der volle Krümmungstensor $R$ algebraisch durch
> den Ricci-Tensor und die Metrik bestimmt.**

Das ist der Grund, warum sich Hamiltons Ricci-Fluss in 3D überhaupt
zur Klassifikation eignet: Eine Evolutionsgleichung *für $\mathrm{Ric}$*
genügt, um die gesamte Geometrie zu kontrollieren. In höheren
Dimensionen geht diese Reduktion verloren – der Weyl-Tensor bleibt
übrig und macht das Problem deutlich schwerer.

## 7. Volumen- und Diameter-Vergleich

Krümmungsschranken übersetzen sich in geometrische und topologische
Konsequenzen.

- **Bonnet–Myers:** Ist $\mathrm{Ric} \ge (n-1) k\, g$ mit $k > 0$,
  so ist $M$ kompakt und der Diameter erfüllt
  $\mathrm{diam}(M) \le \pi/\sqrt{k}$.
- **Bishop–Gromov:** Eine untere Schranke an $\mathrm{Ric}$ liefert
  ein oberes Volumenwachstum von Bällen.
- **Cheeger–Gromoll-Splitting:** Ist $\mathrm{Ric} \ge 0$ und
  enthält $M$ eine Geraden-Geodäte, so spaltet $M$ isometrisch als
  $N \times \mathbb{R}$ ab.

Diese Vergleichssätze sind zentrale Werkzeuge bei Perelmans Analyse
der Ricci-Fluss-Singularitäten.

## 8. Einstein-Mannigfaltigkeiten

Eine Riemannsche Mannigfaltigkeit heißt **Einstein**, wenn

$$\mathrm{Ric} = \lambda\, g \quad \text{für ein } \lambda \in \mathbb{R}.$$

Solche Metriken sind Fixpunkte des normalisierten Ricci-Flusses
(siehe [Artikel 03](03-hamiltons-ricci-fluss.md)). Die runde Sphäre,
der Euklidische Raum und der hyperbolische Raum sind Einstein, ebenso
allgemeiner symmetrische Räume. Das Auffinden Einstein-Metriken auf
einer gegebenen Mannigfaltigkeit ist ein eigenes Forschungsfeld
(Yamabe-Problem).

## 9. Auf dem Weg zum Fluss

Mit Riemannscher Metrik (Artikel 01), Krümmungstensor und Ricci-Tensor
liegen alle Bausteine bereit, um die Evolutionsgleichung

$$\frac{\partial g}{\partial t} = -2\,\mathrm{Ric}(g)$$

aufzustellen und ihre Wirkung zu analysieren. Das ist Gegenstand des
nächsten Artikels.

## Quellen

- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer (2018), Kap. 7.
- Manfredo do Carmo, *Riemannian Geometry*, Birkhäuser (1992), Kap. 4–6.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS Clay Math. Monographs Vol. 3 (2007), §1–2.
- Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer (2016), Kap. 3 & 9.

## Querverweise

- Vorheriger Artikel: [Riemannsche Metrik](01-riemannsche-metrik.md)
- Nächster Artikel: [Hamiltons Ricci-Fluss](03-hamiltons-ricci-fluss.md)
- Akt 1, Artikel 05: [Geometrisierungs-Vermutung](../topologie/05-geometrisierungs-vermutung.md)
