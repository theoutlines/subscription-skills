---
name: state-of-in-app-subscriptions-2026
description: "Answer questions from Adapty's State of In-App Subscriptions 2026 report: subscription LTV curves, retention, renewals, refunds, prices by region and country, trial vs direct, paywall placement and type, experiments, iOS vs Android, AI apps and web paywalls, by category and region."
---

# State of In-App Subscriptions 2026 (Adapty) — unofficial skill

This skill holds the content and chart data of Adapty's **State of In-App Subscriptions 2026** (interactive web report): https://adapty.io/state-of-in-app-subscriptions-report/

It replaces reading the report. People ask questions; you answer from the numbers below.

This is a **different report** from Adapty's *State of Paywalls 2026* (paywall-view conversion, paywall design patterns). This one focuses on subscription economics after install: LTV, retention, renewals, refunds, pricing, trials, platforms, AI apps.

Use it for: "what's a good LTV for weekly/monthly/annual", "does a trial increase LTV", "how many weekly subscribers are left after a year", "renewal rates", "refund rate", "what do apps charge in Europe vs US", "price index for country X", "onboarding vs in-app paywall", "hard vs soft paywall", "which A/B tests win", "iOS vs Android", "AI app benchmarks", "web paywall vs in-app".

## How to answer

1. **Answer in the language the person writes in.** Keep metric names recognizable (LTV, install→trial, trial→paid, renewal).
2. **Numbers first, short.** Lead with the benchmark, then 2–4 supporting points.
3. **Only use numbers from this file.** If the report doesn't cover something, say so and give the closest thing. Never invent a number.
4. **Pick the right slice.** Most charts are filterable by trial/no trial, plan length, category and region. This file has the All Categories × Global view, plus category and region cuts where they were captured. If a slice isn't here, say so; don't interpolate.
5. **Precision.** Values on line and box charts were read from the rendered chart geometry (±1–2% of the axis range, prices ±$0.05). Bar values and labels are exact. Say "about" for curve values.
6. **Cite once per answer:** "Adapty, State of In-App Subscriptions 2026". The report sits behind an email form; mention that if someone wants to open it.
7. **Vendor caveat:** Adapty sells paywalls, A/B testing and analytics. Findings like "teams that experiment make 40× more" are correlations from a vendor.

### Combining with other report skills

Adapty *State of Paywalls 2026* (paywall-view conversion), RevenueCat *SOSA 2026* (install and trial-based, 115k apps) and FunnelFox *State of Web2App 2026* (web funnels) may also be installed. Use them side by side but never merge numbers: definitions, samples and periods differ. Example: Adapty's install→paid here is an average of per-app rates across all durations; RevenueCat's D35 download→paid is a median.

### When someone gives you their own numbers

1. Identify plan length, trial vs direct, category, region, metric (LTV month, retention month, renewal number, price, conversion step).
2. Compare to the matching cell; say above or below.
3. End with **one lever**. Low install→trial → onboarding paywall (1.35% vs 0.89% in-app with trial). Low LTV on weekly → add a trial (weekly 12-month LTV $54.5 with trial vs $27.0 without). Price → check region index and price-bucket LTV. Next test → structural tests (locales, trial, plan duration, number of plans) beat visual/copy.

## Methodology

- 16,000+ apps, $3B+ subscription revenue processed through Adapty; mostly Apple App Store (Google Play where stores are compared); calendar 2025; gross revenue in USD.
- Segments: region (North America/US, Europe, LATAM, MEA, APAC), billing cycle (weekly, monthly, annual, plus lifetime where relevant), acquisition (trial vs direct), sometimes paywall type and country.
- Categories: Health & Fitness, Education, Lifestyle, Photo & Video, Productivity, Utilities, Entertainment, Graphics & Design.
- Benchmarks are computed per app, then aggregated by segment, so big apps don't dominate. Apps with too little data are excluded, so early-stage apps are under-represented. The report shows medians, percentiles and averages, depending on the chart.
- Install→trial and install→paid are averages of per-app rates. Since plan length isn't known at install, those are the same across durations.

