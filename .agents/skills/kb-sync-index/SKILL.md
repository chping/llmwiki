---
name: kb-sync-index
description: Use after creating, renaming, or moving wiki pages to update wiki/index.md.
---

# 索引同步技能

当新增、重命名或移动 `wiki/` 页面后，必须更新 `wiki/index.md`。

执行：

```bash
python3 -m tools/kb_sync_index.py
```

完成后继续运行：

```bash
python3 -m tools/kb_link_check.py
python3 -m tools/kb_lint_fix.py
```

## 规则

- 新页面应当能从 `wiki/index.md` 被发现。
- 不要重复添加相同页面。
