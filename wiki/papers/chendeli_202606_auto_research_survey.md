---
category: paper
created: 2026-06-10T10:35:15
updated: 2026-06-10T10:35:15
tags:
  - autonomous-research-agents
  - foundation-models
  - LLM-agents
  - scientific-discovery
  - multi-agent-systems
  - research-automation
summary: 本文综述基础模型时代的自主研究代理，提出 L1-L5 自主性分类、四类架构模式和六项开放问题，指出当前前沿多停留在有边界的 L4，自主选题与可靠自评仍是关键瓶颈。
references: 103
citations: null
zotero:
  item_key: JGPQHEAG
  citation_key: chendeli_202606_auto_research_survey
source_uri: 'https://victorchen96.github.io/auto_research/auto_research_survey.pdf'
session: '019eaf60-c777-7952-8546-0de6a8b7e100'
---

# From Copilots to Colleagues: A Survey of Autonomous Research Agents in the Age of Foundation Models

## Domains & Problem

这篇文章属于 LLM agents、autonomous research agents、scientific discovery automation 和 AI for software engineering 交叉领域。作者关注的问题是：代码代理、科学发现系统和多代理研究平台虽然快速发展，但术语、评估框架和能力边界并不统一，导致不同系统之间难以比较。论文试图把这些系统统一到“能够在高层研究目标下独立执行假设生成、实验设计、执行、分析与迭代”的自主研究代理框架中，并回答当前系统距离真正自导研究还有多远。

## Research Ideas

作者的核心思路是用综述方式建立一个统一分析框架，而不是只罗列系统。论文先定义 autonomous research agent，再提出 L1-L5 自主性等级，用决策范围和无人监督运行时长刻画能力边界；随后从架构角度比较 single-agent loops、multi-agent collaboration、hierarchical orchestration 和 tool-augmented execution；再用六维矩阵分析 17 个代表系统，最后总结认知循环、上下文限制、新颖性评估、可复现性、安全和成本六类开放问题。

## Solutions & Methods

论文的主要方法包括四部分。第一，提出类似自动驾驶分级的 L1-L5 分类：L1 是补全，L2 是带人工批准的任务执行，L3 是带检查点的多步执行，L4 是有边界的全流程自主执行，L5 是能够自选问题和长期推进的自导研究。第二，比较四类架构模式：单代理循环强调简单执行和反馈，多代理系统通过角色分工提升覆盖面，层级编排用 supervisor-worker 或树搜索组织复杂任务，工具增强执行通过 shell、浏览器、数据库、实验环境和自动评测形成闭环。第三，选取 AutoGPT、AI Scientist、GPT-Researcher、STORM、SWE-Agent、Devin、Claude Code、OpenHands、Coscientist、FunSearch 等 17 个系统，按自主等级、领域、架构、工具、评估和开放性比较。第四，把 benchmark coverage、系统能力和失败模式联系起来，讨论为什么代码任务更容易推进到 L4，而开放式科学研究仍受制于新颖性、验证和长期记忆。

## Main Conclusions

论文的主要结论是，当前前沿系统已经从辅助工具发展为在有边界场景内可完成多步研究或工程流程的 L4 系统，但 L5 仍是目标而非现实。作者认为限制 L5 的关键并非单纯的基础模型能力，而是持续知识积累、可靠自我评估、开放问题选择、可复现验证和可控成本。代码代理因为有测试、仓库环境和 SWE-bench 等标准评估，进展最快；科学发现代理在化学、数学和机器学习实验中已有强样例，但跨领域通用研究代理仍缺少统一的工具环境和验证机制。

## Innovations & Contributions

论文的贡献包括：提出面向研究代理的 L1-L5 自主性分类，为不同系统比较提供统一词汇；归纳四类主导架构模式，并比较其在可扩展性、成本、可靠性和人工监督方面的取舍；构建 17 个主要系统的六维比较矩阵，展示从脆弱通用代理到领域受限高可靠代理的演化路径；系统提出六类开放问题和对应研究方向。一个特殊贡献是论文自身由 Deli AutoResearch framework 生成，因此也提供了一个 L4 自主研究系统生产综述论文的案例数据。

## Limitations

论文也存在明显限制。首先，L1-L5 分类主要是描述性框架，不能解释系统如何机制性地从低等级跃迁到高等级。其次，综述覆盖到 2026 年初，许多系统和指标变化很快，部分性能数字会迅速过期。第三，论文由自主研究框架生成，虽然作者报告了引用验证和迭代过程，但仍需要人工进一步审校其引用完整性、系统选择偏差和判断标准。第四，对安全、治理、学术制度和知识产权的讨论更偏议题梳理，缺少可操作的评估协议或实证结果。

## Future Work

后续值得研究的方向包括：构建面向研究代理的持久记忆和知识图谱，使系统能跨项目积累经验；发展可靠的新颖性评估和自我批判机制，减少表面创新和错误自信；建立可复现实验沙箱、数据版本管理和自动审计流程，让代理输出可被独立验证；设计跨领域 benchmark，覆盖文献理解、假设生成、实验执行、成本控制和安全约束；研究多代理组织结构、动态拓扑和长期协作机制；探索自主研究代理在学术评价、作者身份、双重用途和资源集中方面的治理框架。
