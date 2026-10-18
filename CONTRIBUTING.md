# Contributing

Contributions from Dynamics 365 functional consultants, solution architects, and partners are welcome. A skill should solve a focused ERP task, be useful in more than one compatible agent client, and be published alongside a matching blog post.

## Skill structure and naming

- Put each skill in `skills/<category>/<skill-name>/SKILL.md`.
- Use one of the repository categories: `supply-chain`, `finance`, or `consultant-toolkit`.
- The skill folder name must exactly match the frontmatter `name`.
- Names may contain only lowercase letters, digits, and hyphens and must be no more than 64 characters.
- Keep `SKILL.md` under 500 lines. Put longer mappings, sample data, or checklists in a directly linked `references/` file one level below the skill folder. Optional `assets/` and `scripts/` may also be included.

## Required frontmatter

Follow the [Agent Skills specification](https://agentskills.io/specification). Use this frontmatter shape and keep repository-specific fields under `metadata`:

```yaml
---
name: skill-name
description: What the skill does and when a consultant should use it.
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
```

The description must say both what the skill does and when to use it, in language a consultant would naturally use. Keep it within the specification's 1024-character limit. Use `draft`, `tested`, or `stable` as the status. New contributions should start as `draft`; only mark a skill tested or stable when that status is supported by actual review and testing. Replace `coming soon` with the matching blog post URL when it is published.

## Required body sections

Use these sections in this order:

1. `Purpose`
2. `When to use / when not to use`
3. `Inputs needed`
4. `Step-by-step instructions`
5. `D365 data and ERP MCP tools used (if any)`
6. `Output format`
7. `Guardrails`
8. `Example prompts`
9. `Limitations`

Start from [`templates/skill-template/SKILL.md`](templates/skill-template/SKILL.md). Keep instructions specific, auditable, and clear about assumptions. Do not invent ERP MCP tool names or imply a client integration exists when it has not been verified.

## Safety and sample data

- Default to read-only behavior. Any action that creates, posts, or changes ERP data must require explicit human approval first.
- Never include customer data, real company names, tenant URLs, credentials, or screenshots of real environments.
- Use fictional examples only, such as Contoso or the USMF demo company.
- Describe uncertainty and limitations; do not present an agent's recommendation as an approved business decision.

## Validate and submit

Run the repository validator before opening a pull request:

```sh
python scripts/validate_skills.py
```

The GitHub Actions workflow runs the same check for pushes and pull requests to `main`. Include the matching blog post URL in the skill metadata once published, and describe the skill's purpose, tested client(s), and any relevant limitations in your pull request.
