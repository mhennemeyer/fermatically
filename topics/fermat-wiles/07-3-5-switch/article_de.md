---
title: "Der 3-5-Switch und der Abschluss"
slug: fermat-wiles/07-3-5-switch
series: fermat-wiles
part: 7
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - 3-5-switch
  - langlands-tunnell
  - modularitaet
requires:
  - beweisarten
---
# Der 3-5-Switch und der Abschluss

!!! abstract "Zusammenfassung"
    Der 3-5-Switch ist der elegante letzte Baustein in Wiles' Beweis.
    Das Theorem von Langlands-Tunnell liefert die residuale Modularität
    für $p = 3$. Wenn die 3-Darstellung reduzibel ist, wechselt Wiles
    zu $p = 5$ und konstruiert eine Hilfs-Kurve, die den Einstieg
    ermöglicht. So wird jede semistabile elliptische Kurve als modular
    erkannt – und Fermats letzter Satz ist bewiesen.

## Voraussetzungen

- [Der Taylor-Wiles-Trick](../06-taylor-wiles-trick/article_de.md) – Patching-Argument und $R = T$

| Thema | Beschreibung |
|-------|-------------|
| [Beweisarten](../../vorwissen/beweisarten/article_de.md) | Direkter Beweis, Widerspruch, Induktion, Abstieg |

---

## 1. Das Problem mit $p = 3$

### Erinnerung: Die Beweisstrategie

Wiles' Beweis der Modularität semistabiler Kurven hat zwei Stufen:

1. **Residuale Modularität**: Zeige, dass $\bar{\rho}_{E,p}$ modular ist.
2. **Liftung**: Beweise $R = T$, um von residualer zu voller Modularität zu gelangen.

Stufe 2 ist erledigt (Taylor-Wiles-Trick). Bleibt Stufe 1: Woher kommt die residuale Modularität?

### Langlands-Tunnell

Für $p = 3$ gibt es ein mächtiges Ergebnis:

!!! note "Theorem (Langlands-Tunnell)"
    Sei $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_3)$ eine stetige,
    ungerade Darstellung. Dann ist $\bar{\rho}$ modular – es existiert eine
    Modulform $f$ vom Gewicht 1 mit $\bar{\rho} \cong \bar{\rho}_f$.

Der Beweis nutzt eine besondere Eigenschaft von $\text{GL}_2(\mathbb{F}_3)$: Diese Gruppe ist **auflösbar** (sie hat Ordnung 48 und ist isomorph zu einer Erweiterung von $S_3$ durch $\mathbb{Z}/2\mathbb{Z}$). Für auflösbare Gruppen stehen die Werkzeuge des **Langlands-Programms** zur Verfügung – insbesondere der Basiswechsel (base change) für $\text{GL}_2$.

Langlands bewies 1980 die Modulformen-Korrespondenz für auflösbare Galois-Darstellungen, und Tunnell verfeinerte das Ergebnis 1981.

### Vom Gewicht 1 zum Gewicht 2

Langlands-Tunnell liefert eine Modulform vom **Gewicht 1**, benötigt wird aber Gewicht 2 (für den Zusammenhang mit elliptischen Kurven). Wiles löst das durch ein Liftungsargument:

Aus der Gewicht-1-Form $f$ konstruiert man eine Gewicht-2-Form $g$ mit $\bar{\rho}_g \cong \bar{\rho}_{E,3}$. Dies nutzt Hidas Theorie ordinärer $p$-adischer Modulformen.

---

## 2. Warum reicht $p = 3$ nicht?

### Die Irreduzibilitätsbedingung

Wiles' Beweis von $R = T$ (und das Taylor-Wiles-Patching) erfordert, dass $\bar{\rho}_{E,p}$ **irreduzibel** ist. Für die Frey-Kurve ist das für $p \geq 5$ automatisch erfüllt (nach Mazur). Aber für eine allgemeine semistabile Kurve $E$ kann $\bar{\rho}_{E,3}$ **reduzibel** sein.

### Wann ist $\bar{\rho}_{E,3}$ reduzibel?

Die Darstellung $\bar{\rho}_{E,3}$ ist reduzibel genau dann, wenn $E$ einen rationalen **3-Isogenie-Kern** hat – einen $G_{\mathbb{Q}}$-stabilen Untervektorraum von $E[3]$ der Dimension 1 über $\mathbb{F}_3$. Geometrisch bedeutet das: Es gibt eine Isogenie $E \to E'$ vom Grad 3 mit rationalem Kern.

Dies kommt durchaus vor – es gibt unendlich viele solcher Kurven. Für diese Kurven scheitert der Beweis mit $p = 3$.

### Die Situation

| $\bar{\rho}_{E,3}$ | Modular? | Irreduzibel? | $R = T$ möglich? |
|---------------------|----------|--------------|-------------------|
| irreduzibel | Ja (Langlands-Tunnell) | Ja | ✓ Beweis funktioniert |
| reduzibel | Ja (Langlands-Tunnell) | **Nein** | ✗ Irreduzibilität fehlt |

