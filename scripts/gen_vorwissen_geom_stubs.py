"""Generates stubs for docs/vorwissen/geometrie-analysis/. One-shot helper."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "vorwissen" / "geometrie-analysis"
DATE = "2026-04-25"

ARTICLES = [
    ("vektoranalysis",
     "Vektoranalysis kompakt", "Vector Calculus in Brief",
     ["vektoranalysis", "gradient", "divergenz", "laplace"]),
    ("waermeleitung",
     "Wärmeleitungsgleichung – Intuition", "Heat Equation – Intuition",
     ["waermeleitung", "pde", "intuition"]),
    ("mannigfaltigkeit-anschaulich",
     "Mannigfaltigkeit anschaulich", "Manifolds – an Intuitive View",
     ["mannigfaltigkeit", "intuition"]),
    ("tangentialraum-tensoren",
     "Tangentialraum und Tensoren", "Tangent Space and Tensors",
     ["tangentialraum", "tensoren"]),
    ("kruemmung-flaechen-gauss",
     "Krümmung von Flächen (Gauß)", "Curvature of Surfaces (Gauss)",
     ["kruemmung", "gauss", "flaechen"]),
]


def write(name: str, content: str) -> None:
    (ROOT / name).write_text(content)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for slug, title_de, title_en, tags in ARTICLES:
        tag_block = "\n".join(f"  - {t}" for t in tags)
        write(f"{slug}.de.md", f"""---
title: "{title_de}"
slug: vorwissen/geometrie-analysis/{slug}
series: vorwissen
category: geometrie-analysis-aufbau
date: {DATE}
status: stub
lang: de
tags:
{tag_block}
---
# {title_de}

!!! warning "Stub"
    Dieser Vorwissen-Artikel ist ein Platzhalter. Inhalt folgt – er bereitet die Poincaré-Storyline geometrisch-analytisch vor.
""")
        write(f"{slug}.md", f"""---
title: "{title_en}"
slug: vorwissen/geometrie-analysis/{slug}
series: vorwissen
category: geometrie-analysis-aufbau
date: {DATE}
status: stub
lang: en
tags:
{tag_block}
---
# {title_en}

!!! warning "Stub"
    This prerequisite article is a placeholder. Content forthcoming – it lays the geometric/analytic groundwork for the Poincaré storyline.
""")


if __name__ == "__main__":
    main()
    print("done")
