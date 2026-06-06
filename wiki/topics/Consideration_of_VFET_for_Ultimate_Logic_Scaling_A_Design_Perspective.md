---
type: page
source: raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - VFET
  - DTCO
  - 标准单元
topics:
  - vfet-layout-design
  - advanced-3d-integration
concepts:
  - vertical-field-effect-transistor-vfet
  - complementary-fet-cfet
  - flip-fet
entities:
  - peking-university
---

<!-- markdownlint-disable-next-line MD013 -->
# [[pages/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective|Consideration of VFET for Ultimate Logic Scaling: A Design Perspective]]

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：Consideration of VFET for Ultimate Logic Scaling: A Design Perspective
- 原始文件路径：[原始 PDF](../../../../raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf)
- 文件类型：PDF
- 来源：2025 IEEE Electron Devices Technology & Manufacturing Conference (EDTM)
- 作者 / 机构：Yimeng Wang 等，[[entities/peking-university|北京大学]]
- 时间：2025
- DOI：`10.1109/EDTM61175.2025.11040360`

## 2. 摘要（Summary）

本文从 DTCO 视角系统讨论 [[concepts/vertical-field-effect-transistor-vfet|VFET]]
用于先进逻辑缩放时的版图与电路设计问题，重点比较横向与纵向
nanosheet placement，以及器件正向 / 反向工作模式带来的 PPA 差异。
结果表明，纵向 nanosheet 的 FWD 设计在相同功耗下可获得约 7% 的性能优势，
同时把单元面积再缩小约 33%；而器件非对称性使 FWD 模式相较 REV 模式拥有
约 20% 更大的 Ieff、约 30% 更低的 Cgd，并带来约 68% 的性能提升。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：后摩尔时代需要在 FinFET 之后继续寻找更高密度的器件与版图方案。
- 目标问题：VFET 的 nanosheet 放置方向和源漏非对称性会如何影响标准单元设计与 PPA。
- 应用场景：先进逻辑标准单元、复杂门电路、后续 VFET library 与 P&R 方法学。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 用 DTCO 流程联合 SPICE 模型、PEX 寄生和 15-stage ring oscillator 电路仿真。
- 比较 Horizontal Nanosheet（HNS）与 Vertical Nanosheet（VNS）两种放置方式。
- 比较 VFET 的 FWD / REV 两种工作模式，并提出混合模式复杂单元设计。

### 4.2 核心原理 / 机制

- VFET 的上下源漏形貌与位置不同，导致它本质上是非对称器件。
- HNS 设计更灵活，但 VNS 在 FWD 模式下能显著减小标准单元面积。
- 复杂门在 VNS 中面临更强布线约束，因此作者提出混合 FWD / REV 的布局策略。

### 4.3 数据与实验（如适用）

- VNS 相比 HNS 可实现约 33% 的单元面积缩减。
- FWD 模式相较 REV 模式具有约 20% 更高 Ieff 和约 30% 更低 Cgd。
- 在电路仿真中，VNS FWD 相比 HNS FWD 可获得约 7% 的频率提升。

## 5. 关键结论（Key Findings）

- VFET 的非对称性不是次要细节，而是标准单元设计必须显式利用的约束。
- VNS FWD 是当前最具面积与性能平衡的布局方案，但复杂门仍需要更细的 mixed-mode 设计。
- 若后续工艺能改善上下源漏对称性，VFET 的电路可用性会进一步提升。

## 6. 关键概念（Concepts）

- [[concepts/vertical-field-effect-transistor-vfet|Vertical Field-Effect Transistor (VFET)]]
- [[concepts/complementary-fet-cfet|Complementary FET (CFET)]]
- [[concepts/flip-fet|Flip FET]]

## 7. 相关实体（Entities）

- [[entities/peking-university|北京大学]]

## 8. 关联主题（Topics）

- [[topics/vfet-layout-design|VFET 布局设计]]
- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：把器件方向、寄生和复杂门布局同时放进同一个 DTCO 框架中。
- 局限性：结论主要基于标准单元和 RO 级实验，尚未覆盖更大规模 block。
- 潜在风险：VFET 的源漏非对称性若在工艺上难以压低，会持续拖累 library 质量与变化一致性。

## 10. 参考与来源（References）

- [原始文件](../../../../raw/2026/04_26/Consideration_of_VFET_for_Ultimate_Logic_Scaling_A_Design_Perspective.pdf)
- [[topics/vfet-layout-design|VFET 布局设计]]
