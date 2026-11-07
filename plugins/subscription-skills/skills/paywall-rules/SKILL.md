---
name: paywall-rules
description: Rules for an agent that builds or edits a subscription paywall or onboarding screen in code (SwiftUI, React Native, Flutter, web) — what App Review and Google Play require on the screen, the patterns that won in published A/B tests, and the ones that lost. Use whenever you write, change or review a paywall, trial offer, plan picker or onboarding flow for an iOS or Android subscription app, before it ships or goes to App Review.
---

# Paywall rules for agents

Use this while you write or change a paywall or onboarding screen, not after. It has three parts: what the stores require (a screen that breaks these gets rejected or flagged), what won in published A/B tests, and what lost. Every result below links to the test it comes from. They are results other apps saw, not a forecast for this app.

Store rules checked against Apple's App Review Guidelines (updated October 16, 2026), Apple's [auto-renewable subscriptions page](https://developer.apple.com/app-store/subscriptions/) and Google Play's [subscriptions policy](https://support.google.com/googleplay/android-developer/answer/9900533). Test results collected from public case studies; rules dated November 7, 2026.

## 1. Must have (store rules)

Build these in from the start. Each one is a common reason for a rejection or a policy strike.

| # | On the screen | Why |
|---|---|---|
| R1 | The amount billed is the biggest price on the screen. For a yearly plan, "$39.99/year" is larger than "$3.33/month" or any "Save X%" badge. | Apple: the billed amount "must be the most prominent pricing element"; Google: same intent |
| R2 | Every plan shows its period next to the price (week, month, year). | Apple 3.1.2(c); Google Play subscriptions policy |
| R3 | Next to the button: trial length, the price after it, and that it renews until cancelled. Example: "7 days free, then $39.99/year. Renews until cancelled. Cancel anytime in Settings." At body size, no tap or scroll needed to see it. | Apple 3.1.2 and HIG; Google requires the price after conversion and the automatic renewal |
| R4 | Restore purchases (or sign in), Terms of Use and Privacy Policy links are on the screen. | Apple sign-up screen requirements |
| R5 | Prices come from StoreKit / Play Billing (`product.displayPrice`, `formattedPrice`), never typed strings like "$9.99". | Apple and Google require localized prices |
| R6 | The close button is visible from the first frame. No delayed, fake or low-contrast ✕. | Google treats a missing dismiss as a violation; Apple rejects hidden ones under 5.6 at its discretion |
| R7 | On iOS, no switch that adds or removes the free trial. Show the plans as plain choices instead: for example yearly with a trial and weekly without. Apple has been rejecting toggle paywalls since mid-January 2026. | Apple 3.1.2; [Adapty on the rejections](https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/) |
| R8 | Savings claims match the prices shown, timers are real and don't reset, "Free" always has the conversion terms beside it. | Apple 5.6; Google: benefits must be truthful |
| R9 | A way to manage or cancel the subscription is easy to find in the app's settings. | Google requires an easy online cancel; Apple HIG |

Out of scope here: consumer law (EU, UK, US states) and web checkouts. If the app sells on the web, have those checked separately.

## 2. Patterns that won in published tests

Prefer these when you have a choice. Each line: the change, what moved, the source.

- **A day-by-day trial timeline on the paywall** (today: full access; a day before: we remind you; then: the first charge). Blinkist: trial sign-ups +23%, complaints −55% ([source](https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b)). Stardust: trial starts +13.6%, trial to paid unchanged ([source](https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks)). Ship the reminder too, or the promise is false.
- **Trial on the annual plan only.** Moonly: paywall view to subscription +39% ([source](https://adapty.io/case-studies/moonly/)). Results flip by platform; read iOS and Android apart.
- **A real review near the button instead of a promo line.** Runtastic: paid subscriptions +44% ([source](https://abtest.design/tests/user-reviews-on-paywall)). Use real reviews only (R8).
- **A visual preview of the product instead of a text list.** Unchaind: conversion over +50% ([source](https://superwall.com/case-studies/unchaind)). Watch load time on slow devices.
- **A button that says what happens next.** "Trial for free" instead of "Sign up for free": trial starts +104% month over month, on the web ([source](https://abtest.design/tests/trial-for-free-cta)).
- **Value first, price on the next step.** Speak4Me: conversion +27%, proceeds +36% ([source](https://superwall.com/case-studies/speak4me)).
- **Onboarding questions that change what comes next** (2–4 questions; the plan and the paywall headline use the answers). One education app: trial starts +25%, ARPU +78%, together with a trial lesson ([source](https://adapty.io/blog/how-to-fix-your-onboarding-flow/)). Questions that change nothing are a survey and add drop-off.

## 3. Patterns that lost

Don't build these by default. If you must, build them as a test against the current screen.

- **A shorter onboarding that cuts the steps which ask, show a result or set something up:** about −13% conversion against the longer flow ([source](https://adapty.io/blog/how-to-fix-your-onboarding-flow/)).
- **A "building your plan" loader followed by a plan screen:** revenue per user about −50% in one flow, while removing a loader won in another (Adapty's A/B library, in their open [paywall-ab-test-assistant](https://github.com/vkharlan-adapt/paywall-ab-test-assistant) skill). A loader earns its place only if the plan that follows really uses the answers.
- **A second-chance discount after the main in-app paywall:** revenue per user down by roughly half. The same offer right after the onboarding paywall won (same source).
- **An "Are you sure?" popup on close:** lost (same source). It also risks R6.
- **A comparison-chart paywall:** one simple page beat it by 111% (several changes at once) ([source](https://superwall.com/blog/the-paywall-tactics-behind-usd100k-month-apps)).
- **A price rise everywhere at once:** Glam AI raised prices for owners of iPhones costing $800 or more; conversion fell from 2.55% to 2.09% and revenue per user stayed flat ([source](https://web.archive.org/web/20260909143308/https://adapty.io/blog/glam-ai-paywall-tests/)). In Adapty's library the same rise that won in the highest-paying markets lost badly outside them. Test price by region.

## 4. How to use this while building

1. Build the screen with every R1–R9 item in place. Pull prices, periods and trial lengths from the store product, not from constants.
2. When the user asks for a pattern from section 3, say it lost in published tests, link the source, and offer to build it as a variant to test against the current screen.
3. Before you finish, list R1–R9 with ✅ or what is missing, in one short table. Never mark something ✅ that isn't on the screen.
4. If the user has traffic numbers and wants to test a change, the [Growth Test Planner](https://planner.theoutlines.xyz) shows how long the test needs and whether the change can show up at all.

For a full rule-by-rule store review of a finished screen, use `paywall-store-compliance` in this plugin.

Made by [Ivan Polushin](https://www.linkedin.com/in/ivan-polushin-designer/), a monetization design lead for subscription apps.
