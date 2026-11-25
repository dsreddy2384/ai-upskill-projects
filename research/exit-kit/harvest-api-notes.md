# Exit Kit: Harvest API notes and day-one test checklist

Read on 2026-11-25 from Harvest's official API v2 documentation (help.getharvest.com/api-v2) and its Terms of Service (last updated April 15, 2026). Harvest's help-centre pages on the built-in export refused automated reading (HTTP 403), so the built-in export is **unverified**.

## Verdict

The archive is buildable in two weeks. The API exposes nearly everything, the limits are generous, and one account owner can create a token alone. Two things could still kill it: Harvest's own export may already be good enough, and one clause in the terms needs a careful read.

## What the API exposes

| Data | Available? | Detail |
|---|---|---|
| Clients, contacts, projects, tasks, assignments, users, roles, company | Yes | Standard list endpoints |
| Time entries | Yes | Include `billable_rate` and `cost_rate` per entry |
| Invoices, line items, payments, messages | Yes | Payments and messages are per-invoice calls |
| Invoice PDFs | Indirectly | No PDF field. `client_key` builds a public web invoice URL; adding `.pdf` gives a PDF. Docs do not say if a login is needed |
| Estimates | Yes | Same `client_key` pattern; no PDF field |
| Expenses | Yes | Admins see all |
| Expense receipts | Yes | `receipt.url`, `file_name`, `file_size`, `content_type`. Docs do not say if the URL needs the token |
| Rates | Yes | User billable rates, user cost rates (admin only), project and task hourly rates |
| Reports and bulk exports | Yes, beta | `POST /v2/reports/exports`; formats csv, xlsx, pdf, zip. `zip` only for `invoice_pack` and `estimate_pack`; `expense_receipt` as pdf |

## Limits and access

- **Token:** a personal access token from Harvest ID, full scope by default. Headers: `Authorization: Bearer`, `Harvest-Account-Id`, and a required `User-Agent`.
- **Role:** must be an Administrator for invoices, estimates and cost rates.
- **Rate limit:** 100 requests per 15 seconds; reports 100 per 15 minutes. HTTP 429 with `Retry-After`.
- **Pagination:** up to 2,000 per page; several endpoints are cursor-based and the `page` parameter is deprecated there. Follow the `links.next` URL.
- **Time reports:** at most 365 days per request.

## Terms to read before selling

- Section 3.5(iv) bars using the service "to develop, commercialize, license, or sell any product, service, or technology that could" compete with it. An export tool run by the customer on their own data is not a time tracker, but this is the clause to check. Not legal advice.
- Section 7.1: "you own and retain all rights to the Customer Data."
- Section 6.5: after cancellation "we may delete your data from the Service" and "You are responsible for regularly backing up your data". This supports the product's promise.
- No clause was found that restricts moving data to a competitor. Only the first third of the terms was read verbatim.
- Harvest reserves the right to change limits and says APIs "may not be available at all times".

## New risk found

Harvest's API has its own beta bulk exports, including an `invoice_pack` zip and an `expense_receipt` PDF. If the same exports are offered in the product's interface, the built-in export may already cover invoices and receipts. The day-one test must check this first.

## Day-one test checklist

Set up a free trial with: 2 clients, 2 projects with different rates, 10 time entries, 1 sent invoice with a payment, 1 estimate, 1 expense with a receipt image.

Then run every export the interface offers and tick what comes out:

- [ ] Invoice PDFs, one file each, with the original numbering
- [ ] Invoice line items and payments as data, not only as PDF
- [ ] Estimates
- [ ] Expense receipts as the original image files
- [ ] Time entries with the rate that applied to each
- [ ] Client contacts
- [ ] Project and task rates
- [ ] Invoice messages (what was sent and when)
- [ ] Everything in one step, or one report at a time?
- [ ] Is any export limited by date range or by role?
- [ ] Can you still log in and read the data after cancelling?

Then check two API unknowns with a token:

- [ ] Does the `client_key` invoice URL with `.pdf` download without a login?
- [ ] Does `receipt.url` download with the bearer token?

**Go:** three or more boxes are missing from the built-in export, or it takes many manual steps.
**Stop:** one built-in step gives invoices, receipts and data together.
