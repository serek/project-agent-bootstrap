# Copper Ledger review workflow

This is the amended review workflow for the fictional service. Use the existing testing strategy as the authority for command details and CI configuration as the authority for hosted gate status.

## Checks

The synthetic current CI configuration has these blocking checks:

- pytest for automated behavior checks;
- Ruff for configured lint and formatting checks;
- mypy over the configured scoped paths.

Whole-tree mypy is advisory. Report its result separately; its status does not replace the scoped blocking check. The illustrative commands below are hypothetical and must be verified against a real repository before use:

```sh
uv run pytest
uv run ruff check .
uv run mypy src/domain src/web
uv run mypy .  # advisory only
```

## Review and handoff

Reviewers assess the change against its owning product and architecture guidance, changed behavior, data handling, and failure paths. Record the candidate revision, changed paths, exact checks and results, unresolved findings, and any unavailable check. Distinguish local command results from hosted CI results.

This example has not verified whether independent agent reviewers, a tracker, or an orchestration system are configured. A reviewer being mentioned in a repository document would not establish that a review ran. A tracker item, if one exists, does not itself approve new service authority. Human acceptance remains a separate recorded decision.
