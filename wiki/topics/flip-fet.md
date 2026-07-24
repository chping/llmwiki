---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - 三维晶体管
  - 双面互连
related_topics:
  - advanced-3d-integration
  - ffet-sram-design
related_pages:
  - from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
  - Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology
  - FFET工艺特点及对SRAM设计影响表格汇总
---

# Flip FET

## 1. 定义（Definition）

Flip FET 是一种把 3D 堆叠沟道器件与双面互连结合起来的器件与互连协同方案。
其目标是在单个晶圆内同时利用 frontside 与 backside，改善布线资源与集成密度。

## 2. 背景（Background）

- 来源：论文把 FFET 视为连接先进逻辑缩放与更广义 3D 集成路线的关键节点。
- 发展过程：FFET 从早期仅作概念验证，进一步扩展到支持更成熟的双面互连与多次翻转工艺。

## 3. 原理说明（Explanation）

- 通过双面引脚与双面布线，FFET 允许信号在晶圆两侧独立分布。
- 论文中特别强调其 Drain Merge 相关设计，使输出 pin 可同时存在于前后两面，从而减少跨面信号转接结构。

## 4. 数学形式（Formalism）

本文未给出统一数学定义，主要以工艺流程、布线资源与 PPA 指标来描述 FFET 的收益。

## 5. 应用场景（Applications）

- 高密度逻辑核心设计
- 与 [[topics/dual-sided-interconnects|双面互连]] 配合的先进三维集成

## 6. 示例（Examples）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|该论文]]在 32-bit RISC-V 核上展示了 FFET 与 DSI 2.0 结合后的面积和 EDP 收益。
- [[topics/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|首次实验论文]]
  展示了 FFET 的 2.5T 标准单元与 SRAM 扩展。
- [[topics/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA 路线图]]
  把 FFET 扩展到了 F3ET、F4ET 与 CFFET。

## 7. 相关概念（Related Concepts）

- [[topics/flip-3d-integration-f3d|Flip 3D Integration (F3D)]]
- [[topics/dual-sided-interconnects|Dual-Sided Interconnects]]

## 8. 来源（Sources）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|From Flip FET to Flip 3D Integration (F3D)]]
- [[topics/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|First Experimental Demonstration of FFET]]
- [[topics/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET|Overlay-aware Variation Study of Flip FET and Benchmark with CFET]]
- [[topics/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology|Process Development and Optimization of FFET]]
