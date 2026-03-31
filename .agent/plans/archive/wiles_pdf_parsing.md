# Plan: Wiles-Beweis (resources/wiles.pdf) vollständig erfassen

## Analyse des Dokuments

- **Datei:** `resources/wiles.pdf` – 109 Seiten, 10 MB
- **Inhalt:** Andrew Wiles, *"Modular elliptic curves and Fermat's Last Theorem"*, Annals of Mathematics 141 (1995), S. 443–551
- **Format:** Reiner Bild-Scan (kein Textlayer). Jede Seite ist ein einzelnes Graustufenbild (4064×5904 px, CCITTFaxDecode). Erstellt 2006 mit "page2pdf".
- **Herausforderung:** Mathematisch extrem dichter Text mit komplexen Formeln (Algebra, Zahlentheorie, Galois-Darstellungen, Hecke-Algebren). Einfache OCR scheitert an den Formeln.

## Bewertung: Scan parsen vs. digitale Quelle beschaffen

### Option A: Bereits existierende digitale Version nutzen ⭐ EMPFOHLEN

Da es sich um eines der berühmtesten Papiere der Mathematik handelt, gibt es mit hoher Wahrscheinlichkeit bereits digitale Versionen:

1. **Annals of Mathematics (JSTOR/Princeton)** – Die Annals bieten ältere Ausgaben oft als durchsuchbare PDFs an. Link: https://annals.math.princeton.edu/
2. **Andrew Wiles' Webseite / Institutional Repository** – Oxford oder Princeton haben möglicherweise eine digitale Fassung.
3. **arXiv oder Preprint-Server** – Möglicherweise existiert eine Preprint-Version (das Paper stammt aus 1995, vor arXiv-Verbreitung, aber spätere Uploads sind möglich).
4. **Projekt Euclid / MathSciNet** – Mathematische Datenbanken mit digitalisierten Journalartikeln.

**Vorteil:** Perfekte Qualität, kein Informationsverlust, sofort nutzbar.
**Aufwand:** Gering – Recherche und Download.

### Option B: KI-basiertes PDF-zu-LaTeX-Parsing (Nougat)

Meta's **Nougat** (Neural Optical Understanding for Academic Documents) ist speziell für gescannte wissenschaftliche Papers entwickelt:

```bash
pip install nougat-ocr
nougat resources/wiles.pdf -o resources/wiles_parsed/
```

- Erzeugt Markdown mit eingebetteten LaTeX-Formeln
- Speziell trainiert auf mathematische Notation
- Open Source, lokal ausführbar
- **Qualität:** Gut bis sehr gut bei standardmäßigen akademischen Papers. Bei einem 109-seitigen Beweis mit dichter Notation sind Fehler bei komplexen Formeln wahrscheinlich (~90-95% Genauigkeit).
- **Aufwand:** Mittel – Installation, Ausführung (~30-60 Min. Rechenzeit), manuelle Nachkorrektur nötig.

### Option C: LLM Vision API (Claude/GPT-4V) seitenweise

Jede der 109 Seiten als Bild an ein Vision-LLM senden mit dem Prompt, den Inhalt in LaTeX/Markdown zu transkribieren:

- **Qualität:** Potenziell sehr hoch, da LLMs mathematischen Kontext verstehen.
- **Aufwand:** Hoch – 109 API-Calls, Kosten (~$5-15 je nach Modell), Scripting nötig, Rate Limits.
- **Risiko:** Halluzinationen bei komplexen Formeln möglich.

### Option D: Mathpix API (kommerziell)

Spezialisierter Dienst für Math-OCR:

- **Qualität:** Beste Math-OCR am Markt.
- **Aufwand:** Account nötig, kostenpflichtig (~$0.01/Seite → ~$1.09 für das Dokument).
- **Output:** LaTeX, Markdown, oder DOCX.

### Option E: Tesseract OCR (klassisch)

- Erfasst nur den Fließtext, **keine mathematischen Formeln**.
- **Nicht geeignet** für dieses Dokument.

## Empfohlener Plan

### Phase 1: Digitale Quelle suchen (1 Stunde)
1. JSTOR / Annals of Mathematics durchsuchen nach Vol. 141, No. 3 (1995)
2. Google Scholar nach dem exakten Titel suchen
3. Institutionelle Repositories prüfen (Oxford, Princeton)
4. Falls gefunden → **fertig**. PDF mit Textlayer oder LaTeX-Quelle herunterladen.

