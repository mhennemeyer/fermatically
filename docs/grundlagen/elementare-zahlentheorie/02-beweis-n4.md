---
title: "Der Beweis für n=4"
slug: elementare-zahlentheorie/02-beweis-n4
series: elementare-zahlentheorie
part: 2
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - fermat
  - infinite-descent
  - beweis
requires: []
---

# Der Beweis für $n = 4$

!!! abstract "Zusammenfassung"
    Fermats einziger überlieferter Fallbeweis von FLT. Die Methode des unendlichen
    Abstiegs zeigt: $x^4 + y^4 = z^2$ hat keine Lösung in positiven ganzen Zahlen.

## Voraussetzungen

- [Was ist Fermats letzter Satz?](01-was-ist-flt.md)

---

## 1. Die Methode des unendlichen Abstiegs

Der **unendliche Abstieg** (*descente infinie*) ist eine Beweistechnik, die Fermat selbst entwickelte. Die Grundidee:

**Angenommen**, eine Gleichung hätte eine Lösung in positiven ganzen Zahlen. Dann lässt sich aus dieser Lösung eine *kleinere* Lösung konstruieren – eine Lösung, bei der die beteiligten Zahlen echt kleiner sind. Aus der kleineren Lösung ergibt sich eine noch kleinere, und so weiter – *ad infinitum*.

Positive ganze Zahlen können jedoch nicht unendlich klein werden. Es gibt kein unendliches Absteigen in $\mathbb{Z}^+$. Die Annahme ist also falsch, und die Gleichung hat keine Lösung.

Formal nutzt der Abstieg das **Wohlordnungsprinzip**: Jede nichtleere Teilmenge von $\mathbb{N}$ hat ein kleinstes Element. Eine unendlich absteigende Folge positiver ganzer Zahlen kann es daher nicht geben.

> „I have discovered a truly marvellous demonstration [...] which this margin is too narrow to contain."
> — Pierre de Fermat, Randnotiz zur *Arithmetica* (ca. 1637)

!!! note "Abstieg vs. Widerspruch"
    Der unendliche Abstieg ist ein spezieller **Widerspruchsbeweis**: Die Annahme einer Lösung führt zu einer unmöglichen Konsequenz (einer unendlich absteigenden Folge). In moderner Formulierung äquivalent: Eine *minimale* Lösung wird betrachtet, und es wird gezeigt, dass eine noch kleinere existieren müsste – Widerspruch.

## 2. Pythagoreische Tripel

Für den Beweis des Falls $n = 4$ ist ein klassisches Ergebnis erforderlich: die vollständige Beschreibung aller Lösungen von $x^2 + y^2 = z^2$.

**Satz (Parametrisierung der pythagoreischen Tripel).** Alle *primitiven* pythagoreischen Tripel $(x, y, z)$ mit $\gcd(x, y) = 1$ und $x$ gerade haben die Form:

$$
x = 2st, \quad y = s^2 - t^2, \quad z = s^2 + t^2
$$

wobei $s > t > 0$, $\gcd(s, t) = 1$ und $s \not\equiv t \pmod{2}$ (also $s$ und $t$ verschiedener Parität).

**Beweisskizze.** Es gilt $x^2 = z^2 - y^2 = (z-y)(z+y)$. Da $(x, y, z)$ primitiv ist, sind $z - y$ und $z + y$ teilerfremd (bis auf den Faktor 2). Da $x$ gerade ist, sind $z$ und $y$ beide ungerade, also $z - y$ und $z + y$ beide gerade. Mit $z - y = 2u$ und $z + y = 2v$ folgt $x^2 = 4uv$ mit $\gcd(u, v) = 1$. Da das Produkt $uv$ ein Quadrat und die Faktoren teilerfremd sind, müssen $u$ und $v$ selbst Quadrate sein: $u = t^2$, $v = s^2$. Einsetzen liefert die Parametrisierung. $\square$

**Beispiele:**

| $s$ | $t$ | $x = 2st$ | $y = s^2 - t^2$ | $z = s^2 + t^2$ |
|-----|-----|-----------|------------------|------------------|
| 2   | 1   | 4         | 3                | 5                |
| 3   | 2   | 12        | 5                | 13               |
| 4   | 1   | 8         | 15               | 17               |
| 4   | 3   | 24        | 7                | 25               |

## 3. Von FLT zu einer stärkeren Aussage

Fermats Beweis für $n = 4$ zeigt nicht direkt, dass $x^4 + y^4 = z^4$ keine Lösung hat, sondern die **stärkere** Aussage:

!!! tip "Satz (Fermat)"
    Die Gleichung $x^4 + y^4 = z^2$ hat keine Lösung in positiven ganzen Zahlen.

Die Implikation: Da $z^4 = (z^2)^2$ ein spezielles Quadrat ist, folgt aus der Nichtexistenz von Lösungen für $z^2$ auf der rechten Seite erst recht die Nichtexistenz für $z^4$.

$$
x^4 + y^4 = z^4 \implies x^4 + y^4 = (z^2)^2
$$

Also: $x^4 + y^4 = z^2$ hat keine Lösung $\implies$ $x^4 + y^4 = z^4$ hat keine Lösung.

## 4. Der Beweis im Detail

Zu zeigen: $x^4 + y^4 = z^2$ hat keine Lösung in $x, y, z \in \mathbb{Z}^+$.

**Annahme zum Widerspruch.** Sei $(x, y, z)$ eine Lösung mit *minimalem* $z$. Ohne Einschränkung gelte $\gcd(x, y) = 1$ (andernfalls ergibt Herauskürzen des gemeinsamen Faktors eine kleinere Lösung).

**Schritt 1: Pythagoreische Tripel anwenden.**

