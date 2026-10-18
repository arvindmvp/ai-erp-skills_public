---
name: quality-nonconformance-triage
description: Review open quality orders and nonconformances, group related findings by item, vendor, or test group, and suggest next steps when a quality user needs a read-only triage summary.
license: MIT
metadata:
  author: [YOUR NAME]
  version: "1.0.0"
  category: supply-chain
  d365-module: Quality management
  blog-post: coming soon
  tested-in: Copilot Studio, Copilot Cowork
  status: draft
---

## Purpose

Help a quality user organize open quality orders and nonconformances into a concise review, identify repeated patterns, and suggest possible follow-up for a person to assess.

## When to use / when not to use

Use this skill when a quality user wants to review a supplied or authorized read-only extract of open quality orders and nonconformances.

Do not use it to decide product disposition, release or block inventory, investigate a safety incident, or replace an approved quality procedure.

## Inputs needed

- The open quality orders and nonconformances to review, or access to an authorized read-only D365 data source.
- A date range or scope, if the user does not want all currently open records.
- Any organization-approved definitions for priority, severity, and escalation.
- Confirmation of which fields may be used for grouping, such as item, vendor, test group, status, and creation date.

## Step-by-step instructions

1. Confirm the requested scope and that the source is authorized for read-only review.
2. Review only the supplied or accessible records. Do not infer missing test results, causes, or dispositions.
3. Group related records by item, vendor, and test group where those fields are present; keep records with missing values in an explicitly labeled unknown group.
4. Summarize record counts, statuses, dates, and repeated patterns. Distinguish observed facts from possible interpretations.
5. Suggest proportionate next steps for a quality professional to consider, such as checking the test result, reviewing the nonconformance details, or contacting the responsible owner.
6. Call out urgent-looking or incomplete records for human review without changing their status or making a disposition decision.

## D365 data and ERP MCP tools used (if any)

Relevant data may include quality orders, nonconformance records, item identifiers, vendor identifiers, test groups, test results, statuses, and dates. Actual entities and field availability depend on the D365 environment.

No specific ERP MCP tool is assumed. Use only a read-only connector or user-provided extract that is actually available in the client; do not invent tool names or request write access.

## Output format

Provide:

1. A short scope and data-quality note.
2. A summary table grouped by item, vendor, and/or test group, including counts and notable statuses.
3. A prioritized list of suggested checks, each linked to the record facts that prompted it.
4. Missing information and records that need a quality professional's judgment.

Do not include unnecessary personal or sensitive data in the summary.

## Guardrails

- Default to read-only. Do not update a quality order or nonconformance, change inventory status, release or block material, or create a record.
- Any action that creates, posts, or changes ERP data requires explicit human approval first, even if a connected tool can perform it.
- Never determine final disposition, root cause, regulatory compliance, or product safety from incomplete records.
- Show the evidence and uncertainty behind suggestions; defer decisions to the responsible quality professional and approved procedure.
- Use fictional sample data only, such as Contoso or the USMF demo company. Never include customer data, real company names, tenant URLs, credentials, or real-environment screenshots.

## Example prompts

- "Review these open quality orders for USMF and group them by item and test group. Suggest what the quality team should check next; do not change any records."
- "Summarize the open Contoso nonconformances by vendor and flag repeated issues, separating facts from possible causes."

## Limitations

The skill depends on the completeness and accuracy of the source records and the user's access permissions. It does not establish root cause, determine disposition, or replace D365 configuration knowledge, quality procedures, or professional review.
