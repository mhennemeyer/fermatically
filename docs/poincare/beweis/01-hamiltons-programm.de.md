---
title: "Hamiltons Programm und seine Hindernisse"
slug: poincare/beweis/01-hamiltons-programm
series: poincare
part: 1
act: beweis
date: 2026-04-27
status: draft
lang: de
tags:
  - hamilton
  - programm
  - surgery
  - perelman
---
# Hamiltons Programm und seine Hindernisse

!!! abstract "Zusammenfassung"
    Bevor Perelman 2002–2003 die Geometrisierungs-Vermutung bewies, hatte
    Richard **Hamilton** über zwanzig Jahre lang ein klares Programm
    skizziert: starte mit einer beliebigen Riemannschen Metrik auf einer
    geschlossenen 3-Mannigfaltigkeit $M^3$, lasse den **Ricci-Fluss**
    laufen, schneide auftretende Singularitäten chirurgisch heraus und
    fließe weiter – bis am Ende eine **Geometrisierung** im Sinne
    [Thurstons](../topologie/05-geometrisierungs-vermutung.md) sichtbar
    wird. Dieser Artikel zeichnet das Programm nach, fasst Hamiltons
    Teilresultate zusammen und benennt die fünf Hindernisse, an denen
    es bis 2002 gescheitert war. Perelmans drei Preprints
    schließen genau diese Lücken; die folgenden Artikel von Akt 3
    setzen seine Lösungen einzeln um.

## 1. Die Vision von 1982

Hamiltons erste Arbeit zum Ricci-Fluss ([Hamilton 1982,
*Three-manifolds with positive Ricci curvature*][hamilton1982]) ist
auch der Geburtsort des Programms. Er bewies dort:

> **Satz (Hamilton 1982).** Sei $(M^3, g_0)$ geschlossen mit strikt
> positivem Ricci-Tensor. Dann existiert der Ricci-Fluss
> $\partial_t g = -2\,\mathrm{Ric}(g)$ für alle Zeiten und konvergiert
> nach Reskalierung gegen eine Metrik konstanter positiver
> Schnittkrümmung. Insbesondere ist $M^3$ diffeomorph zu einer
> sphärischen Raumform $S^3/\Gamma$.

Schon in der Einleitung dieser Arbeit notiert Hamilton, dass derselbe
Mechanismus *im Prinzip* die Geometrisierungs-Vermutung beweisen
könnte – wenn man Singularitäten verstehen und kontrolliert
herausoperieren kann. In den darauffolgenden zwei Jahrzehnten arbeitete
er die Werkzeuge dafür aus: Kurzzeitexistenz mittels
DeTurck-Trick, Maximumsprinzipien für Tensoren, der
[Kompaktheitssatz](../ricci-fluss/04-singularitaeten-blowup.md), die
Differential-Harnack-Ungleichung und eine erste Surgery-Theorie in
Dimension 4.

## 2. Das Programm in einem Satz

Sei $(M^3, g_0)$ geschlossen, orientierbar. Der Ricci-Fluss ist eine
quasi-parabolische Evolutionsgleichung; nach Hamilton (vgl.
[Akt 2, Artikel 03](../ricci-fluss/03-hamiltons-ricci-fluss.md))
existiert er auf einem maximalen Intervall $[0, T_{\max})$. Das
Programm besteht aus vier Schritten:

1. **Fließen lassen**, bis $T_{\max}$ erreicht wird oder die Krümmung
   in endlich vielen Punkten explodiert.
2. **Singularitäten lokalisieren**: zeigen, dass jede entstehende
   Hochkrümmungsregion einer von wenigen Modellgeometrien ähnelt
   (Hals, Kappe, sphärische Raumform).
3. **Chirurgie**: jeden Hals durch zwei runde Kugelkappen ersetzen,
   die sphärischen Komponenten verwerfen.
4. **Wiederholen**, bis nach endlich vielen Surgery-Schritten und
   eventuell unendlicher Zeit eine Geometrisierung sichtbar wird.

Geometrisch heißt das: Der Fluss soll die *primäre* Zerlegung der
3-Mannigfaltigkeit in [zusammenhängende Summen](../topologie/05-geometrisierungs-vermutung.md)
und JSJ-Stücke automatisch ausführen.

## 3. Hamiltons Werkzeuge bis 2002

Bis zur Jahrtausendwende hatte Hamilton zentrale Bausteine
bereitgestellt:

