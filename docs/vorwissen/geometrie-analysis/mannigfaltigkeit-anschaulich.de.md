---
title: "Mannigfaltigkeit anschaulich"
slug: vorwissen/geometrie-analysis/mannigfaltigkeit-anschaulich
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: de
tags:
  - mannigfaltigkeit
  - intuition
---

# Mannigfaltigkeit anschaulich

> *„Eine Mannigfaltigkeit ist ein Raum, der in der Nähe jedes Punktes
> aussieht wie der gewohnte $\mathbb{R}^n$ – global aber etwas ganz anderes
> sein kann."*

Die Erdoberfläche ist – grob – eine Kugelsphäre $S^2$. Wer einen
Stadtplan zeichnet, glättet sie lokal zu einem Stück $\mathbb{R}^2$. Wer
mehrere solcher Stadtpläne aneinanderfügt, erhält einen Atlas. Genau
dieses Bild – lokal wie $\mathbb{R}^n$, global durch verträgliche Karten
zusammengeklebt – ist der Begriff der **Mannigfaltigkeit**.

## 1. Das lokale Versprechen

Ein **topologischer Raum** $M$ heißt $n$-dimensionale **topologische
Mannigfaltigkeit**, wenn jeder Punkt $p \in M$ eine offene Umgebung
$U \subset M$ besitzt, die zu einer offenen Teilmenge des $\mathbb{R}^n$
*homöomorph* ist. Die zugehörige Abbildung
$$
\varphi : U \to V \subset \mathbb{R}^n
$$
heißt **Karte**. Eine Familie von Karten, deren Definitionsbereiche $M$
überdecken, heißt **Atlas**.

Zusätzliche technische Forderungen (Hausdorff, zweitabzählbar) sind
fast immer erfüllt und werden hier stillschweigend angenommen.

## 2. Glatt verträgliche Karten

Wo zwei Karten $\varphi : U \to V$ und $\psi : U' \to V'$ überlappen,
gibt es einen **Kartenwechsel**
$$
\psi \circ \varphi^{-1} : \varphi(U \cap U') \to \psi(U \cap U').
$$
Das ist eine Abbildung zwischen offenen Mengen des $\mathbb{R}^n$. Wird
verlangt, dass alle Kartenwechsel **glatt** ($C^\infty$) sind, heißt $M$
**glatte Mannigfaltigkeit**.

Glattheit ist die minimale Voraussetzung dafür, dass Begriffe wie
*Differenzierbarkeit*, *Tangentialraum* oder *Krümmung* überhaupt
definiert werden können – unabhängig davon, welche Karte man wählt.

## 3. Beispiele

| Mannigfaltigkeit | Dimension | Beschreibung |
|------------------|-----------|---------------|
| $\mathbb{R}^n$ | $n$ | Trivialer Fall, eine Karte reicht. |
| Kreis $S^1$ | 1 | Zwei Karten (zwei sich überlappende Bögen). |
| Sphäre $S^2$ | 2 | Standardatlas: stereographische Projektion vom Nord- und Südpol. |
| Torus $T^2$ | 2 | Quadrat $[0,1]^2$ mit gegenüberliegenden Seiten verklebt. |
| Möbius-Band | 2 | nicht orientierbar, Rand vorhanden. |
| Reell-projektiver Raum $\mathbb{RP}^n$ | $n$ | $S^n$ mit Antipodenidentifikation. |

Die ersten drei Beispiele sind kompakt und ohne Rand – genau die Klasse,
in der die [Poincaré-Vermutung](../../poincare/topologie/04-was-ist-poincare-vermutung.md)
formuliert wird.

## 4. Was eine Mannigfaltigkeit *nicht* ist

Eine Mannigfaltigkeit hat per Definition keine *Selbstdurchdringungen*,
*Spitzen* oder *Kanten*: An jedem Punkt sieht sie aus wie ein Stück
$\mathbb{R}^n$. Die Doppelkegelfläche $\{x^2 + y^2 = z^2\}$ ist im
Schnittpunkt $(0,0,0)$ keine Mannigfaltigkeit; ein Würfel ist es an den
Kanten und Ecken nicht. *Topologische* Mannigfaltigkeiten dürfen keine
solchen Singularitäten enthalten – im Ricci-Fluss treten sie aber
*während* der Entwicklung auf, was Perelmans Chirurgie reparieren muss.

## 5. Orientierbarkeit, Rand, Kompaktheit

Drei Eigenschaften treten in der Poincaré-Storyline immer wieder auf:

- **Orientierbarkeit:** Es gibt einen global konsistenten Drehsinn. $S^2$
  und $T^2$ sind orientierbar, das Möbius-Band nicht.
- **Rand:** Eine Mannigfaltigkeit *mit Rand* erlaubt Karten in den
  Halbraum $\mathbb{R}^n_{\ge 0}$. Der Rand $\partial M$ ist selbst eine
  Mannigfaltigkeit der Dimension $n - 1$.
- **Kompaktheit:** Geschlossen und beschränkt. Die Poincaré-Vermutung
  betrifft *kompakte, randlose, einfach zusammenhängende* 3-Mannigfaltigkeiten.

## 6. Warum der Begriff so mächtig ist

Auf einer Mannigfaltigkeit kann man – durch Karten – alle Konzepte der
Analysis lokal anwenden: Funktionen, Vektorfelder, Differentialformen,
Integrale, Differentialgleichungen. Wegen der Kartenverträglichkeit
liefern verschiedene Karten dasselbe Ergebnis – die Begriffe sind
*intrinsisch*. Das ist die technische Voraussetzung dafür, dass man auf
$M$ eine Riemannsche Metrik (siehe [Tangentialraum und Tensoren](tangentialraum-tensoren.md))
und damit Krümmung erklären kann.

## Querverweise

- Weiter zu: [Tangentialraum und Tensoren](tangentialraum-tensoren.md), [Krümmung von Flächen](kruemmung-flaechen-gauss.md).
- Anwendung in der Storyline: [Akt 1, Mannigfaltigkeiten](../../poincare/topologie/02-mannigfaltigkeiten.md), [Akt 1, Sphäre & einfacher Zusammenhang](../../poincare/topologie/03-sphaere-einfacher-zusammenhang.md).

## Quellen

- Lee, John M. (2013). *Introduction to Smooth Manifolds.* Springer GTM 218, 2. Auflage. Kap. 1–2.
- Tu, Loring W. (2011). *An Introduction to Manifolds.* Springer Universitext. Kap. 5–6.
- Spivak, Michael (1999). *A Comprehensive Introduction to Differential Geometry, Vol. 1.* Publish or Perish, 3. Auflage.
