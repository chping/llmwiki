---
type: topic
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - SRAM
  - 存储设计
related_pages:
  - 3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler
  - FFET工艺特点及对SRAM设计影响表格汇总
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
related_concepts:
  - flip-fet
  - bipolar-sram
  - drain-merge
  - complementary-fet-cfet
related_entities:
  - peking-university
  - open-source-memory-compiler
---

# [[topics/ffet-sram-design|FFET 与 SRAM 设计]]

## 1. 主题概述（Overview）

该主题关注 [[concepts/flip-fet|FFET]] 与相关三维器件路线进入 SRAM 设计后，
bitcell、外围、电阻寄生、编译器流程和阵列组织会发生什么变化。
它不仅讨论单个 bitcell 面积，更强调双面布线、读路径寄生和
测试可测性的系统性影响。

## 2. 背景与意义（Background）

- 技术背景：SRAM 对器件失配、寄生和统计尾部高度敏感，因此是检验新器件成熟度的硬指标。
- 研究动机：FFET 在逻辑单元上已有密度优势，但 SRAM 是否真正受益需要单独验证。
- 应用价值：可指导 bitcell 选择、外围电路 DTCO、测试芯片规划和 memory compiler 扩展。

## 3. 核心问题（Key Problems）

- 双面器件与双面互连是否真的能转化为 SRAM 阵列和外围的可用收益。
- 读路径寄生、overlay 和热效应会如何放大到 Vmin、Iread 与良率问题。

## 4. 方法与技术路线（Methods）

- 通过 [[concepts/bipolar-sram|Bipolar SRAM]] 和 folded array 结构探索继续缩放。
- 在外围层面利用 FFET 的双面布线降低 WL / BL 与 driver 路由拥塞。
- 结合 [[entities/open-source-memory-compiler|开源 memory compiler]]
  探索 3D SRAM 的自动化设计空间搜索。

## 5. 核心结论与共识（Key Insights）

- FFET 对 SRAM 的收益很大一部分来自外围与布线，而非单独 bitcell 极限缩小。
- [[concepts/drain-merge|Drain Merge]]、overlay 和 BL / WL RC 是 SRAM 导入中的关键风险点。

## 6. 相关页面（Source Pages）

- [[pages/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler|3D SRAM Design & Optimization with Open Source Memory Compiler]]
- [[pages/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总|FFET工艺特点及对SRAM设计影响表格汇总]]
- [[pages/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|First Experimental Demonstration of FFET]]
- [[pages/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]

## 7. 关键概念（Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/bipolar-sram|Bipolar SRAM]]
- [[concepts/drain-merge|Drain Merge]]
- [[concepts/complementary-fet-cfet|Complementary FET (CFET)]]

## 8. 相关实体（Entities）

- [[entities/peking-university|北京大学]]
- [[entities/open-source-memory-compiler|Open Source Memory Compiler]]

## 9. 发展趋势（Trends）

- 从单独 bitcell 研究扩展到外围电路与编译器协同优化。
- 从 A14-A5 的双极 / 单极 SRAM 探索进一步走向 A2 级 folded 结构。

## 10. 未解决问题（Open Problems）

- 双面寄生与热效应如何系统映射到 SRAM 的统计尾部仍需更多 silicon 数据。
- 开源 compiler 是否能准确覆盖 3D SRAM 的层间 RC 和工艺约束仍待验证。
