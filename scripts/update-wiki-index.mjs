#!/usr/bin/env node

import { readdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const wikiDir = path.join(root, "wiki")
const indexPath = path.join(wikiDir, "index.md")
const sections = [
  ["topics", "主题"],
  ["papers", "论文"],
  ["chats", "对话"],
]
const startMarker = "<!-- AUTO-GENERATED:START -->"
const endMarker = "<!-- AUTO-GENERATED:END -->"

function frontmatterValue(content, key) {
  const frontmatter = content.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (!frontmatter) return ""
  const match = frontmatter[1].match(new RegExp(`^${key}:\\s*(.*)$`, "m"))
  return match?.[1].trim().replace(/^['"]|['"]$/g, "") ?? ""
}

function pageTitle(content, fallback) {
  const heading = content.match(/^#\s+(.+)$/m)?.[1].trim()
  if (!heading) return fallback
  const wikilink = heading.match(/^\[\[(?:[^|\]]+\|)?([^\]]+)\]\]$/)
  return wikilink?.[1] ?? heading.replace(/\*\*/g, "")
}

function fallbackSummary(content) {
  const body = content.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, "")
  return (
    body
      .split(/\r?\n/)
      .map((line) => line.trim())
      .find(
        (line) =>
          line &&
          !line.startsWith("#") &&
          !line.startsWith("-") &&
          !line.startsWith("<!--"),
      ) ?? "暂无摘要。"
  )
}

async function collectPages(directory) {
  const absoluteDir = path.join(wikiDir, directory)
  let names = []
  try {
    names = await readdir(absoluteDir)
  } catch (error) {
    if (error.code === "ENOENT") return []
    throw error
  }

  return Promise.all(
    names
      .filter((name) => name.endsWith(".md") && name !== "template.md")
      .map(async (name) => {
        const content = await readFile(path.join(absoluteDir, name), "utf8")
        const stem = name.slice(0, -3)
        return {
          link: `${directory}/${stem}`,
          title: pageTitle(content, stem),
          updated:
            frontmatterValue(content, "updated") ||
            frontmatterValue(content, "created") ||
            "0000-00-00",
          summary: frontmatterValue(content, "summary") || fallbackSummary(content),
        }
      }),
  )
}

const groups = await Promise.all(
  sections.map(async ([directory, label]) => ({
    directory,
    label,
    pages: await collectPages(directory),
  })),
)
const allPages = groups.flatMap(({ pages }) => pages)
const recentPages = allPages
  .toSorted(
    (a, b) =>
      b.updated.localeCompare(a.updated) || a.link.localeCompare(b.link),
  )
  .slice(0, 5)

const stats = groups.map(({ label, pages }) => `${label} ${pages.length}`).join(" · ")
const generated = [
  `- 总计 ${allPages.length} 页 · ${stats}`,
  "",
  "### 最近更新",
  "",
  ...recentPages.map(
    ({ link, title, updated, summary }) =>
      `- ${updated.slice(0, 10)} · [[${link}|${title}]] — ${summary}`,
  ),
].join("\n")

const index = await readFile(indexPath, "utf8")
const start = index.indexOf(startMarker)
const end = index.indexOf(endMarker)
if (start === -1 || end === -1 || end < start) {
  throw new Error("wiki/index.md 缺少有效的 AUTO-GENERATED 标记")
}

const generatedIndex = `${index.slice(0, start + startMarker.length)}\n\n${generated}\n\n${index.slice(end)}`
const latestDate = recentPages[0]?.updated.slice(0, 10)
const nextIndex = latestDate
  ? generatedIndex.replace(/^updated:\s*.*$/m, `updated: ${latestDate}`)
  : generatedIndex
if (nextIndex !== index) {
  await writeFile(indexPath, nextIndex)
  console.log("已更新 wiki/index.md")
} else {
  console.log("wiki/index.md 已是最新")
}
