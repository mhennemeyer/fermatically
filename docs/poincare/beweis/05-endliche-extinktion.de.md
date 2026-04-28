---
title: "Endliche Auslöschungszeit"
slug: poincare/beweis/05-endliche-extinktion
series: poincare
part: 5
act: beweis
date: 2026-04-28
status: draft
lang: de
tags:
  - finite-extinction
  - poincare
  - perelman
  - minimalflaechen
---

# Endliche Auslöschungszeit

> *„For any metric $g_0$ on a closed simply connected three-manifold $M$,
> the Ricci flow with surgery starting from $g_0$ becomes extinct in finite
> time."*
> — Perelman, *Finite extinction time for the solutions to the Ricci flow
> on certain three-manifolds*, arXiv:math/0307245, Theorem 1.1

In [Artikel 04](04-long-time-verhalten.md) haben wir die Geometrisierung
mittels dünn-dick-Zerlegung bewiesen – das *eigentliche* Resultat
Perelmans. Für die **Poincaré-Vermutung** allein gibt es jedoch einen
deutlich kürzeren Weg: Ist $M$ einfach zusammenhängend, so verschwindet
der Ricci-Fluss mit Chirurgie schon in **endlicher Zeit**. Dieser Artikel
folgt Perelman *0307245* und der parallel publizierten Arbeit von
Colding & Minicozzi (2005).

## 1. Was bedeutet „Extinktion"?

Eine Lösung des Ricci-Flusses mit Chirurgie heißt **endlich erloschen**,
wenn es ein $T < \infty$ gibt mit $M_t = \emptyset$ für alle $t \ge T$ –
d. h. ab $T$ wurde *jede* Komponente durch Chirurgie als sphärische
Raumform $S^3/\Gamma$ erkannt und entfernt. Mit anderen Worten: Der
Algorithmus aus [Artikel 03](03-chirurgie.md) terminiert, statt unendlich
viele Chirurgie-Zeiten anzusammeln.

Das ist eine *topologische* Aussage in analytischer Verkleidung: Wenn die
Mannigfaltigkeit nur aus sphärischen Komponenten besteht, sieht der Fluss
das durch eine global wachsende positive Krümmung und löscht alles aus.

## 2. Schlüsselidee: Flächeninhalt von Minimalflächen unter dem Fluss

Perelmans Strategie ist nicht analytisch (Volumens- oder
Krümmungsabschätzungen), sondern **topologisch-geometrisch**: Man
betrachtet 2-Sphären in $M$, die unter dem Fluss als Hindernis gegen
Extinktion fungieren würden, und zeigt, dass deren minimaler
Flächeninhalt monoton fällt – schnell genug, um in endlicher Zeit auf
Null zu treffen.

### 2.1 Das Funktional $W_2$ (für $\pi_2(M) \neq 0$)

Sei $M$ kompakt mit $\pi_2(M) \neq 0$. Für jede nichttriviale Klasse
$\alpha \in \pi_2(M)$ definiere
$$
W_2(g, \alpha) := \inf\{\,\mathrm{Area}_g(f)\ :\ f : S^2 \to M,\ [f] = \alpha\,\}.
$$
Das ist der minimale **harmonische 2-Sphären-Flächeninhalt** in der
Klasse $\alpha$ – existiert nach Sacks–Uhlenbeck (1981).

**Lemma (Perelman 0307245, §2).** Längs des Ricci-Flusses gilt für die
Funktion $t \mapsto W_2(g(t), \alpha)$ die Differentialungleichung
$$
\frac{d}{dt} W_2(g(t), \alpha) \le -4\pi - \tfrac{1}{2} R_{\min}(t)\, W_2(g(t), \alpha),
$$
wobei $R_{\min}(t) = \min_{x \in M_t} R(x, t)$ die minimale Skalarkrümmung
ist.

Das ist die zentrale Differentialungleichung des Beweises. Sie sagt: Selbst
wenn $R_{\min} \le 0$ ist, fällt $W_2$ um mindestens $4\pi$ pro Zeiteinheit,
weil die mittlere Krümmung der Minimalfläche durch die Gauß-Bonnet-Konstante
$4\pi \chi(S^2) = 4\pi \cdot 2 / 2 = 4\pi$ beschränkt ist. Konsequenz:
$W_2 \to 0$ in endlicher Zeit, was nur möglich ist, wenn die Klasse
$\alpha$ verschwindet, d. h. die zugehörige $S^2$ in der Prim-Zerlegung
durch Chirurgie abgekapselt wurde.

### 2.2 Das Funktional $W_3$ (für $\pi_3(M) \neq 0$)

Wenn $\pi_2(M) = 0$, aber $\pi_1(M) = 0$ und $M$ ist 3-dimensional,
folgt aus der Hurewicz-Sequenz $\pi_3(M) \cong H_3(M; \mathbb{Z})
\cong \mathbb{Z}$. Statt 2-Sphären betrachtet man nun **Familien** von
2-Sphären, parametrisiert durch $S^1$ (also stetige Loops im Raum der
Abbildungen $S^2 \to M$, deren Anfangs- und Endabbildung konstant sind).
Solche Familien repräsentieren Klassen in $\pi_1(\Lambda M, *) \cong
\pi_3(M)$.

Definiere für eine nichttriviale Klasse $\beta \in \pi_3(M)$:
$$
W_3(g, \beta) := \inf_{[\gamma] = \beta}\ \max_{s \in S^1} \mathrm{Area}_g(\gamma(s)).
$$

