---
title: "Deformationstheorie"
slug: fermat-wiles/04-deformationstheorie
series: fermat-wiles
part: 4
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - deformationstheorie
  - mazur
  - deformationsring
requires:
  - fermat-wiles/03-galois-darstellungen
  - p-adische-zahlen/01-p-adische-zahlen
---
# Deformationstheorie

!!! abstract "Zusammenfassung"
    Mazurs Deformationstheorie fragt: Gegeben eine residuale Galois-Darstellung
    $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p)$, welche „Liftungen"
    nach $\text{GL}_2(A)$ für lokale Ringe $A$ existieren? Der universelle
    Deformationsring $R$ parametrisiert alle zulässigen Liftungen, die Hecke-Algebra
    $T$ die modularen. Wiles' Ziel: $R = T$.

## Voraussetzungen

- [Galois-Darstellungen](../03-galois-darstellungen/article_de.md) – Residuale und $p$-adische Darstellungen, Modularität
- [p-adische Zahlen](../../p-adische-zahlen/01-p-adische-zahlen/article_de.md) – Lokale Ringe, $\mathbb{Z}_p$, $p$-adische Topologie

---

## 1. Die Ausgangslage

### Was wir haben

Nach den Ergebnissen von Langlands-Tunnell (für $p = 3$) oder durch den 3-5-Switch (für $p = 5$) wissen wir: Für eine semistabile elliptische Kurve $E/\mathbb{Q}$ ist die **residuale Darstellung**

$$
\bar{\rho} = \bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p)
$$

**modular** – sie kommt von einer Neuform.

### Was wir zeigen wollen

Wir müssen beweisen, dass auch die **volle $p$-adische Darstellung**

$$
\rho = \rho_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p)
$$

modular ist. Die residuale Darstellung ist die Reduktion modulo $p$: $\rho \bmod p = \bar{\rho}$.

### Die Frage der Liftung

Das Problem lässt sich so formulieren: Unter allen Darstellungen $\rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p)$, die modulo $p$ die gegebene Darstellung $\bar{\rho}$ ergeben, welche sind modular? **Wiles' Antwort: Alle (unter geeigneten Bedingungen).**

Dazu braucht man ein systematisches Werkzeug, um den „Raum aller Liftungen" zu beschreiben – und genau das leistet Mazurs Deformationstheorie.

---

## 2. Was ist eine Deformation?

### Lokale Ringe

Ein **vollständiger lokaler noetherscher Ring** $A$ mit Restklassenkörper $\mathbb{F}_p$ ist ein Ring der Form

$$
A = \varprojlim A/\mathfrak{m}^n,
$$

wobei $\mathfrak{m}$ das maximale Ideal ist und $A/\mathfrak{m} \cong \mathbb{F}_p$. Beispiele:

- $A = \mathbb{F}_p$ (triviale Liftung – nur die residuale Darstellung)
- $A = \mathbb{Z}_p$ (die $p$-adischen ganzen Zahlen)
- $A = \mathbb{Z}_p[[x_1, \ldots, x_n]]$ (formale Potenzreihenringe)
- $A = \mathbb{Z}_p[x]/(x^2)$ (Dualzahlen – für infinitesimale Deformationen)

### Liftungen

Eine **Liftung** von $\bar{\rho}$ nach $A$ ist ein stetiger Homomorphismus

$$
\rho_A: G_{\mathbb{Q}} \to \text{GL}_2(A),
$$

der modulo $\mathfrak{m}$ die gegebene Darstellung $\bar{\rho}$ ergibt:

$$
\rho_A \pmod{\mathfrak{m}} = \bar{\rho}.
$$

### Deformationen

Zwei Liftungen $\rho_A$ und $\rho_A'$ heißen **äquivalent**, wenn sie durch Konjugation mit einer Matrix $M \in \ker(\text{GL}_2(A) \to \text{GL}_2(\mathbb{F}_p))$ ineinander überführt werden können:

$$
\rho_A' = M \rho_A M^{-1}, \qquad M \equiv I_2 \pmod{\mathfrak{m}}.
$$

Eine **Deformation** ist eine Äquivalenzklasse von Liftungen. Die Passage von Liftungen zu Deformationen eliminiert die „unwesentlichen" Freiheitsgrade der Basiswahl.

---

## 3. Der universelle Deformationsring $R$

### Mazurs Darstellbarkeitssatz

Das zentrale Ergebnis von **Barry Mazur** (1989) ist:

!!! note "Theorem (Mazur, 1989)"
    Sei $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p)$ eine stetige,
    irreduzible Darstellung. Dann existiert ein **universeller Deformationsring**
    $R$ (ein vollständiger lokaler noetherscher Ring mit Restklassenkörper $\mathbb{F}_p$)
    und eine **universelle Deformation**
    $$
    \rho^{\text{univ}}: G_{\mathbb{Q}} \to \text{GL}_2(R),
    $$
    so dass jede Deformation von $\bar{\rho}$ nach einem Ring $A$ **eindeutig** durch
    einen lokalen Ringhomomorphismus $R \to A$ faktorisiert.

