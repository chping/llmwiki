---
name: ppt-paper-outline
description: 基于用户提供的 Zotero citation key 查找论文，全面阅读后生成用于 Presentation 的 PPT 目录提纲，并保存到当前项目 presentations/<citation_key>/outline.md。适用于用户要求为论文准备 PPT 提纲、逐页标题、主要观点和解说词，但暂不制作 PPT 的场景。
---

# ppt-paper-outline

Use this skill when the user provides a Zotero citation key and wants a paper-based PPT outline saved in the current project.

## Inputs

- Required: one Zotero citation key, e.g. `chendeli_202606_auto_research_survey`
- Optional: slide count, audience, language, talk duration, emphasis

Default output language is Chinese unless the user says otherwise.

## Workflow

1. Locate the Zotero item.
   - Use Zotero tools first.
   - If direct search by citation key is unavailable, export BibTeX and match the entry key exactly.
   - Record citation key, Zotero item key, title, authors, year, DOI/URL, collection path if available.
   - If multiple items match, ask the user to choose.
   - If no item matches, stop and report the missing citation key.
2. Read the paper fully.
   - Prefer Zotero PDF/full-text/attachment content.
   - If Zotero has only a URL, retrieve the PDF/page from the recorded URL when possible.
   - Cover at least: abstract, introduction, definitions, framework/taxonomy, methods/architecture, system comparison, evaluation, limitations/challenges, future work, conclusion, key tables and figures.
   - Do not rely only on abstract or metadata.
3. Create the PPT outline.
   - Default to 12-20 slides unless the user specifies otherwise.
   - For every slide include:
     - slide number
     - slide title
     - main point
     - speaker notes / script
   - Favor a coherent narrative over exhaustive section-by-section copying.
   - Make the outline suitable for later PPT creation, but do not create or edit a PPT unless the user explicitly asks.
4. Save the outline.
   - Target directory: `<project-root>/wiki/presentations/<citation_key>/`
   - If the directory does not exist, create it.
   - Target file: `<project-root>/wiki/presentations/<citation_key>/outline.md`
   - If `outline.md` already exists, ask the user before overwriting.
5. Markdown format.
   - Include YAML frontmatter with at least:
     - `title`
     - `citation_key`
     - `zotero_item_key`
     - `created`
     - `updated`
     - `presentation`
   - Put Presentation plugin options under `presentation` so `ppt-generate` can read them later. Use this default shape unless the user specifies overrides:

```yaml
presentation:
  task_mode: create
  deck_profile: engineering-platform
  template_pptx: ""
  reference_deck: ""
  style: academic-tech
  audience: technical-research
  slide_size: "1280x720"
  language: zh-CN
  output_dir: ""
  output_filename: "<citation_key>.pptx"
  include_speaker_notes: true
  visual_density: standard
  assets_policy: editable_shapes_first
  allow_imagegen: false
  keep_qa_artifacts: false
  overwrite_existing_pptx: confirm
```

After the `presentation` block:

- Set `deck_profile` from the paper type when obvious: AI/EDA/system papers usually use `engineering-platform`; strategy surveys use `strategy-leadership`; dense appendix/table decks use `appendix-heavy`.
- Set `task_mode: template-following` only when the user provides a PPTX template/source deck.
- Use one main heading and a Markdown table for the slide outline.
- Keep paragraphs as single continuous lines.
- Run `npx --yes markdownlint-cli <file>` if available; fix formatting issues before finishing.

## Output Contract

Final response should state:

- the Zotero item found
- the citation key used
- the saved absolute file path
- whether markdownlint passed
