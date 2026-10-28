---
name: state-of-web2app-2026
description: "Answer questions from FunnelFox's State of Web2App 2026 report: web-to-app funnel benchmarks for adoption, funnel conversion, pricing and country price index, trials, upsells, LTV, retention, churn, refunds and payments (methods, failures, retries)."
---

# State of Web2App 2026 (FunnelFox) — unofficial skill

This skill holds the content and chart data of **State of Web2App 2026** by FunnelFox (74-page PDF, edition 01, January 2026): https://funnelfox.com/state-of-web2app-2026

It replaces reading the report. People ask questions; you answer from the numbers below.

Use it for anything about **web-to-app (web2app) subscription funnels**: acquiring users through a web quiz/onboarding funnel and taking payment on the web before the app install. Typical questions: "is web2app worth it", "what does a good web funnel conversion look like", "web vs in-app LTV", "how should I price on web", "how much more can I charge in country X", "upsell price", "web subscription retention", "refund rates on web", "Apple Pay vs card vs PayPal", "how many payments fail", "how many retries".

## How to answer

1. **Answer in the language the person writes in.** Keep metric names recognizable (LTV, ARPU, ARPPU, price index).
2. **Numbers first, short.** Lead with the benchmark, then 2–4 supporting points. No preamble.
3. **Only use numbers from this file.** If the report doesn't cover something, say so and give the closest thing it does cover. Never invent a number and present it as the report's.
4. **Mind what each number is.** Most data is FunnelFox platform data (web funnels and web payments) plus Meta Ads Library parsing for market-size charts. Say which. Many charts don't state sample size, period granularity or whether values are means or medians; when the report doesn't say, don't claim it.
5. **Text vs chart.** When the report's prose and its own charts or tables disagree: if the text is provably wrong (the arithmetic doesn't work, it copies another section's numbers, or it contradicts the report's own table), use the data value and say the text is in error. Otherwise give both: the text figure first, as the publisher's stated number, then the chart value, and say they differ. Don't silently pick one. See Errata.
6. **Vendor caveat.** FunnelFox sells web2app funnels and web payments. Headline claims ("web converts 2× better", "upsells lift LTV", web LTV > app LTV) come from a party that benefits from them. Present them as the report's findings, not settled fact, especially when the person is deciding whether to move to web.
7. **Cite once per answer:** "FunnelFox, State of Web2App 2026". Add the link when they want to read more.

### Combining with other report skills

If the RevenueCat SOSA 2026 or Adapty State of Paywalls 2026 skills are available, you may use them side by side but never merge numbers. Those measure in-app (store) subscriptions; this one measures web funnels. Funnel definitions differ (this report counts from ad click / session start; RevenueCat from install; Adapty from paywall view).

### When someone gives you their own numbers

1. Identify which step or metric (session → 2nd screen → paywall → purchase, plan, price, region, LTV month, retention period, refund, payment success).
2. Compare to the matching benchmark below; say where they stand.
3. End with **one lever** tied to their weakest step: early drop-off → second screen / landing-to-quiz continuity (biggest drop is screen 2); low purchase → pricing as conversion lever, no-trial or paid-trial offers, Apple Pay first; low LTV → upsells after purchase, 3-month plan; churn → act before renewal 1, cancellation flow; payment failures → wallet coverage, 3DS handling, retry timing (first 3 retries matter most).

## Methodology

- Sources: aggregated parsing of global web funnels, **Meta Ads Library**, third-party ad intelligence (Web Funnels Club), and anonymized **FunnelFox** platform data (apps with active web2app funnels above minimum traffic and revenue thresholds; funnel management and web payments). Data processed in batches with added randomization for privacy.
- Period: 2025 (adoption comparisons vs 2023–2024).
- Categories: Health & Fitness, EdTech, Utilities, Photo & Video, Lifestyle, Social, Finance & Career, Productivity (market charts use finer sub-categories).
- Regions: United States, Europe, Latin America (LATAM), Asia Pacific (APAC), Middle East & Africa (MEA); Canada shown separately in several charts.
- Sample size, app count and whether figures are means or medians are not stated.

