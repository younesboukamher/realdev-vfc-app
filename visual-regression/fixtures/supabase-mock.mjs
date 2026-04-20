// Stub Supabase pour Playwright.
// Intercepte tous les appels a jgytwvtdqpotdaleotok.supabase.co et retourne
// des fixtures deterministes. Le test reste ainsi 100% offline.
//
// Couvre : auth, REST (select/insert/update/upsert), realtime (WebSocket rejete),
// Edge Functions (204).

import { fixtures } from './fixtures.mjs';

const SUPA_HOST = 'jgytwvtdqpotdaleotok.supabase.co';

function jsonResponse(body, status = 200, extra = {}) {
  return {
    status,
    contentType: 'application/json',
    body: JSON.stringify(body),
    headers: { 'content-range': '0-' + (Array.isArray(body) ? body.length : 1) + '/*', ...extra },
  };
}

// Tres petit parseur de la query REST Supabase.
// Retourne { table, eqFilters, selectCols, order, limit, method }
function parseSupaReq(url, method) {
  const u = new URL(url);
  const parts = u.pathname.split('/');
  const table = parts[parts.length - 1];
  const eq = [];
  for (const [k, v] of u.searchParams.entries()) {
    if (v.startsWith('eq.')) eq.push([k, v.slice(3)]);
  }
  return { table, eq, method };
}

export async function installSupabaseMock(page, options = {}) {
  const data = { ...fixtures, ...(options.override || {}) };

  // 1) Realtime WebSocket : on laisse echouer silencieusement (l'app a un try/catch).
  await page.route(`https://${SUPA_HOST}/realtime/v1/**`, (route) => route.abort());

  // 2) Auth
  await page.route(`https://${SUPA_HOST}/auth/v1/**`, async (route) => {
    const req = route.request();
    const url = req.url();
    if (url.includes('/token')) {
      // Login
      return route.fulfill(jsonResponse({
        access_token: 'test-access',
        refresh_token: 'test-refresh',
        token_type: 'bearer',
        expires_in: 3600,
        user: data.authUser,
      }));
    }
    if (url.includes('/user')) {
      return route.fulfill(jsonResponse(data.authUser));
    }
    if (url.includes('/recover') || url.includes('/logout')) {
      return route.fulfill(jsonResponse({}, 204));
    }
    return route.fulfill(jsonResponse({}));
  });

  // 3) REST
  await page.route(`https://${SUPA_HOST}/rest/v1/**`, async (route) => {
    const req = route.request();
    const method = req.method();
    const parsed = parseSupaReq(req.url(), method);
    const table = parsed.table;
    let rows = data[table] || [];

    // Applique eq filters
    for (const [col, val] of parsed.eq) {
      rows = rows.filter((r) => String(r[col]) === val);
    }

    if (method === 'GET') return route.fulfill(jsonResponse(rows));
    if (method === 'POST' || method === 'PATCH' || method === 'PUT') {
      return route.fulfill(jsonResponse(rows.length ? rows[0] : {}, 201));
    }
    if (method === 'DELETE') return route.fulfill(jsonResponse({}, 204));
    return route.fulfill(jsonResponse({}));
  });

  // 4) Edge Functions
  await page.route(`https://${SUPA_HOST}/functions/v1/**`, (route) =>
    route.fulfill(jsonResponse({ ok: true }))
  );

  // 5) Storage (public URLs : laisse passer ; signed : stub)
  await page.route(`https://${SUPA_HOST}/storage/v1/object/sign/**`, (route) =>
    route.fulfill(jsonResponse({ signedURL: 'about:blank' }))
  );
}
