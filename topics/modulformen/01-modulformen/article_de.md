---
title: "Modulformen – Symmetrische Funktionen der oberen Halbebene"
slug: modulformen/01-modulformen
series: modulformen
part: 1
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - modulformen
  - fourier
  - hecke-operatoren
requires:
  - komplexe-zahlen
  - summen-produktnotation
  - grenzwerte-konvergenz
  - abbildungen
---

# Modulformen

!!! abstract "Zusammenfassung"
    Holomorphe Funktionen mit Symmetrie unter $\text{SL}_2(\mathbb{Z})$. Ihre Fourier-Koeffizienten
    tragen zahlentheoretische Information, und ihre $L$-Reihen sind die Gegenstücke
    der $L$-Reihen elliptischer Kurven.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](../../gruppen-und-symmetrie/01-gruppen/article_de.md)
- [Ringe und Körper](../../ringe-und-koerper/01-ringe-koerper/article_de.md)

| Thema | Beschreibung |
|-------|-------------|
| [Komplexe Zahlen](../../vorwissen/komplexe-zahlen/article_de.md) | Zahlen $a + bi$ mit $i^2 = -1$, Polarform, Einheitswurzeln |
| [Summen- und Produktnotation](../../vorwissen/summen-produktnotation/article_de.md) | $\sum$- und $\prod$-Notation |
| [Grenzwerte und Konvergenz](../../vorwissen/grenzwerte-konvergenz/article_de.md) | $\lim_{n \to \infty} a_n = L$, Cauchy-Folgen, Reihen |
| [Abbildungen (Funktionen)](../../vorwissen/abbildungen/article_de.md) | $f: A \to B$, injektiv, surjektiv, bijektiv |

Hilfreich, aber nicht zwingend:
- [Elliptische Kurven](../../elliptische-kurven/01-elliptische-kurven/article_de.md)

---

## 1. Die obere Halbebene

Die **obere Halbebene** ist die Menge der komplexen Zahlen mit positivem Imaginärteil:

$$
\mathbb{H} = \{z \in \mathbb{C} \mid \text{Im}(z) > 0\}
$$

Auf $\mathbb{H}$ wirkt die Gruppe $\text{SL}_2(\mathbb{Z})$ – die $2 \times 2$-Matrizen mit ganzzahligen Einträgen und Determinante $1$:

$$
\text{SL}_2(\mathbb{Z}) = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \mid a, b, c, d \in \mathbb{Z}, \, ad - bc = 1 \right\}
$$

Die Wirkung geschieht durch **Möbius-Transformationen**:

$$
\gamma \cdot z = \frac{az + b}{cz + d} \qquad \text{für } \gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

Für $z \in \mathbb{H}$ gilt auch $\gamma \cdot z \in \mathbb{H}$ – die obere Halbebene ist unter dieser Wirkung abgeschlossen.

$\text{SL}_2(\mathbb{Z})$ wird von zwei Matrizen erzeugt:

$$
T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}: z \mapsto z + 1 \qquad \text{(Translation)}
$$

$$
S = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}: z \mapsto -\frac{1}{z} \qquad \text{(Inversion)}
$$

## 2. Definition einer Modulform

Eine **Modulform vom Gewicht $k$** für $\text{SL}_2(\mathbb{Z})$ ist eine holomorphe Funktion $f: \mathbb{H} \to \mathbb{C}$, die zwei Bedingungen erfüllt:

**(M1) Transformationsverhalten.** Für alle $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \text{SL}_2(\mathbb{Z})$:

$$
f\left(\frac{az + b}{cz + d}\right) = (cz + d)^k f(z)
$$

**(M2) Holomorphie am Rand.** $f$ ist auch „bei $z \to i\infty$" holomorph (die Fourier-Entwicklung hat keine negativen Potenzen).

Aus der Translation $T: z \mapsto z + 1$ folgt:

$$
f(z + 1) = f(z)
$$

$f$ ist also periodisch mit Periode $1$ und besitzt eine **Fourier-Entwicklung**.

> „Modular forms are functions on the upper half plane which are inordinately symmetric."
> — Fred Diamond, Jerry Shurman, *A First Course in Modular Forms* (2005), S. 1

!!! note "Das Gewicht"
    Das Gewicht $k$ muss eine gerade natürliche Zahl sein (für $\text{SL}_2(\mathbb{Z})$). Der Faktor $(cz + d)^k$ ist der „Preis" der Symmetrie: $f$ ist nicht invariant unter $\text{SL}_2(\mathbb{Z})$, sondern transformiert sich mit einem Korrekturfaktor.

