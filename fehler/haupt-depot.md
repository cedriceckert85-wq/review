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

### F-H-002 · 2026-06-08–10 · Einstiegs-Timing: jeder Kauf sofort im Minus
- **Was passiert ist:** NVDA, CEG, IWM — alle drei Positionen notierten unmittelbar nach Kauf im Minus. Käufe erfolgten in fallende Kurse hinein, ohne Bestätigung (kein Stabilisierungs-Kriterium).
- **Einstufung:** UNKLAR — bei n=3 kann das Zufall sein. Wird zum SKILL-FEHLER, wenn sich das Muster bei den nächsten 5 Einstiegen fortsetzt.
- **Messlatte:** Anteil der Einstiege, die nach 2 Handelstagen im Minus sind. > 70 % bei n≥8 → SKILL-FEHLER „kauft fallende Messer".
- **Update 11.06.2026 (22:00):** Stand Tag 4: NVDA −2,76 %, CEG −2,16 %, IWM +0,40 %. IWM erstmals leicht positiv — 2/3 noch im Minus. Muster läuft weiter.
- **Update 12.06.2026 (17:57):** AMZN neu eingegangen zu 236,56 — sofort −0,13 % auf Einstand. **n=4, alle 4 Einstiege sofort im Minus.** IWM-Aufstockung (294,25) nur marginal unter aktuellem Kurs (294,11). Das Muster ist bei n=4 eindeutiger als bei n=3. Messlatte rückt näher.
- **Update 13.06.2026 (17:00, Sa):** Wochenende, kein neuer Einstieg. Fr-Schluss im (eingefrorenen) 17:48-Haupt-Stand: NVDA −2,05 %, CEG −1,46 %, IWM +0,43 %, AMZN −0,13 %. Der echte CEG-Schluss (253,76 laut Auto-Kursen) liegt bei +0,42 % auf Einstand — der 17:48-Stand überzeichnet das Muster also leicht. n=4 unverändert, Messlatte n≥8 weiter offen.
- **Update 14.06.2026 (17:00, So — Wochen-Review KW24):** Daten eingefroren ggü. Sa, n=4 unverändert. Erkenntnis aus dem Wochen-Review: Dieser Eintrag und der neue **F-H-004 (AMD-Chase)** teilen dieselbe Wurzel — *Einstieg ohne Bestätigung*. F-H-002 ist Kauf in Schwäche, F-H-004 ist Chase in Stärke; beidem fehlt ein Stabilisierungs-/Bestätigungskriterium. Eine einzige Einstiegs-Bestätigungsregel würde beide adressieren. Die Diagnose „kauft fallende Messer" war damit zu eng.
- **Update 15.06.2026 (17:00, 1. Montagslauf):** Frische Kurse — die 4 Alt-Einstiege haben sich erholt (NVDA −0,01 %, CEG +3,84 %, IWM +0,80 %, AMZN +3,88 %): das „sofort im Minus" war Einstiegs-*Timing*, nicht Titelauswahl. Neuer 5. Einstieg XLP (85,43 €) notiert +0,04 % — der ERSTE, der nicht sofort ins Minus läuft. Aber XLP ist ein defensiver, niedrig-volatiler ETF (kein Chase, keine Schwäche) und damit kein sauberer Test der Messer-These; **n bleibt 4**. Eine Einstiegs-Bestätigungsregel wurde weiterhin NICHT eingeführt.
- **Status:** OFFEN (n=4, alle 4 Alt-Einstiege erholt aber ex post — Timing-Leck; Messlatte bei n≥8; Wurzel teilt sich mit F-H-004)

