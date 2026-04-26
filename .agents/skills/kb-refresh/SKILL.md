---
name: kb-refresh
description: Re-analyze existing pages based on their source files.
---

# 知识库重分析技能（Refresh）

用于对已有 `pages` 进行重建或更新。

## 输入范围

支持：
- 单文件：
  - `wiki/pages/xxx.md`
- 目录：
  - `wiki/pages/<dir>/`
- 全量：
  - `wiki/pages/`

## 执行步骤

### 1. 收集 pages

- 遍历范围内所有 `.md`
- 忽略：`template.md`

### 2. 解析 Frontmatter

- 读取字段：`source`
- 要求：
  - 必须指向 `raw/` 下文件
  - 文件必须存在
- 否则：输出错误信息 Invalid source path
- 跳过该文件

### 3. 构建原始文件列表

- 收集所有合法 source：`raw/…/*.*`

### 4. 调用 analyze

将上述文件列表作为输入，调用SKILL `kb-analyze`

## 约束
- refresh 不直接分析内容
- refresh 仅负责：
  - 从 pages 反查 source
  - 触发 analyze

## 典型场景
- 修改模板后全量重建
- 修复历史数据错误
- 更新解析策略（如 PDF parser）