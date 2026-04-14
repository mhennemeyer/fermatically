import { test, expect } from '@playwright/test';
import { expectMathJaxRendered } from './helpers/mathjax';
import { expectSidebarVisible } from './helpers/navigation';

test.describe('Smoke-Tests: Seiten laden korrekt', () => {

  test('Landing Page: Titel und Navigation', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle(/fermatically/i);

    // Navigation sichtbar (MkDocs Material Tabs oder Sidebar)
    const nav = page.locator('.md-tabs, .md-nav--primary');
    await expect(nav.first()).toBeVisible();
  });

  test('Landing Page: Theme-Toggle vorhanden', async ({ page }) => {
    await page.goto('/');
    const toggle = page.locator('[data-md-component="palette"] button, form.md-header__option label');
    await expect(toggle.first()).toBeVisible();
  });

  test('Grundlagen-Artikel: Seite lädt und hat Überschrift', async ({ page }) => {
    await page.goto('/grundlagen/elementare-zahlentheorie/01-was-ist-flt/');
    await expect(page).not.toHaveTitle(/404/);

    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
    await expect(heading).not.toBeEmpty();
  });

  test('Grundlagen-Artikel: MathJax rendert Formeln', async ({ page }) => {
    await page.goto('/grundlagen/elementare-zahlentheorie/02-beweis-n4/');
    await expectMathJaxRendered(page);
  });

  test('Vorwissen-Seite: Seite lädt und Admonitions gerendert', async ({ page }) => {
    await page.goto('/vorwissen/teilbarkeit-ggt/');
    await expect(page).not.toHaveTitle(/404/);

    // MkDocs Material Admonitions haben die Klasse .admonition oder details
    const admonitions = page.locator('.admonition, details, .md-typeset .admonition');
    const count = await admonitions.count();
    // Es ist OK wenn keine Admonitions vorhanden sind, aber Seite muss laden
    if (count > 0) {
      await expect(admonitions.first()).toBeVisible();
    }
  });

  test('Navigation: Sidebar vorhanden und klickbar', async ({ page }) => {
    await page.goto('/');
    await expectSidebarVisible(page);

    // Klick auf einen Navigationslink
    const navLink = page.locator('.md-nav a[href*="grundlagen"], .md-tabs a[href*="grundlagen"]').first();
    await expect(navLink).toBeVisible();
    await navLink.click();
    await page.waitForLoadState('domcontentloaded');
    expect(page.url()).toContain('grundlagen');
  });

});
