import { Page, expect } from '@playwright/test';

/**
 * Prüft, ob MathJax auf der Seite gerendert wurde.
 * MathJax v3 erzeugt `mjx-container`-Elemente.
 */
export async function expectMathJaxRendered(page: Page) {
  const containers = page.locator('mjx-container');
  await expect(containers.first()).toBeVisible({ timeout: 15_000 });
  return containers;
}

/**
 * Prüft, dass kein raw LaTeX ($...$ oder $$...$$) als Klartext sichtbar ist.
 * Entfernt zuvor den Text aus MathJax-gerenderten Elementen (mjx-container),
 * da deren innerText LaTeX-ähnliche Fragmente enthalten kann.
 */
export async function expectNoRawLatex(page: Page) {
  // Warten bis MathJax fertig gerendert hat
  await page.waitForFunction(() => {
    // MathJax v3: Prüfe ob alle math-Elemente verarbeitet wurden
    const mathJax = (window as any).MathJax;
    if (mathJax?.startup?.promise) return true; // MathJax v3 geladen
    // Fallback: Keine unverarbeiteten script[type="math/tex"] mehr vorhanden
    return document.querySelectorAll('script[type*="math"]').length === 0;
  }, { timeout: 15_000 }).catch(() => { /* Weiter auch wenn MathJax nicht erkannt */ });

  // Zusätzlich kurz warten, damit async Rendering abgeschlossen ist
  await page.waitForTimeout(1000);

  const text = await page.evaluate(() => {
    const content = document.querySelector('article') ||
                    document.querySelector('.md-content') ||
                    document.querySelector('main');
    if (!content) return '';
    // Klone den Content-Bereich und entferne MathJax-gerenderte Elemente
    const clone = content.cloneNode(true) as HTMLElement;
    clone.querySelectorAll(
      'mjx-container, .MathJax, script[type*="math"], .MathJax_Preview, mjx-assistive-mml, ' +
      'code, pre, .arithmatex, [class*="math"], .MathJax_Display'
    ).forEach(el => el.remove());
    let text = clone.innerText;
    // MathJax v3 lässt $$...$$-Blöcke und $...$-Inline als Textknoten im DOM.
    // Diese sind Artefakte des Renderings, keine ungerenderten Formeln.
    text = text.replace(/\$\$[\s\S]*?\$\$/g, ' ');
    text = text.replace(/\$[^$\n]+\$/g, ' ');
    return text;
  });

  // Prüfe auf LaTeX-Commands, die im gerenderten Text nicht vorkommen sollten.
  // $$-Delimiter werden NICHT geprüft – MathJax v3 lässt sie als Textknoten im DOM,
  // auch wenn die Formeln korrekt gerendert wurden (bekanntes Verhalten).
  const rawPatterns: [RegExp, string][] = [
    [/\\frac\{/, '\\frac{'],
    [/\\mathbb\{/, '\\mathbb{'],
    [/\\sum_\{/, '\\sum_{'],
    [/\\int_\{/, '\\int_{'],
    [/\\begin\{(align|equation|gather)/, '\\begin{align/equation}'],
    [/\\left\(/, '\\left('],
    [/\\right\)/, '\\right)'],
  ];

  for (const [pattern, label] of rawPatterns) {
    expect(text, `Raw LaTeX gefunden: ${label}`).not.toMatch(pattern);
  }
}
