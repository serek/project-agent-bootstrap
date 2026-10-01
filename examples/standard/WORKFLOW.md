# Fieldglass engineering workflow

## Available skills in this fictional fixture

The example assumes the repository has installed `grilling`,
`domain-modeling`, `codebase-design`, `tdd`, `implementation`, `code-review`,
and `summarize`. A real bootstrap names only skills actually present. If one is
absent, use the owning document or ordinary repository workflow for that phase;
none of these skills is a prerequisite for using this guide.

1. **Shape:** identify the user outcome, current evidence, and governing
   product or architecture source. Use `grilling` when available to surface
   unresolved decisions. Finish when authority and unresolved choices are clear.
2. **Specify:** record behavior changes in the owning product specification
   and significant technical trade-offs in an architecture decision. Preserve
   prior reasoning; use `domain-modeling` when available.
3. **Slice:** use an issue for one bounded, independently verifiable outcome.
   A milestone is a project checkpoint; readiness does not assign work.
4. **Design and implement:** understand the baseline, make a simple coherent
   change within service ownership, and verify the result independently at its
   public boundary. Use `codebase-design`, `tdd`, and `implementation` when
   available; otherwise follow the accepted contract and repository practices.
5. **Review:** run applicable local gates and configured independent review.
   Use `code-review` when available. Record actual results and unresolved
   findings; a configured reviewer is not a completed review.
6. **Deliver:** attach candidate identity and evidence to the configured issue.
   Use `summarize` when available. Explicit delegation is a separate authorized
   action.
7. **Accept:** the product owner records whether the delivered outcome meets
   the agreed requirement. Delivery alone is not acceptance.

CEO/product, CTO/technical leadership, and engineering views filter the same
initiative, project, milestone, and issue records. They do not create duplicate
boards or work items. Read actual configured fields and state names before
using them; this example defines no defaults.
