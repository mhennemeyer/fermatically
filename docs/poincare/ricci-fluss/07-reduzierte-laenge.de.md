---
title: "Reduzierte Länge und reduziertes Volumen"
slug: poincare/ricci-fluss/07-reduzierte-laenge
series: poincare
part: 7
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - reduzierte-laenge
  - reduziertes-volumen
---

# Reduzierte Länge und reduziertes Volumen

!!! abstract "Zusammenfassung"
    Perelman ergänzt seine Entropie-Funktionale
    ([Artikel 05](05-perelman-entropie.md)) durch eine zweite,
    pfad-basierte Maschinerie: die **$\mathcal{L}$-Länge**, die
    daraus abgeleitete **reduzierte Länge** $\ell(q, \tau)$ und das
    **reduzierte Volumen** $\tilde V(\tau)$. Wie schon $\mathcal{W}$
    sind diese Größen unter dem Ricci-Fluss monoton, allerdings
    rückwärts in der Zeit – und sie liefern einen zweiten,
    *lokalen* Beweis des $\kappa$-Nichtkollaps
    ([Artikel 06](06-kappa-nichtkollaps.md)) sowie das technische
    Werkzeug, mit dem Blow-up-Folgen tatsächlich konvergieren.

## 1. Worum es geht

Bei einer Singularität bei $T < \infty$ ist der natürliche
Zeitparameter nicht mehr $t$, sondern die **Rest-Zeit**
$\tau = T - t$. Auf der gleichen Mannigfaltigkeit löst $g(\tau)$
die *Rückwärts*-Ricci-Gleichung

$$
\partial_\tau g_{ij} = 2\, R_{ij}.
$$

Perelman betrachtet auf $(M, g(\tau))$ den nichtlinearen Pfad-
Integral-Funktional

$$
\mathcal{L}(\gamma)
= \int_0^{\bar\tau} \sqrt{\tau}\,\Big(R\big(\gamma(\tau), \tau\big) + |\dot\gamma(\tau)|_{g(\tau)}^{2}\Big)\, d\tau,
$$

definiert auf Kurven $\gamma : [0, \bar\tau] \to M$ mit
$\gamma(0) = p$. Die Konstanten und das $\sqrt{\tau}$ sind exakt so
gewählt, dass die zugehörigen Euler-Lagrange-Gleichungen mit der
konjugierten Wärmegleichung verträglich werden – das ist das
formale Bindeglied zu $\mathcal{W}$.

## 2. $\mathcal{L}$-Geodäten

Eine Kurve $\gamma$, die $\mathcal{L}$ stationär macht, heißt
**$\mathcal{L}$-Geodäte**. Die Euler-Lagrange-Gleichung lautet

$$
\nabla_{\dot\gamma}\dot\gamma - \tfrac12\,\nabla R + \tfrac{1}{2\tau}\dot\gamma + 2\,\mathrm{Ric}(\dot\gamma, \cdot)^{\sharp} = 0.
$$

Wesentliche Eigenschaften:

- Reskalierte Geschwindigkeit $X(\tau) := \sqrt{\tau}\,\dot\gamma(\tau)$
  hat einen **endlichen Grenzwert** $X(0)$ in $T_p M$; jede
  $\mathcal{L}$-Geodäte ist also durch $(p, X(0))$ eindeutig
  bestimmt.
- Die **$\mathcal{L}$-Exponentialabbildung**
  $\mathcal{L}\exp_p^\tau : T_p M \to M$, $X(0) \mapsto \gamma(\tau)$,
  ist analog zur Riemannschen Exponentialabbildung.

## 3. Reduzierte Länge $\ell$

Sei $L(q, \bar\tau)$ das Infimum von $\mathcal{L}(\gamma)$ über alle
Kurven von $p$ nach $q$ in der Zeit $\bar\tau$. Die **reduzierte
Länge** ist

