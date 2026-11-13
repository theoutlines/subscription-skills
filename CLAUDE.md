# subscription-skills — project memory

A Claude marketplace and plugin, `subscription-skills`: the paywall and its numbers for subscription apps. Author: Ivan Polushin (theoutlines). Public repo; original text CC BY 4.0, Adapty's two skills MIT.

## Product split (agreed 2026-10-30)
- This plugin = the paywall and the testing mechanics around it: benchmark reports (RevenueCat SOSA 2026, Adapty State of In-App Subscriptions 2026, FunnelFox Web2App 2026), Adapty Pricing Index, `subscription-benchmarks` router, `paywall-store-compliance`, and Adapty's `paywall-teardown`, `paywall-ab-test-assistant` and `state-of-paywalls-2026-by-adapty` (bundled since v1.5.0). Self-contained: one install, everything included.
- Growth work beyond the paywall (onboarding, flow, upsell, retention, cancel flow, web2app) lives in theoutlines/growth-skills, which is private and paid since 2026-11-07 and copies these skills in before each release. This plugin stays free and public; never link to growth-skills from here. Keep the plugin path `plugins/subscription-skills` stable.
- Removed for good: Apple Ads and AppsFlyer skills (not designer work), Recurly. Standalone per-skill repos are deleted.

## Layout
- `.claude-plugin/marketplace.json` at the root; plugin at `plugins/subscription-skills/` (11 skills). `credits-rules` (2026-11-08): store and EU rules for credit packs, balances and Apple's expiring AI credits, plus the states coding agents leave silent (from a baseline run of two agents); public sources only. `paywall-rules` (2026-11-07): store must-haves and published wins and losses for agents that build paywalls in code; a free demand test for the Paywall Pack idea (signal: installs on skills.sh). Use only results already public in the planner (`js/data.js` TESTS) or in this repo; never copy from the private growth-skills base.
- Our skills are edited in place in `plugins/subscription-skills/skills/`. `scripts/sync.sh` only pulls Adapty's three skills from upstream (github.com/vkharlan-adapt) and subsets paywall-teardown's fonts. Never edit them here.
- State of Paywalls bundled 2026-11-13 after Adapty added the MIT licence. It and the A/B assistant list a delayed close button as a win; the router overrides that (dark pattern, owner 2026-11-08).
- Adapty's State of Onboarding 2026 (MIT, 2026-11-13) is onboarding, not paywall: it goes into growth-skills only, never here.

## Rules
- Public sources only; never employer data. Never invent a number; every figure keeps its source and denominator (per install vs per trial start vs per paywall view vs per web visitor). Each report skill keeps an Errata section.
- Bump `version` in plugin.json and the marketplace entry on every release, and add `.github/release-notes/vX.Y.Z.md`. Pushing the version change to main runs `.github/workflows/release.yml`, which zips each skill and publishes the release (tag pushes and the releases API are blocked from this session). Repo settings (About, topics) are changed through the owner's signed-in Chrome.
- Run `claude plugin validate .` and `claude plugin validate plugins/subscription-skills` before every push.

## Status (Oct 2026)
- v1.5.0 (2026-11-13): Adapty's State of Paywalls 2026 bundled (11 skills); router rule against the delayed close.
- v1.4.0 (10 skills, + credits-rules). v1.3.0 (9 skills, + paywall-rules). v1.2.0 (8 skills). Submitted to the Anthropic directory earlier; development continues without waiting for the review.
