# ParcelNote agent entry point

## Current boundary

ParcelNote ingests carrier shipment updates and displays the resulting event
timeline to customers. The current service has no outbound carrier-update or
shipment-change capability.

## Authority

The API contract in the root `README.md` defines customer-visible event
ordering. The maintainer's accepted product decisions govern new behavior.
An issue or tool does not grant permission to contact carriers or release a
change.

## Before changing files

Read the API contract, this file, and [`TESTING.md`](TESTING.md). Preserve event
ordering and use deterministic carrier fixtures for behavior checks. Report a
contract conflict with the specific source and affected behavior.

## Delivery

Record candidate revision, changed paths, checks, and remaining gaps in
[`EVIDENCE.md`](EVIDENCE.md). The maintainer decides whether to release.
