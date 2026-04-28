---
title: "Der Beweis"
slug: poincare/beweis/index
series: poincare
date: 2026-04-28
status: active
lang: de
---

# Der Beweis

!!! abstract "Worum es im dritten Akt geht"
    Akt 1 hat geklärt, **was** zu zeigen ist (Poincaré- und
    Geometrisierungs-Vermutung in Dim 3). Akt 2 hat die
    analytisch-geometrischen **Werkzeuge** bereitgestellt: Ricci-Fluss,
    Perelman-Entropie, $\kappa$-Nichtkollaps, kanonische Nachbarschaften,
    reduzierte Länge. Akt 3 setzt sie zusammen. Sechs Artikel führen von
    Hamiltons ursprünglichem Programm und seinen fünf Hindernissen über
    Singularitätsanalyse, Chirurgie und Long-time-Verhalten bis hin zur
    Poincaré-Vermutung als topologischem Korollar.

## Die Idee in einem Satz

Hamiltons Vision war 1982: *Lasse den Ricci-Fluss laufen, bis die
Mannigfaltigkeit eine kanonische Form annimmt – und lies daraus die
Topologie ab.* Perelman zeigt, dass das **wörtlich funktioniert**, sofern
man (a) Singularitäten klassifiziert, (b) durch **Chirurgie** aus dem
Fluss herausschneidet und (c) das asymptotische Bild bei $t \to \infty$
korrekt liest.

## Die sechs Artikel

| # | Artikel | Worum es geht |
|---|---------|----------------|
| 01 | [Hamiltons Programm und seine Hindernisse](01-hamiltons-programm.md) | Vier-Schritte-Vision Hamiltons (1982–1997); fünf strukturelle Hindernisse H1–H5; Werkzeug-Tabelle Hamilton ↔ Perelman; Roadmap des Aktes. |
| 02 | [Singularitätsanalyse in Dimension 3](02-singularitaeten-dim3.md) | Hamilton–Ivey-Pinching; Klassifikation antiker $\kappa$-Lösungen (Zylinder, $S^3/\Gamma$, Bryant-Modell); kanonischer Nachbarschaftssatz. |
| 03 | [Ricci-Fluss mit Chirurgie](03-chirurgie.md) | $\delta$-Hälse, Standardlösung auf $\mathbb{R}^3$, Chirurgie-Algorithmus mit Parameterfolgen $(\varepsilon_i, \delta_i, r_i, h_i)$, Surgery-Theorem 0303109 §5. |
| 04 | [Long-time-Verhalten und dünn-dick-Zerlegung](04-long-time-verhalten.md) | reskalierte Metrik $\hat g = g/(4t)$; persistente Hyperbolik-Stücke + JSJ-Tori; Kollaps-Theorem; volle Geometrisierung. |
| 05 | [Endliche Auslöschungszeit](05-endliche-extinktion.md) | Perelman 0307245: $W_2$/$W_3$-Monotonie via Gauß-Bonnet; finite Extinktion für einfach zusammenhängende $M$ als Kurzweg. |
| 06 | [Geometrisierung impliziert Poincaré](06-poincare-aus-geometrisierung.md) | Topologisches Schluss-Argument: Prim-Zerlegung + Van-Kampen + sphärische Raumformen ⇒ $M \cong S^3$. |

## Logik des Beweises

```
                     Hamiltons Programm (1982)
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   Singularitätsanalyse (02)         Perelman-Werkzeuge aus Akt 2
              │                       (Entropie, κ, Reduktion)
              └───────────────┬───────────────┘
                              ▼
                  Ricci-Fluss mit Chirurgie (03)
                       Lösung auf [0, ∞)
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        Long-time-Limes (04)        Finite Extinction (05)
        thin–thick → 8 Geom.        π₁ = 0 ⇒ T < ∞
                │                           │
                └─────────────┬─────────────┘
                              ▼
                Geometrisierung ⇒ Poincaré (06)
                          M ≅ S³
```

## Welche Hindernisse fallen wo

| Hindernis (Artikel 01) | Aufgelöst in |
|-----------------------|---------------|
| H1 Singularitäten klassifizieren | 02 (kanonische Nachbarschaften) |
| H2 Singularitäten chirurgisch entfernen | 03 (Surgery-Theorem) |
| H3 unendliche Chirurgie-Akkumulation | 03 (diskrete Parameterfolgen) und 05 (finite Extinktion) |
| H4 asymptotisches Bild bei $t \to \infty$ | 04 (dünn-dick + Kollaps-Theorem) |
| H5 Topologie aus Geometrie ablesen | 06 (Prim-Zerlegung + sphärische Raumformen) |

## Vorwissen

Für diesen Akt sollte das Werkzeug-Repertoire aus
[Akt 2 (Ricci-Fluss)](../ricci-fluss/index.md) verfügbar sein,
insbesondere
[$\kappa$-Nichtkollaps](../ricci-fluss/06-kappa-nichtkollaps.md) und
[reduzierte Länge](../ricci-fluss/07-reduzierte-laenge.md). Topologisch
genügen die Inhalte aus
[Akt 1](../topologie/index.md) (Mannigfaltigkeit, einfach zusammenhängend,
Geometrisierungs-Vermutung).

## Was nach Akt 3 folgt

Mit Artikel 06 ist die Poincaré-Vermutung in Dimension 3 vollständig
bewiesen. Offen bleiben jedoch verwandte Fragen, auf die der Beweis
*nicht* direkt antwortet:

- **Glatte 4-dim Poincaré-Vermutung:** ungelöst.
- **Effektive Schranken** für die Anzahl der Chirurgien in Abhängigkeit
  von der Anfangs-Geometrie: weitgehend offen (vgl. Bamler 2018).
- **Ricci-Fluss in höheren Dimensionen:** Hamilton-style Singularitäten
  sind in Dim $\ge 4$ unvollständig klassifiziert (Brendle 2020; Bamler
  2020).

Diese Themen sind nicht Bestandteil der vorliegenden Artikelserie,
werden aber an gegebener Stelle in den Quellen verlinkt.

## Quellen (Akt-übergreifend)

- Perelman, G. (2002, 2003). arXiv:math/0211159, 0303109, 0307245.
- Hamilton, R. S. (1995). *The formation of singularities in the Ricci flow*. Surveys Diff. Geom. 2, 7–136.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. CMI/AMS.
- Morgan, J. & Tian, G. (2014). *The Geometrization Conjecture*. CMI/AMS.
- Cao, H.-D. & Zhu, X.-P. (2006). *A complete proof of the Poincaré and geometrization conjectures*. Asian J. Math. 10.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12.
- Kleiner, B. & Lott, J. (2014). *Locally collapsed 3-manifolds*. Astérisque 365.
- Colding, T. H. & Minicozzi, W. P. (2008). *Width and finite extinction time of Ricci flow*. Geom. Topol. 12.
