---
name: kb-link-check
description: Use after creating or modifying wiki Markdown pages to validate wikilinks.
---

# 链接检查技能

当 `wiki/` 下的 Markdown 文件发生修改后，使用本技能检查 `[[wikilink]]` 是否有效，步骤如下：

1. 执行：

```bash
python3 -m tools/kb_link_check.py
```

2. 如果命令返回非 0 状态码，说明存在未解析的 [[wikilink]],调用者必须读取命令输出中的 missing link 列表，格式如下：
- [[概念名称]] referenced by wiki/topics/example.md

4. 根据每个 missing link 的名称和引用来源，重新分析原始资料与相关 wiki 页面，并手动创建或更新对应的 markdown 文件：
- 如果 missing link 指向概念，创建或更新 wiki/concepts/<slug>.md
- 如果 missing link 指向主题，创建或更新 wiki/topics/<slug>.md
- 如果 missing link 指向实体，创建或更新 wiki/entities/<slug>.md

5. 创建或更新页面后，重新运行：

```bash
python3 -m tools/check_wikilinks.py
```
直到输出：`All wikilinks resolve.`

