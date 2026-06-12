# -*- coding: utf-8 -*-
"""Sammelt jeden Abend die Performance aller Depots fuer den Vergleichs-Chart.

Quellen:
- Swing/Speku/Haupt: echte Alpaca-Paper-Equity (Secrets ALPACA_<NAME>_KEY/SECRET),
  Rendite = (Equity / 100000 - 1) * 100.
- Schatten: data/schatten.json -> aktuell.rendite (eigenes Review-Depot).
- SPY: Yahoo-Schlusskurs; Referenz = erster verfuegbarer Schluss ab 12.06. (meta.spyStart).
- Tagesgeld: 2 % p.a. linear seit 12.06.2026.
Idempotent: Eintrag des heutigen Datums wird ersetzt, sonst angehaengt.
Fehlertolerant: nicht erreichbare Quellen liefern den letzten bekannten Wert.
"""
import json
import os
import datetime
import urllib.request
from zoneinfo import ZoneInfo

P = "data/vergleich.json"
START = datetime.date(2026, 6, 12)


def alpaca_equity(prefix):
    key = os.environ.get(prefix + "_KEY", "")
    sec = os.environ.get(prefix + "_SECRET", "")
    if not key:
        return None
    req = urllib.request.Request(
        "https://paper-api.alpaca.markets/v2/account",
        headers={"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": sec})
    with urllib.request.urlopen(req, timeout=20) as r:
        return float(json.load(r)["equity"])


def spy_kurs():
    req = urllib.request.Request(
        "https://query1.finance.yahoo.com/v8/finance/chart/SPY?interval=1d&range=5d",
        headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        d = json.load(r)
    closes = [c for c in d["chart"]["result"][0]["indicators"]["quote"][0]["close"] if c]
    return float(closes[-1])


def sicher(fn, *a):
    try:
        return fn(*a)
    except Exception as e:
        print(f"WARN {getattr(fn, '__name__', fn)}: {e}")
        return None


def main():
    with open(P, encoding="utf-8") as f:
        d = json.load(f)
    heute = datetime.datetime.now(ZoneInfo("Europe/Berlin")).date()
    letzter = d["verlauf"][-1] if d["verlauf"] else {}

    punkt = {"datum": heute.isoformat(), "label": heute.strftime("%d.%m.")}

    for name, prefix in (("swing", "ALPACA_SWING"), ("speku", "ALPACA_SPEKU"), ("haupt", "ALPACA_HAUPT"),
                         ("solid", "ALPACA_SOLID"), ("risk", "ALPACA_RISK")):
        eq = sicher(alpaca_equity, prefix)
        punkt[name] = round((eq / 100000 - 1) * 100, 2) if eq else letzter.get(name, 0.0)

    try:
        with open("data/schatten.json", encoding="utf-8") as f:
            punkt["schatten"] = json.load(f)["aktuell"]["rendite"]
    except Exception as e:
        print(f"WARN schatten: {e}")
        punkt["schatten"] = letzter.get("schatten", 0.0)

    spy = sicher(spy_kurs)
    if spy and not d["meta"].get("spyStart"):
        d["meta"]["spyStart"] = spy
    if spy and d["meta"].get("spyStart"):
        punkt["spy"] = round((spy / d["meta"]["spyStart"] - 1) * 100, 2)
    else:
        punkt["spy"] = letzter.get("spy", 0.0)

    punkt["tagesgeld"] = round(2.0 * max(0, (heute - START).days) / 365, 3)

    d["verlauf"] = [p for p in d["verlauf"] if p["datum"] != punkt["datum"]] + [punkt]

    with open(P, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Punkt:", json.dumps(punkt, ensure_ascii=False))


if __name__ == "__main__":
    main()
