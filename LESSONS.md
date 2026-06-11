# Lektionen-Speicher (Fehler-Lernen)

Dieser Speicher wird bei jedem Review-Lauf gelesen und fortgeschrieben.
Vor jeder neuen Bewertung prüfen: Welche früheren Einschätzungen waren falsch, welche richtig?

## Offene Hypothesen (bei nächsten Läufen prüfen)

- **H1 (11.06.2026):** Das Haupt-Depot kauft systematisch in Schwäche ohne Bestätigung — drei Käufe, drei Positionen sofort im Minus. → Bei künftigen Trades prüfen, ob Einstiege weiter sofort ins Minus laufen.
- **H2 (11.06.2026):** Das Quantum-Klumpenrisiko im Speku-Depot (QBTS/IONQ/RGTI, Korrelation ~1) wird sich bei der nächsten Marktschwäche in einem gleichzeitigen Drawdown aller drei Positionen zeigen.
- **H3 (11.06.2026):** NVDA-Stop bei 199: Wenn der Stop reißt und sich der Kurs danach erholt (Whipsaw), ist das ein Hinweis, dass die Stops des Haupt-Depots zu eng am Markt-Rauschen liegen. → *Stand 17:03 Uhr: NVDA bei 199,95 — nur 0,5 % über dem Stop. Oracle-Catalyst hat NVDA nicht gestützt; Relative-Stärke-These inhaltlich gebrochen.*

## Bestätigte Lektionen

- **L1 (11.06.2026):** Makro-Reflexe sind keine Strategie. „Geopolitik-Krise → Gold steigt" ist gescheitert (GLD −5,20 % trotz Iran-Eskalation). Hedge-Thesen müssen vor dem Kauf an historischen Episoden geprüft werden.
- **L2 (11.06.2026, 13:48 — bestätigt aus H4):** Lokaler Checkout ist die robuste Primärquelle. Der Agent liest `index.html` und `speku.html` direkt aus dem `epmt-dashboard`-Checkout — das umgeht HTTP 403 bei GitHub Pages vollständig. Die Review-Pipeline ist damit unabhängig von öffentlichem Netzzugang zu den Pages-URLs.
- **L3 (11.06.2026, 13:48):** Die Dashboards aktualisieren Kursdaten nur ~16 Uhr und ~22 Uhr Berlin-Zeit. Läufe zwischen diesen Zeiten finden immer dieselben Preisdaten vor. Der Erkenntnisgewinn in Zwischenläufen liegt im News/Kontext-Update, nicht in neuen Kursen — Kursvergleiche zwischen Zwischenläufen sind daher sinnlos.

## Verworfene Annahmen

_(noch keine)_

## Eigene Prognose-Bilanz des Reviewers

Hier wird festgehalten, welche Einschätzungen aus früheren Reviews sich als richtig oder falsch erwiesen haben — der Reviewer bewertet sich selbst mit.

| Datum | Einschätzung | Ergebnis | Urteil |
|-------|--------------|----------|--------|
| 11.06.2026 (14:05) | NVDA 0,7 % vom Stop 199 — Whipsaw-Gefahr, Stop trotzdem halten | 17:03 Uhr: NVDA 199,95 — Stop noch nicht gerissen, aber Oracle-Catalyst hat nicht geholfen. Entscheidung bis 22:00 Uhr. | Ausstehend |
| 11.06.2026 (14:05) | IWM-Kauf (Chips→Small-Cap-Rotation) blutet Tag 2 weiter | IWM 284,97 (+1,04 % am 11.06., 17:03 Uhr) — Rotations-These zeigt Stärke, kein weiteres Bluten | **FALSCH** |
| 11.06.2026 (14:05) | Quantum-Positionen: bei nächster Marktschwäche gleichzeitiger Drawdown aller drei | Kein Stressereignis heute — QBTS/IONQ/RGTI alle positiv auf Einstand | Ausstehend |
| 11.06.2026 (13:48) | Oracle-Earnings (Capex 70 Mrd. $) → AI-Hardware vorbörslich im Plus; NVDA wird Stop 199 heute halten und eröffnet ≥ 201 | NVDA 199,95 (17:03) — nicht ≥ 201; fällt trotz Oracle-Catalyst. CEG +1,83 % bestätigt AI-Strom-Rückenwind ✓, NVDA-Magnitude ✗ | **TEILWEISE FALSCH** (CEG ✓, NVDA ✗) |
| 11.06.2026 (17:04) | NVDA reißt den Stop 199 heute noch — Relative-Stärke-These ist gebrochen (kein Catalyst hilft) | Offen — US-Markt bis 22:00 Uhr | Ausstehend |
