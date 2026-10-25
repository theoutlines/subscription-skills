---
name: subscription-benchmarks
description: Router for subscription-app benchmark questions (conversion, trials, pricing, LTV, retention, paywalls, web2app, Apple Ads, store compliance). Picks the right report skill, keeps metric definitions apart, and combines sources without mixing denominators. Use for any "is X good / what's normal / what should we test" question about subscription monetization.
---

# Subscription benchmarks — router

Use this skill to decide **which benchmark source answers the question**, and how to combine sources safely. Then load and answer from the specific skill or skills.

## Available skills

| Skill | Source | Best for |
|---|---|---|
| `state-of-subscription-apps-2026` | RevenueCat SOSA 2026 | The broadest funnel benchmarks by category, region and price tier: download→trial, trial→paid, D35 download→paid, RPI, realized LTV, retention, renewals, refunds, reactivation, AI vs non-AI |
| `state-of-in-app-subscriptions-2026` | Adapty, State of In-App Subscriptions 2026 | LTV curves (trial vs direct), retention by plan length, price distributions by region, renewal by price bucket, refunds, paywall placement and type, iOS vs Android, AI apps, web paywalls |
| `state-of-paywalls-2026-by-adapty` | Adapty, State of Paywalls 2026 | **Paywall-level** conversion, paywall design patterns, A/B test ideas, paywall screenshot audits |
| `state-of-web2app-2026` | FunnelFox, State of Web2App 2026 | Web funnels: adoption, funnel conversion, web pricing, upsells, web vs app LTV, payment methods, failures and retries |
| `adapty-pricing-index` | Adapty Pricing Index | **Localized price points** for weekly, monthly and annual plans in 64 countries vs the US |
| `apple-ads-subscription-apps-2026` | Adapty, Apple Ads 2026 | Apple Ads funnel by country and niche, CPT/CPA/TTR/CR, cost per payer vs LTV, CPP and keyword-matched paywall uplift |
| `state-of-app-monetization-2026` | AppsFlyer | Subscription vs IAP vs ads growth, D90 ARPU/ARPPU, revenue timing, paid vs organic share, hybrid monetization (skews to gaming) |
| `paywall-store-compliance` | Apple and Google rules | Will this paywall, trial or cancel flow pass App Review or Play policy? |

If a listed skill isn't installed, say which one would answer the question and answer from the others.

## Routing table

| Question type | Primary skill | Cross-check with |
|---|---|---|
| "Is our trial→paid / trial start rate good?" | SOSA | Adapty In-App (trial vs direct LTV) |
| "Paywall conversion is X%. Is that good?" | **State of Paywalls** (per paywall view) | SOSA only if the user means per install |
| "What should our price be in country X?" | **Pricing Index** | Adapty In-App (price box plots by region), SOSA (price tier vs conversion) |
| "Weekly vs monthly vs annual: which plan to push?" | Adapty In-App (LTV and retention by plan) | SOSA (plan mix, retention), Pricing Index (local plan ladder) |
| "Trial length: 3 vs 7 days?" | SOSA | Adapty In-App |
| "Hard paywall vs freemium?" | SOSA (access method), Adapty In-App (hard vs soft) | State of Paywalls |
| "Onboarding paywall vs contextual placement?" | Adapty In-App (placement), State of Paywalls | — |
| "Expected refund rate / renewal rate / churn?" | SOSA | Adapty In-App, FunnelFox (web) |
| "Should we move purchases to web?" | **FunnelFox** | Adapty In-App (web paywalls), AppsFlyer (organic share) |
| "Which countries to buy Apple Ads in?" | **Apple Ads** | Pricing Index (what users pay there), SOSA region LTV |
| "LTV window: is D7 enough to judge?" | AppsFlyer (revenue timing) | Adapty In-App (LTV curves) |
| "Will this paywall get rejected?" | **paywall-store-compliance** | State of Paywalls for conversion impact |
| "Full paywall review" | paywall-store-compliance **and** State of Paywalls | Pricing Index for the prices shown |

## Metric definitions: never mix denominators

| Metric as people say it | RevenueCat SOSA | Adapty In-App | Adapty Paywalls | FunnelFox | AppsFlyer | Adapty Apple Ads |
|---|---|---|---|---|---|---|
| "Conversion" | per **install** (D35 download→paid) or per **trial start** | per **install** (install→trial, install→paid; per-app averages) | per **paywall view** | per **web funnel visitor / step** | per **installer**, buyers within 30 days (incl. one-time IAP) | App Store **tap→download** (CR); in-app install→trial / paid |
| "Trial conversion" | trial→paid | trial→paid | trial→paid | web trial→paid | — | trial→paid (relative uplift only) |
| "LTV" | realized LTV per payer (net) | LTV per **install** or per payer, by month (gross) | — | web vs app LTV | D90 ARPU (per installer) / ARPPU (per payer), store-only | year-1 LTV per paying user from Apple Ads |
| "Price" | average price by tier | price distributions (box plots) | price shown on paywalls | web prices and price index | — | — |
| Revenue basis | net of store fees and refunds (realized) | gross | — | web gross | gross store revenue | — |

**Rules**
1. Quote each number with its **source and denominator**. For example: "trial→paid 39.7% (SOSA, H&F, North America median)".
2. **Never average or compare** numbers across sources as if they were the same metric. An 8% paywall-view conversion (Adapty) is not comparable to a 2% install→paid (SOSA).
3. When sources disagree on the same metric, show both ranges and explain why: different samples (RevenueCat vs Adapty customers), medians vs means, gross vs net, iOS-heavy samples.
4. Prefer **medians and percentiles** over averages when the user benchmarks a single app. Place their number in a quartile.
5. Category names differ between sources. Map them explicitly. For example, a music-creation app is "Media & Entertainment" or "Productivity" in SOSA, but "Entertainment" or "Utilities" elsewhere. Say which bucket you used.
6. Regions differ too. SOSA "Western Europe" ≠ Adapty "Europe" ≠ Pricing Index "Europe" (which includes Eastern Europe).

## Answer pattern for "is our number good?"

1. Restate the user's metric with its denominator. If it's ambiguous, ask one question or pick the most likely definition and say so.
2. Pull the closest segment (category × region × plan) from the primary skill, with p25, median and p75 where available.
3. Place their number: below p25, p25–median, median–p75, or above p75.
4. Cross-check with one secondary source, labeled as a different definition.
5. Give **one lever** to pull, with the benchmark that supports it. For example, trial length or price tier.

## Answer pattern for "what should we test?"

1. Find the gap: the user's metric versus the benchmark median.
2. Suggest 2–3 tests, ranked by expected impact. Cite the benchmark delta behind each one. For example: "tailored paywall by keyword: +41.5% install→trial (Adapty Apple Ads)".
3. Run every proposed paywall change through `paywall-store-compliance` before recommending it.
