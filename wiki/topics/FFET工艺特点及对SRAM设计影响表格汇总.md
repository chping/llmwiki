---
type: page
source: raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - SRAM
  - 设计备忘
topics:
  - ffet-sram-design
  - advanced-3d-integration
concepts:
  - flip-fet
  - bipolar-sram
  - drain-merge
entities: []
---

# [[FFET工艺特点及对SRAM设计影响表格汇总]]

## 1. 文件信息（Metadata）

- 文章标题：FFET工艺特点及对SRAM设计影响表格汇总
- 原始文件路径：[原始 Markdown](../../../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)
- 文件类型：Markdown
- 来源：研究整理笔记
- 作者 / 机构：未署名
- 时间：2026

## 2. 摘要（Summary）

这份表格把 FFET 的器件堆叠、双面互连、对准误差、Drain Merge、
双面制造、热预算和 3D 集成兼容性等因素，与 SRAM 设计中的
bitcell 面积、SNM、Vmin、Iread、外围拥塞和可测性逐项对应起来。
它不是论文式定量研究，而是一份面向架构与测试芯片规划的设计备忘，
重点强调 FFET 导入 SRAM 时应优先考虑 overlay-aware 版图、读路径寄生、
外围 DTCO 和热 / IR 监测，而不是一开始就追求极限密度。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：FFET 在逻辑单元与 3D 集成上已有明显潜力，但 SRAM 对失配和尾部统计更敏感。
- 目标问题：梳理 FFET 的工艺特征会如何逐项影响 SRAM 的稳定性、速度和良率。
- 应用场景：SRAM bitcell 早期架构选择、测试芯片规划、FFET-friendly 外围设计。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 把 FFET 工艺特征分为器件拓扑、双面互连、overlay、Drain Merge、热预算等十类。
- 针对每类特征，分别给出主要优势、主要风险、对 SRAM 的影响与设计注意点。

### 4.2 核心原理 / 机制

- FFET 的收益不仅来自 bitcell 缩小，还来自外围电路可用双面布线缓解拥塞。
- 与此同时，overlay 和 [[concepts/drain-merge|Drain Merge]] 的波动会放大 SRAM 读路径寄生和统计尾部。
- 表格强调首颗芯片应优先建立“结构变化到失效机理”的可测关系。

### 4.3 数据与实验（如适用）

- 表格引用了若干已有公开数据，例如 2.5T 级标准单元、
  相对 CFET / FinFET 的密度、频率和功耗改善。
- 但其核心价值在于系统性设计建议，而非单独新增实验。

## 5. 关键结论（Key Findings）

- FFET 导入 SRAM 时，外围电路 DTCO 与 overlay-aware 版图和 bitcell 本体同样关键。
- 读路径相关寄生，尤其是 Drain Merge 及其波动，是 SRAM 评估中不能后置的问题。
- 首版芯片应强调可测性、可分解性和对照结构，而非盲目追求最大容量。

## 6. 关键概念（Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/bipolar-sram|Bipolar SRAM]]
- [[concepts/drain-merge|Drain Merge]]

## 7. 相关实体（Entities）

- 无

## 8. 关联主题（Topics）

- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]
- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：把分散的 FFET 工艺问题直接映射到 SRAM 设计决策，适合做项目起点。
- 局限性：它是工程总结而非单独实验论文，很多条目仍依赖后续 silicon 验证。
- 潜在风险：若把表格中的设计建议当成定量结论直接使用，可能会高估当前成熟度。

## 10. 参考与来源（References）

- [原始文件](../../../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)
- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]
