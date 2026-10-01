# Fieldglass agent entry point

## Current boundary

Fieldglass produces inventory forecasts from admitted planning records. It
does not submit orders to suppliers.

## Authority

Accepted product specifications in `product/` govern product behavior.
Accepted architecture decisions in `architecture/` govern their recorded
trade-offs. Linear prioritizes and coordinates work; an issue does not approve
a new order-submission capability.

## Before changing files

Read this file, the relevant specification and architecture decision, and
[`TESTING.md`](TESTING.md). Follow the available repository skills for the
task. Report conflicts against the owning source.

## Delivery and acceptance

Record candidate identity, changed paths, checks, review findings, and gaps in
the issue's configured evidence fields. Delivery does not imply merge, release,
or product-owner acceptance.
