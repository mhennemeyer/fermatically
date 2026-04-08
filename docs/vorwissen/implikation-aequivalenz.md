---
title: "Implikation und Äquivalenz"
description: "Logische Folgerung, Kontraposition und die Äquivalenz von Aussagen"
lang: de
type: vorwissen
---

# Implikation und Äquivalenz

## Implikation (⟹)

Die **Implikation** $A \Rightarrow B$ („aus $A$ folgt $B$", „wenn $A$, dann $B$") ist nur dann falsch, wenn $A$ wahr und $B$ falsch ist.

| $A$ | $B$ | $A \Rightarrow B$ |
|-----|-----|--------------------|
| w   | w   | w                  |
| w   | f   | f                  |
| f   | w   | w                  |
| f   | f   | w                  |

**Zentrale Beobachtung:** Ist die Voraussetzung $A$ falsch, ist die Implikation immer wahr – unabhängig von $B$. Diese Konvention heißt **ex falso quodlibet**.

**Beispiel.** „Wenn $n$ durch 6 teilbar ist, dann ist $n$ durch 3 teilbar." → Für $n = 12$: wahr ⟹ wahr = wahr. Für $n = 5$: falsch ⟹ falsch = wahr.

## Äquivalenz zu ¬A ∨ B

Die Implikation $A \Rightarrow B$ ist **logisch äquivalent** zur Disjunktion $\neg A \lor B$:

$$
(A \Rightarrow B) \iff (\neg A \lor B)
$$

| $A$ | $B$ | $\neg A$ | $\neg A \lor B$ | $A \Rightarrow B$ |
|-----|-----|----------|------------------|--------------------|
| w   | w   | f        | w                | w                  |
| w   | f   | f        | f                | f                  |
| f   | w   | w        | w                | w                  |
| f   | f   | w        | w                | w                  |

Die Spalten stimmen überein. Das bedeutet: „Wenn $A$, dann $B$" sagt dasselbe wie „$A$ ist falsch oder $B$ ist wahr".

## Kontraposition

Die **Kontraposition** einer Implikation $A \Rightarrow B$ ist $\neg B \Rightarrow \neg A$. Beide sind logisch äquivalent:

$$
(A \Rightarrow B) \iff (\neg B \Rightarrow \neg A)
$$

**Beispiel.** „Wenn $n^2$ gerade ist, dann ist $n$ gerade." Die Kontraposition lautet: „Wenn $n$ ungerade ist, dann ist $n^2$ ungerade." Beide Aussagen sind gleichwertig.

Die Kontraposition ist ein häufig genutztes Beweismittel: Statt $A \Rightarrow B$ direkt zu zeigen, zeigt man $\neg B \Rightarrow \neg A$.

## Umkehrung

Die **Umkehrung** von $A \Rightarrow B$ ist $B \Rightarrow A$. Die Umkehrung ist **nicht** automatisch äquivalent zur Originalaussage.

**Beispiel.** „Wenn $n$ durch 6 teilbar ist, dann ist $n$ durch 3 teilbar." → wahr. Umkehrung: „Wenn $n$ durch 3 teilbar ist, dann ist $n$ durch 6 teilbar." → falsch ($n = 9$).

## Äquivalenz (⟺)

Die **Äquivalenz** $A \Leftrightarrow B$ („$A$ genau dann, wenn $B$") ist wahr, wenn beide Aussagen denselben Wahrheitswert haben:

| $A$ | $B$ | $A \Leftrightarrow B$ |
|-----|-----|------------------------|
| w   | w   | w                      |
| w   | f   | f                      |
| f   | w   | f                      |
| f   | f   | w                      |

Die Äquivalenz entspricht der Konjunktion beider Richtungen:

$$
(A \Leftrightarrow B) \iff (A \Rightarrow B) \land (B \Rightarrow A)
$$

**Beispiel.** „$n$ ist gerade $\Leftrightarrow$ $n^2$ ist gerade." Beide Richtungen gelten, also liegt Äquivalenz vor.

---

## Zusammenfassung

| Verknüpfung | Symbol | Bedeutung |
|-------------|--------|-----------|
| Implikation | $A \Rightarrow B$ | „wenn $A$, dann $B$"; äquivalent zu $\neg A \lor B$ |
| Kontraposition | $\neg B \Rightarrow \neg A$ | äquivalent zu $A \Rightarrow B$ |
| Umkehrung | $B \Rightarrow A$ | **nicht** äquivalent zu $A \Rightarrow B$ |
| Äquivalenz | $A \Leftrightarrow B$ | beide Richtungen gelten |

## Quellen

- Ebbinghaus, H.-D.; Flum, J.; Thomas, W.: *Einführung in die mathematische Logik.* Springer, 6. Auflage, 2018. Kapitel 1.
- Velleman, Daniel J.: *How to Prove It.* Cambridge University Press, 3. Auflage, 2019. Kapitel 2.
