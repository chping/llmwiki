---
title: Multi-Flipping Processes
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - 晶圆翻转
  - 热预算
  - 三维集成
related_topics:
  - advanced-3d-integration
related_pages:
  - from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration
---

## 1. 定义（Definition）

Multi-Flipping Processes 是论文为 [[concepts/flip-3d-integration-f3d|F3D]]
提出的一组晶圆多次翻转制造流程，通过在前后两面的 FEOL、MOL、BEOL
之间重新排序，缓解高温步骤对金属与介质材料的热预算约束。

## 2. 背景（Background）

- 来源：作者将其视为把 [[concepts/flip-fet|Flip FET]]
  扩展到双面 M3D 与双面 die stacking 的关键工艺基础。
- 发展过程：从仅用于概念验证的 Single Flip，发展到 Double
  Flips 与 Triple Flips，以兼顾先进逻辑节点的 gate-last 需求和后续
  互连优化空间。

## 3. 原理说明（Explanation）

- Double Flips 在前面源漏外延后先执行第一次翻转，等 backside 相关高温过程完成后再翻回 frontside 形成金属栅，以避免高温外延破坏已形成的金属栅。
- Triple Flips 在 Double Flips 基础上再增加一次翻转，使前后两面的 MOL 与 BEOL 尽量都安排在 FEOL 之后完成，从而支持更优的金属和介质组合。
- 该流程的核心不是增加翻转次数本身，而是把热预算冲突从器件层转移到更可控的工艺顺序设计上。

## 4. 数学形式（Formalism）

本文未给出统一数学模型，主要以流程图和 block-level PPA 指标对
Double Flips / Triple Flips 的收益进行比较。

## 5. 应用场景（Applications）

- 支持双面 Monolithic 3D 的制造流程设计
- 为双面 hybrid bonding 与更自由的 3D 堆叠提供工艺可行性
- 在先进逻辑节点中平衡器件性能、互连材料与热预算限制

## 6. 示例（Examples）

- 论文报告相较未优化方案，Triple Flips 优化后可进一步带来最高 3.2%
  的 EDP 改善和 2.3% 的频率提升。

## 7. 相关概念（Related Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/flip-3d-integration-f3d|Flip 3D Integration (F3D)]]
- [[concepts/dual-sided-interconnects|Dual-Sided Interconnects]]

## 8. 来源（Sources）

<!-- markdownlint-disable-next-line MD013 -->
- [[from-flip-fet-to-flip-3d-integration-f3d-maximizing-the-scaling-potential-of-wafer-both-sides-beyond-conventional-3d-integration|From Flip FET to Flip 3D Integration (F3D)]]
