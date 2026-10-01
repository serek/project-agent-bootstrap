---
name: project-bootstrap
description: Adapt an agent-workflow starter kit to an existing software repository, including project instructions, testing, task prompts, evidence, and optional Cyrus/Linear integration. Use when establishing or consolidating these documents for a new project; not for routine feature implementation.
license: Apache-2.0
---

# Project bootstrap

Build an adapted workflow, not a copied policy. The target repository's current
contracts, code, tests, instructions, and configured integrations are the
evidence. Assets in `assets/` are starting shapes only.

## Audit before writing

Inspect the target's existing `AGENTS.md`/`CLAUDE.md`, test commands, product
contracts, ADRs/PRDs, task tracker, agent integrations, and Git state. Determine
the implemented product boundary and any authorization or data-safety rules.
Produce a responsibility map for each proposed document: **reuse, amend,
create, or omit**, with the existing owner and reason. Flag contradictions and
unknowns; do not silently supersede an accepted decision or overwrite user work.

Choose **Lean** for a small project with one current gate and a simple review
path; choose **Standard** when sustained product contracts, multiple work lanes,
or verified Cyrus/Linear integration justify the extra documents. The user may
choose either. The included 17-section task prompt is a selectable convention,
not a universal Cyrus protocol.

When the target uses Linear and needs team-level planning guidance, consult
[`references/LINEAR-OPERATING-MODEL.md`](references/LINEAR-OPERATING-MODEL.md);
adapt it to observed configuration and read back actual state before relying
on it.

## Adapt the assets

Read only the assets selected by the responsibility map. Populate them from
observed target facts; remove inapplicable material instead of leaving generic
rules or unresolved placeholders. Keep one owner for each rule:

- `AGENTS.md.template`: current boundary, authority/conflicts, mandatory safety,
  and conditional pointers.
- `Claude.md.template`: task-phase and skill routing when Claude uses that entry
  point; name only available skills.
- `TESTING.md.template`: the runnable current gate and proportionate behavior
  checks; future test ambitions are marked separately.
- `WORKFLOW.md.template`: shape, specify, slice, implement, verify, review,
  deliver, and human-accept.
- `LINEAR-DESCRIPTION.md.template`: full outcome/evidence task prompt when the
  target uses the OpenCode/OMO `ultrawork` flow. Keep 17 sections if selected;
  resolve every placeholder and select actual review/security policies.
- `EVIDENCE.md.template`: candidate-bound verification and delivery receipt.
- `CYRUS-LINEAR.md.template`: optional integration; use only after checking the
  target's actual Cyrus and Linear contract, status names, handoff marker, and
  reviewer availability.
- `PRD-README.md.template`, `ADR-README.md.template`, `CONTEXT.md.template`:
  optional contract lifecycle and vocabulary owners for sustained product work.

Do not transplant example-project rules, old task IDs, status IDs, model rosters,
test commands, review receipts, paths, or pending approvals. In particular,
configured reviewer names and a passing review are different facts. A policy
that requires a reviewer or security evaluation without a usable mechanism is
an explicit blocker, not a paper pass.

## Deliver a reviewable local result

First show the responsibility map and one fully filled task example for user
review. With authorization for the local edit, make the smallest coherent diff
in the target repository. Verify links, unresolved placeholders, current test
command availability, policy consistency, and preservation of prior decisions.
Run applicable checks when the target's instructions and task scope require
them; report exact results and gaps. A second bootstrap pass should not create
duplicate files or competing policy owners.

Tracker publication, agent dispatch, runtime changes, and final acceptance
are separate actions. Do not perform or claim them from a documentation diff.
