# -*- coding: utf-8 -*-
"""Schreibt alle ~5 Minuten (Marktzeiten) einen LIVE-Datenpunkt nach data/live.json:
die echten Alpaca-Equities aller fuenf Konten + Schatten (rebasiert) + SPY + Tagesgeld.
Die Vergleichs-Seite holt die Datei jede Minute ab — quasi-live ohne Keys im Browser.
"""
import json
import os
import datetime
import urllib.request
from zoneinfo import ZoneInfo

START = datetime.date(2026, 6, 12)


def alpaca_equity(prefix):
    key = os.environ.get(prefix + "_KEY", "")
    sec = os.environ.get(prefix + "_SECRET", "")
    if not key:
        return None
    req = urllib.request.Request(
        "https://paper-api.alpaca.markets/v2/account",
        headers={"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": sec})
    with urllib.request.urlopen(req, timeout=15) as r:
        return float(json.load(r)["equity"])


def spy_kurs():
    req = urllib.request.Request(
        "https://query1.finance.yahoo.com/v8/finance/chart/SPY?interval=1m&range=1d",
        headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        d = json.load(r)
    return float(d["chart"]["result"][0]["meta"]["regularMarketPrice"])


def sicher(fn, *a):
    try:
        return fn(*a)
    except Exception as e:
        print(f"WARN {getattr(fn, '__name__', fn)}: {e}")
        return None


def main():
    with open("data/vergleich.json", encoding="utf-8") as f:
        meta = json.load(f)["meta"]
    jetzt = datetime.datetime.now(ZoneInfo("Europe/Berlin"))
    punkt = {"datum": jetzt.date().isoformat(), "label": "live", "standUhr": jetzt.strftime("%H:%M")}

    # Schatten seit 12.06. abends wie alle anderen: eigenes Alpaca-Konto PA3XH5SA83HN.
    for name, prefix in (("swing", "ALPACA_SWING"), ("speku", "ALPACA_SPEKU"), ("haupt", "ALPACA_HAUPT"),
                         ("solid", "ALPACA_SOLID"), ("risk", "ALPACA_RISK"), ("schatten", "ALPACA_SCHATTEN"),
                         ("crypto", "ALPACA_CRYPTO")):
        eq = sicher(alpaca_equity, prefix)
        punkt[name] = round((eq / 100000 - 1) * 100, 2) if eq else None

    spy = sicher(spy_kurs)
    punkt["spy"] = round((spy / meta["spyStart"] - 1) * 100, 2) if spy and meta.get("spyStart") else None
    punkt["tagesgeld"] = round(2.0 * max(0, (jetzt.date() - START).days) / 365, 3)

    with open("data/live.json", "w", encoding="utf-8") as f:
        json.dump(punkt, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("LIVE:", json.dumps(punkt, ensure_ascii=False))


if __name__ == "__main__":
    main()
