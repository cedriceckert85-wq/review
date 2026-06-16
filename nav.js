// EPMT-Flotte — zentrale Navigations-Komponente (eine Datei fuer ALLE Seiten).
// Einbindung:  <div id="flotten-nav" data-active="<key>"></div>
//              <script src="https://cedriceckert85-wq.github.io/review/nav.js" defer></script>
// Desktop: Pill-Leiste. Handy (<760px): Dropdown mit allen Fenstern.
(function () {
  const B = "https://cedriceckert85-wq.github.io";
  const GRUPPEN = [
    ["Trader", [
      ["haupt",    "📊 Haupt-Depot",   B + "/review/agent.html?a=haupt"],
      ["speku",    "🚀 Speku-Depot",   B + "/review/agent.html?a=speku"],
      ["schatten", "👤 Schatten",      B + "/review/agent.html?a=schatten"],
      ["swing",    "◆ Gegentrend",          B + "/review/agent.html?a=swing"],
      ["solid",    "🤍 SOLID",         B + "/review/agent.html?a=solid"],
      ["risk",     "🔥 RISK",          B + "/review/agent.html?a=risk"],
      ["crypto",   "₿ Crypto-Bot",     B + "/review/agent.html?a=crypto"],
    ]],
    ["Flotte", [
      ["vergleich", "📈 Vergleich",    B + "/review/vergleich.html"],
      ["logs",      "📜 Live-Log",     B + "/review/logs.html"],
      ["reviews",   "📝 Reviews",      B + "/review/index.html"],
      ["woche",     "🗓 Wochen-Review", B + "/review/woche.html"],
    ]],
    ["Detail-Ansichten", [
      ["haupt-detail",    "📊 Haupt-Details",    B + "/epmt-dashboard/index.html"],
      ["speku-detail",    "🚀 Speku-Details",    B + "/epmt-dashboard/speku.html"],
      ["manuell",         "🧠 Manuell/Research", B + "/epmt-dashboard/spec.html"],
      ["schatten-detail", "👤 Schatten-Details", B + "/review/schatten.html"],
      ["swing-detail",    "◆ Gegentrend-Details",     B + "/swing/"],
      ["duo",             "🤍🔥 Bot-Duo-Details", B + "/bots/"],
    ]],
  ];

  const css = `
  #flotten-nav { margin-bottom: 16px; }
  #flotten-nav .fn-pills { display: flex; flex-wrap: wrap; gap: 4px;
    background: #161618; border-radius: 14px; padding: 4px; }
  #flotten-nav .fn-pills::-webkit-scrollbar { display: none; }
  #flotten-nav .fn-pills a { white-space: nowrap; padding: 9px 13px; border-radius: 10px; color: #98989d;
    text-decoration: none; font-size: 13px; font-weight: 600;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', Roboto, sans-serif; }
  #flotten-nav .fn-pills a.aktiv { background: #2f2f31; color: #f5f5f7; }
  #flotten-nav .fn-select { display: none; width: 100%; appearance: none; -webkit-appearance: none;
    background: #1c1c1e url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='8'%3E%3Cpath d='M1 1l6 6 6-6' stroke='%2398989d' stroke-width='2' fill='none'/%3E%3C/svg%3E") no-repeat right 14px center;
    color: #f5f5f7; border: 1px solid #2c2c2e; border-radius: 14px; padding: 13px 40px 13px 14px;
    font-size: 16px; font-weight: 600;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Segoe UI', Roboto, sans-serif; }
  @media (max-width: 760px) {
    #flotten-nav .fn-pills { display: none; }
    #flotten-nav .fn-select { display: block; }
  }`;

  function bauen() {
    const ziel = document.getElementById("flotten-nav");
    if (!ziel) return;
    const aktiv = ziel.dataset.active || "";

    const style = document.createElement("style");
    style.textContent = css;
    document.head.appendChild(style);

    const pills = document.createElement("div");
    pills.className = "fn-pills";
    const select = document.createElement("select");
    select.className = "fn-select";
    select.setAttribute("aria-label", "Flotten-Navigation");

    GRUPPEN.forEach(([gruppe, seiten]) => {
      const og = document.createElement("optgroup");
      og.label = gruppe;
      seiten.forEach(([key, titel, url]) => {
        if (gruppe !== "Detail-Ansichten") {
          const a = document.createElement("a");
          a.href = url;
          a.textContent = titel;
          if (key === aktiv) a.className = "aktiv";
          pills.appendChild(a);
        }
        const opt = document.createElement("option");
        opt.value = url;
        opt.textContent = titel + (key === aktiv ? "  ✓" : "");
        if (key === aktiv) opt.selected = true;
        og.appendChild(opt);
      });
      select.appendChild(og);
    });

    select.addEventListener("change", () => { if (select.value) location.href = select.value; });
    ziel.appendChild(pills);
    ziel.appendChild(select);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bauen);
  } else {
    bauen();
  }
})();

