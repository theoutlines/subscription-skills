---
name: subscription-benchmarks
description: Router for subscription-app benchmark questions (conversion, trials, pricing, LTV, retention, paywalls, web2app, store compliance). Picks the right report skill, keeps metric definitions apart, and combines sources without mixing denominators. Use for any "is X good / what's normal / what should we test" question about subscription monetization.
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
| `subscription-pricing-index` | Adapty Pricing Index | **Localized price points** for weekly, monthly and annual plans in 64 countries vs the US |
| `paywall-store-compliance` | Apple and Google rules | Will this paywall, trial or cancel flow pass App Review or Play policy? |
| `paywall-teardown` (by Adapty, bundled) | Paywall pattern library + 100-point rubric | Score a paywall screenshot across 6 dimensions, ranked A/B test ideas, annotated report card |
| `paywall-ab-test-assistant` (by Adapty, bundled) | Evidence library of A/B tests run on Adapty | Grade one test idea, rank a test backlog, or find where to start, with an evidence-strength label for each answer |

If a listed skill isn't installed, say which one would answer the question and answer from the others.

`paywall-teardown` and `paywall-ab-test-assistant` are by Adapty (MIT) and ship in this plugin. `state-of-paywalls-2026-by-adapty` is installed separately: https://github.com/vkharlan-adapt/state-of-paywalls-2026-skill

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
| "Should we move purchases to web?" | **FunnelFox** | Adapty In-App (web paywalls) |
| "LTV window: is D7 enough to judge?" | Adapty In-App (LTV curves by month) | SOSA (realized LTV) |
| "Will this paywall get rejected?" | **paywall-store-compliance** | paywall-teardown or State of Paywalls for conversion impact |
| "Full paywall review" | **paywall-teardown** (score + test ideas) **and** paywall-store-compliance (rules) | State of Paywalls (conversion benchmarks), Pricing Index (the prices shown) |
| "Is this A/B test idea worth running?" / "Rank our test backlog" | **paywall-ab-test-assistant** | The report skill that covers the metric the test should move |

## Metric definitions: never mix denominators

| Metric as people say it | RevenueCat SOSA | Adapty In-App | Adapty Paywalls | FunnelFox |
|---|---|---|---|---|
| "Conversion" | per **install** (D35 download→paid) or per **trial start** | per **install** (install→trial, install→paid; per-app averages) | per **paywall view** | per **web funnel visitor / step** |
| "Trial conversion" | trial→paid | trial→paid | trial→paid | web trial→paid |
| "LTV" | realized LTV per payer (net) | LTV per **install** or per payer, by month (gross) | — | web vs app LTV |
| "Price" | average price by tier | price distributions (box plots) | price shown on paywalls | web prices and price index |
| Revenue basis | net of store fees and refunds (realized) | gross | — | web gross |

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
2. Suggest 2–3 tests, ranked by expected impact. Cite the benchmark delta behind each one. For example: "a 7-day trial instead of 3 days: trial→paid is 37.4% for 5–9-day trials vs 25.5% for trials of 4 days or less (SOSA)".
3. If `paywall-ab-test-assistant` is installed, grade each idea with it and show its evidence-strength label next to the benchmark delta.
4. Run every proposed paywall change through `paywall-store-compliance` before recommending it.
