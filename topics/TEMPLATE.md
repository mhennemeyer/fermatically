# Vorlage für neue Artikel

## Dateistruktur pro Artikel

Jeder Artikel liegt in einem eigenen Verzeichnis:

```
topics/{serie-slug}/{nn-artikel-slug}/
├── article_de.md     ← Deutscher Artikel
├── article_en.md     ← Englische Version (optional, wird nachgezogen)
└── outline.md        ← Gliederung / Outline
```

## Frontmatter-Schema (article_de.md / article_en.md)

```yaml
---
title: "Titel des Artikels"
slug: serie-slug/nn-artikel-slug
series: serie-slug
part: 1
date: 2026-03-30
status: draft          # draft | review | published
lang: de               # de | en
category: zahlentheorie
tags:
  - tag1
  - tag2
requires: []           # Liste von Topic-Pfaden, die als Voraussetzung gelten
  # Beispiel:
  # - gruppen-und-symmetrie/01-gruppen
  # - ringe-und-koerper/01-ringe-koerper
---
```

## Artikel-Aufbau

```markdown
---
(Frontmatter wie oben)
---

# Titel

!!! abstract "Zusammenfassung"
    Ein bis zwei Sätze, die den Artikel zusammenfassen.

## Voraussetzungen

Kurze Beschreibung, welche Vorkenntnisse nötig sind, mit Links zu den
entsprechenden Topics:

- [Gruppen – Symmetrie als Sprache](../gruppen-und-symmetrie/01-gruppen/article_de.md)

## Inhalt

### Abschnitt 1
...

### Abschnitt 2
...

## Zusammenfassung & Ausblick

Was wurde gezeigt? Wie geht es weiter?

## Quellen

- Quelle 1
- Quelle 2
```

## Outline-Format (outline.md)

```markdown
# Outline: Titel des Artikels

## Ziel
Was soll der Leser nach diesem Artikel verstanden haben?

## Gliederung
1. Abschnitt – Kurzbeschreibung
2. Abschnitt – Kurzbeschreibung
3. ...

## Kernaussagen
- Kernaussage 1
- Kernaussage 2

## Querverweise
- Setzt voraus: [Topic-Name](Pfad)
- Wird benötigt von: [Topic-Name](Pfad)

## Quellen
- Primärquelle(n) für diesen Artikel
```
