"""Additional English guides, added 24 Nov 2026. Same ids as guides_de_2.py (hreflang pairs).

Search demand (Google autocomplete, 24 Nov 2026): 50/30/20 rule (calculator, examples),
how much should i spend on groceries a month / a week / for one person, envelope budgeting (app,
disadvantages), kakeibo method, emergency fund how much, how to budget on a low income,
no spend challenge (rules), budget categories, what receipts to keep / receipt scanner,
cancel subscriptions android, how to stop impulse buying, how much rent can i afford,
budget for couples (different incomes), how to budget irregular income, how much should i save
each month.

Written for an international audience: no country-specific law unless it is marked as such.
Amounts in euros, made up. The app has NO per-category analysis, NO per-category envelopes,
NO sync, and does NOT store receipt images.
"""

U = "2026-11-24"
UL = "November 2026"

GUIDES = [
    {
        "id": "rule503020",
        "slug": "50-30-20-rule",
        "title": "50/30/20 rule: how to work it out – and what if it doesn't fit",
        "desc": "The 50/30/20 rule splits take-home pay into needs, wants and savings. Worked example, the grey areas, and variants for when fixed costs already eat half.",
        "h1": "The 50/30/20 rule: maths, example and limits",
        "teaser": "Split take-home pay into needs, wants and savings – and what to do when 50% isn't enough.",
        "answer": "**The 50/30/20 rule splits your take-home pay into three pots: 50% for needs, 30% for wants, 20% for savings.** On €2,400 a month that's €1,200, €720 and €480. If your fixed costs already take more than half, treat the rule as a guide, not a test – and use 60/30/10 or 70/20/10 instead.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "fixed", "savehowmuch"],
        "sections": [
            ["maths", "How to work out the 50/30/20 rule", [
                "Start from what actually lands in your account each month, not your gross salary. Then split it:",
                {"table": [
                    ["Pot", "Share", "What goes in"],
                    ["Needs", "50%", "rent, utilities, insurance, groceries, getting to work, minimum loan payments"],
                    ["Wants", "30%", "eating out, hobbies, streaming, clothes beyond the basics, holidays"],
                    ["Savings", "20%", "emergency fund, sinking funds, retirement, extra debt payments"],
                ]},
                {"calc": [["Take-home pay", "€2,400.00"], ["50% needs", "€1,200.00"], ["30% wants", "€720.00"], ["**20% savings**", "€480.00"]],
                 "caption": "Example with made-up numbers"},
                "The rule was popularised by Elizabeth Warren and Amelia Warren Tyagi in their book *All Your Worth*. Its appeal: three numbers instead of twenty budget lines.",
                {"table": [
                    ["Take-home pay", "50% needs", "30% wants", "20% savings"],
                    ["€1,500", "€750", "€450", "€300"],
                    ["€2,000", "€1,000", "€600", "€400"],
                    ["€2,500", "€1,250", "€750", "€500"],
                    ["€3,000", "€1,500", "€900", "€600"],
                    ["€3,500", "€1,750", "€1,050", "€700"],
                ]},
            ]],
            ["doesnt-fit", "When 50% isn't enough for your needs", [
                "In expensive cities or on a small income, housing alone can take half. The rule isn't wrong then – it just doesn't match your situation. Two common variants:",
                {"calc": [["Take-home pay", "€2,400.00"], ["60% needs", "€1,440.00"], ["30% wants", "€720.00"], ["**10% savings**", "€240.00"]],
                 "caption": "60/30/10 variant, same made-up numbers"},
                {"calc": [["Take-home pay", "€2,400.00"], ["70% needs", "€1,680.00"], ["20% wants", "€480.00"], ["**10% savings**", "€240.00"]],
                 "caption": "70/20/10 variant, same made-up numbers"},
                "What matters is the order, not the exact percentage: **savings come first** – by automatic transfer the day after payday. Wants get what's left after that.",
                {"note": "A percentage you manage every month beats 20% you give up after three months."},
            ]],
            ["grey-areas", "Need or want? The grey areas", [
                {"list": [
                    "**Food:** basic groceries are a need, the deli counter is a want.",
                    "**Phone:** a contract is a need, the expensive handset on instalments partly a want.",
                    "**Car:** if you need it to get to work, it's a need; a second car is a want.",
                    "**Loans:** the minimum payment is a need, voluntary overpayments count as savings.",
                ]},
                "Be honest, not pedantic. If you try to classify every coffee, you'll soon stop. Sorting the big items once is enough.",
            ]],
            ["in-practice", "Putting the rule into practice", [
                {"steps": [
                    "**Add up your fixed costs** – the [fixed expenses list](/en/guides/fixed-expenses-list/) helps. They're most of your needs.",
                    "**Set up a automatic transfer** for your savings the day after payday.",
                    "**Treat the rest as your monthly budget** for groceries and wants together – the spending you steer day to day.",
                    "**Check at month end** whether it worked. Anything left can go to savings too: [money left at the end of the month](/en/guides/leftover-money-end-of-month/).",
                ]},
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "The app doesn't split into percentage pots – it keeps it simpler: income minus fixed costs is your monthly budget. Add your savings as a fixed item – during setup, or later under **Settings → Income and fixed costs** (it then counts from the next period). From then on they're out of the available money on the first day of every month – exactly the order the rule asks for.",
                "What's left shows as the large number on the home screen, and every expense comes off it right away.",
            ],
        },
        "faq": [
            ["Is the 50/30/20 rule based on gross or net income?",
             ["Net – what actually arrives in your account after tax and deductions."]],
            ["Do retirement savings count towards the 20%?",
             ["Private savings you pay yourself, yes. Anything your employer deducts before you're paid is already out of your take-home pay and doesn't count twice."]],
            ["What if I can't save anything?",
             ["Start with a small fixed amount, say €20 or €30 a month, and raise it when a fixed cost drops away. More: [how to budget on a low income](/en/guides/budget-on-a-low-income/)."]],
        ],
    },

    {
        "id": "groceries",
        "slug": "how-much-to-spend-on-groceries",
        # 28.11.2026: Gegenstueck zur deutschen Seite (Titel "Lebensmittel pro Monat: 1, 2, 4 Personen").
        # Belegte Zahlen gibt es hier nur fuer Deutschland (Destatis LWR 2024) - deshalb ausdruecklich so
        # beschriftet; USDA-Werte liessen sich am 28.11. nicht an der Quelle pruefen (Seite gesperrt).
        "title": "Groceries per month for 1, 2 or 4 people (Germany) – and yours",
        "desc": "Groceries per month in Germany (official statistics): 1 person €270, 2 people €505, 4 people €759 – per person and per week, and how to find your own number.",
        "h1": "How much should I spend on groceries a month?",
        "teaser": "Averages for 1 to 4 people – and your own number in four weeks.",
        "answer": "**In Germany, households spend on average per month: 1 person €270, 2 people €505, 3 people €653, 4 people €759** – food, drinks and tobacco together, according to the Federal Statistical Office (2024). Per person it gets cheaper with every extra member: €270 alone, about €190 each in a four-person household. Whether that fits you, four weeks of writing it down will show.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "categories", "envelope"],
        "sections": [
            ["averages", "Groceries per month: the average for 1 to 4 people", [
                {"table": [
                    ["Household", "per month", "per person, per month", "per week (whole household)"],
                    ["1 person", "€270", "€270", "about €62"],
                    ["2 people", "€505", "about €253", "about €116"],
                    ["3 people", "€653", "about €218", "about €150"],
                    ["4 people", "€759", "about €190", "about €174"],
                ]},
                "**Source:** [Federal Statistical Office of Germany (Destatis), continuous household budget surveys – consumer spending by household size](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Einkommen-Konsum-Lebensbedingungen/Konsumausgaben-Lebenshaltungskosten/Tabellen/privater-konsum-haushaltsgroesse-lwr.html) (in German), average for 2024 (table dated 17 August 2026). The “per month” column is from the table; “per person” and “per week” are our own conversion, rounded.",
                "**What’s included:** food, drinks and tobacco – that’s what the row in the table is called; alcoholic drinks count as drinks in the official breakdown. If you don’t smoke and buy little alcohol, your grocery bill alone will tend to be a bit lower. Eating out, canteen lunches and takeaway are **not** included. Prices and habits differ from country to country, so take these as a rough guide outside Germany.",
                "Averages like these mix city and countryside, discount stores and organic shops, canteen lunches and home cooking. No average can tell you whether your number is “too high” – only comparing yourself before and after a change can.",
                "So measure first, decide second.",
            ]],
            ["four-weeks", "Find your own number in four weeks", [
                {"steps": [
                    "**Pick four normal weeks** – no holidays, no parties.",
                    "**Write down every shopping trip**, including the bakery and food bought at the petrol station.",
                    "**Total each week** and take the average.",
                    "**Scale to a month:** weekly average × 4.35 (a month has about 4.35 weeks on average).",
                ]},
                {"calc": [["Week 1", "€54.20"], ["Week 2", "€38.90"], ["Week 3", "€61.30"], ["Week 4", "€47.60"],
                          ["Total, four weeks", "€202.00"], ["÷ 4 = per week", "€50.50"], ["**× 4.35 = per month**", "€219.68"]],
                 "caption": "Example with made-up numbers, one household"},
            ]],
            ["weekly", "A weekly budget beats a monthly one", [
                "For groceries a week works better than a month. If you notice on the 20th that the month's money is gone, there's little you can do. If you notice on Thursday that the week is tight, you still can.",
                "Set your weekly budget just below what you measured – €48 instead of €50.50 in the example. Small cuts stick, big ones don't.",
            ]],
            ["levers", "Five ways to cut the bill without going hungry", [
                {"list": [
                    "**Shop from a meal plan.** If you know what you'll cook, you buy fewer duplicates and throw less away.",
                    "**Shop less often.** Every extra trip to the shop brings impulse buys with it.",
                    "**Try own brands** one product at a time. If one doesn't taste right, go back to the brand for that one.",
                    "**Plan for leftovers**, for example one leftovers night a week.",
                    "**Track food on the go separately.** Takeaway coffee and lunch snacks are often the biggest item, but they don't show up as “groceries”.",
                ]},
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "For the four measuring weeks the amount and the category **Groceries** are enough. Type a description such as “weekly shop” and the app suggests the category itself. Hold receipts up to the camera instead of typing them in.",
                "How much you spend per day overall is in the analysis under **Per day** (on average, across all spending). The app doesn't total spending per category or week – for the four measuring weeks, add up your grocery entries in the history yourself.",
            ],
            "shot": "en-receipt.webp",
            "alt": "Simple Household Budget: the camera reads a receipt, the total line is highlighted.",
        },
        "faq": [
            ["Do toiletries count as groceries?",
             ["Ideally not. Washing powder, shower gel and toilet paper are often a surprisingly large part of the shop. Tracked separately, you see what really goes on food."]],
            ["How much does one person spend on groceries a month?",
             ["A one-person household in Germany spends €270 a month on average on food, drinks and tobacco (Federal Statistical Office, 2024) – about €62 a week. Without alcohol and tobacco it’s a little less."]],
            ["How much does a family of four spend on groceries?",
             ["In Germany a four-person household spends €759 a month on average – about €174 a week for everyone together, or about €190 per person a month."]],
            ["How do I work it out for a family?",
             ["The same way: write down everything the household spends on food for four weeks. You only need a per-person figure if you're splitting the costs."]],
            ["Why multiply by 4.35 and not by 4?",
             ["Because a month is longer than four weeks: 365 days ÷ 12 months ÷ 7 days is about 4.35. Multiply by 4 and you're two or three days of shopping short at month end."]],
        ],
    },

    {
        "id": "envelope",
        "slug": "envelope-budgeting",
        "title": "Envelope budgeting: how it works – with cash, accounts or on your phone",
        "desc": "Envelope budgeting splits your monthly money into envelopes for groceries, fun and more – with cash (cash stuffing), separate accounts or one number on your phone.",
        "h1": "Envelope budgeting: cash, accounts or digital",
        "teaser": "Split your monthly money into envelopes – and what's left of the idea without cash.",
        "answer": "**With envelope budgeting you split the money you have free each month into envelopes – one per spending area.** When an envelope is empty, that area is done until next month. With real cash this is also called cash stuffing. Without cash you can do it with separate accounts or in a simpler form: a single digital “envelope” that shows what's left this month.",
        "updated": U, "updated_label": UL,
        "related": ["daily", "categories", "nospend"],
        "sections": [
            ["principle", "The principle in three steps", [
                {"steps": [
                    "**Work out your spending money:** income minus fixed costs minus savings. How: [how much can I spend per day?](/en/guides/how-much-can-i-spend-per-day/)",
                    "**Split it into envelopes** – one for each area where you spend day to day.",
                    "**Only pay from the matching envelope.** Empty is empty. Moving money between envelopes is allowed, but deliberately.",
                ]},
                {"calc": [["Groceries", "€320.00"], ["Transport", "€100.00"], ["Fun", "€120.00"], ["Clothes", "€60.00"],
                          ["Toiletries", "€40.00"], ["Gifts", "€40.00"], ["Buffer", "€120.00"], ["**Spending money in total**", "€800.00"]],
                 "caption": "Example with made-up numbers"},
                "The **buffer** is the most important envelope. Without it the system collapses at the first flat bike tyre.",
            ]],
            ["variants", "Cash, accounts or digital?", [
                {"table": [
                    ["Variant", "What's good", "The catch"],
                    ["Cash in real envelopes (cash stuffing)", "very tangible – you watch the money shrink", "hard to use online or by card; cash at home"],
                    ["Separate bank accounts", "works with cards and online", "moving money around; not every bank offers enough sub-accounts"],
                    ["One digital envelope", "one number, no sorting", "no separate limits per area"],
                ]},
                "Many people start with six envelopes and end up with two or three after a few months: one for groceries, one for everything else – or just one.",
            ]],
            ["start-cash", "How to start with cash", [
                {"steps": [
                    "**Withdraw once, on payday** – the whole month's spending money in one go.",
                    "**Ask for small notes**, so you can pay exactly from each envelope.",
                    "**For online purchases**, take the amount out of the envelope and pay it back into your account – otherwise online shopping escapes the system.",
                ]},
            ]],
            ["one-envelope", "The simpler form: one envelope", [
                "If sorting is what makes you give up, one envelope for all everyday spending is enough. The limit is then not “fun is empty” but “the month is empty”.",
                "For that to work you need a sense of pace: are you spending faster than the month is passing? The pace check is in [how much can I spend per day?](/en/guides/how-much-can-i-spend-per-day/)",
            ]],
            ["mistakes", "Common mistakes", [
                {"list": [
                    "**Budgeting too tightly.** Envelopes with no slack lead to reshuffling after two weeks – and then to giving up.",
                    "**Forgetting yearly bills.** Insurance doesn't belong in the everyday envelope: [yearly bills in a monthly budget](/en/guides/yearly-expenses-monthly-budget/).",
                    "**Not counting card payments.** If you pay both cash and card, both come out of the same envelope.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Simple Household Budget as one envelope",
            "body": [
                "The app has no separate envelopes per category. It works like the simpler form: the large number **Available** is your single envelope – income minus fixed costs, minus every expense you save.",
                "The bar below shows the pace: the fill is what you've spent, the mark how far along the month is. No cash, no moving money between accounts.",
            ],
            "shot": "en-home.webp",
            "alt": "Simple Household Budget: home screen with Available €1,222.65 and a bar with a time mark.",
        },
        "faq": [
            ["What happens to money left in an envelope at month end?",
             ["Decide in advance: roll it into next month, move it to savings, or collect it for something specific. More: [money left at the end of the month](/en/guides/leftover-money-end-of-month/)."]],
            ["How many envelopes make sense?",
             ["As few as possible. Three to six is a good start, and a buffer always belongs in there."]],
            ["Can I move money between envelopes?",
             ["Yes, but openly: if you move money from “clothes” to “groceries”, you know there's less for clothes afterwards."]],
        ],
    },

    {
        "id": "kakeibo",
        "slug": "kakeibo-method",
        "title": "Kakeibo method: the Japanese way to budget, explained simply",
        "desc": "Kakeibo is a Japanese household budget built on four questions and four categories. How the method works, with a sample month and tips for everyday use.",
        "h1": "Kakeibo: the Japanese household budget in four questions",
        "teaser": "Four questions, four categories and a month-end review.",
        "answer": "**Kakeibo is a Japanese household budget built on four questions: How much money do I have? How much do I want to save? How much am I spending? How can I improve?** Spending goes into four categories – needs, wants, culture, unexpected. The heart of it is the honest review at month end, not the table.",
        "updated": U, "updated_label": UL,
        "related": ["simple", "categories", "habit"],
        "sections": [
            ["origin", "Where kakeibo comes from", [
                "Kakeibo (家計簿, pronounced kah-keh-boh) simply means household account book in Japanese. The printed ledger goes back to the journalist Motoko Hani, who published a household account book in her women's magazine in 1904. The four questions and four categories known outside Japan were popularised by Fumiko Chiba's 2017 book *Kakeibo: The Japanese Art of Saving Money*. Many people still keep it by hand, often in a dedicated notebook.",
            ]],
            ["four-questions", "The four questions", [
                {"steps": [
                    "**How much money do I have?** At the start of the month: income minus fixed costs.",
                    "**How much do I want to save?** One amount, before the first money is spent.",
                    "**How much am I spending?** Every expense through the month, with one of the four categories.",
                    "**How can I improve?** At month end: what was worth it, what wasn't?",
                ]},
                {"calc": [["Take-home pay", "€2,050.00"], ["− Fixed costs", "€1,130.00"], ["− Savings goal", "€150.00"], ["**For the month**", "€770.00"]],
                 "caption": "Questions 1 and 2 as a sum, made-up numbers"},
            ]],
            ["categories", "The four categories", [
                {"table": [
                    ["Category", "Examples"],
                    ["Needs", "groceries, toiletries, travel pass, medicine"],
                    ["Wants", "eating out, clothes, hobbies"],
                    ["Culture", "books, cinema, concerts, museums, courses"],
                    ["Unexpected", "repairs, doctor's bills, a broken washing machine, last-minute gifts"],
                ]},
                "The categories are deliberately broad. The point isn't where every euro went, but whether your money matches what matters to you.",
            ]],
            ["review", "The month-end review – the real kakeibo", [
                "At the end of the month, take ten minutes and answer in writing:",
                {"list": [
                    "Did I reach my savings goal? If not, why?",
                    "Which purchase was worth it – which one wouldn't I make again?",
                    "What exactly will I do differently next month? One thing, not five.",
                ]},
                "The review works because it's slow. Collecting numbers without looking at them is a list, not kakeibo.",
            ]],
        ],
        "app": {
            "h2": "Kakeibo with Simple Household Budget",
            "body": [
                "Setup answers questions 1 and 2: enter income and fixed costs, and add your savings as a fixed item. Question 3 is every expense you save. You can create the four kakeibo categories as your own categories if the defaults are too detailed. The app doesn't total spending per category – add up the four kakeibo totals in the history at month end.",
                "For question 4 the analysis shows the month in three numbers: spent, left, per day on average. The review itself is best still written by hand.",
            ],
        },
        "faq": [
            ["Do I need a special kakeibo book?",
             ["No. A notebook with one page per month is enough. Printed kakeibo books just give you the questions and columns."]],
            ["Is kakeibo the same as a normal budget?",
             ["The numbers are the same. The difference is the review: kakeibo asks every month whether your spending matched your goals."]],
            ["Where do fixed costs go?",
             ["They're not in the four categories. You subtract them at the start of the month, before you plan."]],
        ],
    },

    {
        "id": "emergency",
        "slug": "emergency-fund-how-much",
        "title": "Emergency fund: how much you need and how to build it",
        "desc": "How big should your emergency fund be? The common rule is three to six months of expenses – worked out from your fixed costs, with a plan and where to keep it.",
        "h1": "Emergency fund: how much, how to build it, where to keep it",
        "teaser": "Work out the size from your own spending and build it step by step.",
        "answer": "**A common rule of thumb: three to six months of essential expenses.** Add up your fixed costs plus the bare essentials for daily life – with €1,150 fixed costs and €450 essentials that's €1,600 a month, so €4,800 to €9,600. Keep the money separate from your everyday account but available at any time, for example in an savings account you can withdraw from at any time.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "yearly", "lowincome"],
        "sections": [
            ["what-for", "What the emergency fund is for", [
                "An emergency fund isn't holiday money or savings for the insurance bill in March. It's for what you can't plan: a broken washing machine, a car repair, losing your job, an unexpected bill. Without it, such things end up on an overdraft or a credit card – and that costs interest.",
                {"note": "Plannable costs such as yearly insurance belong in a separate pot: [yearly bills in a monthly budget](/en/guides/yearly-expenses-monthly-budget/)."},
            ]],
            ["size", "The size, from your own numbers", [
                {"steps": [
                    "**Add up your fixed costs** – rent, utilities, insurance, contracts. The [fixed expenses list](/en/guides/fixed-expenses-list/) helps.",
                    "**Add the essentials:** groceries, toiletries, getting around. Not what you spend now, but what you'd need in an emergency.",
                    "**Multiply by three to six.** The less secure your income, the closer to six.",
                ]},
                {"calc": [["Fixed costs per month", "€1,150.00"], ["+ Essentials", "€450.00"], ["= Monthly need", "€1,600.00"],
                          ["× 3 months", "€4,800.00"], ["**× 6 months**", "€9,600.00"]],
                 "caption": "Example with made-up numbers"},
                "If you're self-employed, have children or live on one income, aim for the upper end. In a secure job with two incomes, the lower end is often enough.",
            ]],
            ["build", "Build it in stages", [
                "A target of €4,800 can feel out of reach on a small budget. Break it up:",
                {"table": [
                    ["Stage", "Amount", "at €100 a month", "at €200 a month"],
                    ["Starter fund", "€1,000", "10 months", "5 months"],
                    ["One month's need", "€1,600", "16 months", "8 months"],
                    ["Three months' need", "€4,800", "48 months", "24 months"],
                ]},
                "One-off money gets you there faster: a tax refund, a bonus, what's left at month end. If you consistently move leftovers into the fund, you'll usually get there a lot sooner.",
            ]],
            ["where", "Where to keep it", [
                {"list": [
                    "**Separate from your everyday account**, so it doesn't look like spending money.",
                    "**Available at any time**, with no notice period and no market risk – for example an savings account you can withdraw from at any time.",
                    "**Not in stocks or investment funds.** Emergencies don't wait for good markets.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Read your monthly need from Simple Household Budget",
            "body": [
                "The analysis shows under **Breakdown** how much income and fixed costs are. Fixed costs are the biggest part of your monthly need – leave out any savings item, it isn't a need. For the essentials, take the **Per day** figure from the analysis × 30 as an upper limit and trim it to what you'd really need.",
                "Add your monthly emergency-fund saving as a fixed item; if you add it later, it counts from the next period.",
            ],
            "shot": "en-summary.webp",
            "alt": "Simple Household Budget: analysis with spent, left, per day and the breakdown into income and fixed costs.",
        },
        "faq": [
            ["Does an overdraft count as an emergency fund?",
             ["No. An overdraft is an expensive loan. The emergency fund is there so you don't need it."]],
            ["Should I pay off debt or build the fund first?",
             ["A small fund of around €1,000 usually comes first – otherwise the next repair creates new debt. After that, it pays to clear expensive debt such as overdrafts or credit cards faster."]],
            ["What if I've had to use it?",
             ["Top it back up before saving for anything else. Keep your usual savings amount running until it's full."]],
        ],
    },

    {
        "id": "lowincome",
        "slug": "budget-on-a-low-income",
        "title": "How to budget and save on a low income: 7 steps that work",
        "desc": "Budgeting on a low income: start with small fixed amounts, check fixed costs and benefits, find the small leaks – with a worked example for €1,450 a month.",
        "h1": "How to budget and save on a low income",
        "teaser": "Small fixed amounts, a fixed-costs check and the spending you don't notice.",
        "answer": "**On a low income you don't save with percentages but with a small fixed amount that goes out automatically** – say €30 by automatic transfer the day after payday. The money for it rarely comes from going without day to day; it comes from fixed costs that are too high and small spending you don't notice.",
        "updated": U, "updated_label": UL,
        "related": ["rule503020", "subscriptions", "emergency"],
        "sections": [
            ["starting-point", "Write down where you stand", [
                {"calc": [["Take-home pay", "€1,450.00"], ["− Fixed costs", "€1,020.00"], ["= Left for the month", "€430.00"], ["÷ 30 days", ""], ["**Per day**", "€14.33"]],
                 "caption": "Example with made-up numbers"},
                "With about €14 a day for food, toiletries and everything else, the 50/30/20 rule is unrealistic. That's not failure, it's maths. So take a different approach:",
            ]],
            ["steps", "Seven steps", [
                {"steps": [
                    "**Start with a tiny fixed amount.** €20 or €30 a month by automatic transfer. €30 is €360 a year – enough for broken glasses or an unexpected bill.",
                    "**Check fixed costs, not your coffee.** Phone plan, energy, insurance, subscriptions: switching takes effort once and saves money every month. Finding subscriptions: [cancel subscriptions you don't use](/en/guides/cancel-subscriptions/).",
                    "**Check what you're entitled to.** Housing support, child benefits or social tariffs for energy and transport often go unclaimed. Free debt or money advice services can help you check.",
                    "**Write everything down for four weeks.** On a tight budget the small amounts – vending machine, bakery, delivery – are often the difference between ending the month in the black or in the red.",
                    "**Use a weekly grocery budget** instead of a monthly one: [how much to spend on groceries](/en/guides/how-much-to-spend-on-groceries/).",
                    "**Park one-off money straight away.** Tax refund, bonus, cash gifts: whatever isn't planned for daily life goes straight to savings.",
                    "**Emergency fund first, everything else later.** A small buffer keeps the next repair off your overdraft: [emergency fund](/en/guides/emergency-fund-how-much/).",
                ]},
            ]],
            ["leaks", "Where money disappears unnoticed", [
                {"table": [
                    ["Small expense", "per week", "per year (× 52)"],
                    ["Takeaway coffee, 3 × €2.80", "€8.40", "€436.80"],
                    ["Vending-machine snack, 4 × €1.50", "€6.00", "€312.00"],
                    ["Food delivery, 1 × €18.00", "€18.00", "€936.00"],
                ]},
                "This isn't about cutting all of it. But once you see it, you decide differently – sometimes halving one of the three habits is enough.",
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "The app is free to use with ads (one banner from day five at the earliest; a one-time purchase removes it) and needs no account and no bank connection. Add your savings as a fixed item (added later, it counts from the next period); then the large number on the home screen only shows money you can really spend.",
                "Small amounts are quick to add: type the amount, tap Save. At month end a card in the analysis asks – optionally – for your account balance. From the second month on, the app compares it with your entries and shows whether you've missed any expenses.",
            ],
        },
        "faq": [
            ["Is saving €20 a month even worth it?",
             ["Yes. It's less about interest than about broken glasses or a surprise bill not landing on your overdraft. €20 a month is €240 after a year."]],
            ["What if I'm always short at month end?",
             ["First check fixed costs, then write down every expense for four weeks. If it still doesn't add up, a free debt or budgeting advice service is the right next step."]],
            ["Should I pay in cash to spend less?",
             ["It helps some people because they see the money go. Just make sure cash spending gets written down too – otherwise it's missing at month end."]],
        ],
    },

    {
        "id": "nospend",
        "slug": "no-spend-challenge",
        "title": "No-spend challenge: rules, variations and how to stick with it",
        "desc": "No-spend challenge: a day, a week or a month without non-essential spending. Set the rules, decide the exceptions and measure the result – with a worked example.",
        "h1": "No-spend challenge: rules, variations, results",
        "teaser": "Collect days without spending – with clear rules instead of guilt.",
        "answer": "**In a no-spend challenge you don't spend money on non-essentials for a set time.** Fixed costs keep running, and groceries from a list are usually allowed. What makes it work: rules you write down beforehand – and a number at the end that shows what it achieved.",
        "updated": U, "updated_label": UL,
        "related": ["impulse", "envelope", "habit"],
        "sections": [
            ["variations", "Three variations", [
                {"table": [
                    ["Variation", "For whom", "Typical goal"],
                    ["No-spend days", "beginners", "e.g. 10 days a month with no spending at all"],
                    ["No-spend week", "after an expensive month", "one week of groceries from a list only"],
                    ["No-spend month", "experienced budgeters", "a month without clothes, eating out or online shopping"],
                ]},
                "No-spend days are the easiest start. A full month without exceptions often fails at the first birthday invitation.",
            ]],
            ["rules", "Write the rules down first", [
                {"list": [
                    "**What keeps running:** rent, utilities, insurance, subscriptions – everything that goes out automatically.",
                    "**What's allowed:** groceries from a list? Fuel for the commute? Medicine?",
                    "**What's not allowed:** eating out, delivery, clothes, online shopping, takeaway coffee.",
                    "**What happens with exceptions:** a gift for a party isn't failure if the rules allow it.",
                ]},
                "Without written rules every exception becomes a negotiation with yourself – and you usually lose.",
            ]],
            ["measure", "Measure the result", [
                "Compare spending without fixed costs to a normal month:",
                {"calc": [["Spending last month", "€860.00"], ["Spending in the no-spend month", "€610.00"], ["**Difference**", "€250.00"]],
                 "caption": "Example with made-up numbers"},
                "Set the difference aside straight away – to savings or your emergency fund. Otherwise it vanishes next month.",
            ]],
            ["worth", "What a no-spend day is worth", [
                {"calc": [["Spending last month", "€860.00"], ["÷ 30 days", "€28.67"], ["**× 10 no-spend days**", "about €287"]],
                 "caption": "Same made-up numbers"},
                "That only holds if the spending isn't simply moved to the next day. Ten no-spend days followed by a big weekend shop save nothing.",
            ]],
            ["after", "After the challenge", [
                "The value is less in the money saved than in what you noticed: what did you really miss, and what not at all? What you didn't miss can go for good. What you did miss can come back into the budget – on purpose.",
            ]],
        ],
        "app": {
            "h2": "See no-spend days in Simple Household Budget",
            "body": [
                "The analysis shows a chart by day. Days without spending show only a small pale dot instead of a bar – so you see your no-spend days at a glance, without a separate tally. Use the arrows in the analysis to compare **Spent** with the previous period.",
                "The bar on the home screen shows how much of the month's money is spent and how far along the month is. In a no-spend month the fill stays well behind the mark.",
            ],
            "shot": "en-summary.webp",
            "alt": "Simple Household Budget: analysis with a daily chart in which days without spending show only a dot.",
        },
        "faq": [
            ["Do groceries count as spending?",
             ["You decide. Most people allow groceries from a list and rule out impulse buys and eating out."]],
            ["What if I break the challenge?",
             ["Write down why and carry on. One exception doesn't end the challenge – it shows you where a rule was too strict or too vague."]],
            ["How often should you do a no-spend challenge?",
             ["Hardly anyone keeps it up permanently. One no-spend month a year or a few fixed no-spend days each month work better for many people."]],
        ],
    },

    {
        "id": "categories",
        "slug": "budget-categories",
        "title": "Budget categories: which ones make sense – and how many",
        "desc": "Sensible budget categories: a list with examples, how many you need, why fixed costs stay out of everyday categories, and why fewer categories last longer.",
        "h1": "Budget categories: which, how many, what for",
        "teaser": "A lean category list with examples – and when you can do without.",
        "answer": "**For everyday spending eight to twelve categories are usually enough** – such as groceries, eating out, transport, clothing, health, personal care, hobbies and gifts. Fixed costs like rent and insurance don't need an everyday category; you subtract them first. If you're just starting, you can leave categories out entirely.",
        "updated": U, "updated_label": UL,
        "related": ["simple", "fixed", "envelope"],
        "sections": [
            ["list", "A lean category list", [
                {"table": [
                    ["Category", "What goes in"],
                    ["Groceries", "supermarket, bakery, market, drinks at home"],
                    ["Eating out", "restaurants, takeaway, delivery, canteen"],
                    ["Going out", "bars, clubs, cinema, concerts"],
                    ["Transport", "fuel, tickets, parking, bike, taxi"],
                    ["Clothing & accessories", "clothes, shoes, bags, jewellery"],
                    ["Personal care", "toiletries, hairdresser, cosmetics"],
                    ["Health", "pharmacy, prescriptions, glasses"],
                    ["Hobbies & leisure", "sport, books, games, courses"],
                    ["Home & furnishing", "furniture, decor, tools, appliances"],
                    ["Tech", "phone, accessories, computer, apps"],
                    ["Gifts", "birthdays, weddings, Christmas"],
                    ["Travel", "accommodation, getting there, day trips"],
                ]},
                "If an expense fits nowhere, “No category” is more honest than a “Miscellaneous” pot that grows every month.",
            ]],
            ["how-many", "How many categories make sense?", [
                "Every category is a decision at every purchase. Twenty categories means twenty chances to get stuck. So:",
                {"list": [
                    "**To start: none or two.** Say groceries and on the go, with everything else left without a category – or amounts only: [simple household budget](/en/guides/simple-household-budget/).",
                    "**After a month:** split the areas where you really want to know where the money goes.",
                    "**Rarely more than twelve to fifteen** for everyday spending. If you haven't used a category for three months, drop it.",
                ]},
            ]],
            ["fixed-costs", "Fixed costs stay out of everyday categories", [
                "Rent, utilities, insurance and subscriptions go out every month anyway. Mixed in with your shopping, they hide what's happening day to day. Better: collect fixed costs once and subtract them from income – the list is in [fixed expenses list](/en/guides/fixed-expenses-list/).",
            ]],
            ["grey-areas", "Settle the grey areas once", [
                {"list": [
                    "**Toiletries bought at the supermarket:** split on the receipt or all under groceries – as long as it's always the same.",
                    "**Lunch at work:** its own category if it's regular; it's often bigger than you'd think.",
                    "**Online orders:** sort by purpose (clothing, tech), not by retailer.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Categories in Simple Household Budget",
            "body": [
                "The app comes with a lean default list – including Groceries, Eating out, Lunch at work, Transport, Personal care, Health, Clothing & accessories, Gifts and Travel. You can rename and remove categories and add your own. There's deliberately no “Miscellaneous”; there's “No category” instead.",
                "The category is optional. When you type a description, the app suggests a matching category – from your own earlier entries and a built-in word list, on the device only. There's no breakdown by category; the category is shown under each entry in the history.",
            ],
            "shot": "en-history.webp",
            "alt": "Simple Household Budget: history with expenses by day, each with description and category.",
        },
        "faq": [
            ["Do I need categories at all?",
             ["Not to know how much is left. Categories help when you specifically want to know where the money goes – for example before deciding where to cut."]],
            ["Where does fuel go?",
             ["Under transport. Snacks or drinks bought at the petrol station are really groceries; if you want to keep it simple, put the whole receipt under transport."]],
            ["What about cash withdrawals?",
             ["The withdrawal itself isn't spending. Only what you buy with the cash belongs in the budget – otherwise you count it twice or not at all."]],
        ],
    },

    {
        "id": "receipts",
        "slug": "what-receipts-to-keep",
        "title": "Which receipts to keep – and for how long? Scan, file or bin",
        "desc": "Which receipts should you keep for warranties, returns and taxes? How long, why thermal receipts fade, how to scan the few that matter and what to do with the rest.",
        "h1": "Which receipts to keep, scan or throw away",
        "teaser": "The receipts you need, how to back them up, and what to do with the rest.",
        "answer": "**Most receipts can go once the expense is written down.** Keep the ones for expensive purchases (warranty, returns) and anything you need for your taxes. Because thermal paper fades, it's worth backing up those few as a photo or scan. Most shop receipts are thermal paper, which in many places belongs in general waste rather than paper recycling – check your local rules.",
        "updated": U, "updated_label": UL,
        "related": ["categories", "simple", "groceries"],
        "sections": [
            ["keep", "Which receipts to keep", [
                {"table": [
                    ["Receipt", "Why", "Roughly how long"],
                    ["Electronics, furniture, appliances", "warranty or legal guarantee", "at least until the warranty or guarantee period ends"],
                    ["Clothes, gifts", "returns", "until the shop's return period ends"],
                    ["Work equipment, tax-deductible expenses", "tax return", "as long as your tax authority can ask for proof"],
                    ["Everyday shopping", "none, once written down", "–"],
                ]},
                "Rules for guarantees and tax records differ by country – in the EU, for example, the legal guarantee on goods is at least two years. If in doubt, check your country's consumer or tax authority.",
            ]],
            ["thermal", "Why receipts fade", [
                "Most receipts are printed on thermal paper. Heat, light and friction make the print disappear over time – in a wallet often within a few months. If you'll need a receipt in two years, back it up as a photo or scan too.",
            ]],
            ["scan", "How to digitise the receipts that matter", [
                {"steps": [
                    "**Photograph it right after buying** – laid flat, good light, the whole receipt in view.",
                    "**Name it sensibly:** date, shop, item, e.g. “2026-11-24 electronics store washing machine”.",
                    "**Keep it in one place** – a “Receipts” folder in your cloud or photo storage, split by year.",
                    "**Keep the original too** until the warranty or return period is over. Some manufacturer warranties ask for the original.",
                ]},
            ]],
            ["dispose", "How to dispose of receipts", [
                "Thermal paper has a chemical coating that interferes with paper recycling, so many local authorities ask for it to go in general waste. A quick test: scratch the receipt with a fingernail – if a dark line appears, it's thermal paper. Plain-paper receipts can usually be recycled.",
            ]],
        ],
        "app": {
            "h2": "Receipts in Simple Household Budget",
            "body": [
                "For your budget you don't need to type receipts in: tap the camera icon and hold the receipt in view. The app reads the total, the shop, date and time and fills them in – you just tap Save. Text recognition runs on your phone.",
                "Important: the app is not a receipt archive. The image is neither stored nor sent anywhere. Back up receipts for warranties and taxes separately, as described above.",
            ],
            "shot": "en-receipt.webp",
            "alt": "Simple Household Budget: the camera reads a receipt, the total line “TOTAL EUR 22.42” is highlighted in green.",
        },
        "faq": [
            ["Do I have to keep every receipt?",
             ["No. For your budget, writing down the expense is enough. Only keep receipts you need for warranties, returns or taxes."]],
            ["Is a photo enough for a warranty claim?",
             ["Often, but not always – the shop or manufacturer decides. Keep the original until the warranty period is over and the photo as a backup."]],
            ["Can I get digital receipts instead?",
             ["Some shops offer receipts by app or email. That saves paper; for warranty cases, file the digital receipt like a scan."]],
        ],
    },

    {
        "id": "subscriptions",
        "slug": "cancel-subscriptions",
        "title": "Find and cancel subscriptions: a 30-minute subscription audit",
        "desc": "Subscription audit: find every recurring payment on bank statements, PayPal, Google Play and the App Store, add up the yearly cost and cancel what you don't use.",
        "h1": "Find and cancel subscriptions: the 30-minute audit",
        "teaser": "Track down every subscription, add it up per year, decide – in half an hour.",
        "answer": "**For a subscription audit, go through three months of bank and card statements, PayPal and the subscription lists in Google Play or the App Store**, and write down every recurring payment with its amount. Add everything up for a year – only then do you see what it really costs. Whatever you didn't use last month, cancel.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "lowincome", "yearly"],
        "sections": [
            ["find", "Where subscriptions hide", [
                {"list": [
                    "**Bank statements for the last three months** – direct debits with the same amount or payee.",
                    "**Credit card statements** – many subscriptions run on the card, not your everyday account.",
                    "**PayPal** – under automatic payments in the settings.",
                    "**Google Play** – open the Play Store, tap your profile picture, “Payments & subscriptions”, then “Subscriptions”.",
                    "**App Store (iPhone)** – open the Settings app, tap your name, then “Subscriptions”.",
                    "**Yearly subscriptions** – only show up once a year. Check the statement from twelve months ago or search your email for “renewal”.",
                ]},
            ]],
            ["add-up", "Add it up for a year", [
                {"table": [
                    ["Subscription", "per month", "per year", "last used"],
                    ["Streaming A", "€13.99", "€167.88", "yesterday"],
                    ["Streaming B", "€8.99", "€107.88", "6 weeks ago"],
                    ["Music", "€10.99", "€131.88", "daily"],
                    ["Cloud storage", "€2.99", "€35.88", "runs in the background"],
                    ["Gym", "€29.90", "€358.80", "2 months ago"],
                    ["Digital magazine", "€6.99", "€83.88", "3 weeks ago"],
                ]},
                {"calc": [["Total per month", "€73.85"], ["**Total per year**", "€886.20"]],
                 "caption": "Example with made-up amounts"},
                "Monthly amounts look small, yearly ones don't. “Would I sign up today for €358.80 a year?” is often an easier question.",
            ]],
            ["cancel", "How to cancel so it sticks", [
                {"steps": [
                    "**Cancel store subscriptions in the store** – via the subscription list in Google Play or the App Store. Uninstalling an app does not end the subscription.",
                    "**Cancel other contracts where you signed up** – usually in your account settings on the provider's website. Some countries require providers to offer online cancellation for contracts made online.",
                    "**Check the minimum term and notice period.** Gym, phone and insurance contracts often run for a fixed term. Note the last day you can cancel and set a reminder a month before.",
                    "**Keep the confirmation** – screenshot or email – until the last payment has gone through.",
                    "**Check next month** that nothing else was charged.",
                ]},
            ]],
            ["rhythm", "Repeat once a year", [
                "Subscriptions pile up quietly: free trials that keep running, price rises nobody notices. One fixed date a year – January, say – is enough to stay on top of them.",
            ]],
        ],
        "app": {
            "h2": "Subscriptions in Simple Household Budget",
            "body": [
                "In the app, subscriptions are fixed costs. Setup already suggests items such as music streaming, video streaming or gym behind the plus button; later you add them under **Settings → Income and fixed costs** – monthly, quarterly or yearly with a due date. The app then deducts them by itself, starting with the next period.",
                "When you cancel one, remove the item; from the next period the large number on the home screen shows how much more you have each month.",
            ],
        },
        "faq": [
            ["Does uninstalling an app cancel the subscription?",
             ["No. A subscription billed through Google Play or the App Store has to be cancelled there, or you'll keep being charged."]],
            ["Do I keep access after cancelling?",
             ["With most subscriptions, yes, until the end of the period you've paid for. Access ends after that."]],
            ["What about subscriptions I share?",
             ["Treat them the same: work out the cost per person and decide whether it's worth it for you. Shared subscriptions often keep running because nobody feels responsible."]],
        ],
    },

    {
        "id": "impulse",
        "slug": "stop-impulse-buying",
        "title": "How to stop impulse buying: 7 practical tricks that work",
        "desc": "How to stop impulse buying: the 24-hour rule, a wish list, the hours-of-work test and fewer triggers – seven practical tricks against spur-of-the-moment purchases.",
        "h1": "How to stop impulse buying: seven everyday tricks",
        "teaser": "The 24-hour rule, a wish list and the question: how many hours of work is that?",
        "answer": "**What helps most against impulse buying is time between wanting and paying.** With the 24-hour rule, anything unplanned goes on a wish list first. If it still matters the next day, you buy it. On top of that, remove triggers – no saved card details, no shop newsletters – and write down every expense right away.",
        "updated": U, "updated_label": UL,
        "related": ["nospend", "habit", "lowincome"],
        "sections": [
            ["tricks", "Seven tricks", [
                {"steps": [
                    "**The 24-hour rule.** For unplanned buys above an amount you set (say €30), wait a day. For bigger amounts, a week.",
                    "**A wish list instead of a basket.** Note what you want, with the date. Many items lose their appeal within a week without you buying anything.",
                    "**Count in hours of work.** Divide the price by your hourly take-home pay (example below).",
                    "**Don't save card details.** If you have to fetch your card for every online purchase, you buy less on a whim.",
                    "**Unsubscribe from shop newsletters and push notifications.** Discount emails create needs that weren't there before.",
                    "**Shop with a list** – and only go down the aisles you need.",
                    "**Write down every expense right away.** Having to type the amount makes you notice it.",
                ]},
            ]],
            ["hours", "The hours-of-work test", [
                {"calc": [["Price of the jacket", "€89.00"], ["÷ take-home pay per hour", "€15.00"], ["**= hours of work**", "about 6 hours"]],
                 "caption": "Example with made-up numbers"},
                "Your hourly take-home pay, roughly: monthly take-home pay divided by monthly working hours (about 173 at 40 hours a week). “Is this worth six hours of work?” sounds different from “Is €89 okay?”.",
            ]],
            ["already-bought", "Already bought it?", [
                "Check the return period straight away. For online purchases in the EU you can usually withdraw within 14 days of delivery; elsewhere, and in shops, the retailer's policy applies.",
                {"calc": [["Jacket", "€89.00"], ["÷ times worn", "30"], ["**= cost per wear**", "€2.97"]],
                 "caption": "The cost-per-use test for things you keep, made-up numbers"},
            ]],
            ["triggers", "Know your triggers", [
                "Impulse buys are rarely random. Common triggers are boredom, stress, rewarding yourself after a hard day or scrolling in the evening. If you know when you buy on impulse, you can push back right then – for example by moving shopping apps off your phone's home screen.",
                {"note": "If buying feels out of control and debt is building up, debt advice and counselling services offer free help."},
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "Adding an expense in the app is quick enough to do at the till: type the amount, tap Save. The large number **Available** drops straight away – which is often enough to make you think twice about the next one.",
                "If the bar's fill runs past the time mark, it changes colour: a hint that you're spending faster than the month is passing.",
            ],
        },
        "faq": [
            ["Is every spontaneous purchase a problem?",
             ["No. An ice cream on a hot day is fine. It's about purchases you regret soon after or that blow the monthly budget."]],
            ["From what amount should the 24-hour rule apply?",
             ["Pick an amount that fits your budget – often €20 to €50. What matters is that it's set beforehand, not negotiated in the shop."]],
            ["Does paying only in cash help?",
             ["For many people, yes, because they see the money go. That doesn't work online – there a wish list and unsaved card details help more."]],
        ],
    },

    {
        "id": "rent",
        "slug": "how-much-rent-can-i-afford",
        "title": "How much rent can I afford? Rules of thumb and the real check",
        "desc": "How much rent can you afford? The 30% and one-third rules, why utilities count, and how to check with your own take-home pay and fixed costs what's left afterwards.",
        "h1": "How much rent can I afford?",
        "teaser": "The rules of thumb, their limits and a check with your own numbers.",
        "answer": "**Common rules of thumb say housing shouldn't take more than about 30% of income** – in the US usually measured against gross income, elsewhere often as a third of take-home pay. On €2,700 take-home, a third is €900 and 30% is €810 – in both cases including heating and utilities. The more useful test is the reverse: subtract rent and all other fixed costs from your take-home pay and check whether the rest covers daily life and some savings.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "rule503020", "daily"],
        "sections": [
            ["rule", "The one-third rule", [
                {"calc": [["Take-home pay", "€2,700.00"], ["÷ 3", ""], ["**Rent incl. heating and utilities, at most**", "€900.00"]],
                 "caption": "Example with made-up numbers"},
                "Count the rent together with heating and utilities – otherwise flats with different heating systems can't be compared. Electricity is usually billed separately: leave it out of the rent figure, but include it in the fixed-costs check below.",
                "In expensive cities many households pay a much higher share. In that case the rule is a warning sign rather than a hard limit: the higher the share, the less room for everything else.",
            ]],
            ["check", "The real check: your fixed costs", [
                "More important than the percentage is what's left after all fixed costs:",
                {"calc": [["Take-home pay", "€2,700.00"], ["− Rent incl. charges", "€980.00"], ["− Electricity", "€60.00"], ["− Insurance", "€95.00"],
                          ["− Phone, internet", "€55.00"], ["− Transport pass", "€58.00"], ["− Subscriptions", "€25.00"], ["− Savings", "€200.00"],
                          ["**= Left for the month**", "€1,227.00"]],
                 "caption": "Example: rent at 36%, made-up numbers"},
                {"table": [
                    ["Take-home pay", "30%", "one third"],
                    ["€1,800", "€540", "€600"],
                    ["€2,400", "€720", "€800"],
                    ["€3,000", "€900", "€1,000"],
                    ["€3,600", "€1,080", "€1,200"],
                ]},
                "Landlords often apply the rule from the other side and ask for income of about three times the rent. Check what's usual where you live.",
                "If there's enough left for groceries, clothes, fun and a buffer, the flat can be above a third. If it's tight even without savings, it's too expensive – whatever the rule of thumb says.",
            ]],
            ["forgotten", "What people forget when moving", [
                {"list": [
                    "**Deposit:** often one to three months' rent, depending on country and landlord.",
                    "**Utility top-ups:** where heating and utilities are paid as monthly advances, they're often set too low at first, and a top-up bill follows after a year.",
                    "**Commuting:** the cheaper flat further out can cost more in tickets or fuel.",
                    "**Furnishing:** kitchen, lamps, curtains – one-off costs worth planning for.",
                ]},
            ]],
        ],
        "app": {
            "h2": "The check in Simple Household Budget",
            "body": [
                "During setup the app asks for rent, heating, electricity and utilities one item at a time – after that the large number shows what's left after all fixed costs.",
                "If you change the rent item later, the new amount applies from the next period, so the current month isn't thrown off. To compare a new flat before moving, use the check above.",
            ],
        },
        "faq": [
            ["Should I use gross or net income?",
             ["For the check, take-home pay – that's what you actually pay rent from. The US 30% rule is usually quoted on gross income, which makes it more generous than it sounds."]],
            ["Does the rule apply to couples?",
             ["Yes, based on your combined take-home pay. Also run the check in case one income stops for a while."]],
            ["What if rent already takes more than half?",
             ["Then look at your other fixed costs and at any housing support you may be entitled to. Tenant or money advice services can help you check."]],
        ],
    },

    {
        "id": "couples",
        "slug": "budgeting-for-couples",
        "title": "Budgeting for couples: how to split shared costs fairly",
        "desc": "Budgeting for couples: three account set-ups, splitting shared costs by income with a worked example, and how to keep shared spending in view without arguments.",
        "h1": "Budgeting for couples: splitting costs fairly",
        "teaser": "Three account set-ups, splitting by income and who keeps the budget.",
        "answer": "**Couples usually split shared costs in one of three ways: everything joint, everything separate, or a joint account for shared costs plus one personal account each.** If you earn different amounts, splitting by income is often fairer than 50/50: on €2,800 and €1,700 take-home, one partner pays 62% of shared costs and the other 38%.",
        "updated": U, "updated_label": UL,
        "related": ["fixed", "rent", "categories"],
        "sections": [
            ["setups", "Three account set-ups", [
                {"table": [
                    ["Set-up", "How it works", "Fits if …"],
                    ["Everything joint", "both incomes into one account, everything paid together", "you handle money similarly and trust is high"],
                    ["Everything separate", "each pays certain items, the rest is settled up", "you've only just moved in together or want to stay very independent"],
                    ["Three accounts", "joint account for rent, groceries and so on, plus one personal account each", "you want to pool shared costs but keep your own money"],
                ]},
                "One thing to know about a joint account either of you can use alone: you're usually both liable for it – including an overdraft only one of you ran up.",
                "The three-account set-up is popular because it separates two sources of conflict: what's shared is clearly settled – and what each of you does with your own money is your own business.",
            ]],
            ["split", "50/50 or by income?", [
                "50/50 is simple, but with unequal incomes one of you is left with much less. The alternative: each pays in the same **share** of their income.",
                {"calc": [["Take-home, partner A", "€2,800.00"], ["Take-home, partner B", "€1,700.00"], ["Together", "€4,500.00"], ["Shared costs", "€2,000.00"],
                          ["A's share: 2,800 ÷ 4,500 = 62.2%", "€1,244.44"], ["**B's share: 1,700 ÷ 4,500 = 37.8%**", "€755.56"]],
                 "caption": "Example with made-up numbers"},
                "That leaves €1,555.56 and €944.44 – each about 56% of their own take-home pay. With 50/50, A would keep €1,800 and B only €700.",
            ]],
            ["shared", "What counts as shared?", [
                {"list": [
                    "**Clearly shared:** rent, utilities, energy, internet, contents insurance, groceries, household items.",
                    "**Agree together:** car, holidays, eating out as a couple, presents for family.",
                    "**Usually personal:** clothes, hobbies, phone contract, own subscriptions.",
                ]},
                "Write the list down once and review it when something changes – moving, a baby, a new job.",
            ]],
            ["who", "Who keeps the budget?", [
                "A shared budget works best when it's clear who keeps it – or when each of you watches your own budget and the joint account only gets fixed amounts. Ten minutes together once a month is enough.",
            ]],
        ],
        "app": {
            "h2": "Simple Household Budget for two",
            "body": [
                "To be upfront: the app doesn't sync between two phones – there's no cloud and no server. Here's how couples can use it: each of you keeps your own budget, with your share of shared costs as a fixed item.",
                "Or one of you keeps the budget for the joint account and records shared shopping.",
            ],
        },
        "faq": [
            ["Is 50/50 unfair?",
             ["Not necessarily. With similar incomes it's the simplest solution. With big differences, the partner who earns less is often left with little room – then splitting by income is an alternative."]],
            ["How do we handle savings goals?",
             ["Shared goals like a holiday or a move can run to the joint account like a fixed cost. Personal savings goals stay in personal accounts."]],
            ["Are there budget apps that sync between two phones?",
             ["Yes, many. Syncing usually means your data is stored on the provider's servers or in a cloud account – check the privacy policy. What to look for in apps without a cloud: [budget app without bank linking](/en/guides/budget-app-without-bank-account/)."]],
        ],
    },

    {
        "id": "irregular",
        "slug": "budget-irregular-income",
        "title": "How to budget with an irregular income: a plan for freelancers",
        "desc": "Budgeting with an irregular income: pay yourself a fixed salary, keep a buffer account and set the amount from recent months – for freelancers and shift workers.",
        "h1": "How to budget with an irregular income",
        "teaser": "A fixed salary to yourself and a buffer that absorbs the swings.",
        "answer": "**With an irregular income, don't plan with whatever just came in – pay yourself a fixed “salary”.** All income goes into a buffer account first; from there you transfer the same amount to your current account every month. Set that amount between your weakest month and your average – and budget with it like a normal salary.",
        "updated": U, "updated_label": UL,
        "related": ["payday", "emergency", "daily"],
        "sections": [
            ["principle", "The principle: buffer and base salary", [
                {"steps": [
                    "**Open a buffer account**, for example an savings account you can withdraw from at any time. All income goes there.",
                    "**Set a base salary** – the amount you transfer to yourself on the same day each month.",
                    "**Budget with the base salary** as if it were a wage: subtract fixed costs, plan the rest.",
                    "**Surpluses stay in the buffer.** If it grows bigger than needed, part can go to savings goals – or a pay rise for yourself.",
                ]},
                {"note": "If you're self-employed, set aside tax and pension contributions first. The base salary is what's left for personal spending."},
            ]],
            ["size", "How big the base salary should be", [
                "Look at what was left for you personally in recent months – after setting tax aside:",
                {"table": [
                    ["Month", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"],
                    ["Income", "€1,900", "€3,400", "€2,200", "€1,600", "€2,800", "€2,100"],
                ]},
                {"calc": [["Total, six months", "€14,000.00"], ["Average", "€2,333.33"], ["Weakest month", "€1,600.00"], ["**Base salary, set cautiously**", "€1,900.00"]],
                 "caption": "Example with made-up numbers"},
                "Planning with the average is risky: two weak months in a row empty the buffer. An amount between the weakest month and the average is safer.",
                {"table": [
                    ["Month", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"],
                    ["Buffer at €1,900", "0", "1,500", "1,800", "1,500", "2,400", "2,600"],
                    ["Buffer at €2,333 (average)", "−433", "634", "501", "−232", "235", "2"],
                ]},
                "With the cautious amount the buffer never dips below its starting level and grows by €2,600 in six months. With the average it goes into the red in the first month, again in September, and ends at zero.",
            ]],
            ["buffer", "How big the buffer should be", [
                "As a starting point: two to three base salaries before you start paying yourself a fixed amount. If your work is very seasonal, more. The buffer doesn't replace the emergency fund – that's for emergencies, the buffer for normal swings: [emergency fund](/en/guides/emergency-fund-how-much/).",
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "Enter your base salary as monthly income – on the day you transfer it to yourself. You can set the start of the budget to that exact day under **Settings → Budget starts**: [budget from payday](/en/guides/budget-from-payday/).",
                "Income you want to spend right away can be added as income with the plus button in the history. If you change the base salary, the new amount applies from the next period. What stays in the buffer doesn't belong in the budget – otherwise the month looks bigger than it is.",
            ],
        },
        "faq": [
            ["What if the buffer runs dry?",
             ["Then the base salary is set too high. Lower it for the next few months and check your fixed costs until the buffer grows again."]],
            ["Does this work for shift work or zero-hours contracts?",
             ["Yes. Wherever pay varies with hours, the same principle helps: plan with a cautious base amount and set aside anything above it for weaker months."]],
            ["How often should I adjust the base salary?",
             ["About twice a year, using the last six to twelve months. Not after every good month."]],
        ],
    },

    {
        "id": "savehowmuch",
        "slug": "how-much-should-i-save",
        "title": "How much should I save each month? Rules of thumb and your number",
        "desc": "How much should you save each month? 10 to 20% as a rule of thumb, the right order of savings goals and a simple sum to find an amount you can actually keep up.",
        "h1": "How much should I save each month?",
        "teaser": "Rules of thumb, the right order and a sum for your own amount.",
        "answer": "**Common rules of thumb suggest saving 10 to 20% of take-home pay.** A realistic amount is what's left after fixed costs and an honest everyday budget – one you manage every month. Save for an emergency fund first, then for plannable big costs, then for long-term goals.",
        "updated": U, "updated_label": UL,
        "related": ["rule503020", "emergency", "leftover"],
        "sections": [
            ["rules", "What the rules of thumb say", [
                {"table": [
                    ["Take-home pay", "10%", "15%", "20% (50/30/20 rule)"],
                    ["€1,800", "€180", "€270", "€360"],
                    ["€2,200", "€220", "€330", "€440"],
                    ["€3,000", "€300", "€450", "€600"],
                ]},
                {"formula": "Savings rate = monthly savings ÷ take-home pay × 100"},
                "Both are guides for people who have enough left after fixed costs. On a small income a small fixed amount makes more sense than a percentage: [how to budget on a low income](/en/guides/budget-on-a-low-income/).",
            ]],
            ["your-number", "Find your own amount", [
                {"calc": [["Take-home pay", "€2,200.00"], ["− Fixed costs", "€1,180.00"], ["− Everyday budget (measured)", "€760.00"], ["**= Possible to save**", "€260.00"]],
                 "caption": "Example with made-up numbers, 11.8% of take-home pay"},
                "The everyday budget should be measured, not guessed: write down all spending for four weeks. Guesses are almost always too low – and then the savings disappear again at month end.",
            ]],
            ["backwards", "Work backwards from a goal", [
                "Often the reverse question helps: how much do you want, and by when?",
                {"calc": [["Savings goal", "€3,000.00"], ["÷ 18 months", "€166.67"], ["**÷ 24 months**", "€125.00"]],
                 "caption": "Example without interest, made-up numbers"},
                {"table": [
                    ["Monthly", "after 1 year", "after 5 years"],
                    ["€50", "€600", "€3,000"],
                    ["€100", "€1,200", "€6,000"],
                    ["€260", "€3,120", "€15,600"],
                ]},
                "If the amount doesn't fit your budget, stretch the time or shrink the goal – rather than squeezing your everyday spending.",
            ]],
            ["order", "The order of savings goals", [
                {"steps": [
                    "**Emergency fund** for the unexpected: [how much?](/en/guides/emergency-fund-how-much/)",
                    "**Sinking funds for the plannable:** insurance, car, December presents: [yearly bills in a monthly budget](/en/guides/yearly-expenses-monthly-budget/).",
                    "**Medium-term goals:** moving, furniture, holidays.",
                    "**Long-term:** retirement, building wealth.",
                ]},
            ]],
            ["automatic", "Save before the money is gone", [
                "Savings work best by automatic transfer the day after payday. Whatever's left at month end is a bonus on top. Saving the other way round – “whatever's left at the end” – means saving nothing in most months.",
            ]],
        ],
        "app": {
            "h2": "With Simple Household Budget",
            "body": [
                "Add your savings as a fixed item – during setup or later under **Settings → Income and fixed costs** (added later, it counts from the next period). From then on they're out of the available money on the first day of every month, and the large number only shows what you can really spend.",
                "At month end the analysis shows what's left. If you move the rest to savings, leave **Carry surplus over** switched off in the settings – otherwise the app counts money next month that's already gone.",
            ],
        },
        "faq": [
            ["Does paying off a loan count as saving?",
             ["Overpaying works much like saving, because it cuts future interest. The regular payment belongs to fixed costs."]],
            ["Should I save while I have overdraft debt?",
             ["A small emergency fund first, then clear the overdraft. An overdraft usually costs far more interest than a savings account pays."]],
            ["What if I can't save anything one month?",
             ["It happens. What matters is that the automatic transfer runs in normal months. If it fails often, the amount is set too high – smaller, but every month, is better."]],
        ],
    },

    # ------------------------------------------------------------ seniors / helpers (25 Nov 2026)
    # Search demand (autocomplete 25 Nov): "helping elderly parents with finances", "budget for elderly",
    # "budget worksheet for elderly".
    {
        "id": "seniors",
        "slug": "budget-for-elderly-parents",
        "title": "Budgeting for seniors – and helping an elderly parent with money",
        "desc": "A simple budget for seniors: pension minus fixed costs, what's left per day, and how adult children can help set it up without taking over.",
        "h1": "A simple budget for seniors – and for family members who help",
        "teaser": "Pension minus fixed costs, one number per day – and how to help a parent set it up.",
        "answer": "**One simple sum is enough: pension minus what goes out for sure.** Divide what's left by the days in the month. You only write down amounts. Family can help the first time.",
        "updated": "2026-11-25", "updated_label": "November 2026",
        "related": ["daily", "fixed", "payday"],
        "sections": [
            ["calculation", "The one calculation: income minus fixed costs", [
                {"steps": [
                    "**Add up the income:** state pension, private or workplace pension, benefits – whatever reliably arrives every month.",
                    "**Subtract the fixed costs:** rent, utilities, heating, phone, insurance, regular prescription costs, subscriptions, standing orders such as donations.",
                    "**Divide by the days:** what's left, divided by the days until the next payment, is the money per day for groceries, pharmacy, hairdresser and gifts.",
                ]},
                {"calc": [["Pension (after tax)", "1,480.00"], ["− fixed costs", "940.00"], ["= free this month", "540.00"], ["÷ 30 days", ""], ["**per day**", "18.00"]],
                 "caption": "Example with made-up numbers"},
                "You can work it out with the [daily budget calculator](/en/guides/how-much-can-i-spend-per-day/#rechner).",
            ]],
            ["payday", "Match the budget to the day the money arrives", [
                "Pensions and benefits are often paid on a fixed day that isn't the 1st, and some are paid every four weeks. If the money arrives on the 28th, a budget from the 1st to the 31st fits badly. Start the budget month on payment day instead: [budget from payday to payday](/en/guides/budget-from-payday/). If you're paid every four weeks, the date moves each month; then budget with the monthly average (13 payments ÷ 12).",
                "Divide yearly bills such as home insurance or a TV licence by twelve and plan them in monthly: [yearly expenses in a monthly budget](/en/guides/yearly-expenses-monthly-budget/).",
            ]],
            ["simple", "Keeping it simple", [
                {"list": [
                    "**Write down the amount only.** Categories are optional. If you know what's available per day, you don't need statistics.",
                    "**At the till or in the evening**, but at the same time every day. Putting receipts in a bowl and writing them down in the evening works well.",
                    "**Cash counts too.** Don't write down the withdrawal, write down what is actually spent.",
                    "**Paper is fine.** A notebook or a printed sheet is enough, such as our [printable household budget](/en/guides/printable-household-budget/). What matters is that it's within reach every day.",
                ]},
            ]],
            ["family", "For family: helping without taking over", [
                "It's often adult children or grandchildren who suggest a budget. It works best when your parent decides and stays in charge of their own money:",
                {"list": [
                    "**Set it up together once:** copy income and fixed costs from bank statements together. That's the real work. Keeping the budget afterwards is easy.",
                    "**Show only what's needed:** enter an amount and see what's left. Nothing more.",
                    "**Ask, don't check up:** look at it together once a month, if your parent wants to.",
                    "**Legal matters don't belong in the budget.** If you're going to handle a parent's banking, you need formal authority such as a power of attorney. A bank or solicitor can advise.",
                ]},
            ]],
        ],
        "app": {
            "h2": "Simple Household Budget for older users",
            "body": [
                "The home screen shows one large number: what's left this month after fixed costs. Adding an expense takes two taps: type the amount, save. If the keypad doesn't fit on the screen, for example with very large text, the app shows a **Track now** button instead – one more tap, but the keys stay large.",
                "Income and fixed costs are entered once, and family members can do that during setup. To be clear: the app has no account and no cloud. Family can't see the numbers remotely. They stay on your parent's phone. From day five at the earliest, the app shows an ad banner at the top; a one-time purchase removes it for good.",
            ],
        },
        "faq": [
            ["Do I need a computer to keep a budget?",
             ["No. A notebook, a printed sheet or an app on the phone is enough. What matters is that it's where you pay or where you sit in the evening."]],
            ["Do I have to put every expense in a category?",
             ["No. To answer \"Will the money last until the next payment?\", the amount is enough."]],
            ["How often should family look at it?",
             ["As often as your parent wants. Ten minutes once a month is enough for most."]],
        ],
    },

    # ------------------------------------------------------------ new year (25 Nov 2026)
    # Search demand: "new year budget plan", "new year budget template", "new year budgeting tips".
    {
        "id": "newyear",
        "slug": "new-year-budget-plan",
        "title": "New year budget plan: start a budget in January in 4 steps",
        "desc": "A new year budget plan in four steps: a money check-up, fixed and yearly costs, a daily budget and 30 days of writing down amounts only – so it lasts past February.",
        "h1": "New year budget plan: start fresh in 4 steps",
        "teaser": "A money check-up, yearly bills, a daily budget – and why the first 30 days need amounts only.",
        "answer": "**Four steps are enough.** Check what's in your account. Write down what goes out for sure. Work out what's left per day. Then, for 30 days, write down amounts only – nothing else.",
        "updated": "2026-11-25", "updated_label": "November 2026",
        "related": ["simple", "habit", "yearly"],
        "sections": [
            ["checkup", "Step 1: a money check-up after the holidays", [
                "After the holidays the account is often emptier than expected. Write down where things really stand: balance, unpaid bills, credit card statement, buy-now-pay-later instalments. Don't judge, just record. Next December, this is what you compare against.",
            ]],
            ["costs", "Step 2: fixed and yearly costs", [
                "List everything that leaves every month for sure: rent, utilities, phone, insurance, subscriptions. A checklist: [fixed expenses list](/en/guides/fixed-expenses-list/).",
                "January is a good month to deal with **yearly** costs, because many of them renew around now. Divide them by twelve and plan them in monthly: [yearly expenses in a monthly budget](/en/guides/yearly-expenses-monthly-budget/).",
                "While you're at it, cancel the subscriptions nobody uses: [cancel subscriptions](/en/guides/cancel-subscriptions/).",
            ]],
            ["daily", "Step 3: one number per day", [
                {"formula": "Daily budget = (income − fixed costs − savings) ÷ days in the month"},
                "This number is your compass for January. No savings amount yet? Use 0 for the first month. Work it out with the [daily budget calculator](/en/guides/how-much-can-i-spend-per-day/#rechner).",
            ]],
            ["thirty-days", "Step 4: 30 days, amounts only", [
                "Many resolutions fail not for lack of willpower but because they take too much effort. So the first month has one rule: **write down every expense with its amount, right away or the same evening.** No categories, no goals, no guilt.",
                "At the end of the month, look back once: what's left? Where did it pinch? Only then is it worth setting a savings amount or adding categories. More on sticking with it: [expense tracking tips](/en/guides/expense-tracking-tips/).",
                {"note": "If you like a challenge, start with a [no-spend challenge](/en/guides/no-spend-challenge/), but not as a permanent state."},
            ]],
        ],
        "app": {
            "h2": "Into the new year with Simple Household Budget",
            "body": [
                "Enter your income and fixed costs once, yearly ones with their due date – the app deducts them in the month they're due. After that the home screen shows what's left this month, and adding an expense takes two taps: type the amount, save.",
                "At the end of the month a **Month end** card appears under Analysis: if you like, type in your account balance. From the second month on, the app shows whether spending is missing that you didn't record. Once a year it asks: **Are income and fixed costs still right?**",
            ],
        },
        "faq": [
            ["Do I have to start on 1 January?",
             ["No. It's best to start on the day your pay arrives, so the budget month matches your money: [budget from payday to payday](/en/guides/budget-from-payday/)."]],
            ["What about the holiday spending?",
             ["It belongs to last year. The check-up shows what's still open, such as a credit card bill. Plan the outstanding amount into January as a fixed cost."]],
            ["Paper or app?",
             ["Both work. What matters is having it to hand when you pay or in the evening. For paper: [printable household budget](/en/guides/printable-household-budget/)."]],
        ],
    },
    # ------------------------------------------------------------ printable (26 Nov 2026)
    {
        "id": "printable",
        "slug": "printable-household-budget",
        "title": "Printable household budget: free PDF template",
        "desc": "A free printable household budget PDF in large print: one page for income and fixed monthly costs, then one sheet per month.",
        "h1": "Printable household budget",
        "teaser": "Large print, one page for fixed costs, one sheet per month. Free PDF.",
        "answer": "**Free to print, in large type.** The first page holds your income and fixed costs. On the month sheets you write down what you spend.",
        "updated": "2026-11-26", "updated_label": "November 2026",
        "related": ["simple", "fixed", "seniors"],
        "sections": [
            ["download", "Download", [
                {"download": ["Download PDF", "/vorlagen/my-household-budget.pdf", "A4, 13 pages, free"]},
                {"pages": [["vorlage-en-seite-1.webp", "First page: monthly income, fixed monthly costs, left to live on"],
                           ["vorlage-en-monat.webp", "Month sheet: left to live on, list with day, what for and amount, total left"]]},
            ]],
            ["how", "How it works", [
                {"steps": [
                    "**Fill in the first page once:** what comes in each month and what goes out for sure. At the bottom you see what's left to live on.",
                    "**Every month**, copy that number to the top of a month sheet.",
                    "**Write down what you spend.** At the end of the month, add it up and take it off.",
                ]},
                "If one sheet isn't enough, just print another.",
            ]],
        ],
        "app": {
            "h2": "Prefer your phone?",
            "body": [
                "Simple Household Budget for Android does the adding up for you. Enter fixed costs once, and adding an expense takes two taps: type the amount, save.",
            ],
        },
        "faq": [
            ["Does the template cost anything?",
             ["No. Print it, fill it in, done."]],
            ["Do I have to start in January?",
             ["No. Start in whichever month you like."]],
            ["What if one sheet isn't enough?",
             ["Print a second month sheet and carry on there."]],
        ],
    },
]
