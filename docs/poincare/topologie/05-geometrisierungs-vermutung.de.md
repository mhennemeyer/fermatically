---
title: "Die Geometrisierungs-Vermutung von Thurston"
slug: poincare/topologie/05-geometrisierungs-vermutung
series: poincare
part: 5
act: topologie
date: 2026-04-25
status: draft
lang: de
tags:
  - thurston
  - geometrisierung
  - 3-mannigfaltigkeiten
---

# Die Geometrisierungs-Vermutung von Thurston

!!! abstract "Zusammenfassung"
    William Thurston verallgemeinerte 1982 die Poincaré-Vermutung zu
    einer vollständigen Klassifikations-Aussage über alle geschlossenen
    3-Mannigfaltigkeiten: Jede solche Mannigfaltigkeit lässt sich
    kanonisch in Stücke zerlegen, die je eine von **acht
    Modellgeometrien** tragen. Perelmans Beweis betrifft diese
    Geometrisierungs-Vermutung; die Poincaré-Vermutung folgt als
    Spezialfall.

## 1. Vom Klassifizieren in Dimension 2 zu Dimension 3

In Dimension 2 ist die Klassifikation geschlossener Flächen klassisch.
Der **Uniformisierungssatz** (Klein, Poincaré, Koebe, 1907) verschärft
sie geometrisch: Auf jeder geschlossenen Fläche existiert eine
Riemannsche Metrik konstanter Krümmung – sphärisch ($K = +1$),
euklidisch ($K = 0$) oder hyperbolisch ($K = -1$).

| Geschlecht $g$ | Krümmung | Modellgeometrie |
|----------------|----------|-----------------|
| $0$ ($S^2$) | $+1$ | sphärisch $S^2$ |
| $1$ ($T^2$) | $0$ | euklidisch $\mathbb{E}^2$ |
| $\geq 2$ | $-1$ | hyperbolisch $\mathbb{H}^2$ |

Die Frage stellte sich: Lässt sich diese geometrische Klassifikation auf
Dimension 3 ausweiten? Die Antwort ist subtil – drei konstante
Krümmungen reichen nicht.

## 2. Die acht Modellgeometrien

Thurston zeigte 1982: Eine **maximale, einfach zusammenhängende,
homogene Riemannsche 3-Mannigfaltigkeit** mit kompaktem Stabilisator
zerfällt in genau acht Isomorphieklassen – die **acht
Thurston-Geometrien**:

| # | Geometrie | Krümmung | Beispiel-Mannigfaltigkeit |
|---|-----------|----------|---------------------------|
| 1 | $S^3$ – sphärisch | $+1$ | $S^3$, Linsenräume, Poincaré-Homologie-Sphäre |
| 2 | $\mathbb{E}^3$ – euklidisch | $0$ | 3-Torus $T^3$, Bieberbach-Mannigfaltigkeiten |
| 3 | $\mathbb{H}^3$ – hyperbolisch | $-1$ | „die meisten" 3-Mannigfaltigkeiten |
| 4 | $S^2 \times \mathbb{R}$ | gemischt | $S^2 \times S^1$ |
| 5 | $\mathbb{H}^2 \times \mathbb{R}$ | gemischt | Produkte mit Flächen $g \geq 2$ |
| 6 | $\widetilde{\mathrm{SL}}_2(\mathbb{R})$ | negativ | Einheits-Tangentialbündel hyperbolischer Flächen |
| 7 | Nil | nilpotent | Heisenberg-Quotienten |
| 8 | Sol | auflösbar | Torusbündel über $S^1$ mit Anosov-Monodromie |

Drei davon haben *konstante* Krümmung ($S^3, \mathbb{E}^3, \mathbb{H}^3$),
zwei sind Produkte, die restlichen drei sind Lie-Gruppen mit
links-invarianten Metriken. Genau diese Liste – nicht mehr, nicht
weniger – beherrscht alle homogenen 3-Geometrien.

