# Fehler-Akte: Speku-Depot (Zukunfts-Mandat)

Jeder Eintrag hat eine ID (F-S-001, …), eine Einstufung und einen Status.

**Einstufung:**
- **SKILL-FEHLER** — Prozessfehler oder ungetestete Annahme. War vermeidbar. Muss abgestellt werden.
- **PECH** — Prozess war korrekt, Ergebnis trotzdem schlecht. Kein Handlungsbedarf, nicht überreagieren.
- **UNKLAR** — noch nicht entscheidbar, mehr Daten nötig.

Diese Akte wird bei jedem Lauf gepflegt und sonntags im Wochen-Review ausgewertet.
Ziel: Muster erkennen → abstellen → profitabler Trader. Ein Fehler, der zweimal vorkommt, ist kein Fehler mehr, sondern eine Gewohnheit.

---

## Offene Fehler / Beobachtungen

### F-S-001 · 2026-06-11 · Klumpenrisiko: 100 % des investierten Kapitals in einem Thema
- **Was passiert ist:** QBTS, IONQ, RGTI — drei Positionen, eine Wette. Korrelation nahe 1; ein negativer Quantum-Katalysator trifft alles gleichzeitig. Das eigene Research warnt selbst vor der gemeinsamen Zinssensitivität — ohne Konsequenz.
- **Einstufung:** UNKLAR (strukturelles Risiko, noch kein realisierter Schaden) — wird zum SKILL-FEHLER, wenn ein gemeinsamer Drawdown >10 % aller drei Positionen eintritt und keine Diversifikation stattgefunden hat.
- **Messlatte:** Gleichzeitiger Drawdown aller drei Positionen; Umsetzung von Tranche 2 (Space) als erste echte Diversifikation.
- **Update 11.06.2026 (22:00):** RKLB-Short (120 €) eingebucht — taktische Ergänzung in entgegengesetzter Richtung, aber kein Ersatz für strukturelle Diversifikation. Quantum-Klumpenrisiko bleibt ungelöst.
- **Status:** OFFEN

### F-S-002 · 2026-06-11 · Nachkauf-Automatik in Story-Aktien
- **Was passiert ist:** Regel „IONQ < 50 $ / QBTS < 21 $ → aufstocken bis 500 €" — automatisches Averaging-down in unprofitable Spekulationswerte. Die Automatik erhöht genau dann, wenn die These bröckelt.
- **Einstufung:** UNKLAR — bewertbar, sobald ein Trigger auslöst (siehe Schatten-Depot D4). Strukturell ein klassischer Speku-Depot-Killer.
- **Messlatte:** Löst ein Nachkauf-Trigger aus: Fällt der Kurs danach weiter Richtung Stop → SKILL-FEHLER. Dreht die Position → die Automatik hatte (diesmal) recht.
- **Update 11.06.2026 (22:00):** IONQ 58,28 $, QBTS 24,05 $ — beide weit über Trigger-Niveaus. Kein Trigger.
- **Status:** OFFEN

### F-S-003 · 2026-06-11 · Scout-Fehlalarme als Prozessrisiko
- **Was passiert ist:** ~14 „Material"-Fehlalarme an Tag 1 (u. a. Quellen vom 04.06. für ein angebliches Ereignis „vom 13.06."). Alle wurden manuell abgefangen — im Voll-Autonom-Modus wäre jeder davon ein potenzieller Fehltrade.
- **Einstufung:** SKILL-FEHLER (Prozess) — kein Marktfehler, sondern eine ungesicherte Datenquelle im Entscheidungsweg.
- **Lehre:** Kein Handeln auf unverifizierte Meldungen (Quellendatum < 24 h + zwei unabhängige Quellen). Wird durch den Master-Fix technisch abgesichert.
- **Kosten:** 0 € (bisher abgefangen)
- **Update 11.06.2026 (22:00):** 7 Fehlalarme heute (Tag 2: down von ~14 auf 7) — Master-Fix greift, Verbesserung sichtbar. Noch nicht bei 0 Fehlalarmen.
- **Status:** OFFEN (Fehlalarm-Rate: Tag 1 ~14, Tag 2 7 — Ziel: 0 über eine Woche)

---

## Erledigte Einträge (im Wochen-Review abgeschlossen)

_(noch keine — erstes Wochen-Review am Sonntag, 14.06.2026)_

---

## Muster-Zähler

| Muster | Vorkommen | IDs | Trend |
|---|---|---|---|
| Konzentration ohne Risiko-Kennzahl | 1 | F-S-001 | beobachten |
| Automatik ohne Stabilisierungs-Bedingung | 1 | F-S-002 | beobachten |
| Ungesicherte Datenquelle im Entscheidungsweg | 1 | F-S-003 | rückläufig (14→7 Fehlalarme/Tag) |
