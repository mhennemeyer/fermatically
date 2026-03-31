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
  - gruppen-und-symmetrie/01-gruppen
  - ringe-und-koerper/01-ringe-koerper
---

# Galois-Theorie

!!! abstract "Zusammenfassung"
    Évariste Galois entdeckte mit 19 Jahren, dass die Lösbarkeit einer Gleichung durch
    die Symmetrien ihrer Nullstellen bestimmt wird. Seine Theorie verbindet Körpererweiterungen
    mit Gruppen – und liefert den konzeptuellen Rahmen für Wiles' Beweis.

## Voraussetzungen

- [Gruppen – Symmetrie als Sprache der Mathematik](../../gruppen-und-symmetrie/01-gruppen/article_de.md)
- [Ringe und Körper](../../ringe-und-koerper/01-ringe-koerper/article_de.md)

---

## 1. Das Problem der Lösungsformeln

Jeder kennt die **Lösungsformel für quadratische Gleichungen**:

$$
x^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4c}}{2}
$$

Die Nullstellen lassen sich durch die Koeffizienten ausdrücken – mithilfe von Addition, Subtraktion, Multiplikation, Division und Wurzelziehen.

Für Gleichungen dritten und vierten Grades gibt es ebenfalls (kompliziertere) Lösungsformeln, die Cardano (1545) und Ferrari entdeckten. Natürlich stellt sich die Frage: Gibt es auch für Grad $5$ und höher solche Formeln?

Die Antwort ist **nein** – und die Begründung führt direkt zur Galois-Theorie.

## 2. Abels Unmöglichkeitsbeweis

**Niels Henrik Abel** bewies 1824, dass es **keine** allgemeine Lösungsformel für Polynome vom Grad $\geq 5$ in Radikalen gibt. Das heißt: Es gibt Polynome fünften Grades, deren Nullstellen sich nicht durch endlich viele Wurzeln aus den Koeffizienten ausdrücken lassen.

Abels Beweis war ein Meilenstein, ließ aber eine entscheidende Frage offen: **Welche** Polynome lassen sich durch Radikale lösen und welche nicht? Ein konkretes Polynom fünften Grades kann durchaus eine Lösung in Radikalen haben – etwa $x^5 - 2 = 0$ mit $x = \sqrt[5]{2}$. Abels Theorem sagt nur, dass es kein *allgemeines* Verfahren gibt.

## 3. Galois' Idee

**Évariste Galois** (1811–1832) löste dieses Problem vollständig – mit einer Idee, die ihrer Zeit um Jahrzehnte voraus war. Er starb mit 20 Jahren bei einem Duell; in der Nacht davor schrieb er seine mathematischen Erkenntnisse fieberhaft nieder.

Galois' zentrale Einsicht: **Die Lösbarkeit einer Gleichung wird durch die Symmetrien ihrer Nullstellen bestimmt.**

Betrachte ein Polynom $f \in \mathbb{Q}[x]$ mit Nullstellen $\alpha_1, \ldots, \alpha_n \in \overline{\mathbb{Q}}$. Der **Zerfällungskörper** ist der kleinste Körper, der $\mathbb{Q}$ und alle Nullstellen enthält:

$$
L = \mathbb{Q}(\alpha_1, \ldots, \alpha_n)
$$

Eine **Symmetrie** dieses Körpers ist ein Automorphismus $\sigma: L \to L$, der $\mathbb{Q}$ elementweise festhält. Jeder solche Automorphismus permutiert die Nullstellen $\alpha_1, \ldots, \alpha_n$ – denn er muss die Gleichung $f(\alpha_i) = 0$ erhalten.

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

Die Galois-Gruppe ist $\text{Gal}(L/\mathbb{Q}) \cong S_3$ – die symmetrische Gruppe auf $3$ Elementen. Das liegt daran, dass die Automorphismen die drei Nullstellen beliebig permutieren können (unter der Einschränkung, dass $\omega \mapsto \omega$ oder $\omega \mapsto \omega^2$).

### Beispiel: Kreisteilungskörper

Der $p$-te Kreisteilungskörper $\mathbb{Q}(\zeta_p)$ (mit $\zeta_p = e^{2\pi i/p}$) hat die Galois-Gruppe:

$$
\text{Gal}(\mathbb{Q}(\zeta_p)/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^*
$$

Das ist die Gruppe der Einheiten modulo $p$ – eine abelsche Gruppe der Ordnung $p - 1$. Jeder Automorphismus $\sigma_a$ sendet $\zeta_p \mapsto \zeta_p^a$ für ein $a \in \{1, \ldots, p-1\}$.

## 5. Der Hauptsatz der Galois-Theorie

Der **Hauptsatz** ist das Herzstück der Theorie. Er stellt eine perfekte Korrespondenz zwischen der algebraischen Struktur der Körpererweiterung und der Gruppenstruktur der Galois-Gruppe her.

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

Galois' ursprüngliche Frage war: Wann lässt sich eine Gleichung durch Radikale lösen? Der Hauptsatz liefert die Antwort.

**Definition.** Eine Gruppe $G$ heißt **auflösbar**, wenn sie eine Kette von Untergruppen besitzt:

$$
\{e\} = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_n = G
$$

wobei jeder Faktor $G_{i+1}/G_i$ abelsch (zyklisch von Primordnung) ist.

**Satz (Galois).** Ein Polynom $f \in K[x]$ ist genau dann durch Radikale auflösbar, wenn seine Galois-Gruppe auflösbar ist.

**Konsequenz für Grad $\geq 5$:** Die symmetrische Gruppe $S_n$ ist für $n \geq 5$ **nicht** auflösbar (weil die alternierende Gruppe $A_n$ für $n \geq 5$ einfach und nicht abelsch ist). Da es Polynome mit Galois-Gruppe $S_5$ gibt, sind diese nicht durch Radikale auflösbar.

**Konsequenz für Grad $\leq 4$:** Die Gruppen $S_1, S_2, S_3, S_4$ sind alle auflösbar – daher existieren Lösungsformeln für Polynome bis Grad $4$.

## 7. Die absolute Galois-Gruppe

Für die Zahlentheorie – und insbesondere für Wiles' Beweis – ist nicht die Galois-Gruppe einer einzelnen Erweiterung entscheidend, sondern die **absolute Galois-Gruppe**:

$$
G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})
$$

Dies ist die Galois-Gruppe der Erweiterung aller algebraischen Zahlen über $\mathbb{Q}$. Sie ist eine unendliche, proendliche Gruppe – der projektive Limes aller endlichen Galois-Gruppen $\text{Gal}(L/\mathbb{Q})$.

$G_{\mathbb{Q}}$ ist eines der geheimnisvollsten Objekte der Mathematik. Trotz intensiver Forschung ist ihre vollständige Struktur unbekannt. Was wir kennen, sind ihre **Darstellungen** – Homomorphismen von $G_{\mathbb{Q}}$ in Matrizengruppen.

### Galois-Darstellungen

Eine **(stetige) Galois-Darstellung** ist ein Homomorphismus:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)
$$

für einen geeigneten Körper oder Ring $K$. Für Wiles' Beweis sind die **zweidimensionalen** Darstellungen ($n = 2$) zentral:

$$
\rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p) \quad \text{oder} \quad \rho: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p)
$$

Jede elliptische Kurve $E$ über $\mathbb{Q}$ liefert solche Darstellungen – über die Wirkung von $G_{\mathbb{Q}}$ auf den $p$-Teilungspunkten $E[p]$. Und jede Modulform liefert ebenfalls eine Galois-Darstellung. Die **Taniyama-Shimura-Vermutung** besagt im Kern: Die Darstellung der elliptischen Kurve *ist* die Darstellung einer Modulform.

### Lokale Galois-Gruppen

Für jede Primzahl $p$ gibt es eine **lokale Galois-Gruppe** $G_{\mathbb{Q}_p} = \text{Gal}(\overline{\mathbb{Q}_p}/\mathbb{Q}_p)$. Sie kontrolliert das Verhalten algebraischer Objekte „an der Stelle $p$". Jede globale Darstellung $\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)$ induziert durch Einschränkung lokale Darstellungen:

$$
\rho|_{G_{\mathbb{Q}_p}}: G_{\mathbb{Q}_p} \to \text{GL}_n(K)
$$

Das **Lokal-Global-Prinzip** fragt: Wann bestimmen die lokalen Darstellungen die globale? Diese Frage steht im Zentrum von Wiles' Beweis.

---

## Weiterführende Quellen

- **Nigel Boston**: *The Proof of Fermat's Last Theorem*, Kap. 4
- **Ian Stewart**: *Galois Theory* – zugängliche Einführung
- **Emil Artin**: *Galois Theory* – der klassische Zugang
