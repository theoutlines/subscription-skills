#!/usr/bin/env bash
# Pull Adapty's three skills (MIT, (c) Adapty Tech Inc.) from upstream into the bundled plugin.
# Our own skills are edited directly in plugins/subscription-skills/skills/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/plugins/subscription-skills/skills"
TMP="$(mktemp -d)"
# Copy with their LICENSE, then subset fonts (raw Inter TTFs trip the directory scanner)
for skill in paywall-teardown paywall-ab-test-assistant; do
  git clone -q --depth 1 "https://github.com/vkharlan-adapt/$skill" "$TMP/$skill"
  rm -rf "${DEST:?}/$skill"
  cp -r "$TMP/$skill/skills/$skill" "$DEST/$skill"
  cp "$TMP/$skill/LICENSE" "$DEST/$skill/LICENSE"
  echo "synced $skill"
done
# State of Paywalls keeps SKILL.md at the repo root
git clone -q --depth 1 "https://github.com/vkharlan-adapt/state-of-paywalls-2026-skill" "$TMP/sop"
rm -rf "${DEST:?}/state-of-paywalls-2026-by-adapty"
mkdir -p "$DEST/state-of-paywalls-2026-by-adapty"
cp "$TMP/sop/SKILL.md" "$TMP/sop/LICENSE" "$DEST/state-of-paywalls-2026-by-adapty/"
echo "synced state-of-paywalls-2026-by-adapty"
for f in "$DEST"/paywall-teardown/assets/fonts/Inter-*.ttf; do
  pyftsubset "$f" --unicodes="U+0020-007E,U+00A0-00FF,U+2010-2027,U+2030-203A,U+2190-21FF,U+2212,U+2264,U+2265,U+20AC,U+2122" --layout-features='*' --output-file="$f.sub" && mv "$f.sub" "$f"
done
rm -rf "$TMP"
echo "Now bump the version in plugins/subscription-skills/.claude-plugin/plugin.json and .claude-plugin/marketplace.json"
