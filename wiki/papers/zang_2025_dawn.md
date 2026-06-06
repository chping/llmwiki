---
category: paper
created: 2026-06-06T20:03:12
updated: 2026-06-06T20:12:15
tags:
  - agentic-EDA
  - autonomous-chip-design
  - RTL-to-GDSII
  - LLM-agents
  - formal-verification
  - EDA-benchmarks
  - constrained-neuro-symbolic-optimization
  - EDA-tool-orchestration
  - multi-agent-systems
  - Sim-to-Silicon-gap
  - trustworthy-AI
summary: 本文综述 Agentic EDA 从局部 AI 辅助走向 RTL-to-GDSII 自治编排的范式，提出 Cognitive Stack 与方法分类，强调工具验证、形式化约束、工业级 benchmark 和 Sim-to-Silicon 可信性仍是落地关键。
references: 56
citations: 0
zotero:
  item_key: GTL4C5BA
  citation_key: zang_2025_dawn
source_uri: '/Users/chengping/workspace/Zotero/zotero.data/storage/44YPAJFH/zang_2025_dawn_[preprint]_The dawn of agentic EDA a survey of autonomous digital chip.pdf'
session: '019e9cd2-81f1-7820-8357-4423dc09e318'
---

# The dawn of agentic EDA: a survey of autonomous digital chip design

## Domains & Problem

这篇文章属于 EDA、数字芯片设计自动化、LLM agents 与 autonomous chip design 交叉领域，重点讨论从 RTL implementation 到 physical design、verification、signoff 的长流程自动化。作者关注的核心问题是半导体设计复杂度增长快于人力设计能力，传统 AI for EDA 多数只优化 placement、congestion prediction、parameter tuning 等局部点问题，缺少跨阶段推理、工具执行和闭环修复能力，难以应对 RTL-to-GDSII 流程中的全局约束、物理规则和零容错工程要求。

## Research Ideas

作者将 Agentic EDA 定义为从 L2 AI-assisted copilots 走向 L3/L4 autonomous orchestration 的范式，并把它概括为 Constrained Neuro-Symbolic Optimization problem。论文的基本思路是用 LLM agent 负责搜索、规划、分解任务、生成 Tcl/Python/RTL 等候选动作，再用 compiler、simulator、timer、DRC、formal verification 等确定性 EDA 工具执行和验证，从而把概率式生成约束在工程可检查的闭环中。文章以 Cognitive Stack 作为统一框架，分析 agent 如何感知设计数据、进行受约束推理，并把计划落到实际工具链执行。

## Solutions & Methods

论文提出三层 Cognitive Stack：Perception 层将 HDL、netlist、layout、log、waveform、PPA report 等异构输入转成可对齐的多模态表示；Cognition 层负责 planning、reasoning、long-horizon memory、Domain-Specific RAG、多智能体协作和约束管理；Action 层把计划转换为 EDA 工具可执行的脚本或代码，并通过工具反馈持续修复。方法分类上，作者把现有工作分为 Prompt-Based Reasoning、Fine-Tuned Specialization 与 Multi-Agent Collaboration 三类，并按 frontend、backend、foundation/security 等阶段梳理代表性系统。Frontend 部分强调从 one-shot RTL generation 转向 dual-loop repair，内层用 compiler log 快速修语法，外层用 simulation waveform、AST trace 或 formal verification 修语义。Backend 部分区分 algorithm-centric solver 与 agent-centric orchestrator，前者偏向特定优化器，后者偏向把 EDA toolchain 作为可执行环境进行流程编排。

## Main Conclusions

论文认为 Agentic EDA 的价值在于端到端工具编排、跨阶段推理和长流程自动化，而关键机制是 Neuro-Symbolic Handshake：LLM 提供非凸搜索空间中的候选探索，确定性 EDA 工具负责物理约束、时序、DRC 和形式化验证。作者指出 frontend agent 已在 RTL 生成、debug 和 verification planning 中较成熟，backend agent 正在向 Tcl/Python orchestration、placement optimization、PPA tuning 和 multi-agent negotiation 发展，但目前系统多仍停留在研究原型或 block-level 实验。论文特别强调工业采用的主要障碍是 Trustworthiness gap 和 Sim-to-Silicon gap，现有 benchmark 往往不能证明复杂工业约束下的可复现 tape-out 能力。

## Innovations & Contributions

论文的主要贡献是为 Agentic EDA 提供一个系统化综述框架，把自主等级、Cognitive Stack、方法分类和 EDA 流程阶段结合起来，明确区分 AI for EDA 的局部预测能力与 Agentic EDA 的自治执行层。文章提出将 agentic chip design 理解为受物理和形式化约束的 neuro-symbolic optimization，并用 Perception-Cognition-Action 解释 agent 的闭环行为。它还归纳了 frontend 的 syntactic-semantic dual-loop repair、backend 的 solver/orchestrator 分化、多智能体协作、formal verification as explainability mechanism、Proof-Carrying Code、Semantic EDA Interfaces 和 Open Agentic EDA Standard 等方向，为后续研究提供了结构化地图。

