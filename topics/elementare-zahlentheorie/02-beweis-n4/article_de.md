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
    Fermats eigener Beweis – der einzige Fall von FLT, den er selbst bewiesen hat.
    Wir lernen die Methode des unendlichen Abstiegs kennen und zeigen:
    $x^4 + y^4 = z^2$ hat keine Lösung in positiven ganzen Zahlen.

## Voraussetzungen

- [Was ist Fermats letzter Satz?](../01-was-ist-flt/article_de.md)

---

## 1. Die Methode des unendlichen Abstiegs

Der **unendliche Abstieg** (*descente infinie*) ist eine Beweistechnik, die Fermat selbst erfand – und die er als seine liebste Methode bezeichnete. Die Grundidee ist bestechend einfach:

**Angenommen**, eine Gleichung hätte eine Lösung in positiven ganzen Zahlen. Dann zeige, dass aus dieser Lösung eine *kleinere* Lösung konstruiert werden kann – also eine Lösung, bei der die beteiligten Zahlen echt kleiner sind. Aus dieser kleineren Lösung ließe sich eine noch kleinere konstruieren, und so weiter – *ad infinitum*.

Aber: Positive ganze Zahlen können nicht unendlich klein werden. Es gibt kein unendliches Absteigen in $\mathbb{Z}^+$. Also ist die Annahme falsch, und die Gleichung hat keine Lösung.

Formal nutzt der Abstieg das **Wohlordnungsprinzip**: Jede nichtleere Teilmenge von $\mathbb{N}$ hat ein kleinstes Element. Eine unendlich absteigende Folge positiver ganzer Zahlen kann es daher nicht geben.

!!! note "Abstieg vs. Widerspruch"
    Der unendliche Abstieg ist ein spezieller **Widerspruchsbeweis**: Man nimmt an, es gäbe eine Lösung, und leitet daraus eine unmögliche Konsequenz ab (die unendliche absteigende Folge). In der modernen Formulierung äquivalent: Man betrachtet eine *minimale* Lösung und zeigt, dass eine noch kleinere existieren müsste – Widerspruch.

## 2. Pythagoreische Tripel

Bevor wir den Beweis für $n = 4$ führen können, brauchen wir ein klassisches Ergebnis: die vollständige Beschreibung aller Lösungen von $x^2 + y^2 = z^2$.

**Satz (Parametrisierung der pythagoreischen Tripel).** Alle *primitiven* pythagoreischen Tripel $(x, y, z)$ mit $\gcd(x, y) = 1$ und $x$ gerade haben die Form:

$$
x = 2st, \quad y = s^2 - t^2, \quad z = s^2 + t^2
$$

wobei $s > t > 0$, $\gcd(s, t) = 1$ und $s \not\equiv t \pmod{2}$ (also $s$ und $t$ haben verschiedene Parität).

**Beweisskizze.** Wir schreiben $x^2 = z^2 - y^2 = (z-y)(z+y)$. Da $(x, y, z)$ primitiv ist, sind $z - y$ und $z + y$ teilerfremd (bis auf den Faktor 2). Da $x$ gerade ist, sind $z$ und $y$ beide ungerade, also sind $z - y$ und $z + y$ beide gerade. Setze $z - y = 2u$ und $z + y = 2v$, dann ist $x^2 = 4uv$ mit $\gcd(u, v) = 1$. Da das Produkt $uv$ ein Quadrat und die Faktoren teilerfremd sind, müssen $u$ und $v$ selbst Quadrate sein: $u = t^2$, $v = s^2$. Einsetzen liefert die Parametrisierung. $\square$

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

Warum ist das stärker? Weil $z^4 = (z^2)^2$ ein spezielles Quadrat ist. Wenn es keine Lösung mit $z^2$ auf der rechten Seite gibt, dann erst recht nicht mit $z^4$.

$$
x^4 + y^4 = z^4 \implies x^4 + y^4 = (z^2)^2
$$

Also: $x^4 + y^4 = z^2$ hat keine Lösung $\implies$ $x^4 + y^4 = z^4$ hat keine Lösung.

## 4. Der Beweis im Detail

Wir beweisen: $x^4 + y^4 = z^2$ hat keine Lösung in $x, y, z \in \mathbb{Z}^+$.

**Annahme zum Widerspruch.** Sei $(x, y, z)$ eine Lösung mit *minimalem* $z$. Ohne Einschränkung sei $\gcd(x, y) = 1$ (sonst kürzen wir den gemeinsamen Faktor heraus und erhalten eine kleinere Lösung).

**Schritt 1: Pythagoreische Tripel anwenden.**

