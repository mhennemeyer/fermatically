# Abhängigkeitsgraph der Topics

## Legende

- `→` bedeutet „setzt voraus"
- Topics ohne eingehende Pfeile sind Einstiegspunkte
- Die Nummern entsprechen der empfohlenen Lesereihenfolge

## Graph

```
GRUNDLAGEN (keine Voraussetzungen)
──────────────────────────────────

elementare-zahlentheorie/01-was-ist-flt
  └→ elementare-zahlentheorie/02-beweis-n4
      └→ elementare-zahlentheorie/03-primzahlen-reduktion
          └→ elementare-zahlentheorie/04-beweis-n3

gruppen-und-symmetrie/01-gruppen
  (keine Voraussetzungen)


WERKZEUGE (bauen auf Grundlagen auf)
─────────────────────────────────────

gruppen-und-symmetrie/01-gruppen
  └→ ringe-und-koerper/01-ringe-koerper
      ├→ galois-theorie/01-galois-theorie        (+ gruppen)
      ├→ p-adische-zahlen/01-p-adische-zahlen
      ├→ elliptische-kurven/01-elliptische-kurven (+ gruppen)
      └→ modulformen/01-modulformen               (+ gruppen)


DER BEWEIS (Fermat-Wiles)
─────────────────────────

elliptische-kurven + modulformen
  └→ fermat-wiles/01-taniyama-shimura
      └→ fermat-wiles/02-frey-ribet              (+ elliptische-kurven)

gruppen + ringe-koerper + galois-theorie + elliptische-kurven
  └→ fermat-wiles/03-galois-darstellungen

galois-darstellungen + p-adische-zahlen
  └→ fermat-wiles/04-deformationstheorie
      └→ fermat-wiles/05-r-gleich-t
          └→ fermat-wiles/06-taylor-wiles-trick
              └→ fermat-wiles/07-3-5-switch
                  └→ fermat-wiles/08-was-danach-kam
```

## Empfohlene Lesereihenfolge

### Für den kompletten Weg (18 Artikel):

1. Was ist Fermats letzter Satz?
2. Der Beweis für n=4
3. Primzahlen und warum sie reichen
4. Der Beweis für n=3
5. Gruppen – Symmetrie als Sprache
6. Ringe und Körper
7. Galois-Theorie
8. p-adische Zahlen
9. Elliptische Kurven
10. Modulformen
11. Die Taniyama-Shimura-Vermutung
12. Freys Idee und Ribets Theorem
13. Galois-Darstellungen
14. Deformationstheorie
15. R = T – Das Herz des Beweises
16. Der Taylor-Wiles-Trick
17. Der 3-5-Switch und der Abschluss
18. Was danach kam

### Schnelleinstieg (für Leser mit Algebra-Vorkenntnissen):

1. Was ist Fermats letzter Satz? (Kontext)
2. Elliptische Kurven
3. Modulformen
4. Taniyama-Shimura → Frey-Ribet → Galois-Darstellungen → Deformationstheorie → R=T → Taylor-Wiles → 3-5-Switch
