#!/bin/bash
# Kopiert alle englischen Artikel aus topics/ nach docs/ als .en.md-Dateien
set -e
cd "$(dirname "$0")/.."

# Elementare Zahlentheorie (4)
cp topics/elementare-zahlentheorie/01-was-ist-flt/article_en.md docs/grundlagen/elementare-zahlentheorie/01-was-ist-flt.en.md
cp topics/elementare-zahlentheorie/02-beweis-n4/article_en.md docs/grundlagen/elementare-zahlentheorie/02-beweis-n4.en.md
cp topics/elementare-zahlentheorie/03-primzahlen-reduktion/article_en.md docs/grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.en.md
cp topics/elementare-zahlentheorie/04-beweis-n3/article_en.md docs/grundlagen/elementare-zahlentheorie/04-beweis-n3.en.md

# Werkzeuge (6)
cp topics/gruppen-und-symmetrie/01-gruppen/article_en.md docs/werkzeuge/gruppen.en.md
cp topics/ringe-und-koerper/01-ringe-koerper/article_en.md docs/werkzeuge/ringe-koerper.en.md
cp topics/galois-theorie/01-galois-theorie/article_en.md docs/werkzeuge/galois-theorie.en.md
cp topics/p-adische-zahlen/01-p-adische-zahlen/article_en.md docs/werkzeuge/p-adische-zahlen.en.md
cp topics/elliptische-kurven/01-elliptische-kurven/article_en.md docs/werkzeuge/elliptische-kurven.en.md
cp topics/modulformen/01-modulformen/article_en.md docs/werkzeuge/modulformen.en.md

# Fermat-Wiles (8)
cp topics/fermat-wiles/01-taniyama-shimura/article_en.md docs/fermat-wiles/01-taniyama-shimura.en.md
cp topics/fermat-wiles/02-frey-ribet/article_en.md docs/fermat-wiles/02-frey-ribet.en.md
cp topics/fermat-wiles/03-galois-darstellungen/article_en.md docs/fermat-wiles/03-galois-darstellungen.en.md
cp topics/fermat-wiles/04-deformationstheorie/article_en.md docs/fermat-wiles/04-deformationstheorie.en.md
cp topics/fermat-wiles/05-r-gleich-t/article_en.md docs/fermat-wiles/05-r-gleich-t.en.md
cp topics/fermat-wiles/06-taylor-wiles-trick/article_en.md docs/fermat-wiles/06-taylor-wiles-trick.en.md
cp topics/fermat-wiles/07-3-5-switch/article_en.md docs/fermat-wiles/07-3-5-switch.en.md
cp topics/fermat-wiles/08-was-danach-kam/article_en.md docs/fermat-wiles/08-was-danach-kam.en.md

# Vorwissen (22)
for topic in abbildungen aussagenlogik beweisarten binomische-formeln bruchrechnung \
  gleichungen grenzwerte-konvergenz implikation-aequivalenz kombinatorik \
  komplexe-zahlen koordinatengeometrie mengen modulare-arithmetik \
  potenzen-polynome primfaktorzerlegung pythagoras relationen-aequivalenzklassen \
  summen-produktnotation teilbarkeit-ggt ungleichungen was-ist-ein-beweis zahlenbereiche; do
  cp "topics/vorwissen/${topic}/article_en.md" "docs/vorwissen/${topic}.en.md"
done

echo "40 englische Artikel nach docs/ kopiert."
