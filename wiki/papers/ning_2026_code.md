---
category: paper
created: 2026-06-10T11:18:16
updated: 2026-06-10T11:18:16
tags:
  - agent-harness
  - coding-agents
  - LLM-agents
  - harness-engineering
  - multi-agent-systems
  - executable-verification
summary: 论文提出 code as agent harness 视角，把代码视为智能体推理、行动、状态管理、反馈验证和多智能体协作的可执行基础设施，并综述接口、机制、扩展与开放问题。
references: 478
citations: 0
zotero:
  item_key: Y3UHWCTB
  citation_key: ning_2026_code
source_uri: '/Users/chengping/workspace/Zotero/zotero.data/storage/2HTI9N9W/ning_2026_code_[preprint]_Code as Agent Harness.pdf'
session: '019eaf88-8c2d-76f3-bf77-7feb7b260156'
---

# Code as Agent Harness

## Domains & Problem

这篇文章属于 agentic AI、LLM agents、coding agents、software engineering automation 与 multi-agent systems 的交叉综述。作者关注的问题是：在新一代智能体系统中，代码不再只是模型生成的最终产物，它正在成为连接模型、工具、环境、状态、验证和协作流程的运行媒介。现有综述通常分别讨论代码生成、工具使用、多智能体协作或具身控制，缺少一个统一框架来解释代码如何在智能体执行循环中承载推理、行动、反馈、状态保存和协同验证。论文因此提出 code as agent harness，把代码视为可执行、可检查、有状态的 agent harness 基础设施，并试图回答代码如何支撑长期任务、如何通过执行反馈提升可靠性、如何扩展到多智能体共享工作空间，以及如何评价和治理这类系统。

## Research Ideas

作者的核心思路是把 agent harness 分成三类耦合要素：模型内部能力、系统预置的 harness infrastructure，以及智能体主动创建和修改的 code artifacts。论文重点放在第三类，即智能体在任务循环中生成、执行、观察、修订、持久化和共享的代码对象，例如测试、临时工具、DSL 程序、可执行 workflow、可复用技能和中间程序状态。围绕这一视角，论文建立三层 taxonomy：第一层是 harness interface，说明代码如何作为 reasoning substrate、action interface 和 environment representation；第二层是 harness mechanisms，讨论 planning、memory、tool use、control 和 optimization 如何维持长期执行；第三层是 scaling the harness，分析多个智能体如何围绕共享代码、仓库、测试、trace 和 workflow 协作。

## Solutions & Methods

论文的具体方案是一篇面向 2026 年前相关工作的系统性综述。第一部分讨论 code for reasoning，包括 program-delegated reasoning、formal verification、symbolic reasoning interfaces 和 iterative code-grounded reasoning，强调代码让中间推理可以执行、记录和验证。第二部分讨论 code for acting，包括 grounded skill selection、programmatic policy generation 和 lifelong code-based agents，覆盖 embodied agents、GUI/OS agents 与软件环境中的动作生成。第三部分讨论 code for environment，把 repository state、execution traces、simulators、tests、DOM/API 状态和可验证环境构造视为智能体理解世界和获得反馈的结构化表示。

在机制层面，论文把长期 code-centric agents 的运行拆成 planning、memory、tool use、feedback-driven control 和 harness optimization。planning 包括线性分解、结构化计划、搜索式规划和 workflow orchestration；memory 包括 working memory、semantic memory、experiential memory、long-term memory、多智能体记忆以及 context compaction/state offloading；tool use 包括函数式工具调用、环境交互工具、验证驱动工具和 workflow 编排工具；control 通过 plan-execute-verify loop，把静态分析、运行错误、测试结果和 human-in-the-loop 反馈转化为可迭代修复信号。论文还提出 harness optimization 的方向，即利用 telemetry、evolution agents 和 governed harness mutation 让 harness 本身可被审计地改进。

在扩展层面，论文围绕 multi-agent orchestration over code 组织已有工作。它把智能体角色分为 manager、planner、coder、reviewer、tester 等，把协作模式分为编程、修复、debate、red-teaming 和 adversarial interaction，把 workflow topology 分为 centralized、distributed、streaming collaboration 等。作者强调，共享仓库、测试、execution feedback、trace、PR workflow 和结构化 artifact 是多智能体形成共同状态、互相审查和收敛到可靠结果的关键基础。

## Main Conclusions

论文的主要结论是，代码在智能体系统中的地位应从“输出物”提升为“运行时 harness”。代码的 executability 让模型意图可以被执行和验证；inspectability 让中间过程、错误和状态可被 harness 读取；statefulness 让长期任务不完全依赖上下文窗口，而可以通过仓库、文件、测试、trace 和工具状态持续演化。基于这个视角，coding assistants、GUI/OS automation、embodied agents、scientific discovery、personalization/recommendation、DevOps 和 enterprise workflows 都可以被统一理解为代码承载智能体推理、行动、反馈和协调的不同应用形态。

论文还指出，可靠智能体的瓶颈不只在 base model 的推理能力，也在 harness 是否能把模型输出接入可控工具、沙箱、权限、记忆、验证器和反馈通道。对于多智能体系统，关键问题进一步变成共享程序状态是否一致、不同角色产生的代码和反馈是否可合并、冲突是否可语义化解决，以及人类监督是否能作为 harness state 被记录和约束。

## Innovations & Contributions

论文的主要贡献有三点。第一，提出 code as agent harness 的概念框架，把代码从 LLM 生成目标重新定位为智能体系统中的可执行、可验证、有状态操作基底。第二，给出三层 taxonomy，将 harness interface、harness mechanisms 和 scaling the harness 串联起来，系统整理了 program-aided reasoning、code-based acting、environment modeling、planning、memory、tool use、feedback control、多智能体协作等研究线索。第三，连接实际应用和未来议题，说明这一框架如何覆盖 coding assistants、GUI/OS agents、embodied agents、scientific discovery、personalization 与 enterprise workflows，并提出评价、验证、安全、人类监督和多模态扩展方面的研究议程。

## Limitations

这篇论文是综述和概念框架，主要贡献在问题重组和文献整合，没有提出新的算法、系统实现或统一 benchmark。由于主题覆盖面很大，从程序推理、软件工程智能体到具身控制、GUI agent、科学发现和推荐系统都有涉及，单个方向的技术细节和实验比较相对有限。OpenAlex 记录中 referenced_works_count 为 0，但 PDF 参考文献编号到 478，说明外部元数据尚不完整。论文也没有给出一个可操作的 harness engineering 标准流程，很多概念如 harness-state convergence、semantic conflict resolution、governed harness mutation 仍偏研究议程。

## Future Work

后续研究可以沿几个方向推进。第一，建立 harness-level evaluation，不只评估最终任务成功率，还评估执行轨迹、验证器充分性、状态一致性、权限边界、失败恢复和长期回归。第二，研究 incomplete feedback 下的 semantic verification，让智能体在测试不完备、环境反馈稀疏或用户目标模糊时仍能校验关键语义。第三，探索 self-evolving harness 的回归控制，包括变更审计、版本化、自动回滚、差分测试和 human approval。第四，面向多智能体系统设计 transactional shared program state，使仓库、测试、trace、计划和记忆能够支持并发修改、冲突检测和语义合并。第五，把 human-in-the-loop safety 做成可持久记录的 harness state，而不只是临时审批。第六，扩展到 multimodal code-harness systems，让视觉、语音、GUI、机器人和仿真环境中的状态也能被代码化、执行化和验证化。