> „We may divide the geometries of three-manifolds into eight
> types."
> — William P. Thurston, *Three-dimensional manifolds, Kleinian
> groups and hyperbolic geometry*, BAMS (1982)

## 3. Die Geometrisierungs-Vermutung

Thurston wagte 1982 die kühne Vermutung, dass diese acht Geometrien
ausreichen, um *jede* geschlossene 3-Mannigfaltigkeit zu beschreiben –
nach geeigneter Zerlegung:

> **Geometrisierungs-Vermutung (Thurston, 1982).** Jede geschlossene,
> orientierbare 3-Mannigfaltigkeit lässt sich kanonisch in Stücke
> zerschneiden, von denen jedes eine vollständige, lokal-homogene
> Riemannsche Metrik aus einer der acht Thurston-Geometrien trägt.

Die Zerlegung verläuft in zwei Schritten, die jeder für sich klassisch
sind:

1. **Prim-Zerlegung** (Kneser 1929, Milnor 1962). Längs eingebetteter
   2-Sphären zerlegt sich $M$ eindeutig in eine zusammenhängende Summe
   $M = M_1 \# M_2 \# \cdots \# M_k$ von **prim**-Stücken, die nicht
   weiter sphärisch zerlegt werden können.
2. **JSJ-Zerlegung** (Jaco-Shalen 1979, Johannson 1979). Längs
   eingebetteter Tori zerschneidet man jedes prim-Stück weiter, bis nur
   noch **atoroidale** Stücke übrigbleiben.

Thurstons Vermutung ergänzt: Jedes der so entstehenden Stücke trägt
genau eine der acht geometrischen Strukturen.

## 4. Poincaré als Korollar

Wendet man die Vermutung auf eine geschlossene, einfach zusammenhängende
3-Mannigfaltigkeit $M$ an, lässt sich Schritt für Schritt ausschließen,
welche Geometrien in Frage kommen:

- $\pi_1(M) = 0$ ist endlich. Das schließt $\mathbb{E}^3$, $\mathbb{H}^3$,
  $\mathbb{H}^2 \times \mathbb{R}$, $\widetilde{\mathrm{SL}}_2$, Nil und
  Sol aus, denn alle diese tragen unendliche Fundamentalgruppen.
- Ebenso scheidet $S^2 \times \mathbb{R}$ aus, da seine Quotienten
  unendliche $\pi_1$ ($\mathbb{Z}$) oder eine $\mathbb{Z}/2$-Wirkung mit
  $\pi_1 = \mathbb{Z}/2$ haben.
- In der Prim-Zerlegung ist $M = M_1$, weil eine zusammenhängende Summe
  $M_1 \# M_2$ mit beiden Summanden $\neq S^3$ stets nichttriviale $\pi_1$
  hätte (Satz von van Kampen).

Damit bleibt nur die **sphärische Geometrie**: $M$ ist ein Quotient
$S^3 / \Gamma$ mit endlicher freier Gruppenwirkung. Die einzige Wirkung
mit trivialer Gruppe ist die triviale: $\Gamma = \{1\}$, also $M \cong
S^3$. Das ist die Poincaré-Vermutung.

> „The Poincaré Conjecture is a special case of Thurston's
> Geometrization Conjecture."
> — John W. Morgan, Gang Tian, *Ricci Flow and the Poincaré
> Conjecture* (2007), S. 4

## 5. Hyperbolisch ist generisch

Thurston bewies große Teile seiner Vermutung selbst: Für **Haken-Mannigfaltigkeiten**
– eine technische, aber breite Klasse, die viele knottenkomplementäre
Räume umfasst – etablierte er das **Hyperbolisierungs-Theorem**: Atoroidale
Haken-Mannigfaltigkeiten sind hyperbolisch. Ein bemerkenswertes
empirisches Bild entstand daraus: Unter den 3-Mannigfaltigkeiten ist
die hyperbolische Geometrie die *generische*; die anderen sieben
treten als Sonderfälle auf, in denen Symmetrie oder Faserstruktur die
Hyperbolizität blockiert.

## 6. Was Perelman bewies

