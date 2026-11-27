# Market map

Running file. Last updated 2026-11-25 (run 2). Run 1 covered AI / developer tools; run 2 added a ten-niche scan (see the last section).

Confidence labels: **primary** = read on the vendor's own page tonight; **secondary** = from third-party articles found by search, not checked against a primary source; **unverified** = single secondary source or sources that conflict.

## How the money flows

- Developers and companies pay model vendors, either a flat subscription ($8 to $200 per person per month) or per-token API prices.
- Tool vendors that sit on top of models (Cursor, code review bots, observability) charge per seat and pass model cost through or absorb it. Cursor's pricing page says third-party model usage is billed separately from its plan price (primary).
- Heavy users report a large gap between subscription and API cost. One commenter on the $200 plan said the same work cost $200 in 2 to 3 days on API keys ([HN](https://news.ycombinator.com/item?id=50147314)).

## Biggest products and prices

| Product | Price | Confidence |
|---|---|---|
| Claude (includes Claude Code) | Pro $17/mo annual or $20 monthly; Max $100; Ultra $200; Team seats $20 to $125 | primary ([claude.com/pricing](https://claude.com/pricing)) |
| Cursor | Plus $8; Premium $30; Super $100; Ultra $200; Teams from $30/user | primary ([cursor.com/pricing](https://cursor.com/pricing)) |
| GitHub Copilot | Pro $10; Business $19/user; Enterprise $39/user | secondary |
| CodeRabbit (AI code review) | Essentials $24 to $30/user; Team $48 to $60; Advanced $72 to $90 | primary ([coderabbit.ai/pricing](https://www.coderabbit.ai/pricing)) |
| Theseus (PR explanation for human reviewers) | from $99/mo for 100 guides, waitlist only | primary ([theseus.dev](https://theseus.dev)) |
| LLM observability (Langfuse, LangSmith, Braintrust, Arize) | entry tiers roughly $29 to $249/mo; sources conflict | unverified |

Codex is sold through ChatGPT plans; I did not verify those prices tonight.

## Revenue, funding and growth

All secondary or unverified. Do not quote these without checking.

- Cursor: reported at about $2B annualised revenue in early 2026 (secondary, several blogs).
- Claude Code: estimates range from $1B+ to $2.5B run-rate (unverified, sources conflict).
- GitHub Copilot: 4.7M paid subscribers cited from Microsoft's January 2026 earnings (secondary).
- Braintrust: $80M Series B at an $800M valuation, February 2026 (secondary).
- Langfuse: reported acquired by ClickHouse, January 2026 (unverified, one source).
- Market size estimates for AI coding tools in 2026 range from about $8B to $12.8B (unverified, sources conflict).

## New entrants in the last 12 months

| Entrant | What it is | Source |
|---|---|---|
| Manufact (formerly mcp-use) | MCP SDK and hosting; $6.3M seed, February 2026 | secondary |
| Theseus | Explains large PRs beside the diff for human reviewers | [theseus.dev](https://theseus.dev) |
| Guided Review | Free, open-source tool that orders a diff into review units | [guidedreview.dev](https://guidedreview.dev/) |
| Devin Review | Organises large diffs for human review | secondary |
| Pipelock | Open-source agent egress firewall with secret scanning, May 2026 | [GitHub](https://github.com/luckyPipewrench/pipelock) |
| hoop.dev | SSH proxy that blocks or holds agent commands | [hoop.dev](https://hoop.dev/blog/ai-agent-ssh-safe) |
| Estratos | Per-client knowledge base for accounting, law and marketing firms; invite-only | [estratos.ai](https://estratos.ai) |
| Farero | Free desktop app to run many coding agents with searchable history | [farero.ai](https://farero.ai) |
| Momentic "Mo" | Agents that find bugs by using your app; Launch HN 2026-11-02 | [HN](https://news.ycombinator.com/item?id=50339913) |

## Growing

- Agent-first workflows and parallel agents. "What's your current AI agentic setup?" drew 717 comments ([HN](https://news.ycombinator.com/item?id=50366117)).
- Verification of agent output: review tools for humans, mutation testing, QA agents.
- Agent security: sandboxes, egress firewalls, command guards.

## Under pressure

- Tab completion ("Ask HN: Are tab completion models dead?", [HN](https://news.ycombinator.com/item?id=50229834)).
- Copilot's share of paid tools (secondary; figures conflict between 37% and 51%).
- MCP enthusiasm: top comments on "MCP Explained" call it a dead end compared with CLIs ([HN](https://news.ycombinator.com/item?id=50382702)).
- LiteLLM's reputation: a compromised PyPI release in October 2026 ([GitHub](https://github.com/BerriAI/litellm/issues/47826)) and commenters asking for alternatives.

## Categories where customers pay a lot and still complain

1. **$100 to $200 per month coding plans.** Users hit weekly limits in a day and cannot see why ([GitHub](https://github.com/anthropics/claude-code/issues/103376), [GitHub](https://github.com/openai/codex/issues/58530)).
2. **AI code review.** Teams pay $24 to $90 per developer and humans still rubber-stamp ([HN](https://news.ycombinator.com/item?id=50157933)).
3. **Agent autonomy.** One Codex user reported $10,000+ of damage from a reboot request; the issue has 548 thumbs-up ([GitHub](https://github.com/openai/codex/issues/59060)).

## Sources that did not work tonight

- Reddit: blocked for both fetch and search from this environment.
- X, G2 and app-store reviews: not reachable in a way that lets me verify quotes, so I used none.
- All quoted complaints tonight come from Hacker News and GitHub issues. That skews toward senior, vocal developers.

## Open question for the next run

Do the same pains show up on Reddit (r/ClaudeAI, r/cursor, r/ExperiencedDevs) and in G2 reviews of CodeRabbit and Copilot? Needs a source I can read.

---

# Run 2 additions (2026-11-25): ten-niche scan

Full ranking and ideas are in `ideas/2026-11-25.md`. Facts below carry the same confidence labels.

## Biggest market change of the month

- **Bending Spoons is buying and repricing established software.** Customers report Harvest bills rising about 10x in November 2026 ([HN thread, 450 points](https://news.ycombinator.com/item?id=50420035); secondary reports agree). Intuit agreed to sell Mailchimp to Bending Spoons for $3.68B on 2026-11-19 ([HN](https://news.ycombinator.com/item?id=50573044); secondary). Commenters also name MileIQ and Airtable as acquired (unverified).
- **Anki's iOS app was redesigned in version 26.10** and the main complaint thread has 757 likes ([forum](https://forums.ankiweb.net/t/undo-26-10-update/74279)). Forum posts say AnkiHub now owns Anki (unverified).
- **Zwift launched Zwift Plus** with video routes and an AI coach at $10/month, per forum posts ([Zwift forum](https://forums.zwift.com/t/video-routes-yay-ai-coach-boo/672658)); TrainerRoad users are debating a switch.

## Prices seen (secondary unless noted)

| Product | Price | Note |
|---|---|---|
| Harvest | Listed from $9 to $14 per seat; customers report usage fees on top | Listed price secondary; bills from customer posts |
| Zebu (Harvest alternative) | €5/month | From its founder's HN comment |
| beehiiv | Lite $49 for 1,000 subscribers after an October 2026 rise | Secondary, one source |
| Substack | 10% of paid subscription revenue | Secondary |
| Ghost Pro | from $9/month for 500 members | Secondary |
| Kit | Free to 10,000 subscribers; 3.5% + 30¢ on paid products | Secondary |
| RentRedi | $12/month on annual billing | Vendor's own comparison page |
| DoorLoop | $69/month billed yearly | Secondary |
| TurboTenant | Free tier; premium $149 to $999 per year | Secondary, sources conflict |
| athletedata.health MCP | $9/month | Secondary |

## Categories where customers pay a lot and still complain (new)

1. **Time tracking and invoicing for consultancies** after the Harvest repricing.
2. **Indoor cycling training**: riders pay for TrainerRoad and Zwift together and distrust both AI coaches.
3. **Calorie trackers**: of 94 recent low-star reviews of MyFitnessPal, Lose It! and Cronometer, 34% mention redesigns or updates, 28% price or subscription and 23% ads. Counts only; the review text was lost when the feed stopped responding.

## Open question for the next run

Can the App Store review feed be read slowly enough to stay unblocked? It is the only route found to consumer evidence for nutrition, health, real estate and driving.

---

# Run 3 additions (2026-11-26): real estate, driving, nutrition

Ideas and scores are in `ideas/2026-11-26.md`. Confidence labels as above.

## What changed

- **MileIQ (owned by Bending Spoons) has raised its price.** Unlimited is $13.99/month or $11.66/month billed annually ($139.92/yr); the free tier gives 40 drives a month (primary, [mileiq.com/pricing](https://mileiq.com/pricing)). App Store reviewers in November 2026 report earlier annual prices of $49.99 and $89.99 (customer reports). Of MileIQ's 50 most recent US reviews (Nov 9 to Nov 24), 9 mention price. Bending Spoons bought MileIQ in July 2025 (secondary, [Willkie release](https://www.willkie.com/news/2025/07/willkie-advises-bending-spoons-on-acquisition-of-mileiq)). A reported $233M price is **unverified**. This is the second Bending Spoons repricing in the research, after Harvest.
- **Cheaper mileage alternatives already exist.** TripLog Basic is free and Premium is $59.99/yr (primary, [triplog.net/pricing](https://www.triplog.net/pricing)). Stride and Everlance are also widely used. Prices not checked tonight.
- **An owner-side property-manager auditing product has appeared.** DoorVault's Knox reads a manager's monthly owner statement and checks rent, fee %, duplicate expenses and net payout. Free for 2 properties, $6/door, Growth $29 (up to 10 doors), Scale $79 (up to 50), Enterprise $149 (primary, [doorvault.app/pricing](https://doorvault.app/pricing)). Launch date and funding unknown (© 2026).
- **TurboTenant acquired TenantCloud** on 2026-08-18; terms not disclosed (secondary, [LLR Partners](https://llrpartners.com/turbotenant-acquires-tenantcloud-expanding-its-property-management-solution)). Outside the 30-day window but new to this map.
- **MyFitnessPal owns Cal AI.** The deal closed December 2025 and was announced 2026-03-02 (secondary, [The Next Web](https://thenextweb.com/news/myfitnesspal-acquires-cal-ai-the-viral-calorie-tracking-app-built-by-teens)). Reported Cal AI revenue of $30 to 40M is **unverified**. Cal AI's App Store listing shows about 377K ratings (Apple search API, tonight).
- **No November 2026 funding news found** for Baselane, Stessa, RentRedi or DoorLoop. DoorLoop's $20M Series A and RentRedi's $12M Series A appear only on undated pages (**unverified** timing).

## Growing

- **Distrust of property managers among out-of-state owners.** Roughly 8 owner-written threads in 30 days in one BiggerPockets forum (my count): unpaid rent, skipped inspections, ignored approval limits.
- **Owners and small PMs building their own tools with AI**: Jira + MCP, a custom portal, an "agent" that reads statements. People are doing the same for food logging on HN.

## Under pressure

- **MileIQ**: open churn in App Store reviews after the repricing.
- **Rentec Direct**: one small landlord says it deleted properties they had entered and could not restore them ([BiggerPockets](https://www.biggerpockets.com/forums/52/topics/1320832-under-50-units-what-functionality-do-you-look-for-in-a-pm-software-platform#post_7336923)). Single report.

## Data-quality warning

BiggerPockets forum replies are full of AI-written advice and vendor seeding: several posters say they build tools in the same space. Count only original owner posts as evidence.

## Open question for the next run

Is the App Store review feed now effectively closed? Tonight it returned one page (MileIQ) and then empty feeds for 7 other apps across 21 slow attempts. If it stays closed, nutrition and health need another consumer source. Candidates: Google Play review pages, or forums such as diabetes communities (untested).

---

# Run 4 additions (2026-11-27): health, gaming, newsletters

Ideas and scores are in `ideas/2026-11-27.md`. Labels: **primary** = read on the vendor's or owner's own page; **secondary** = reported by press or search results; **unverified** = could not open the original.

## What changed

- **Gaming: Steam Next Fest (Oct 19–26, 2026) roughly doubled in size, to 8,000+ demos.** PC Gamer counted 8,011 demos and said that was about double June. Of 4,397 demos listed on SteamDB, 551 carry the "AI Content Disclosed" tag. PC Gamer also reported at least seven Roblox clones of *Escape the Walls* on the first day (all secondary, via search: [PC Gamer](https://www.pcgamer.com/gaming-industry/steam-week-in-review-steam-next-fest-has-over-8-000-demos-as-worthless-vibe-coded-slop-levels-up/), [PC Gamer](https://pcgamer.com/gaming-industry/steam-next-fests-top-played-games-include-only-1-of-over-500-demos-with-an-ai-disclosure/)).
- **Gaming: AI clones of indie games are now a standing worry among indie developers.** How To Market A Game (2026-10-28) documents *Needle In A Haystack Simulator* being overtaken by the clone *Find The Needle* (secondary, [HTMAG](https://howtomarketagame.com/2026/10/28/ai-cloners-are-here-are-indie-devs-cooked/)). Valve, at Steam Indie Connect, announced no new AI rules and advised building community and shipping steady updates (secondary, [esports.gg](https://esports.gg/news/valve-indie-devs-ai-clones-updates/); the page refused my fetch). Reports of extortion emails threatening to clone developers' games are **unverified** ([TweakTown](https://www.tweaktown.com/news/114349/valve-responds-to-steam-devs-getting-extortion-emails-threatening-ai-clones-of-their-games/index.html) returned 403).
- **Gaming: new entrant, Clone Report** (clonereport.com). Free crowd-reported clone database with 188 reported clones and 25,000 verified originals, plus Chrome and Firefox extensions that warn buyers on Steam, PlayStation, Xbox, eShop, App Store, Google Play and itch.io. Moderated by verified industry professionals (primary, read tonight). Funding and owner unknown.
- **Gaming: itch.io** is extending generative-AI disclosure filtering across its site, and is reported to have deleted "a couple terabytes of AI slop" (secondary: [HN thread](https://news.ycombinator.com/item?id=50353193), [GamesRadar](https://www.gamesradar.com/games/as-steam-struggles-with-clones-itch-io-wipes-out-a-couple-terabytes-of-ai-slop-and-adds-a-crucial-new-filter-to-its-search-function-so-you-can-avoid-ai-altogether/) headline only).
- **Gaming: Godot community backlash** over ManusAI sponsoring the Godot development fund: a 207-post, 357-like thread this month (primary, [Godot forum](https://forum.godotengine.org/t/147467)). Epic is running a "2026 Epic AI MegaJam" with a $50k headline (secondary, Unreal forum thread title).
- **Newsletters: Ghost is shipping marketing automation quickly.** Lifecycle triggers for Automations on 2026-11-04 and custom member fields on 2026-11-10 (primary, Ghost changelog posts on [forum.ghost.org](https://forum.ghost.org/t/64182)). A user-reported gap: welcome flows never fire for members created through the Admin API, which includes social sign-in plugins (primary user report, [forum](https://forum.ghost.org/t/64138/1)). Expect Ghost to close it.
- **Freelancer tools: Harvest's repricing is still pushing users away.** On Mac Power Users, one would-be buyer chose Toggl instead, and an indie competitor, **Zebu** (time tracking and invoicing, Mac app), is picking up former Harvest users; its author is a 15-year Harvest user (primary: author's post on [MPU](https://talk.macpowerusers.com/t/zebu-time-tracking/47955/5); Zebu pricing not checked).
- **Smart home: SmartThings is ending free personal access tokens on 2026-12-15** and moving API users to paid developer and business plans, according to an email posted by a user (primary user report, [HA forum](https://community.home-assistant.io/t/smartthings-charging-for-api-access-as-of-december-15th-2026/1032782/1); **not verified** with Samsung).
- **Health: hobbyists are building their own health-data pipes.** This month two new open-source bridges appeared: Health Hook (Apple Health → Home Assistant, MIT licence) and Samsung Health Bridge. Medication-reminder integrations for Home Assistant have active threads of 217 and 103 posts (primary, HA forum). No pricing or funding news found for consumer health tools tonight.

## Growing

- Indie developers holding back demos and playtests for fear of AI clones (GDevelop, Godot and HN, all within 30 days).
- Home Assistant "Month of WTH" requests from people who want their smart home to be understandable by family members (documentation, per-person notifications, user roles).

## Under pressure

- **Steam Next Fest as a discovery channel**: the press calls it "next-to-worthless" (secondary, FRVR opinion piece).
- **Harvest and other Bending Spoons products**: "Ah, Bending Spoons, where once great apps go to die." ([MPU](https://talk.macpowerusers.com/t/zebu-time-tracking/47955/2)).

## Open question for the next run

**Where can consumer health complaints be read?** Tonight forum.tudiabetes.org refused access (403), the App Store feed was empty (MyChart, one attempt), and about 60 health and fitness hostnames gave no Discourse answer. The OpenEMR forum is readable but is aimed at clinics. Next run, try: Google Play review pages; patient communities on other forum software (phpBB, XenForo) such as apneaboard.com and cpaptalk; and HN with narrower queries ("my mother's medications", "explanation of benefits").
