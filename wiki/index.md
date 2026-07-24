---
category: topic
created: 2026-07-24
updated: 2026-07-24
tags:
  - index
summary: 芯片设计、先进器件、SRAM 与 Agentic EDA 研究知识库导航。
zotero:
  item_key:
  citation_key:
source_uri:
---

# 芯片设计与 Agentic EDA 知识库

这里记录 SRAM、先进晶体管、三维集成、数字芯片设计与 Agentic EDA 相关的研究笔记。

## 核心研究方向

### SRAM 与 Memory Compiler

- [[topics/sram|SRAM]]
- [[topics/sram-memory-compiler|SRAM Memory Compiler 功能与配置]]
- [[topics/sram-source-bias|SRAM Source Bias]]
- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]
- [[topics/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler|3D SRAM 设计与开源 Memory Compiler]]

### 先进器件与三维集成

- [[topics/advanced-3d-integration|先进三维集成]]
- [[topics/complementary-fet-cfet|Complementary FET（CFET）]]
- [[topics/flip-fet|Flip FET]]
- [[topics/vertical-field-effect-transistor-vfet|Vertical Field-Effect Transistor（VFET）]]
- [[topics/dual-sided-interconnects|双面互连]]

### 数字芯片设计

- [[topics/Verilog|Verilog]]
- [[topics/RTL|RTL]]
- [[topics/ASIC Flow|ASIC Flow]]
- [[topics/RISC-V|RISC-V]]

### Agentic EDA 与自主研究

- [[papers/zang_2025_dawn|The dawn of agentic EDA]]
- [[papers/ning_2026_code|Code as Agent Harness]]
- [[papers/chendeli_202606_auto_research_survey|From Copilots to Colleagues]]
- [[topics/agent_common_frameworks|Agent 常用框架]]

## 推荐阅读路径

- SRAM：[[topics/sram|SRAM]] → [[topics/sram-memory-compiler|Memory Compiler]] → [[topics/ffet-sram-design|FFET SRAM]] → [[topics/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler|3D SRAM]]
- FFET：[[topics/advanced-3d-integration|先进三维集成]] → [[topics/complementary-fet-cfet|CFET]] → [[topics/flip-fet|Flip FET]] → [[topics/dual-sided-interconnects|双面互连]] → [[topics/flip-3d-integration-f3d|Flip 3D Integration]]
- 数字设计：[[topics/Verilog|Verilog]] → [[topics/RTL|RTL]] → [[topics/ASIC Flow|ASIC Flow]] → [[topics/RISC-V|RISC-V]]
- Agentic EDA：[[papers/zang_2025_dawn|Agentic EDA 综述]] → [[papers/ning_2026_code|Agent Harness]] → [[papers/chendeli_202606_auto_research_survey|Autonomous Research Agents]]

## 重点专题

- [[topics/sram|SRAM]]：位单元、阵列、外围电路、关键指标与先进工艺研究方向。
- [[topics/flip-fet|Flip FET]]：双面互连、堆叠晶体管及其 PPA 和工艺影响。
- [[papers/zang_2025_dawn|Agentic EDA]]：自主芯片设计的认知架构、工具闭环与可信性挑战。

## Wiki 概览

<!-- AUTO-GENERATED:START -->

- 总计 38 页 · 主题 34 · 论文 4 · 对话 0

### 最近更新

- 2026-07-24 · [[topics/sram|SRAM]] — SRAM 的基本原理、位单元结构、关键指标、阵列组织、设计流程与先进工艺研究方向。
- 2026-07-24 · [[topics/sram-memory-compiler|SRAM Memory Compiler 功能与配置]] — SRAM Memory Compiler 的容量配置、阵列组织、输入 Slew、输出负载、低功耗、测试冗余、交付视图及选型签核说明。
- 2026-07-24 · [[topics/sram-source-bias|SRAM Source Bias]] — SRAM Source Bias 通过待机时调整 Cell 源极电位降低亚阈值漏电，并在功耗、数据保持裕量和唤醒开销之间进行权衡。
- 2026-06-10 · [[papers/ning_2026_code|Code as Agent Harness]] — 论文提出 code as agent harness 视角，把代码视为智能体推理、行动、状态管理、反馈验证和多智能体协作的可执行基础设施，并综述接口、机制、扩展与开放问题。
- 2026-06-10 · [[papers/chendeli_202606_auto_research_survey|From Copilots to Colleagues: A Survey of Autonomous Research Agents in the Age of Foundation Models]] — 本文综述基础模型时代的自主研究代理，提出 L1-L5 自主性分类、四类架构模式和六项开放问题，指出当前前沿多停留在有边界的 L4，自主选题与可靠自评仍是关键瓶颈。

<!-- AUTO-GENERATED:END -->

## 浏览知识库

- `wiki/topics/`：围绕概念和技术方向持续整理的主题页面。
- `wiki/papers/`：论文阅读笔记、方法总结与问答记录。
- [[logs/2026-07|更新日志]]：按月记录知识库的重要变更。
