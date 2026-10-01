# HarborPortal context

This file preserves the existing context-document role for the fictional
HarborPortal repository. Its vocabulary and product boundary are illustrative.

## Product boundary

HarborPortal is a public information portal. Its React and TypeScript
application renders pages on the server and reads published records from a
managed Postgres database. Edge functions perform bounded application work.
The current application reads and presents published information. It does not
create or publish source records; publication follows the existing content
process.

## Terms

- **Published record**: information admitted for display by the application's
  existing publishing rules.
- **Server-rendered page**: a page whose initial HTML is produced by the
  server-side application before delivery to a visitor.
- **Edge function**: a bounded server-side function used by the application;
  its presence alone does not grant access to new data or external services.
- **Publication**: the existing content process that admits source records for
  public display; changing that process requires its established approval.

## Decision ownership

Accepted ADRs remain the source for their documented architectural trade-offs.
This context file describes current terms and product scope; it does not
replace an ADR or approve a new capability. `QA.md` owns check procedures and
the pull request process owns change review, evidence handoff, and human
acceptance.
