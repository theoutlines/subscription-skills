---
name: subscription-pricing-index
description: Answer questions from Adapty's Pricing Index (2024–2025): what users actually pay for weekly, monthly and annual app subscriptions in 64 countries vs the US baseline. Use for localizing subscription prices, regional price tiers, and checking a price against country medians.
---

# Adapty Pricing Index — unofficial skill

Source: Adapty, *The Adapty Pricing Index: What people really pay for subscriptions*. The PDF is gated behind a form at https://adapty.io/app-subscription-pricing-index/
Unofficial. Not made or endorsed by Adapty. All data belongs to Adapty.

## How to answer

- Answer from the country table below. Each value is the **median gross price** users paid, in USD, for that plan length in that country.
- **Gross means what the user pays.** That includes VAT and Apple's commission, so it is not developer proceeds. To estimate proceeds, remove local VAT and then the store fee (15% or 30%).
- **Data is App Store only**: iOS subscription transactions. Google Play is not included.
- **Prices are medians.** They describe where the market clusters, not what is optimal. Many medians sit exactly on Apple price points ($6.99, $9.99, $34.99, $39.99), which reflects Apple's tier grid and developers' defaults.
- When recommending a local price, use this flow:
  1. Start from the country's deviation for the **same plan length**. Deviations differ a lot by plan.
  2. Round to the local store price point.
  3. Tell the user to validate with an A/B test.
- Adapty's own guidance: check market presence, conversion signals, PMF, local competitors and market dynamics. Don't blindly trust Apple's or Google's suggested local prices.
- Every text-vs-chart conflict in this report is provable from the report's own price data (see Errata), so use the price data and say the text is in error.
- Columns marked *derived* were computed for this skill from the report's prices. They are not printed in the report.

## Methodology

- **Data:** anonymized App Store subscription transactions from 11,000+ apps and $1.9B in revenue. Adapty overall tracks $1.9B revenue, 215M transactions and 73K paywalls.
- **Scope:** subscriptions only, both new purchases and renewals. Period: full years 2024–2025, to capture seasonality.
- **Prices:** the gross end-user price in local currency, converted to USD at the exchange rate on the purchase date.
- **Statistic:** the transaction-weighted median per country and plan length. This guards against outliers.
- **Index:** US median = 1.00. Deviation % = (country index − 1) × 100.
- **US baseline medians:**
  - Weekly **$6.99**
  - Monthly **$12.99**
  - Annual **$39.99**
- **Coverage:** 64 countries in 7 regions: Europe 25, North America 7, South America 7, Middle East 7, Asia 13, Africa 3, Oceania 2.
- **Privacy:** data is aggregated, with statistical sampling across categories.
- The report doesn't break prices down by category, app size, or trial vs no trial.

## Headline findings (Adapty)

1. Prices vary up to **4×** between countries. A $10 US monthly plan maps to **$16.20 in the Netherlands** and **$3.70 in Nigeria**.
2. **Europe pays more for weekly plans.** Nearly every European country is above the US for weekly, even those that discount longer plans.
3. **Monthly plans vary the most.** The range runs from Netherlands **+62%** to Nigeria **−63%**. Local pricing matters most for monthly.
4. **Annual prices are the most stable.** Most countries sit at **75–110% of the US price**. Exceptions: Nigeria −70% and Egypt −71%.
5. **LATAM is not one market.**
   - Argentina and Uruguay match the US on weekly price, while Brazil is 30% lower.
   - For annual, Uruguay ($35.99) and Argentina ($34.99) are the most expensive in South America.
   - For monthly, they tie with Ecuador at $9.99. The report's text overstates this (Errata 3).
6. **Asia has big gaps.**
   - Singapore pays more than the US: weekly +5%, monthly +3%, annual +11%.
   - The Philippines and Pakistan pay 47% less for monthly plans.
   - A $10 US monthly plan maps to about $5.30 in the Philippines and about $10.30 in Singapore. The report says "$11" (Errata 2).
7. **Japan monthly is −49%** ($6.68). The report's deviation chart and text say −57% (Errata 1).

**Corrected figures:** when a user asks about any point listed in Errata, answer with the corrected value and say in one line that the report's text or deviation chart shows a different number.

## Summary statistics (*derived* from the 64-country table)