Eine Modulform heißt **Spitzenform** (cusp form), wenn zusätzlich $f(z) \to 0$ für $z \to i\infty$, also wenn der konstante Term der Fourier-Entwicklung verschwindet.

## 3. Fourier-Entwicklung

Da $f(z + 1) = f(z)$, lässt sich die Variable $q = e^{2\pi i z}$ einführen. Für $z \in \mathbb{H}$ ist $|q| < 1$, und $f$ hat eine Entwicklung:

$$
f(z) = \sum_{n=0}^{\infty} a_n q^n = a_0 + a_1 q + a_2 q^2 + a_3 q^3 + \cdots
$$

Die Koeffizienten $a_n$ heißen **Fourier-Koeffizienten** der Modulform. Für Spitzenformen gilt $a_0 = 0$.

Die Fourier-Koeffizienten tragen die gesamte arithmetische Information der Modulform. Dass diese Koeffizienten zahlentheoretische Bedeutung besitzen, zählt zu den tiefsten Phänomenen der Mathematik.

## 4. Beispiele

### Eisenstein-Reihen

Für gerades $k \geq 4$ ist die **Eisenstein-Reihe** definiert als:

$$
G_k(z) = \sum_{\substack{(c,d) \in \mathbb{Z}^2 \\ (c,d) \neq (0,0)}} \frac{1}{(cz + d)^k}
$$

Die normierte Version $E_k(z) = \frac{G_k(z)}{2\zeta(k)}$ hat die Fourier-Entwicklung:

$$
E_k(z) = 1 - \frac{2k}{B_k} \sum_{n=1}^{\infty} \sigma_{k-1}(n) \, q^n
$$

wobei $B_k$ die $k$-te Bernoulli-Zahl und $\sigma_{k-1}(n) = \sum_{d \mid n} d^{k-1}$ die Teilersummenfunktion ist.

**Beispiel:** $E_4(z) = 1 + 240(q + 9q^2 + 28q^3 + 73q^4 + \cdots)$

### Die Diskriminante $\Delta$

Die bekannteste Spitzenform ist die **Ramanujan-Diskriminante**:

$$
\Delta(z) = q \prod_{n=1}^{\infty} (1 - q^n)^{24} = \sum_{n=1}^{\infty} \tau(n) q^n
$$

Gewicht $12$, und (bis auf Skalierung) die einzige Spitzenform vom Gewicht $12$ für $\text{SL}_2(\mathbb{Z})$.

Die Koeffizienten $\tau(n)$ sind die **Ramanujan-$\tau$-Funktion**:

$$
\tau(1) = 1, \quad \tau(2) = -24, \quad \tau(3) = 252, \quad \tau(4) = -1472, \quad \ldots
$$

Ramanujan vermutete 1916, dass $|\tau(p)| \leq 2p^{11/2}$ für alle Primzahlen $p$ gilt. Der Beweis gelang erst 1974 durch Deligne (als Konsequenz der Weil-Vermutungen).

> „The Ramanujan $\tau$-function is perhaps the most important single example in the theory of modular forms."
> — Jean-Pierre Serre, *A Course in Arithmetic* (1973), S. 98

### Die $j$-Invariante

Die $j$-Invariante $j(z) = E_4(z)^3 / \Delta(z)$ ist keine Modulform (Gewicht $0$ und Pol bei $i\infty$), aber eine **modulare Funktion**. Sie klassifiziert elliptische Kurven: Zwei Kurven sind genau dann isomorph (über $\overline{K}$), wenn sie dieselbe $j$-Invariante haben.

## 5. Hecke-Operatoren

Die Räume der Modulformen tragen zusätzliche Symmetrien – die **Hecke-Operatoren** $T_n$. Für eine Modulform $f(z) = \sum a_m q^m$ und eine Primzahl $p$:

$$
(T_p f)(z) = \sum_{m=0}^{\infty} (a_{mp} + p^{k-1} a_{m/p}) \, q^m
$$

(wobei $a_{m/p} = 0$ wenn $p \nmid m$).

**Eigenformen.** Eine Modulform heißt **Hecke-Eigenform**, wenn sie Eigenvektor aller $T_n$ ist:

$$
T_n f = \lambda_n f \quad \text{für alle } n
$$

Für normierte Hecke-Eigenformen ($a_1 = 1$) gilt: Die Eigenwerte *sind* die Fourier-Koeffizienten: $\lambda_n = a_n$.

!!! tip "Multiplikativität"
    Die Fourier-Koeffizienten einer Hecke-Eigenform sind **multiplikativ**: $a_{mn} = a_m a_n$ für $\gcd(m, n) = 1$. Außerdem gilt $a_{p^{r+1}} = a_p a_{p^r} - p^{k-1} a_{p^{r-1}}$. Die $a_p$ (für Primzahlen $p$) bestimmen damit die gesamte Fourier-Entwicklung.

