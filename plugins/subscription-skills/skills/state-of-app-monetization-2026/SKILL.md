---
name: state-of-app-monetization-2026
description: Answer questions from AppsFlyer's State of App Monetization 2026 report: subscription vs IAP vs ad revenue growth, Day 90 ARPU/ARPPU by gaming genre and region, revenue timing curves (Day 1–60), paid vs organic revenue share by region, monetization model mix, and one-time vs repeat buyer conversion by category and region.
---

# State of App Monetization 2026 (AppsFlyer) — unofficial skill

Source: AppsFlyer, *The State of App Monetization – 2026 Edition* — https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/
Unofficial. Not made or endorsed by AppsFlyer. All data belongs to AppsFlyer.

## How to answer

- Cite the number with its exact definition (ARPU vs ARPPU, Day 90 vs Day 60, revenue share vs share of apps vs share of accounts). The report mixes per-install, per-payer and per-account metrics.
- **Text vs chart.** When the report's prose and its own charts or tables disagree: if the text is provably wrong (the arithmetic doesn't work, it copies another section's numbers, or it contradicts the report's own table), use the data value and say the text is in error. Otherwise give both: the text figure first, as the publisher's stated number, then the chart value, and say they differ. Don't silently pick one. See Errata. The biggest gap is the gaming monetization mix.
- AppsFlyer is an attribution platform (MMP). The sample skews toward apps buying paid UA and toward **gaming**: IAA revenue in the sample is ~4× IAP+IAS combined. Say so when someone generalizes to subscription apps.
- IAP and IAS figures are **store revenue only** (App Store + Google Play). Web payments are excluded.
- Subscription specifics (trial conversion, prices, renewals, churn) are **not** in this report. Point to RevenueCat SOSA, Adapty or FunnelFox benchmarks for those.
- Values marked "measured" were read from chart geometry (no data labels) and are accurate to about ±1pp. All other chart values are the chart's own labels.

## Methodology

- Period: January 2025 – March 2026 (15 months). YoY compares Q1 2026 with Q1 2025.
- Sample:
  - $900M verified IAP store revenue
  - $800M verified IAS (in-app subscription) store revenue
  - $7.2B IAA (in-app advertising) revenue
- Anonymous and aggregated. Values are shown only when they meet volume thresholds, which is why some region × genre cells are missing.
- Stream definitions:
  - IAP = one-time in-app purchases
  - IAS = in-app subscriptions
  - IAA = in-app advertising
  - Hybrid = more than one stream
- Gaming genres: Casino, Casual, Midcore, Hypercasual. Non-gaming is one bucket. Subscription-heavy categories named: health & fitness, productivity, education, generative AI, photo & video, utilities, news.
- Regions:
  - Charts use Global, North America & Europe (NA+Europe), APAC and LATAM.
  - The buyer chart splits North America and Europe.
  - The text also mentions MEA.
- Metric definitions:
  - ARPU = revenue per installer within N days of install.
  - ARPPU = revenue per paying user within N days.
  - One-time buyer = at least 1 purchase within 30 days of install.
  - Repeat buyer = at least 2 purchases within 30 days of install.

## Key findings (headline)

1. Subscription revenue grew **+105% YoY**; IAP grew +29%, IAA +14%. **71%** of subscription accounts grew, vs 57% for IAA and 53% for IAP.
2. Casino D90 IAP ARPU is **$2.43**, nearly double Casual ($1.34).
3. IAA earns ~**89%** of its Day 60 revenue by Day 7. IAS earns only ~52% by Day 7 and ~81% by Day 30.
4. Paid installs drive the majority of gaming IAP revenue. Non-gaming subscription revenue is **~70% organic**.
5. **16%** of non-gaming apps monetize via subscriptions: 10% IAS only plus 6% IAS+IAP. Text: 15.6% = 10.2% + 5.4%.
6. **9.84%** of non-gaming installers buy within 30 days. Gaming converts fewer, but its payers are more likely to buy again.

## 1. Revenue growth by stream

| Metric | IAS | IAP | IAA |
|---|---|---|---|
| Revenue growth Q1 2026 vs Q1 2025 | **+105%** | +29% | +14% |
| Accounts that grew YoY | **71%** | 53% | 57% |
| Accounts that declined YoY | 29% | 47% | 43% |

**Normalized monthly trend** (measured, ±0.1pp). Each value is that month's share of the stream's own 15-month total, so the lines show shape, not size.

