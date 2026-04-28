---
title: "Long-time-Verhalten und dünn-dick-Zerlegung"
slug: poincare/beweis/04-long-time-verhalten
series: poincare
part: 4
act: beweis
date: 2026-04-27
status: draft
lang: de
tags:
  - long-time
  - thin-thick
  - geometrisierung
  - perelman
---

# Long-time-Verhalten und dünn-dick-Zerlegung

> *„The thick part has bounded geometry and consists of hyperbolic pieces, while
> the thin part collapses with bounded curvature."*
> — Perelman, *Ricci flow with surgery on three-manifolds*, arXiv:math/0303109, §§6–7

In [Artikel 03](03-chirurgie.md) haben wir gezeigt, dass der Ricci-Fluss mit
Chirurgie für jede kompakte, orientierte 3-Mannigfaltigkeit auf $[0, \infty)$
existiert. Damit ist der Fluss als analytisches Objekt gerettet – aber wir
wissen noch nicht, *was* aus der Mannigfaltigkeit für $t \to \infty$ wird.
Dieser Artikel folgt Perelman *0303109* §§6–7 und zeigt, dass der Fluss in
asymptotisch identifizierbare Stücke zerfällt: hyperbolische Komponenten und
sogenannte „graph manifolds" – das letzte Puzzleteil der Geometrisierung.

## 1. Reskalierung und die richtige Skala

Direkt $g(t)$ für $t \to \infty$ zu betrachten, ist sinnlos: Auf einem
Hyperbolik-Stück wächst der Durchmesser linear und die Krümmung fällt wie
$1/t$. Die richtige Größe ist die **reskalierte Metrik**

$$
\hat g(t) := \frac{1}{4t}\, g(t).
$$

Der Faktor $1/(4t)$ ist so gewählt, dass eine konstante hyperbolische
Metrik der Schnittkrümmung $-1/(4t)$ unter $\hat g(t)$ stationär wird. Das
Ricci-Fluss-System wird dadurch in einen *asymptotischen Solitonen-Fluss*
verwandelt, dessen Fixpunkte genau die hyperbolischen Metriken der
Sektionalkrümmung $-1/4$ sind.

## 2. Die dünn-dick-Zerlegung

Sei $w > 0$ ein kleiner Parameter. Für jeden Zeitpunkt $t > 0$ definiert man

$$
M_{\text{dick}}(w, t) = \{\, x \in M_t \ \big| \ \mathrm{vol}(B_{\hat g(t)}(x, 1)) \ge w \,\},
\qquad
M_{\text{dünn}}(w, t) = M_t \setminus M_{\text{dick}}(w, t).
$$

Auf dem **dicken Teil** ist das Volumen einer 1-Kugel nach unten beschränkt –
nach dem $\kappa$-Nichtkollaps-Theorem ist dort die Krümmung in $C^k$ unter
Kontrolle und Cheeger–Gromov-Konvergenzargumente greifen. Auf dem **dünnen
Teil** bricht das Volumen zusammen, ohne dass die Krümmung explodiert: Genau
der Kollaps, den $\kappa$-Nichtkollaps lokal verbietet, *darf* hier global
auftreten.

## 3. Konvergenz der dicken Stücke gegen Hyperbolik

**Theorem (Perelman 0303109 §7.3, Hyperbolisierung des dicken Teils).**
Für jede Folge $t_i \to \infty$ existiert eine Teilfolge, eine endliche
Kollektion vollständiger hyperbolischer 3-Mannigfaltigkeiten endlichen
Volumens $(H_1, h_1), \dots, (H_k, h_k)$ und eine Folge glatter
Abbildungen
$$
\varphi_i : H_1 \sqcup \dots \sqcup H_k \to M_{t_i}
$$
so dass $\varphi_i^* \hat g(t_i) \to h_1 \sqcup \dots \sqcup h_k$ in
$C^\infty_{\text{loc}}$.

Die Bilder $\varphi_i(H_j)$ heißen **persistente Hyperbolik-Stücke**. Sie
sind durch *einbettungserhaltende inkompressible 2-Tori* in $M_t$
abgegrenzt – Tori, deren Fundamentalgruppe injektiv in $\pi_1(M)$
einbettet. Diese Tori werden in Akt 3 zu den Schnittflächen der
**JSJ-Zerlegung** (siehe [Geometrisierungs-Vermutung](../topologie/05-geometrisierungs-vermutung.md)).

## 4. Der dünne Teil: Kollaps mit beschränkter Krümmung

Der dünne Teil ist analytisch dramatischer. Hier benötigt Perelman einen
Satz aus der **Cheeger–Fukaya–Gromov-Theorie des Kollapses**:

