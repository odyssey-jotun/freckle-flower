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

