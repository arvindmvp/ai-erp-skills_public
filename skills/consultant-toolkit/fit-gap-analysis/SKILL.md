---
name: fit-gap-analysis
description: Turn workshop notes or a requirements list into a structured fit-gap table against standard Dynamics 365 Finance and Operations capability when a functional consultant needs to document scope, gaps, workarounds, and open questions.
license: MIT
metadata:
  author: [YOUR NAME]
  version: "1.0.0"
  category: consultant-toolkit
  d365-module: Cross-functional
  blog-post: coming soon
  tested-in: Copilot Studio, Copilot Cowork
  status: draft
---

## Purpose

Convert workshop notes or a requirements list into a traceable fit-gap analysis that helps a project team distinguish standard Dynamics 365 Finance and Operations capability from unmet or unverified requirements.

## When to use / when not to use

Use this skill to organize requirements during discovery, solution design, or fit-gap workshops when the user supplies notes, requirements, and relevant project context.

Do not treat the output as a confirmed product capability assessment, signed-off scope, estimate, or design decision. Do not infer requirements that are not in the source material.

## Inputs needed

- Workshop notes or a numbered requirements list.
- Relevant business process, D365 module, and project phase.
- Any known D365 version, localization, enabled features, and configuration context.
- The team's definitions for fit, partial fit, gap, workaround, and priority, if they differ from common usage.

## Step-by-step instructions

1. Identify each distinct business requirement in the provided material and preserve its source reference when available.
2. Rewrite each requirement concisely without changing its meaning. Mark ambiguous statements for clarification instead of silently resolving them.
3. Compare the requirement with standard D365 F&O capability only to the extent supported by supplied context and reliable knowledge. Label unverified capability claims as needing product or solution-architect validation.
4. Classify each requirement as a potential fit, partial fit, gap, or open question. Explain the basis and assumptions for each classification.
5. For partial fits or gaps, suggest a possible configuration option, process workaround, or extension for investigation. Do not present suggestions as approved designs.
6. Record open questions, dependencies, and decisions needed from the project team.
7. Return the analysis in the requested format and identify any requirements that could not be assessed from the supplied notes.

## D365 data and ERP MCP tools used (if any)

This skill works from workshop notes and requirements supplied by the user. No ERP data or MCP tool is required. If a client provides approved product documentation or a read-only source, cite the source and distinguish it from assumptions.

## Output format

Return a table with one row per requirement:

| ID / source | Requirement | Assessment | Standard capability / evidence | Gap or assumption | Workaround or option to investigate | Open questions |
|---|---|---|---|---|---|---|
| ... | ... | Potential fit / Partial fit / Gap / Open question | ... | ... | ... | ... |

Add a short summary of assessment counts, major assumptions, and decisions needed. Do not assign effort, cost, or delivery dates unless the user provides a basis and asks for them.

## Guardrails

- Default to read-only analysis. Do not change D365 configuration, create project records, or make commitments on behalf of the project team.
- Any action that creates, posts, or changes ERP data requires explicit human approval first.
- Do not claim that a requirement is supported by standard product capability unless the claim is sufficiently established; flag uncertain or version-dependent claims for verification.
- Preserve traceability to source requirements and label assumptions, interpretations, and proposals.
- Use fictional examples only, such as Contoso or the USMF demo company. Never include customer data, real company names, tenant URLs, credentials, or screenshots of real environments.

## Example prompts

- "Turn these fictional Contoso workshop notes into a fit-gap table for D365 Finance. Keep assumptions separate and list open questions."
- "Analyze these requirements for warehouse operations in D365 Supply Chain Management. Flag anything that needs a solution architect to verify."

## Limitations

Standard capability can vary by application version, localization, configuration, licensing, and enabled features. The analysis is a working artifact for consultant review, not a substitute for current Microsoft documentation, a fit-gap workshop, or project sign-off.
