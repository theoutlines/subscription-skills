---
name: credits-rules
description: Rules for an agent that builds or edits AI credits, usage limits, credit packs, top-ups or a virtual currency in code (SwiftUI, React Native, Flutter, web) — what App Review, Google Play and EU consumer rules require on the screen, Apple's expiring-credits program for generative AI, and the states coding agents usually leave silent (failed runs, store refunds, pending purchases, restore). Use whenever you add or change a credits system, token or coin balance, free daily limit, pay-as-you-go top-up, "out of credits" screen, credit store or usage page in an iOS or Android app, before it ships or goes to App Review. Also for questions like "how should I show credits", "can credits expire on iOS", "what happens to credits after a refund", with StoreKit 2, Play Billing, RevenueCat Virtual Currency, Superwall or Adapty.
---

# Credits rules for agents

Use this while you build a credits or limits system, not after. Part 1 is what the stores and regulators require on the screen. Part 2 is the states a user needs that a plain "add credits" build usually skips. Part 3 is the check to run before you finish.

Sources: Apple's [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) (3.1.1, 3.1.2, 5.6), Apple's [expiring consumables program](https://developer.apple.com/in-app-purchase/expiring-consumables/), Apple's [HIG on in-app purchase](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase), Google Play's [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738), and the EU consumer network's principles on virtual currencies (games guidance, March 2025; [enforced against 10 games companies on September 30, 2026](https://www.tlt.com/insights-and-events/insight/fair-play-for-gamers-cpc-network-takes-enforcement-action-on-in-game-virtual-currencies)). Rules dated November 8, 2026. These are design rules with a source, not legal advice.

## Before you start

- **Do purchased credits expire?** On iOS they may not, unless the app joins Apple's expiring-consumables program for generative AI (C2). If the user hasn't said, build credits that never expire and say why in one line.
- **Where does the balance live?** Keep it on your server, tied to the user's account, before the first purchase. The stores don't restore consumables (C6), so a device-only balance is lost on a new phone.
- **Does a subscription include credits?** Then there are at least two buckets (plan and purchased) and the spend order is part of the screen (C3).

## 1. Must have (store and regulator rules)

| # | On the screen | Status | Source |
|---|---|---|---|
| C1 | Credits bought through in-app purchase never expire, unless C2 applies. A recurring credit pack is an auto-renewable subscription, with all its paywall rules. | Enforced, Apple | 3.1.1, 3.1.2(a) |
| C2 | Apple's expiring credits (opt-in, generative-AI credits only, new IAPs only): expiry of at least 12 months shown next to the price or the buy button; what the credits are spent on; the balance shown in the app; soonest-expiring credits spent first; credits included in a subscription spent before expiring packs and never expire themselves; email 30 and 7 days before credits expire. Non-AI consumables in the same app still never expire. | Enforced, Apple (App Review checks it) | [Expiring consumables](https://developer.apple.com/in-app-purchase/expiring-consumables/) |
| C3 | A subscription that includes credits states the amount per period ("200 credits a month") before the user subscribes, and what happens to unused credits at renewal. If there are several buckets, say the order they're spent in. | Enforced, Apple; Google requires clear terms | 3.1.2(a), 3.1.2(c) |
| C4 | Each pack shows its total billed price from the store (`product.displayPrice`, `formattedPrice`), never a typed string and never only a per-credit price. | Enforced, both | Apple [HIG](https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase); Google Payments policy |
| C5 | Next to the credit amount, what it buys in real actions ("≈ 75 HD images"), and pack sizes that let people buy close to what they need, so they aren't forced into leftovers. In the EU, show the real-money cost wherever the price is in credits. | Regulator guidance, EU (enforced for games) | CPC virtual-currency principles |
| C6 | The Restore button says that credits live in the account (sign in on the new device). The store doesn't restore consumables, and they aren't shared through Family Sharing (Apple) or Family Library (Google). | Store mechanics | [Apple Family Sharing](https://developer.apple.com/documentation/storekit/supporting-family-sharing-in-your-app); [Google Family Library](https://support.google.com/googleplay/answer/7007852) |
| C7 | A pending purchase (Ask to Buy, which covers in-app purchases and lasts 24 hours; Play cash or bank payments) shows a waiting state with the balance unchanged, not an error or an endless spinner. Credits arrive when it clears, with a notification. | Store guidance, both | [Apple Ask to Buy](https://support.apple.com/en-gu/105055); [Google Play pending purchases](https://developer.android.com/google/play/billing/integrate#pending) |
| C8 | After a store refund of a pack, the app adjusts the balance and tells the user in the app what happened. The balance is shown as it is (below zero, or held at 0 with the debt stated), with how the debt clears ("your Dec 1 refill pays it off first"). The debt must actually clear: if free or plan credits are spent before the bucket that holds it, it never does, and the account is locked in effect. Never lock the account, openly or in effect. | Apple guidance; US regulator case | [Apple: handling refund notifications](https://developer.apple.com/documentation/storekit/handling-refund-notifications); [FTC v. Epic](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations) |
| C9 | No fake urgency on packs ("only today", timers on the normal price), no pre-selected add-ons, no pack pre-picked to a bigger size than the user needs. | Enforced, Apple 5.6; EU rules | 5.6; CPC principles |

## 2. States a user needs (and agents tend to skip)

On November 8, 2026 we gave two coding agents (Claude Opus and Sonnet) a plain brief: "add a credits system with a subscription, packs and a free daily limit". Both built solid server logic: verified purchases, a server balance, charge before the run and return on failure. Both left most of the states below silent on screen. None of these states has a published A/B test; they come from the store rules above and from public complaints when they were missing.

- **Balance where credits are spent.** On the screen with the action (nav bar, next to the button), not only in a profile or settings page. Tapping it opens the history.
- **Cost before the run.** On the button: "Generate · 4 credits". For variable cost, a range and "charged for what you keep". Then the balance after the run.
- **Warning before zero, for everyone.** Free users and subscribers. Offer the cheaper option if there is one ("Standard costs 2").
- **Zero.** Three ways out, side by side: buy a pack, upgrade, or wait, with the refill date and time. Keep the user's prompt or input.
- **Limits with a reset.** Show the reset in the user's local time ("14:20, in 2 h 13 min"), never just "resets daily" on a UTC clock. For rolling windows, say when each use comes back. The server decides when the limit resets (by the account's fixed time zone or a rolling window); the device only converts it for display. A reset that follows the device's time zone can be farmed by switching zones.
- **Failed run.** Say the problem was on your side and the credits are back ("+4 returned"), in place of the result and as a line in the history. Say what counts as a failure and what doesn't.
- **History.** Spend, purchases, returns, refunds, expiry, each with its bucket. A return line always follows the spend line it returns, so the two add up. Error copy promises a return only when one actually happens.
- **Refill date only while the plan renews.** After a cancel, show when the plan credits end instead.
- **Changes to costs or allowances.** If prices or credit costs can change from the server, build the notice now, not as a comment: a banner or sheet with the old and new numbers and the date it takes effect, shown before it lands. Cursor apologised and refunded after a credit change users couldn't see coming ([Cursor, July 2025](https://cursor.com/blog/june-2025-pricing)).

## 3. Before you finish

List C1–C9 and the states in part 2 in one short table, each as ✅, missing (with what is wrong), or "not on this screen, check elsewhere". Never mark something ✅ that isn't on the screen. If a state is handled only on the server (a refund, a pending purchase), it is missing until the user can see it.

For the subscription paywall itself, use `paywall-rules` in this plugin; for a full store review of a finished screen, `paywall-store-compliance`.

Made by [Ivan Polushin](https://www.linkedin.com/in/ivan-polushin-designer/), a monetization design lead for subscription apps.
