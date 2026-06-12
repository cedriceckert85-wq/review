# -*- coding: utf-8 -*-
"""Alpaca-Paper-Spiegelkonto fuer das Schatten-Depot (Reviewer).

Gleiche Anbindung wie bei allen anderen Agenten (Nutzerauftrag 12.06.2026):
Das Alpaca-Konto PA3XH5SA83HN (100.000 $ Paper) ist BEOBACHTER, nie Blocker —
es spiegelt die Positionen aus data/schatten.json als unabhaengige P&L-Kontrolle.
Bei Alpaca-Fehlern laeuft das Schatten-Depot normal weiter; schatten.json bleibt
die Wahrheit fuer Chart und Bewertung.

SKALIERUNG: Spiegel-Stueckzahl = round(einsatz/einstand * 50)
(2.000-EUR-Journal -> 100.000-$-Konto, identische Groessenverhaeltnisse).
Ganze Stueckzahlen -> GTC-Schutz-Stops moeglich.

CLI:
  python scripts/alpaca_schatten.py status  -> Equity + Positionen + offene Orders
  python scripts/alpaca_schatten.py sync    -> Voll-Abgleich gegen data/schatten.json
                                               (schliesst Weggefallenes, eroeffnet
                                               Fehlendes, zieht Schutz-Stops nach)
Keys: Umgebungsvariablen ALPACA_SCHATTEN_KEY / ALPACA_SCHATTEN_SECRET
      (GitHub-Actions-Secrets im review-Repo), lokal alpaca_keys.json (gitignored).
"""
import json
import os
import sys
import urllib.request
import urllib.error

_HIER = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(_HIER)
SKALIERUNG = 50  # 2.000-EUR-Journal -> 100.000-$-Alpaca-Konto
BASE = "https://paper-api.alpaca.markets/v2"


def _keys():
    if os.environ.get("ALPACA_SCHATTEN_KEY"):
        return {"key": os.environ["ALPACA_SCHATTEN_KEY"],
                "secret": os.environ["ALPACA_SCHATTEN_SECRET"]}
    with open(os.path.join(_REPO, "alpaca_keys.json"), encoding="utf-8") as f:
        return json.load(f)


def api(pfad, methode="GET", body=None):
    k = _keys()
    req = urllib.request.Request(
        BASE + pfad, method=methode,
        headers={"APCA-API-KEY-ID": k["key"], "APCA-API-SECRET-KEY": k["secret"],
                 "Content-Type": "application/json"},
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            inhalt = r.read().decode()
            return json.loads(inhalt) if inhalt else {}
    except urllib.error.HTTPError as e:
        print(f"ALPACA-FEHLER {methode} {pfad}: HTTP {e.code} {e.read().decode()[:250]}")
        return None
    except Exception as e:
        print(f"ALPACA-FEHLER {methode} {pfad}: {e}")
        return None


def market_order(symbol, qty, side):
    return api("/orders", "POST", {"symbol": symbol, "qty": str(int(qty)),
                                   "side": side, "type": "market", "time_in_force": "day"})


def stop_order(symbol, qty, side, stop):
    return api("/orders", "POST", {"symbol": symbol, "qty": str(int(qty)), "side": side,
                                   "type": "stop", "stop_price": f"{stop:.2f}",
                                   "time_in_force": "gtc"})


def alle_orders_canceln(symbol):
    for o in (api("/orders?status=open") or []):
        if o["symbol"] == symbol:
            api(f"/orders/{o['id']}", "DELETE")


def _journal_positionen():
    with open(os.path.join(_REPO, "data", "schatten.json"), encoding="utf-8") as f:
        return json.load(f)["positionen"]


def _spiegel_qty(p):
    return max(1, int(p["einsatz"] / p["einstand"] * SKALIERUNG + 0.5))


def sync():
    """Voll-Abgleich: schliesst Alpaca-Positionen, die nicht mehr in schatten.json
    stehen, eroeffnet fehlende (skaliert, Market), zieht GTC-Schutz-Stops nach."""
    journal = {p["ticker"]: p for p in _journal_positionen()}
    alpaca_pos = {p["symbol"]: p for p in (api("/positions") or [])}
    offene_orders = api("/orders?status=open") or []
    in_arbeit = {o["symbol"] for o in offene_orders if o["type"] == "market"}

    for sym, pos in alpaca_pos.items():
        if sym not in journal:
            alle_orders_canceln(sym)
            qty = abs(int(float(pos["qty"])))
            seite = "sell" if pos["side"] == "long" else "buy"
            market_order(sym, qty, seite)
            print(f"{sym}: nicht mehr im Schatten-Journal -> geschlossen ({seite} {qty})")

    for sym, p in journal.items():
        if sym in alpaca_pos or sym in in_arbeit:
            print(f"{sym}: schon gespiegelt/in Arbeit")
            continue
        qty = _spiegel_qty(p)
        o = market_order(sym, qty, "buy")
        if o:
            print(f"{sym}: buy {qty} Stk. ({p['einsatz']} EUR x{SKALIERUNG}) — Market-Order ({o['status']})")

    stops_offen = {o["symbol"] for o in (api("/orders?status=open") or []) if o["type"] == "stop"}
    for pos in (api("/positions") or []):
        sym = pos["symbol"]
        if sym in stops_offen or sym not in journal:
            continue
        qty = abs(int(float(pos["qty"])))
        o = stop_order(sym, qty, "sell", journal[sym]["stop"])
        if o:
            print(f"{sym}: Schutz-Stop {journal[sym]['stop']} (sell {qty} Stk.) gesetzt")


def status():
    a = api("/account") or {}
    print(f"Equity: {a.get('equity')} USD | Status: {a.get('status')}")
    for p in (api("/positions") or []):
        print(f"  {p['symbol']} {p['side']} {p['qty']} Stk. @ {p['avg_entry_price']} | "
              f"Kurs {p['current_price']} | unrealisiert {p['unrealized_pl']} USD")
    for o in (api("/orders?status=open") or []):
        preis = o.get("stop_price") or o.get("limit_price") or "Market"
        print(f"  ORDER {o['symbol']} {o['side']} {o['qty']} {o['type']} @ {preis} ({o['status']})")


if __name__ == "__main__":
    kommando = sys.argv[1] if len(sys.argv) > 1 else "status"
    {"sync": sync, "status": status}.get(kommando, status)()
