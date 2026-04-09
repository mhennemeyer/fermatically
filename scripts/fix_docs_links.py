#!/usr/bin/env python3
"""Fixes internal links in docs/ files from topics/-style to docs/-style paths."""
import re
import os

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(PROJECT, "docs")

# Mapping: topics slug -> docs path (relative to docs/)
TOPIC_TO_DOCS = {
    "elementare-zahlentheorie/01-was-ist-flt": "grundlagen/elementare-zahlentheorie/01-was-ist-flt.md",
    "elementare-zahlentheorie/02-beweis-n4": "grundlagen/elementare-zahlentheorie/02-beweis-n4.md",
    "elementare-zahlentheorie/03-primzahlen-reduktion": "grundlagen/elementare-zahlentheorie/03-primzahlen-reduktion.md",
    "elementare-zahlentheorie/04-beweis-n3": "grundlagen/elementare-zahlentheorie/04-beweis-n3.md",
    "gruppen-und-symmetrie/01-gruppen": "werkzeuge/gruppen.md",
    "ringe-und-koerper/01-ringe-koerper": "werkzeuge/ringe-koerper.md",
    "galois-theorie/01-galois-theorie": "werkzeuge/galois-theorie.md",
    "p-adische-zahlen/01-p-adische-zahlen": "werkzeuge/p-adische-zahlen.md",
    "elliptische-kurven/01-elliptische-kurven": "werkzeuge/elliptische-kurven.md",
    "modulformen/01-modulformen": "werkzeuge/modulformen.md",
    "fermat-wiles/01-taniyama-shimura": "fermat-wiles/01-taniyama-shimura.md",
    "fermat-wiles/02-frey-ribet": "fermat-wiles/02-frey-ribet.md",
    "fermat-wiles/03-galois-darstellungen": "fermat-wiles/03-galois-darstellungen.md",
    "fermat-wiles/04-deformationstheorie": "fermat-wiles/04-deformationstheorie.md",
    "fermat-wiles/05-r-gleich-t": "fermat-wiles/05-r-gleich-t.md",
    "fermat-wiles/06-taylor-wiles-trick": "fermat-wiles/06-taylor-wiles-trick.md",
    "fermat-wiles/07-3-5-switch": "fermat-wiles/07-3-5-switch.md",
    "fermat-wiles/08-was-danach-kam": "fermat-wiles/08-was-danach-kam.md",
    # Vorwissen-Artikel
    "vorwissen/aussagenlogik": "vorwissen/aussagenlogik.md",
    "vorwissen/implikation-aequivalenz": "vorwissen/implikation-aequivalenz.md",
    "vorwissen/beweisarten": "vorwissen/beweisarten.md",
    "vorwissen/was-ist-ein-beweis": "vorwissen/was-ist-ein-beweis.md",
    "vorwissen/bruchrechnung": "vorwissen/bruchrechnung.md",
    "vorwissen/gleichungen": "vorwissen/gleichungen.md",
    "vorwissen/ungleichungen": "vorwissen/ungleichungen.md",
    "vorwissen/teilbarkeit-ggt": "vorwissen/teilbarkeit-ggt.md",
    "vorwissen/primfaktorzerlegung": "vorwissen/primfaktorzerlegung.md",
    "vorwissen/modulare-arithmetik": "vorwissen/modulare-arithmetik.md",
    "vorwissen/komplexe-zahlen": "vorwissen/komplexe-zahlen.md",
    "vorwissen/mengen": "vorwissen/mengen.md",
    "vorwissen/abbildungen": "vorwissen/abbildungen.md",
    "vorwissen/relationen-aequivalenzklassen": "vorwissen/relationen-aequivalenzklassen.md",
    "vorwissen/zahlenbereiche": "vorwissen/zahlenbereiche.md",
    "vorwissen/pythagoras": "vorwissen/pythagoras.md",
    "vorwissen/koordinatengeometrie": "vorwissen/koordinatengeometrie.md",
    "vorwissen/potenzen-polynome": "vorwissen/potenzen-polynome.md",
    "vorwissen/binomische-formeln": "vorwissen/binomische-formeln.md",
    "vorwissen/summen-produktnotation": "vorwissen/summen-produktnotation.md",
    "vorwissen/kombinatorik": "vorwissen/kombinatorik.md",
    "vorwissen/grenzwerte-konvergenz": "vorwissen/grenzwerte-konvergenz.md",
}


def make_relative(from_file, to_docs_path):
    """Compute relative path from from_file's directory to to_docs_path (both relative to DOCS)."""
    from_dir = os.path.dirname(from_file)
    return os.path.relpath(to_docs_path, from_dir)


def fix_link(match, doc_rel_path):
    """Replace a topics-style link with the correct docs-style relative link."""
    full = match.group(0)
    link_path = match.group(1)

    # Extract the topic slug from the link
    # Pattern: ../../<topic>/<article>/article_de.md or ../<article>/article_de.md
    # Cross-topic: ../../galois-theorie/01-galois-theorie/article_de.md
    m = re.match(r'(?:\.\./)*(\S+?)/article_de\.md', link_path)
    if not m:
        return full

    slug = m.group(1)
    # slug could be "galois-theorie/01-galois-theorie" or "01-was-ist-flt" (within same series)

    # If slug is just an article name (no /), determine the series from the source file
    if '/' not in slug:
        # Intra-series link: source is e.g. grundlagen/elementare-zahlentheorie/01-was-ist-flt.md
        # The article slug is within the same topic series
        from_dir = os.path.dirname(doc_rel_path)
        if from_dir == "grundlagen/elementare-zahlentheorie":
            slug = "elementare-zahlentheorie/" + slug
        elif from_dir == "fermat-wiles":
            slug = "fermat-wiles/" + slug

    if slug in TOPIC_TO_DOCS:
        new_rel = make_relative(doc_rel_path, TOPIC_TO_DOCS[slug])
        return full.replace(link_path, new_rel)

    print(f"  ⚠ Unmapped slug: {slug} in {doc_rel_path}")
    return full


def fix_file(doc_rel_path):
    """Fix all article_de.md links in a single docs/ file."""
    filepath = os.path.join(DOCS, doc_rel_path)
    with open(filepath, 'r') as f:
        content = f.read()

    # Match markdown links containing article_de.md
    pattern = r'\(([^)]*article_de\.md)\)'

    def replacer(match):
        return fix_link(match, doc_rel_path)

    new_content = re.sub(pattern, replacer, content)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        count = content.count('article_de.md') - new_content.count('article_de.md')
        print(f"  ✅ {doc_rel_path}: {content.count('article_de.md')} links fixed")
    else:
        if 'article_de.md' in content:
            print(f"  ⚠ {doc_rel_path}: links remain unchanged")


# Process all docs files
ALL_DOCS_FILES = []
for root, dirs, files in os.walk(DOCS):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), DOCS)
            ALL_DOCS_FILES.append(rel)

for doc_file in sorted(ALL_DOCS_FILES):
    fix_file(doc_file)

print("\nDone.")
