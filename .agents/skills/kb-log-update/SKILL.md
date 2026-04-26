---
name: kb-log-update
description: Use when recording significant repository operations in wiki/log.md.
---

# 操作日志技能

当完成导入、页面创建、页面更新、索引同步或结构调整后，必须更新 `wiki/log.md`。

执行：

```bash
python3 -m tools/kb_log_update.py "操作说明"
```

## 规则

- 日志必须简洁、客观。
- 日志按日期分组。
- 不要故意重复记录相同操作。
