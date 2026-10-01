# LanternDesk as an adaptation example

LanternDesk is a fictional customer-support inbox. Assume its current product
accepts messages, assigns them to agents, and records replies. An AI-drafted
reply and automatic sending are proposed features, not current authority. Its
repository has a runnable local test command and an existing product brief,
but no verified Cyrus, Linear, or independent-review integration.

The bootstrap should first map the existing brief, tests, and instructions to
the proposed documents. A Lean setup could use a short `AGENTS.md`, a truthful
`TESTING.md`, a task prompt, and an evidence handoff. It should omit the
optional Cyrus/Linear adapter until that integration is observed and approved.

For example, a task to add a reply-draft preview can authorize a draft visible
to an agent while keeping send authority with a human. Its Definition of Done
would include a message-level test, a failed-draft case, and evidence that no
automatic send path was added. The target repository's own product decisions
and configured reviewers determine the actual gates.

This example is illustrative. Replace its product name, capabilities, paths,
commands, contracts, reviewers, and task facts with those verified in the
target repository; never copy them as policy.
