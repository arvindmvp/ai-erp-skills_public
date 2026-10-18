---
name: vendor-invoice-exception-review
description: Review pending vendor invoices with matching or capture exceptions, explain likely causes from the available evidence, and propose a resolution when an accounts payable user is preparing an exception review.
license: MIT
metadata:
  author: [YOUR NAME]
  version: "1.0.0"
  category: finance
  d365-module: Accounts payable
  blog-post: coming soon
  tested-in: Copilot Studio, Copilot Cowork
  status: draft
---

## Purpose

Help an accounts payable user understand pending vendor invoice exceptions by organizing the available evidence, describing plausible causes, and proposing a resolution for human review.

## When to use / when not to use

Use this skill to review pending invoices when a matching discrepancy or invoice-capture exception is available in a user-provided extract or authorized read-only D365 source.

Do not use it to approve, post, pay, reject, or modify an invoice; resolve a vendor dispute; or make a tax, legal, or accounting determination.

## Inputs needed

- The pending invoice and exception details, or access to an authorized read-only D365 data source.
- Relevant purchase order, receipt, invoice line, and matching information when available.
- The exception category and any organization-approved tolerance or escalation rules.
- The currency and legal-entity context, if needed to interpret amounts.

## Step-by-step instructions

1. Confirm the invoice scope and that the source is authorized for read-only review.
2. Identify the exception type, affected lines, and the available comparison values, such as invoice, purchase order, and receipt quantities or amounts.
3. Compare only values present in the source. Note differences, missing references, currency, and any relevant tolerance information supplied by the user.
4. Explain likely causes as hypotheses, not conclusions, and cite the evidence for each.
5. Propose one or more next steps for an AP user to verify, such as checking a receipt, confirming a price variance, or requesting a corrected invoice.
6. Identify the owner or approval path only when provided by the user or source; otherwise mark it as an open question.
7. Return the review without changing invoice status, workflow, payment, or accounting data.

## D365 data and ERP MCP tools used (if any)

Relevant data may include pending vendor invoice headers and lines, invoice capture exceptions, purchase orders, product receipts, matching results, currency, and workflow status. Actual entities and field availability depend on the D365 environment.

No specific ERP MCP tool is assumed. Use only a read-only connector or user-provided extract actually available in the client. Do not invent tool names or request write access.

## Output format

Provide an exception review with:

| Invoice reference | Exception | Evidence observed | Likely cause (hypothesis) | Proposed check or resolution |
|---|---|---|---|---|
| Fictional reference only | ... | ... | ... | ... |

Follow the table with any missing data, assumptions, and decisions that require AP or approver review. Clearly distinguish verified values from hypotheses.

## Guardrails

- Default to read-only. Do not edit, approve, reject, post, settle, or pay an invoice; do not change a vendor, purchase order, receipt, workflow, or ledger record.
- Any action that creates, posts, or changes ERP data requires explicit human approval first, even if a connected tool can perform it.
- Do not infer fraud, vendor fault, tax treatment, accounting policy, or approval authority from an exception alone.
- Do not expose full bank details, credentials, tenant URLs, or unnecessary personal information.
- Use fictional sample data only, such as Contoso or the USMF demo company. Never include customer data, real company names, or screenshots of real environments.

## Example prompts

- "Review this pending USMF invoice capture exception, compare the invoice and purchase order details provided, and suggest what AP should verify. Do not approve or post it."
- "Group these fictional Contoso vendor invoice matching exceptions by likely cause and give each a safe next check."

## Limitations

The review is only as reliable as the invoice, purchase order, receipt, and exception data supplied. Matching tolerances, workflow configuration, tax rules, and company policies vary; an AP professional or authorized approver must validate the proposed resolution.
