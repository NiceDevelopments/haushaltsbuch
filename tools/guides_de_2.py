"""Zusatz-Anleitungen (deutsch), angelegt 24.11.2026. Aufbau wie content_de.py "guides".

Suchnachfrage (Google-Autocomplete 24.11.2026): 50 30 20 regel (rechner, funktioniert nicht),
wie viel geld für lebensmittel pro monat (1/2/4 personen), umschlagmethode (digital, app),
kakeibo methode, notgroschen wie hoch / aufbauen, sparen mit wenig einkommen, no spend challenge,
ausgaben tracken kategorien, kassenzettel scannen / entsorgen / welcher müll, abos kündigen android,
impulskäufe vermeiden, wie viel sollte man für miete ausgeben, haushaltsbuch app für paare,
budget planen als freelancer.

Regeln: nur Fakten, die stimmen; Beispielbeträge erfunden; keine Rang- oder Superlativaussagen
über die App. Die App kann KEINE Auswertung nach Kategorien, keine Umschläge je Kategorie,
keine Synchronisierung, kein Belegarchiv (das Zettelbild wird nicht gespeichert).
"""

U = "2026-11-24"
UL = "November 2026"

GUIDES = [
    # ------------------------------------------------------------ 50/30/20
    {
        "id": "rule503020",
        "slug": "50-30-20-regel",
        "title": "50/30/20-Regel: so rechnest du sie – und was tun, wenn sie nicht passt",
        "desc": "Die 50/30/20-Regel teilt dein Netto in Bedarf, Wünsche und Sparen. Mit Rechenbeispiel und Varianten, wenn die Fixkosten schon mehr als die Hälfte fressen.",
        "h1": "50/30/20-Regel: Rechnung, Beispiel und Grenzen",
        "teaser": "Netto aufteilen in Bedarf, Wünsche und Sparen – und was tun, wenn 50 % nicht reichen.",
        "answer": "**Die 50/30/20-Regel teilt dein Netto-Einkommen in drei Töpfe: 50 % für das, was du brauchst, 30 % für das, was du willst, 20 % zum Sparen.** Bei 2.400 € netto sind das 1.200 €, 720 € und 480 €. Liegen deine festen Kosten schon über der Hälfte, ist die Regel kein Maßstab, sondern ein Richtwert – dann rechnest du mit 60/30/10 oder 70/20/10.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "fixed", "savehowmuch"],
        "sections": [
            ["rechnung", "So rechnest du die 50/30/20-Regel", [
                "Ausgangspunkt ist, was netto auf dem Konto ankommt – nicht das Brutto. Dann teilst du:",
                {"table": [
                    ["Topf", "Anteil", "Was hineingehört"],
                    ["Bedarf", "50 %", "Miete, Nebenkosten, Strom, Versicherungen, Lebensmittel, Weg zur Arbeit, Kreditraten"],
                    ["Wünsche", "30 %", "Essen gehen, Hobbys, Streaming, Kleidung über das Nötige hinaus, Urlaub"],
                    ["Sparen", "20 %", "Notgroschen, Rücklagen, Altersvorsorge, Sondertilgung"],
                ]},
                {"calc": [["Netto-Einkommen", "2.400,00 €"], ["50 % Bedarf", "1.200,00 €"], ["30 % Wünsche", "720,00 €"], ["**20 % Sparen**", "480,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Die Regel wurde durch das Buch *All Your Worth* von Elizabeth Warren und Amelia Warren Tyagi bekannt. Ihr Reiz: drei Zahlen statt zwanzig Budgetposten.",
                {"table": [
                    ["Netto", "50 % Bedarf", "30 % Wünsche", "20 % Sparen"],
                    ["1.500 €", "750 €", "450 €", "300 €"],
                    ["2.000 €", "1.000 €", "600 €", "400 €"],
                    ["2.500 €", "1.250 €", "750 €", "500 €"],
                    ["3.000 €", "1.500 €", "900 €", "600 €"],
                    ["3.500 €", "1.750 €", "1.050 €", "700 €"],
                ]},
            ]],
            ["passt-nicht", "Wenn 50 % für den Bedarf nicht reichen", [
                "In Städten mit hohen Mieten oder bei kleinem Einkommen frisst allein das Wohnen oft die Hälfte. Dann ist die Regel nicht falsch, sie passt nur nicht zu deiner Lage. Zwei gängige Varianten:",
                {"calc": [["Netto-Einkommen", "2.400,00 €"], ["60 % Bedarf", "1.440,00 €"], ["30 % Wünsche", "720,00 €"], ["**10 % Sparen**", "240,00 €"]],
                 "caption": "Variante 60/30/10, gleiche erfundene Zahlen"},
                {"calc": [["Netto-Einkommen", "2.400,00 €"], ["70 % Bedarf", "1.680,00 €"], ["20 % Wünsche", "480,00 €"], ["**10 % Sparen**", "240,00 €"]],
                 "caption": "Variante 70/20/10, gleiche erfundene Zahlen"},
                "Wichtig ist die Reihenfolge, nicht die exakte Prozentzahl: **Das Sparen kommt zuerst** – per Dauerauftrag am Tag nach dem Gehalt. Wünsche bekommen, was danach übrig ist.",
                {"note": "Ein Prozentsatz, den du jeden Monat schaffst, ist mehr wert als 20 %, die du nach drei Monaten aufgibst."},
            ]],
            ["abgrenzung", "Bedarf oder Wunsch? Die Grauzonen", [
                {"list": [
                    "**Lebensmittel:** Der Grundeinkauf ist Bedarf, der Feinkostladen ist Wunsch.",
                    "**Handyvertrag:** Ein Vertrag ist Bedarf, das teure Modell mit Ratenzahlung zum Teil Wunsch.",
                    "**Auto:** Wer es für den Weg zur Arbeit braucht, zählt es zum Bedarf; der Zweitwagen ist Wunsch.",
                    "**Kreditraten:** Der Mindestbetrag gehört zum Bedarf, eine freiwillige Sondertilgung zum Sparen.",
                ]},
                "Sei ehrlich, aber nicht pedantisch. Wer jeden Kaffee einordnen will, hört bald auf. Es reicht, die großen Posten einmal zuzuordnen.",
            ]],
            ["umsetzen", "Die Regel im Alltag umsetzen", [
                {"steps": [
                    "**Fixkosten zusammenrechnen** – die [Fixkosten-Liste](/anleitungen/fixkosten-liste/) hilft. Das ist der größte Teil deines Bedarfs.",
                    "**Sparrate per Dauerauftrag** am Tag nach dem Gehaltseingang aufs Sparkonto.",
                    "**Den Rest als Monatsbudget nehmen** für Lebensmittel und Wünsche zusammen – das sind die Ausgaben, die du im Alltag steuerst.",
                    "**Am Monatsende prüfen**, ob es gereicht hat. Was übrig ist, darf auch noch aufs Sparkonto: [Geld übrig am Monatsende](/anleitungen/rest-am-monatsende/).",
                ]},
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Die App teilt nicht in Prozent-Töpfe, sie rechnet einfacher: Einkommen minus Fixkosten ist dein Monatsbudget. Trägst du die Sparrate als festen Posten bei den Fixkosten ein – die Einrichtung fragt eigens nach dem Sparkonto –, ist sie in jedem Monat vom ersten Tag an aus dem verfügbaren Geld heraus. Genau die Reihenfolge, die die Regel will. Legst du den Posten später an, zählt er ab dem nächsten Zeitraum.",
                "Was bleibt, zeigt die große Zahl auf dem Startbildschirm, und jede Ausgabe zieht sie sofort ab.",
            ],
        },
        "faq": [
            ["Bezieht sich die 50/30/20-Regel auf Brutto oder Netto?",
             ["Auf das Netto, also das, was tatsächlich auf deinem Konto ankommt. Steuern und Sozialabgaben sind darin schon abgezogen."]],
            ["Gehört die Altersvorsorge zu den 20 %?",
             ["Private Vorsorge, die du selbst bezahlst, ja. Was der Arbeitgeber direkt vom Lohn abzieht, ist im Netto schon nicht mehr enthalten und zählt nicht noch einmal."]],
            ["Was, wenn ich nichts sparen kann?",
             ["Dann fang mit einem kleinen festen Betrag an, etwa 20 oder 30 € im Monat, und erhöh ihn, wenn eine Fixkostenposition wegfällt. Wie das gehen kann: [Sparen mit wenig Einkommen](/anleitungen/sparen-mit-wenig-einkommen/)."]],
        ],
    },

    # ------------------------------------------------------------ Lebensmittel
    {
        "id": "groceries",
        "slug": "wie-viel-geld-fuer-lebensmittel",
        "title": "Wie viel Geld für Lebensmittel im Monat? So findest du deinen Betrag",
        "desc": "Wie viel Geld für Lebensmittel pro Monat? Durchschnitt für 1 bis 4 Personen – und wie du in vier Wochen deinen eigenen Betrag ermittelst und senkst.",
        "h1": "Wie viel Geld für Lebensmittel im Monat?",
        "teaser": "Durchschnitt für 1 bis 4 Personen – und dein eigener Betrag in vier Wochen.",
        "answer": "**Im Schnitt geben Haushalte in Deutschland 270 € (eine Person) bis 759 € (vier Personen) im Monat für Nahrungsmittel und Getränke aus.** Dein passender Betrag ist der, den du in vier normalen Wochen tatsächlich ausgibst – minus das, was du ohne Verzicht einsparen kannst. Schreib vier Wochen lang jeden Lebensmitteleinkauf auf, teile die Summe durch vier und rechne mal 4,35 auf den Monat hoch. Bei 202 € in vier Wochen sind das rund 220 € im Monat.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "categories", "envelope"],
        "sections": [
            ["warum-nicht-durchschnitt", "Was Haushalte im Schnitt ausgeben – und warum das wenig über dich sagt", [
                {"table": [
                    ["Haushalt", "pro Monat"],
                    ["1 Person", "270 €"],
                    ["2 Personen", "505 €"],
                    ["3 Personen", "653 €"],
                    ["4 Personen", "759 €"],
                ]},
                "Nahrungsmittel, Getränke und Tabakwaren, Durchschnitt 2024 laut [Statistischem Bundesamt, Laufende Wirtschaftsrechnungen](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Einkommen-Konsum-Lebensbedingungen/Konsumausgaben-Lebenshaltungskosten/Tabellen/privater-konsum-haushaltsgroesse-lwr.html).",
                "Tabellen mit Beträgen pro Person sind beliebt, aber sie mischen Großstadt und Land, Discounter und Bioladen, Kantine und Selbstkocher. Ob dein Betrag „zu hoch“ ist, sagt dir kein Durchschnitt – nur der Vergleich mit dir selbst vor und nach einer Änderung.",
                "Deshalb zuerst messen, dann entscheiden.",
            ]],
            ["vier-wochen", "Den eigenen Betrag in vier Wochen ermitteln", [
                {"steps": [
                    "**Vier normale Wochen wählen** – ohne Urlaub, Feiertage oder Geburtstagsfeier.",
                    "**Jeden Einkauf aufschreiben**, auch den Bäcker und die Tankstelle, wenn dort Lebensmittel gekauft werden.",
                    "**Wochensumme bilden** und daraus den Durchschnitt.",
                    "**Auf den Monat hochrechnen:** Wochendurchschnitt × 4,35 (ein Monat hat im Schnitt etwa 4,35 Wochen).",
                ]},
                {"calc": [["Woche 1", "54,20 €"], ["Woche 2", "38,90 €"], ["Woche 3", "61,30 €"], ["Woche 4", "47,60 €"],
                          ["Summe vier Wochen", "202,00 €"], ["÷ 4 = pro Woche", "50,50 €"], ["**× 4,35 = pro Monat**", "219,68 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen, ein Haushalt"},
            ]],
            ["wochenbudget", "Ein Wochenbudget statt eines Monatsbetrags", [
                "Für Lebensmittel funktioniert eine Woche besser als ein Monat: Wer am 20. merkt, dass das Monatsgeld weg ist, kann kaum noch gegensteuern. Wer am Donnerstag merkt, dass die Woche knapp wird, schon.",
                "Setz das Wochenbudget knapp unter deinen gemessenen Wert – im Beispiel 48 statt 50,50 €. Kleine Senkungen hält man durch, große nicht.",
            ]],
            ["senken", "Fünf Hebel, die ohne Verzicht wirken", [
                {"list": [
                    "**Einkaufsliste nach Wochenplan.** Wer weiß, was er kocht, kauft weniger doppelt und wirft weniger weg.",
                    "**Seltener einkaufen.** Jeder zusätzliche Gang in den Laden bringt Spontankäufe mit.",
                    "**Eigenmarken probieren**, Produkt für Produkt. Was nicht schmeckt, kauft man wieder als Marke.",
                    "**Reste einplanen**, zum Beispiel ein fester Restetag pro Woche.",
                    "**Unterwegs-Essen trennen.** Coffee-to-go und Mittagssnack sind oft der größte Posten, laufen aber nicht unter „Einkauf“ – getrennt aufschreiben.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Für die vier Messwochen reicht der Betrag und die Kategorie **Lebensmittel**. Tippst du eine Bezeichnung wie „Aldi“ oder „Wocheneinkauf“, schlägt die App die Kategorie selbst vor. Kassenzettel hältst du vor die Kamera, statt sie abzutippen.",
                "Wie viel du insgesamt pro Tag ausgibst, steht in der Auswertung unter **Pro Tag im Schnitt**. Eine Summe je Kategorie oder Woche rechnet die App nicht aus. Für die vier Messwochen zählst du die Lebensmittel-Einträge im Verlauf selbst zusammen.",
            ],
            "shot": "de-kassenzettel.webp",
            "alt": "Einfaches Haushaltsbuch: Die Kamera liest einen Kassenzettel, die Summenzeile ist markiert.",
        },
        "faq": [
            ["Zählen Drogerieartikel zu den Lebensmitteln?",
             ["Besser nicht. Waschmittel, Duschgel und Klopapier sind oft ein überraschend großer Teil des Einkaufs. Getrennt aufgeschrieben siehst du, was wirklich fürs Essen draufgeht."]],
            ["Wie rechne ich für mehrere Personen?",
             ["Genauso: vier Wochen alles aufschreiben, was der Haushalt an Lebensmitteln kauft. Ein Betrag „pro Person“ ist nur nötig, wenn ihr euch die Kosten teilen wollt."]],
            ["Warum mal 4,35 und nicht mal 4?",
             ["Weil ein Monat mehr als vier Wochen hat: 365 Tage geteilt durch 12 Monate und 7 Tage ergibt etwa 4,35. Mit mal 4 fehlen dir am Monatsende zwei bis drei Tage Einkauf."]],
        ],
    },

    # ------------------------------------------------------------ Umschlagmethode
    {
        "id": "envelope",
        "slug": "umschlagmethode-digital",
        "title": "Umschlagmethode: so funktioniert sie – auch digital ohne Bargeld",
        "desc": "Umschlagmethode (Cash Stuffing): Monatsgeld auf Umschläge für Lebensmittel, Freizeit und Co. verteilen – mit Bargeld, Unterkonten oder vereinfacht am Handy.",
        "h1": "Umschlagmethode: mit Bargeld, mit Konten oder digital",
        "teaser": "Monatsgeld in Umschläge verteilen – und was davon ohne Bargeld übrig bleibt.",
        "answer": "**Bei der Umschlagmethode verteilst du dein frei verfügbares Geld am Monatsanfang auf Umschläge – einen pro Ausgabenbereich.** Ist ein Umschlag leer, ist für diesen Bereich Schluss bis zum nächsten Monat. Ohne Bargeld geht das mit Unterkonten oder in vereinfachter Form: ein einziger digitaler „Umschlag“, der zeigt, was diesen Monat noch da ist.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "categories", "nospend"],
        "sections": [
            ["prinzip", "Das Prinzip in drei Schritten", [
                {"steps": [
                    "**Frei verfügbares Geld bestimmen:** Einkommen minus Fixkosten minus Sparrate. Wie das geht: [Tagesbudget berechnen](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/).",
                    "**Auf Umschläge verteilen** – für jeden Bereich, in dem du im Alltag Geld ausgibst.",
                    "**Nur aus dem passenden Umschlag bezahlen.** Leer ist leer. Umschichten ist erlaubt, aber bewusst.",
                ]},
                {"calc": [["Lebensmittel", "320,00 €"], ["Mobilität", "100,00 €"], ["Freizeit", "120,00 €"], ["Kleidung", "60,00 €"],
                          ["Drogerie", "40,00 €"], ["Geschenke", "40,00 €"], ["Puffer", "120,00 €"], ["**Frei verfügbar gesamt**", "800,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Der **Puffer** ist der wichtigste Umschlag. Ohne ihn bricht das System beim ersten kaputten Fahrradschlauch zusammen.",
            ]],
            ["varianten", "Bargeld, Unterkonten oder digital?", [
                {"table": [
                    ["Variante", "Gut daran", "Der Haken"],
                    ["Bargeld in echten Umschlägen", "sehr greifbar – man sieht das Geld schwinden", "online und mit Karte kaum nutzbar, Bargeld zu Hause"],
                    ["Unterkonten bei der Bank", "funktioniert mit Karte und online", "Umbuchen zwischen Konten, nicht jede Bank bietet genug Unterkonten"],
                    ["Ein digitaler Umschlag", "eine Zahl, kein Sortieren", "keine getrennten Grenzen je Bereich"],
                ]},
                "In sozialen Medien heißt die Bargeld-Variante „Cash Stuffing“. Viele starten mit sechs Umschlägen und landen nach ein paar Monaten bei zwei oder drei: einer für Lebensmittel, einer für alles andere – oder sogar nur einem.",
            ]],
            ["ein-umschlag", "Die vereinfachte Form: ein Umschlag", [
                "Wenn das Sortieren der Grund ist, warum du aufhörst, reicht ein einziger Umschlag für alle Alltagsausgaben. Die Grenze ist dann nicht „Freizeit leer“, sondern „Monat leer“.",
                "Damit das funktioniert, brauchst du ein Tempo-Gefühl: Bist du schneller unterwegs, als der Monat vergeht? Die Tempo-Probe dazu steht in [Wie viel darf ich pro Tag ausgeben?](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/)",
            ]],
            ["fehler", "Typische Fehler", [
                {"list": [
                    "**Zu knapp geplant.** Umschläge auf Kante führen nach zwei Wochen zum Umschichten – und dann zum Aufgeben.",
                    "**Jährliche Kosten vergessen.** Versicherungen gehören nicht in den Alltagsumschlag: [jährliche Kosten einplanen](/anleitungen/jaehrliche-kosten-im-budget/).",
                    "**Kartenzahlungen nicht mitgezählt.** Wer bar und mit Karte zahlt, muss beides aus demselben Umschlag rechnen.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Das Einfache Haushaltsbuch als ein Umschlag",
            "body": [
                "Getrennte Umschläge je Kategorie gibt es in der App nicht. Sie arbeitet wie die vereinfachte Form: Die große Zahl **Verfügbar** ist dein einziger Umschlag – Einkommen minus Fixkosten, abzüglich jeder gespeicherten Ausgabe.",
                "Der Balken darunter zeigt das Tempo: Die Füllung ist das Ausgegebene, der Strich, wie weit der Monat ist. Ohne Bargeld, ohne Umbuchen.",
            ],
            "shot": "de-start.webp",
            "alt": "Einfaches Haushaltsbuch: Startbildschirm mit Verfügbar 1.222,65 € und Balken mit Zeitstrich.",
        },
        "faq": [
            ["Was passiert mit dem Rest im Umschlag am Monatsende?",
             ["Das entscheidest du vorher: in den nächsten Monat mitnehmen, aufs Sparkonto legen oder für etwas Bestimmtes sammeln. Mehr dazu: [Geld übrig am Monatsende](/anleitungen/rest-am-monatsende/)."]],
            ["Wie viele Umschläge sind sinnvoll?",
             ["So wenige wie möglich. Drei bis sechs ist für den Anfang ein guter Rahmen, ein Puffer gehört immer dazu."]],
            ["Darf ich zwischen Umschlägen umschichten?",
             ["Ja, aber bewusst und nicht still: Wer aus „Kleidung“ in „Lebensmittel“ schiebt, weiß danach, dass bei Kleidung weniger übrig ist."]],
        ],
    },

    # ------------------------------------------------------------ Kakeibo
    {
        "id": "kakeibo",
        "slug": "kakeibo-methode",
        "title": "Kakeibo-Methode: das japanische Haushaltsbuch einfach erklärt",
        "desc": "Kakeibo ist ein japanisches Haushaltsbuch mit vier Fragen und vier Kategorien. So funktioniert die Methode, mit Beispiel-Monat und Tipps für den Alltag.",
        "h1": "Kakeibo: das japanische Haushaltsbuch in vier Fragen",
        "teaser": "Vier Fragen, vier Kategorien, ein Rückblick am Monatsende.",
        "answer": "**Kakeibo ist ein japanisches Haushaltsbuch, das mit vier Fragen arbeitet: Wie viel Geld habe ich? Wie viel will ich sparen? Wie viel gebe ich aus? Was kann ich besser machen?** Ausgaben landen in vier Kategorien – Grundbedarf, Wünsche, Kultur, Unerwartetes. Der Kern ist der ehrliche Rückblick am Monatsende, nicht die Tabelle.",
        "updated": U, "updated_label": UL,
        "related": ["simple", "categories", "habit"],
        "sections": [
            ["herkunft", "Woher Kakeibo kommt", [
                "„Kakeibo“ heißt auf Japanisch schlicht Haushaltsbuch. Das gedruckte Haushaltsbuch geht auf die Journalistin Hani Motoko zurück, die 1904 in ihrer Frauenzeitschrift ein Haushaltsbuch herausgab. Die vier Fragen und vier Kategorien, wie man sie außerhalb Japans kennt, hat vor allem Fumiko Chibas Buch *Kakeibo: The Japanese Art of Saving Money* (2017) bekannt gemacht. Viele führen es bis heute von Hand, oft in einem eigenen Heft.",
            ]],
            ["vier-fragen", "Die vier Fragen", [
                {"steps": [
                    "**Wie viel Geld habe ich?** Am Monatsanfang: Einkommen minus Fixkosten.",
                    "**Wie viel möchte ich sparen?** Ein Betrag, bevor das erste Geld ausgegeben ist.",
                    "**Wie viel gebe ich aus?** Jede Ausgabe im Lauf des Monats, mit einer der vier Kategorien.",
                    "**Wie kann ich mich verbessern?** Am Monatsende: Was hat sich gelohnt, was nicht?",
                ]},
                {"calc": [["Netto-Einkommen", "2.050,00 €"], ["− Fixkosten", "1.130,00 €"], ["− Sparziel", "150,00 €"], ["**Für den Monat**", "770,00 €"]],
                 "caption": "Frage 1 und 2 als Rechnung, erfundene Zahlen"},
            ]],
            ["kategorien", "Die vier Kategorien", [
                {"table": [
                    ["Kategorie", "Beispiele"],
                    ["Grundbedarf", "Lebensmittel, Drogerie, Fahrkarte, Medikamente"],
                    ["Wünsche", "Essen gehen, Kleidung, Hobby"],
                    ["Kultur", "Bücher, Kino, Konzert, Museum, Kurse"],
                    ["Unerwartetes", "Reparaturen, Arztkosten, kaputte Waschmaschine, Geschenke für spontane Anlässe"],
                ]},
                "Die Kategorien sind bewusst grob. Es geht nicht um die Frage, wohin jeder Euro ging, sondern ob das Geld zu dem passt, was dir wichtig ist.",
            ]],
            ["rueckblick", "Der Monatsrückblick – das eigentliche Kakeibo", [
                "Am Monatsende nimmst du dir zehn Minuten und beantwortest schriftlich:",
                {"list": [
                    "Habe ich mein Sparziel erreicht? Wenn nicht: woran lag es?",
                    "Welche Ausgabe hat sich gelohnt – welche würde ich nicht noch einmal machen?",
                    "Was nehme ich mir für den nächsten Monat konkret vor? Eine Sache, nicht fünf.",
                ]},
                "Der Rückblick wirkt, weil er langsam ist. Wer nur Zahlen sammelt, ohne sie anzusehen, führt eine Liste, kein Kakeibo.",
            ]],
        ],
        "app": {
            "h2": "Kakeibo mit dem Einfachen Haushaltsbuch",
            "body": [
                "Frage 1 und 2 beantwortet die Einrichtung: Einkommen und Fixkosten eintragen, die Sparrate als festen Posten dazu. Frage 3 ist jede gespeicherte Ausgabe. Die vier Kakeibo-Kategorien kannst du als eigene Kategorien anlegen, wenn dir die Vorgaben zu fein sind. Eine Summe je Kategorie rechnet die App nicht aus – die vier Kakeibo-Summen zählst du am Monatsende im Verlauf selbst zusammen.",
                "Für Frage 4 zeigt die Auswertung den Monat in drei Zahlen: ausgegeben, übrig, pro Tag im Schnitt. Den Rückblick selbst schreibst du am besten weiter von Hand.",
            ],
        },
        "faq": [
            ["Brauche ich ein spezielles Kakeibo-Buch?",
             ["Nein. Ein Heft mit einer Seite pro Monat reicht. Gedruckte Kakeibo-Bücher geben nur die Fragen und Spalten vor."]],
            ["Ist Kakeibo dasselbe wie ein normales Haushaltsbuch?",
             ["Die Zahlen sind dieselben. Der Unterschied liegt im Rückblick: Kakeibo fragt jeden Monat ausdrücklich, ob die Ausgaben zu deinen Zielen gepasst haben."]],
            ["Wohin gehören Fixkosten?",
             ["Sie stehen nicht in den vier Kategorien. Du ziehst sie am Monatsanfang ab, bevor du planst."]],
        ],
    },

    # ------------------------------------------------------------ Notgroschen
    {
        "id": "emergency",
        "slug": "notgroschen-wie-hoch",
        "title": "Notgroschen: wie hoch er sein sollte und wie du ihn aufbaust",
        "desc": "Wie hoch sollte der Notgroschen sein? Faustregel drei bis sechs Monatsausgaben – mit Rechnung aus deinen Fixkosten, Sparplan und wo das Geld liegen sollte.",
        "h1": "Notgroschen: wie hoch, wie aufbauen, wo parken?",
        "teaser": "Die Höhe aus deinen eigenen Ausgaben berechnen und Schritt für Schritt ansparen.",
        "answer": "**Die Verbraucherzentrale nennt als Faustregel zwei bis drei Monatsgehälter; wer mit den Ausgaben rechnet, landet meist bei drei bis sechs Monatsausgaben.** Rechne dafür deine Fixkosten plus das Nötigste für den Alltag zusammen – bei 1.150 € Fixkosten und 450 € Lebensnotwendigem sind das 1.600 € im Monat, also 4.800 bis 9.600 €. Parke das Geld getrennt vom Girokonto, aber jederzeit verfügbar, zum Beispiel auf einem Tagesgeldkonto.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "yearly", "lowincome"],
        "sections": [
            ["wofuer", "Wofür der Notgroschen da ist", [
                "Der Notgroschen ist kein Urlaubsgeld und keine Rücklage für die Versicherung im März. Er ist für das, was man nicht planen kann: Waschmaschine kaputt, Autoreparatur, Jobverlust, eine Nachzahlung. Ohne ihn landet so etwas im Dispo – und der kostet Zinsen.",
                {"note": "Planbare Kosten wie Jahresversicherungen gehören in eine eigene Rücklage: [Jährliche Kosten im Monatsbudget](/anleitungen/jaehrliche-kosten-im-budget/)."},
            ]],
            ["hoehe", "Die Höhe aus deinen eigenen Zahlen", [
                {"steps": [
                    "**Fixkosten zusammenrechnen** – Miete, Strom, Versicherungen, Verträge. Die [Fixkosten-Liste](/anleitungen/fixkosten-liste/) hilft.",
                    "**Das Nötigste für den Alltag dazu:** Lebensmittel, Drogerie, Fahrtkosten. Nicht das, was du ausgibst, sondern was du im Notfall bräuchtest.",
                    "**Mal drei bis sechs.** Je unsicherer dein Einkommen, desto näher an sechs.",
                ]},
                {"calc": [["Fixkosten im Monat", "1.150,00 €"], ["+ Lebensnotwendiges", "450,00 €"], ["= Monatsbedarf", "1.600,00 €"],
                          ["× 3 Monate", "4.800,00 €"], ["**× 6 Monate**", "9.600,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Die [Verbraucherzentrale](https://www.verbraucherzentrale.de/laura-zieht-aus/sparen) rechnet mit zwei bis drei Netto-Monatsgehältern – die einfachere Faustregel, wenn du deine Ausgaben noch nicht kennst. Wer selbstständig ist, Kinder hat oder allein von einem Einkommen lebt, liegt eher am oberen Ende. Wer in einer sicheren Anstellung mit zwei Einkommen lebt, eher am unteren.",
            ]],
            ["aufbauen", "In Etappen aufbauen", [
                "Ein Ziel von 4.800 € wirkt bei kleinem Budget unerreichbar. Teil es auf:",
                {"table": [
                    ["Etappe", "Betrag", "bei 100 € im Monat", "bei 200 € im Monat"],
                    ["Starthilfe", "1.000 €", "10 Monate", "5 Monate"],
                    ["Ein Monatsbedarf", "1.600 €", "16 Monate", "8 Monate"],
                    ["Drei Monatsbedarfe", "4.800 €", "48 Monate", "24 Monate"],
                ]},
                "Schneller geht es mit Einmalbeträgen: Steuererstattung, Weihnachtsgeld, Rest am Monatsende. Wer den Rest konsequent auf den Notgroschen legt, ist oft deutlich früher am Ziel.",
            ]],
            ["wo", "Wo der Notgroschen liegen sollte", [
                {"list": [
                    "**Getrennt vom Girokonto**, damit er nicht wie normales Geld aussieht.",
                    "**Jederzeit verfügbar**, ohne Kündigungsfrist und ohne Kursrisiko – etwa auf einem Tagesgeldkonto.",
                    "**Nicht in Aktien oder Fonds.** Der Notfall kommt nicht dann, wenn die Kurse gut stehen.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Den Monatsbedarf aus dem Einfachen Haushaltsbuch ablesen",
            "body": [
                "Die Auswertung zeigt unter **Zusammensetzung**, wie hoch Einnahmen und Fixkosten sind. Die Fixkosten sind der größte Teil deines Monatsbedarfs – eine eingetragene Sparrate ziehst du davon ab, sie ist kein Bedarf. Für den Alltag ist **Pro Tag** mal 30 die Obergrenze; im Notfall kämst du mit weniger aus.",
                "Die Sparrate für den Notgroschen trägst du als festen Posten bei den Fixkosten ein; legst du ihn nachträglich an, zählt er ab dem nächsten Zeitraum.",
            ],
            "shot": "de-auswertung.webp",
            "alt": "Einfaches Haushaltsbuch: Auswertung mit Ausgegeben, Übrig, Pro Tag und der Zusammensetzung aus Einnahmen und Fixkosten.",
        },
        "faq": [
            ["Zählt der Dispo als Notgroschen?",
             ["Nein. Der Dispo ist ein teurer Kredit. Ein Notgroschen soll gerade verhindern, dass du ihn brauchst."]],
            ["Soll ich erst Schulden tilgen oder erst den Notgroschen aufbauen?",
             ["Ein kleiner Notgroschen, etwa 1.000 €, kommt meist zuerst – sonst führt die nächste Reparatur zu neuen Schulden. Danach lohnt es sich, teure Schulden wie den Dispo schneller abzubauen."]],
            ["Was mache ich, wenn ich den Notgroschen gebraucht habe?",
             ["Wieder auffüllen, bevor du für andere Ziele sparst. Dafür die bisherige Sparrate weiterlaufen lassen."]],
        ],
    },

    # ------------------------------------------------------------ wenig Einkommen
    {
        "id": "lowincome",
        "slug": "sparen-mit-wenig-einkommen",
        "title": "Sparen mit wenig Einkommen: 7 Schritte, die auch bei knappem Geld gehen",
        "desc": "Sparen mit wenig Geld: wie du mit kleinen Beträgen anfängst, Fixkosten prüfst, Ansprüche checkst und Lecks findest – mit Rechenbeispiel für 1.450 € netto.",
        "h1": "Sparen mit wenig Einkommen: so geht es trotzdem",
        "teaser": "Kleine feste Beträge, Fixkosten-Check und die Ausgaben, die man nicht bemerkt.",
        "answer": "**Mit wenig Einkommen sparst du nicht mit Prozenten, sondern mit einem kleinen festen Betrag, der automatisch abgeht** – etwa 30 € per Dauerauftrag am Tag nach dem Gehalt. Das Geld dafür kommt selten vom Verzicht im Alltag, sondern aus Fixkosten, die zu hoch sind, und aus kleinen Ausgaben, die man nicht bemerkt.",
        "updated": U, "updated_label": UL,
        "related": ["rule503020", "subscriptions", "emergency"],
        "sections": [
            ["ausgangslage", "Die Ausgangslage ehrlich aufschreiben", [
                {"calc": [["Netto-Einkommen", "1.450,00 €"], ["− Fixkosten", "1.020,00 €"], ["= frei für den Monat", "430,00 €"], ["÷ 30 Tage", ""], ["**pro Tag**", "14,33 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Mit gut 14 € am Tag für Essen, Drogerie und alles andere ist die 50/30/20-Regel unrealistisch. Das ist kein Versagen, sondern Rechnung. Deshalb anders vorgehen:",
            ]],
            ["schritte", "Sieben Schritte", [
                {"steps": [
                    "**Mit einem festen Mini-Betrag anfangen.** 20 oder 30 € im Monat per Dauerauftrag. 30 € sind 360 € im Jahr – genug für eine kaputte Brille oder eine Nebenkostennachzahlung.",
                    "**Fixkosten prüfen, nicht den Kaffee.** Handytarif, Strom, Versicherungen, Abos: Ein Wechsel spart einmal Arbeit und dann jeden Monat Geld. Wie du Abos findest: [Abos finden und kündigen](/anleitungen/abos-finden-und-kuendigen/).",
                    "**Ansprüche prüfen.** Wohngeld, Kinderzuschlag oder ein Sozialticket im Nahverkehr werden oft nicht beantragt, obwohl ein Anspruch besteht. Wer Sozialleistungen wie Bürgergeld bzw. Grundsicherung oder BAföG bekommt, kann sich auf Antrag vom Rundfunkbeitrag befreien lassen. Eine Schuldner- oder Sozialberatung hilft kostenlos beim Prüfen.",
                    "**Vier Wochen alles aufschreiben.** Bei knappem Geld sind die kleinen Beträge – Automat, Bäcker, Lieferdienst – oft der Unterschied zwischen plus und minus.",
                    "**Ein Wochenbudget für Lebensmittel** statt Monatsbudget: [Wie viel Geld für Lebensmittel?](/anleitungen/wie-viel-geld-fuer-lebensmittel/)",
                    "**Einmalbeträge sofort parken.** Steuererstattung, Bonus, Nebenkosten-Guthaben, Geldgeschenk: Was nicht im Alltag verplant ist, geht direkt aufs Sparkonto.",
                    "**Erst Notgroschen, dann alles andere.** Ein kleiner Puffer verhindert, dass die nächste Reparatur im Dispo landet: [Notgroschen](/anleitungen/notgroschen-wie-hoch/).",
                ]},
            ]],
            ["lecks", "Wo das Geld unbemerkt verschwindet", [
                {"table": [
                    ["Kleine Ausgabe", "pro Woche", "pro Jahr (× 52)"],
                    ["Coffee to go, 3 × 2,80 €", "8,40 €", "436,80 €"],
                    ["Snack am Automaten, 4 × 1,50 €", "6,00 €", "312,00 €"],
                    ["Lieferdienst, 1 × 18,00 €", "18,00 €", "936,00 €"],
                ]},
                "Es geht nicht darum, das alles zu streichen. Aber wer es sieht, entscheidet anders – manchmal reicht es, eine der drei Gewohnheiten zu halbieren.",
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Die App kostet nichts; frühestens ab dem fünften Tag zeigt sie einen Werbebanner, den ein einmaliger Kauf entfernt. Sie braucht kein Konto und keine Bankverbindung. Die Sparrate gehört zu den Fixkosten (nachträglich angelegt ab dem nächsten Zeitraum); dann zeigt die große Zahl auf dem Startbildschirm nur das Geld, das du wirklich ausgeben kannst.",
                "Kleine Beträge sind schnell erfasst: Betrag eintippen, Speichern antippen. Am Monatsende kannst du in der Auswertung deinen Kontostand eintragen; ab dem zweiten Mal zeigt die App, ob Ausgaben fehlen.",
            ],
        },
        "faq": [
            ["Lohnt sich Sparen bei 20 € im Monat überhaupt?",
             ["Ja. Es geht weniger um die Zinsen als darum, dass eine kaputte Brille oder eine Nachzahlung nicht im Dispo landet. 20 € im Monat sind nach einem Jahr 240 €."]],
            ["Was mache ich, wenn am Monatsende immer etwas fehlt?",
             ["Erst die Fixkosten prüfen, dann vier Wochen jede Ausgabe aufschreiben. Wenn die Rechnung trotzdem nicht aufgeht, ist eine kostenlose Schuldner- oder Budgetberatung der richtige nächste Schritt."]],
            ["Soll ich Geld in bar abheben, um weniger auszugeben?",
             ["Manchen hilft es, weil sie das Geld schwinden sehen. Wichtig ist nur, dass auch Barausgaben aufgeschrieben werden – sonst fehlen sie am Monatsende."]],
        ],
    },

    # ------------------------------------------------------------ No-Spend
    {
        "id": "nospend",
        "slug": "no-spend-challenge",
        "title": "No-Spend-Challenge: Regeln, Varianten und wie du sie durchhältst",
        "desc": "No-Spend-Challenge: ein Tag, eine Woche oder ein Monat ohne unnötige Ausgaben. Regeln festlegen, Ausnahmen klären, Ergebnis messen – mit Beispielrechnung.",
        "h1": "No-Spend-Challenge: Regeln, Varianten, Ergebnis",
        "teaser": "Tage ohne Ausgaben sammeln – mit klaren Regeln statt schlechtem Gewissen.",
        "answer": "**Bei einer No-Spend-Challenge gibst du für eine bestimmte Zeit kein Geld für Nicht-Notwendiges aus.** Fixkosten laufen weiter, und meist sind auch Lebensmittel nach Einkaufsliste erlaubt. Entscheidend sind Regeln, die du vorher aufschreibst – und eine Zahl am Ende, die zeigt, was es gebracht hat.",
        "updated": U, "updated_label": UL,
        "related": ["impulse", "envelope", "habit"],
        "sections": [
            ["varianten", "Drei Varianten", [
                {"table": [
                    ["Variante", "Für wen", "Typisches Ziel"],
                    ["No-Spend-Tage", "Einstieg", "z. B. 10 Tage im Monat ohne jede Ausgabe"],
                    ["No-Spend-Woche", "nach einem teuren Monat", "eine Woche nur Lebensmittel nach Liste"],
                    ["No-Spend-Monat", "Fortgeschrittene", "ein Monat ohne Kleidung, Essen gehen, Online-Shopping"],
                ]},
                "Für den Anfang sind No-Spend-Tage am leichtesten. Ein voller Monat ohne Ausnahmen scheitert oft an der ersten Geburtstagseinladung.",
            ]],
            ["regeln", "Die Regeln vorher aufschreiben", [
                {"list": [
                    "**Was weiterläuft:** Miete, Strom, Versicherungen, Abos – alles, was ohnehin abgebucht wird.",
                    "**Was erlaubt ist:** Lebensmittel nach Liste? Tanken für den Arbeitsweg? Medikamente?",
                    "**Was nicht erlaubt ist:** Essen gehen, Lieferdienst, Kleidung, Online-Shopping, Coffee to go.",
                    "**Was bei Ausnahmen passiert:** Ein Geschenk für eine Feier ist kein Scheitern, wenn die Regel es vorsieht.",
                ]},
                "Ohne geschriebene Regeln wird jede Ausnahme zur Verhandlung mit dir selbst – und die verliert man meistens.",
            ]],
            ["messen", "Das Ergebnis messen", [
                "Vergleiche die Ausgaben ohne Fixkosten mit einem normalen Monat:",
                {"calc": [["Ausgaben im Vormonat", "860,00 €"], ["Ausgaben im No-Spend-Monat", "610,00 €"], ["**Unterschied**", "250,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Leg den Unterschied sofort zur Seite – aufs Sparkonto oder auf den Notgroschen. Sonst verschwindet er im nächsten Monat.",
            ]],
            ["vorbereitung", "Vorbereitung in der Woche davor", [
                {"list": [
                    "**Vorräte sichten und einen Essensplan machen**, damit die erste Woche nicht an einem leeren Kühlschrank scheitert.",
                    "**Termine ansehen:** Geburtstage, Feiern, Ausflüge – und gleich in die Regeln schreiben, was dafür erlaubt ist.",
                    "**Shopping-Apps und Newsletter stummschalten**, bevor es losgeht.",
                    "**Je Gewohnheit eine kostenlose Alternative notieren:** Kaffee von zu Hause mitnehmen, Bibliothek statt Buchladen, Spaziergang statt Café.",
                ]},
            ]],
            ["danach", "Nach der Challenge", [
                "Der Wert liegt weniger im gesparten Betrag als in dem, was du gemerkt hast: Was hat wirklich gefehlt, was gar nicht? Was nicht gefehlt hat, kann dauerhaft weg. Was gefehlt hat, darf wieder ins Budget – bewusst.",
            ]],
        ],
        "app": {
            "h2": "No-Spend-Tage im Einfachen Haushaltsbuch sehen",
            "body": [
                "Die Auswertung zeigt ein Diagramm nach Tagen. Tage ohne Ausgabe erscheinen darin nur als blasser Punkt statt eines Balkens – so siehst du deine No-Spend-Tage auf einen Blick, ohne extra Strichliste. Mit dem Pfeil oben in der Auswertung blätterst du zum vorigen Zeitraum und vergleichst **Ausgegeben**.",
                "Der Balken auf dem Startbildschirm zeigt, wie viel vom Monatsgeld ausgegeben ist und wie weit der Monat ist. In einem No-Spend-Monat bleibt die Füllung deutlich hinter dem Strich.",
            ],
            "shot": "de-auswertung.webp",
            "alt": "Einfaches Haushaltsbuch: Auswertung mit Tagesdiagramm, in dem Tage ohne Ausgaben als blasser Punkt erscheinen.",
        },
        "faq": [
            ["Zählen Lebensmittel als Ausgabe?",
             ["Das legst du selbst fest. Die meisten erlauben Lebensmittel nach Einkaufsliste und schließen Spontankäufe und Essen gehen aus."]],
            ["Was, wenn ich die Challenge breche?",
             ["Aufschreiben, warum, und weitermachen. Eine Ausnahme beendet die Challenge nicht – sie zeigt dir nur, wo die Regel zu streng oder zu unklar war."]],
            ["Wie oft sollte man eine No-Spend-Challenge machen?",
             ["Als Daueranstrengung hält das kaum jemand durch. Ein No-Spend-Monat im Jahr oder ein paar feste No-Spend-Tage pro Monat funktionieren für viele besser."]],
        ],
    },

    # ------------------------------------------------------------ Kategorien
    {
        "id": "categories",
        "slug": "haushaltsbuch-kategorien",
        "title": "Haushaltsbuch-Kategorien: welche sinnvoll sind – und wie viele",
        "desc": "Sinnvolle Kategorien fürs Haushaltsbuch: eine Liste mit Beispielen, wie viele du brauchst, was zu Fixkosten gehört und warum weniger Kategorien länger durchhalten.",
        "h1": "Haushaltsbuch-Kategorien: welche, wie viele, wofür",
        "teaser": "Eine schlanke Kategorienliste mit Beispielen – und wann man ganz ohne auskommt.",
        "answer": "**Für die Alltagsausgaben reichen meist acht bis zwölf Kategorien** – etwa Lebensmittel, Essen gehen, Mobilität, Kleidung, Gesundheit, Pflege, Freizeit und Geschenke. Fixkosten wie Miete und Versicherungen bekommen keine eigene Alltagskategorie, sie werden vorher abgezogen. Wer gerade erst anfängt, kann Kategorien auch ganz weglassen.",
        "updated": U, "updated_label": UL,
        "related": ["simple", "fixed", "envelope"],
        "sections": [
            ["liste", "Eine schlanke Kategorienliste", [
                {"table": [
                    ["Kategorie", "Was hineingehört"],
                    ["Lebensmittel", "Supermarkt, Bäcker, Markt, Getränke für zu Hause"],
                    ["Essen gehen", "Restaurant, Imbiss, Lieferdienst, Kantine"],
                    ["Ausgehen", "Bar, Club, Kino, Konzert"],
                    ["Mobilität", "Tanken, Fahrkarten, Parken, Fahrrad, Taxi"],
                    ["Kleidung & Accessoires", "Kleidung, Schuhe, Taschen, Schmuck"],
                    ["Pflege", "Drogerie, Friseur, Kosmetik"],
                    ["Gesundheit", "Apotheke, Zuzahlungen, Brille"],
                    ["Hobby & Freizeit", "Sport, Bücher, Spiele, Kurse"],
                    ["Wohnen & Einrichtung", "Möbel, Deko, Werkzeug, Haushaltsgeräte"],
                    ["Technik", "Handy, Zubehör, Computer, Apps"],
                    ["Geschenke", "Geburtstage, Hochzeiten, Feiertage"],
                    ["Reisen", "Unterkunft, Anreise, Ausflüge"],
                ]},
                "Passt eine Ausgabe nirgends, ist „Ohne Kategorie“ ehrlicher als ein Sammeltopf „Sonstiges“, der jeden Monat wächst.",
            ]],
            ["wie-viele", "Wie viele Kategorien sind sinnvoll?", [
                "Jede Kategorie ist eine Entscheidung bei jeder Ausgabe. Zwanzig Kategorien heißen zwanzig Möglichkeiten, ins Grübeln zu kommen. Deshalb:",
                {"list": [
                    "**Zum Anfang: keine oder zwei.** Etwa Lebensmittel und Unterwegs, alles andere bleibt ohne Kategorie – oder nur Beträge: [Einfaches Haushaltsbuch führen](/anleitungen/einfaches-haushaltsbuch-fuehren/).",
                    "**Nach einem Monat:** die Bereiche aufteilen, bei denen du wirklich wissen willst, wohin das Geld geht.",
                    "**Selten mehr als zwölf bis fünfzehn** für den Alltag. Wenn du eine Kategorie drei Monate nicht benutzt hast, kann sie weg.",
                ]},
            ]],
            ["fixkosten", "Fixkosten gehören nicht in die Alltagskategorien", [
                "Miete, Strom, Versicherungen und Abos gehen ohnehin jeden Monat ab. Wer sie zwischen die Einkäufe mischt, sieht nicht mehr, was im Alltag passiert. Besser: Fixkosten einmal sammeln und vom Einkommen abziehen – die Liste steht in [Fixkosten-Liste](/anleitungen/fixkosten-liste/).",
            ]],
            ["grauzonen", "Grauzonen eindeutig regeln", [
                {"list": [
                    "**Drogerie im Supermarkt:** auf dem Zettel getrennt oder komplett unter Lebensmittel – Hauptsache, immer gleich.",
                    "**Mittagessen bei der Arbeit:** eigene Kategorie, wenn es regelmäßig ist; es ist oft ein größerer Posten als gedacht.",
                    "**Online-Bestellungen:** nach dem Zweck einsortieren (Kleidung, Technik), nicht nach dem Händler.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Kategorien im Einfachen Haushaltsbuch",
            "body": [
                "Die App bringt eine schlanke Vorgabeliste mit – unter anderem Lebensmittel, Essen gehen, Arbeit Essen, Mobilität, Pflege, Gesundheit, Kleidung & Accessoires, Geschenke und Reisen. Du kannst Kategorien umbenennen, löschen und eigene anlegen. Ein „Sonstiges“ gibt es bewusst nicht, dafür „Ohne Kategorie“.",
                "Die Kategorie ist freiwillig. Tippst du eine Bezeichnung, schlägt die App eine passende Kategorie vor – aus deinen früheren Einträgen und einer eingebauten Wortliste, nur auf dem Gerät. Eine Auswertung nach Kategorien gibt es nicht; die Kategorie steht im Verlauf bei jedem Eintrag.",
            ],
            "shot": "de-verlauf.webp",
            "alt": "Einfaches Haushaltsbuch: Verlauf mit Ausgaben nach Tagen, jeweils mit Bezeichnung und Kategorie.",
        },
        "faq": [
            ["Wohin gehört ein Einkauf mit Lebensmitteln und Kleidung auf einem Zettel?",
             ["Zum größeren Teil. Wer es genau will, trägt zwei Beträge ein; meist lohnt das erst, wenn der kleinere Teil nennenswert ist."]],
            ["Wohin gehört Tanken?",
             ["Zu Mobilität. Kaufst du an der Tankstelle Snacks oder Getränke, gehören die eigentlich zu Lebensmitteln; wer es einfach halten will, bucht den ganzen Zettel unter Mobilität."]],
            ["Soll ich Kategorien nachträglich ändern?",
             ["Ja, wenn eine Kategorie zu groß wird, teil sie für die Zukunft. Alte Einträge musst du nicht umsortieren."]],
        ],
    },

    # ------------------------------------------------------------ Kassenzettel
    {
        "id": "receipts",
        "slug": "kassenzettel-digitalisieren",
        "title": "Kassenzettel digitalisieren: was aufheben, was scannen, was wegwerfen",
        "desc": "Kassenzettel digitalisieren: welche Belege du für Garantie, Umtausch und Steuer aufhebst, warum Thermopapier verblasst und in welchen Müll Bons gehören.",
        "h1": "Kassenzettel digitalisieren, aufheben oder wegwerfen?",
        "teaser": "Welche Bons du brauchst, wie du sie sicherst und in welchen Müll der Rest gehört.",
        "answer": "**Die meisten Kassenzettel kannst du wegwerfen, sobald die Ausgabe notiert ist.** Aufheben solltest du Belege für teure Anschaffungen (Gewährleistung, Garantie, Umtausch) und Rechnungen, die du für die Steuer brauchst. Weil Thermopapier verblasst, lohnt es sich, diese wenigen Belege als Foto oder Scan zu sichern. Der Rest gehört in den Restmüll, nicht ins Altpapier.",
        "updated": U, "updated_label": UL,
        "related": ["categories", "simple", "groceries"],
        "sections": [
            ["aufheben", "Welche Belege du aufheben solltest", [
                {"table": [
                    ["Beleg", "Warum", "Wie lange ungefähr"],
                    ["Elektronik, Möbel, Haushaltsgeräte", "Gewährleistung und Herstellergarantie", "mindestens 2 Jahre, bei längerer Garantie entsprechend länger"],
                    ["Kleidung, Geschenke", "Umtausch", "bis die Umtauschfrist des Händlers abgelaufen ist"],
                    ["Handwerker, haushaltsnahe Dienstleistungen", "Steuerermäßigung, Gewährleistung", "mindestens 2 Jahre – für Rechnungen über Arbeiten an Haus oder Wohnung ist das Pflicht ([§ 14b UStG](https://www.gesetze-im-internet.de/ustg_1980/__14b.html))"],
                    ["Arbeitsmittel, Fachliteratur", "Werbungskosten in der Steuererklärung", "bis der Steuerbescheid bestandskräftig ist"],
                    ["Alltagseinkauf", "keiner, sobald notiert", "–"],
                ]},
                {"note": "Für die Steuerermäßigung bei Handwerkerleistungen verlangt das Finanzamt eine Rechnung und eine Zahlung aufs Konto des Handwerkers – ein Kassenzettel über Barzahlung reicht dafür nicht."},
            ]],
            ["thermopapier", "Warum Kassenzettel verblassen", [
                "Die meisten Bons sind auf Thermopapier gedruckt. Wärme, Licht und Reibung lassen die Schrift mit der Zeit verschwinden – im Portemonnaie oft schon nach wenigen Monaten. Wer einen Beleg in zwei Jahren noch braucht, sollte ihn deshalb zusätzlich als Foto oder Scan sichern.",
            ]],
            ["digitalisieren", "So digitalisierst du die wichtigen Belege", [
                {"steps": [
                    "**Direkt nach dem Kauf fotografieren** – flach hinlegen, gutes Licht, der ganze Zettel im Bild.",
                    "**Sinnvoll benennen:** Datum, Geschäft, Gegenstand, etwa „2026-11-24 Elektromarkt Waschmaschine“.",
                    "**An einem Ort ablegen** – ein Ordner „Belege“ in deinem Cloud- oder Fotospeicher, nach Jahren getrennt.",
                    "**Das Original trotzdem aufheben**, solange die Frist läuft – manche Herstellergarantien verlangen den Originalbeleg.",
                ]},
            ]],
            ["entsorgen", "In welchen Müll Kassenzettel gehören", [
                "Kassenzettel aus Thermopapier gehören in den **Restmüll**, nicht ins Altpapier – die Beschichtung stört das Recycling. Das [Umweltbundesamt](https://www.umweltbundesamt.de/themen/kassenbons-gehoeren-nicht-ins-altpapier) empfiehlt das vorsorglich für alle Thermopapiere, weil sich die Sorten von außen nicht sicher unterscheiden lassen. Nur Belege auf normalem Papier, die sich beim Kratzen mit dem Fingernagel nicht verfärben, dürfen ins Altpapier.",
            ]],
        ],
        "app": {
            "h2": "Kassenzettel im Einfachen Haushaltsbuch",
            "body": [
                "Für das Haushaltsbuch musst du Bons nicht abtippen: Tipp auf das Kamera-Symbol und halte den Kassenzettel ins Bild. Die App liest Summe, Geschäft, Datum und Uhrzeit und füllt sie ein – du tippst nur noch auf Speichern. Die Texterkennung läuft auf dem Telefon.",
                "Wichtig: Die App ist kein Belegarchiv. Das Bild wird weder gespeichert noch irgendwohin geschickt. Belege für Garantie und Steuer sicherst du wie oben beschrieben separat.",
            ],
            "shot": "de-kassenzettel.webp",
            "alt": "Einfaches Haushaltsbuch: Die Kamera liest einen Kassenzettel, die Summenzeile „SUMME EUR 22,42“ ist grün markiert.",
        },
        "faq": [
            ["Muss ich jeden Kassenzettel aufheben?",
             ["Nein. Für das Haushaltsbuch reicht es, die Ausgabe zu notieren. Aufheben musst du nur Belege, die du für Garantie, Umtausch oder Steuer brauchst."]],
            ["Reicht ein Foto für die Garantie?",
             ["Für die gesetzliche Gewährleistung gegenüber dem Händler genügt ein Kaufnachweis – auch ein Foto des Bons oder der Kontoauszug. Bei einer freiwilligen Herstellergarantie gelten deren Bedingungen; manche verlangen den Originalbeleg."]],
            ["Kann ich mir den Kassenbon digital geben lassen?",
             ["Händler müssen seit 2020 für jeden Kauf einen Beleg ausstellen, du musst ihn aber nicht mitnehmen. Der Beleg darf auch digital sein, wenn du zustimmst – per App, E-Mail oder QR-Code. Für Garantiefälle legst du ihn wie einen Scan ab."]],
        ],
    },

    # ------------------------------------------------------------ Abos
    {
        "id": "subscriptions",
        "slug": "abos-finden-und-kuendigen",
        "title": "Abos finden und kündigen: der Abo-Check in 30 Minuten",
        "desc": "Abo-Check: so findest du alle laufenden Abos auf Kontoauszug, PayPal, Google Play und App Store, rechnest sie aufs Jahr hoch und kündigst, was du nicht brauchst.",
        "h1": "Abos finden und kündigen: der Abo-Check",
        "teaser": "Alle Abos aufspüren, aufs Jahr hochrechnen, entscheiden – in einer halben Stunde.",
        "answer": "**Für den Abo-Check gehst du drei Monate Kontoauszüge, PayPal und die Abo-Liste in Google Play bzw. im App Store durch** und schreibst jedes wiederkehrende Abo mit Betrag auf. Rechne alles aufs Jahr hoch – erst dann sieht man, was es wirklich kostet. Was du im letzten Monat nicht genutzt hast, kündigst du.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "lowincome", "yearly"],
        "sections": [
            ["finden", "Wo sich Abos verstecken", [
                {"list": [
                    "**Kontoauszüge der letzten drei Monate** – Lastschriften mit gleichem Betrag oder gleichem Empfänger.",
                    "**Kreditkartenabrechnung** – viele Abos laufen über die Karte, nicht übers Girokonto.",
                    "**PayPal** – in den Einstellungen unter den automatischen Zahlungen.",
                    "**Google Play** – Play Store öffnen, Profilbild antippen, „Zahlungen und Abos“, dann „Abos“.",
                    "**App Store** – in den Einstellungen auf deinen Namen tippen, dann „Abonnements“.",
                    "**Jahresabos** – tauchen nur einmal im Jahr auf. Dafür lohnt ein Blick in den Auszug von vor zwölf Monaten oder in die E-Mails nach „Verlängerung“.",
                ]},
            ]],
            ["hochrechnen", "Aufs Jahr hochrechnen", [
                {"table": [
                    ["Abo", "im Monat", "im Jahr", "letzte Nutzung"],
                    ["Streaming A", "13,99 €", "167,88 €", "gestern"],
                    ["Streaming B", "8,99 €", "107,88 €", "vor 6 Wochen"],
                    ["Musik", "10,99 €", "131,88 €", "täglich"],
                    ["Cloud-Speicher", "2,99 €", "35,88 €", "läuft im Hintergrund"],
                    ["Fitnessstudio", "29,90 €", "358,80 €", "vor 2 Monaten"],
                    ["Zeitschrift digital", "6,99 €", "83,88 €", "vor 3 Wochen"],
                ]},
                {"calc": [["Summe im Monat", "73,85 €"], ["**Summe im Jahr**", "886,20 €"]],
                 "caption": "Beispiel mit erfundenen Beträgen"},
                "Monatsbeträge wirken klein, Jahresbeträge nicht. Bei der Frage „Würde ich das heute für 358,80 € im Jahr abschließen?“ fällt die Entscheidung oft leichter.",
            ]],
            ["kuendigen", "Kündigen ohne Umwege", [
                {"steps": [
                    "**Im Store gekaufte Abos im Store kündigen** – über die Abo-Liste von Google Play oder App Store. Eine App zu deinstallieren beendet das Abo nicht.",
                    "**Online abgeschlossene Verträge über den Kündigungsbutton.** Wer in Deutschland Abos oder Laufzeitverträge über seine Website anbietet, muss dort seit dem 1. Juli 2022 einen gut sichtbaren Kündigungsbutton haben – auch für ältere Verträge. Ausgenommen sind unter anderem Finanzdienstleistungen.",
                    "**Laufzeit prüfen.** Für Verträge, die seit dem 1. März 2022 geschlossen wurden, gilt: Nach der ersten Laufzeit (höchstens zwei Jahre) kommst du mit einem Monat Frist heraus. Versicherungen sind ausgenommen.",
                    "**Bestätigung aufheben** – Screenshot oder E-Mail, bis die letzte Abbuchung vorbei ist.",
                    "**Im nächsten Monat prüfen**, ob wirklich nichts mehr abgebucht wurde.",
                ]},
            ]],
            ["rhythmus", "Einmal im Jahr wiederholen", [
                "Abos sammeln sich still an: Probemonate, die weiterlaufen, Preiserhöhungen, die niemand bemerkt. Ein fester Termin im Jahr – etwa im Januar – reicht, um den Überblick zu behalten.",
            ]],
        ],
        "app": {
            "h2": "Abos im Einfachen Haushaltsbuch",
            "body": [
                "Abos gehören in der App zu den Fixkosten. Schon die Einrichtung schlägt hinter dem Plus Posten wie Musik-Streaming, Video-Streaming oder Fitnessstudio vor. Später ergänzt du Abos unter **Einstellungen → Einnahmen und Fixkosten** – monatlich, vierteljährlich oder jährlich mit Fälligkeitsdatum. Die App zieht sie danach selbst ab, ab dem nächsten Zeitraum.",
                "Kündigst du ein Abo, entfernst du den Posten. Er zählt ab dem nächsten Zeitraum nicht mehr – dann zeigt die große Zahl, was dir zusätzlich bleibt.",
            ],
        },
        "faq": [
            ["Beendet Deinstallieren einer App das Abo?",
             ["Nein. Ein Abo, das über Google Play oder den App Store läuft, musst du dort kündigen. Sonst wird weiter abgebucht."]],
            ["Bekomme ich nach dem Kündigen noch Zugriff?",
             ["Bei den meisten Abos ja, bis zum Ende des bezahlten Zeitraums. Erst danach endet der Zugang."]],
            ["Was ist mit Abos, die ich mit anderen teile?",
             ["Gleich behandeln: Kosten pro Person ausrechnen und entscheiden, ob es sich für dich lohnt. Geteilte Abos werden oft weitergezahlt, weil niemand sich zuständig fühlt."]],
        ],
    },

    # ------------------------------------------------------------ Impulskäufe
    {
        "id": "impulse",
        "slug": "impulskaeufe-vermeiden",
        "title": "Impulskäufe vermeiden: 7 Tricks, die im Alltag funktionieren",
        "desc": "Impulskäufe vermeiden: 24-Stunden-Regel, Wunschliste, Arbeitsstunden-Rechnung und weniger Kaufanreize – sieben alltagstaugliche Tricks gegen Spontankäufe.",
        "h1": "Impulskäufe vermeiden: sieben Tricks für den Alltag",
        "teaser": "24-Stunden-Regel, Wunschliste und die Frage: Wie viele Arbeitsstunden ist das?",
        "answer": "**Gegen Impulskäufe hilft vor allem eines: Zeit zwischen Wunsch und Bezahlen.** Mit der 24-Stunden-Regel kommt alles, was nicht geplant war, erst auf eine Wunschliste. Ist es am nächsten Tag noch wichtig, kaufst du es. Dazu kommen weniger Anreize – keine gespeicherten Zahlungsdaten, keine Newsletter – und das sofortige Aufschreiben jeder Ausgabe.",
        "updated": U, "updated_label": UL,
        "related": ["nospend", "habit", "lowincome"],
        "sections": [
            ["tricks", "Sieben Tricks", [
                {"steps": [
                    "**24-Stunden-Regel.** Ungeplante Käufe ab einem Betrag, den du festlegst (etwa 30 €), wartest du einen Tag ab. Bei größeren Beträgen eine Woche.",
                    "**Wunschliste statt Warenkorb.** Notiere, was du willst, mit Datum. Viele Einträge sind nach einer Woche erledigt, ohne dass du etwas gekauft hast.",
                    "**In Arbeitsstunden rechnen.** Teile den Preis durch deinen Netto-Stundenlohn (Beispiel unten).",
                    "**Zahlungsdaten nicht speichern.** Wer für jeden Onlinekauf die Karte holen muss, kauft weniger nebenbei.",
                    "**Newsletter und Push-Mitteilungen von Shops abbestellen.** Rabatt-Mails erzeugen Bedarf, den es vorher nicht gab.",
                    "**Mit Liste einkaufen** – und nur in die Gänge gehen, in denen etwas von der Liste liegt.",
                    "**Jede Ausgabe sofort aufschreiben.** Wer den Betrag eintippen muss, nimmt ihn bewusster wahr.",
                ]},
            ]],
            ["arbeitsstunden", "Die Arbeitsstunden-Rechnung", [
                {"calc": [["Preis der Jacke", "89,00 €"], ["÷ Netto-Stundenlohn", "15,00 €"], ["**= Arbeitsstunden**", "ca. 6 Stunden"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Den Netto-Stundenlohn bekommst du grob so: Netto im Monat geteilt durch die Arbeitsstunden im Monat (bei 40 Stunden pro Woche etwa 173). Die Frage „Ist mir das sechs Stunden Arbeit wert?“ klingt anders als „Sind 89 € okay?“.",
            ]],
            ["ausloeser", "Die eigenen Auslöser kennen", [
                "Impulskäufe passieren selten zufällig. Typische Auslöser sind Langeweile, Stress, Belohnung nach einem harten Tag oder das Scrollen am Abend. Wer weiß, wann er spontan kauft, kann genau dann gegensteuern – etwa die Shopping-Apps vom Startbildschirm des Handys nehmen.",
                {"note": "Wer merkt, dass Kaufen sich nicht mehr steuern lässt und Schulden entstehen, findet bei Schuldner- und Suchtberatungsstellen kostenlose Hilfe."},
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Das Aufschreiben ist in der App schnell genug, um es an der Kasse zu tun: Betrag eintippen, Speichern antippen. Die große Zahl **Verfügbar** sinkt sofort – das ist oft Bremse genug für den nächsten Spontankauf.",
                "Läuft die Füllung des Balkens über den Zeitstrich hinaus, färbt sie sich um: ein Hinweis, dass du schneller ausgibst, als der Monat vergeht.",
            ],
        },
        "faq": [
            ["Ist jeder spontane Kauf ein Problem?",
             ["Nein. Ein Eis an einem heißen Tag ist kein Problem. Es geht um Käufe, die du kurz danach bereust oder die das Monatsbudget sprengen."]],
            ["Ab welchem Betrag sollte die 24-Stunden-Regel gelten?",
             ["Leg einen Betrag fest, der zu deinem Budget passt – oft 20 bis 50 €. Wichtig ist, dass er vorher feststeht und nicht im Laden verhandelt wird."]],
            ["Kann ich einen Impulskauf rückgängig machen?",
             ["Online meist ja: Es gilt in der Regel ein 14-tägiges Widerrufsrecht ab Lieferung, mit Ausnahmen etwa für Maßanfertigungen oder Tickets für feste Termine. Im Laden gibt es kein gesetzliches Umtauschrecht – Rücknahme ist Kulanz, also vor dem Kauf fragen."]],
        ],
    },

    # ------------------------------------------------------------ Miete
    {
        "id": "rent",
        "slug": "wie-viel-miete",
        "title": "Wie viel Miete kann ich mir leisten? Faustregel und Rechnung",
        "desc": "Wie viel Miete kann ich mir leisten? Die Drittel-Faustregel, Kalt- oder Warmmiete, und die Gegenprobe mit Netto und Fixkosten: Was bleibt danach?",
        "h1": "Wie viel Miete kann ich mir leisten?",
        "teaser": "Die Drittel-Regel, ihre Grenzen und eine Rechnung mit deinen eigenen Zahlen.",
        "answer": "**Die bekannteste Faustregel lautet: höchstens ein Drittel des Netto-Einkommens fürs Wohnen, gerechnet mit der Warmmiete.** Bei 2.700 € netto wären das 900 €. Aussagekräftiger ist die Gegenprobe: Zieh Warmmiete und alle anderen Fixkosten vom Netto ab und prüf, ob der Rest für den Alltag und eine Sparrate reicht.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "rule503020", "daily"],
        "sections": [
            ["faustregel", "Die Drittel-Regel", [
                {"calc": [["Netto-Einkommen", "2.700,00 €"], ["÷ 3", ""], ["**Warmmiete höchstens**", "900,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Die Regel kursiert in zwei Fassungen: Vermieter verlangen oft ein Netto vom Dreifachen der Kaltmiete. Für dein eigenes Budget zählt die Warmmiete – Kaltmiete plus Nebenkosten und Heizung –, denn nur sie zeigt, was wirklich abgeht. Strom läuft meist über einen eigenen Vertrag und kommt noch dazu.",
                "In teuren Städten liegt die Wohnkostenquote vieler Haushalte deutlich höher. Die Regel ist dann kein Ausschlusskriterium, sondern eine Warnung: Je höher der Anteil, desto weniger Spielraum für alles andere.",
            ]],
            ["gegenprobe", "Die Gegenprobe mit deinen Fixkosten", [
                "Wichtiger als der Prozentsatz ist, was nach allen festen Kosten übrig bleibt:",
                {"calc": [["Netto-Einkommen", "2.700,00 €"], ["− Warmmiete", "980,00 €"], ["− Strom", "60,00 €"], ["− Versicherungen", "95,00 €"],
                          ["− Handy, Internet", "55,00 €"], ["− Deutschlandticket", "63,00 €"], ["− Abos", "25,00 €"], ["− Sparrate", "200,00 €"],
                          ["**= frei für den Monat**", "1.222,00 €"]],
                 "caption": "Beispiel: 36 % Warmmiete, erfundene Zahlen"},
                "Bleibt genug für Lebensmittel, Kleidung, Freizeit und einen Puffer, kann die Wohnung auch über einem Drittel liegen. Wird es schon ohne Sparrate knapp, ist sie zu teuer – egal, was die Faustregel sagt.",
            ]],
            ["nicht-vergessen", "Was beim Umzug gern vergessen wird", [
                {"list": [
                    "**Kaution:** höchstens drei Nettokaltmieten ([§ 551 BGB](https://www.gesetze-im-internet.de/bgb/__551.html)); du darfst sie in drei Monatsraten zahlen.",
                    "**Nachzahlungen:** Neue Wohnungen haben oft zu niedrig angesetzte Nebenkosten-Vorauszahlungen.",
                    "**Fahrtkosten:** Die günstigere Wohnung weiter draußen kann über Ticket oder Sprit teurer werden.",
                    "**Einrichtung:** Küche, Lampen, Gardinen – einmalige Kosten, die man einplanen sollte.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Die Gegenprobe im Einfachen Haushaltsbuch",
            "body": [
                "Bei der Einrichtung fragt die App Posten für Posten nach Miete, Heizkosten, Strom und Nebenkosten – danach zeigt die große Zahl, was nach allen Fixkosten bleibt.",
                "Änderst du später den Mietposten, gilt der neue Betrag ab dem nächsten Zeitraum; der laufende Monat bleibt, wie er ist. Eine neue Wohnung rechnest du vor dem Umzug deshalb mit der Gegenprobe oben durch.",
            ],
        },
        "faq": [
            ["Zählt die Kalt- oder die Warmmiete?",
             ["Für dein Budget die Warmmiete, also mit Nebenkosten und Heizung – nur so lassen sich Wohnungen mit unterschiedlicher Heizart vergleichen. Vermieter rechnen dagegen oft mit der Kaltmiete und wollen ein Netto von etwa dem Dreifachen sehen."]],
            ["Gilt die Drittel-Regel auch für Paare?",
             ["Ja, bezogen auf das gemeinsame Netto. Rechnet die Gegenprobe aber auch für den Fall durch, dass ein Einkommen eine Zeit lang wegfällt."]],
            ["Was, wenn die Miete schon jetzt mehr als die Hälfte frisst?",
             ["Dann lohnt ein Blick auf die übrigen Fixkosten und auf mögliche Ansprüche wie Wohngeld. Eine Mieter- oder Sozialberatung hilft beim Prüfen."]],
        ],
    },

    # ------------------------------------------------------------ Paare
    {
        "id": "couples",
        "slug": "haushaltsbuch-fuer-paare",
        "title": "Haushaltsbuch für Paare: gemeinsame Kosten fair aufteilen",
        "desc": "Haushaltsbuch für Paare: drei Kontomodelle, faire Aufteilung nach Einkommen mit Rechenbeispiel und wie ihr gemeinsame Ausgaben ohne Streit im Blick behaltet.",
        "h1": "Haushaltsbuch für Paare: Kosten fair teilen",
        "teaser": "Drei Kontomodelle, Aufteilung nach Einkommen und wer das Haushaltsbuch führt.",
        "answer": "**Paare teilen gemeinsame Kosten meist nach einem von drei Modellen: alles gemeinsam, alles getrennt oder ein Gemeinschaftskonto für die gemeinsamen Kosten plus je ein eigenes Konto.** Verdienen beide unterschiedlich, ist die Aufteilung nach Einkommen oft fairer als halbe-halbe: Bei 2.800 € und 1.700 € netto trägt die eine Person 62 %, die andere 38 % der gemeinsamen Kosten.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "rent", "categories"],
        "sections": [
            ["modelle", "Drei Kontomodelle", [
                {"table": [
                    ["Modell", "So geht es", "Passt, wenn …"],
                    ["Alles gemeinsam", "Beide Einkommen auf ein Konto, alles wird gemeinsam bezahlt", "ihr ähnlich mit Geld umgeht und viel Vertrauen da ist"],
                    ["Alles getrennt", "Jede Person zahlt bestimmte Posten, Rest wird ausgeglichen", "ihr erst kurz zusammenwohnt oder sehr unabhängig bleiben wollt"],
                    ["Drei Konten", "Gemeinschaftskonto für Miete, Einkauf & Co., dazu je ein eigenes Konto", "ihr Gemeinsames teilen, aber eigenes Geld behalten wollt"],
                ]},
                "Wichtig beim Gemeinschaftskonto, über das jede Person allein verfügen darf („Oder-Konto“): Beide haften gemeinsam – auch für ein Minus, das nur eine Person verursacht hat.",
                "Das Drei-Konten-Modell ist verbreitet, weil es zwei Streitpunkte trennt: Was gemeinsam ist, ist klar geregelt – und was jede Person mit dem eigenen Geld macht, geht die andere nichts an.",
            ]],
            ["aufteilung", "Halbe-halbe oder nach Einkommen?", [
                "Halbe-halbe ist einfach, aber bei ungleichen Einkommen bleibt einer Person deutlich weniger für sich. Die Alternative: Jede Person zahlt denselben **Anteil** ihres Einkommens ein.",
                {"calc": [["Netto Person A", "2.800,00 €"], ["Netto Person B", "1.700,00 €"], ["Zusammen", "4.500,00 €"], ["Gemeinsame Kosten", "2.000,00 €"],
                          ["Anteil A: 2.800 ÷ 4.500 = 62,2 %", "1.244,44 €"], ["**Anteil B: 1.700 ÷ 4.500 = 37,8 %**", "755,56 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "So bleiben beiden 1.555,56 € bzw. 944,44 € – jeweils etwa 56 % des eigenen Netto. Bei halbe-halbe blieben A 1.800 € und B nur 700 €.",
            ]],
            ["was-gemeinsam", "Was zählt als gemeinsam?", [
                {"list": [
                    "**Klar gemeinsam:** Miete, Nebenkosten, Strom, Internet, Hausrat, Lebensmittel, Haushaltsartikel.",
                    "**Absprechen:** Auto, Urlaub, Essen gehen zu zweit, Geschenke für Familie.",
                    "**Meist eigen:** Kleidung, Hobbys, Handyvertrag, eigene Abos.",
                ]},
                "Schreibt die Liste einmal auf und prüft sie, wenn sich etwas ändert – Umzug, Kind, neuer Job.",
            ]],
            ["fuehren", "Wer führt das Haushaltsbuch?", [
                "Ein gemeinsames Haushaltsbuch funktioniert am besten, wenn klar ist, wer es führt – oder wenn jede Person ihr eigenes Budget im Blick behält und das Gemeinschaftskonto nur die festen Beträge bekommt. Einmal im Monat zehn Minuten gemeinsam draufschauen reicht.",
            ]],
        ],
        "app": {
            "h2": "Das Einfache Haushaltsbuch zu zweit",
            "body": [
                "Ehrlich vorweg: Die App synchronisiert nicht zwischen zwei Handys – es gibt keine Cloud und keinen Server. Für Paare passt sie deshalb so: Jede Person führt ihr eigenes Budget, und der eigene Anteil an den gemeinsamen Kosten steht bei den Fixkosten.",
                "Oder eine Person führt das Haushaltsbuch für das Gemeinschaftskonto und trägt die gemeinsamen Einkäufe ein.",
            ],
        },
        "faq": [
            ["Ist halbe-halbe unfair?",
             ["Nicht unbedingt. Bei ähnlichen Einkommen ist es die einfachste Lösung. Bei großen Unterschieden bleibt der Person mit weniger Einkommen aber oft kaum Spielraum – dann ist die Aufteilung nach Einkommen eine Alternative."]],
            ["Wie gehen wir mit Sparzielen um?",
             ["Gemeinsame Ziele wie Urlaub oder Umzug können wie eine Fixkostenposition aufs Gemeinschaftskonto laufen. Persönliche Sparziele bleiben auf den eigenen Konten."]],
            ["Gibt es Haushaltsbuch-Apps, die auf zwei Handys synchronisieren?",
             ["Ja, viele – dafür liegen die Daten dann auf einem Server des Anbieters. Worauf du bei Apps ohne Cloud achten solltest: [Haushaltsbuch-App ohne Bankverbindung](/anleitungen/haushaltsbuch-app-ohne-bankverbindung/)."]],
        ],
    },

    # ------------------------------------------------------------ unregelmäßiges Einkommen
    {
        "id": "irregular",
        "slug": "budget-unregelmaessiges-einkommen",
        "title": "Budget bei unregelmäßigem Einkommen: so planen Selbstständige",
        "desc": "Budget bei schwankendem Einkommen: Grundgehalt an dich selbst, Puffer-Konto, Rechnung aus den letzten Monaten – für Selbstständige, Freelancer, Aushilfen.",
        "h1": "Budget bei unregelmäßigem Einkommen",
        "teaser": "Ein festes Gehalt an dich selbst und ein Puffer, der die Schwankungen schluckt.",
        "answer": "**Bei schwankendem Einkommen planst du nicht mit dem, was gerade reinkommt, sondern mit einem festen „Gehalt an dich selbst“.** Alle Einnahmen landen zuerst auf einem Puffer-Konto; von dort überweist du dir jeden Monat denselben Betrag aufs Girokonto. Diesen Betrag setzt du zwischen deinem schwächsten Monat und dem Durchschnitt an – und budgetierst damit wie mit einem normalen Gehalt.",
        "updated": U, "updated_label": UL,
        "related": ["payday", "emergency", "daily"],
        "sections": [
            ["prinzip", "Das Prinzip: Puffer und Grundgehalt", [
                {"steps": [
                    "**Puffer-Konto einrichten**, zum Beispiel ein Tagesgeldkonto. Alle Einnahmen gehen dorthin.",
                    "**Grundgehalt festlegen** – den Betrag, den du dir jeden Monat zum selben Tag überweist.",
                    "**Mit dem Grundgehalt budgetieren**, als wäre es ein Lohn: Fixkosten abziehen, Rest einteilen.",
                    "**Überschüsse bleiben im Puffer.** Wird er größer als nötig, darf ein Teil in Sparziele oder eine Gehaltserhöhung an dich selbst fließen.",
                ]},
                {"note": "Wer selbstständig ist, legt vorher zur Seite: die eingenommene Umsatzsteuer komplett, dazu einen festen Anteil des Gewinns für die Einkommensteuer sowie die Beiträge für Kranken- und Rentenversicherung. Wie viel, zeigen der Vorauszahlungsbescheid oder die Steuerberatung. Das Grundgehalt ist das, was danach privat verfügbar ist."},
            ]],
            ["hoehe", "Wie hoch das Grundgehalt sein sollte", [
                "Schau dir die privaten Netto-Einnahmen der letzten Monate an – nach Steuerrücklage:",
                {"table": [
                    ["Monat", "Juni", "Juli", "Aug.", "Sept.", "Okt.", "Nov."],
                    ["Einnahmen", "1.900 €", "3.400 €", "2.200 €", "1.600 €", "2.800 €", "2.100 €"],
                ]},
                {"calc": [["Summe sechs Monate", "14.000,00 €"], ["Durchschnitt", "2.333,33 €"], ["Schwächster Monat", "1.600,00 €"], ["**Grundgehalt, vorsichtig angesetzt**", "1.900,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Mit dem Durchschnitt zu planen ist riskant: Zwei schwache Monate hintereinander leeren den Puffer. Sicherer ist ein Betrag zwischen schwächstem Monat und Durchschnitt.",
                {"table": [
                    ["Monat", "Juni", "Juli", "Aug.", "Sept.", "Okt.", "Nov."],
                    ["Puffer-Änderung bei 1.900 €", "0", "+1.500", "+300", "−300", "+900", "+200"],
                    ["Puffer-Stand bei 1.900 €", "0", "1.500", "1.800", "1.500", "2.400", "2.600"],
                    ["Puffer-Stand bei 2.333 € (Durchschnitt)", "−433", "+634", "+501", "−232", "+235", "+2"],
                ]},
                "Mit dem vorsichtigen Betrag wächst der Puffer in sechs Monaten um 2.600 € und fällt nie unter den Startwert. Mit dem Durchschnitt rutscht er gleich im ersten Monat ins Minus, im September noch einmal, und steht am Ende bei null.",
            ]],
            ["puffer", "Wie groß der Puffer sein sollte", [
                "Als Startwert: zwei bis drei Grundgehälter, bevor du das System umstellst. Wer stark saisonal arbeitet, eher mehr. Der Puffer ersetzt nicht den Notgroschen – der ist für Notfälle, der Puffer für normale Schwankungen: [Notgroschen](/anleitungen/notgroschen-wie-hoch/).",
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Trag dein Grundgehalt als monatliche Einnahme ein – an dem Tag, an dem du es dir überweist. Den Budgetbeginn kannst du unter **Einstellungen → Budget beginnt** auf genau diesen Tag legen: [Budget ab Gehaltseingang](/anleitungen/budget-ab-gehaltseingang/).",
                "Einnahmen, die du direkt ausgeben willst, trägst du über das Plus im Verlauf als Einnahme nach. Änderst du das Grundgehalt, gilt der neue Betrag ab dem nächsten Zeitraum. Was im Puffer bleibt, gehört nicht ins Haushaltsbuch – sonst sieht das Monatsbudget größer aus, als es ist.",
            ],
        },
        "faq": [
            ["Was mache ich, wenn der Puffer leer läuft?",
             ["Dann ist das Grundgehalt zu hoch angesetzt. Senk es für die nächsten Monate und prüf die Fixkosten, bis der Puffer wieder wächst."]],
            ["Gilt das auch für Minijob oder Schichtarbeit?",
             ["Ja. Wo der Lohn je nach Stunden schwankt, hilft dasselbe Prinzip: mit einem vorsichtigen Grundbetrag planen, was darüber hinausgeht, für schwache Monate zurücklegen."]],
            ["Wie oft sollte ich das Grundgehalt anpassen?",
             ["Etwa einmal im Halbjahr, mit den Zahlen der letzten sechs bis zwölf Monate. Nicht nach jedem guten Monat."]],
        ],
    },

    # ------------------------------------------------------------ Wie viel sparen
    {
        "id": "savehowmuch",
        "slug": "wie-viel-sollte-man-sparen",
        "title": "Wie viel sollte man im Monat sparen? Faustregeln und deine Zahl",
        "desc": "Wie viel sollte man im Monat sparen? 10 bis 20 % als Faustregel, Rechnung vom Sparziel rückwärts und die Reihenfolge: Notgroschen, Rücklagen, Langfristiges.",
        "h1": "Wie viel sollte man im Monat sparen?",
        "teaser": "Faustregeln, die richtige Reihenfolge und eine Rechnung für deinen Betrag.",
        "answer": "**Verbreitete Faustregeln nennen 10 bis 20 % des Netto-Einkommens als Sparrate.** Realistisch ist der Betrag, der nach Fixkosten und einem ehrlichen Alltagsbudget übrig bleibt – und den du jeden Monat schaffst. Spar zuerst für einen Notgroschen, dann für planbare größere Ausgaben, dann für langfristige Ziele.",
        "updated": U, "updated_label": UL,
        "related": ["rule503020", "emergency", "leftover"],
        "sections": [
            ["faustregeln", "Was die Faustregeln sagen", [
                {"table": [
                    ["Netto", "10 %", "15 %", "20 % (50/30/20-Regel)"],
                    ["1.800 €", "180 €", "270 €", "360 €"],
                    ["2.200 €", "220 €", "330 €", "440 €"],
                    ["3.000 €", "300 €", "450 €", "600 €"],
                ]},
                {"formula": "Sparquote = monatliche Sparrate ÷ Netto-Einkommen × 100"},
                "Beide Werte sind Richtwerte für Menschen, bei denen nach den Fixkosten genug übrig bleibt. Bei kleinem Einkommen ist ein fester kleiner Betrag sinnvoller als ein Prozentsatz: [Sparen mit wenig Einkommen](/anleitungen/sparen-mit-wenig-einkommen/).",
            ]],
            ["deine-zahl", "Deinen eigenen Betrag finden", [
                {"calc": [["Netto-Einkommen", "2.200,00 €"], ["− Fixkosten", "1.180,00 €"], ["− Alltagsbudget (gemessen)", "760,00 €"], ["**= möglich zu sparen**", "260,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen, 11,8 % vom Netto"},
                "Das Alltagsbudget sollte gemessen sein, nicht geschätzt: vier Wochen alle Ausgaben aufschreiben. Geschätzte Werte sind fast immer zu niedrig – und dann geht die Sparrate am Monatsende wieder verloren.",
            ]],
            ["rueckwaerts", "Vom Ziel rückwärts rechnen", [
                "Oft hilft die umgekehrte Frage: Was willst du bis wann haben?",
                {"calc": [["Sparziel", "3.000,00 €"], ["÷ 18 Monate", "166,67 €"], ["**÷ 24 Monate**", "125,00 €"]],
                 "caption": "Beispiel ohne Zinsen, erfundene Zahlen"},
                {"table": [
                    ["Monatlich", "nach 1 Jahr", "nach 5 Jahren"],
                    ["50 €", "600 €", "3.000 €"],
                    ["100 €", "1.200 €", "6.000 €"],
                    ["260 €", "3.120 €", "15.600 €"],
                ]},
                "Passt die nötige Rate nicht ins Budget, verlängere die Zeit oder verkleinere das Ziel – statt die Alltagsausgaben auf Kante zu planen.",
            ]],
            ["reihenfolge", "Die Reihenfolge der Sparziele", [
                {"steps": [
                    "**Notgroschen** für Unvorhergesehenes: [wie hoch?](/anleitungen/notgroschen-wie-hoch/)",
                    "**Rücklagen für Planbares:** Versicherungen, Auto, Geschenke im Dezember: [jährliche Kosten einplanen](/anleitungen/jaehrliche-kosten-im-budget/).",
                    "**Mittelfristige Ziele:** Umzug, Möbel, Urlaub.",
                    "**Langfristig:** Altersvorsorge, Vermögensaufbau.",
                ]},
            ]],
            ["automatisch", "Sparen, bevor das Geld weg ist", [
                "Die Sparrate geht am besten per Dauerauftrag am Tag nach dem Gehaltseingang ab. Was am Monatsende übrig ist, kommt zusätzlich dazu. Wer umgekehrt spart – „was am Ende übrig ist“ –, spart in den meisten Monaten nichts.",
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch",
            "body": [
                "Trag die Sparrate als festen Posten bei den Fixkosten ein – bei der Einrichtung oder später unter **Einstellungen → Einnahmen und Fixkosten**; nachträglich zählt sie ab dem nächsten Zeitraum. Danach ist sie in jedem Monat vom ersten Tag an aus dem verfügbaren Geld heraus, und die große Zahl zeigt nur, was du wirklich ausgeben kannst.",
                "Am Monatsende steht in der Auswertung, was übrig ist. Überweist du den Rest aufs Sparkonto, lass **Plus mitnehmen** in den Einstellungen aus – sonst rechnet die App im nächsten Monat mit Geld, das schon weg ist.",
            ],
        },
        "faq": [
            ["Zählt die Tilgung eines Kredits als Sparen?",
             ["Eine Sondertilgung wirkt ähnlich wie Sparen, weil sie künftige Zinsen spart. Die reguläre Rate gehört zu den Fixkosten."]],
            ["Sollte ich sparen, wenn ich Dispo-Schulden habe?",
             ["Erst einen kleinen Notgroschen, dann den Dispo abbauen. Der Dispo kostet in der Regel deutlich mehr Zinsen, als ein Sparkonto bringt."]],
            ["Was ist, wenn ich in einem Monat nichts sparen kann?",
             ["Das passiert. Wichtig ist, dass der Dauerauftrag in normalen Monaten läuft. Wenn es öfter nicht klappt, ist die Sparrate zu hoch angesetzt – lieber kleiner, dafür jeden Monat."]],
        ],
    },

    # ------------------------------------------------------------ Senioren / Helfer (25.11.2026)
    # Suchnachfrage (Autocomplete 25.11.): „haushaltsbuch für senioren“, „haushaltsbuch für rentner“,
    # „budget rentner ehepaar“; en „helping elderly parents with finances“, „budget worksheet for elderly“.
    {
        "id": "seniors",
        "slug": "haushaltsbuch-fuer-senioren",
        "title": "Haushaltsbuch für Senioren: einfach anfangen, auch mit Hilfe",
        "desc": "Haushaltsbuch für Senioren und Rentner: Rente minus feste Kosten, was pro Tag bleibt, und wie Angehörige beim Einrichten helfen, ohne zu bevormunden.",
        "h1": "Haushaltsbuch für Senioren – und für Angehörige, die helfen",
        "teaser": "Rente minus feste Kosten, ein Betrag pro Tag – und wie Kinder oder Enkel beim Einrichten helfen.",
        "answer": "**Es reicht eine einfache Rechnung: Rente minus feste Kosten.** Was übrig bleibt, teilst du durch die Tage im Monat. Aufschreiben musst du nur die Beträge. Kinder oder Enkel können beim ersten Mal helfen.",
        "updated": "2026-11-25", "updated_label": "November 2026",
        "related": ["daily", "fixed", "payday"],
        "sections": [
            ["rechnung", "Die eine Rechnung: Rente minus feste Kosten", [
                {"steps": [
                    "**Einnahmen zusammenzählen:** Rente, Betriebsrente, Witwenrente, Wohngeld, also alles, was jeden Monat sicher aufs Konto kommt.",
                    "**Feste Kosten abziehen:** Miete oder Hausgeld, Strom, Heizung, Telefon, Versicherungen, regelmäßige Zuzahlungen für Medikamente, Abos, Spenden per Dauerauftrag.",
                    "**Durch die Tage teilen:** Was übrig ist, geteilt durch die Tage bis zur nächsten Rente, ist das Geld pro Tag für Einkauf, Apotheke, Friseur und Geschenke.",
                ]},
                {"calc": [["Rente (netto)", "1.480,00 €"], ["− feste Kosten", "940,00 €"], ["= frei im Monat", "540,00 €"], ["÷ 30 Tage", ""], ["**pro Tag**", "18,00 €"]],
                 "caption": "Beispiel mit erfundenen Zahlen"},
                "Selbst rechnen geht mit dem [Tagesbudget-Rechner](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/#rechner).",
            ]],
            ["rentenzahltag", "Wann kommt die Rente? Den Monat danach ausrichten", [
                "Die gesetzliche Rente kommt am **letzten Bankarbeitstag des Monats**: bei Rentenbeginn ab April 2004 für den ablaufenden Monat, bei älteren Renten im Voraus für den nächsten. Das Geld ist also kurz vor dem Monatsersten da, und ein Haushaltsbuch vom 1. bis zum Monatsende passt dazu. Kommt anderes Geld mitten im Monat, etwa eine Betriebsrente, kann der Budgetmonat am Zahltag beginnen: [Monatsbudget ab Gehaltseingang](/anleitungen/budget-ab-gehaltseingang/).",
                "Jährliche Kosten wie Kfz-Versicherung, Hausrat oder die Nebenkostenabrechnung durch zwölf teilen und monatlich einplanen: [Jährliche Kosten im Monatsbudget](/anleitungen/jaehrliche-kosten-im-budget/).",
            ]],
            ["einfach", "So bleibt es einfach", [
                {"list": [
                    "**Nur den Betrag aufschreiben.** Kategorien sind freiwillig. Wer weiß, was pro Tag geht, braucht keine Statistik.",
                    "**Gleich an der Kasse oder abends**, aber jeden Tag zur selben Zeit. Kassenzettel in eine Schale legen und abends eintragen ist ein guter Weg.",
                    "**Bargeld zählt mit.** Wer viel bar bezahlt, schreibt nicht das Abheben auf, sondern das, was ausgegeben wird.",
                    "**Papier ist in Ordnung.** Ein Heft oder ein ausgedrucktes Blatt reicht völlig, zum Beispiel unser [Haushaltsbuch zum Ausdrucken](/anleitungen/haushaltsbuch-zum-ausdrucken/). Wichtig ist nur, dass es jeden Tag griffbereit liegt.",
                ]},
            ]],
            ["angehoerige", "Für Angehörige: helfen, ohne zu bevormunden", [
                "Oft schlagen Kinder oder Enkel ein Haushaltsbuch vor. Das klappt am besten, wenn die Eltern selbst entscheiden und ihr eigenes Geld im Blick behalten:",
                {"list": [
                    "**Einmal gemeinsam einrichten:** Einnahmen und feste Kosten zusammen von den Kontoauszügen abschreiben. Das ist die eigentliche Arbeit, danach ist das Führen leicht.",
                    "**Nur das Nötigste zeigen:** einen Betrag eintragen und sehen, was noch übrig ist. Mehr nicht.",
                    "**Nachfragen statt kontrollieren:** Einmal im Monat gemeinsam draufschauen, wenn die Eltern das möchten.",
                    "**Rechtliches gehört nicht ins Haushaltsbuch.** Wer Bankgeschäfte für die Eltern erledigen soll, braucht eine Vollmacht. Dazu beraten Bank, Notar oder Betreuungsvereine.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Das Einfache Haushaltsbuch für Ältere",
            "body": [
                "Auf dem Startbildschirm steht groß eine Zahl: was in diesem Monat nach den festen Kosten noch übrig ist. Eine Ausgabe sind zwei Klicks: Betrag eintippen, speichern. Passt das Ziffernfeld nicht auf den Bildschirm, etwa bei sehr großer Schrift, zeigt die App stattdessen den Knopf **Jetzt tracken**. Das ist ein Klick mehr, dafür bleiben die Tasten groß.",
                "Einnahmen und feste Kosten trägt man einmal ein. Das können Angehörige beim Einrichten übernehmen. Ehrlich dazu: Die App hat kein Konto und keine Cloud. Angehörige sehen die Zahlen also nicht aus der Ferne, sie bleiben auf dem Handy der Eltern. Frühestens ab dem fünften Tag zeigt die App oben einen Werbebanner; ein einmaliger Kauf entfernt ihn dauerhaft.",
            ],
        },
        "faq": [
            ["Brauche ich für ein Haushaltsbuch einen Computer?",
             ["Nein. Ein Heft, ein ausgedrucktes Blatt oder eine App auf dem Handy reichen. Entscheidend ist, dass es dort liegt, wo man bezahlt oder abends sitzt."]],
            ["Muss ich jede Ausgabe einer Kategorie zuordnen?",
             ["Nein. Für die Frage „Reicht das Geld bis zur nächsten Rente?“ genügt der Betrag."]],
            ["Wie oft sollten Angehörige mit draufschauen?",
             ["So oft, wie die Eltern es möchten. Einmal im Monat zehn Minuten sind für die meisten genug."]],
        ],
    },

    # ------------------------------------------------------------ Jahresanfang (25.11.2026)
    # Suchnachfrage DE schwach (Autocomplete: „haushaltsbuch wie anfangen“, keine Vorsatz-Begriffe);
    # en stärker („new year budget plan/template/tips“). Januar-Landeseite auf Gideons Wunsch (24.11.).
    {
        "id": "newyear",
        "slug": "haushaltsbuch-anfangen-neues-jahr",
        "title": "Haushaltsbuch anfangen zum neuen Jahr: Start in 4 Schritten",
        "desc": "Haushaltsbuch zum Jahresanfang anfangen: Kassensturz, feste und jährliche Kosten, Tagesbudget und 30 Tage nur Beträge – damit der Vorsatz den Februar übersteht.",
        "h1": "Haushaltsbuch anfangen: der Start ins neue Jahr in 4 Schritten",
        "teaser": "Kassensturz, Jahreskosten, Tagesbudget – und warum die ersten 30 Tage nur Beträge brauchen.",
        "answer": "**Vier Schritte reichen.** Schau, was auf dem Konto ist. Schreib auf, was fest abgeht. Rechne aus, was pro Tag bleibt. Dann schreibst du 30 Tage lang nur die Beträge auf – sonst nichts.",
        "updated": "2026-11-25", "updated_label": "November 2026",
        "related": ["simple", "habit", "yearly"],
        "sections": [
            ["kassensturz", "Schritt 1: Kassensturz nach den Feiertagen", [
                "Nach Weihnachten ist das Konto oft leerer als gedacht. Schreib einmal auf, wie es wirklich steht: Kontostand, offene Rechnungen, Kreditkartenabrechnung, Ratenkäufe. Nicht bewerten, nur festhalten. Daran misst du im Dezember, was sich verändert hat.",
            ]],
            ["kosten", "Schritt 2: feste und jährliche Kosten", [
                "Liste alles auf, was jeden Monat sicher abgeht: Miete, Strom, Handy, Versicherungen, Abos. Eine Vorlage: [Fixkosten-Liste](/anleitungen/fixkosten-liste/).",
                "Der Januar ist ein guter Monat für die **jährlichen** Kosten, denn viele werden zum Jahresanfang fällig, zum Beispiel Kfz-Versicherung, Jahresabos und Mitgliedsbeiträge. Teile sie durch zwölf und plane sie monatlich ein: [Jährliche Kosten im Monatsbudget](/anleitungen/jaehrliche-kosten-im-budget/).",
                "Gleich mit erledigen: Abos kündigen, die keiner mehr nutzt. [Abos finden und kündigen](/anleitungen/abos-finden-und-kuendigen/).",
            ]],
            ["tagesbudget", "Schritt 3: eine Zahl pro Tag", [
                {"formula": "Tagesbudget = (Einkommen − feste Kosten − Sparrate) ÷ Tage im Monat"},
                "Diese Zahl ist dein Kompass für den Januar. Noch keine Sparrate? Rechne im ersten Monat mit 0. Rechnen kannst du sie mit dem [Tagesbudget-Rechner](/anleitungen/wie-viel-darf-ich-pro-tag-ausgeben/#rechner).",
            ]],
            ["dreissig-tage", "Schritt 4: 30 Tage nur Beträge", [
                "Viele Vorsätze scheitern nicht am Willen, sondern am Aufwand. Deshalb gilt im ersten Monat nur eine Regel: **Jede Ausgabe mit Betrag aufschreiben, sofort oder am selben Abend.** Keine Kategorien, keine Ziele, kein schlechtes Gewissen.",
                "Am Monatsende schaust du einmal zurück: Was ist übrig? Wo hat es gezwickt? Erst dann lohnt es sich, eine Sparrate festzulegen oder Kategorien zu ergänzen. Mehr zum Dranbleiben: [Haushaltsbuch führen und durchhalten](/anleitungen/haushaltsbuch-fuehren-tipps/).",
                {"note": "Wer es sportlicher mag, beginnt mit einer [No-Spend-Challenge](/anleitungen/no-spend-challenge/). Als Dauerzustand taugt sie aber nicht."},
            ]],
        ],
        "app": {
            "h2": "Mit dem Einfachen Haushaltsbuch ins neue Jahr",
            "body": [
                "Einnahmen und feste Kosten trägst du einmal ein, jährliche mit ihrem Fälligkeitsdatum – die App zieht sie in dem Monat ab, in dem sie fällig sind. Danach zeigt der Startbildschirm, was im Monat noch übrig ist, und eine Ausgabe sind zwei Klicks: Betrag eintippen, speichern.",
                "Am Monatsende erscheint in der Auswertung die Karte **Monatsende**: Wenn du magst, tippst du deinen Kontostand ein. Ab dem zweiten Monat zeigt die App, ob Ausgaben fehlen, die du nicht eingetragen hast. Einmal im Jahr fragt sie: **Stimmen Einkommen und Fixkosten noch?**",
            ],
        },
        "faq": [
            ["Muss ich am 1. Januar anfangen?",
             ["Nein. Am besten startest du an dem Tag, an dem dein Gehalt kommt. Dann passt der Budgetmonat zu deinem Geld: [Budget ab Gehaltseingang](/anleitungen/budget-ab-gehaltseingang/)."]],
            ["Was mache ich mit den Ausgaben von Weihnachten?",
             ["Sie gehören zum alten Jahr. Im Kassensturz siehst du, was davon noch offen ist, etwa eine Kreditkartenabrechnung. Plane den offenen Betrag im Januar als feste Ausgabe ein."]],
            ["Papier oder App?",
             ["Beides funktioniert. Entscheidend ist, dass du es beim Bezahlen oder abends sofort zur Hand hast. Für Papier: [Haushaltsbuch zum Ausdrucken](/anleitungen/haushaltsbuch-zum-ausdrucken/)."]],
        ],
    },
    # ------------------------------------------------------------ Druckvorlage (26.11.2026, Gideon)
    # Suchnachfrage: „haushaltsbuch vorlage zum ausdrucken“, „haushaltsbuch führen handschriftlich“.
    {
        "id": "printable",
        "slug": "haushaltsbuch-zum-ausdrucken",
        "title": "Haushaltsbuch zum Ausdrucken: kostenlose PDF-Vorlage",
        "desc": "Haushaltsbuch zum Ausdrucken, kostenlos als PDF: große Schrift, eine Seite für Einnahmen und feste Ausgaben, dann ein Blatt pro Monat.",
        "h1": "Haushaltsbuch zum Ausdrucken",
        "teaser": "Große Schrift, eine Seite für das Feste, ein Blatt pro Monat. Kostenloses PDF.",
        "answer": "**Kostenlos zum Ausdrucken, in großer Schrift.** Auf der ersten Seite stehen deine Einnahmen und festen Ausgaben. Auf den Monatsblättern schreibst du auf, was du ausgibst.",
        "updated": "2026-11-26", "updated_label": "November 2026",
        "related": ["simple", "fixed", "seniors"],
        "sections": [
            ["download", "Herunterladen", [
                {"download": ["PDF herunterladen", "/vorlagen/mein-haushaltsbuch.pdf", "A4, 13 Seiten, kostenlos"]},
                {"pages": [["vorlage-de-seite-1.webp", "Erste Seite: Monatliche Einnahmen, feste monatliche Ausgaben, Zum Leben übrig"],
                           ["vorlage-de-monat.webp", "Monatsblatt: Zum Leben übrig, Liste mit Tag, Wofür und Betrag, Übrig gesamt"]]},
            ]],
            ["so-gehts", "So geht's", [
                {"steps": [
                    "**Erste Seite einmal ausfüllen:** was jeden Monat reinkommt und was fest abgeht. Unten steht dann, was dir zum Leben übrig bleibt.",
                    "**Jeden Monat** diese Zahl oben auf ein Monatsblatt schreiben.",
                    "**Aufschreiben, was du ausgibst.** Am Monatsende zusammenzählen und abziehen.",
                ]},
                "Reicht ein Blatt nicht, druckst du einfach ein weiteres aus.",
            ]],
        ],
        "app": {
            "h2": "Lieber am Handy?",
            "body": [
                "Das Einfache Haushaltsbuch für Android rechnet alles selbst. Feste Ausgaben trägst du einmal ein, eine Ausgabe sind zwei Klicks: Betrag eintippen, speichern.",
            ],
        },
        "faq": [
            ["Kostet die Vorlage etwas?",
             ["Nein. Ausdrucken, ausfüllen, fertig."]],
            ["Muss ich im Januar anfangen?",
             ["Nein. Du fängst in dem Monat an, in dem du willst."]],
            ["Was mache ich, wenn ein Blatt nicht reicht?",
             ["Druck ein zweites Monatsblatt aus und schreib dort weiter."]],
        ],
    },
]
