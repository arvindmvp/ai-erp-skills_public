# AI ERP Skills

An open library of practical, reusable Agent Skills for Microsoft Dynamics 365 Finance and Supply Chain Management.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Validate skills](https://github.com/[YOUR-GITHUB-USERNAME]/ai-erp-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/[YOUR-GITHUB-USERNAME]/ai-erp-skills/actions/workflows/validate-skills.yml)

## What is a skill?

A skill is a set of instructions that helps an AI agent handle a specific task consistently. It describes when to use the skill, what information it needs, how to work through the task, and what output to produce. Skills in this repository follow the open [Agent Skills standard](https://agentskills.io/specification), so compatible clients can use them. Read more in [What are skills?](docs/what-are-skills.md).

## Skill catalog

| Skill | Category | D365 module | What it does | Blog post | Status |
|---|---|---|---|---|---|
| [Quality nonconformance triage](skills/supply-chain/quality-nonconformance-triage/SKILL.md) | Supply Chain | Quality management | Reviews open quality orders and nonconformances, groups findings, and suggests next actions. | Coming soon | Draft |
| [Create purchase requisition](skills/supply-chain/create-purchase-requisition/SKILL.md) | Supply Chain | Procurement and sourcing | Gathers, validates, previews, and creates a purchase requisition after explicit confirmation; submission is separately conditional. | Coming soon | Draft |
| [Track purchase requisition](skills/supply-chain/track-purchase-requisition/SKILL.md) | Supply Chain | Procurement and sourcing | Tracks existing requisition status and reports evidenced approval assignments without changing ERP data. | Coming soon | Draft |
| [Vendor invoice exception review](skills/finance/vendor-invoice-exception-review/SKILL.md) | Finance | Accounts payable | Reviews pending vendor invoices with matching or capture exceptions and proposes resolutions. | Coming soon | Draft |
| [Fit-gap analysis](skills/consultant-toolkit/fit-gap-analysis/SKILL.md) | Consultant Toolkit | Cross-functional | Structures workshop notes or requirements into a fit-gap analysis against standard D365 F&O capability. | Coming soon | Draft |

## Quick start

Choose a skill folder and provide its `SKILL.md` to a compatible client. Product-specific setup steps are intentionally left for the repository author to verify.

- **Copilot Studio:** See [Using skills in Copilot Studio](docs/using-in-copilot-studio.md). **TODO:** Add and verify the current import/setup steps for your Copilot Studio environment.
- **Copilot Cowork:** See [Using skills in Copilot Cowork](docs/using-in-copilot-cowork.md). **TODO:** Add and verify the current skill setup steps for Copilot Cowork.
- **Other Agent Skills clients:** See [Using skills with other agents](docs/using-with-other-agents.md) and the [Agent Skills specification](https://agentskills.io/specification). **TODO:** Add client-specific discovery or installation steps after verifying them.

Always review a skill and its proposed actions before using it with business data.

## Roadmap

1. **Supply Chain** — launch focus, starting with quality management.
2. **Finance** — accounts payable and other finance workflows.
3. **Consultant Toolkit** — reusable support for functional consultants across project phases.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for skill authoring rules, validation, and the contribution process. New skills are published alongside a matching blog post; include the post URL when it is available.

## Disclaimer

This is a personal community project, not official Microsoft guidance, a Microsoft product, or Microsoft support. Test every skill in a sandbox before production use, and review every action an agent proposes.

## Author

**[YOUR NAME]** — Dynamics 365 F&O and agentic AI solution architect.

- LinkedIn: [TODO: add LinkedIn profile]
- Blog: [TODO: add blog URL]
- YouTube: [TODO: add YouTube channel]
