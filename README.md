# LLM Wiki

一个我个人研究、学习后积累的个人知识仓库，使用 LLM 辅助进行构建。

这个 wiki 既要便于 LLM 需要时进行快速检索，又要尽量方便人类阅读，便于我日常的总结和回顾。

## 信息来源

主要信息来源包括：

- **网络**：平时在微信和知乎等网站上看到的新闻和网络文章，可以通过Web Clipper 保存到 Zotero
- **文献**：科研论文、技术白皮书等文档资料，这些资料通常直接保存到 Zotero 
- **文档**：一些项目中我自己或其他人创建的文档资料，这些资料和上面的文献可能有交集，目前保存在我的obsidian workspace 中
- **对话**：和 AI 的对话，问答等，目前都留存在各个 AI 的 chat app 中
- **图片**：包括照片和截图、网络收集的素材等，保存在我的手机相册（iCloud）和 Eagle 图片管理软件中
- **代码**：我自己以及与其他人合作编写的代码，保存在 github 以及公司的代码仓库（gitea）中

目前来看，大部分有价值的资料文档都可以保存在 Zotero 本地仓库中，我自己创建的文档保存在 obsidian 中，对话还没有有效的保存方法，图片和代码虽然也很有价值，但我还没有想好如何在本知识库中进行处理。

## Wiki 结构

- **wiki** ：主目录，这个目录下的内容全部由 LLM + 脚本代码来创建和维护，尽量不要引入手动处理
  - **papers**：保存阅读的论文和技术文档的笔记和摘要，使用 Zotero 中的对于文献 citation key 作为文件名
  - **topics**：有时我会针对一个主题，阅读多个文献和信息来源进行总结，这里就是保存针对一个主题（或话题）的汇总研究总结，使用主题名称（例如 AgenticEDA_paper_survey.md）作为文件名
  - **chats**：保存我和 AI 的会话，使用会话主题+日期（例如 AgenticEDA_市场研究_2026_0606.md）作为文件名
  - **logs**：wiki 更新的日志记录
    - 记录每次 LLM 更新 wiki 时发生了什么（包括 ingest、query、lint 等各种操作）
    - 为避免单个日志文件过大，将日志按月份进行切片和保存，例如 2026-06.md
  - **index.md**：这是 wiki 的入口页面和内容导航，包含：wiki 统计信息（总页面数、总索引数等）；各个子目录的页面数量，以及其最近 5 个页面内容的摘要；
- **outputs**：基于 wiki 内容产出的其他内容，例如 PPT
- **.idx**：给 AI 大模型 query 用的关键词索引数据目录（暂时没有用，wiki 文件少的时候使用 grep 搜索即可）

### 自动更新首页

运行 `node scripts/update-wiki-index.mjs` 会根据页面 frontmatter 更新 `wiki/index.md` 中的统计信息和最近 5 条内容。仓库的 pre-commit hook 和 GitHub Pages 部署流程都会自动执行该脚本。首次克隆后运行以下命令启用提交钩子：

```bash
git config core.hooksPath .githooks
```

## Scenarios

### 读文献

- 输入`/read-paper <citation_key>` 
  - 首先在 `wiki/papers` 下搜索是否已有 `<citation_key>.md` 文件
  - 如果有说明该论文已经读过，从 `<citation_key>.md` 中读取上一次会话的`session` 并加载原先的会话
  - 如果该文件不存在或原先会话无法加载，则到 Zotero 文献库中搜索该文件
  - 读取该文件全文内容并进行提炼，形成摘要笔记，使用 `<citation_key>.md` 作为文件名，写入 `wiki/papers` 目录下
- 打开 Zotero 开始阅读文献，然后继续和 Agent 对话交流，提问题
- 输入 `/save-paper-chat` 将本次会话的内容以 Q & A 的方式，追加到 `wiki/papers/<citation_key>.md` 末尾

### 研究主题

