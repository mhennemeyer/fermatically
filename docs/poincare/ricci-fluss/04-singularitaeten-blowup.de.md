---
title: "Singularitäten und Blow-up-Limits"
slug: poincare/ricci-fluss/04-singularitaeten-blowup
series: poincare
part: 4
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - singularitaeten
  - blow-up
---

# Singularitäten und Blow-up-Limits

!!! abstract "Zusammenfassung"
    Der Ricci-Fluss bricht in endlicher Zeit ab, sobald die Krümmung
    irgendwo divergiert. Um zu verstehen, *wie* er abbricht, zoomt man
    an die Singularität heran: Hamiltons **Blow-up-Verfahren** liefert
    parabolisch reskalierte Limesflüsse. Die Klassifikation dieser
    Limesmodelle – insbesondere des $\kappa$-Lösungs-Begriffs – ist
    der Schlüssel zu Perelmans Surgery-Programm.

## 1. Wann bricht der Fluss ab?

Aus der Kurzzeitexistenz (siehe [Artikel 03](03-hamiltons-ricci-fluss.md))
folgt ein maximales Existenzintervall $[0, T)$. Der Endzeitpunkt $T$
ist durch ein **Krümmungs-Blow-up** charakterisiert:

> **Lemma (Hamilton 1982).** Falls $T < \infty$ das maximale
> Existenzintervall ist, so gilt
> $\displaystyle \limsup_{t \to T} \max_M \lvert\mathrm{Rm}(\cdot, t)\rvert = +\infty.$

Mit anderen Worten: Solange die volle Riemann-Krümmung beschränkt
bleibt, lässt sich der Fluss verlängern. Eine endliche Singularitätszeit
ist also stets ein **Krümmungs-Konzentrationspunkt**.

## 2. Typ-I- und Typ-II-Singularitäten

Hamilton (1995) klassifizierte Singularitäten nach dem
Wachstumsverhalten der Krümmung relativ zur Restzeit
$T - t$:

| Typ | Bedingung | Modellbild |
|---|---|---|
| I | $\sup_{M\times[0,T)} (T-t)\,\lvert\mathrm{Rm}\rvert < \infty$ | runder Schrumpf-Zylinder, $S^3$-Schrumpf |
| II | $\sup (T-t)\,\lvert\mathrm{Rm}\rvert = \infty$ | Degenerierte „Zigarren-" und Bryant-Solitonen |
| III | $\sup t\,\lvert\mathrm{Rm}\rvert < \infty$, $T = \infty$ | unendliche Zeit, hyperbolische Stücke |

In Dimension 3 sind nach Perelman alle endlichen Singularitäten
**vom Typ I oder II mit $\kappa$-Lösungs-Modell** – Typ III tritt
erst nach allen Surgeries als Langzeitverhalten auf.

## 3. Der Neckpinch als Modellsingularität

Das prototypische Beispiel: ein **Hantel-förmiger** $S^3$ mit dünnem
Hals. Unter dem Ricci-Fluss schrumpft der Hals schneller als die
Glocken; die Metrik konvergiert lokal gegen einen runden Zylinder
$S^2 \times \mathbb{R}$ mit verschwindendem $S^2$-Radius
(Angenent–Knopf 2004 als rigorose Konstruktion).

In geeigneten Koordinaten verhält sich der Halsradius wie
$r(t) \sim \sqrt{2(T-t)}$ – der reskalierte Fluss ist ein
schrumpfender Zylinder, also ein **Gradient-Schrumpf-Soliton**.

## 4. Parabolisches Reskalieren (Blow-up)

Hamiltons Idee, um in eine Singularität „hineinzuschauen": Wähle eine
Folge $(p_k, t_k)$ mit $t_k \to T$ und
$Q_k := \lvert\mathrm{Rm}(p_k, t_k)\rvert \to \infty$. Definiere die
**parabolisch reskalierten** Metriken

$$g_k(s) := Q_k \cdot g\!\left(t_k + \frac{s}{Q_k}\right),\qquad s \in [-Q_k\, t_k,\, 0].$$

Diese Skalierung ist die einzige, die den Ricci-Fluss invariant lässt
(Artikel 03, §5): mit $g$ erfüllt auch jedes $g_k$ den Fluss
$\partial_s g_k = -2\,\mathrm{Ric}(g_k)$. Die Krümmung im Aufpunkt wird
auf 1 normiert.

## 5. Hamiltons Kompaktheitssatz

Damit aus der Folge $(M, g_k(s), p_k)$ ein Limesfluss extrahiert
werden kann, braucht man zwei Voraussetzungen:

1. **Krümmungs-Schranken auf jedem Rückblick-Intervall** (gleichmäßig in $k$).
2. **Untere Injektivitätsradius-Schranke** $\mathrm{inj}(p_k) \ge \iota > 0$
   bezüglich $g_k$.

