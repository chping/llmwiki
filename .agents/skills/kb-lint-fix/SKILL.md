---
name: kb-lint-fix
description: Use after modifying Markdown files under wiki to run markdownlint auto-fix and final validation.
---

# Markdown 格式检查技能

当 `wiki/` 下任意 Markdown 文件被创建或修改后，必须使用本技能。

执行：

```bash
python3 -m tools/kb_lint_fix.py
```

该命令等价于：

```bash
npx markdownlint wiki/ --fix
npx markdownlint wiki/
```

## 规则

- markdownlint 错误是阻塞问题。
- 不允许在 lint 失败时结束任务。
- 自动修复后仍然存在的问题必须人工修复。
