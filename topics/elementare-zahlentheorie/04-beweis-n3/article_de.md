---
title: "Der Beweis für n=3"
slug: elementare-zahlentheorie/04-beweis-n3
series: elementare-zahlentheorie
part: 4
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - fermat
  - euler
  - gauss
  - algebraische-zahlen
requires: []
---

# Der Beweis für $n = 3$

!!! abstract "Zusammenfassung"
    Eulers Beweis von FLT für $n = 3$ – und die daraus resultierende Notwendigkeit,
    die gewöhnlichen ganzen Zahlen zu verlassen. Einstieg in die algebraische Zahlentheorie.

## Voraussetzungen

- [Was ist Fermats letzter Satz?](../01-was-ist-flt/article_de.md)
- [Der Beweis für $n = 4$](../02-beweis-n4/article_de.md)
- [Primzahlen und warum sie reichen](../03-primzahlen-reduktion/article_de.md)

---

## 1. Warum $n = 3$ schwieriger ist als $n = 4$

Im Beweis für $n = 4$ ließ sich die Gleichung $x^4 + y^4 = z^2$ vollständig in $\mathbb{Z}$ behandeln. Der Schlüssel war die Parametrisierung der pythagoreischen Tripel – eine Formel, die *alle* Lösungen von $x^2 + y^2 = z^2$ beschreibt.

Für $n = 3$ existiert kein Analogon. Die Gleichung $x^3 + y^3 = z^3$ lässt sich in $\mathbb{Z}$ nicht so faktorisieren, dass ein Abstieg möglich wird. Die Faktorisierung

$$
x^3 + y^3 = (x + y)(x^2 - xy + y^2)
$$

liefert zwei Faktoren, deren Teilerfremdheit schwer zu kontrollieren ist. Informationen über $\gcd(x + y, \, x^2 - xy + y^2)$ sind in $\mathbb{Z}$ nicht leicht zu gewinnen.

Eulers Lösung: Erweiterung des Zahlbereichs.

## 2. Die Eisenstein-Zahlen

Sei $\omega = e^{2\pi i/3} = \frac{-1 + \sqrt{-3}}{2}$ eine primitive dritte Einheitswurzel. Die **Eisenstein-Zahlen** sind der Ring:

$$
\mathbb{Z}[\omega] = \{ a + b\omega \mid a, b \in \mathbb{Z} \}
$$

Geometrisch bilden die Eisenstein-Zahlen ein regelmäßiges Dreiecksgitter in der komplexen Ebene. Jedes Element hat die Form $a + b\omega$ mit ganzzahligen Koordinaten.

### Grundlegende Eigenschaften

**Norm.** Für $\alpha = a + b\omega$ ist die Norm definiert als:

$$
N(\alpha) = \alpha \cdot \bar{\alpha} = a^2 - ab + b^2
$$

wobei $\bar{\alpha} = a + b\bar{\omega} = a + b\omega^2$ die konjugierte Zahl ist (denn $\omega^2 = \bar{\omega}$). Die Norm ist stets eine nichtnegative ganze Zahl und multiplikativ: $N(\alpha\beta) = N(\alpha) \cdot N(\beta)$.

**Einheiten.** Die Einheiten (invertierbaren Elemente) von $\mathbb{Z}[\omega]$ sind genau die Elemente mit Norm $1$:

$$
\mathbb{Z}[\omega]^\times = \{ \pm 1, \pm \omega, \pm \omega^2 \}
$$

Sechs Einheiten – im Vergleich zu den zwei Einheiten $\pm 1$ in $\mathbb{Z}$.

**Primelemente.** Ein Eisenstein-Element $\pi$ heißt *prim*, wenn es keine Einheit ist und $\pi \mid \alpha\beta$ impliziert $\pi \mid \alpha$ oder $\pi \mid \beta$. Die Primstruktur von $\mathbb{Z}[\omega]$ unterscheidet sich von der in $\mathbb{Z}$:

- Die Primzahl $3$ zerfällt besonders: $3 = -\omega^2 (1 - \omega)^2$, also ist $\lambda := 1 - \omega$ ein Primelement mit $N(\lambda) = 3$.
- Primzahlen $p \equiv 2 \pmod{3}$ bleiben prim in $\mathbb{Z}[\omega]$.
- Primzahlen $p \equiv 1 \pmod{3}$ zerfallen: $p = \pi \bar{\pi}$ für ein Primelement $\pi$.

### Der entscheidende Vorteil

In $\mathbb{Z}[\omega]$ lässt sich $x^3 + y^3$ *vollständig* faktorisieren:

$$
x^3 + y^3 = (x + y)(x + \omega y)(x + \omega^2 y)
$$

Drei lineare Faktoren statt zwei. Diese feinere Faktorisierung ermöglicht den Abstieg.

## 3. Eindeutige Faktorisierung

Der Beweis setzt voraus, dass $\mathbb{Z}[\omega]$ ein **Hauptidealring** (HIR) ist – dass also jedes Element eine im Wesentlichen eindeutige Zerlegung in Primelemente besitzt.

