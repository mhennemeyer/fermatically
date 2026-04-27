---
title: "Poincaré-Vermutung – Der Beweis von Perelman"
slug: poincare/index
series: poincare
date: 2026-04-25
status: active
lang: de
---
# Poincaré-Vermutung – Der Weg zum Beweis

!!! abstract "Überblick"
    Henri Poincaré formulierte 1904 eine scheinbar einfache Frage über die dreidimensionale Sphäre. Ein Jahrhundert später lieferte Grigori Perelman mit drei arXiv-Preprints (2002–2003) einen Beweis, der die Poincaré-Vermutung als Korollar einer viel tieferen Aussage erhält: der Geometrisierungs-Vermutung von Thurston. Diese Artikelserie zeichnet den Weg nach – von der Topologie über Hamiltons Ricci-Fluss bis zur Ricci-Fluss-Chirurgie.

## Die Vermutung

**Poincaré-Vermutung (1904).** Jede geschlossene, einfach zusammenhängende, dreidimensionale Mannigfaltigkeit ist homöomorph zur 3-Sphäre \(S^3\).

Anschaulich: Wenn sich auf einem dreidimensionalen Raum ohne Rand jede Schleife stetig zu einem Punkt zusammenziehen lässt, dann ist dieser Raum topologisch nichts anderes als die Oberfläche einer vierdimensionalen Kugel. In den Dimensionen \(n \geq 5\) wurde die analoge Aussage bereits 1961 von Stephen Smale bewiesen, in Dimension 4 von Michael Freedman 1982. Die ursprüngliche Vermutung in Dimension 3 widerstand allen Versuchen, bis Perelman 2002–2003 drei Preprints auf arXiv hochlud und damit den Knoten löste.

Perelmans Beweis lehnt sich an ein Programm von Richard Hamilton an: den **Ricci-Fluss**, eine Differentialgleichung, die eine Riemannsche Metrik wie eine Wärmeleitungsgleichung „glättet". Hamilton hatte gezeigt, wie der Fluss in günstigen Fällen funktioniert, scheiterte aber an der Kontrolle der Singularitäten. Perelman lieferte die fehlenden analytischen Werkzeuge – Entropie-Funktionale, das \(\kappa\)-Nichtkollaps-Theorem, kanonische Nachbarschaften – und ein Chirurgie-Verfahren, das Singularitäten kontrolliert entfernt und den Fluss fortsetzt.

---

## Der Weg in drei Akten

### 🌐 Akt 1: Topologie und die Vermutung

Was wird überhaupt behauptet? Der erste Akt klärt die Sprache der Topologie und stellt die Geometrisierungs-Vermutung von Thurston als das größere Bild vor, in dem Poincaré nur ein Spezialfall ist.

| # | Artikel | Thema |
|---|---------|-------|
| 1 | [Was ist Topologie?](topologie/01-was-ist-topologie.md) | Stetige Verformung, Homöomorphie, topologische Invarianten |
| 2 | [Mannigfaltigkeiten](topologie/02-mannigfaltigkeiten.md) | Lokal euklidische Räume, Dimension, geschlossen vs. mit Rand |
| 3 | [Die Sphäre und einfacher Zusammenhang](topologie/03-sphaere-einfacher-zusammenhang.md) | \(S^n\), Fundamentalgruppe, Homotopie |
| 4 | [Was ist die Poincaré-Vermutung?](topologie/04-was-ist-poincare-vermutung.md) | Original 1904, Verallgemeinerung, höhere Dimensionen |
| 5 | [Die Geometrisierungs-Vermutung von Thurston](topologie/05-geometrisierungs-vermutung.md) | Acht Modellgeometrien, Zerlegung von 3-Mannigfaltigkeiten |

→ [Akt 1 im Überblick](topologie/index.md)

### 🌊 Akt 2: Werkzeuge – Ricci-Fluss und Geometrische Analysis

Bevor der Beweis kommt, braucht man die Differentialgleichung, die das Ganze antreibt. Hamiltons Ricci-Fluss und Perelmans Erweiterungen werden hier eigenständig entwickelt; sie werden im dritten Akt referenziert.

| # | Artikel | Thema |
|---|---------|-------|
| 1 | [Riemannsche Metrik](ricci-fluss/01-riemannsche-metrik.md) | Längen- und Winkelmessung auf Mannigfaltigkeiten |
| 2 | [Krümmung und Ricci-Tensor](ricci-fluss/02-kruemmung-ricci-tensor.md) | Schnitt-, Ricci- und Skalarkrümmung |
| 3 | [Hamiltons Ricci-Fluss](ricci-fluss/03-hamiltons-ricci-fluss.md) | \(\partial_t g_{ij} = -2 R_{ij}\) als Wärmeleitungsgleichung |
| 4 | [Singularitäten und Blow-up-Limits](ricci-fluss/04-singularitaeten-blowup.md) | Wie der Fluss zusammenbricht und was man daraus liest |
| 5 | [Perelmans Entropie-Funktionale](ricci-fluss/05-perelman-entropie.md) | \(\mathcal{F}\), \(\mathcal{W}\) und ihre Monotonie |
| 6 | [κ-Nichtkollaps und kanonische Nachbarschaften](ricci-fluss/06-kappa-nichtkollaps.md) | Volumenkontrolle, lokale Modelle |
| 7 | [Reduzierte Länge und reduziertes Volumen](ricci-fluss/07-reduzierte-laenge.md) | Perelmans \(\mathcal{L}\)-Geometrie |