## Key findings

1. **Weekly is winning:** weekly plans went from 43.3% of revenue (2023) to 55.5% (2025). Weekly + trial 12-month LTV grows $7.40 → $54.50 (+636%), the best of any setup.
2. **Europe got expensive:** European prices +18% YoY. Europe is now the priciest region on weekly, monthly and annual, up to 40% above North America.
3. **Concentration:** top 10% of apps earn 94.5% of revenue (92.7% in 2023). Lifestyle is the most concentrated category (97.9%).
4. **Utilities + trials:** annual with trial reaches $68.90 first-year LTV, the best category. Utilities also has the best retention.
5. **Most apps earn little:** 57.7% of new apps with any revenue make $1–1,000 a year; 7.9% pass $100K.
6. **Trials help renewals:** first renewal on weekly is 59.2% with trial vs 37.0% direct (+60%). Weekly one-year retention is 5.5% vs 3.9% (+43%).
7. **Structural tests win:** localization (62.3%), trial (59.6%), plan duration (58.7%) and number of plans (57.1%) lift LTV far more often than visual or copy tests (34.6%).

## LTV

**Cumulative subscription LTV per subscriber, $** (Month 0 / 1 / 3 / 6 / 12), Global:

| Category | Trial: Weekly | Trial: Monthly | Trial: Annual | No trial: Weekly | No trial: Monthly | No trial: Annual |
|---|---|---|---|---|---|---|
| All | 7.4 / 19.0 / 33.1 / 43.2 / 54.5 | 10.3 / 14.8 / 21.6 / 27.8 / 35.3 | 42.1 → 49.9 | 6.5 / 12.2 / 18.4 / 22.6 / 27.0 | 10.6 / 14.2 / 19.4 / 24.1 / 29.7 | 35.8 → 42.5 |
| Health & Fitness | 6.0 / 16.0 / 27.6 / 35.5 / 43.6 | 10.2 / 15.3 / 21.8 / 27.3 / 33.3 | 43.6 → 51.9 | 5.1 / 11.3 / 17.8 / 22.2 / 27.2 | 10.2 / 15.1 / 21.1 / 26.0 / 31.1 | 26.6 → 31.7 |
| Education | 6.7 / 17.7 / 30.5 / 39.3 / 48.4 | 9.6 / 14.7 / 21.9 / 28.2 / 35.5 | 53.2 → 63.3 | 7.0 / 17.3 / 28.8 / 35.8 / 42.4 | 11.9 / 18.0 / 25.8 / 32.3 / 38.9 | 33.2 → 42.1 |
| Lifestyle | 7.8 / 18.9 / 31.3 / 39.2 / 47.5 | 11.3 / 15.9 / 23.1 / 29.8 / 38.9 | 30.0 → 36.0 | 6.3 / 11.1 / 16.0 / 19.4 / 22.9 | 12.3 / 15.6 / 21.3 / 26.6 / 34.4 | 38.4 → 45.7 |
| Photo & Video | 6.9 / 15.9 / 26.0 / 32.8 / 39.8 | 8.4 / 11.9 / 17.4 / 22.3 / 28.8 | 40.6 → 46.9 | 6.6 / 11.9 / 17.2 / 20.5 / 23.9 | 9.3 / 13.0 / 18.0 / 22.5 / 27.7 | 34.3 → 39.7 |
| Productivity | 7.2 / 18.7 / 32.3 / 42.0 / 52.8 | 12.5 / 17.5 / 25.1 / 32.1 / 41.1 | 40.5 → 49.1 | 6.5 / 14.4 / 23.9 / 30.8 / 38.6 | 11.6 / 16.6 / 24.5 / 32.4 / 43.2 | 45.7 → 56.9 |
| Utilities | 8.2 / 21.8 / 39.1 / 52.1 / 67.1 | 12.0 / 16.9 / 24.8 / 32.0 / 40.1 | 58.6 → 68.9 | 7.1 / 13.6 / 21.2 / 26.7 / 32.6 | 12.4 / 16.3 / 22.1 / 27.2 / 31.9 | 32.1 → 37.2 |
| Entertainment | 6.2 / 14.1 / 22.7 / 28.2 / 33.7 | 12.2 / 17.2 / 24.4 / 30.4 / 37.8 | 40.8 → 49.8 | 6.9 / 11.8 / 17.0 / 20.6 / 24.6 | 14.5 / 17.2 / 20.9 / 24.2 / 28.1 | 44.8 → 52.5 |
| Graphics & Design | 6.7 / 15.8 / 25.5 / 31.7 / 37.9 | 8.6 / 11.9 / 17.2 / 22.3 / 29.3 | 34.8 → 41.5 | 6.7 / 12.4 / 18.2 / 21.9 / 25.4 | 7.0 / 10.0 / 14.5 / 18.8 / 24.4 | 37.2 → 43.2 |

