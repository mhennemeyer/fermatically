---
title: "Was ist Fermats letzter Satz?"
slug: elementare-zahlentheorie/01-was-ist-flt
series: elementare-zahlentheorie
part: 1
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - fermat
  - zahlentheorie
  - geschichte
requires: []
---

# Was ist Fermats letzter Satz?

!!! abstract "Zusammenfassung"
    Fermats letzter Satz – eine Vermutung aus dem Jahr 1637, die 358 Jahre
    unbewiesen blieb. Von der Randnotiz bis zu Wiles' Beweis 1995.

## Voraussetzungen

Keine – dieser Artikel bildet den Einstieg in die Serie.

---

## 1. Fermats Randnotiz (1637)

Im Jahr 1637 notierte Pierre de Fermat am Rand seines Exemplars der *Arithmetica* von Diophant:

> *„Cubum autem in duos cubos, aut quadratoquadratum in duos quadratoquadratos, et generaliter nullam in infinitum ultra quadratum potestatem in duos eiusdem nominis fas est dividere. Cuius rei demonstrationem mirabilem sane detexi. Hanc marginis exiguitas non caperet."*

Auf Deutsch:

> *„Es ist unmöglich, einen Kubus in zwei Kuben zu zerlegen, oder eine vierte Potenz in zwei vierte Potenzen, oder allgemein irgendeine Potenz höher als die zweite in zwei Potenzen derselben Art. Ich habe hierfür einen wahrhaft wunderbaren Beweis entdeckt, den dieser Rand nicht fassen kann."*

Die Notiz wurde erst nach Fermats Tod (1665) von seinem Sohn Clément-Samuel veröffentlicht. Sie begründete eines der bekanntesten offenen Probleme der Mathematik.

Fermat war kein Berufsmathematiker, sondern Jurist am Parlament von Toulouse. Dennoch zählen seine Beiträge zur Zahlentheorie zu den bedeutendsten des 17. Jahrhunderts. Viele seiner Behauptungen stellte er ohne Beweis auf – nahezu alle erwiesen sich als korrekt. Nur diese eine, die bekannteste, widerstand jedem Beweisversuch über dreieinhalb Jahrhunderte.

> „Fermat's Last Theorem has always been the Holy Grail of mathematics."
> — Simon Singh, *Fermat's Last Theorem* (1997), Vorwort

## 2. Die Aussage formal

Die Behauptung lässt sich präzise formulieren:

$$
x^n + y^n = z^n \quad \text{hat für } n \geq 3 \text{ keine Lösung in } x, y, z \in \mathbb{Z}^+
$$

Es gibt keine drei positiven ganzen Zahlen $x$, $y$ und $z$, die diese Gleichung für einen ganzzahligen Exponenten $n \geq 3$ erfüllen.

Für $n = 2$ existieren dagegen unendlich viele Lösungen – die **pythagoreischen Tripel**:

$$
3^2 + 4^2 = 5^2, \quad 5^2 + 12^2 = 13^2, \quad 8^2 + 15^2 = 17^2, \quad \ldots
$$

Der Satz von Pythagoras garantiert unendlich viele solcher Tripel, und sie lassen sich vollständig parametrisieren. Beim Übergang von Exponent $2$ zu $3$ verschwinden sämtliche Lösungen.

## 3. Die Schwierigkeit des Problems

Die Behauptung wirkt auf den ersten Blick einfach. Mehrere strukturelle Gründe machen den Beweis jedoch außerordentlich schwierig.

**Nichtexistenz-Beweis.** Es ist zu zeigen, dass unter den unendlich vielen Kombinationen von $x$, $y$, $z$ und $n$ keine einzige die Gleichung erfüllt. Ein einziges Gegenbeispiel hätte den Satz widerlegt – doch keines wurde je gefunden.

**Computersuchen.** Systematische Suchen im 20. Jahrhundert verifizierten den Satz bis in den Billionenbereich. Das liefert ein starkes Indiz, aber keinen Beweis. In der Mathematik existieren Vermutungen, die erst bei extrem großen Zahlen scheitern.

**Fehlende geometrische Struktur.** Für $n = 2$ hat die Gleichung eine reiche geometrische Interpretation: Jede Lösung entspricht einem rechtwinkligen Dreieck mit ganzzahligen Seiten. Für $n \geq 3$ fehlt eine vergleichbare Deutung – und damit fehlen die Werkzeuge.

