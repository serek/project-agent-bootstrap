# Copper Ledger architecture

This is the amended architecture guidance for the fictional Copper Ledger service. It reflects a read-only synthetic audit of the current code layout; it is not a new product contract.

## Runtime boundaries

- FastAPI routes expose the service's HTTP API and delegate application behavior to the service layer.
- PostgreSQL is the durable store. Route and template code access it through the established persistence and service boundaries.
- Server-rendered administration pages are an operator interface to existing service capabilities. They do not create a separate data authority.
- Background workers process queued work through the same application and persistence rules as request handling. A worker is not permission to bypass validation or authorization.

Keep new behavior in the existing owning layer and preserve transaction boundaries. Changes that add external authority, new data flows, or a new persistence boundary need an accepted product or architecture decision before implementation.

## Current quality-gate shape

The repository's testing strategy owns exact commands and CI gate definitions. Its current synthetic CI contract makes pytest, Ruff, and the configured scoped mypy run blocking. Whole-tree mypy is advisory and must not be described as a required merge gate. Consult the testing strategy when changing checks; this architecture note does not redefine them.
