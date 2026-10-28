# Evidence library: paywall & flow tests

Merged from real A/B tests run on subscription apps, organized by flow element.
Each entry gives: what the element is, its evidence label, what we've observed
(as ranges), the trap that most often burns people, and untested tactics worth
trying, flagged as hypotheses.

Reading rules baked into this file:
- Figures are **bands**, not promises. Big one-off spikes are described as
  "directional" rather than quoted, because they don't generalize.
- Volume is **qualitative**: "most-tested", "tested repeatedly", "one-off". No
  counts.
- **No client names, no single identifiable results.** Platform and geo splits
  appear as caveats, never attached to an app.
- "Untested — hypothesis" means exactly that: no evidence behind it yet.
- **Platform splits are the norm.** Many tests win on iOS or Android but not
  both. "Won on one platform, flat on the other" is often the honest headline.

Evidence labels (defined in SKILL.md): Strong · Solid · Mixed · Thin · Untested.
Where one element holds results of different strength, each finding carries its
own label.

**Terms.** ARPU: revenue per user in the test cohort. CR: conversion rate (to
trial or purchase, as stated). Trial-to-paid: the share of trials that convert
to a paid subscription. Tier-1: the highest-paying markets (US, Western Europe
and similar). Guardrail: a metric you watch so a win on the primary metric
doesn't hide a loss elsewhere.

---

## PAYWALL ELEMENTS

### Paywall plans (selector, visibility, combinations)
One of our most-tested elements. What the person shows, hides and pre-selects.

**What we've seen**
- **Strong:** steering toward annual wins reliably. Annual-forward layouts and
  toggle-style selectors (annual pre-selected, trial on annual) show **ARPU
  uplift roughly +25–40%**, sometimes building over the first few months rather
  than on day one.
- **Solid:** adding a lifetime option alongside annual gives a **modest revenue
  lift, ~+10–15%**.
- **Solid:** upgrade paths mid-flow (monthly → annual offers) can capture a large
  share of purchases on their own.

**Mixed / lost**
- **Mixed:** hiding plans is where it turns. Cutting the plan count (e.g. four
  plans down to two) has **lost on revenue, in the double digits**, even when it
  looked cleaner. "Weekly visible vs. all plans visible" **won on conversion
  (~+20%) in one test and was flat in another.**

**Trap to avoid**
Some plan changes lift conversion while quietly costing revenue per user. Judge
plan tests on **revenue per user, not CR**. Your price gaps decide whether it
nets out, so it's always a real A/B, never a copy-paste.

**Untested — hypotheses**
Decoy pricing (a deliberately unattractive middle plan), reordering plan
sequence, per-segment plan sets.

### Paywall prices & discounts
Price level, intro offers and discount mechanics. Tested repeatedly.

**What we've seen**
- **Mixed (geo-split):** raising prices tends to win **in Tier-1 markets (ARPU
  roughly +15–25%)**, but the same increase has **lost badly outside Tier-1 (ARPU
  negative, CR down sharply).** This split is the whole story on pricing.
- **Strong:** seasonal and campaign discounts (Black Friday, holidays) are
  consistent winners, with **large ARPU and revenue lifts** when tied to a real
  moment.
- **Strong (iOS-heavy):** a discount or upsell offered **right after the
  onboarding paywall closes** is one of the better-evidenced wins here, often a
  decisive lift on iOS (**premium conversion roughly +25–30% or more,
  significant**), frequently as an **annual-mix shift** (more people taking the
  annual plan). It has also won **outside the US** (premium conversion up
  strongly, net revenue positive).
- **Mixed (platform-split):** a **wheel-framed discount** (spin-to-win styling
  vs. a plain discount) **won on one platform** (premium conversion up sharply,
  revenue per user up ~+20%, significant) but was **not shipped on the other**
  (revenue effectively flat, with retention and ad revenue slipping). Ship by
  platform and watch guardrails.

**Lost**
- The *same* second-chance discount offered **after the main in-app paywall**
  (rather than the onboarding one) has **lost hard (ARPU down by roughly
  half).** Timing and placement flip the sign.
- Discount and upsell wins are often **iOS-heavy**. The equivalent Android
  cohorts sometimes barely convert at all, so the "win" is really an iOS win.

**Trap to avoid**
Three traps: price moves are **geo-dependent** (Tier-1 ≠ everywhere), discounts
can **train people to wait** or cannibalize full-price buyers, and discount
effects **split by platform**. Watch net revenue (including ad revenue and
retention, not just subscription CR), and mind *where* in the flow the discount
fires.

**Untested — hypotheses**
Countdown timers, price rounding / charm pricing, regional price tailoring
beyond the Tier-1 split.

### Trial
Whether to offer a trial, how long, on which plan, and how to explain it. One of
our most-tested elements.

**What we've seen**
- **Strong:** trial framing is a strong lever. Putting the trial on the **annual
  plan** and emphasizing it lifts conversion, commonly **~+15–30%**; trial-only
  configurations have posted larger swings.
- **Strong:** "how your trial works" explainer screens generally win (**ARPU up
  ~+12–36%**) when placed next to the paywall.

