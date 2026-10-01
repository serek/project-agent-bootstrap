# Linear team operating model guide

Use this guide when a target team uses Linear for planning or engineering work.
Treat it as concepts to map to observed configuration, not a required workspace
schema or a source of default status names. Read the team's actual configuration
before adapting the guide; record only what was observed.

## Planning objects

- **Initiative:** a strategic outcome that may span multiple projects.
- **Project:** a bounded delivery effort with an owner, outcome, and timeframe.
- **Milestone:** a meaningful checkpoint within a project, expressed as an
  outcome or evidence rather than a date alone.
- **Issue:** a piece of work with one accountable owner, a bounded result, and
  acceptance evidence. Use sub-issues only when their independent outcomes help
  coordination.

Use only the objects the team actually configures. Map parent-child links and
ownership from read-back state rather than assuming a hierarchy is enabled.

## Views by responsibility

CEO / product, CTO / technical leadership, and engineering are filtered views
over the same underlying initiative, project, milestone, and issue records.
They do not require duplicate boards or parallel copies of work.

- **CEO / product view:** initiative outcomes, project health, material
  decisions, dependencies, risks, and human acceptance. Keep implementation
  detail linked at the project or issue where it belongs. Filter to active or
  decision-needed outcomes and group by initiative or project, if those fields
  exist in the team's configuration.
- **CTO / technical leadership view:** project architecture, technical
  dependencies, delivery risk, quality gates, and unresolved technical
  decisions. Filter to blocked or decision-needed work and group by project or
  technical owner, if configured. Route contract decisions to their owning
  product or architecture document.
- **Engineering view:** issue outcome, scope, prerequisites, verification,
  owner, blockers, and handoff evidence. Keep one shared engineering board;
  use the team's configured fields to filter ready, blocked, and review or
  handoff work. Group by project or milestone when useful and supported. A
  board view is a projection of configured state, not an independent
  authorization source.

These are useful views, not mandatory Linear teams, labels, or custom fields.

## Readiness, delegation, and acceptance

Represent these as distinct facts in the team's configured workflow:

1. **Readiness** means a human or documented gate has confirmed that the issue
   has enough authority, context, and acceptance evidence to begin.
2. **Delegation** means an authorized person or system explicitly assigned or
   dispatched the work through the configured mechanism. Readiness alone does
   not imply pickup.
3. **Delivery** means the candidate and its evidence were handed off. It does
   not imply merge, release, or product acceptance.
4. **Human acceptance** means the named product or operational owner reviewed
   the delivered outcome and recorded their decision.

Document who may move each state, the actual configured state name, and what
evidence makes the transition true. Before relying on a state or field, read it
back from the configured team. Never infer an automatic write, assignment, or
dispatch from a status label.

## Teammate roles

Map roles to people or agent capabilities that the team actually has. A useful
division is product owner (outcome and acceptance), technical lead (interfaces
and technical trade-offs), implementer (bounded change and evidence), and
reviewer (independent findings). One person may hold multiple roles when the
team permits it; a role name does not prove that a reviewer is configured or
that a review occurred.

Keep exact reviewers, status names, handoff markers, and write permissions in
the target's operational configuration or its project-specific integration
guide. This generic guide supplies no defaults for them. Tracker reads are
observations; creating or changing tracker state and dispatching teammates
require the target's explicit authorization.

## Read-back and cadence

At team onboarding and whenever the workflow changes, a workspace owner or
authorized team administrator should confirm the configured object types,
fields, state names, role permissions, and delegation mechanism. Read back the
actual configuration; keep a dated link or observation note in the team's
integration guide. Team leads can review initiative and project outcomes at
the team's planning cadence, while engineers update issue evidence as work
moves. A product owner records acceptance after delivery. These are suggested
checkpoints; map them to the team's real cadence and permissions.
