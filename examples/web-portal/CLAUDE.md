# HarborPortal agent entry point

## Current product boundary

HarborPortal is a public information portal. It renders published information
through a React and TypeScript server-side rendered application. The current
application reads published records from managed Postgres and uses edge
functions for bounded application work. It does not create or publish source
records; publication follows the existing content process.

## Authority

The existing context document owns current product terms and boundaries.
Accepted ADRs own their recorded architectural decisions. `QA.md` owns the
local, conditional database, and hosted-check procedures. The GitHub pull
request process owns review and human acceptance. A pull request or successful
check does not approve a new product capability.

If a proposed change conflicts with an accepted ADR or the documented product
boundary, identify the source and affected behavior in the pull request and
wait for the existing decision process to resolve it.

## Before changing code

Read this file, the relevant context section, applicable accepted ADRs, and
[`QA.md`](QA.md). Inspect the package scripts and current repository setup
before choosing a command. Keep server-rendered behavior, data access, and edge
function changes within the affected contract and existing authority.

Use the repository's established GitHub pull request process. Record exact
commands and observed outcomes there; label unavailable or skipped checks as
such. Hosted CI runs only when a maintainer starts it manually. Do not infer a
hosted result from local checks.

## Completion

The pull request states the changed behavior, checks actually run, checks not
run and why, and remaining gaps. Human review and acceptance remain explicit
steps in the existing pull request process.
