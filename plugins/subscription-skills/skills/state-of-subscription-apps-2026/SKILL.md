---
name: state-of-subscription-apps-2026
description: "Answer questions from RevenueCat's State of Subscription Apps 2026 (SOSA) report: benchmarks for conversion, trials, pricing, RPI, LTV, retention, renewals, refunds, paywalls and offers by category, region, price tier, store, framework and AI vs non-AI."
---

# State of Subscription Apps 2026 (SOSA 2026) — unofficial skill

This skill holds the content and chart data of **State of Subscription Apps 2026** by RevenueCat (340-page PDF): https://www.revenuecat.com/state-of-subscription-apps

It replaces reading the report. People ask questions; you answer from the numbers below.

Use it when someone wants to benchmark download → trial, trial → paid, download → paid (D35), revenue per install (RPI), realized LTV per payer (RLTV), retention, renewal rates, refunds, reactivation, prices, plan mix, trial length, offers, paywall UI patterns, hard paywall vs freemium, App Store vs Google Play, native vs cross-platform, AI vs non-AI apps — by category (11 buckets) or region (7). Also for "what's a good trial conversion rate", "how does my app compare", "is my price too high", "should I use a hard paywall", "how long should my trial be", even without naming the report.

## How to answer

1. **Answer in the language the person writes in.** Keep metric names recognizable (trial → paid, D35 download → paid, RPI, RLTV).
2. **Numbers first, short.** Lead with the benchmark, then 2–4 supporting points. No preamble.
3. **Only use numbers from this file.** If something isn't covered (a single country, a category outside the 11 buckets, paywall-view conversion), say so and give the closest thing. Never invent a number and present it as the report's.
4. **Pick the right slice.** Benchmarks swing hugely by category × region × price tier × plan length. If the person didn't say, give the overall number and note what shifts it; ask for the missing piece only if it changes the answer a lot.
5. **Cite once per answer:** "RevenueCat, State of Subscription Apps 2026". Add the link when they want to read more.
6. **Text vs chart.** Every number in the data appendix was read from the charts. When the report's prose and its own charts or tables disagree: if the text is provably wrong (the arithmetic doesn't work, it copies another section's numbers, or it contradicts the report's own table), use the data value and say the text is in error. Otherwise give both: the text figure first, as the publisher's stated number, then the chart value, and say they differ. Don't silently pick one. See Errata.
7. **Medians, not averages.** Box charts show p10 / p25 / median / p75 / p90. In this file cells read **p25 / median / p75 / p90** unless marked "med". "Typical app" = median, "top quartile" = above p75, "top 10%" = above p90.
8. **Time frame:** target period is calendar 2025 (some renewal metrics use 2024 cohorts). Data: 115,000+ apps, $16B+ revenue, 1B+ transactions, iOS + Android + web, apps using RevenueCat. Older than Adapty's State of Paywalls 2026 (Oct 2025 – Sep 2026).

### When someone gives you their own numbers (benchmarking)

1. Identify category, region, price tier, plan length, store, and the exact metric. Watch the definitions: trial → paid here is per trial start; D35 download → paid is per install; download → trial is within 30 days of install.
2. Pull the matching cell. Category × region cells live in *Category breakouts*; otherwise use the chapter tables.
3. Place them: bottom 25% (< p25), below median, above median, top 25% (> p75), top 10% (> p90).
4. Show their number vs. the segment median and the North America median for the same category.
5. Check the rest of their setup: price vs. category median, plan mix, trial length (≤4 days converts worst), access model, store.
6. End with **one concrete lever** tied to their weakest step: low trial starts → paywall/onboarding at Day 0 (80–90% of trials start Day 0); low trial → paid → longer trial (5–9+ days), trial timeline/reminders, first-session value (55% of 3-day-trial cancels happen Day 0); weak RPI → hard paywall or annual push; weak retention → first-renewal work, annual plans; Google Play churn → billing-failure recovery (32% of Play cancels are billing errors).

### Combining with Adapty's State of Paywalls 2026

If the Adapty skill is also available, you may use both but **never merge their numbers**. Adapty measures conversion per **paywall view**; RevenueCat measures per **install** (D35) or per **trial start**. Region sets differ (RevenueCat "North America" = US + Canada; "Western Europe" = 20 named countries). Periods differ. Present them side by side, labelled.

## Methodology and definitions

- **Dataset:** apps with active subscription revenue above a minimum installs/revenue threshold, integrated with RevenueCat. Anonymized; small segments merged or omitted. Two charts (new launches, revenue by launch cohort) use Appfigures data.
- **RLTV per payer:** net realized revenue per paying user over a period (subscriptions, reactivations, upgrades, one-time purchases).
- **RPI:** total revenue ÷ total installs, at Day 14 or Day 60.
- **D35 download → paid:** share of installs with ≥1 paid subscription within 35 days.
- **Download → trial (trial start rate):** share of installs starting a free trial within 30 days (trial-using apps only).
- **Trial → paid:** share of trial starts that convert to paid.
- **Retention:** share of paid subscriptions still active after N months (subscription-level, e.g. 12 monthly renewals or 1 annual renewal).
- **Renewal rate (1st/2nd/3rd):** share of subscriptions renewing at each billing cycle.
- **Active renewal rate:** share of renewals made by subscribers seen in the app in the second half of the previous period.
- **Reactivation rate:** share of churned subscribers who resubscribe within 12 months.
- **Refund rate:** share of paid subscriptions refunded in their first billing period.
- **Price tiers:** app's average price vs. all measured apps (low / mid / high). **Access method:** freemium vs hard paywall.
- **Regions (user location):** North America (US, CA); Western Europe (UK, DE, FR, ES, IT, NL, SE, NO, FI, BE, AT, CH, DK, IE, PT, LU, LI, IS, MC, MT); Asia-Pacific (JP, KR, AU, NZ); Latin America (BR, MX, AR, CL, CO, PE); MEA (SA, ZA, AE, EG, NG, KE, TR); IN/SEA (IN, ID, TH, PH, VN, MY, SG); ROW = everything else. Chapter 1 uses **developer HQ** instead of user location.
- **Category buckets:** Utilities (incl. Weather, Reference, Finance, Tools); Health & Fitness (incl. Medical); Media & Entertainment (incl. Music, News, Sports); Education; Productivity (incl. Graphics & Design, Art & Design, Developer tools); Social & Lifestyle (incl. Dating); Gaming; Photo & Video; Business; Travel; Shopping. Note: a music-creation app would most likely sit in Media & Entertainment (Music) or Productivity — say which bucket you assume.
- **AI app:** primary value from AI/ML (gen AI, chatbots, AI photo/video, AI writing). 27.1% of apps.

## Key insights (report's headline six)

1. **The divide is accelerating.** Top 25% grew MRR 80%+ YoY; bottom 25% shrank 33%. Median +5.3%, top 10% +306%.
2. **Hard paywalls convert 5× better than freemium** (D35 10.7% vs 2.1%), but Year-1 retention is nearly identical (annual 26.8% vs 27.7%).
3. **The window is Day 0.** 55% of 3-day-trial cancellations happen on Day 0; ~50% of paid conversions happen Day 0; 80–90% of trial starts happen Day 0.
4. **Google Play's billing leak.** 32.2% of Play cancellations are billing errors vs 15.2% on the App Store.
5. **AI sells but doesn't stick.** AI apps: +41% Y1 RLTV per payer ($30.16 vs $21.37), but annual 12-month retention 21.1% vs 30.7%.
6. **Trials are getting shorter despite the data.** 17–32-day trials convert 42.5% vs 25.5% for ≤4 days, yet ≤4-day trials rose to 46.5% of trials (from 42.1%).

## Chapter 1. State of the market

- New subscription apps per month: ~2,000 (Jan 2022) → 14,700+ (Jan 2026), ~7×. iOS ~77% of new launches (from ~67% in 2023); Android ~700 → ~3,300/month.
- Revenue by app launch cohort (Jan 2026): before 2020 **69%**; 2020–21 9%; 2022–23 14%; 2024 5%; 2025+ 3%.
- Revenue is concentrated: median app makes ~$72/month one year after launch; top 10% $2,574+.
- Developer-HQ tables: Appendix A.

## Chapter 2. Store and revenue economics

- 63.5% of apps are subscriptions-only; 23.2% add lifetime; 10.7% add consumables; 2.5% all three. Gaming is the hybrid outlier (40.5% subs-only, 27.5% + consumables).
- Plan mix by category varies wildly: Gaming 82% weekly, Productivity 77% monthly, Health & Fitness 68% annual (subscriptions sold).
- **Web revenue:** 3.2% of revenue globally (4.9% NA, 0.8% IN/SEA), but 41% of top-tier apps have some web revenue vs 1.3% of hobby apps.
- **RPI:** all-category median $0.23 at D14, $0.34 at D60 (~1.5× D14→D60). Hard paywall $2.32 / $3.09 vs freemium $0.27 / $0.38 (~8–9×). Apps whose top plan is yearly lead (D14 $0.36, D60 $0.46).
- **RLTV per payer:** all-category median $14.50 at month 1, $22.86 at Year 1. High-priced apps $62.19 Y1 vs low-priced $10.69. Hard paywall $53.70 vs freemium $25.63.
- **Time to milestones:** median 58 days to $1K monthly revenue, 109 days to $10K (among apps that get there). Only 17.3% of new apps hit $1K/month within 2 years, 4.6% hit $10K, 1.7% hit $25K.

## Chapter 3. Funnel performance

- **Download → trial:** median 5.8% (top quartile 12.4%+). Business 9.1% highest; Media & Entertainment 4.0% lowest. NA 7.1% vs ~3–3.7% in emerging regions. High-priced apps 8.9% vs low-priced 4.4%.
- **Trial starts happen immediately:** 78–90% on Day 0 (Business 89.9%, H&F 82.1%, Gaming 81.5%, Education 78.5%, Productivity 78%). After Day 3, <5% in every category.
- **Trial → paid:** overall median 32.2% (2025). Travel 43.5%, H&F 37.7%, Education 36.1% lead; Photo & Video 22.2% and Gaming 25.0% lag. NA 34.2%, APAC 31.9%, WEU 29.7%, IN/SEA 15.2%.
- **Trial length matters:** ≤4 days 25.5%; 5–9 days 37.4%; 10–16 days 35.4% (very wide spread); 17–32 days 42.5%.
- **Trial cancellations front-load:** share of cancellations on Day 0 — 3-day trials 55.4%, 7-day 39.8%, 14-day 35.7%, 30-day 31.1%. 84% of 3-day and 64% of 7-day cancellations happen Day 0–1; 7-day trials show a second bump Days 3–6.
- **D35 download → paid:** overall median 2.0% (p75 4.6%, p90 9.1%). H&F 2.9%, Business 2.6%; Gaming 1.0%. NA 2.8% vs IN/SEA 0.7%. Hard paywall 10.7% (p90 38.7%) vs freemium 2.1%. High-priced 2.8%, mid 2.0%, low 1.4%.
- **Time to paid:** 50.6% of paid conversions on Day 0 overall (Productivity 71.9%, Education 28.5%); 19.2% come in Week 6+ (Travel 28.2%). MEA 63.5% on Day 0, NA 44.2%. Hard paywalls spike Days 4–7 (25.7%, 7-day trial expiries); freemium has a long tail (22.9% in Week 6+ vs 15.5% hard paywall). → Don't judge freemium cohorts on D7 ROAS.

