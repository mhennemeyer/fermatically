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
    Die Geschichte einer Vermutung, die 358 Jahre lang unbewiesen blieb –
    von Fermats Randnotiz bis zu Andrew Wiles' Beweis im Jahr 1995.

## Voraussetzungen

Keine – dieser Artikel ist der Einstieg in die Serie.

---

## 1. Fermats Randnotiz (1637)

Im Jahr 1637 schrieb Pierre de Fermat an den Rand seines Exemplars der *Arithmetica* von Diophant einen Satz, der die Mathematik über drei Jahrhunderte beschäftigen sollte:

> *„Cubum autem in duos cubos, aut quadratoquadratum in duos quadratoquadratos, et generaliter nullam in infinitum ultra quadratum potestatem in duos eiusdem nominis fas est dividere. Cuius rei demonstrationem mirabilem sane detexi. Hanc marginis exiguitas non caperet."*

Auf Deutsch:

> *„Es ist unmöglich, einen Kubus in zwei Kuben zu zerlegen, oder eine vierte Potenz in zwei vierte Potenzen, oder allgemein irgendeine Potenz höher als die zweite in zwei Potenzen derselben Art. Ich habe hierfür einen wahrhaft wunderbaren Beweis entdeckt, den dieser Rand nicht fassen kann."*

Diese Randnotiz wurde erst nach Fermats Tod (1665) von seinem Sohn Clément-Samuel veröffentlicht. Sie begründete eines der berühmtesten ungelösten Probleme der Mathematik – und eine 358 Jahre währende Jagd nach dem Beweis.

Fermat selbst war kein Berufsmathematiker. Er war Jurist am Parlament von Toulouse und betrieb Mathematik als Leidenschaft. Doch seine Beiträge zur Zahlentheorie waren so tiefgreifend, dass er oft als „Fürst der Amateure" bezeichnet wird. Viele seiner Behauptungen stellte er ohne Beweis auf – fast alle erwiesen sich als richtig. Nur diese eine, die berühmteste von allen, widerstand jedem Beweisversuch.

## 2. Die Aussage formal

Was Fermat behauptete, lässt sich präzise so formulieren:

$$
x^n + y^n = z^n \quad \text{hat für } n \geq 3 \text{ keine Lösung in } x, y, z \in \mathbb{Z}^+
$$

Das heißt: Es gibt keine drei positiven ganzen Zahlen $x$, $y$ und $z$, die diese Gleichung für einen ganzzahligen Exponenten $n \geq 3$ erfüllen.

Für $n = 2$ kennen wir dagegen unendlich viele Lösungen – die **pythagoreischen Tripel**:

$$
3^2 + 4^2 = 5^2, \quad 5^2 + 12^2 = 13^2, \quad 8^2 + 15^2 = 17^2, \quad \ldots
$$

Der Satz von Pythagoras garantiert sogar, dass es unendlich viele solcher Tripel gibt, und sie lassen sich vollständig parametrisieren. Doch sobald der Exponent von $2$ auf $3$ steigt, scheinen alle Lösungen zu verschwinden – als hätte man eine unsichtbare Barriere überschritten.

## 3. Warum ist das schwer?

Auf den ersten Blick wirkt die Behauptung harmlos. Man könnte meinen, ein cleverer algebraischer Trick genüge. Doch der Teufel steckt im Detail.

**Das Problem der Nichtexistenz.** Einen Beweis dafür zu finden, dass *etwas existiert*, ist oft einfacher als zu zeigen, dass *etwas nicht existiert*. Man müsste zeigen, dass unter den unendlich vielen Kombinationen von $x$, $y$, $z$ und $n$ keine einzige die Gleichung erfüllt. Ein einziges Gegenbeispiel hätte genügt, um den Satz zu widerlegen – aber niemand fand eines.

**Computersuchen.** Im 20. Jahrhundert wurden systematische Suchen durchgeführt. Bis in die Billionen – keine Lösung. Das ist ein starkes Indiz, aber kein Beweis. In der Mathematik gibt es Vermutungen, die erst bei astronomisch großen Zahlen scheitern.

**Die Asymmetrie zum Satz von Pythagoras.** Für $n = 2$ hat die Gleichung eine reiche geometrische Struktur: Jede Lösung entspricht einem rechtwinkligen Dreieck mit ganzzahligen Seiten. Für $n \geq 3$ fehlt eine vergleichbare geometrische Deutung – und damit fehlen die Werkzeuge.

**Fermats „wunderbarer Beweis".** Fast alle Mathematikhistoriker sind sich einig: Fermat konnte keinen korrekten Beweis besessen haben. Der tatsächliche Beweis von Wiles nutzt Konzepte – elliptische Kurven, Modulformen, Galois-Darstellungen –, die erst im 19. und 20. Jahrhundert entwickelt wurden. Wahrscheinlich hatte Fermat eine Idee, die für $n = 4$ funktionierte (diesen Beweis kennen wir), aber für allgemeine $n$ fehlerhaft war.

## 4. Die Geschichte der Teilbeweise

