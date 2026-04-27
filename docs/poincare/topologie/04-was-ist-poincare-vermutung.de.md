---
title: "Was ist die Poincaré-Vermutung?"
slug: poincare/topologie/04-was-ist-poincare-vermutung
series: poincare
part: 4
act: topologie
date: 2026-04-25
status: draft
lang: de
tags:
  - poincare-vermutung
  - geschichte
---

# Was ist die Poincaré-Vermutung?

!!! abstract "Zusammenfassung"
    Henri Poincaré stellte 1904 am Ende seines fünften
    *Complément à l'Analysis Situs* eine Frage zur 3-Sphäre, die ein
    Jahrhundert offen blieb. In den Dimensionen $n \geq 5$ und $n = 4$
    wurde sie längst gelöst, gerade Dimension 3 widerstand allen
    klassischen Methoden. Dieser Artikel erzählt die Geschichte der
    Vermutung – von der Originalformulierung über die Homologie-Sphäre
    bis zu Hamiltons Ricci-Fluss-Programm.

## 1. Die Originalformulierung 1904

Poincaré hatte zwischen 1895 und 1904 in *Analysis Situs* und fünf
Ergänzungen die Grundlagen der algebraischen Topologie geschaffen. In
einer früheren Arbeit (1900) hatte er noch behauptet, eine geschlossene
3-Mannigfaltigkeit mit derselben **Homologie** wie $S^3$ sei bereits
homöomorph zu $S^3$. 1904 widerlegte er diese Aussage selbst durch ein
Gegenbeispiel: die **Poincaré-Homologie-Sphäre**, eine geschlossene
3-Mannigfaltigkeit mit $H_*(M) = H_*(S^3)$, aber nichttrivialer
Fundamentalgruppe (es ist die binäre Ikosaedergruppe der Ordnung 120).

Am Ende des fünften Complément formulierte er deshalb eine Frage, in der
„Homologie" durch das stärkere „Fundamentalgruppe" ersetzt ist:

> *„Est-il possible que le groupe fondamental de $V$ se réduise à la
> substitution identique, et que pourtant $V$ ne soit pas simplement
> connexe?"*
> — Henri Poincaré, *Cinquième complément à l'Analysis Situs* (1904)

Frei: Kann eine geschlossene 3-Mannigfaltigkeit mit trivialer
Fundamentalgruppe von der 3-Sphäre verschieden sein? Poincaré schließt
mit dem berühmten Satz: *„Mais cette question nous entraînerait trop
loin"* – diese Frage würde uns zu weit führen.

In moderner Sprache:

> **Poincaré-Vermutung (1904).** Jede geschlossene, einfach
> zusammenhängende 3-Mannigfaltigkeit ist homöomorph zu $S^3$.

## 2. Was die Vermutung ausschließt

Die Vermutung sagt nicht, dass $S^3$ die einzige geschlossene
3-Mannigfaltigkeit ist – das ist offensichtlich falsch. Es gibt
unendlich viele:

- den 3-Torus $T^3$ mit $\pi_1(T^3) = \mathbb{Z}^3$,
- die Linsenräume $L(p, q)$ mit $\pi_1 = \mathbb{Z}/p$,
- die Poincaré-Homologie-Sphäre mit $\pi_1$ der Ordnung 120,
- den Quotienten $S^2 \times S^1$ mit $\pi_1 = \mathbb{Z}$,
- und alle Konstruktionen aus Heegaard-Zerlegungen oder
  Dehn-Chirurgie.

Allen ist gemein: $\pi_1 \neq 0$. Die Vermutung behauptet, dass *unter
den einfach zusammenhängenden* nur eine einzige Mannigfaltigkeit
übrigbleibt. Wer die Geometrisierungs-Vermutung kennt
([Artikel 05](05-geometrisierungs-vermutung.md)), erkennt: Poincaré
ist genau der „kugelförmige" Spezialfall.

## 3. Warum war sie schwer?

Die scheinbare Einfachheit der Vermutung steht in scharfem Gegensatz zur
Schwere ihres Beweises.

**Keine direkte Konstruktion.** Aus „$\pi_1(M) = 0$" folgt nicht
unmittelbar eine Homöomorphie zu $S^3$. Die Fundamentalgruppe sieht nur
Schleifen; eine 3-dimensionale Identifikation mit $S^3$ verlangt
2-dimensionale Verklebungen.

**Klassische Werkzeuge versagen.** Heegaard-Zerlegung,
Dehn-Chirurgie, Ende-Theorie – alle blieben ohne durchgreifenden
Erfolg. Auch die Charakterisierung über Homotopie-Äquivalenz half nicht:
*Whitehead* zeigte 1934 in einem berüchtigten „Beweis", dass diese ohne
zusätzliche Annahmen scheitert.

**Dimensions-Wechsel hilft nicht.** In Dimension 1 und 2 ist die
Vermutung trivial bzw. klassisch (Klassifikation der Flächen). In
Dimension $\geq 5$ stehen Werkzeuge zur Verfügung, die in Dimension 3
fehlen, und in Dimension 4 funktionieren wieder andere Methoden. Genau
Dimension 3 ist „zu eng" für höhere Tricks und „zu weit" für
elementare Argumente.

> „Dimension three is at once the most and the least mysterious of the
> dimensions; we live in it, yet have struggled for over a century to
> understand its global topology."
> — John W. Morgan, *Recent progress on the Poincaré Conjecture and
> the classification of 3-manifolds*, BAMS (2005)

## 4. Die Verallgemeinerung – höhere Dimensionen

Sobald algebraische Topologie und Differentialtopologie reif waren,
ließ sich Poincarés Frage in beliebiger Dimension stellen:

