---
title: "Wärmeleitungsgleichung – Intuition"
slug: vorwissen/geometrie-analysis/waermeleitung
series: vorwissen
category: geometrie-analysis-aufbau
date: 2026-04-28
status: ready
lang: de
tags:
  - waermeleitung
  - pde
  - intuition
---

# Wärmeleitungsgleichung – Intuition

> *„Der Ricci-Fluss ist – grob – die Wärmeleitungsgleichung der
> Riemannschen Metrik. Wer Wärme verteilt sieht, sieht Krümmung
> ausgeglichen werden."*

Die Wärmeleitungsgleichung ist die einfachste *parabolische* partielle
Differentialgleichung. Ihre qualitativen Eigenschaften – Glättung,
Maximum-Prinzip, Energie-Abnahme – sind das didaktische Vorbild für
alles, was im Ricci-Fluss passiert.

## 1. Die Gleichung

Auf $\mathbb{R}^n$ oder einer Riemannschen Mannigfaltigkeit $(M, g)$:
$$
\partial_t u = \Delta u, \qquad u(0, x) = u_0(x).
$$
Hier ist $u(t, x)$ z. B. die Temperatur am Ort $x$ zur Zeit $t$, und
$\Delta$ ist der Laplace-Operator (siehe
[Vektoranalysis kompakt](vektoranalysis.md)).

Die Gleichung sagt: Die Zeitableitung von $u$ ist gleich dem
Laplace-Operator von $u$ – also der Abweichung von $u$ vom lokalen
Mittelwert. *Wenn $u$ in der Umgebung höher liegt als im Punkt, wächst
$u$; ist es niedriger, fällt $u$.*

## 2. Drei Grundeigenschaften

**Glättung.** Selbst wenn $u_0$ nur stetig (oder $L^2$) ist, ist
$u(t, \cdot)$ für $t > 0$ unendlich oft differenzierbar. Die
Wärmeleitung erzeugt Regularität aus dem Nichts.

**Maximum-Prinzip.** Auf einem kompakten Gebiet ohne Quellen gilt
$$
\min_x u_0 \le u(t, x) \le \max_x u_0 \qquad \forall t > 0.
$$
Anschaulich: Heißes wird nicht heißer, Kaltes nicht kälter, ohne dass
Wärme von außen einströmt.

**Energie-Abnahme.** Auf einem kompakten $M$ ohne Rand:
$$
\frac{\mathrm{d}}{\mathrm{d}t} \int_M u^2\, \mathrm{d}V = 2\int_M u\, \Delta u\, \mathrm{d}V = -2\int_M |\nabla u|^2\, \mathrm{d}V \le 0.
$$
Die $L^2$-Norm fällt monoton; die Lösung „verteilt" sich.

## 3. Wärmekern auf $\mathbb{R}^n$

Die fundamentale Lösung mit Anfangswert $\delta_y$ ist der **Wärmekern**
$$
K(t, x, y) = (4\pi t)^{-n/2}\, \exp\!\Big(-\frac{|x - y|^2}{4t}\Big).
$$
Jede Lösung mit ausreichend gutem $u_0$ schreibt sich als
$$
u(t, x) = \int_{\mathbb{R}^n} K(t, x, y)\, u_0(y)\, \mathrm{d}y.
$$
$K$ ist eine Gaußkurve, deren Standardabweichung mit $\sqrt{t}$ wächst –
das ist die typische **parabolische Skalierung** $x \sim \sqrt{t}$, die
auch beim Ricci-Fluss-Blow-up auftaucht
([Akt 2, Artikel 04](../../poincare/ricci-fluss/04-singularitaeten-blowup.md)).

## 4. Auf einer Mannigfaltigkeit

Auf $(M, g)$ ersetzt man $\Delta$ durch den Laplace-Beltrami-Operator
$\Delta_g$. Glättung und Maximum-Prinzip bleiben gültig. Der Wärmekern
existiert ebenfalls und kodiert Geometrie: Auf $S^n$ und auf
hyperbolischen Räumen ist $K_M(t, x, y)$ explizit bekannt; allgemein
liefern seine Asymptotiken den **Heat-Kernel-Expansion** mit
Krümmungsinvarianten als Koeffizienten – die Brücke zwischen Spektral-
und Differentialgeometrie.

## 5. Warum „Ricci-Fluss = Wärmegleichung der Metrik"

Linearisiert man die Ricci-Fluss-Gleichung
$\partial_t g = -2\mathrm{Ric}$ um eine flache Lösung in geeigneter
Eichung (z. B. via DeTurck-Trick), erhält man
$$
\partial_t h_{ij} \approx \Delta_g h_{ij} + \text{Krümmungsterme}.
$$
Bis auf Eich-Korrekturen ist der Ricci-Fluss eine *Wärmeleitungsgleichung
für den Metriktensor*. Die qualitativen Eigenschaften – Glättung,
Maximum-Prinzip auf der Skalarkrümmung
([Akt 3, Artikel 02](../../poincare/beweis/02-singularitaeten-dim3.md)),
Energie-Monotonie der Funktionale $\mathcal{F}$, $\mathcal{W}$
([Akt 2, Artikel 05](../../poincare/ricci-fluss/05-perelman-entropie.md))
– sind direkte Verwandte der drei oben aufgeführten
Wärmeleitungs-Eigenschaften.

## 6. Konjugierte Wärmeleitung

Für eine zeitabhängige Metrik $g(t)$, die dem Ricci-Fluss folgt, ist die
**konjugierte Wärmeleitung**
$$
\partial_\tau u = -\Delta_g u + R\, u, \qquad \tau = T - t,
$$
das natürliche Gegenstück. Sie taucht in der Definition der
Perelman-Entropie und der reduzierten Länge
([Akt 2, Artikel 07](../../poincare/ricci-fluss/07-reduzierte-laenge.md)) auf.

## Querverweise

- Vorher: [Vektoranalysis kompakt](vektoranalysis.md).
- Anwendung: [Akt 2, Hamiltons Ricci-Fluss](../../poincare/ricci-fluss/03-hamiltons-ricci-fluss.md), [Akt 2, Singularitäten und Blow-up](../../poincare/ricci-fluss/04-singularitaeten-blowup.md), [Akt 2, Perelman-Entropie](../../poincare/ricci-fluss/05-perelman-entropie.md).

## Quellen

- Evans, Lawrence C. (2010). *Partial Differential Equations.* AMS GSM 19, 2. Auflage. Kap. 2.3.
- John, Fritz (1991). *Partial Differential Equations.* Springer, 4. Auflage.
- Grigor'yan, Alexander (2009). *Heat Kernel and Analysis on Manifolds.* AMS/IP.
- Topping, Peter (2006). *Lectures on the Ricci Flow.* Cambridge University Press, Kap. 1.