// === Bot-Umbenennen (LOKAL, nur dieser Browser; localStorage) ===
(function () {
  try {
    var KEY = "epmt_bot_namen";
    var BOTS = [
      { k: "haupt", def: "Haupt" }, { k: "speku", def: "Speku" }, { k: "schatten", def: "Schatten" },
      { k: "swing", def: "Gegentrend" }, { k: "solid", def: "SOLID" }, { k: "risk", def: "RISK" }
    ];
    function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
    function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
    function save(m) { try { localStorage.setItem(KEY, JSON.stringify(m)); } catch (e) {} }
    function pairs() {
      var m = load();
      return BOTS
        .map(function (b) { return [b.def, (m[b.k] || "").trim()]; })
        .filter(function (p) { return p[1] && p[1] !== p[0] && !new RegExp("\\b" + esc(p[0]) + "\\b").test(p[1]); });
    }
    function apply() {
      var ps = pairs();
      if (!ps.length) return;
      var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
      var nodes = [], n;
      while ((n = w.nextNode())) nodes.push(n);
      nodes.forEach(function (node) {
        var p = node.parentNode;
        if (!p || /^(SCRIPT|STYLE|INPUT|TEXTAREA|OPTION)$/.test(p.nodeName)) return;
        var t = node.nodeValue, o = t;
        ps.forEach(function (pr) { t = t.replace(new RegExp("\\b" + esc(pr[0]) + "\\b", "g"), pr[1]); });
        if (t !== o) node.nodeValue = t;
      });
    }
    function panel() {
      var m = load();
      var rows = BOTS.map(function (b) {
        return '<label style="display:flex;gap:8px;align-items:center;margin:6px 0;color:#f5f5f7;font-size:14px">'
          + '<span style="width:90px;color:#98989d">' + b.def + '</span>'
          + '<input data-k="' + b.k + '" value="' + (m[b.k] || "").replace(/"/g, "&quot;") + '" placeholder="' + b.def + '" '
          + 'style="flex:1;background:#1c1c1e;border:1px solid #2c2c2e;border-radius:8px;color:#f5f5f7;padding:8px;font-size:15px"></label>';
      }).join("");
      var ov = document.createElement("div");
      ov.style.cssText = "position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:99999;display:flex;align-items:center;justify-content:center;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif";
      ov.innerHTML = '<div style="background:#161618;border-radius:16px;padding:20px;max-width:360px;width:90%">'
        + '<div style="color:#f5f5f7;font-weight:700;font-size:16px;margin-bottom:4px">Bots umbenennen</div>'
        + '<div style="color:#98989d;font-size:12px;margin-bottom:10px">Gilt nur in diesem Browser. Leer lassen = Standardname.</div>'
        + rows
        + '<div style="display:flex;gap:8px;margin-top:14px">'
        + '<button id="bn-save" style="flex:1;background:#2f6fed;color:#fff;border:0;border-radius:10px;padding:11px;font-weight:700;cursor:pointer">Speichern</button>'
        + '<button id="bn-reset" style="background:#2f2f31;color:#f5f5f7;border:0;border-radius:10px;padding:11px;cursor:pointer">Zurücksetzen</button>'
        + '<button id="bn-close" style="background:#2f2f31;color:#f5f5f7;border:0;border-radius:10px;padding:11px 14px;cursor:pointer">✕</button>'
        + '</div></div>';
      document.body.appendChild(ov);
      ov.querySelector("#bn-save").onclick = function () {
        var nm = {};
        ov.querySelectorAll("input[data-k]").forEach(function (i) { if (i.value.trim()) nm[i.dataset.k] = i.value.trim(); });
        save(nm); location.reload();
      };
      ov.querySelector("#bn-reset").onclick = function () { save({}); location.reload(); };
      ov.querySelector("#bn-close").onclick = function () { ov.remove(); };
      ov.onclick = function (e) { if (e.target === ov) ov.remove(); };
    }
    function addButton() {
      var nav = document.getElementById("flotten-nav");
      if (!nav || document.getElementById("bn-btn")) return;
      var btn = document.createElement("button");
      btn.id = "bn-btn";
      btn.textContent = "✏️ Namen";
      btn.title = "Bot-Namen umbenennen (nur dieser Browser)";
      btn.style.cssText = "margin-top:6px;background:#1c1c1e;color:#98989d;border:1px solid #2c2c2e;border-radius:10px;padding:7px 11px;font-size:12px;font-weight:600;cursor:pointer";
      btn.onclick = panel;
      nav.appendChild(btn);
    }
    function run() {
      addButton();
      var t = null, busy = false;
      var obs = new MutationObserver(function () {
        if (busy) return;
        clearTimeout(t);
        t = setTimeout(function () {
          busy = true; obs.disconnect();
          try { apply(); } catch (e) {}
          obs.observe(document.body, { childList: true, subtree: true });
          busy = false;
        }, 250);
      });
      try { apply(); } catch (e) {}
      obs.observe(document.body, { childList: true, subtree: true });
    }
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
    else run();
  } catch (e) { /* Umbenenn-Feature darf die Seite niemals brechen */ }
})();
