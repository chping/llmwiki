---
name: kb-ingest
description: Use when the user asks to ingest, archive, import, or process materials from inbox and complete the whole knowledge-base workflow automatically.
---

# 知识库导入技能

当用户要求导入、分析、处理或归档 `inbox/` 中的资料时，按顺序执行以下步骤

1. 执行下面的命令，将 `inbox/` 目录下所有未处理文件移动到 `raw/` 目录，同时从该命令返回值获取要处理的全部原始文件清单

```bash
python3 tools/archive.py inbox
```
2. 分析上面命令返回文件清单中的全部待处理原始文件，完成后面的步骤
3. 提炼文件涉及的主题，总结每个主题的摘要和核心内容，更新 `wiki/topics` 目录下相关主题页面内容。
4. 提炼原始文件涉及的概念（例如理论、术语、定义），更新 `wiki/concepts/` 目录下相关概念页面内容
5. 提炼原始文件涉及的实体（例如人名、工具、产品、公司、组织），更新 `wiki/entities` 目录下相关实体页面内容
6. 更新 `wiki/index.md`，添加新创建的主题页面。
8. 运行 markdownlint 自动修复和最终检查。
9. 更新 `wiki/log.md`。

## 主题页面维护规则

- 根据主题，搜索 `wiki/topics` 目录下所有的页面，如果存在相关页面，则优先更新相关页面而不是新建重复主题的页面
- 如果在 `wiki/topics` 下没有找到相关主题页面，则在该目录下创建新的主题页面
- 在主题页面中写入你分析和提炼的摘要及核心内容
- 创建或更新主题页面时，遵循模板要求： `wiki/topics/template.md` 模板中的内容分层和要求
- 如果原始文件的内容涉及多个主题，则需要更新相应的所有主题页面，插入和该主题相关的内容

## 概念页面维护规则
- 根据概念名称，搜索 `wiki/concepts` 目录下所有的页面，如果存在相关页面，则优先更新相关页面而不是新建重复概念页面
- 如果没有找到相关概念页面，则在`wiki/concepts/`下使用概念名称创建新的概念页面
- 创建或更新概念页面时，遵循 `wiki/concepts/template.md` 模板的要求
- 如果原始文件涉及多个概念，则需要更新相应的所有概念页面，插入和该概念相关的内容

## 实体页面维护规则
- 根据实体名称，搜索 `wiki/entities` 目录下所有的页面，如果存在相关页面，则优先更新相关页面而不是新建重复实体页面
- 如果没有找到相关实体页面，则在`wiki/entities/`下，使用实体名称创建新的实体页面
- 创建或更新实体页面时，遵循 `wiki/entities/template.md` 模板的要求
- 如果原始文件涉及多个实体，则需要更新相应的所有实体页面，插入和该实体相关的内容

## 语言和内容要求
- 语言要求：除了专业名词和术语外，必须使用中文
- 交叉引用： 所有的数据和关键结论必须标注引用来源
- 不确定性处理：对于你不确定的内容，在内容结尾添加 tag 标注：#needs-verification