| Baustein | Quelle | Rolle im Programm |
|----------|--------|-------------------|
| Kurzzeitexistenz, Eindeutigkeit | Hamilton 1982 / DeTurck 1983 | Schritt 1 starten |
| Maximumsprinzip für Tensoren | Hamilton 1986 | Krümmungs-Pinching |
| **Differential-Harnack** | Hamilton 1993 | Klassifikation antiker Lösungen |
| **Kompaktheitssatz für Flüsse** | Hamilton 1995 | Blow-up-Limits konstruieren |
| Hamilton–Ivey-Pinching | Hamilton 1995, Ivey 1993 | $\sec \to {\geq}\,0$ in Dim 3 |
| Klassifikation 2D antiker Lösungen | Hamilton 1995 | Modell für Hals/Zigarre |
| Surgery in Dimension 4 | Hamilton 1997 | Prototyp, $\mathrm{Rm}\geq 0$ |

[Hamilton 1995, *The formation of singularities in the Ricci flow*][hamilton1995],
ist dabei der wichtigste Übersichtsartikel: er führt den
Typ-I/II/III-Begriff ein, beweist den Kompaktheitssatz und formuliert
die strukturelle Vermutung, dass Singularitäten in Dim 3 auf
asymptotisch zylindrische Geometrien hinauslaufen.

## 4. Die fünf Hindernisse

Trotz dieser Werkzeuge blieb das Programm bis 2002 unvollständig.
Genau fünf Probleme widerstanden Hamiltons Methoden:

### H1 – Kollaps-Versagen

Hamiltons Kompaktheitssatz liefert Blow-up-Limits **nur**, wenn die
Volumen-Verhältnisse $\mathrm{Vol}(B_r)/r^n$ nicht entarten. Ohne eine
solche universelle Schranke kann eine Folge reskalierter Metriken
gegen ein **niederdimensionales** Objekt entarten – der „Kollaps".
Hamilton hatte zwar Spezialfälle abgedeckt, aber keinen allgemeinen
Beweis.

### H2 – Klassifikation antiker $\kappa$-Lösungen

Selbst wenn ein Blow-up-Limit existiert, muss man wissen *wie* es
aussieht. Hamilton hatte die Klassifikation in 2D, aber in Dimension 3
nur Vermutungen: $S^3/\Gamma$, $S^2 \times \mathbb{R}$ und ein
$\kappa$-nichtkollabierter Bryant-Soliton sollten alle möglichen
antiken Modelle sein.

### H3 – Kanonische Nachbarschaften

Selbst mit klassifiziertem Blow-up-Limit ist nicht klar, dass *jede*
Hochkrümmungsregion einer der Modellgeometrien ähnelt. Diesen
Strukturschritt – „großer Krümmungsskalar $\Rightarrow$ lokal
$\varepsilon$-nahe an Modell" – nennt man heute **kanonischen
Nachbarschaftssatz**.

### H4 – Surgery mit kontrollierten Konstanten

Hamilton hatte Surgery in Dim 4 nur unter der Annahme
$\mathrm{Rm}\geq 0$ konstruiert. In Dim 3 ohne diese Annahme war
unklar, ob die Surgery-Skalen $\delta, h, r$ untereinander mit
kohärenten Schranken gewählt werden können – und ob das
$\kappa$-Nichtkollaps nach jedem Surgery-Schritt erhalten bleibt.

### H5 – Endlich viele Surgeries auf endlichem Intervall

Selbst bei perfekter Surgery muss man ausschließen, dass
Surgery-Zeiten sich auf endlichem Intervall häufen. Andernfalls würde
der Prozess in endlicher Zeit „explodieren" und keine Geometrisierung
ergeben.

## 5. Was Perelman beitrug

Perelmans drei Preprints lösen diese Hindernisse in derselben
Reihenfolge:

| Hindernis | Perelmans Werkzeug | Verweis |
|-----------|--------------------|---------|
| H1 | Entropie $\mathcal{W}$ + reduziertes Volumen $\tilde V$ | [Akt 2, Art. 05](../ricci-fluss/05-perelman-entropie.md), [Art. 07](../ricci-fluss/07-reduzierte-laenge.md) |
| H2 | Hamilton–Ivey + $\kappa$-Nichtkollaps + $\mathcal{L}$-Geometrie | [Akt 2, Art. 06](../ricci-fluss/06-kappa-nichtkollaps.md) |
| H3 | Kanonischer Nachbarschaftssatz (0211159 §12) | [Akt 3, Art. 02](02-singularitaeten-dim3.md) |
| H4 | Surgery mit $\delta(t)$-Funktion (0303109 §3–§4) | [Akt 3, Art. 03](03-chirurgie.md) |
| H5 | Long-time-Existenz und thin–thick (0303109 §6, 0307245) | [Akt 3, Art. 04](04-long-time-verhalten.md), [Art. 05](05-endliche-extinktion.md) |

