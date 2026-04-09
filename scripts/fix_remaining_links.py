#!/usr/bin/env python3
"""Fix remaining article_de.md links in docs/ that fix_docs_links.py missed."""
import os
import re

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")

# Simple replacements for inline links that fix_docs_links.py couldn't handle
# These are links embedded in markdown text like [text](path/article_de.md)
REPLACEMENTS = {
    # Vorwissen inline links (in docs, relative to grundlagen/elementare-zahlentheorie/)
    "../../vorwissen/pythagoras/article_de.md": "../../vorwissen/pythagoras.md",
    "../../vorwissen/teilbarkeit-ggt/article_de.md": "../../vorwissen/teilbarkeit-ggt.md",
    "../../vorwissen/modulare-arithmetik/article_de.md": "../../vorwissen/modulare-arithmetik.md",
    "../../vorwissen/beweisarten/article_de.md": "../../vorwissen/beweisarten.md",
    "../../vorwissen/gleichungen/article_de.md": "../../vorwissen/gleichungen.md",
    "../../vorwissen/zahlenbereiche/article_de.md": "../../vorwissen/zahlenbereiche.md",
    "../../vorwissen/potenzen-polynome/article_de.md": "../../vorwissen/potenzen-polynome.md",
    "../../vorwissen/komplexe-zahlen/article_de.md": "../../vorwissen/komplexe-zahlen.md",
    "../../vorwissen/mengen/article_de.md": "../../vorwissen/mengen.md",
    "../../vorwissen/abbildungen/article_de.md": "../../vorwissen/abbildungen.md",
    "../../vorwissen/koordinatengeometrie/article_de.md": "../../vorwissen/koordinatengeometrie.md",
    "../../vorwissen/bruchrechnung/article_de.md": "../../vorwissen/bruchrechnung.md",
    "../../vorwissen/summen-produktnotation/article_de.md": "../../vorwissen/summen-produktnotation.md",
    "../../vorwissen/grenzwerte-konvergenz/article_de.md": "../../vorwissen/grenzwerte-konvergenz.md",
    "../../vorwissen/primfaktorzerlegung/article_de.md": "../../vorwissen/primfaktorzerlegung.md",
    "../../vorwissen/kombinatorik/article_de.md": "../../vorwissen/kombinatorik.md",
    "../../vorwissen/relationen-aequivalenzklassen/article_de.md": "../../vorwissen/relationen-aequivalenzklassen.md",
    # Cross-article links that may remain
    "../07-3-5-switch/article_de.md": "07-3-5-switch.md",
    "../04-deformationstheorie/article_de.md": "04-deformationstheorie.md",
    "../04-beweis-n3/article_de.md": "04-beweis-n3.md",
    "../01-was-ist-flt/article_de.md": "01-was-ist-flt.md",
    "../02-beweis-n4/article_de.md": "02-beweis-n4.md",
    "../03-primzahlen-reduktion/article_de.md": "03-primzahlen-reduktion.md",
}

count = 0
for root, dirs, files in os.walk(DOCS):
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r") as f:
            content = f.read()
        if "article_de.md" not in content:
            continue
        original = content
        for old, new in REPLACEMENTS.items():
            content = content.replace(old, new)
        if content != original:
            with open(fpath, "w") as f:
                f.write(content)
            remaining = content.count("article_de.md")
            rel = os.path.relpath(fpath, DOCS)
            print(f"  Fixed: {rel}" + (f" ({remaining} article_de.md remaining)" if remaining else ""))
            count += 1

# Report any remaining article_de.md links
print(f"\nFixed {count} files.")
for root, dirs, files in os.walk(DOCS):
    for fname in files:
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r") as f:
            content = f.read()
        if "article_de.md" in content:
            rel = os.path.relpath(fpath, DOCS)
            for i, line in enumerate(content.split("\n"), 1):
                if "article_de.md" in line:
                    print(f"  REMAINING: {rel}:{i}: {line[:120]}")