Die Gleichung $x^4 + y^4 = z^2$ lässt sich als $(x^2)^2 + (y^2)^2 = z^2$ lesen – ein pythagoreisches Tripel. Da $\gcd(x, y) = 1$ ist das Tripel primitiv. Ohne Einschränkung sei $x$ gerade (sonst Vertauschung von $x$ und $y$). Dann existieren $s, t$ mit $s > t > 0$, $\gcd(s, t) = 1$, $s \not\equiv t \pmod{2}$, sodass:

$$
x^2 = 2st, \quad y^2 = s^2 - t^2, \quad z = s^2 + t^2
$$

**Schritt 2: Zweites pythagoreisches Tripel.**

Aus $y^2 = s^2 - t^2$ folgt $y^2 + t^2 = s^2$ – erneut ein pythagoreisches Tripel. Da $\gcd(s, t) = 1$ und $s \not\equiv t \pmod{2}$ ist auch dieses Tripel primitiv. Da $y$ ungerade ist ($x$ gerade und $\gcd(x, y) = 1$), ist $t$ gerade. Die Parametrisierung liefert $u, v$ mit $u > v > 0$, $\gcd(u, v) = 1$, $u \not\equiv v \pmod{2}$:

$$
t = 2uv, \quad y = u^2 - v^2, \quad s = u^2 + v^2
$$

**Schritt 3: Analyse von $x^2$ als Produkt.**

Einsetzen von $s = u^2 + v^2$ und $t = 2uv$ in $x^2 = 2st$:

$$
x^2 = 2 \cdot (u^2 + v^2) \cdot 2uv = 4uv(u^2 + v^2)
$$

Also $(x/2)^2 = uv(u^2 + v^2)$. Da $\gcd(u, v) = 1$, sind die drei Faktoren $u$, $v$ und $u^2 + v^2$ paarweise teilerfremd. Ihr Produkt ist ein Quadrat, also muss *jeder einzelne* Faktor ein Quadrat sein:

$$
u = a^2, \quad v = b^2, \quad u^2 + v^2 = c^2
$$

für gewisse positive ganze Zahlen $a, b, c$.

**Schritt 4: Der Abstieg.**

Aus $u^2 + v^2 = c^2$ und $u = a^2$, $v = b^2$ folgt:

$$
a^4 + b^4 = c^2
$$

Dieselbe Gleichung wie die Ausgangsgleichung. Und es gilt:

$$
c^2 = u^2 + v^2 = s \leq s^2 < s^2 + t^2 = z
$$

Also $c < z$ – eine *kleinere* Lösung.

**Widerspruch.** $(x, y, z)$ war als Lösung mit minimalem $z$ gewählt, aber $(a, b, c)$ ist eine Lösung mit $c < z$. $\blacksquare$

## 5. Struktur des Abstiegs

Die Beweisstruktur im Überblick:

```
Lösung (x, y, z) mit z minimal
    → Parametrisierung als pyth. Tripel → (s, t)
    → Zweites pyth. Tripel → (u, v)
    → Drei teilerfremde Quadrate → (a², b², c²)
    → Neue Lösung (a, b, c) mit c < z
    → WIDERSPRUCH
```

Der Schlüssel: Jeder Schritt verkleinert die Zahlen. Von $z$ über $s$ (kleiner als $z$) über $u$ und $v$ (kleiner als $s$) bis zu $c$ (kleiner als $z$). Die Wohlordnung von $\mathbb{N}$ garantiert, dass dieser Prozess nicht unendlich weitergehen kann.

> „The method of infinite descent is Fermat's most important legacy to number theory."
> — Harold M. Edwards, *Fermat's Last Theorem* (1977), S. 9

!!! note "Die stärkere Aussage als Notwendigkeit"
    Fermats Wahl von $z^2$ statt $z^4$ ist kein Zufall. Im Abstieg entsteht die Gleichung $a^4 + b^4 = c^2$ – nur wenn die rechte Seite ein *allgemeines* Quadrat sein darf (nicht nur eine vierte Potenz), schließt sich der Induktionskreis. Bei $x^4 + y^4 = z^4$ allein wäre die im Abstieg entstehende Gleichung nicht von derselben Form – der Beweis bräche zusammen.

## 6. Historische Einordnung

Dieser Beweis ist der **einzige Fall von FLT**, für den Fermat einen nachvollziehbaren Beweis hinterließ. Er erscheint in den *Observationes* (Anhang zur Arithmetica-Ausgabe von 1670) und beweist dort die Aussage, dass die Fläche eines rechtwinkligen Dreiecks mit ganzzahligen Seiten kein Quadrat sein kann – äquivalent zu $x^4 + y^4 = z^2$.

**Reichweite und Grenzen:**

- ✅ FLT gilt für $n = 4$ (und damit für alle durch $4$ teilbaren $n$: $8, 12, 16, \ldots$)
- ❌ Die Methode lässt sich **nicht** direkt auf $n = 3$ übertragen – die einfache Parametrisierung „kubischer Tripel" fehlt
- ❌ Für allgemeine Primzahlen $p$ versagt der elementare Abstieg

Der Fall $n = 3$ erfordert einen konzeptuellen Sprung: die Erweiterung des Zahlbereichs von $\mathbb{Z}$ auf $\mathbb{Z}[\omega]$. Damit beginnt der Weg zur algebraischen Zahlentheorie (siehe [Artikel 04](04-beweis-n3.md)).

---

## Quellen

- **Pierre de Fermat**: *Observationes ad Diophantum* (1670) – der Originalbeweis
- **Harold M. Edwards**: *Fermat's Last Theorem: A Genetic Introduction to Algebraic Number Theory*, Springer (1977)
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 1
