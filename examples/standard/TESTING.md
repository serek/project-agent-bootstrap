# Fieldglass testing contract

## Current runnable gates

Run the service command recorded in that service's `package.json` scripts from
the service directory. The service's accepted specification and the workflow
link its required focused checks. Hosted CI is a separate gate; report its
observed result independently from local commands.

## Behavior checks

Exercise the changed public service boundary through domain logic with
deterministic fixtures. Derive expected forecast values from the governing
specification. If a service has no runnable local command, report that gap
instead of substituting a guessed command.
