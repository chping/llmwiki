---
name: kb-ingest
description: Use when the user asks to ingest, archive, import, or process materials from inbox and complete the whole knowledge-base workflow automatically.
---

# 知识库导入技能

当用户要求导入、分析、处理或归档 `inbox/` 中的资料时，按顺序执行以下步骤

## 步骤

1. 执行归档命令：

```bash
python3 tools/archive.py inbox
```

2. 解析命令返回的 JSON 输出，获取：
- 所有归档后的原始文件路径（raw/...）
- 对应生成的 pages 路径（wiki/pages/...）

3. 将返回的原始文件清单作为输入，调用分析 SKILL： kb-analyze

# 约束规则
- ingest 不负责内容分析
- ingest 仅负责：
  - 文件归档
  - 触发分析流程