Perelmans drei arXiv-Preprints liefern den Beweis der vollen
Geometrisierungs-Vermutung. Die Strategie ist analytisch, nicht
topologisch:

1. **Ricci-Fluss starten.** Auf $M$ wird eine beliebige Riemannsche
   Anfangsmetrik $g_0$ gewählt und der Ricci-Fluss
   $\partial_t g = -2 \mathrm{Ric}(g)$ gestartet
   (siehe [Akt 2](../ricci-fluss/index.md)).
2. **Singularitäten klassifizieren.** Treten Singularitäten auf, sind
   sie nach Perelmans Klassifikation der $\kappa$-Lösungen lokal von
   wenigen Modelltypen (Hals, Kappe).
3. **Chirurgie durchführen.** Hälse werden ausgeschnitten, Kappen
   eingeklebt; der Fluss wird auf einer modifizierten Mannigfaltigkeit
   fortgesetzt (siehe [Akt 3](../beweis/index.md)).
4. **Long-time-Verhalten analysieren.** Im Limes $t \to \infty$
   zerlegt sich die Mannigfaltigkeit in einen **dicken** Teil
   (hyperbolisch, $\mathbb{H}^3$-Stücke) und einen **dünnen** Teil
   (lokal kollabiert, Graphen-Mannigfaltigkeit aus den anderen
   Geometrien).
5. **Geometrisierung ablesen.** Aus der dicken/dünnen Zerlegung folgt
   die geometrische Struktur jedes Stücks.

Im einfach zusammenhängenden Spezialfall (Poincaré) lässt sich der
Beweis abkürzen: Das dritte Perelman-Paper (arXiv:math/0307245) zeigt
**endliche Auslöschungszeit** – der Fluss kollabiert in endlicher Zeit
vollständig, und das ist nur für $S^3$ möglich. Dieser **Kurzweg**
umgeht die volle Geometrisierungs-Maschinerie.

## 7. Bedeutung für die Topologie

Mit Thurstons Vermutung – jetzt **Satz** – ist die Klassifikation
geschlossener 3-Mannigfaltigkeiten effektiv abgeschlossen. Jede solche
Mannigfaltigkeit ist durch ihre Prim-Zerlegung, ihre JSJ-Zerlegung und
die geometrische Struktur ihrer Stücke beschreibbar. Die Topologie der
Dimension 3 verlässt damit den Status eines „Sammelsuriums von
Konstruktionen" und wird – wie Dimension 2 – durch Geometrie
strukturiert.

## 8. Ausblick

Akt 1 ist damit abgeschlossen. Was wird, was die Vermutung ist und
warum sie schwer war, ist klar. Im **zweiten Akt** wird die
Maschinerie aufgebaut, die den Beweis trägt: Riemannsche Metrik,
Krümmungstensoren, Hamiltons Ricci-Fluss, Perelmans
Entropie-Funktionale.

| Akt | Thema |
|-----|-------|
| [Akt 2 – Werkzeuge: Ricci-Fluss](../ricci-fluss/index.md) | Differentialgleichung für Metriken |
| [Akt 3 – Der Beweis: Ricci-Fluss mit Chirurgie](../beweis/index.md) | Singularitätsanalyse, Chirurgie, Geometrisierung |

---

## Quellen

- **William P. Thurston**: *Three-dimensional manifolds, Kleinian
  groups and hyperbolic geometry*, Bulletin of the American
  Mathematical Society 6 (1982), 357–381
- **William P. Thurston**: *Three-Dimensional Geometry and Topology,
  Volume 1*, Princeton University Press (1997)
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007), Kapitel 1
- **Peter Scott**: *The geometries of 3-manifolds*, Bulletin of the
  London Mathematical Society 15 (1983), 401–487 – die kanonische
  Übersicht über die acht Geometrien
- **Hellmuth Kneser**: *Geschlossene Flächen in dreidimensionalen
  Mannigfaltigkeiten*, Jahresbericht DMV 38 (1929), 248–260 –
  Prim-Zerlegung