Annual is flat from month 0 to month 6 (one payment); "→" gives month 0 → month 12 (after the renewal).

By region, All Categories (Month 0 / 1 / 3 / 6 / 12):

| Region | Trial: Weekly | Trial: Monthly | Trial: Annual | No trial: Weekly | No trial: Monthly | No trial: Annual |
|---|---|---|---|---|---|---|
| North America | 7.5 / 20.5 / 37.1 / 49.6 / 63.9 | 11.7 / 17.2 / 25.2 / 32.6 / 41.5 | 43.0 → 51.2 | 6.4 / 12.8 / 20.1 / 25.2 / 30.6 | 11.9 / 15.9 / 21.5 / 26.6 / 32.5 | 38.4 → 46.0 |
| Europe | 8.1 / 19.9 / 33.7 / 43.3 / 54.1 | 10.6 / 15.1 / 21.8 / 27.9 / 35.5 | 44.2 → 53.1 | 7.2 / 12.8 / 18.4 / 22.2 / 26.1 | 11.4 / 15.0 / 20.5 / 25.6 / 31.8 | 38.1 → 45.4 |
| LATAM | 6.8 / 17.4 / 30.1 / 39.0 / 48.7 | 8.3 / 11.6 / 16.6 / 21.0 / 26.3 | 35.8 → 41.2 | 5.7 / 10.8 / 16.3 / 20.1 / 23.9 | 8.8 / 11.9 / 16.3 / 20.3 / 24.6 | 32.1 → 37.9 |
| MEA | 6.8 / 18.0 / 31.9 / 42.0 / 53.1 | 8.6 / 12.6 / 19.1 / 25.1 / 32.5 | 37.9 → 44.8 | 6.0 / 12.4 / 19.7 / 24.8 / 30.1 | 8.7 / 11.9 / 16.6 / 21.0 / 25.9 | 31.0 → 36.0 |
| APAC | 7.0 / 17.7 / 30.5 / 39.8 / 50.1 | 9.2 / 12.9 / 18.9 / 24.0 / 29.8 | 42.0 → 48.9 | 5.8 / 10.9 / 16.4 / 20.1 / 23.9 | 9.2 / 12.5 / 17.0 / 21.1 / 25.7 | 32.9 → 38.5 |

- Trials lift annual LTV in Utilities, Health & Fitness and Education. In Productivity, Lifestyle and Entertainment, direct buyers are worth more: Productivity annual $56.9 direct vs $49.1 with trial; Lifestyle trial users are ~21% less valuable (Sven Jürgens).
- **Top countries by median one-year LTV, $:** Switzerland 28.5 · Qatar 27.5 · Israel 27.0 · Iceland 23.9 · UK 23.6 · Japan 23.4 · Singapore 22.2 · UAE 21.8 · Australia 21.5 · Canada 20.9 · US 19.9 · Argentina 17.9 · Mexico 17.6 · Chile 15.3.
- **Median one-year install LTV (per install), $:** Health & Fitness 1.21 · Productivity 1.10 · Utilities 1.09 · Education 1.06 · Photo & Video 0.82 · Graphics & Design 0.78 · Lifestyle 0.70 · Entertainment 0.59.

## Pricing

