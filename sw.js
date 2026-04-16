const CACHE = 'rdv-vanalytics2'; // bumped — invalide l'ancien cache
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
