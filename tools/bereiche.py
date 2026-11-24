"""Bereiche der Anleitungen (angelegt 24.11.2026, Gideon: Brotkrumen und Bereiche wie bei Removication).

Jede Anleitung gehoert ueber ihre "id" zu genau einem Bereich. Bereichsseiten:
/anleitungen/<slug>/ (de) und /en/guides/<slug>/ (en). Die Uebersicht zeigt die Anleitungen nach
Bereichen gruppiert statt als eine lange Liste; jede Anleitung bekommt die Brotkrumen
Haushaltsbuch / Anleitungen / Bereich und "Weitere Anleitungen" bevorzugt aus ihrem Bereich.
URLs der Anleitungen bleiben unveraendert. Neue Anleitung -> hier ihre id eintragen
(build.py bricht sonst mit einer klaren Meldung ab). Die Reihenfolge in OF ist die Reihenfolge
der Kacheln auf der Bereichsseite und in der Uebersicht.

Textregeln (Lektorat 24.11.2026): Die Einleitung behauptet nur, was die Anleitungen des Bereichs
wirklich hergeben (z. B. nennt en "groceries" keine Durchschnittswerte; Kakeibo = vier Fragen +
Monatsrueckblick, nicht "Nachdenken vor dem Kauf"). Titel <= 65 Zeichen ohne Anhaengsel, en in
normaler Schreibung (kein Title Case, wie die Anleitungen). Titel nicht auf die Suchbegriffe einer
einzelnen Anleitung legen (z. B. nicht "Haushaltsbuch fuehren ... Tipps" - das gehoert der
Anleitung "habit"). Beschreibung <= 160 Zeichen.
"""

ORDER = ["basics", "methods", "howmuch", "costs"]

OF = {
    "basics": ["simple", "habit", "nobank", "categories", "receipts", "couples"],
    "methods": ["rule503020", "envelope", "kakeibo", "nospend", "payday"],
    "howmuch": ["daily", "groceries", "rent", "savehowmuch", "emergency"],
    "costs": ["fixed", "yearly", "subscriptions", "impulse", "lowincome", "irregular", "leftover"],
}
HUB_OF = {gid: hub for hub, ids in OF.items() for gid in ids}

