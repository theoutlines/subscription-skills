#!/usr/bin/env bash
# Pull the latest SKILL.md from each standalone skill repo into the bundled plugin.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/plugins/subscription-skills/skills"
TMP="$(mktemp -d)"
for pair in \
  state-of-subscription-apps-2026:state-of-subscription-apps-2026-skill \
  state-of-in-app-subscriptions-2026:state-of-in-app-subscriptions-2026-skill \
  state-of-web2app-2026:state-of-web2app-2026-skill \
  state-of-app-monetization-2026:state-of-app-monetization-2026-skill \
  subscription-pricing-index:adapty-pricing-index-skill \
  search-ads-subscription-apps-2026:apple-ads-subscription-apps-2026-skill \
  paywall-store-compliance:paywall-store-compliance-skill \
  subscription-benchmarks:subscription-benchmarks-skill; do
  skill="${pair%%:*}"; repo="${pair##*:}"
  git clone -q --depth 1 "https://github.com/theoutlines/$repo" "$TMP/$repo"
  rm -rf "${DEST:?}/$skill"
  cp -r "$TMP/$repo/skills/$skill" "$DEST/$skill"
  echo "synced $skill"
done
# Adapty skills (MIT, (c) Adapty Tech Inc.): copy with their LICENSE, then subset fonts (raw Inter TTFs trip the directory scanner)
for skill in paywall-teardown paywall-ab-test-assistant; do
  git clone -q --depth 1 "https://github.com/vkharlan-adapt/$skill" "$TMP/$skill"
  rm -rf "${DEST:?}/$skill"
  cp -r "$TMP/$skill/skills/$skill" "$DEST/$skill"
  cp "$TMP/$skill/LICENSE" "$DEST/$skill/LICENSE"
  echo "synced $skill"
done
for f in "$DEST"/paywall-teardown/assets/fonts/Inter-*.ttf; do
  pyftsubset "$f" --unicodes="U+0020-007E,U+00A0-00FF,U+2010-2027,U+2030-203A,U+2190-21FF,U+2212,U+2264,U+2265,U+20AC,U+2122" --layout-features='*' --output-file="$f.sub" && mv "$f.sub" "$f"
done
rm -rf "$TMP"
echo "Now bump the version in plugins/subscription-skills/.claude-plugin/plugin.json and .claude-plugin/marketplace.json"
