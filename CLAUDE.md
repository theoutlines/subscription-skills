# subscription-skills — project memory

A Claude marketplace and plugin, `subscription-skills`: the paywall and its numbers for subscription apps. Author: Ivan Polushin (theoutlines). Public repo; original text CC BY 4.0, Adapty's two skills MIT.

## Product split (agreed 2026-10-30)
- This plugin = the paywall and the testing mechanics around it: benchmark reports (RevenueCat SOSA 2026, Adapty State of In-App Subscriptions 2026, FunnelFox Web2App 2026), Adapty Pricing Index, `subscription-benchmarks` router, `paywall-store-compliance`, and Adapty's `paywall-teardown` and `paywall-ab-test-assistant`. Self-contained: one install, everything included.
- Growth work beyond the paywall (onboarding, flow, upsell, retention, cancel flow, web2app) lives in theoutlines/growth-skills. Its marketplace lists this plugin by `git-subdir` and depends on it, so edits here reach both products. Keep the plugin path `plugins/subscription-skills` stable.
- Removed for good: Apple Ads and AppsFlyer skills (not designer work), Recurly. Standalone per-skill repos are deleted.

## Layout
- `.claude-plugin/marketplace.json` at the root; plugin at `plugins/subscription-skills/` (8 skills).
- Our skills are edited in place in `plugins/subscription-skills/skills/`. `scripts/sync.sh` only pulls Adapty's two skills from upstream (github.com/vkharlan-adapt) and subsets their fonts.
- Adapty's State of Paywalls is not bundled (no MIT licence yet); the router uses it when installed. Bundle it once the licence lands.

## Rules
- Public sources only; never employer data. Never invent a number; every figure keeps its source and denominator (per install vs per trial start vs per paywall view vs per web visitor). Each report skill keeps an Errata section.
- Bump `version` in plugin.json and the marketplace entry on every release. The owner publishes GitHub releases with one zip per skill (this session can't create releases). Repo settings (About, topics) are changed through the owner's signed-in Chrome.
- Run `claude plugin validate .` and `claude plugin validate plugins/subscription-skills` before every push.

## Status (Oct 2026)
- v1.2.0 (8 skills). Submitted to the Anthropic directory earlier; development continues without waiting for the review.
