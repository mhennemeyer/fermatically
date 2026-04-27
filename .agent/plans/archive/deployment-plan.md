# Plan: Statisches Deployment für fermatically.com

Erstellt: 2026-04-14
Aktualisiert: 2026-04-16
Status: Abgeschlossen ✅

## Ausgangslage

- MkDocs Material-Seite, Build-Output in `site/`
- Domain `fermatically.com` registriert
- Kein Git-Remote konfiguriert (rein lokales Repo)
- Dockerfile vorhanden (Python-Build → nginx), aber für statisches Hosting nicht nötig
- 38 Playwright-Tests vorhanden, alle grün

## Optionen-Bewertung

### Option A: GitHub Pages ⭐ Empfehlung

**Setup:** GitHub-Repo erstellen → `mkdocs gh-deploy` oder GitHub Actions Workflow

| Kriterium | Bewertung |
|-----------|-----------|
| Kosten | Kostenlos |
| Setup-Aufwand | Minimal – MkDocs hat eingebauten `gh-deploy`-Befehl |
| Custom Domain | ✅ Einfach (`CNAME`-Datei + DNS-Eintrag) |
| HTTPS | ✅ Automatisch (Let's Encrypt) |
| CI/CD | GitHub Actions Workflow (Build + Deploy bei Push) |
| CDN | GitHub CDN (schnell genug für statische Seite) |
| MkDocs-Support | Nativ – `mkdocs gh-deploy` deployt direkt auf `gh-pages`-Branch |

**Vorteile:**
- Geringster Aufwand: Ein Befehl (`mkdocs gh-deploy`) reicht für erstes Deployment
- GitHub Actions für automatisches Build+Deploy bei jedem Push
- Playwright-Tests können im CI laufen (vor Deployment)
- Kein zusätzlicher Account/Service nötig (GitHub wird bereits genutzt)

**Nachteile:**
- Repo muss public sein (oder GitHub Pro für private Pages)
- Kein serverseitiges Redirect/Rewrite

### Option B: Cloudflare Pages

**Setup:** Cloudflare-Account → Git-Repo verbinden → Build-Command konfigurieren

| Kriterium | Bewertung |
|-----------|-----------|
| Kosten | Kostenlos (Free-Tier: 500 Builds/Monat) |
| Setup-Aufwand | Mittel – Account + Build-Config + DNS-Umstellung |
| Custom Domain | ✅ Einfach (besonders wenn DNS bei Cloudflare) |
| HTTPS | ✅ Automatisch |
| CI/CD | Eingebaut (Build bei Push) |
| CDN | ✅ Cloudflare Edge-Network (weltweit schnell) |
| MkDocs-Support | Ja – Build-Command: `pip install -r requirements.txt && mkdocs build` |

**Vorteile:**
- Schnellstes CDN weltweit
- DNS + Hosting aus einer Hand möglich
- Preview-Deployments für Branches

**Nachteile:**
- Zusätzlicher Service/Account
- DNS muss bei Cloudflare liegen (oder CNAME-Setup)
- Playwright-Tests nicht direkt integrierbar (separates CI nötig)

### Option C: Netlify

**Setup:** Netlify-Account → Git-Repo verbinden → Build-Settings

| Kriterium | Bewertung |
|-----------|-----------|
| Kosten | Kostenlos (Free-Tier: 300 Build-Minuten/Monat) |
| Setup-Aufwand | Mittel – Account + Build-Config |
| Custom Domain | ✅ Einfach |
| HTTPS | ✅ Automatisch |
| CI/CD | Eingebaut |
| CDN | ✅ Netlify Edge |
| MkDocs-Support | Ja – via `runtime.txt` + Build-Command |

**Vorteile:**
- Deploy-Previews, Rollbacks
- Redirect-Regeln (`_redirects`-Datei)

**Nachteile:**
- Zusätzlicher Service/Account
- Build-Minuten begrenzt (300/Monat im Free-Tier)
- Python-Runtime muss konfiguriert werden (`runtime.txt`)

## Empfehlung: GitHub Pages

**Begründung:** Geringstes Setup, kein zusätzlicher Account, native MkDocs-Unterstützung, CI/CD über GitHub Actions für Build + Tests + Deploy. Für eine Content-Seite mit gelegentlichen Updates ist die Performance völlig ausreichend.

## Umsetzungsschritte

### Phase 1: GitHub-Repository einrichten
- [x] GitHub-Repo `fermatically` erstellen (public)
- [x] Git-Remote hinzufügen und pushen
- [x] `.gitignore` prüfen (site/ muss ignoriert sein)

### Phase 2: GitHub Actions Workflow
- [x] `.github/workflows/deploy.yml` erstellt:
  - Trigger: Push auf `main`
  - Steps: Python installieren, `pip install -r requirements.txt`, `mkdocs gh-deploy --force --strict`
- [x] Erster Push → Workflow lief → `gh-pages`-Branch wurde erstellt

### Phase 3: Custom Domain konfigurieren
- [x] `docs/CNAME`-Datei erstellt (Inhalt: `fermatically.com`)
- [x] DNS-Einträge gesetzt: 4 × A-Record bei df.eu
- [x] HTTPS in GitHub Pages Settings aktiviert
- [x] DNS-Propagation + SSL-Zertifikat abgeschlossen

### Phase 4: Verifizierung
- [x] `https://fermatically.com` aufrufen und prüfen
- [x] MathJax-Rendering testen
- [x] Navigation und Links prüfen
- [ ] Mobile Ansicht testen (optional, CSS-Overflow bei MathJax-Formeln bei 375px dokumentiert)
- [ ] Playwright-Tests gegen Live-URL laufen lassen (optional)

### Phase 5: Aufräumen
- [x] Dockerfile entfernt
- [x] `.dockerignore` entfernt
- [x] Pläne und Status aktualisiert