**Price distribution by region, All Categories, $** (min / p25 / median / p75 / max):

| Year · plan | North America | Europe | LATAM | MEA | APAC |
|---|---|---|---|---|---|
| 2025 Weekly | 4.99 / 5.99 / 7.29 / 9.99 / 9.99 | 2.34 / 6.71 / 9.38 / 10.58 / 12.09 | 1.80 / 4.55 / 7.25 / 9.07 / 10.72 | 2.33 / 4.99 / 6.88 / 8.65 / 10.66 | 1.68 / 4.92 / 6.86 / 8.70 / 11.13 |
| 2025 Monthly | 4.99 / 9.99 / 12.99 / 14.99 / 29.99 | 4.54 / 9.40 / 14.07 / 20.16 / 26.90 | 1.83 / 3.64 / 8.09 / 10.95 / 13.99 | 1.40 / 3.97 / 9.32 / 12.49 / 16.29 | 1.74 / 3.34 / 6.39 / 12.05 / 15.39 |
| 2025 Annual | 20.00 / 30.00 / 39.99 / 49.99 / 69.99 | 21.15 / 28.19 / 41.17 / 53.83 / 82.14 | 13.00 / 18.26 / 30.00 / 43.85 / 55.08 | 10.55 / 18.00 / 30.44 / 42.33 / 54.46 | 14.02 / 22.33 / 33.57 / 47.70 / 62.04 |
| 2024 Weekly | 4.86 / 4.99 / 6.99 / 7.99 / 9.99 | 4.13 / 6.20 / 7.99 / 8.78 / 10.40 | 4.03 / 4.35 / 5.02 / 6.99 / 8.67 | 2.83 / 4.90 / 5.66 / 7.98 / 9.86 | 3.39 / 4.53 / 6.17 / 7.31 / 9.28 |
| 2024 Monthly | 5.49 / 9.99 / 11.99 / 13.99 / 19.99 | 4.16 / 7.78 / 11.30 / 14.49 / 20.69 | 1.95 / 4.17 / 8.07 / 11.56 / 14.71 | 2.66 / 5.68 / 8.99 / 11.97 / 13.86 | 2.25 / 5.24 / 8.97 / 12.33 / 13.57 |
| 2024 Annual | 20.00 / 27.84 / 35.00 / 48.55 / 74.27 | 18.00 / 23.81 / 36.33 / 46.92 / 72.87 | 14.72 / 19.99 / 29.10 / 40.22 / 49.45 | 7.65 / 16.46 / 28.28 / 41.18 / 53.21 | 14.32 / 20.94 / 31.35 / 44.54 / 62.15 |
| 2023 Weekly | 3.99 / 4.99 / 6.99 / 8.99 / 8.99 | 3.82 / 5.08 / 6.62 / 8.83 / 9.98 | 3.09 / 4.99 / 5.83 / 8.21 / 10.26 | 1.39 / 3.46 / 5.44 / 8.07 / 10.18 | 3.59 / 4.96 / 5.78 / 7.41 / 10.21 |
| 2023 Monthly | 4.99 / 9.79 / 11.99 / 14.99 / 19.99 | 4.43 / 7.25 / 11.45 / 14.64 / 22.20 | 3.69 / 5.80 / 10.28 / 14.08 / 20.16 | 3.39 / 5.33 / 10.18 / 11.99 / 12.80 | 2.84 / 5.96 / 10.98 / 13.28 / 20.22 |
| 2023 Annual | 20.00 / 27.51 / 39.99 / 45.00 / 69.99 | 16.56 / 22.29 / 32.65 / 49.74 / 69.99 | 15.00 / 20.60 / 23.52 / 39.99 / 52.86 | 6.28 / 9.18 / 16.97 / 34.66 / 50.89 | 12.22 / 20.00 / 31.79 / 42.49 / 68.50 |

