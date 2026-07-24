---
type: page
source: raw/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - PPA
  - SRAM
topics:
  - advanced-3d-integration
  - ffet-sram-design
concepts:
  - flip-fet
  - fully-aligned-ffet-f3et
  - forksheet-based-f3et-f4et
  - cfet-based-ffet-cffet
  - complementary-fet-cfet
  - bipolar-sram
entities:
  - peking-university
  - risc-v
---

<!-- markdownlint-disable-next-line MD013 -->
# PPA Scaling of Flip FET Technology Down to A2 Node Enabled by Architecture Innovations: Self-aligned Gate, 2T Design with Embedded Power Rail and Ultra-stacked 4-Tier Transistors

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：PPA Scaling of Flip FET Technology Down to A2 Node Enabled by Architecture Innovations: Self-aligned Gate, 2T Design with Embedded Power Rail and Ultra-stacked 4-Tier Transistors
- 原始文件路径：原始 PDF（仓库中未提供）
- 文件类型：PDF
- 来源：2025 Symposium on VLSI Technology and Circuits
- 作者 / 机构：Wanyue Peng 等，北京大学
- 时间：2025

## 2. 摘要（Summary）

本文把 [[topics/flip-fet|FFET]] 的路线图系统推进到 A2 节点，依次引入
[[topics/fully-aligned-ffet-f3et|F3ET]]、
[[topics/forksheet-based-f3et-f4et|F4ET]] 和
[[topics/cfet-based-ffet-cffet|CFFET]] 等架构创新，覆盖器件、
标准单元、32-bit [[topics/RISC-V|RISC-V]] 核和 SRAM 阵列四个层级。
作者报告从 A14 到 A5，RISC-V 核面积可缩小约 44.9% / 49.8%
（HP / HD），频率提升约 20.0% / 27.9%；A3 HP F4ET 在
`Vdd = 0.7 V` 时较 A14 HP FFETFin 可实现约 38.9% 的等功耗频率提升。
在 SRAM 侧，Bipolar SRAM 与 A2 CFFET SRAM 被用来探索 A2 之后的继续缩放。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：单纯依赖器件缩放已不足以支撑 A14 到 A2 的连续逻辑与 SRAM 缩放。
- 目标问题：FFET 能否通过一系列架构与 DTCO 创新在电路和 block 级保持可持续 PPA 收益。
- 应用场景：先进逻辑标准单元库、RISC-V 核实现、SRAM 阵列与后续 A2 级路线规划。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 建立从 A14 FFETFin、A10 FFETNS、A7
  [[topics/fully-aligned-ffet-f3et|F3ET]]、A5 / A3
  [[topics/forksheet-based-f3et-f4et|F4ET]] 到 A2
  [[topics/cfet-based-ffet-cffet|CFFET]] 的路线图。
- 用 compact model、RO、标准单元库、32-bit
  [[topics/RISC-V|RISC-V]] 核 P&R 和 256×256 SRAM 阵列进行多层评估。
- 比较 FFET 与 [[topics/complementary-fet-cfet|CFET]]
  在面积、性能和 SRAM 缩放上的差异。

### 4.2 核心原理 / 机制

- F3ET 用 self-aligned gate 缓解前后门失配问题，并降低门电阻。
- F4ET 结合 Forksheet 与 embedded power rail，把 cell height 压到 2T。
- CFFET 通过四层超堆叠继续挤出面积，但逻辑侧性能收益不如 SRAM 明显。

### 4.3 数据与实验（如适用）

- A3 HP F4ET 相比 A14 HP FFETFin，等功耗频率提升约 38.9%。
- 32-bit RISC-V 核从 A14 到 A5 的面积缩减约 44.9%（HP）和 49.8%（HD）。
- A2 CFFET SRAM 通过 folded 组织可在相同容量下获得约 50% 面积收益。

## 5. 关键结论（Key Findings）

- FFET 的可扩展性不是来自单一器件改进，而是持续引入 F3ET / F4ET / CFFET 等架构旋钮。
- F4ET 是当前逻辑侧最关键的节点，兼顾了 2T cell height 与相对可控的 PP。
- A2 CFFET 对 SRAM 的吸引力强于逻辑，因为其四层超堆叠更容易转化为存储密度收益。

## 6. 关键概念（Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/fully-aligned-ffet-f3et|Fully-aligned FFET (F3ET)]]
- [[topics/forksheet-based-f3et-f4et|Forksheet-based F3ET (F4ET)]]
- [[topics/cfet-based-ffet-cffet|CFET-based FFET (CFFET)]]
- [[topics/complementary-fet-cfet|Complementary FET (CFET)]]
- [[topics/bipolar-sram|Bipolar SRAM]]

## 7. 相关实体（Entities）

- 北京大学
- [[topics/RISC-V|RISC-V]]

## 8. 关联主题（Topics）

- [[topics/advanced-3d-integration|先进三维集成]]
- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]

## 9. 评估与思考（Analysis）

- 方法优点：同时覆盖器件、单元库、核和 SRAM 阵列，形成较完整的缩放证据链。
- 局限性：A2 CFFET 在逻辑侧的频率收益不足，说明超堆叠并不自动等于更好 PP。
- 潜在风险：embedded power rail、超堆叠寄生和 SRAM RC 退化，会成为更靠后的主要瓶颈。

## 10. 参考与来源（References）

- 原始文件（仓库中未提供）
- [[topics/advanced-3d-integration|先进三维集成]]
