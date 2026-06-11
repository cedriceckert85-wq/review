# Fehler-Akte: Haupt-Depot (Regel-Trader)

Jeder Eintrag hat eine ID (F-H-001, …), eine Einstufung und einen Status.

**Einstufung:**
- **SKILL-FEHLER** — Prozessfehler oder ungetestete Annahme. War vermeidbar. Muss abgestellt werden.
- **PECH** — Prozess war korrekt, Ergebnis trotzdem schlecht. Kein Handlungsbedarf, nicht überreagieren.
- **UNKLAR** — noch nicht entscheidbar, mehr Daten nötig.

Diese Akte wird bei jedem Lauf gepflegt und sonntags im Wochen-Review ausgewertet.
Ziel: Muster erkennen → abstellen → profitabler Trader. Ein Fehler, der zweimal vorkommt, ist kein Fehler mehr, sondern eine Gewohnheit.

---

## Offene Fehler / Beobachtungen

### F-H-001 · 2026-06-09/10 · Gold als Kriegs-Hedge gekauft
- **Was passiert ist:** GLD als Hedge auf die Iran-Eskalation gekauft. Gold fiel trotz Eskalation, Verkauf zu −5,20 % (−2,09 €).
- **Einstufung:** SKILL-FEHLER — „Krise → Gold steigt" war eine Reflexannahme ohne Prüfung. Gold fällt regelmäßig auch in Geopolitik-Stress, wenn Dollar und Realzinsen steigen (CPI 4,2 %!).
- **Lehre:** Hedge-Thesen vor dem Kauf an mindestens 3 historischen Episoden prüfen.
- **Kosten:** −2,09 € realisiert
- **Status:** OFFEN

### F-H-002 · 2026-06-08–10 · Einstiegs-Timing: jeder Kauf sofort im Minus
- **Was passiert ist:** NVDA, CEG, IWM — alle drei Positionen notierten unmittelbar nach Kauf im Minus. Käufe erfolgten in fallende Kurse hinein, ohne Bestätigung (kein Stabilisierungs-Kriterium).
- **Einstufung:** UNKLAR — bei n=3 kann das Zufall sein. Wird zum SKILL-FEHLER, wenn sich das Muster bei den nächsten 5 Einstiegen fortsetzt.
- **Messlatte:** Anteil der Einstiege, die nach 2 Handelstagen im Minus sind. > 70 % bei n≥8 → SKILL-FEHLER „kauft fallende Messer".
- **Status:** OFFEN (Beobachtung läuft)

### F-H-003 · 2026-06-11 · Stop-Abstand im Nachrichtensturm (NVDA 0,7 %)
- **Was passiert ist:** NVDA-Stop 199 lag nur 0,7 % unter dem Kurs — bei 3–4 % Tagesschwankung (Iran + CPI) ist das innerhalb des Rauschens.
- **Einstufung:** UNKLAR — wird zum SKILL-FEHLER, wenn der Stop reißt und der Kurs sich danach erholt (Whipsaw). War der Stop-Riss der Beginn eines echten Abverkaufs, war der enge Stop richtig.
- **Messlatte:** Kursverlauf nach Stop-Riss beobachten (siehe Schatten-Depot D1).
- **Status:** OFFEN

---

## Erledigte Einträge (im Wochen-Review abgeschlossen)

_(noch keine — erstes Wochen-Review am Sonntag, 14.06.2026)_

---

## Muster-Zähler

| Muster | Vorkommen | IDs | Trend |
|---|---|---|---|
| Ungetestete Makro-These | 1 | F-H-001 | neu |
| Kauf ohne Bestätigung in Schwäche | 1 (3 Trades) | F-H-002 | beobachten |
| Stop im Rauschen platziert | 1 | F-H-003 | beobachten |
