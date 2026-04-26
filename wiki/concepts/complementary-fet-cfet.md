---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - CFET
  - 堆叠晶体管
related_topics:
  - advanced-3d-integration
  - vfet-layout-design
  - ffet-sram-design
related_pages:
  - Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
  - Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology
---

# [[Complementary FET (CFET)]]

## 1. 定义（Definition）

CFET 是把 nFET 与 pFET 以垂直方向堆叠在同一 footprint 中的
互补晶体管架构，是后二维缩放时代的重要堆叠器件路线。

## 2. 背景（Background）

- 来源：CFET 被广泛视为先进逻辑缩放的主流候选路线之一。
- 发展过程：它带来显著面积收益，但也因高纵横比和复杂垂直集成步骤承受较大工艺压力。

## 3. 原理说明（Explanation）

- 通过垂直堆叠 n/p 器件，CFET 把逻辑单元高度进一步压缩。
- 其主要代价来自 HAR 工艺、底层接触形成、门极与源漏的复杂垂直组织。

## 4. 数学形式（Formalism）

相关论文主要通过面积、频率、功耗与寄生比较，而非统一封闭公式描述 CFET。

## 5. 应用场景（Applications）

- 先进逻辑标准单元
- 作为 FFET、VFET 等新路线的基准比较对象

## 6. 示例（Examples）

- 多篇 FFET 与 VFET 论文都把 CFET 作为面积、工艺复杂度和变异的对照基线。

## 7. 相关概念（Related Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/vertical-field-effect-transistor-vfet|Vertical Field-Effect Transistor (VFET)]]

## 8. 来源（Sources）

- [[pages/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|Consideration of VFET for Ultimate Logic Scaling]]
- [[pages/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET|Overlay-aware Variation Study of Flip FET and Benchmark with CFET]]
- [[pages/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology|Process Development and Optimization of FFET]]
