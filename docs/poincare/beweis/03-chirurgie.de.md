---
title: "Ricci-Fluss mit Chirurgie"
slug: poincare/beweis/03-chirurgie
series: poincare
part: 3
act: beweis
date: 2026-04-27
status: draft
lang: de
tags:
  - chirurgie
  - surgery
  - ricci-fluss
  - perelman
---

# Ricci-Fluss mit Chirurgie

> *„We construct a solution which is a smooth Ricci flow on its time-of-definition,
> punctuated by a discrete set of surgery times at which the metric is modified."*
> — Perelman, *Ricci flow with surgery on three-manifolds*, arXiv:math/0303109 (2003)

In [Artikel 02](02-singularitaeten-dim3.md) haben wir die Singularitäten des
Ricci-Flusses in Dimension 3 lokal verstanden: Jede Hochkrümmungsregion sieht
wie ein Hals, eine Kappe oder eine sphärische Raumform aus. In diesem Artikel
folgen wir dem zweiten Perelman-Preprint *0303109* und konstruieren daraus
einen **globalen Fluss mit Chirurgie**, der über jede Singularität hinweg
weiterläuft – das technische Herzstück des Beweises der
Geometrisierungs-Vermutung.

## 1. Die Idee: Schneiden vor der Singularität

Hamiltons Originalprogramm scheiterte an Hindernis **O3** aus
[Artikel 01](01-hamiltons-programm.md): Singularitäten lokal zu verstehen
genügt nicht; man muss sie *operativ* entfernen, ohne den Beweis durch immer
neue Sonderfälle zu sprengen.

Perelmans Lösung ist verblüffend einfach im Prinzip:

1. **Beobachte** den Fluss, bis die Krümmung an einer ersten Stelle eine
    feste Schranke $\Omega$ überschreitet (kurz vor der Singularität).
2. **Lokalisiere** die Hochkrümmungsregion mit Hilfe des kanonischen
    Nachbarschaftssatzes – sie zerfällt in Hälse, Kappen und kompakte
    Komponenten sphärischer Raumformen.
3. **Schneide** entlang einer mittleren 2-Sphäre eines jeden Halses heraus
    und verklebe die zwei Enden mit einer **Standardlösung** (einer fest
    gewählten, expliziten Metrik auf $D^3$).
4. **Wirf** kompakte Komponenten weg, die bereits als sphärische Raumform
    erkannt sind – sie sind topologisch identifiziert und ändern den Fluss
    nicht mehr.
5. **Setze** den Ricci-Fluss auf der so modifizierten Mannigfaltigkeit
    glatt fort, bis die nächste Singularität auftritt.

Das Ergebnis ist eine Folge $(M_t, g(t))$ glatter Ricci-Flüsse auf
Zeitintervallen $[t_{i-1}, t_i]$, getrennt durch eine **diskrete** Menge von
Chirurgie-Zeiten $0 < t_1 < t_2 < \dots$.

## 2. δ-Hälse und der Schnittort

Ein präziser Schnitt erfordert einen Hals, der „dünn genug" ist. Sei
$\delta > 0$ ein Parameter (klein).

**Definition (δ-Hals).** Ein Punkt $(x, t)$ liegt in einem $\delta$-Hals der
Skala $r$, falls die parabolische Reskalierung von $g(t)$ um $x$ in der
$C^{\lfloor 1/\delta \rfloor}$-Norm $\delta$-nahe an dem
runden zylindrischen Modell $S^2_1 \times (-1/\delta, 1/\delta)$ liegt.

**Lemma (Existenz eines $\delta$-Halses, 0303109 §4).** Für jedes
hinreichend kleine $\delta$ gibt es eine Krümmungsschranke $h(\delta)$, so
dass jeder Punkt mit $|\mathrm{Rm}|(x,t) \ge h(\delta)$ und in einem
$\varepsilon$-Hals (im Sinne von Akt 2, [Artikel 06](../ricci-fluss/06-kappa-nichtkollaps.md))
einen *zentralen* $\delta$-Hals enthält.