- 展开新研究：输入`/create-topic <key_word_1, key_word_2>` 
  - 检查是否存在类似研究主题：
    - 首先在 `wiki/topics` 下查找是否有关键字相同/相近的已有 topic
    - 如果有，先列出来询问用户是否要继续已有的 topic

  - 如果用户继续已有某个 topic ，则从该 topic 的 Markdwon 文件的 frontmatter 读取该 topic 会话的 session 并加载原先的会话
  - 否则基于输入的 topic keywords 展开新的研究
    -  首先基于输入的 topic keywords 提出针对性的研究计划
    - 在问答过程中逐渐展开研究和讨论

- 保存研究主题：当用户输入 `/save-topic <topic_name>` 后，将历史会话内容进行总结后，写入 `wiki/topics` 目录下，如果目标文件已存在，则在文件后进行追加
- 打开已有研究主题： 当用户输入 `/open-topic <topic_name>` 
  - 在`wiki/topics` 目录下查找对应的 topic Markdown 文件是否存在
  - 如果存在，读取其 frontmatter 中的会话 session 并加载原有会话
  - 如果不存在，提示用户是否创建新的 topic


### 自由对话

- `/save-chat <chat_name>` 保存用户和 AI 的会话内容
  - 将用户和 AI 当前全部历史会话内容进行总结
    - 以 Q & A 的方式总结，即同时保存用户的问题和 AI 的回答
    - Markdown 文件应当列出全部 Question 的目录索引
  - 使用会话主题加日期作为文件名：`<chat_name>_yyyy_mm_dd.md` ，例如AgenticEDA_市场研究_2026_0606.md
  

> 备注：chat 和 topic 的区别在于：topic 是将整个会话进行总结提炼后的结构化输出结果，而 chat 则是几乎原样保存会话的内容

## Skills & Workflows

### `/read-paper`

- 何时使用：当用户直接调用 Skill，或输入阅读读论文并附加论文的 $citation_key 时

- 输入：Zotero 的 `<citation_key>` 

- 技能说明：

  - 首先在 `wiki/papers` 下搜索是否已有同名的 `<citation_key>.md` 文件
  - 如果则从对应的 `<citation_key>.md` 中读取上一次会话的`session` 并加载原先的会话
  - 如果该文件不存在或原先会话无法加载，则到 Zotero 文献库中搜索该 `<citation_key>`对应的文献
  - 读取文献全文内容并进行提炼，形成摘要笔记，使用 `<citation_key>.md` 作为文件名，写入 `wiki/papers` 目录下

- 输出：文献全文内容的摘要笔记，保存到`wiki/papers/<citation_key>.md` ，内容模版和相关内容要求如下

```markdown
---
category: paper
created: YYYY-MM-DD HH:MM:SS
updated: YYYY-MM-DD HH:MM:SS
tags: [keyword1,keyword2,...]
summary: 200字以内的全文精炼摘要
references: 参考文献数量
citations：文章被引用的次数
zotero: 
  item_key:
  citation_key:
source_uri: 文章全文文件的路径
session: 会话 ID，可以根据该 ID 恢复会话
---

# 文章 Title

## Domains & Problem
这篇文章术语什么研究/技术领域
作者提出或者解决了哪些问题？

## Research Ideas

简要总结作者的研究方法和解决问题的思路

## Solutions & Methods

介绍作者的具体解决方案

## Main Conclusions

总结文章的主要结论

## Innovations & Contributions

总结文章的创新点和主要工作贡献

## Limitations

总结文章的不足

## Future Work

针对该论文的研究领域，未来还有哪些值得进一步研究的方向和内容
``

```

- 约束：
  - 缺省使用中文，英文和术语使用遵循 AGENTS.md 的要求
  - 写入时必须检查目标文件是否存在，如果目标文件已经存在，未经用户明确输入“同意”不允许覆盖
  - 写入时必须严格遵守模板文件的内容结构要求，不可擅自新增章节，也不能遗漏章节
  - 使用简洁、清晰、准确、易懂的表达语言
  - 不要使用表情符号
  - 避免使用“不是..., 而是...” 这种 AI 风格的语言
  - 保持紧凑的格式，避免过多的短行，只有必要时才分段换行
  - 写入时必须更新 markdown 文件的frontmatter
    - category：paper
    - created：本文档创建时间，格式为 YYYY-MM-DD HH:MM:SS
    - updated:  本文档更新时间，格式为 YYYY-MM-DD HH:MM:SS
    - tags: 总结并提炼文献的关键词，可以是多个： [keyword1, keyword2, ...]
    - summary: 200字以内的全文精炼摘要
    - references: 参考文献数量
    - citations：文章被引用的次数
    - zotero: 
      - item_key:
      - citation_key:
    - source_uri: 文章全文文件的路径
    - session: Chat 会话 ID，可以根据该 ID 恢复会话 Chat