### F-H-003 · 2026-06-11 · Stop-Abstand im Nachrichtensturm (NVDA 0,7 %)
- **Was passiert ist:** NVDA-Stop 199 lag nur 0,7 % unter dem Kurs — bei 3–4 % Tagesschwankung (Iran + CPI) ist das innerhalb des Rauschens.
- **Einstufung:** UNKLAR → stark Richtung SKILL-FEHLER — NVDA fiel am 11.06. intraday auf 199,88 (nur 0,4 % über Stop 199). Der Stop wurde nicht getriggert, weil Trumps Iran-Nacht-Absage eine Relief-Rally auslöste (exogenes Glück, kein Prozess-Verdienst). Das Rauschen hat den Stop beinahe ausgelöst — das ist ein starkes Indiz für einen zu engen Stop, unabhängig vom Ausgang.
- **Messlatte:** Reißt der Stop 199 und erholt sich NVDA danach über 205 → SKILL-FEHLER (klassischer Whipsaw). Fällt NVDA nach Stop-Riss weiter unter 195 → enger Stop war richtig.
- **Update 11.06.2026 (22:00):** Near-Miss 199,88 am 11.06. bestätigt Kernthese der Hypothese H3 → L4. Endgültige Einstufung bei nächstem Stop-Riss.
- **Update 12.06.2026 (17:57):** NVDA aktuell 205,17 — Stop 199 nun 3,0 % entfernt (deutlich entspannter). Keine Gefahr mehr kurzfristig. Messlatte (Stop reißt, NVDA erholt sich danach über 205) nicht getriggert. Die ursprüngliche Fehlplatzierung (0,7 % Abstand) war trotzdem ein Fehler — das Rauschen hat den Stop beinahe ausgelöst, gerettet durch exogenes Geopolitik-Glück. Max. Haltedauer endet 15.06. — dann Verlängerung oder Zeit-Exit.
- **Update 13.06.2026 (17:00):** NVDA 205,17, Stop 199 = 3,0 % entfernt. **Die maximale Haltedauer endet Mo 15.06.** — die Verlängerungs-/Zeit-Exit-Entscheidung steht beim Montags-Lauf an und ist der nächste konkrete Prüfpunkt dieses Eintrags.
- **Update 14.06.2026 (17:00, So — Wochen-Review KW24):** Daten eingefroren, Messlatte unverändert nicht getriggert. **Mo 15.06. ist der entscheidende Prüfpunkt:** endet die Haltedauer (Tag 7/7), ist der NVDA-Zeit-Exit zu vollziehen; reißt dabei der Stop 199 und NVDA erholt sich danach über 205 → SKILL-FEHLER (Whipsaw), sonst war die enge Platzierung gerade noch tragbar. Bis dahin OFFEN.
- **Update 15.06.2026 (17:00):** Auflösung der Stop-Frage zugunsten von „benigne": NVDA hat den Stop 199 nach dem Near-Miss vom 11.06. NIE wieder getestet und ist auf 209,44 € (Breakeven, −0,01 %) zurückgekehrt. Die Messlatte (Stop reißt + Erholung > 205) ist nicht getriggert worden — die enge Platzierung war ex post folgenlos, das Near-Miss vom 11.06. war bestätigt Intraday-Rauschen (stützt L4). ABER ein NEUER Punkt: Der **Zeit-Exit (7-Tage-Limit) wurde NICHT vollzogen** — das Dashboard zeigt **Tag 8/7**, NVDA wurde über das eigene Limit hinaus gehalten. Eine ganze Woche Kapitalbindung (70 €) für 0 % Ergebnis = Opportunitätskosten. Ob bewusste Verlängerung oder Disziplin-Slip ist unklar (Dashboard: „Entscheidung ausstehend"). Verbesserungspunkt 3 der Vorwoche (Zeit-Exit konsequent einhalten) damit faktisch ignoriert.
- **Update 15.06.2026 (22:00):** NVDA schloss bei 212,20 € (+1,31 %) — Stop 199 endgültig nie wieder getestet, die Stop-Abstands-Frage ist damit benigne erledigt (L4 voll bestätigt). Zeit-Exit weiter NICHT vollzogen (Tag 8/7); Dashboard verschiebt die Entscheidung auf den Abend-Check / Di. Wird die Position Di ohne dokumentierte neue These weiter gehalten, verfestigt sich die Zeit-Exit-Disziplin-Lücke.
- **Update 16.06.2026 (17:30):** Der für heute (Di) erwartete Zeit-Exit-Prüfpunkt ist NICHT verifizierbar — das Haupt-Dashboard ist auf Mo 15.06. 19:04 eingefroren (Tag-Zähler unverändert Tag 8/7, kein Di-Stand). Ob die NVDA-Position heute ge-exited, verlängert oder unverändert weiterläuft, ist mangels frischer Daten offen. Nächster prüfbarer Punkt: erster Lauf mit aktualisiertem Haupt-Dashboard (L6 gilt auch werktags).
- **Update 16.06.2026 (22:30, Schluss):** Der NVDA-Zeit-Exit ist VOLLZOGEN — Verkauf zu 208,57 € (−0,49 %, −0,34 € realisiert), Position glattgestellt, Cash-Quote auf 70 %. Damit ist die Disziplin-Lücke geschlossen, aber 2 Tage zu spät (Tag 9 statt Tag 7): Hätte die Position am Mo-Stand 212,20 € (Tag 8) gegriffen, wäre +1,31 % statt −0,49 % realisiert worden — die Verzögerung kostete ~1,8 Pp / ~1,25 € auf die 70-€-Position. Einstufung der Lateness: SKILL-FEHLER (vermeidbarer Disziplin-Slip), aber kleine Magnitude. Die Stop-Abstands-Frage bleibt benigne erledigt (L4).
- **Update 17.06.2026 (17:30):** NEUER Zeit-Exit-Prüfpunkt am selben Muster — CEG steht bei Tag 10/10 (Max-Haltedauer erreicht) und nahe Ziel 273 (271,35 €, +7,39 %). Wird CEG heute/morgen pünktlich am Limit ge-exited (oder via Ziel 273), ist die NVDA-Lateness ein Einzel-Slip; läuft CEG wie NVDA über das eigene Limit hinaus, verfestigt sich „Zeit-Exit nicht eingehalten" zur Gewohnheit (n=2). Pre-FOMC hält Haupt korrekt still (keine Neukäufe, 70 % Cash).
- **Status:** ENTSCHEIDUNGSREIF (NVDA-Teil) — Stop-Abstand benigne, NVDA-Zeit-Exit vollzogen (spät, kleiner SKILL-Slip); NEU offen: CEG Tag 10/10 als zweiter Zeit-Exit-Test. Im KW25-Wochen-Review auswerten.

