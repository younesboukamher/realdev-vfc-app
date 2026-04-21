const CACHE = 'rdv-v29'; // bump lean sprint 2 2026-04-21: Home 3 sections + alertes collapsed
const APP_VERSION = '1.18.0';
const STATIC = ['/realdev-vfc-app/', '/realdev-vfc-app/index.html'];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE).then(c =>
      Promise.all(STATIC.map(u => fetch(u, {cache:'no-store'}).then(r => c.put(u, r)).catch(()=>{})))
    )
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
      .then(() => self.clients.matchAll().then(clients => clients.forEach(c => c.navigate(c.url))))
  );
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  
  // Supabase — toujours réseau
  if (url.hostname.includes('supabase.co')) return;
  
  // Fonts Google — cache long
  if (url.hostname.includes('fonts')) {
    e.respondWith(caches.match(e.request).then(c => c || fetch(e.request)));
    return;
  }

  // HTML — toujours réseau en priorité (pas de cache stale)
  if (e.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/')) {
    e.respondWith(
      fetch(e.request, {cache:'no-store'})
        .then(r => { caches.open(CACHE).then(c => c.put(e.request, r.clone())); return r; })
        .catch(() => caches.match(e.request))
    );
    return;
  }

  // Autres assets — cache first
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request).then(r => {
      if (r.ok) caches.open(CACHE).then(c => c.put(e.request, r.clone()));
      return r;
    }))
  );
});


// P3 — Web Push handlers (Sprint 5)
self.addEventListener('push', (event) => {
  let data = {};
  try{ data = event.data ? event.data.json() : {}; }catch(_){ data = { title: 'RealDev VFC', body: event.data ? event.data.text() : '' }; }
  const title = data.title || 'RealDev VFC';
  const options = {
    body: data.body || '',
    icon: data.icon || '/realdev-vfc-app/icon-192.png',
    badge: data.badge || '/realdev-vfc-app/icon-192.png',
    data: { url: data.url || '/realdev-vfc-app/?page=planning' },
    tag: data.tag || 'rdv-session-reminder',
    renotify: true
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const target = (event.notification.data && event.notification.data.url) || '/realdev-vfc-app/?page=planning';
  event.waitUntil(
    clients.matchAll({ type:'window', includeUncontrolled:true }).then(list => {
      for (const c of list) {
        if (c.url.includes('/realdev-vfc-app/') && 'focus' in c) { c.navigate(target); return c.focus(); }
      }
      if (clients.openWindow) return clients.openWindow(target);
    })
  );
});