Der Schnittort wird auf der mittleren 2-Sphäre $\Sigma$ eines solchen Halses
gewählt. Die feinere Bedingung $\delta \ll \varepsilon$ stellt sicher, dass
der Hals lang und dünn genug ist, um eine Standardlösung einzukleben, ohne
die zukünftige Krümmungsentwicklung zu stören.

## 3. Die Standardlösung

Die *Standardlösung* ist eine fest gewählte, vollständige, asymptotisch
zylindrische Metrik $\bar g$ auf $\mathbb{R}^3$ mit folgenden Eigenschaften
(0303109 §2, ausgearbeitet in Cao–Zhu §7.3):

- $\bar g$ ist rotationssymmetrisch, hat positive Schnittkrümmung.
- Außerhalb einer großen Kugel ist $(\mathbb{R}^3, \bar g)$ isometrisch zum
    runden Halbzylinder $S^2_1 \times [0, \infty)$.
- Der Ricci-Fluss mit Anfangsdatum $\bar g$ existiert glatt auf $[0, 1)$,
    schrumpft zu einem Punkt bei $t = 1$ und ist $\kappa$-nicht-kollabiert.

Die Standardlösung dient als **Modell-Kappe**: Nach dem Schnitt wird der
ungewünschte Halsteil durch ein Stück $\bar g$ ersetzt, glatt verklebt durch
eine Cut-off-Funktion. Die Existenz und Eindeutigkeit ihres Flusses ist ein
eigenes technisches Theorem (Cao–Zhu, Kleiner–Lott Kap. 12).

## 4. Der Chirurgie-Algorithmus

Die Konstruktion hängt von drei Parameter-Folgen ab, die *gleichzeitig*
gewählt werden müssen:

| Parameter | Rolle |
|-----------|-------|
| $\varepsilon_i \to 0$ | Genauigkeit der kanonischen Nachbarschaft |
| $\delta_i \to 0$ | Halsgüte am Schnittort, $\delta_i \ll \varepsilon_i$ |
| $r_i \to 0$ | Skala, ab der kanonische Nachbarschaften gelten |
| $h_i \to 0$ | Schnitt-Schranke, $h_i \ll \delta_i r_i$ |

**Definition (Ricci-Fluss mit Chirurgie).** Eine Familie
$\{(M_t, g(t))\}_{t \ge 0}$ heißt *Ricci-Fluss mit $(r, \delta)$-Chirurgie*,
wenn auf jedem Intervall $[t_{i-1}, t_i)$ glatt nach $\partial_t g = -2\,\mathrm{Ric}$
geflossen wird, an den Zeiten $t_i$ Chirurgie an allen $\delta_i$-Hälsen
durchgeführt wird, und die kanonische-Nachbarschafts-Eigenschaft mit
Parametern $(\varepsilon_i, r_i)$ bis $t_i$ erhalten bleibt.

## 5. Das Surgery-Theorem (0303109 §5)

**Theorem (Perelman, Surgery existiert global).** Für jede kompakte,
orientierte 3-Mannigfaltigkeit $(M, g_0)$ existieren Folgen
$\varepsilon_i, \delta_i, r_i, h_i \to 0$, so dass ein Ricci-Fluss mit
$(r, \delta)$-Chirurgie auf $[0, \infty)$ existiert.

Die zentrale Schwierigkeit ist die **Induktionsschleife**: Damit kanonische
Nachbarschaften beim Schritt $i \to i+1$ erhalten bleiben, braucht man
$\kappa$-Nichtkollaps **trotz** der vorangegangenen Chirurgien. Perelman
zeigt:

- Lokaler $\kappa$-Nichtkollaps ([Artikel 06 in Akt 2](../ricci-fluss/06-kappa-nichtkollaps.md))
    überträgt sich auf den Fluss mit Chirurgie, sofern $\delta_i$ klein
    genug gewählt ist.
