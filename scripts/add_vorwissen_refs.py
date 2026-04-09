#!/usr/bin/env python3
"""Adds Vorwissen references (frontmatter + table) to all main articles."""
import os
import re

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS = os.path.join(PROJECT, "topics")

# Vorwissen slug -> (display name, short description)
VORWISSEN_INFO = {
    "teilbarkeit-ggt": ("Teilbarkeit und ggT", "Teilerfremdheit, $\\gcd$, Euklidischer Algorithmus"),
    "beweisarten": ("Beweisarten", "Direkter Beweis, Widerspruch, Induktion, Abstieg"),
    "gleichungen": ("Gleichungen", "Äquivalente Umformungen und Lösungsstrategien"),
    "pythagoras": ("Pythagoras und pythagoräische Tripel", "$a^2 + b^2 = c^2$ und ganzzahlige Lösungen"),
    "modulare-arithmetik": ("Modulare Arithmetik", "Kongruenzen $a \\equiv b \\pmod{n}$ und Restklassen"),
    "potenzen-polynome": ("Potenzen und Polynome", "Potenzschreibweise $a^n$ und Polynomrechnung"),
    "zahlenbereiche": ("Zahlenbereiche", "$\\mathbb{N}, \\mathbb{Z}, \\mathbb{Q}, \\mathbb{R}, \\mathbb{C}$ und ihre Beziehungen"),
    "komplexe-zahlen": ("Komplexe Zahlen", "Zahlen $a + bi$ mit $i^2 = -1$, Polarform, Einheitswurzeln"),
    "primfaktorzerlegung": ("Primfaktorzerlegung", "Eindeutige Zerlegung in Primfaktoren (Fundamentalsatz der Arithmetik)"),
    "kombinatorik": ("Kombinatorik", "Permutationen, Kombinationen, Binomialkoeffizienten"),
    "mengen": ("Mengen und Mengenoperationen", "Mengennotation, $\\cup, \\cap, \\setminus, \\times$"),
    "abbildungen": ("Abbildungen (Funktionen)", "$f: A \\to B$, injektiv, surjektiv, bijektiv"),
    "relationen-aequivalenzklassen": ("Relationen und Äquivalenzklassen", "Äquivalenzrelationen, Restklassen, Quotientenmengen"),
    "koordinatengeometrie": ("Koordinatengeometrie", "Punkte, Geraden, Kurven als Gleichungen"),
    "bruchrechnung": ("Bruchrechnung", "Rechnen mit Brüchen $a/b$"),
    "summen-produktnotation": ("Summen- und Produktnotation", "$\\sum$- und $\\prod$-Notation"),
    "grenzwerte-konvergenz": ("Grenzwerte und Konvergenz", "$\\lim_{n \\to \\infty} a_n = L$, Cauchy-Folgen, Reihen"),
}

# Article -> list of vorwissen slugs (from the matrix in the plan)
ARTICLE_VORWISSEN = {
    # Already done: 01-was-ist-flt, 02-beweis-n4
    "elementare-zahlentheorie/03-primzahlen-reduktion": [
        "teilbarkeit-ggt", "beweisarten", "modulare-arithmetik",
        "primfaktorzerlegung", "kombinatorik"
    ],
    "elementare-zahlentheorie/04-beweis-n3": [
        "komplexe-zahlen", "teilbarkeit-ggt", "modulare-arithmetik",
        "beweisarten", "zahlenbereiche", "primfaktorzerlegung"
    ],
    "gruppen-und-symmetrie/01-gruppen": [
        "mengen", "abbildungen", "zahlenbereiche", "modulare-arithmetik",
        "kombinatorik", "relationen-aequivalenzklassen"
    ],
    "ringe-und-koerper/01-ringe-koerper": [
        "mengen", "abbildungen", "gleichungen", "teilbarkeit-ggt",
        "primfaktorzerlegung", "komplexe-zahlen", "relationen-aequivalenzklassen"
    ],
    "galois-theorie/01-galois-theorie": [
        "potenzen-polynome", "abbildungen", "komplexe-zahlen", "zahlenbereiche"
    ],
    "p-adische-zahlen/01-p-adische-zahlen": [
        "teilbarkeit-ggt", "modulare-arithmetik", "grenzwerte-konvergenz",
        "summen-produktnotation", "potenzen-polynome"
    ],
    "elliptische-kurven/01-elliptische-kurven": [
        "koordinatengeometrie", "bruchrechnung", "modulare-arithmetik",
        "abbildungen", "summen-produktnotation"
    ],
    "modulformen/01-modulformen": [
        "komplexe-zahlen", "summen-produktnotation", "grenzwerte-konvergenz",
        "abbildungen"
    ],
    "fermat-wiles/01-taniyama-shimura": [
        "summen-produktnotation", "modulare-arithmetik", "komplexe-zahlen"
    ],
    "fermat-wiles/02-frey-ribet": [
        "teilbarkeit-ggt", "primfaktorzerlegung", "beweisarten"
    ],
    "fermat-wiles/03-galois-darstellungen": [
        "abbildungen", "mengen", "modulare-arithmetik"
    ],
    "fermat-wiles/04-deformationstheorie": [
        "grenzwerte-konvergenz", "relationen-aequivalenzklassen"
    ],
    "fermat-wiles/05-r-gleich-t": [
        "summen-produktnotation"
    ],
    "fermat-wiles/06-taylor-wiles-trick": [
        "grenzwerte-konvergenz", "modulare-arithmetik"
    ],
    "fermat-wiles/07-3-5-switch": [
        "beweisarten"
    ],
    # 08-was-danach-kam has no additional vorwissen requirements
}