> **Satz (Hamilton, *Compactness*, 1995).** Unter diesen Voraussetzungen
> existiert eine Teilfolge, die in $C^\infty_{\mathrm{loc}}$ (im
> Sinne pointierter Cheeger–Gromov-Konvergenz) gegen einen
> vollständigen Ricci-Fluss $(M_\infty, g_\infty(s), p_\infty)$ auf einem
> Intervall $(-\infty, 0]$ konvergiert.

Das ist die Maschine, die **eine Singularität in einen
„unendlich-alten" Limesfluss übersetzt** – ein sog. **Antiker Fluss**
(ancient solution).

## 6. Wo der Kompaktheitssatz scheitert: Kollaps

Bedingung 2 ist die heikle: ohne untere Injektivitätsradius-Schranke
kann der Limes **kollabieren** (lokal niedrigerdimensional werden).
Beispiel: ein dünner Torus, dessen $S^1$-Faktor schrumpft – im Limes
bleibt nur der zweidimensionale Faktor übrig.

Genau hier setzt Perelmans Durchbruch an: das
**$\kappa$-Nichtkollaps-Theorem** (siehe
[Artikel 06](06-kappa-nichtkollaps.md)) erzwingt eine universelle
untere Injektivitätsradius-Schranke entlang der Singularität – und
macht damit Hamiltons Kompaktheitssatz erst anwendbar.

## 7. Antike $\kappa$-Lösungen

Die Grenzobjekte des Blow-up-Verfahrens sind in Dimension 3 nach
Perelman extrem stark eingeschränkt:

> **Definition.** Eine **antike $\kappa$-Lösung** ist ein vollständiger,
> nicht-flacher Ricci-Fluss $(M, g(s))$ auf $(-\infty, 0]$ mit
> nicht-negativer Krümmung, beschränkter Krümmung auf jedem
> kompakten Zeitintervall und $\kappa$-Nichtkollaps.

Perelman (2002, §11) klassifiziert in Dim 3 alle antiken
$\kappa$-Lösungen – sie sind **Quotienten der runden Sphäre**, der
**runden Zylinder** $S^2 \times \mathbb{R}$, oder spezielle
**Bryant-Solitonen** (rotationssymmetrische, asymptotisch zylindrische
Solitonen).

Konsequenz: Jede Singularität in Dim 3 sieht aus der Nähe wie eines
dieser drei Modelle – die **kanonische Nachbarschaft**, auf der
Perelmans Surgery-Konstruktion aufbaut.

## 8. Solitonen: stationäre Modellösungen

Selbstähnliche Lösungen des Ricci-Flusses heißen **Ricci-Solitonen**:

$$\mathrm{Ric}(g) + \nabla^2 f = \lambda\, g,\qquad \lambda \in \{-1, 0, +1\}.$$

- $\lambda > 0$: **schrumpfendes Soliton** (Modell für Typ-I-Singularitäten),
  z. B. die runde Sphäre, der runde Zylinder, der **Gauß-Soliton**
  $(\mathbb{R}^n, g_{\text{flat}}, f = \lvert x \rvert^2/4)$.
- $\lambda = 0$: **stationäres Soliton**, z. B. das **Cigar-Soliton**
  von Hamilton (Modell für Typ-II in Dim 2).
- $\lambda < 0$: **expandierendes Soliton**, Modell für
  Singularitätsauflösung nach Surgery.

Solitonen bilden den **Phasenraum** des Ricci-Flusses; das
$\mathcal{W}$-Funktional (siehe [Artikel 05](05-perelman-entropie.md))
identifiziert schrumpfende Solitonen als kritische Punkte.

## 9. Vom Modell zur Surgery

Der rote Faden für den Beweis der Geometrisierungs-Vermutung lautet:

1. Fluss läuft bis zur Singularität bei $t = T_1$.
2. Blow-up an der Singularität liefert eine antike $\kappa$-Lösung.
3. Klassifikation zeigt: lokales Bild ist Sphäre/Quotient, runder Hals
   oder Bryant-Kappe.
4. **Surgery:** Schneide bei einem Hals, klebe Standard-Kappen ein.
5. Restmannigfaltigkeit hat einfachere Topologie; Fluss läuft weiter.
6. Iteration; Akt 3 zeigt, dass der Prozess in endlicher Zeit endet
   und die Topologie rekonstruiert.

## Quellen

- Richard S. Hamilton, *The formation of singularities in the Ricci flow*, Surveys Diff. Geom. 2 (1995), 7–136.
- Sigurd Angenent & Dan Knopf, *An example of neckpinching for Ricci flow on $S^{n+1}$*, Math. Res. Lett. 11 (2004), 493–518.
- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §11.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§9–12.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§37–43.

## Querverweise

- Vorheriger Artikel: [Hamiltons Ricci-Fluss](03-hamiltons-ricci-fluss.md)
- Nächster Artikel: [Perelmans Entropie-Funktionale](05-perelman-entropie.md)
- Akt 3, Artikel 03: [Chirurgie am Ricci-Fluss](../beweis/03-chirurgie.md)
