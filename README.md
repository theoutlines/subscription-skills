<p align="center"><img src=".github/assets/character.png" alt="Subscription Skills character" width="240"></p>

# Subscription Skills for Claude

Claude skills for **subscription-app monetization**: benchmarks from the 2026 industry reports, localized pricing, a router that keeps metric definitions apart, a paywall teardown and A/B test assistant, and a paywall review against App Store and Google Play rules.

Made by a monetization design lead for day-to-day work on paywalls, onboarding, pricing and growth experiments.

**Works with:** Claude Code as a one-install plugin, the Claude app (upload each skill), and any agent that supports the open [Agent Skills](https://agentskills.io) format, such as Codex, Gemini CLI, Cursor and GitHub Copilot. See [Install](#install).

## What's inside

| Skill | What it answers | Source |
|---|---|---|
| `subscription-benchmarks` | **Start here.** Routes a question to the right report and keeps denominators apart (per install vs per paywall view vs per web visitor) | — |
| `state-of-subscription-apps-2026` | Download→trial, trial→paid, RPI, LTV, retention, renewals and refunds, by category, region and price tier | [RevenueCat SOSA 2026](https://www.revenuecat.com/state-of-subscription-apps) |
| `state-of-in-app-subscriptions-2026` | LTV curves, retention by plan, prices by region, trial vs direct, paywall placement, iOS vs Android, AI apps | [Adapty](https://adapty.io/state-of-in-app-subscriptions-report/) |
| `state-of-web2app-2026` | Web funnels: conversion, web pricing, upsells, web vs app LTV, payments | [FunnelFox](https://funnelfox.com/state-of-web2app-2026) |
| `subscription-pricing-index` | Weekly, monthly and annual prices in 64 countries vs the US | [Adapty Pricing Index](https://adapty.io/app-subscription-pricing-index/) |
| `paywall-store-compliance` | Will this paywall, trial or cancel flow pass App Review and Play policy? Gives a check-by-check table with fixes | Apple Guidelines, HIG, Google Play policy |
| `paywall-teardown` | Scores a paywall screenshot out of 100 across 6 dimensions, gives ranked A/B test ideas and an annotated report card. By Adapty, MIT | [Adapty](https://github.com/vkharlan-adapt/paywall-teardown) |
| `paywall-ab-test-assistant` | Grades a test idea or ranks a backlog against A/B tests run on Adapty, with an evidence-strength label. By Adapty, MIT | [Adapty](https://github.com/vkharlan-adapt/paywall-ab-test-assistant) |

## Works well with

[Growth Skills](https://github.com/theoutlines/growth-skills) adds screen teardowns for the rest of the user's journey: web funnel, onboarding, upsells, the first weeks before renewal and the cancel flow. It installs Subscription Skills with it.

[State of Paywalls 2026](https://github.com/vkharlan-adapt/state-of-paywalls-2026-skill) by Adapty adds paywall-level conversion benchmarks from 78,000+ paywalls. The router uses it when it's installed.

**A full paywall review** combines `paywall-teardown` (score and test ideas) with `paywall-store-compliance` (App Store and Google Play rules).

## Install

**Claude Code: everything in one plugin**

```
/plugin marketplace add theoutlines/subscription-skills
/plugin install subscription-skills@theoutlines-subscription-skills
```

**Other agents (Codex, Gemini CLI, Cursor, GitHub Copilot and others) via the [skills CLI](https://skills.sh):**

```
npx skills add theoutlines/subscription-skills
```

**Claude app (web, desktop):** download the zip files from the [latest release](https://github.com/theoutlines/subscription-skills/releases/latest), then upload each one in Settings → Capabilities → Skills. Start with `subscription-benchmarks`.

**Just one skill?**

- **Claude app (web, desktop):** download that skill's zip from the [latest release](https://github.com/theoutlines/subscription-skills/releases/latest) and upload it in Settings → Capabilities → Skills.
- **Claude Code:** install the plugin. Skills Claude doesn't need cost nothing: until a skill is used, only its short description is loaded.
- **Other agents:** `npx skills add theoutlines/subscription-skills` and pick the skills you want.

## Example prompts

- "Our H&F app: trial→paid 31%, annual $49.99, mostly US. How do we compare, and what should we test first?"
- "What should our $9.99/month plan cost in Brazil, Germany and Japan?"
- "Review this paywall screenshot for App Store and Google Play compliance."
- "Should we move checkout to web? What do the benchmarks say about web vs app LTV?"

## Accuracy and attribution

- **Unofficial.** Not made or endorsed by RevenueCat, Adapty, FunnelFox, Apple or Google. All report data and findings belong to their publishers. Get the original reports from the links above.
- Every number was transcribed from the source and cross-checked. Each skill has an **Errata** section listing places where a report's text contradicts its own charts. The skills quote the chart.
- The compliance skill is not legal advice. Store rules change, so check the linked sources for borderline calls.

Found a mistake? Open an issue.

License: original text and analysis under [CC BY 4.0](LICENSE). Report data belongs to its publishers; see [NOTICE](NOTICE.md).

## Maintainers

Skills are edited here, in `plugins/subscription-skills/skills/`. Adapty's two skills are pulled from upstream with `scripts/sync.sh`. On every release, bump the version in both manifests and attach one zip per skill to the GitHub release.
