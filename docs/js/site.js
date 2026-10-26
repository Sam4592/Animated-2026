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
  function themeLabel() {
    var mode = root.getAttribute("data-theme");
    if (mode === "light") return "Theme: light";
    if (mode === "dark") return "Theme: dark";
    return "Theme: system";
  }
  function paintTheme() {
    if (themeBtn) themeBtn.textContent = themeLabel();
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

  var input = document.querySelector("#q");
  var chips = document.querySelectorAll("[data-filter]");
  var tools = document.querySelectorAll("[data-tool]");
  var sections = document.querySelectorAll("[data-section]");
  var count = document.querySelector("#count");
  if (!input || !tools.length) return;

  var cat = "all";
  var total = document.querySelectorAll("[data-section]:not([data-count='skip']) [data-tool]").length;

  function apply() {
    var query = input.value.trim().toLowerCase();
    var shown = 0;
    tools.forEach(function (el) {
      var inCat = cat === "all" || el.getAttribute("data-cat") === cat;
      var hay = (el.getAttribute("data-search") || "").toLowerCase();
      var ok = inCat && (!query || hay.indexOf(query) !== -1);
      el.hidden = !ok;
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
  }

  input.addEventListener("input", apply);
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      cat = chip.getAttribute("data-filter") || "all";
      chips.forEach(function (other) {
        other.setAttribute("aria-pressed", other === chip ? "true" : "false");
      });
      apply();
    });
  });
  apply();
})();