| Month | IAA | IAS | IAP |
|---|---|---|---|
| 2025-01 | 6.2 | 4.1 | 6.1 |
| 2025-02 | 5.7 | **4.0** (low) | **5.3** (low) |
| 2025-03 | 6.6 | 4.8 | 5.9 |
| 2025-04 | 5.9 | 5.2 | 6.0 |
| 2025-05 | 6.5 | 5.7 | 6.8 |
| 2025-06 | 6.4 | 5.5 | 6.6 |
| 2025-07 | 6.7 | 6.2 | 6.6 |
| 2025-08 | 6.7 | 6.7 | 6.6 |
| 2025-09 | 6.5 | 7.2 | 7.0 |
| 2025-10 | 6.9 | 7.7 | 7.4 |
| 2025-11 | 7.3 | 7.8 | 6.5 |
| 2025-12 | **7.8** (peak) | 8.5 | 7.1 |
| 2026-01 | 7.4 | **9.6** (peak) | 7.3 |
| 2026-02 | 6.6 | 8.3 | 6.8 |
| 2026-03 | 7.2 | 8.7 | **8.1** (peak) |

Text values for the same points: IAS low 4.1% (Feb 2025), IAS peak 9.7% (Jan 2026, +136%), IAA peak 7.8%, IAP peak 8.1%, IAP low 5.3%. IAS more than doubled its monthly run-rate across the period. IAA and IAP stayed roughly flat with seasonality.

**Revenue mix in apps with all three streams** (cohort skews gaming; measured from stacked bars, ±0.3pp):

| Month | IAA | IAP | IAS |
|---|---|---|---|
| 2025-01 | 60.8% | 35.4% | 3.7% |
| 2025-03 | 63.0% | 33.1% | 4.0% |
| 2025-06 | 61.4% | 34.1% | 4.5% |
| 2025-09 | 59.3% | 35.4% | 5.3% |
| 2025-12 | 60.3% | 33.6% | 6.1% |
| 2026-01 | 57.1% | 36.0% | 6.9% |
| 2026-03 | 56.3% | 37.0% | 6.6% |

- IAS share nearly doubles, from ~4% to ~7%.
- IAA loses ~4–7pp.
- IAP holds at ~33–37%.
- The text rounds these as IAA 63% → 56–57% and IAP ~35%. The chart starts IAA at ~61%; 63% is the March 2025 peak.

## 2. ARPU and ARPPU (Day 90)

| Genre | IAP ARPU Global | IAP ARPU NA+Europe | IAP ARPPU Global | IAP ARPPU NA+Europe | IAA ARPU Global | IAA ARPU NA+Europe |
|---|---|---|---|---|---|---|
| Casino | **$2.43** | $2.55 | **$11.40** | $11.76 | $0.47 | $0.54 |
| Midcore | $2.13 | **$2.66** | $9.80 | $9.97 | $0.40 | $0.45 |
| Casual | $1.34 | $1.63 | $7.26 | $7.68 | **$0.55** | **$0.65** |
| Hypercasual | — | — | — | — | $0.22 | $0.28 |
| Non-gaming | $2.32 (IAS) | $2.79 (IAS) | **$10.85** (IAS) | $11.78 (IAS) | $0.29 | $0.37 |

**Reading the gaps**
- Casino vs Casual, globally: ARPU is +81% higher, ARPPU only +57%. Casino's lead comes as much from conversion as from spend per payer.
- Non-gaming subscription ARPPU ($10.85) is on par with Casino and above Midcore.
  - Its per-install value is $2.32 globally ($2.79 in NA+Europe).
  - That is close to the top gaming genres.

**NA+Europe premium over global**

| Genre | IAP ARPU | ARPPU |
|---|---|---|
| Casual | +22% | +6% |
| Midcore | **+25%** | +2% |
| Casino | only **+5%** | +3% |
| Non-gaming IAS | +20% | +9% |

- The regional ARPU gap is mostly conversion rate, not spend per payer.
- **Exception: Casino.** Casino earns nearly the same everywhere.
- **In NA+Europe, Midcore ($2.66) out-earns Casino ($2.55) per install.** Globally, Casino leads.

IAA ARPU ranks Casual first. Ad revenue per install is roughly 20–40% of IAP ARPU in gaming.

## 3. Revenue timing (cumulative share of Day 60 revenue)

