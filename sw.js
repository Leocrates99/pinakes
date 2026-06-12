/* Pinakes — Service Worker
   Strategia:
   - App shell (HTML, icone, manifest): cache-first  -> apertura istantanea e uso offline
   - Navigazioni: network-first con fallback alla shell in cache
   - Librerie/font da CDN (Chart.js, Quagga, Google Fonts): stale-while-revalidate
   - Lookup ISBN (Google Books / Open Library) e copertine: solo rete, mai in cache
   Bump SHELL_CACHE quando cambi index.html o gli asset locali. */
const SHELL_CACHE = 'pinakes-shell-v9';
const RUNTIME_CACHE = 'pinakes-runtime-v9';

const SHELL_ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon.svg',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon-32.png'
];

// host le cui risposte servono offline (librerie e font)
const RUNTIME_HOSTS = ['cdnjs.cloudflare.com', 'cdn.jsdelivr.net', 'fonts.googleapis.com', 'fonts.gstatic.com'];
// host che devono SEMPRE andare in rete (API e copertine): non sporcano la cache
const NETWORK_ONLY_HOSTS = [
  'www.googleapis.com', 'openlibrary.org', 'covers.openlibrary.org',
  'books.google.com', 'books.googleusercontent.com'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(SHELL_CACHE)
      .then((c) => c.addAll(SHELL_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== SHELL_CACHE && k !== RUNTIME_CACHE).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('message', (e) => {
  if (e.data === 'skipWaiting') self.skipWaiting();
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  let url;
  try { url = new URL(req.url); } catch { return; }

  // API e copertine: passthrough alla rete (se offline falliscono, l'app lo gestisce)
  if (NETWORK_ONLY_HOSTS.includes(url.hostname)) return;

  // Navigazione: prova la rete, altrimenti la shell in cache
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).catch(() => caches.match('./index.html')));
    return;
  }

  // Asset locali: cache-first
  if (url.origin === self.location.origin) {
    e.respondWith(caches.match(req).then((r) => r || fetch(req)));
    return;
  }

  // Librerie/font CDN: stale-while-revalidate
  if (RUNTIME_HOSTS.includes(url.hostname)) {
    e.respondWith(
      caches.open(RUNTIME_CACHE).then(async (cache) => {
        const cached = await cache.match(req);
        const network = fetch(req)
          .then((resp) => {
            if (resp && (resp.status === 200 || resp.type === 'opaque')) cache.put(req, resp.clone());
            return resp;
          })
          .catch(() => cached);
        return cached || network;
      })
    );
  }
});