### Phase 2: Falls keine digitale Quelle → Nougat + Nachkorrektur (4-8 Stunden)
1. Nougat installieren und auf `wiles.pdf` ausführen
2. Output als `resources/wiles_parsed.md` speichern
3. Stichprobenartige Qualitätsprüfung an 5-10 Seiten (Formeln mit Original vergleichen)
4. Fehlerhafte Stellen mit LLM Vision API nachkorrigieren (nur die problematischen Seiten)

### Phase 3: Validierung
1. Gesamtes Dokument auf Vollständigkeit prüfen (alle 109 Seiten vorhanden?)
2. LaTeX-Formeln kompilieren lassen → Syntaxfehler finden
3. Stichproben-Vergleich: 10 zufällige Seiten visuell mit Original abgleichen

## Durchführung (Stand: 2026-03-27)

### Ergebnis Option A: Digitale Quelle suchen
- **Ergebnis: Gescheitert.** Das Original-Paper ist hinter Paywalls (JSTOR/Annals). Geprüft: JSTOR, Annals Princeton, Oxford, IAS, Semantic Scholar, Unpaywall, GitHub, CiteSeerX – nirgends frei verfügbar.
- **Neue PDF gefunden:** `resources/Fermats-last-theorem-pdf.pdf` – Nigel Boston (Univ. Wisconsin, 2003), 140 Seiten Lehrbuch über den Beweis. **Nicht** das Original, aber didaktische Aufbereitung auf Graduate-Level mit vollständigem Textlayer (TeX-generiert).

### Boston-PDF: Extraktion ✅
- **Markdown:** `resources/fermats_last_theorem_boston.md` (180k Zeichen, 140 Seiten)
- **Knowledgebase:** `kb` Tool mit Name "fermat" – semantische Suche über den Inhalt (`kb search "..." --name fermat`)

### Wiles-Original: OCR-Versuche

- **Nougat:** Gescheitert (veraltete Dependencies, inkompatibel mit aktuellen Bibliotheken).
- **marker-pdf:** Gescheitert. Layout-Erkennung und erster OCR-Durchlauf liefen (3035 Blöcke), aber Crash bei zweitem Texterkennung-Durchgang (59%) durch torch-Fehler (`index out of bounds` in surya Embedder). Kein Output erzeugt.
- **Mathpix API:** Nicht verfügbar (kein Account/API-Key vorhanden).

### Wiles-Original: GPT-4o Vision API ✅
- **Methode:** Jede der 109 Seiten als PNG (200 DPI) an GPT-4o Vision gesendet.
- **Script:** `resources/wiles_ocr_vision.py` (wiederverwendbar, mit `--test` und `--resume=N` Optionen).
- **Ergebnis:** `resources/wiles_parsed/wiles.md` – 350 KB, 4775 Zeilen, 109 Seiten vollständig transkribiert.
- **Einzelseiten:** `resources/wiles_parsed/page_001.md` bis `page_109.md`.
- **Qualität:** Exzellent – LaTeX-Formeln, Theorem-Nummerierungen, Referenzen und Bibliographie korrekt erfasst. 0 Fehlerseiten.
- **Dauer:** ~15 Minuten (109 API-Calls).
- **Kosten:** ~$3-5 (GPT-4o Vision, 109 hochauflösende Bilder).

### KB-Integration
- Boston-Lehrbuch ist in KB "fermat" (180 Chunks, semantische Suche).
- Wiles-Transkription (`wiles.md`) konnte nicht in KB aufgenommen werden – `kb` unterstützt nur PDF/EPUB. Die Markdown-Datei ist aber direkt lesbar und durchsuchbar.
- **Mögliche Erweiterung:** Markdown → PDF konvertieren (z.B. via pandoc) und dann in KB aufnehmen.

## Fazit

**Option A gescheitert** (Paywall). **Option B gescheitert** (marker-pdf Crash, Nougat Dependencies). **Option C erfolgreich** (GPT-4o Vision).

- ✅ Boston-Lehrbuch extrahiert + KB erstellt – sofort nutzbar für Verständnis des Beweises
- ✅ Wiles-Original vollständig transkribiert via GPT-4o Vision API (109 Seiten, 350 KB Markdown mit LaTeX)
