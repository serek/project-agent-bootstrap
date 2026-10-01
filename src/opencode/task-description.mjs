const SECTION_HEADING = /^##\s+(\d{1,2})\.(?:\s+.+)?\s*$/gm

export function checkTaskDescription(description) {
  if (typeof description !== "string") throw new TypeError("description must be a string")

  const firstLine = description.split(/\r?\n/, 1)[0].trim()
  const actual = [...description.matchAll(SECTION_HEADING)].map((match) => Number(match[1]))
  const expected = Array.from({ length: 17 }, (_, index) => index + 1)
  const missing = expected.filter((number) => !actual.includes(number))
  const duplicates = [...new Set(actual.filter((number, index) => actual.indexOf(number) !== index))]
  const placeholders = [...description.matchAll(/\{\{[^{}\r\n]*\}\}/g)].map((match) => ({
    placeholder: match[0],
    index: match.index,
  }))
  const sectionsPassed = actual.length === 17 && actual.every((number, index) => number === expected[index])
  const checks = {
    firstLineTrigger: { passed: firstLine === "ultrawork", expected: "ultrawork", actual: firstLine },
    sections: { passed: sectionsPassed && duplicates.length === 0, expected, actual, missing, duplicates },
    unresolvedPlaceholders: { passed: placeholders.length === 0, occurrences: placeholders },
  }

  return {
    passed: Object.values(checks).every((check) => check.passed),
    checks,
    limitation: "Structural checks only. This result does not assess content quality, readiness, review, or acceptance.",
  }
}
