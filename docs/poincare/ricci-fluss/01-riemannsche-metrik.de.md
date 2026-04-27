---
title: "Riemannsche Metrik"
slug: poincare/ricci-fluss/01-riemannsche-metrik
series: poincare
part: 1
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - riemannsche-geometrie
  - metrik
---

# Riemannsche Metrik

!!! abstract "Zusammenfassung"
    Eine Riemannsche Metrik ist die Zusatzstruktur, die einer glatten
    Mannigfaltigkeit Längen, Winkel und Volumina verleiht. Sie ist das
    fundamentale Objekt, das Hamiltons Ricci-Fluss zeitlich verformt –
    ohne Metrik gibt es keine Krümmung, ohne Krümmung keinen Ricci-Fluss.

## 1. Von der Topologie zur Geometrie

In Akt 1 ([Artikel 02](../topologie/02-mannigfaltigkeiten.md)) wurden
Mannigfaltigkeiten als Räume eingeführt, die lokal wie $\mathbb{R}^n$
aussehen. Eine glatte Mannigfaltigkeit kennt aber nur ihre topologische
und differenzierbare Struktur: Welche Funktionen sind glatt, welche
Vektorfelder existieren? Sie weiß nicht, wie *lang* ein Vektor ist oder
welcher *Winkel* zwischen zweien liegt.

Genau diese Information liefert eine **Riemannsche Metrik**. Sie macht aus
einer glatten Mannigfaltigkeit eine **Riemannsche Mannigfaltigkeit**
$(M, g)$ und ist die kleinste Zusatzstruktur, mit der man Geometrie im
klassischen Sinn betreiben kann.

## 2. Definition

Sei $M$ eine glatte $n$-Mannigfaltigkeit. Eine **Riemannsche Metrik** $g$
ordnet jedem Punkt $p \in M$ ein Skalarprodukt
$g_p \colon T_pM \times T_pM \to \mathbb{R}$
auf dem Tangentialraum zu, das

- **bilinear** in beiden Argumenten,
- **symmetrisch** ($g_p(v,w) = g_p(w,v)$),
- **positiv definit** ($g_p(v,v) \ge 0$ mit Gleichheit nur für $v = 0$)

ist und **glatt** vom Punkt $p$ abhängt. In lokalen Koordinaten
$(x^1, \dots, x^n)$ schreibt man

$$g = g_{ij}(x)\, dx^i \otimes dx^j,$$

wobei die Matrix $\bigl(g_{ij}(p)\bigr)$ symmetrisch und positiv definit
ist. Die Einsteinsche Summenkonvention wird im Folgenden stillschweigend
verwendet.

> „A Riemannian metric on a smooth manifold $M$ is a smooth, symmetric,
> positive-definite 2-tensor field on $M$."
> — John M. Lee, *Introduction to Riemannian Manifolds* (2018), S. 11

## 3. Was die Metrik leistet

Sobald $g$ vorliegt, sind alle klassischen geometrischen Größen definiert.

**Länge eines Vektors.** Für $v \in T_pM$ ist
$\lvert v\rvert_g = \sqrt{g_p(v,v)}$.

**Winkel.** Zwischen $v, w \in T_pM \setminus\{0\}$:

$$\cos\theta = \frac{g_p(v,w)}{\lvert v\rvert_g\,\lvert w\rvert_g}.$$

**Bogenlänge einer Kurve** $\gamma\colon [a,b]\to M$:

$$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}\bigl(\dot\gamma(t),\dot\gamma(t)\bigr)}\,dt.$$

**Riemannscher Abstand.** $d_g(p,q) = \inf_\gamma L(\gamma)$, wobei das
Infimum über alle stückweise glatten Kurven von $p$ nach $q$ läuft.
$(M, d_g)$ wird damit zu einem metrischen Raum, dessen Topologie mit der
ursprünglichen Mannigfaltigkeitstopologie übereinstimmt.

**Volumenform.** In orientierbaren Karten:

$$d\mathrm{vol}_g = \sqrt{\det(g_{ij})}\,dx^1 \wedge \cdots \wedge dx^n.$$

Damit lassen sich Volumina von Teilmengen, Integrale glatter Funktionen
und – über die Hesse-Form von $g$ – auch Krümmungsgrößen definieren
(siehe [Artikel 02](02-kruemmung-ricci-tensor.md)).

## 4. Beispiele

**Euklidischer Raum.** Auf $\mathbb{R}^n$ ist
$g_{\mathrm{eukl}} = \delta_{ij}\,dx^i\,dx^j$ die flache Standardmetrik –
Längen, Winkel und Volumen sind die gewohnten.

**Sphäre $S^n$.** Eingebettet in $\mathbb{R}^{n+1}$ erbt $S^n$ die
**Rundmetrik** $g_{\mathrm{round}}$ als Restriktion des euklidischen
Skalarprodukts auf den Tangentialraum. Großkreise sind Geodäten, der
Schnittkrümmungs-Wert ist konstant gleich $1$ (für die Einheits-Sphäre).

