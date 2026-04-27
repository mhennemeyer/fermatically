---
title: "Hamiltons Ricci-Fluss"
slug: poincare/ricci-fluss/03-hamiltons-ricci-fluss
series: poincare
part: 3
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - ricci-fluss
  - hamilton
---

# Hamiltons Ricci-Fluss

!!! abstract "Zusammenfassung"
    Richard Hamilton führte 1982 die Evolutionsgleichung
    $\partial_t g = -2\,\mathrm{Ric}(g)$ ein. Sie verformt eine
    Riemannsche Metrik so, dass sich Krümmung wie Wärme „ausgleicht".
    Hamilton bewies damit, dass jede 3-Mannigfaltigkeit mit positivem
    Ricci-Tensor einer sphärischen Raumform entspricht – die
    Blaupause für Perelmans Beweis.

## 1. Die Idee

Eine Metrik enthält Krümmungs-Inhomogenitäten – starke Krümmung an
einer Stelle, schwache anderswo. Hamilton stellte 1982 die Frage:
*Gibt es eine natürliche Bewegungsgleichung, die eine Metrik so
umverteilt, dass die Krümmung gleichmäßiger wird – ähnlich wie die
Wärmeleitungsgleichung Temperaturunterschiede ausgleicht?* Sein
Vorschlag:

$$\boxed{\,\frac{\partial g(t)}{\partial t} = -2\,\mathrm{Ric}\bigl(g(t)\bigr)\,}\quad\text{(Hamilton 1982).}$$

Anfangsbedingung: $g(0) = g_0$. Die Gleichung ist autonom in $g$ – die
rechte Seite hängt nur über die Ricci-Krümmung von $g$ selbst ab
(siehe [Artikel 02](02-kruemmung-ricci-tensor.md)).

## 2. Warum „minus zwei mal Ricci"?

Drei Beobachtungen erklären die Form der Gleichung.

**(a) Differential-topologische Natürlichkeit.** $\mathrm{Ric}$ ist
das einzige natürliche symmetrische $(0,2)$-Tensorfeld zweiter Ordnung
in $g$, das an jedem Punkt nur von den $\le 2$ Ableitungen der Metrik
abhängt. Das Vorzeichen $-2$ macht die Gleichung **parabolisch in der
Linearisierung** – ähnlich der Wärmegleichung $\partial_t u = \Delta u$.

**(b) Wärmeleitungs-Heuristik.** In harmonischen Koordinaten
($\Box x^k = 0$) gilt approximativ

$$\frac{\partial g_{ij}}{\partial t} = \Delta_g g_{ij} + \text{niedere Ordnungsterme}.$$

Die Metrik diffundiert also wie eine Skalargröße – mit dem Effekt,
dass Krümmungs-Spitzen geglättet werden.

**(c) Variationsprinzip.** Hamilton selbst motivierte die Gleichung
über Symmetrieargumente; Perelman zeigte später, dass der Ricci-Fluss
der **Gradientenfluss** des
$\mathcal{F}$-Funktionals (siehe [Artikel 05](05-perelman-entropie.md))
ist – ein nachträgliches Variationsprinzip.

## 3. Hamiltons Originalsatz (1982)

Im wegweisenden Paper *Three-manifolds with positive Ricci curvature*
zeigte Hamilton:

> **Satz (Hamilton 1982).** Sei $(M^3, g_0)$ eine geschlossene
> 3-Mannigfaltigkeit mit $\mathrm{Ric}(g_0) > 0$. Dann existiert der
> Ricci-Fluss $g(t)$ für alle $t \in [0, T)$, und der **normalisierte**
> Ricci-Fluss konvergiert für $t \to T$ gegen eine Metrik konstanter
> positiver Schnittkrümmung. Insbesondere ist $M$ diffeomorph zu
> einem sphärischen Raumform $S^3/\Gamma$.

— Hamilton, *J. Differential Geometry* 17 (1982), 255–306.

Der Beweis kombiniert Maximumprinzipien für Tensoren, eine sorgfältige
Analyse des Krümmungstensors unter dem Fluss und die Beobachtung,
dass in Dimension 3 der Ricci-Tensor den vollen Krümmungstensor
festlegt (Artikel 02, §6).

## 4. Kurzzeitexistenz und Eindeutigkeit

Die Gleichung ist nicht streng parabolisch (sie hat eine
Diffeomorphismus-Eichfreiheit), wird aber durch DeTurcks Trick zu
einer parabolischen Gleichung: man fügt einen Lie-Ableitungs-Term
hinzu, der eine Eichung fixiert. Damit folgt:

> **Kurzzeitexistenz.** Zu jeder glatten Anfangsmetrik $g_0$ auf einer
> geschlossenen Mannigfaltigkeit existiert ein $T > 0$ und eine
> eindeutige Lösung $g(t)$ des Ricci-Flusses für $t \in [0, T)$.