## Key findings

1. **Adoption:** 82% of the 100 top-grossing apps used web2app in 2025, up from 30% in 2024. The number of apps with web2app funnels grew +77% YoY in 2025 (+63% in 2024).
2. **Scale effect:** brands that scale web funnels see ~176% YoY revenue growth, and web funnels make up ~90% of their advertising-driven revenue (10% from in-app funnel campaigns).
3. **More funnels, more revenue:** top-quartile-revenue apps run many funnels, often 100+, up to ~300; bottom-quartile apps run fewer than ~35.
4. **US dominates:** 63.6% of global web2app revenue.
5. **Conversion:** web funnel converts 3% of ad clicks to purchase vs 1.5% for the app-store funnel ("2×"). Biggest drop is the second screen (47.5% reach it).
6. **Trials:** 56.9% of web2app revenue comes from offers without any trial; paid trials 28.9%; free trials only 14.3%.
7. **Monthly leads:** 48.8% of revenue from monthly plans; weekly 30.5%.
8. **Web LTV beats app LTV** at 12 months in the US: annual $69 vs $34, monthly $55 vs $38, weekly $45 vs $35 (no store fees, better retention per the report).
9. **ARPPU is flat worldwide** ($27–31 per paying session) while ARPU per session varies 3.4× (US $1.46 vs LATAM $0.43).
10. **Payments:** Apple Pay ~60% of web transactions; 30–50% of initiated payments fail; retries recover up to 17.5% of renewals (15–20% revenue uplift).

## Market overview

