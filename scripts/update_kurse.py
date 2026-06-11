"""Aktualisiert die Kurse der Schatten-Depot-Positionen in data/schatten.json.

Läuft alle 15 Minuten per GitHub Actions während US-Marktzeiten.
Quellen: Yahoo Finance (primär), Stooq (Fallback). Plausibilitäts-Guard:
Kurse mit >50 % Abweichung zum letzten Stand werden verworfen.
Stops werden hier NICHT exekutiert (das macht der Review-Agent) — nur als
stopVerletzt markiert, damit die GUI warnen kann.
"""
import json
import datetime
import urllib.request
from zoneinfo import ZoneInfo

PFAD = "data/schatten.json"


def yahoo(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        d = json.load(r)
    return float(d["chart"]["result"][0]["meta"]["regularMarketPrice"])


def stooq(ticker):
    url = f"https://stooq.com/q/l/?s={ticker.lower()}.us&f=sd2t2ohlcv&e=csv"
    with urllib.request.urlopen(url, timeout=15) as r:
        zeilen = r.read().decode().strip().splitlines()
    return float(zeilen[1].split(",")[6])


def kurs_holen(ticker, alter_kurs):
    for quelle in (yahoo, stooq):
        try:
            k = quelle(ticker)
            if k > 0 and (alter_kurs <= 0 or abs(k / alter_kurs - 1) < 0.5):
                return round(k, 2)
            print(f"{ticker}: {quelle.__name__}-Kurs {k} unplausibel (alt {alter_kurs}) — verworfen")
        except Exception as e:
            print(f"{ticker}: {quelle.__name__} fehlgeschlagen: {e}")
    return None


def main():
    with open(PFAD, encoding="utf-8") as f:
        d = json.load(f)

    geaendert = False
    for p in d["positionen"]:
        neu = kurs_holen(p["ticker"], p.get("kurs", 0))
        if neu is None or abs(neu - p["kurs"]) < 0.005:
            continue
        p["kurs"] = neu
        p["rendite"] = round((neu / p["einstand"] - 1) * 100, 2)
        p["stopVerletzt"] = neu <= p["stop"]
        geaendert = True
        print(f"{p['ticker']}: {neu} ({p['rendite']:+.2f} %)" + (" STOP VERLETZT" if p["stopVerletzt"] else ""))

    if not geaendert:
        print("Keine Kursänderung.")
        return

    wert = d["aktuell"]["cash"] + sum(p["einsatz"] * p["kurs"] / p["einstand"] for p in d["positionen"])
    d["aktuell"]["vermoegen"] = round(wert, 2)
    d["aktuell"]["rendite"] = round((wert / d["meta"]["startKapital"] - 1) * 100, 2)
    d["aktuell"]["cashQuote"] = round(d["aktuell"]["cash"] / wert * 100, 1)
    jetzt = datetime.datetime.now(ZoneInfo("Europe/Berlin"))
    d["aktuell"]["stand"] = jetzt.strftime("%d.%m.%Y, %H:%M") + " (Auto-Kurse)"

    with open(PFAD, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("Aktualisiert:", d["aktuell"]["stand"], "| Vermögen:", d["aktuell"]["vermoegen"], "€")


if __name__ == "__main__":
    main()
