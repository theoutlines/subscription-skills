---
name: paywall-store-compliance
description: Review a paywall, onboarding offer, subscription sign-up screen, upsell or cancel flow (screenshot, Figma frame, mockup or description) against Apple App Store and Google Play subscription rules, and flag rejection risks with the exact rule and a fix. Use before design handoff or App Review submission.
---

# Paywall store compliance review (Apple + Google Play)

Checks a subscription purchase surface against what Apple and Google actually require. This is a **compliance** review: will this get rejected, or will it mislead users? It is not a conversion review. For conversion benchmarks, use `state-of-paywalls-2026-by-adapty` or the `subscription-benchmarks` router.

Sources (rules change, so re-check the dates when a call is borderline):
- Apple App Review Guidelines 3.1.1, 3.1.2 and 5.6 (page last updated October 16, 2026): https://developer.apple.com/app-store/review/guidelines/#subscriptions
- Apple, Auto-renewable subscriptions (sign-up screen requirements): https://developer.apple.com/app-store/subscriptions/
- Apple HIG, Apple In-App Purchase (revised September 17, 2026): https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase
- Google Play policy, Subscriptions: https://support.google.com/googleplay/android-developer/answer/9900533

Not covered: consumer-protection law (EU, UK, US states such as California auto-renewal rules), web checkout and payment-processor rules. Flag them as "check with legal" only when the design clearly touches them, for example a web paywall or the cancellation flow in the EU.

## How to run a review

1. **Identify the surface.** It is one of:
   - an onboarding paywall
   - a contextual paywall (feature gate)
   - a settings/upgrade screen
   - a trial offer
   - a promo, win-back or discount offer
   - a plan picker
   - a cancel/retention flow
   - an App Store promo or metadata

   Note the platform(s): iOS, Android or both.
2. **List what is on screen.**
   - Plans, with name, billed amount, period, per-period breakdown and their visual sizes.
   - Trial or intro offer text.
   - CTA label.
   - Close/dismiss control.
   - Restore and sign-in options.
   - Terms and privacy links.
   - Footnote text.
   - Any toggles, preselected options, timers or badges.
3. **Run the checklist below.** Go top to bottom; skip items that don't apply.
4. **Report** in this format:

   | # | Check | Platform | Status | Evidence on screen | Rule | Fix |
   |---|---|---|---|---|---|---|

   - Status is one of ✅ OK, ⚠️ Risk or ❌ Violation.
   - After the table, list the 3 most important fixes. Each fix should be a concrete copy or layout change.
   - **Severity:**
     - ❌ means a likely rejection or policy strike.
     - ⚠️ means reviewer discretion, or that it misleads users even if it might pass.
   - Never mark something as OK if it isn't visible. Write "not visible — confirm" instead.
5. If the input is a screenshot, say which parts you could not read.

## Checklist

### A. Price and billing clarity

| ID | Check | Apple | Google |
|---|---|---|---|
| A1 | **The amount actually billed is the most prominent price element** for each plan. For annual, the yearly total is bigger and more prominent than any "per month" or "per week" breakdown or any "save X%" badge. | ❌ Apple: billed amount "must be the most prominent pricing element"; breakdowns go "in a subordinate position and size" | ❌ Google: "Annual subscriptions that most prominently display their pricing in terms of monthly cost" is a listed violation |
| A2 | Every plan shows its **billing period** (week, month, year) next to the price. | ❌ 3.1.2(c), sign-up screen requirements | ❌ cost and "frequency of your billing cycle" |
| A3 | The design says it **auto-renews** and keeps charging until cancelled. A plain "/month" isn't enough on Google. | ⚠️ implied by 3.1.2(c) and the DPLA Schedule 2 disclosures | ❌ violation: monthly subscriptions "that do not inform users they will be automatically renewed" |
| A4 | Prices are **localized** to currency and storefront. Use StoreKit / Play Billing prices, not hard-coded strings like "$9.99". | ❌ "localized in available currencies" | ❌ "incompletely localized" pricing is a violation |
| A5 | The **savings claim is true and consistent with the billed prices** on screen. For example, "Save 50%" must match monthly × 12 vs annual. | ⚠️ 5.6: no tricky pricing; 3.1.2(a): no bait-and-switch | ⚠️ benefits must be "truthful and accurate" |
| A6 | Crossed-out or "was" prices reflect a real previous or standard price. | ⚠️ 5.6, misleading | ⚠️ misleading offer |

### B. Free trial and intro offers

