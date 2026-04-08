---
title: "Aussagenlogik"
description: "Aussagen, Wahrheitswerte, Konjunktion, Disjunktion und Negation"
lang: de
type: vorwissen
---

# Aussagenlogik

## Aussagen und Wahrheitswerte

Eine **Aussage** ist ein Satz, dem genau einer der Wahrheitswerte **wahr** (w) oder **falsch** (f) zugeordnet werden kann.

**Beispiele für Aussagen:**

- „7 ist eine Primzahl." → wahr
- „4 ist ungerade." → falsch
- „$2 + 3 = 5$." → wahr

**Keine Aussagen** sind Fragen („Ist 7 eine Primzahl?"), Aufforderungen („Berechne den ggT!") oder unbestimmte Ausdrücke („$x > 3$" – hängt von $x$ ab).

## Negation (¬)

Die **Negation** einer Aussage $A$ kehrt den Wahrheitswert um. Notation: $\neg A$.

| $A$ | $\neg A$ |
|-----|----------|
| w   | f        |
| f   | w        |

**Beispiel.** $A$: „5 ist gerade." (falsch) → $\neg A$: „5 ist nicht gerade." (wahr)

## Konjunktion (∧)

Die **Konjunktion** $A \land B$ („$A$ und $B$") ist genau dann wahr, wenn **beide** Aussagen wahr sind.

| $A$ | $B$ | $A \land B$ |
|-----|-----|-------------|
| w   | w   | w           |
| w   | f   | f           |
| f   | w   | f           |
| f   | f   | f           |

**Beispiel.** „7 ist eine Primzahl **und** 7 ist ungerade." → wahr ∧ wahr = wahr.

## Disjunktion (∨)

Die **Disjunktion** $A \lor B$ („$A$ oder $B$") ist wahr, wenn **mindestens eine** der Aussagen wahr ist.

| $A$ | $B$ | $A \lor B$ |
|-----|-----|------------|
| w   | w   | w          |
| w   | f   | w          |
| f   | w   | w          |
| f   | f   | f          |

Das mathematische „oder" ist **inklusiv**: Auch wenn beide wahr sind, ist die Disjunktion wahr.

**Beispiel.** „4 ist gerade **oder** 4 ist eine Primzahl." → wahr ∨ falsch = wahr.

## De Morgansche Gesetze

Zwei fundamentale Umformungsregeln:

$$
\neg (A \land B) \iff (\neg A) \lor (\neg B)
$$

$$
\neg (A \lor B) \iff (\neg A) \land (\neg B)
$$

In Worten: Die Negation eines „und" wird zu einem „oder" der Negationen – und umgekehrt.

---

## Zusammenfassung

| Verknüpfung | Symbol | Wahr wenn… |
|-------------|--------|-----------|
| Negation | $\neg A$ | $A$ falsch ist |
| Konjunktion | $A \land B$ | beide wahr |
| Disjunktion | $A \lor B$ | mindestens eine wahr |

## Quellen

- Ebbinghaus, H.-D.; Flum, J.; Thomas, W.: *Einführung in die mathematische Logik.* Springer, 6. Auflage, 2018. Kapitel 1.
