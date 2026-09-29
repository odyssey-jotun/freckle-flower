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


// The party clip only downloads once it is close to the viewport.
(function () {
  var v = document.querySelector('.party-video[data-src]');
  if (!v) return;
  function start() { v.src = v.getAttribute('data-src'); v.removeAttribute('data-src'); v.autoplay = true; v.load(); var p = v.play(); if (p && p.catch) p.catch(function () {}); }
  if (!('IntersectionObserver' in window)) { start(); return; }
  var io = new IntersectionObserver(function (entries) { if (entries.some(function (e) { return e.isIntersecting; })) { io.disconnect(); start(); } }, { rootMargin: '600px 0px' });
  io.observe(v);
})();
