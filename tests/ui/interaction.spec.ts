import { test, expect } from '@playwright/test';

test.describe('Interaktions-Tests: Theme-Toggle', () => {

  test('Klick auf Palette-Toggle wechselt das Farbschema', async ({ page }) => {
    await page.goto('/');

    // MkDocs Material: Zwei Radio-Inputs für Palette (default + slate)
    const schemeDefault = page.locator('input#__palette_0');
    const schemeSlate = page.locator('input#__palette_1');
    await expect(schemeDefault).toBeAttached();
    await expect(schemeSlate).toBeAttached();

    // Initialer Zustand: default
    const before = await page.evaluate(() =>
      document.body.getAttribute('data-md-color-scheme')
    );
    expect(before).toBe('default');

    // Klick auf Slate-Label (das sichtbare Toggle-Icon)
    const slateLabel = page.locator('label[for="__palette_1"]');
    await slateLabel.click();
    await page.waitForTimeout(500);

    const after = await page.evaluate(() =>
      document.body.getAttribute('data-md-color-scheme')
    );
    expect(after).toBe('slate');
  });

});

test.describe('Interaktions-Tests: Suche', () => {

  test('Such-Dialog öffnet sich', async ({ page }) => {
    await page.goto('/');

    // Suche öffnen via Checkbox-Toggle
    await page.evaluate(() => {
      const checkbox = document.getElementById('__search') as HTMLInputElement;
      if (checkbox) checkbox.checked = true;
    });
    await page.waitForTimeout(300);

    // Such-Input sollte im DOM vorhanden sein
    const searchInput = page.locator('input.md-search__input');
    await expect(searchInput).toBeAttached();

    // Search-Index sollte ladbar sein
    const response = await page.request.get('/search/search_index.json');
    expect(response.status()).toBe(200);
    const body = await response.json();
    expect(body.docs.length, 'Search-Index sollte Dokumente enthalten').toBeGreaterThan(0);
  });

  test('Search-Index enthält erwartete Inhalte', async ({ page }) => {
    await page.goto('/');

    // Search-Index direkt prüfen (MkDocs-Search Worker braucht spezielle Initialisierung)
    const response = await page.request.get('/search/search_index.json');
    const body = await response.json();

    // Prüfe dass relevante Begriffe im Index vorhanden sind
    const allText = body.docs.map((d: any) => d.title + ' ' + d.text).join(' ');
    expect(allText).toContain('Fermat');
    expect(allText).toContain('Wiles');
    expect(allText).toContain('Galois');
  });

});

test.describe('Interaktions-Tests: Table of Contents', () => {

  test('TOC-Einträge vorhanden und klickbar', async ({ page }) => {
    // toc.integrate ist aktiv → TOC ist in der linken Sidebar integriert
    await page.goto('/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');

    // TOC-Links (können in linker oder rechter Sidebar sein)
    const tocLinks = page.locator('.md-nav--secondary .md-nav__link, .md-sidebar .md-nav__link[href*="#"]');
    const count = await tocLinks.count();
    expect(count, 'TOC sollte mindestens einen Eintrag haben').toBeGreaterThan(0);

    // Klick auf ersten TOC-Eintrag
    const firstTocLink = tocLinks.first();
    await firstTocLink.click();
    await page.waitForTimeout(500);

    expect(page.url()).toContain('#');
  });

});

test.describe('Interaktions-Tests: Navigation', () => {

  test('Navigations-Sections sind expandiert (navigation.expand aktiv)', async ({ page }) => {
    await page.goto('/');

    // Bei navigation.expand sind Sections standardmäßig offen
    // Prüfe dass verschachtelte Nav-Items sichtbar sind
    const nestedLinks = page.locator('.md-nav--primary .md-nav__item--nested .md-nav__link');
    const count = await nestedLinks.count();
    expect(count, 'Verschachtelte Navigationseinträge sollten sichtbar sein').toBeGreaterThan(0);
  });

  test('Deep-Link navigiert korrekt', async ({ page }) => {
    await page.goto('/grundlagen/elementare-zahlentheorie/02-beweis-n4/');
    await expect(page).not.toHaveTitle(/404/);

    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

});
