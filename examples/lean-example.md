# Lean adaptation example: ParcelNote

ParcelNote is a fictional single-repository service that accepts shipment
updates and displays them to customers. Its existing `README.md` describes the
API, `tests/` contains a runnable local suite, and `AGENTS.md` is the only
repository-wide agent instruction. A human maintainer approves releases. There
is no configured tracker integration or independent review mechanism.

This is a completed illustrative result, not a claim about a real repository.
The paths and command below belong only to this fictional example. No tracker,
agent, or release action was taken.

## Responsibility map

| Proposed document | Action | Existing owner / source | Reason |
| --- | --- | --- | --- |
| `README.md` API contract | Reuse | Existing `README.md` | It remains the owner of the public API behavior; avoid copying it into an agent guide. |
| `examples/lean/AGENTS.md` | Amend | Existing `AGENTS.md` | Preserve its API constraints; add a concise current boundary, reading order, and link to the test gate. |
| `examples/lean/TESTING.md` | Create | `tests/` and `pyproject.toml` | Record the verified local command and distinguish current checks from future CI. |
| `WORKFLOW.md` | Omit | Existing maintainer practice | One maintainer and one local gate do not justify a second process document. |
| `LINEAR-DESCRIPTION.md` | Omit | No task tracker is configured | An executable tracker prompt would imply an integration that does not exist. |
| `CYRUS-LINEAR.md` | Omit | No Cyrus or Linear configuration | No adapter or delegation contract is available to document. |
| `examples/lean/EVIDENCE.md` | Create | Current release notes are informal | A short delivery receipt makes checks and human release approval visible. |
| `PRD-README.md` / PRDs | Omit | `README.md` describes current behavior; no durable product roadmap | Do not create an empty contract hierarchy. Revisit if product decisions become sustained and cross-cutting. |
| `ADR-README.md` / ADRs | Omit | No significant unresolved architectural trade-off | Record an ADR when a concrete trade-off warrants one. |
| `CONTEXT.md` | Omit | Terms are conventional and documented in the API README | A separate glossary would repeat existing definitions. |
| `Claude.md` | Omit | Claude does not use a separate entry point | Keep the existing agent entry point as the single instruction owner. |

## Adapted output

The complete synthetic outputs are in [`lean/`](lean/). `AGENTS.md` states that ParcelNote currently ingests carrier updates and
displays them. It does not submit shipment changes to carriers. Before a change,
read the API section in `README.md`, this file, and `TESTING.md`. Preserve
customer-visible event ordering and do not add outbound carrier calls without
an accepted product decision. For a conflict, preserve the documented API
contract and report the exact discrepancy.

`TESTING.md` records the observed command `python -m pytest` as the local gate.
It says that a successful local suite is not a hosted CI or release result.
Changed event ordering is checked through the public timeline endpoint using
deterministic carrier fixtures.

`EVIDENCE.md` records candidate revision and changed paths, exact commands and
results, remaining gaps, and the maintainer's release decision as separate
facts. It contains no prefilled passing result or assumed approval.

This setup selects no 17-section task prompt: that format is optional and
ParcelNote has no verified tracker workflow. The bootstrap output contains no
unresolved template tokens.
