---
title: "Tangentialraum und Tensoren"
slug: vorwissen/geometrie-analysis/tangentialraum-tensoren
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: de
tags:
  - tangentialraum
  - tensoren
  - riemannsche-metrik
---

# Tangentialraum und Tensoren

> *„Der Tangentialraum ist die richtige Ableitung einer Mannigfaltigkeit
> an einem Punkt – und alles, was Geometrie misst, lebt auf ihm."*

Auf einer glatten Mannigfaltigkeit (siehe
[Mannigfaltigkeit anschaulich](mannigfaltigkeit-anschaulich.md)) lassen
sich Funktionen ableiten. Dazu braucht man eine Vorstellung von
*Geschwindigkeit* in einem Punkt. Diese Vorstellung formalisiert der
**Tangentialraum**. Auf seinen Tensorprodukten leben dann Begriffe wie
Längenmessung (Riemannsche Metrik), Krümmung und Volumen.

## 1. Tangentialvektoren

Sei $M$ eine glatte Mannigfaltigkeit, $p \in M$. Eine **glatte Kurve
durch $p$** ist eine glatte Abbildung $\gamma : (-\varepsilon,
\varepsilon) \to M$ mit $\gamma(0) = p$. Zwei Kurven $\gamma_1, \gamma_2$
heißen **äquivalent**, wenn in jeder (und damit jeder) Karte
$$
\frac{\mathrm{d}}{\mathrm{d}t}\Big|_{t=0}(\varphi \circ \gamma_1)
=
\frac{\mathrm{d}}{\mathrm{d}t}\Big|_{t=0}(\varphi \circ \gamma_2).
$$
Eine Äquivalenzklasse heißt **Tangentialvektor** an $p$. Die Menge aller
Tangentialvektoren ist der **Tangentialraum** $T_p M$.

$T_p M$ ist ein reeller Vektorraum der Dimension $n = \dim M$. In einer
Karte $(x^1, \dots, x^n)$ um $p$ liefert die Basis
$$
\Big\{ \partial_1 \big|_p, \dots, \partial_n \big|_p \Big\},
\qquad
\partial_i \big|_p f := \frac{\partial(f \circ \varphi^{-1})}{\partial x^i}(\varphi(p)).
$$

**Bild:** $T_p M$ ist die Tangentialebene/-gerade an $M$ in $p$, von der
Mannigfaltigkeit *abgelöst* und zu einem eigenen Vektorraum gemacht.

## 2. Vektorfelder und Kotangentialraum

Ein **Vektorfeld** $X$ ordnet jedem Punkt $p$ einen Vektor
$X_p \in T_p M$ zu (glatt). In Koordinaten:
$X = X^i(x)\, \partial_i$ (Einsteinsche Summenkonvention).

Der **Kotangentialraum** $T_p^* M$ ist der Dualraum von $T_p M$. Eine
**1-Form** ordnet jedem Punkt eine Linearform auf $T_p M$ zu. Basis dual
zu $\partial_i$: die Differentiale $\mathrm{d}x^i$. Dann ist eine 1-Form
$\omega = \omega_i(x)\, \mathrm{d}x^i$, und es gilt
$\mathrm{d}x^i(\partial_j) = \delta^i_j$.

## 3. Tensoren und Tensorfelder

Ein **$(r,s)$-Tensor** an $p$ ist eine multilineare Abbildung
$$
T : \underbrace{T_p^* M \times \dots \times T_p^* M}_{r}
   \times \underbrace{T_p M \times \dots \times T_p M}_{s}
   \to \mathbb{R}.
$$
Ein **Tensorfeld** ordnet jedem Punkt einen solchen Tensor zu. In
Koordinaten:
$$
T = T^{i_1 \dots i_r}{}_{j_1 \dots j_s}\,
\partial_{i_1} \otimes \dots \otimes \partial_{i_r} \otimes
\mathrm{d}x^{j_1} \otimes \dots \otimes \mathrm{d}x^{j_s}.
$$