$$
\ell(q, \bar\tau) := \frac{L(q, \bar\tau)}{2\sqrt{\bar\tau}}.
$$

$\ell$ ist die richtige skalierungsinvariante Größe: unter
parabolischer Reskalierung $g \to \lambda^{-2} g$, $\tau \to \lambda^{-2}\tau$
bleibt $\ell$ unverändert. Sie ist außerdem **lokal Lipschitz**, fast
überall differenzierbar und erfüllt die Differentialungleichung

$$
\partial_\tau \ell - \Delta \ell + |\nabla \ell|^2 - R + \frac{n}{2\tau} \ge 0
\quad\text{(im distributionellen Sinn).}
$$

Diese Ungleichung ist das Pendant zur konjugierten Wärmegleichung
für $u = (4\pi\tau)^{-n/2} e^{-f}$ aus
[Artikel 05](05-perelman-entropie.md), §8.

## 4. Reduziertes Volumen

Das **reduzierte Volumen** zum Basispunkt $(p, T)$ ist

$$
\tilde V(\tau) := \int_M (4\pi\tau)^{-n/2}\, e^{-\ell(q, \tau)}\, dV_{g(\tau)}(q).
$$

Es misst, wie viel Masse einer auf $p$ konzentrierten
„Wahrscheinlichkeitsverteilung" nach Rückwärts-Zeit $\tau$ noch im
Volumen liegt.

## 5. Die Monotonie-Formel

!!! note "Monotonie-Theorem (Perelman 2002, §7)"
    Für jede glatte Lösung des Ricci-Flusses auf einem geschlossenen
    Intervall ist
    $$
    \tau \;\longmapsto\; \tilde V(\tau)
    $$
    **monoton fallend**. Gleichheit für alle $\tau$ in einem
    Intervall liefert ein **schrumpfendes Gradienten-Soliton**.

Das ist die zweite Säule neben Monotonie der $\mathcal{W}$-Entropie:
eine pfad-basierte, lokal definierbare Lyapunov-Funktion.

Die Modellrechnung auf flachem $\mathbb{R}^n$ liefert
$\ell(q, \tau) = |q-p|^2 / (4\tau)$, also
$\tilde V(\tau) \equiv 1$ – die Flachraum-Konstante. Auf jedem
nichttrivialen Fluss ist $\tilde V(\tau) \le 1$ ein Defizit-Mass
für Krümmung.

## 6. Anwendung 1: $\kappa$-Nichtkollaps neu bewiesen

Aus der Monotonie von $\tilde V$ folgt direkt
[Artikel 06](06-kappa-nichtkollaps.md) §3:

1. Wäre $g(t)$ in $(p, t)$ kollabiert, so läge fast die gesamte
   Masse von $\tilde V(\tau)$ in einer kleinen Umgebung – und
   $\tilde V(\tau)$ wäre für kleine $\tau$ nahe Null.
2. Wegen Monotonie wäre dann $\tilde V$ schon für **alle** späteren
   $\tau$ klein, was der Anfangsbedingung
   $\tilde V(\tau) \to 1$ für $\tau \to 0$ widerspricht.

Dieser Beweis ist *lokaler* als der Entropie-Beweis (er nutzt nur
Pfade von $p$ aus) und überträgt sich direkt auf
**Ricci-Fluss-mit-Surgery** (Perelman 0303109 §6).

## 7. Anwendung 2: Konvergenz von Blow-up-Folgen

Sei $(M, g_i(t), p_i)$ eine Folge parabolisch reskalierter Flüsse
um eine Singularität herum. Aus

- $\kappa$-Nichtkollaps (untere Volumen-Schranke),
- Hamilton-Kompaktheit (Krümmungs-Schranken),
- Monotonie von $\tilde V$ (verhindert Massen-Verlust),

