---
type: concept
created: 2026-04-26
updated: 2026-04-26
tags:
  - VFET
  - 垂直器件
related_topics:
  - vfet-layout-design
  - advanced-3d-integration
related_pages:
  - Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective
---

# Vertical Field-Effect Transistor (VFET)

## 1. 定义（Definition）

VFET 是一种沟道电流沿垂直方向传输的场效应晶体管结构，
通过把源 / 栅 / 漏沿垂直方向堆叠来换取更小 footprint。

## 2. 背景（Background）

- 来源：该概念常被用于后 FinFET / nanosheet 时代的极限逻辑缩放讨论。
- 发展过程：相较 lateral 器件，VFET 更强调布局方向、接触可达性和器件非对称性。

## 3. 原理说明（Explanation）

- VFET 的上下电极与沟道在几何上并不对称，因此 Forward / Reverse 模式电学特性不同。
- nanosheet 的摆放方向直接决定电源轨连接能力与布局布线方式。

## 4. 数学形式（Formalism）

本文没有单独给出统一公式，主要通过 Ieff、Cgd、面积和 RO 频率进行比较。

## 5. 应用场景（Applications）

- 先进逻辑标准单元
- 面向极限缩放的 DTCO 探索

## 6. 示例（Examples）

- [[topics/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|该论文]]
  讨论了 HNS / VNS 与 FWD / REV 对 VFET PPA 的影响。

## 7. 相关概念（Related Concepts）

- [[topics/complementary-fet-cfet|Complementary FET (CFET)]]
- [[topics/flip-fet|Flip FET]]

## 8. 来源（Sources）

- [[topics/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|Consideration of VFET for Ultimate Logic Scaling]]
