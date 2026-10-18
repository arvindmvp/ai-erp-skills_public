# Using skills with other agents

The skills are authored to follow the open [Agent Skills specification](https://agentskills.io/specification), but client support and discovery behavior vary.

1. Check whether your client supports the Agent Skills specification and review any client-specific import requirements.
2. Select a skill and read its `SKILL.md`, any directly linked references, and its limitations.
3. **TODO:** Add client-specific installation, discovery, and update steps after verifying them.
4. Provide only the data and tools the task needs. Prefer read-only ERP access.
5. Test in a sandbox with fictional data and require explicit human approval for any action that creates, posts, or changes ERP data.

Do not assume that a skill grants access to ERP data or that a client's tools have the permissions described in the instructions. Never add customer data, real company names, tenant URLs, credentials, or real-environment screenshots to the repository.
