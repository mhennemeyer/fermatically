---
title: "Vektoranalysis kompakt"
slug: vorwissen/geometrie-analysis/vektoranalysis
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: de
tags:
  - vektoranalysis
  - gradient
  - divergenz
  - laplace
---

# Vektoranalysis kompakt

> *„Gradient, Divergenz und Laplace-Operator sind die drei Werkzeuge, mit
> denen Differentialgeometrie und Analysis dieselbe Sprache sprechen."*

Die Vektoranalysis stellt die analytischen Werkzeuge bereit, ohne die
weder die Wärmeleitung noch der Ricci-Fluss formulierbar wären.
Hier werden die Konzepte des $\mathbb{R}^n$ kurz wiederholt und gleich
auf Riemannsche Mannigfaltigkeiten verallgemeinert.

## 1. Gradient

Auf $\mathbb{R}^n$: Für eine glatte Funktion $f$ ist
$$
\nabla f = \big(\partial_1 f, \dots, \partial_n f\big).
$$

Auf einer Riemannschen Mannigfaltigkeit $(M, g)$: Der Gradient ist der
Vektor, der das Differential darstellt,
$$
g(\nabla f, X) = \mathrm{d}f(X) = X(f) \quad \forall X.
$$
In Koordinaten: $(\nabla f)^i = g^{ij}\, \partial_j f$. Der Gradient ist
das Vektorfeld der *steilsten Anstiegsrichtung* von $f$.

## 2. Divergenz

Auf $\mathbb{R}^n$: $\operatorname{div} X = \sum_i \partial_i X^i$.

Auf $(M, g)$ in lokalen Koordinaten:
$$
\operatorname{div} X = \frac{1}{\sqrt{\det g}}\, \partial_i \big(\sqrt{\det g}\, X^i\big).
$$
Anschaulich misst $\operatorname{div} X$, wie viel Volumen unter dem Fluss
von $X$ pro Zeiteinheit „verloren" oder „gewonnen" wird – die
infinitesimale Quellstärke des Vektorfeldes.

## 3. Laplace-Operator

Auf $\mathbb{R}^n$:
$$
\Delta f = \operatorname{div}(\nabla f) = \sum_i \partial_i^2 f.
$$

Auf $(M, g)$ – der **Laplace-Beltrami-Operator**:
$$
\Delta_g f = \frac{1}{\sqrt{\det g}}\, \partial_i\!\Big(\sqrt{\det g}\, g^{ij}\, \partial_j f\Big).
$$
Der Laplace-Operator misst die Abweichung einer Funktion von ihrem
*lokalen Mittelwert*. Funktionen mit $\Delta f \equiv 0$ heißen
**harmonisch**.

## 4. Integralsätze

Drei klassische Integralsätze stehen am Fundament jeder analytischen
Geometrie:

**Divergenzsatz (Gauß).** Für $X$ auf einem kompakten Gebiet
$\Omega \subset M$ mit Rand $\partial \Omega$:
$$
\int_\Omega \operatorname{div} X\, \mathrm{d}V_g = \int_{\partial \Omega} g(X, \nu)\, \mathrm{d}A,
$$
wobei $\nu$ die äußere Einheitsnormale ist.

**Greensche Identität.** Für $f, h$ auf $\Omega$:
$$
\int_\Omega (f\, \Delta h - h\, \Delta f)\, \mathrm{d}V_g = \int_{\partial \Omega} (f\, \partial_\nu h - h\, \partial_\nu f)\, \mathrm{d}A.
$$

**Stokes** (allgemein): Für eine $(n-1)$-Form $\omega$
$$
\int_M \mathrm{d}\omega = \int_{\partial M} \omega.
$$

Diese Sätze erlauben es, partielle Ableitungen *im Mittel* durch
Randwerte zu kontrollieren – ein Mechanismus, der in jeder
Energie-Abschätzung des Ricci-Flusses auftaucht.

## 5. Wichtige Identitäten

| Identität | Inhalt |
|-----------|--------|
| $\operatorname{div}(fX) = f\operatorname{div} X + g(\nabla f, X)$ | Produktregel |
| $\Delta(fh) = f\Delta h + h\Delta f + 2 g(\nabla f, \nabla h)$ | Produktregel für $\Delta$ |
| $\int_M f\, \Delta f\, \mathrm{d}V = -\int_M |\nabla f|^2\, \mathrm{d}V$ | partielle Integration (kompaktes $M$, kein Rand) |
| $\partial_t \int_M f\, \mathrm{d}V_{g(t)} = \int_M (\partial_t f - f\, R_g)\, \mathrm{d}V_{g(t)}$ | Ricci-Fluss-Variante (mit $\partial_t g = -2\mathrm{Ric}$, also $\partial_t \log\sqrt{\det g} = -R$) |

Die letzte Zeile ist die elementare Identität, die bei *jeder*
Variation eines Integrals unter dem Ricci-Fluss verwendet wird – etwa
in den Monotonie-Beweisen Perelmans
([Akt 2, Artikel 05](../../poincare/ricci-fluss/05-perelman-entropie.md)).

## 6. Warum das im Ricci-Fluss zentral ist

Der Ricci-Fluss ist eine *parabolische* Differentialgleichung
$\partial_t g = -2 \mathrm{Ric}$. Ihre Linearisierung enthält $\Delta$,
und Perelmans Energie-/Entropie-Funktionale werden durch partielle
Integration in geschlossener Form ausgewertet. Ohne Gauß'schen
Divergenzsatz und Greensche Identitäten gäbe es weder das
$\mathcal{F}$- noch das $\mathcal{W}$-Funktional.

## Querverweise

- Vorher: [Tangentialraum und Tensoren](tangentialraum-tensoren.md), [Krümmung von Flächen](kruemmung-flaechen-gauss.md).
- Weiter: [Wärmeleitungsgleichung – Intuition](waermeleitung.md).
- Anwendung: [Akt 2, Hamiltons Ricci-Fluss](../../poincare/ricci-fluss/03-hamiltons-ricci-fluss.md), [Akt 2, Perelman-Entropie](../../poincare/ricci-fluss/05-perelman-entropie.md).

## Quellen

- Lee, John M. (2018). *Introduction to Riemannian Manifolds.* Springer GTM 176, 2. Auflage. Kap. 2.
- Forster, Otto (2017). *Analysis 3.* Springer Spektrum, 8. Auflage.
- Marsden, J. & Tromba, A. (2011). *Vector Calculus.* W. H. Freeman, 6. Auflage.
- do Carmo, Manfredo P. (1992). *Riemannian Geometry.* Birkhäuser. App. A.