**Lemma (Perelman 0307245, §3; Colding–Minicozzi 2005).**
$$
\frac{d}{dt} W_3(g(t), \beta) \le -4\pi - \tfrac{1}{2} R_{\min}(t)\, W_3(g(t), \beta).
$$

Die Ungleichung ist *strukturell identisch* zu der für $W_2$: Sie folgt aus
einer min-max-Konstruktion und dem Gauß-Bonnet-Satz. Wieder erzwingt sie
$W_3 \to 0$ in endlicher Zeit.

## 3. Hauptsatz und Korollar

**Theorem (Perelman 0307245, Theorem 1.1).** Sei $M$ eine kompakte
orientierte 3-Mannigfaltigkeit ohne azyklische sphärische Faktoren in
ihrer Prim-Zerlegung – konkret: ohne Faktor mit unendlicher
Fundamentalgruppe und ohne aspherische Faktoren. Dann erlischt der
Ricci-Fluss mit Chirurgie aus [Artikel 03](03-chirurgie.md) für *jede*
Anfangsmetrik in endlicher Zeit.

**Korollar (Beweis-relevanter Spezialfall).** Ist $M$ einfach
zusammenhängend, so erlischt der Fluss in endlicher Zeit.

Beweisskizze des Korollars: Aus $\pi_1(M) = 0$ und Hurewicz folgt
$\pi_3(M) \neq 0$ (sogar $\cong \mathbb{Z}$ für eine Sphäre, $\cong
\mathbb{Z}^k$ für eine Verbindungssumme). Die $W_3$-Ungleichung erzwingt
endliche Extinktion: Der Fluss kann nicht für alle Zeiten existieren,
ohne dass alle nichttrivialen Klassen in $\pi_2$ und $\pi_3$ durch
Chirurgie aufgelöst werden. Da der Algorithmus jede solche Auflösung als
sphärische Raumform abwirft, bleibt am Ende nichts übrig.

## 4. Zwei unabhängige Beweise

| Autor | Preprint | Strategie |
|-------|----------|-----------|
| Perelman (2003) | arXiv:math/0307245, 7 S. | min-max über Loops, Gauß-Bonnet, $W_3$ |
| Colding & Minicozzi (2005) | arXiv:math/0308090, 16 S. | Birkhoff-min-max, harmonic replacement |

Beide nutzen die Idee „2-Sphären unter Ricci-Fluss schrumpfen wegen
Gauß-Bonnet"; Colding & Minicozzi liefern eine vollständig
ausgearbeitete Version, die heute als Standardreferenz gilt
(*Annals of Math.* 2008).

## 5. Was Extinktion *nicht* leistet

Endliche Extinktion erkennt nur, *dass* die Mannigfaltigkeit aus
sphärischen Raumformen besteht. Sie liefert keine **Strukturaussage über
hyperbolische oder Seifert-gefaserte Stücke** – dafür braucht man
weiterhin die dünn-dick-Zerlegung aus [Artikel 04](04-long-time-verhalten.md).
Für die volle Geometrisierung ist das Extinktions-Argument *nicht*
ausreichend.

| Vermutung | benötigt Extinktion? | benötigt dünn-dick? |
|-----------|----------------------|---------------------|
| Poincaré (einfach zusammenhängend) | ja (Kurzweg) | nein |
| Sphärische-Raumform-Vermutung ($\pi_1$ endlich) | ja | nein |
| Volle Geometrisierung | nein | ja |

## 6. Welche Hindernisse jetzt fallen

| Hindernis (siehe [Artikel 01](01-hamiltons-programm.md)) | Lösung |
|-----------|--------|
| O5: Topologie aus dem Limes ablesen, *speziell* für einfach zusammenhängende $M$ | $\pi_3 \neq 0 \Rightarrow$ $W_3$-Monotonie $\Rightarrow$ endliche Extinktion |
| O3' (Variante): unendlich viele Chirurgie-Zeiten ausschließen | $W_3 \to 0$ in endlicher Zeit terminiert den Algorithmus |

## Querverweise

- Vorher: [Ricci-Fluss mit Chirurgie](03-chirurgie.md) – stellt den Algorithmus bereit, dessen Termination wir hier zeigen.
- Vorher: [Long-time-Verhalten](04-long-time-verhalten.md) – der lange Weg über die volle Geometrisierung.
- Vorwissen Topologie: [Sphäre & einfacher Zusammenhang](../topologie/03-sphaere-einfacher-zusammenhang.md), [Was ist die Poincaré-Vermutung?](../topologie/04-was-ist-poincare-vermutung.md).
- Nächster Artikel: [Geometrisierung impliziert Poincaré](06-poincare-aus-geometrisierung.md) – das topologische Schluss-Argument.

## Quellen

- Perelman, G. (2003). *Finite extinction time for the solutions to the Ricci flow on certain three-manifolds*. arXiv:math/0307245.
- Colding, T. H. & Minicozzi, W. P. (2005). *Estimates for the extinction time for the Ricci flow on certain 3-manifolds and a question of Perelman*. J. Amer. Math. Soc. 18, 561–569. arXiv:math/0308090.
- Colding, T. H. & Minicozzi, W. P. (2008). *Width and finite extinction time of Ricci flow*. Geom. Topol. 12, 2537–2586.
- Sacks, J. & Uhlenbeck, K. (1981). *The existence of minimal immersions of 2-spheres*. Ann. of Math. 113, 1–24.
- Morgan, J. & Tian, G. (2007). *Ricci Flow and the Poincaré Conjecture*. AMS, Kapitel 18 – ausgearbeiteter Extinktions-Beweis.
- Kleiner, B. & Lott, J. (2008). *Notes on Perelman's papers*. Geom. Topol. 12, §§94–96.