## Chapter 4. Pricing and packaging

- **Trial strategy:** "mixed" (some plans with trial, some without) dominates: 38–59% by category (H&F 59.1%). No-trial 18–44% (Social & Lifestyle 43.6%, the only category where no-trial beats mixed). Pure trial 14–31% (Gaming 31.1%).
- **Trial lengths 2025 vs 2024:** ≤4 days 46.5% (42.1%); 5–9 days 39.9% (43.5%); 10–16 days 8.6% (8.4%); 17–32 days 5.0% (6.1%).
- **Price points (all apps, current year):** weekly most common $5, median $5.90; monthly most common $10, median $8; yearly most common $30, median $34.80 (up from $31.60); yearly p90 $90.
- **Region:** NA $6.99 / $9.99 / $39.99 (weekly/monthly/yearly); WEU highest weekly ($7.03); IN/SEA ~45–55% of NA prices.
- **Plan mix sold (all categories):** monthly 41.7%, yearly 33.6%, weekly 23.2%. Annual's share fell from 41.4% the previous year. NA is the most annual-skewed region (39.7%); MEA the most monthly (54.5%); LATAM the most weekly (29.0%).

## Chapter 5. Paywalls and offers

- **Plans shown:** 2-plan paywalls are the norm (41–60% by category; H&F 60.2%). Single-plan 20–39% (Shopping 39.4%). 3+ plans 7–25% (Travel 25.4%).
- **Durations shown on paywalls:** annual 28–44% of plans shown (H&F 43.8%), monthly 22–44%, weekly 10–33% (Photo & Video 33.2%), lifetime 4–17% (Gaming 17.4%).
- **UI elements (adoption):** highlighted pricing ~73–77% (median 74.5%); multiple plan options ~55–64%; feature list ~50–61%; free-trial messaging 44–60% (median 54%); discount badge 36–50%; cancel assurance 25–40%; testimonials 6–17%; countdown timers ≤1.4%; progress bars ≤0.2%.
- **Text density:** high-density paywalls dominate (44–61%). **Scrolling:** 58–75% of paywalls scroll (Travel 74.8%, Photo & Video 57.8%).
- **CTA copy:** "Continue" is the most common, followed by dynamic price templates ({{product.price}}), "Subscribe", "Start free trial", "Try for free", "Unlock full access", "Upgrade to premium". "Cancel anytime" sits next to the CTA. "Continue in-app" appearing = early app-to-web flows.
- **Promo offers:** only 9.3% of apps use them (H&F 14.0%, Gaming 3.6%). On iOS, among offer users: offer codes 47.6%, intro offers 41.2%, promotional 8.6%, win-back 2.5%. On Google Play: intro offers 72.9%, offer codes 27.1%, promo/win-back 0%.
- **Intro-offer reliance falls with scale:** share of new payers via intro offer — hobby tier median 23.8% (p75 64.8%, p90 94.5%), top tier median 7.0%. Exceptions: top-tier Business 70.7%, top-tier H&F 21.9%. The report's text ("~30% overall, hobby 65–99%, top performers 0–10%") describes the spread loosely; use Appendix L.
- **Intro discount depth:** median −50.1% (p75 −33.4%, p25 −78.5%). Category medians cluster at −47% to −50%, except Travel −62.7%, Shopping −80.5%, Business −83.6%.

## Chapter 6. Retention and billing health

- **12-month retention (all categories, median):** annual 27.5%, monthly 8.2%, weekly 1.2%. Previous cohort: 31.2% / 9.6% / 1.7% — retention slipped across the board.
- **6-month retention:** monthly 18.3%, weekly 3.7%.
- **Price vs retention:** low-priced apps retain annual subs best (36.1% vs 26.2% mid, 23.3% high). Access method barely matters (annual: freemium 27.7%, hard paywall 26.8%).
- **The first renewal is the cliff.** Renewal rates jump 18–30pp between the 1st and 2nd renewal. Typical 1st → 3rd renewal medians: weekly ~35–58% → ~77–81%; monthly ~42–61% → ~73–82%; annual ~23–40% → ~56–76%. YoY: annual 1st renewal fell 3.6pp; 3rd renewals flat (weekly/monthly 77–79%, annual 62.5%).
- **Region:** gaps are largest at the 1st renewal (weekly NA 50% vs IN/SEA 37%) and close by the 3rd (all within ~5–10pp).
- **Price:** 1st annual renewal low 37% vs high 24%; converges by the 3rd.
- **Refunds:** most categories 3–4.5% median (Productivity 4.7%, Business 4.5%; Travel 2.5%). NA 3.4% vs IN/SEA 7.7%; emerging regions have p90 ~33%. Low price 2.7%, mid 3.9%, high 4.5%. Freemium 2.9% vs hard paywall 2.5% (noise).
- **Why subscriptions end:** App Store 82.9% voluntary / 15.2% billing error; Google Play 66.3% / 32.2%. Price increases, developer cancels and pauses ≤0.5% each.
- **Google Play churn survey (all):** cost 36.4%, not enough usage 33.7%, found better app 9.7%, technical 7.3%, other 12.9%. Productivity is most price-driven (44.4% cost); Travel most usage-driven (46.7%).
- **Annual cancellation timing:** 34% of annual cancellations happen in month 1, then ~4–9% per month, then a month-12 bump (11%). Shopping 50% in month 1.

## Chapter 7. Reactivation

- Within 1 year of churn: monthly churners return most (all-category 20.1%), weekly 9.0%, annual 5.2%.
- Productivity monthly 36.1% (come-back-when-needed SaaS behaviour); Photo & Video monthly 20.2%; Gaming 4–8% (once gone, gone).
- Regions: monthly 18–24% (APAC 24% highest, NA 18% lowest); annual 4.9–5.9% everywhere.
- Price: high-priced monthly reactivates 28.9% vs low 15.4% / mid 12.4%; high-priced annual just 4.4%.

## Chapter 8. Segments

**Apple vs Google**
- D60 RPI median: App Store $0.42 vs Google Play $0.16 (NA $0.65 vs $0.29).
- Y1 RLTV per payer nearly converges: $23.38 vs $21.62 (Play ahead in NA $26.51 vs $25.90 and WEU $27.08 vs $26.47).
- D35 download → paid: 2.6% vs 0.9% (iOS ahead in every category).
- Trial → paid: parity, 32.0% vs 32.5% (Travel 39.7% vs 53.0% on Play).
- Revenue concentration: 66–75% of projects get >80% of revenue from the App Store.
- Prices identical in NA; diverge in emerging markets (IN/SEA yearly $21.27 iOS vs $14.64 Play).
- 1st renewals: iOS leads weekly (47.7% vs 43.3%); Play leads monthly (57.6% vs 54.1%) and annual (33.4% vs 26.1%); converge by the 3rd.

**Native vs cross-platform**
- D35 conversion: React Native 2.5%, Native 2.0%, Flutter 1.8%.
- RPI D14/D60: React Native $0.34 / $0.51; Native $0.22 / $0.31; Flutter $0.19 / $0.29.
- Y1 RLTV per payer: React Native $31.78; Native $20.88; Flutter $21.18.
- Annual retention: 27.0–30.6% for all frameworks. Within-framework spread dwarfs between-framework gaps — execution, not stack.

