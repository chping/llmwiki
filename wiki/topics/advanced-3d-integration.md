---
type: topic
created: 2026-04-26
updated: 2026-04-26
tags:
  - 三维集成
  - 先进封装
  - 单片三维
related_pages:
  - from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration
  - Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
  - Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology
related_concepts:
  - flip-fet
  - flip-3d-integration-f3d
  - dual-sided-interconnects
  - multi-flipping-processes
  - vertical-field-effect-transistor-vfet
  - complementary-fet-cfet
  - drain-merge
  - fully-aligned-ffet-f3et
  - forksheet-based-f3et-f4et
  - cfet-based-ffet-cffet
  - bipolar-sram
related_entities:
  - peking-university
  - risc-v
  - open-source-memory-compiler
---

# 先进三维集成

## 1. 主题概述（Overview）

先进三维集成关注如何在器件、互连、封装和系统层面同时提升集成密度。
相较传统单面设计，它强调利用晶圆前后两面、垂直堆叠路径以及更细粒度的
芯粒或单片级集成，以突破二维布线和面积缩放的边界。

## 2. 背景与意义（Background）

- 技术背景：传统缩放收益下降后，行业开始同时推进 3D 晶体管、backside power delivery、混合键合和 Monolithic 3D。
- 研究动机：单独优化器件或单独优化封装都不足以释放完整密度潜力，需要跨层协同。
- 应用价值：可用于高密度逻辑、HBM 邻近集成、逻辑与存储协同设计，以及更高带宽的 die-to-die 连接。

## 3. 核心问题（Key Problems）

- 如何让前后两面都承担有效的信号与供电功能，而不是仅把 backside 当作辅助层。
- 如何在引入更多三维工艺步骤后，仍控制热预算、材料兼容性与制造复杂度。

## 4. 方法与技术路线（Methods）

- 3D 晶体管路线：以 [[topics/flip-fet|Flip FET]] 为代表，
  强调更可制造的三维晶体管集成。
- 双面互连路线：以 [[topics/dual-sided-interconnects|双面互连]]
  提升引脚分布与布线灵活性。
- 系统级整合路线：以 [[topics/flip-3d-integration-f3d|F3D]]
  作为统一框架，连接器件、互连、封装与双面 M3D。
- 工艺重排路线：以 [[topics/multi-flipping-processes|Multi-Flipping Processes]]
  重新安排前后两面的高温步骤和互连形成顺序，降低热预算冲突。

## 5. 核心结论与共识（Key Insights）

- 真正有效的三维扩展来自跨层协同，而不是单点创新。
- 前后两面同时参与信号、供电与键合，是进一步提升三维集成收益的关键方向。

## 6. 相关页面（Source Pages）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|From Flip FET to Flip 3D Integration (F3D)]]
- [[topics/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|Consideration of VFET for Ultimate Logic Scaling]]
- [[topics/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|First Experimental Demonstration of FFET]]
- [[topics/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET|Overlay-aware Variation Study of Flip FET and Benchmark with CFET]]
- [[topics/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]
- [[topics/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology|Process Development and Optimization of FFET]]

## 7. 关键概念（Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/flip-3d-integration-f3d|Flip 3D Integration (F3D)]]
- [[topics/dual-sided-interconnects|Dual-Sided Interconnects]]
- [[topics/multi-flipping-processes|Multi-Flipping Processes]]
- [[topics/vertical-field-effect-transistor-vfet|Vertical Field-Effect Transistor (VFET)]]
- [[topics/complementary-fet-cfet|Complementary FET (CFET)]]
- [[topics/drain-merge|Drain Merge]]
- [[topics/fully-aligned-ffet-f3et|Fully-aligned FFET (F3ET)]]
- [[topics/forksheet-based-f3et-f4et|Forksheet-based F3ET (F4ET)]]
- [[topics/cfet-based-ffet-cffet|CFET-based FFET (CFFET)]]
- [[topics/bipolar-sram|Bipolar SRAM]]

## 8. 相关实体（Entities）

- 北京大学
- [[topics/RISC-V|RISC-V]]
- [[topics/sram-memory-compiler|Open Source Memory Compiler]]

## 9. 发展趋势（Trends）

- 从 backside power 扩展到 backside signal 与双面 I/O。
- 从单一 die stacking 扩展到双面 hybrid bonding 与更自由的堆叠拓扑。

## 10. 未解决问题（Open Problems）

- 双面对准、公差控制、热应力与可靠性验证仍是工程瓶颈。
- 大规模量产下的成本收益比尚待进一步验证。

## 11. 来源补充（Source Notes）

<!-- source: wiki/pages/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.md -->
VFET 设计论文补充了另一条垂直器件路线，说明先进三维集成并不只包含 FFET /
F3D，也包括 VFET 这类更偏器件与单元布局协同的方案。
<!-- /source: wiki/pages/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.md -->

<!-- source: wiki/pages/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET.md -->
Overlay-aware 研究说明 advanced-3d-integration 的难点不仅是结构创新，
还包括 variation-aware 设计规则与寄生鲁棒性。
<!-- /source: wiki/pages/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET.md -->
