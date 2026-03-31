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
* `resources/wiles.pdf` – Original-Scan (Annals of Mathematics, 1995, 109 Seiten)
* `resources/wiles_parsed/wiles.md` – Vollständige Transkription via GPT-4o Vision (350 KB, LaTeX)
* `resources/Fermats-last-theorem-pdf.pdf` – Nigel Boston Lehrbuch (2003, 140 Seiten)
* `resources/fermats_last_theorem_boston.md` – Markdown-Extraktion des Boston-Lehrbuchs
* KB "fermat" – Semantische Suche: `kb search "..." --name fermat`
