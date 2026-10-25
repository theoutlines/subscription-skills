# Subscription Skills for Claude

Claude skills for **subscription-app monetization**: benchmarks from the 2026 industry reports, localized pricing, Apple Ads economics, a router that keeps metric definitions apart, and a paywall review against App Store and Google Play rules.

Made by a monetization design lead for day-to-day work on paywalls, onboarding, pricing and growth experiments.

## What's inside

| Skill | What it answers | Source |
|---|---|---|
| `subscription-benchmarks` | **Start here.** Routes a question to the right report and keeps denominators apart (per install vs per paywall view vs per web visitor) | — |
| `state-of-subscription-apps-2026` | Download→trial, trial→paid, RPI, LTV, retention, renewals and refunds, by category, region and price tier | [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps) |
| `state-of-in-app-subscriptions-2026` | LTV curves, retention by plan, prices by region, trial vs direct, paywall placement, iOS vs Android, AI apps | [Adapty](https://adapty.io/state-of-in-app-subscriptions-report/) |
| `state-of-web2app-2026` | Web funnels: conversion, web pricing, upsells, web vs app LTV, payments | [FunnelFox](https://funnelfox.com/state-of-web2app-2026) |
| `state-of-app-monetization-2026` | Subscription vs IAP vs ads growth, D90 ARPU/ARPPU, revenue timing, paid vs organic | [AppsFlyer](https://www.appsflyer.com/resources/reports/app-marketing-monetization-report/) |
| `adapty-pricing-index` | Weekly, monthly and annual prices in 64 countries vs the US | [Adapty Pricing Index](https://adapty.io/app-subscription-pricing-index/) |
| `apple-ads-subscription-apps-2026` | Apple Ads funnel, cost per payer vs LTV by country, 59-niche benchmarks, CPP and tailored-paywall uplift | [Adapty Apple Ads](https://adapty.io/apple-ads-for-subscription-apps/) |
| `paywall-store-compliance` | Will this paywall, trial or cancel flow pass App Review and Play policy? Gives a check-by-check table with fixes | Apple Guidelines, HIG, Google Play policy |

Also pairs well with [Adapty's State of Paywalls 2026 skill](https://github.com/vkharlan-adapt/state-of-paywalls-2026-skill), which covers paywall-level conversion and design audits.

## Install

**Claude Code: everything in one plugin**

```
/plugin marketplace add theoutlines/subscription-skills
/plugin install subscription-skills@theoutlines-subscription-skills
```

**Any agent (Claude Code, Cursor, Codex and others) via the [skills CLI](https://skills.sh):**

```
npx skills add theoutlines/subscription-skills
```

**Claude.ai / Claude desktop:** download this repo, zip each folder in `plugins/subscription-skills/skills/` separately, and upload each one in Settings → Capabilities → Skills.

**Just one skill?** Each skill also has its own repo:

- [state-of-subscription-apps-2026-skill](https://github.com/theoutlines/state-of-subscription-apps-2026-skill)
- [state-of-in-app-subscriptions-2026-skill](https://github.com/theoutlines/state-of-in-app-subscriptions-2026-skill)
- [state-of-web2app-2026-skill](https://github.com/theoutlines/state-of-web2app-2026-skill)
- [state-of-app-monetization-2026-skill](https://github.com/theoutlines/state-of-app-monetization-2026-skill)
- [adapty-pricing-index-skill](https://github.com/theoutlines/adapty-pricing-index-skill)
- [apple-ads-subscription-apps-2026-skill](https://github.com/theoutlines/apple-ads-subscription-apps-2026-skill)
- [paywall-store-compliance-skill](https://github.com/theoutlines/paywall-store-compliance-skill)
- [subscription-benchmarks-skill](https://github.com/theoutlines/subscription-benchmarks-skill)

## Example prompts

- "Our H&F app: trial→paid 31%, annual $49.99, mostly US. How do we compare, and what should we test first?"
- "What should our $9.99/month plan cost in Brazil, Germany and Japan?"
- "Review this paywall screenshot for App Store and Google Play compliance."
- "Is Apple Ads worth it in Brazil vs the US for an app with a $30 year-1 LTV?"
- "Should we move checkout to web? What do the benchmarks say about web vs app LTV?"

## Accuracy and attribution

- **Unofficial.** Not made or endorsed by RevenueCat, Adapty, FunnelFox, AppsFlyer, Apple or Google. All report data and findings belong to their publishers. Get the original reports from the links above.
- Every number was transcribed from the source and cross-checked. Each skill has an **Errata** section listing places where a report's text contradicts its own charts. The skills quote the chart.
- The compliance skill is not legal advice. Store rules change, so check the linked sources for borderline calls.

Found a mistake? Open an issue.

## Maintainers

The bundled skills are copies of the standalone repos. To update, run `scripts/sync.sh`, bump the version in both manifests, and commit.
