(function () {
  var root = document.documentElement;
  var key = "animated-2026-theme";
  var saved = null;
  try {
    saved = localStorage.getItem(key);
  } catch (err) {
    saved = null;
  }
  if (saved === "light" || saved === "dark") {
    root.setAttribute("data-theme", saved);
  }

  var themeBtn = document.querySelector("[data-theme-toggle]");
  function themeName() {
    var mode = root.getAttribute("data-theme");
    if (mode === "light") return "Light";
    if (mode === "dark") return "Dark";
    return "System";
  }
  function paintTheme() {
    if (!themeBtn) return;
    var mode = root.getAttribute("data-theme");
    var full = mode === "light" ? "Theme: light" : mode === "dark" ? "Theme: dark" : "Theme: system";
    themeBtn.textContent = themeName();
    themeBtn.setAttribute("aria-label", full);
  }
  paintTheme();
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var mode = root.getAttribute("data-theme");
      var next = mode === "dark" ? "light" : mode === "light" ? "" : "dark";
      if (next) root.setAttribute("data-theme", next);
      else root.removeAttribute("data-theme");
      try {
        if (next) localStorage.setItem(key, next);
        else localStorage.removeItem(key);
      } catch (err) {
        /* storage can be blocked; the toggle still works for this view */
      }
      paintTheme();
    });
  }

  var toggle = document.querySelector("[data-nav-toggle]");
  var navEl = document.getElementById("site-nav");
  function setNavOpen(open, restoreFocus) {
    if (!toggle || !navEl) return;
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    navEl.classList.toggle("is-open", open);
    if (!open && restoreFocus) toggle.focus();
  }
  if (toggle && navEl) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      setNavOpen(!open, false);
      if (!open) {
        var first = navEl.querySelector("a");
        if (first) first.focus();
      }
    });
    navEl.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) setNavOpen(false, false);
    });
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape") setNavOpen(false, true);
    });
    document.addEventListener("click", function (ev) {
      if (!navEl.classList.contains("is-open")) return;
      if (navEl.contains(ev.target) || toggle.contains(ev.target)) return;
      setNavOpen(false, false);
    });
  }

  var input = document.querySelector("#q");
  var chips = document.querySelectorAll("[data-filter]");
  var tools = document.querySelectorAll("[data-tool]");
  var sections = document.querySelectorAll("[data-section]");
  var count = document.querySelector("#count");
  var empty = document.querySelector("#none");
  var clearBtn = document.querySelector("[data-clear-filters]");
  if (!input || !tools.length) return;

  var cat = "all";
  var total = document.querySelectorAll("[data-section]:not([data-count='skip']) [data-tool]").length;
  var known = {};
  chips.forEach(function (chip) {
    var id = chip.getAttribute("data-filter");
    if (id && id !== "all") known[id] = true;
  });

  function readState() {
    var params = new URLSearchParams(window.location.search);
    var q = params.get("q") || "";
    var catQ = params.get("cat") || "";
    var hash = (window.location.hash || "").replace(/^#/, "");
    var next = "all";
    if (known[hash]) next = hash;
    else if (known[catQ]) next = catQ;
    return { q: q, cat: next };
  }

  function syncUrl(q, nextCat) {
    var url = new URL(window.location.href);
    if (q) url.searchParams.set("q", q);
    else url.searchParams.delete("q");
    if (nextCat && nextCat !== "all") url.searchParams.set("cat", nextCat);
    else url.searchParams.delete("cat");
    var hash = (url.hash || "").replace(/^#/, "");
    if (nextCat && nextCat !== "all") url.hash = nextCat;
    else if (known[hash]) url.hash = "";
    var next = url.pathname + url.search + url.hash;
    var current = window.location.pathname + window.location.search + window.location.hash;
    if (next !== current) history.replaceState(null, "", next);
  }

  function setCat(next) {
    cat = next || "all";
    chips.forEach(function (chip) {
      chip.setAttribute("aria-pressed", chip.getAttribute("data-filter") === cat ? "true" : "false");
    });
  }

  function apply() {
    var query = input.value.trim().toLowerCase();
    var shown = 0;
    var any = false;
    tools.forEach(function (el) {
      var inCat = cat === "all" || el.getAttribute("data-cat") === cat;
      var hay = (el.getAttribute("data-search") || "").toLowerCase();
      var ok = inCat && (!query || hay.indexOf(query) !== -1);
      el.hidden = !ok;
      if (ok) any = true;
      if (ok && el.closest("[data-section]:not([data-count='skip'])")) shown += 1;
    });
    sections.forEach(function (section) {
      var visible = section.querySelector("[data-tool]:not([hidden])");
      section.hidden = !visible;
    });
    if (count) {
      count.textContent =
        query || cat !== "all"
          ? "Showing " + shown + " of " + total + " tools"
          : total + " tools";
    }
    if (empty) empty.hidden = any;
  }

  function applyFromUrl() {
    var state = readState();
    input.value = state.q;
    setCat(state.cat);
    apply();
    syncUrl(input.value.trim(), cat);
  }

  input.addEventListener("input", function () {
    apply();
    syncUrl(input.value.trim(), cat);
  });
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      setCat(chip.getAttribute("data-filter") || "all");
      apply();
      syncUrl(input.value.trim(), cat);
    });
  });
  if (clearBtn) {
    clearBtn.addEventListener("click", function () {
      input.value = "";
      setCat("all");
      apply();
      syncUrl("", "all");
      input.focus();
    });
  }
  window.addEventListener("hashchange", applyFromUrl);
  window.addEventListener("popstate", applyFromUrl);
  applyFromUrl();
})();
