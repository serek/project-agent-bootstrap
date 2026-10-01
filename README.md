# Project agent bootstrap

An adapting starter kit for a repository that uses coding agents, durable
product decisions, local quality gates, and optionally Cyrus + Linear +
OpenCode/OMO. It is not a replacement orchestration controller. The included
`project-bootstrap` skill is designed for Codex and OpenCode skill formats and
can be used by path. Host-specific compatibility has not been smoke-tested.

## Use it

Open Codex in the target repository and give it this request (replace the path):

> Read `<bootstrap-checkout>/skills/project-bootstrap/SKILL.md`
> completely. Audit this repository for a Lean or Standard agent-workflow
> bootstrap. First show the existing-versus-proposed responsibility map and one
> filled example task. Then prepare a reviewable local documentation diff using
> the kit's assets where they fit. Do not publish tracker changes, dispatch an
> agent, install tools, or change runtime configuration.

The skill is deliberately usable by path; installation into a global skill
directory is optional and is not part of this package. Start in an existing
repository so its current contracts, tests, and instructions can be inspected.

For OpenCode's native skill discovery, copy the entire
`skills/project-bootstrap/` directory into the target repository at
`.agents/skills/project-bootstrap/` or `.opencode/skills/project-bootstrap/`.
Check for an existing skill at that path before copying; keep both `assets/`
and `references/` beside `SKILL.md`.

## Optional OpenCode plugin

The repository also provides a small local plugin for two read-only checks.
The local development environment had OpenCode 1.18.32, but plugin registration
has not yet passed a live smoke test. The plugin uses OpenCode's documented
`@opencode-ai/plugin` helper. Its source is kept outside `.opencode/plugins/`,
so opening this repository does not automatically load it.

To install into a target project, copy `plugins/project-bootstrap.ts` into
`.opencode/plugins/` and `src/opencode/` into
`.opencode/src/opencode/`. The imports already match this layout. Restart
OpenCode to load it. The tools are named
`project_bootstrap_inventory` and `project_bootstrap_check_task`.

The inventory tool takes no arguments and reports matching paths and
categories only, with explicit scan errors and truncation status. It does not
read contents, call the network, run shell commands, or write files. The task
checker accepts a `description` string and checks for a first-line
`ultrawork` trigger, numbered section headings 1–17 in
order, and unresolved `{{...}}` placeholders. It reports structural facts
only; it does not judge content quality, readiness, review, or acceptance.

Run the dependency-free tests with `node --test test/opencode.test.mjs`.

## License

Apache-2.0; see [LICENSE](LICENSE).

## Contents

- `skills/project-bootstrap/SKILL.md` — audit, adaptation, and completion
  criteria.
- `skills/project-bootstrap/assets/` — editable document starters. The assets
  are inputs, not authority until adapted and approved in the target repository.
- `examples/lanterndesk-map.md` — short fictional Lean adaptation sketch.
- `examples/lean-example.md` and `examples/standard-example.md` — complete
  illustrative responsibility maps with synthetic adapted documents; these
  are documentation fixtures, not runnable sample applications.
- `examples/web-portal-example.md` and `examples/python-service-example.md` —
  synthetic cross-stack reconciliation cases with illustrative adapted
  documents.
- `skills/project-bootstrap/references/LINEAR-OPERATING-MODEL.md` — optional,
  team-neutral guidance for mapping Linear planning and execution to observed
  configuration.
- `scripts/check_conformance.py` — offline package checks
  (`python3 scripts/check_conformance.py`).

Lean keeps a current-boundary entry point, one runnable gate, a task/evidence
contract, and the project's real review policy. Standard adds explicit
contract/decision indexes and the optional integration document when those
surfaces exist. Both preserve observable behavior, human acceptance, and
truthful incomplete outcomes.

## Boundaries

The kit does not authorize target-project Linear writes, Cyrus delegation,
OpenCode or OMO configuration, global skill installation, external
credentials, target CI setup, or production action. Those require separate
target-project decisions. The package's own offline conformance script is a
local check only. The kit also does not copy example-project product rules or
claim that target reviewers, tests, or security harnesses are available.