**Hyperbolischer Raum $\mathbb{H}^n$.** Auf der oberen Halbebene
$\{(x^1,\dots,x^n) : x^n > 0\}$ definiert
$g_{\mathrm{hyp}} = (x^n)^{-2}\,\delta_{ij}\,dx^i\,dx^j$
eine Metrik mit konstanter Schnittkrümmung $-1$.

**Produktmetriken.** Auf $M \times N$ kombiniert
$g_M \oplus g_N$ die Faktoren – etwa die Standardmetrik auf
$T^2 = S^1 \times S^1$ oder $S^2 \times \mathbb{R}$.

**Gequetschte Sphäre.** Die runde $S^2$ lässt sich durch Skalierung in
eine Richtung zu einem Ellipsoid verformen. Topologisch bleibt es eine
2-Sphäre, geometrisch ändern sich Krümmung, Geodäten und Volumen.

## 5. Existenz und Vielfalt

Eine grundlegende Beobachtung: Auf jeder parakompakten glatten
Mannigfaltigkeit existiert mindestens eine Riemannsche Metrik. Der Beweis
verwendet eine Zerlegung der Eins, kombiniert lokale
Koordinatenmetriken in den Karten und überträgt die positive Definitheit
auf das globale Objekt (siehe Lee 2018, Prop. 2.4).

Wichtiger noch: Auf einer fixierten glatten Mannigfaltigkeit existiert
ein **unendlich-dimensionaler Raum** Riemannscher Metriken. Dieser Raum
$\mathcal{M}(M)$ ist der eigentliche Spielplatz des Ricci-Flusses: Eine
Anfangsmetrik $g_0$ wird unter dem Fluss zu einer Familie $g(t)$ – eine
Trajektorie in $\mathcal{M}(M)$ (siehe
[Artikel 03](03-hamiltons-ricci-fluss.md)).

## 6. Levi-Civita-Zusammenhang

Eine Riemannsche Metrik liefert kanonisch einen **Zusammenhang**
$\nabla$ auf dem Tangentialbündel – den **Levi-Civita-Zusammenhang**.
Charakterisiert ist er durch zwei Eigenschaften:

- **Torsionsfreiheit:** $\nabla_X Y - \nabla_Y X = [X,Y]$.
- **Metrik-Verträglichkeit:** $X(g(Y,Z)) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$.

Der Fundamentalsatz der Riemannschen Geometrie besagt, dass $\nabla$
durch diese beiden Bedingungen eindeutig bestimmt ist. Die zugehörigen
Christoffel-Symbole

$$\Gamma^k_{ij} = \tfrac{1}{2}\,g^{kl}\bigl(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij}\bigr)$$

sind die rechentechnische Grundlage für Krümmung und Geodäten.

## 7. Geodäten

Eine **Geodäte** ist eine Kurve $\gamma$ mit
$\nabla_{\dot\gamma}\dot\gamma = 0$ – sie verläuft „so gerade wie möglich".
Geodäten verallgemeinern Geraden des $\mathbb{R}^n$ und Großkreise auf
$S^n$. In Koordinaten:

$$\ddot\gamma^k + \Gamma^k_{ij}\,\dot\gamma^i\,\dot\gamma^j = 0.$$

Lokal sind Geodäten die kürzesten Verbindungen; global stimmt das nur
unter Zusatzannahmen (etwa Vollständigkeit). Der Hopf-Rinow-Satz
verbindet metrische und geodätische Vollständigkeit.

## 8. Warum die Metrik in Akt 2 zentral ist

Hamiltons Ricci-Fluss ist die Evolutionsgleichung

$$\frac{\partial g(t)}{\partial t} = -2\,\mathrm{Ric}(g(t)).$$

Sie ist eine partielle Differentialgleichung **für die Metrik selbst**.
Sämtliche geometrischen Größen, mit denen die nachfolgenden Artikel
arbeiten – Krümmungstensoren, Volumen, Diameter, Entropie-Funktionale –
sind Funktionen von $g$. Wer den Fluss verstehen will, muss zuerst
verstehen, was eine Metrik ist und wie sie sich ändert, wenn man an ihr
„dreht".

## Quellen

- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer (2018), Kap. 2.
- Manfredo do Carmo, *Riemannian Geometry*, Birkhäuser (1992), Kap. 1–3.
- Peter Petersen, *Riemannian Geometry*, 3rd ed., Springer (2016), Kap. 2.

## Querverweise

- Vorbereitung: [Artikel 02 – Mannigfaltigkeiten](../topologie/02-mannigfaltigkeiten.md)
- Nächster Artikel: [Krümmung und Ricci-Tensor](02-kruemmung-ricci-tensor.md)
- Vorwissen: [Geometrie und Analysis (Aufbau)](../../vorwissen/index.md)
