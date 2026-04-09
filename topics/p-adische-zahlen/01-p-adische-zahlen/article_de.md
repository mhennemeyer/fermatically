---
title: "p-adische Zahlen – Eine andere Art, Zahlen zu betrachten"
slug: p-adische-zahlen/01-p-adische-zahlen
series: p-adische-zahlen
part: 1
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - p-adisch
  - bewertung
  - lokal-global
requires:
  - teilbarkeit-ggt
  - modulare-arithmetik
  - grenzwerte-konvergenz
  - summen-produktnotation
  - potenzen-polynome
---

# $p$-adische Zahlen

!!! abstract "Zusammenfassung"
    Neben den reellen Zahlen $\mathbb{R}$ gibt es für jede Primzahl $p$ die $p$-adischen Zahlen $\mathbb{Q}_p$ –
    eine alternative Vervollständigung von $\mathbb{Q}$, in der „nah bei Null" gleichbedeutend mit
    „durch hohe $p$-Potenzen teilbar" ist.

## Voraussetzungen

- [Ringe und Körper](../../ringe-und-koerper/01-ringe-koerper/article_de.md)

| Thema | Beschreibung |
|-------|-------------|
| [Teilbarkeit und ggT](../../vorwissen/teilbarkeit-ggt/article_de.md) | Teilerfremdheit, $\gcd$, Euklidischer Algorithmus |
| [Modulare Arithmetik](../../vorwissen/modulare-arithmetik/article_de.md) | Kongruenzen $a \equiv b \pmod{n}$ und Restklassen |
| [Grenzwerte und Konvergenz](../../vorwissen/grenzwerte-konvergenz/article_de.md) | $\lim_{n \to \infty} a_n = L$, Cauchy-Folgen, Reihen |
| [Summen- und Produktnotation](../../vorwissen/summen-produktnotation/article_de.md) | $\sum$- und $\prod$-Notation |
| [Potenzen und Polynome](../../vorwissen/potenzen-polynome/article_de.md) | Potenzschreibweise $a^n$ und Polynomrechnung |

---

## 1. Eine andere Metrik

Die übliche Abstandsmessung auf $\mathbb{Q}$ nutzt den **gewöhnlichen Betrag** $|x|$: Die Zahl $1/1000$ ist nah bei $0$, weil $|1/1000|$ klein ist.

Es gibt jedoch eine andere Definition von „Nähe", die auf Teilbarkeit basiert statt auf Größe.

**Definition.** Sei $p$ eine Primzahl. Die **$p$-adische Bewertung** $v_p(n)$ einer ganzen Zahl $n \neq 0$ ist die höchste Potenz von $p$, die $n$ teilt:

$$
v_p(n) = \max\{k \geq 0 \mid p^k \mid n\}
$$

Beispiele für $p = 3$: $v_3(54) = 3$ (denn $54 = 2 \cdot 3^3$), $v_3(7) = 0$, $v_3(81) = 4$.

Der **$p$-adische Betrag** ist:

$$
|x|_p = p^{-v_p(x)} \quad \text{für } x \neq 0, \qquad |0|_p = 0
$$

Je mehr $p$-Potenzen eine Zahl enthält, desto *kleiner* ihr $p$-adischer Betrag. Für $p = 5$:

| Zahl $x$ | $v_5(x)$ | $\|x\|_5$ | $\|x\|$ (gewöhnlich) |
|-----------|-----------|------------|----------------------|
| $1$ | $0$ | $1$ | $1$ |
| $5$ | $1$ | $1/5$ | $5$ |
| $25$ | $2$ | $1/25$ | $25$ |
| $625$ | $4$ | $1/625$ | $625$ |
| $1/5$ | $-1$ | $5$ | $0{,}2$ |

Die Zahl $625$ ist $5$-adisch nahe $0$ (Betrag $1/625$), gewöhnlich jedoch groß.

## 2. Konvergenz in $\mathbb{Q}_p$

Der $p$-adische Betrag definiert eine Metrik auf $\mathbb{Q}$: $d_p(x, y) = |x - y|_p$. In dieser Metrik gelten Konvergenzaussagen, die aus Sicht der reellen Analysis unerwartet sind.

**Beispiel: Die Reihe $\sum_{n=0}^{\infty} p^n$ konvergiert in $\mathbb{Q}_p$.**

Die Partialsummen $S_N = 1 + p + p^2 + \cdots + p^N$ konvergieren $p$-adisch, weil $|p^n|_p = p^{-n} \to 0$. Der Grenzwert:

$$
\sum_{n=0}^{\infty} p^n = \frac{1}{1-p} = \frac{-1}{p-1}
$$

In $\mathbb{Q}_5$ gilt also $1 + 5 + 25 + 125 + \cdots = -\frac{1}{4}$. Das klingt paradox, ist $5$-adisch aber korrekt.

> „The $p$-adic numbers are just as 'real' as the real numbers — they are simply a different completion of the rationals."
> — Fernando Gouvêa, *p-adic Numbers: An Introduction* (1997), S. 1

