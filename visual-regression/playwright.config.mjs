// Playwright config — visual regression pour RealDev VFC
// Servi localement sur http://127.0.0.1:4173, Supabase stubbé via page.route().
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  fullyParallel: false, // une seule app, screenshots deterministes
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  reporter: [['list'], ['html', { outputFolder: 'playwright-report', open: 'never' }]],

  // Baseline screenshots compares. Tolerance ajustable par test.
  expect: {
    toHaveScreenshot: { maxDiffPixels: 120, threshold: 0.15, animations: 'disabled' }
  },

  use: {
    baseURL: 'http://127.0.0.1:4173',
    viewport: { width: 402, height: 874 }, // iPhone 17 Pro portrait
    deviceScaleFactor: 2,
    hasTouch: true,
    isMobile: true,
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    locale: 'fr-FR',
    timezoneId: 'Europe/Brussels',
  },

  projects: [
    { name: 'iphone-17-pro', use: { ...devices['iPhone 14 Pro'] } },
    // Ajouter desktop / tablet au besoin.
    // { name: 'desktop', use: { ...devices['Desktop Chrome'], viewport: { width: 1280, height: 800 } } },
  ],

  webServer: {
    command: 'node serve.mjs',
    url: 'http://127.0.0.1:4173',
    reuseExistingServer: !process.env.CI,
    timeout: 10_000,
  },
});