**Satz.** $\mathbb{Z}[\omega]$ ist ein euklidischer Ring (mit der Normfunktion als euklidischer Funktion) und daher insbesondere ein HIR.

**Beweisskizze.** Für $\alpha, \beta \in \mathbb{Z}[\omega]$ mit $\beta \neq 0$ wird $\alpha/\beta \in \mathbb{Q}(\omega)$ betrachtet. Dieses Element lässt sich durch ein Gitterelement $\gamma \in \mathbb{Z}[\omega]$ approximieren mit $N(\alpha/\beta - \gamma) < 1$ (das Dreiecksgitter ist dicht genug). Dann ist $\alpha = \beta\gamma + \rho$ mit $N(\rho) < N(\beta)$ – die Division mit Rest. $\square$

!!! warning "Nicht selbstverständlich"
    Für $p = 3$ ist $\mathbb{Z}[\omega]$ ein HIR – aber $\mathbb{Z}[\zeta_p]$ ist für allgemeines $p$ **kein** HIR. Bereits für $p = 23$ versagt die eindeutige Faktorisierung. An diesem Punkt scheiterte Lamé, und Kummer entwickelte die Idealtheorie.

## 4. Der Beweis: Schritt für Schritt

Zu zeigen: $x^3 + y^3 = z^3$ hat keine Lösung in positiven ganzen Zahlen.

Äquivalent (und technisch geschickter) die allgemeinere Aussage in $\mathbb{Z}[\omega]$:

$$
\alpha^3 + \beta^3 + \gamma^3 = 0 \quad \text{hat keine Lösung mit } \alpha, \beta, \gamma \in \mathbb{Z}[\omega] \setminus \{0\} \text{ und } \lambda \nmid \alpha\beta\gamma
$$

wobei $\lambda = 1 - \omega$ das Primelement über $3$ ist. (Die symmetrische Form $\alpha^3 + \beta^3 + \gamma^3 = 0$ ist äquivalent zu $x^3 + y^3 = z^3$ mit umgedrehtem Vorzeichen von $z$.)

Der Beweis erfolgt mittels unendlichem Abstieg in mehreren Stufen.

### Vorbereitung: Kubische Reste modulo $\lambda$

Da $N(\lambda) = 3$, ist $\mathbb{Z}[\omega]/(\lambda) \cong \mathbb{Z}/3\mathbb{Z} = \{0, 1, 2\}$. Jedes Element von $\mathbb{Z}[\omega]$, das nicht durch $\lambda$ teilbar ist, ist kongruent zu $\pm 1 \pmod{\lambda}$. Daraus folgt: Jede dritte Potenz eines solchen Elements ist ebenfalls kongruent zu $\pm 1 \pmod{\lambda}$.

Genauer gilt für jedes $\alpha$ mit $\lambda \nmid \alpha$:

$$
\alpha^3 \equiv \pm 1 \pmod{\lambda^4}
$$

Die Analogie zur Aussage „jedes Quadrat ist $\equiv 0$ oder $1 \pmod{4}$" in $\mathbb{Z}$ – aber eine Stufe komplizierter.

### Der Abstieg

**Annahme.** Sei $(\alpha, \beta, \gamma)$ eine Lösung von $\alpha^3 + \beta^3 + \gamma^3 = 0$ mit $\lambda \nmid \alpha\beta\gamma$ und mit *minimaler* $\lambda$-Bewertung in einem der Terme. Konkret: $\lambda \mid \gamma$ (nach Umordnung), mit $\gamma = \lambda^n \delta$, $\lambda \nmid \delta$ und minimalem $n \geq 1$.

Zu zeigen: Aus dieser Lösung lässt sich eine neue Lösung mit kleinerem $n$ konstruieren – Widerspruch.

**Schritt 1: Faktorisierung.** In $\mathbb{Z}[\omega]$:

$$
\alpha^3 + \beta^3 = -\gamma^3 = -\lambda^{3n} \delta^3
$$

$$
(\alpha + \beta)(\alpha + \omega\beta)(\alpha + \omega^2\beta) = -\lambda^{3n} \delta^3
$$

**Schritt 2: Teilerfremdheit der Faktoren.** Die drei Faktoren $\alpha + \beta$, $\alpha + \omega\beta$, $\alpha + \omega^2\beta$ lassen sich paarweise durch $\lambda$ trennen: Ihre paarweisen Differenzen sind $(1 - \omega)\beta = \lambda\beta$ und $(1 - \omega^2)\beta$, also ist $\lambda$ der einzige gemeinsame Faktor. Nach Analyse der $\lambda$-Bewertung: Genau einer der drei Faktoren ist durch $\lambda^{3n-2}$ teilbar, die anderen beiden nicht durch $\lambda$.