Measured from line charts (±1pp), calibrated so Day 60 = 100%. The calibrated values reproduce every number stated in the text.

| Segment | Stream | D1 | D3 | D7 | D14 | D30 |
|---|---|---|---|---|---|---|
| **All apps** | IAA | **57** | 78 | **89–90** | 96 | 99 |
| | IAP | 38 | 48 | 60 | 72 | 88 |
| | IAS | 28 | 42 | 52 | 64 | 81 |
| **All gaming** | IAA | 57 | 78 | 89 | 96 | 99 |
| | IAP | 32 | 42 | 55 | 68 | 87 |
| | IAS | **21** | 32 | 42 | 56 | 77 |
| Hypercasual | IAA | **63** | 82 | 92 | 97 | 100 |
| | IAP | 38 | 48 | 61 | 74 | 90 |
| | IAS | 11 | 28 | 36 | 52 | 76 |
| Casual | IAA | 52 | 74 | 87 | 94 | 98 |
| | IAP | 32 | 41 | 54 | 67 | 85 |
| | IAS | 29 | 38 | 50 | 63 | 82 |
| Midcore | IAA | 54 | 76 | 88 | 96 | 99 |
| | IAP | 30 | 41 | 55 | 70 | 88 |
| | IAS | 24 | 33 | 42 | 55 | 74 |
| Casino | IAA | 52 | 74 | 87 | 95 | 99 |
| | IAP | **23** | 32 | 46 | 62 | 84 |
| | IAS | 21 | 29 | 42 | 57 | 75 |
| **All non-gaming** | IAA | 56 | 75 | 87 | 95 | 99 |
| | IAP | **70** | 76 | 81 | 87 | 95 |
| | IAS | 33 | 46 | 60 | 71 | 85 |

**Readings**
- **Ads mature fastest.** Day 7 LTV is a fair proxy for Day 60 IAA, but it understates IAP and especially IAS.
- **Non-gaming IAP is front-loaded.** 70% of its Day 60 revenue arrives on Day 1: one-off unlocks and lifetime purchases right after install.
- **Non-gaming IAS reaches 60% by Day 7 and 85% by Day 30.** It is faster than gaming IAS (42% / 77%), but still back-loaded vs ads.
  - The curve averages two models.
  - Hard paywalls at first launch give a high Day 1 share.
  - Trial-first apps give a low Day 1 share.
- **Gaming subscriptions need play time first:** IAS is only 21% on Day 1 and 42% by Day 7.
- The text says the timing pattern holds in all five regions. The model, not geography, drives timing.
- Revenue is still growing at Day 60 for IAS, so these are shares of D60, not of lifetime value.

## 4. Paid vs organic revenue share

**Gaming IAP**, organic / paid:

| Genre | Global | NA+Europe | APAC | LATAM |
|---|---|---|---|---|
| Hypercasual | 21 / **79** | 21 / 79 | 26 / 74 | — |
| Casino | 37 / 63 | 38 / 62 | — | — |
| Casual | 39 / 61 | 37 / 63 | 41 / 59 | **63 / 37** |
| Midcore | 51 / 49 | 49 / 51 | 54 / 46 | 57 / 43 |

- The text gives gaming IAP overall as **59% paid**.
- In LATAM, paid and organic flip: UA budgets concentrate in NA+Europe.
- Midcore is the most organic genre (community, word of mouth).

**Non-gaming IAS**, organic / paid:

| Global | NA+Europe | APAC | LATAM |
|---|---|---|---|
| **71 / 29** | 69 / 31 | 76 / 24 | 68 / 32 |

- The text rounds this to 70/30 and says MEA is 80% organic. The chart has no MEA tab.
- Subscription decisions are deliberate and intent-led: people search for a specific meditation or invoicing app.
- AppsFlyer's takeaway: organic payers show **higher per-user revenue than paid** in most non-gaming categories, so prioritize ASO and brand alongside paid UA.

## 5. Monetization model mix (share of apps)

**Gaming** (chart):

| Genre | IAP only | IAA only | Hybrid |
|---|---|---|---|
| Gaming overall | 43% | 28% | 29% |
| Midcore | **81%** | 4% | 15% |
| Casino | 68% | 12% | 20% |
| Casual | 38% | 27% | **35%** |
| Hypercasual | 9% | **55%** | 36% |

