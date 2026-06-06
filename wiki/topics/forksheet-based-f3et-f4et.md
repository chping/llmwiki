---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - F4ET
  - forksheet
  - FFET
related_topics:
  - advanced-3d-integration
related_pages:
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
---

# [[Forksheet-based F3ET (F4ET)]]

## 1. 定义（Definition）

F4ET 是在 F3ET 基础上进一步结合 Forksheet 与 embedded power rail 的
FFET 变体，用来把 cell height 推进到 2T 级。

## 2. 背景（Background）

- 来源：作者为继续压缩 FFET 单元高度而引入 F4ET。
- 发展过程：它是 FFET 从 A7 向 A5 / A3 持续缩放时的关键结构升级。

## 3. 原理说明（Explanation）

- Forksheet 帮助压缩 cell height。
- embedded power rail 把原本限制边界缩放的供电轨嵌入介质墙中，释放更多布局空间。

## 4. 数学形式（Formalism）

主要通过 CH、RO 频率、IR-drop 与 block-level PPA 展示其收益。

## 5. 应用场景（Applications）

- A5 / A3 高性能与高密度 FFET 单元库
- 更激进的 FFET PPA 缩放路线

## 6. 示例（Examples）

- A5 HP / HD F4ET 在多种 BEOL 负载下都展现出明显优于 A14 FFET 的速度优势。

## 7. 相关概念（Related Concepts）

- [[concepts/fully-aligned-ffet-f3et|Fully-aligned FFET (F3ET)]]
- [[concepts/cfet-based-ffet-cffet|CFET-based FFET (CFFET)]]

## 8. 来源（Sources）

- [[pages/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]
