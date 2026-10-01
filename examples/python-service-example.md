# Python service adaptation example: Copper Ledger

Copper Ledger is a fully fictional mature service built with FastAPI, PostgreSQL, server-rendered administration pages, and background workers. Its existing `AGENTS.md` and `CLAUDE.md`, testing strategy, review workflow, architecture guide, and onboarding guide already own those topics. A read-only audit of this fictional repository found that architecture, onboarding, and review guidance had fallen behind the implementation and CI: blocking checks now include pytest, Ruff, and scoped mypy; whole-tree mypy is advisory.

This fixture demonstrates reconciliation with existing guidance instead of adding generic `TESTING.md`, `WORKFLOW.md`, tracker, or orchestration documents. Names, paths, commands, and observations are synthetic. The example does not claim to inspect or change a real service, tracker, CI system, or agent configuration.

## Responsibility map

| Proposed document or guidance | Action | Existing owner / evidence | Reason and output |
| --- | --- | --- | --- |
| `AGENTS.md` and `CLAUDE.md` | Reuse | Existing entry points | They already define agent routing and repository-wide constraints; no competing instruction file is needed. |
| Testing strategy | Reuse | Existing testing strategy and CI configuration | It remains the owner of test commands and gate semantics. The synthetic audit says pytest, Ruff, and scoped mypy block CI; whole-tree mypy is advisory. |
| `examples/python-service/architecture.md` | Amend | Existing architecture guide, checked against current application and worker boundaries | Replace stale topology and describe the observed API, PostgreSQL, admin-rendering, and worker boundaries in this output. |
| `examples/python-service/onboarding.md` | Amend | Existing onboarding guide and current project scripts | Update the setup path and commands in this output; link to the testing strategy for its authoritative gate details. |
| `examples/python-service/review-workflow.md` | Amend | Existing review workflow and current CI configuration | Correct stale gate claims and retain reviewer responsibilities in this output. |
| Generic `TESTING.md` or `WORKFLOW.md` | Omit | Existing testing strategy and review workflow | A second generic guide would split ownership and drift. |
| Linear, Cyrus, or agent-dispatch guide | Omit | No integration state was established in this fictional audit | No tracker or orchestration configuration is asserted or documented. |
| New agent instructions or architecture decision | Omit | Existing entry points and architecture owner | The reconciliation needs no new instruction router or invented decision record. |

## Adapted outputs

The three complete synthetic amendments are in [`python-service/`](python-service/). The architecture note records the service's current component boundaries without introducing a new product capability. The onboarding note points contributors to existing owned guidance. The review note describes blocking and advisory checks accurately and leaves external reviewer or tracker configuration explicitly unverified.

Commands in these outputs are illustrative and hypothetical. In a real bootstrap, verify command spelling, scope, and CI behavior from project configuration before recording them as facts.
