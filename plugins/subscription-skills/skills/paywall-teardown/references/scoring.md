# Paywall Score Rubric

A 100-point score across six dimensions. The score exists so two people who
run the same screenshot get the same number, and so a team can re-run the
teardown after shipping changes and see the score move. Score from the
checks below, never from overall impression.

## How to score

- Each check has a point value. Award **full** points when the check is
  clearly met, **half** (round down) when it is partly met, **zero** when it
  is missing. No other values.
- Score only what is visible. If a check can't be judged from the screenshot
  (e.g. the image is cropped above the CTA), award half and say so in the
  read line.
- **Consistency rule:** every dimension that loses 3+ points must show up in
  the hypotheses table. A deduction with no matching test idea means the
  score or the table is wrong. Fix one.
- When a check reads as borderline, use the tie-breaks written under it.
  They exist so that two runs land on the same number.
- **Hard cap:** if prices contradict each other or the billing period is
  unreadable for any plan, cap Pricing clarity at 5 and make that row
  "Fix first".

## 1. Value clarity — 20

| Check | Pts |
|---|---|
| Headline states an outcome or the user's goal, not "Go Premium" / "Unlock Pro" / the app name | 5 |
| Value points describe results, not feature names. Half: a mix of both | 5 |
| Value block is scannable: 5 items or fewer, one line each, icons or clear markers, no paragraph | 4 |
| Hero shows the result, the product in use, or something category-relevant (not abstract filler) | 3 |
| A free-vs-paid or before/after contrast is visible. A before/after hero earns this AND the hero check: it's the strongest value signal a paywall can show | 3 |

## 2. Pricing clarity — 20

| Check | Pts |
|---|---|
| Every plan shows its billing period unambiguously next to the price | 6 |
| The longer plan shows a per-week / per-month equivalent, or a comparison against the shorter plan. Half: only a crossed-out reference price with no period equivalent | 5 |
| Savings are visible (badge, strikethrough, "Save X%") and legible | 5 |
| Trial offered: full if trial length AND the price that follows are both stated on the selected plan or under the CTA, with the link between them explicit ("then $X/year"); half if they sit near each other but the link is implied. No trial: full if the charge today is unambiguous | 4 |

## 3. Visual hierarchy — 20

| Check | Pts |
|---|---|
| One plan is clearly dominant (fill, border, size or pre-selection) and sits first or is pre-selected | 6 |
| Clear scan path: headline → value → plans → CTA, with nothing competing with the CTA for attention | 5 |
| Legibility: key text has strong contrast, nothing important sits on a busy image without a scrim, nothing important is tiny grey text | 5 |
| Decision zone (plans → CTA) is uncluttered: no legal paragraph or secondary content between them | 4 |

## 4. Trust & proof — 15

| Check | Pts |
|---|---|
| Social proof is on screen. Full: specific rating + volume, or result-referencing testimonial. Half: vague ("Loved by millions") or a rating without volume | 6 |
| A reassurance line sits next to the CTA ("Cancel anytime", "No charge today") | 5 |
| The category's trust axis is addressed — see the table below | 4 |

## 5. CTA — 15

| Check | Pts |
|---|---|
| CTA is the single highest-contrast element on screen | 5 |
| CTA text names the outcome or exactly what happens ("Start My Free Week", "Unlock My Plan"). Half: a short generic action with the offer in it ("Try Free", "Start Trial"). Zero: "Continue" / "Subscribe" / "Next" | 4 |
| CTA is full-width or close to it (~80%+ of the screen width) | 3 |
| CTA is visible without scrolling and sits in the bottom third (thumb zone) | 3 |

## 6. Offer & nudges — 10

| Check | Pts |
|---|---|
| The target plan carries a high-contrast badge: "Best value", "Most popular", or a savings badge like "Save 70%" | 5 |
| Price anchoring: a reference plan or reference price makes the target plan look like the deal | 3 |
| Urgency matches the offer: with a visible discount, a deadline or timer sits near the plans; without a discount, there is no timer. Either way full points. Discount with no deadline, or a timer with no discount: zero | 2 |

### Trust axis by category

| Category | Trust axis — what earns the 4 points |
|---|---|
| Fitness / health | Results proof: outcome numbers, before/after, result testimonials |
| Beauty / skincare / AI photo | Realism: a real result on a real face, not a styled mockup |
| Education / kids / parenting | Parent credibility: parent testimonials, outcomes with timeframes |
| Finance / utilities | Refund anxiety: "cancel anytime", clear renewal terms by the CTA |
| Dating | Purchase anxiety: honest reference prices, clear terms, no clutter at the CTA |
| Productivity / AI tools | Trial clarity: what's charged and when, stated next to the CTA |
| News / media | Credibility: recognizable proof of quality or volume |
| Adult / privacy-sensitive | Discretion: "discreet billing" or equivalent |

Other categories: name the axis you're judging in the read line.

Single-plan paywalls: award the badge check in full (nothing to pick between)
and judge anchoring by whether the price is framed against something
(per-day cost, a crossed-out reference, a monthly-vs-annual note).

## Grade bands

| Score | Grade | How to frame the teardown |
|---|---|---|
| 85–100 | Strong | Refinements. Say it's a strong paywall. |
| 70–84 | Solid | A few clear gaps worth testing. |
| 50–69 | Leaking | The basics are costing conversions. |
| 0–49 | Needs work | Fix the basics before testing anything subtle. |

The render script computes the grade from the total, so only pass the
dimension scores.
