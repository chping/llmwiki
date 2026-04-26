---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - 寄生
  - 互连
  - FFET
related_topics:
  - advanced-3d-integration
  - ffet-sram-design
related_pages:
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET
  - FFET工艺特点及对SRAM设计影响表格汇总
---

# [[Drain Merge]]

## 1. 定义（Definition）

Drain Merge 是 FFET 中连接前后两面相关漏极区域的跨层连接结构，
通常既承担电连接功能，也直接决定关键读写路径的寄生电阻。

## 2. 背景（Background）

- 来源：它是 FFET 实现双面器件协同工作的关键结构之一。
- 发展过程：随着 FFET 从器件演示走向 variation-aware DTCO，Drain Merge 从“连接结构”变成“性能瓶颈”。

## 3. 原理说明（Explanation）

- Drain Merge 若与前面结构对准不佳，其电阻会显著波动。
- 在 SRAM 和标准单元中，这种波动会直接拖慢读路径或关键反相链路。

## 4. 数学形式（Formalism）

相关工作主要讨论其寄生电阻变化 `ΔRDM` 对 RO 频率和统计分布的影响。

## 5. 应用场景（Applications）

- FFET 标准单元与反相器
- FFET SRAM 读路径与关键串联节点

## 6. 示例（Examples）

- Overlay-aware 研究表明 Drain Merge 是 FFET misalignment variation 的主导源。

## 7. 相关概念（Related Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/bipolar-sram|Bipolar SRAM]]

## 8. 来源（Sources）

- [[pages/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET|Overlay-aware Variation Study of Flip FET and Benchmark with CFET]]
- [[pages/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|First Experimental Demonstration of FFET]]
