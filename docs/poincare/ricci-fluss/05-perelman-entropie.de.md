---
title: "Perelmans Entropie-Funktionale"
slug: poincare/ricci-fluss/05-perelman-entropie
series: poincare
part: 5
act: ricci-fluss
date: 2026-04-27
status: draft
lang: de
tags:
  - entropie
  - perelman
---

# Perelmans Entropie-Funktionale

!!! abstract "Zusammenfassung"
    Perelmans erste Veröffentlichung *The entropy formula for the
    Ricci flow* (2002) zeigte: Der Ricci-Fluss ist der Gradientenfluss
    zweier Funktionale, $\mathcal{F}$ und $\mathcal{W}$. Beide sind
    unter dem Fluss **monoton** und liefern damit das Konservative,
    das Hamilton fehlte: eine Lyapunov-Funktion. Aus $\mathcal{W}$
    folgt unmittelbar das $\kappa$-Nichtkollaps-Theorem, der zentrale
    Hebel für die Kompaktheit von Blow-up-Folgen.

## 1. Worum es geht

Der Ricci-Fluss (siehe [Artikel 03](03-hamiltons-ricci-fluss.md))
glättet Krümmung lokal, kann aber Singularitäten produzieren. Bevor
man eine Blow-up-Analyse (siehe
[Artikel 04](04-singularitaeten-blowup.md)) starten kann, braucht
man eine **kontrollierende Größe**, die unter dem Fluss eine feste
Richtung hat – analog zur Energie in einem Gradientenfluss. Perelman
fand zwei solche Größen.

## 2. Das $\mathcal{F}$-Funktional

Perelman definiert für eine Metrik $g$ und eine Funktion
$f \in C^\infty(M)$:

$$\mathcal{F}(g, f) := \int_M \bigl(R + \lvert\nabla f\rvert^2\bigr)\, e^{-f}\, dV.$$

Hier ist $R$ die Skalarkrümmung,
$d\mu := e^{-f}\, dV$ ein gewichtetes Maß. Variiert man $g$ und $f$
unter der Nebenbedingung
$\int_M e^{-f}\, dV = 1$ (festes Gesamtmaß), erhält man als
Euler–Lagrange-Gleichungen

$$\partial_t g = -2\,(\mathrm{Ric} + \nabla^2 f),\qquad \partial_t f = -R - \Delta f + \lvert\nabla f\rvert^2.$$

> **Schlüsselbeobachtung (Perelman §1).** Modulo einer Diffeomorphismen-
> Eichung ist das Paar $(g, f)$ ein Gradientenfluss von $\mathcal{F}$
> bezüglich der Metrik $\int_M (\cdots)\, e^{-f}\, dV$ auf
> dem Konfigurationsraum. Insbesondere wächst $\mathcal{F}$ monoton:
>
> $$\frac{d}{dt}\mathcal{F} = 2\int_M \bigl\lvert\mathrm{Ric} + \nabla^2 f\bigr\rvert^2\, e^{-f}\, dV \ge 0.$$

Die kritischen Punkte sind genau die **steady solitons**
$\mathrm{Ric} + \nabla^2 f = 0$.

## 3. Vom $\mathcal{F}$- zum $\lambda$-Funktional

Optimiert man $\mathcal{F}$ über $f$ unter der Nebenbedingung, so
entsteht eine geometrische Invariante der Metrik:

$$\lambda(g) := \inf_{f}\, \mathcal{F}(g, f),\qquad \int_M e^{-f}\, dV = 1.$$

$\lambda(g)$ ist der kleinste Eigenwert des Schrödinger-Operators
$-4\Delta + R$. Unter dem Ricci-Fluss gilt
$\frac{d}{dt}\lambda \ge 0$.

**Konsequenz.** Auf einer geschlossenen Mannigfaltigkeit mit
$\lambda(g_0) > 0$ kann der Ricci-Fluss niemals ein Steady Soliton
mit nicht-positiver Skalarkrümmung als Limes haben. Bereits hier
verschwinden ganze Klassen von potenziellen Limesgeometrien.

## 4. Der Schritt zum $\mathcal{W}$-Funktional

$\mathcal{F}$ kontrolliert steady solitons; für die
Singularitätenanalyse braucht man jedoch **schrumpfende solitons**.
Perelman ersetzt deshalb $\mathcal{F}$ durch das skalierungs-bewusste
**$\mathcal{W}$-Funktional**:

$$\mathcal{W}(g, f, \tau) := \int_M \Bigl[\tau\bigl(R + \lvert\nabla f\rvert^2\bigr) + f - n\Bigr]\, (4\pi\tau)^{-n/2}\, e^{-f}\, dV.$$

Hier ist $\tau > 0$ ein **Rückwärtszeit-Parameter**
(typisch $\tau = T - t$), $n$ die Dimension, und die Nebenbedingung
ist $\int_M (4\pi\tau)^{-n/2}\, e^{-f}\, dV = 1$.

**Skalierungsinvarianz.** $\mathcal{W}$ ist invariant unter
$(g, \tau) \mapsto (\lambda^2 g, \lambda^2 \tau)$ – genau die
Skalierung des Ricci-Flusses (Artikel 03, §5). Das macht $\mathcal{W}$
zum natürlichen Werkzeug für **Blow-up-Limites**, deren Skala
divergiert.

