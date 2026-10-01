# ParcelNote testing contract

## Current runnable gate

The verified local gate is `python -m pytest`, run from the repository root
with the development dependencies installed. Hosted CI is not part of this
local result.

## Behavior checks

For a timeline change, exercise the public timeline endpoint with deterministic
carrier fixtures. Verify event ordering and the empty-timeline case. Report
exact commands and exit codes; do not describe an unrun hosted check as a pass.