---

## 3. Der Switch zu $p = 5$

### Die Idee

Wenn $\bar{\rho}_{E,3}$ reduzibel ist, betrachte stattdessen $\bar{\rho}_{E,5}$. Die 5-Darstellung hat gute Chancen, irreduzibel zu sein – denn eine Kurve, die sowohl einen 3-Isogenie-Kern als auch einen 5-Isogenie-Kern hat, wäre sehr speziell.

### Irreduzibilität von $\bar{\rho}_{E,5}$

Wiles zeigt: Wenn $E$ semistabil ist und $\bar{\rho}_{E,3}$ reduzibel, dann ist $\bar{\rho}_{E,5}$ **irreduzibel**. Dies folgt aus Mazurs Klassifikation der möglichen Torsionsstrukturen rationaler elliptischer Kurven:

!!! note "Theorem (Mazur, 1978)"
    Sei $E/\mathbb{Q}$ eine elliptische Kurve. Wenn $E$ eine rationale Isogenie
    vom Grad $\ell$ hat (für eine Primzahl $\ell$), dann $\ell \leq 19$ oder
    $\ell \in \{37, 43, 67, 163\}$.

Für eine **semistabile** Kurve kann man die Möglichkeiten weiter einschränken. Insbesondere gibt es keine semistabile Kurve mit gleichzeitig rationalem 3- und 5-Isogenie-Kern (dies würde eine rationale 15-Isogenie implizieren, die Mazur ausschließt).

### Das neue Problem

$\bar{\rho}_{E,5}$ ist nun irreduzibel – aber woher kommt die **residuale Modularität**? Langlands-Tunnell funktioniert nur für $p = 3$, nicht für $p = 5$ (denn $\text{GL}_2(\mathbb{F}_5)$ ist **nicht auflösbar**).

Hier kommt der geniale Trick.

---

## 4. Eine Hilfs-Kurve konstruieren

### Die Strategie

Wiles sucht eine **zweite elliptische Kurve** $E'$ mit folgenden Eigenschaften:

1. $E'[5] \cong E[5]$ als Galois-Modul (die 5-Torsion stimmt überein)
2. $\bar{\rho}_{E',3}$ ist **irreduzibel** (damit $p = 3$ für $E'$ funktioniert)
3. $E'$ ist semistabil

### Warum eine solche Kurve existiert

Die Menge der elliptischen Kurven $E'$ mit $E'[5] \cong E[5]$ wird durch eine **modulare Kurve** $X(5)$ parametrisiert – eine Kurve vom Geschlecht 0 (also rational!). Es gibt daher unendlich viele solche Kurven $E'$.

