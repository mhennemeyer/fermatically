---
title: "Was danach kam"
slug: fermat-wiles/08-was-danach-kam
series: fermat-wiles
part: 8
date: 2026-03-30
status: draft
lang: de
category: zahlentheorie
tags:
  - bcdt
  - langlands-programm
  - ausblick
requires:
  - fermat-wiles/07-3-5-switch
---
# Was danach kam

!!! abstract "Zusammenfassung"
    Wiles' Beweis war nicht das Ende, sondern ein Anfang. Innerhalb von
    sechs Jahren verallgemeinerten Breuil, Conrad, Diamond und Taylor
    das Ergebnis auf alle elliptischen Kurven. Serres Vermutung wurde 2009
    bewiesen. Das Langlands-Programm – die natürliche Verallgemeinerung
    der Taniyama-Shimura-Vermutung – bleibt die große Vision der
    modernen Zahlentheorie.

## Voraussetzungen

- [Der 3-5-Switch und der Abschluss](../07-3-5-switch/article_de.md) – Der vollständige Beweis von FLT

---

## 1. Von semistabil zu allgemein

### Die offene Frage

Wiles bewies 1995 die Modularität **semistabiler** elliptischer Kurven über $\mathbb{Q}$. Die vollständige Taniyama-Shimura-Vermutung – Modularität **aller** elliptischen Kurven – blieb zunächst offen.

### Der Weg zur Verallgemeinerung

Nach Wiles' Durchbruch wandten sich mehrere Mathematiker der Verallgemeinerung zu. Die Methoden waren im Kern dieselben (Deformationstheorie, Taylor-Wiles-Patching), aber die technischen Schwierigkeiten bei nicht-semistabilen Kurven – insbesondere bei Kurven mit **additiver Reduktion** – erforderten neue Ideen.

Wichtige Zwischenschritte:

- **Fred Diamond (1996)**: Erweiterte den Beweis auf einen größeren Bereich von Deformationsbedingungen und vereinfachte die Taylor-Wiles-Konstruktion wesentlich.
- **Conrad, Diamond, Taylor (1999)**: Behandelten viele der verbleibenden Fälle, insbesondere Kurven mit additiver Reduktion bei kleinen Primzahlen.

### BCDT (2001)

!!! note "Theorem (Breuil-Conrad-Diamond-Taylor, 2001)"
    **Jede** elliptische Kurve über $\mathbb{Q}$ ist modular.

Christophe **Breuil** lieferte den entscheidenden letzten Baustein: die Behandlung der Fälle mit additiver Reduktion bei $p = 3$. Sein Werkzeug war die Theorie der **Breuil-Module** (endliche flache Gruppenschemata), die eine feinere Kontrolle der lokalen Deformationsbedingungen ermöglichte.

Der Beweis erschien in der Zeitschrift *Journal of the AMS* und schloss das Kapitel, das Taniyama 1955 eröffnet hatte.

### Die vollständige Modularitätsvermutung

Mit BCDT wurde die Taniyama-Shimura-Vermutung zum **Modularitätssatz** (Modularity Theorem):

$$
\boxed{\text{Jede elliptische Kurve } E/\mathbb{Q} \text{ ist modular.}}
$$

Dies hat weitreichende Konsequenzen: Für **jede** elliptische Kurve über $\mathbb{Q}$ gilt die analytische Fortsetzung und Funktionalgleichung der $L$-Reihe, und die Birch-Swinnerton-Dyer-Vermutung wird zugänglich.

---

## 2. Serres Vermutung

### Die Vermutung

Jean-Pierre Serre formulierte 1987 eine viel allgemeinere Vermutung als die $\varepsilon$-Vermutung, die Ribet für die Frey-Kurve bewiesen hatte:

!!! note "Serres Vermutung (1987)"
    Jede stetige, ungerade, irreduzible Darstellung
    $\bar{\rho}: G_{\mathbb{Q}} \to \text{GL}_2(\mathbb{F}_p)$
    ist modular – und Serre spezifiziert explizit das minimale Gewicht $k(\bar{\rho})$
    und die minimale Stufe $N(\bar{\rho})$ der zugehörigen Modulform.

Diese Vermutung verallgemeinert die Taniyama-Shimura-Vermutung drastisch: Nicht nur Darstellungen, die von elliptischen Kurven kommen, sondern **alle** 2-dimensionalen Darstellungen über endlichen Körpern sollen modular sein.

### Der Beweis (2009)

**Chandrashekhar Khare** und **Jean-Pierre Wintenberger** bewiesen Serres Vermutung in einer Serie von Arbeiten (2006–2009). Ihr Beweis nutzt:

- Taylor-Wiles-Patching (in verallgemeinerter Form)
- Kisin's Ergebnisse über Deformationsringe
- Potentielle Modularitätsresultate von Taylor
- Eine ingeniöse induktive Strategie über Gewicht und Stufe

Khare erhielt 2011 die Cole-Preis der AMS für dieses Ergebnis.

### Konsequenzen

Serres Vermutung hat bemerkenswerte Folgerungen:

