# Plan: GitHub Pages Go-Live

Erstellt: 2026-04-14
Status: In Arbeit (Schritte 1–3 erledigt)

## Erledigt
- [x] GitHub-Repo `fermatically` erstellt (public)
- [x] Git-Remote hinzugefügt und gepusht
- [x] GitHub Pages aktiviert (Source: GitHub Actions)

## Nächste Schritte

### 4. Custom Domain eintragen
- [ ] GitHub Repo → **Settings** → **Pages** → Custom domain: `fermatically.com` eingeben → **Save**
- [ ] **Enforce HTTPS** aktivieren (ggf. erst nach DNS-Propagation möglich)

### 5. DNS-Einträge setzen (beim Domain-Registrar)
```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  <username>.github.io
```

### 6. Warten & Prüfen
- [ ] DNS-Propagation abwarten (meistens unter 1 Std, max 48 Std)
- [ ] `https://fermatically.com` aufrufen und prüfen:
  - Seite lädt
  - MathJax-Formeln rendern
  - Navigation funktioniert
  - HTTPS-Schloss im Browser

### 7. Aufräumen
- [ ] `Dockerfile` löschen
- [ ] `.dockerignore` löschen
- [ ] `deployment-plan.md` als erledigt markieren
- [ ] `artikelserie-plan.md` Punkt #17 als erledigt markieren
- [ ] `status.md` aktualisieren