Unter diesen unendlich vielen Kandidaten muss Wiles eine finden, die:
- semistabil ist (an allen Primzahlen), und
- $\bar{\rho}_{E',3}$ irreduzibel hat.

Da die Bedingung „$\bar{\rho}_{E',3}$ reduzibel" eine echte Teilmenge ausschließt und die Parametrisierung über eine rationale Kurve verläuft, existiert eine solche Kurve $E'$.

### Die Konstruktion

Konkret: Über dem Funktionenkörper $\mathbb{Q}(t)$ gibt es eine „universelle" Kurve mit der richtigen 5-Torsion. Durch Spezialisierung bei geeigneten rationalen Werten $t = t_0$ erhält man die gewünschte Hilfs-Kurve $E'$.

---

## 5. Die Kette schließen

### Schritt 1: $E'$ ist modular (via $p = 3$)

Da $\bar{\rho}_{E',3}$ irreduzibel ist, lässt sich der gesamte Beweisapparat für $p = 3$ anwenden:

$$
\bar{\rho}_{E',3} \text{ irreduzibel} \xrightarrow{\text{Langlands-Tunnell}} \bar{\rho}_{E',3} \text{ modular} \xrightarrow{R = T} \rho_{E',3} \text{ modular} \implies E' \text{ modular.}
$$

### Schritt 2: $E[5]$ ist modular

Da $E'$ modular ist, gilt insbesondere: $\bar{\rho}_{E',5}$ ist modular (die 5-residuale Darstellung kommt von einer Modulform). Da $E'[5] \cong E[5]$, folgt:

$$
\bar{\rho}_{E,5} \cong \bar{\rho}_{E',5} \quad \text{ist modular.}
$$

### Schritt 3: $E$ ist modular (via $p = 5$)

Damit ist der Einstieg für $p = 5$ gesichert: $\bar{\rho}_{E,5}$ ist modular und irreduzibel. Der Taylor-Wiles-Trick liefert $R = T$ für $p = 5$:

$$
\bar{\rho}_{E,5} \text{ modular + irreduzibel} \xrightarrow{R = T} \rho_{E,5} \text{ modular} \implies E \text{ modular.}
$$

### Die gesamte Kette

$$
\boxed{E'[5] \cong E[5]} \quad + \quad \boxed{E' \text{ modular (via } p=3\text{)}} \implies \boxed{\bar{\rho}_{E,5} \text{ modular}} \xrightarrow{R=T} \boxed{E \text{ modular}}
$$

---

## 6. FLT ist bewiesen

### Die Fallunterscheidung

Für jede semistabile elliptische Kurve $E/\mathbb{Q}$:

**Fall 1: $\bar{\rho}_{E,3}$ irreduzibel.** Langlands-Tunnell + Taylor-Wiles ($p = 3$) → $E$ modular. ✓

**Fall 2: $\bar{\rho}_{E,3}$ reduzibel.** Dann $\bar{\rho}_{E,5}$ irreduzibel. Konstruiere Hilfs-Kurve $E'$ mit $E'[5] \cong E[5]$ und $\bar{\rho}_{E',3}$ irreduzibel. Dann: $E'$ modular (Fall 1) → $\bar{\rho}_{E,5}$ modular → Taylor-Wiles ($p = 5$) → $E$ modular. ✓

**In beiden Fällen ist $E$ modular.** Da die Frey-Kurve semistabil ist, folgt Fermats letzter Satz.

### Das vollständige Beweisdiagramm

$$
\text{FLT-Lösung} \xrightarrow{\text{Frey}} E_{\text{Frey}} \xrightarrow{\text{Wiles (3 oder 3-5)}} \text{modular} \xrightarrow{\text{Ribet}} \text{Widerspruch}
$$

!!! note "Theorem (Wiles, Taylor-Wiles, 1995)"
    Jede semistabile elliptische Kurve über $\mathbb{Q}$ ist modular.

!!! note "Korollar (Fermats letzter Satz)"
    Die Gleichung $x^n + y^n = z^n$ hat für $n \geq 3$ keine Lösung in positiven ganzen Zahlen.

---

## 7. Rückblick: Die gesamte Beweisstruktur

### Von Fermat zu Wiles

Der vollständige Beweis verbindet Ideen aus über vier Jahrhunderten Mathematik:

| Jahr | Mathematiker | Beitrag |
|------|-------------|---------|
| 1637 | Fermat | Die Vermutung |
| 1640 | Fermat | Beweis für $n = 4$ (Infinite Descent) |
| 1770 | Euler | Beweis für $n = 3$ |
| 1955 | Taniyama, Shimura | TSV: Elliptische Kurven ↔ Modulformen |
| 1980 | Langlands, Tunnell | Modularität auflösbarer Darstellungen |
| 1985 | Frey | FLT-Lösung → „unmögliche" elliptische Kurve |
| 1986 | Ribet | Level-Lowering: TSV ⟹ FLT |
| 1989 | Mazur | Universelle Deformationsringe |
| 1995 | Wiles | $R = T$ für semistabile Kurven |
| 1995 | Taylor-Wiles | Patching-Argument (Lückenschluss) |

### Die logische Struktur

```
FLT-Lösung (hypothetisch)
  ↓  [Frey 1985]
Frey-Kurve E (semistabil, extreme Diskriminante)
  ↓  [Wiles 1995: 3-5-Switch + R=T + Taylor-Wiles]
E ist modular
  ↓  [Ribet 1986: Level-Lowering]
ρ̄(E,p) kommt von Neuform der Stufe 2
  ↓  [S₂(Γ₀(2)) = 0]
Widerspruch → FLT-Lösung existiert nicht   □
```

### Was den Beweis so bemerkenswert macht

1. **Indirektheit**: FLT wird nicht direkt bewiesen, sondern durch Widerspruch – über den Umweg elliptischer Kurven, Modulformen und Galois-Darstellungen.
2. **Vereinigung**: Der Beweis vereint Zahlentheorie, algebraische Geometrie, komplexe Analysis und Darstellungstheorie.
3. **Tiefe**: Die Methoden (Deformationstheorie, Patching) sind nicht speziell für FLT, sondern Werkzeuge von allgemeiner Bedeutung.
4. **Menschlichkeit**: Die Geschichte von Wiles' siebenjährigem Geheimprojekt, der Lücke und ihrer Schließung ist einzigartig in der Mathematikgeschichte.

---

## Ausblick

Der nächste und letzte Artikel blickt über Wiles' Beweis hinaus:

| Artikel | Thema |
|---------|-------|
| [08 – Was danach kam](../08-was-danach-kam/article_de.md) | BCDT, Serres Vermutung, Langlands-Programm |

---

## Quellen

- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §5
- **Robert Langlands**: *Base change for GL(2)*, Annals of Mathematics Studies 96 (1980)
- **Jerrold Tunnell**: *Artin's conjecture for representations of octahedral type*, Bulletin of the AMS 5 (1981)
- **Barry Mazur**: *Rational isogenies of prime degree*, Inventiones Mathematicae 44 (1978)
- **Gary Cornell, Joseph Silverman, Glenn Stevens** (Hrsg.): *Modular Forms and Fermat's Last Theorem*, Springer (1997), Kapitel XV–XVI
