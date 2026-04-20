// Helpers communs aux tests visuels.
import { installSupabaseMock } from './supabase-mock.mjs';
import { fixtures } from './fixtures.mjs';

// Prepare la page :
// - freeze Date.now() a la date de la fixture pour stabiliser les screenshots
// - stub Supabase
// - stub service worker register (evite de voir la biblio sw.js casser la page en test)
// - force le theme (pas de flicker dark/light)
// - disable CSS animations
export async function setupPage(page, { theme = 'dark', frozen = true } = {}) {
  await installSupabaseMock(page);

  await page.addInitScript(({ date, theme, frozen }) => {
    if (frozen) {
      const FROZEN = new Date(date + 'T12:00:00').getTime();
      // Geler Date() sans casser les usages (new Date('2026-04-25') doit marcher)
      const OrigDate = Date;
      class FrozenDate extends OrigDate {
        constructor(...args) {
          if (args.length === 0) super(FROZEN);
          else super(...args);
        }
        static now() { return FROZEN; }
      }
      // eslint-disable-next-line no-global-assign
      Date = FrozenDate;
    }

    // Pas de SW pendant les tests
    if ('serviceWorker' in navigator) {
      Object.defineProperty(navigator, 'serviceWorker', {
        value: { register: () => Promise.resolve(), ready: Promise.resolve() },
        configurable: true,
      });
    }

    // Theme
    try { localStorage.setItem('rdv_theme', theme); } catch(_) {}

    // Kill all animations/transitions
    const style = document.createElement('style');
    style.textContent = `
      *, *::before, *::after {
        animation-duration: 0s !important;
        animation-delay: 0s !important;
        transition-duration: 0s !important;
        transition-delay: 0s !important;
      }
    `;
    (document.head || document.documentElement).appendChild(style);
  }, { date: fixtures.TODAY, theme, frozen });
}

// Se logger puis attendre que l'app soit visible.
export async function loginAsCoach(page) {
  await page.goto('/');
  // Splash peut etre affiche ; attendre login OU app
  await page.waitForSelector('#scr-login, #app', { timeout: 10_000 });
  const loginVisible = await page.locator('#scr-login').isVisible().catch(() => false);
  if (loginVisible) {
    await page.locator('#login-email').fill('coach@rdv.test');
    await page.locator('#login-pwd').fill('test-password');
    await page.locator('#btn-login').click();
    await page.waitForSelector('#app', { state: 'visible', timeout: 10_000 });
  }
  // Attendre fin du premier render
  await page.waitForFunction(() => !!window.S && Array.isArray(window.S.players));
  // Petite pause deterministe pour laisser requestAnimationFrame se stabiliser
  await page.waitForTimeout(100);
}

export async function gotoTab(page, tab) {
  // Les onglets sont declenchables via nav-<tab>
  const sel = `#nav-staff [data-tab="${tab}"], [data-tab="${tab}"]`;
  await page.locator(sel).first().click();
  await page.waitForTimeout(100);
}
