import { readdir } from "node:fs/promises"
import path from "node:path"

const IGNORED_DIRECTORIES = new Set([
  ".git", ".hg", ".svn", "node_modules", "vendor", "dist", "build",
  "coverage", ".next", ".venv", "venv", ".turbo", ".cache", "target",
  ".output", ".vercel", ".serverless", ".svelte-kit", ".nuxt",
  "generated", "tmp", "temp", "out",
])
const ALLOWED_HIDDEN_DIRECTORIES = new Set([".agents", ".circleci", ".github", ".gitlab", ".opencode"])
const MAX_DEPTH = 12
const MAX_ENTRIES = 20_000
const MAX_FILES = 5_000

const CATEGORIES = [
  ["instructions", (name) => /^(AGENTS(?:\.override)?\.md|CLAUDE\.md|GEMINI\.md|CONSTITUTION\.md)$/i.test(name) || /(^|\/)\.agents\//i.test(name) || /(^|\/)\.opencode\/(skills|agents)\//i.test(name)],
  ["contracts", (name) => /(^|\/)(docs?\/)?(adrs?|prds?|contracts?)(\/|$)/i.test(name) || /(^|\/)(CONTEXT|TESTING|WORKFLOW|EVIDENCE)\.md$/i.test(name)],
  ["tests", (name) => /(^|\/)(tests?|__tests__|spec)(\/|$)/i.test(name) || /\.(test|spec)\.[cm]?[jt]sx?$/i.test(name)],
  ["ci", (name) => name.startsWith(".github/workflows/") || name.startsWith(".gitlab/") || /(^|\/)(Jenkinsfile|azure-pipelines\.ya?ml|\.circleci\/config\.ya?ml)$/i.test(name)],
  ["tracker", (name) => /(^|\/)(linear|tracker|issues?)(\/|$)/i.test(name) || /(^|\/)(CYRUS-LINEAR|LINEAR-DESCRIPTION)(\.md)?(\.template)?$/i.test(name)],
]

function categoriesFor(relativePath, basename) {
  const candidate = relativePath.split(path.sep).join("/")
  return CATEGORIES.filter(([, matches]) => matches(candidate) || matches(basename)).map(([category]) => category)
}

export async function inventoryProject(projectRoot) {
  const root = path.resolve(projectRoot)
  const files = []
  const scanErrors = []
  const pending = [{ directory: root, depth: 0 }]
  let entriesSeen = 0
  let truncated = false

  while (pending.length > 0 && !truncated) {
    const { directory, depth } = pending.shift()
    let entries
    try {
      entries = await readdir(directory, { withFileTypes: true })
    } catch (error) {
      scanErrors.push({ path: path.relative(root, directory).split(path.sep).join("/") || ".", code: error.code || "READ_ERROR" })
      continue
    }
    entries.sort((a, b) => a.name < b.name ? -1 : a.name > b.name ? 1 : 0)
    const availableEntries = MAX_ENTRIES - entriesSeen
    if (entries.length > availableEntries) truncated = true
    for (const entry of entries.slice(0, availableEntries)) {
      entriesSeen += 1
      if (entry.isSymbolicLink()) continue
      const absolute = path.join(directory, entry.name)
      if (entry.isDirectory()) {
        if (IGNORED_DIRECTORIES.has(entry.name)) continue
        if (entry.name.startsWith(".") && !ALLOWED_HIDDEN_DIRECTORIES.has(entry.name)) continue
        if (depth >= MAX_DEPTH) {
          truncated = true
          continue
        }
        pending.push({ directory: absolute, depth: depth + 1 })
      } else if (entry.isFile() && !entry.name.startsWith(".env")) {
        const relativePath = path.relative(root, absolute).split(path.sep).join("/")
        const categories = categoriesFor(relativePath, entry.name)
        if (categories.length > 0) {
          if (files.length >= MAX_FILES) {
            truncated = true
            break
          }
          files.push({ path: relativePath, categories })
        }
      }
    }
  }

  files.sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0)
  scanErrors.sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : 0)
  return {
    files,
    truncated,
    scanErrors,
    scope: "Existing paths only; file contents are not read.",
  }
}
