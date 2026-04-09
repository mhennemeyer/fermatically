---
title: "Galois-Darstellungen"
slug: fermat-wiles/03-galois-darstellungen
series: fermat-wiles
part: 3
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - galois-darstellungen
  - darstellungstheorie
  - modularitaet
requires:
  - abbildungen
  - mengen
  - modulare-arithmetik
---
# Galois-Darstellungen

!!! abstract "Zusammenfassung"
    Galois-Darstellungen übersetzen die Symmetrien algebraischer Gleichungen in
    die Sprache der linearen Algebra: Homomorphismen von Galois-Gruppen in
    Matrizengruppen. Jede elliptische Kurve liefert eine natürliche 2-dimensionale
    Darstellung, und Wiles' Beweis zeigt Modularität auf genau dieser Ebene.

## Voraussetzungen

- [Gruppen und Symmetrie](../werkzeuge/gruppen.md) – Homomorphismen, Normalteiler, Quotientengruppen
- [Ringe und Körper](../werkzeuge/ringe-koerper.md) – Körpererweiterungen, endliche Körper $\mathbb{F}_p$, $p$-adische Zahlen $\mathbb{Z}_p$
- [Galois-Theorie](../werkzeuge/galois-theorie.md) – Galois-Gruppen, Frobenius-Elemente, Verzweigung
- [Elliptische Kurven](../werkzeuge/elliptische-kurven.md) – Gruppenstruktur, Torsionspunkte, Reduktion modulo $p$

| Thema | Beschreibung |
|-------|-------------|
| [Abbildungen (Funktionen)](../vorwissen/abbildungen.md) | $f: A \to B$, injektiv, surjektiv, bijektiv |
| [Mengen und Mengenoperationen](../vorwissen/mengen.md) | Mengennotation, $\cup, \cap, \setminus, \times$ |
| [Modulare Arithmetik](../vorwissen/modulare-arithmetik.md) | Kongruenzen $a \equiv b \pmod{n}$ und Restklassen |

---

## 1. Von Galois-Gruppen zu Matrizen

### Was ist eine Darstellung?

Eine **Darstellung** einer Gruppe $G$ ist ein Homomorphismus

$$
\rho: G \to \text{GL}_n(K),
$$

wobei $\text{GL}_n(K)$ die Gruppe der invertierbaren $n \times n$-Matrizen über einem Körper (oder Ring) $K$ ist. Die Darstellung „übersetzt" die abstrakte Gruppenstruktur in die konkrete Sprache der linearen Algebra.

### Warum Darstellungen?

Galois-Gruppen – insbesondere die absolute Galois-Gruppe $G_{\mathbb{Q}}$ – sind unendlich und hochkomplex. Direkt mit ihnen zu arbeiten ist oft unmöglich. Darstellungen liefern ein handhabbares Werkzeug: Statt die Gruppe selbst zu studieren, studiert man ihre **Wirkung auf Vektorräumen**.

Die zentrale Einsicht von Wiles' Beweis ist: Modularität einer elliptischen Kurve lässt sich als Eigenschaft ihrer Galois-Darstellung formulieren – und auf dieser Ebene beweisen.

---

## 2. Die absolute Galois-Gruppe

### Definition

Die **absolute Galois-Gruppe** von $\mathbb{Q}$ ist

$$
G_{\mathbb{Q}} = \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}),
$$

wobei $\overline{\mathbb{Q}}$ der algebraische Abschluss von $\mathbb{Q}$ ist (die Menge aller algebraischen Zahlen). $G_{\mathbb{Q}}$ besteht aus allen Körperautomorphismen von $\overline{\mathbb{Q}}$, die $\mathbb{Q}$ elementweise festlassen.

### Profinite Struktur

$G_{\mathbb{Q}}$ ist eine **profinite Gruppe** – der inverse Limes aller endlichen Galois-Gruppen $\text{Gal}(K/\mathbb{Q})$:

$$
G_{\mathbb{Q}} = \varprojlim_{K/\mathbb{Q} \text{ endlich, Galois}} \text{Gal}(K/\mathbb{Q}).
$$

Sie ist überabzählbar und trägt eine natürliche Topologie (die Krull-Topologie), unter der sie kompakt und total unzusammenhängend ist. Jedes offene Untergruppe hat endlichen Index.

### Zerlegungsgruppen und Frobenius

Für jede Primzahl $p$ gibt es eine **Zerlegungsgruppe** $D_p \subset G_{\mathbb{Q}}$ und eine **Trägheitsgruppe** $I_p \subset D_p$. Das Frobenius-Element

$$
\text{Frob}_p \in D_p / I_p
$$

ist die „Signatur" der Primzahl $p$ in $G_{\mathbb{Q}}$. Es wirkt auf Reduktionen modulo $p$ wie $x \mapsto x^p$.

Für eine Darstellung $\rho: G_{\mathbb{Q}} \to \text{GL}_n(K)$ kann man die **Spur des Frobenius**

$$
\text{tr}(\rho(\text{Frob}_p))
$$

berechnen – und diese Zahl kodiert die arithmetische Information der Darstellung bei $p$.

---

## 3. $p$-Torsion elliptischer Kurven

### Das Galois-Modul $E[p]$

Sei $E$ eine elliptische Kurve über $\mathbb{Q}$ und $p$ eine Primzahl. Die **$p$-Torsionspunkte** sind:

$$
E[p] = \{P \in E(\overline{\mathbb{Q}}) : pP = \mathcal{O}\},
$$

wobei $\mathcal{O}$ der Punkt im Unendlichen (das Neutralelement der Gruppenstruktur) ist.

Als abelsche Gruppe ist $E[p]$ isomorph zu

$$
E[p] \cong (\mathbb{Z}/p\mathbb{Z})^2.
$$

Es ist ein zweidimensionaler Vektorraum über $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.

### Die Galois-Wirkung

Die Punkte in $E[p]$ haben Koordinaten in $\overline{\mathbb{Q}}$, und die absolute Galois-Gruppe wirkt auf ihnen durch ihre Wirkung auf die Koordinaten:

$$
\sigma(P) = (\sigma(x_P), \sigma(y_P)) \quad \text{für } \sigma \in G_{\mathbb{Q}}.
$$

Diese Wirkung respektiert die Gruppenstruktur: $\sigma(P + Q) = \sigma(P) + \sigma(Q)$. Damit ist $E[p]$ ein **Galois-Modul** – ein $\mathbb{F}_p$-Vektorraum mit einer linearen Wirkung von $G_{\mathbb{Q}}$.

---

## 4. Die residuale Darstellung

### Definition

Wählt man eine Basis $\{P_1, P_2\}$ von $E[p]$ über $\mathbb{F}_p$, so wird die Galois-Wirkung durch eine Matrix beschrieben:

$$
\sigma(P_j) = \sum_i a_{ij}(\sigma) P_i, \qquad (a_{ij}(\sigma)) \in \text{GL}_2(\mathbb{F}_p).
$$

Dies definiert die **residuale Galois-Darstellung**:

$$
\bar{\rho}_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p).
$$

Sie ist ein stetiger Gruppenhomomorphismus (bezüglich der Krull-Topologie auf $G_{\mathbb{Q}}$ und der diskreten Topologie auf $\text{GL}_2(\mathbb{F}_p)$). Bis auf Konjugation ist sie unabhängig von der Basiswahl.

### Irreduzibilität

Die Darstellung $\bar{\rho}_{E,p}$ heißt **irreduzibel**, wenn $E[p]$ keine nichttriviale $G_{\mathbb{Q}}$-invariante Untergruppe hat (d.h. keinen $\mathbb{F}_p$-Untervektorraum, der unter der Galois-Wirkung stabil ist).