| ID | Check | Apple | Google |
|---|---|---|---|
| B1 | The **trial length** is stated, for example "7 days free". | ❌ "clearly indicate how long the free trial lasts" | ❌ must say how long the trial or intro price lasts |
| B2 | The **price after the trial** and its period are stated next to the trial, for example "then $29.99/year". | ❌ "the price billed once the free trial is over" | ❌ must state the price after conversion |
| B3 | The design says **payment starts automatically** when the trial ends. | ❌ HIG: make sure people know "a payment will be automatically initiated" | ❌ must say it converts automatically to paid |
| B4 | The design says **how to cancel**, or that you can cancel anytime before the trial ends, with a pointer to where. | ⚠️ good practice; HIG and the subscriptions page | ❌ users must be told how to cancel |
| B5 | Intro pricing (for example "$0.99 first month") shows the intro price, its duration **and** the standard price after. | ❌ HIG: list the intro price, duration and standard price | ❌ offers that show only the intro price are a listed example |
| B6 | The CTA doesn't hide the charge. "Start free trial" is OK. "Continue", combined with an auto-enrolled trial and no terms nearby, is risky. | ⚠️ 3.1.2(a), no false pretenses | ❌ an offer must not obscure automatic enrollment |
| B7 | **Trial toggle patterns** ("Enable free trial" switch that changes the plan). The state and the resulting charge must be unambiguous in both positions. No toggle that only flips the copy. | ⚠️ Apple has rejected misleading toggles under 3.1.2 / 5.6 (reviewer discretion) | ⚠️ "Free Trial" SKU naming that hides an auto-renewing charge is a listed violation |
| B8 | Product and SKU names don't misdescribe the product. A plan called "Free Trial" that is really a paid auto-renewing plan fails. | ⚠️ 3.1.2(a) | ❌ listed violation |

### C. Required elements on the sign-up screen

| ID | Check | Apple | Google |
|---|---|---|---|
| C1 | Subscription **name, duration and what you get** each period are shown (features, limits, storage and so on). | ❌ sign-up screen requirement; 3.1.2(c) | ❌ terms "without requiring users to take extra steps" |
| C2 | A **Restore purchases** and/or **sign-in** option for existing subscribers. | ❌ required on the sign-up screen | ⚠️ good practice |
| C3 | **Terms of Use and Privacy Policy** links (in the app and in store metadata). | ❌ required | ⚠️ expected |
| C4 | Key terms are readable on the paywall itself. No scrolling, tap-to-expand or tiny low-contrast text needed to see price, period, renewal or trial terms. | ⚠️ "clearly and prominently" | ❌ "Users should not have to perform any additional action to review the information" |
| C5 | **Required versus optional.** If the app is usable without subscribing, the design must not suggest a subscription is required. | ⚠️ HIG: let people experience the app; 3.1.2(a) | ❌ promotions that don't show content is available without a subscription are a violation |

### D. Dismissal and choice architecture

| ID | Check | Apple | Google |
|---|---|---|---|
| D1 | A **close/dismiss control is visible** and works, unless this is a true hard paywall in front of a subscription-only app. In that case, say so and check that the free path (if any) is still discoverable. | ⚠️ reviewer discretion; hidden or delayed X is a frequent rejection reason under 3.1.2 / 5.6 | ❌ "Dismiss button is missing or not clearly visible" is a listed example |
| D2 | No **delayed-appearing X**, fake X, or low-contrast X that blends into the background. | ⚠️ 5.6 manipulative practices | ❌ same as D1 |
| D3 | No multi-screen flow that leads to **accidental purchase**. For example, the same button position means "Next" and then "Subscribe". | ⚠️ 5.6 "trick them into making unwanted purchases" | ❌ listed violation |
| D4 | No **pre-checked add-ons** or silently preselected higher tiers that the user doesn't notice. A preselected default plan is fine if it's visible. | ⚠️ 5.6 | ⚠️ misleading |
| D5 | Countdown timers and "limited offer" claims are real. They must not reset on reopen. | ⚠️ 5.6 misleading | ⚠️ truthful benefits |
| D6 | Apple's **system purchase confirmation sheet** is not modified or replicated. | ❌ HIG: "Don't modify or replicate this sheet" | — |
| D7 | No upsell to the same subscription for people who already have it. | ⚠️ HIG: encourage a new subscription only for non-subscribers | — |

### E. Value and permissible use