folgt: nach Teilfolge konvergiert $(M, g_i(t), p_i)$ glatt im
Cheeger-Gromov-Sinn gegen einen vollständigen Ricci-Fluss-Limes –
genau die *antike $\kappa$-Lösung*, die in
[Artikel 06](06-kappa-nichtkollaps.md) §5 verwendet wird.

Ohne $\tilde V$ hätte man zwar Krümmungs-Schranken, aber keine
Kontrolle, dass der Limes vollständig ist – Punkte könnten „nach
Unendlich entweichen". Die Monotonie von $\tilde V$ ist die fehlende
Schranke.

## 8. Asymptotische Solitonen

Eine Konsequenz der Gleichheits-Aussage in der Monotonie-Formel:

!!! note "Asymptotisches-Soliton-Theorem (0211159 §11)"
    Jede antike $\kappa$-Lösung in Dimension 3 hat einen
    asymptotischen schrumpfenden Gradient-Ricci-Soliton-Limes, wenn
    man $\tau \to \infty$ und reskaliert.

Zusammen mit dem Splitting-Theorem ist das die **eigentliche**
Quelle der diskreten Klassifikation antiker $\kappa$-Lösungen aus
[Artikel 06](06-kappa-nichtkollaps.md) §6: Schrumpfende Solitonen
in Dimension 3 sind eine endliche Liste, und die ganze antike
$\kappa$-Lösung ist „nur" der Ricci-Fluss-Vorlauf zu einem solchen
Soliton.

## 9. Verhältnis zu $\mathcal{W}$

| | $\mathcal{W}$-Entropie | Reduzierte Länge / Volumen |
|--|------|------|
| Gegenstand | globale Funktion $f$ auf $M$ | Pfade $\gamma$ ab $p$ |
| Monotone Größe | $\mu(g(t), \tau)$ wächst in $t$ | $\tilde V(\tau)$ fällt in $\tau$ |
| Hauptanwendung | $\kappa$-Nichtkollaps (global) | $\kappa$-Nichtkollaps (lokal), Blow-up-Konvergenz |
| Erweiterbar auf Surgery | mit zusätzlicher Arbeit | direkt |
| Vorbild | log-Sobolev / Wärme-Kerne | klassische Riemannsche $\exp$ |

Beide Maschinen reden über dieselbe konjugierte Wärmegleichung –
nur einmal aus Sicht der **Dichte** $u$, einmal aus Sicht der
**charakteristischen Pfade** $\gamma$.

## 10. Was als Nächstes kommt

Mit den Werkzeugen Entropie, $\kappa$-Nichtkollaps, kanonische
Nachbarschaften und reduzierte Länge ist die analytische Maschinerie
abgeschlossen. Akt 3
([Beweis-Akt-Übersicht](../beweis/index.md)) verwendet sie, um
**Ricci-Fluss-mit-Surgery** zu konstruieren, dessen Stetigkeit zu
beweisen, **finite extinction time** für einfach zusammenhängende
3-Mannigfaltigkeiten zu zeigen und damit
Poincaré-Vermutung
([Akt 1, Artikel 04](../topologie/04-was-ist-poincare-vermutung.md))
sowie Geometrisierung
([Akt 1, Artikel 05](../topologie/05-geometrisierungs-vermutung.md))
zu beweisen.

## Quellen

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§7–8, 11.
- Grigori Perelman, *Ricci flow with surgery on three-manifolds*, [arXiv:math/0303109](https://arxiv.org/abs/math/0303109), §§5–6.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§6–7.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§14–24.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §3.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), Kap. 7.
- Bennett Chow et al., *The Ricci Flow: Techniques and Applications, Part I*, AMS (2007), Kap. 7.

## Querverweise

- Vorheriger Artikel: [κ-Nichtkollaps und kanonische Nachbarschaften](06-kappa-nichtkollaps.md)
- Akt-Übersicht: [Werkzeuge: Ricci-Fluss](index.md)
- Nächster Akt: [Der Beweis – Übersicht](../beweis/index.md)