**Theorem (Perelman 0303109 §7.4, Kollaps-Theorem).** Es gibt $w_0 > 0$,
so dass für $w < w_0$ und alle hinreichend großen $t$ der dünne Teil
$M_{\text{dünn}}(w, t)$ eine *Graph-Mannigfaltigkeit* ist, d. h. eine
3-Mannigfaltigkeit, die sich entlang eingebetteter inkompressibler Tori in
**Seifert-gefaserte** Stücke zerlegen lässt.

Den vollständigen Beweis hat Perelman nur skizziert; er wurde in zwei
unabhängigen Arbeiten ausgearbeitet:

- Shioya & Yamaguchi (2005), *Volume collapsed three-manifolds with a
    lower curvature bound*. Math. Ann. 333.
- Kleiner & Lott (2014), *Locally collapsed 3-manifolds*. Astérisque 365 –
    der heute kanonische Beweis ohne Annahme einer unteren Krümmungsschranke.

## 5. Zusammensetzen: Die Geometrisierung

Aus den dicken (hyperbolischen) und dünnen (Seifert-gefaserten) Stücken
plus den Komponenten, die in Akt 3 [Artikel 03](03-chirurgie.md) durch
Chirurgie als sphärische Raumformen entfernt wurden, ergibt sich:

| Zerlegungsstufe | Hervorgegangen aus |
|-----------------|---------------------|
| Prim-Zerlegung | Hals-Schnitten der Chirurgie |
| Sphärische Raumformen $S^3/\Gamma$ | weggeworfenen Komponenten |
| Hyperbolische Stücke | persistenter dicker Teil |
| Seifert-gefaserte Stücke | dünner Teil mit beschränkter Krümmung |
| JSJ-Tori | Grenztori zwischen dick und dünn |

Das ist – Stück für Stück – exakt Thurstons
**Geometrisierungs-Vermutung** (vgl. [Akt 1, Artikel 05](../topologie/05-geometrisierungs-vermutung.md)).
Damit ist der Hauptsatz für *jede* kompakte orientierte 3-Mannigfaltigkeit
bewiesen.

## 6. Was nicht ohne Weiteres folgt

Der hier skizzierte Beweis zeigt die Geometrisierung mit eventuell
*unendlich vielen* Chirurgien auf $[0, \infty)$. Für die Poincaré-Vermutung
genügt ein deutlich kürzeres Argument: Wenn $M$ einfach zusammenhängend
ist, dann verschwindet der Fluss in **endlicher Zeit**. Dieses
**Extinktions-Theorem** ist Perelmans dritter Preprint
*0307245* und wird in [Artikel 05: Endliche Extinktion](05-endliche-extinktion.md)
behandelt. Nur damit ist die Poincaré-Vermutung *ohne* die volle Maschinerie
der dünn-dick-Zerlegung beweisbar (die Geometrisierung wird sie aber
trotzdem brauchen).

## 7. Welche Hindernisse jetzt fallen

| Hindernis (siehe [Artikel 01](01-hamiltons-programm.md)) | Lösung in diesem Artikel |
|-----------|--------------------------|
| O4: Long-time-Existenz allein reicht nicht | reskalierte Metrik $\hat g = g/(4t)$ |
| O4': Konvergenz auf hyperbolischen Stücken | Cheeger–Gromov auf $M_{\text{dick}}$ |
| O4'': Was passiert auf $M_{\text{dünn}}$? | Kollaps-Theorem → Seifert-gefaserte Graph-Mannigfaltigkeiten |
| O5 (teilweise): Topologie aus dem Limes ablesen | dick = hyperbolisch, dünn = Seifert, Schnitte = JSJ-Tori |

## Querverweise

- Vorher: [Ricci-Fluss mit Chirurgie](03-chirurgie.md) – stellt den Fluss auf $[0, \infty)$ bereit.
- Werkzeuge aus Akt 2: [κ-Nichtkollaps](../ricci-fluss/06-kappa-nichtkollaps.md), [Reduzierte Länge](../ricci-fluss/07-reduzierte-laenge.md).
- Topologie aus Akt 1: [Geometrisierungs-Vermutung](../topologie/05-geometrisierungs-vermutung.md).
- Nächster Artikel: [Endliche Extinktion](05-endliche-extinktion.md) – der Kurzweg zur Poincaré-Vermutung.

## Quellen

- Perelman, G. (2003). *Ricci flow with surgery on three-manifolds*. arXiv:math/0303109, §§6–7.
- Morgan, J. & Tian, G. (2014). *The Geometrization Conjecture*. CMI/AMS – ausgearbeitete Version des Long-time-Arguments.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, §§90–93.
- Kleiner, B. & Lott, J. (2014). *Locally collapsed 3-manifolds*. Astérisque 365 – Kollaps-Theorem ohne untere Krümmungsschranke.
- Shioya, T. & Yamaguchi, T. (2005). *Volume collapsed three-manifolds with a lower curvature bound*. Math. Ann. 333.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10, §§7.5–7.7.
