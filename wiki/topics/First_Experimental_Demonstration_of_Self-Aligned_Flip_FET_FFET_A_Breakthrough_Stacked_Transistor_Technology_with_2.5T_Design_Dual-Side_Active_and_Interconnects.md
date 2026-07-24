---
type: page
source: raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - 标准单元
  - SRAM
topics:
  - advanced-3d-integration
  - ffet-sram-design
concepts:
  - flip-fet
  - complementary-fet-cfet
  - drain-merge
  - bipolar-sram
entities:
  - peking-university
---

<!-- markdownlint-disable-next-line MD013 -->
# First Experimental Demonstration of Self-aligned Flip FET (FFET): a Breakthrough Stacked Transistor Technology with 2.5T Design, Dual-side Active and Interconnects

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：First Experimental Demonstration of Self-aligned Flip FET (FFET): a Breakthrough Stacked Transistor Technology with 2.5T Design, Dual-side Active and Interconnects
- 原始文件路径：原始 PDF（仓库中未提供）
- 文件类型：PDF
- 来源：2024 IEEE Symposium on VLSI Technology and Circuits
- 作者 / 机构：Haoran Lu 等，北京大学
- 时间：2024
- DOI：`10.1109/VLSITECHNOLOGYANDCIR46783.2024.10631460`

## 2. 摘要（Summary）

本文报告了 [[topics/flip-fet|FFET]] 的首次实验性演示，重点展示其
self-aligned active、双面有源区和双面互连如何把堆叠晶体管推进到
2.5T 级标准单元设计。作者强调 FFET 在制造友好性上优于
[[topics/complementary-fet-cfet|CFET]]，并用标准单元、反相器、
SRAM 与 Bi-SRAM 结构说明它在密度、布线和寄生优化上的潜力。
论文给出的代表性结果包括：2.5T 标准单元在同设计规则下相较 CFET
可进一步缩小约 12%，相较 FinFET SRAM 可获得约 35.9% 的密度提升；
在 Bi-SRAM 中把 WL / BL 分置到两面后，BL 金属线电阻可下降约 31.5%，
WL 金属线电阻可下降约 55%。文中还指出，
[[topics/drain-merge|Drain Merge]] 与 Gate Merge 等跨面连接结构是
紧凑布局与双面信号组织的关键。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：堆叠晶体管是后 FinFET / nanosheet 时代继续缩放的重要方向。
- 目标问题：如何在避免 CFET 高纵横比工艺负担的同时实现更紧凑的 3D 器件与标准单元。
- 应用场景：先进逻辑标准单元、SRAM、双面互连和后续 FFET DTCO。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 提出 FFET 的 back-to-back stacked transistor 结构。
- 在同一晶圆两侧实现 self-aligned active 与 dual-side interconnect。
- 构建最小 2.5T 标准单元库，并讨论 Bi-SRAM 交叉耦合结构。
- 对比 FFET、CFET 与 FinFET 在标准单元、反相器和 SRAM 上的面积与寄生差异。

### 4.2 核心原理 / 机制

- FFET 把 n/p 器件放在晶圆前后两面，缓解 CFET 的高 AR 垂直集成难题。
- 双面互连让信号和电源能分摊到两侧，提高 pin access 和系统级可布线性。
- 通过 Gate Merge 与 [[topics/drain-merge|Drain Merge]] 连接两侧关键节点，
  使紧凑标准单元和 SRAM 结构成为可能。
- FFET 对每一层晶体管的 N / P 极性没有强约束，因此更容易构造
  Bipolar SRAM 这类双面协同的存储结构。

### 4.3 数据与实验（如适用）

- 2.5T FFET 标准单元相较同规则 CFET 进一步缩小约 12%。
- 相较 FinFET SRAM，FFET 相关 SRAM 结构可获得约 35.9% 的密度提升，
  在相同 push rule 下可实现约 45% 的面积缩减。
- Bi-SRAM 中，双面 WL / BL 布置可使 BL 金属线电阻降低约 31.5%，
  WL 金属线电阻降低约 55%。
- FFET inverter 的源电阻相较 CFET 可降低约 70.5%，输入电容可降低约 34.2%，
  在加入更多 DTCO knobs 后，约可带来 5.0% 的等功耗频率提升。

## 5. 关键结论（Key Findings）

- FFET 不只是另一种堆叠晶体管，而是同时把自对准有源区与双面互连纳入同一平台。
- 双面互连对 SRAM 外围与阵列布线都有直接收益。
- 首次实验演示表明 FFET 具备从器件走向标准单元与 SRAM 的连续扩展性。
- 在当前比较中，FFET 的优势不仅是面积缩小，还包括更低寄生和更灵活的双面路由组织。

## 6. 关键概念（Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/complementary-fet-cfet|Complementary FET (CFET)]]
- [[topics/drain-merge|Drain Merge]]
- [[topics/bipolar-sram|Bipolar SRAM]]

## 7. 相关实体（Entities）

- 北京大学

## 8. 关联主题（Topics）

- [[topics/advanced-3d-integration|先进三维集成]]
- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]

## 9. 评估与思考（Analysis）

- 方法优点：把工艺、单元库和 SRAM 证明链条放在同一篇工作中，完整度较高。
- 局限性：虽然已有实验演示，但大规模设计库、良率与统计波动仍未完全回答。
- 潜在风险：跨面连接结构的寄生与变化一致性，会在大阵列和复杂 block 中进一步放大。
- 补充判断：论文更像“技术可行性与路线证明”，而不是已经完成大规模产品级收敛。

<!-- user-notes:start -->
测试不能删除
<!-- user-notes:end -->

## 10. 参考与来源（References）

- 原始文件（仓库中未提供）
- [[topics/advanced-3d-integration|先进三维集成]]