In der Sprache der Kategorientheorie: Der Funktor „Deformationen von $\bar{\rho}$" ist **darstellbar**, und $R$ ist das darstellende Objekt.

### Was bedeutet das konkret?

Der universelle Deformationsring $R$ ist die „größtmögliche" Liftung:

- Jede Deformation von $\bar{\rho}$ nach $\mathbb{Z}_p$ entsteht durch einen Ringhomomorphismus $R \to \mathbb{Z}_p}$ (Spezialisierung der universellen Deformation).
- Die Struktur von $R$ kodiert alle Informationen über alle möglichen Liftungen gleichzeitig.
- $R$ kann als $\mathbb{Z}_p$-Algebra geschrieben werden: $R \cong \mathbb{Z}_p[[x_1, \ldots, x_r]] / (f_1, \ldots, f_s)$ für geeignete $r$ und Relationen $f_i$.

### Analogie

Man kann sich $R$ vorstellen wie den **Koordinatenring einer Moduli-Varietät**: Punkte von $\text{Spec}(R)$ (genauer: $\mathbb{Z}_p$-wertige Punkte) entsprechen Deformationen von $\bar{\rho}$. Die Geometrie von $\text{Spec}(R)$ spiegelt die Struktur des Raums aller Deformationen wider.

---

## 4. Deformationsbedingungen

### Warum Bedingungen nötig sind

Der „nackte" universelle Deformationsring $R$ parametrisiert **alle** Deformationen von $\bar{\rho}$ – ohne jede Einschränkung. Für Wiles' Beweis ist das zu viel: Man braucht Deformationen, die zusätzliche **lokale Bedingungen** erfüllen.

### Lokale Bedingungen bei $q \neq p$

Für jede Primzahl $q \neq p$ kann man fordern, dass die Deformation bei $q$ eine bestimmte Form hat. Die wichtigsten Bedingungen:

- **Unverzweigt**: Die Trägheitsgruppe $I_q$ wirkt trivial. Dies erzwingt man an Stellen guter Reduktion.
- **Steinberg**: Die Darstellung hat bei $q$ eine spezielle Form, die multiplikativer Reduktion entspricht.
- **Minimale Bedingung**: Die Darstellung bei $q$ hat denselben Typ wie $\bar{\rho}$ – keine zusätzliche Verzweigung erlaubt.

### Lokale Bedingungen bei $p$

Bei der Primzahl $p$ selbst gibt es besonders wichtige Bedingungen:

- **Flach (flat)**: Die Darstellung kommt von einem flachen Gruppenschema über $\mathbb{Z}_p$. Dies ist die stärkste Bedingung und entspricht guter Reduktion.
- **Ordinär**: Die Darstellung hat bei $p$ eine obere Dreiecksform mit unramifiziertem Quotienten.
- **Semistabil**: Eine Verallgemeinerung, die multiplikative Reduktion erlaubt.

### Der eingeschränkte Deformationsring $R_{\mathcal{D}}$

Fasst man eine Menge $\mathcal{D}$ lokaler Bedingungen zusammen, so erhält man einen **Quotienten** des universellen Deformationsrings:

$$
R \twoheadrightarrow R_{\mathcal{D}},
$$

der nur diejenigen Deformationen parametrisiert, die die Bedingungen $\mathcal{D}$ erfüllen. Im Folgenden schreiben wir einfach $R$ für den eingeschränkten Ring $R_{\mathcal{D}}$.

---

## 5. Der Hecke-Ring $T$

### Modulare Deformationen

Unter allen Deformationen von $\bar{\rho}$ gibt es eine besondere Teilmenge: die **modularen Deformationen** – solche, die von Neuformen kommen.

Zu jeder Neuform $f$ vom Gewicht 2 und Stufe $N$ gibt es (nach Eichler-Shimura) eine Galois-Darstellung $\rho_f: G_{\mathbb{Q}} \to \text{GL}_2(\mathcal{O}_f)$, wobei $\mathcal{O}_f$ der Koeffizientenring von $f$ ist. Wenn $\bar{\rho}_f \cong \bar{\rho}$, dann ist $\rho_f$ eine Deformation von $\bar{\rho}$.

### Die Hecke-Algebra

Die **Hecke-Algebra** $\mathbb{T}$ wird erzeugt von den Hecke-Operatoren $T_q$ (für Primzahlen $q \nmid N$) und $U_q$ (für $q \mid N$), wirkend auf dem Raum der Spitzenformen $S_2(\Gamma_0(N))$.

Der **lokalisierte Hecke-Ring** $T$ ist der Quotient von $\mathbb{T}$, der die modularen Deformationen von $\bar{\rho}$ parametrisiert:

$$
T = \mathbb{T}_{\mathfrak{m}},
$$

lokalisiert am maximalen Ideal $\mathfrak{m}$, das durch $\bar{\rho}$ bestimmt wird (konkret: $T_q - \text{tr}(\bar{\rho}(\text{Frob}_q)) \in \mathfrak{m}$ für alle $q$).

### Die modulare Deformation

Die Hecke-Algebra $T$ trägt eine **universelle modulare Deformation**:

$$
\rho^{\text{mod}}: G_{\mathbb{Q}} \to \text{GL}_2(T),
$$

die alle modularen Deformationen simultan erfasst.

---

## 6. Die natürliche Surjektion $R \twoheadrightarrow T$

### Warum eine Surjektion existiert

Da jede modulare Deformation insbesondere eine Deformation ist, gibt es (durch die universelle Eigenschaft von $R$) einen **natürlichen Ringhomomorphismus**:

$$
\varphi: R \twoheadrightarrow T.
$$

Dieser Homomorphismus ist **surjektiv**: Die Hecke-Algebra $T$ wird von den Spuren $\text{tr}(\rho^{\text{mod}}(\text{Frob}_q))$ erzeugt, und diese sind Bilder der entsprechenden Spuren der universellen Deformation.

### Was die Surjektion bedeutet

$$
R \twoheadrightarrow T
$$

bedeutet: $T$ ist ein Quotient von $R$. Oder geometrisch: Die „modularen Punkte" bilden eine **abgeschlossene Teilmenge** des Deformationsraums.

Die entscheidende Frage ist: **Ist $\varphi$ ein Isomorphismus?** Also: $R = T$?

---

## 7. Wiles' Ziel: $R = T$

### Was $R = T$ bedeutet

Wenn $R \cong T$ (als Ringe), dann ist jede zulässige Deformation von $\bar{\rho}$ automatisch modular:

$$
R = T \implies \text{jede Deformation von } \bar{\rho} \text{ mit den gegebenen Bedingungen ist modular.}
$$

Insbesondere: Die Darstellung $\rho_{E,p}$ der elliptischen Kurve $E$ ist eine Deformation von $\bar{\rho}$ mit den richtigen lokalen Bedingungen (weil $E$ semistabil ist). Wenn $R = T$, dann ist $\rho_{E,p}$ modular – und damit ist $E$ modular.

### Die Beweisstruktur

$$
\boxed{\bar{\rho} \text{ modular}} \xrightarrow{R = T} \boxed{\rho_{E,p} \text{ modular}} \implies \boxed{E \text{ modular}} \implies \boxed{\text{FLT}}
$$

### Warum $R = T$ schwierig ist

Die Surjektion $R \twoheadrightarrow T$ ist „geschenkt" – sie folgt aus der universellen Eigenschaft. Die Injektivität ist das Schwierige: Man muss zeigen, dass der Kern trivial ist, also dass es **keine** nichtmodularen Deformationen gibt.

Wiles' großer Durchbruch war die Entwicklung eines **numerischen Kriteriums** – einer rein algebraischen Bedingung, die $R = T$ impliziert. Dieses Kriterium und sein Beweis sind Gegenstand des [nächsten Artikels](../05-r-gleich-t/article_de.md).

### Übersicht der Beweismaschinerie

| Objekt | Beschreibung | Parametrisiert |
|--------|-------------|----------------|
| $\bar{\rho}$ | Residuale Darstellung | Ausgangspunkt |
| $R$ | Universeller Deformationsring | Alle zulässigen Deformationen |
| $T$ | Hecke-Algebra | Modulare Deformationen |
| $R \twoheadrightarrow T$ | Natürliche Surjektion | Modulare ⊂ Alle |
| $R = T$ | Isomorphismus | Alle = Modulare |

---

## Ausblick

Die Deformationstheorie liefert den konzeptionellen Rahmen für Wiles' Beweis. Aber das Herzstück ist der Beweis von $R = T$ – eine tiefe algebraische Aussage, die im nächsten Artikel entfaltet wird:

| Artikel | Thema |
|---------|-------|
| [05 – R = T](../05-r-gleich-t/article_de.md) | Das numerische Kriterium, Selmer-Gruppen und der Beweis |
| [06 – Der Taylor-Wiles-Trick](../06-taylor-wiles-trick/article_de.md) | Das Patching-Argument, das die Lücke schloss |

---

## Quellen

- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1.2–1.6
- **Barry Mazur**: *Deforming Galois representations*, in: Galois Groups over $\mathbb{Q}$, MSRI Publications 16 (1989) – Die Grundlegung der Deformationstheorie
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 11 – Deformationsringe und Hecke-Algebren
- **Gebhard Böckle**: *Deformations of Galois representations*, in: Clay Mathematics Proceedings 4 (2005) – Moderne Darstellung