def find_article_path(slug):
    """Find the article_de.md file for a given slug."""
    parts = slug.split("/")
    return os.path.join(TOPICS, parts[0], parts[1], "article_de.md")


def build_vorwissen_table(slugs, article_path):
    """Build the Vorwissen table for an article."""
    # Compute relative path from article to vorwissen
    article_dir = os.path.dirname(article_path)
    vorwissen_base = os.path.join(TOPICS, "vorwissen")
    
    lines = []
    lines.append("")
    lines.append("| Thema | Beschreibung |")
    lines.append("|-------|-------------|")
    for slug in slugs:
        name, desc = VORWISSEN_INFO[slug]
        # All topic articles are at topics/SERIES/ARTICLE/article_de.md
        # Vorwissen is at topics/vorwissen/SLUG/article_de.md
        # Relative path is always ../../vorwissen/SLUG/article_de.md
        link = f"../../vorwissen/{slug}/article_de.md"
        lines.append(f"| [{name}]({link}) | {desc} |")
    
    return "\n".join(lines)


def update_requires_frontmatter(content, slugs):
    """Update the requires: field in frontmatter."""
    if not slugs:
        return content
    
    # Replace requires: [] or requires:\n  - ... with new list
    new_requires = "requires:\n" + "\n".join(f"  - {s}" for s in slugs)
    
    # Match requires: [] 
    content = re.sub(r'requires: \[\]', new_requires, content)
    # Match existing requires with items
    content = re.sub(r'requires:\n(?:  - .+\n)*', new_requires + "\n", content)
    
    return content


def add_vorwissen_table(content, table_text):
    """Add the Vorwissen table after the Voraussetzungen section header and existing items."""
    # Find the "## Voraussetzungen" section
    # The table should go after any existing bullet points but before the "---"
    
    # Pattern: ## Voraussetzungen\n\n(existing content)\n\n---
    pattern = r'(## Voraussetzungen\n\n(?:- .+\n)*)'
    
    match = re.search(pattern, content)
    if match:
        existing = match.group(1)
        # Check if table already exists
        if "| Thema |" in content[:content.find("## 1.")]:
            return content  # Already has a table
        replacement = existing + table_text + "\n"
        content = content[:match.start()] + replacement + content[match.end():]
    
    return content


def process_article(slug, vorwissen_slugs):
    """Process a single article."""
    path = find_article_path(slug)
    if not os.path.exists(path):
        print(f"  ❌ Not found: {path}")
        return False
    
    with open(path, 'r') as f:
        content = f.read()
    
    # Update frontmatter
    content = update_requires_frontmatter(content, vorwissen_slugs)
    
    # Build and add table
    table = build_vorwissen_table(vorwissen_slugs, path)
    content = add_vorwissen_table(content, table)
    
    with open(path, 'w') as f:
        f.write(content)
    
    print(f"  ✅ {slug}: {len(vorwissen_slugs)} Vorwissen-Themen")
    return True


# Process all articles
print("Adding Vorwissen references to articles...\n")

for slug, vw_slugs in sorted(ARTICLE_VORWISSEN.items()):
    process_article(slug, vw_slugs)

print("\nDone.")