Dass dieselben Werkzeuge gleichzeitig die *Geometrisierung* und – über
finite extinction time – die *Poincaré-Vermutung* liefern, ist der
inhaltliche Kern von Akt 3.

## 6. Was Hamilton vorausgesehen hatte

Es ist instruktiv zu sehen, wie viel Hamiltons Programm bereits
vorzeichnete:

- Die Surgery-Architektur (Hals erkennen, durchschneiden, mit Kappe
  füllen) ist in Hamilton 1997 schon angelegt.
- Die strukturelle Vermutung „Singularitäten in Dim 3 sehen aus wie
  Zylinder" ist Hamilton 1995 wörtlich enthalten.
- Hamilton selbst betonte, dass *Volumen-Nichtkollaps* die fehlende
  globale Schranke ist – seine Differential-Harnack-Arbeit liefert
  bereits die Hälfte des Werkzeugs.

Was fehlte, war ein **Monotonieprinzip**, das diese Schranke aus dem
Fluss selbst gewinnt – Perelmans Entropie und reduzierte Länge.

## 7. Roadmap durch Akt 3

Die folgenden Artikel führen die Lösung der fünf Hindernisse aus:

- **02 – Singularitätsanalyse Dim 3** klassifiziert antike
  $\kappa$-Lösungen und beweist den kanonischen Nachbarschaftssatz
  (H2 + H3).
- **03 – Ricci-Fluss mit Chirurgie** definiert Standard-Lösung,
  $\delta$-Hälse und führt Surgery auf einem Intervall mit
  kontrollierten Konstanten durch (H4).
- **04 – Long-time-Verhalten** zeigt, dass Surgery-Zeiten sich nicht
  häufen, und liefert die thin–thick-Zerlegung als $t \to \infty$
  (H5 + Geometrisierung).
- **05 – Finite Extinction Time** ist der Kurzweg zur
  Poincaré-Vermutung: bei einfach-zusammenhängender Anfangs-
  Mannigfaltigkeit erlischt der Fluss in endlicher Zeit
  (Perelman 0307245, Colding–Minicozzi 2005).
- **06 – Geometrisierung impliziert Poincaré** schließt den Kreis und
  zeigt, wie das volle Geometrisierungs-Resultat die ursprüngliche
  Vermutung als Korollar enthält.

## Quellen

- **R. Hamilton**, *Three-manifolds with positive Ricci curvature*,
  J. Differential Geom. 17 (1982), 255–306. [PDF][hamilton1982]
- **R. Hamilton**, *The formation of singularities in the Ricci flow*,
  Surveys in Differential Geometry II (1995), 7–136.
  [PDF][hamilton1995]
- **R. Hamilton**, *Four-manifolds with positive isotropic curvature*,
  Comm. Anal. Geom. 5 (1997), 1–92. (Surgery-Prototyp.)
- **G. Perelman**, *The entropy formula for the Ricci flow and its
  geometric applications*,
  [arXiv:math/0211159](https://arxiv.org/abs/math/0211159).
- **G. Perelman**, *Ricci flow with surgery on three-manifolds*,
  [arXiv:math/0303109](https://arxiv.org/abs/math/0303109).
- **G. Perelman**, *Finite extinction time for the solutions to the
  Ricci flow on certain three-manifolds*,
  [arXiv:math/0307245](https://arxiv.org/abs/math/0307245).
- **J. Morgan, G. Tian**, *Ricci Flow and the Poincaré Conjecture*,
  Clay Math. Monographs 3, AMS 2007. (Komplette Ausarbeitung.)
- **B. Kleiner, J. Lott**, *Notes on Perelman's papers*,
  Geom. Topol. 12 (2008), 2587–2855.
- **H.-D. Cao, X.-P. Zhu**, *A complete proof of the Poincaré and
  geometrization conjectures*, Asian J. Math. 10 (2006), 165–492.

[hamilton1982]: https://projecteuclid.org/euclid.jdg/1214436922
[hamilton1995]: https://www.intlpress.com/site/pub/files/_fulltext/journals/sdg/1995/0002/0001/SDG-1995-0002-0001-a002.pdf
