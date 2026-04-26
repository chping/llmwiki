---
title: 3D SRAM
type: source
created: 2026-04-26
updated: 2026-04-26
tags: [sram, 3d-integration, memory-compiler]
---

## 概述

`3D SRAM` 指将 [[concepts/sram|SRAM]] 阵列或其外围电路沿垂直方向分层
集成的实现方式，目标是在面积受限场景下改善密度，并为存储带宽扩展提
供空间。[3D SRAM Design & Optimization with Open Source Memory
Compiler](../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)

## 本次资料的关键信息

### 开源自动化设计

资料显示，论文工作以 [[entities/openram|OpenRAM]] 为基础扩展 3D 设计
能力，使用户可以基于容量、层数和工艺库输入自动生成多层 3D SRAM
的版图，并配套功耗和时序分析流程。[3D SRAM Design & Optimization
with Open Source Memory
Compiler](../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)

### 与 2D SRAM 的对比趋势

根据当前可恢复的论文索引摘要，双层 3D SRAM 在 `32-bit` 字宽下相对
2D SRAM 平均面积约缩小 `17%`，在 `64-bit` 字宽下平均面积约缩小
`38%`；但平均功耗约增加 `1.6%`，读时间约增加 `15%`。这些具体数值
需要回查论文原图表后再次确认，因此先标注为 #needs-verification。
[3D SRAM Design & Optimization with Open Source Memory
Compiler](../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)

### 设计约束

资料强调，小容量 3D SRAM 可能因 `TSV` 寄生效应在性能和功耗上不占优，
因此 3D 集成的收益更依赖容量规模、层间互连开销和外围组织方式。
[3D SRAM Design & Optimization with Open Source Memory
Compiler](../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)

## 关联页面

- [[concepts/sram|SRAM]]
- [[topics/ffet-sram-design|FFET 对 SRAM 设计的影响]]
- [[entities/openram|OpenRAM]]
