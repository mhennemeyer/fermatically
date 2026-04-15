import { test, expect } from '@playwright/test';

test.describe('i18n: Sprachumschalter und zweisprachige Seiten', () => {

  test('Startseite DE: Sprachumschalter vorhanden', async ({ page }) => {
    await page.goto('/');
    const switcher = page.locator('.md-select');
    await expect(switcher).toBeVisible();
  });

  test('Startseite DE → EN: Sprachumschalter wechselt ohne 404', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/fermatically/i);

    // Sprachumschalter öffnen
    const switcherButton = page.locator('.md-select > button, .md-header__option .md-select button').first();
    await switcherButton.click();

    // English-Link klicken
    const enLink = page.locator('.md-select__link[hreflang="en"]');
    await expect(enLink).toBeVisible();
    await enLink.click();
    await page.waitForLoadState('domcontentloaded');

    // Kein 404
    await expect(page).not.toHaveTitle(/404/);
    // URL enthält /en
    expect(page.url()).toContain('/en');
    // Englischer Inhalt vorhanden
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('Startseite EN → DE: Sprachumschalter wechselt zurück ohne 404', async ({ page }) => {
    await page.goto('/en/');
    await expect(page).not.toHaveTitle(/404/);

    // Sprachumschalter öffnen
    const switcherButton = page.locator('.md-select > button, .md-header__option .md-select button').first();
    await switcherButton.click();

    // Deutsch-Link klicken
    const deLink = page.locator('.md-select__link[hreflang="de"]');
    await expect(deLink).toBeVisible();
    await deLink.click();
    await page.waitForLoadState('domcontentloaded');

    // Kein 404
    await expect(page).not.toHaveTitle(/404/);
    // URL enthält kein /en/
    expect(page.url()).not.toContain('/en/');
  });

  test('Artikel-Seite DE → EN: Sprachumschalter funktioniert', async ({ page }) => {
    await page.goto('/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');
    await expect(page).not.toHaveTitle(/404/);

    // Sprachumschalter öffnen
    const switcherButton = page.locator('.md-select > button, .md-header__option .md-select button').first();
    await switcherButton.click();

    // English-Link klicken
    const enLink = page.locator('.md-select__link[hreflang="en"]');
    await expect(enLink).toBeVisible();
    await enLink.click();
    await page.waitForLoadState('domcontentloaded');

    // Kein 404
    await expect(page).not.toHaveTitle(/404/);
    expect(page.url()).toContain('/en');
    // Gleicher Artikel in EN
    expect(page.url()).toContain('01-was-ist-flt');
  });

  test('EN Startseite: Seite lädt korrekt', async ({ page }) => {
    await page.goto('/en/');
    await expect(page).not.toHaveTitle(/404/);
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('EN Artikel: Seite lädt korrekt', async ({ page }) => {
    await page.goto('/en/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');
    await expect(page).not.toHaveTitle(/404/);
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('Alle EN-Hauptseiten laden ohne 404', async ({ page }) => {
    const enPages = [
      '/en/',
      '/en/about/',
      '/en/quellen/',
      '/en/vorwissen/',
      '/en/grundlagen/elementare-zahlentheorie/',
      '/en/werkzeuge/',
      '/en/fermat-wiles/',
    ];

    for (const url of enPages) {
      const response = await page.goto(url);
      expect(response?.status(), `${url} should not be 404`).not.toBe(404);
    }
  });

});
