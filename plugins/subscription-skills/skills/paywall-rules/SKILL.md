---
name: paywall-rules
description: Rules for an agent that builds or edits a subscription paywall or onboarding screen in code (SwiftUI, React Native, Flutter, web) — what App Review and Google Play require on the screen, the patterns that won in published A/B tests, and the ones that lost. Use whenever you write, change or review a paywall, trial offer, plan picker or onboarding flow for an iOS or Android subscription app, before it ships or goes to App Review.
---

# Paywall rules for agents

Use this while you write or change a paywall or onboarding screen, not after. It has three parts: what the stores require (a screen that breaks these gets rejected or flagged), what won in published A/B tests, and what lost. Results are what other apps saw, not a forecast for this app.

Sources: Apple's [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#subscriptions) (3.1.2 and 5.6, updated October 16, 2026), Apple's [auto-renewable subscriptions page](https://developer.apple.com/app-store/subscriptions/), Apple's [HIG on in-app purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase), and Google Play's [subscriptions policy](https://support.google.com/googleplay/android-developer/answer/9900533). Test results come from public case studies, linked on each line. Rules dated November 7, 2026.

## Before you start

- **Where does this paywall appear?** At the end of onboarding, or inside the app (a locked feature, a settings upgrade)? Some results flip with placement (section 3). If the user hasn't said and it matters for what they asked, ask in one line.
- **If the code you were given is incomplete or doesn't compile, say so first**, then judge what is there.
- **Building from scratch?** A ready-made store view covers most of R1–R5: Apple's `SubscriptionStoreView` in SwiftUI, or the paywall component of the subscription SDK the app already uses (RevenueCat Paywalls, Superwall, Adapty Paywall Builder) in React Native and Flutter. Use it unless the user wants a custom layout.

## 1. Must have (store rules)

Build these in from the start. "Enforced" = a written rule that leads to rejection or a policy strike. "Discretion" = the reviewer decides; the row lowers the risk.

| # | On the screen | Status | Source |
|---|---|---|---|
| R1 | The amount billed is the biggest price on the screen. For a yearly plan, "$39.99/year" is larger than "$3.33/month" or any "Save X%" badge. | Stated Apple requirement; Google requires clear billing terms | Apple [subscriptions page](https://developer.apple.com/app-store/subscriptions/): the billed amount must be the most prominent pricing element; Google [policy](https://support.google.com/googleplay/android-developer/answer/9900533) |
| R2 | Every plan shows its period next to the price (week, month, year). | Enforced, both | Apple 3.1.2(c); Google policy |
| R3 | Next to the button: trial length, the price after it, and that it renews until cancelled. Example: "7 days free, then $39.99/year. Renews until cancelled. Cancel anytime in Settings." No tap or scroll to see it, at least `.footnote` size (about 13 pt) with normal text contrast. Show trial wording only to people who can still get the trial: on iOS check `isEligibleForIntroOffer` (or your SDK's eligibility check, e.g. RevenueCat's); on Play, use the offers Play Billing returns for this user. Read the trial length from the product, not a constant. | Enforced, both | Apple 3.1.2 and [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase); Google policy |
| R4 | A Restore purchases button, plus Terms of Use and Privacy Policy links. A sign-in button doesn't replace Restore unless signing in restores the purchase. | Enforced, Apple | Apple [subscriptions page](https://developer.apple.com/app-store/subscriptions/) |
| R5 | Prices come from StoreKit / Play Billing (`product.displayPrice`, `formattedPrice`), never typed strings like "$9.99". Derived prices (per month, per week) are computed from the product price with its own format style. | Enforced, both | Apple and Google require localized prices |
| R6 | The close button is visible from the first frame, including while the paywall loads. No delayed, fake or low-contrast ✕. | Google lists "dismiss button is missing or not clearly visible" as a violation; Apple: reviewer discretion under 5.6 | Google [policy](https://support.google.com/googleplay/android-developer/answer/9900533); Apple 5.6 |
| R7 | On iOS, no switch that adds or removes the free trial. Show the plans as plain choices instead: for example yearly with a trial and weekly without. On Android no rejections are reported yet; in a cross-platform app, build the plain-choice version for both. | Enforced on Apple since mid-January 2026 | Apple 3.1.2; [Adapty on the rejections](https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/) |
| R8 | Savings claims are computed from the store prices and rounded down (yearly $29.99 vs 12 × $4.99 is "Save 49%", not 50%). A countdown only shows the end of a real offer from the store, never runs on the normal price and never resets. "Free" always has the conversion terms beside it. A discount is a real product or offer, never a label on the normal price (see "Discounts" below). | Enforced, both | Apple 5.6; Google: benefits must be truthful |
| R9 | A way to manage or cancel the subscription is easy to find in the app's settings (SwiftUI `.manageSubscriptionsSheet`, or your SDK's manage-subscriptions call or URL). | Enforced on Google; Apple HIG asks for it | Google policy; Apple [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase) |

**Discounts.** A "50% off" must be real. On iOS, a discount for new users is an introductory offer, an offer code or a separate cheaper product set up in App Store Connect; promotional and win-back offers are for current or past subscribers. On Google Play, set it up as an offer in Play Console. Then show the real discounted price from the store, with its period and the price after the offer. Offer types change; check Apple's and Google's current docs when it matters.

Out of scope here: consumer law (EU, UK, US states) and web checkouts. If the app sells on the web, have those checked separately.

## 2. Patterns that won in published tests

Prefer these when you have a choice. Each line: the change, what moved, how strong the evidence is, the source. "A/B" = a controlled test; "directional" = the source gives no control group or method; "bundled" = several changes shipped together. Every step that has the buy button still needs R1–R3 in full.

- **A day-by-day trial timeline on the paywall** (today: full access; two days before the end: we remind you; then: the first charge). Blinkist: trial sign-ups +23%, complaints −55%, with a reminder two days before the trial ends (A/B, bundled with the reminder opt-in) ([source](https://uxplanet.org/how-solving-our-biggest-customer-complaint-at-blinkist-led-to-a-23-increase-in-conversion-b60ad514134b)). Stardust: trial starts +13.6%, trial to paid unchanged (A/B) ([source](https://superwall.com/blog/how-stardust-increased-ios-app-revenue-by-4x-in-six-weeks)). Ship the reminder too, or the promise is false.
- **Trial on the annual plan only.** Moonly: paywall view to subscription +39% (A/B) ([source](https://adapty.io/case-studies/moonly/)). In Adapty's library this pattern won on one platform and not the other, so read iOS and Android apart.
- **A real review near the button instead of a promo line.** Runtastic: paid subscriptions +44% (directional) ([source](https://abtest.design/tests/user-reviews-on-paywall)). Use real reviews only (R8).
- **A visual preview of the product instead of a text list.** Unchaind: conversion over +50% (A/B) ([source](https://superwall.com/case-studies/unchaind)). Watch load time on slow devices.
- **A button that says what happens next.** "Trial for free" instead of "Sign up for free": trial starts +104% month over month, on the web (directional: a before/after, not an A/B) ([source](https://abtest.design/tests/trial-for-free-cta)).
- **Value first, then the plans on the next step.** Speak4Me: conversion +27%, proceeds +36% (A/B) ([source](https://superwall.com/case-studies/speak4me)). The step with the plans and the button carries the full terms.
- **Onboarding questions that change what comes next** (2–4 questions; the plan and the paywall headline use the answers). One education app: trial starts +25%, ARPU +78%, together with a trial lesson (directional, bundled) ([source](https://adapty.io/blog/how-to-fix-your-onboarding-flow/)). Questions that change nothing are a survey and add drop-off.

## 3. Patterns that lost

Don't build these as the default. Lines marked "Adapty's library" come from Adapty's A/B test library as summarised in their open [paywall-ab-test-assistant](https://github.com/vkharlan-adapt/paywall-ab-test-assistant) skill; the library doesn't publish the individual tests, so there is no per-test link.

- **A shorter onboarding that cuts the steps which ask, show a result or set something up:** about −13% conversion against the longer flow ([source](https://adapty.io/blog/how-to-fix-your-onboarding-flow/)).
- **A "building your plan" loader followed by a plan screen:** revenue per user about −50% in one flow, while removing a loader won in another (Adapty's library). A loader earns its place only if the plan that follows really uses the answers.
- **A second-chance discount after a paywall inside the app:** revenue per user down by roughly half. The same offer right after the onboarding paywall won (Adapty's library). This is the case where placement decides: ask if you don't know.
- **An "Are you sure?" popup on close:** lost (Adapty's library; no size given). It also risks R6, because the close button no longer simply closes.
- **A price rise on its own:** Glam AI raised prices for owners of iPhones costing $800 or more (A/B, about 8,100 people per group); conversion fell from 2.55% to 2.09% and revenue per user stayed flat ([source](https://web.archive.org/web/20260909143308/https://adapty.io/blog/glam-ai-paywall-tests/)). In Adapty's library the same rise that won in the highest-paying markets lost badly outside them. Test price by region.

## Mixed: a Free vs Pro comparison

The evidence goes both ways, so build it only as a test. In Adapty's library a Free vs Paid table used as the paywall itself won (about +15% revenue per user), while the same table shown as a teaser before the paywall lost. In one Superwall case a simple one-page paywall beat a comparison-chart paywall by 111% (metric not named, several changes at once) ([source](https://superwall.com/blog/the-paywall-tactics-behind-usd100k-month-apps)). A short list of what Pro adds next to the plans is not a comparison chart.

## 4. How to use this while building

1. Build the screen with every R1–R9 item in place. Pull prices, periods and trial lengths from the store product, not from constants.
2. When the user asks for a pattern from section 3: say it lost in published tests and link the source, then fix the base screen first. Build the pattern only when the user says yes, and only as variant B behind whatever switch the app already uses for tests (an A/B tool such as RevenueCat, Superwall or Adapty, a feature flag or remote config). If the app has none, say a test needs one and keep the current screen as the default.
3. Before you finish, list R1–R9 in one short table, each as ✅, missing (with what is wrong), or "not on this screen, check elsewhere" (R9 usually lives in Settings). Never mark something ✅ that isn't on the screen.
4. If the user has traffic numbers and wants to test a change, the [Growth Test Planner](https://planner.theoutlines.xyz) shows how long the test needs and whether the change can show up at all.

For a full rule-by-rule store review of a finished screen, use `paywall-store-compliance` in this plugin.

Made by [Ivan Polushin](https://www.linkedin.com/in/ivan-polushin-designer/), a monetization design lead for subscription apps.