**Schritt 3: Kubische Struktur erzwingen.** Da $\mathbb{Z}[\omega]$ ein HIR ist und die drei Faktoren (bis auf $\lambda$-Anteile) teilerfremd sind, muss jeder Faktor (bis auf Einheiten und $\lambda$-Potenzen) ein Kubus sein. Es existieren $\alpha_1, \beta_1, \gamma_1 \in \mathbb{Z}[\omega]$ mit:

$$
\alpha + \beta = \varepsilon_1 \lambda^{3n-2} \gamma_1^3, \quad \alpha + \omega\beta = \varepsilon_2 \alpha_1^3, \quad \alpha + \omega^2\beta = \varepsilon_3 \beta_1^3
$$

wobei $\varepsilon_1, \varepsilon_2, \varepsilon_3$ Einheiten sind.

**Schritt 4: Neue Gleichung aufstellen.** Durch Kombination der drei Gleichungen ergibt sich eine Gleichung der Form

$$
\alpha_1^3 + \beta_1^3 + \varepsilon \lambda^{n'} \gamma_1^3 = 0
$$

wobei $n' < n$. Die Einheit $\varepsilon$ lässt sich durch Wahl geeigneter Assoziierter absorbieren.

**Schritt 5: Widerspruch.** Eine Lösung mit $\lambda$-Bewertung $n' < n$ ist konstruiert. Da $n$ minimal war, ergibt sich der Widerspruch. $\blacksquare$

## 5. Die Lücke in Eulers Original

Eulers Beweis, wie er 1770 in seiner *Algebra* erschien, enthielt eine subtile Lücke. Im entscheidenden Schritt des Abstiegs setzte er die **eindeutige Primfaktorzerlegung** in $\mathbb{Z}[\omega]$ voraus, ohne sie zu beweisen.

> „Euler's proof of Fermat's Last Theorem for cubes [...] is essentially correct, but it does assume, without proof, the unique factorization of the Eisenstein integers."
> — Harold M. Edwards, *Fermat's Last Theorem* (1977), S. 39

Die Voraussetzung ist korrekt: $\mathbb{Z}[\omega]$ ist tatsächlich ein HIR. Aber Euler bewies das nicht; er verwendete es als gegeben. Der rigorose Nachweis erfolgte später – unter anderem durch Gauß.

Die Lücke ist heilbar: Eulers Beweis wird vollständig korrekt, wenn die HIR-Eigenschaft von $\mathbb{Z}[\omega]$ vorangestellt wird. Aber die Lücke offenbart ein tiefes konzeptuelles Problem: Für allgemeines $p$ ist $\mathbb{Z}[\zeta_p]$ kein HIR, und Eulers Strategie versagt.

## 6. Wo die Methode an ihre Grenzen stößt

Für $p = 5$ gilt in $\mathbb{Z}[\zeta_5]$ noch die EPZ – der Beweis für $n = 5$ (Dirichlet/Legendre, 1825) nutzt dies, allerdings mit erheblich mehr Aufwand.

Für $p = 23$ ist die Situation grundlegend anders: $\mathbb{Z}[\zeta_{23}]$ hat Klassenzahl $h_{23} = 3 \neq 1$. Die EPZ versagt, und ein direkter Faktorisierungsansatz liefert falsche Ergebnisse. Hier setzte Kummers Idealtheorie an, vertieft im [Artikel über Ringe und Körper](../../ringe-und-koerper/01-ringe-koerper/article_de.md).

Die zentrale Erkenntnis: **Der Beweis für $n = 3$ funktioniert, weil die Eisenstein-Zahlen eindeutige Faktorisierung besitzen.** Für allgemeines $p$ ist diese Eigenschaft nicht gegeben – ein grundlegend anderer Ansatz wird nötig.

## 7. Von Euler zu Kummer – und weiter

Der Beweis für $n = 3$ markiert einen Wendepunkt in der Geschichte von FLT:

| Aspekt | $n = 4$ (Fermat) | $n = 3$ (Euler) |
|--------|-------------------|------------------|
| Zahlbereich | $\mathbb{Z}$ | $\mathbb{Z}[\omega]$ |
| Faktorisierung | pythagoreische Tripel | kubische Faktorisierung |
| Abstieg über | Größe von $z$ | $\lambda$-Bewertung |
| Neue Mathematik | Infinite Descent | Algebraische Zahlentheorie |

Von hier aus verzweigt sich der Weg:

1. **Grundlagen-Werkzeuge**: Gruppen, Ringe, Körper, Galois-Theorie – die Sprache der modernen Algebra.
2. **Spezialwerkzeuge**: Elliptische Kurven und Modulformen – die Objekte, die Wiles' Beweis verbindet.
3. **Der Beweis selbst**: Galois-Darstellungen, Deformationstheorie, der $R = T$-Satz.

Die folgenden Werkzeug-Artikel bauen diese Grundlagen auf.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 2
- **Harold M. Edwards**: *Fermat's Last Theorem: A Genetic Introduction to Algebraic Number Theory*, Springer (1977), Kapitel 3
- **Kenneth Ireland, Michael Rosen**: *A Classical Introduction to Modern Number Theory*, Springer (1990)