- Callouts: European prices +18% YoY. Europe overtook North America as the most expensive region on all three plan lengths. Biggest jump: European Utilities annual, +70.5% over two years. Median annual costs ~3× the monthly price (annual subscribers save ~75%). Median prices rose 7–10% from 2023 to 2025, annual the most (Phil Carter).
- **Pricing index by country** (US = 1.0, All Categories): UK 1.2 · France 1.2 · Germany 1.2 · Italy 1.2 · Spain 1.2 · South Africa 1.1 · Mexico 1.0 · Saudi Arabia 1.0 · US 1.0 · Colombia 1.0 · Chile 1.0 · Canada 0.9 · Brazil 0.9 · Argentina 0.9 · Qatar 0.9 · South Korea 0.9 · UAE 0.9 · Australia 0.8 · Japan 0.8 · Indonesia 0.7 · Turkey 0.7 · India 0.6. Prices vary up to 4× across countries. Example from the report: Argentina weekly $7.06 vs UK $8.72 → UK 1.2.
- **One-year LTV by price bucket, $** (low / lower-mid / upper-mid / high): weekly 6.99 / 8.75 / 15.98 / 17.48 · monthly 6.99 / 10.11 / 14.99 / 19.99 · annual 19.99 / 32.57 / 39.99 / 59.99. High-price apps earn ~3× the LTV of low-price apps.
- **Conversion by price bucket, %** (same buckets): weekly 5.41 / 6.76 / 9.80 / 9.92 · monthly 0.60 / 0.62 / 0.34 / 0.50 · annual 2.65 / 2.24 / 1.83 / 3.40. The chart doesn't define the step; likely install→paid. Weekly converts 2–7× better than annual. Price doesn't hurt weekly conversion here.
- High-priced subscriptions drive 1.5–5× more revenue per install than low-priced ones, despite lower conversion (Phil Carter).

## Conversion, renewals and retention

**Conversion by user-journey stage, %** (All Categories, Global; renewal stages = share of paid subscribers reaching the nth renewal):

| Setup | Install→trial / →paid | Trial→paid | 1st | 2nd | 3rd | 4th | 5th | Refund |
|---|---|---|---|---|---|---|---|---|
| Trial · weekly | 11.2 | 27.8 | 59.2 | 45.1 | 37.1 | 31.6 | 27.6 | 8.3 |
| Trial · monthly | 11.2 | 45.0 | 48.0 | 32.1 | 24.2 | 19.3 | 15.8 | 14.9 |
| Trial · annual | 11.2 | 32.1 | 19.1 | 9.9 | – | – | – | 15.5 |
| Direct · weekly | 4.9 (install→paid) | – | 37.0 | 27.2 | 22.1 | 18.8 | 16.2 | 4.0 |
| Direct · monthly | 4.9 | – | 37.0 | 24.8 | 18.8 | 15.2 | 12.6 | 5.0 |
| Direct · annual | 4.9 | – | 17.7 | 10.0 | – | – | – | 8.5 |

Trials boost the first renewal by up to 60% (weekly 59.2% vs 37.0%). Refund-stage values come from this chart; revenue lost to refunds is a separate metric (below).

**Retention, % of subscribers still active** (Month 0 / 1 / 3 / 6 / 12, Global):
- Trial, All: annual 100 / 100 / 100 / 100 / 19.9 · monthly 100 / 51.8 / 33.3 / 22.4 / 14.2 · weekly 100 / 36.8 / 17.4 / 10.3 / 5.5
- Direct, All: annual 100 / 99.7 / 99.7 / 99.7 / 19.0 · monthly 100 / 38.6 / 23.9 / 15.6 / 9.4 · weekly 100 / 21.1 / 11.0 / 7.1 / 3.9
- Trials boost weekly one-year retention by ~43% (5.5 vs 3.9).
- Trial, by category (annual M12 · monthly M1/M3/M6/M12 · weekly M1/M3/M6/M12):
  - Health & Fitness 20.6 · 56.6/35.3/23.8/15.1 · 38.1/17.8/10.8/4.9
  - Education 19.4 · 54.5/32.7/20.7/12.1 · 37.6/17.5/10.3/5.3
  - Lifestyle 20.2 · 54.1/34.4/22.9/15.3 · 30.9/14.1/8.1/4.4
  - Photo & Video 17.2 · 51.1/34.3/23.9/16.0 · 34.0/17.5/10.8/6.2
  - Productivity 21.9 · 50.9/32.6/21.6/13.8 · 37.9/18.9/11.8/6.6
  - Utilities 22.2 · 48.3/30.0/19.7/11.3 · 38.7/17.8/10.2/5.3
  - Entertainment 18.1 · 42.1/27.5/18.2/12.4 · 31.9/14.3/8.1/4.3
  - Graphics & Design 18.7 · 46.1/31.2/23.1/15.8 · 32.6/15.0/9.1/5.0
  - The report says Productivity retains best overall (~14% after one year).