## Limitations

这篇文章是综述论文，贡献主要在分类、框架和路线图，而非提出新的可复现实验系统。文中也承认当前 LLM-driven autonomous agent 尚未展示完整、无人参与的工业芯片 tape-out，多数工作依赖 proxy metric、开源 PDK 或局部任务 benchmark，难以覆盖先进工艺中的 timing closure、electromigration、multi-patterning、IP 保密和签核级验证。Agent 与 EDA 工具的接口仍偏脆弱，常依赖文本 log 解析，容易出现 deadlooping、context loss、tool hallucination 和 design intent drift。数据方面，工业级设计数据和 tape-out logs 难以公开，限制了训练、评测和跨节点泛化。

## Future Work

后续值得研究的方向包括构建工业级 Sim-to-Silicon benchmark，把评价从 pass@k、wirelength 等局部指标扩展到 end-to-end PPA、wall-clock efficiency、token cost、reproducibility 和 signoff outcome；发展 formal verification、SVA、SMT/SAT 与 LLM agent 的更强耦合，使生成动作带有可机械验证的 proof 或 constraint certificate；设计类似 LSP 的 Semantic EDA Interfaces，让 agent 以结构化 API 查询 timing graph、congestion map、DRC violation 和 tool state；研究面向私有工业数据的 domain adaptation、federated learning 和 synthetic advanced-node constraint generation；完善 failure mode taxonomy、checkpoint rollback、sandbox execution 和 long-horizon memory，提升 block-level 到 full-chip flow 的稳定性与可审计性。

## Chat Q&A

### Question：MAS evolve into Cooperative Games 的含义

Q：文章中提到的 MAS evolve into Cooperative Games 具体是什么意思？
A：这里的 MAS 指 Multi-Agent Systems。论文中的 “MAS evolve into Cooperative Games” 是说 Agentic EDA 中的多个 agent 不能只是并行执行局部任务，而要形成有共同目标、角色分工、冲突协调和约束裁决的协作博弈系统。例如 timing、power、layout、verification 等专家 agent 可能提出互相冲突的方案，Manager agent 负责仲裁和折中，Critic agent 借助 formal verification、仿真、DRC、STA 等确定性工具剪掉无效分支。它强调从“多个专家 agent 各自工作”升级为“多个专家 agent 在全局 PPA、timing、DRC、correctness 约束下协商、让步、验证并共同优化设计”。

### Question：Figure 2 三层 Cognitive Stack 的含义

Q：详细解读这张图的含义

A：Figure 2 说明 Agentic EDA 的三层认知架构：Perception、Cognition、Action。输入包括 netlist graph、RTL/HDL text 与 layout geometry 等异构 EDA 数据，先由 Multimodal Perception/CFMs 转成统一的 multimodal embeddings；中间的 Agent Core 负责理解设计状态、任务分解、规划、推理、工具选择和错误修复；下方 Memory Module 提供长期 RAG 知识与短期执行上下文，长期记忆包括 PDK docs 和 design specs，短期记忆包括 interaction history 和 execution trace；右侧 Action Space 表示 agent 必须把计划落到 logic synthesis、simulation、formal verification、physical design 等真实工具执行中；顶部 logs、waveforms、PPA 构成反馈闭环，使 agent 能根据工具结果迭代修正。图的核心观点是：LLM agent 负责感知、推理和规划，EDA 工具负责执行、验证和反馈，二者通过记忆与闭环反馈共同减少 hallucination，并支撑长流程芯片设计自动化。

### Question：Figure 4 双循环 RTL 修复框架

Q：继续解读 Figure 4 的含义

A：Figure 4 说明 Agentic RTL Repair 的双循环机制，用来平衡验证成本和反馈保真度。左侧 Inner Loop 是 Syntactic Repair：Agent 生成 RTL 后先调用 compiler，例如 iverilog，利用 syntax error、port mismatch、width mismatch、undeclared signal 等编译日志快速修复语法和静态结构错误，这一环节便宜、快速、确定性强。右侧 Outer Loop 是 Semantic Repair：当 RTL 能编译后，再通过 testbench、simulator、waveform、AST/trace analyzer 或 formal verification 检查功能行为，例如某个信号在指定 cycle 未达到期望值，并把这些结果转成自然语言或语义诊断反馈给 Agent 修复状态机、协议时序、握手逻辑等深层错误。该图强调 coarse-to-fine 策略：先用低成本编译器过滤明显无效代码，再用高保真仿真和验证修功能逻辑，从而减少 agentic iteration 的计算开销并提升 RTL 正确性。
