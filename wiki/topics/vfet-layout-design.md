---
type: topic
created: 2026-04-26
updated: 2026-04-26
tags:
  - VFET
  - 版图
  - DTCO
related_pages:
  - Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective
related_concepts:
  - vertical-field-effect-transistor-vfet
  - complementary-fet-cfet
  - flip-fet
related_entities:
  - peking-university
---

# VFET 布局设计

## 1. 主题概述（Overview）

该主题关注 [[topics/vertical-field-effect-transistor-vfet|VFET]]
在标准单元设计中的方向选择、器件非对称性和复杂门布局策略，
重点是把器件结构约束翻译成实际可用的 DTCO 方法。

## 2. 背景与意义（Background）

- 技术背景：VFET 通过垂直沟道提供更强面积缩放潜力，但其版图约束与传统 lateral 器件不同。
- 研究动机：器件层面的潜力只有在标准单元布局与寄生层面兑现，才有真实工程价值。
- 应用价值：可用于 VFET library 规划、复杂门设计和后续 block 级实现策略。

## 3. 核心问题（Key Problems）

- 横向 / 纵向 nanosheet placement 如何影响面积、性能和布线自由度。
- FWD / REV 模式不对称会如何影响复杂标准单元的稳定实现。

## 4. 方法与技术路线（Methods）

- 用 DTCO 联合 TCAD、SPICE、PEX 和 RO 仿真评价不同布局方案。
- 对复杂门引入 mixed-mode 设计，协调布局可行性与器件性能。

## 5. 核心结论与共识（Key Insights）

- VNS FWD 在面积和性能上更有吸引力，但复杂门仍需更精细的 mixed-mode 方法。
- VFET 的器件不对称性必须进入版图方法学，而不能被当作二阶效应忽略。

## 6. 相关页面（Source Pages）

- [[topics/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|Consideration of VFET for Ultimate Logic Scaling]]

## 7. 关键概念（Concepts）

- [[topics/vertical-field-effect-transistor-vfet|Vertical Field-Effect Transistor (VFET)]]
- [[topics/complementary-fet-cfet|Complementary FET (CFET)]]
- [[topics/flip-fet|Flip FET]]

## 8. 相关实体（Entities）

- 北京大学

## 9. 发展趋势（Trends）

- 从单反相器布局比较扩展到 AOI21 等复杂门 mixed-mode 设计。
- 从单元级对比继续迈向更完整的 VFET library 与 P&R 验证。

## 10. 未解决问题（Open Problems）

- 上下源漏非对称性若不能在工艺层面缓解，将长期拖累 VFET 标准单元质量。
- 现阶段对 block 级与系统级效益的验证仍不足。
