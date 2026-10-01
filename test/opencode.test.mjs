import assert from "node:assert/strict"
import { mkdtemp, mkdir, writeFile, rm } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"
import { inventoryProject } from "../src/opencode/project-bootstrap.mjs"
import { checkTaskDescription } from "../src/opencode/task-description.mjs"

const completeDescription = ["ultrawork", ...Array.from({ length: 17 }, (_, i) => `## ${i + 1}. Section ${i + 1}\nFilled content.`)].join("\n\n")

test("accepts a filled description with a first-line trigger and ordered 17 sections", () => {
  assert.equal(checkTaskDescription(completeDescription).passed, true)
})

test("reports missing, duplicate, and out-of-order section numbers", () => {
  const result = checkTaskDescription(completeDescription.replace("## 8.", "## 18.").replace("## 9.", "## 8."))
  assert.equal(result.checks.sections.passed, false)
  assert.deepEqual(result.checks.sections.missing, [9])
  assert.equal(result.checks.sections.actual[7], 18)
})

test("requires ultrawork first and reports unresolved placeholders", () => {
  const result = checkTaskDescription(completeDescription.replace(/^ultrawork/, "# Task").replace("Filled content.", "{{TODO}}"))
  assert.equal(result.checks.firstLineTrigger.passed, false)
  assert.equal(result.checks.unresolvedPlaceholders.passed, false)
  assert.deepEqual(result.checks.unresolvedPlaceholders.occurrences.map(({ placeholder }) => placeholder), ["{{TODO}}"])
  assert.match(result.limitation, /does not assess content quality/)
})

test("rejects non-text task descriptions", () => {
  assert.throws(() => checkTaskDescription(null), { name: "TypeError" })
})

test("reports duplicate numbered headings and the missing section", () => {
  const result = checkTaskDescription(completeDescription.replace("## 9.", "## 8."))
  assert.equal(result.checks.sections.passed, false)
  assert.deepEqual(result.checks.sections.missing, [9])
  assert.deepEqual(result.checks.sections.duplicates, [8])
})

test("reports when a deep project tree exceeds the scan limit", async (context) => {
  const root = await mkdtemp(path.join(os.tmpdir(), "project-bootstrap-depth-"))
  context.after(() => rm(root, { recursive: true, force: true }))
  let nested = root
  for (let depth = 0; depth < 13; depth += 1) {
    nested = path.join(nested, "level-" + depth)
    await mkdir(nested)
  }
  const report = await inventoryProject(root)
  assert.equal(report.truncated, true)
})

test("reports root scan failures instead of implying a complete inventory", async () => {
  const report = await inventoryProject(path.join(os.tmpdir(), "missing-project-bootstrap-root"))
  assert.deepEqual(report.files, [])
  assert.equal(report.truncated, false)
  assert.deepEqual(report.scanErrors, [{ path: ".", code: "ENOENT" }])
})

test("inventory reports sorted matching paths without reading contents or scanning ignored trees", async (context) => {
  const root = await mkdtemp(path.join(os.tmpdir(), "project-bootstrap-"))
  context.after(() => rm(root, { recursive: true, force: true }))
  await mkdir(path.join(root, "docs/prds"), { recursive: true })
  await mkdir(path.join(root, "tests"), { recursive: true })
  await mkdir(path.join(root, ".github/workflows"), { recursive: true })
  await mkdir(path.join(root, ".cache/hidden"), { recursive: true })
  await mkdir(path.join(root, ".next/generated"), { recursive: true })
  await mkdir(path.join(root, "generated/contracts"), { recursive: true })
  await mkdir(path.join(root, "node_modules/secret"), { recursive: true })
  await writeFile(path.join(root, "AGENTS.md"), "SECRET CONTENT MUST NOT APPEAR")
  await writeFile(path.join(root, "docs/prds/roadmap.md"), "Private contract content")
  await writeFile(path.join(root, "tests/example.test.js"), "test")
  await writeFile(path.join(root, ".github/workflows/ci.yml"), "ci")
  await writeFile(path.join(root, "node_modules/secret/AGENTS.md"), "secret")
  await writeFile(path.join(root, ".cache/hidden/AGENTS.md"), "secret")
  await writeFile(path.join(root, ".next/generated/AGENTS.md"), "secret")
  await writeFile(path.join(root, "generated/contracts/PRD.md"), "secret")
  await writeFile(path.join(root, ".env.local"), "secret")

  const report = await inventoryProject(root)
  assert.deepEqual(report.files.map(({ path: item }) => item), [".github/workflows/ci.yml", "AGENTS.md", "docs/prds/roadmap.md", "tests/example.test.js"])
  assert.equal(JSON.stringify(report).includes("SECRET CONTENT"), false)
  assert.equal(JSON.stringify(report).includes(".env.local"), false)
  assert.equal(report.truncated, false)
  assert.deepEqual(report.scanErrors, [])
  assert.deepEqual(report.files.find(({ path: item }) => item === "AGENTS.md").categories, ["instructions"])
})