**Mixed / counterintuitive**
- **Mixed:** **removing the trial entirely** has *won* big where trial-to-paid
  was very low, but the same change **lost on another platform.** Don't assume
  the trial is always the answer.
- Trial explainers placed too early can add drop-off *before* the paywall (see
  Across the flow).

**Trap to avoid**
Trial changes flip by platform and by how bad your current trial-to-paid is. If
trial-to-paid is unusually low, "no trial" is worth testing; otherwise emphasize
and simplify the trial rather than removing it.

**Untested — hypotheses**
Trial only on the target plan, trial vs. intro-price choice, trial length by
segment.

### Social proof
Ratings, reviews, testimonials, "featured by", user counts on the paywall.

**What we've seen**
- **Solid:** adding social proof to the paywall is positive where tested, **CR
  roughly +10–30%.**

**Mixed**
- A combined "comparison table + testimonials" redesign **lost**, suggesting
  more isn't always better and the two can compete for attention.

**Trap to avoid**
Stacking social proof with other heavy elements in one redesign muddies the
signal. Test it as an isolated change so you know what moved.

**Untested — hypotheses**
"Featured by Apple" badges, outcome stats ("users lose X kg"), review sliders
vs. static ratings, audience-size claims.

### Call to action button
The button itself: wording, not just placement.

**What we've seen**
- **Thin:** rewriting button copy alone has produced a sizeable lift in a
  one-off test, with trial starts and purchase CR both moving up in roughly the
  **+15–30%** band. Cheap and real as a lever; the size won't reliably repeat.

**Trap to avoid**
It's cheap to test and easy to over-read a single win. Treat button copy as a
fast, low-risk experiment rather than a guaranteed lift.

