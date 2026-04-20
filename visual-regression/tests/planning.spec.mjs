// Visual regression — Planning
// Couvre Bug #3 (Planning ouvre sur match passe) et Bug #4 (Calendrier mois
// ne montre que les matchs — feature Pl2 cassee).
import { test, expect } from '@playwright/test';
import { setupPage, loginAsCoach, gotoTab } from '../fixtures/helpers.mjs';

test.describe('Planning', () => {
  test.beforeEach(async ({ page }) => {
    await setupPage(page);
    await loginAsCoach(page);
    await gotoTab(page, 'planning');
  });

  test('opens on the next match, not a past one', async ({ page }) => {
    // Fixture : J17 futur, J16 passe
    const body = await page.textContent('body');
    expect(body).toContain('J17');

    // Le titre ou selecteur courant de Planning ne doit pas pointer sur J16
    const currentMatchTitle = await page.locator('.plan-current, .plan-header, [data-plan-title]').first().textContent().catch(() => '');
    if (currentMatchTitle) expect(currentMatchTitle).not.toContain('J16');
  });

  test('screenshot — planning main view', async ({ page }) => {
    await expect(page).toHaveScreenshot('planning-main.png', { fullPage: true });
  });

  test('calendar month view shows sessions (not only matches)', async ({ page }) => {
    // Clique sur l'onglet/bouton vue "mois" (Pl2 - Sprint 5)
    const monthBtn = page.locator('[data-view="month"], #pl-view-month, button:has-text("Mois")').first();
    if (await monthBtn.isVisible().catch(() => false)) {
      await monthBtn.click();
      await page.waitForTimeout(200);
    }

    // Count session dots : doit etre > 0 (bug #4 les mettait a 0)
    const sessionDots = await page.locator('.cal-session-dot, .pl2-session-dot, [data-session-dot]').count();
    expect(sessionDots, 'Calendrier mois doit afficher des pastilles de seances').toBeGreaterThan(0);

    // Screenshot baseline
    await expect(page).toHaveScreenshot('planning-calendar-month.png', { fullPage: true });
  });
});