## 6. $L$-Reihen von Modulformen

Jede Spitzenform $f(z) = \sum_{n=1}^{\infty} a_n q^n$ definiert eine **$L$-Reihe**:

$$
L(f, s) = \sum_{n=1}^{\infty} a_n n^{-s}
$$

Für Hecke-Eigenformen hat diese $L$-Reihe ein Euler-Produkt:

$$
L(f, s) = \prod_p \frac{1}{1 - a_p p^{-s} + p^{k-1-2s}}
$$

Die $L$-Reihe konvergiert für $\text{Re}(s) > (k+1)/2$ und lässt sich analytisch auf ganz $\mathbb{C}$ fortsetzen. Sie erfüllt eine **Funktionalgleichung**, die $L(f, s)$ mit $L(f, k - s)$ verbindet.

### Vergleich mit elliptischen Kurven

Für eine Hecke-Eigenform $f$ vom Gewicht $2$ und eine elliptische Kurve $E$:

$$
L(f, s) = \prod_p \frac{1}{1 - a_p(f) p^{-s} + p^{1-2s}}
$$

$$
L(E, s) = \prod_p \frac{1}{1 - a_p(E) p^{-s} + p^{1-2s}}
$$

Die Strukturen sind **identisch**. Die Taniyama-Shimura-Vermutung besagt: Zu jeder elliptischen Kurve $E$ gibt es eine Hecke-Eigenform $f$ vom Gewicht $2$ mit $a_p(E) = a_p(f)$ für alle (bis auf endlich viele) Primzahlen $p$.

## 7. Kongruenzuntergruppen

Für Wiles' Beweis reichen Modulformen für $\text{SL}_2(\mathbb{Z})$ nicht aus – nötig sind Modulformen für **Kongruenzuntergruppen**. Die wichtigste:

$$
\Gamma_0(N) = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \text{SL}_2(\mathbb{Z}) \mid N \mid c \right\}
$$

Das **Niveau** $N$ bestimmt den Grad der Symmetrie – geringere Symmetrie (größeres $N$) erlaubt mehr Modulformen.

Eine elliptische Kurve $E$ mit **Führer** $N_E$ (ein Maß für die schlechte Reduktion) entspricht einer Hecke-Eigenform vom Gewicht $2$ und Niveau $N_E$.

## 8. Die Brücke zu elliptischen Kurven

Die Verbindung zwischen Modulformen und elliptischen Kurven ist einer der tiefsten Zusammenhänge der Mathematik:

| Elliptische Kurve $E$ | Modulform $f$ |
|------------------------|---------------|
| Koeffizienten $a, b$ in $y^2 = x^3 + ax + b$ | Fourier-Koeffizienten $a_n$ |
| $a_p(E) = p + 1 - \#E(\mathbb{F}_p)$ | $a_p(f)$ = Hecke-Eigenwert |
| $L(E, s)$ | $L(f, s)$ |
| Führer $N_E$ | Niveau $N$ |
| Galois-Darstellung $\rho_{E,\ell}$ | Galois-Darstellung $\rho_{f,\ell}$ |

**Satz (Wiles 1995, Breuil-Conrad-Diamond-Taylor 2001).** Jede elliptische Kurve über $\mathbb{Q}$ ist modular: Es gibt eine Hecke-Eigenform $f$ vom Gewicht $2$ mit $L(E, s) = L(f, s)$.

Wiles bewies 1995 den Fall semistabiler Kurven – ausreichend für FLT. Die vollständige Vermutung wurde 2001 von Breuil, Conrad, Diamond und Taylor bewiesen.

### Die Implikation für FLT

Modularität impliziert Fermats letzten Satz durch Widerspruch:

1. **Annahme:** Es gibt eine Lösung $a^p + b^p = c^p$.
2. **Frey:** Konstruktion der elliptischen Kurve $E: y^2 = x(x - a^p)(x + b^p)$.
3. **Ribet:** Diese Frey-Kurve kann **nicht** modular sein (ihr Führer wäre „zu klein").
4. **Wiles:** Aber jede semistabile elliptische Kurve **ist** modular.
5. **Widerspruch:** Die Frey-Kurve existiert nicht → keine Lösung → FLT ist wahr.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 7
- **Fred Diamond, Jerry Shurman**: *A First Course in Modular Forms*, Springer (2005)
- **Jean-Pierre Serre**: *A Course in Arithmetic*, Springer (1973), Kapitel VII
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1
