import { tool } from "@opencode-ai/plugin"
import { inventoryProject } from "../src/opencode/project-bootstrap.mjs"
import { checkTaskDescription } from "../src/opencode/task-description.mjs"

export const ProjectBootstrapPlugin = async () => ({
  tool: {
    project_bootstrap_inventory: tool({
      description:
        "List existing project instruction, contract, test, CI, and tracker paths. Reports paths and categories only; it does not read file contents or assess project maturity.",
      args: {},
      async execute(_args, context) {
        return JSON.stringify(await inventoryProject(context.worktree || context.directory), null, 2)
      },
    }),
    project_bootstrap_check_task: tool({
      description:
        "Check only the structure of a filled ultrawork task description: first-line trigger, numbered sections 1–17 in order, and unresolved {{...}} placeholders. This does not assess content quality, readiness, review, or acceptance.",
      args: {
        description: tool.schema.string().describe("Complete task description text"),
      },
      async execute(args) {
        return JSON.stringify(checkTaskDescription(args.description), null, 2)
      },
    }),
  },
})
