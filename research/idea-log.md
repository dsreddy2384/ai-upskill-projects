# Idea log

Never pitch the same idea twice. Check this file before pitching.

## Pitched

| Date | Idea | Pain theme | Score | Status |
|---|---|---|---|---|
| 2026-11-17 | Killcount: diff-only mutation check for agent-written tests | untrusted-ai-tests | 19/25 | Pitched; test this week |
| 2026-11-17 | Clientwall: per-client context vault for dev consultants | client-context | 18/25 | Pitched; gap is weak |
| 2026-11-17 | Skill drift checker across model releases | skill-drift | 15/25 | Below bar; watch only |
| 2026-11-25 | Exit Kit: export and migrate out of acquired products (Harvest first, Mailchimp next) | saas-acquisition-exit | 22/25 | Pitched; test this week |
| 2026-11-25 | Supplier price-rise catcher for small Shopify retailers | supplier-price-rises | 17/25 | Below bar; one merchant only |
| 2026-11-25 | Classic Anki client for iOS | app-redesign-backlash | 18/25 | Fails gap check; do not build |
| 2026-11-26 | PMA Watch: monthly check of a property manager against the management agreement, for remote rental owners | pm-oversight-remote-owner | 20/25 | Pitched; partial gap (DoorVault audits statement money); concierge test with 5 owners |

## Killed (pain is real, gap is not)

| Date | Idea | Pain score | Killed by |
|---|---|---|---|
| 2026-11-17 | Guided human review of agent-sized PRs | 21/25 | Devin Review, Theseus ($99/mo), Guided Review (free, open source) |
| 2026-11-17 | "Why did my quota burn" analyser | 21/25 | agent-waste-audit, transcriptmeter, tokscale, ccusage; vendors own the meter |
| 2026-11-17 | SSH command guard for agents on servers | 18/25 | hoop.dev |
| 2026-11-17 | Agent egress firewall with do-not-leak list | 17/25 | Pipelock, iron-proxy |
| 2026-11-17 | Subscription router across Claude, Codex and others | not scored | Provider terms-of-service risk |
| 2026-11-25 | AI training advisor that never changes your plan | 21/25 | Athmex, AskMyCoach, athletedata.health, IntervalCoach, platform coaches |
| 2026-11-25 | Chargeback evidence packets for Shopify | 17/25 | Shopify Payments built-in defence, Parry |
| 2026-11-25 | Junk sign-up filter for Ghost and Shopify | 16/25 | CAPTCHA, integrity tokens, Shopify Flow, email validators |
| 2026-11-25 | CarPlay voice notes | not scored | Note Now, Vocilio, Auto Memo Recorder, Memo AI; Apple restricts recording in CarPlay |
| 2026-11-26 | Cheaper mileage tracker for people leaving MileIQ | 17/25 | TripLog (free / $59.99 a year), Stride, Everlance. MileIQ exit folds into Exit Kit instead |
| 2026-11-26 | Chat-style AI food logger | 13/25 | Cal AI (MyFitnessPal), MyFitnessPal, MacroFactor; people build their own in an afternoon |
| 2026-11-26 | All-in-one software for landlords under 50 units | 15/25 | Stessa, Baselane, RentRedi, TurboTenant, DoorLoop, REI Hub |
| 2026-11-26 | Vendor COI expiry tracker for small property managers | 15/25 | Only demand came from a vendor; PM software already has it |
| 2026-11-27 | Idea validation tool for indie founders | not scored | Preuve AI, BigIdeasDB, PainMap, GummySearch, ValidatorAI, IdeaProof and more; founders buy once |
| 2026-11-27 | "Why does nobody use my app?" report | 17/25 | AI landing-page audits ($0 to $49), Shopify audit apps ($0 to $249), free forum roasts. See ideas/2026-11-27-why-no-users.md |

## Pain themes seen (count the weeks)

| Theme | Weeks seen | First seen |
|---|---|---|
| review-overload | 1 | 2026-11-17 |
| untrusted-ai-tests | 1 | 2026-11-17 |
| quota-and-cost | 1 | 2026-11-17 |
| client-context | 1 | 2026-11-17 |
| agent-egress-secrets | 1 | 2026-11-17 |
| agent-destroys-server | 1 | 2026-11-17 |
| skill-drift | 1 | 2026-11-17 |
| comprehension-loss | 1 | 2026-11-17 |
| saas-acquisition-exit | 2 ⚑ (seen in 2+ weeks: Harvest, Mailchimp, now MileIQ) | 2026-11-25 |
| app-redesign-backlash | 1 | 2026-11-25 |
| ai-training-plan-control | 1 | 2026-11-25 |
| chargeback-evidence | 1 | 2026-11-25 |
| supplier-price-rises | 1 | 2026-11-25 |
| junk-signups | 1 | 2026-11-25 |
| ai-game-flood | 1 | 2026-11-25 |
| subscription-fatigue | 2 ⚑ (MileIQ price reviews) | 2026-11-25 |
| community-tools-breaking | 1 | 2026-11-25 |
| pm-oversight-remote-owner | 1 | 2026-11-26 |
| small-landlord-software | 1 | 2026-11-26 |
| diy-ai-food-log | 1 | 2026-11-26 |

## Sources: what works from the cloud environment

| Source | Status (last checked 2026-11-26) |
|---|---|
| Hacker News (Algolia API) | Works. Good for developer and freelancer topics, very thin for real estate, nutrition and driving. URL-encode `numericFilters` or you get HTTP 400 |
| GitHub issue search (unauthenticated) | Works (needs `is:issue` in the query). Nothing useful for landlord, mileage or nutrition topics |
| BiggerPockets forums (new 2026-11-26) | **Works.** Forum pages `/forums/<id>?page=N`; topic pages embed the full thread as `application/ld+json`. Useful forums: 899 Managing Your Property, 52 Landlord Tips, 51 Tax/Legal, 530 Short-Term Rentals, 48 Rehabbing. Many AI-written and vendor replies: quote owner posts only |
| Discourse forums (`/top.json?period=monthly`, `/t/<id>.json`) | Works: TrainerRoad, Zwift, Intervals.icu, Anki, WaniKani, Ghost, Godot, Defold, Shopify, Bubble, Obsidian, Mac Power Users, Home Assistant, freeCodeCamp, Exercism |
| Apple App Store review feed | 2026-11-26: one page (MileIQ), then empty feeds for 7 apps across 21 attempts with 15 to 40 s gaps. Treat as unreliable; try once early in the run and move on |
| Discourse forums tested 2026-11-26 | Answer but quiet: forum.quantifiedself.com, community.tillerhq.com, forum.beeminder.com. Spam only: community.stessa.com. No answer: Cronometer, MacroFactor, Oura, Whoop, Withings, YNAB, Carb Manager, OwnerRez, Hostaway, Hospitable, Nightscout, OpenAPS, Mealie, Grocy, Monarch, Actual Budget, ABRP |
| Other real-estate forums | propertytribes.com returns 200 (untested further); landlordzone.co.uk and Whirlpool blocked (403) |
| Reddit, Trustpilot, Product Hunt, X, G2 | Blocked |

## Niches

Run 1 (2026-11-17): AI / developer tools.
Run 2 (2026-11-25): real estate, gaming, health, nutrition, fitness, productivity while driving, newsletters, AI / developer tools, education, creator / freelancer. No readable evidence yet for real estate, health, nutrition or driving.
Run 3 (2026-11-26): real estate (deep, BiggerPockets), driving (MileIQ reviews), nutrition (light, HN only). **Health still has no readable evidence**; make it next run's first niche, with gaming or newsletters as the second.
