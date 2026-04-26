---
title: Dual-Sided Interconnects
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - DSI
  - 双面布线
  - backside
related_topics:
  - advanced-3d-integration
related_pages:
  - from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration
---

## 1. 定义（Definition）

双面互连指在晶圆的 frontside 与 backside 两侧同时布置互连资源、引脚和信号路径，使两面都参与供电与通信，而不是仅将 backside 用作供电辅助层。

## 2. 背景（Background）

- 来源：论文把 DSI 的演进分为 DSI 1.0、1.5 与 2.0。
- 发展过程：随着标准单元继续缩小，仅依赖 frontside 布线会导致资源紧张，因此 backside 需要承担更多信号功能。

## 3. 原理说明（Explanation）

- DSI 1.0 中，标准单元引脚主要位于前面，backside 信号需借助 STC 或 nTSV 转接。
- DSI 1.5 中，前后两面都有引脚，但跨面连接仍频繁依赖转接结构，面积代价较高。
- DSI 2.0 通过双面输出 pin 设计减少跨面转接，从而提升布线灵活性并改善面积效率。

## 4. 数学形式（Formalism）

本文没有给出统一数学模型，主要通过面积、EDP 与频率等实现指标比较 DSI 方案。

## 5. 应用场景（Applications）

- 双面标准单元布线
- 双面 I/O bump 与 hybrid bonding
- 更高密度的 3D 逻辑与封装系统

## 6. 示例（Examples）

- 在论文基准中，采用 DSI 2.0 的 FFET 32-bit RISC-V 核可获得约 6.8% 面积下降和 5.9% EDP 改善。

## 7. 相关概念（Related Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/flip-3d-integration-f3d|Flip 3D Integration (F3D)]]

## 8. 来源（Sources）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|From Flip FET to Flip 3D Integration (F3D)]]
