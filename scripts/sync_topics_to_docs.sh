#!/usr/bin/env bash
# Kopiert die fertigen Artikel aus topics/ nach docs/ für MkDocs
set -euo pipefail
cd "$(dirname "$0")/.."

# Grundlagen – Elementare Zahlentheorie
cp topics/elementare-zahlentheorie/01-was-ist-flt/article_de.md docs/grundlagen/elementare-zahlentheorie/01-was-ist-flt.md
cp topics/elementare-zahlentheorie/02-beweis-n4/article_de.md docs/grundlagen/elementare-zahlentheorie/02-beweis-n4.md
cp topics/elementare-zahlentheorie/03-primzahlen-reduktion/article_de.md docs/grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md
cp topics/elementare-zahlentheorie/04-beweis-n3/article_de.md docs/grundlagen/elementare-zahlentheorie/04-beweis-n3.md

# Werkzeuge
cp topics/gruppen-und-symmetrie/01-gruppen/article_de.md docs/werkzeuge/gruppen.md
cp topics/ringe-und-koerper/01-ringe-koerper/article_de.md docs/werkzeuge/ringe-koerper.md
cp topics/galois-theorie/01-galois-theorie/article_de.md docs/werkzeuge/galois-theorie.md
cp topics/p-adische-zahlen/01-p-adische-zahlen/article_de.md docs/werkzeuge/p-adische-zahlen.md
cp topics/elliptische-kurven/01-elliptische-kurven/article_de.md docs/werkzeuge/elliptische-kurven.md
cp topics/modulformen/01-modulformen/article_de.md docs/werkzeuge/modulformen.md

# Fermat-Wiles Beweis
cp topics/fermat-wiles/01-taniyama-shimura/article_de.md docs/fermat-wiles/01-taniyama-shimura.md
cp topics/fermat-wiles/02-frey-ribet/article_de.md docs/fermat-wiles/02-frey-ribet.md
cp topics/fermat-wiles/03-galois-darstellungen/article_de.md docs/fermat-wiles/03-galois-darstellungen.md
cp topics/fermat-wiles/04-deformationstheorie/article_de.md docs/fermat-wiles/04-deformationstheorie.md
cp topics/fermat-wiles/05-r-gleich-t/article_de.md docs/fermat-wiles/05-r-gleich-t.md
cp topics/fermat-wiles/06-taylor-wiles-trick/article_de.md docs/fermat-wiles/06-taylor-wiles-trick.md
cp topics/fermat-wiles/07-3-5-switch/article_de.md docs/fermat-wiles/07-3-5-switch.md
cp topics/fermat-wiles/08-was-danach-kam/article_de.md docs/fermat-wiles/08-was-danach-kam.md

echo "✅ 18 Artikel aus topics/ nach docs/ synchronisiert"