| ID | Check | Apple | Google |
|---|---|---|---|
| E1 | The subscription gives **ongoing value**, not a one-time unlock. A one-time benefit should be a non-consumable or in-app product. | ❌ 3.1.2(a), ongoing value, at least 7 days | ❌ a one-time benefit sold through an auto-renewing subscription is a violation |
| E2 | Benefits don't drop sharply after the first period, and the subscription isn't later turned into a one-time offer. | ❌ bait-and-switch, 3.1.2(a) | ❌ listed violation |
| E3 | Paid features are delivered without extra tasks (posting on social, inviting contacts and so on). | ❌ 3.1.2(a) | ⚠️ |
| E4 | When moving an app to subscriptions, existing paid users keep what they bought. | ❌ 3.1.2(a) | ⚠️ |
| E5 | Digital goods are sold through IAP or Play Billing, except where external purchase links are allowed (for example the US storefront under 3.1.3, or approved programs). | ❌ 3.1.1 / 3.1.3 | ❌ Play Payments policy |
| E6 | Upgrade and downgrade paths don't let users subscribe twice to variants of the same thing. | ❌ 3.1.2(b) | ⚠️ |

### F. Cancellation, retention and win-back flows

| ID | Check | Apple | Google |
|---|---|---|---|
| F1 | There is an **easy, findable way to manage or cancel**: in settings or account, or via the system management sheet or a Play Subscription Center link. It must not be buried. | ⚠️ HIG: "Always make it easy for customers to cancel" | ❌ "access to an easy-to-use, online method to cancel" is required |
| F2 | Retention offers (discount, pause, plan switch) are allowed, but **they can't block cancellation**. "Cancel anyway" stays reachable within one step and is clearly labeled. | ✅ HIG explicitly suggests retention offers; ⚠️ if they become a barrier | ⚠️ must not obstruct |
| F3 | Copy doesn't misstate refund rules (for example "you'll get a refund" when the store handles refunds). Don't characterize Apple's refund policy. | ⚠️ HIG | ⚠️ the current period is generally not refunded on Google; local-law exceptions exist |
| F4 | Win-back and promo offers state their discount, duration and the price after. Offer codes state eligibility limits. | ⚠️ subscriptions page | ❌ same disclosure rules as B-series |
| F5 | The subscription status (plan, price, next renewal date) can be seen in the app. | ⚠️ HIG best practice | — |

### G. Copy and claims

| ID | Check | Apple | Google |
|---|---|---|---|
| G1 | No false urgency, fake social proof or invented review counts. | ⚠️ 5.6, 5.6.3 | ⚠️ |
| G2 | "Free" isn't used for something that auto-converts without the conversion terms right next to it. | ❌ see B1–B3 | ❌ |
| G3 | Family Sharing claims (if any) match the configuration. | ⚠️ HIG | — |

## Common patterns and how to call them

- **Big "$2.49/mo" with small "$29.99 billed yearly"** → A1 ❌ on both platforms. Fix: make "$29.99/year" the primary price. Keep "$2.49/mo" as secondary text at a smaller size and lower contrast.
- **"Try for free" CTA, terms only in grey 10pt footer** → B2/B3 ⚠️–❌ and C4. Fix: put "7 days free, then $29.99/year. Cancel anytime in Settings." directly under or inside the CTA area, at body size.
- **Toggle "Not sure yet? Enable free trial"** → B7 ⚠️. Fix: both states must show what will be charged and when; the CTA label must change with the state.
- **X appears after 3–5 seconds** → D2 ⚠️ on Apple, ❌ on Google. Fix: show the X immediately. To reduce the effect on conversion, use a softer, smaller close button rather than a delayed one.
- **"Save 70%" badge based on weekly × 52 vs annual** → A5 ⚠️ if weekly isn't an offered plan, or if the math is off. Fix: compare against a plan that is actually offered, and recompute.
- **Hard paywall at onboarding, no free tier** → this is allowed on Apple if the app is subscription-only. Check C2 (restore/sign-in) and B-series. On Google, check C5: don't claim content is "free" if it isn't.
- **Lifetime plan next to subscriptions** → OK. Make sure "one-time payment" is explicit and the plan is not auto-renewing.
- **Cancel flow with 3+ screens of offers before the cancel button** → F2 ⚠️, plus legal risk in the EU and some US states. Fix: one save offer, then a clear "Cancel subscription" action.

## Output tone

- Be decisive. Mark ❌ only where a rule clearly applies. Mark ⚠️ where it depends on reviewer judgement or isn't fully visible.
- Give each fix as concrete copy or a concrete layout change, not a general principle.
- If asked "will this pass?", answer with the probability and the top blocking items. Don't give a blanket yes.
