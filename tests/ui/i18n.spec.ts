import { test, expect } from '@playwright/test';

test.describe('i18n: Sprachumschalter und zweisprachige Seiten', () => {

  test('Startseite EN: Sprachumschalter vorhanden', async ({ page }) => {
    await page.goto('/');
    const switcher = page.locator('.md-select');
    await expect(switcher).toBeVisible();
  });

  test('Startseite EN → DE: Sprachumschalter wechselt ohne 404', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/fermatically/i);

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
    // URL enthält /de
    expect(page.url()).toContain('/de');
    // Deutscher Inhalt vorhanden
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('Startseite DE → EN: Sprachumschalter wechselt zurück ohne 404', async ({ page }) => {
    await page.goto('/de/');
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
    // URL enthält kein /de/
    expect(page.url()).not.toContain('/de/');
  });

  test('Artikel-Seite EN → DE: Sprachumschalter funktioniert', async ({ page }) => {
    await page.goto('/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');
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
    expect(page.url()).toContain('/de');
    // Gleicher Artikel in DE
    expect(page.url()).toContain('01-was-ist-flt');
  });

  test('DE Startseite: Seite lädt korrekt', async ({ page }) => {
    await page.goto('/de/');
    await expect(page).not.toHaveTitle(/404/);
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('DE Artikel: Seite lädt korrekt', async ({ page }) => {
    await page.goto('/de/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');
    await expect(page).not.toHaveTitle(/404/);
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
  });

  test('Alle DE-Hauptseiten laden ohne 404', async ({ page }) => {
    const dePages = [
      '/de/',
      '/de/about/',
      '/de/quellen/',
      '/de/vorwissen/',
      '/de/grundlagen/elementare-zahlentheorie/',
      '/de/werkzeuge/',
      '/de/fermat-wiles/',
    ];

    for (const url of dePages) {
      const response = await page.goto(url);
      expect(response?.status(), `${url} should not be 404`).not.toBe(404);
    }
  });

});