- Apps with web2app funnels: +63% YoY (2024), +77% YoY (2025). No absolute counts given.
- Web2app adoption among the 100 top-grossing apps: 30% (2024) → 82% (2025).
- Ad creatives per brand by quarter 2025 (series: top 1% / top 5% / top 10% brands by number of creatives / median per brand; the chart's labelling is ambiguous, values ascend left to right): Q1 360 / 2,905 / 5,398 / 7,186 · Q2 595 / 4,717 / 9,060 / 13,257 · Q3 672 / 7,116 / 11,543 / 24,602 · Q4 372 / 3,761 / 5,725 / 5,952. Average ad volume +254%. Q3 spike linked to Meta's **Andromeda** launch; the largest companies drove most of it.
- Number of funnels with >100 creatives/month by category (read from unlabeled bars, ±3): Health & Fitness ~195 · Edtech & Microlearning ~37 · Astrology & Spirituality ~37 · Language Learning ~35 · Dating & Relationships ~33 · AI Tools & Productivity ~29 · Other ~24 · Kids & Family ~20 · Pets & Hobbies ~13 · Utilities ~12 · Finance & Career ~12 · E-commerce & Shopping ~6 · Photo & Video ~5.
- Health & Fitness sub-categories (same metric, ±2): Fitness ~62 · Mental Health ~58 · Nutrition & Diet ~28 · Beauty & Skincare ~27 · Misc Health ~26.
- 2025 growth in funnel count by category (unlabeled bars, ±2pp): Finance & Career ~70% (fastest) · AI Tools & Productivity ~21% · Language Learning ~18% · Astrology & Spirituality ~14% · Nutrition & Diet ~12% · Dating ~10% · Kids & Family ~10% · E-commerce ~10% · Fitness ~9% · Beauty & Skincare ~6% · Edtech ~6% · Health ~5% · Utilities ~5% · Pets & Hobbies ~4% · Mental Health ~3%.
- Revenue vs number of funnels (scatter by revenue quartile): bottom 25% up to ~35 funnels; 25–50% up to ~95; 50–75% up to ~135; top 25% many at 100+, max ~300.
- Web2app revenue by region: US 63.6% · Europe 14.2% · APAC 7.7% · LATAM 5.6% · MEA 4.6% · Canada 4.2%.
- Takeaways: test many funnels to explore segments; give Andromeda a variety of ads to optimize.

## Conversions

- **Web funnel steps** (share of sessions): session created 100% → second screen 47.5% → paywall 13% → purchase 3%. The second screen is the biggest drop; fixing steps before the paywall has a multiplied effect.
- **App funnel vs web funnel** (share of ad clicks): App: ad click 100% → App Store page 100% → install 30.0% → purchase 1.5%. Web: ad click 100% → onboarding start 100% → second screen 47.5% → purchase 3%. Report headline: web converts ~2× better.

## Monetization

- **Revenue by plan:** 1 month 48.8% · 1 week 30.5% · 1 year 12.2% · 3 months 8.4%.
- **Revenue by trial type:** no trial 56.9% · paid trial 28.9% · free trial 14.3%.
- **Trial mix within each plan** (free trial / paid trial / no trial, % of revenue): 1 month 7.18 / 40.01 / 52.81 · 1 week 28.17 / 21.35 / 50.48 · 3 months 2.17 / 21.84 / 75.99 · 1 year 13.26 / 13.56 / 73.18. Report headline: no-trial offers outperform trial flows for weekly and monthly plans.
- **Average web2app price, US:** 1 week $8.14 · 1 month $15.76 · 3 months $31.76 · 1 year $45.71. Report says web price points closely match in-app prices.
- **Most popular price by region** (US / Canada / Europe / APAC / LATAM): 1 week $7.99 / $9.99 / $5.95 / $9.99 / $13.98 · 1 month $12.49 / $12.49 / $14.59 / $14.59 / $24.98 · 3 months $40.80 / $40.80 / $37.95 / $37.95 / $37.95 · 1 year $74.94 / $74.94 / $69.99 / $69.99 / $59.94. Flag: LATAM weekly and monthly modal prices are the highest, likely a currency/localization artifact; the report doesn't explain it.
- **Upsells:** headline "upsells increase LTV by 20%"; also "x2 revenue lift in median terms"; chart shows LTV growth >200% with upsells vs ~100% without. Upsells average 4.07% of total revenue. They work as LTV multipliers, not a standalone growth driver.
- **Average upsell price by primary subscription, US:** 1 week $10.51 · 1 month $15.77 · 3 months $17.56 · 1 year $8.72. Global median upsell price ≈ $9.31. 3-month subscribers buy the most expensive upsells.
- Takeaways: test plan, tier and billing cadence; design upsells for higher-tier subscribers; segment upsell price by tier, usage and behaviour.

### FunnelFox Pricing Index (median price vs US = 1.00)

| Plan | Countries (index) |
|---|---|
| 1 week | ES 1.62 · LT 1.22 · SE 1.16 · BR 1.15 · PL 1.13 · GB 1.13 · CA 1.03 · AU 1.02 · DE 1.01 · US 1.00 · UA 0.77 · BY 0.65 · KZ 0.63 |
| 1 month | TW 1.63 · PL 1.26 · CH 1.16 · AU 1.12 · FR 1.11 · AE 1.11 · ES 1.09 · NL 1.09 · GB 1.08 · SE 1.08 · CA 1.06 · IT 1.04 · DE 1.02 · NZ 1.00 · US 1.00 · CL 0.98 · SA 0.97 · MX 0.94 · UA 0.77 · TR 0.70 · BR 0.66 |
| 3 months | TW 1.68 · SA 1.51 · MX 1.25 · AE 1.21 · FR 1.20 · DE 1.13 · GB 1.09 · AU 1.09 · NZ 1.07 · CA 1.04 · US 1.00 |
| 1 year | TW 1.98 · TR 1.45 · CA 1.02 · MX 1.00 · US 1.00 · BR 0.99 · UA 0.99 · DE 0.91 · AU 0.82 · FR 0.79 · GB 0.77 |

Some countries sit above the US because of currency localization. The intro example (US = $12.99; Netherlands $21.00 → 1.62; Turkey $3.79 → 0.29) doesn't match the per-plan charts (see *Errata*); prefer the per-plan tables.

## LTV and profitability

- **ARPU per session** (revenue ÷ all sessions): US $1.46 · Canada $1.06 · APAC $0.81 · Europe $0.74 · LATAM $0.43.
- **ARPPU per paying session:** US $26.99 · Canada $30.57 · APAC $30.90 · Europe $29.47 · LATAM $27.31. Narrow $27–31 band: once users pay, spend is similar everywhere; the regional gap is conversion.
- **Web vs app LTV, US, cumulative by month** (web: weekly / monthly / quarterly / annual · app store: weekly / monthly / annual):

| Month | Web weekly | Web monthly | Web quarterly | Web annual | App weekly | App monthly | App annual |
|---|---|---|---|---|---|---|---|
| 1 | $9 | $15 | $23 | $69 | $4 | $9 | $34 |
| 2 | $20 | $26 | $23 | $69 | | | |
| 3 | $27 | $36 | $23 | $69 | $21 | $21 | $34 |
| 4 | $32 | $43 | $45 | $69 | | | |
| 5 | $36 | $48 | $45 | $69 | | | |
| 6 | $38 | $50 | $45 | $69 | $28 | $28 | $34 |
| 7 | $40 | $52 | $48 | $69 | | | |
| 8 | $42 | $53 | $48 | $69 | | | |
| 9 | $43 | $54 | $48 | $69 | $32 | $33 | $34 |
| 10 | $44 | $55 | $55 | $69 | | | |
| 11 | $45 | $55 | $55 | $69 | | | |
| 12 | $45 | $55 | $55 | $69 | $35 | $38 | $34 |

App LTV points are labelled only at months 1, 3, 6, 9, 12.
- Expert view (Anton Kuzmin, AdQuantum): in Health & Fitness, app LTV is typically ~$40–45 while web LTV for the same product can reach $80–90. Web CPAs and auction prices are higher, so web and app need separate unit-economics models.

### Cumulative LTV per user by month of life (web), $

Cells: upper whisker / p75 / median / p25 / lower whisker.

| Month | All plans | 1-week plan | 1-month plan | 3-month plan |
|---|---|---|---|---|
| 1 | 60 / 40 / 29 / 22 / 12 | 22 / 13 / – / – / 8 | 29 / 21 / 15 / 12 / 8 | 50 / 40 / 23 / 20 / 15 |
| 2 | 60 / 51 / 38 / 31 / 19 | 54 / 32 / 20 / 14 / 8 | 47 / 34 / 26 / 20 / 16 | 50 / 40 / 23 / 20 / 15 |
| 3 | 71 / 57 / 46 / 34 / 25 | 83 / 46 / 27 / 18 / 8 | 64 / 49 / 36 / 27 / 22 | 50 / 40 / 23 / 20 / 15 |
| 4 | 83 / 65 / 51 / 40 / 26 | 103 / 55 / 32 / 21 / 8 | 78 / 60 / 43 / 32 / 27 | 89 / 60 / 45 / 37 / 32 |
| 5 | 91 / 66 / 54 / 42 / 29 | 116 / 61 / 36 / 23 / 8 | 87 / 69 / 48 / 36 / 31 | 89 / 60 / 45 / 37 / 32 |
| 6 | 99 / 69 / 56 / 44 / 30 | 130 / 67 / 38 / 25 / 8 | 97 / 76 / 50 / 39 / 34 | 89 / 60 / 45 / 37 / 32 |
| 7 | 105 / 77 / 57 / 48 / 32 | 142 / 71 / 40 / 26 / 8 | 106 / 82 / 52 / 42 / 37 | 116 / 71 / 48 / 45 / 42 |
| 8 | 110 / 79 / 59 / 49 / 34 | 151 / 75 / 42 / 27 / 8 | 113 / 88 / 53 / 44 / 39 | 116 / 71 / 48 / 45 / 42 |
| 9 | 114 / 81 / 60 / 50 / 35 | 159 / 78 / 43 / 28 / 8 | 120 / 93 / 54 / 47 / 41 | 116 / 71 / 48 / 45 / 42 |
| 10 | 118 / 86 / 60 / 52 / 36 | 165 / 80 / 44 / 29 / 8 | 126 / 97 / 55 / 48 / 43 | 133 / 75 / 55 / 49 / 45 |
| 11 | 120 / 88 / 60 / 53 / 37 | 168 / 82 / 45 / 30 / 8 | 134 / 101 / 55 / 50 / 45 | 133 / 75 / 55 / 49 / 45 |
| 12 | 122 / 89 / 60 / 53 / 38 | 169 / 83 / 45 / 30 / 8 | 135 / 101 / 55 / 50 / 45 | 133 / 75 / 55 / 49 / 45 |

1-year plan: flat for all 12 months at 75 / 72 / 69 / 65 / 62.
The 1-week plan has the widest spread (top whisker $169 vs median $45): weekly is a high-variance bet.

### Retention (share of subscribers still active)

| Period | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-week plan | 100% | 54.04% | 28.97% | 19.11% | 12.49% | 9.45% | 7.72% | 6.13% | 4.93% | 4.22% | 3.63% | 3.11% |
| 1-month plan | 100% | 56.50% | 43.57% | 33.74% | 25.92% | 21.29% | 17.44% | 14.55% | 13.18% | 10.68% | 10.45% | 10.22% |

The weekly chart's x-axis unit isn't labelled (the text implies periods). 3-month plan, by month: 100% (M1), 50.53% (M4), 28.05% (M7), 18.29% (M10); flat between renewals.

- **Average renewal cycles:** 1 week 4.21 · 1 month 2.18 · 3 months 1.80 · 1 year 1.20. Short plans renew more often; long plans still win on LTV.
- **Churn timing** (share of cancellations by days after purchase: 0d / 1–3d / 4–7d / 8–14d / 15–30d / 31–60d / 61–90d / 90+d):
  - 1 week: 5.1 / 5.7 / 23.6 / 17.9 / 20.2 / 19.6 / 4.8 / 3.2
  - 1 month: 5.2 / 3.7 / 12.4 / 3.2 / 22.1 / 28.8 / 11.4 / 13.2
  - 3 months: 6.1 / 2.7 / 1.9 / 1.0 / 1.5 / 1.2 / 3.5 / 82.1
  - 1 year: 12.8 / 12.2 / 26.9 / 8.5 / 20.5 / 13.2 / 4.6 / 1.2
  - 3-month plans give the longest window to onboard and intervene before users decide. On annual plans, cancellations cluster early: users turn off auto-renew soon after buying.
- **Cancellation rate by plan × price** (< $10 / $10–20 / $20–30 / $30–40 / $40–50 / $50+):
  - 1 week: 57.96 / 45.76 / 64.08 / 66.67 / 0.00* / 17.65
  - 1 month: 35.35 / 43.75 / 44.66 / 36.73 / 42.88 / 55.97
  - 3 months: 40.54 / 34.96 / 37.73 / 39.86 / 26.59 / 32.60
  - 1 year: 18.11 / 2.02 / 4.95 / 22.26 / 37.99 / 15.88
  - *0.00% is almost certainly an empty cell, not a real 0. Headline: higher-priced weekly plans are the most volatile, with up to 66% cancelling.

### Refunds

- **Refund rate by region, share of revenue:** APAC 8.00% · Europe 3.47% · LATAM 2.60% · US 5.67%.
- **Refund rate by region, share of transactions:** APAC 6.72% · Europe 4.18% · LATAM 2.50% · US 3.67%.
- **Refund rate by plan:** 1 week 0.20% · 1 month 1.81% · 1 year 3.69%.
- **Time to refund:** 45.36% of refunds within 24 hours, 73.46% within 7 days, 91.69% within 30 days. Days to refund: min 0 · median 1.6 · average 11.1 · max 697.1.

## Payments

- **Payment methods (worldwide):** Apple Pay ~60% · cards 20% · PayPal 18% · Google Pay 2%. PayPal is ~90% in Germany; Stripe (cards) is more common in the US. Offer local methods per market.
- **30–50% of initiated payments fail.** Causes: 3DS and bank authentication friction, card declines and issuer restrictions, missing wallets or fallbacks, network or gateway errors.
- **Renewal outcome:** 60% renew on the first attempt; 17.5% fail first and are then recovered; 22.5% fail for good. Recovery adds 15–20% revenue.
- **Retry success by attempt (1–10):** 19.3% · 12.5% · 9.3% · 6.5% · 5.5% · 4.8% · 3.3% · 3.0% · 3.3% · 4.7%. The first 3 attempts recover almost half of what's recoverable.

## Expert takeaways (paraphrased)

- Vasyl Sergiienko (Health & Wellness Apps, Meta): segment funnels by user intent (calisthenics, walking, yoga, Tai Chi); specific funnels beat generic ones.
- Marcus Burke (Meta Ads consultant): judging web only on direct response hides trade-offs. Gating the app behind payment starves ASO and ratings, limits word of mouth, and loses younger users who distrust web payments. Use web-first and app-first flows for what each does best.
- Kirill Makarov (WebFunnels.Club): think in clusters of intent, not single flows. A network of intent-specific funnels suits Meta's Andromeda.
- Vitaly Davydov (Adapty): after Apple v. Epic, external payment links in the US are a practical growth lever.
- Hannah Parvaz (Aperture): build experiments around real user behaviour.
- Steve P. Young (AppMasters): treat price as a conversion lever. Bucket offers into entry, mid-tier and premium; localize and adapt pricing by intent.
- Anton Kuzmin (AdQuantum): web LTV can be ~2× app LTV (H&F: $80–90 vs $40–45), but web CPAs are higher; model them separately.
- Jessica Gotti (Paired): quiz onboarding lifts LTV by filtering for intent, at the cost of volume. It's not plug-and-play.
- Alice Muir Kocourková: retention is continuous value delivery. Balance win-back discounts with value-based engagement.
- Phil Carter (Elemental Growth): treat cancellation flows as insight engines. Ask why users leave, segment by intent, feed it back into the roadmap.

## Errata (report text vs its own charts)

- Region revenue: text says Europe 12% and APAC 6.6%; the chart shows Europe 14.2% and APAC 7.7%.
- Category growth: text says AI Tools, Language Learning, Astrology and Nutrition show "triple-digit growth"; the chart axis tops out at 70% and those bars are ~12–21%.
- Plan mix: text says monthly captures "48.8% of all subscriptions"; the chart is labelled revenue share.
- Upsells: the headline says +20% LTV, the bullet says "x2 revenue lift", and the chart shows >200%. These are incompatible; give all three and say so.
- Pricing index example: Turkey 0.29 ("3.5× cheaper") and Netherlands 1.62 don't match the per-plan charts (Turkey 0.70 monthly and 1.45 annual; Netherlands 1.09 monthly).
- Cancellation heatmap: text says "for annual plans price matters less", but annual cancellation reaches 37.99% at $40–50. The weekly $40–50 cell (0.00%) is likely missing data.
- Refund charts (region by revenue, region by transaction, time to refund) carry the title "Average renewal cycles per plan" and a copy-pasted bullet about billing cycles; the titles are wrong, the data are refunds.
- LTV-by-month charts label the 12th month as "11".