**AI vs non-AI**
- 27.1% of apps are AI-powered (Photo & Video 61.4%, Productivity 41.1%, Gaming 6.2%).
- Trial **start** rate 8.5% vs 5.6% (the report's summary mislabels this as trial-to-paid).
- D35 download → paid 2.4% vs 2.0%.
- RLTV per payer: M1 $18.92 vs $13.59; Y1 $30.16 vs $21.37 (+41%).
- Plan mix: AI apps 59.8% monthly / 24.0% yearly / 15.0% weekly; non-AI 26.2% / 41.8% / 30.3%.
- 12-month retention (median): annual 21.1% vs 30.7%; monthly 6.1% vs 9.5%; weekly 1.2% vs 1.7%.
- Refund rate 4.2% vs 3.5%.

## Expert takeaways worth quoting (paraphrased)

- Mojo (Michal Parizek): in Japan a long, social-proof-heavy paywall with Free vs Pro comparison beat the US layout by 20%+; in parts of LATAM, framing the yearly plan as "just $X/month" lifted trial starts 30% and yearly take rate 10% with no trial → paid hit. Same long paywall flopped in the US. Weekly paywall-on-open for free users drove 15% of new revenue. Always break test results down by geo.
- Duolingo (Anmol Tiwari): a paywall trial timeline (what happens, when you're charged, refunds) beat harder selling; letting users pick their reminder day raised conversion; cutting trial 14 → 7 days doubled experiment velocity.
- Steve P. Young: "reverse trial" after paywall dismissal (temporary premium, no card) lifted freemium conversion 0.4% → 4.5%.
- Tinder (Shawn Gong): ML-picked single best product beat showing all tiers; price à la carte features at the weekly-equivalent of the subscription.
- Lose It! (Patrick Rills): doubling yearly price $40 → $80 funded UA and allowed deeper % discounts; retest prices you ruled out.
- Yousician (Sara Grana): recheck winning tests at 3 and 6 months; refunds/chargebacks can turn a "win" negative.
- Rise Science: on web, a heavily discounted first month beats a free trial (better ad-optimization signal); web funnels should sell the problem first.
- David Vargas: intro prices on hard paywalls give ad networks cleaner signals than free trials; watch payback.
- Vahe Baghdasaryan: paid intro offers ($0.99 first month etc.) are replacing free trials; operationalize win-back, exit and second-purchase offers.
- Alice Muir Kocourková / Asya Paloni: retention breaks at commitment checkpoints, especially the 1st renewal; higher-priced annual loses more at renewal 1 (24% vs 37%) but survivors behave alike.
- Sven Jürgens: paywall type changes how fast you get paid, not who stays.

## Data appendix

Cells: **p25 / median / p75 / p90** unless marked. $ = USD.

### A. Developer-HQ benchmarks (Ch. 1)

| Dev HQ | MRR growth YoY % | Y1 RLTV/payer $ | D35 dl → paid % |
|---|---|---|---|
| Asia-Pacific | −20.4 / 12.3 / 79.3 / 244.1 | 6.88 / 16.61 / 31.48 / 61.06 | 0.5 / 1.7 / 4.3 / 10.1 |
| IN/SEA | −38.5 / 0.4 / 82.8 / 339.1 | 6.87 / 13.88 / 25.62 / 43.80 | 0.4 / 1.4 / 3.1 / 6.0 |
| Latin America | −24.3 / 17.2 / 98.8 / 322.9 | 5.89 / 14.03 / 31.59 / 58.03 | 0.6 / 1.5 / 3.6 / 6.7 |
| MEA | −53.1 / −9.7 / 73.2 / 345.2 | 8.31 / 17.00 / 32.41 / 51.88 | 0.6 / 1.9 / 4.2 / 7.4 |
| North America | −33.2 / 1.6 / 72.0 / 299.4 | 15.74 / 32.12 / 56.10 / 95.18 | 0.9 / 2.6 / 5.6 / 10.4 |
| ROW | −36.3 / 3.6 / 86.6 / 335.7 | 9.63 / 21.01 / 40.31 / 66.44 | 0.6 / 1.8 / 4.4 / 9.3 |
| Western Europe | −25.8 / 12.1 / 82.6 / 289.6 | 12.49 / 24.80 / 45.84 / 76.10 | 0.7 / 2.0 / 4.6 / 9.2 |
| All | −33.3 / 5.3 / 79.7 / 306.2 | 10.49 / 22.86 / 43.57 / 73.98 | 0.7 / 2.0 / 4.6 / 9.1 |

### B. Monetization mix, % of apps (subs only / + lifetime / + consumables / all three)

By category: Business 76.5/14.9/7.5/~1 · Education 66.7/25.0/6.8/~1.5 · Gaming 40.5/22.4/27.5/9.6 · Health & Fitness 73.5/19.5/5.6/~1 · Media & Ent. 61.5/21.3/13.9/3.2 · Photo & Video 45.3/33.0/18.7/3.0 · Productivity 59.3/28.7/9.3/~2.5 · Shopping 79.6/16.5/~3/~1 · Social & Lifestyle 58.5/18.1/20.3/3.1 · Travel 64.4/26.1/7.5/~2 · Utilities 67.0/24.3/6.5/~2 · **All 63.5/23.2/10.7/2.5**
By region: APAC 56.8/27.9/12.2/3.2 · IN/SEA 56.4/29.2/11.3/3.1 · LATAM 57.1/28.0/11.8/3.1 · MEA 57.8/27.3/11.8/3.1 · NA 61.0/25.1/11.0/2.8 · ROW 57.9/27.8/11.4/3.0 · WEU 60.3/25.4/11.4/2.9
AI apps 67.7/17.9/12.5/~2 · non-AI 61.9/25.3/10.0/2.8

### C. Plan mix and revenue share by category, % (weekly / monthly / yearly / other)

| Category | Subscriptions sold | Revenue share |
|---|---|---|
| Business | 40.6 / 35.9 / 23.3 / – | 36.3 / 38.2 / 24.2 / ~1 |
| Education | 6.8 / 29.0 / 58.9 / 5.3 | 4.2 / 30.6 / 57.9 / 7.3 |
| Gaming | 81.7 / 12.7 / 5.4 / – | 21.6 / 6.2 / ~2.7 / 69.5 |
| Health & Fitness | 4.0 / 23.8 / 68.4 / 3.8 | ~2.5 / 30.2 / 59.2 / 8.1 |
| Media & Ent. | 26.9 / 39.5 / 31.9 / ~1.7 | 15.6 / 35.5 / 33.3 / 15.7 |
| Photo & Video | 31.2 / 17.2 / 51.5 / – | 30.4 / 27.2 / 38.0 / 4.3 |
| Productivity | 10.7 / 76.7 / 12.5 / – | 3.4 / 90.7 / 4.7 / ~1 |
| Shopping | 7.9 / 26.0 / 65.6 / – | 6.5 / 45.7 / 40.3 / 7.4 |
| Social & Lifestyle | 46.6 / 30.5 / 20.3 / ~2.6 | 25.5 / 29.0 / 18.0 / 27.4 |
| Travel | 13.4 / 18.2 / 65.9 / ~2.5 | 8.0 / 11.7 / 68.6 / 11.8 |
| Utilities | 41.2 / 20.4 / 38.0 / – | 33.1 / 21.8 / 40.5 / 4.6 |
| **All** | **23.2 / 41.7 / 33.6 / ~1.5** | |

By region (sold, W/M/Y): APAC 15.9/52.0/30.6 · IN/SEA 26.2/47.7/24.2 · LATAM 29.0/40.6/29.1 · MEA 25.0/54.5/19.2 · NA 23.0/36.2/39.7 · ROW 23.2/44.7/30.8 · WEU 21.7/41.0/35.3
"Other" = lifetime/non-standard durations (Gaming's 69.5% revenue share is mostly non-subscription durations).

### D. Revenue per install (RPI), $

| Segment | D14 | D60 |
|---|---|---|
| Business | 0.10 / 0.31 / 0.78 / 1.83 | 0.19 / 0.50 / 1.25 / 2.82 |
| Education | 0.08 / 0.30 / 0.89 / 2.24 | 0.12 / 0.44 / 1.26 / 3.31 |
| Gaming | 0.02 / 0.08 / 0.23 / 0.51 | 0.03 / 0.14 / 0.38 / 0.81 |
| Health & Fitness | 0.16 / 0.48 / 1.30 / 2.93 | 0.23 / 0.66 / 1.74 / 3.93 |
| Media & Ent. | 0.04 / 0.15 / 0.45 / 1.22 | 0.06 / 0.23 / 0.65 / 1.79 |
| Photo & Video | 0.08 / 0.23 / 0.54 / 1.12 | 0.12 / 0.32 / 0.73 / 1.52 |
| Productivity | 0.07 / 0.22 / 0.54 / 1.16 | 0.11 / 0.32 / 0.78 / 1.60 |
| Shopping | 0.03 / 0.14 / 0.42 / 1.33 | 0.04 / 0.22 / 0.58 / 1.72 |
| Social & Lifestyle | 0.06 / 0.22 / 0.62 / 1.64 | 0.10 / 0.33 / 0.86 / 2.27 |
| Travel | 0.06 / 0.27 / 0.71 / 1.50 | 0.11 / 0.36 / 0.88 / 2.08 |
| Utilities | 0.05 / 0.18 / 0.51 / 1.24 | 0.08 / 0.27 / 0.77 / 1.75 |
| **All categories** | **0.07 / 0.23 / 0.65 / 1.64** | **0.10 / 0.34 / 0.93 / 2.28** |
| Asia-Pacific | 0.09 / 0.28 / 0.73 / 1.61 | 0.14 / 0.41 / 1.02 / 2.17 |
| IN/SEA | 0.02 / 0.08 / 0.23 / 0.56 | 0.03 / 0.11 / 0.31 / 0.75 |
| Latin America | 0.03 / 0.11 / 0.32 / 0.77 | 0.05 / 0.16 / 0.45 / 1.06 |
| MEA | 0.03 / 0.10 / 0.28 / 0.68 | 0.04 / 0.15 / 0.40 / 0.92 |
| North America | 0.12 / 0.38 / 0.95 / 2.09 | 0.19 / 0.55 / 1.32 / 2.80 |
| ROW | 0.03 / 0.10 / 0.28 / 0.70 | 0.04 / 0.14 / 0.40 / 0.97 |
| Western Europe | 0.08 / 0.25 / 0.64 / 1.49 | 0.12 / 0.36 / 0.89 / 2.03 |
| Low price | 0.02 / 0.08 / 0.24 / 0.55 | 0.03 / 0.11 / 0.33 / 0.74 |
| Mid price | 0.08 / 0.25 / 0.62 / 1.40 | 0.13 / 0.37 / 0.88 / 1.90 |
| High price | 0.22 / 0.61 / 1.67 / 3.71 | 0.34 / 0.94 / 2.46 / 5.34 |
| Freemium | 0.08 / 0.27 / 0.73 / 1.67 | 0.12 / 0.38 / 1.03 / 2.33 |
| Hard paywall | 0.90 / 2.32 / 4.67 / 9.78 | 1.31 / 3.09 / 5.57 / 12.59 |
| Top plan weekly | 0.07 / 0.19 / 0.44 / 0.87 | 0.12 / 0.32 / 0.71 / 1.44 |
| Top plan monthly | 0.05 / 0.18 / 0.62 / 1.82 | 0.08 / 0.29 / 0.97 / 2.79 |
| Top plan yearly | 0.11 / 0.36 / 0.97 / 2.10 | 0.15 / 0.46 / 1.20 / 2.58 |
| Top plan lifetime | 0.06 / 0.19 / 0.49 / 1.23 | 0.07 / 0.24 / 0.61 / 1.59 |

("Top plan" = the app's most-sold duration; revenue counts all the app's plans.)

### E. Realized LTV per payer, $

| Segment | Month 1 | Year 1 |
|---|---|---|
| Business | 10.30 / 18.76 / 30.76 / 57.67 | 19.74 / 35.48 / 64.09 / 123.56 |
| Education | 8.26 / 17.52 / 33.59 / 51.42 | 10.53 / 27.28 / 54.18 / 82.23 |
| Gaming | 5.06 / 8.41 / 14.31 / 23.12 | 5.57 / 11.22 / 24.15 / 40.33 |
| Health & Fitness | 13.16 / 24.23 / 39.89 / 60.90 | 18.45 / 35.64 / 62.24 / 101.87 |
| Media & Ent. | 6.69 / 12.82 / 22.23 / 36.86 | 9.67 / 21.01 / 39.75 / 70.93 |
| Photo & Video | 8.38 / 14.10 / 20.58 / 29.24 | 12.12 / 21.33 / 34.19 / 50.22 |
| Productivity | 8.05 / 14.19 / 24.12 / 35.82 | 10.92 / 22.03 / 39.39 / 63.59 |
| Shopping | 6.82 / 11.42 / 19.52 / 32.62 | 9.32 / 19.24 / 44.50 / 67.08 |
| Social & Lifestyle | 7.25 / 13.53 / 23.96 / 38.35 | 10.99 / 21.61 / 40.26 / 72.28 |
| Travel | 7.35 / 12.27 / 20.04 / 29.99 | 9.96 / 18.95 / 28.98 / 44.67 |
| Utilities | 6.25 / 12.30 / 21.90 / 34.39 | 8.82 / 19.28 / 36.95 / 61.57 |
| **All categories** | **7.54 / 14.50 / 26.23 / 43.02** | **10.49 / 22.86 / 43.57 / 73.98** |
| Asia-Pacific | 8.08 / 15.24 / 27.19 / 43.88 | 11.45 / 23.93 / 43.81 / 70.68 |
| IN/SEA | 5.72 / 10.59 / 19.57 / 33.70 | 7.53 / 15.31 / 29.47 / 50.57 |
| Latin America | 6.18 / 11.36 / 20.95 / 34.60 | 8.57 / 17.93 / 34.16 / 59.74 |
| MEA | 6.14 / 11.40 / 20.62 / 33.53 | 8.67 / 17.67 / 33.05 / 57.04 |
| North America | 9.41 / 17.02 / 28.50 / 45.28 | 12.85 / 26.07 / 46.92 / 78.17 |
| ROW | 7.15 / 13.04 / 23.55 / 38.34 | 9.64 / 19.54 / 37.55 / 60.29 |
| Western Europe | 9.97 / 17.89 / 30.98 / 49.08 | 13.22 / 26.64 / 48.28 / 78.78 |
| Low price | 3.82 / 6.67 / 10.81 / 15.51 | 6.13 / 10.69 / 17.19 / 24.12 |
| Mid price | 9.40 / 15.78 / 24.41 / 34.43 | 12.90 / 26.07 / 41.20 / 58.76 |
| High price | 23.83 / 35.89 / 56.44 / 86.01 | 36.34 / 62.19 / 95.69 / 143.31 |
| Freemium | 8.93 / 16.61 / 29.19 / 46.53 | 12.58 / 25.63 / 46.89 / 76.34 |
| Hard paywall | 17.88 / 32.05 / 52.27 / 72.52 | 30.25 / 53.70 / 88.13 / 121.79 |
| AI apps | 11.33 / 18.92 / 29.65 / 47.21 | 17.36 / 30.16 / 49.26 / 78.56 |
| Non-AI apps | 7.06 / 13.59 / 25.49 / 42.35 | 9.66 / 21.37 / 42.32 / 73.81 |

### F. New-app outcomes by category

| Category | Monthly revenue 1 yr after launch $ | Days to $1K / $2.5K / $5K / $10K (median) | % hitting $1K / $2.5K / $5K / $10K within 2 yrs |
|---|---|---|---|
| Business | 22 / 90 / 452 / 1,606 | 113 / 146 / 220 / 237 | 14.7 / 7.2 / 4.9 / 1.6 |
| Education | 17 / 77 / 412 / 2,315 | 83 / 114 / 142 / 173 | 16.2 / 9.5 / 5.9 / 3.5 |
| Gaming | 10 / 56 / 552 / 4,554 | 32 / 35 / 43 / 53 | 20.0 / 14.6 / 11.8 / 8.9 |
| Health & Fitness | 20 / 90 / 547 / 3,342 | 56 / 70 / 114 / 140 | 18.9 / 12.0 / 8.2 / 5.3 |
| Media & Ent. | 17 / 87 / 517 / 3,126 | 55 / 65 / 99 / 84 | 19.9 / 12.4 / 8.0 / 5.0 |
| Photo & Video | 25 / 124 / 614 / 3,614 | 52 / 55 / 71 / 98 | 21.4 / 14.1 / 10.3 / 7.3 |
| Productivity | 14 / 58 / 312 / 1,919 | 68 / 86 / 112 / 126 | 15.3 / 8.8 / 5.7 / 3.9 |
| Shopping | 15 / 51 / 453 / 1,250 | 59 / 238 / 296 / 122 | 15.0 / 8.7 / 5.5 / 2.4 |
| Social & Lifestyle | 15 / 60 / 378 / 2,596 | 44 / 60 / 57 / 61 | 16.3 / 10.3 / 7.2 / 4.9 |
| Travel | 11 / 40 / 155 / 822 | 88 / 136 / 139 / 119 | 10.5 / 7.2 / 4.9 / 3.4 |
| Utilities | 15 / 66 / 383 / 2,266 | 54 / 64 / 84 / 122 | 16.9 / 10.5 / 6.9 / 4.1 |
| **All** | **16 / 72 / 429 / 2,574** | **58 / 70 / 92 / 109** | **17.3 / 10.7 / 7.2 / 4.6** |

Days are medians among apps that reached each milestone, so they aren't always increasing. Web revenue presence by revenue tier: T1 hobby 1.33% · T2 6.59% · T3 14.76% · T4 28.10% · T5 top 41.40%.

### G. Funnel conversion, %

| Segment | Download → trial (D30) | Trial → paid | D35 download → paid |
|---|---|---|---|
| Business | 3.4 / 9.1 / 16.5 / 22.5 | 19.9 / 29.4 / 46.8 / 60.4 | 1.1 / 2.6 / 5.0 / 10.9 |
| Education | 2.7 / 6.5 / 11.8 / 18.9 | 24.2 / 36.1 / 50.6 / 65.7 | 0.7 / 2.2 / 5.4 / 11.6 |
| Gaming | 1.0 / 4.4 / 11.1 / 21.2 | 17.1 / 25.0 / 39.8 / 63.1 | 0.3 / 1.0 / 2.3 / 4.8 |
| Health & Fitness | 2.7 / 6.9 / 13.6 / 23.2 | 26.1 / 37.7 / 51.4 / 65.4 | 1.1 / 2.9 / 6.2 / 12.2 |
| Media & Ent. | 1.3 / 4.0 / 9.0 / 16.7 | 19.0 / 32.2 / 52.7 / 69.5 | 0.5 / 1.5 / 3.7 / 7.4 |
| Photo & Video | 2.0 / 5.2 / 9.6 / 18.2 | 14.4 / 22.2 / 33.1 / 45.3 | 0.8 / 2.1 / 4.4 / 7.9 |
| Productivity | 2.1 / 5.7 / 11.5 / 19.2 | 18.0 / 27.2 / 42.1 / 58.7 | 0.7 / 1.9 / 4.2 / 8.2 |
| Shopping | 0.8 / 4.8 / 8.7 / 11.2 | 23.4 / 33.3 / 48.4 / 58.3 | 0.3 / 1.3 / 3.6 / 6.7 |
| Social & Lifestyle | 2.1 / 6.2 / 12.1 / 20.7 | 17.0 / 28.8 / 45.1 / 59.9 | 0.7 / 2.0 / 4.5 / 8.4 |
| Travel | 2.5 / 4.1 / 9.0 / 15.3 | 30.6 / 43.5 / 62.4 / 75.7 | 0.9 / 2.2 / 5.3 / 9.7 |
| Utilities | 2.4 / 6.5 / 14.2 / 24.3 | 19.7 / 31.1 / 47.1 / 66.3 | 0.6 / 1.9 / 4.4 / 8.2 |
| **All** | **2.2 / 5.8 / 12.4 / 21.0** | **20.2 / 32.2 / 48.1 / 64.7** | **0.7 / 2.0 / 4.6 / 9.1** |
| Asia-Pacific | 1.3 / 5.7 / 13.5 / 24.2 | 21.6 / 31.9 / 45.6 / 59.7 | 0.9 / 2.4 / 5.1 / 9.5 |
| IN/SEA | 0.5 / 3.0 / 8.0 / 15.4 | 8.7 / 15.2 / 25.0 / 37.2 | 0.2 / 0.7 / 1.9 / 4.1 |
| Latin America | 0.4 / 3.7 / 9.6 / 18.2 | 14.7 / 23.5 / 36.0 / 50.0 | 0.3 / 1.0 / 2.6 / 5.2 |
| MEA | 0.7 / 3.6 / 9.6 / 17.4 | 11.8 / 19.5 / 31.1 / 45.1 | 0.3 / 0.9 / 2.4 / 5.0 |
| North America | 2.5 / 7.1 / 15.0 / 24.7 | 23.2 / 34.2 / 47.9 / 62.5 | 1.0 / 2.8 / 6.0 / 10.9 |
| ROW | 0.8 / 3.2 / 7.7 / 14.3 | 13.7 / 22.0 / 33.9 / 48.6 | 0.2 / 0.9 / 2.2 / 4.6 |
| Western Europe | 1.7 / 5.0 / 11.0 / 19.4 | 19.0 / 29.7 / 45.8 / 62.5 | 0.7 / 1.8 / 4.0 / 7.9 |
| Low price | 1.6 / 4.4 / 10.3 / 18.0 | | 0.4 / 1.4 / 3.7 / 7.7 |
| Mid price | 2.1 / 5.4 / 11.6 / 19.3 | | 0.7 / 2.0 / 4.4 / 8.1 |
| High price | 3.4 / 8.9 / 16.5 / 27.0 | | 1.0 / 2.8 / 6.1 / 13.5 |
| Freemium | | | 0.8 / 2.1 / 4.5 / 8.2 |
| Hard paywall | | | 6.5 / 10.7 / 20.0 / 38.7 |
| AI apps | 3.8 / 8.5 / 14.8 / 22.9 | | 1.1 / 2.4 / 4.8 / 8.3 |
| Non-AI apps | 2.1 / 5.6 / 12.0 / 20.9 | | 0.7 / 2.0 / 4.7 / 9.8 |
| React Native | | | 0.9 / 2.5 / 5.7 / 11.5 |
| Native | | | 0.7 / 2.0 / 4.4 / 8.3 |
| Flutter | | | 0.6 / 1.8 / 4.3 / 8.6 |

Trial → paid by trial length: ≤4 days 16.5 / 25.5 / 38.5 / 56.2 · 5–9 days 24.8 / 37.4 / 52.8 / 67.1 · 10–16 days 0.3 / 35.4 / 52.8 / 69.5 · 17–32 days 26.8 / 42.5 / 59.4 / 72.8.

### H. Timing

- Time to paid, share of conversions (freemium / hard paywall): Day 0 36.5 / 32.2 · Days 1–3 12.8 / 11.8 · Days 4–7 15.4 / 25.7 · Week 2 6.3 / 9.3 · Week 3 2.5 / 2.3 · Week 4 1.7 / 1.3 · Week 5 1.9 / 2.0 · Week 6+ 22.9 / 15.5.
- Day 0 share of paid conversions: overall 50.6%; Productivity 71.9%; Education 28.5%. Week 6+: overall 19.2%; Travel 28.2%; Media & Ent. and Social ~24–25%. By region Day 0: MEA 63.5%, NA 44.2% (NA Days 4–7 15.6%; WEU Week 6+ 21.2%).
- Trial cancellations on Day 0 (share of all cancellations of that trial length): 3-day 55.4% · 7-day 39.8% · 14-day 35.7% · 30-day 31.1%. Day 1 roughly 29% / 23% / 17% / 15%.

### I. Trial strategy and length by category, %

| Category | Mixed / No trial / Pure trial | Trial length ≤4d / 5–9d / 10–16d / 17–32d |
|---|---|---|
| Business | 45.3 / 31.8 / 22.9 | 54.1 / 30.6 / 8.6 / 6.7 |
| Education | 48.3 / 30.6 / 21.2 | 39.1 / 50.3 / 7.5 / 3.2 |
| Gaming | 38.4 / 30.4 / 31.1 | 73.3 / 23.8 / ~2.9 / ~0 |
| Health & Fitness | 59.1 / 18.3 / 22.6 | 29.0 / 54.0 / 12.1 / 4.9 |
| Media & Ent. | 42.6 / 37.2 / 20.2 | 45.3 / 38.9 / 9.0 / 6.8 |
| Photo & Video | 47.6 / 38.1 / 14.4 | 68.2 / 24.7 / 4.7 / ~2.4 |
| Productivity | 52.9 / 28.8 / 18.3 | 54.5 / 33.6 / 8.2 / 3.6 |
| Shopping | 46.5 / 36.8 / 16.7 | 39.7 / 34.5 / 15.5 / 10.3 |
| Social & Lifestyle | 39.6 / 43.6 / 16.8 | 52.1 / 34.8 / 7.3 / 5.9 |
| Travel | 41.6 / 29.8 / 28.6 | 32.9 / 54.3 / 7.8 / 4.9 |
| Utilities | 46.3 / 29.7 / 24.1 | 51.1 / 33.8 / 8.6 / 6.6 |

### J. Prices, $

All apps, previous → current year (most common / p25 / median / p75 / p90): weekly 5.0/3.4/5.0/8.0/10.0 → 5.0/4.0/5.9/8.1/10.0 · monthly 10.0/3.5/7.0/12.5/20.0 → 10.0/3.9/8.0/13.5/22.7 · yearly 30.0/17.7/31.6/58.9/91.6 → 30.0/20.0/34.8/58.1/90.0

By category (p25 / median / p75 / p90; from category breakouts):

| Category | Weekly | Monthly | Yearly |
|---|---|---|---|
| Business | 4.75 / 6.89 / 9.99 / 12.08 | 4.18 / 8.99 / 17.99 / 35.58 | 20.74 / 39.99 / 71.99 / 99.99 |
| Education | 3.99 / 6.26 / 7.99 / 9.99 | 4.99 / 9.99 / 16.99 / 24.99 | 24.99 / 44.99 / 79.99 / 116.95 |
| Gaming | 3.99 / 5.81 / 8.99 / 9.99 | 2.99 / 4.99 / 9.99 / 14.99 | 11.71 / 24.99 / 39.99 / 59.99 |
| Health & Fitness | 3.11 / 4.99 / 6.99 / 8.49 | 4.99 / 9.99 / 14.99 / 21.10 | 23.90 / 39.94 / 59.99 / 95.08 |
| Media & Ent. | 3.84 / 5.84 / 8.72 / 10.86 | 3.06 / 5.99 / 11.71 / 19.99 | 17.99 / 34.99 / 59.99 / 94.99 |
| Photo & Video | 3.99 / 5.60 / 7.99 / 9.99 | 3.99 / 6.99 / 11.99 / 20.00 | 19.99 / 31.01 / 49.99 / 69.99 |
| Productivity | 4.04 / 5.99 / 7.99 / 9.99 | 3.99 / 7.99 / 13.75 / 21.07 | 17.99 / 29.99 / 50.27 / 89.99 |
| Shopping | 3.86 / 5.17 / 7.00 / 9.28 | 3.22 / 5.84 / 9.99 / 14.99 | 10.45 / 26.69 / 40.48 / 68.30 |
| Social & Lifestyle | 3.99 / 5.99 / 9.72 / 14.99 | 4.78 / 9.99 / 19.99 / 29.99 | 17.99 / 29.99 / 49.99 / 79.99 |
| Travel | 3.99 / 4.99 / 5.39 / 8.54 | 2.99 / 4.99 / 8.00 / 9.99 | 11.60 / 20.00 / 34.99 / 59.99 |
| Utilities | 3.99 / 5.65 / 7.99 / 9.99 | 2.76 / 5.00 / 9.99 / 14.99 | 15.14 / 29.99 / 46.61 / 69.99 |

Median by region and store (weekly / monthly / yearly; App Store | Google Play):

| Region | App Store | Google Play |
|---|---|---|
| Asia-Pacific | 6.48 / 6.69 / 34.72 | 6.52 / 7.48 / 35.74 |
| IN/SEA | 5.08 / 4.61 / 21.27 | 3.88 / 3.12 / 14.64 |
| Latin America | 4.99 / 5.50 / 24.99 | 4.68 / 4.65 / 19.99 |
| MEA | 5.33 / 6.97 / 27.22 | 4.79 / 4.85 / 18.85 |
| North America | 6.99 / 9.99 / 39.99 | 6.99 / 9.99 / 39.99 |
| ROW | 4.99 / 5.85 / 26.15 | 4.99 / 5.99 / 26.75 |
| Western Europe | 7.03 / 9.41 / 40.12 | 6.97 / 9.36 / 36.10 |

### K. Paywall design by category (RevenueCat Paywalls data), %

| Category | Plans shown 1 / 2 / 3+ | Durations shown W / M / Y / Lifetime | Scrolling | Text density low / med / high |
|---|---|---|---|---|
| Business | 33.4 / 44.7 / 21.9 | 25.7 / 33.1 / 35.8 / 5.3 | 65.2 | 15.2 / 24.7 / 60.1 |
| Education | 22.1 / 54.8 / 23.1 | 18.1 / 35.5 / 38.6 / 7.8 | 70.6 | 18.9 / 32.5 / 48.6 |
| Gaming | 37.5 / 41.7 / 20.8 | 27.5 / 26.7 / 28.4 / 17.4 | 60.4 | 16.2 / 22.4 / 61.4 |
| Health & Fitness | 20.4 / 60.2 / 19.4 | 10.9 / 37.6 / 43.8 / 7.7 | 68.6 | 23.5 / 30.1 / 46.4 |
| Media & Ent. | 30.0 / 50.9 / 19.2 | 21.0 / 33.5 / 35.4 / 10.0 | 61.8 | 23.5 / 23.9 / 52.6 |
| Photo & Video | 31.3 / 51.3 / 17.4 | 33.2 / 21.6 / 34.1 / 11.1 | 57.8 | 29.3 / 20.5 / 50.2 |
| Productivity | 23.4 / 56.2 / 20.4 | 23.0 / 28.5 / 39.2 / 9.3 | 68.8 | 25.7 / 25.7 / 48.5 |
| Shopping | 39.4 / 53.8 / 6.7 | 17.1 / 44.3 / 34.2 / 4.4 | 66.3 | 21.2 / 34.6 / 44.2 |
| Social & Lifestyle | 29.3 / 49.4 / 21.3 | 22.4 / 36.0 / 34.3 / 7.4 | 67.2 | 26.5 / 26.0 / 47.5 |
| Travel | 28.9 / 45.6 / 25.4 | 10.1 / 37.4 / 40.4 / 12.1 | 74.8 | 25.6 / 26.6 / 47.8 |
| Utilities | 33.8 / 47.6 / 18.5 | 23.5 / 29.1 / 35.8 / 11.6 | 65.2 | 19.3 / 25.2 / 55.5 |

UI element adoption % (highlighted pricing / multiple plans / feature list / free-trial messaging / discount badge / cancel assurance / testimonials / countdown / progress bar):
Business 76.6/58.5/61.4/60.0/41.5/33.8/10.2/0.5/0.0 · Education 74.5/63.2/57.1/58.9/47.5/39.5/15.4/1.4/0.1 · Gaming 75.9/54.7/60.3/54.7/40.2/36.7/12.2/0.3/0.0 · H&F 75.3/64.0/55.1/58.9/50.4/39.1/12.7/1.2/0.2 · Media 73.4/58.6/57.6/54.0/42.3/34.9/9.2/1.0/0.1 · Photo & Video 72.6/60.0/51.8/45.5/44.7/25.0/5.9/0.9/0.0 · Productivity 77.0/64.2/57.0/53.2/48.2/35.9/11.0/0.9/0.2 · Shopping 73.8/54.6/50.0/46.9/36.2/38.5/16.9/0.0/0.0 · Social 76.5/61.6/57.2/51.6/45.8/36.1/11.3/0.7/0.2 · Travel 74.3/59.2/56.4/43.6/42.5/33.1/15.3/0.7/0.2 · Utilities 72.6/55.2/56.2/57.9/40.4/33.2/10.0/0.8/0.2

### L. Offers

- Apps using promo offers %: Business 8.6 · Education 8.1 · Gaming 3.6 · H&F 14.0 · Media 9.6 · Photo & Video 8.0 · Productivity 8.8 · Shopping 6.7 · Social 8.2 · Travel 9.7 · Utilities 9.1 · **All 9.3**.
- Intro discount depth, median: Business −83.6 · Education −47.1 · Gaming −47.0 · H&F −48.3 · Media −50.1 · Photo & Video −50.0 · Productivity −50.1 · Shopping −80.5 · Social −50.0 · Travel −62.7 · Utilities −50.4 · **All −50.1** (p25 −78.5, p75 −33.4, p90 −20.0).
- Share of new payers acquired via an intro offer, by revenue tier T1 hobby / T2 early traction / T3 indie business / T4 scaling / T5 top-performing. All categories (p25 / median / p75 / p90): T1 7.0/23.8/64.8/94.5 · T2 3.3/13.9/47.9/86.2 · T3 2.0/9.3/29.7/67.9 · T4 1.5/9.1/30.7/66.1 · T5 0.7/7.0/31.9/65.5. Medians by category (T1/T2/T3/T4/T5): Business 36.4/12.1/2.5/8.1/70.7 · Education 16.8/21.9/17.9/13.1/6.9 · Gaming 55.7/14.0/3.0/3.5/n/a · H&F 18.5/11.2/8.9/8.9/21.9 · Media 27.5/13.9/21.7/11.1/7.5 · Photo & Video 39.2/14.2/4.8/2.6/6.6 · Productivity 27.9/14.4/4.2/10.2/2.8 · Shopping 36.4/88.7/~1/n/a/n/a · Social 27.3/18.0/11.7/15.6/5.2 · Travel 26.1/13.8/8.4/3.1/n/a · Utilities 25.0/8.5/7.6/7.1/4.6. Reliance generally falls with scale, but not monotonically (Business and H&F top tiers lean on intro offers heavily).

### M. Retention, % of subscriptions still active

12 months (monthly | weekly | annual):

| Segment | Monthly | Weekly | Annual |
|---|---|---|---|
| Business | 5.7 / 14.2 / 24.9 / 34.0 | 0.4 / 1.8 / 4.1 / 8.1 | 20.7 / 39.9 / 52.9 / 62.6 |
| Education | 3.6 / 6.3 / 11.1 / 17.9 | 0.5 / 1.6 / 2.7 / 4.6 | 17.3 / 23.5 / 31.6 / 41.2 |
| Gaming | 2.4 / 6.6 / 13.9 / 29.3 | 0.8 / 1.3 / 2.6 / 5.0 | 14.7 / 25.3 / 45.1 / 59.6 |
| Health & Fitness | 4.4 / 8.5 / 14.7 / 25.7 | 0.9 / 2.2 / 3.8 / 9.6 | 15.4 / 24.4 / 37.0 / 52.2 |
| Media & Ent. | 4.1 / 10.5 / 22.8 / 36.0 | 0.2 / 1.0 / 2.3 / 4.3 | 19.7 / 36.0 / 55.1 / 68.5 |
| Photo & Video | 4.2 / 8.2 / 14.2 / 22.1 | 0.6 / 1.6 / 3.2 / 6.1 | 14.6 / 23.3 / 34.7 / 44.7 |
| Productivity | 4.5 / 8.8 / 16.5 / 30.0 | 0.5 / 1.4 / 2.7 / 4.3 | 13.7 / 22.9 / 37.6 / 52.6 |
| Shopping | 2.7 / 6.8 / 19.0 / 24.2 | 0.7 / 2.1 / 4.4 / 7.7 | 16.2 / 30.2 / 50.2 / 62.4 |
| Social & Lifestyle | 1.2 / 3.9 / 11.5 / 21.3 | 0.0 / 0.5 / 1.2 / 3.2 | 13.1 / 24.7 / 40.1 / 56.4 |
| Travel | 4.3 / 9.0 / 16.8 / 34.3 | 1.5 / 2.0 / 4.8 / 6.4 | 26.8 / 38.6 / 58.5 / 71.4 |
| Utilities | 4.4 / 10.3 / 20.2 / 34.5 | 0.2 / 1.3 / 3.2 / 6.3 | 20.1 / 34.2 / 51.4 / 67.6 |
| **All** | **3.6 / 8.2 / 16.4 / 29.9** | **0.3 / 1.2 / 2.7 / 5.3** | **16.8 / 27.5 / 42.7 / 59.6** |
| Previous cohort (all) | 4.3 / 9.6 / 19.2 / 33.4 | 0.6 / 1.7 / 3.6 / 6.9 | 18.8 / 31.2 / 48.2 / 65.1 |
| Low price | 4.6 / 10.8 / 21.8 / 36.0 | 0.4 / 1.3 / 2.7 / 6.0 | 20.7 / 36.1 / 53.2 / 67.9 |
| Mid price | 3.6 / 8.4 / 16.4 / 29.5 | 0.3 / 1.2 / 2.8 / 5.3 | 16.1 / 26.2 / 40.7 / 57.3 |
| High price | 2.6 / 6.1 / 11.4 / 20.0 | 0.2 / 1.0 / 2.4 / 4.6 | 14.5 / 23.3 / 34.3 / 48.5 |
| Freemium | 3.7 / 8.3 / 16.3 / 28.9 | 0.5 / 1.3 / 2.9 / 5.6 | 17.3 / 27.7 / 42.4 / 58.1 |
| Hard paywall | 4.8 / 9.2 / 15.9 / 25.3 | 0.7 / 1.2 / 2.2 / 7.8 | 17.4 / 26.8 / 40.0 / 54.4 |
| AI apps | 3.3 / 6.1 / 11.8 / 20.3 | 0.6 / 1.2 / 2.5 / 4.2 | 13.8 / 21.1 / 31.5 / 44.5 |
| Non-AI apps | 4.7 / 9.5 / 18.5 / 32.4 | 0.7 / 1.7 / 3.4 / 6.6 | 19.3 / 30.7 / 46.5 / 62.6 |
| Native | 4.2 / 8.8 / 17.2 / 29.6 | 0.5 / 1.5 / 3.2 / 6.2 | 16.5 / 27.0 / 41.5 / 58.2 |
| Flutter | 3.3 / 7.4 / 16.1 / 30.4 | 0.1 / 0.8 / 1.8 / 3.6 | 16.5 / 27.8 / 45.1 / 62.4 |
| React Native | 3.1 / 7.4 / 15.2 / 26.8 | 0.2 / 0.8 / 1.8 / 3.5 | 17.3 / 27.1 / 43.6 / 59.0 |

6 months (monthly | weekly): Business 14.4/26.3/40.1/50.4 | 1.7/5.0/9.4/15.8 · Education 10.2/15.5/24.3/33.6 | 2.6/5.0/7.1/10.8 · Gaming 7.7/14.7/26.1/45.3 | 2.7/3.8/6.4/10.7 · H&F 11.8/19.5/29.1/42.6 | 2.7/6.1/9.0/17.7 · Media 11.1/22.0/37.2/52.4 | 1.2/3.3/6.0/10.1 · Photo & Video 10.5/17.0/26.1/35.8 | 2.2/4.2/8.0/13.5 · Productivity 11.1/18.7/29.7/45.3 | 2.2/4.0/6.9/10.2 · Shopping 8.9/12.2/30.9/40.7 | 3.4/6.2/10.1/13.0 · Social 3.7/10.9/23.9/38.7 | 0.9/1.9/3.9/8.3 · Travel 11.1/16.6/29.1/51.1 | 3.1/4.8/7.8/13.6 · Utilities 11.2/20.7/34.2/50.5 | 1.5/4.2/8.2/13.4 · **All 10.0/18.3/30.2/45.7 | 1.6/3.7/7.0/12.0**

### N. Renewal rates, median % (1st / 2nd / 3rd renewal)

| Category | Weekly | Monthly | Annual | Active renewal W / M / Y |
|---|---|---|---|---|
| Business | 52.2 / 72.4 / 80.5 | 61.4 / 77.2 / 82.1 | 40.0 / 61.9 / 68.6 | 16.6 / 48.5 / 82.1 |
| Education | 57.8 / 72.7 / 80.0 | 56.2 / 68.5 / 75.0 | 23.7 / 43.8 / 55.7 | 18.1 / 40.4 / 76.9 |
| Gaming | 50.5 / 71.4 / 78.8 | 53.1 / 71.8 / 77.3 | 25.6 / 55.6 / 63.2 | 13.5 / 44.5 / 78.1 |
| Health & Fitness | 54.2 / 74.6 / 81.2 | 57.3 / 72.2 / 77.5 | 24.6 / 47.4 / 60.3 | 23.9 / 61.9 / 86.4 |
| Media & Ent. | 45.4 / 70.5 / 78.7 | 57.8 / 74.5 / 79.7 | 37.1 / 59.0 / 69.1 | 20.4 / 58.3 / 84.8 |
| Photo & Video | 37.6 / 71.4 / 80.5 | 47.8 / 71.1 / 78.1 | 23.2 / 51.0 / 61.8 | 21.8 / 60.7 / 84.4 |
| Productivity | 44.8 / 72.9 / 80.5 | 53.6 / 72.7 / 78.8 | 23.1 / 50.0 / 64.5 | 14.4 / 28.2 / 85.6 |
| Shopping | 50.7 / 71.3 / 78.3 | 57.7 / 75.8 / 81.0 | 29.8 / 64.8 / 72.7 | – |
| Social & Lifestyle | 35.4 / 67.1 / 76.6 | 42.1 / 64.8 / 73.3 | 25.2 / 50.0 / 62.4 | 27.9 / 66.1 / 76.9 |
| Travel | 47.8 / 68.9 / 78.7 | 53.3 / 69.1 / 78.0 | 39.9 / 63.7 / 76.1 | 26.9 / 41.2 / 81.2 |
| Utilities | 48.5 / 73.5 / 81.0 | 57.2 / 74.5 / 80.4 | 34.9 / 60.0 / 69.9 | 13.3 / 57.5 / 82.5 |
| All (active) | | | | 18.7 / 39.2 / 83.4 |

By region (weekly | monthly | annual): APAC 49/74/82 | 57/74/80 | 26/52/63 · IN/SEA 37/63/74 | 46/64/74 | 22/43/56 · LATAM 44/70/78 | 54/70/77 | 24/46/60 · MEA 41/69/78 | 49/67/75 | 24/48/62 · NA 50/74/81 | 55/72/78 | 26/51/64 · ROW 43/68/77 | 51/69/76 | 22/47/59 · WEU 42/71/79 | 55/72/78 | 28/53/65
By price, 1st renewal W/M/Y: low 51/60/37 · mid 46/55/27 · high 45/51/24 (3rd renewals converge 68–81%).
By store (App Store | Google Play): weekly 47.7/72.7/80.6 | 43.3/66.3/75.5 · monthly 54.1/72.0/78.0 | 57.6/71.4/77.6 · annual 26.1/51.8/63.9 | 33.4/52.4/63.4

### O. Refunds, % of paid subscriptions refunded in first period

By category: Business 2.1/4.5/9.8/17.7 · Education 2.0/4.3/8.1/15.2 · Gaming 1.6/3.0/5.1/10.1 · H&F 2.0/3.9/7.4/13.5 · Media 1.6/3.3/7.2/13.7 · Photo & Video 2.3/4.2/8.4/17.6 · Productivity 2.4/4.7/9.4/17.2 · Shopping 2.0/3.1/5.6/8.9 · Social 1.8/3.4/6.8/13.0 · Travel 1.1/2.5/5.5/9.1 · Utilities 1.9/3.7/7.6/14.9
By region: APAC 2.3/5.2/12.5/33.3 · IN/SEA 3.4/7.7/16.7/34.7 · LATAM 2.9/6.1/14.3/33.3 · MEA 2.6/5.6/13.5/33.3 · NA 1.7/3.4/7.1/14.2 · ROW 2.8/6.2/13.3/28.5 · WEU 2.0/4.1/8.7/18.8
By price: low 1.3/2.7/5.8/11.5 · mid 1.9/3.9/8.0/15.0 · high 2.4/4.5/8.6/16.0. Access: freemium 1.5/2.9/5.3/8.9 · hard paywall 1.3/2.5/5.6/9.4. AI 2.2/4.2/8.6/15.8 · non-AI 1.7/3.5/6.9/12.5.

### P. Churn reasons and timing

Google Play churn survey % (cost / not enough usage / found better app / technical / other): Business 28.3/38.5/12.8/7.7/12.7 · Education 36.5/39.5/8.6/3.8/11.5 · Gaming 35.7/35.6/10.1/6.2/12.4 · H&F 38.7/40.4/7.7/3.1/10.1 · Media 36.7/34.4/9.5/6.5/12.9 · Photo & Video 33.4/37.4/11.9/6.6/10.6 · Productivity 44.4/26.4/9.5/7.0/12.7 · Shopping 31.1/36.2/9.7/9.2/13.8 · Social 31.2/34.3/9.3/8.6/16.5 · Travel 24.4/46.7/10.6/6.5/11.9 · Utilities 28.4/33.1/11.2/12.4/14.8 · **All 36.4/33.7/9.7/7.3/12.9**
Annual-subscription cancellations by month of first year (all): M1 34.2 · M2 8.9 · M3 7.1 · M4 6.1 · M5 5.4 · M6 5.0 · M7 4.6 · M8 4.4 · M9 4.3 · M10 4.4 · M11 4.7 · M12 11.1. Month-1 share by category: Business 32.0 · Education 30.5 · Gaming 37.5 · H&F 33.8 · Media 34.5 · Photo & Video 38.3 · Productivity 34.0 · Shopping 50.0 · Social 33.8 · Travel 38.5 · Utilities 35.3.

### Q. Reactivation within 1 year of churn, % (weekly / monthly / annual)

Business 7.9/10.3/5.6 · Education 9.1/10.8/3.6 · Gaming 7.7/6.4/4.2 · H&F 8.1/12.4/4.8 · Media 11.8/15.8/7.0 · Photo & Video 11.5/20.2/8.4 · Productivity 6.6/36.1/4.8 · Shopping 15.7/8.7/2.9 · Social 10.2/13.9/4.5 · Travel 3.4/9.4/8.1 · Utilities 6.4/10.5/5.1 · **All 9.0/20.1/5.2**. By price (W/M/Y): low ~8/15.4/~6 · mid ~8/12.4/~5.6 · high ~9/28.9/4.4.

### R. App Store vs Google Play (medians, App Store | Google Play)

| Category | Trial → paid % | D35 download → paid % |
|---|---|---|
| Business | 28.6 / 33.5 | 3.0 / 1.3 |
| Education | 36.3 / 35.1 | 3.1 / 0.9 |
| Gaming | 27.3 / 20.5 | 1.3 / 0.4 |
| Health & Fitness | 38.2 / 35.7 | 3.5 / 1.6 |
| Media & Ent. | 31.6 / 34.9 | 2.1 / 0.7 |
| Photo & Video | 22.7 / 17.1 | 2.6 / 0.4 |
| Productivity | 26.9 / 29.6 | 2.5 / 0.6 |
| Shopping | 31.6 / 39.5 | 1.7 / 0.7 |
| Social & Lifestyle | 28.7 / 29.1 | 2.5 / 1.2 |
| Travel | 39.7 / 53.0 | 2.4 / 1.8 |
| Utilities | 30.5 / 32.4 | 2.4 / 1.0 |
| **All** | **32.0 / 32.5** | **2.6 / 0.9** |

| Region | D60 RPI $ | Y1 RLTV/payer $ | % of projects >80% iOS revenue |
|---|---|---|---|
| Asia-Pacific | 0.46 / 0.29 | 24.19 / 23.38 | 71.6 |
| IN/SEA | 0.15 / 0.04 | 17.46 / 11.52 | 66.4 |
| Latin America | 0.24 / 0.06 | 20.51 / 13.37 | 66.2 |
| MEA | 0.21 / 0.06 | 20.15 / 13.28 | 70.3 |
| North America | 0.65 / 0.29 | 25.90 / 26.51 | 75.1 |
| ROW | 0.19 / 0.06 | 19.66 / 19.32 | 69.1 |
| Western Europe | 0.41 / 0.23 | 26.47 / 27.08 | 69.1 |
| **All** | **0.42 / 0.16** | **23.38 / 21.62** | |

### S. Frameworks

RPI D14 / D60 ($, p25/med/p75/p90): Native 0.07/0.22/0.55/1.27 | 0.10/0.31/0.78/1.71 · Flutter 0.05/0.19/0.59/1.59 | 0.08/0.29/0.88/2.28 · React Native 0.10/0.34/1.04/2.58 | 0.16/0.51/1.50/3.60 · Other 0.04/0.19/0.65/1.57 | 0.06/0.28/0.92/2.21
Y1 RLTV per payer: Native 10.14/20.88/38.26/61.81 · Flutter 9.66/21.18/40.43/74.68 · React Native 15.13/31.78/58.23/95.32 · Other 7.94/20.32/43.47/71.73

### T. AI share of apps by category, %

Business 19.1 · Education 25.6 · Gaming 6.2 · H&F 23.7 · Media 23.1 · Photo & Video 61.4 · Productivity 41.1 · Shopping 22.0 · Social 25.6 · Travel 12.3 · Utilities 23.1 · **All 27.1**

## Category breakouts (category × user region)

Regions in this order: **APAC / IN-SEA / LATAM / MEA / NA / ROW / WEU**. Values are **medians** unless noted. Plan mix = share of subscriptions sold (weekly/monthly/yearly). Time-to-paid by region is at the end of this section.

| Category | Plan mix W/M/Y by region | Trial start % | Trial → paid % | D35 dl → paid % |
|---|---|---|---|---|
| Business | 39/36/24 · 57/23/19 · 36/40/23 · 51/32/17 · 39/35/26 · 44/33/22 · 37/43/21 | 8.4 · 3.9 · 6.4 · 5.4 · 12.3 · 3.8 · 6.6 | 32.8 · 15.4 · 21.9 · 21.0 · 33.9 · 25.2 · 23.9 | 3.0 · 0.9 · 1.5 · 1.4 · 3.5 · 1.0 · 2.1 |
| Education | 3/21/74 · 7/30/60 · 5/31/54 · 6/26/57 · 8/32/57 · 8/26/58 · 6/29/58 | 5.8 · 2.9 · 3.7 · 3.1 · 7.2 · 3.0 · 5.1 | 33.3 · 18.3 · 27.6 · 24.9 · 37.6 · 26.6 · 34.9 | 2.0 · 0.7 · 0.9 · 0.9 · 2.7 · 0.8 · 1.8 |
| Gaming | 77/17/6 · 88/7/5 · 89/6/4 · 79/16/5 · 76/17/6 · 89/7/4 · 88/7/5 | 5.1 · 3.1 · 3.0 · 2.8 · 5.6 · 2.5 · 4.2 | 27.5 · 13.9 · 17.7 · 17.2 · 28.6 · 15.4 · 20.0 | 1.2 · 0.3 · 0.5 · 0.5 · 1.5 · 0.5 · 0.9 |
| Health & Fitness | 4/29/63 · 7/21/70 · 5/27/64 · 6/27/64 · 4/23/70 · 3/23/72 · 3/25/66 | 6.7 · 3.3 · 4.1 · 4.5 · 7.5 · 4.1 · 6.2 | 36.8 · 18.7 · 29.4 · 24.2 · 39.7 · 25.7 · 35.0 | 3.4 · 1.0 · 1.5 · 1.4 · 3.6 · 1.3 · 2.6 |
| Media & Ent. | 28/36/36 · 25/33/25 · 34/37/29 · 20/52/27 · 23/43/34 · 31/42/27 · 36/30/34 | 4.2 · 1.8 · 2.4 · 2.1 · 4.9 · 2.0 · 3.1 | 30.4 · 15.1 · 23.7 · 19.9 · 32.9 · 20.1 · 30.3 | 2.0 · 0.6 · 0.8 · 0.6 · 2.1 · 0.6 · 1.4 |
| Photo & Video | 33/13/53 · 30/13/57 · 30/13/57 · 34/16/50 · 36/13/51 · 23/35/42 · 32/15/53 | 5.8 · 3.6 · 4.1 · 4.4 · 8.6 · 3.1 · 5.5 | 23.8 · 12.3 · 19.5 · 17.2 · 27.8 · 16.4 · 20.7 | 3.1 · 0.9 · 1.4 · 1.3 · 4.1 · 1.1 · 2.3 |
| Productivity | 5/86/8 · 6/84/10 · 12/75/13 · 7/87/6 · 14/69/17 · 12/76/13 · 12/76/12 | 5.8 · 3.2 · 4.1 · 4.0 · 7.7 · 3.3 · 5.0 | 29.0 · 14.0 · 23.5 · 17.7 · 31.7 · 18.8 · 27.1 | 2.5 · 0.8 · 1.2 · 1.0 · 3.4 · 0.9 · 1.9 |
| Shopping* | 3/60/37 · 16/41/35 · 42/47/11 · 2/65/33 · 5/20/75 · 11/48/41 · 14/26/60 | 5.8 · 0.2 · 0.4 · 3.1 · 5.1 · 2.9 · 4.8 | 53.4 · 28.2 · 48.3 · 24.4 · 32.6 · 25.3 · 24.1 | 1.7 · 0.4 · 0.9 · 0.7 · 1.7 · 0.7 · 0.9 |
| Social & Lifestyle | 30/40/24 · 59/31/9 · 75/14/10 · 66/25/7 · 36/34/27 · 50/25/23 · 42/33/22 | 5.8 · 3.0 · 3.4 · 3.7 · 8.3 · 2.7 · 4.8 | 31.0 · 12.4 · 19.8 · 15.8 · 31.8 · 19.6 · 28.9 | 2.4 · 0.7 · 0.9 · 1.0 · 2.8 · 0.8 · 1.9 |
| Travel | 16/24/58 · 19/18/37 · 13/28/50 · 24/25/44 · 12/13/75 · 24/23/51 · 11/22/66 | 3.3 · 2.1 · 2.8 · 3.0 · 4.1 · 3.7 · 3.6 | 38.7 · 21.5 · 34.2 · 33.4 · 43.2 · 39.8 · 42.3 | 1.8 · 0.9 · 1.6 · 1.1 · 2.5 · 1.3 · 2.0 |
| Utilities | 42/22/35 · 60/18/22 · 47/31/21 · 53/25/21 · 37/17/46 · 49/23/28 · 31/21/47 | 6.6 · 3.6 · 4.8 · 4.5 · 8.7 · 3.8 · 5.8 | 32.6 · 14.8 · 23.1 · 17.1 · 32.6 · 21.1 · 27.7 | 2.1 · 0.7 · 1.0 · 0.9 · 2.7 · 0.8 · 1.6 |

| Category | D14 RPI $ | D60 RPI $ | Y1 RLTV per payer $ |
|---|---|---|---|
| Business | 0.40 · 0.08 · 0.15 · 0.15 · 0.53 · 0.13 · 0.31 | 0.65 · 0.15 · 0.26 · 0.25 · 0.87 · 0.20 · 0.49 | 37.96 · 22.33 · 23.53 · 24.91 · 40.21 · 30.45 · 41.21 |
| Education | 0.33 · 0.09 · 0.14 · 0.11 · 0.51 · 0.12 · 0.32 | 0.45 · 0.13 · 0.20 · 0.16 · 0.69 · 0.17 · 0.44 | 31.29 · 18.30 · 25.40 · 20.09 · 39.15 · 25.12 · 33.07 |
| Gaming | 0.10 · 0.03 · 0.03 · 0.04 · 0.14 · 0.04 · 0.08 | 0.17 · 0.04 · 0.05 · 0.06 · 0.22 · 0.07 · 0.14 | 11.64 · 7.74 · 8.08 · 11.94 · 11.82 · 11.14 · 12.81 |
| Health & Fitness | 0.56 · 0.16 · 0.21 · 0.21 · 0.69 · 0.20 · 0.49 | 0.74 · 0.22 · 0.29 · 0.28 · 0.89 · 0.27 · 0.67 | 36.63 · 26.61 · 28.12 · 26.62 · 37.82 · 31.97 · 41.97 |
| Media & Ent. | 0.22 · 0.06 · 0.07 · 0.06 · 0.24 · 0.06 · 0.16 | 0.32 · 0.09 · 0.10 · 0.10 · 0.37 · 0.10 · 0.25 | 23.16 · 14.02 · 15.74 · 15.25 · 23.44 · 18.48 · 25.35 |
| Photo & Video | 0.32 · 0.08 · 0.13 · 0.12 · 0.45 · 0.11 · 0.29 | 0.45 · 0.11 · 0.19 · 0.19 · 0.62 · 0.16 · 0.39 | 22.52 · 15.86 · 19.76 · 19.12 · 23.90 · 19.37 · 25.83 |
| Productivity | 0.30 · 0.08 · 0.12 · 0.10 · 0.44 · 0.10 · 0.27 | 0.41 · 0.11 · 0.17 · 0.15 · 0.59 · 0.14 · 0.36 | 22.53 · 16.63 · 18.80 · 20.41 · 24.89 · 19.16 · 24.63 |
| Shopping* | 0.14 · 0.05 · 0.07 · 0.07 · 0.17 · 0.10 · 0.15 | 0.20 · 0.07 · 0.14 · 0.09 · 0.26 · 0.13 · 0.23 | 18.16 · 9.12 · 13.32 · 8.55 · 25.88 · 16.30 · 25.77 |
| Social & Lifestyle | 0.26 · 0.07 · 0.08 · 0.09 · 0.33 · 0.08 · 0.24 | 0.38 · 0.09 · 0.12 · 0.14 · 0.49 · 0.12 · 0.33 | 23.35 · 12.35 · 14.77 · 14.45 · 24.31 · 16.95 · 25.51 |
| Travel | 0.20 · 0.12 · 0.17 · 0.12 · 0.38 · 0.18 · 0.25 | 0.29 · 0.18 · 0.25 · 0.18 · 0.50 · 0.23 · 0.35 | 15.38 · 13.07 · 13.83 · 11.50 · 18.22 · 14.41 · 20.09 |
| Utilities | 0.21 · 0.06 · 0.09 · 0.08 · 0.31 · 0.08 · 0.20 | 0.32 · 0.09 · 0.14 · 0.12 · 0.46 · 0.12 · 0.29 | 20.67 · 13.31 · 14.22 · 15.32 · 22.01 · 15.69 · 22.87 |

Y1 RLTV per payer by price tier and access (low / mid / high | freemium / hard paywall), $:
Business 14.28 / 36.17 / 87.77 | 35.39 / 62.84 · Education 9.48 / 26.41 / 68.95 | 32.15 / 50.66 · Gaming 10.60 / 10.26 / 41.70 | 13.60 / 14.33 · Health & Fitness 12.61 / 34.47 / 77.42 | 36.91 / 67.45 · Media & Ent. 10.12 / 26.07 / 56.63 | 25.08 / 37.43 · Photo & Video 12.12 / 23.53 / 36.60 | 24.46 / 30.63 · Productivity 11.34 / 25.60 / 51.50 | 24.79 / 36.25 · Shopping* 8.72 / 30.89 / 66.59 | 28.94 / n/a · Social & Lifestyle 10.82 / 23.83 / 53.25 | 24.36 / 27.42 · Travel 13.81 / 21.95 / 33.82 | 22.78 / n/a · Utilities 10.21 / 26.05 / 50.81 | 21.51 / 36.48

Useful upper quartiles (p75) for North America, Y1 RLTV per payer: Business 73.40 · Education 63.79 · Gaming 25.38 · H&F 63.28 · Media 43.46 · Photo & Video 36.04 · Productivity 42.31 · Shopping 40.63 · Social 42.04 · Travel 31.41 · Utilities 40.07.

Y1 retention by category × region, medians (monthly / weekly / annual):
- Business: 20.5/1.3/41.6 · 8.1/0.6/30.7 · 12.2/1.3/33.2 · 8.1/0.4/31.3 · 14.6/2.3/40.2 · 12.5/1.2/33.6 · 13.2/1.2/42.2
- Education: 8.0/2.1/19.7 · 3.4/0.5/19.2 · 5.1/1.4/20.1 · 5.5/0.6/22.6 · 6.8/1.8/22.7 · 5.3/1.1/20.0 · 7.1/1.5/22.8
- Gaming: 6.9/1.7/26.0 · 5.5/0.5/23.5 · 4.4/1.1/26.7 · 9.1/1.0/32.5 · 6.2/1.6/23.7 · 5.2/1.1/25.0 · 4.6/1.1/25.0
- Health & Fitness: 8.3/1.9/23.0 · 5.0/0.8/20.3 · 8.5/1.7/25.2 · 7.3/1.5/21.4 · 8.2/2.4/22.9 · 7.1/2.5/21.3 · 8.4/1.6/23.0
- Media & Ent.: 11.9/1.5/29.2 · 4.7/0.5/29.6 · 8.6/0.6/31.4 · 6.9/0.5/30.0 · 9.4/1.2/31.6 · 6.5/0.8/23.7 · 11.2/0.8/39.4
- Photo & Video: 10.4/1.8/27.3 · 5.5/0.8/23.1 · 7.3/1.0/22.1 · 8.0/1.3/24.1 · 8.4/1.8/23.3 · 7.9/1.3/21.6 · 8.6/1.0/26.4
- Productivity: 9.8/1.8/23.0 · 6.2/0.9/23.0 · 9.6/1.0/21.2 · 7.9/1.3/23.0 · 8.8/1.5/23.2 · 7.3/1.2/21.2 · 10.5/1.0/25.0
- Shopping* (sparse): APAC M 20.9 / Y 44.7 · NA 9.2/1.0/38.9 · WEU 5.4/1.2/18.2
- Social & Lifestyle: 5.1/0.5/27.2 · 2.7/0.1/21.6 · 3.5/0.3/24.2 · 2.5/0.3/21.9 · 4.5/0.6/24.1 · 4.4/0.6/21.0 · 3.8/0.4/27.2
- Travel: 10.2/2.9/29.9 · 3.4/3.1/31.0 · 5.2/0.5/31.2 · 4.0/1.0/34.8 · 6.1/2.2/32.3 · 7.1/1.0/37.0 · 8.9/3.1/39.9
- Utilities: 14.5/2.7/32.0 · 5.2/0.5/22.9 · 6.7/1.1/24.2 · 5.2/0.6/24.1 · 10.0/2.0/30.2 · 7.9/0.9/23.3 · 11.4/1.2/36.4

Time to paid by category × region: share of paid conversions by time since install, % — **Day 0 / Days 1–3 / Days 4–7 / Week 2 / Week 3 / Week 4 / Week 5 / Week 6+**. These charts have no value labels in the PDF; values were measured from bar heights (±1pp, rows sum to ~98–100). Spikes at Days 4–7 reflect 7-day trial expiries.

| Category | APAC | IN/SEA | LATAM | MEA | NA | ROW | WEU |
|---|---|---|---|---|---|---|---|
| Business | 57/9/6/3/1/1/2/18 | 42/16/6/5/3/2/2/22 | 38/17/6/4/2/2/1/26 | 62/10/4/3/1/1/1/15 | 33/23/13/6/2/1/2/20 | 62/13/5/3/1/1/1/13 | 44/20/8/3/1/1/1/20 |
| Education | 24/7/28/10/2/1/1/24 | 42/9/14/8/3/2/1/20 | 34/9/19/10/3/2/1/21 | 33/9/19/9/3/2/1/22 | 22/9/32/9/2/2/1/22 | 40/8/16/8/3/1/1/21 | 29/10/22/10/3/2/2/23 |
| Gaming | 45/21/8/6/3/2/1/13 | 48/20/9/4/2/1/1/11 | 44/21/9/6/3/2/1/12 | 36/24/9/6/3/2/1/17 | 40/21/9/7/3/2/1/15 | 43/22/8/5/3/2/1/14 | 40/21/8/6/3/2/1/17 |
| Health & Fitness | 30/7/23/9/3/1/2/23 | 46/10/15/7/2/1/1/16 | 31/9/18/8/3/2/2/25 | 43/11/14/6/2/1/1/19 | 27/8/26/8/2/2/3/20 | 43/9/17/6/2/1/1/18 | 32/7/20/9/3/2/2/25 |
| Media & Ent. | 45/11/7/4/2/1/5/23 | 40/13/10/7/2/2/2/22 | 41/13/9/5/2/1/1/26 | 37/8/6/11/3/2/3/27 | 38/11/14/5/2/1/2/26 | 50/11/8/4/2/1/2/21 | 42/12/8/5/2/1/2/26 |
| Photo & Video | 47/11/12/4/2/1/1/21 | 38/8/15/10/2/1/1/23 | 30/12/17/6/2/1/1/28 | 49/9/12/5/1/1/1/20 | 48/13/12/3/1/1/1/20 | 44/9/9/4/2/1/1/30 | 43/13/12/4/2/1/1/22 |
| Productivity | 74/2/3/2/1/0/0/15 | 70/4/4/2/1/0/0/17 | 73/3/4/2/1/0/0/14 | 80/2/2/1/0/0/0/12 | 70/5/6/2/1/0/0/14 | 72/3/4/1/1/0/0/16 | 71/3/5/1/1/0/0/17 |
| Shopping* | 49/10/9/6/2/1/2/17 | 62/8/7/4/2/2/1/11 | 50/11/9/10/4/2/2/10 | 45/11/7/6/3/3/2/19 | 35/29/11/6/3/2/1/11 | 70/5/5/4/1/1/1/10 | 52/9/14/4/2/1/1/15 |
| Social & Lifestyle | 43/13/11/5/2/1/1/21 | 35/12/5/3/2/1/1/39 | 47/14/6/4/2/2/1/21 | 57/10/4/3/1/1/1/21 | 41/12/13/6/2/1/2/21 | 47/12/7/4/2/1/1/24 | 42/13/9/5/2/1/1/23 |
| Travel | 43/7/11/5/2/1/1/27 | 48/9/7/6/2/1/1/23 | 42/10/10/6/3/2/1/25 | 62/8/5/3/1/1/1/16 | 32/8/13/10/3/2/1/29 | 55/6/8/3/2/1/1/22 | 38/8/11/5/2/2/2/30 |
| Utilities | 38/17/14/5/2/1/2/19 | 63/11/9/3/1/1/1/8 | 53/11/9/6/2/1/1/14 | 64/10/6/2/1/1/1/13 | 31/18/20/6/2/1/1/18 | 61/12/7/3/1/1/1/12 | 41/12/13/4/2/1/3/22 |

*Shopping has a small sample: distributions are lumpy and some regional cells look unstable. Flag that when quoting it.

## Errata (where the PDF's text contradicts its own charts)

Provably wrong text (use the data, flag the text): the copy-pasted category summaries, the Shopping page titled "Productivity", and the AI summary's "trial-to-paid" label. For the rest, give the text figure first and the chart figure next to it.
- Category-breakout summaries reuse other categories' numbers: Business, Gaming and Health & Fitness summaries quote Education's figures ($39.15 NA / $33.07 WEU / $68.95 high / $9.48 low). Shopping and Social summaries quote Productivity's ($24.89 / $24.63 / $16.63 / $24.79 vs $36.25). Shopping's summary page is even titled "Productivity".
- p85 text says Productivity is 77% yearly and Health & Fitness is monthly-heavy; the chart shows the reverse (Productivity 76.7% **monthly**, H&F 68.4% **annual**).
- p40 text: Productivity Y1 RLTV $24.95 and Education $22.82; chart: $22.03 and $27.28.
- p42 text: IN/SEA Y1 RLTV $19.32; chart: $15.31.
- p35 expert comment: weekly-plan RPI $0.07 (D14) / $0.09 (D60); the chart gives weekly-dominant apps $0.19 / $0.32.
- p103 text: Utilities deepest intro discount (−63%); chart: Travel −62.7%, with Business (−83.6%) and Shopping (−80.5%) deeper still.
- p119 text: NA weekly 1st renewal 55%; chart: 50%.
- p150 summary: "download-to-paid 2.9% vs 2.6%" and "D60 RPI $0.42 vs $0.23"; the detailed charts say 2.6% vs 0.9% and $0.42 vs $0.16.
- AI chapter summary calls 8.5% vs 5.6% "trial-to-paid"; it is the **trial start** rate. Its weekly retention figures (2.5% vs 3.4%) are p75s; medians are 1.2% vs 1.7%.
- p89 text says Travel 27% three-plan and Shopping 40% single-plan; chart: 25.4% and 39.4%.
- p99 text: top performers get 0–10% of new payers via intro offers; chart: all-category top-tier median 7.0%, but top-tier Business 70.7% and H&F 21.9%.
