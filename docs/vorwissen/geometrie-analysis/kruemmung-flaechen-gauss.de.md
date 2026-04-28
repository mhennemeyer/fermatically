---
title: "Krümmung von Flächen (Gauß)"
slug: vorwissen/geometrie-analysis/kruemmung-flaechen-gauss
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: de
tags:
  - kruemmung
  - gauss
  - flaechen
---

# Krümmung von Flächen (Gauß)

> *„Theorema Egregium: Die Gauß-Krümmung ist eine intrinsische Größe –
> sie hängt nur von der ersten Fundamentalform ab, nicht davon, *wie*
> die Fläche eingebettet ist."*
> — Carl Friedrich Gauß, *Disquisitiones generales circa superficies curvas*, 1827.

Die Gauß-Krümmung ist der historische Ausgangspunkt der modernen
Differentialgeometrie. Sie misst, wie eine Fläche in einem Punkt
gekrümmt ist – und Gauß' Entdeckung, dass diese Größe *intrinsisch* ist,
ist das Sprungbrett zu Schnitt-, Ricci- und Skalar-Krümmung im
Hochdimensionalen.

## 1. Hauptkrümmungen

Sei $\Sigma \subset \mathbb{R}^3$ eine glatte Fläche und $p \in \Sigma$.
Wähle eine Einheitsnormale $\nu(p)$. Schneidet man $\Sigma$ mit einer
Ebene durch $p$, die $\nu(p)$ enthält, erhält man eine ebene Kurve mit
einer **Normalkrümmung** $\kappa$.

Lässt man die Schnittebene um $\nu(p)$ rotieren, schwankt $\kappa$
zwischen einem Minimum $\kappa_2$ und einem Maximum $\kappa_1$. Diese
beiden Extremalwerte heißen **Hauptkrümmungen** an $p$ (Euler 1760,
ausgearbeitet von Meusnier 1776).

Daraus definiert man:

- **Gauß-Krümmung:** $K = \kappa_1 \kappa_2$.
- **Mittlere Krümmung:** $H = \tfrac{1}{2}(\kappa_1 + \kappa_2)$.

| Fläche | $K$ | Vorzeichen |
|--------|-----|------------|
| Ebene | $0$ | flach |
| Sphäre Radius $R$ | $1/R^2$ | positiv |
| Zylinder | $0$ | flach (eine Hauptkrümmung verschwindet) |
| Sattel-Fläche | $< 0$ | hyperbolisch |
| Pseudosphäre | $-1$ konstant | hyperbolisch |

## 2. Erste und zweite Fundamentalform

Lokal lässt sich $\Sigma$ als $\mathbf r(u, v)$ parametrisieren. Die
**erste Fundamentalform** beschreibt das Längenmessen auf $\Sigma$:
$$
\mathrm{I} = E\, \mathrm{d}u^2 + 2F\, \mathrm{d}u\, \mathrm{d}v + G\, \mathrm{d}v^2,
\quad E = \mathbf r_u \cdot \mathbf r_u,\ F = \mathbf r_u \cdot \mathbf r_v,\ G = \mathbf r_v \cdot \mathbf r_v.
$$
Sie ist die Riemannsche Metrik der Fläche (siehe
[Tangentialraum und Tensoren](tangentialraum-tensoren.md)).

Die **zweite Fundamentalform** misst, wie sich die Normalenrichtung mit
dem Punkt ändert:
$$
\mathrm{II} = L\, \mathrm{d}u^2 + 2M\, \mathrm{d}u\, \mathrm{d}v + N\, \mathrm{d}v^2,
\quad L = \mathbf r_{uu} \cdot \nu, \dots
$$
Sie kennt die Einbettung der Fläche.

In dieser Sprache ist
$$
K = \frac{LN - M^2}{EG - F^2}.
$$

## 3. Theorema Egregium

Gauß' überraschende Entdeckung (1827):
$$
K \text{ hängt nur von } E, F, G \text{ und ihren Ableitungen ab.}
$$
Das heißt: Wer auf der Fläche mit Längen- und Winkelmessungen lebt,
ohne den umgebenden $\mathbb{R}^3$ zu kennen, kann $K$ trotzdem
berechnen. $K$ ist also ein *intrinsisches* Datum der Riemannschen
Metrik.

Konsequenz: Eine Sphäre kann nicht auf eine Ebene abgewickelt werden,
ohne Strecken zu verzerren – jede Weltkarte lügt.

## 4. Geodätische Dreiecke und Gauß-Bonnet

Auf einer Fläche mit Krümmung $K$ ergibt sich der **Winkelsummensatz
für Geodätendreiecke**:
$$
\alpha + \beta + \gamma - \pi = \int_T K\, \mathrm{d}A.
$$
Auf der Sphäre ($K = 1/R^2 > 0$) ist die Winkelsumme größer als $\pi$,
auf einer hyperbolischen Fläche ($K < 0$) kleiner.

Das **Theorema von Gauß-Bonnet** verallgemeinert dies auf geschlossene
Flächen:
$$
\int_\Sigma K\, \mathrm{d}A = 2\pi\, \chi(\Sigma),
$$
wobei $\chi(\Sigma)$ die **Euler-Charakteristik** ist. Für $\Sigma = S^2$
ergibt das $\chi(S^2) = 2$, für den Torus $\chi(T^2) = 0$. Diese Formel
ist die Brücke zwischen Krümmung (Analysis) und Topologie (was die
Fläche „ist") – das gleiche Bauprinzip, das Perelmans Beweis der
finiten Extinktion in [Akt 3, Artikel 05](../../poincare/beweis/05-endliche-extinktion.md)
auf der 2-Sphäre wieder verwendet.

## 5. Vom Spezialfall zur höherdimensionalen Krümmung

In $n$ Dimensionen verallgemeinert sich $K$ zur **Schnittkrümmung**
$\sec(P)$ einer 2-Ebene $P \subset T_p M$. Mittelt man über alle
Schnitt-Ebenen, die einen Vektor $v$ enthalten, erhält man die
**Ricci-Krümmung** $\mathrm{Ric}(v, v)$. Mittelt man weiter über alle
Richtungen, erhält man die **Skalar-Krümmung** $R$. Die Gauß-Krümmung
ist also der zweidimensionale Großvater des gesamten Krümmungs-Zoos
([Akt 2, Artikel 02](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md)).

## Querverweise

- Vorher: [Tangentialraum und Tensoren](tangentialraum-tensoren.md).
- Weiter: [Vektoranalysis kompakt](vektoranalysis.md), [Wärmeleitungsgleichung – Intuition](waermeleitung.md).
- Anwendung: [Akt 2, Krümmung und Ricci-Tensor](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md), [Akt 3, Endliche Extinktion](../../poincare/beweis/05-endliche-extinktion.md) (Gauß-Bonnet im Beweis).

## Quellen

- do Carmo, Manfredo P. (1976). *Differential Geometry of Curves and Surfaces.* Prentice Hall. Kap. 3–4.
- Spivak, Michael (1999). *A Comprehensive Introduction to Differential Geometry, Vol. 2.* Publish or Perish, 3. Auflage.
- Gauß, Carl Friedrich (1827). *Disquisitiones generales circa superficies curvas.*
- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2. Auflage. Kap. 8.
