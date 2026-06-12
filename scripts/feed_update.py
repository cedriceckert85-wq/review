# -*- coding: utf-8 -*-
"""Flotten-Log: sammelt die juengsten Aktivitaeten ALLER Agenten (Commits der
oeffentlichen Repos) in einen chronologischen Feed (data/feed.json).
Laeuft im Minuten-Laeufer (live.yml) ca. alle 5 Minuten.
"""
import json
import os
import urllib.request

REPOS = [
    ("epmt-dashboard", None),   # Haupt/Speku pushen hier mit Prefix "Haupt:"/"Speku:"
    ("review", "schatten"),
    ("swing", "swing"),
    ("bots", "bots"),
]
# Commit-Muster, die Rauschen sind (Minuten-Punkte, reine Daten-Jobs)
RAUSCHEN = ("live", "Live ", "Kurse ", "Quant-Snapshot", "Vergleich ", "Preis-Snapshot",
            "Trade-Auswertung", "Alpaca-Orders ")

AGENT_MAP = {
    "Haupt:": ("haupt", "📊 Haupt"),
    "Speku:": ("speku", "🚀 Speku"),
    "Review ": ("schatten", "👤 Review/Schatten"),
    "SOLID-Lauf": ("solid", "🤍 SOLID"),
    "RISK-Lauf": ("risk", "🔥 RISK"),
    "Swing-Lauf": ("swing", "◆ Swing"),
}


def commits(repo):
    url = f"https://api.github.com/repos/cedriceckert85-wq/{repo}/commits?per_page=40"
    headers = {"User-Agent": "flotten-log", "Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_API_TOKEN", "")
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def einordnen(repo, fallback, msg):
    for prefix, (key, label) in AGENT_MAP.items():
        if msg.startswith(prefix):
            return key, label
    if fallback == "schatten":
        return "system", "🛠 Review-System"
    if fallback == "swing":
        return "swing", "◆ Swing"
    if fallback == "bots":
        return "bots", "🤍🔥 Bot-Duo"
    return "system", "🛠 System"


def main():
    eintraege = []
    for repo, fallback in REPOS:
        try:
            for c in commits(repo):
                msg = c["commit"]["message"].split("\n")[0]
                if any(msg.startswith(r) or msg == r.strip() for r in RAUSCHEN):
                    continue
                key, label = einordnen(repo, fallback, msg)
                eintraege.append({
                    "zeit": c["commit"]["author"]["date"],
                    "agent": key, "label": label, "repo": repo,
                    "text": msg[:180],
                })
        except Exception as e:
            print(f"WARN {repo}: {e}")
    eintraege.sort(key=lambda e: e["zeit"], reverse=True)
    feed = {"standUtc": eintraege[0]["zeit"] if eintraege else None, "eintraege": eintraege[:80]}
    with open("data/feed.json", "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"Feed: {len(feed['eintraege'])} Eintraege")


if __name__ == "__main__":
    main()