→ [Akt 2 im Überblick](ricci-fluss/index.md)

### 🏔️ Akt 3: Der Beweis – Ricci-Fluss mit Chirurgie

Wie aus den Werkzeugen ein Beweis wird: Singularitätsanalyse in Dimension 3, kontrollierte Chirurgie, Long-time-Verhalten, und schließlich die beiden Wege zur Poincaré-Vermutung.

| # | Artikel | Thema |
|---|---------|-------|
| 1 | [Hamiltons Programm und seine Hindernisse](beweis/01-hamiltons-programm.md) | Was funktionierte, was fehlte |
| 2 | [Singularitätsanalyse in Dimension 3](beweis/02-singularitaeten-dim3.md) | \(\kappa\)-Lösungen und ihre Klassifikation |
| 3 | [Ricci-Fluss mit Chirurgie](beweis/03-chirurgie.md) | Hals-Operationen, Definition der Chirurgie |
| 4 | [Long-time-Verhalten und dünn-dick-Zerlegung](beweis/04-long-time-verhalten.md) | Asymptotik, hyperbolische und Graphen-Stücke |
| 5 | [Endliche Auslöschungszeit](beweis/05-endliche-extinktion.md) | Der Kurzweg über arXiv:math/0307245 |
| 6 | [Geometrisierung impliziert Poincaré](beweis/06-poincare-aus-geometrisierung.md) | Wie aus dem allgemeinen Resultat das Korollar wird |

→ [Akt 3 im Überblick](beweis/index.md)

---

## Empfohlene Reihenfolge

Die Akte bauen aufeinander auf. Der empfohlene Weg:

1. **Topologie** (Akt 1) – als Einstieg in die Begriffswelt.
2. **Ricci-Fluss** (Akt 2) – die analytische Maschinerie, eigenständig lesbar.
3. **Der Beweis** (Akt 3) – streng der Reihe nach.

!!! tip "Vorwissen"
    Für die Riemannsche Geometrie und partielle Differentialgleichungen, die Akt 2 voraussetzt, gibt es im [Vorwissen](../vorwissen/index.md) den Block „Geometrie und Analysis (Aufbau)". Die Artikel dort werden aus der Storyline heraus verlinkt, wenn sie benötigt werden.

!!! info "Verhältnis zu Fermat/Wiles"
    Die Poincaré-Storyline ist unabhängig von [Fermats letztem Satz](../flt-overview.md) lesbar. Beide Beweise teilen aber ein Muster: Eine zahlentheoretische bzw. topologische Aussage wird über eine tiefere Struktur (Modularität bzw. Geometrisierung) gewonnen, die ihrerseits den Hauptaufwand trägt.

---

## Quellen

**Originalarbeiten von Perelman (alle frei auf arXiv).**

- Perelman, G. *The entropy formula for the Ricci flow and its geometric applications.* arXiv:[math/0211159](https://arxiv.org/abs/math/0211159), 11. November 2002.
- Perelman, G. *Ricci flow with surgery on three-manifolds.* arXiv:[math/0303109](https://arxiv.org/abs/math/0303109), 10. März 2003.
- Perelman, G. *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds.* arXiv:[math/0307245](https://arxiv.org/abs/math/0307245), 17. Juli 2003.

**Ausarbeitungen und Lehrbücher.**

- Morgan, J.; Tian, G. *Ricci Flow and the Poincaré Conjecture.* Clay Mathematics Monographs 3, AMS 2007.
- Kleiner, B.; Lott, J. *Notes on Perelman's papers.* Geometry & Topology 12 (2008), 2587–2855.
- Cao, H.-D.; Zhu, X.-P. *A Complete Proof of the Poincaré and Geometrization Conjectures – Application of the Hamilton-Perelman Theory of the Ricci Flow.* Asian Journal of Mathematics 10 (2006), 165–492.
- Hamilton, R. S. *Three-manifolds with positive Ricci curvature.* Journal of Differential Geometry 17 (1982), 255–306.

**Populärwissenschaftlich.**

- O'Shea, D. *The Poincaré Conjecture: In Search of the Shape of the Universe.* Walker & Company 2007.
