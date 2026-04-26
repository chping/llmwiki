---
name: kb-link-check
description: Use after creating or modifying wiki Markdown pages to validate wikilinks.
---

# 链接检查技能

当 `wiki/` 下的 Markdown 文件发生修改后，使用本技能检查 `[[wikilink]]` 是否有效。

执行：

```bash
python3 -m tools/kb_link_check.py
```

如果明确需要为缺失概念创建占位页面：

```bash
python3 -m tools/kb_link_check.py --create-missing
```

## 规则

- 不要为实体页面自动创建概念占位页。
- 如果目标明显是实体，应创建 `type: entity` 页面。
- 占位页面必须使用中文内容，并标注 `[!needs-verification]`。