| Plan | Above US | At US | Below US | Median deviation | Within −25%…+10% |
|---|---|---|---|---|---|
| Weekly | 29 | 11 | 24 | **0%** | 36 / 64 |
| Monthly | 18 | 2 | 44 | **−13.5%** | 43 / 64 |
| Annual | 16 | 5 | 43 | **−6.5%** | 56 / 64 |

**Median deviation by region** (weekly / monthly / annual) and median annual ÷ (12 × monthly):

| Region | Weekly | Monthly | Annual | Annual ÷ 12×monthly |
|---|---|---|---|---|
| Europe (25) | **+18%** | +5% | +3% | 25% |
| North America (7) | 0% | −8% | −13% | 27% |
| South America (7) | −14% | −35% | −23% | 30% |
| Middle East (7) | −2% | −8% | −13% | 25% |
| Asia (13) | −5% | −35% | −11% | 34% |
| Africa (3) | −47% | −63% | −70% | 21% |
| Oceania (2) | −2.5% | +2.5% | −3.5% | 24.5% |

**Plan ladder in the US** (*derived*):
- Annual ÷ (12 × monthly) = 26%, so annual is about a 74% discount vs paying monthly.
- 52 × weekly ÷ annual = 9.1×.

**Readings for pricing work**
- **The weekly price is the least localized.** Half the countries price at or above the US, and Europe is +18% at the median. Weekly plans are rarely discounted abroad. In Europe they are marked up, partly because VAT is included.
- **The monthly price is the most localized.** Discounts are deep in Asia, South America and Africa.
- **Annual stays near US levels in many emerging markets** while monthly drops a lot.
  - Japan: monthly −49%, annual only −3%.
  - Vietnam: monthly −40%, annual −2%.
  - Pakistan: monthly −47%, annual −11%.
  - In these markets the **annual-vs-monthly discount shrinks**: annual ÷ 12×monthly is 49% in Japan and 42% in Vietnam, vs 26% in the US. A US-style "save 74%" annual anchor doesn't hold there.
- **Europe's ordering changes by plan.** The Netherlands is the most expensive for monthly (+62%) but below the US for annual (−5%). Poland leads weekly (+38%) but sits at −16% monthly.

## Country price table (median gross price, USD)

Bold = US baseline. "vs US" is the deviation from the US median for that plan. All deviations are computed from the chart prices and match the report's deviation charts (pp. 6–8) except where noted in Errata. Sorted by region, then by monthly price.

