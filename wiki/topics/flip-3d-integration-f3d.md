---
title: Flip 3D Integration (F3D)
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - F3D
  - 三维集成
  - 晶圆翻转
related_topics:
  - advanced-3d-integration
related_pages:
  - from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration
---

## 1. 定义（Definition）

F3D 是论文提出的一种统一三维集成框架，目标是在同一技术路径中整合 3D 晶体管堆叠、双面互连、双面混合键合堆叠以及双面 Monolithic 3D。

## 2. 背景（Background）

- 来源：作者将其定位为对 [[topics/flip-fet|Flip FET]] 的进一步扩展。
- 发展过程：F3D 并非单一器件创新，而是把前期分散发展的多种 3D 集成技术拼接成更完整的工艺蓝图。

## 3. 原理说明（Explanation）

- 在器件层，F3D 继承 FFET 的三维晶体管和双面互连能力。
- 在封装层，F3D 依赖双面 I/O 与双面 hybrid bonding，
  支持 face-to-face、back-to-back、face-to-back 等堆叠方式。
- 在工艺层，F3D 使用 [[topics/multi-flipping-processes|Multi-Flipping Processes]]
  缓解热预算冲突，使双面 M3D 更可落地。

## 4. 数学形式（Formalism）

本文主要以架构与流程图说明 F3D，不提供单一封闭公式。

## 5. 应用场景（Applications）

- 高密度逻辑与存储协同集成
- 去除部分 TSV 依赖的 3D die stacking
- 面向未来更自由的双面堆叠系统

## 6. 示例（Examples）

- 作者以 32-bit RISC-V 核展示了 F3D 相关布线与 PPA 改善，
  并给出 Double Flips / Triple Flips 的 block-level 对比。

## 7. 相关概念（Related Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/dual-sided-interconnects|Dual-Sided Interconnects]]
- [[topics/multi-flipping-processes|Multi-Flipping Processes]]

## 8. 来源（Sources）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|From Flip FET to Flip 3D Integration (F3D)]]
