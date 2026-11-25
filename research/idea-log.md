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
| saas-acquisition-exit | 1 | 2026-11-25 |
| app-redesign-backlash | 1 | 2026-11-25 |
| ai-training-plan-control | 1 | 2026-11-25 |
| chargeback-evidence | 1 | 2026-11-25 |
| supplier-price-rises | 1 | 2026-11-25 |
| junk-signups | 1 | 2026-11-25 |
| ai-game-flood | 1 | 2026-11-25 |
| subscription-fatigue | 1 | 2026-11-25 |
| community-tools-breaking | 1 | 2026-11-25 |

## Sources: what works from the cloud environment

| Source | Status on 2026-11-25 |
|---|---|
| Hacker News (Algolia API) | Works. Good for developer and freelancer topics, noisy for consumer niches |
| GitHub issue search (unauthenticated) | Works |
| Discourse forums (`/top.json?period=monthly`, `/t/<id>.json`) | Works: TrainerRoad, Zwift, Intervals.icu, Anki, WaniKani, Ghost, Godot, Defold, Shopify, Bubble, Obsidian, Mac Power Users, Home Assistant, freeCodeCamp, Exercism |
| Apple App Store review feed | Works briefly, then returns empty pages. Fetch slowly, save after every app, never overwrite |
| Reddit, Trustpilot, Product Hunt, X, G2 | Blocked |

## Niches

Run 1 (2026-11-17): AI / developer tools.
Run 2 (2026-11-25): real estate, gaming, health, nutrition, fitness, productivity while driving, newsletters, AI / developer tools, education, creator / freelancer. No readable evidence yet for real estate, health, nutrition or driving.
