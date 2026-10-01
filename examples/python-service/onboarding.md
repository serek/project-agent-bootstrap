# Copper Ledger onboarding

This is the amended onboarding guide for the fictional service. Existing `AGENTS.md` and `CLAUDE.md` remain the instruction entry points; the testing strategy owns quality-check details, and the review workflow owns review and delivery responsibilities.

## Local setup

Use the repository's documented Python environment and dependency lock. The following commands are illustrative placeholders for this fixture, not verified commands for a real project:

```sh
uv sync --dev
uv run pytest
```

Start the API and worker only with the repository's documented local configuration. Keep credentials local and use the project's approved development data. Do not infer access to shared, staging, or production systems from successful local setup.

Before changing code, read the relevant architecture section and the existing testing strategy. For current check names, scopes, and blocking status, follow the testing strategy and CI configuration rather than copying commands into this guide.

## First-change completion

A first change is ready for review when the relevant behavior is understood, the repository's blocking local checks have been run as applicable, their exact results are recorded, and any unavailable service or CI dependency is stated as a gap. A local setup command does not establish CI success or reviewer approval.