| Tensor | Typ | Beispiele |
|--------|-----|-----------|
| Funktion | $(0,0)$ | Skalarfeld |
| Vektorfeld | $(1,0)$ | $\partial_i$ |
| 1-Form | $(0,1)$ | $\mathrm{d}f$, $\mathrm{d}x^i$ |
| Riemannsche Metrik | $(0,2)$, symmetrisch | $g_{ij}$ |
| Krümmungstensor | $(1,3)$ | $R^l{}_{ijk}$ |
| Ricci-Tensor | $(0,2)$, symmetrisch | $R_{ij}$ |

## 4. Die Riemannsche Metrik

Eine **Riemannsche Metrik** $g$ ist ein symmetrisches, positiv definites
$(0,2)$-Tensorfeld. In jedem Punkt liefert $g_p$ ein Skalarprodukt auf
$T_p M$, in Koordinaten $g_{ij}(x)$ mit $g_{ij} = g_{ji}$ und
$g_{ij}\xi^i \xi^j > 0$ für $\xi \neq 0$.

Damit definiert man:

- **Länge eines Vektors:** $|v|_g = \sqrt{g_{ij} v^i v^j}$.
- **Länge einer Kurve:** $L(\gamma) = \int_a^b |\dot\gamma(t)|_g\, \mathrm{d}t$.
- **Volumenform:** $\mathrm{d}V_g = \sqrt{\det g_{ij}}\, \mathrm{d}x^1 \wedge \dots \wedge \mathrm{d}x^n$.
- **Inverse Metrik:** $g^{ij}$, definiert durch $g^{ij}g_{jk} = \delta^i_k$.

Beispiel: Auf $\mathbb{R}^n$ ist die euklidische Metrik
$g_{ij} = \delta_{ij}$. Auf der Sphäre $S^2 \subset \mathbb{R}^3$ ergibt
sich aus der Einbettung in Polarkoordinaten
$g = \mathrm{d}\theta^2 + \sin^2\theta\,\mathrm{d}\phi^2$.

## 5. Index hoch- und runterziehen

Mit $g_{ij}$ und $g^{ij}$ kann man Indizes umwandeln. Aus einem
Vektorfeld $X^i$ wird die 1-Form $X_i := g_{ij} X^j$. Aus dem
Krümmungstensor $R^l{}_{ijk}$ wird der vierstellige Riemann-Tensor
$R_{lijk} := g_{lm} R^m{}_{ijk}$. Wer sich an diese Mechanik gewöhnt,
liest fast jede Formel der Differentialgeometrie als Bilanz oben/unten
stehender Indizes.

## 6. Was kommt als Nächstes?

Sobald eine Metrik gewählt ist, gibt es einen *eindeutigen*
Zusammenhang ohne Torsion mit metrischer Verträglichkeit – den
**Levi-Civita-Zusammenhang** – und damit kovariante Ableitungen,
Geodätische und den Riemannschen Krümmungstensor. Daraus entstehen
Ricci- und Skalar-Krümmung, die im Ricci-Fluss
$\partial_t g_{ij} = -2 R_{ij}$ die zentrale Rolle spielen.

## Querverweise

- Vorher: [Mannigfaltigkeit anschaulich](mannigfaltigkeit-anschaulich.md).
- Weiter: [Krümmung von Flächen (Gauß)](kruemmung-flaechen-gauss.md), [Vektoranalysis kompakt](vektoranalysis.md).
- Anwendung: [Akt 2, Riemannsche Metrik](../../poincare/ricci-fluss/01-riemannsche-metrik.md), [Akt 2, Krümmung und Ricci-Tensor](../../poincare/ricci-fluss/02-kruemmung-ricci-tensor.md).

## Quellen

- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2. Auflage. Kap. 1–3.
- do Carmo, Manfredo P. (1992). *Riemannian Geometry.* Birkhäuser.
- Petersen, Peter (2016). *Riemannian Geometry.* Springer GTM 171, 3. Auflage.
