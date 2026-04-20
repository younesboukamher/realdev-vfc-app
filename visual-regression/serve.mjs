// Serveur statique minimal pour servir index.html local.
// Usage : INDEX_PATH=/chemin/vers/realdev-vfc-app node serve.mjs
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, resolve, extname } from 'node:path';

const ROOT = resolve(process.env.INDEX_PATH || '../realdev-vfc-app');
const PORT = Number(process.env.PORT || 4173);

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js':   'application/javascript; charset=utf-8',
  '.mjs':  'application/javascript; charset=utf-8',
  '.css':  'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.ico':  'image/x-icon',
  '.webmanifest': 'application/manifest+json',
};

const server = createServer(async (req, res) => {
  try {
    let urlPath = decodeURIComponent((req.url || '/').split('?')[0]);
    if (urlPath === '/' || urlPath === '') urlPath = '/index.html';
    // Evite path traversal
    if (urlPath.includes('..')) { res.writeHead(400); return res.end('nope'); }
    const filePath = join(ROOT, urlPath);
    const st = await stat(filePath).catch(() => null);
    if (!st || !st.isFile()) {
      res.writeHead(404);
      return res.end('not found: ' + urlPath);
    }
    const body = await readFile(filePath);
    res.writeHead(200, {
      'content-type': MIME[extname(filePath).toLowerCase()] || 'application/octet-stream',
      'cache-control': 'no-store',
    });
    res.end(body);
  } catch (e) {
    res.writeHead(500);
    res.end('serve error: ' + e.message);
  }
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`[serve] root=${ROOT}  listening on http://127.0.0.1:${PORT}`);
});
