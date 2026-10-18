# What are skills?

An Agent Skill is a reusable package of instructions that tells an AI agent how to approach a focused task. In this repository, a skill is a folder containing a `SKILL.md` file with metadata and task guidance; it may also include references, assets, or scripts.

The [Agent Skills specification](https://agentskills.io/specification) defines a common format so compatible clients can discover and use skills. A skill provides instructions, not guaranteed access to D365 data or tools: available connections and permissions depend on the client and environment.

Skills here focus on Microsoft Dynamics 365 Finance and Supply Chain Management workflows. They default to read-only review and require explicit human approval before any action that creates, posts, or changes ERP data.

## Anatomy of a skill

- **Frontmatter** identifies the skill, explains what it does and when to use it, and stores repository-specific metadata.
- **Instructions** describe inputs, steps, expected output, guardrails, examples, and limitations.
- **Optional supporting files** hold longer references, assets, or scripts. Keep references one folder level below the skill and link to them from `SKILL.md`.

See the [skill template](../templates/skill-template/SKILL.md) and [contribution guide](../CONTRIBUTING.md) to author one.