1. **Fontaine-Mazur-Vermutung** (Spezialfall): Jede geometrische $p$-adische Darstellung, die modulo $p$ irreduzibel ist, kommt von einer Modulform.
2. **Artins Vermutung** (für 2-dimensionale Darstellungen): Die $L$-Reihe jeder irreduziblen 2-dimensionalen Artin-Darstellung hat eine analytische Fortsetzung.

---

## 3. Das Langlands-Programm

### Die große Vision

Das **Langlands-Programm**, formuliert von Robert Langlands ab 1967, ist die natürliche Verallgemeinerung der Ideen hinter der Taniyama-Shimura-Vermutung. Es postuliert eine systematische Korrespondenz zwischen:

- **Galois-Darstellungen** (Zahlentheorie/algebraische Geometrie)
- **Automorphen Formen** (Analysis/Darstellungstheorie)

Die TSV und der Modularitätssatz sind ein Spezialfall: 2-dimensionale Darstellungen über $\mathbb{Q}$ ↔ Modulformen vom Gewicht 2.

### Die Langlands-Korrespondenz

In voller Allgemeinheit postuliert das Langlands-Programm für jeden Zahlkörper $F$ und jede reduktive Gruppe $G$:

$$
\left\{\begin{array}{c} n\text{-dimensionale} \\ \text{Galois-Darstellungen} \\ \text{von } G_F \end{array}\right\} \longleftrightarrow \left\{\begin{array}{c} \text{Automorphe} \\ \text{Darstellungen} \\ \text{von } G(\mathbb{A}_F) \end{array}\right\}
$$

wobei $\mathbb{A}_F$ der Adèle-Ring von $F$ ist.

### Fortschritte nach Wiles

Wiles' Methoden und der Taylor-Wiles-Trick haben eine Welle von Ergebnissen ausgelöst:

| Jahr | Resultat | Autoren |
|------|----------|---------|
| 2001 | Modularität aller ell. Kurven / $\mathbb{Q}$ | BCDT |
| 2006 | Sato-Tate-Vermutung (viele Fälle) | Taylor, Clozel, Harris, Shepherd-Barron |
| 2009 | Serres Vermutung | Khare-Wintenberger |
| 2013 | Potentielle Automorphie in höheren Dimensionen | Barnet-Lamb, Geraghty, Harris, Taylor |
| 2018 | Symmetrische Potenzen (alle) | Newton-Thorne |
| 2022 | Modularität abelscher Flächen | Boxer-Calegari-Gee-Pilloni |

### Was offen bleibt

Trotz enormer Fortschritte bleibt das Langlands-Programm weitgehend offen:

- **Funktorialität**: Die allgemeine Langlands-Funktorialität ist unbewiesen.
- **Über Totalreelle Körper hinaus**: Für allgemeine Zahlkörper fehlen fundamentale Werkzeuge.
- **Geometrisches Langlands-Programm**: Die Analogie über Funktionenkörpern (Kurven über endlichen Körpern) ist weiter fortgeschritten (Fargues-Scholze, 2021).
- **$p$-adisches Langlands-Programm**: Eine $p$-adische Variante, initiiert von Breuil und Colmez.

---

## 4. Formale Verifikation

### Die Frage

Wiles' Beweis umfasst über 100 Seiten dichter Mathematik und stützt sich auf Hunderte Seiten vorheriger Arbeiten. Kann man einen solchen Beweis **formal verifizieren** – also maschinenprüfbar in einem Beweisassistenten (Lean, Coq, Isabelle) formalisieren?

### Der aktuelle Stand

Eine vollständige Formalisierung von Wiles' Beweis existiert noch nicht (Stand 2026). Die Hindernisse sind erheblich:

1. **Umfang**: Der Beweis setzt algebraische Geometrie, Darstellungstheorie, $p$-adische Hodge-Theorie und die Theorie der Modulformen voraus – Gebiete, die in keinem Beweisassistenten vollständig formalisiert sind.
2. **Technische Tiefe**: Selbst einzelne Bestandteile (z.B. die Theorie der Hecke-Algebren oder Mazurs Deformationstheorie) erfordern Jahre der Formalisierung.
3. **Community-Kapazität**: Die Zahl der Mathematiker, die sowohl den Beweis als auch formale Verifikation beherrschen, ist sehr klein.

### Verwandte Erfolge

Dennoch gibt es beeindruckende Fortschritte in der formalen Verifikation großer Beweise:

- **Vier-Farben-Satz** (Gonthier, 2005): Vollständig in Coq formalisiert.
- **Kepler-Vermutung** (Hales/Flyspeck, 2014): Vollständig in HOL Light/Isabelle.
- **Flüssige Vektorraumtheorie** (Scholze, 2022): Zentrales Lemma in Lean formalisiert – ein Test für fortgeschrittene Mathematik.
- **FLT für reguläre Primzahlen** (Lean/Mathlib, 2024): Kummers Beweis für reguläre Primzahlen wurde formalisiert – ein erster Schritt Richtung FLT.

