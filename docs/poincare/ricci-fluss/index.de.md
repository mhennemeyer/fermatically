---
title: "Werkzeuge: Ricci-Fluss"
slug: poincare/ricci-fluss/index
series: poincare
date: 2026-04-27
status: active
lang: de
---

# Werkzeuge: Ricci-Fluss

!!! abstract "Worum es im zweiten Akt geht"
    Akt 1 hat erklärt, **was** zu zeigen ist: Jede einfach
    zusammenhängende, geschlossene 3-Mannigfaltigkeit ist
    homöomorph zu $S^3$ – und allgemeiner kann jede geschlossene
    3-Mannigfaltigkeit kanonisch in geometrische Stücke zerlegt
    werden (Geometrisierung). Akt 2 baut die analytische
    Maschinerie, mit der das **gemacht** wird: den **Ricci-Fluss**
    nach Hamilton und seine **Verfeinerung durch Perelman**
    – Entropie-Funktionale, $\kappa$-Nichtkollaps, kanonische
    Nachbarschaften und reduzierte Länge.

## Die Idee in einem Satz

Hamiltons Ricci-Fluss
$$
\partial_t g_{ij} = -2\,R_{ij}
$$
ist eine geometrische Wärmegleichung für die Metrik selbst:
Krümmung wird ausgeglichen, hochkrümmungsbereiche werden glatter,
und im Idealfall konvergiert der Fluss gegen eine besonders
symmetrische („geometrische") Endmetrik. Die Schwierigkeit ist nicht
die Definition, sondern die **Singularitäten**: lokale Stellen, an
denen die Krümmung in endlicher Zeit explodiert. Akt 2 erklärt, wie
Perelman diese Singularitäten genau klassifiziert hat – als
Vorbereitung auf die *Surgery* in Akt 3.

## Die sieben Artikel

| # | Artikel | Worum es geht |
|---|---------|---------------|
| 1 | [Riemannsche Metrik](01-riemannsche-metrik.md) | Sprache und Modelle: $\mathbb{R}^n$, $S^n$, $\mathbb{H}^n$, Levi-Civita, Geodäten |
| 2 | [Krümmung und Ricci-Tensor](02-kruemmung-ricci-tensor.md) | Riemann-, Schnitt-, Ricci-, Skalarkrümmung; Vergleichsgeometrie |
| 3 | [Hamiltons Ricci-Fluss](03-hamiltons-ricci-fluss.md) | Definition, Wärmeleitungs-Heuristik, Hamilton-1982-Originalsatz, DeTurck |
| 4 | [Singularitäten und Blow-up-Limits](04-singularitaeten-blowup.md) | Typ-I/II/III, Neckpinch, parabolisches Reskalieren, antike $\kappa$-Lösungen |
| 5 | [Perelmans Entropie-Funktionale](05-perelman-entropie.md) | $\mathcal{F}$, $\mathcal{W}$, $\mu$/$\nu$, Monotonie, Gradientenfluss-Struktur |
| 6 | [κ-Nichtkollaps und kanonische Nachbarschaften](06-kappa-nichtkollaps.md) | Volumen-Schranke, Klassifikation antiker $\kappa$-Lösungen, Hals/Kappe/Raumform |
| 7 | [Reduzierte Länge und reduziertes Volumen](07-reduzierte-laenge.md) | $\mathcal{L}$-Geometrie, $\ell$, $\tilde V$, lokaler $\kappa$-Nichtkollaps, Blow-up-Konvergenz |

Die ersten beiden Artikel sind reine Sprachvorbereitung; wer Lee
*Introduction to Riemannian Manifolds* kennt, kann sie überfliegen.
Artikel 3 ist der historische Einstieg (Hamilton 1982). Ab
Artikel 4 beginnt Perelmans Programm, dessen Höhepunkt Artikel 7
markiert.

## Logischer Ablauf

```
01 Metrik   ──►  02 Krümmung  ──►  03 Hamilton-Fluss
                                         │
                                         ▼
                              04 Singularitäten / Blow-up
                                         │
                       ┌─────────────────┼─────────────────┐
                       ▼                 ▼                 ▼
                  05 Entropie       06 κ-Nichtkollaps   07 Reduzierte Länge
                       │                 │                 │
                       └─────────────────┼─────────────────┘
                                         ▼
                                  Akt 3: Surgery + Beweis
```

Artikel 5–7 hängen wechselseitig zusammen: $\mathcal{W}$ und
$\tilde V$ sind beides Lyapunov-Größen, beide implizieren
unabhängig $\kappa$-Nichtkollaps; die reduzierte Länge ist außerdem
das eigentliche Vehikel für Blow-up-Konvergenz und damit den
Existenzbeweis kanonischer Nachbarschaften.

## Vorwissen

Für Akt 2 sind die folgenden Themen aus dem
[Vorwissen-Bereich](../../vorwissen/index.md) hilfreich:

- Riemannsche Geometrie (Metrik, Krümmung, Geodäten)
- Differentialgeometrie auf Mannigfaltigkeiten
- Partielle Differentialgleichungen, insbesondere die
  Wärmegleichung und parabolische Skalierung
- Tensoranalysis und Indexkalkül

Wer diese Sprache neu lernt, beginnt am besten bei
Artikel 01 und überspringt zunächst die formaleren Identitäten in
Artikel 02.

## Übergang zu Akt 3

Mit Entropie, $\kappa$-Nichtkollaps, kanonischen Nachbarschaften
und reduzierter Länge ist die analytische Maschinerie
abgeschlossen. Akt 3 ([Der Beweis](../beweis/index.md)) verwendet
sie, um:

- **Ricci-Fluss-mit-Surgery** zu konstruieren,
- die *Stetigkeit der topologischen Konsequenzen* unter Surgery zu
  beweisen,
- **finite extinction time** für einfach zusammenhängende
  3-Mannigfaltigkeiten zu zeigen,
- daraus
  [Poincaré-Vermutung](../topologie/04-was-ist-poincare-vermutung.md)
  und
  [Geometrisierung](../topologie/05-geometrisierungs-vermutung.md)
  zu folgern.
