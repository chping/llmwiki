---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - SRAM
  - FFET
  - 存储结构
related_topics:
  - ffet-sram-design
  - advanced-3d-integration
related_pages:
  - First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
  - FFET工艺特点及对SRAM设计影响表格汇总
---

# Bipolar SRAM

## 1. 定义（Definition）

Bipolar SRAM 是 FFET 路线下提出的一类 SRAM 组织方式，
利用双面器件和跨面连接结构来重新安排单元内的耦合与外围连接。

## 2. 背景（Background）

- 来源：它出现在 FFET 论文中，作为比传统单极组织更能利用双面结构的 SRAM 方案。
- 发展过程：从早期结构可行性讨论，发展到 A14-A2 缩放路线中的阵列级比较对象。

## 3. 原理说明（Explanation）

- Bipolar SRAM 试图用双面 WL / BL 与更紧凑的跨面耦合来降低部分 RC 与面积开销。
- 它的收益与风险都更依赖器件匹配、BL / WL RC 和跨面寄生控制。

## 4. 数学形式（Formalism）

相关工作主要比较读写延迟、写裕量和 BL / WL RC，而非给出统一封闭模型。

## 5. 应用场景（Applications）

- FFET SRAM bitcell 研究
- A2 之后 SRAM 继续缩放的结构探索

## 6. 示例（Examples）

- FFET 首次实验论文和 A2 PPA 路线图都把 Bipolar SRAM 作为重要存储方向来研究。

## 7. 相关概念（Related Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/drain-merge|Drain Merge]]

## 8. 来源（Sources）

- [[topics/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects|First Experimental Demonstration of FFET]]
- [[topics/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]