- 失败情况：
  - 目标文件不存在，且在 Zotero 中找不到用户输入的 `<citation_key>` 对应的文献。此时提示用户错误信息，不必创建文件。
  - 目标文件已存在，但其中的 frontmatter 不存在，或 frontmatter 中没有 session 字段，因此不能恢复历史会话。此时提示用户无法恢复历史会话，直接在新会话中继续。

### `/save-paper-chat`

- 何时使用：当用户直接调用 Skill，或在会话中输入保存会话并附加论文的 $citation_key 时
- 输入：Zotero 的 `<citation_key>` ，如果用户没有输入 `<citation_key>` ，则需要从历史会话中检索 `<citation_key>` 并让用户确认后再执行保存操作
- 技能说明：
  - 将本次会话的内容以 Q & A 的方式，追加到 `wiki/papers/<citation_key>.md` 末尾
- 输出：基于下面 Markdown 段落模版，追加到 `wiki/papers/<citation_key>.md` 末尾 `## Chat Q&A`章节中


```markdown

## Chat Q&A

### Question：<用户在会话中提出的问题摘要，不超过 50 中文字符>

Q：用户在会话中提出的问题原文
A：你输出的答复。

### Question：<用户在会话中提出的问题摘要，不超过 50 中文字符>

Q：用户在会话中提出的问题原文
A：你输出的答复。

```

- 约束：
  - 缺省使用中文，英文和术语使用遵循 AGENTS.md 的要求
  - 只能修改目标文件尾部 `## Chat Q&A` 这个子章节的内容
  - 绝对不允许覆盖或修改目标文件除  `## Chat Q&A` 之外其他章节的内容
  - 绝对不允许直接覆盖或删除已有目标文件
  - 用户在会话中提出的问题（Question）如果长度超过50中文字符，需要进行摘要缩短到50字符以内作为Question 子章节标题
  - 你的答复需要进行总结提炼，用更加紧凑的格式（避免过多的短行，只有必要时才分段换行）
  - 只追加会话中新增的 Q&A，不要重复添加已有的 Q&A 
  - 写入时需更新 markdown 文件的frontmatter 中下面的字段
    - updated:  本文档更新时间，格式为 YYYY-MM-DD HH:MM:SS
    - session: 如果 Chat 会话 ID有更新，允许使用新的 session ID替换
- 失败情况：
  - 目标文件不存在，提示用先使用 `/read-paper` 这个 skill 创建目标文件后再继续

### `logging`

- 何时使用：当用户在本项目中调用任何 SKILL ，完成目标 SKILL 任务后自动触发本日志记录功能
- 输入：无需输入
- 技能说明：
  - 记录用户刚刚调用的 SKILL 名称，以及用户执行的操作摘要
  - 每一条日志记录至少应当包含下面的内容：
    - 日期和时间：格式为 YYYY-MM-DD HH:MM:SS
    - 调用的SKILL 名称
    - 用户执行的任务简短摘要说明（不超过 50个中文字符）
  - 日志采用“Monthly log rotation”的方式，追加到 `wiki/logs` 目录下
- 输出：输出格式为 Markdwon

```markdown

# YYYY-MM <例如 2026-06>

## YYYY-MM-DD

滚动记录操作时间、SKILL 名称和具体任务摘要，示例如下

- [2026-04-02 19:21:00] read-paper | read paper @chen_2024_large, save note to wiki/papers/chen_2024_large.md 

```

- 约束：
  - 采用“Monthly log rotation”的方式进行追加，不允许覆盖或删除已有日志文件
  - 只能追加，不可以修改已有日志记录