> **Verallgemeinerte Poincaré-Vermutung.** Jede geschlossene
> $n$-Mannigfaltigkeit, die homotopieäquivalent zu $S^n$ ist, ist
> homöomorph zu $S^n$.

In Dimension $\geq 5$ ist „einfach zusammenhängend + Homologie wie
$S^n$" bereits stark genug. Die Resolution lief paradoxerweise von oben
nach unten:

| Jahr | Dim | Autor | Methode |
|------|-----|-------|---------|
| 1961 | $n \geq 5$ | Stephen Smale | $h$-Kobordismus, Handlebody-Theorie |
| 1962 | $n \geq 5$ | John Stallings, Christopher Zeeman | PL-Version, Engulfing |
| 1982 | $n = 4$ | Michael Freedman | Casson-Henkel, topologische Kategorie |
| 2002–2003 | $n = 3$ | Grigori Perelman | Ricci-Fluss mit Chirurgie |

Smale, Freedman und Perelman erhielten je eine Fields-Medaille bzw. den
Clay-Millennium-Preis. Bemerkenswert: In der **glatten** Kategorie ist
die Frage in Dimension 4 bis heute offen – die *Smooth Poincaré
Conjecture* in Dimension 4 ist eines der prominentesten ungelösten
Probleme der Topologie.

## 5. Die Clay-Millennium-Probleme

Im Jahr 2000 setzte das **Clay Mathematics Institute** sieben
„Millennium Prize Problems" mit je einer Million US-Dollar Preisgeld
aus. Die Poincaré-Vermutung in Dimension 3 war eines davon – und ist
bis heute das einzige gelöste.

Perelman lud zwischen November 2002 und Juli 2003 drei Preprints auf
arXiv hoch, die zusammen den Beweis lieferten. Nach jahrelanger
Verifikation durch mehrere Teams (Kleiner-Lott; Cao-Zhu; Morgan-Tian)
sprach das Clay-Institut 2010 den Preis offiziell zu. Perelman lehnte
sowohl Preisgeld als auch die ihm 2006 verliehene Fields-Medaille ab.

## 6. Hamiltons Programm – der Weg, der funktionierte

Der Weg zum Beweis führte nicht über klassische topologische Methoden,
sondern über **geometrische Analysis**. 1982 schlug Richard Hamilton
vor, eine Riemannsche Metrik $g$ auf $M$ einer Wärmeleitungs-artigen
Differentialgleichung zu unterwerfen:

$$
\frac{\partial g_{ij}}{\partial t} = -2 R_{ij},
$$

dem **Ricci-Fluss**. Hamilton bewies: Wenn $M^3$ einfach zusammenhängend
ist und eine Anfangsmetrik **positiver Ricci-Krümmung** existiert,
glättet der Fluss diese zu einer runden Sphäre. Die Mannigfaltigkeit ist
also $S^3$.

Diese Voraussetzung – *positive* Ricci-Krümmung – ist allerdings stark.
Ohne sie produziert der Fluss **Singularitäten**: Bereiche, in denen die
Krümmung in endlicher Zeit ins Unendliche wächst. Hamiltons Programm
sah vor, diese Singularitäten zu klassifizieren und durch **Chirurgie**
(kontrolliertes Ausschneiden und Einkleben) zu entfernen, um den Fluss
fortzusetzen. Bis 2002 fehlten dazu die analytischen Werkzeuge.

Perelman lieferte sie:

- ein **Entropie-Funktional** $\mathcal{F}$ und sein
  geheimnisvolleres Geschwister $\mathcal{W}$, deren Monotonie eine
  versteckte Variationsstruktur des Flusses offenbart;
- das **$\kappa$-Nichtkollaps-Theorem**, das untere Volumenschranken
  garantiert;
- die Klassifikation von **$\kappa$-Lösungen**, also den möglichen
  Singularitätsmodellen in Dimension 3;
- ein präzises Chirurgie-Verfahren samt Long-time-Analyse.

Akt 2 und Akt 3 der Poincaré-Storyline werden diese Werkzeuge
ausführlich entwickeln.

## 7. Ausblick

Im nächsten Artikel wird die **Geometrisierungs-Vermutung** von
William Thurston (1982) vorgestellt. Sie ist das eigentliche Resultat,
das Perelman bewiesen hat – die Poincaré-Vermutung folgt daraus als
Korollar. Thurston schlug vor, jede geschlossene 3-Mannigfaltigkeit
in geometrische Stücke zu zerlegen, von denen es genau **acht
Modellgeometrien** gibt.

| Artikel | Thema |
|---------|-------|
| [05 – Die Geometrisierungs-Vermutung](05-geometrisierungs-vermutung.md) | Acht Modellgeometrien, Zerlegung |
| [Akt 2 – Werkzeuge: Ricci-Fluss](../ricci-fluss/index.md) | Riemannsche Metrik, Krümmung, Hamiltons Fluss |

---

## Quellen

- **Henri Poincaré**: *Cinquième complément à l'Analysis Situs*,
  Rendiconti del Circolo Matematico di Palermo 18 (1904), 45–110
- **Stephen Smale**: *Generalized Poincaré's conjecture in dimensions
  greater than four*, Annals of Mathematics 74 (1961), 391–406
- **Michael H. Freedman**: *The topology of four-dimensional manifolds*,
  Journal of Differential Geometry 17 (1982), 357–453
- **Richard S. Hamilton**: *Three-manifolds with positive Ricci
  curvature*, Journal of Differential Geometry 17 (1982), 255–306
- **John W. Morgan, Gang Tian**: *Ricci Flow and the Poincaré
  Conjecture*, Clay Mathematics Monographs 3, AMS (2007)
- **Donal O'Shea**: *The Poincaré Conjecture: In Search of the Shape
  of the Universe*, Walker & Company (2007)
