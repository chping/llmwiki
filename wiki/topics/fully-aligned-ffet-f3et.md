---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - F3ET
  - FFET
  - self-aligned-gate
related_topics:
  - advanced-3d-integration
related_pages:
  - PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors
---

# Fully-aligned FFET (F3ET)

## 1. 定义（Definition）

F3ET 是 FFET 的 fully-aligned 演进版本，
核心特征是前后两面的 gate 采用更充分的 self-aligned 组织。

## 2. 背景（Background）

- 来源：作者为解决 FFET 前后门失配问题而提出 F3ET。
- 发展过程：F3ET 是把 FFET 从概念验证推进到更成熟节点缩放的关键过渡形态。

## 3. 原理说明（Explanation）

- self-aligned gate 能减小前后门失配、降低门电阻并扩展可用 nanosheet 宽度。
- 这使 F3ET 在 cascade-heavy 电路里更容易把器件收益转化为频率收益。

## 4. 数学形式（Formalism）

相关工作主要通过 RO 频率、Rgate 与 block-level PPA 对 F3ET 进行比较。

## 5. 应用场景（Applications）

- A7 节点 FFET 扩展
- 低门电阻标准单元与小型 block

## 6. 示例（Examples）

- A7 F3ETNS 在 RO 与 library 评估中展现了较普通 FFET 更优的性能潜力。

## 7. 相关概念（Related Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/forksheet-based-f3et-f4et|Forksheet-based F3ET (F4ET)]]

## 8. 来源（Sources）

- [[topics/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors|PPA Scaling of FFET Technology Down to A2]]
