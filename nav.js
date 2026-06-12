// EPMT-Flotte — zentrale Navigations-Komponente (eine Datei fuer ALLE Seiten).
// Einbindung:  <div id="flotten-nav" data-active="<key>"></div>
//              <script src="https://cedriceckert85-wq.github.io/review/nav.js" defer></script>
// Desktop: Pill-Leiste. Handy (<760px): Dropdown mit allen Fenstern.
(function () {
  const B = "https://cedriceckert85-wq.github.io";
  const GRUPPEN = [
    ["Trader", [
      ["haupt",    "📊 Haupt-Depot",   B + "/epmt-dashboard/index.html"],
      ["speku",    "🚀 Speku-Depot",   B + "/epmt-dashboard/speku.html"],
      ["schatten", "👤 Schatten",      B + "/review/agent.html?a=schatten"],
      ["swing",    "◆ Swing",          B + "/review/agent.html?a=swing"],
      ["solid",    "🤍 SOLID",         B + "/review/agent.html?a=solid"],
      ["risk",     "🔥 RISK",          B + "/review/agent.html?a=risk"],
    ]],
    ["Flotte", [
      ["vergleich", "📈 Vergleich",    B + "/review/vergleich.html"],
      ["logs",      "📜 Live-Log",     B + "/review/logs.html"],
      ["reviews",   "📝 Reviews",      B + "/review/index.html"],
      ["woche",     "🗓 Wochen-Review", B + "/review/woche.html"],
    ]],
    ["Detail-Ansichten", [
      ["manuell",         "🧠 Manuell/Research", B + "/epmt-dashboard/spec.html"],
      ["schatten-detail", "👤 Schatten-Details", B + "/review/schatten.html"],
      ["swing-detail",    "◆ Swing-Details",     B + "/swing/"],
      ["duo",             "🤍🔥 Bot-Duo-Details", B + "/bots/"],
    ]],
  ];

  const css = `
  #flotten-nav { margin-bottom: 16px; }
  #flotten-nav .fn-pills { display: flex; gap: 4px; overflow-x: auto; -webkit-overflow-scrolling: touch;
    background: #161618; border-radius: 14px; padding: 4px; scrollbar-width: none; }
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