TEXT = {
    "de": {
        "others_h": "Weitere Bereiche",
        "basics": {
            "slug": "haushaltsbuch-grundlagen", "name": "Grundlagen",
            "title": "Haushaltsbuch-Grundlagen: anfangen, Kategorien, Belege, zu zweit",
            "desc": "Grundlagen fürs Haushaltsbuch: einfach anfangen, dranbleiben, Kategorien wählen, Kassenzettel aufheben oder wegwerfen, App ohne Bankverbindung, zu zweit.",
            "h1": "Haushaltsbuch führen: die Grundlagen",
            "intro": [
                "Ein Haushaltsbuch scheitert selten an der Mathematik, sondern daran, dass man nach zwei Wochen aufhört. Die Anleitungen in diesem Bereich drehen sich um das Führen selbst: wie wenig Aufwand reicht, welche Kategorien sinnvoll sind (und wann du keine brauchst), welche Kassenzettel du aufheben musst, worauf du bei einer App ohne Bankverbindung achtest und wie ihr die Kosten zu zweit teilt.",
                "Das meiste davon geht auch mit Stift und Papier – die App nimmt dir das Rechnen ab.",
            ],
        },
        "methods": {
            "slug": "budget-methoden", "name": "Budget-Methoden",
            "title": "Budget-Methoden: 50/30/20-Regel, Umschlagmethode, Kakeibo & Co.",
            "desc": "Budget-Methoden erklärt: 50/30/20-Regel, Umschlagmethode, Kakeibo, No-Spend-Challenge und Budget ab Gehaltseingang – mit Beispielen.",
            "h1": "Budget-Methoden: welche passt zu dir?",
            "intro": [
                "Es gibt nicht die eine richtige Methode. Die 50/30/20-Regel teilt das Netto in drei feste Anteile, die Umschlagmethode gibt jedem Ausgabenbereich ein eigenes Budget, Kakeibo arbeitet mit vier Fragen und einem ehrlichen Rückblick am Monatsende, und eine No-Spend-Challenge ist eine begrenzte Zeit ohne Ausgaben für Nicht-Notwendiges.",
                "Dazu kommt eine Frage, die sich bei jeder Methode stellt: an welchem Tag dein Budgetmonat beginnt, wenn das Gehalt nicht am 1. kommt. Die Anleitungen arbeiten mit erfundenen Beispielzahlen und zeigen am Ende, wie du die Methode mit dem Einfachen Haushaltsbuch umsetzt.",
            ],
        },
        "howmuch": {
            "slug": "wie-viel-geld-fuer", "name": "Wie viel Geld für …?",
            "title": "Wie viel Geld für Lebensmittel, Miete und Sparen? Richtwerte",
            "desc": "Richtwerte und Rechenwege: wie viel pro Tag, für Lebensmittel, für Miete, wie viel sparen und wie hoch der Notgroschen sein sollte.",
            "h1": "Wie viel Geld für …? Richtwerte und Rechenwege",
            "intro": [
                "„Ist das viel?“ – die Frage kommt, sobald die ersten Ausgaben im Haushaltsbuch stehen. Diese Anleitungen geben Richtwerte und Faustregeln für Lebensmittel, Miete, Sparen und Notgroschen und zeigen, wie du aus deinen eigenen Zahlen ein Tagesbudget ausrechnest.",
                "Richtwerte sind ein Startpunkt, kein Urteil: Was für dich passt, zeigen erst deine eigenen Ausgaben.",
            ],
        },
        "costs": {
            "slug": "kosten-im-griff", "name": "Kosten im Griff",
            "title": "Kosten im Griff: Fixkosten, Abos, Impulskäufe, wenig Einkommen",
            "desc": "Anleitungen, um Kosten in den Griff zu bekommen: Fixkosten-Liste, jährliche Kosten, Abos kündigen, Impulskäufe, wenig oder unregelmäßiges Einkommen.",
            "h1": "Kosten im Griff: Fixkosten, Abos und Monatsende",
            "intro": [
                "Knapp wird das Geld selten wegen einer einzelnen großen Anschaffung. Häufiger liegt es an festen Kosten, die keiner mehr ansieht, an jährlichen Rechnungen, die überraschend kommen, und an vielen kleinen Spontankäufen.",
                "Diese Anleitungen helfen dir, die festen Kosten vollständig zu erfassen, Abos zu finden, mit wenig oder schwankendem Einkommen zu planen – und zu entscheiden, was am Monatsende mit dem Rest oder einem Minus passiert.",
            ],
        },
    },
    "en": {
        "others_h": "More topics",
        "basics": {
            "slug": "budget-basics", "name": "Basics",
            "title": "Budget basics: getting started, categories, receipts, couples",
            "desc": "Budget basics: start simple, stick with it, choose categories, know which receipts to keep, use an app without bank linking, budget as a couple.",
            "h1": "Keeping a household budget: the basics",
            "intro": [
                "A budget rarely fails because of the maths – it fails because people stop after two weeks. The guides in this area are about the habit itself: how little effort is enough, which categories make sense (and when you need none), which receipts to keep, what to look for in an app without bank linking, and how to split costs as a couple.",
                "Most of it works with pen and paper too – the app just does the arithmetic.",
            ],
        },
        "methods": {
            "slug": "budgeting-methods", "name": "Budgeting methods",
            "title": "Budgeting methods: 50/30/20 rule, envelopes, kakeibo and more",
            "desc": "Budgeting methods explained: the 50/30/20 rule, envelope budgeting, kakeibo, a no-spend challenge and budgeting from payday – with examples.",
            "h1": "Budgeting methods: which one fits you?",
            "intro": [
                "There is no single right method. The 50/30/20 rule splits your take-home pay into three fixed shares, envelope budgeting gives each spending area its own budget, kakeibo works with four questions and an honest month-end review, and a no-spend challenge is a set time without spending on non-essentials.",
                "One question comes up with every method: which day your budget month starts when you're not paid on the 1st. The guides use made-up example numbers and end by showing how to run the method in Simple Household Budget.",
            ],
        },
        "howmuch": {
            "slug": "how-much-to-spend", "name": "How much for …?",
            "title": "How much to spend on groceries, rent and savings: rules of thumb",
            "desc": "Rules of thumb and calculations: how much per day, for groceries, for rent, how much to save and how big an emergency fund should be.",
            "h1": "How much for …? Rules of thumb and calculations",
            "intro": [
                "“Is that a lot?” is a question that comes up as soon as the first expenses are written down. These guides give rules of thumb for rent, savings and an emergency fund, show how to find your own grocery number, and how to work out a daily budget from your own numbers.",
                "Rules of thumb are a starting point, not a verdict – only your own spending shows what fits you.",
            ],
        },
        "costs": {
            "slug": "control-costs", "name": "Control costs",
            "title": "Control your costs: fixed expenses, subscriptions, impulse buys",
            "desc": "Guides to getting costs under control: fixed expenses list, yearly costs, cancelling subscriptions, impulse buying, low or irregular income.",
            "h1": "Getting costs under control: fixed costs, subscriptions, month end",
            "intro": [
                "Money rarely gets tight because of one big purchase. More often it's fixed costs nobody looks at any more, yearly bills that arrive as a surprise, and many small impulse buys.",
                "These guides help you list your fixed costs completely, find subscriptions, plan with a low or irregular income – and decide what happens to a surplus or a shortfall at month end.",
            ],
        },
    },
}
