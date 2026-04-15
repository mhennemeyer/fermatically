---
title: "Galois-Theorie – Warum Gleichungen keine Lösungsformeln haben"
slug: galois-theorie/01-galois-theorie
series: galois-theorie
part: 1
date: 2026-03-30
status: draft
lang: de
category: algebra
tags:
  - galois
  - koerpererweiterungen
  - symmetrie
requires:
  - potenzen-polynome
  - abbildungen
  - komplexe-zahlen
  - zahlenbereiche
---

# Galois-Theorie

!!! abstract "Zusammenfassung"
    Die Lösbarkeit einer Polynomgleichung wird durch die Symmetrien ihrer Nullstellen bestimmt.
    Galois' Theorie verbindet Körpererweiterungen mit Gruppen – konzeptueller Rahmen für Wiles' Beweis.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](gruppen.md)
- [Ringe und Körper](ringe-koerper.md)

| Thema | Beschreibung |
|-------|-------------|
| [Potenzen und Polynome](../vorwissen/potenzen-polynome.md) | Potenzschreibweise $a^n$ und Polynomrechnung |
| [Abbildungen (Funktionen)](../vorwissen/abbildungen.md) | $f: A \to B$, injektiv, surjektiv, bijektiv |
| [Komplexe Zahlen](../vorwissen/komplexe-zahlen.md) | Zahlen $a + bi$ mit $i^2 = -1$, Polarform, Einheitswurzeln |
| [Zahlenbereiche](../vorwissen/zahlenbereiche.md) | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ und ihre Beziehungen |

---

## 1. Das Problem der Lösungsformeln

Die **Lösungsformel für quadratische Gleichungen** ist allgemein bekannt:

$$
x^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4c}}{2}
$$

Die Nullstellen lassen sich durch die Koeffizienten ausdrücken – mithilfe von Addition, Subtraktion, Multiplikation, Division und Wurzelziehen.

Für Gleichungen dritten und vierten Grades existieren ebenfalls (kompliziertere) Lösungsformeln, entdeckt von Cardano (1545) und Ferrari. Die Frage: Gibt es auch für Grad $5$ und höher solche Formeln?

Die Antwort ist **nein** – und die Begründung führt direkt zur Galois-Theorie.

## 2. Abels Unmöglichkeitsbeweis

**Niels Henrik Abel** bewies 1824, dass **keine** allgemeine Lösungsformel für Polynome vom Grad $\geq 5$ in Radikalen existiert. Es gibt Polynome fünften Grades, deren Nullstellen sich nicht durch endlich viele Wurzeln aus den Koeffizienten ausdrücken lassen.

Abels Beweis ließ eine entscheidende Frage offen: **Welche** Polynome lassen sich durch Radikale lösen und welche nicht? Ein konkretes Polynom fünften Grades kann durchaus eine Lösung in Radikalen haben – etwa $x^5 - 2 = 0$ mit $x = \sqrt[5]{2}$. Abels Theorem besagt nur, dass kein *allgemeines* Verfahren existiert.

## 3. Galois' Einsicht

**Évariste Galois** (1811–1832) löste dieses Problem vollständig. Seine zentrale Einsicht: **Die Lösbarkeit einer Gleichung wird durch die Symmetrien ihrer Nullstellen bestimmt.**

> „Since the beginning of this century, computational procedures have become so complicated that any progress by those means has become impossible."
> — Évariste Galois, Vorwort zum Mémoire (1831)

Gegeben ein Polynom $f \in \mathbb{Q}[x]$ mit Nullstellen $\alpha_1, \ldots, \alpha_n \in \overline{\mathbb{Q}}$. Der **Zerfällungskörper** ist der kleinste Körper, der $\mathbb{Q}$ und alle Nullstellen enthält:

$$
L = \mathbb{Q}(\alpha_1, \ldots, \alpha_n)
$$

Eine **Symmetrie** dieses Körpers ist ein Automorphismus $\sigma: L \to L$, der $\mathbb{Q}$ elementweise festhält. Jeder solche Automorphismus permutiert die Nullstellen $\alpha_1, \ldots, \alpha_n$ – er muss die Gleichung $f(\alpha_i) = 0$ erhalten.