**Fermats „wunderbarer Beweis".** Die Konsensposition unter Mathematikhistorikern: Fermat besaß keinen korrekten Beweis für den allgemeinen Fall. Der tatsächliche Beweis von Wiles nutzt Konzepte – elliptische Kurven, Modulformen, Galois-Darstellungen –, die erst im 19. und 20. Jahrhundert entwickelt wurden.

> „It is now clear that Fermat did not have a proof of his 'Last Theorem'. The techniques available in the seventeenth century are simply insufficient."
> — Nigel Boston, *The Proof of Fermat's Last Theorem* (2003), S. 1

## 4. Die Geschichte der Teilbeweise

Die Geschichte von Fermats letztem Satz ist zugleich eine Geschichte der Entwicklung der Mathematik. Jeder Teilbeweis erforderte neue Methoden und trieb ganze Forschungsgebiete voran.

### Fermat: $n = 4$ (ca. 1640)

Fermat lieferte den einzigen Fallbeweis, der von ihm überliefert ist. Die Methode: **unendlicher Abstieg** (*descente infinie*). Angenommen, es existiert eine Lösung. Dann lässt sich daraus eine kleinere Lösung konstruieren, und daraus eine noch kleinere – ad infinitum. Da positive ganze Zahlen nicht beliebig klein werden können, führt dies zum Widerspruch. Details in [Artikel 02](02-beweis-n4.md).

### Euler: $n = 3$ (1770)

Euler erweiterte die Abstiegsmethode auf den Fall $n = 3$. Dafür verließ er die gewöhnlichen ganzen Zahlen $\mathbb{Z}$ und rechnete mit den **Eisenstein-Zahlen** $\mathbb{Z}[\omega]$, wobei $\omega = e^{2\pi i/3}$ eine primitive dritte Einheitswurzel ist. In diesem erweiterten Zahlenbereich ließ sich die Gleichung faktorisieren und der Abstieg durchführen. Eulers Beweis enthielt eine Lücke: Er setzte implizit voraus, dass in $\mathbb{Z}[\omega]$ die eindeutige Primfaktorzerlegung gilt – was zutrifft, aber eines separaten Beweises bedarf. Der vollständige Beweis ist Thema von [Artikel 04](04-beweis-n3.md).

### Sophie Germain: Eine allgemeine Strategie (1823)

Sophie Germain entwickelte einen Ansatz, der erstmals für unendlich viele Exponenten gleichzeitig galt. Ihr Resultat: Wenn $p$ eine ungerade Primzahl ist und $2p + 1$ ebenfalls prim (eine **Germain-Primzahl**), dann hat $x^p + y^p = z^p$ keine Lösung, bei der $p$ keinen der Werte $x$, $y$, $z$ teilt (**Fall 1** von FLT).

### Kummer: Reguläre Primzahlen (1847–1857)

Kummer entwickelte die **Idealtheorie** – ein Konzept, das die fehlende eindeutige Faktorisierung in allgemeinen Zahlringen kompensiert. Er bewies FLT für alle **regulären Primzahlen**: Primzahlen $p$, die nicht die Klassenzahl des $p$-ten Kreisteilungskörpers teilen. Bis $p = 100$ sind alle Primzahlen außer $37$, $59$ und $67$ regulär. Für irreguläre Primzahlen versagt die Methode.

> „Kummer's introduction of ideal numbers [...] was one of the most important advances in number theory in the nineteenth century."
> — Harold M. Edwards, *Fermat's Last Theorem: A Genetic Introduction to Algebraic Number Theory* (1977), S. 76

### 20. Jahrhundert: Computerergebnisse

Mit zunehmender Rechenleistung wurde FLT für immer größere Exponenten verifiziert. 1993, kurz vor Wiles' Durchbruch, war der Satz für alle $n \leq 4{,}000{,}000$ bewiesen. Diese Ergebnisse blieben Einzelfallprüfungen – sie konnten den allgemeinen Fall nicht abdecken.

## 5. Fehlgeschlagene Beweisversuche

Hunderte fehlerhafte Beweise wurden eingereicht – von Amateuren und Fachleuten gleichermaßen.

Ein typischer Fehler: Die Gleichung $x^p + y^p = z^p$ wird direkt im Zahlring $\mathbb{Z}[\zeta_p]$ faktorisiert (mit $\zeta_p = e^{2\pi i/p}$), und die Teilerfremdhheit der Faktoren wird stillschweigend vorausgesetzt. Für $p = 3$ funktioniert dies (weil $\mathbb{Z}[\omega]$ ein Hauptidealring ist), für allgemeines $p$ ist die eindeutige Faktorisierung nicht gegeben. Gabriel Lamé verkündete 1847 einen vermeintlichen Beweis, der genau an dieser Stelle scheiterte – Kummer wies den Fehler noch am selben Tag nach.