**Untested — hypotheses**
Action-oriented vs. value-oriented wording, first-person phrasing ("Start my
trial"), button colour and size.

### Close button
Dismiss behaviour: whether and when the paywall can be closed.

**What we've seen**
- **Solid:** delaying the close control (a few seconds before the X is
  tappable) wins modestly and repeatably, **CR roughly +8–15%.**

**Lost**
- An "Are you sure?" popup on close **lost.** Nagging on exit backfires where a
  quiet delay doesn't.

**Trap to avoid**
There's a line between a gentle delay (works) and interrupting the user
(backfires). Delay the close; don't harass the exit.

**Untested — hypotheses**
Optimal delay length, close-button visibility and contrast, a second offer on
close vs. a plain delay.

### Headline
The top-of-paywall message, badges and captions.

**What we've seen**
- **Thin (directional):** headline and badge/label copy can move revenue
  meaningfully; badge and caption tests have posted **large shifts in plan
  mix** (pushing people toward a higher-value plan). The mechanism (framing the
  offer) is real even if the exact number won't repeat.

**Trap to avoid**
Headline wins often come from *shifting plan mix*, not raw conversion. Check
what actually moved (mix vs. rate) before banking the lift.

**Untested — hypotheses**
Outcome-led vs. feature-led headlines, emphasis on results, emoji use, a
headline personalized to the goal the user picked in onboarding.

### Media elements
Images, illustration, animation and video on the paywall and intro screens.

**What we've seen**
- **Solid:** animation and stronger visuals win, especially on intro and
  onboarding screens: **CR up ~+13–27%, ARPU up ~+16–34%.**

**Trap to avoid**
Rich media raises perceived value but adds load time and complexity. Make sure
the visual supports the offer rather than just decorating it.

**Untested — hypotheses**
Video vs. static hero, abstract art vs. product screenshots, background
patterns, lifestyle imagery.

### Showcasing paid features / comparison
How the paid offer is made legible: feature lists and free-vs-paid comparison.

**What we've seen**
- **Strong:** a **free-vs-paid comparison table paywall** is among the
  most-tested and strongest moves in the library. As an onboarding paywall it
  has posted **very large lifts (CR to purchase and ARPU each up well into
  triple digits in the best cases)**; as an in-app paywall it lifts iOS
  subscription starts and **revenue per user (~+15%)** while holding Android
  flat. Treat the largest figures as **directional** (small samples, big
  percentages), but the direction is consistent.
- **Solid:** reframing a long feature dump as a shorter, use-case-led layout
  wins.

**Lost / careful**
- A **bare free-vs-premium comparison shown as a step *before* the paywall** (as
  onboarding education, not as the paywall itself) has **lost (ARPU and CR both
  down).** A comparison *paywall* wins, even inside onboarding; a comparison
  *teaser* ahead of the paywall can backfire.
- One comparison "win" turned out to be a **randomization-bug artifact**: the
  uplift came from users who registered mid-test, while correctly randomized
  users were flat to slightly negative. Trust clean cohorts, not the dashboard
  headline.

**Trap to avoid**
Placement and clean measurement decide whether the win is real. Put the
comparison *on* the paywall, not as a teaser upstream, and sanity-check big
uplifts against correctly randomized users.

**Untested — hypotheses**
Table vs. bulleted comparison, number of features shown, loss framing ("what
you lose") vs. gain framing ("what you get").

### Paid features description & visualization
How individual premium features are described and shown.

**What we've seen**
- **Thin:** making the paid value concrete and visual (use cases, "what you'll
  be able to do") tracks with the comparison-table and media wins above, but has
  little evidence of its own.

**Trap to avoid**
Most evidence sits under comparison, media and headline. Treat isolated
"describe the feature better" tests as directional.

**Untested — hypotheses**
Feature-by-feature visualization, before/after of using the feature,
interactive previews.

### Handling objections
Guarantees, FAQs, grace periods, billing reassurance.

**What we've seen**
- **Mixed, leaning negative:** a weak lever overall. Turning on a grace period
  gave a **small revenue positive.** A billing-issue popup **lost.** A
  **money-back-guarantee screen placed before the paywall lost** (ARPU and CR
  both slightly down).

**Trap to avoid**
Objection handling *before* the ask can plant doubt rather than remove it. Don't
pre-empt objections the user didn't have yet.

**Untested — hypotheses**
FAQ on the paywall itself, guarantee shown *on* the paywall (vs. before it),
cancellation-reassurance copy ("cancel anytime in two taps").

### Paywall placement
Where and when the paywall, or an entry point to it, appears.

**What we've seen**
- **Strong:** **contextual, limit-triggered paywalls** are a significant win. A
  paywall shown when a user hits a daily limit lifted CR to purchase **roughly
  +50–60%, significant on both platforms**, a rare both-platform result.
  Context beats interruption.
- **Solid:** other earned placements win too: an in-app paywall tab or icon
  (**CR to open ~+20–25%**), a paywall triggered by a relevant action such as a
  language switch (**ARPU ~+20%, CR ~+15%**), and contextual reward or feature
  placements.
- **Mixed:** **hard vs. soft paywall.** A hard paywall (harder to dismiss)
  lifted trial CR and revenue substantially in one test, but on low volume, and
  afterwards an upsell-based variant did better. A hard gate can win; pair it
  with a fallback offer rather than a dead end.
- **Solid:** the onboarding paywall placement is strong overall.

**Lost**
- A cross-placement test mixing a consumable and a subscription **lost.** Extra
  placements aren't free if they confuse the offer.

**Trap to avoid**
More placements ≠ more revenue. Contextual, earned placements (after value, at
a limit) beat scattering the paywall around.

**Untested — hypotheses**
Paywall frequency on app open, placement after a core feature vs. before it,
locked-feature entry points.

---

## ONBOARDING (pre-paywall)

Onboarding is part of the monetization flow: it sets up the value the paywall
charges for. Tested repeatedly.

**What we've seen**
- **Strong:** **personalization wins.** Onboarding that asks about goals and
  tailors the experience lifts downstream conversion and ARPU, commonly **CR up
  ~+8–17%, ARPU up ~+13–35%.** Personalization-led onboarding concepts have
  driven **large jumps in annual-subscription share.**
- **Solid:** **longer, richer onboarding tends to beat shorter.** Cutting
  onboarding down **lost (CR and ARPU both around −13%).** Adding relevant steps
  (age, reminders, setup) generally helps.
- **Solid:** reducing *registration* friction (not the whole flow) won (**CR
  ~+8%, ARPU ~+17%**).

**Mixed — the loader question**
- Loaders are contested. **Removing a loading screen won** (CR ~+22%, ARPU
  ~+30%) in one flow, while a **loading + personalized-plan screen lost badly
  (ARPU around −50%)** in another. A loader earns its keep only if it genuinely
  sells the personalization payoff; otherwise it's just delay.

**Trap to avoid**
Don't cut onboarding for the sake of "less friction". Depth that builds
perceived value converts better downstream. But a loader or extra step that
doesn't pay off in perceived value is pure drop-off. The test is whether the
step *adds value*, not whether it adds time.

**Untested — hypotheses**
Before/after outcome screens, commitment screens (sign or hold to commit),
quiz-to-plan personalization depth, trial lesson vs. survey ordering.

---

## ACROSS THE FLOW (the onboarding → paywall seam)

The most important section, and the reason paywall and onboarding can't be
treated separately. The *same tactic flips sign* depending on where in the flow
it sits.

- **Comparison table:** wins as a **paywall**, including as the onboarding
  paywall, but a bare comparison **teaser shown before** the paywall has
  **lost.** Same element, opposite sign.
- **Second-chance discount:** wins right **after the onboarding paywall**
  (premium conversion ~+25–30%); **loses** after the **main in-app paywall**
  (ARPU down by roughly half). Timing in the flow decides it.
- **"How your trial works" explainer:** wins on ARPU next to the paywall, but
  too early it adds **drop-off before the paywall is ever seen**, a cost that
  only shows up when you look at the whole flow.
- **Guarantees before the paywall:** tend to **lose**, planting doubt ahead of
  the ask rather than answering it at the ask.

**Why this matters for the answer**
When someone asks about one of these tactics, don't grade it in isolation. The
honest answer is "it depends where in the flow it sits", and that dependency is
the strongest argument for designing onboarding and paywall together. Building
and testing the two as one flow, rather than bolting a paywall onto the end, is
what lets these tactics land on the winning side of the split.