**Renewal rate by price bucket, %** (low / lower-mid / upper-mid / high):
- Weekly: paid→1st 48 / 46 / 47 / 54 · 1st→2nd 74 / 73 / 73 / 74 · 2nd→3rd 81 / 80 / 80 / 81
- Monthly: paid→1st 48 / 44 / 39 / 38 · 1st→2nd 68 / 66 / 62 / 60 · 2nd→3rd 74 / 73 / 70 / 69
- Higher-priced weekly retains ~12% better at the first renewal. On monthly it's the reverse: higher price, lower renewal.

**Revenue lost to refunds, %** (Global / North America / MEA / LATAM / Europe / APAC): with trial 3.69 / 3.53 / 3.06 / 4.27 / 3.19 / 5.26 · direct 3.11 / 3.00 / 2.51 / 4.81 / 3.00 / 3.40. The headline says refunds can cost up to 14% of subscription revenue in the worst segments.

**Timing, share by days since install** (Day 0 / 1–3 / 4–14 / 15–30 / 31+):

| Category | Install→trial | Install→paid |
|---|---|---|
| Education | 71.3 / 2.5 / 1.7 / 1.0 / 23.5 | 19.3 / 15.1 / 47.9 / 6.0 / 11.6 |
| Entertainment | 94.5 / 1.5 / 1.0 / 0.5 / 2.5 | 42.7 / 35.2 / 9.2 / 4.7 / 8.2 |
| Graphics & Design | 88.9 / 2.2 / 1.5 / 0.9 / 6.5 | 63.9 / 19.1 / 7.5 / 2.9 / 6.6 |
| Health & Fitness | 86.1 / 4.3 / 2.6 / 1.3 / 5.8 | 31.9 / 21.7 / 33.8 / 4.2 / 8.5 |
| Lifestyle | 88.6 / 3.0 / 2.0 / 1.1 / 5.3 | 42.7 / 31.6 / 9.1 / 4.9 / 11.6 |
| Photo & Video | 91.2 / 1.9 / 1.3 / 0.8 / 4.8 | 68.9 / 15.4 / 6.0 / 2.7 / 6.9 |
| Productivity | 89.1 / 2.1 / 1.6 / 1.0 / 6.1 | 47.9 / 32.1 / 7.5 / 4.1 / 8.6 |
| Utilities | 91.0 / 1.4 / 1.1 / 0.7 / 5.7 | 19.0 / 48.6 / 16.6 / 5.7 / 10.1 |

- All apps, trial activations: Day 0 89.37% · days 1–3 2.04% · 4–7 0.76% · 8–14 0.70% · 15–30 0.85% · 31+ 6.28%. ~90% of trial starts happen on Day 0, but only 44.5% of purchases do. Utilities buyers mostly pay on days 1–3 (3-day trials); Education and Health & Fitness on days 4–14 (7-day trials).

## Market trends