## 4. Die Galois-Gruppe

Die **Galois-Gruppe** einer Körpererweiterung $L/K$ ist die Gruppe aller $K$-Automorphismen von $L$:

$$
\text{Gal}(L/K) = \{\sigma: L \to L \mid \sigma \text{ ist Automorphismus mit } \sigma|_K = \text{id}\}
$$

Die Verknüpfung ist die Komposition von Abbildungen.

### Beispiel: $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$

Die Erweiterung $\mathbb{Q}(\sqrt{2}) = \{a + b\sqrt{2} \mid a, b \in \mathbb{Q}\}$ hat Grad $2$. Die einzigen $\mathbb{Q}$-Automorphismen sind:

- $\text{id}: \sqrt{2} \mapsto \sqrt{2}$
- $\sigma: \sqrt{2} \mapsto -\sqrt{2}$

Also $\text{Gal}(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}$.

### Beispiel: Zerfällungskörper von $x^3 - 2$

Die Nullstellen von $x^3 - 2$ sind $\sqrt[3]{2}$, $\omega\sqrt[3]{2}$ und $\omega^2\sqrt[3]{2}$ (mit $\omega = e^{2\pi i/3}$). Der Zerfällungskörper ist $L = \mathbb{Q}(\sqrt[3]{2}, \omega)$ mit $[L:\mathbb{Q}] = 6$.

Die Galois-Gruppe ist $\text{Gal}(L/\mathbb{Q}) \cong S_3$ – die symmetrische Gruppe auf $3$ Elementen. Die Automorphismen permutieren die drei Nullstellen (unter der Einschränkung, dass $\omega \mapsto \omega$ oder $\omega \mapsto \omega^2$).

### Beispiel: Kreisteilungskörper

Der $p$-te Kreisteilungskörper $\mathbb{Q}(\zeta_p)$ (mit $\zeta_p = e^{2\pi i/p}$) hat die Galois-Gruppe:

$$
\text{Gal}(\mathbb{Q}(\zeta_p)/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^*
$$

Die Gruppe der Einheiten modulo $p$ – abelsch, der Ordnung $p - 1$. Jeder Automorphismus $\sigma_a$ sendet $\zeta_p \mapsto \zeta_p^a$ für ein $a \in \{1, \ldots, p-1\}$.

## 5. Der Hauptsatz der Galois-Theorie

Der **Hauptsatz** stellt eine Bijektion zwischen der algebraischen Struktur der Körpererweiterung und der Gruppenstruktur der Galois-Gruppe her.

**Satz (Galois-Korrespondenz).** Sei $L/K$ eine endliche Galois-Erweiterung mit Galois-Gruppe $G = \text{Gal}(L/K)$. Dann gibt es eine inklusionsumkehrende Bijektion:

$$
\{\text{Zwischenkörper } K \subseteq M \subseteq L\} \longleftrightarrow \{\text{Untergruppen } H \leq G\}
$$

gegeben durch:

$$
M \longmapsto \text{Gal}(L/M), \qquad H \longmapsto L^H = \{x \in L \mid \sigma(x) = x \text{ für alle } \sigma \in H\}
$$

Dabei gilt:
- $[M : K] = [G : H]$ (Index der Untergruppe = Grad der Erweiterung)
- $M/K$ ist genau dann eine Galois-Erweiterung, wenn $H \trianglelefteq G$ (Normalteiler)
- In diesem Fall ist $\text{Gal}(M/K) \cong G/H$

!!! tip "Die Korrespondenz visualisiert"
    ```
    Körper                  Gruppen
    L                       {e}
    |                        |
    M₂                     H₂
    |    \                 /    |
    M₁     M₃          H₁    H₃
    |    /                 \    |
    K                       G
    ```
    Größere Körper entsprechen *kleineren* Untergruppen (und umgekehrt).

## 6. Auflösbarkeit

Galois' ursprüngliche Frage: Wann lässt sich eine Gleichung durch Radikale lösen? Der Hauptsatz liefert die Antwort.

**Definition.** Eine Gruppe $G$ heißt **auflösbar**, wenn eine Kette von Untergruppen existiert:

$$
\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G
$$

wobei jeder Faktor $G_{i+1}/G_i$ abelsch (zyklisch von Primordnung) ist.

**Satz (Galois).** Ein Polynom $f \in K[x]$ ist genau dann durch Radikale auflösbar, wenn seine Galois-Gruppe auflösbar ist.

**Konsequenz für Grad $\geq 5$:** Die symmetrische Gruppe $S_n$ ist für $n \geq 5$ **nicht** auflösbar (weil die alternierende Gruppe $A_n$ für $n \geq 5$ einfach und nicht abelsch ist). Da Polynome mit Galois-Gruppe $S_5$ existieren, sind diese nicht durch Radikale auflösbar.

**Konsequenz für Grad $\leq 4$:** Die Gruppen $S_1, S_2, S_3, S_4$ sind alle auflösbar – daher existieren Lösungsformeln für Polynome bis Grad $4$.

## 7. Die absolute Galois-Gruppe

Für die Zahlentheorie – und insbesondere für Wiles' Beweis – ist nicht die Galois-Gruppe einer einzelnen Erweiterung entscheidend, sondern die **absolute Galois-Gruppe**:

$$
G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})
$$

