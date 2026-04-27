"""Generates stub files for docs/poincare/. One-shot helper, can be deleted after use."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "poincare"
DATE = "2026-04-25"

ACTS = [
    ("topologie",
     "Topologie und die Vermutung", "Topology and the Conjecture",
     [
        ("01-was-ist-topologie", "Was ist Topologie?", "What Is Topology?",
         ["topologie", "intuition"]),
        ("02-mannigfaltigkeiten", "Mannigfaltigkeiten", "Manifolds",
         ["mannigfaltigkeit", "topologie"]),
        ("03-sphaere-einfacher-zusammenhang",
         "Die Sphäre und einfacher Zusammenhang",
         "The Sphere and Simple Connectedness",
         ["sphaere", "homotopie", "fundamentalgruppe"]),
        ("04-was-ist-poincare-vermutung",
         "Was ist die Poincaré-Vermutung?",
         "What Is the Poincaré Conjecture?",
         ["poincare-vermutung", "geschichte"]),
        ("05-geometrisierungs-vermutung",
         "Die Geometrisierungs-Vermutung von Thurston",
         "Thurston's Geometrization Conjecture",
         ["thurston", "geometrisierung"]),
     ]),
    ("ricci-fluss",
     "Werkzeuge: Ricci-Fluss", "Tools: Ricci Flow",
     [
        ("01-riemannsche-metrik",
         "Riemannsche Metrik", "Riemannian Metric",
         ["riemannsche-geometrie", "metrik"]),
        ("02-kruemmung-ricci-tensor",
         "Krümmung und Ricci-Tensor", "Curvature and the Ricci Tensor",
         ["kruemmung", "ricci-tensor"]),
        ("03-hamiltons-ricci-fluss",
         "Hamiltons Ricci-Fluss", "Hamilton's Ricci Flow",
         ["ricci-fluss", "hamilton"]),
        ("04-singularitaeten-blowup",
         "Singularitäten und Blow-up-Limits",
         "Singularities and Blow-up Limits",
         ["singularitaeten", "blow-up"]),
        ("05-perelman-entropie",
         "Perelmans Entropie-Funktionale",
         "Perelman's Entropy Functionals",
         ["entropie", "perelman"]),
        ("06-kappa-nichtkollaps",
         "κ-Nichtkollaps und kanonische Nachbarschaften",
         "κ-Non-collapsing and Canonical Neighborhoods",
         ["kappa-nichtkollaps", "kanonische-nachbarschaften"]),
        ("07-reduzierte-laenge",
         "Reduzierte Länge und reduziertes Volumen",
         "Reduced Length and Reduced Volume",
         ["reduzierte-laenge", "reduziertes-volumen"]),
     ]),
    ("beweis",
     "Der Beweis", "The Proof",
     [
        ("01-hamiltons-programm",
         "Hamiltons Programm und seine Hindernisse",
         "Hamilton's Program and Its Obstacles",
         ["hamilton", "programm"]),
        ("02-singularitaeten-dim3",
         "Singularitätsanalyse in Dimension 3",
         "Singularity Analysis in Dimension 3",
         ["dim-3", "kappa-loesungen"]),
        ("03-chirurgie",
         "Ricci-Fluss mit Chirurgie",
         "Ricci Flow with Surgery",
         ["chirurgie", "surgery"]),
        ("04-long-time-verhalten",
         "Long-time-Verhalten und dünn-dick-Zerlegung",
         "Long-time Behavior and Thin–Thick Decomposition",
         ["long-time", "thin-thick"]),
        ("05-endliche-extinktion",
         "Endliche Auslöschungszeit",
         "Finite Extinction Time",
         ["finite-extinction"]),
        ("06-poincare-aus-geometrisierung",
         "Geometrisierung impliziert Poincaré",
         "Geometrization Implies Poincaré",
         ["geometrisierung", "korollar"]),
     ]),
]


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


INDEX_DE = """---
title: "Poincaré-Vermutung – Der Beweis von Perelman"
slug: poincare/index
series: poincare
date: 2026-04-25
status: stub
lang: de
---
# Poincaré-Vermutung – Der Beweis von Perelman

!!! abstract "Überblick"
    Grigori Perelmans Beweis der Poincaré-Vermutung (2002–2003) ist – neben Wiles' Beweis von Fermats letztem Satz – der zweite große Beweis, den diese Plattform Schritt für Schritt erschließt. Der Weg führt von der Topologie über Hamiltons Ricci-Fluss bis zu Perelmans Chirurgie-Verfahren.

*Stub – Inhalt folgt. Siehe `.agent/plans/poincare-perelman-plan.md` für die Roadmap.*

## Drei Akte

