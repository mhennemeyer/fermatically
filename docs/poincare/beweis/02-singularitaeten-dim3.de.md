---
title: "Singularitätsanalyse in Dimension 3"
slug: poincare/beweis/02-singularitaeten-dim3
series: poincare
part: 2
act: beweis
date: 2026-04-27
status: draft
lang: de
tags:
  - dim-3
  - kappa-loesungen
  - kanonische-nachbarschaften
  - hamilton-ivey
---
# Singularitätsanalyse in Dimension 3

!!! abstract "Zusammenfassung"
    Dieser Artikel löst die beiden Hindernisse **H2** (Klassifikation
    antiker $\kappa$-Lösungen) und **H3** (kanonischer
    Nachbarschaftssatz) aus
    [Artikel 01](01-hamiltons-programm.md). Er kombiniert drei
    Bausteine: (i) das **Hamilton–Ivey-Pinching**, das in Dimension 3
    asymptotisch nichtnegative Krümmung erzwingt, (ii) das
    [$\kappa$-Nichtkollaps-Theorem](../ricci-fluss/06-kappa-nichtkollaps.md)
    von Perelman, das Volumen-Untergrenzen liefert, und (iii) die
    [reduzierte $\mathcal{L}$-Geometrie](../ricci-fluss/07-reduzierte-laenge.md),
    die Blow-up-Limits als $\kappa$-Lösungen identifiziert. Daraus
    folgen die **Klassifikation antiker $\kappa$-Lösungen in Dim 3**
    und der **kanonische Nachbarschaftssatz**: an jedem Punkt mit
    hinreichend großem Krümmungsskalar gleicht der Fluss bis auf
    $\varepsilon$ einem von drei Modellen – Hals, Kappe oder
    sphärische Raumform.

## 1. Hamilton–Ivey-Pinching: positive Krümmung gewinnt

Auf einer geschlossenen 3-Mannigfaltigkeit hat der Riemann-Tensor nur
drei unabhängige Eigenwerte $\lambda_1 \leq \lambda_2 \leq \lambda_3$
des Krümmungsoperators. Hamilton 1995 / Ivey 1993 zeigten:

> **Pinching-Schätzung.** Für jeden Ricci-Fluss auf einer
> geschlossenen 3-Mannigfaltigkeit existiert eine Funktion
> $\phi:[0,\infty)\to\mathbb{R}$ mit $\phi(s)/s \to 0$ für
> $s\to\infty$, sodass an jedem Raumzeit-Punkt
> $$
>   \lambda_1 \;\geq\; -\phi(\lambda_3).
> $$

Inhaltlich: die negativste Krümmungsrichtung kann nur logarithmisch
schlechter sein als die positivste. Insbesondere wird **bei
explodierender Krümmung jede Schnittkrümmung im Limes nichtnegativ**.
Dies ist der Grund, warum die Singularitätsanalyse in Dimension 3 –
und nur dort – mit der ferneren Theorie nichtnegativ gekrümmter
antiker Lösungen geführt werden kann.

## 2. Antike $\kappa$-Lösungen: die Liste der Modelle

Eine **antike Lösung** ist ein Ricci-Fluss $(M, g(t))_{t \in (-\infty, 0]}$
mit beschränkter Krümmung auf endlichen Zeitintervallen. Sie heißt
**$\kappa$-nichtkollabiert**, wenn auf jeder Skala $r$
$$
\frac{\mathrm{Vol}(B(p,t,r))}{r^n} \;\geq\; \kappa
\quad\text{für}\quad |\mathrm{Rm}|\leq r^{-2}.
$$

Für Blow-up-Limits gilt dank Hamilton–Ivey zusätzlich
$\mathrm{Rm}\geq 0$.

