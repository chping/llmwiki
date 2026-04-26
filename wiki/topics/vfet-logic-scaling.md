---
title: VFET 逻辑缩放
type: source
created: 2026-04-26
updated: 2026-04-26
tags: [vfet, logic-scaling, dtco]
---

## 概述

本页记录 `VFET` 在极限逻辑缩放语境下的设计问题，重点是版图、对称性、
`DTCO` 和电路级 `PPA`，而不是单独讨论某一个器件指标。
[Consideration of VFET for Ultimate Logic Scaling: A Design
Perspective](../../raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf)

## 当前可确认的信息

### 论文关注范围

PDF 元数据将论文关键词列为 `VFET`、`layout`、`DTCO`、`circuit level
PPA`、`nanosheet channel placement` 与 `device asymmetry`。据此可推断，
作者是在设计视角下评估 VFET，而不是把它当作纯工艺论文来讨论。
[Consideration of VFET for Ultimate Logic Scaling: A Design
Perspective](../../raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf)

### 对知识库的意义

这篇材料把当前路线图补齐了一块关键对照：如果 FFET 强调双面资源与堆叠
制造友好性，那么 VFET 更像是在垂直沟道器件下重新审视版图与电路映射。
因此，后续比较 [[concepts/vfet|VFET]]、[[concepts/cfet|CFET]] 与
[[concepts/ffet|FFET]] 时，应重点看：

- 器件几何是否迫使标准单元布局产生新的非对称。
- 垂直方向的通道放置是否改变局部互连与 pin access。
- 器件优势能否在 block 级 `PPA` 上兑现，而不只是停留在器件指标层面。

### 待补充项

由于本地 PDF 还未成功抽取到完整摘要，关于 VFET 在具体节点、标准单元
或电路 benchmark 上的量化结论暂不写死，统一标记为
`#needs-verification`。
[Consideration of VFET for Ultimate Logic Scaling: A Design
Perspective](../../raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf)

## 关联页面

- [[concepts/vfet|VFET]]
- [[concepts/cfet|CFET]]
- [[concepts/ffet|FFET]]
- [[topics/flip-3d-integration|Flip 3D Integration（F3D）]]