1. **[Topologie und die Vermutung](topologie/index.md)** – Was wird behauptet? Mannigfaltigkeiten, Sphären, einfacher Zusammenhang, Geometrisierungs-Vermutung.
2. **[Werkzeuge: Ricci-Fluss](ricci-fluss/index.md)** – Riemannsche Geometrie, Hamiltons Ricci-Fluss, Perelmans Entropie und κ-Nichtkollaps.
3. **[Der Beweis](beweis/index.md)** – Singularitätsanalyse in Dimension 3, Ricci-Fluss mit Chirurgie, Geometrisierung impliziert Poincaré.

## Quellen

- arXiv:math/0211159 (Perelman, 2002) – Entropie-Formel
- arXiv:math/0303109 (Perelman, 2003) – Ricci-Fluss mit Chirurgie
- arXiv:math/0307245 (Perelman, 2003) – Endliche Auslöschungszeit
- Morgan / Tian: *Ricci Flow and the Poincaré Conjecture*, AMS 2007
- Kleiner / Lott: *Notes on Perelman's papers*, Geom. Topol. 2008
- Cao / Zhu: *A Complete Proof of the Poincaré and Geometrization Conjectures*, AJM 2006
"""

INDEX_EN = """---
title: "The Poincaré Conjecture – Perelman's Proof"
slug: poincare/index
series: poincare
date: 2026-04-25
status: stub
lang: en
---
# The Poincaré Conjecture – Perelman's Proof

!!! abstract "Overview"
    Grigori Perelman's proof of the Poincaré Conjecture (2002–2003) is – alongside Wiles' proof of Fermat's Last Theorem – the second great proof this platform unpacks step by step. The path leads from topology through Hamilton's Ricci flow to Perelman's surgery procedure.

*Stub – content forthcoming. See `.agent/plans/poincare-perelman-plan.md` for the roadmap.*

## Three Acts

1. **[Topology and the Conjecture](topologie/index.md)** – What is being claimed? Manifolds, spheres, simple connectedness, the geometrization conjecture.
2. **[Tools: Ricci Flow](ricci-fluss/index.md)** – Riemannian geometry, Hamilton's Ricci flow, Perelman's entropy and κ-non-collapsing.
3. **[The Proof](beweis/index.md)** – Singularity analysis in dimension 3, Ricci flow with surgery, geometrization implies Poincaré.

## Sources

- arXiv:math/0211159 (Perelman, 2002) – Entropy formula
- arXiv:math/0303109 (Perelman, 2003) – Ricci flow with surgery
- arXiv:math/0307245 (Perelman, 2003) – Finite extinction time
- Morgan / Tian: *Ricci Flow and the Poincaré Conjecture*, AMS 2007
- Kleiner / Lott: *Notes on Perelman's papers*, Geom. Topol. 2008
- Cao / Zhu: *A Complete Proof of the Poincaré and Geometrization Conjectures*, AJM 2006
"""


def main() -> None:
    write("index.de.md", INDEX_DE)
    write("index.md", INDEX_EN)

    for act_slug, act_de, act_en, articles in ACTS:
        rows_de = "\n".join(
            f"| {i + 1} | [{art_de}]({num}.md) |"
            for i, (num, art_de, _, _) in enumerate(articles)
        )
        rows_en = "\n".join(
            f"| {i + 1} | [{art_en}]({num}.md) |"
            for i, (num, _, art_en, _) in enumerate(articles)
        )
        write(f"{act_slug}/index.de.md",
              f"""---
title: "{act_de}"
slug: poincare/{act_slug}/index
series: poincare
date: {DATE}
status: stub
lang: de
---
# {act_de}

*Akt-Übersicht – Inhalt folgt.*

| # | Artikel |
|---|---------|
{rows_de}
""")
        write(f"{act_slug}/index.md",
              f"""---
title: "{act_en}"
slug: poincare/{act_slug}/index
series: poincare
date: {DATE}
status: stub
lang: en
---
# {act_en}

*Act overview – content forthcoming.*

| # | Article |
|---|---------|
{rows_en}
""")
        for i, (num, art_de, art_en, tags) in enumerate(articles, start=1):
            tag_block = "\n".join(f"  - {t}" for t in tags)
            write(f"{act_slug}/{num}.de.md",
                  f"""---
title: "{art_de}"
slug: poincare/{act_slug}/{num}
series: poincare
part: {i}
act: {act_slug}
date: {DATE}
status: stub
lang: de
tags:
{tag_block}
---
# {art_de}

!!! warning "Stub"
    Dieser Artikel ist ein Platzhalter. Inhalt folgt gemäß `.agent/plans/poincare-perelman-plan.md`.
""")
            write(f"{act_slug}/{num}.md",
                  f"""---
title: "{art_en}"
slug: poincare/{act_slug}/{num}
series: poincare
part: {i}
act: {act_slug}
date: {DATE}
status: stub
lang: en
tags:
{tag_block}
---
# {art_en}

!!! warning "Stub"
    This article is a placeholder. Content forthcoming, see `.agent/plans/poincare-perelman-plan.md`.
""")


if __name__ == "__main__":
    main()
    print("done")