- Die Anzahl der Chirurgien auf jedem endlichen Zeitintervall ist endlich,
    weil jede einen festen Volumensbetrag entfernt
    ($\ge c\, h_i^3$).

## 6. Was die Chirurgie *nicht* zerstört

Die Chirurgie ist so entworfen, dass sie alle für den Beweis essentiellen
Strukturen erhält:

- **Hamilton–Ivey-Pinching** (siehe [Artikel 02](02-singularitaeten-dim3.md))
    bleibt nach jedem Chirurgieschritt gültig, weil die Standardlösung
    selbst positive Krümmung hat.
- **κ-Nichtkollaps** wird mit einer kleineren, aber positiven Konstante
    $\kappa'$ erhalten.
- **Topologische Information**: Jede entfernte Komponente ist eine
    sphärische Raumform $S^3/\Gamma$, jede Chirurgie ersetzt einen Hals
    $S^2 \times I$ durch zwei Kappen $D^3$. Beides sind die zwei
    Standardoperationen einer **Prim-Zerlegung** (vgl.
    [Geometrisierungs-Vermutung](../topologie/05-geometrisierungs-vermutung.md)).

Die Topologie der ursprünglichen Mannigfaltigkeit lässt sich daher exakt aus
den entfernten Stücken plus dem Endzustand des Flusses rekonstruieren – das
ist die Brücke, die in [Artikel 06](06-poincare-aus-geometrisierung.md)
geschlagen wird.

## 7. Was bleibt zu zeigen

Mit dem Surgery-Theorem ist der **Fluss als analytisches Objekt** gerettet.
Offen bleiben zwei Fragen, die Akt 3 beantworten muss:

- **Was passiert für $t \to \infty$?** – behandelt in
    [Artikel 04: Long-time-Verhalten](04-long-time-verhalten.md).
- **Stoppt der Fluss in endlicher Zeit, wenn $M$ einfach zusammenhängend
    ist?** – Perelmans dritter Preprint *0307245*, behandelt in
    [Artikel 05: Endliche Extinktion](05-endliche-extinktion.md).

## Zusammenfassung

| Hindernis (Akt 1, [Artikel 01](01-hamiltons-programm.md)) | Lösung in diesem Artikel |
|-----------|--------------------------|
| O3: Singularitäten *operativ* entfernen | Chirurgie-Algorithmus mit $(\delta, r, h)$-Parametern |
| O3': Algorithmus liefert nur endlich viele Schnitte | Volumens-Argument $\ge c\, h^3$ pro Chirurgie |
| O3'': Pinching/κ-Nichtkollaps nach Chirurgie | Standardlösung hat positive Krümmung; lokaler κ-Nichtkollaps überträgt sich |
| O3''': Topologie wird verfolgbar | Schnitte = Prim-Zerlegung, entfernte Stücke = $S^3/\Gamma$ |

## Querverweise

- Vorher: [Singularitätsanalyse Dim 3](02-singularitaeten-dim3.md) – stellt die kanonischen Nachbarschaften bereit.
- Werkzeuge: [κ-Nichtkollaps](../ricci-fluss/06-kappa-nichtkollaps.md), [Reduzierte Länge](../ricci-fluss/07-reduzierte-laenge.md).
- Topologie: [Geometrisierungs-Vermutung](../topologie/05-geometrisierungs-vermutung.md), [Was ist die Poincaré-Vermutung?](../topologie/04-was-ist-poincare-vermutung.md).
- Nächster Artikel: [Long-time-Verhalten und dünn-dick-Zerlegung](04-long-time-verhalten.md).

## Quellen

- Perelman, G. (2003). *Ricci flow with surgery on three-manifolds*. arXiv:math/0303109.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. AMS, Kap. 13–17.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, 2587–2855, §§57–72.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10, §7.
- Hamilton, R. (1997). *Four-manifolds with positive isotropic curvature*. Comm. Anal. Geom. 5 – Original der Surgery-Idee in Dim 4.
