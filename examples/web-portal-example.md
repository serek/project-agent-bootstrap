# Web portal adaptation example: HarborPortal

HarborPortal is a fully fictional public information portal built with React,
TypeScript, and server-side rendering. Its application uses a managed Postgres
database and edge functions for bounded application work. The repository
already has `CLAUDE.md`, `QA.md`, a context document, accepted ADRs, and a
GitHub pull request process. Local pre-push checks are expected; hosted CI is
available only when a maintainer starts it manually. Database checks depend on
having the disposable local database setup available.

This fixture demonstrates a cross-stack bootstrap fit. Every name, path,
command, process, and status below is hypothetical. It contains no real
project material and makes no claim that checks or reviews ran.

## Responsibility map

| Proposed document or owner | Action | Existing owner / source | Adapted output | Reason |
| --- | --- | --- | --- | --- |
| `examples/web-portal/CLAUDE.md` | Amend | Existing `CLAUDE.md` | [`web-portal/CLAUDE.md`](web-portal/CLAUDE.md) | Keep task routing in its current home and make the boundary, read order, and links to QA and context unambiguous. |
| `examples/web-portal/QA.md` | Amend | Existing `QA.md` | [`web-portal/QA.md`](web-portal/QA.md) | Reconcile the local pre-push gate, optional database checks, and manually started hosted checks; define accurate evidence language. |
| `examples/web-portal/CONTEXT.md` | Amend | Existing context document | [`web-portal/CONTEXT.md`](web-portal/CONTEXT.md) | Keep domain terms and the current public information and publishing boundary in their existing owner without duplicating procedures. |
| `examples/web-portal/.github/PULL_REQUEST_TEMPLATE.md` | Amend | Existing GitHub pull request process | [`web-portal/.github/PULL_REQUEST_TEMPLATE.md`](web-portal/.github/PULL_REQUEST_TEMPLATE.md) | Add a concise record of local, conditional database, and hosted-check state to the existing review handoff. |
| Accepted architecture decisions | Reuse | Existing accepted ADRs | None | They remain authoritative for their recorded trade-offs. New or changed architecture still follows their amendment process. |
| `AGENTS.md` | Omit | Existing `CLAUDE.md` and context owner | None | A new root instruction entry point would duplicate the existing guidance. |
| `TESTING.md` / `TESTING.md.template` | Omit | Existing `QA.md` | None | QA already owns the current quality gate; a second testing guide would create competing commands and evidence language. |
| `WORKFLOW.md` / `WORKFLOW.md.template` | Omit | Existing pull request process | None | The established review flow already owns implementation handoff and human acceptance. |
| `EVIDENCE.md` / `EVIDENCE.md.template` | Omit | Existing QA guide and PR template | None | The PR is the delivery record; a parallel receipt would split check status. |
| Linear prompt, Linear/Cyrus integration docs | Omit | No such verified workflow is part of this fixture | None | No tracker or orchestration contract is assumed. |
| New PRD or ADR index | Omit | Existing context and accepted ADRs | None | Existing decision owners are sufficient for this example; the map does not add a new contract hierarchy. |

The action vocabulary is deliberately limited to **Reuse**, **Amend**, and
**Omit**. No row proposes creating a new generic owner.

## Adapted output

The complete synthetic amended documents are in [`web-portal/`](web-portal/).
`CLAUDE.md` points to the existing authority owners. `QA.md` describes the
hypothetical local pre-push command, conditional database gate, and manual
hosted CI without representing any of them as completed. `CONTEXT.md` keeps the
product boundary and terms together. The pull request template asks the author
to state observed results and gaps.

All commands are illustrative placeholders for this fictional fixture. The
status words in the QA guide describe possible evidence states, not actual
workflow runs. In particular, a local pass does not establish a hosted CI pass,
and a hosted check that was not manually started remains unrun.
