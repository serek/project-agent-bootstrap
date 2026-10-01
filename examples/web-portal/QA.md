# HarborPortal quality checks

This is the complete synthetic QA guide for the fictional HarborPortal
fixture. Its commands and workflow are hypothetical and must not be treated as
commands for another repository.

## Local pre-push gate

Before pushing a code change, run the repository's local gate from the project
root:

```sh
pnpm check
pnpm test
```

In this fixture, `pnpm check` represents linting and TypeScript validation, and
`pnpm test` represents the deterministic application test suite. Confirm the
actual package scripts before using commands in a real checkout. Record the
exact command, exit result, and any relevant scope in the pull request.

## Conditional database checks

When a change affects database schema, data access, or an edge function that
uses persisted data, run the database checks if the repository's disposable
local database environment is available:

```sh
pnpm db:check
pnpm db:test
```

These checks are conditional on both relevant code changes and an available
local database setup. If the setup is unavailable, state `Not run` and why;
do not describe the database behavior as verified. For changes outside these
areas, mark the database checks `Not applicable` and give the reason.

Use synthetic or repository-approved local records. Do not point these
illustrative checks at production data or enable an external provider as a
shortcut.

## Hosted CI

Hosted CI is manual-only in this fixture. A maintainer must start the hosted
workflow for the candidate revision. The local pre-push gate does not start or
prove a hosted run.

Report one observed state for the exact candidate revision:

- `Not requested`: nobody requested a hosted run.
- `Queued`: a maintainer started it and it has not completed.
- `Passed`: the started run completed successfully.
- `Failed`: the started run completed with a failure.
- `Not run`: it was expected or requested, but no run was started; state why.

Include a run reference when one exists. Leave the outcome unknown while the
run is queued. Never claim a pass based on an earlier revision, a local check,
or a workflow that was not started.

## Evidence and completion

The pull request template is the delivery record. It lists local results,
conditional database applicability and outcome, hosted CI state, and remaining
gaps separately. A check is complete only when its command or hosted run has
actually executed for the candidate being reviewed. Skips and unavailable
checks remain visible; they are not passes.
