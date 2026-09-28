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

// Scroll-scrubbed video: the party clip plays forward as the page scrolls down
// through its section and rewinds on the way back up.
(function () {
  var outer = document.querySelector('.party-outer');
  var video = document.querySelector('.party-video');
  if (!outer || !video) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var ready = false, target = 0, ticking = false;
  function measure() {
    var r = outer.getBoundingClientRect();
    var range = r.height - window.innerHeight;
    if (range <= 0) return 0;
    var p = -r.top / range;
    return p < 0 ? 0 : p > 1 ? 1 : p;
  }
  function apply() {
    ticking = false;
    if (!ready || !video.duration) return;
    var t = target * video.duration;
    if (Math.abs(video.currentTime - t) > 0.02) video.currentTime = t;
  }
  function onScroll() {
    target = measure();
    if (!ticking) { ticking = true; window.requestAnimationFrame(apply); }
  }
  video.addEventListener('loadedmetadata', function () { ready = true; video.pause(); onScroll(); });
  video.load();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();
})();