- **Revenue share by region:** 2023 North America 58.8 · Europe 21.9 · APAC 8.6 · MEA 5.6 · LATAM 5.1. 2024: 56.8 · 21.2 · APAC 9.5 · LATAM 6.2 · MEA 6.2. 2025: 55.6 · 21.3 · APAC 9.9 · LATAM 6.9 · MEA 6.2.
- **Fastest-growing markets** (revenue growth): Japan 88% · Mexico 82% · Turkey 70% · Brazil 58% · Australia 55% · Canada 54% · Netherlands 52% · Saudi Arabia 22%.
- **Revenue captured by the top 10% of apps** (2025): Lifestyle 97.9 · Education 96.0 · Productivity 95.6 · Photo & Video 94.6 · Graphics & Design 94.6 · All 94.5 (92.7 in 2023) · Entertainment 94.0 · Health & Fitness 92.6 · Utilities 92.6.
- **New apps:** +31% launches in 2025 while median monthly revenue per new app fell 22% ($627 → $492). First-year revenue distribution of new apps with any revenue: $1–1,000 57.7% · $1,001–10,000 22.4% · $10,001–100,000 12.0% · $100,001+ 7.9%.
- **Revenue share by plan** (weekly / monthly / annual / one-time): 2023 43.32 / 21.08 / 29.18 / 6.42 · 2024 51.48 / 14.97 / 25.73 / 7.83 · 2025 55.52 / 11.65 / 22.51 / 10.32.
- **Trial usage, % of apps with trial:** Education 82 · Entertainment 60 · Graphics & Design 58 · Health & Fitness 77 · Lifestyle 57 · Photo & Video 62 · Productivity 70 · Utilities 85. About 7 in 10 apps overall; stable over time.
- **Discount usage, % of subscriptions sold with a discount:** All 6.9 · Education 14.3 · Productivity 11.1 · Graphics & Design 10.9 · Health & Fitness 10.0 · Photo & Video 7.3 · Entertainment 5.7 · Lifestyle 4.2 · Utilities 1.2. About 9 in 10 subscriptions sell at full price.

## Paywalls and experiments

- **Experiment win rates** (% of tests that lifted LTV / conversion), 105,000 paywalls: locales 62.3 / 44.9 · number of plans 57.1 / 46.1 · plan duration 58.7 / 37.8 · trial 59.6 / 39.9 · price changes 45.5 / 28.3 · visual/text only 34.6 / 31.4. Price tests rarely improve conversion but lift LTV 46% of the time. Apps that test run 14.7 experiments on average. "Teams that experiment can make up to 40× more revenue" is a correlation.
- **Install→paid by placement:** with trial, onboarding 1.35% vs in-app 0.89%; without trial, onboarding 0.82% vs in-app 0.76%. Onboarding paywalls with trials convert best.
- **Hard vs soft paywall:** one-year LTV (p10 / p25 / median / p75 / p90, $): hard 4.99 / 7.99 / 24.0 / 55.9 / 89.9 · soft 4.99 / 8.99 / 20.0 / 41.9 / 70.0. Hard is +21% at the median; the gap sits at the top end. Paywall view→payment: soft 4.85% vs hard 3.34%.
- **Best setups** (illustrative examples in the report): weekly $5.99 with a 3-day free trial is the best; monthly around $18.99–19.99 with a 7-day trial does well; an annual $79.99 setup sits among the worst.

## iOS vs Android

- Revenue share: iOS 84.75% · Android 15.25% (iOS ~5.6×). Per Natalia Burakova, Android has ~70% of users.
- One-year LTV, $ (Android / iOS): weekly 8.47 / 10.34 · monthly 10.61 / 12.13 · annual 32.54 / 36.68. The weekly gap is the biggest (~18%).
- Install→paid, % (Android / iOS): weekly 0.26 / 1.55 · monthly 0.17 / 0.49 · annual 0.14 / 0.53. iOS converts ~3× better. Monthly install→paid reached parity in Entertainment.
- Advice (Burakova): weekly plans for APAC and LATAM; location-based pricing (Android users are more price-sensitive); upsell after value; test hard paywalls; Android matters for web2app funnels.

## AI apps

