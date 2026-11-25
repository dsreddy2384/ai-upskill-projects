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
