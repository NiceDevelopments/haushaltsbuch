/* Dezente Bewegung (23.11.2026). Laeuft nur, wenn <html> die Klasse "anim" hat – die setzt ein Einzeiler im
   <head>, ausser bei prefers-reduced-motion. Ohne JavaScript bleibt alles sichtbar und ruhig. */
(function () {
  var root = document.documentElement;
  if (!root.classList.contains("anim")) return;
  var targets = document.querySelectorAll(".phone, .feature__text, .meter:not(.calc-tool__result)");

  /* Verfuegbar zaehlt vom Monatsbudget herunter, waehrend der Balken (ausgegeben) sich fuellt: 38 % weg. */
  function countDown(meter) {
    var num = meter.querySelector(".meter__num");
    if (!num || !num.firstChild || num.firstChild.nodeType !== 3) return;
    var node = num.firstChild, text = node.nodeValue, m = text.match(/\d+/);
    if (!m) return;
    var end = parseInt(m[0], 10), start = Math.round(end / 0.62), t0 = null, dur = 1200;
    function step(t) {
      if (t0 === null) t0 = t;
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      node.nodeValue = text.replace(m[0], String(Math.round(start + (end - start) * e)));
      if (p < 1) requestAnimationFrame(step);
    }
    node.nodeValue = text.replace(m[0], String(start));
    requestAnimationFrame(step);
  }

  function show(el) {
    el.classList.add("in");
    if (el.classList.contains("meter")) countDown(el);
    var img = el.closest(".hero__shot") && el.querySelector("img");
    if (img) {  /* Pille erst, wenn das Hero-Bild da und das Handy im Blick ist */
      if (img.complete && img.naturalWidth) el.classList.add("go");
      else img.addEventListener("load", function () { el.classList.add("go"); }, { once: true });
    }
  }

  if (!("IntersectionObserver" in window)) {
    Array.prototype.forEach.call(targets, show);
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { show(en.target); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.15 });
  Array.prototype.forEach.call(targets, function (el) { io.observe(el); });
})();
