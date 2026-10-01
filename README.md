# Project agent bootstrap

An adapting starter kit for a repository that uses coding agents, durable
product decisions, local quality gates, and optionally Cyrus + Linear +
OpenCode/OMO. It is not a replacement orchestration controller. The included
`project-bootstrap` skill is compatible with Codex and OpenCode.

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
Check for an existing skill at that path before copying; keep the `assets/`
directory beside `SKILL.md`. This package does not contain an executable
OpenCode plugin.

## License

Apache-2.0; see [LICENSE](LICENSE).

## Contents

- `skills/project-bootstrap/SKILL.md` — audit, adaptation, and completion
  criteria.
- `skills/project-bootstrap/assets/` — editable document starters. The assets
  are inputs, not authority until adapted and approved in the target repository.
- `examples/lanterndesk-map.md` — fictional adaptation example; replace its
  product facts with those observed in the target repository.

Lean keeps a current-boundary entry point, one runnable gate, a task/evidence
contract, and the project's real review policy. Standard adds explicit
contract/decision indexes and the optional integration document when those
surfaces exist. Both preserve observable behavior, human acceptance, and
truthful incomplete outcomes.

## Boundaries

The kit does not authorize Linear writes, Cyrus delegation, OpenCode or OMO
configuration, global skill installation, external credentials, CI setup, or
production action. Those require separate target-project decisions. It also
does not copy the example project's product rules or claim that target
reviewers, tests, or security harnesses are available.