Die Gleichung $x^4 + y^4 = z^2$ lässt sich als $(x^2)^2 + (y^2)^2 = z^2$ lesen – ein pythagoreisches Tripel! Da $\gcd(x, y) = 1$ ist das Tripel primitiv, und wir können die Parametrisierung anwenden. Ohne Einschränkung sei $x$ gerade (sonst vertausche $x$ und $y$). Dann existieren $s, t$ mit $s > t > 0$, $\gcd(s, t) = 1$, $s \not\equiv t \pmod{2}$, sodass:

$$
x^2 = 2st, \quad y^2 = s^2 - t^2, \quad z = s^2 + t^2
$$

**Schritt 2: Noch ein pythagoreisches Tripel.**

Aus $y^2 = s^2 - t^2$ folgt $y^2 + t^2 = s^2$ – wieder ein pythagoreisches Tripel! Da $\gcd(s, t) = 1$ und $s \not\equiv t \pmod{2}$ ist auch dieses Tripel primitiv. Nun ist $y$ ungerade (weil $x$ gerade und $\gcd(x, y) = 1$), also ist $t$ gerade. Die Parametrisierung liefert $u, v$ mit $u > v > 0$, $\gcd(u, v) = 1$, $u \not\equiv v \pmod{2}$:

$$
t = 2uv, \quad y = u^2 - v^2, \quad s = u^2 + v^2
$$

**Schritt 3: $x^2$ als Produkt analysieren.**

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

Das ist dieselbe Gleichung wie unsere Ausgangsgleichung! Und es gilt:

$$
c^2 = u^2 + v^2 = s \leq s^2 < s^2 + t^2 = z
$$

Also $c < z$ – wir haben eine *kleinere* Lösung gefunden.

**Widerspruch.** Wir hatten $(x, y, z)$ als Lösung mit minimalem $z$ gewählt, aber $(a, b, c)$ ist eine Lösung mit $c < z$. Widerspruch! $\blacksquare$

## 5. Warum der Abstieg funktioniert

Der Beweis hat eine elegante Struktur:

```
Lösung (x, y, z) mit z minimal
    → Parametrisierung als pyth. Tripel → (s, t)
    → Zweites pyth. Tripel → (u, v)
    → Drei teilerfremde Quadrate → (a², b², c²)
    → Neue Lösung (a, b, c) mit c < z
    → WIDERSPRUCH
```

Der Schlüssel ist, dass jeder Schritt die Zahlen verkleinert. Von $z$ über $s$ (das kleiner als $z$ ist) über $u$ und $v$ (die kleiner als $s$ sind) bis zu $c$ (das kleiner als $z$ ist). Die Wohlordnung von $\mathbb{N}$ garantiert, dass dieser Prozess nicht unendlich weitergehen kann.

!!! note "Warum die stärkere Aussage?"
    Fermats Trick, $z^2$ statt $z^4$ zu betrachten, ist kein Zufall. Im Abstieg entsteht eine Gleichung $a^4 + b^4 = c^2$ – nur wenn die rechte Seite ein *allgemeines* Quadrat sein darf (nicht nur eine vierte Potenz), schließt sich der Induktionskreis. Hätten wir nur $x^4 + y^4 = z^4$ betrachtet, wäre die im Abstieg entstehende Gleichung $a^4 + b^4 = c^2$ nicht von derselben Form – und der Beweis bräche zusammen.

## 6. Historische Einordnung

Dieser Beweis ist der **einzige Fall von FLT**, für den Fermat selbst einen nachvollziehbaren Beweis hinterließ. Er erscheint in seinen *Observationes* (Anhang zur Arithmetica-Ausgabe von 1670) und beweist dort die Aussage, dass die Fläche eines rechtwinkligen Dreiecks mit ganzzahligen Seiten kein Quadrat sein kann – was äquivalent zu $x^4 + y^4 = z^2$ ist.

**Was der Beweis zeigt – und was nicht:**

- ✅ FLT ist wahr für $n = 4$ (und damit für alle $n$, die durch $4$ teilbar sind: $n = 8, 12, 16, \ldots$)
- ❌ Die Methode lässt sich **nicht** direkt auf $n = 3$ übertragen – dafür fehlt die einfache Parametrisierung der „kubischen Tripel"
- ❌ Für allgemeine Primzahlen $p$ versagt der elementare Abstieg

Der Fall $n = 3$ erfordert, wie wir in [Artikel 4](../04-beweis-n3/article_de.md) sehen werden, einen entscheidenden konzeptuellen Sprung: Man muss den Zahlbereich von $\mathbb{Z}$ auf $\mathbb{Z}[\omega]$ erweitern. Hier beginnt der Weg zur algebraischen Zahlentheorie.

---

## Weiterführende Quellen

- **Fermat**: *Observationes ad Diophantum* (1670) – der Originalbeweis
- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Kap. 1
- **Harold Edwards**: *Fermat's Last Theorem* – historisch detaillierte Darstellung
