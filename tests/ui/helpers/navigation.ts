import { Page, expect } from '@playwright/test';

/**
 * Prüft, dass die MkDocs Material Sidebar-Navigation sichtbar ist.
 */
export async function expectSidebarVisible(page: Page) {
  const sidebar = page.locator('.md-sidebar--primary nav, .md-nav--primary');
  await expect(sidebar.first()).toBeVisible();
  return sidebar;
}

/**
 * Prüft, dass ein Navigationslink existiert und zur erwarteten URL führt.
 */
export async function clickNavLinkAndVerify(page: Page, linkText: string, expectedUrlPart: string) {
  const navLink = page.locator('.md-nav a', { hasText: linkText }).first();
  await expect(navLink).toBeVisible();
  await navLink.click();
  await page.waitForLoadState('domcontentloaded');
  expect(page.url()).toContain(expectedUrlPart);
}

/**
 * Sammelt alle internen Links auf der aktuellen Seite.
 */
export async function collectInternalLinks(page: Page): Promise<string[]> {
  return page.evaluate(() => {
    const anchors = document.querySelectorAll('a[href]');
    const currentUrl = window.location.href;
    const origin = window.location.origin;
    const links: string[] = [];
    anchors.forEach(a => {
      const href = a.getAttribute('href') || '';
      // Externe Links und Anker-nur-Links ignorieren
      if (href.startsWith('http') && !href.startsWith(origin)) return;
      if (href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('javascript:')) return;
      try {
        // Relative Links gegen aktuelle Seiten-URL auflösen
        const url = new URL(href, currentUrl);
        if (url.origin === origin) {
          links.push(url.pathname);
        }
      } catch { /* ungültige URLs ignorieren */ }
    });
    return [...new Set(links)];
  });
}
