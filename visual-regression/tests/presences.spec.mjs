// Visual regression — Presences
// Couvre le Bug #5 (noms joueurs qui ecrasent le bouton Present sur mobile).
import { test, expect } from '@playwright/test';
import { setupPage, loginAsCoach, gotoTab } from '../fixtures/helpers.mjs';

test.describe('Presences', () => {
  test.beforeEach(async ({ page }) => {
    await setupPage(page);
    await loginAsCoach(page);
    await gotoTab(page, 'presences');
  });

  test('screenshot — default presences view', async ({ page }) => {
    await expect(page).toHaveScreenshot('presences-default.png', { fullPage: true });
  });

  test('long player names never overlap the Present button (Bug #5)', async ({ page }) => {
    // Inject un joueur avec nom tres long pour verifier truncature ellipsis
    await page.evaluate(() => {
      if (window.S && Array.isArray(window.S.players)) {
        window.S.players.push({
          id: 999,
          number: 99,
          name: 'Kylian-Mbappe-Cardozo-Gonzalez-Alberto Van Der Berg',
          position: 'FW',
          birthdate: '2000-01-01',
        });
        window.renderPresences && window.renderPresences();
      }
    });
    await page.waitForTimeout(150);

    // Trouve la ligne correspondante et verifie que le nom et le bouton "Present"
    // ne se chevauchent pas.
    const bbox = await page.locator('.roster-row:has-text("Kylian-Mbappe")').first().evaluate((row) => {
      const name = row.querySelector('.roster-name');
      const btn = row.querySelector('.btn-present, [data-action="present"]');
      if (!name || !btn) return null;
      const n = name.getBoundingClientRect();
      const b = btn.getBoundingClientRect();
      return { nameRight: n.right, btnLeft: b.left, nameText: name.textContent };
    });

    expect(bbox, 'roster row avec btn Present requis').not.toBeNull();
    expect(bbox.nameRight, 'le nom doit finir AVANT le bouton Present').toBeLessThanOrEqual(bbox.btnLeft);

    // Et le nom doit etre tronque avec ellipsis
    const hasEllipsis = await page.locator('.roster-row:has-text("Kylian-Mbappe") .roster-name').first().evaluate((el) => {
      const s = getComputedStyle(el);
      return s.textOverflow === 'ellipsis' && (s.overflow === 'hidden' || s.overflowX === 'hidden');
    });
    expect(hasEllipsis, '.roster-name doit avoir text-overflow:ellipsis + overflow:hidden').toBe(true);

    // Screenshot avec le long nom
    await expect(page).toHaveScreenshot('presences-long-name.png', { fullPage: true });
  });
});