### Die ultrametrische Ungleichung

Der $p$-adische Betrag erfüllt eine stärkere Eigenschaft als die Dreiecksungleichung:

$$
|x + y|_p \leq \max(|x|_p, |y|_p)
$$

Die **ultrametrische Ungleichung** (oder „starke Dreiecksungleichung") hat Konsequenzen:

- Jedes Dreieck in $\mathbb{Q}_p$ ist **gleichschenklig** (die beiden längsten Seiten sind gleich lang)
- Jeder Punkt eines „Kreises" ist dessen Mittelpunkt
- Reihen konvergieren genau dann, wenn ihre Summanden gegen $0$ gehen (kein Quotientenkriterium nötig)

## 3. Konstruktion von $\mathbb{Q}_p$

Die reellen Zahlen $\mathbb{R}$ entstehen als **Vervollständigung** von $\mathbb{Q}$ bezüglich des gewöhnlichen Betrags $|\cdot|$: Hinzufügen der Grenzwerte aller Cauchy-Folgen.

Analog: Die **$p$-adischen Zahlen** $\mathbb{Q}_p$ sind die Vervollständigung von $\mathbb{Q}$ bezüglich des $p$-adischen Betrags $|\cdot|_p$.

Formal: $\mathbb{Q}_p$ ist der Quotientenkörper der Cauchy-Folgen in $(\mathbb{Q}, |\cdot|_p)$ modulo Nullfolgen. Jedes Element von $\mathbb{Q}_p$ lässt sich eindeutig als **$p$-adische Entwicklung** schreiben:

$$
x = \sum_{n=k}^{\infty} a_n p^n \quad \text{mit } a_n \in \{0, 1, \ldots, p-1\}, \quad k \in \mathbb{Z}
$$

Eine Art „Dezimalentwicklung", aber nach links unendlich statt nach rechts. Die gewöhnliche Dezimaldarstellung $0{,}333\ldots = 1/3$ hat endlich viele Stellen vor dem Komma und unendlich viele danach. In $\mathbb{Q}_p$ ist es umgekehrt: endlich viele Stellen nach dem „Komma" (negative $p$-Potenzen) und potenziell unendlich viele davor.

## 4. Ostrowskis Satz

Wie viele wesentlich verschiedene Beträge existieren auf $\mathbb{Q}$?

**Satz (Ostrowski, 1916).** Jeder nichttriviale Betrag auf $\mathbb{Q}$ ist äquivalent zu einem der folgenden:

- Dem **gewöhnlichen Betrag** $|\cdot|$ (dessen Vervollständigung $\mathbb{R}$ liefert)
- Einem **$p$-adischen Betrag** $|\cdot|_p$ für eine Primzahl $p$ (dessen Vervollständigung $\mathbb{Q}_p$ liefert)

$\mathbb{R}$ und die $\mathbb{Q}_p$ (für alle Primzahlen $p$) sind also die **einzigen** Vervollständigungen von $\mathbb{Q}$. Jede Stelle – jede Art, $\mathbb{Q}$ zu vervollständigen – entspricht entweder dem archimedischen Betrag ($\infty$-Stelle) oder einem $p$-adischen Betrag ($p$-Stelle).

!!! note "Hasses Prinzip"
    Die Stellen von $\mathbb{Q}$ werden als $v \in \{\infty, 2, 3, 5, 7, \ldots\}$ indiziert. Die lokalen Körper $\mathbb{Q}_v$ (mit $\mathbb{Q}_\infty = \mathbb{R}$) bilden zusammen ein vollständiges Bild der rationalen Zahlen – $\mathbb{Q}$, betrachtet aus allen lokalen Perspektiven gleichzeitig.

## 5. Die $p$-adischen ganzen Zahlen $\mathbb{Z}_p$

Der **Bewertungsring** von $\mathbb{Q}_p$ besteht aus allen Elementen mit $p$-adischem Betrag $\leq 1$:

$$
\mathbb{Z}_p = \{x \in \mathbb{Q}_p \mid |x|_p \leq 1\} = \left\{ \sum_{n=0}^{\infty} a_n p^n \mid a_n \in \{0, \ldots, p-1\} \right\}
$$

$\mathbb{Z}_p$ ist ein **lokaler Ring** mit dem einzigen maximalen Ideal $(p) = p\mathbb{Z}_p$. Der Restklassenkörper ist:

$$
\mathbb{Z}_p / p\mathbb{Z}_p \cong \mathbb{F}_p
$$

Alternative Beschreibung als **projektiver Limes**:

$$
\mathbb{Z}_p = \varprojlim_n \mathbb{Z}/p^n\mathbb{Z}
$$

Ein Element von $\mathbb{Z}_p$ ist ein kompatibles System $(a_1, a_2, a_3, \ldots)$ von Restklassen: $a_n \in \mathbb{Z}/p^n\mathbb{Z}$ mit $a_{n+1} \equiv a_n \pmod{p^n}$.

**Eigenschaften von $\mathbb{Z}_p$:**

- $\mathbb{Z}_p$ ist ein Hauptidealring (sogar ein diskreter Bewertungsring)
- Die Einheiten sind $\mathbb{Z}_p^\times = \{x \in \mathbb{Z}_p \mid |x|_p = 1\} = \mathbb{Z}_p \setminus p\mathbb{Z}_p$
- $\mathbb{Z} \subset \mathbb{Z}_p$ ist dicht (jede $p$-adische ganze Zahl ist Limes einer Folge ganzer Zahlen)
- $\mathbb{Z}_p$ ist kompakt (als topologischer Raum)

## 6. Hensels Lemma

Eines der zentralen Werkzeuge der $p$-adischen Analysis – die $p$-adische Version des Newtonschen Näherungsverfahrens.

**Satz (Hensel).** Sei $f \in \mathbb{Z}_p[x]$ ein Polynom. Wenn $a \in \mathbb{Z}$ eine **einfache** Nullstelle von $f$ modulo $p$ ist (d.h. $f(a) \equiv 0 \pmod{p}$ und $f'(a) \not\equiv 0 \pmod{p}$), dann existiert eine eindeutige Nullstelle $\alpha \in \mathbb{Z}_p$ von $f$ mit $\alpha \equiv a \pmod{p}$.

Die Konstruktion: Aus einer approximativen Lösung modulo $p$ wird schrittweise eine exakte Lösung in $\mathbb{Z}_p$ erzeugt – durch iteriertes Liften modulo $p^2$, $p^3$, $p^4$, und so weiter.

**Beispiel:** Existiert $\sqrt{2}$ in $\mathbb{Q}_7$? Prüfung: $3^2 = 9 \equiv 2 \pmod{7}$ und $2 \cdot 3 = 6 \not\equiv 0 \pmod{7}$. Nach Hensel existiert $\sqrt{2} \in \mathbb{Z}_7$. Dagegen ist $x^2 \equiv 2 \pmod{5}$ unlösbar, also $\sqrt{2} \notin \mathbb{Q}_5$.

!!! tip "Hensel als Reduktionswerkzeug"
    Hensels Lemma reduziert $p$-adische Fragen auf endliche Rechnungen modulo $p$. Statt im unendlichen Körper $\mathbb{Q}_p$ zu arbeiten, genügt es oft, im endlichen Körper $\mathbb{F}_p$ zu rechnen – und dann zu liften.

## 7. Das Lokal-Global-Prinzip

Die zentrale Idee: Informationen über $\mathbb{Q}$ lassen sich aus der Kombination **aller** lokalen Informationen (über $\mathbb{R}$ und alle $\mathbb{Q}_p$) gewinnen.

**Hasse-Minkowski-Theorem.** Eine quadratische Form über $\mathbb{Q}$ hat genau dann eine nichttriviale Lösung in $\mathbb{Q}$, wenn sie eine Lösung in $\mathbb{R}$ **und** in $\mathbb{Q}_p$ für **alle** Primzahlen $p$ hat.

Dieses Lokal-Global-Prinzip funktioniert für quadratische Formen, aber nicht immer. Für kubische Gleichungen und elliptische Kurven kann es versagen: Es gibt Kurven mit lokalen Punkten überall, aber ohne globalen rationalen Punkt. Das Maß für dieses Versagen ist die **Tate-Shafarevich-Gruppe** $\Sha$.

### Lokale Bedingungen in Wiles' Beweis

In Wiles' Beweis spielen die lokalen Körper $\mathbb{Q}_p$ eine fundamentale Rolle:

1. **Reduktion modulo $p$**: Eine elliptische Kurve $E/\mathbb{Q}$ kann modulo jeder Primzahl $p$ betrachtet werden, was eine Kurve $\tilde{E}/\mathbb{F}_p$ liefert. Ob diese Reduktion glatt ist oder Singularitäten hat, bestimmt den **Typ** der Kurve an der Stelle $p$.

2. **Lokale Galois-Darstellungen**: Die Einschränkung $\rho|_{G_{\mathbb{Q}_p}}$ einer Galois-Darstellung auf die lokale Galois-Gruppe kodiert das Verhalten der Darstellung an der Stelle $p$. Die **Deformationstheorie** von Mazur klassifiziert Darstellungen nach ihren lokalen Eigenschaften.

3. **Semistabilität**: Eine elliptische Kurve heißt **semistabil**, wenn sie an jeder Stelle $p$ entweder gute oder multiplikative Reduktion hat. Wiles bewies die Taniyama-Shimura-Vermutung zunächst nur für semistabile Kurven – ausreichend für FLT, da die Frey-Kurve semistabil ist.

> „The interplay between the local and the global is one of the central themes of modern number theory."
> — Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (1984), Vorwort

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 5
- **Neal Koblitz**: *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, Springer (1984)
- **Fernando Gouvêa**: *p-adic Numbers: An Introduction*, Springer (1997)