Irreduzibilität ist eine entscheidende Voraussetzung für Wiles' Beweis. Für die Frey-Kurve ist $\bar{\rho}_{E,p}$ irreduzibel für $p \geq 5$ – eine Folge von Mazurs bahnbrechender Arbeit über isogene elliptische Kurven.

### Verzweigung und Konduktor

Die Darstellung $\bar{\rho}_{E,p}$ ist **unverzweigt** bei einer Primzahl $q \neq p$, wenn die Trägheitsgruppe $I_q$ trivial auf $E[p]$ wirkt. Dies geschieht genau dann, wenn $E$ gute Reduktion bei $q$ hat.

Der **Artin-Konduktor** $N(\bar{\rho}_{E,p})$ misst die Verzweigung der Darstellung und ist ein Teiler des Konduktors $N_E$ der Kurve.

---

## 5. Die $p$-adische Darstellung

### Der Tate-Modul

Statt nur die $p$-Torsion zu betrachten, kann man alle $p^n$-Torsionspunkte simultan erfassen. Der **Tate-Modul** ist der inverse Limes:

$$
T_p(E) = \varprojlim_{n} E[p^n],
$$

wobei die Übergangsabbildungen die Multiplikation-mit-$p$-Abbildungen $E[p^{n+1}] \to E[p^n]$ sind.

Als $\mathbb{Z}_p$-Modul ist $T_p(E)$ frei vom Rang 2:

$$
T_p(E) \cong \mathbb{Z}_p^2.
$$

### Die $p$-adische Darstellung

Die Galois-Wirkung auf $T_p(E)$ liefert die **$p$-adische Galois-Darstellung**:

$$
\rho_{E,p}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p) \hookrightarrow \text{GL}_2(\mathbb{Q}_p).
$$

Dies ist eine stetige Darstellung bezüglich der $p$-adischen Topologie. Sie ist eine „Liftung" der residualen Darstellung: Reduktion modulo $p$ gibt

$$
\rho_{E,p} \pmod{p} = \bar{\rho}_{E,p}.
$$

### Die Verbindung zu $L$-Reihen

Die $p$-adische Darstellung kodiert die arithmetische Information der Kurve vollständig:

$$
\text{tr}(\rho_{E,p}(\text{Frob}_q)) = a_q(E), \qquad \det(\rho_{E,p}(\text{Frob}_q)) = q,
$$

für jede Primzahl $q$ guter Reduktion (mit $q \neq p$). Damit bestimmt die Darstellung die $L$-Reihe $L(E, s)$ – und umgekehrt.

---

## 6. Modulare Darstellungen

### Darstellungen von Modulformen

Nicht nur elliptische Kurven liefern Galois-Darstellungen – auch **Modulformen** tun dies. Zu jeder Neuform $f$ vom Gewicht 2 und Stufe $N$ konstruierten Eichler und Shimura eine zugehörige Galois-Darstellung:

$$
\rho_f: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{Z}_p),
$$

mit der Eigenschaft

$$
\text{tr}(\rho_f(\text{Frob}_q)) = b_q(f), \qquad \det(\rho_f(\text{Frob}_q)) = q,
$$

wobei $b_q$ der $q$-te Fourier-Koeffizient von $f$ ist.

### Modularität als Darstellungseigenschaft

Jetzt wird die Verbindung klar: Eine elliptische Kurve $E$ ist genau dann **modular**, wenn ihre Galois-Darstellung $\rho_{E,p}$ mit der Darstellung $\rho_f$ einer Neuform $f$ übereinstimmt:

$$
\rho_{E,p} \cong \rho_f \quad \iff \quad a_q(E) = b_q(f) \text{ für alle } q \quad \iff \quad L(E, s) = L(f, s).
$$

Die Modularitätsvermutung (TSV) wird damit zu einer Aussage über Galois-Darstellungen: **Jede Darstellung, die von einer elliptischen Kurve kommt, kommt auch von einer Modulform.**