Die Geschichte von Fermats letztem Satz ist auch eine Geschichte der Entwicklung der Mathematik. Jeder Teilbeweis erforderte neue Methoden und trieb ganze Forschungsgebiete voran.

### Fermat selbst: $n = 4$ (ca. 1640)

Fermat bewies den einzigen Fall, für den wir einen vollständigen Beweis von ihm kennen. Er nutzte die Methode des **unendlichen Abstiegs** (*descente infinie*): Angenommen, es gäbe eine Lösung. Dann könnte man daraus eine *kleinere* Lösung konstruieren, und daraus eine noch kleinere – ad infinitum. Da positive ganze Zahlen aber nicht unendlich klein werden können, ist die Annahme falsch. Diesen Beweis behandeln wir im [nächsten Artikel](../02-beweis-n4/article_de.md) im Detail.

### Leonhard Euler: $n = 3$ (1770)

Euler erweiterte Fermats Methode auf den Fall $n = 3$. Doch dafür musste er einen entscheidenden Schritt tun: Er verließ die gewöhnlichen ganzen Zahlen $\mathbb{Z}$ und rechnete stattdessen mit den **Eisenstein-Zahlen** $\mathbb{Z}[\omega]$, wobei $\omega = e^{2\pi i/3}$ eine primitive dritte Einheitswurzel ist. In diesem erweiterten Zahlenbereich konnte er die Gleichung faktorisieren und den Abstieg durchführen. Eulers Beweis enthielt allerdings eine Lücke: Er setzte implizit voraus, dass in $\mathbb{Z}[\omega]$ die eindeutige Primfaktorzerlegung gilt – was zufällig stimmt, aber bewiesen werden muss. Den vollständigen Beweis besprechen wir in [Artikel 4](../04-beweis-n3/article_de.md).

### Sophie Germain: Eine neue Strategie (1823)

Sophie Germain – eine der ersten bedeutenden Mathematikerinnen – entwickelte einen allgemeineren Ansatz. Sie bewies: Wenn $p$ eine ungerade Primzahl ist und $2p + 1$ ebenfalls prim (eine sogenannte **Germain-Primzahl**), dann hat $x^p + y^p = z^p$ keine Lösung, bei der $p$ keinen der Werte $x$, $y$, $z$ teilt (**Fall 1** von FLT). Dies war der erste Teilerfolg, der für unendlich viele Exponenten gleichzeitig galt.

### Ernst Kummer: Reguläre Primzahlen (1847–1857)

Kummer revolutionierte die algebraische Zahlentheorie, indem er die **Idealtheorie** entwickelte – ein Konzept, das die fehlende eindeutige Faktorisierung in allgemeinen Zahlringen kompensiert. Er bewies FLT für alle **regulären Primzahlen** – das sind Primzahlen $p$, die nicht die Klassenzahl des $p$-ten Kreisteilungskörpers teilen. Bis $p = 100$ sind alle Primzahlen außer $37$, $59$ und $67$ regulär. Doch es gibt unendlich viele irreguläre Primzahlen, und Kummers Methode versagt für sie.

### Das 20. Jahrhundert: Computerbeweise und Schranken

Mit dem Aufkommen von Computern wurde FLT für immer größere Exponenten verifiziert. 1993, kurz vor Wiles' Durchbruch, war der Satz für alle $n \leq 4{,}000{,}000$ bewiesen. Doch diese Ergebnisse blieben Stückwerk – sie konnten den allgemeinen Fall nicht abdecken.

## 5. Fehlgeschlagene Versuche und Irrwege

Die Geschichte von FLT ist auch eine Geschichte der Irrtümer. Hunderte von fehlerhaften Beweisen wurden eingereicht – von Amateuren und Profis gleichermaßen.

Ein typischer Fehler: Man versucht, die Gleichung $x^p + y^p = z^p$ direkt in einem Zahlring $\mathbb{Z}[\zeta_p]$ zu faktorisieren (mit $\zeta_p = e^{2\pi i/p}$) und nimmt an, dass die Faktoren teilerfremd sind. Für $p = 3$ funktioniert das (weil $\mathbb{Z}[\omega]$ ein Hauptidealring ist), aber für allgemeines $p$ ist die eindeutige Faktorisierung nicht gegeben. Gabriel Lamé verkündete 1847 einen vermeintlichen Beweis, der genau an dieser Stelle scheiterte – Kummer wies den Fehler noch am selben Tag nach.

Diese Fehlschläge waren nicht nutzlos: Sie trieben die Entwicklung der algebraischen Zahlentheorie, der Idealtheorie und schließlich der modernen algebraischen Geometrie voran.

## 6. Der Wolfskehl-Preis

Im Jahr 1908 stiftete der Darmstädter Industrielle **Paul Wolfskehl** einen Preis von 100.000 Goldmark für den Beweis von Fermats letztem Satz. Der Legende nach hatte Wolfskehl, der an einer unheilbaren Krankheit litt, seinen Selbstmord für Mitternacht geplant. Beim Warten vertiefte er sich in Kummers Arbeit, vergaß die Zeit – und fand neuen Lebensmut. Zum Dank stiftete er den Preis.

