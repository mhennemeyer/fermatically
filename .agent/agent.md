Sprache: Deutsch
Ansprache: Du (nicht Sie)

In diesem Ordner befinden sich
    * Anweisungen für den AI-Agent
    * und Möglichkeiten zur Ablage von Informationen für den AI-Agent.

### Globale Regeln (via Symlink aus `~/.agent/`)
Die folgenden Dateien sind Symlinks auf `~/.agent/` und gelten projektübergreifend:
* `rules.md` – Coding-Standards, Architektur, Workflow, Commit-Strategie
* `functional.md` – FP-Regeln für Code-Generierung

### Projektübergreifend
* `status.md` – Kompakter Projektstatus (Phase, Priorität, nächste Schritte, Blocker). Am Ende jeder Session aktualisieren.
* `~/agent/projects.md` – Zentrales Verzeichnis aller Projekte.

### Projektspezifisch
Die spezifischen Anforderungen für dieses Projekt befinden sich
in der Datei `specification.md` und README.md, wobei das README in
inhaltlichen Fragen Vorrang haben sollte.

### Quellen & Knowledgebase

#### Fermat / Wiles
* `resources/wiles.pdf` – Original-Scan (Annals of Mathematics, 1995, 109 Seiten)
* `resources/wiles_parsed/wiles.md` – Vollständige Transkription via GPT-4o Vision (350 KB, LaTeX)
* `resources/Fermats-last-theorem-pdf.pdf` – Nigel Boston Lehrbuch (2003, 140 Seiten)
* `resources/fermats_last_theorem_boston.md` – Markdown-Extraktion des Boston-Lehrbuchs
* KB "fermat" – Semantische Suche: `kb search "..." --name fermat`

#### Poincaré / Perelman
* `resources/perelman.pdf` – arXiv:math/0211159v1 (11.11.2002, 39 S.) – *„The entropy formula for the Ricci flow and its geometric applications"* (Paper 1/3)
* `resources/perelman_0303109.pdf` – arXiv:math/0303109v1 (10.03.2003, 22 S.) – *„Ricci flow with surgery on three-manifolds"* (Paper 2/3)
* `resources/perelman_0307245.pdf` – arXiv:math/0307245v1 (17.07.2003, 7 S.) – *„Finite extinction time for the solutions to the Ricci flow on certain three-manifolds"* (Paper 3/3)
* Empfohlene Sekundärliteratur (nicht im Repo): Kleiner/Lott „Notes on Perelman's papers" (Geom. Topol. 2008); Cao/Zhu „A Complete Proof…" (AJM 2006); Morgan/Tian „Ricci Flow and the Poincaré Conjecture" (AMS 2007).
