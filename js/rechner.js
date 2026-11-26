/* Tagesbudget-Rechner (Einfaches Haushaltsbuch, seit 25.11.2026).
   Rechnet nur im Browser. Nichts wird gespeichert oder gesendet. */
(function () {
  "use strict";
  var box = document.getElementById("rechner");
  var cfgEl = document.getElementById("rt-cfg");
  if (!box || !cfgEl) return;
  var cfg = JSON.parse(cfgEl.textContent);
  var $ = function (id) { return document.getElementById(id); };
  var inc = $("rt-income"), spentEl = $("rt-spent"), startEl = $("rt-start");
  var fixedEls = Array.prototype.slice.call(box.querySelectorAll("input[data-fixed]"));
  var yearlyEls = Array.prototype.slice.call(box.querySelectorAll("input[data-yearly]"));
  var inputs = Array.prototype.slice.call(box.querySelectorAll("input"));
  var DAY = 86400000;
  var dec = cfg.locale.indexOf("de") === 0 ? "," : ".";

  /* Ein einzelnes Trennzeichen mit 1–2 Ziffern dahinter ist das Dezimalzeichen, egal welches
     ("2100.50" und "2100,50" sind beide 2100,50). Sonst gilt die Schreibweise der Sprache. */
  function num(el) {
    var v = (el.value || "").replace(/[\s  '€$£]/g, "");
    if (!v) return 0;
    var m = v.match(/^(\d+)[.,](\d{1,2})$/);
    var k = v.match(/^(\d{1,3})[.,](\d{3})$/);   /* "2.100" / "2,100" = Tausender */
    if (m) v = m[1] + "." + m[2];
    else if (k) v = k[1] + k[2];
    else if (dec === ",") v = v.replace(/\./g, "").replace(",", ".");
    else v = v.replace(/,/g, "");
    var n = parseFloat(v);
    return isFinite(n) && n > 0 ? n : 0;
  }

  function money(n) {
    var s = new Intl.NumberFormat(cfg.locale, { minimumFractionDigits: 2, maximumFractionDigits: 2 }).format(n);
    return cfg.cur ? s + " " + cfg.cur : s;
  }

  function dateOf(y, m, d) {
    var last = new Date(y, m + 1, 0).getDate();
    return new Date(y, m, Math.min(d, last));
  }

  /* Zeitraum ab Budgetbeginn (Tag 1–31; gibt es den Tag nicht, gilt wie in der App der Monatsletzte).
     Ende über Kalendertage, nicht über Millisekunden – sonst verrutscht es bei der Zeitumstellung. */
  function period(today, startDay) {
    var y = today.getFullYear(), m = today.getMonth();
    var start = dateOf(y, m, startDay);
    if (start > today) start = dateOf(y, m - 1, startDay);
    var next = dateOf(start.getFullYear(), start.getMonth() + 1, startDay);
    return { start: start, end: new Date(next.getFullYear(), next.getMonth(), next.getDate() - 1) };
  }

  function days(a, b) { return Math.round((b - a) / DAY); }

  function update() {
    var income = num(inc), spent = num(spentEl);
    var fixed = fixedEls.reduce(function (a, el) { return a + num(el); }, 0)
              + yearlyEls.reduce(function (a, el) { return a + num(el); }, 0) / 12;
    var anyFixed = fixedEls.concat(yearlyEls).some(function (el) { return (el.value || "").trim() !== ""; });
    $("rt-fixedsum").textContent = anyFixed ? money(fixed) : "–";
    var hasSpent = (spentEl.value || "").trim() !== "";
    var startDay = Math.max(1, Math.min(31, Math.round(num(startEl)) || 1));
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    var p = period(today, startDay);
    var total = days(p.start, p.end) + 1;
    var left = days(today, p.end) + 1;           /* heute mitgezählt */
    var budget = income - fixed;
    var avail = budget - spent;
    var note = $("rt-note"), out = $("rt-avail"), perday = $("rt-perday");

    box.classList.remove("over", "ahead");
    if (!income) {
      out.textContent = "–"; perday.textContent = ""; note.textContent = cfg.empty;
      $("rt-fill").style.width = "0"; $("rt-mark").style.left = "0";
      return;
    }
    out.textContent = money(avail);
    if (hasSpent) {
      var until = new Intl.DateTimeFormat(cfg.locale, { day: "numeric", month: "long" }).format(p.end);
      perday.textContent = cfg.until.replace("{0}", money(Math.max(avail, 0) / left)).replace("{1}", until);
    } else {
      perday.textContent = cfg.over_days.replace("{0}", money(Math.max(budget, 0) / total)).replace("{1}", total);
    }

    var spentPct = budget > 0 ? Math.min(1, Math.max(0, spent / budget)) : 1;
    var timePct = (total - left + 1) / total;     /* heute zählt mit, wie in der App */
    $("rt-fill").style.width = (spentPct * 100).toFixed(1) + "%";
    $("rt-mark").style.left = "calc(" + (timePct * 100).toFixed(1) + "% - 1px)";
    $("rt-mark").style.visibility = hasSpent ? "visible" : "hidden";   /* Zeitstrich nur mit Ausgaben */

    if (budget < 0) { box.classList.add("over"); note.textContent = cfg.fixed_over; }
    else if (avail < 0) { box.classList.add("over"); note.textContent = cfg.over; }
    else if (spent > 0 && spentPct > timePct + 0.02) { box.classList.add("ahead"); note.textContent = cfg.fast; }
    else if (spent > 0) note.textContent = cfg.ok;
    else note.textContent = hasSpent ? "" : cfg.bar_hint;
  }

  var timer;
  function later() { clearTimeout(timer); timer = setTimeout(update, 350); }
  inputs.forEach(function (el) { el.addEventListener("input", later); });
  box.hidden = false;
  update();
})();