Der Wolfskehl-Preis löste eine Flut von Einsendungen aus. Die Universität Göttingen, die den Preis verwaltete, erhielt tausende vermeintliche Beweise – die meisten mit offensichtlichen Fehlern. Edmund Landau soll Formularkarten gedruckt haben:

> *„Sehr geehrter Herr/Frau ..., Ihr vermeintlicher Beweis von Fermats letztem Satz enthält einen Fehler auf Seite ..., Zeile ..."*

Nach zwei Weltkriegen und Inflation war der Preis nur noch einen Bruchteil seines ursprünglichen Wertes wert. Als Andrew Wiles ihn 1997 schließlich erhielt, betrug er umgerechnet etwa 50.000 DM – aber der symbolische Wert war unbezahlbar.

## 7. Die moderne Wende

Der Durchbruch kam von einer völlig unerwarteten Seite. Nicht die Zahlentheorie selbst löste das Problem, sondern eine Brücke zwischen zwei scheinbar unverbundenen Gebieten der Mathematik.

### Die Taniyama-Shimura-Vermutung (1955)

Die japanischen Mathematiker **Yutaka Taniyama** und **Goro Shimura** stellten eine kühne Vermutung auf: Jede **elliptische Kurve** über $\mathbb{Q}$ ist **modular** – das heißt, sie lässt sich durch eine **Modulform** beschreiben. Das klingt zunächst wie ein rein technisches Resultat ohne Bezug zu FLT. Doch drei Jahrzehnte später wurde klar, dass diese Verbindung der Schlüssel war.

### Die Frey-Kurve und Ribets Beweis (1985–1986)

Der deutsche Mathematiker **Gerhard Frey** hatte 1985 eine spektakuläre Idee: Wenn FLT *falsch* wäre – wenn es also eine Lösung $a^p + b^p = c^p$ gäbe –, dann könnte man daraus eine elliptische Kurve konstruieren:

$$
y^2 = x(x - a^p)(x + b^p)
$$

Diese „**Frey-Kurve**" hätte so exotische Eigenschaften, dass sie unmöglich modular sein könnte. Wenn also die Taniyama-Shimura-Vermutung stimmt (alle elliptischen Kurven sind modular), dann kann die Frey-Kurve nicht existieren – und FLT muss wahr sein.

**Kenneth Ribet** bewies 1986, dass Freys Intuition korrekt war: Die Frey-Kurve ist tatsächlich nicht modular. Damit war die Implikation gesichert:

$$
\text{Taniyama-Shimura} \implies \text{Fermats letzter Satz}
$$

### Andrew Wiles (1993–1995)

Andrew Wiles, ein britischer Mathematiker in Princeton, hatte seit seiner Kindheit davon geträumt, FLT zu beweisen. Nach Ribets Ergebnis arbeitete er sieben Jahre lang im Geheimen an einem Beweis der Taniyama-Shimura-Vermutung – zumindest für die Klasse der **semistabilen** elliptischen Kurven, die für FLT ausreicht.

Im Juni 1993 verkündete Wiles seinen Beweis in einer dramatischen Vorlesungsreihe in Cambridge. Doch bei der Begutachtung fand sich eine Lücke. Monatelang versuchte Wiles, sie zu schließen – fast gab er auf. Dann, im September 1994, fand er zusammen mit seinem ehemaligen Studenten **Richard Taylor** die Lösung: den berühmten **Taylor-Wiles-Trick**.

Am 25. Oktober 1995 wurde der korrigierte Beweis in den *Annals of Mathematics* veröffentlicht. Fermats letzter Satz war bewiesen – nach 358 Jahren.

## 8. Ausblick: Was kommt in den nächsten Artikeln?

Dieser erste Artikel hat den großen Bogen gespannt. In den folgenden Artikeln tauchen wir in die Details ein:

| Artikel | Thema |
|---------|-------|
| [02 – Der Beweis für $n = 4$](../02-beweis-n4/article_de.md) | Fermats eigener Beweis mit der Methode des unendlichen Abstiegs |
| [03 – Primzahlen und warum sie reichen](../03-primzahlen-reduktion/article_de.md) | Warum es genügt, FLT für Primzahl-Exponenten zu beweisen |
| [04 – Der Beweis für $n = 3$](../04-beweis-n3/article_de.md) | Eulers Beweis und der Einstieg in die algebraische Zahlentheorie |

Nach den Grundlagen folgen die **Werkzeug-Topics** – eigenständige Artikel zu Gruppen, Ringen, Galois-Theorie, elliptischen Kurven und Modulformen. Und schließlich die **Beweis-Topics**, die Schritt für Schritt durch Wiles' Beweis führen.

Das Ziel: Am Ende soll jeder Leser – ob Student, Mathematik-Enthusiast oder Fachkollege – verstehen, *warum* Wiles' Beweis funktioniert und welche Ideen ihn tragen.

---

## Weiterführende Quellen

- **Simon Singh**: *Fermats letzter Satz* – Die abenteuerliche Geschichte eines mathematischen Rätsels (populärwissenschaftlich, hervorragend erzählt)
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003) – Lehrbuch mit mathematischen Details
- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), 443–551
