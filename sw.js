/* ComDraft — service worker cho phép ôn tập khi không có mạng.
   Đổi PHIEN_BAN mỗi lần phát hành để trình duyệt tải lại tài nguyên mới.
   © Đỗ Thùy Hương, 2026. */
const PHIEN_BAN = 'comdraft-v3';

const VO = [
  './',
  './index.html',
  './manifest.webmanifest',
  './assets/css/style.css',
  './assets/js/app.js',
  './assets/js/i18n.js',
  './assets/icons/persona.png',
  './assets/icons/co-huong-dung.png',
  './assets/icons/co-huong-di.png',
  './assets/icons/co-huong-ipad.png',
  './data/lectures.js',
  './assets/icons/favicon-32.png',
  './assets/icons/apple-touch-icon.png',
  './assets/icons/icon-192.png',
  './assets/icons/icon-512.png',
  './data/ch1.js',
  './data/ch2.js',
  './data/ch3.js',
  './data/ch4.js',
  './data/ch5.js'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(PHIEN_BAN)
      .then((c) => c.addAll(VO))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((ds) => Promise.all(ds.filter((k) => k !== PHIEN_BAN).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Ưu tiên bản đã lưu để mở nhanh và chạy được khi mất mạng; nếu chưa có thì lấy
// từ mạng rồi lưu lại cho lần sau.
self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const u = new URL(e.request.url);
  if (u.origin !== location.origin) return;
  e.respondWith(
    caches.match(e.request).then((san) => san || fetch(e.request).then((res) => {
      if (res && res.ok) {
        const ban = res.clone();
        caches.open(PHIEN_BAN).then((c) => c.put(e.request, ban));
      }
      return res;
    }).catch(() => caches.match('./index.html')))
  );
});