### Residuale Modularität

Analog heißt $\bar{\rho}_{E,p}$ **modular**, wenn sie isomorph zur Reduktion modulo $p$ einer modularen Darstellung ist:

$$
\bar{\rho}_{E,p} \cong \bar{\rho}_f \pmod{p}
$$

für eine Neuform $f$. Dies ist eine schwächere Bedingung als volle Modularität – und genau der Ausgangspunkt von Wiles' Beweisstrategie.

---

## 7. Wiles' Strategie

### Die zwei Schritte

Wiles' Beweis der Modularität semistabiler elliptischer Kurven zerfällt in zwei große Schritte:

**Schritt 1: Residuale Modularität zeigen.** Man muss beweisen, dass $\bar{\rho}_{E,p}$ modular ist – also von einer Neuform kommt. Für $p = 3$ folgt dies aus einem berühmten Ergebnis von **Langlands und Tunnell**: Da $\text{GL}_2(\mathbb{F}_3)$ auflösbar ist, kann man Langlands' Basis-Wechsel-Techniken (base change) anwenden. Für $p = 5$ nutzt Wiles den sogenannten **3-5-Switch** (siehe [Artikel 07](07-3-5-switch.md)).

**Schritt 2: Von residualer zu voller Modularität „liften".** Dies ist das Herzstück des Beweises: Gegeben, dass $\bar{\rho}_{E,p}$ modular ist, muss man zeigen, dass auch die volle Darstellung $\rho_{E,p}$ modular ist. Dazu führt Wiles die Sprache der **Deformationstheorie** ein (siehe [Artikel 04](04-deformationstheorie.md)).

### Warum Darstellungen der richtige Rahmen sind

Die Umformulierung der TSV in die Sprache der Galois-Darstellungen hat entscheidende Vorteile:

1. **Algebraische Werkzeuge**: Darstellungstheorie, Kohomologie und kommutative Algebra werden anwendbar.
2. **Lokale-globale Prinzipien**: Man kann Darstellungen „lokal" (bei jeder Primzahl) und „global" (über $\mathbb{Q}$) studieren.
3. **Deformationen**: Die residuale Darstellung $\bar{\rho}$ hat einen „Raum aller Liftungen" – den Deformationsraum, der mit algebraischen Methoden analysiert werden kann.
4. **Reduktion**: Man kann Modularität schrittweise beweisen – zuerst residual, dann voll.

Diese Perspektive – Modularität als Eigenschaft von Galois-Darstellungen – war Wiles' entscheidende konzeptionelle Innovation und hat die Zahlentheorie nach 1995 nachhaltig geprägt.

---

## Ausblick

Galois-Darstellungen bilden die Sprache, in der Wiles' Beweis formuliert ist. Die zentrale Frage des nächsten Schritts: Wie lässt sich zeigen, dass eine residuale modulare Darstellung zu einer vollen modularen Darstellung geliftet werden kann?

| Artikel | Thema |
|---------|-------|
| [04 – Deformationstheorie](04-deformationstheorie.md) | Der universelle Deformationsring $R$ und Mazurs Theorie |
| [05 – R = T](05-r-gleich-t.md) | Warum $R = T$ Modularität beweist |

---

## Quellen

- **Andrew Wiles**: *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), §1
- **Nigel Boston**: *The Proof of Fermat's Last Theorem* (2003), Kapitel 10 – Galois-Darstellungen
- **Jean-Pierre Serre**: *Abelian $\ell$-adic representations and elliptic curves*, W.A. Benjamin (1968) – Klassische Referenz für $\ell$-adische Darstellungen
- **Barry Mazur**: *Deforming Galois representations*, in: Galois Groups over $\mathbb{Q}$, MSRI Publications 16 (1989) – Grundlegend für den Deformationsansatz
