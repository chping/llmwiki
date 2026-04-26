---
title: FFET 对 SRAM 设计的影响
type: source
created: 2026-04-26
updated: 2026-04-26
tags: [ffet, sram, dtco, 3d-integration]
---
%%  %%

## 概述

本页整理 `FFET` 工艺特征对 [[concepts/sram|SRAM]] bitcell、外围电路
与测试策略的主要影响，内容来自对 FFET 工艺特性与 SRAM 设计关系的
结构化表格汇总。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

## 关键影响

### 单元面积与拓扑自由度

资料指出，FFET 的双面器件堆叠与 `dual-side active` 机制有利于缩小
bitcell footprint，并支持更激进的 3D split SRAM 或非传统 `6T/8T`
组织；但跨面不对称也会放大失配，进而影响 `SNM`、写入能力与
`Vmin`。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

结合 2024 年 FFET 首次实验验证论文，双面极性自由度还被用来提出
bipolar SRAM，摘要声称其面积相对 CFET SRAM 进一步缩小约 `12%`，
相对 FinFET SRAM 缩小至少 `35.9%`。这一结果说明 FFET 对 SRAM 的
潜在收益不仅在外围布线，也可能直接体现在 bitcell 拓扑重组上。
`#needs-verification`
[First Experimental Demonstration of Self-Aligned Flip FET \(FFET\):
A Breakthrough Stacked Transistor Technology with 2.5T Design, Dual-Side
Active and
Interconnects](../../raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf)

### 布线与外围收益更直接

双面互连、双面引脚和双面布线资源对 SRAM 的主要收益集中在外围，
包括字线、位线、译码器、驱动器与 sense 路径的拥塞缓解和层次拆分。
因此 FFET 的系统级收益不应只用 bitcell 面积衡量，也应纳入外围
`PPA` 改善。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

### 制造对准与寄生是首要风险

资料将 `overlay/misalignment`、`drain-merge` 电阻波动、垂直电静耦合
与跨面寄生列为 FFET SRAM 的关键风险源。这些因素会直接改变器件
匹配、读路径电阻与统计尾部，进而影响 `RSNM`、`WSNM`、`Iread`
与良率。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

### 测试芯片策略

资料建议首版芯片优先强调“可测性、可分解性、可回归性”，包括：

- 设置 overlay-aware monitor，并与 SRAM fail bitmap、`Iread` 分布联动分析。
- 针对读路径相关器件与 `drain-merge` 结构设计专门测试结构。
- 以小规模 FFET SRAM 与小规模 `F2F demo` 为主，而不是同时追求大容量和最复杂 3D 架构。
- 建立温升到 `Iread`、`SNM`、`Vmin` 的一阶关系，而非首版就做长时寿命结论。

[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

### 工艺与缩放约束

2025 年 TED 与 VLSI 资料补充了 SRAM 导入 FFET 时更现实的边界条件：
前者强调 thermal budget、金属污染、substrate thinning 与多次 flipping
流程的工程权衡，后者则表明 FFET 路线正在向 `A2` 节点推进，并已把
SRAM 阵列缩放研究推进到 `256 x 256` 规模。也就是说，SRAM 设计问题
不能只停留在概念验证，而必须和工艺选项、节点目标、测试阵列规模一起看。
`#needs-verification`
[Process Development and Optimization of Flip FET \(FFET\) for Stacked
Transistors
Technology](../../raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf)

[PPA Scaling of Flip FET Technology Down to A2 Node Enabled by
Architecture Innovations: Self-Aligned Gate, 2T Design with Embedded
Power Rail and Ultra-Stacked 4-Tier
Transistors](../../raw/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors.pdf)

## 设计判断

结合本次资料，FFET 对 SRAM 的价值更像是“bitcell 与 periphery 联合
DTCO 问题”，而不是单纯的器件替换问题。若缺乏对准监控、寄生建模和
热/IR 观测，阵列密度提升很容易被统计尾部和稳定性代价吞掉。
[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

## 关联页面

- [[concepts/ffet|FFET]]
- [[concepts/sram|SRAM]]
- [[topics/3d-sram|3D SRAM]]
- [[concepts/cfet|CFET]]