> **Klassifikation (Perelman 0211159 §11).** Jede antike
> $\kappa$-Lösung in Dimension 3 mit nichtnegativem
> Krümmungsoperator ist eine der folgenden:
>
> 1. der **runde Zylinder** $S^2 \times \mathbb{R}$ oder sein
>    $\mathbb{Z}_2$-Quotient;
> 2. ein **schrumpfendes sphärisches Quotient** $S^3/\Gamma$;
> 3. ein **antikes nicht-zylindrisches Modell** mit nichtkompakter
>    Topologie $\mathbb{R}^3$, asymptotisch zylindrisch (Bryant-artig).

Beweisidee: Hamilton-Harnack + Toponogov-Vergleich liefern, dass die
Schnittkrümmung an Unendlichkeit lokal vom Zylinder dominiert wird;
die $\mathcal{L}$-Geometrie zeigt, dass jeder asymptotische Soliton
einer dieser Modelle ist; das $\kappa$-Nichtkollaps schließt
„Zigarren" (Hamilton-Soliton in Dim 2) und damit eine vierte Klasse
aus.

## 3. Geometrische Bausteine: Hals, Kappe, Raumform

Aus der Klassifikation extrahiert Perelman drei lokale
**Modellgeometrien**, an denen jede Hochkrümmungsregion gemessen
wird.

| Modell | Lokale Form | Skala |
|--------|-------------|-------|
| **$\varepsilon$-Hals** | $\varepsilon$-nahe an $S^2 \times [-\varepsilon^{-1}, \varepsilon^{-1}]$, runde $S^2$ | $r = R^{-1/2}$ |
| **$\varepsilon$-Kappe** | Diffeomorph zu $D^3$ oder $\mathbb{RP}^3 \setminus \overline{B}$, am offenen Ende ein $\varepsilon$-Hals | $r$ |
| **Sphärische Raumform** | $S^3/\Gamma$ mit fast konstanter positiver Schnittkrümmung | gesamte Komponente |

Hierbei steht $R$ für den Krümmungsskalar am Mittelpunkt des Halses.
Die genaue Definition (Cao–Zhu, Morgan–Tian) verlangt
$\varepsilon$-Nähe in der $C^{[1/\varepsilon]}$-Topologie nach
parabolischer Reskalierung.

## 4. Der kanonische Nachbarschaftssatz

> **Satz (Perelman 0211159 §12.1).** Zu $\varepsilon > 0$ gibt es
> eine Funktion $r_0(t) > 0$, sodass: jeder Punkt $(x,t)$ in einem
> Ricci-Fluss auf einer geschlossenen 3-Mannigfaltigkeit mit
> $R(x,t) \geq r_0(t)^{-2}$ liegt in einer **kanonischen
> Nachbarschaft**, d. h. nach Reskalierung mit Faktor $R(x,t)$ ist
> sie $\varepsilon$-nahe an einem der drei Modelle (Hals, Kappe,
> sphärische Raumform).

Beweisstrategie (Skizze):

1. Annahme zur Widerspruchsführung: es gibt eine Folge $(x_i, t_i)$
   mit $R(x_i,t_i) \to \infty$, deren Reskalierung *kein* Modell
   ergibt.
2. Mit Hamilton-Kompaktheit (Volumenuntergrenze aus
   $\kappa$-Nichtkollaps, Krümmungsschranken aus dem
   Pinching-Argument) konvergiert eine Teilfolge im
   Cheeger–Gromov-Sinn.
3. Dank $\mathcal{L}$-Geometrie ist der Limes eine antike
   $\kappa$-Lösung mit $\mathrm{Rm}\geq 0$ – also nach §2 eines der
   drei Modelle.
4. Widerspruch zur Annahme.

Der Beweis verwendet *alle* Werkzeuge aus Akt 2 zusammen: ohne
Entropie kein $\kappa$-Nichtkollaps (Schritt 2), ohne reduzierte
Länge keine Konvergenz zu antiken Solitonen (Schritt 3), ohne
Hamilton–Ivey kein nichtnegativer Krümmungsoperator im Limes.

## 5. Lokale Konsequenz: Hochkrümmung ist kanonisch