| Country | Region | Weekly $ | vs US | Monthly $ | vs US | Annual $ | vs US | Annual ÷ (12×monthly) |
|---|---|---|---|---|---|---|---|---|
| Netherlands | Europe | 8.39 | +20% | 21.00 | +62% | 38.13 | -5% | 15% |
| Belgium | Europe | 8.36 | +20% | 17.62 | +36% | 42.10 | +5% | 20% |
| Denmark | Europe | 8.55 | +22% | 16.29 | +25% | 43.57 | +9% | 22% |
| UK | Europe | 8.77 | +25% | 15.74 | +21% | 44.44 | +11% | 24% |
| Ireland | Europe | 8.28 | +18% | 15.28 | +18% | 41.16 | +3% | 22% |
| Finland | Europe | 8.26 | +18% | 14.58 | +12% | 37.86 | -5% | 22% |
| Sweden | Europe | 8.88 | +27% | 14.44 | +11% | 38.46 | -4% | 22% |
| Switzerland | Europe | 7.78 | +11% | 14.43 | +11% | 43.46 | +9% | 25% |
| Germany | Europe | 8.36 | +20% | 14.19 | +9% | 41.55 | +4% | 24% |
| France | Europe | 8.40 | +20% | 14.06 | +8% | 41.58 | +4% | 25% |
| Greece | Europe | 7.28 | +4% | 13.84 | +7% | 37.96 | -5% | 23% |
| Norway | Europe | 8.15 | +17% | 13.82 | +6% | 41.43 | +4% | 25% |
| Portugal | Europe | 8.29 | +19% | 13.70 | +5% | 43.02 | +8% | 26% |
| Austria | Europe | 8.30 | +19% | 13.64 | +5% | 38.61 | -3% | 24% |
| Croatia | Europe | 7.32 | +5% | 11.83 | -9% | 42.29 | +6% | 30% |
| Hungary | Europe | 7.67 | +10% | 11.24 | -13% | 33.78 | -16% | 25% |
| Bulgaria | Europe | 7.23 | +3% | 11.10 | -15% | 36.73 | -8% | 28% |
| Italy | Europe | 8.02 | +15% | 11.07 | -15% | 42.32 | +6% | 32% |
| Poland | Europe | 9.64 | +38% | 10.97 | -16% | 37.56 | -6% | 29% |
| Lithuania | Europe | 8.07 | +15% | 10.85 | -16% | 41.21 | +3% | 32% |
| Spain | Europe | 8.08 | +16% | 10.83 | -17% | 41.25 | +3% | 32% |
| Romania | Europe | 7.39 | +6% | 10.71 | -18% | 33.39 | -17% | 26% |
| Slovakia | Europe | 8.19 | +17% | 10.57 | -19% | 27.20 | -32% | 21% |
| Czechia | Europe | 8.23 | +18% | 10.39 | -20% | 26.09 | -35% | 21% |
| Ukraine | Europe | 6.99 | +0% | 9.99 | -23% | 34.99 | -13% | 29% |
| **United States** | North America | 6.99 | +0% | 12.99 | +0% | 39.99 | +0% | 26% |
| Canada | North America | 6.96 | -0% | 12.93 | -0% | 34.85 | -13% | 22% |
| Costa Rica | North America | 6.99 | +0% | 11.99 | -8% | 29.99 | -25% | 21% |
| Dominica | North America | 5.99 | -14% | 11.99 | -8% | 39.99 | +0% | 28% |
| Mexico | North America | 5.84 | -16% | 10.42 | -20% | 33.84 | -15% | 27% |
| Guatemala | North America | 6.99 | +0% | 9.99 | -23% | 34.99 | -13% | 29% |
| Panama | North America | 4.99 | -29% | 9.99 | -23% | 39.99 | +0% | 33% |
| Argentina | South America | 6.99 | +0% | 9.99 | -23% | 34.99 | -13% | 29% |
| Uruguay | South America | 6.99 | +0% | 9.99 | -23% | 35.99 | -10% | 30% |
| Ecuador | South America | 5.99 | -14% | 9.99 | -23% | 29.99 | -25% | 25% |
| Colombia | South America | 6.60 | -6% | 8.50 | -35% | 23.47 | -41% | 23% |
| Peru | South America | 5.55 | -21% | 8.19 | -37% | 31.98 | -20% | 33% |
| Chile | South America | 5.35 | -23% | 7.42 | -43% | 30.71 | -23% | 34% |
| Brazil | South America | 4.86 | -30% | 5.96 | -54% | 29.86 | -25% | 42% |
| UAE | Middle East | 6.80 | -3% | 13.61 | +5% | 40.84 | +2% | 25% |
| Bahrain | Middle East | 7.99 | +14% | 11.99 | -8% | 32.99 | -18% | 23% |
| Kuwait | Middle East | 6.99 | +0% | 11.99 | -8% | 34.99 | -13% | 24% |
| Oman | Middle East | 6.99 | +0% | 11.99 | -8% | 34.99 | -13% | 24% |
| Qatar | Middle East | 6.86 | -2% | 11.76 | -9% | 41.09 | +3% | 29% |
| Israel | Middle East | 6.87 | -2% | 11.21 | -14% | 40.01 | +0% | 30% |
| Saudi Arabia | Middle East | 5.86 | -16% | 10.12 | -22% | 34.62 | -13% | 29% |
| Singapore | Asia | 7.33 | +5% | 13.41 | +3% | 44.42 | +11% | 28% |
| Hong Kong | Asia | 6.81 | -3% | 12.60 | -3% | 37.05 | -7% | 25% |
| China | Asia | 6.22 | -11% | 12.24 | -6% | 27.80 | -30% | 19% |
| Armenia | Asia | 7.99 | +14% | 11.99 | -8% | 39.99 | +0% | 28% |
| Taiwan | Asia | 6.66 | -5% | 11.55 | -11% | 39.64 | -1% | 29% |
| Azerbaijan | Asia | 6.99 | +0% | 9.99 | -23% | 29.99 | -25% | 25% |
| Uzbekistan | Asia | 7.99 | +14% | 8.49 | -35% | 34.99 | -13% | 34% |
| Kyrgyzstan | Asia | 6.99 | +0% | 8.49 | -35% | 34.99 | -13% | 34% |
| Vietnam | Asia | 5.17 | -26% | 7.73 | -40% | 39.20 | -2% | 42% |
| Philippines | Asia | 5.22 | -25% | 6.92 | -47% | 30.74 | -23% | 37% |
| Pakistan | Asia | 5.19 | -26% | 6.84 | -47% | 35.52 | -11% | 43% |
| Kazakhstan | Asia | 5.96 | -15% | 6.77 | -48% | 31.55 | -21% | 39% |
| Japan | Asia | 5.37 | -23% | 6.68 | -49% | 38.88 | -3% | 49% |
| South Africa | Africa | 6.77 | -3% | 10.63 | -18% | 35.96 | -10% | 28% |
| Egypt | Africa | 3.72 | -47% | 4.87 | -63% | 11.41 | -71% | 20% |
| Nigeria | Africa | 2.58 | -63% | 4.82 | -63% | 12.08 | -70% | 21% |
| Australia | Oceania | 6.48 | -7% | 13.33 | +3% | 37.61 | -6% | 24% |
| New Zealand | Oceania | 7.16 | +2% | 13.23 | +2% | 39.43 | -1% | 25% |

