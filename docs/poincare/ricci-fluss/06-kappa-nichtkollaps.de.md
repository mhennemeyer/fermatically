---
title: "κ-Nichtkollaps und kanonische Nachbarschaften"
slug: poincare/ricci-fluss/06-kappa-nichtkollaps
series: poincare
part: 6
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - kappa-nichtkollaps
  - kanonische-nachbarschaften
---

# κ-Nichtkollaps und kanonische Nachbarschaften

!!! abstract "Zusammenfassung"
    Hamiltons Kompaktheitssatz ([Artikel 04](04-singularitaeten-blowup.md))
    liefert Blow-up-Limits **nur**, wenn das Volumen lokal nicht
    entartet. Genau diese Schranke garantiert Perelmans
    **$\kappa$-Nichtkollaps-Theorem**: Auf jeder endlichen Skala bleibt
    das Verhältnis Volumen/Krümmungs-Radius über einer universellen
    Konstanten $\kappa>0$. Aus dem Theorem zusammen mit
    Hamilton-Harnack folgt die **Klassifikation antiker
    $\kappa$-Lösungen** in Dimension 3 – und damit, dass jeder
    Hochkrümmungsbereich eines drei-dimensionalen Ricci-Flusses einer
    von endlich vielen Modellgeometrien (Hals, Kappe, sphärische
    Raumform) ähnelt. Diese „kanonischen Nachbarschaften" sind die
    geometrische Vorbedingung für Surgery
    ([Akt 3, Artikel 03](../beweis/03-chirurgie.md)).

## 1. Das Kollapsproblem

Eine Folge $(M_i, g_i, p_i)$ von Riemannschen Mannigfaltigkeiten
**kollabiert** in $p_i$ auf Skala $r$, wenn

$$
\frac{\mathrm{Vol}\big(B_{g_i}(p_i, r)\big)}{r^{n}} \longrightarrow 0,
$$

obwohl die Krümmung in $B_{g_i}(p_i, r)$ beschränkt bleibt
($|\mathrm{Rm}|\le r^{-2}$). Anschaulich werden Richtungen so dünn,
dass die Mannigfaltigkeit lokal zu einer niederdimensionalen
Struktur entartet (z. B. ein langer dünner Zylinder in eine Kreislinie).

Für die Blow-up-Analyse aus
[Artikel 04](04-singularitaeten-blowup.md) ist Kollaps fatal: ohne
untere Volumen-Schranke versagt Hamiltons Kompaktheitssatz, und der
Blow-up-Limes existiert in der Klasse der Riemannschen
Mannigfaltigkeiten gar nicht – er degeneriert auf einen Raum
niedrigerer Dimension.

## 2. Definition: $\kappa$-Nichtkollaps

Sei $\kappa > 0$ und $r_0 > 0$. Ein Ricci-Fluss $(M, g(t))$ heißt in
$(p, t)$ **$\kappa$-nichtkollabiert auf Skala $r_0$**, wenn für jedes
$0 < r < r_0$ gilt:

$$
\sup_{B_{g(t)}(p, r)} |\mathrm{Rm}| \le r^{-2}
\;\Longrightarrow\;
\frac{\mathrm{Vol}\big(B_{g(t)}(p, r)\big)}{r^{n}} \ge \kappa.
$$

In Worten: Wenn die Krümmung im Ball auf Skala $r$ höchstens $r^{-2}$
ist, dann ist der Ball mindestens $\kappa$-voll.

## 3. Perelmans $\kappa$-Nichtkollaps-Theorem

!!! note "Theorem (Perelman 2002, §4)"
    Sei $g(t)$ eine glatte Lösung des Ricci-Flusses auf einer
    geschlossenen $n$-Mannigfaltigkeit $M$, definiert auf
    $[0, T)$ mit $T < \infty$. Dann existiert ein
    $\kappa = \kappa(g(0), T) > 0$, sodass $g(t)$ in jedem Punkt und
    auf jeder Skala $r < \sqrt{T}$ $\kappa$-nichtkollabiert ist.

Das Theorem gilt **ohne** Voraussetzungen an die Krümmung – es
folgt allein aus der Monotonie der $\mathcal{W}$-Entropie und ist
damit ein qualitativer Erhaltungssatz des Flusses selbst.

## 4. Beweisstrategie über $\mathcal{W}$

Die Idee verbindet [Artikel 05](05-perelman-entropie.md) mit der
Volumen-Geometrie:

1. Wäre der Fluss in $(p, t)$ kollabiert, ließe sich eine Testfunktion
   $f$ konstruieren, die Masse auf $B(p, r)$ konzentriert.
2. Direktes Einsetzen in $\mathcal{W}(g, f, \tau)$ mit $\tau \sim r^2$
   liefert dann

   $$
   \mu(g(t), r^2) \le \mathcal{W}(g(t), f, r^2) \to -\infty
   \quad\text{für}\quad
   \frac{\mathrm{Vol}\, B(p, r)}{r^n} \to 0.
   $$

3. Andererseits ist $\mu(g(t), \tau)$ entlang des Ricci-Flusses
   **monoton wachsend** und durch $\mu(g(0), \tau + t)$
   nach unten beschränkt.

Der Widerspruch zwischen 2 und 3 erzwingt ein universelles
$\kappa(g(0), T)$. Das Argument findet sich in
Perelman 0211159 §4 sowie ausgeführt in Kleiner–Lott §13 und
Morgan–Tian §8.

## 5. Lokale Variante und antike Lösungen

Die obige Aussage gilt global. Für die Singularitätsanalyse
([Artikel 04](04-singularitaeten-blowup.md)) braucht man eine
**lokale**, **antike** Variante:

