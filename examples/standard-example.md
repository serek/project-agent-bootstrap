# Standard adaptation example: Fieldglass

Fieldglass is a fictional multi-team inventory planning product. Its repository
contains accepted product specifications, architecture decisions, several
service test suites, and a configured Linear workspace. An operator has
verified the team's Linear initiative, project, milestone, issue, and status
configuration read-only. Agent dispatch remains an explicit human action; a
human product owner accepts delivered work. The team has not enabled a fixed
17-section task description.

This example shows one possible result after those facts were observed. All
names, files, commands, and roles below are fictional. No Linear records were
created, updated, or dispatched by this example.

## Responsibility map

| Proposed document | Action | Existing owner / source | Reason |
| --- | --- | --- | --- |
| `examples/standard/AGENTS.md` | Amend | Existing `AGENTS.md` | Retain service boundaries and add contract precedence. |
| `examples/standard/TESTING.md` | Amend | Existing service test documentation and package scripts | Consolidate current runnable gates and label hosted checks separately. |
| `examples/standard/WORKFLOW.md` | Create | Multiple existing team practices | Make specification, slicing, delivery evidence, and product acceptance responsibilities explicit. |
| Product specifications | Reuse | Accepted specifications in `product/` | Preserve decision history and amend contracts explicitly. |
| Architecture decisions | Reuse | Accepted decisions in `architecture/` | Link existing decisions and retain superseded history. |
| `Claude.md` | Omit | Claude does not use a separate entry point | Avoid a second instruction router. |
| `EVIDENCE.md` | Omit | Delivery evidence lives in each issue | Avoid duplicating tracker evidence in a parallel file. |
| `CONTEXT.md` | Omit | Terms are defined in accepted specifications | Avoid a competing vocabulary owner. |
| `CYRUS-LINEAR.md` | Omit | Existing workspace docs already own the verified mapping | Keep one integration contract owner. |
| 17-section `LINEAR-DESCRIPTION.md` | Omit | No accepted team convention for this format | Use the team's existing issue template; section count is not universal. |

## Adapted output

The complete synthetic outputs are in [`standard/`](standard/). `AGENTS.md` says Fieldglass produces inventory forecasts from admitted planning
records. It does not place supplier orders. Product requirements in accepted
specifications govern behavior; accepted architecture decisions govern their
documented trade-offs. A tracker item may prioritize work but cannot authorize
an order-submission capability.

`TESTING.md` points to the exact repository scripts observed for each service,
then names the relevant contract tests for the changed behavior. Hosted CI is
listed as a separate gate with its actual configured status. A missing service
command is reported as a gap rather than replaced with a guessed command.

The Linear integration is owned by the team's existing workspace documentation.
CEO/product, CTO/technical leadership, and engineering use filtered views over
the same records. Readiness, explicit delegation, delivery, and human
acceptance remain separate states. The team reads back its actual configured
state names before relying on them.

The team's current issue description remains its task contract. If the team
later adopts the optional 17-section template, the project owner records that
choice and populates all sections for the particular task. This Standard
example does not imply any external write, agent run, review receipt, merge, or
acceptance.
