(function () {
  var t = document.querySelector('.nav-toggle');
  var m = document.getElementById('menu');
  if (!t || !m) return;
  t.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  m.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () { m.classList.remove('open'); t.setAttribute('aria-expanded', 'false'); });
  });
})();


// Home video band: a crafting clip and a gaming clip that cross-fade and loop as a pair.
// Nothing downloads until the band is near the viewport, and phones get the smaller files.
(function () {
  var vids = Array.prototype.slice.call(document.querySelectorAll('.party-video[data-src]'));
  if (!vids.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var small = window.matchMedia('(max-width: 900px)').matches;
  function load(v) {
    if (v.getAttribute('src')) return;
    v.src = (small && v.getAttribute('data-src-small')) || v.getAttribute('data-src');
    v.preload = 'auto'; v.load();
  }
  function show(i) {
    var v = vids[i], next = vids[(i + 1) % vids.length];
    load(v);
    try { v.currentTime = 0; } catch (e) {}
    var p = v.play(); if (p && p.catch) p.catch(function () {});
    vids.forEach(function (o) { o.classList.toggle('is-on', o === v); });
    v.onplaying = function () { load(next); };
    v.onended = function () { show((i + 1) % vids.length); };
  }
  if (!('IntersectionObserver' in window)) { show(0); return; }
  var io = new IntersectionObserver(function (entries) {
    if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); show(0); }
  }, { rootMargin: '600px 0px' });
  io.observe(vids[0].parentNode);
})();
