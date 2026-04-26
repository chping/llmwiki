---
title: SRAM
type: concept
created: 2026-04-26
updated: 2026-04-26
tags: [memory, circuit]
---

## 定义

`SRAM` 是以双稳态存储单元保存数据的静态随机存取存储器，常见实现围绕 `6T` bitcell 展开，并通过字线、位线、sense amplifier 与外围译码驱动组成完整宏单元。

## 本次资料补充

- 在 [[topics/3d-sram|3D SRAM]] 资料中，SRAM 被扩展到多层集成场景，
  设计空间同时覆盖容量、层数、版图生成与时序功耗分析。
  [3D SRAM Design & Optimization with Open Source Memory
  Compiler](../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)
- 在 [[topics/ffet-sram-design|FFET 对 SRAM 设计的影响]] 资料中，SRAM
  的关键敏感指标包括 `SNM`、`WSNM`、`Iread`、retention 与
  `Vmin`，这些指标会受到层间寄生、制造对准和热效应的强烈影响。
  [FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)
- 新导入的 FFET 论文进一步把 SRAM 放到更激进的器件缩放背景下讨论，
  包括 bipolar SRAM、`A2` 节点阵列缩放和 `256 x 256` 级别的评估；
  这说明 SRAM 已经成为 FFET 路线中验证 layout、variation 与 PPA
  是否能真正闭环的重要 benchmark。`#needs-verification`
  [First Experimental Demonstration of Self-Aligned Flip FET
  \(FFET\): A Breakthrough Stacked Transistor Technology with 2.5T
  Design, Dual-Side Active and
  Interconnects](../../raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf)

  [PPA Scaling of Flip FET Technology Down to A2 Node Enabled by
  Architecture Innovations: Self-Aligned Gate, 2T Design with Embedded
  Power Rail and Ultra-Stacked 4-Tier
  Transistors](../../raw/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors.pdf)

## 关联页面

- [[topics/3d-sram|3D SRAM]]
- [[topics/ffet-sram-design|FFET 对 SRAM 设计的影响]]
- [[concepts/ffet|FFET]]
- [[concepts/cfet|CFET]]