!!! note "Korollar"
    Jeder Blow-up-Limes einer endlich-Zeit-Singularität eines
    Ricci-Flusses auf einer geschlossenen 3-Mannigfaltigkeit ist
    eine **antike $\kappa$-Lösung**: vollständig, definiert für
    $t \in (-\infty, 0]$, mit nichtnegativer Schnittkrümmung,
    $\kappa$-nichtkollabiert auf allen Skalen und beschränkter
    Krümmung auf jedem kompakten Zeitintervall.

Antike $\kappa$-Lösungen erben die Volumen-Schranke aus dem
$\kappa$-Nichtkollaps-Theorem im Limes; ohne sie wäre der Limes
nicht einmal ein Riemannscher Raum.

## 6. Klassifikation antiker $\kappa$-Lösungen in Dimension 3

Mit dem $\kappa$-Nichtkollaps zusammen mit Hamiltons differentieller
Harnack-Ungleichung und der Splitting-Theorem-Maschinerie zeigt
Perelman (0211159 §11):

!!! note "Klassifikationssatz"
    Eine antike $\kappa$-Lösung in Dimension 3 ist eine der folgenden:

    - der **schrumpfende runde Zylinder** $S^2 \times \mathbb{R}$,
    - sein $\mathbb{Z}_2$-Quotient,
    - die **Bryant-Soliton**-artige rotationssymmetrische Kappe,
    - der **runde schrumpfende** $S^3$ oder ein sphärischer Quotient,
    - oder jeder Ball ist asymptotisch ein Hals oder eine Kappe.

Diese diskrete Liste ist die geometrische Substanz, aus der die
„kanonischen Nachbarschaften" gewonnen werden.

## 7. Kanonische Nachbarschaften

Für $\varepsilon > 0$ klein definiert Perelman drei Modelltypen:

| Typ | Geometrie | Topologie |
|-----|-----------|-----------|
| $\varepsilon$-**Hals** | $\varepsilon$-nahe an einem Stück $S^2 \times [-\varepsilon^{-1}, \varepsilon^{-1}]$ des runden Zylinders | $S^2 \times I$ |
| $\varepsilon$-**Kappe** | $\varepsilon$-nahe an einer Bryant-artigen Halbkugel mit angehängtem Hals | $D^3$ oder $\mathbb{RP}^3 \setminus \overline{D^3}$ |
| **Sphärische Raumform** | Ganze Komponente $\varepsilon$-nahe an einem runden Quotienten $S^3/\Gamma$ | $S^3/\Gamma$ |

!!! note "Theorem über kanonische Nachbarschaften (0211159 §12)"
    Zu jedem $\varepsilon > 0$ existiert $r_0 > 0$, sodass auf einem
    Ricci-Fluss auf einer geschlossenen 3-Mannigfaltigkeit jeder
    Punkt $(x, t)$ mit $|\mathrm{Rm}|(x,t) \ge r_0^{-2}$
    eine $\varepsilon$-Nachbarschaft eines der drei Typen besitzt.

Hochkrümmungs-Bereiche sind also nicht beliebig – sie sehen, bis
auf $\varepsilon$, immer wie eine endliche Liste von Modellen aus.

## 8. Bedeutung für Surgery

Surgery
([Akt 3, Artikel 03](../beweis/03-chirurgie.md)) schneidet entlang
eines $\varepsilon$-Halses und klebt Kappen ein. Damit das Verfahren
**wohldefiniert** ist, müssen drei Bedingungen erfüllt sein:

1. Hochkrümmungsbereiche sind **klassifiziert**
   (Klassifikationssatz, §6).
2. Hochkrümmungsbereiche besitzen **kanonische Nachbarschaften**
   (§7).
3. Nach jedem Schnitt ist das Ergebnis **erneut $\kappa'$-nichtkollabiert**
   für ein nur leicht verschlechtertes $\kappa'$.

Punkt 3 erfordert eine *Ricci-Fluss-mit-Surgery*-Variante des
$\kappa$-Nichtkollaps-Theorems – sie ist Gegenstand von
Perelman 0303109 §5–§7.

## 9. Was die Entropie und was die reduzierte Länge tut

Es gibt **zwei** unabhängige Beweise des $\kappa$-Nichtkollaps:

- über die $\mathcal{W}$-Entropie ([Artikel 05](05-perelman-entropie.md), §4 oben),
- über die **reduzierte Länge** $\ell(q, \tau)$ und das **reduzierte Volumen**
  $\tilde V(\tau)$ ([Artikel 07](07-reduzierte-laenge.md)).

Beide nutzen denselben Mechanismus – Monotonie einer skalierungs-
invarianten Größe entlang des Flusses. Die reduzierte Länge ist für
**lokale** Aussagen und für Blow-up-Argumente besser geeignet, weil
sie pfad-basiert konstruiert ist und nicht von einer globalen
Testfunktion abhängt.

## Quellen

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§4, 7, 11–12.
- Grigori Perelman, *Ricci flow with surgery on three-manifolds*, [arXiv:math/0303109](https://arxiv.org/abs/math/0303109), §§5–7.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§8, 9, 11.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§13, 25–28, 41–48.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §§4, 6.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), Kap. 8.

## Querverweise

- Vorheriger Artikel: [Perelmans Entropie-Funktionale](05-perelman-entropie.md)
- Nächster Artikel: [Reduzierte Länge und reduziertes Volumen](07-reduzierte-laenge.md)
- Akt 3, Artikel 03: [Chirurgie am Ricci-Fluss](../beweis/03-chirurgie.md)