Notes on the table:
- **Panama annual:** the bar sits at the US level ($39.99) and the deviation chart shows 0%, but the price label is hidden in the chart.
- **Annual ÷ (12×monthly)** is *derived*. A low ratio means annual is a deep discount vs monthly; a high ratio means annual is priced close to US levels while monthly is localized down.

## Quick lookups

- **Most expensive (vs US):**
  - Weekly: Poland +38%, Sweden +27%, UK +25%, Denmark +22%, France and Germany +20%
  - Monthly: Netherlands +62%, Belgium +36%, Denmark +25%, UK +21%, Ireland +18%
  - Annual: UK +11%, Singapore +11%, Denmark +9%, Switzerland +9%, Portugal +8%
- **Cheapest (vs US):**
  - Weekly: Nigeria −63%, Egypt −47%, Brazil −30%, Panama −29%, Pakistan and Vietnam −26%
  - Monthly: Nigeria −63%, Egypt −63%, Brazil −54%, Japan −49%, Kazakhstan −48%, Philippines and Pakistan −47%
  - Annual: Egypt −71%, Nigeria −70%, Colombia −41%, Czechia −35%, Slovakia −32%
- **Exactly at US price points** (common in USD-priced or dollarized markets):
  - Weekly $6.99: Ukraine, Costa Rica, Guatemala, Argentina, Uruguay, Kuwait, Oman, Azerbaijan, Kyrgyzstan
  - Monthly $9.99: Ukraine, Guatemala, Panama, Argentina, Ecuador, Uruguay, Azerbaijan

## Using with other benchmarks

- This index gives **what users pay**, as medians by country. For **conversion, LTV and price-vs-conversion trade-offs**, pair it with:
  - Adapty's State of In-App Subscriptions 2026 skill: price buckets and LTV by region.
  - RevenueCat SOSA 2026: price tiers vs conversion and retention.
- Adapty's region buckets in other reports (for example "Europe", "LATAM", "APAC") are not identical to this index's seven regions.

## Errata / inconsistencies in the report

1. **Japan monthly:** the deviation chart and text say **−57%**, but the price chart shows **$6.68**, which is −49% vs $12.99. The other Asian values match their price charts. Quote $6.68 and note the conflict.
2. **Singapore "$11 for a $10 plan":** the text says "a $10 monthly plan runs … $11 in Singapore", but Singapore's monthly median is $13.41 (+3%), so a $10 plan maps to ~$10.30. The "+5–10% more than the US" claim fits weekly (+5%) and annual (+11%), not monthly.
3. **"Argentina and Uruguay are the most expensive in LATAM for monthly":**
   - For monthly, they tie with Ecuador at $9.99 in South America. Mexico ($10.42) and Costa Rica ($11.99), grouped under North America in the charts, are higher.
   - The claim holds for **annual**: Uruguay $35.99 and Argentina $34.99 lead South America.
4. **"Nearly all European countries beat US weekly prices":** all 24 European countries except Ukraine are above the US. Ukraine is at parity at $6.99.