Eine vollständige Formalisierung von Wiles' Beweis wäre ein Meilenstein für die formale Mathematik – aber realistisch ist sie noch Jahre, wenn nicht Jahrzehnte entfernt.

---

## 5. FLT und der Schulunterricht

### Die Kluft

Fermats letzter Satz hat eine einzigartige Eigenschaft: Die **Aussage** ist für jeden Schüler verständlich ($x^n + y^n = z^n$ hat keine ganzzahlige Lösung für $n \geq 3$), aber der **Beweis** verwendet Mathematik, die selbst in einem Masterstudium kaum vollständig abgedeckt wird.

### Was man verstehen kann

Ohne die Beweisdetails kann man dennoch die **Struktur** des Beweises vermitteln:

1. Die Grundidee des Widerspruchsbeweises (Frey-Kurve)
2. Die Rolle der Modularität als Brücke zwischen verschiedenen mathematischen Welten
3. Die historische Entwicklung – von Fermat über Euler und Kummer bis Wiles
4. Die menschliche Geschichte – sieben Jahre Geheimarbeit, die Lücke, die Rettung

Diese Artikelserie versucht genau das: den Beweis auf einem Niveau darzustellen, das mathematische Reife voraussetzt, aber keine Forschungsexpertise.

---

## 6. Offene Fragen

### Rund um FLT

- **ABC-Vermutung**: Mochizukis beanspruchter Beweis (2012) ist umstritten. Wenn bestätigt, würde er einen völlig anderen Beweis von FLT liefern (für hinreichend große $n$).
- **Effektive Schranken**: Kann man die Konstanten in Faltings' Satz oder verwandten Ergebnissen explizit machen?
- **Verallgemeinerungen**: Für welche anderen Diophantischen Gleichungen funktioniert die modulare Methode? (Beispiel: Fermats Gleichung über Zahlkörpern.)

### In der Zahlentheorie allgemein

- **Birch-Swinnerton-Dyer-Vermutung**: Eines der Clay-Millennium-Probleme. Der Modularitätssatz macht die analytische Seite zugänglich, aber der Beweis steht aus.
- **Riemann-Hypothese**: Das tiefste offene Problem der Mathematik – verbunden mit $L$-Reihen, aber mit ganz anderen Methoden.
- **Langlands-Programm**: Das große Vereinheitlichungsprojekt der Zahlentheorie – weit offen in seiner vollen Allgemeinheit.

---

## 7. Epilog

### Ein Beweis und seine Folgen

Andrew Wiles' Beweis von Fermats letztem Satz war mehr als die Lösung eines 358 Jahre alten Problems. Er demonstrierte die **Einheit der Mathematik**: Eine Frage aus der elementaren Zahlentheorie wurde durch Werkzeuge aus der algebraischen Geometrie, der komplexen Analysis und der Darstellungstheorie beantwortet.

Die Methoden, die Wiles und Taylor entwickelten – insbesondere das Taylor-Wiles-Patching –, sind heute Standardwerkzeuge der algebraischen Zahlentheorie. Die Vision, die Taniyama 1955 andeutete – eine tiefe Verbindung zwischen scheinbar getrennten mathematischen Welten –, hat sich als prophetisch erwiesen und bildet den Kern des Langlands-Programms.

### Fermats Randnotiz, revisited

Fermat schrieb 1637:

> *„Ich habe hierfür einen wahrhaft wunderbaren Beweis entdeckt, den dieser Rand nicht fassen kann."*

358 Jahre später wissen wir: Der Rand hätte Fermats Beweis wahrscheinlich gar nicht fassen **müssen** – denn Fermat konnte die Werkzeuge, die für den Beweis nötig sind, nicht kennen. Modulformen wurden erst im 19. Jahrhundert entwickelt, Galois-Darstellungen im 20., und Deformationstheorie erst 1989.

Ob Fermat tatsächlich einen Beweis hatte (möglicherweise nur für $n = 4$, den er ja bewiesen hat), wird für immer ein Geheimnis bleiben. Was bleibt, ist der Beweis von Wiles – und die Erkenntnis, dass die tiefsten Fragen der Mathematik oft die überraschendsten Antworten finden.

---

## Quellen

- **Christophe Breuil, Brian Conrad, Fred Diamond, Richard Taylor**: *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises*, Journal of the AMS 14 (2001), 843–939
- **Chandrashekhar Khare, Jean-Pierre Wintenberger**: *Serre's modularity conjecture (I) und (II)*, Inventiones Mathematicae 178 (2009)
- **Robert Langlands**: *Problems in the theory of automorphic forms*, Lectures in Modern Analysis and Applications III, Springer (1970)
- **Peter Scholze, Dustin Clausen**: *Condensed Mathematics and Analytic Geometry*, Vorlesungsnotizen (2019–2022)
- **Kevin Buzzard**: *The Xena Project*, Formalisierung von Mathematik in Lean
- **Simon Singh**: *Fermats letzter Satz*, dtv (1998)
- **Andrew Wiles**: Abel-Preis-Vortrag, Oslo (2016) – Rückblick auf den Beweis und seine Folgen