Diese Fehlschläge trieben die Entwicklung der algebraischen Zahlentheorie, der Idealtheorie und der modernen algebraischen Geometrie voran.

## 6. Der Wolfskehl-Preis

Im Jahr 1908 stiftete der Darmstädter Industrielle **Paul Wolfskehl** einen Preis von 100.000 Goldmark für den Beweis von Fermats letztem Satz.

Der Preis löste eine Flut von Einsendungen aus. Die Universität Göttingen, die den Preis verwaltete, erhielt tausende vermeintliche Beweise. Edmund Landau soll Formularkarten gedruckt haben:

> *„Sehr geehrter Herr/Frau ..., Ihr vermeintlicher Beweis von Fermats letztem Satz enthält einen Fehler auf Seite ..., Zeile ..."*

Nach zwei Weltkriegen und Inflation war der Preis nur noch einen Bruchteil seines ursprünglichen Wertes wert. Andrew Wiles erhielt ihn 1997 – umgerechnet etwa 50.000 DM.

## 7. Die moderne Wende

Der Durchbruch kam nicht aus der klassischen Zahlentheorie, sondern aus einer Verbindung zwischen zwei scheinbar getrennten Gebieten.

### Die Taniyama-Shimura-Vermutung (1955)

Yutaka Taniyama und Goro Shimura formulierten die Vermutung, dass jede **elliptische Kurve** über $\mathbb{Q}$ **modular** ist – also durch eine **Modulform** beschrieben werden kann. Ein Zusammenhang zu FLT war zu diesem Zeitpunkt nicht erkennbar.

### Die Frey-Kurve und Ribets Theorem (1985–1986)

Gerhard Frey beobachtete 1985: Wenn FLT falsch wäre – wenn also eine Lösung $a^p + b^p = c^p$ existierte –, dann definiert

$$
y^2 = x(x - a^p)(x + b^p)
$$

eine elliptische Kurve mit Eigenschaften, die Modularität ausschließen. Kenneth Ribet bewies 1986, dass diese Beobachtung korrekt ist: Die Frey-Kurve ist nicht modular. Damit stand die Implikation:

$$
\text{Taniyama-Shimura} \implies \text{Fermats letzter Satz}
$$

### Wiles' Beweis (1993–1995)

Andrew Wiles arbeitete ab 1986 an einem Beweis der Taniyama-Shimura-Vermutung für die Klasse der **semistabilen** elliptischen Kurven – ausreichend für FLT.

Im Juni 1993 stellte Wiles den Beweis in Cambridge vor. Bei der Begutachtung zeigte sich eine Lücke. Im September 1994 fand Wiles zusammen mit Richard Taylor die Lösung: den **Taylor-Wiles-Trick**, eine patching-Methode für Galois-Deformationen.

Am 25. Oktober 1995 erschien der korrigierte Beweis in den *Annals of Mathematics*. Fermats letzter Satz war bewiesen – 358 Jahre nach der Randnotiz.

> „The proof represents the culmination of a remarkable era in the history of the problem, beginning with the pioneering work of Frey, Serre, and Ribet."
> — Andrew Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), S. 443

## 8. Ausblick

Dieser Artikel hat den historischen und mathematischen Rahmen abgesteckt. Die folgenden Artikel behandeln die technischen Details:

| Artikel | Thema |
|---------|-------|
| [02 – Der Beweis für $n = 4$](02-beweis-n4.md) | Fermats Abstiegsmethode |
| [03 – Primzahlen und warum sie reichen](03-primzahlen-reduktion.md) | Reduktion auf Primzahl-Exponenten |
| [04 – Der Beweis für $n = 3$](04-beweis-n3.md) | Eulers Beweis und algebraische Zahlentheorie |

Es folgen die **Werkzeug-Artikel** (Gruppen, Ringe, Galois-Theorie, elliptische Kurven, Modulformen) und schließlich die **Beweis-Artikel**, die Wiles' Argument Schritt für Schritt darstellen.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 1
- **Harold M. Edwards**: *Fermat's Last Theorem: A Genetic Introduction to Algebraic Number Theory*, Springer (1977)
- **Simon Singh**: *Fermat's Last Theorem*, Fourth Estate (1997)
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), 443–551