Zwei direkte Korollare strukturieren den Fluss kurz vor einer
Singularität:

**5.1 Strukturelle Zerlegung.** Auf jedem Zeitschnitt $t$ knapp
unterhalb einer singulären Zeit $T$ zerfällt die Region
$\{R(\cdot,t) \geq r_0(t)^{-2}\}$ in eine Vereinigung
disjunkter $\varepsilon$-Hälse, $\varepsilon$-Kappen und ganzer
sphärischer Komponenten.

**5.2 Volumenkontrolle.** Die globale Volumen-Schranke
$\mathrm{Vol}(M, g(t))$ bleibt durch das Pinching-Argument bis
$T$ kontrolliert; insbesondere bleiben Hälse vom Volumen her
*klein*.

Beide Aussagen sind die geometrische Vorbedingung dafür, dass man im
nächsten Artikel **Surgery** definieren kann: Die Hälse sind
gefunden, ihr Mittel-$S^2$ ist explizit lokalisiert, und das, was
nach dem Schnitt überlebt, ist topologisch kontrolliert.

## 6. Was die Surgery aus dieser Analyse erbt

Aus §3 + §4 ergibt sich der **lokale Schnittplan**:

- An jedem $\varepsilon$-Hals existiert eine eindeutige Mittel-
  $S^2$.
- Die zwei Komponenten, die ein Schnitt entlang dieser $S^2$
  erzeugt, haben jeweils eine $\varepsilon$-Kappe als Anfang.
- Sphärische Komponenten ($S^3/\Gamma$) verschwinden in der
  Singularität in endlicher Zeit und können verworfen werden.

Was offen bleibt: die *globale* Konstanten-Wahl
$(\delta(t), h(t), r(t))$, die Definition der **Standardlösung**
(Modell zum Auffüllen), und die Erhaltung von
$\kappa$-Nichtkollaps + Pinching nach jedem Surgery-Schritt. Genau
das ist Inhalt von [Artikel 03](03-chirurgie.md).

## 7. Übersicht: Hindernis → Lösung

| Hindernis aus Art. 01 | Werkzeug | Resultat |
|-----------------------|----------|----------|
| H2 (Klassifikation $\kappa$-Lösungen) | Hamilton-Ivey + $\mathcal{L}$-Geom. | §2 (3 Modelle) |
| H3 (kanonische Nachbarschaft) | Hamilton-Kompaktheit + §2 | §4 (Satz) |
| Vorbereitung H4 (Surgery) | §3 + §5 | lokaler Schnittplan |

Akt 3 ist damit zum dritten Artikel hin vollständig vorbereitet:
Wir wissen *wo* zu schneiden ist und *was* nach dem Schnitt
gleich bleibt.

## Quellen

- **G. Perelman**, *The entropy formula for the Ricci flow and its
  geometric applications*, §§11–12,
  [arXiv:math/0211159](https://arxiv.org/abs/math/0211159).
- **R. Hamilton**, *The formation of singularities in the Ricci flow*,
  Surveys in Differential Geometry II (1995), 7–136.
- **T. Ivey**, *Ricci solitons on compact three-manifolds*,
  Differential Geom. Appl. 3 (1993), 301–307. (Pinching-Vorform.)
- **J. Morgan, G. Tian**, *Ricci Flow and the Poincaré Conjecture*,
  Clay Math. Monographs 3, AMS 2007, Kap. 9 (Standard-Solutions),
  Kap. 10 (kanonische Nachbarschaften).
- **B. Kleiner, J. Lott**, *Notes on Perelman's papers*,
  §§40–53, Geom. Topol. 12 (2008).
- **H.-D. Cao, X.-P. Zhu**, *A complete proof of the Poincaré and
  geometrization conjectures*, Asian J. Math. 10 (2006), §§5–6.
- **B. Chow, P. Lu, L. Ni**, *Hamilton's Ricci Flow*,
  AMS GSM 77, 2006. (Hamilton-Ivey-Beweis im Detail.)