The text gives different values; see Errata. Give the text figure and the chart figure together. The direction is the same in both:
- Midcore is the most IAP-led genre.
- Hypercasual is the most IAA-led.
- Casual is the most diversified.
- Hybrid is growing everywhere.

**Non-gaming** (apps with purchase or subscription revenue):

| IAP only | IAS only | IAP + IAS |
|---|---|---|
| 84% | **10%** | 6% |

- That means **16%** use subscriptions; the text says 15.6% = 10.2% + 5.4%.
- IAS penetration is highest in health & fitness, productivity, education, generative AI, and photo & video.
- Subscriptions are largely untapped in gaming. IAP+IAS hybrids are gaining in Casual, Generative AI, and Health & Fitness.

## 6. Buyer conversion within 30 days of install

| Segment | One-time buyers | Repeat buyers | Ratio |
|---|---|---|---|
| Non-gaming | **9.84%** | 4.64% | 2.12× |
| Casino | 4.95% | 3.01% | **1.65×** |
| Midcore | 3.89% | 2.20% | 1.76× |
| Casual | 2.22% | 1.18% | 1.89× |
| North America | **11.14%** | **5.08%** | 2.19× |
| Europe | 9.24% | 4.71% | 1.96× |
| APAC | 8.36% | 3.64% | 2.30× |
| LATAM | 6.51% | 3.09% | 2.11× |

- Midcore, Casual and Europe/APAC values are measured from bars (±0.05pp). All others match the text exactly.
- Non-gaming converts **2–4.5× more installers** to buyers than gaming genres.
- Gaming payers are more likely to come back. Casino is tightest: about 61% of first-time buyers buy again.
- First-purchase conversion tracks spending power and market maturity, from NA 11.1% down to LATAM 6.5%.
- The repeat ratio is roughly stable at 2.0–2.3×. The text says "~2.1× in all four regions".

## Key takeaways (AppsFlyer's)

1. **Evaluate subscription as a revenue layer.** It is growing at multiples of IAP and IAA, and 71% of subscription accounts grew.
2. **Calibrate LTV windows by model.** IAA is ~90% complete by Day 7; IAS is ~52%. One shared window undervalues the slower streams.
3. **Invest in organic for subscription apps.** About 70% of non-gaming IAS revenue is organic.
4. **Activate repeat buyers.** Design post-purchase mechanics for a second transaction, especially in high-session-frequency formats.
5. **Explore hybrid monetization.** Layer IAA and IAP; Midcore and Casino are mostly single-stream.

## Using with other benchmarks

- For subscription funnel metrics (trial → paid, price, retention, refunds), use RevenueCat SOSA 2026, Adapty State of In-App Subscriptions 2026 or FunnelFox State of Web2App 2026.
- AppsFlyer's IAS ARPPU ($10.85, D90, store-only, per paying user) is **not** comparable to RevenueCat's realized LTV or Adapty's LTV per payer. The windows and definitions differ.

## Errata / inconsistencies in the report

1. **Gaming monetization mix:** text and chart disagree, and neither is provably wrong. Give both.

   | Genre | Text | Chart |
   |---|---|---|
   | Midcore | 90% IAP only | 81% |
   | Casino | 83% IAP | 68% IAP only, plus 20% hybrid |
   | Casual | IAP 47 / IAA 28 / Hybrid 21 | 38 / 27 / 35 |
   | Hypercasual | 79% IAA only | 55% |

2. **Paid share, Casino and Casual:**
   - The text says Casino 64% and Casual 61% paid, "in NA+Europe" in one place and globally in another.
   - The chart: Global Casino 63% / Casual 61%; NA+Europe Casino 62% / Casual 63%.
3. **NA+Europe ARPU premium:** the text says "20–25% above global across all categories". Casino is only +5% ($2.55 vs $2.43).
4. **Multi-stream IAA share:** the key findings say 63% → 57%; the body says → ~56%. The chart reads ~61% (Jan 2025) → ~56% (Mar 2026), with 63% only in Mar 2025.
5. **IAS timing:** the headline "IAS takes until Day 30" means IAS reaches ~81% by Day 30 vs IAA's ~89% by Day 7. It never matches IAA's Day 7 level before Day 30.
6. **Non-gaming IAS organic share:** 70% in the text, 71% in the chart. MEA (80% in the text) is not in the chart.
7. **Repeat ratio:** "~2.1× in all four regions" is really 1.96× (Europe) to 2.30× (APAC).