## 5. Die Monotonie-Formel

> **Satz (Perelman 2002, §3).** Sei $g(t)$ eine Lösung des Ricci-Flusses
> auf $[0, T)$, $\tau = T - t$, und $f(t)$ erfülle die rückwärts-
> Konjugationswärmegleichung
> $\partial_\tau f = -\Delta f + \lvert\nabla f\rvert^2 - R + n/(2\tau)$.
> Dann gilt
>
> $$\frac{d}{dt}\mathcal{W}(g, f, \tau) = 2\tau \int_M \Bigl\lvert\mathrm{Ric} + \nabla^2 f - \frac{1}{2\tau} g\Bigr\rvert^2\, (4\pi\tau)^{-n/2}\, e^{-f}\, dV \ge 0.$$

Die Identität ist die **Entropieformel**. Die kritischen Punkte sind
genau die **schrumpfenden Gradient-Solitonen**
$\mathrm{Ric} + \nabla^2 f = \tfrac{1}{2\tau}\, g$.

## 6. Das $\mu$- und $\nu$-Funktional

Wie bei $\mathcal{F}$ optimiert man über $f$ und $\tau$:

$$\mu(g, \tau) := \inf_f \mathcal{W}(g, f, \tau),\qquad
\nu(g) := \inf_{\tau > 0} \mu(g, \tau).$$

$\mu$ und $\nu$ sind geometrische Invarianten. $\mu$ ist
**zeitlich** monoton steigend entlang des Flusses; $\nu$ liefert
eine echte konforme Schranke. Beide sind zugleich logarithmische
**Sobolev-Konstanten** auf $(M, g)$ – der Brückenschlag zur
funktionalanalytischen Maschinerie.

## 7. Was die Entropie ausschließt

Aus der Monotonie folgen drei strukturelle Aussagen, die für Akt 3
zentral sind:

1. **Keine schrumpfenden Solitonen mit Singularität in endlicher
   Zeit, außer den klassifizierten.** Jeder Blow-up-Limes ist ein
   schrumpfender Gradient-Soliton; in Dim 3 zwingt
   $\mathcal{W}$-Monotonie + $R \ge 0$-Erhaltung dies auf
   Sphären-Quotienten und runde Zylinder ein.
2. **Keine Soliton-Steady-States in kompakten Dim-3-Mannigfaltigkeiten,
   außer flachen.** $\mathcal{F}$-Monotonie schließt nicht-flache
   geschlossene Steady Solitons aus.
3. **Lokale Volumen-Schranken.** Die Entropie kontrolliert das
   Verhältnis Volumen / Krümmungsskala – die Vorstufe zum
   $\kappa$-Nichtkollaps (siehe
   [Artikel 06](06-kappa-nichtkollaps.md)).

## 8. Bezug zum Wärme-/Schrödinger-Operator

Die mit $\mathcal{W}$ assoziierte Gleichung für $f$ ist die
**konjugierte Wärmegleichung**

$$\Box^{*} u = (-\partial_t - \Delta + R)\, u = 0,\qquad u = (4\pi\tau)^{-n/2}\, e^{-f}.$$

Sie ist dual zur Wärmegleichung $\Box u = (\partial_t - \Delta) u$
unter dem Ricci-Fluss. Diese Dualität ist der Schlüssel zur
Konstruktion von **reduzierten Längen** (siehe
[Artikel 07](07-reduzierte-laenge.md)) und zur monotonen Volumen-
Größe $\tilde V$.

## 9. Historische Einordnung

Vor Perelman war der Ricci-Fluss ein technisches Werkzeug ohne
Variationsstruktur; Hamilton hatte mehrere ad-hoc-Maximumprinzipien.
Mit $\mathcal{F}$ und $\mathcal{W}$ wird der Fluss

- ein **Gradientenfluss** mit klar definiertem Variationsraum,
- mit **Lyapunov-Funktion**,
- die zudem **skalierungsinvariant** ist und damit unter Blow-ups
  überlebt.

Diese drei Eigenschaften zusammen sind der konzeptionelle Sprung von
Hamilton 1982 zu Perelman 2002.

## Quellen

- Grigori Perelman, *The entropy formula for the Ricci flow and its geometric applications*, [arXiv:math/0211159](https://arxiv.org/abs/math/0211159), §§1–4.
- John W. Morgan & Gang Tian, *Ricci Flow and the Poincaré Conjecture*, AMS (2007), §§5–6.
- Bruce Kleiner & John Lott, *Notes on Perelman's papers*, Geom. Topol. 12 (2008), 2587–2855, §§4–9.
- Huai-Dong Cao & Xi-Ping Zhu, *A complete proof of the Poincaré and geometrization conjectures*, Asian J. Math. 10 (2006), §§3–4.
- Peter Topping, *Lectures on the Ricci Flow*, LMS Lecture Notes 325 (2006), Kap. 6.

## Querverweise

- Vorheriger Artikel: [Singularitäten und Blow-up-Limits](04-singularitaeten-blowup.md)
- Nächster Artikel: [κ-Nichtkollaps und kanonische Nachbarschaften](06-kappa-nichtkollaps.md)
- Akt 1, Artikel 04: [Was ist die Poincaré-Vermutung?](../topologie/04-was-ist-poincare-vermutung.md)
