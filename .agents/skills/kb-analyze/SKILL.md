---
name: kb-analyze
description: Analyze raw source files and update knowledge-base pages.
---

# 知识库分析技能（Analyze）

输入：一组原始文件路径（位于 `raw/` 目录）

## 全局写入和更新规则

在更新 `pages / topics / concepts / entities` 页面时，必须采用“先读取、后比较、再写入”的策略，避免重复写入和无意义覆盖。

### 1. 写入前读取模板和现有页面
在更新任何 `.md` 页面前，必须先读取目录下的`template.md`模板和已有内容：
- 若页面不存在，则按模板创建新页面
- 若页面已存在，则解析其 Frontmatter 和正文内容
- 根据`template.md`的要求，移除模板中不再存在的字段，保留已有 Frontmatter 中仍然有效的字段
- 仅更新必要字段，例如：
  - `updated`
  - `sources`
  - `related_pages`
  - `related_topics`
  - `related_concepts`
  - `related_entities`

### 2. Pages 页面更新策略

`wiki/pages/` 页面与原始文件保持 1:1 映射，因此 pages 页面可以按当前原始文件内容进行整体重写。

规则：
- 根据模板`template.md`，从 page 的 Frontmatter 的移除模板 Frontmatter 中不存在的项目，添加缺失的项目
- 根据模板`template.md`，正文内容可根据当前 source 重新生成
- 不合并旧正文，避免旧解析结果污染新分析结果
- 若重新分析结果与旧内容完全一致，则不写入文件，仅在日志中记录为 unchanged

### 3. Topics / Concepts / Entities 页面更新策略

`topics / concepts / entities` 页面可能聚合多个 source，因此禁止整体覆盖正文。

必须采用增量合并策略：
- 读取已有页面
- 根据模板`template.md`，保留或更新 Frontmatter
- 定位与当前 source/page 相关的内容块
- 若同一 source/page 已存在对应内容块，则更新该内容块
- 若不存在，则追加新的内容块
- 不删除其他 source/page 贡献的内容，除非用户明确要求重建

推荐为每个来源内容块添加稳定边界标记，例如

```markdown
<!-- source: wiki/pages/example.md -->
来自该 source 的摘要、结论或定义补充。
<!-- /source: wiki/pages/example.md -->
更新时根据该边界标记进行替换，而不是简单追加。
```

### 4. 去重规则

写入前必须执行去重检查。

#### 4.1 链接去重
- 以下字段和列表中的链接必须去重：
  - related_pages
  - related_topics
  - related_concepts
  - related_entities
  - sources
  - 页面正文中的来源中的 wikilink 列表
- 去重规则：
 - 同一链接只保留一次
 - 大小写、路径形式不同但指向同一页面的链接，应视为重复
 - 保持原有顺序，新增项追加到末尾

#### 4.2 内容块去重
- 对于 source block：
  - 同一个 <!-- source: ... --> 块只能出现一次
  - 如果重复出现，保留最新分析生成的块
  - 删除旧的重复块

#### 4.3 标题去重
 - 同一级别下不得创建重复标题。
 - 如果目标章节已存在：
 - 更新该章节内容
 - 不新增同名章节

### 5. 禁止行为
- 禁止向同一 topic / concept / entity 页面反复追加相同内容
- 禁止整体覆盖 topics / concepts / entities 页面
- 禁止删除其他 source 贡献的内容
- 禁止在没有 source 引用的情况下写入关键结论

## 执行步骤

### 1. 遍历输入文件

对每个原始文件：
- 读取内容
- 提取文本
- 提取图像并对图像进行解析

### 2. 更新 Pages（单文件维度）

- 根据文件名（不含后缀）定位：`wiki/pages/<name>.md`
- 若存在 → 更新  
- 若不存 → 创建

内容要求：
- 与 raw 文件 1：1 对应（同名映射）
- 对原始文件进行深入分析，遵循下面模板要求写入内容
  - `wiki/pages/template.md`

### 3. 更新 Topics（跨文件聚合研究主题）
- 提取该文件涉及的主题
- 对每个主题：
  - 查找 `wiki/topics/`
  - 存在 → 更新
  - 不存在 → 创建

内容要求：
- 提炼总结原始文件和该主题相关的内容摘要，遵循下面模板要求插入或更新内容
  - `wiki/topics/template.md`
- 必须标注来源（来着哪个 page）

### 4. 更新 Concepts（跨文件聚合概念层）

- 提取概念（术语 / 理论 / 定义）
- 对每个概念：
  - 查找 `wiki/concepts/`
  - 存在 → 更新
  - 不存在 → 创建

内容要求：
- 定义清晰
- 提炼总结原始文件中和该概念相关的内容摘要，遵循下面模板要求插入或更新内容
  `wiki/concepts/template.md`
- 必须标注来源（来自哪个 page）

### 5. 更新 Entities（跨文件聚合实体层）

- 提取实体（人 / 公司 / 工具 / 产品等）
- 对每个实体：
  - 查找 `wiki/entities/`
  - 存在 → 更新
  - 不存在 → 创建

更新内容：
- 定义清晰
- 提炼总结原始文件中和该实体相关的内容摘要，遵循下面模板要求插入或更新内容
  `wiki/entities/template.md`
- 必须标注来源（来自哪个 page）

### 6. 更新 index

- 若新增 topic / concept / entity：
  - 更新 `wiki/index.md`

### 7. Wikilink 校验（强制）

执行：

```bash
python3 tools/link_check.py
```
- 若失败，根据 missing links：创建或补全对应页面（concept / topic / entity）
- 重新执行，直到通过：`All wikilinks resolve.`

### 8. Markdownlint

`markdownlint '**/*.md' --fix`

### 9. 更新日志

更新：`wiki/log.md`

记录：
- 处理的文件
- 更新的 pages / topics / concepts / entities

## 约束
- 所有内容必须来源于输入原始文件
- `pages` 页面可以基于当前 source 整体重写
- `topics / concepts / entities` 页面必须增量更新
- 不允许跨文件污染 pages
- 必须遵循模板结构
