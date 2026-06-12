# Lektionen-Speicher (Fehler-Lernen)

Dieser Speicher wird bei jedem Review-Lauf gelesen und fortgeschrieben.
Vor jeder neuen Bewertung prüfen: Welche früheren Einschätzungen waren falsch, welche richtig?

## Offene Hypothesen (bei nächsten Läufen prüfen)

- **H1 (11.06.2026):** Das Haupt-Depot kauft systematisch in Schwäche ohne Bestätigung — drei Käufe, drei Positionen sofort im Minus. Stand 22:00 Uhr: NVDA −2,76 %, CEG −2,16 %, IWM +0,40 %. Bei künftigen Trades prüfen, ob Einstiege weiter sofort ins Minus laufen. **Update 12.06.2026 (17:57):** AMZN als vierter Einstieg eingegangen — sofort −0,13 % auf Einstand. n=4, alle 4 Einstiege sofort im Minus. Muster festigt sich; Messlatte (>70 % bei n≥8 → SKILL-FEHLER) rückt näher.
- **H2 (11.06.2026):** Das Quantum-Klumpenrisiko im Speku-Depot (QBTS/IONQ/RGTI, Korrelation ~1) wird sich bei der nächsten Marktschwäche in einem gleichzeitigen Drawdown aller drei Positionen zeigen. Heute keine Marktschwäche (SPY +1,07 %, alle drei Quantum-Titel im Plus) — Hypothese ungetestet. **Update 12.06.2026:** Teilweise Divergenz sichtbar — RGTI +6,58 %, QBTS −1,33 %, IONQ +0,25 %. Korrelation ist nicht ~1 auf Tagesbasis; strukturelles Klumpenrisiko bleibt trotzdem bestehen.
- **H6 (12.06.2026) — RANGLISTEN-PROGNOSE des Reviewers (Nutzerfrage „wer performt am besten?"):**
  Risikoadjustierte Rangfolge über 4 Wochen (Stichtag 10.07.2026): 1. Schatten-Depot
  (Subtraktions-Edge: gleiches Buch minus dokumentierte Fehler), 2. Swing-Agent (beste
  Prozessarchitektur, Edge unbewiesen), 3. Haupt-Depot (Disziplin top, Einstiegs-Timing offen),
  4. Speku-Depot (höchste Varianz — Kandidat für nominal besten UND schlechtesten Platz
  zugleich). Hintergrund-These: Wahrscheinlichster Gesamtsieger bleibt SPY Buy&Hold (SPIVA).
  Messlatten am 10.07.: (a) Schatten-Rendite > Haupt-Rendite, (b) Swing-Erwartungswert ≥ 0 R,
  (c) Speku belegt nominal Platz 1 ODER Platz 4 der vier Depots. Jede Teilprognose wird
  einzeln als richtig/falsch gewertet.

## Bestätigte Lektionen

- **L1 (11.06.2026):** Makro-Reflexe sind keine Strategie. „Geopolitik-Krise → Gold steigt" ist gescheitert (GLD −5,20 % trotz Iran-Eskalation). Hedge-Thesen müssen vor dem Kauf an historischen Episoden geprüft werden.
- **L2 (11.06.2026, 13:48 — bestätigt aus H4):** Lokaler Checkout ist die robuste Primärquelle. Der Agent liest `index.html` und `speku.html` direkt aus dem `epmt-dashboard`-Checkout — das umgeht HTTP 403 bei GitHub Pages vollständig. Die Review-Pipeline ist damit unabhängig von öffentlichem Netzzugang zu den Pages-URLs.
- **L3 (11.06.2026, 13:48):** Die Dashboards aktualisieren Kursdaten nur ~16 Uhr und ~22 Uhr Berlin-Zeit. Läufe zwischen diesen Zeiten finden immer dieselben Preisdaten vor. Der Erkenntnisgewinn in Zwischenläufen liegt im News/Kontext-Update, nicht in neuen Kursen — Kursvergleiche zwischen Zwischenläufen sind daher sinnlos.
- **L4 (11.06.2026, 22:00 — bestätigt aus H3):** Ein Stop, der reguläres Intraday-Rauschen fast auslöst, ist kein Schutz — er ist nur ein schlechterer Verkaufskurs. NVDA fiel intraday auf 199,88 (0,4 % vom Stop 199), erholte sich dann durch Trumps Iran-Nacht-Absage auf 203,68. Der Stop wurde nicht benötigt, aber die Nähe war reines Intraday-Rauschen, kein Trendsignal. Stops sollten mindestens 1 ATR (Average True Range) unter dem letzten Swing-Tief liegen — nicht am Rand des täglichen Rauschens.
- **L5 (12.06.2026 — bestätigt aus H5):** Sell-the-News-Thesen funktionieren, wenn der Auslöser konkret und binär ist. Der RKLB-Short (SpaceX-IPO-Fade) schloss profitabel zu 106,05 (+5,25 €, +4,37 %) — RKLB eröffnete am SPCX-Listing-Tag auf 109,50 und fiel weiter. Der binäre Test lieferte exakt das erwartete Ergebnis. Zweite Erkenntnis: Ein nachbörslicher Stop-Breach (RKLB 121,50 vs. Stop 119,80) wurde durch mechanisches Cover zur Markteröffnung gerettet — das Regelwerk funktioniert unter Druck. Der Overnight-Squeeze war PECH; das Covered-at-Open war korrekte Prozessausführung.

## Verworfene Annahmen

_(noch keine)_

## Eigene Prognose-Bilanz des Reviewers

Hier wird festgehalten, welche Einschätzungen aus früheren Reviews sich als richtig oder falsch erwiesen haben — der Reviewer bewertet sich selbst mit.

| Datum | Einschätzung | Ergebnis | Urteil |
|-------|--------------|------------|--------|
| 11.06.2026 (14:05) | NVDA 0,7 % vom Stop 199 — Whipsaw-Gefahr, Stop trotzdem halten | 22:00: NVDA 203,68 — Stop 199 nicht gerissen. Tief 199,88 durch Iran-Panik, Erholung durch Trumps Iran-Absage. Stop halten war die richtige Prozessentscheidung. | **RICHTIG** |
| 11.06.2026 (14:05) | IWM-Kauf (Chips→Small-Cap-Rotation) blutet Tag 2 weiter | IWM 284,97 → 289,91 (+0,40 % auf Einstand) — keine Blutung, stattdessen Erholung | **FALSCH** |
| 11.06.2026 (14:05) | Quantum-Positionen: bei nächster Marktschwäche gleichzeitiger Drawdown aller drei | Kein Stressereignis heute — QBTS +3,44 % / IONQ +2,91 % / RGTI +6,32 %, alle positiv auf Einstand | Ausstehend |
| 11.06.2026 (13:48) | Oracle-Earnings (Capex 70 Mrd. $) → AI-Hardware vorbörslich im Plus; NVDA wird Stop 199 heute halten und eröffnet ≥ 201 | NVDA 203,68 (22:00) — hielt dank Iran-Deeskalation, nicht Oracle allein. CEG AI-Strom-Rückenwind ✓, NVDA-Magnitude ohne externe Hilfe ✗ | **TEILWEISE FALSCH** (CEG ✓, NVDA ✗ ohne Geopolitik-Hilfe) |
| 11.06.2026 (17:04) | NVDA reißt den Stop 199 heute noch — Relative-Stärke-These ist gebrochen (kein Catalyst hilft) | 22:00: NVDA 203,68 — Stop 199 NICHT gerissen. Tief 199,88 um 19:18, dann +2,0 % durch Trumps Iran-Nacht-Absage | **FALSCH** |
| 11.06.2026 (22:00) | SpaceX-SPCX-Listing 12.06. löst Sell-the-News bei RKLB aus — RKLB-Short schließt vor Zeit-Exit 15.06. profitabel (Schlusskurs < 110,90) | 12.06.: RKLB eröffnet zu 109,50 (Gap-Down trotz Stop-Breach 121,50 nach Börsenschluss), fällt auf 106,05 (Cover). +5,25 € (+4,37 %). Sell-the-News hat exakt geliefert. | **RICHTIG** |
| 12.06.2026 (D5) | Reviewer hat RKLB-Short bewusst nicht mitgemacht — Risk-on-Umfeld nach Iran-Deeskalation als zu gefährlich eingestuft | 12.06.: RKLB-Short profitabel (+5,25 €, +4,37 %). Reviewer hat kontrollierten, ertrag­reichen Trade verpasst. Risk-on-Rallye schließt einen kalibrierten Extrem-Speku-Short nicht aus. | **FALSCH** |
| 12.06.2026 (H6) | Ranglisten-Prognose 4 Wochen: Schatten > Swing > Haupt; Speku = Platz 1 oder 4 (Varianz). Drei Messlatten (a/b/c), Stichtag 10.07. | Offen | Ausstehend |