- Median conversion (all apps / AI apps): install→trial 10.92% / 5.31% · trial→paid 25.59% / 20.60% · install→direct purchase 3.71% / 4.20%. AI apps convert into trial ~2× worse.
- LTV, $ (month 0 / 1 / 3 / 6 / 12; all apps vs AI apps):
  - Weekly with trial: 7.4 / 19.0 / 33.1 / 43.2 / 54.5 vs 7.9 / 19.2 / 32.2 / 40.9 / 49.5
  - Weekly direct: 6.5 / 12.2 / 18.4 / 22.6 / 27.0 vs 7.2 / 13.2 / 19.8 / 24.2 / 28.7
  - Monthly with trial: 10.3 / 14.8 / 21.6 / 27.8 / 35.3 vs 15.2 / 21.8 / 32.4 / 43.5 / 56.2
  - Monthly direct: 10.6 / 14.2 / 19.4 / 24.1 / 29.7 vs 13.2 / 17.1 / 23.1 / 28.8 / 36.6
  - Annual with trial: 42.1 → 49.9 vs 55.1 → 66.7
  - Annual direct: 35.8 → 42.5 vs 42.5 → 49.2
  - AI apps earn the most on annual with trial (+35% vs direct).
- Median install LTV: all apps $0.84 · AI apps $1.44 (+70%).
- Retention, % (month 0 / 1 / 3 / 6 / 12; all apps vs AI apps; this chart's "all apps" baseline differs slightly from the main retention chart):
  - Weekly with trial: 100 / 39.1 / 19.6 / 12.0 / 6.0 vs 100 / 31.3 / 13.4 / 7.4 / 4.2
  - Weekly direct: 100 / 20.0 / 10.6 / 6.9 / 3.8 vs 100 / 16.0 / 8.3 / 5.3 / 2.8
  - Monthly with trial: 100 / 52.8 / 34.6 / 23.5 / 13.9 vs 100 / 48.4 / 31.2 / 20.5 / 12.7
  - Monthly direct: 100 / 43.9 / 29.4 / 20.5 / 13.1 vs 100 / 38.2 / 27.3 / 20.9 / 16.2
  - Annual with trial: M12 21.6 vs 23.3
  - Annual direct: M12 20.4 vs 15.7
  - AI apps churn faster but charge more, so LTV still comes out ahead.
- AI app revenue growth, 2025 vs 2024: Lifestyle 691% · Graphics & Design 202% · Utilities 174% · Productivity 173% · Photo & Video 151% · Entertainment 113% · Education 81% · Health & Fitness 69%.

## Web paywalls (early data; US web paywalls since mid-2025)

- Install→paid: in-app 1.60% vs web 1.10% (in-app +45%).
- Retention, month 0 / 1 / 3 / 6: web 100 / 64.5 / 40.7 / 19.9 · in-app 100 / 46.2 / 34.4 / 29.6. Web starts higher and drops faster.
- Average LTV, $, month 0 / 1 / 3 / 6: in-app 38.7 / 40.1 / 42.0 / 43.2 · web 33.9 / 35.8 / 38.5 / 40.7. Web paywalls don't close the LTV gap, even without store fees.
- This is a **plain web paywall**, not a full web2app funnel. FunnelFox's CEO argues in the report that structured web2app funnels perform differently; see the FunnelFox skill if installed.

## Expert takeaways (paraphrased)

- Sven Jürgens: "always offer a free trial" is bad advice. In some categories trials filter for quality; in others (Productivity, Lifestyle) they attract worse subscribers.
- Hannah Parvaz (Aperture): conversion is a belief problem, not a price problem. Let users experience value before the paywall, add positive friction (questions, personalization), and show the paywall right after progress. 77% of users never return after day one.
- Sylvain Gauchet (Reading.com): niche down within competitive categories. Test base price more than discounts, plus weekly plans and trial vs no-trial, and watch retention. Localize for Japan, Mexico and Turkey.
- Steve P. Young (App Masters): the first session is the whole game. Discount only when a user is close to converting.
- Phil Carter (Elemental Growth): pricing optimization adds 5–15% revenue. Use Van Westendorp, Gabor-Granger and in-product price tests; this matters most for AI apps with LLM costs.
- Vahe Baghdasaryan (Tangent): stop starting with visuals. Test trial, placement and number of plans first, and test continuously.
- Natalia Burakova: Android monetization gap is closing (see the iOS vs Android section).
