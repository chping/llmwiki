---
title: Flip 3D Integration（F3D）
type: source
created: 2026-04-26
updated: 2026-04-26
tags: [f3d, ffet, 3d-integration, packaging]
---

## 概述

`F3D` 是从 [[concepts/ffet|FFET]] 延展出的更大尺度 3D 集成路线，试图
把 3D 晶体管堆叠、双面互连、3D die stacking 与双面 monolithic 3D
统一到同一框架下。
[From Flip FET to Flip 3D Integration \(F3D\): Maximizing the Scaling
Potential of Wafer Both Sides Beyond Conventional 3D
Integration](../../raw/2026/04_26/From_Flip_FET_to_Flip_3D_Integration_F3D_Maximizing_the_Scaling_Potential_of_Wafer_Both_Sides_Beyond_Conventional_3D_Integration.pdf)

## 本次资料的关键信息

### 体系目标

资料把 F3D 描述为“同时利用晶圆正反两面”的系统级平台，使逻辑、存储和
互连可以在更高密度下协同集成。它不仅继承 FFET 的器件级收益，还把
dual-sided routing、hybrid bonding 与 M3D 一并纳入设计空间。
[From Flip FET to Flip 3D Integration \(F3D\): Maximizing the Scaling
Potential of Wafer Both Sides Beyond Conventional 3D
Integration](../../raw/2026/04_26/From_Flip_FET_to_Flip_3D_Integration_F3D_Maximizing_the_Scaling_Potential_of_Wafer_Both_Sides_Beyond_Conventional_3D_Integration.pdf)

### 公开结果

当前可获得摘要显示，基于 `32-bit FFET RISC-V core` 的评估中，双面信号
布线带来约 `6.8%` 面积降低和 `5.9%` `EDP` 改善；在 `Triple Flips`
相关 `BEOL` 优化后，核心 `EDP` 与频率最高进一步改善约 `3.2%` 与
`2.3%`。这些数字需要与原文图表交叉确认，因此保留
`#needs-verification`。
[From Flip FET to Flip 3D Integration \(F3D\): Maximizing the Scaling
Potential of Wafer Both Sides Beyond Conventional 3D
Integration](../../raw/2026/04_26/From_Flip_FET_to_Flip_3D_Integration_F3D_Maximizing_the_Scaling_Potential_of_Wafer_Both_Sides_Beyond_Conventional_3D_Integration.pdf)

### 方法学意义

对知识库当前主题而言，F3D 的重要性在于它把 FFET 从“器件与标准单元
问题”推进到“跨晶圆双面资源调度问题”。这意味着后续讨论 SRAM 或逻辑
PPA 时，不能只看单个 bitcell 或单个标准单元，而要把 routing、
thermal budget 与 bonding 约束一起考虑。
[From Flip FET to Flip 3D Integration \(F3D\): Maximizing the Scaling
Potential of Wafer Both Sides Beyond Conventional 3D
Integration](../../raw/2026/04_26/From_Flip_FET_to_Flip_3D_Integration_F3D_Maximizing_the_Scaling_Potential_of_Wafer_Both_Sides_Beyond_Conventional_3D_Integration.pdf)

## 关联页面

- [[concepts/ffet|FFET]]
- [[topics/3d-sram|3D SRAM]]
- [[topics/vfet-logic-scaling|VFET 逻辑缩放]]