— Hamilton 1982 (Existenz), DeTurck 1983 (vereinfachter Beweis).

## 5. Skalierungsverhalten

Der Ricci-Fluss ist nicht skaleninvariant. Eine Reskalierung
$g \mapsto \lambda^2 g$ skaliert auch die Zeit:
$\mathrm{Ric}$ ist skaleninvariant, aber $\partial_t$ trägt die
$\lambda^{-2}$-Skala. Daraus folgt:

- Auf einem **Einstein-Anfangsraum** $\mathrm{Ric}(g_0) = \lambda g_0$
  bleibt $g(t) = (1 - 2\lambda t)\, g_0$. Bei $\lambda > 0$ kollabiert
  die Sphäre in endlicher Zeit zu einem Punkt; bei $\lambda < 0$
  expandiert der hyperbolische Raum unbegrenzt.
- Beim **normalisierten Ricci-Fluss**
  $\partial_t g = -2\,\mathrm{Ric} + \tfrac{2}{n}\bar R\, g$
  bleibt das Volumen konstant; Einstein-Metriken werden zu echten
  Fixpunkten.

## 6. Beispiele

**Runde Sphäre.** Auf $(S^3, g_{\mathrm{round}})$ ist
$\mathrm{Ric} = 2\, g_{\mathrm{round}}$. Lösung: $g(t) = (1 - 4t)\, g_{\mathrm{round}}$,
Singularität bei $T = 1/4$ (Schrumpf-Soliton).

**Flacher Torus.** Auf $T^3$ mit flacher Metrik ist
$\mathrm{Ric} = 0$, also $g(t) \equiv g_0$ – statisch.

**Hyperbolischer Raumform.** $\mathrm{Ric} = -2\, g$ ergibt
$g(t) = (1 + 4t)\, g$ – ewige Expansion.

**Zylinder $S^2 \times \mathbb{R}$.** Der $S^2$-Faktor schrumpft,
der $\mathbb{R}$-Faktor steht still – die Lösung degeneriert nach
endlicher Zeit zu einer Linie. Diese „Halsbildung" ist der
Modellfall der **Neckpinch-Singularität** (siehe
[Artikel 04](04-singularitaeten-blowup.md)).

## 7. Was der Fluss kontrolliert

Unter dem Ricci-Fluss erfüllen viele Krümmungsgrößen eigene
Evolutionsgleichungen, die zu **Maximumprinzip-Argumenten** einladen:

- $\partial_t R = \Delta R + 2\,\lvert\mathrm{Ric}\rvert^2$
  – Skalarkrümmung wächst mindestens wie Wärmegleichung mit
  Quellterm; insbesondere bleibt $R \ge 0$ erhalten.
- $\partial_t \mathrm{Ric} = \Delta_L \mathrm{Ric}$
  (Lichnerowicz-Laplace) – Ricci-Tensor diffundiert.
- Diametrale, Volumen- und Krümmungs-Schranken propagieren mit
  expliziten Vergleichsabschätzungen.

Das ist der Werkzeugkasten, mit dem Hamilton 1982 sein Resultat
bewies und den Perelman 2002–03 entscheidend erweiterte.

## 8. Was der Fluss *nicht* kann

Drei Probleme blieben nach Hamilton offen und definierten das
Forschungsprogramm der nächsten 20 Jahre:

1. **Singularitätenbildung.** Der Fluss bricht in endlicher Zeit ab,
   bevor eine glatte Grenzmetrik erreicht wird – etwa beim
   Neckpinch.
2. **Kollaps.** Volumen kann lokal verschwinden, sodass keine
   sinnvollen Vergleichssätze mehr greifen.
3. **Topologie-Wechsel.** Um über die Singularität hinaus
   weiterzulaufen, muss man den Raum zerschneiden („Surgery"),
   topologisch verändern, dann den Fluss neu starten.

Die Werkzeuge zur Lösung – $\mathcal{F}$- und $\mathcal{W}$-Entropie,
$\kappa$-Nichtkollaps, reduzierte Länge, kanonische Nachbarschaften –
folgen in den Artikeln 04–07.

## Quellen

- Richard S. Hamilton, *Three-manifolds with positive Ricci curvature*, J. Differential Geom. 17 (1982), 255–306.
- Richard S. Hamilton, *The formation of singularities in the Ricci flow*, Surveys Diff. Geom. 2 (1995), 7–136.
- Bennett Chow & Dan Knopf, *The Ricci Flow: An Introduction*, AMS Math. Surveys 110 (2004).
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §3.

## Querverweise

- Vorheriger Artikel: [Krümmung und Ricci-Tensor](02-kruemmung-ricci-tensor.md)
- Nächster Artikel: [Singularitäten und Blow-up-Limits](04-singularitaeten-blowup.md)
- Akt 1, Artikel 04: [Was ist die Poincaré-Vermutung?](../topologie/04-was-ist-poincare-vermutung.md)
