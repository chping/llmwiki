---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - CFFET
  - 四层堆叠
  - FFET
related_topics:
  - advanced-3d-integration
  - ffet-sram-design
related_pages:
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
---

# [[CFET-based FFET (CFFET)]]

## 1. 定义（Definition）

CFFET 是 FFET 路线在 A2 节点上的超堆叠扩展，
通过 back-to-back stacked CFET 实现四层晶体管组织。

## 2. 背景（Background）

- 来源：作者希望把 FFET 的双面处理能力进一步推向 4-tier transistor。
- 发展过程：CFFET 被视为 FFET 路线的极限延伸，但逻辑和 SRAM 收益并不相同。

## 3. 原理说明（Explanation）

- CFFET 利用双面信号 / 供电和更激进的 intra-cell routing 压缩面积。
- 但因为有效宽度和寄生共同制约，逻辑电路的性能收益可能不如面积收益明显。

## 4. 数学形式（Formalism）

相关工作主要比较 cell area、RO 频率与 SRAM array 面积收益。

## 5. 应用场景（Applications）

- A2 之后的极限逻辑缩放探索
- 更偏向存储密度导向的 4-tier SRAM 结构

## 6. 示例（Examples）

- 论文表明 CFFET 在逻辑侧性能提升有限，但在 A2 SRAM 上更容易兑现面积优势。

## 7. 相关概念（Related Concepts）

- [[concepts/forksheet-based-f3et-f4et|Forksheet-based F3ET (F4ET)]]
- [[concepts/bipolar-sram|Bipolar SRAM]]

## 8. 来源（Sources）

- [[pages/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]