### F-H-004 · 2026-06-08/10 · Momentum-Chase ohne Pullback (AMD)
- **Was passiert ist:** AMD am +5,8 %-Tag (08.06., 493,40) ohne Rücksetzer gekauft („Chase am +5,8 %-Tag", im Agenten-Kommentar schon als Lesson-Kandidat markiert); 10.06. Stop 469 gerissen, −4,36 % (−2,17 € realisiert).
- **Einstufung:** SKILL-FEHLER — der überdehnte Einstieg (Kauf am Hoch eines +5,8 %-Tags ohne Pullback/Bestätigung) ist der vermeidbare Prozessfehler. Der Stop-Exit selbst war diszipliniert (das ist der PECH-Anteil am schlechten Ergebnis, nicht der Können-Fehler).
- **Lehre:** Überdehnte Momentum-Tage (>+4 %) nicht chasen — auf Pullback zur Ausbruchszone / zum gleitenden Durchschnitt warten. Spiegelbild zu F-H-002 (dort Kauf in Schwäche): gemeinsame Wurzel ist *Einstieg ohne Bestätigung*.
- **Messlatte:** SKILL-FEHLER bestätigt sich als Gewohnheit, wenn ein weiterer Kauf an einem >+4 %-Tag innerhalb der nächsten 4 Wochen wieder vor Erreichen des Ziels ausgestoppt wird (n≥2). Einmaliges Vorkommen bleibt ein dokumentierter, aber nicht überzubewerteter Einzelfehler.
- **Kosten:** −2,17 € realisiert
- **Status:** OFFEN (n=1 — neu im Wochen-Review KW24 formalisiert; Wurzel teilt sich mit F-H-002)

---

## Erledigte Einträge (im Wochen-Review abgeschlossen)

### F-H-001 · 2026-06-09/10 · Gold als Kriegs-Hedge gekauft — **SKILL-FEHLER** (KW24 abgeschlossen)
- GLD als Iran-Kriegs-Hedge gekauft, fiel TROTZ Eskalation, Verkauf −5,20 % (−2,09 € realisiert). „Krise → Gold steigt" war eine ungeprüfte Reflexannahme; Gold fällt regelmäßig bei steigendem Dollar/Realzins (CPI 4,2 %).
- **Urteil KW24:** entschieden als SKILL-FEHLER, Trade geschlossen, Lehre in L1 verankert (Hedge-Thesen vor Kauf an ≥3 historischen Episoden prüfen). Wiederholung wird über den Muster-Zähler „Ungetestete Makro-These" verfolgt.

---

## Muster-Zähler

| Muster | Vorkommen | IDs | Trend |
|---|---|---|---|
| Ungetestete Makro-These | 1 | F-H-001 (erledigt KW24, SKILL-FEHLER) | abgeschlossen — Wiederholung beobachten |
| **Einstieg ohne Bestätigung** (Oberkategorie) | 2 (Schwäche + Stärke) | F-H-002, F-H-004 | **verfestigt sich** — beide Eintritts-Muster ohne Bestätigung |
| — Kauf ohne Bestätigung in Schwäche | 1 (4 Trades: NVDA, CEG, IWM, AMZN) | F-H-002 | Tendenz SKILL-FEHLER — alle 4 sofort im Minus |
| — Momentum-Chase ohne Pullback (Stärke) | 1 (AMD) | F-H-004 | neu (KW24) — n=1, auf Wiederholung achten |
| Stop im Rauschen platziert | 1 | F-H-003 | benigne ausgegangen — NVDA nie wieder am Stop, zurück auf Breakeven (Rauschen-These bestätigt, L4) |
| Zeit-Exit nicht eingehalten | 1 (CEG-Test offen) | F-H-003 (NVDA Tag 9; CEG Tag 10/10) | NVDA 16.06. spät vollzogen (~1,8 Pp); 17.06. CEG bei Tag 10/10 nahe Ziel 273 = nächster Test, ob pünktlich (Einzel-Slip) oder Gewohnheit (n=2) |
