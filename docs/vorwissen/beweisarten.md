---
title: "Beweisarten"
description: "Direkter Beweis, Widerspruchsbeweis, vollständige Induktion und Beweis durch Gegenbeispiel"
lang: de
type: vorwissen
---

# Beweisarten

## Direkter Beweis

Ein **direkter Beweis** zeigt eine Aussage $A \Rightarrow B$, indem aus der Annahme $A$ durch logische Schlüsse $B$ abgeleitet wird.

**Beispiel.** *Behauptung:* Die Summe zweier gerader Zahlen ist gerade.

*Beweis.* Seien $a = 2m$ und $b = 2n$ mit $m, n \in \mathbb{Z}$. Dann gilt:

$$
a + b = 2m + 2n = 2(m + n)
$$

Da $m + n \in \mathbb{Z}$, ist $a + b$ gerade. $\square$

## Widerspruchsbeweis (Reductio ad Absurdum)

Ein **Widerspruchsbeweis** nimmt das Gegenteil der zu zeigenden Aussage an und leitet daraus einen Widerspruch ab. Formal: Um $A$ zu beweisen, wird $\neg A$ angenommen und gezeigt, dass dies zu einem logischen Widerspruch führt.

**Beispiel.** *Behauptung:* $\sqrt{2}$ ist irrational.

*Beweis.* Annahme: $\sqrt{2} = \frac{p}{q}$ mit $p, q \in \mathbb{Z}$, $q \neq 0$, $\gcd(p, q) = 1$ (vollständig gekürzt). Dann $2 = \frac{p^2}{q^2}$, also $p^2 = 2q^2$. Damit ist $p^2$ gerade, also $p$ gerade, also $p = 2k$. Einsetzen: $(2k)^2 = 2q^2$, also $4k^2 = 2q^2$, also $q^2 = 2k^2$. Damit ist auch $q$ gerade. Widerspruch zu $\gcd(p, q) = 1$. $\square$

## Beweis durch Kontraposition

Der **Beweis durch Kontraposition** nutzt die logische Äquivalenz $(A \Rightarrow B) \iff (\neg B \Rightarrow \neg A)$. Statt $A \Rightarrow B$ direkt zu zeigen, wird $\neg B \Rightarrow \neg A$ bewiesen.

**Beispiel.** *Behauptung:* Wenn $n^2$ gerade ist, dann ist $n$ gerade.

*Beweis (Kontraposition).* Zu zeigen: Wenn $n$ ungerade ist, dann ist $n^2$ ungerade. Sei $n = 2k + 1$. Dann $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, also ungerade. $\square$

## Vollständige Induktion

Die **vollständige Induktion** beweist Aussagen der Form „für alle $n \geq n_0$ gilt $P(n)$" in zwei Schritten:

1. **Induktionsanfang (IA):** $P(n_0)$ ist wahr.
2. **Induktionsschritt (IS):** Für beliebiges $n \geq n_0$ gilt: Wenn $P(n)$ wahr ist (**Induktionsvoraussetzung**, IV), dann ist auch $P(n+1)$ wahr.

**Beispiel.** *Behauptung:* $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ für alle $n \geq 1$.

*IA:* $n = 1$: $\sum_{k=1}^{1} k = 1 = \frac{1 \cdot 2}{2}$. ✓

*IS:* Angenommen, die Formel gilt für $n$ (IV). Dann:

$$
\sum_{k=1}^{n+1} k = \underbrace{\sum_{k=1}^{n} k}_{\text{IV: } \frac{n(n+1)}{2}} + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}
$$

Das ist die Formel für $n+1$. $\square$

## Beweis durch Gegenbeispiel

Ein **Beweis durch Gegenbeispiel** widerlegt eine Allaussage „für alle $x$ gilt $P(x)$", indem ein konkretes $x_0$ angegeben wird, für das $P(x_0)$ falsch ist.

**Beispiel.** *Behauptung:* „Alle Primzahlen sind ungerade." *Gegenbeispiel:* $2$ ist eine Primzahl und gerade. $\square$

Ein einziges Gegenbeispiel genügt, um eine Allaussage zu widerlegen.

---

## Zusammenfassung

| Beweisart | Vorgehen |
|-----------|----------|
| Direkter Beweis | Aus $A$ wird $B$ direkt abgeleitet |
| Widerspruchsbeweis | $\neg A$ annehmen → Widerspruch |
| Kontraposition | $\neg B \Rightarrow \neg A$ zeigen |
| Vollständige Induktion | IA + IS (von $n$ auf $n+1$) |
| Gegenbeispiel | Ein $x_0$ mit $\neg P(x_0)$ angeben |

## Quellen

- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3. Auflage, 2019.
- Hammack, Richard: *Book of Proof.* 3. Auflage, 2018. (frei verfügbar)
