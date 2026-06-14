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
- **Update 12.06.2026 (17:57):** RKLB-Short profitabel gecovert (+5,25 €). Das taktische Gegen-Buch ist abgeschlossen — das offene Aktienbuch ist nun wieder 100 % Quantum (QBTS/IONQ/RGTI). Teilweise Divergenz der Titel heute (RGTI +6,58 % vs. QBTS −1,33 %) zeigt, dass die Korrelation nicht ~1 ist. Trotzdem: ein einziger negativer Quantum-Katalysator würde alle drei gleichzeitig treffen. Strukturell keine Verbesserung, Tranche 2 (Space/Diversifikation) weiter offen.
- **Update 13.06.2026 (17:00, Sa):** Fr-Schluss — alle drei Quantum-Titel im Plus (RGTI +7,87 %, IONQ +2,15 %, QBTS +0,52 %), Divergenz breit. Kein gemeinsamer Drawdown (kein Stressereignis), Klumpenrisiko strukturell unverändert; Tranche-2-Diversifikation (Space) weiter offen. Kein neuer Trade (Börse zu).
- **Update 14.06.2026 (17:00, So — Wochen-Review KW24):** Daten eingefroren, kein Stressereignis → Klumpenrisiko weiter ungetestet, aber strukturell unverändert (100 % Quantum nach RKLB-Cover). **PRIO-1-Empfehlung der Woche:** harte Themen-Obergrenze 60–70 % je Thema + Tranche 2 (Space) als erste echte Diversifikation. Der erste gemeinsame Quantum-Drawdown trifft sonst alle drei gleichzeitig.
- **Status:** OFFEN

### F-S-002 · 2026-06-11 · Nachkauf-Automatik in Story-Aktien
- **Was passiert ist:** Regel „IONQ < 50 $ / QBTS < 21 $ → aufstocken bis 500 €" — automatisches Averaging-down in unprofitable Spekulationswerte. Die Automatik erhöht genau dann, wenn die These bröckelt.
- **Einstufung:** UNKLAR — bewertbar, sobald ein Trigger auslöst (siehe Schatten-Depot D4). Strukturell ein klassischer Speku-Depot-Killer.
- **Messlatte:** Löst ein Nachkauf-Trigger aus: Fällt der Kurs danach weiter Richtung Stop → SKILL-FEHLER. Dreht die Position → die Automatik hatte (diesmal) recht.
- **Update 11.06.2026 (22:00):** IONQ 58,28 $, QBTS 24,05 $ — beide weit über Trigger-Niveaus. Kein Trigger.
- **Update 12.06.2026 (17:57):** IONQ 56,77 $, QBTS 22,94 $ — beide weiterhin weit über Trigger-Niveaus (50 $ bzw. 21 $). Kein Trigger ausgelöst.
- **Update 13.06.2026 (17:00):** IONQ 57,85 $, QBTS 23,37 $ — weit über Triggern (50 $ / 21 $). Kein Trigger.
- **Update 14.06.2026 (17:00, So — Wochen-Review KW24):** Unverändert, kein Trigger (Daten eingefroren). KW24-Empfehlung: Limit-Automatik durch eine Stabilisierungs-Bedingung ersetzen, bevor je ein Trigger im fallenden Markt feuert — Averaging-down per Limit bleibt der dokumentierte Speku-Killer.
- **Status:** OFFEN

### F-S-003 · 2026-06-11 · Scout-Fehlalarme als Prozessrisiko
- **Was passiert ist:** ~14 „Material"-Fehlalarme an Tag 1 (u. a. Quellen vom 04.06. für ein angebliches Ereignis „vom 13.06."). Alle wurden manuell abgefangen — im Voll-Autonom-Modus wäre jeder davon ein potenzieller Fehltrade.
- **Einstufung:** SKILL-FEHLER (Prozess) — kein Marktfehler, sondern eine ungesicherte Datenquelle im Entscheidungsweg.
- **Lehre:** Kein Handeln auf unverifizierte Meldungen (Quellendatum < 24 h + zwei unabhängige Quellen). Wird durch den Master-Fix technisch abgesichert.
- **Kosten:** 0 € (bisher abgefangen)
- **Update 11.06.2026 (22:00):** 7 Fehlalarme heute (Tag 2: down von ~14 auf 7) — Master-Fix greift, Verbesserung sichtbar. Noch nicht bei 0 Fehlalarmen.
- **Update 12.06.2026 (17:57):** Kein expliziter Fehlalarm-Count im Dashboard sichtbar. Beobachtung läuft weiter.
- **Update 14.06.2026 (17:00, So — Wochen-Review KW24):** Am Wochenende kein neuer Fehlalarm-Count belegbar (kein Scout-Lauf). KW24-Bilanz der Woche: Tag 1 ~14 → Tag 2 7 → danach unbelegt; Trend rückläufig, aber Ziel 0/Woche noch nicht erreicht und nicht verifizierbar. Bleibt SKILL-FEHLER (Prozess), bis eine volle Woche mit 0 unverifizierten Handels-Auslösern belegt ist.
- **Status:** OFFEN (Fehlalarm-Rate: Tag 1 ~14, Tag 2 7, danach unbelegt — Ziel: 0 über eine Woche)

---

## Erledigte Einträge (im Wochen-Review abgeschlossen)

### F-S-004 · 2026-06-11/12 · Overnight-Stop-Breach bei Extrem-Speku-Short (RKLB) — **PECH** (KW24 abgeschlossen)
- **Was passiert ist:** RKLB-Short (Stop 119,80) handelte nachbörslich am 11.06. bis 121,50 $ über den Stop; das mechanische Cover-at-Open (12.06., 106,05) rettete +5,25 € (+4,37 %).
- **Urteil KW24 gegen die Messlatte:** **PECH** — der Overnight-Breach entstand aus einem nicht-antizipierbaren After-Hours-Squeeze, und das Cover wurde mechanisch ausgeführt (kein Slippage-Verlust, sogar Gewinn). Damit ist exakt der PECH-Zweig der Messlatte erfüllt, nicht der SKILL-Zweig.
- **Leitplanke (bleibt gültig):** Das Designrisiko ist nicht „erledigt", weil es harmlos ausging — der nächste Extrem-Speku-Short braucht weiterhin (a) AH-Monitoring + enge Positionsgröße ODER (b) Day-only-Charakter. Schließt ein künftiger Short durch Overnight-Breach schlechter als sein Stop, wird dafür ein neuer SKILL-FEHLER-Eintrag eröffnet.

---

## Muster-Zähler

| Muster | Vorkommen | IDs | Trend |
|---|---|---|---|
| Konzentration ohne Risiko-Kennzahl | 1 | F-S-001 | beobachten — RKLB-Schließung macht 100 % Quantum wieder vollständig |
| Automatik ohne Stabilisierungs-Bedingung | 1 | F-S-002 | beobachten — kein Trigger |
| Ungesicherte Datenquelle im Entscheidungsweg | 1 | F-S-003 | rückläufig (14→7→unbekannt Fehlalarme/Tag) |
| Kein AH-Schutz für Extrem-Speku-Short | 1 | F-S-004 (erledigt KW24, PECH) | abgeschlossen — Leitplanke aktiv, neuer Eintrag bei künftigem Breach |
