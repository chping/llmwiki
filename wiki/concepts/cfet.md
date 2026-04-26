---
title: CFET
type: concept
created: 2026-04-26
updated: 2026-04-26
tags: [device, logic-scaling, 3d-integration]
---

## 定义

`CFET` 通常指将互补 `n/p FET` 在垂直方向单片堆叠的器件路线，是先进
逻辑缩放中的关键候选。

## 本次资料中的定位

- 多篇 FFET 论文将 CFET 作为直接 benchmark，对比工艺复杂度、
  高纵横比制程压力、布线资源与功率性能。
- FFET 路线的核心论点之一，是在维持 3D 堆叠收益的同时，相比单片 CFET
  获得更友好的制造流程和更高的设计自由度。
- overlay-aware 研究指出，CFET 由于 self-aligned gate，受 backside
  misalignment 的影响较小；但其高纵横比工艺仍然带来显著制造挑战。

[First Experimental Demonstration of Self-Aligned Flip FET
\(FFET\): A Breakthrough Stacked Transistor Technology with 2.5T
Design, Dual-Side Active and
Interconnects](../../raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf)

[Process Development and Optimization of Flip FET \(FFET\) for Stacked
Transistors
Technology](../../raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf)

[Overlay-aware variation study of flip FET and benchmark with
CFET](../../raw/2026/04_26/Overlay-aware%20variation%20study%20of%20flip%20FET%20and%20benchmark%20with%20CFET.pdf)

## 关联页面

- [[concepts/ffet|FFET]]
- [[concepts/vfet|VFET]]
- [[topics/vfet-logic-scaling|VFET 逻辑缩放]]