Die Galois-Gruppe der Erweiterung aller algebraischen Zahlen über $\mathbb{Q}$. Sie ist eine unendliche, proendliche Gruppe – der projektive Limes aller endlichen Galois-Gruppen $\text{Gal}(L/\mathbb{Q})$.

$G_{\mathbb{Q}}$ zählt zu den am intensivsten untersuchten und zugleich am wenigsten verstandenen Objekten der Mathematik. Bekannt sind vor allem ihre **Darstellungen** – Homomorphismen von $G_{\mathbb{Q}}$ in Matrizengruppen.

> „The Galois group of the algebraic closure of the rationals is an extraordinarily rich and mysterious group."
> — Barry Mazur, *Number Theory as Gadfly*, The American Mathematical Monthly 98 (1991)

### Galois-Darstellungen

Eine **(stetige) Galois-Darstellung** ist ein Homomorphismus:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)
$$

für einen geeigneten Körper oder Ring $K$. Für Wiles' Beweis sind die **zweidimensionalen** Darstellungen ($n = 2$) zentral:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p) \quad \text{oder} \quad \rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p)
$$

Jede elliptische Kurve $E$ über $\mathbb{Q}$ liefert solche Darstellungen – über die Wirkung von $G_{\mathbb{Q}}$ auf den $p$-Teilungspunkten $E[p]$. Ebenso liefert jede Modulform eine Galois-Darstellung. Die **Taniyama-Shimura-Vermutung** besagt im Kern: Die Darstellung der elliptischen Kurve *ist* die Darstellung einer Modulform.

### Lokale Galois-Gruppen

Für jede Primzahl $p$ gibt es eine **lokale Galois-Gruppe** $G_{\mathbb{Q}_p} = \text{Gal}(\overline{\mathbb{Q}_p}/\mathbb{Q}_p)$. Sie kontrolliert das Verhalten algebraischer Objekte „an der Stelle $p$". Jede globale Darstellung $\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)$ induziert durch Einschränkung lokale Darstellungen:

$$
\rho|_{G_{\mathbb{Q}_p}}: G_{\mathbb{Q}_p} \to \text{GL}_n(K)
$$

Das **Lokal-Global-Prinzip**: Wann bestimmen die lokalen Darstellungen die globale? Diese Frage steht im Zentrum von Wiles' Beweis.

---

## Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 4
- **Ian Stewart**: *Galois Theory*, Chapman & Hall (2003)
- **Emil Artin**: *Galois Theory*, Dover (1998)
- **Barry Mazur**: *Number Theory as Gadfly*, The American Mathematical Monthly 98 (1991), 593–610
