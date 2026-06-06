---
name: ppt-generate
description: 根据用户提供的 outline.md 或 Zotero citation key 读取 PPT 目录提纲和 presentation frontmatter 配置，调用 Presentations 插件生成可编辑 PPTX。适用于用户已经有论文或报告提纲，并要求制作 PowerPoint 文件的场景。
---

# ppt-generate

Use this skill when the user provides an `outline.md` or a Zotero citation key and wants a PPTX generated from the saved outline.

## Required Input

- Absolute or project-relative path to `outline.md`; or
- Zotero citation key, such as `meng_2026_agent`.

The outline should include YAML frontmatter with a `presentation` block produced by `ppt-paper-outline`. If fields are missing, use the defaults below and note the assumption.

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

## Workflow

1. Resolve and read `outline.md`.
   - If the user input is a path ending in `outline.md`, use that file.
   - Otherwise treat the input as a Zotero citation key and look for `<project-root>/wiki/presentations/<citation_key>/outline.md`.
   - If that file does not exist, stop and tell the user to run `ppt-paper-outline` for that citation key first.
   - Parse frontmatter.
   - Parse the slide outline table: slide number, title, main point, speaker notes/script.
   - Infer `citation_key` from frontmatter or the parent directory name.
   - If the outline is missing slide-level content, stop and ask for a usable outline.

2. Resolve output path.
   - Resolve `PRESENTATION_DIR=<project-root>/wiki/presentations/<citation_key>`.
   - If `presentation.output_dir` is set, use it.
   - Otherwise use `PRESENTATION_DIR`.
   - If `presentation.output_filename` is empty or still contains `<citation_key>`, replace it with `<citation_key>.pptx`.
   - If the target PPTX already exists and `overwrite_existing_pptx` is `confirm`, ask the user before overwriting.

3. Invoke the Presentations plugin workflow.
   - Read the installed Presentations skill instructions before building.
   - Use artifact-tool presentation JSX only.
   - Do not use Python OOXML edits, LibreOffice save-as, or any non-artifact-tool PPTX runtime.
   - Use thread-scoped workspace paths under the citation presentation directory, not under the project root:
     - `PRESENTATION_DIR=<project-root>/wiki/presentations/<citation_key>`
     - `WORKSPACE=$PRESENTATION_DIR/outputs/<thread>/presentations/<task-slug>/`
     - `SLIDES_DIR=$WORKSPACE/slides`
     - `PREVIEW_DIR=$WORKSPACE/preview`
     - `LAYOUT_DIR=$WORKSPACE/layout`
     - `ASSET_DIR=$WORKSPACE/assets`
     - `QA_DIR=$WORKSPACE/qa`
   - If the input `outline.md` is outside `wiki/presentations/<citation_key>/`, still create or reuse `PRESENTATION_DIR` from the inferred `citation_key` and place the workspace there.
   - If `presentation.output_dir` is empty, write the final PPTX to `PRESENTATION_DIR`; otherwise write only the final deliverable to the requested output directory.

4. Select mode and profile from frontmatter.
   - `task_mode: create`: build a new deck from the outline.
   - `task_mode: template-following`: only when `template_pptx` points to a real PPTX; import, duplicate mapped source slides, and edit copied slides in place.
   - `task_mode: targeted-edit`: only when the user supplies an existing deck and asks for limited edits.
   - Use `deck_profile` as the primary profile. Default technical paper decks to `engineering-platform`.

5. Build planning artifacts required by Presentations.
   - Create `profile-plan.txt`.
   - Create `claim-spine.txt` from the outline. Convert topic titles into claim titles when needed.
   - Create `design-system.txt` from `style`, `audience`, `slide_size`, `visual_density`, and `assets_policy`.
   - Create `contact-sheet-plan.txt` with varied macro layouts.

6. Build the PPTX.
   - Create one editable slide module per outline row.
   - Use native editable shapes, text, tables, diagrams, and chart-like constructs.
   - Include speaker notes when `include_speaker_notes: true`.
   - For `assets_policy: editable_shapes_first`, prefer editable geometry over screenshots.
   - Use image generation only if `allow_imagegen: true` and it is not fabricating real logos, UI, evidence, or product imagery.

7. QA and export.
   - Render every slide to PNG through artifact-tool.
   - Review contact sheet and full-size renders.
   - Run layout checks and fix hard failures.
   - Export the final PPTX only after QA passes.
   - If `keep_qa_artifacts: false`, run the Presentations cleanup helper and keep only final deliverables.

## Final Response

Report only:

- source outline path
- final PPTX absolute path
- slide count
- QA/render status
- any important residual caveat
